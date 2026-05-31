# Scalable Architecture for Decision Support Information Systems

> Towards Agile Data Modeling and Integrated Predictive Analytics

---

## Identification

| | |
|---|---|
| **Thesis code** | 26/2852M |
| **Specialties** | Intelligent Systems and Data (SID) · Information Systems and Technologies (SIT) |
| **Academic year** | 2025 / 2026 |
| **Institution** | École Nationale Supérieure d'Informatique (ESI), Oued Smar, Alger |
| **Author** | ABDELKEBIR Achraf · Matricule: 21/0298 · la_abdelkebir@esi.dz |
| **Supervisor** | Mr. ABBAS Mohamed Amir (ESI) |

---

## Abstract

Classical Decision Support Information Systems (DSIS) rely on data warehouse architectures designed for stable business environments and fixed analytical needs. Faced with accelerating organizational transformations, the proliferation of heterogeneous data sources, and the growing analytical maturity of organizations, these rigid architectures become an obstacle to the evolution of decision support systems.

This research addresses the problem of scalability in decision-making architectures along two complementary axes: **structural scalability** and **analytical scalability**. It relies on the Data Vault 2.0 methodology as the foundation of the agile modeling layer, and explores patterns for integrating advanced analytical models within modern architectures (Lakehouse, Delta Architecture).

**Keywords:** `Data Vault 2.0` · `Lakehouse` · `Scalable Architecture` · `DSIS` · `Agile Data Warehouse` · `Predictive Analytics` · `Schema Evolution`

---

## Research Questions

- **RQ1 (structural):** How can a DSIS architecture absorb new sources, schema changes, and volume growth without disruptive re-engineering?
- **RQ2 (analytical):** How can predictive/prescriptive capability be integrated *natively* into the decision pipeline rather than bolted on downstream?
- **RQ3 (composability):** Under what conditions can DV2.0 and a file-based Lakehouse paradigm be composed into a single coherent architecture, and what are the trade-offs?

---

## Contributions

| | Chapter | Description |
|---|---|---|
| **C1** | Chapter 1 | Dual-scalability conceptualization — structural & analytical dimensions |
| **C2** | Chapter 2 | Composability analysis of DV2.0 ↔ Lakehouse + six-criteria evaluation grid |
| **C3** | Chapter 3 | Layered reference framework with integration contract + analytical evaluation |

---

## Repository Structure

```
esi-master-thesis/
│
├── main.tex                    # Master file — ties everything together
├── references.bib              # Bibliography (BibTeX / Biber)
├── master.md                   # Thesis registration form
├── README.md                   # This file
│
├── Guide/                      # Writing guide (one file per chapter)
│   ├── 00_README_master_guide.md
│   ├── 01_general_introduction.md
│   ├── 02_chapter1_state_of_the_art.md
│   ├── 03_chapter2_critical_analysis.md
│   ├── 04_chapter3_framework_evaluation.md
│   ├── 05_general_conclusion.md
│   ├── 06_bibliography_and_sources.md
│   ├── 07_writing_conventions_and_jury_checklist.md
│   └── 08_visuals_guide.md
│
├── config/
│   ├── packages.tex            # All \usepackage{} declarations
│   ├── settings.tex            # Fonts, margins, spacing, colors, headers
│   └── commands.tex            # Custom commands & shortcuts (\fig, \todo, …)
│
├── frontmatter/
│   ├── cover.tex               # Title page
│   ├── dedication.tex          # Dedication
│   ├── acknowledgements.tex    # Acknowledgements
│   ├── abstract_en.tex         # Abstract (English)
│   ├── abstract_fr.tex         # Résumé (French)
│   ├── abstract_ar.tex         # ملخص (Arabic)
│   └── abbreviations.tex       # List of Abbreviations
│
├── mainmatter/
│   ├── introduction.tex        # General Introduction
│   ├── chapter1/
│   │   ├── chapter1.tex        # Chapter 1: State of the Art and Conceptual Foundations
│   │   └── figures/
│   ├── chapter2/
│   │   ├── chapter2.tex        # Chapter 2: Critical Analysis of Agile Modeling and Analytical Integration
│   │   └── figures/
│   ├── chapter3/
│   │   ├── chapter3.tex        # Chapter 3: Proposed Reference Framework and Analytical Evaluation
│   │   └── figures/
│   └── conclusion.tex          # General Conclusion
│
├── backmatter/
│   └── annexes/
│       ├── annexe_a.tex
│       └── annexe_b.tex
│
├── assets/
│   ├── logos/                  # ESI logo and other institutional logos
│   └── global-figures/         # Figures shared across chapters
│
├── build/                      # Auto-generated — all compilation artefacts
└── out/                        # Final PDF output (out/main.pdf)
```

---

## Document Order

```
Cover · Dedication · Acknowledgements · Abstract (EN / FR / AR)
Table of Contents · List of Figures · List of Tables · List of Abbreviations
─────────────────────────────────────────────────────────────────
General Introduction
─────────────────────────────────────────────────────────────────
Chapter 1: State of the Art and Conceptual Foundations       [C1]
Chapter 2: Critical Analysis of Agile Modeling               [C2]
Chapter 3: Reference Framework and Analytical Evaluation     [C3]
─────────────────────────────────────────────────────────────────
General Conclusion
Bibliography
─────────────────────────────────────────────────────────────────
Annexes
  Annexe A · Annexe B
```

---

## Prerequisites

- [MiKTeX](https://miktex.org/) with XeLaTeX and `latexmk`
- Windows fonts installed: **Times New Roman**, **Arial**, **Courier New**

> This project requires **XeLaTeX** — standard `pdflatex` will not work due to `fontspec` and `polyglossia` (Arabic support).

## Build

```bash
# Full build (xelatex → biber → xelatex → xelatex), handled automatically
latexmk main
```

Output: `out/main.pdf` · Auxiliary files: `build/`

## Clean build artifacts

```bash
latexmk -C main
```

## VS Code (LaTeX Workshop)

The `.latexmkrc` at the root configures the engine automatically.

1. Install the **LaTeX Workshop** extension
2. Open `main.tex`
3. Use `Ctrl+Alt+B` to build — the extension picks up `.latexmkrc` automatically
