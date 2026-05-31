# Writing Conventions and Jury Self-Check — Meta Guide

## Writing conventions (apply across all parts)
- **Page budget:** body ≤ 50 pages, appendix ≤ 10 pages (≤ 60 total). Keep survey chapters tight; give the contribution chapter the most room; push extended tables/rubrics/diagrams to the appendix.
- **Prefer visuals always:** wherever a point can be made with a graph, chart, table, or diagram, use the visual instead of prose. It is faster to read, reads as more rigorous, and saves pages. Always number, caption, reference in text, and interpret each one.
- **Language:** write the thesis in English.
- **Voice:** formal academic, third person or impersonal. Define every acronym on first use (DSIS, DV2.0, CDC, ELT, SCD, EDW).
- **Citations:** Use APA style for citations.
- **Figures/tables:** every one is numbered, captioned, referenced in text, and *interpreted* in prose (never drop a table without discussing it).
- **Traceability:** keep RQ1/RQ2/RQ3 and C1/C2/C3 labels stable everywhere. Reviewers love being able to follow the thread.
- **Honesty markers:** when a claim rests on industry practice rather than peer-reviewed evidence, say so. This is a strength in a theoretical thesis, not a weakness.

## Anti-patterns that get attacked at defense
1. Survey chapters that never become analytical (Ch.1 must end on C1, not a reading list).
2. "Two stapled topics" in Ch.2 (must converge on the §2.3 tension).
3. A framework that is a block diagram with no component definitions and no integration contract.
4. A comparison table with scores but no stated evaluation method or per-rating justification.
5. The proposed framework winning every criterion (concede the complexity cost).
6. A problem statement that is just a premise ("rigid is bad") instead of a forced-premature-commitment gap.
7. Generic future work ("more research needed") instead of concrete next steps (prototype, OURQUILANE case study, perf benchmark).

## Pre-defense self-check (run before submission)
- [ ] Does the introduction state RQ1–RQ3 and C1–C3 explicitly?
- [ ] Does each chapter visibly deliver its contribution?
- [ ] Is "scalability" *defined and dimensioned* (not asserted) in §1.5?
- [ ] Is the DV2.0↔Lakehouse tension treated critically (alignments AND conflicts) in §2.3?
- [ ] Does §2.4 produce a criteria grid with rubric definitions?
- [ ] Is the framework a formal artifact (named components + integration contract + numbered invariants), not just a diagram?
- [ ] Is the evaluation method stated (§3.3) before the comparison (§3.4)?
- [ ] Are limitations (non-empirical) owned candidly?
- [ ] Does the conclusion answer all three RQs by name?
- [ ] Are vendor/blog sources flagged as industry practice in-text?
- [ ] Is the scope finishable within the ~3-month timeline? (If §3.2 formalism is at risk, scope it with stated assumptions rather than abandoning it.)

## Likely jury questions — prepare answers
- "What is *your* contribution versus a redrawn vendor diagram?" → C1 definitions, C2 composability analysis + criteria instrument, C3 integration contract + invariants.
- "Your comparison — what's the method?" → §3.3 criteria-based conceptual assessment, rubric-defined, evidence per rating.
- "Do DV2.0 and the Lakehouse really compose?" → §2.3: yes in current practice (DV2.0 *on* Delta), with specific conflicts (join cost, schema discipline vs schema-on-read); academically under-evaluated — which is itself a finding.
- "Why no implementation?" → theoretical thesis by design (practical work is the engineering thesis); framework is a reference model; prototype is stated future work.
