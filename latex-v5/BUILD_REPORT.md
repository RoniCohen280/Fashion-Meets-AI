# Fashion Meets AI · Assignment 02 build and image report

## Edition and local checks

- The edition uses a 20-page A4 folio plan. The four stand-alone features are design and development on 5–7, forecasting on 8–10, campaigns on 11–15, and the future of fashion on 16–18.
- The cover and PDF metadata use the same fields in `pages/metadata.tex`. The names were supplied explicitly for this edition.
- The packaged Hebrew fonts are Heebo static faces. English display uses the bundled Bodoni Moda, with TeX Gyre Heros for English running text and Latin Modern Math for notation from the TeX installation.
- The GeoStyle CSV, Python, PDF and PNG are packaged. The chart shows 1.01, 1.45, 0.90 and 0.77 percentage points from GeoStyle Table 2. The separate worked example averages 2 and 1 percentage points to obtain a 1.5-point MAE.
- Folio 17 has a four-column comparison table in Hebrew and an original vector process diagram with a right-to-left flow and return arrow.
- The hosted Overleaf build of this edition requires a separate check. The local XeLaTeX command and requirements are in [README.md](README.md).

## Image and graphic register

| Folio | File | Production and permission | Published treatment |
| --- | --- | --- | --- |
| 1 | `assets/cover.png` | Original OpenAI ImageGen fashion editorial portrait, 1024 × 1536. | Centered crop with adjacent Hebrew AI disclosure. |
| 4 | `assets/discovery.png` | Original OpenAI ImageGen city fashion silhouettes, 1536 × 1024. | Landscape crop with adjacent Hebrew AI disclosure. |
| 5 | `components/design-stages.tex` | Original vector editorial summary. | Three ordered illustrations of work stages, with no garment cutting pattern implied. |
| 10 | `figures/v4-chart/geostyle_mae.pdf` | Original Python visualization of published results by Mall and colleagues. [GeoStyle conference paper](https://openaccess.thecvf.com/content_ICCV_2019/papers/Mall_GeoStyle_Discovering_Fashion_Trends_and_Events_ICCV_2019_paper.pdf) | Vector chart with selectable caption and formula. |
| 11 | `assets/fashion-show-backstage.jpg` | mandiberg, *Fashion Week: Philosophy Show*, 6 February 2008. [Wikimedia Commons, revision 1097167461](https://commons.wikimedia.org/w/index.php?title=File:Fashion_show_backstage.jpg&oldid=1097167461) · [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/) | Crop under the same license; caption identifies the event as a runway show. |
| 12 | `assets/hybrid-editorial.png` | Original OpenAI ImageGen imagined studio and repeated set, 1536 × 1024. | Upper-biased crop to retain the figure’s face; caption identifies a fictional editorial image, separate from the Mango example. |
| 16 | `assets/fitting-room.png` | Original OpenAI ImageGen imagined fitting room, 1536 × 1024. | Upper-biased crop with both faces and adjacent Hebrew AI disclosure. It illustrates the topic without representing Google or Zalando. |
| 17 | `components/workflow.tex` | Original vector editorial diagram. | Hebrew RTL feedback path includes a team decision before manufacturing and distribution. |
| 18 | `assets/hands-at-work.jpg` | Sajid213, *Tailor sewing machine*. [Wikimedia Commons, revision 1186360323](https://commons.wikimedia.org/w/index.php?title=File:Tailor_sewing_machine.jpg&oldid=1186360323) · [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) | Crop under the same license. The photograph illustrates physical garment work. |

Folio 20 lists the four generated illustrations and their generator and the two attributed documentary photographs with their licenses. No imagery from Mango, H&M, Renuar, H&O, Super-Pharm, Genpire, Google or Zalando is reproduced. The campaigns and deployed products link to their public records. The source research found no confirmation of an identifiable Dé Rococo AI campaign and uses H&O’s documented Israeli campaign as the second folio 14 case.

