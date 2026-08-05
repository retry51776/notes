#!/usr/bin/env python3
"""Convert a Claude .skill archive into a Codex skill folder.

Claude `.skill` files are zip archives. Codex skills are ordinary folders with a
top-level `SKILL.md` and optional supporting directories such as `references/`
and `templates/`. This script extracts the archive, removes macOS archive junk,
and copies the skill root into the destination directory.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path


DEFAULT_OUTPUT_DIR = Path(".").expanduser()


class ConversionError(Exception):
    """Raised when a `.skill` archive cannot be converted safely."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a Claude .skill archive into a Codex skill folder."
    )
    parser.add_argument("archive", type=Path, help="Path to the .skill zip archive")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory that will receive the skill folder (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--name",
        help="Override the destination folder name. Defaults to the name in SKILL.md.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing destination folder.",
    )
    parser.add_argument(
        "--install",
        action="store_true",
        help="Install directly into ~/.codex/skills instead of --output-dir.",
    )
    return parser.parse_args()


def is_junk_path(path: Path) -> bool:
    parts = path.parts
    return (
        "__MACOSX" in parts
        or ".DS_Store" in parts
        or any(part.startswith("._") for part in parts)
    )


def safe_extract_zip(archive: Path, target: Path) -> None:
    try:
        with zipfile.ZipFile(archive) as zf:
            for member in zf.infolist():
                member_path = Path(member.filename)
                if member_path.is_absolute() or ".." in member_path.parts:
                    raise ConversionError(f"Unsafe archive member: {member.filename}")
                if is_junk_path(member_path):
                    continue
                zf.extract(member, target)
    except zipfile.BadZipFile as exc:
        raise ConversionError(f"Not a valid zip/.skill archive: {archive}") from exc


def find_skill_root(extracted: Path) -> Path:
    skill_files = sorted(extracted.rglob("SKILL.md"))
    if not skill_files:
        raise ConversionError("Archive does not contain a SKILL.md file")
    if len(skill_files) > 1:
        listed = ", ".join(str(path.relative_to(extracted)) for path in skill_files)
        raise ConversionError(f"Archive contains multiple SKILL.md files: {listed}")
    return skill_files[0].parent


def parse_skill_name(skill_md: Path) -> str | None:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None

    end = text.find("\n---", 3)
    if end == -1:
        return None

    frontmatter = text[3:end]
    for line in frontmatter.splitlines():
        match = re.match(r"^\s*name\s*:\s*(.+?)\s*$", line)
        if match:
            return match.group(1).strip().strip('"').strip("'")
    return None


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-._")
    if not value:
        raise ConversionError("Could not derive a valid skill folder name")
    return value


def copy_skill_tree(source: Path, destination: Path, overwrite: bool) -> None:
    if destination.exists():
        if not overwrite:
            raise ConversionError(
                f"Destination already exists: {destination}. Use --overwrite to replace it."
            )
        shutil.rmtree(destination)

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        source,
        destination,
        ignore=shutil.ignore_patterns("__MACOSX", ".DS_Store", "._*"),
    )


def convert_archive(
    archive: Path,
    output_dir: Path,
    name_override: str | None,
    overwrite: bool,
) -> Path:
    archive = archive.expanduser().resolve()
    if not archive.exists():
        raise ConversionError(f"Archive not found: {archive}")
    if not archive.is_file():
        raise ConversionError(f"Archive is not a file: {archive}")

    with tempfile.TemporaryDirectory(prefix="skill-convert-") as tmp:
        extracted = Path(tmp)
        safe_extract_zip(archive, extracted)
        skill_root = find_skill_root(extracted)

        raw_name = name_override or parse_skill_name(skill_root / "SKILL.md") or skill_root.name
        destination = output_dir.expanduser().resolve() / slugify(raw_name)
        copy_skill_tree(skill_root, destination, overwrite=overwrite)
        return destination


def main() -> int:
    args = parse_args()
    output_dir = Path("~/.codex/skills").expanduser() if args.install else args.output_dir

    try:
        destination = convert_archive(
            archive=args.archive,
            output_dir=output_dir,
            name_override=args.name,
            overwrite=args.overwrite,
        )
    except ConversionError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
