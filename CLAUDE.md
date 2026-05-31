# CLAUDE.md

This file provides guidance to Claude Code when working on this repository.
Read it fully at the start of every session before touching any file.

---

## Thesis identity

| Field | Value |
|---|---|
| Code | 26/2852M |
| Title | Scalable Architecture for Decision Support Information Systems: Towards Agile Data Modeling and Integrated Predictive Analytics |
| Author | ABDELKEBIR Achraf (21/0298) |
| Supervisor | Mr. ABBAS Mohamed Amir (ESI) |
| Institution | ESI — École nationale Supérieure d'Informatique, Algiers |
| Year | 2025/2026 |
| Language | English |
| Type | Theoretical master's thesis — no prototype, no experiment |
| Page budget | **50 pages body max + 10 pages appendix max = 60 total** |

---

## Stable identifiers — never renumber or rename

| Identifier | Location | What it is |
|---|---|---|
| **RQ1** | introduction.tex | Structural scalability question |
| **RQ2** | introduction.tex | Analytical scalability question |
| **RQ3** | introduction.tex | DV2.0 ↔ Lakehouse composability question |
| **C1** | §1.5 | Dual-scalability conceptualization |
| **C2** | §2.4 | Composability analysis + criteria instrument |
| **C3** | §3.2 | Reference framework + integration contract |

RQ1/RQ2/RQ3 are stated verbatim in `introduction.tex` and answered
explicitly in `conclusion.tex` — both files must mirror each other.
C1/C2/C3 labels must appear consistently across all chapters.

---

## Build

**Requires XeLaTeX** — `pdflatex` will not work (`fontspec` + `polyglossia`).

```bash
# Full build (xelatex → biber → xelatex → xelatex)
latexmk main

# Clean all build artefacts
latexmk -C main
```

Output: `out/main.pdf`. Intermediates: `build/`. Never pass `-output-directory` manually — `.latexmkrc` handles it.

**VS Code:** LaTeX Workshop + `Ctrl+Alt+B`. The extension reads `.latexmkrc`.

**Required fonts (Windows):** Times New Roman, Arial, Courier New.

---

## Architecture

Entry point: `main.tex` — wires everything via `\input` / `\include`.

**Configuration layer** (`config/`) — loaded first:
- `packages.tex` — all `\usepackage{}` declarations; bibliography via `biblatex` + `biber` (APA style, sorted name-year-title).
- `settings.tex` — fonts, spacing, colors, `\graphicspath`, PDF metadata, header/footer.
- `commands.tex` — metadata macros (`\thesisTitle`, `\thesisSupervisorA`, etc.) and helpers (`\fig`, `\uchapter`, `\todo`).

**Metadata is centralized in `commands.tex`** — change once, propagates everywhere.

**Chapter structure** — flat under `mainmatter/`:
```
mainmatter/introduction.tex
mainmatter/chapter1/chapter1.tex   ← State of the Art + C1 (11–13 pp)
mainmatter/chapter2/chapter2.tex   ← Critical Analysis + C2 (13–15 pp)
mainmatter/chapter3/chapter3.tex   ← Reference Framework + C3 (15–18 pp)
mainmatter/conclusion.tex
```
Each chapter has a `figures/` sibling. All figure paths registered in `settings.tex` via `\graphicspath`.

**Bibliography** — `references.bib` at root. Two tiers:
- Foundational: `linstedt2015`, `kimball2013`, `inmon2005`, `armbrust2021`, `deltalake2020`, etc.
- Current 2020–2026: `schneider2024`, `bifet2018`, etc.
- Industry/vendor sources flagged: `note = {Industry/vendor source — reflects current practice, not peer-reviewed}`

**`\todo{}`** renders in red — marks sections still needing content.
Run `grep -r "\\todo" mainmatter/` to see all remaining work.

---

## Key LaTeX conventions

- `\uchapter{Title}` — unnumbered chapters that still appear in TOC (introduction, conclusion, abstract, abbreviations).
- Arabic abstract (`abstract_ar.tex`) — wrap in `\begin{Arabic}...\end{Arabic}` with `\phantomsection`.
- Section labels: `sec:ch<N>-<slug>` (e.g. `sec:ch2-tension`).
- Subsection labels: `subsec:ch<N>-<slug>`.
- Keep labels stable — conclusion cross-references them.

---

## Guide files — mandatory reading before drafting

All writing specs live in `Guide/`. Read the relevant file **before** writing or editing any section.

| File | Read before working on |
|---|---|
| `Guide/00_README_master_guide.md` | Anything — read first every session |
| `Guide/01_general_introduction.md` | `introduction.tex` |
| `Guide/02_chapter1_state_of_the_art.md` | `chapter1.tex` |
| `Guide/03_chapter2_critical_analysis.md` | `chapter2.tex` |
| `Guide/04_chapter3_framework_evaluation.md` | `chapter3.tex` |
| `Guide/05_general_conclusion.md` | `conclusion.tex` |
| `Guide/06_bibliography_and_sources.md` | Any citation work |
| `Guide/07_writing_conventions_and_jury_checklist.md` | Before any review |
| `Guide/08_visuals_guide.md` | Before any figure or table |

---

## Visuals — always preferred over prose

A table, diagram, or chart that can replace a paragraph **must** replace it.
Read `Guide/08_visuals_guide.md` before generating any visual.

**Three categories — apply in order:**

**A — Generate directly:**
- Markdown tables → compile to LaTeX `tabular` / `booktabs`
- Mermaid diagrams → render to PDF/PNG, include via `\fig`
- Python matplotlib/seaborn → save PNG to `mainmatter/chapterN/figures/`
- Use consistent style across all chapters (same font, same color palette)

**B — Reuse from literature:**
Insert a LaTeX comment placeholder:
```latex
% VISUAL_REUSE: Figure X — [Title]
% Source: [Author, Year] — [URL]
% Description: [what it shows and why used here]
% Action: locate, verify fair-use, insert via \fig{}
```

**C — Manual design required (draw.io / Excalidraw):**
```latex
% VISUAL_MANUAL: Figure X — [Title]
% Tool: draw.io
% Description: [detailed spec — components, layers, arrows, labels]
% Priority: HIGH / MEDIUM / LOW
```

Every figure: numbered, captioned (`Figure X — Title. Source: .`),
referenced in text, and interpreted in one sentence.
Large/supporting visuals → `appendix.tex`.

---

## Writing style — apply to every sentence drafted

- **Language:** English. Academic register. Formal but not inflated.
- **Structure:** claim first, evidence second. Every paragraph opens with its point.
- **Sentences:** one idea per sentence. Short paragraphs (3–5 sentences).
- **Voice:** active preferred. Passive only when the agent is genuinely unknown.
- **Hedging:** use only when the claim needs it (`suggests`, `indicates`). Never decorative.
- **Forbidden phrases:** "it is worth noting", "it is important to highlight", "in today's rapidly evolving landscape", "leveraging", "robust solution", "holistic approach", "synergy", "this paper aims to".
- **Citations:** every non-obvious claim gets one. Industry/vendor sources flagged explicitly in-text: *"(industry practice; not peer-reviewed)"*.
- **Tone:** precise engineer explaining to a peer — not a consultant writing a report.

---

## Workflow — follow this order for every section

1. Read the relevant `Guide/0N_*.md` spec file.
2. Read `Guide/08_visuals_guide.md`.
3. Draft content — prefer visuals over prose throughout.
4. Check page budget — body target per chapter is in the guide files.
5. Run `/academic review mainmatter/chapterN/chapterN.tex` before finalizing.
6. Verify all citations exist in `references.bib`.
7. Build with `latexmk main` and confirm no errors.

---

## What NOT to do

- Do not use `pdflatex` — XeLaTeX only.
- Do not pass `-output-directory` to latexmk.
- Do not renumber C1/C2/C3 or RQ1/RQ2/RQ3.
- Do not change section label slugs — conclusion references them.
- Do not add prose where a table or diagram would work.
- Do not cite vendor sources as peer-reviewed — flag them.
- Do not let chapter1 or chapter2 exceed their page targets — push to appendix.
- Do not write the conclusion before introduction.tex is finalized (they must mirror).