# Assignment 02 build verification

## Exact release

| File | SHA-256 |
| --- | --- |
| [Fashion-Meets-AI-Assignment-02.pdf](Fashion-Meets-AI-Assignment-02.pdf) | `bdaee6edfaf525e84e590b1f2d132aa43c9e3245c937d300a5e48c34fad312c2` |
| Fashion-Meets-AI-Assignment-02-Overleaf.zip | `b618212e8155bd0b15c2beb21cbd0cab2f9ec2b75c63cf2718f1bf12806502c3` |

## Checks performed

- Technical built the working sources and a fresh extraction of the 46-entry Overleaf ZIP with two passes of XeLaTeX (MiKTeX 25.12). The ZIP passed CRC verification and its files matched the archived sources byte for byte. Both second-pass document logs were clear of warnings, overfull or underfull boxes, missing characters, and unresolved references. MiKTeX displayed its separate package-update reminder.
- The archive rebuild produced the same 20 A4 page rasters at 72 dpi, with identical extracted text and link destinations. The cover and PDF metadata name אסתר גדליה and רוני כהן. Folio marks match physical pages, the Hebrew runs use Heebo, and all eight contents links land on their intended pages.
- The coordinator independently built the staged GitHub source in two passes using XeLaTeX’s recorder option. The second-pass document log was clean. The recorder showed no dependencies on other workspace copies. All 20 rebuilt page rasters at 72 dpi, extracted text and link destinations also matched the exact release.
- All 35 distinct bibliography and image-credit URLs in the final PDF match their source targets. A separate direct-link row preserves targets that vanished when the longer mixed-direction bibliography entries wrapped. The bibliography source records report what was checked and where links require access. [Source register](content/V5_SOURCES.md)
- The chart script was run in a clean output directory using the bundled CSV and Matplotlib 3.10.8. Both outputs matched byte for byte. PDF chart SHA-256 `3b970944949815509423e82c170f3b679b94e096b7ec575c7bc696782669cd4d`; PNG chart SHA-256 `5b138d757bf7d1e649d8108da2758dee50b79ecfa8c5b865bbf891289d1ff66c`. The four selected values match Table 2. The independent example computes `(2 + 1) / 2 = 1.5` percentage points. [GeoStyle conference paper](https://openaccess.thecvf.com/content_ICCV_2019/papers/Mall_GeoStyle_Discovering_Fashion_Trends_and_Events_ICCV_2019_paper.pdf)
- The contact sheet and preview images come from the final PDF. The final reference [12] page range reads 257–273 after an RTL correction. [Visual overview](docs/assignment-02/contact-sheet.png) · [Design report](docs/ASSIGNMENT_02_DESIGN_REVIEW.md) · [Independent audit](reviews/ASSIGNMENT_02_REVIEW.md)

## External checks

This revision was compiled locally. A hosted Overleaf build of this release and official course instructions outside the workspace are unverified. The archive can be imported without Python or shell escape. No Git commit, push, or submission was made.
