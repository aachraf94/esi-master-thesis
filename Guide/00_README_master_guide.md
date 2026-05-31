# Master's Thesis — Implementation Guide (Master Index)

**Thesis Code:** 26/2852M · **Academic Year:** 2025/2026
**Student:** ABDELKEBIR Achraf (21/0298) — ESI, Algiers
**Supervisor:** ABBAS Mohamed Amir

**Title:** _Scalable Architecture for Decision Support Information Systems: Towards Agile Data Modeling and Integrated Predictive Analytics_

---

## Purpose of this guide

This is a **writing guide / implementation spec**, not the thesis itself. Each file below describes one part of the thesis: its role, what it must contain, the argument it must carry, and the references that ground it. Hand any single file to an AI (or use it yourself) to draft that part. The files are ordered to be written sequentially, but each is self-contained.

This is a **theoretical master's thesis** (the practical work lives in the separate engineering thesis). There is **no prototype and no experiment**. The construct is therefore _conceptual_: definitions, a critical analysis, a formal reference framework, and a literature-grounded comparative evaluation. Everything in this guide is engineered to make that conceptual construct defensible before a jury.

## Page budget (hard constraint)

The thesis body must not exceed **50 pages**, plus a **maximum 10-page appendix** (60 pages total). Indicative split for the 50-page body:

| Part                                   | Pages |
| -------------------------------------- | ----- |
| General introduction                   | 3–4   |
| Chapter 1 (state of the art + C1)      | 11–13 |
| Chapter 2 (critical analysis + C2)     | 13–15 |
| Chapter 3 (framework + evaluation, C3) | 15–18 |
| General conclusion                     | 3–4   |

These are guides, not quotas — total stays under 50. Chapter 3 (the construct chapter) gets the most room; the survey chapters must stay disciplined and not sprawl. Push secondary material (extended tables, full criteria rubrics, detailed diagrams, expanded comparison matrices) into the **10-page appendix** to protect the body budget.

## Visuals are always preferable

Wherever a point can be carried by a **graph, chart, table, or diagram**, prefer the visual over prose — it conveys structure faster, reads as more rigorous to a jury, and saves precious page space. Every chapter spec below lists the visual artifacts it should contain; treat those as a minimum. Always number, caption, reference, and briefly interpret each visual. Large or supporting visuals belong in the appendix; the key construct visuals (dual-scalability dimensions table, criteria grid, reference architecture diagram, evaluation matrix) stay in the body.

## The three-construct spine (read this before anything else)

A theoretical thesis fails if it is "a survey with a diagram at the end." This thesis avoids that by carrying **three theoretical constructs**, one per chapter:

1. **C1 — Dual-scalability conceptualization** (Chapter 1): a precise definition and operationalization of _structural scalability_ and _analytical scalability_ in DSIS, with characterizing dimensions for each. This turns the survey into an analytical instrument.
2. **C2 — Composability analysis + criteria instrument** (Chapter 2): a critical examination of whether Data Vault 2.0 (relational-lineage modeling) and the Lakehouse/Delta paradigm (file-based, schema-flexible) actually _compose_, culminating in a criteria grid used for evaluation.
3. **C3 — Reference framework + analytical evaluation** (Chapter 3): a formal, layered reference architecture with a defined _integration contract_ between the agile-modeling layer and the native-analytics layer, plus a systematic criteria-based comparison.

The progression is **conceptualize → analyze → construct & evaluate**. Keep this arc visible in every part.

## The intellectual heart

The single most important question — and the one a sharp jury will probe — is **the DV2.0 ↔ Lakehouse composability tension** (developed in §2.3 and resolved/scoped in §3.2). Data Vault 2.0 is a structured, hash-keyed, lineage-driven relational discipline; the Lakehouse is file-based and schema-on-read. The recent literature (Databricks, Scalefree "DV2.0.1", VaultSpeed, Medium deep-dives) shows the industry _is_ combining them — but unevenly and with real trade-offs. Lean into this; it is what makes the topic a research question rather than a textbook recap.

## File list

| File                                           | Part         | What it covers                                                          |
| ---------------------------------------------- | ------------ | ----------------------------------------------------------------------- |
| `00_README_master_guide.md`                    | —            | This index, spine, conventions                                          |
| `01_general_introduction.md`                   | Front matter | Context, sharpened gap, RQs, constructs, methodology, outline           |
| `02_chapter1_state_of_the_art.md`              | Chapter 1    | Survey + dual-scalability conceptualization (C1)                        |
| `03_chapter2_critical_analysis.md`             | Chapter 2    | DV2.0, analytics integration, composability tension, criteria grid (C2) |
| `04_chapter3_framework_evaluation.md`          | Chapter 3    | Reference framework + integration contract + analytical evaluation (C3) |
| `05_general_conclusion.md`                     | Back matter  | Constructs vs RQs, limitations, future work                             |
| `06_bibliography_and_sources.md`               | References   | Curated, current bibliography with notes on how to use each source      |
| `07_writing_conventions_and_jury_checklist.md` | Meta         | Style rules, anti-patterns, and a pre-defense self-check                |
| `08_visuals_guide.md`                          | -            | Visuals guide                                                           |

## Research questions (used throughout — keep numbering stable)

- **RQ1 (structural):** How can a DSIS architecture absorb new sources, schema changes, and volume growth without disruptive re-engineering?
- **RQ2 (analytical):** How can predictive/prescriptive capability be integrated _natively_ into the decision pipeline rather than bolted on downstream?
- **RQ3 (composability):** Under what conditions can an agile relational-lineage modeling discipline (DV2.0) and a file-based Lakehouse paradigm be composed into a single coherent architecture, and what are the trade-offs?

Every chapter must trace back to one or more of these. The conclusion answers all three explicitly.

## Scope discipline (timeline warning)

The registered timeline is **~3 months** (2 months review + 1 month writing). This structure is more ambitious than a plain survey. Protect scope by treating the formalism in §3.2 as the one place that must be tight and finishable; do not let the survey chapters sprawl. If the framework formalism threatens the deadline, scope it (clearly stated assumptions) rather than abandoning rigor.
