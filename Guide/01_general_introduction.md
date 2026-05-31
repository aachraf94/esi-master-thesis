# General Introduction — Writing Spec

**Target length:** 3–4 pages. This sets up the entire defense; spend disproportionate care here despite the tight page budget.

## Role
The introduction must convert a broad topic ("scalable DSIS") into a **defensible research problem** with explicit questions and claimed contributions. A jury decides in the first five minutes whether the thesis has a real problem. Do not open with generic "data is growing" platitudes.

## Required sections and what each must do

### 1. Context (≈1 page)
Establish three converging pressures, each backed by a citation:
- **Organizational transformation / agility:** business environments change faster than fixed schemas can follow.
- **Heterogeneous, high-velocity sources:** proliferation of sources, streaming, CDC, semi/unstructured data.
- **Rising analytical maturity:** organizations move along the descriptive → diagnostic → predictive → prescriptive spectrum; most are stuck low (cite the Gartner/McKinsey-type figure: ~90% descriptive, <10% prescriptive at scale).

End the context by naming the object of study precisely: **Decision Support Information Systems (DSIS)** built on data-warehouse architectures.

### 2. Problem statement — the sharpened gap (≈1 page)
**Do NOT write "rigid architectures are an obstacle."** That is a premise, not a problem. Write the gap as a *forced premature commitment*:

> Classical DSIS architectures force organizations to commit *prematurely and rigidly* to two things at once: (a) a fixed schema/structure, and (b) a fixed analytical scope (typically descriptive BI). Both commitments are made before requirements stabilize, and neither can evolve cheaply. Structural change triggers costly re-engineering; analytical advancement (toward predictive/prescriptive) is bolted on downstream rather than designed in.

Then state the gap crisply: the literature treats **structural agility** (Data Vault 2.0, schema evolution) and **analytical integration** (Lakehouse, embedded ML) as *separate* conversations. There is **no consolidated reference framework that treats both dimensions of scalability jointly**, and the **composability** of the leading structural approach (DV2.0) with the leading analytical paradigm (Lakehouse) is asserted in industry blogs but **under-examined conceptually**.

### 3. Research questions
State **RQ1, RQ2, RQ3 verbatim** as in the master README. Keep the numbering stable across the whole thesis.

### 4. Objectives
Map directly to the registered objectives (literature review; limitation analysis; reference framework; comparative study). Phrase each as a verb-led objective and tie it to an RQ.

### 5. Contributions claimed (≈half page) — IMPORTANT
State the three contributions up front (C1 dual-scalability conceptualization; C2 composability analysis + criteria instrument; C3 reference framework + analytical evaluation). Juries reward a thesis that *declares* its contributions early and then delivers exactly those.

### 6. Methodology of the thesis (≈half page)
Name the method explicitly so the work reads as research, not opinion:
- **Narrative + semi-systematic literature review** (state inclusion criteria loosely: foundational texts + peer-reviewed 2020–2026 + authoritative industry/vendor primary sources for current practice).
- **Conceptual design** for the reference framework.
- **Analytical (non-empirical) evaluation** via a criteria-based comparison grounded in the literature.
Acknowledge explicitly that validation is conceptual, not experimental — owning this pre-empts the obvious attack.

### 7. Thesis outline (≈quarter page)
One short paragraph per chapter.

## Anti-patterns to avoid
- No undefined buzzwords ("synergy", "leverage", "holistic").
- Do not promise a prototype or benchmark you will not deliver.
- Do not let the context section exceed the problem section in length — the problem is the star.

## Source anchors for this part
Lakehouse premise (Armbrust/Zaharia et al., CIDR 2021); maturity spectrum figures (Gartner/McKinsey-cited); DV2.0 as scalable-DWH foundation (Linstedt & Olschimke 2015); DSS-as-DW core (Vassiliadis 2009; DW evolution surveys). Full entries in `06_bibliography_and_sources.md`.
