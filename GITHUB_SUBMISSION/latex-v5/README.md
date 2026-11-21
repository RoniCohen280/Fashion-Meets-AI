# Fashion Meets AI · Version 5

## Import to Overleaf

Upload the contents of this directory to an Overleaf project. Select **XeLaTeX** and set **main.tex** as the main document. The project includes the fonts, images, pre-rendered GeoStyle chart, and editable folio sources. A normal build needs neither Python nor shell escape. See the [submission build verification](../BUILD_VERIFICATION.md).

## Build locally

From this directory run `xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex` twice. The first pass places citation and folio destinations. The second resolves references. The source validates each declared folio number and reports overflow.

To regenerate the GeoStyle chart independently from the CSV, run `python -m pip install -r figures/v4-chart/requirements.txt` and then `python figures/v4-chart/geostyle_mae.py`. The historical chart directory name identifies the same unchanged, reusable data artifact. Folio 10 prints the four published values in Hebrew and distinguishes the illustrative worked MAE example.

## Source map

- `pages/` contains the cover, metadata and 19 numbered folio files.
- `style/` defines Heebo body and headings, Bodoni Moda English display, Hebrew RTL, editorial color and page composition.
- `components/` contains the original vector stages, comparison table and right-to-left feedback diagram.
- `figures/v4-chart/` contains the empirical chart, dataset and regeneration code.
- `assets/` contains the six credited fashion-related images.
- The repository’s `content/V5_CHAPTERS.md`, `content/V5_SOURCES.md` and approved abstract are the editorial source material. See the [V5 build and image report](BUILD_REPORT.md) for the compiled evidence and permissions.

