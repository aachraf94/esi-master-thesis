# Prompt for Claude Design — MSc Thesis Research Poster

> **Before you paste this into Claude Design — attach ONE local file:**
> `assets/logos/esi_logo.png` (the ESI logo, for the header).
> Every diagram below is described precisely so Claude Design **draws them natively as clean vector graphics** — do **not** attach the thesis figures (their raster styles would clash). Everything the tool needs is in this prompt.

---

## ROLE & TASK

Design a **single-page academic research poster** for a Master's thesis defense at ESI (École nationale Supérieure d'Informatique, Algiers). The poster presents a **theoretical state-of-the-art literature survey** — there is no prototype and no experiment. It surveys and compares decision-support data architectures along two axes of scalability and reports what the literature concludes.

The audience is an academic jury and fellow researchers. The poster must read at three distances: **title from across the room, section headers from a few steps away, detail up close.** Favor **figures, diagrams, and color-coded tables over dense text** — a diagram or table that can replace a paragraph must replace it.

---

## FORMAT & LAYOUT

- **Orientation / size:** Large-format **landscape poster, A0 proportions** (√2 : 1 ratio, e.g. 1684 × 1191 px or larger), print-ready at 300 DPI.
- **Grid:** Full-width header band on top; below it a **4-column grid** with generous gutters; a thin full-width references/footer strip at the bottom.
- **Reading flow:** top-to-bottom within each column, left-to-right across columns. Numbered sections (01–08) guide the eye.
- **Suggested column placement (balance as needed so columns end evenly):**
  - **Column 1:** 01 Context & Problem · 02 Objectives · 03 Methodology
  - **Column 2:** 04 Two Axes of Scalability · 05 Structural Scalability (criteria + Inmon + Kimball)
  - **Column 3:** 05 Structural (Data Vault 2.0 + comparison table + verdict) · 06 Analytical Scalability (maturity spectrum + criteria)
  - **Column 4:** 06 Analytical (Data Lake + Lakehouse/Delta + comparison table + verdict) · 07 Dual Scalability · 08 Conclusion · Key References
- Each numbered section sits in a **card** (white panel, soft rounded corners, subtle shadow) under a **colored section-header bar** showing the number + title.

---

## VISUAL SYSTEM

**Color palette (use consistently):**
- Primary deep indigo `#27348B` — section-header bars, title band, key labels.
- Primary dark `#1A1F5C` — top title bar, footer strip.
- Accent blue `#2E7CD6` — rules, arrows, links, highlights.
- Verdict green `#1F9D57` — "Verdict" callouts and the favourable end of tables.
- Warning amber `#E8A13A` / muted red-gray `#C0556B` — mid/low ends of tables.
- Neutrals — text `#1F2430`, secondary text `#5A6472`, page background `#FFFFFF`, panel tint `#F4F6FB`, alternate table row `#EAEEF7`.

**Semantic diagram colors (keep identical everywhere they appear):**
- Data Vault objects → **Hub** = indigo `#27348B` (white text); **Link** = green `#2E8B57` (white text); **Satellite** = amber outline `#E8A13A` on light fill `#FBE3C0` (dark text).
- Medallion layers → **Bronze** `#CD7F32`, **Silver** `#9AA0AE`, **Gold** `#D4AF37`.
- Analytical maturity → classical levels in gray `#C9CFDA`; advanced levels in a blue ramp `#7FA8E0` → `#27348B`.

**Typography:**
- Headings: a strong geometric sans — **Montserrat** or **Poppins**, Bold.
- Body: a clean humanist sans — **Inter** or **Source Sans 3**, Regular/SemiBold.
- Keep body text short; prefer bullets and labels over sentences.

**Components:** numbered section-header bars, info cards, color-coded comparison tables (header row in indigo, cells tinted by rating), rounded "criterion" chips, flat boxes-and-arrows diagrams, and a green "Verdict" ribbon for sections 05 and 06.

---

## HEADER (full width)

- **Left:** ESI logo (attached file `esi_logo.png`).
- **Center (stacked):**
  - **Title (largest):** Scalable Architecture for Decision Support Information Systems
  - **Subtitle:** Towards Agile Data Modeling and Integrated Predictive Analytics
  - One thin accent rule, then a single line: **Theoretical state of the art — literature survey & comparison**
- **Right:** a small info badge (indigo) reading: **MSc Thesis · Academic year 2025 / 2026**
- **Author / Supervisor row** (below the title, spanning width):
  - **Author:** ABDELKEBIR Achraf
  - **Supervisor:** Mr. ABBAS Mohamed Amir (ESI)
  - **Institution:** ESI — École nationale Supérieure d'Informatique, Algiers
- **Keywords strip** (small, centered, dot-separated chips):
  Data Vault 2.0 · Lakehouse · Decision support system · Structural scalability · Analytical scalability · State of the art

---

## SECTION CONTENT

### 01 — Context & Problem
For three decades the **data warehouse** has been the core of decision support — built for a stable world: fixed relational sources, a schema settled at design time, reporting on the past. **Two shifts broke that assumption:**

- **Data shift** — sources multiplied: transactional systems, streaming feeds, change-data-capture, semi-structured data now arrive together. A fixed schema becomes a liability the moment a source or definition changes.
- **Demand shift** — analytics moved from *"what happened"* toward *"what will happen / what to do."* Most organizations still only describe and explain the past, while demand for prediction grows.

These are **two distinct properties of an architecture, studied separately in the literature:**
- **Structural scalability** — absorb new sources & schema change without re-engineering.
- **Analytical scalability** — support ever more advanced analytics on the same data.

> **The gap:** no single study compares architectures on **both** axes and asks what already exists where they meet.
> *(Render this as a highlighted callout box.)*

### 02 — Objectives
*(Render as three numbered items with icons.)*
1. Survey data-warehouse **modeling approaches**; compare on **structural scalability** → which best absorbs source & schema change.
2. Survey modern **analytical architectures**; compare on **analytical scalability** → which best supports the full analytics spectrum.
3. Review what the literature reports at the **intersection** — architectures that address both at once — and describe where it stands today.

*Small note line:* Every conclusion traces to a cited source; industry/vendor sources are flagged and weighed accordingly. **This thesis surveys and compares — it proposes no new architecture.**

### 03 — Methodology
*(Render as a compact left-to-right flow: three stacked source tiers → a "criteria" gate → "comparison & verdict.")*
- **Type:** theoretical state-of-the-art study — no prototype, no experiment.
- **Method:** narrative, semi-systematic literature review.
- **Three source tiers:**
  - **Foundational** — standard texts (Inmon, Kimball, Linstedt…).
  - **Current** — peer-reviewed 2020–2026 (Lakehouse, streaming, MLOps).
  - **Industry / vendor** — document current practice; **flagged, never treated as peer-reviewed.**
- Comparison runs against **explicit criteria defined per axis** → so conclusions are assessments, not opinions.

### 04 — Two Axes of Scalability
*(Render as a 2×2 positioning map — this is a key figure. See **FIG-AXES** below.)*
- **Structural scalability** — capacity of a warehouse architecture to absorb new data sources, schema changes, and volume growth **without disruptive re-engineering** of existing structures or their consumers.
- **Analytical scalability** — capacity to progress along the maturity spectrum (descriptive → prescriptive) with advanced analytics **built into the pipeline, not added on later.**

The two are independent properties — and the thesis maps the field on both.

### 05 — Structural Scalability
**Guiding question: "Which model best absorbs change?"**

**Five criteria** *(render as labelled chips, each with its one-line meaning):*
- **Source integration** — cost of absorbing a new, heterogeneous source.
- **Schema evolution** — cost of a structural change and how far it spreads; additive vs destructive.
- **Volume / throughput growth** — scale data volume & load without redesigning the model.
- **Historization & auditability** — completeness & non-destructiveness of the historical record.
- **Change-propagation coupling** — how well the systems that use the data are shielded from a change.

**Architectures** *(render each as a small card with a mini-diagram + 1–2 points):*
- **Inmon — Corporate Information Factory.** Top-down: one normalized **3NF** enterprise core feeding dependent marts. *Strength:* integration & enterprise consistency. *Weakness:* a change ripples through the normalized core, so it spreads widely and is slow to deliver value. *(diagram: **FIG-INMON**)*
- **Kimball — Dimensional model.** Bottom-up **star schemas** (fact + conformed dimensions); bus matrix; SCD for history. *Strength:* query simplicity, fast delivery. *Weakness:* shared dimensions are reused everywhere, so changing them ripples across reports; only the history you planned for is kept. *(diagram: **FIG-STAR**)*
- **Data Vault 2.0.** Splits each entity into **Hub** (business key) / **Link** (relationship) / **Satellite** (historized context); **Raw + Business Vault**; insert-only loading, hash keys. Change is **additive, not destructive.** *Strength:* source integration, schema evolution, historization, low coupling. *Cost:* join-heavy queries + implementation complexity — these fall on **query/build effort, not on structure.** *(diagram: **FIG-DV2**)*

*No Anchor modeling: same additive profile as Data Vault 2.0, but heavier — no distinct verdict.*

**Comparison table** — ratings **Strong / Partial / Weak** (color cells: Strong = green, Partial = amber, Weak = red-gray). Legend: *Strong = favourable end of the criterion. Ordinal author assessment grounded in cited sources — not measured.*

| Criterion | Inmon | Kimball | Data Vault 2.0 |
|---|---|---|---|
| Source integration | Partial | Partial | **Strong** |
| Schema evolution | Weak | Weak | **Strong** |
| Volume / throughput | Partial | **Strong** | Partial |
| Historization | Partial | Partial | **Strong** |
| Change-propagation coupling | Weak | Partial | **Strong** |

> **🏆 Verdict — Data Vault 2.0.** The literature's practical reference point for structural scalability: change is additive, history and lineage are governed, and there is a clear path to serve the data.
> *(Render as a green Verdict ribbon.)*

### 06 — Analytical Scalability
**Maturity spectrum** *(render as a rising staircase — see **FIG-MATURITY**):*
**Descriptive → Diagnostic → Predictive → Prescriptive.** Architectural demand rises sharply; **most organizations stall at diagnostic.** The jump to predictive is **not a harder query — it needs a different pipeline shape.**

**Five criteria** *(labelled chips):*
- **Maturity reach** — highest level supported natively.
- **Native model integration** — ML built into the pipeline vs added from outside.
- **Data readiness** — freshness, trust, and feature availability when the data is used.
- **Workload plurality** — serve BI **and** ML from one governed layer without duplication.
- **Lifecycle support** — retraining, feedback loops, model governance inside the pipeline.

**Architectures** *(cards):*
- **Data Lake.** Schema-on-read; raw data in cheap object storage; ML-ready, multi-engine. *Strength:* workload plurality & maturity potential. *Weakness:* no ACID, no schema enforcement, no governance → **"data swamp."** Advanced analytics made **possible but not dependable.**
- **Lakehouse / Delta.** **ACID table semantics + a transaction log** over open columnar files (Parquet/ORC) → **one governed store for BI + ML.** **Open table formats** (Delta / Iceberg / Hudi) add ACID, schema enforcement & evolution, **time travel.** A **native model loop** (feature store → training → serving → monitoring → retrain) reaches predictive & prescriptive. **Delta = the medallion pattern: Bronze → Silver → Gold.** *(diagrams: **FIG-LAKEHOUSE**, **FIG-MEDALLION**)*

*No Lambda / Kappa: streaming designs for data freshness, not analytical maturity.*

**Comparison table** — same Strong/Partial/Weak color coding.

| Criterion | Data Lake | Lakehouse | Delta |
|---|---|---|---|
| Maturity reach | Partial | **Strong** | **Strong** |
| Native model integration | Partial | **Strong** | **Strong** |
| Data readiness | Weak | Partial | **Strong** |
| Workload plurality | **Strong** | **Strong** | **Strong** |
| Lifecycle support | Weak | **Strong** | **Strong** |

> **🏆 Verdict — Lakehouse / Delta.** The only approach Strong across maturity reach, native integration, workload plurality & lifecycle support — the full spectrum on one governed store.
> *(Green Verdict ribbon.)*

### 07 — Dual Scalability *(keep compact)*
**Data Vault 2.0 on the Lakehouse — complementary strengths.**
- Data Vault 2.0 brings the trustworthy history, stable keys, and lineage the Lakehouse lacks; the Lakehouse brings the **open storage and built-in ML loop** Data Vault can't reach.
- The vault lives **inside** the open store, fully governed.
- **Medallion mapping** *(diagram: **FIG-DUAL**):* Staging → **Bronze**; Raw + Business Vault → **Silver**; star-schema marts → **Gold** → **BI + ML**.

> **⚠ The gap:** used and documented in **industry** sources, but barely studied in peer-reviewed research; its trade-offs (join cost, double history, skills needed) are noted but **not measured.**

### 08 — Conclusion *(keep compact)*
*(Render as a clean 3-row summary + one future-work line.)*
- **Structure →** Data Vault 2.0
- **Analytics →** Lakehouse / Delta
- **Combined →** exists in practice (DV2.0 on the Lakehouse), but **used ahead of the research that would prove it.**
- **Future work:** test Data Vault 2.0 on an open table format against both sets of criteria — turning a common practice into a **measured** result.

---

## FIGURE SPECIFICATIONS

Draw all of these natively, flat-design, in the palette above. Each gets a **bold short title** and a **one-line italic takeaway caption**. Keep arrows clean; align everything to a grid.

**FIG-AXES — Two axes positioning map (Section 04, key figure).**
A 2×2 chart. **X-axis →** Analytical scalability (low → high). **Y-axis ↑** Structural scalability (low → high). Plot four labelled markers:
- bottom-left: **Classical DW (Inmon / Kimball)** — low/low.
- top-left: **Data Vault 2.0** — high structural, low analytical.
- bottom-right: **Lakehouse / Delta** — high analytical, low-ish structural.
- top-right (highlighted, dashed "target" glow): **DV2.0 on the Lakehouse** — high/high.
*Caption: "The field answers each axis well; their combination is the open frontier."*

**FIG-INMON — Inmon Corporate Information Factory (Section 05).**
Horizontal layered flow: **Source systems** → **Staging** → **Normalized 3NF enterprise core** (central, emphasized) → **Dependent data marts** → **BI**. Show the core feeding several marts.
*Caption: "One normalized core — consistent, but change ripples outward."*

**FIG-STAR — Kimball star schema (Section 05).**
A central **FACT_SALES** box (indigo) with FK keys + measures, surrounded by four dimension boxes connected by lines: **DIM_DATE, DIM_PRODUCT, DIM_CUSTOMER, DIM_STORE** (light blue).
*Caption: "Query-friendly stars; shared dimensions are hard to change."*

**FIG-DV2 — Data Vault 2.0 topology (Section 05, important).**
Top row: **HUB_CUSTOMER** (indigo) — **LNK_CUSTOMER_ORDER** (green, center) — **HUB_ORDER** (indigo). Below each hub a **Satellite** (amber): **SAT_CUSTOMER** (name, address, phone · *historized*) under the customer hub; **SAT_ORDER** (date, status, amount · *historized*) under the order hub. Arrows hub→link and hub→satellite. Include a small legend: Hub = business key · Link = relationship · Satellite = historized context.
*Caption: "Keys, relationships, and context separated — new data is added, never altered."*

**FIG-MATURITY — Analytical maturity staircase (Section 06, key figure).**
Four rising steps left→right, each taller than the last: **Descriptive** (gray, "what happened?"), **Diagnostic** (gray, "why?"), **Predictive** (blue, "what will happen?"), **Prescriptive** (deep indigo, "what to do?"). Under each step a small requirement tag: DW+OLAP · DW+OLAP · ML platform + feature pipelines · Closed-loop + governance. A vertical dashed line between Diagnostic and Predictive labelled **"architecture must change here"**; a bracket under the first two steps labelled **"where most organizations stall."** Y-axis label: "architectural demand."
*Caption: "The jump to prediction needs a new pipeline shape, not a harder query."*

**FIG-LAKEHOUSE — Lakehouse layered stack (Section 06).**
Stacked horizontal bands, top to bottom: **Unified governance & catalog** (amber band — lineage, access control, schema registry) → a row of three engine boxes (**BI & SQL**, **Data science & ML**, **Streaming**) → **Open table format** (green band — Delta / Iceberg / Hudi: ACID, schema enforcement & evolution, time travel) → **Open file storage** (gray band — Parquet / ORC on low-cost object storage). Arrows from the three engines down into the table-format band.
*Caption: "One governed store serves BI and ML — warehouse reliability on lake storage."*

**FIG-MEDALLION — Delta medallion pipeline (Section 06).**
Left-to-right arrow flow: **Sources** → **Bronze** (raw) → **Silver** (cleansed) → **Gold** (business-ready) → **BI + ML**. Color the three zones Bronze/Silver/Gold.
*Caption: "Data refined step by step through governed layers."*

**FIG-DUAL — Data Vault 2.0 on the medallion (Section 07).**
The same Bronze→Silver→Gold flow as FIG-MEDALLION, but with DV2.0 overlaid: **Staging → Bronze**; **Raw Vault + Business Vault → Silver** (show the vault objects living here); **Star-schema marts → Gold** → **BI + ML**.
*Caption: "Data Vault hosted inside the open store."*

*(Optional, only if space allows — **FIG-MLLOOP**: a closed loop Governed Store → Feature Store → Model Training → Serving → Monitoring, with a dashed "retraining trigger" arrow back to training and "outcomes + feedback" back to the store. Caption: "A built-in model loop enables prescriptive analytics.")*

---

## KEY REFERENCES (footer strip, small two-column text)

- Linstedt, D. & Olschimke, M. (2015). *Building a Scalable Data Warehouse with Data Vault 2.0.* Morgan Kaufmann.
- Inmon, W. H. (2005). *Building the Data Warehouse* (4th ed.). Wiley.
- Kimball, R. & Ross, M. (2013). *The Data Warehouse Toolkit* (3rd ed.). Wiley.
- Armbrust, M. et al. (2021). Lakehouse: A New Generation of Open Platforms… *CIDR 2021.*
- Armbrust, M. et al. (2020). Delta Lake: High-Performance ACID Table Storage… *PVLDB, 13*(12).
- Harby, A. A. & Zulkernine, F. (2024). Data Lakehouse: A Survey and Experimental Study. *Information Systems, 127.*
- Schneider, J. et al. (2024). The Lakehouse: State of the Art on Concepts and Technologies. *SN Computer Science, 5*(5).
- Nambiar, A. & Mundra, D. (2022). An Overview of Data Warehouse and Data Lake… *Big Data and Cognitive Computing, 6*(4).
- Giebler, C. et al. (2019). Modeling Data Lakes with Data Vault. *ER 2019,* LNCS 11788.

*Footer small print:* Databricks (2022) and other vendor reference architectures are used as **industry sources (not peer-reviewed)** and flagged as such.

---

## QUALITY BAR

- Crisp, modern, **academic** — not a marketing flyer. Generous whitespace; strong visual hierarchy; perfect alignment to the grid.
- **Figures and color-coded tables carry the message; text stays terse.**
- Consistent color semantics across every diagram (Hub/Link/Satellite, Bronze/Silver/Gold, maturity ramp).
- The two **Verdict ribbons** (05, 06) and the 2×2 axes map (04) should be the most eye-catching elements after the title.
- All text in **English**, professional register, no filler.
- **If space is tight, protect these first:** the three key figures (FIG-AXES, FIG-MATURITY, FIG-DV2), both comparison tables, and both Verdict ribbons. The architecture mini-diagrams (Inmon, star, Lakehouse stack, medallion) may shrink to small icons, and FIG-MLLOOP may be dropped. Never shrink body text below legibility to force a fit — cut detail instead.
