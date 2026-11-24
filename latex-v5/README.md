# Fashion Meets AI · Assignment 02

## Import to Overleaf

1. Select **New Project → Upload Project** and choose **Fashion-Meets-AI-Assignment-02-Overleaf.zip**. Alternatively, upload the contents of this directory to an empty project.
2. Set the compiler to **XeLaTeX** and the main document to **main.tex** at the ZIP root.
3. Compile and check the hosted PDF and full log. Confirm 20 A4 pages, the cover and author metadata (אסתר גדליה ורוני כהן), the eight contents links, and the Hebrew reading order. Record the hosted TeX Live version.

The import ZIP includes the licensed fonts, images, pre-rendered GeoStyle chart, and editable folio sources. Building on Overleaf does not require Python or shell escape.

## Build locally

From this directory run `xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex` twice. The first pass places citation and folio destinations. The second resolves references. The source validates each declared folio number and reports overflow.

To regenerate the GeoStyle chart independently from the CSV, run `python -m pip install -r figures/v4-chart/requirements.txt` and then `python figures/v4-chart/geostyle_mae.py`. The historical chart directory name identifies the same unchanged, reusable data artifact. Folio 10 prints the four published values in Hebrew and distinguishes the illustrative worked MAE example.

## Source map

- `pages/` contains the cover, metadata and 19 numbered folio files.
- `style/` defines Heebo body and headings, Bodoni Moda English display, Hebrew RTL, editorial color and page composition.
- `components/` contains the original vector stages, comparison table and right-to-left feedback diagram.
- `figures/v4-chart/` contains the empirical chart, dataset and regeneration code.
- `assets/` contains the six credited fashion-related images.
- See the [image and build register](BUILD_REPORT.md) for asset permissions and the edition’s verification record.

