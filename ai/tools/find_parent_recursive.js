import fs from 'fs';
import glob from 'glob';
import { parse } from '@babel/parser';
import traversePkg from '@babel/traverse';
import generatorPkg from '@babel/generator';
import fetch from 'node-fetch';
import { Command } from 'commander';

const traverse = traversePkg.default;
const generate = generatorPkg.default;

const program = new Command();

// There is 2 types codes: target_definition, invoked_target
// node find_parent_recursive.js claude_coder.js CV6 -d 1
program
  .name('find-calls')
  .description('Search JS files for nested calls and generate a visualization prompt')
  .argument('<pattern>', 'glob pattern for JS files, e.g. "./src/**/*.js"')
  .argument('<method>', 'method name to find')
  .option('-d, --depth <number>', 'ancestor depth', (v) => parseInt(v, 10), 1)
  .option('-k, --api-key <key>', 'OpenAI API key', process.env.OPENAI_API_KEY)
  .option('-m, --model <model>', 'OpenAI model', 'gpt-4o')
  .action(async (pattern, methodName, opts) => {
    const { depth: ancestorDepth, apiKey, model } = opts;
    if (!apiKey) {
      console.error('❌ Please provide an OpenAI API key via --api-key or OPENAI_API_KEY');
      process.exit(1);
    }

    const targets = new Set([methodName]);
    const referencesByLevel = {
      0: [{
        name: methodName,
        level: 0,
        target_name: methodName,
      }]
    };  // { level: [ { code, name, level, traverse } ] }
    let definitionAstNode = null;

    function record(target_name, node, level, traverseType, nameOverride) {
      const name = nameOverride
        ? nameOverride
        : traverseType === 'CallExpression'
        ? node.id?.name
        : traverseType === 'Identifier'
        ? node.name
        : traverseType === 'FunctionDeclaration' || traverseType === 'ClassDeclaration'
        ? node.id?.name
        : traverseType === 'VariableDeclaration'
        ? node.declarations[0].id.name
        : ''
        ?? node.loc?.start.line;

      const recorded = find_level(name);

      if (recorded > 0 || level === null || !name) {
        return
      }
      const code = generate(node).code.trim();
      const entry = { code, name, level, traverse: traverseType, target_name,
        'start': node.loc?.start.line,
        'end': node.loc?.end.line,
      };
      if (!referencesByLevel[level]) referencesByLevel[level] = [];
      // For root, uses update instead .push()
      if (level === 0) {
        if (referencesByLevel[0][0]?.traverse !== 'VariableDeclarator') {
          referencesByLevel[0][0] = Object.assign(referencesByLevel[0][0], entry);
        }
        return
      }
      if (
        !referencesByLevel[level].some(
          (e) => e.code === code && e.name === name && e.traverse === traverseType
        )
      ) {
        referencesByLevel[level].push(entry);
      }
    }

    function find_level(cur_name) {
      const levels = Object.keys(referencesByLevel)
        .map(l => parseInt(l, 10))
        .sort((a, b) => a - b);
      for (const level of levels) {
        if (referencesByLevel[level]?.some(item => item.name === cur_name)) {
          return level;
        }
      }
      return null;
    }

    function getNamedParent(path) {
      let current = path?.parentPath;
      while (current) {
        const id = current?.node?.id;
        if (id && id.name) {
          return current;
        }
        current = current.parentPath;
      }
      return null;
    }

    function findNestedCallsAndVariableSource(filePath) {
      const code = fs.readFileSync(filePath, 'utf8');
      const ast = parse(code, {
        sourceType: 'module',
        plugins: ['jsx', 'typescript', 'classProperties'],
      });

      traverse(ast, {
        CallExpression(path) {
          // Step 1: find nearest name from path(include path itself) 
          const invoked = path.node.callee?.name ? path.node.callee : getNamedParent(path);
          if (invoked && invoked.type === 'Identifier' && targets.has(invoked.name)) {
            const invoked_level = find_level(invoked.name);
            // When referencesByLevel doesn't have invoked.name, this is beyond what we care about
            if (invoked_level === null) {
              return;
            }
            // Step 2: Record path stacktrace
            record(invoked.name, path.node, invoked_level, 'CallExpression');

            // Step 3: Gather parent_path
            const parent_path = getNamedParent(path),
              parent_name = parent_path?.node?.id?.name,
              parent_level = invoked_level + 1;

            // Step 3: If path_parent within ancestorDepth, add targets & record parent_path
            if (parent_name && parent_level <= ancestorDepth) {
              targets.add(parent_name);
              record(invoked.name, parent_path.node, parent_level, 'CallExpression');
            }
          }
        },
        Identifier(path) {
          const def_name = path.node.name;
          if (targets.has(def_name) && path.isReferencedIdentifier()) {
            const level = find_level(def_name);
            record(def_name, path.node, level, 'Identifier');
          }
        },
        FunctionDeclaration(path) {
          const cur_name = path.node.id?.name;
          if (cur_name === methodName) {
            definitionAstNode = path.node;
            record(cur_name, path.node, 0, 'FunctionDeclaration');
          }
        },
        ClassDeclaration(path) {
          const cur_name = path.node.id?.name;
          if (cur_name === methodName) {
            definitionAstNode = path.node;
            record(cur_name, path.node, 0, 'ClassDeclaration');
          }
        },
        VariableDeclarator(path) {
          const cur_name = path.node.id?.name;
          if (cur_name === methodName) {
            definitionAstNode = path.parent;
            record(cur_name, path.parent, 0, 'VariableDeclarator', path.node.id.name);
          }
        },
      });
    }

    console.log(`🔍 Scanning "${pattern}" for method "${methodName}" (depth ${ancestorDepth})`);
    const files = glob.sync(pattern, { ignore: 'node_modules/**' });
    files.forEach(findNestedCallsAndVariableSource);

    //console.log(referencesByLevel);
    let traverse_stack = '';
    for (const l of Object.values(referencesByLevel)) {
      l.map(c => {
        const { code, ...rest } = c;
        console.log(rest);
        traverse_stack += code + '\n\n\n';
      })
    }

    const prompt = `
referenced targets by level & traverse:
${traverse_stack}
----
Explain above code with intuitive variable names, group business logic into steps, and generate a quick visualization.
`;
    console.log(prompt);

    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        model,
        messages: [{ role: 'user', content: prompt }],
        temperature: 0.7,
      }),
    });

    if (!response.ok) {
      console.error(`❌ OpenAI API Error: ${response.status} ${await response.text()}`);
      process.exit(1);
    }

    const data = await response.json();
    console.log('✅ Response:\n', data.choices[0].message.content);
  });

program.parse(process.argv);