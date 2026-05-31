# Chapter 1 — State of the Art and Conceptual Foundations — Writing Spec

**Target length:** 11–13 pages. **Carries construct C1.**

## Role

This is the survey chapter, but it must _end as analysis, not encyclopedia_. The trick that makes it a theoretical construct: it closes by defining **dual scalability** (your C1), so the reader leaves Chapter 1 with your conceptual instrument, not just a reading list. Every survey subsection should be written with the eventual dual-scalability framing in mind — i.e., constantly ask "is this about structural evolution or analytical evolution?"

## Section-by-section spec

### 1.1 Decision Support Information Systems: concepts and evolution

Define DSS/DSIS; position the data warehouse as the historical core of the DSIS. Trace the evolution from reporting → OLAP → modern analytical platforms. Establish vocabulary used for the rest of the thesis.
_Anchors:_ DW-as-DSS-core (DW evolution surveys); Davenport & Harris (analytics as competitive capability); Chen, Chiang & Storey (BI&A evolution, MISQ 2012).

### 1.2 Classical data warehouse modeling paradigms

- **Inmon (CIF):** normalized, integrated enterprise DW; top-down.
- **Kimball:** dimensional modeling, star schema, conformed dimensions; bottom-up; SCD types.
- **Comparative reading:** strengths/weaknesses on integration, agility, query simplicity, time-to-value.
  Frame the limitation that motivates the rest: both assume _relatively stable requirements and schema_.
  _Anchors:_ Inmon 2005; Kimball & Ross 2013; Golfarelli & Rizzi 2009; Kimball ETL Toolkit 2004.

### 1.3 Modern decision-making architectures

- **Lambda & Kappa:** batch/speed duality vs stream-first; why they emerged; their operational cost.
- **Data Lake → Lakehouse:** open formats (Parquet), ACID table layers (Delta/Iceberg/Hudi), unified BI + ML on one store.
- **Delta architecture / medallion (Bronze/Silver/Gold):** as the dominant implementation pattern.
  _Anchors:_ Armbrust/Zaharia et al. (Lakehouse, CIDR 2021); Delta Lake paper (VLDB 2020); Schneider et al. "The Lakehouse: State of the Art" (SN Computer Science 2024) — use this as the academic anchor; Kleppmann 2017 for systems fundamentals.

### 1.4 The analytical maturity spectrum

Descriptive → diagnostic → predictive → prescriptive. Tie maturity progression to architectural demands (predictive/prescriptive need feature pipelines, model lifecycle, fresh trusted data). Cite the empirical reality that most organizations stall at descriptive.
_Anchors:_ analytics maturity model literature; prescriptive analytics maturity (Matillion 2024); Gartner/McKinsey-cited distribution figures; Jordan & Mitchell (ML trends, Science 2015) for the ML grounding.

### 1.5 Conceptual framing of scalability in DSIS — **construct C1**

This is the payload of the chapter. Define two orthogonal axes and give each _characterizing dimensions_ so they become assessable (not vague):

- **Structural scalability** — capacity to evolve the data structure and integration footprint without disruptive re-engineering. Proposed dimensions:
  1. _Source integration_ (cost of adding a new heterogeneous source)
  2. _Schema evolution_ (cost/impact of structural change; versioning)
  3. _Volume/throughput growth_ (scaling data and load without redesign)
  4. _Historization & auditability_ (full-history, non-destructive change)
  5. _Loosely-coupled change propagation_ (blast radius of a change)

- **Analytical scalability** — capacity to progress along the maturity spectrum with capability integrated _natively_ in the pipeline. Proposed dimensions:
  1. _Maturity reach_ (descriptive → prescriptive support)
  2. _Native model integration_ (ML/predictive as first-class, not downstream)
  3. _Data readiness for analytics_ (freshness, trust, feature availability)
  4. _Workload plurality_ (BI + DS/ML on the same governed data)
  5. _Lifecycle support_ (retraining, feedback loops, model governance)

State that these axes structure the entire remainder of the thesis (Ch.2 analyzes approaches against them; Ch.3 evaluates against them). Present the dimensions in a clean table.

### 1.6 Synthesis: critical reading and the research gap

Re-read the surveyed approaches _through the dual-scalability lens_: classical modeling = decent structurally on some dimensions but weak on schema-evolution agility and analytically capped at descriptive; Lakehouse = strong on analytical scalability but offers no modeling discipline for structural integration/historization; DV2.0 (previewed) = strong structurally but not analytically native. Conclude with the explicit gap → motivates Chapter 2.

## Anti-patterns

- Don't let 1.2–1.4 become a neutral textbook. Every paragraph should be steering toward 1.5.
- Don't define scalability vaguely; the _dimensions_ are what make C1 defensible.
- Don't introduce DV2.0 in depth here — only preview it; the deep dive is Chapter 2.

## Visual artifacts to include

- A comparison table: Inmon / Kimball on key properties.
- A diagram of the maturity spectrum mapped to architectural requirements.
- The **dual-scalability dimensions table** (the C1 centerpiece).
