# Visuals Guide — Instructions for Claude Code

## Core rule

Visuals are always preferred over prose. Every table, diagram, or chart that can replace a paragraph should replace it.

---

## Three categories — apply in order

### Category A — Generate directly

If the visual is a table, a simple diagram, a flowchart, or a data chart: **generate it inline, right now.** Do not use a placeholder.

Tools to use:

- **Markdown tables** — comparison tables, criteria grids, evaluation matrices, dimension tables
- **Mermaid** (fenced ```mermaid blocks) — architecture diagrams, layer diagrams, flowcharts, topology diagrams (DV2.0 Hubs/Links/Satellites, medallion layers, maturity flow)
- **Python matplotlib/seaborn script** — any chart with numbers (adoption stats, maturity distribution, comparison radar). Output a `.png` into `assets/figures/`. Use a consistent style across all charts.

Every generated visual must have: a sequential number, a caption, and one sentence of interpretation in the body text.

---

### Category B — Reuse from papers or web (placeholder)

If a well-known figure from the literature conveys the point better than anything you can generate (e.g., the original Lakehouse architecture figure from Armbrust et al. 2021, the Delta Lake medallion diagram from the Databricks paper, a DV2.0 canonical diagram from Linstedt & Olschimke):

Insert a placeholder in this exact format:

```
<!-- VISUAL_REUSE
Figure X — [Title of the figure]
Source: [Author, Year, Paper/Blog title]
URL: [direct link to the figure or paper]
Description: [What the figure shows and why it is used here — 2–3 sentences]
Action: Locate this figure, verify reuse rights (academic fair use / open access), and insert it here.
-->
```

---

### Category C — Manual design required (placeholder)

If the visual is a key construct figure that needs design quality (the reference architecture centerpiece, a custom conceptual diagram, the dual-scalability axes) and cannot be generated cleanly by code:

Insert a placeholder in this exact format:

```
<!-- VISUAL_MANUAL
Figure X — [Title]
Tool: [draw.io | Excalidraw | Figma]
Description: [Detailed spec of what to draw — components, layers, arrows, labels, color coding. Enough detail that a designer or you-in-two-days can execute it without rereading the chapter.]
Time estimate: [15 min | 30 min | 1 hour]
Priority: [HIGH — jury sees this / MEDIUM / LOW]
-->
```

---

## Appendix rule

If a visual is supporting (full rubric tables, extended comparison matrices, detailed sub-diagrams): generate or place it in `appendix.md` and reference it from the body with `(see Appendix, Figure X)`.

## Style consistency

- All generated charts: same font family, same color palette, same figure numbering sequence across chapters.
- All Mermaid diagrams: use `theme: neutral` or `theme: default` — no dark themes.
- Caption format: **Figure X — Title.** _Source: ... / Author-generated._
