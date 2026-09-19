#!/usr/bin/env python3
"""Build a week's PDF from its Markdown source using Pandoc and XeLaTeX."""
from pathlib import Path
import argparse
import re
import shutil
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("week", help="Session directory, for example week-01")
    args = parser.parse_args()
    if not re.fullmatch(r"week-\d{2,}", args.week):
        parser.error("Use a session name such as week-01.")
    root = Path(__file__).resolve().parents[1]
    week = root / "weeks" / args.week
    if not (week / "notes.md").is_file():
        parser.error(f"No notes.md in {week}")
    for executable in ("pandoc", "xelatex"):
        if not shutil.which(executable):
            parser.error(f"Install {executable} before building the PDF.")
    subprocess.run([
        "pandoc", "notes.md", "--from=markdown+tex_math_dollars",
        "--standalone", "--pdf-engine=xelatex",
        "--include-in-header", str(root / "scripts" / "pdf-header.tex"),
        "--variable=fontsize:11pt", "--variable=papersize:a4",
        "--variable=geometry:margin=24mm", "--variable=colorlinks:true",
        "--variable=linkcolor:blue", "--variable=urlcolor:blue",
        "--output=notes.pdf",
    ], cwd=week, check=True)
    print(week / "notes.pdf")


if __name__ == "__main__":
    main()
