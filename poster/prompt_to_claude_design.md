# Prompt — Design my Master's thesis research poster

> Paste everything below the line into Claude (with design/Canva) as a single message.
> Attach the files listed in the "Files to attach" section at the end before sending.

---

## ROLE

You are an academic poster designer. Produce a **single A0 portrait research poster**
(841 × 1189 mm proportions, vertical) for an MSc thesis defense / poster session, **as one
self-contained interactive HTML artifact** (a single `.html` file with inline CSS/JS, no
external dependencies). The audience is a university jury and CS peers. All content must be
**real selectable HTML text and real HTML tables — never a flat raster image with baked-in
text**. It must be legible from ~1.5 m and visually clean. Use only the content I give you
below. **Do not invent facts, numbers, citations, or findings.** If something is missing,
leave a clearly marked placeholder.

## DELIVERABLE

- One self-contained `.html` file: the whole poster lives on a single large canvas (use CSS
  `transform: scale()/translate()` for zoom/pan, not separate slides).
- It must read correctly **both** as a static full-overview poster (one screenshot / print to
  PDF at A0 proportions) **and** as the animated zoom-through below.
- The animation runs live in the browser on load (and replays on click/keypress). No video
  export needed — it can be screen-recorded if a clip is wanted.
- Type scale relative to the full A0 canvas: body ≥ 24 pt equivalent; section headers ≥ 40 pt;
  main title ≥ 90 pt. Provide simple controls: Space / → advances to the next section,
  ← goes back, Esc returns to full overview.

## ANIMATION FLOW (core behavior)

The poster is presented as an animated, single-canvas zoom walkthrough:

- **Start fully zoomed out** — the entire poster fills the screen (overview mode), so the
  viewer first sees the whole layout at once.
- The view then **smoothly zooms in** to the first section, holds long enough to read it,
  then **passes to the next section** (smooth zoom-out/pan/zoom-in transition between sections).
- Move through the sections **in the layout order below** (1 → 11): Header → Context & Problem
  → Definitions → Method → Architecture-evolution timeline → Axis 1 (structural table) → Axis 2
  (maturity staircase + analytical table) → Intersection → Key takeaways → Limitations & future
  work → Footer/references.
- Each transition is **smooth and continuous** (ease-in/ease-out), never a hard cut.
- End by **zooming back out to the full overview** so the poster reads as a complete static
  artifact at rest.
- **Style: clean academic** — calm, slow pacing; no flashy effects, spins, or bounces; the
  motion only guides the eye. The static A0 poster and the animation share one identical canvas.

---

## IDENTITY (header block — reproduce exactly)

- **Title:** Scalable Architecture for Decision Support Information Systems: Towards Agile Data Modeling and Integrated Predictive Analytics
- **Author:** ABDELKEBIR Achraf
- **Supervisor:** Mr. ABBAS Mohamed Amir (ESI)
- **Institution:** ESI — École nationale Supérieure d'Informatique, Algiers
- **Option:** Information Systems and Technologies (SIT)
- **Year:** 2025 / 2026
- **Type:** Theoretical state-of-the-art (literature survey & comparison) — no prototype, no experiment.
- **Keywords:** Data Vault 2.0 · Lakehouse · Decision support system · Structural scalability · Analytical scalability · State of the art.
- Place the **ESI logo** (attached) top-left of the header.

## VISUAL SYSTEM

- Palette (from the thesis — use these exactly):
  - ESI blue `#0054A6` (primary accent, header band, structural axis)
  - Slate charcoal `#2D3E48` (table headers, dark text)
  - Teal `#1A9E78` (analytical axis accent)
  - Light blue `#EBF2FC` (structural section background)
  - Light teal `#EAF9F4` (analytical section background)
  - Near-white `#F4F5F8` (alternating table rows), white page background.
- Fonts: a clean academic sans (e.g. Inter / Source Sans / Lato) for body; the title can be
  a slightly heavier weight of the same family. No more than two type families.
- Score legend (used in both tables): **Strong** = filled green dot/cell,
  **Partial** = amber, **Weak** = red. Show this legend once, near the top of the two tables.

---

## LAYOUT (top → bottom, single column header then two-axis body)

**1. Header band** — logo, title, author, supervisor, institution, year.

**2. Context & Problem** (short, ~4 lines):
> Decision support systems are built on data warehouses. Two pressures now strain them:
> growing **source heterogeneity** (more, more varied, faster-arriving data) and rising
> **analytical ambition** (from reporting toward prediction). The literature studies these
> two concerns separately. This thesis surveys and compares the architectures on **both**
> axes and reports what already exists at their intersection. It proposes no new architecture.

**3. Two definitions box** (two side-by-side tinted cards):
- **Structural scalability** (light-blue card): the capacity to absorb new sources, schema
  change, and volume growth without disruptive re-engineering.
- **Analytical scalability** (light-teal card): the capacity to support the full analytical
  maturity spectrum — descriptive → diagnostic → predictive → prescriptive — natively in the pipeline.

**4. Method strip** (one line, small): Narrative semi-systematic literature review. Three source
tiers — foundational texts, peer-reviewed 2020–2026, and flagged industry/vendor sources.
Comparison against explicit, literature-derived criteria on an ordinal **Strong / Partial / Weak**
scale (not measured benchmarks).

**5. Architecture-evolution timeline** (full-width band). **Build this yourself natively in
HTML/CSS — do not import any image.** Draw four left-to-right cards with a `→` arrow between
each, each card carrying a decade label, a name, and one short note:
> **1990s — Traditional DWH** (grey: Inmon / Kimball; fixed schema; BI & reporting only) →
> **2000s — Data Lake** (blue: open object storage; schema-on-read; ML-ready but ungoverned) →
> **2010s — Lambda / Kappa** (amber: streaming pipelines; fresh data; velocity, not modeling) →
> **2020s — Lakehouse / Delta** (green: open table formats; ACID; unified BI & ML).
Caption: *Each stage relaxes a limit of its predecessor; the medallion pattern is an
implementation discipline within the Lakehouse, not a separate peer architecture. Author-generated.*

**6. AXIS 1 — Structural scalability** (blue-accented column / panel).
Heading: *"Which warehouse model best absorbs change?"*
Render this as a **native table** exactly (color the cells by the legend):

| Criterion | Inmon CIF | Kimball | **Data Vault 2.0** | Anchor |
|---|---|---|---|---|
| Source integration | Partial | Partial | **Strong** | **Strong** |
| Schema evolution | Weak | Weak | **Strong** | **Strong** |
| Volume / throughput | Partial | **Strong** | Partial | Partial |
| Historization | Partial | Partial | **Strong** | **Strong** |
| Change-propagation coupling | Weak | Partial | **Strong** | **Strong** |

Small criteria key beside/under the table (one line each, light grey):
- *Source integration* — cost of absorbing a new heterogeneous source.
- *Schema evolution* — blast radius of structural change; additive vs. destructive.
- *Volume / throughput* — scaling data and load without redesign.
- *Historization* — completeness and non-destructiveness of the historical record.
- *Change-propagation coupling* — how far a change is isolated from downstream consumers.

One-line takeaway under the table:
> Classical models (Inmon, Kimball) are weakest exactly where change is costly — schema
> evolution and change-propagation coupling. The additive family inverts this. **Verdict: Data
> Vault 2.0** is the literature's reference point for structural scalability (cost: query
> complexity, implementation effort).

**7. AXIS 2 — Analytical scalability** (teal-accented column / panel).
Heading: *"Which modern architecture best supports full-spectrum analytics?"*

First, a small **maturity staircase** (four rising steps; first two grey, last two teal):
> **Descriptive** (*what happened?*) → **Diagnostic** (*why?*) ‖ **Predictive** (*what will
> happen?*) → **Prescriptive** (*what to do?*).
> Mark a divider between Diagnostic and Predictive labelled *"architecture must change here"*;
> grey steps = served by the classical warehouse, teal steps = require a different pipeline shape.

Then render this as a **native table** exactly:

| Criterion | Lambda | Kappa | Data Lake | **Lakehouse** | **Delta** |
|---|---|---|---|---|---|
| Maturity reach | Partial | Partial | Partial | **Strong** | **Strong** |
| Native model integration | Partial | Partial | Partial | **Strong** | **Strong** |
| Data readiness | **Strong** | **Strong** | Weak | Partial | **Strong** |
| Workload plurality | Partial | Partial | **Strong** | **Strong** | **Strong** |
| Lifecycle support | Weak | Partial | Weak | **Strong** | **Strong** |

Small criteria key beside/under the table (one line each, light grey):
- *Maturity reach* — highest maturity level supported natively (descriptive → prescriptive).
- *Native model integration* — are ML models first-class in the pipeline, or external appendages?
- *Data readiness* — freshness, trust, and feature availability at consumption.
- *Workload plurality* — serving BI and ML from one governed layer without duplication.
- *Lifecycle support* — in-pipeline retraining, feedback loops, and model governance.

One-line takeaway under the table:
> Streaming designs solve freshness but leave advanced analytics outside the pipeline; the
> data lake opens ML but can't make data dependable. **Verdict: the Lakehouse, implemented
> through the Delta (medallion) architecture**, is the only one Strong across maturity, native
> integration, workload plurality, and lifecycle.

**8. INTERSECTION — Dual scalability** (full-width band spanning both colors).
Heading: *"Do the two best answers combine?"*
> Yes — and it already exists in practice: **Data Vault 2.0 implemented on the Lakehouse**,
> with the vault as a governed tenant of the open store. The strengths are complementary:
> Data Vault supplies the historization, stable business keys, and governed lineage the
> Lakehouse's data-readiness left unfilled; the Lakehouse supplies the open storage, workload
> plurality, and native model loop Data Vault's analytical ceiling left unreachable.
> But the evidence is **uneven**: the combination rests mostly on industry/vendor sources, with
> thin peer-reviewed evaluation and trade-offs acknowledged informally rather than measured.

Add a small mapping strip (the medallion placement): **File stage → Bronze** (landing) ·
**Raw + Business Vault → Silver** · **Star-schema marts / PIT views → Gold** → **BI + ML**.
You may place the attached `dv2-on-lakehouse-databricks.png` here, but **redraw it** to drop the
Databricks branding; if used as-is, caption it *industry/vendor source — not peer-reviewed*.

**9. Key takeaways** (3 bullet callouts, large):
- **Structure →** Data Vault 2.0
- **Analytics →** Lakehouse / Delta
- **Combined →** practised, but not yet evaluated in peer-reviewed work.

**10. Limitations & future directions** (small, two short columns):
- *Limitations:* no measurement (ordinal, not benchmarked); uneven evidence at the
  intersection; survey covers mainstream approaches, not exhaustive.
- *Future work:* empirical benchmark of DV2.0-on-Lakehouse; quantify the join-cost and
  historization-vs-time-travel trade-offs; a validated dual-scalability criteria instrument.

**11. Footer** — key references (small, single line each):
Inmon (2005); Kimball (2013); Linstedt & Olschimke (2015) — Data Vault 2.0;
Armbrust et al. (2021) — Lakehouse; Delta Lake (2020); Databricks (2022, industry).
Add author name, supervisor, ESI, 2025/2026, and the keywords line.

---

## STRICT RULES

- Reproduce the two tables **verbatim** — same criteria, same Strong/Partial/Weak values.
  Bold cells above mark the winning architecture per row; keep them visually emphasized.
- Keep all text crisp and editable. **Do not** render tables or paragraphs as AI images.
- Flag industry/vendor material as such wherever it appears (Databricks, the dv2-on-lakehouse diagram).
- Academic register, no marketing language. Whitespace is welcome — do not overcrowd.
- If you must add a decorative diagram, keep it schematic and unlabeled rather than inventing labels.

## FILES TO ATTACH (send with this prompt)

Embed these into the HTML as base64 data URIs so the `.html` stays self-contained (no external links).

1. `assets/logos/esi_logo.png` — **required**; header logo (top-left).
2. `mainmatter/chapter2/figures/dv2-on-lakehouse-databricks.png` — *optional reference* for
   Section 8. It is a **Databricks vendor diagram** (carries vendor branding): prefer to **redraw**
   it as a clean schematic; if used as-is, caption it *industry/vendor source — not peer-reviewed*.

The **only** image to definitely attach is the ESI logo. Everything else on the poster — the
architecture-evolution timeline (Section 5), both score tables, the maturity staircase, and the
medallion mapping — is described in full above and must be **built as native HTML/CSS**, not
attached as images. (The old `fig_arch_evolution.png` is incomplete/clipped — do not use it.)
