# Bibliography and Sources — Curated, with Usage Notes

Two tiers: **foundational** (the canonical books/papers a jury expects to see) and **current** (2020–2026, including the recent search results that show the topic is live). Each entry notes *where in the thesis to use it*. Verify every DOI/URL and final formatting against your school's citation style (IEEE or APA — confirm with your supervisor) before submission. Treat vendor/blog sources as *primary evidence of current industry practice*, and always flag them as such in-text rather than presenting them as peer-reviewed.

---

## Tier 1 — Foundational (canonical)

1. **Linstedt, D., & Olschimke, M. (2015).** *Building a Scalable Data Warehouse with Data Vault 2.0.* Morgan Kaufmann. — Core DV2.0 reference. Use in §2.1, §3.2. The backbone citation of the thesis.
2. **Kimball, R., & Ross, M. (2013).** *The Data Warehouse Toolkit* (3rd ed.). Wiley. — Dimensional modeling. §1.2, comparison in §3.4.
3. **Inmon, W. H. (2005).** *Building the Data Warehouse* (4th ed.). Wiley. — CIF/normalized EDW. §1.2, §3.4.
4. **Kimball, R., et al. (2004).** *The Data Warehouse ETL Toolkit.* Wiley. — ETL fundamentals. §1.2, §2.2.
5. **Golfarelli, M., & Rizzi, S. (2009).** *Data Warehouse Design: Modern Principles and Methodologies.* McGraw-Hill. — DW design theory. §1.2.
6. **Armbrust, M., Ghodsi, A., Xin, R., & Zaharia, M. (2021).** *Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics.* CIDR 2021. — The Lakehouse thesis + first-class ML claim. §1.3, §2.2, §2.3, §3.2.
7. **Delta Lake (2020).** *Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores.* Proc. VLDB Endowment, 13(12). — ACID-on-files foundation. §1.3, §2.3.
8. **Kleppmann, M. (2017).** *Designing Data-Intensive Applications.* O'Reilly. — Systems fundamentals (storage, streams, consistency). §1.3, §2.2.
9. **Davenport, T. H., & Harris, J. G. (2007).** *Competing on Analytics.* Harvard Business Press. — Analytics as competitive capability. Intro, §1.1.
10. **Jordan, M. I., & Mitchell, T. M. (2015).** *Machine Learning: Trends, Perspectives, and Prospects.* Science, 349(6245), 255–260. — ML grounding. §1.4, §2.2.
11. **Chen, H., Chiang, R. H. L., & Storey, V. C. (2012).** *Business Intelligence and Analytics: From Big Data to Big Impact.* MIS Quarterly, 36(4), 1165–1188. — BI&A framing. §1.1.
12. **Vassiliadis, P. (2009).** *A Survey of Extract-Transform-Load Technology.* IJDWM, 5(3), 1–27. — ETL survey. §1.1, §2.2.
13. **Varga, M. (2014).** *Data Vault Standards, Naming Conventions and Modeling Principles.* Data Vault Alliance. — DV2.0 standards/naming. §2.1.
14. **Bifet, A., et al. (2018).** *Machine Learning for Data Streams.* MIT Press. — Streaming/incremental analytics. §2.2.

---

## Tier 2 — Current (2020–2026) — shows the topic is live

15. **Schneider, J., et al. (2024).** *The Lakehouse: State of the Art on Concepts and Technologies.* SN Computer Science, vol. 5. — **Key recent academic anchor** for the Lakehouse survey. Use prominently in §1.3 and §2.2 as your peer-reviewed Lakehouse reference (preferable to citing vendor blogs there).
16. **Data Lakehouse: Next Generation Information System (2024).** *Seminars in Medical Writing and Education,* 3:67. ResearchGate. — Academic treatment of the lakehouse paradigm and its difficulties (governance, architectural challenge). §1.3, §2.3.
17. **Lakehouse-Oriented Big Data Infrastructure for Educational Analytics (2024/2025).** *Int. J. of Information Technology and Computer Science Applications.* — Concrete *lakehouse reference architecture + predictive integration* example (administrative + assessment data, RF/LogReg). Excellent §2.2 / §3 illustration of native analytics on a lakehouse. URL: ejurnal.jejaringppm.org/index.php/jitcsa/article/view/248
18. **AI-Driven Decision Support System review (2025).** *Future Internet,* 17(9):383. DOI:10.3390/fi17090383. — Review of AI-based DSS integrating ML/NLP/DL for predictive analytics; supports the "native analytics in DSS" argument. §1.4, §2.2.
19. **Feedback-Driven Decision Support System (2025).** arXiv:2508.07107. — DSS with incremental retraining + feedback loop (LightGBM, SHAP). Use as a concrete pattern for the *feedback-loop / lifecycle* dimension in §2.2 and future work in conclusion.
20. **Databricks (2022/updated).** *Data Vault Best Practice on the Lakehouse Platform.* Databricks Blog. — **Primary industry evidence** for DV2.0-on-Lakehouse (Raw/Business Vault in Delta, Delta Live Tables). §2.3, §3.2. Flag as industry source.
21. **Moermans, K. (VaultSpeed) & Olschimke, M. (2023).** *Data Vault 2.0 using Databricks Lakehouse Architecture on Azure.* Microsoft Tech Community. — Industry evidence on Delta tables for Raw/Business Vault, bronze landing, partitioning. §2.3.
22. **Scalefree.** *What's New in Data Vault? ("DV2.0.1" enhancements).* — Living-standard updates: virtualized load-end-date, hybrid lake-staging architectures. §2.1 (currency), §2.3.
23. **AnalyticsCreator (2025).** *Data Modeling for Modern DWH: Data Vault 2.0 vs Kimball, Inmon, Anchor & Mixed.* — Reference architectures across DWH/lake/lakehouse/fabric/mesh; **BARC/Eckerson adoption figures** (skills 48%, implementation complexity 35%, query performance 32%, design complexity 29%). Use these figures (cited) in §2.1 drawbacks and §3.4. Flag as industry source.
24. **CelerData (2024).** *Data Vault 2.0: Advantages and Challenges Uncovered.* — Balanced industry view of DV2.0 benefits/challenges. §2.1.
25. **Moronta, S. (2026).** *Data Vault 2.0 in the Lakehouse Era: Advanced Architecture and Patterns.* Towards Data Engineering (Medium). — Recent deep-dive articulating the *structural tension* (streaming/CDC/microservices vs integration & auditability) that motivates §2.3. Flag as industry source.
26. **Matillion (2024).** *A Prescriptive Data Analytics Maturity Model.* — Maturity spectrum + cloud DWH/Lakehouse framing. §1.4.
27. **Comparative study: Dimensional Modeling vs Data Vault 2.0** (Chaturvedi 2025; Helskyaho, Ruotsalainen & Männistö 2024 — as cited in recent ResearchGate comparative work). — Supports the §3.4 comparison axes (scalability, adaptability, lineage, query efficiency). Track down and cite the primary papers directly.

---

## Schema-evolution thread (for the structural-scalability dimension)

28. **A Survey on Data Warehouse Evolution.** — DW-as-DSS-core + schema/data/structure change taxonomy. §1.1, §1.5, §1.6.
29. **Schema Evolution for Data Warehouse: A Survey.** — Structural/conceptual/behavioural levels of schema evolution. Grounds the *schema-evolution* dimension in §1.5 and the §3.4 criterion.

---

## How to use the source tiers (rule for the implementer)
- For **definitional/theoretical claims**, cite Tier 1 + peer-reviewed Tier 2 (15–19, 28–29).
- For **"this is what industry does now"** claims (especially §2.3 composability), cite Tier 2 industry sources (20–25) and **explicitly say in-text** that this reflects current practice/vendor guidance rather than peer-reviewed evaluation. That caveat is itself one of your findings (the academic gap).
- Replace any thin/secondary entry with its primary source where possible before final submission, and confirm citation style with your supervisor.
