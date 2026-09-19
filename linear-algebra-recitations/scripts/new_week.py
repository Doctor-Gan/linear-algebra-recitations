#!/usr/bin/env python3
"""Create a new session folder and add a draft row to the archive index."""
from pathlib import Path
import argparse
import json
import re


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("number", type=int)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()
    if args.number < 1:
        parser.error("The week number must be positive.")
    if not args.title.strip() or any(c in args.title for c in "\n\r"):
        parser.error("Supply a nonempty, single-line title.")
    root = Path(__file__).resolve().parents[1]
    number = f"{args.number:02d}"
    relative = f"weeks/week-{number}"
    target = root / relative
    if target.exists():
        parser.error(f"{target} already exists. Nothing was changed.")
    index = root / "README.md"
    lines = index.read_text(encoding="utf-8").splitlines()
    rows = [i for i, line in enumerate(lines) if re.match(r"^\| \[\d+\]\(weeks/week-", line)]
    if not rows:
        parser.error("Cannot locate the sessions table in README.md.")
    insert_at = next((i for i in rows if int(re.match(r"^\| \[(\d+)\]", lines[i])[1]) > args.number), rows[-1] + 1)
    title = args.title.strip()
    table_title = title.replace("|", "&#124;")
    row = (f"| [{number}]({relative}/README.md) | {table_title} | "
           f"[Draft]({relative}/notes.md) | Not yet added | "
           f"[Not yet supplied]({relative}/recording.md) |")
    target.mkdir(parents=True)
    for source in sorted((root / "templates" / "week").glob("*.md")):
        text = source.read_text(encoding="utf-8").replace("{{WEEK}}", number)
        if source.name == "notes.md":
            text = text.replace('"{{TITLE}}"', json.dumps(title, ensure_ascii=False))
        text = text.replace("{{TITLE}}", title)
        (target / source.name).write_text(text, encoding="utf-8")
    lines.insert(insert_at, row)
    index.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Created {target} and updated the archive index.")


if __name__ == "__main__":
    main()
