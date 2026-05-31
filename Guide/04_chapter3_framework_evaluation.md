# Chapter 3 — Proposed Reference Framework and Analytical Evaluation — Writing Spec

**Target length:** 15–18 pages. **Carries contribution C3. This is the chapter the jury weighs most.**

## Role
This is the contribution chapter. In a theoretical thesis with no prototype, this chapter must deliver a **formal artifact** (not a block diagram + prose) and a **methodical evaluation** (not an opinion table). The two attack surfaces a jury will target are exactly these — close both here.

## Section-by-section spec

### 3.1 Requirements and design rationale
Derive requirements *directly and traceably* from RQ1–RQ3 and the dual-scalability dimensions (§1.5). Present a requirements table: each requirement → the RQ and dimension it serves. This traceability is what makes the framework look engineered rather than invented.

### 3.2 The reference framework — present as a FORMAL ARTIFACT
Do not stop at a picture. Specify the framework with the following formal elements:

- **Layered reference model** with **named components** and their responsibilities. Suggested layers:
  1. *Ingestion & staging layer* (heterogeneous sources, CDC, lake landing)
  2. *Agile modeling layer* (DV2.0 Raw Vault + Business Vault on open table format)
  3. *Consumption/serving layer* (dimensional marts / serving views for BI)
  4. *Native analytics layer* (feature pipelines, model training/serving, feedback loops) — positioned to read from the modeling layer, not bolted past the marts
  5. *Governance & metadata plane* (cross-cutting: lineage, schema registry, catalog)

- **Component definitions:** for each component state inputs, outputs, responsibility, and which scalability dimension it serves.

- **The integration contract — the centerpiece.** This is where you *resolve or explicitly scope* the §2.3 composability tension. Define the contract between the agile-modeling layer and the native-analytics layer precisely: what the modeling layer guarantees to the analytics layer (e.g., historized, business-keyed, lineage-stamped feature-ready entities), how features are derived from Satellites/Business Vault, how schema evolution is propagated without breaking models, and how the open table format mediates both relational-lineage discipline and ML file access. State assumptions explicitly where you scope rather than fully solve (honesty here is strength).

- **Optional light formalism** to raise rigor: a metamodel (entities: Layer, Component, Contract, DataEntity, with relationships), or a set of numbered *design rules / invariants* (e.g., "R1: every analytical feature must trace to a historized Satellite attribute"). Numbered invariants are cheap to write and read as genuine formalism.

### 3.3 Evaluation methodology — STATE THE METHOD
Before any comparison, define *how* you evaluate. This section is short but mandatory:
- Method type: **conceptual, criteria-based comparative assessment** grounded in literature evidence (explicitly non-empirical).
- The criteria: the six from §2.4, with their rubric definitions restated.
- Scoring scheme: qualitative levels (Low/Medium/High, or a 1–5 scale) with the *meaning of each level defined per criterion*.
- Evidence rule: every rating must be justified by a cited source or a stated argument — no bare scores.
- Threats to validity stated up front (subjectivity, literature gaps, vendor-source bias).

### 3.4 Comparative study
Apply the methodology systematically across **Kimball, Inmon, DV2.0, and the proposed framework** over the six criteria. Present as a matrix, then a paragraph of justification per cell-cluster (not per cell — keep it readable). The proposed framework should not trivially "win everything"; show where it inherits DV2.0's complexity cost. A framework that honestly concedes weaknesses is more credible.

### 3.5 Discussion
- Trade-offs the framework makes and why.
- Conditions of applicability (when this architecture is worth its complexity — e.g., high source heterogeneity + ambition toward predictive maturity; when it is overkill — stable, descriptive-only contexts).
- Threats to validity revisited.
- Limitations (no empirical validation; reliance on industry evidence for composability claims).

## Anti-patterns
- A block diagram with no component definitions and no integration contract = automatic jury attack. The contract and the numbered invariants are non-negotiable.
- A comparison table with scores but no stated method or per-rating justification = "just opinion." Always pair scores with the methodology of §3.3.
- Framework winning every criterion = not credible. Concede the complexity cost.

## Visual artifacts to include
- The layered reference architecture diagram (with the governance plane cross-cutting).
- A requirements → RQ → dimension traceability table.
- The numbered design rules / invariants list.
- The evaluation matrix (approaches × criteria) with rubric legend.

## Source anchors for this part
DV2.0 reference architectures for lakehouse/lake/mesh (Linstedt & Olschimke; AnalyticsCreator; Databricks DV best-practice); Lakehouse first-class ML (Armbrust/Zaharia et al.); criteria/adoption evidence (BARC/Eckerson figures); schema-evolution framing (DW evolution surveys). Full entries in `06_bibliography_and_sources.md`.
