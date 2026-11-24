# Assignment 02 requirements and evidence

This matrix uses the project [PRD](PRD.md), its record of the assignment, and the [approved editorial brief](EDITORIAL_BRIEF_V5.md). The printed page numbers correspond to the physical page positions in the [final PDF](Fashion-Meets-AI-Assignment-02.pdf).

| Requirement | PDF page | Source or evidence |
| --- | --- | --- |
| 20 portrait A4 pages, Hebrew RTL, XeLaTeX | 1–20 | [Document entry point](latex-v5/main.tex), [RTL and font setup](latex-v5/style/magazine.tex), [build verification](BUILD_VERIFICATION.md) |
| Cover, correct author names and issue identity | 1 | [Cover](latex-v5/pages/cover.tex), [author fields](latex-v5/pages/metadata.tex) |
| Accurate, clickable contents and structured abstract | 2–3 | [Contents](latex-v5/pages/folio-02.tex), [abstract](latex-v5/pages/folio-03.tex) |
| Four independent editorial features | 5–18 | [Folio entry list](latex-v5/pages/editorial.tex), [case evidence](content/V5_SOURCES.md) |
| Documented design and forecasting cases | 7, 9 | [Genpire](latex-v5/pages/folio-07.tex), [WGSN and Heuritech](latex-v5/pages/folio-09.tex) |
| Documented campaign and virtual model cases | 12–15 | [Mango](latex-v5/pages/folio-12.tex), [H&M](latex-v5/pages/folio-13.tex), [Renuar and H&O](latex-v5/pages/folio-14.tex), [Maya Lor](latex-v5/pages/folio-15.tex). Dé Rococo’s use of AI was not substantiated. |
| Real numerical data and Python-generated chart | 10 | [Data](latex-v5/figures/v4-chart/geostyle_mae.csv), [Python](latex-v5/figures/v4-chart/geostyle_mae.py), [chart](latex-v5/figures/v4-chart/geostyle_mae.pdf) |
| Mathematical formula with worked example | 10 | [MAE folio](latex-v5/pages/folio-10.tex) |
| Comparative table and block diagram | 17 | [Comparison](latex-v5/components/production-table.tex), [RTL process diagram](latex-v5/components/workflow.tex) |
| Images, rights and AI labels | 1, 4, 11, 12, 16, 18, 20 | [Assets](latex-v5/assets/), [image register](latex-v5/BUILD_REPORT.md) |
| Conclusion, complete bibliography and credits | 19–20 | [Conclusion](latex-v5/pages/folio-19.tex), [bibliography](latex-v5/pages/folio-20.tex), [source register](content/V5_SOURCES.md) |
| Multiple agents actually used, plus prompts and workflow | Repository | [Agent activity](AI_AGENT_EVIDENCE.md), [prompts](prompts/), [development log](DEVELOPMENT_LOG.md) |
| Source, documentation, and PDF generated from submitted source | Repository | [README](README.md), [local verification](BUILD_VERIFICATION.md) |

## Submission items awaiting confirmation

- A build of this revision on the hosted Overleaf service is pending. The [build report](BUILD_VERIFICATION.md) records the local XeLaTeX evidence.
- GitHub publication awaits the project owner’s approval.
- The PRD does not establish a submission deadline, a prescribed format for agent evidence, or a tool list beyond the stated LaTeX and Python requirements. Confirm these details against any official instructions distributed outside this workspace.
