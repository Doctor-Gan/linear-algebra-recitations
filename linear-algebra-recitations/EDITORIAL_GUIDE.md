# Preparing a recitation chapter

Each chapter should explain the lecture's reasoning to a reader who did not attend. Use the handwritten notes as the primary outline and the accompanying preparation discussion to recover explanations and proofs.

1. Read every handwritten page, including annotations and diagrams. Preserve the original PDF unchanged.
2. Identify the question motivating each topic and the transition to the next example. Write connected prose around the mathematics, rather than a list of isolated results.
3. Keep definitions and notation appropriate to the students' current course. Explain new terms, and mark later material as optional.
4. State hypotheses before using them. Distinguish a fixed right-hand side from every right-hand side, and distinguish existence from uniqueness.
5. Complete every proof promised in the outline. For parameter-dependent calculations, list the row operations and account for all values excluded by division.
6. Explain how to read a result geometrically when the outline uses a diagram. Recreate exact mathematical figures with plotting or vector tools, keeping the original drawing in the source PDF.
7. Correct mathematical slips in the English exposition and record material corrections in the week's `editorial-notes.md`. Do not silently guess an illegible formula.
8. Include only substantiated descriptions of research. Do not infer unpublished theorem statements, authorship roles, or publication status.
9. Treat `notes.md` as the source of truth. Regenerate the PDF after editing and inspect its layout, especially equations and page breaks.
10. Add a recording URL only when supplied or verified. Add timestamps only after reviewing the actual recording. Do not invent a lecture date or claim that a prepared outline was delivered verbatim.

Write as readable classroom notes, with direct sentences and a natural speaking voice. Give each section a reason to follow the preceding one. Use the examples to raise the next question, and return to them when a general result explains what happened. Keep the necessary arguments but avoid a formal textbook tone, unnecessary theorem/proof labels, frequent bold emphasis, boxed formulas, and appended template summaries. Use inline equations for short calculations and displays for multi-line calculations or statements that need space. Avoid semicolons and repetitive summaries.

Include a short, accurate AI-writing disclosure when ChatGPT has drafted the English notes, for example: “These notes were drafted with the help of ChatGPT from my handwritten notes and the discussion used to prepare the recitation.” Do not claim that the author has reviewed the text unless that review has actually occurred.

## Standard session files

| File | Purpose |
|:--|:--|
| `README.md` | Overview and material links |
| `handwritten.pdf` | Unmodified source notes |
| `notes.md` | Full English exposition |
| `notes.pdf` | Generated reading copy |
| `recording.md` | Recording URL and verified timestamps |
| `editorial-notes.md` | Source mapping, corrections, and unresolved questions |

After adding a week, update the root session index. Use relative links so that materials remain navigable both on GitHub and in a local checkout.
