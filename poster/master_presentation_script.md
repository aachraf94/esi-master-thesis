# Poster Presentation Script
**Thesis:** Scalable Architecture for Decision Support Information Systems
**Author:** ABDELKEBIR Achraf
**Target time:** 12–14 minutes (range 10–15)
**Speaking pace:** calm, take a short pause between sections

> **How to use this script:**
> - Text in *italics* = an action (point to something on the poster).
> - `[~X min]` = roughly how much time has passed.
> - Do not memorize word for word. Read it a few times, then say it in your own way.
> - The bold sentences are your "anchor lines" — if you forget everything else, say those.

---

## OPENING `[~0:00]`

Good morning / afternoon, everyone.

My name is Achraf ABDELKEBIR. The title of my thesis is **"Scalable Architecture for Decision Support Information Systems."**

Let me start with the one idea behind the whole work.

> Organizations make decisions based on the data their systems can give them. For thirty years, that data has lived in the **data warehouse**. But the warehouse was built for a calm world — a fixed set of sources and simple reports about the past. **That world is gone.** Today data comes from everywhere, and managers no longer want to know only *what happened* — they want to know *what will happen* and *what to do.*

So my thesis asks a simple question: **which architectures can handle this new pressure — and is there one architecture that handles both sides of it at the same time?**

This poster gives the answer.

---

## SECTION 01 — Context & Problem `[~1:00]`

*Point to Section 01, top left.*

Let me explain the problem more precisely.

The classic data warehouse rests on one assumption: that you can decide the structure of your data — the **schema** — once, before the data arrives, and then keep it stable.

Two changes broke that assumption.

**The first change is in the data itself.** Sources have multiplied — transactional systems, streaming feeds, change-data-capture, semi-structured data. They all arrive together now. And the moment a new source appears, **a fixed schema becomes a liability** — you have to rebuild part of your structure just to let the new data in.

**The second change is in what people ask for.** Analytics has moved along a spectrum — from describing the past, toward predicting the future and recommending actions. Most organizations are still stuck near the beginning of that spectrum, but the demand for prediction keeps growing.

*Point to the gap callout box.*

Here is the key point. These are **two different problems**, and the research literature studies them **separately.** One side studies how to model the warehouse so it absorbs change. The other side studies how to push analytics toward prediction. **What is missing is a single study that compares architectures on both problems at once — and asks what already exists where the two meet.** That gap is exactly what my thesis fills.

---

## SECTION 02 & 03 — Objectives & Methodology `[~2:30]`

*Point to Sections 02 and 03.*

From that gap, the thesis has **three objectives.**

1. Survey the main **warehouse modeling approaches** and compare them on **structural scalability** — which one best absorbs new sources and schema change.
2. Survey the main **modern analytical architectures** and compare them on **analytical scalability** — which one best supports the full range of analytics.
3. Review what the literature already reports at the **intersection** — architectures that handle both — and describe where that stands today.

*Point to the methodology flow.*

About the method: this is a **theoretical survey.** No prototype, no experiment. Every conclusion comes from published sources, and I use **three tiers** of source:

- **Foundational** — the standard books: Inmon, Kimball, Linstedt.
- **Current** — peer-reviewed papers from 2020 to 2026 on the Lakehouse, streaming, and machine-learning operations.
- **Industry and vendor** — these show what practitioners do, but I always **flag them as not peer-reviewed**, and I never treat them as proof.

And one important point: the comparison is **not** my personal opinion. For each axis I defined **explicit criteria first**, then rated each architecture against them. So the verdicts are **assessments grounded in cited sources**, not impressions.

---

## SECTION 04 — Two Axes of Scalability `[~4:00]`

*Point to Section 04, the 2×2 map. This is your most important diagram — slow down here.*

This map is the backbone of the whole thesis.

The vertical axis is **structural scalability** — how well an architecture absorbs new sources, schema changes, and growth in volume, **without forcing you to re-engineer what already exists.**

The horizontal axis is **analytical scalability** — how far an architecture can move along the analytics spectrum, from reporting up to prediction, with that power **built into the pipeline, not added on afterwards.**

These are **two independent properties.** And the thesis maps the field on both.

*Trace the four corners with your finger.*

- Bottom-left — the classic warehouses, Inmon and Kimball — weak on both.
- Top-left — **Data Vault 2.0** — strong on structure, but weak on analytics.
- Bottom-right — the **Lakehouse** — strong on analytics, but weak on structural discipline.
- Top-right — **strong on both.** This corner is the open question. I will come back to it at the end.

Now let me take the two axes one at a time.

---

## SECTION 05 — Structural Scalability `[~5:15]`

*Point to Section 05.*

First axis: **structural scalability.** The guiding question is simple — **"which model best absorbs change?"**

I compare three approaches against **five criteria.** Quickly:

- **Source integration** — how hard is it to add a new, different source?
- **Schema evolution** — when a definition changes, how far does that change spread?
- **Volume and throughput** — can it grow without redesigning the model?
- **Historization** — is the full history kept, completely and safely?
- **Change-propagation coupling** — are the systems that use the data protected when something changes upstream?

*Point to the three architecture mini-diagrams as you name them.*

**Inmon** builds one central, fully normalized enterprise core that feeds smaller data marts. It gives excellent consistency — every fact is defined in one place. But that strength is also its weakness: when the core changes, the change travels through the whole model.

**Kimball** builds star schemas — a fact table surrounded by dimensions — which are easy and fast to query. But the dimensions are **shared** across many reports, so changing one dimension affects all of them. And it keeps only the history you planned for in advance.

Notice the pattern. **The very thing that gives these classic models their consistency — a shared core, shared dimensions — is also the surface through which change spreads.** That is the price of the classic design.

**Data Vault 2.0** breaks that pattern. It splits every entity into three parts: a **Hub** for the stable business key, a **Link** for relationships, and a **Satellite** for the descriptive details and their history. It loads data **insert-only** — it only adds rows, never overwrites them — so the full history builds up automatically. And it separates a **Raw Vault**, which keeps the source data exactly as received for auditing, from a **Business Vault**, which holds the calculated logic. The result is that **change is additive, not destructive: you absorb new data by adding objects, never by breaking the ones you already have.**

*Point to the comparison table, then to one cell.*

Let me make this concrete with one example from the thesis. Imagine a new source arrives with a customer attribute you never stored before — say, a loyalty tier.

- In **Inmon**, you alter the central customer entity and push that change out to every dependent mart. **Wide blast radius.**
- In **Kimball**, you change a shared dimension and update every star and report that uses it. **Moderate.**
- In **Data Vault 2.0**, you add **one** new Satellite to the existing customer Hub and load it. Everything else is untouched. **Narrow.**

*Point to the table again.*

In the table, Data Vault is Strong on four of the five criteria. The one Partial is volume and throughput — because rebuilding a full view means many joins, which is a query cost. But notice: **that cost falls on query performance and build effort, not on the structure itself** — and structure is exactly what this axis measures.

*Point to the green Verdict ribbon.*

**Verdict: Data Vault 2.0 is the literature's reference point for structural scalability.** But — and this matters for what comes next — **every model on this axis stops at descriptive analytics.** Modeling governs structure, not analytics. That is the second axis.

---

## SECTION 06 — Analytical Scalability `[~8:15]`

*Point to Section 06, then to the maturity staircase.*

Second axis: **analytical scalability.**

Analytics grows through four levels: **Descriptive** — what happened? **Diagnostic** — why? **Predictive** — what will happen? **Prescriptive** — what should we do?

Look at the staircase. The demand on the architecture rises sharply. And there is one critical jump — between diagnostic and predictive. **That jump is not just a harder query. It needs a different shape of pipeline:** machine-learning models, feature engineering, retraining, and monitoring. The old warehouse simply has no place to put those. That is why **most organizations stall at the diagnostic level.**

The five criteria for this axis are: **maturity reach, native model integration, data readiness, workload plurality, and lifecycle support.** The most important idea behind them is whether machine learning is **a first-class part of the pipeline, or just bolted on from outside.**

*Point to the architecture cards.*

**The Data Lake** stores raw files cheaply, and reads the schema only at query time. That makes it flexible and open to machine learning. But it has no transactions, no schema enforcement, and no governance. So files pile up faster than anyone can document them, and it becomes a **"data swamp."** In one line: the lake makes advanced analytics **possible, but not dependable.**

**The Lakehouse, with Delta,** fixes exactly that. It adds **ACID transactions and a transaction log** on top of the same open files — using open table formats like Delta Lake, Iceberg, or Hudi. These give you schema enforcement, controlled schema evolution, and **time travel** — querying the data as it was at any past version. So you get **one governed store that serves both BI and machine learning.** On top of it runs a **native model loop** — feature store, training, serving, monitoring, and retraining — which is what finally reaches the predictive and prescriptive levels. And the Delta architecture organizes this with the **medallion pattern: Bronze for raw data, Silver for cleaned data, Gold for business-ready data.**

*Point to the comparison table.*

In the table, Delta is Strong on all five criteria — the only approach that covers the full spectrum natively, with proper governance.

*Point to the green Verdict ribbon.*

**Verdict: the Lakehouse, implemented through Delta, best addresses analytical scalability.**

But here is the qualification that sets up my final chapter. The Lakehouse gives you trust at the **file level** — clean transactions, no corruption. What it does **not** give you on its own is trust at the **meaning level** — correct history, stable business keys, governed lineage. **That semantic trust depends on a modeling discipline the Lakehouse does not supply.** And that discipline is exactly what Data Vault 2.0 provides.

---

## SECTION 07 — Dual Scalability `[~10:45]`

*Point to Section 07.*

So now look at what we have. Two verdicts that **fit together like two halves.**

Data Vault 2.0 wins on structure — but stops at descriptive analytics. The Lakehouse wins on analytics — but lacks modeling discipline. **Each one supplies exactly what the other is missing.** That is not a coincidence — it is why the field has been combining them rather than choosing between them.

*Point to the FIG-DUAL diagram.*

And this is what the industry has actually been doing: putting **Data Vault 2.0 inside the Lakehouse.** The vault objects are stored as open table-format files, so the vault becomes a **governed tenant of the open store**, not a competitor to it. The medallion mapping is direct: staging goes to **Bronze**, the Raw and Business Vaults live in **Silver**, and the star-schema marts are served from **Gold** — feeding both BI and machine learning.

*Point to the warning callout.*

But here is the honest caveat, and it is the real finding of Chapter 3. This combination is **widely used and documented in industry** — Databricks and others publish reference architectures for it. **Yet in peer-reviewed research, it is barely studied.** Its trade-offs — the heavy joins on columnar storage, the overlap between the vault's history and the table's time travel, and the extra skills needed — are mentioned, **but never actually measured.** In short: **this is a practice that runs ahead of its evidence.**

---

## SECTION 08 — Conclusion `[~12:30]`

*Point to Section 08.*

Let me close with three clear conclusions.

**First — for structure:** Data Vault 2.0. It absorbs change by adding, not by breaking.

**Second — for analytics:** the Lakehouse, through Delta. It is the only approach that natively supports the full spectrum, from reporting to prediction, on one governed store.

**Third — for both together:** an architecture already exists in practice — **Data Vault 2.0 on the Lakehouse** — but it is **used ahead of the research that would prove it.** The industry is ahead of the science.

*Optional — say if you have time.*

So the literature points to three next steps: **benchmark** this combination against both sets of criteria; **measure** the trade-offs that are currently only assumed; and build a **shared, validated set of criteria** so future studies can compare architectures on the same footing. In one sentence — **turn a common practice into a measured result.**

---

## CLOSING `[~13:30]`

That is the heart of the thesis.

The poster in front of you carries the full detail — the criteria, the comparison tables, and the diagrams — so you can check any of these conclusions yourself.

Thank you. I am happy to take your questions.

---

## TIMING GUIDE

| Section | Content | Approx. time |
|---|---|---|
| Opening | Greeting + the one big idea | 1 min |
| 01 | Context & problem | 1.5 min |
| 02–03 | Objectives & methodology | 1.5 min |
| 04 | Two axes — the key diagram | 1.25 min |
| 05 | Structural scalability + trace example | 3 min |
| 06 | Analytical scalability + the bridge | 2.5 min |
| 07 | Dual scalability | 1.75 min |
| 08 + Closing | Conclusion + thanks | 1.25 min |
| **Total** | | **~13.5 min** |

> **If you are running long:** drop the "loyalty tier" trace example in Section 05 (keep just the table) and the optional future-work paragraph in Section 08. That saves ~1.5 min and lands you near 12 min.

---

## QUICK ANSWERS FOR LIKELY JURY QUESTIONS

**Q: Why did you not build a prototype?**
> This is a theoretical state-of-the-art study. Its value is the comparison framework — the explicit criteria on each axis, and the finding that the combined architecture is used but not yet evaluated. A prototype and benchmark are the natural next step, which I state in the conclusion.

**Q: The ratings Strong / Partial / Weak — aren't they subjective?**
> They are **ordinal assessments, not measurements** — they show relative standing, not numbers. Each rating is grounded in a cited source, and the criteria are defined **before** the comparison, so the reasoning is transparent and repeatable. I am careful never to call them measured results.

**Q: Why is Anchor modeling not on the poster?**
> Anchor modeling belongs to the same additive family as Data Vault 2.0 and shows the same profile, but it is heavier — even more objects and more joins — and gives no different verdict under my criteria. Including it adds complexity without changing the conclusion. It is in the thesis as the limit of that family.

**Q: Why are Lambda and Kappa not on the poster?**
> Lambda and Kappa are **streaming-processing** designs. They solve data **freshness and latency** — not the analytical maturity spectrum. They are strong on readiness but only partial on native model integration and lifecycle. They are covered in the thesis, but they are not the answer to the analytical-scalability question, so I kept the poster focused on Data Lake, Lakehouse, and Delta.

**Q: Is "Data Vault 2.0 on the Lakehouse" your own proposal?**
> No. It already exists in industry practice. My contribution is to **read it through both axes**, show **why** the two are complementary — the vault supplies the semantic trust the Lakehouse lacks, the Lakehouse supplies the analytics the vault cannot reach — and to point out that this common practice still **lacks peer-reviewed evaluation.**

**Q: What is the single most important finding?**
> That the field already has a strong answer on **each** axis — Data Vault 2.0 for structure, the Lakehouse for analytics — and that their combination is **already practised but not yet proven** in research. The gap is not a missing architecture; it is missing evidence.

**Q: Why these five criteria and not others?**
> Each criterion is a **recurring concern in the surveyed literature**, and each isolates one distinct way structure or analytics can be forced to change. I keep them separate so the comparison shows **where** an approach is strong, not just **that** it is. I also note in the limitations that these instruments are drawn from the literature but not yet standardized — building a validated, shared instrument is one of my future directions.
