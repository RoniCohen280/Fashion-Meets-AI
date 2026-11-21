# AI agent activity

All three custom Codex agents were activated during Version 5 production. The [development log](DEVELOPMENT_LOG.md) records the actual prompts, handoffs, corrections, and results. The definitions below document role configuration, while the linked deliverables record completed work.

| Agent | Work performed | Evidence |
| --- | --- | --- |
| `/root/content` | Researched and wrote the four Hebrew features, verified case studies and quantitative claims, and handed the copy and source register to CODE. | [Definition](.codex/agents/content.toml) · [Manuscript](content/V5_CHAPTERS.md) · [Source register](content/V5_SOURCES.md) |
| `/root/code` | Built the RTL XeLaTeX project, integrated text and assets, verified page count and the archive build, and corrected bibliography links after review. | [Definition](.codex/agents/code.toml) · [Source](latex-v5/main.tex) · [Build and image report](latex-v5/BUILD_REPORT.md) |
| `/root/review` | Independently audited the manuscript, sources, credits and rendered local proof, reproduced the chart, and rechecked the corrected links. | [Definition](.codex/agents/review.toml) · [Independent audit](reviews/REVIEW_V5.md) |

The coordinator used ImageGen for the four illustrations disclosed in the magazine. The prompts and placements are recorded in the development log.
