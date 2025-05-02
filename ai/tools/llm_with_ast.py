import sys
import glob
import typer
import requests
from tree_sitter import Language, Parser

app = typer.Typer()

# Load or build the Tree-sitter JavaScript grammar
LIB_PATH = 'build/my-languages.so'
JS_REPO = 'vendor/tree-sitter-javascript'
try:
    JS_LANGUAGE = Language(LIB_PATH, 'javascript')
except:
    Language.build_library(
        LIB_PATH,
        [JS_REPO]
    )
    JS_LANGUAGE = Language(LIB_PATH, 'javascript')

parser = Parser()
parser.set_language(JS_LANGUAGE)


def get_node_text(node, source_bytes):
    return source_bytes[node.start_byte:node.end_byte].decode('utf-8')


def get_node_name(node, source_bytes):
    # Extract name for various node types
    if node.type == 'function_declaration' or node.type == 'class_declaration':
        id_node = node.child_by_field_name('name')
        return get_node_text(id_node, source_bytes) if id_node else None
    if node.type == 'variable_declarator':
        id_node = node.child_by_field_name('name')
        return get_node_text(id_node, source_bytes) if id_node else None
    if node.type == 'method_definition':
        prop = node.child_by_field_name('property')
        return get_node_text(prop, source_bytes) if prop else None
    return None


def get_named_parent(node, source_bytes):
    current = node.parent
    while current:
        name = get_node_name(current, source_bytes)
        if name:
            return current
        current = current.parent
    return None


@app.command()
def find_calls(
    pattern: str = typer.Argument(..., help='glob pattern for JS files, e.g. "./src/**/*.js"'),
    method: str = typer.Argument(..., help='method name to find'),
    depth: int = typer.Option(1, '-d', '--depth', help='ancestor depth'),
    api_key: str = typer.Option(None, '-k', '--api-key', envvar='OPENAI_API_KEY'),
    model: str = typer.Option('gpt-4o', '-m', '--model', help='OpenAI model')
):
    if not api_key:
        typer.echo('❌ Please provide an OpenAI API key via --api-key or OPENAI_API_KEY')
        raise typer.Exit(1)

    targets = {method}
    references_by_level = {0: [{'name': method, 'level': 0, 'target_name': method}]}
    definition_node = None

    def find_level(name):
        for lvl in sorted(references_by_level.keys()):
            if any(item['name'] == name for item in references_by_level[lvl]):
                return lvl
        return None

    def record(target_name, node, level, traverse_type, name_override=None):
        name = name_override or get_node_name(node, source_bytes) or ''
        if not name:
            return
        lvl = find_level(name)
        if lvl is not None and level != 0:
            return
        code = get_node_text(node, source_bytes).strip()
        entry = {
            'code': code,
            'name': name,
            'level': level,
            'traverse': traverse_type,
            'target_name': target_name,
            'start': node.start_point,
            'end': node.end_point,
        }
        references_by_level.setdefault(level, [])
        if not any(e['code'] == code and e['name'] == name and e['traverse'] == traverse_type
                   for e in references_by_level[level]):
            references_by_level[level].append(entry)

    def process_file(path):
        nonlocal definition_node, source_bytes
        source_code = open(path, 'rb').read()
        source_bytes = source_code
        tree = parser.parse(source_bytes)
        root = tree.root_node

        def traverse_node(node):
            # Function & Class definitions
            if node.type in ('function_declaration', 'class_declaration'):
                name = get_node_name(node, source_bytes)
                if name == method:
                    definition_node = node
                    record(name, node, 0, node.type)

            # Variable declarations
            if node.type == 'variable_declarator':
                name = get_node_name(node, source_bytes)
                if name == method:
                    definition_node = node
                    record(name, node, 0, 'variable_declarator')

            # Call expressions
            if node.type == 'call_expression':
                callee = node.child_by_field_name('function')
                invoked = None
                if callee and callee.type == 'identifier' and get_node_text(callee, source_bytes) in targets:
                    invoked = callee
                else:
                    parent_named = get_named_parent(node, source_bytes)
                    if parent_named:
                        pname = get_node_name(parent_named, source_bytes)
                        if pname in targets:
                            invoked = parent_named.child_by_field_name('name') or callee
                if invoked and invoked.type == 'identifier':
                    invoked_name = get_node_text(invoked, source_bytes)
                    lvl = find_level(invoked_name)
                    if lvl is not None:
                        record(invoked_name, node, lvl, 'CallExpression')
                        parent_named = get_named_parent(node, source_bytes)
                        parent_name = get_node_name(parent_named, source_bytes) if parent_named else None
                        if parent_name and lvl + 1 <= depth:
                            targets.add(parent_name)
                            record(invoked_name, parent_named, lvl + 1, 'CallExpression')

            # Identifiers
            if node.type == 'identifier':
                name = get_node_text(node, source_bytes)
                lvl = find_level(name)
                if name in targets and lvl is not None and node.parent.type not in (
                        'variable_declarator', 'function_declaration', 'class_declaration'):
                    record(name, node, lvl, 'Identifier')

            for child in node.children:
                traverse_node(child)

        traverse_node(root)

    typer.echo(f'🔍 Scanning "{pattern}" for method "{method}" (depth {depth})')
    files = glob.glob(pattern, recursive=True)
    for f in files:
        if 'node_modules' in f:
            continue
        process_file(f)

    traverse_stack = ''
    for lvl in sorted(references_by_level.keys()):
        for entry in references_by_level[lvl]:
            traverse_stack += entry['code'] + '\n\n'

    prompt = f"""
referenced targets by level & traverse:
{traverse_stack}----
Explain above code with intuitive variable names, group business logic into steps, and generate a quick visualization.
"""

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}',
        }, json={
            'model': model,
            'messages': [{'role': 'user', 'content': prompt}],
            'temperature': 0.7,
        }
    )

    if not response.ok:
        typer.echo(f"❌ OpenAI API Error: {response.status_code} {response.text}")
        raise typer.Exit(1)

    data = response.json()
    typer.echo('✅ Response:')
    typer.echo(data['choices'][0]['message']['content'])


if __name__ == '__main__':
    app()
