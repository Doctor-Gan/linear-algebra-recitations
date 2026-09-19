# Linear Algebra I — Recitation Archive

**Bowen Gan · Fall 2026**

This repository collects the handwritten notes, English expositions, and recording links for my Linear Algebra I recitations. The written notes develop the reasoning behind the examples and include the proofs needed to read each session on its own.

## Sessions

| Week | Topic | English notes | Handwritten notes | Recording |
|:--|:--|:--|:--|:--|
| [01](weeks/week-01/README.md) | Linear systems: solutions, freedom, and geometry | [Read](weeks/week-01/notes.md) · [PDF](weeks/week-01/notes.pdf) | [Original PDF](weeks/week-01/handwritten.pdf) | [Not yet supplied](weeks/week-01/recording.md) |

## What each session contains

- `README.md`: the session overview and links to its materials.
- `handwritten.pdf`: the original handwritten notes, preserved as supplied.
- `notes.md`: the editable English exposition, with mathematics rendered by GitHub.
- `notes.pdf`: a typeset reading copy generated from the Markdown source.
- `recording.md`: the video link and, when available, a timestamped topic index.
- `editorial-notes.md`: a brief record of clarifications made while preparing the written exposition.

The exposition follows the teaching sequence and completes abbreviated arguments. It is not presented as a verbatim transcript. Recording links and timestamps are added only after the corresponding material is available.

## Add another week

Run, for example:

```bash
python3 scripts/new_week.py 2 --title "Your next topic"
```

This creates `weeks/week-02/` from the files in `templates/week/` and adds the session to the table above. Add the handwritten PDF, develop `notes.md`, and enter the recording link in `recording.md`. Update the row's availability labels when the materials are ready.

Full-length recordings can remain on the chosen video platform or university storage, with their links collected here. Raw video formats are excluded from Git by default so that the repository remains easy to clone.

## Build a reading copy

Install Pandoc and a TeX distribution providing XeLaTeX and the Bitstream Charter fonts (included in TeX Live's recommended fonts), then run:

```bash
python3 scripts/build_notes.py week-01
```

The script writes `weeks/week-01/notes.pdf`. All prose, equations, and figure references are maintained in `notes.md`; the PDF does not require a second independently edited text. The PDF header is in `scripts/pdf-header.tex`.

## Preparing future English notes

The [editorial guide](EDITORIAL_GUIDE.md) records how to turn a handwritten outline and its preparation discussion into readable classroom notes. Connect the examples and questions in the order of the lesson, explain the reasoning, and keep the voice informal. Use simple formatting without boxed formulas, and include a brief disclosure of any AI drafting assistance. Record unclear handwriting and missing recording details in the editorial record rather than guessing.

For the first session, the source is a seven-page handwritten PDF, whose final page is blank. It is retained in full. The optional circle discussion and the closing square-matrix theorem are included in the English exposition.

## References

Exercises discussed in Week 1 are from Nanhua Xi, *Basic Algebra*, Volume I (Chinese edition), Science Press, 2016. The repository contains the recitation materials, not a copy of the textbook or the instructor's slide deck.
