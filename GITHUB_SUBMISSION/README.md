# Fashion Meets AI

Version 5 is a 20-page Hebrew fashion magazine about AI in design and product development, trend forecasting, campaigns and virtual models, and the future of the industry.

- [Approved Overleaf PDF](Fashion_Meets_AI_V5_Overleaf.pdf)
- [20-page visual overview](docs/v5-contact-sheet.png)
- [Assignment PRD](PRD.md) and [Version 5 editorial brief](EDITORIAL_BRIEF_V5.md)
- [Development log and significant production prompts](DEVELOPMENT_LOG.md)
- [Three-agent activity record](AI_AGENT_EVIDENCE.md) and [build verification](BUILD_VERIFICATION.md)

## Build with XeLaTeX

Use a full TeX Live or MiKTeX installation. From the repository root, run:

```sh
cd latex-v5
xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

For Overleaf, upload the contents of `latex-v5/` as a project, select **XeLaTeX**, and use `main.tex` as the main document. The project bundles its image files, Heebo and Bodoni Moda fonts and licenses, and a ready-to-use chart. A normal build needs neither Python nor shell escape. The chart’s CSV, Python script and pinned requirements are in `latex-v5/figures/v4-chart/`.

## Project files

- [LaTeX project](latex-v5/README.md), including the 20 folios and reusable graphics
- [Hebrew manuscript](content/V5_CHAPTERS.md) and [sources](content/V5_SOURCES.md)
- [Independent review](reviews/REVIEW_V5.md) and [image credits and licenses](latex-v5/BUILD_REPORT.md)

The review and development log include historical checks of the local proof. The approved PDF for submission is the Overleaf download linked above.
