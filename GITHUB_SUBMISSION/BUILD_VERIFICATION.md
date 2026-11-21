# Submission build verification

- The approved PDF is the unchanged Overleaf download `Fashion_Meets_AI_V5_Overleaf.pdf`. SHA-256 `3238412fb46e6d88bcc511ebca08f1fc1f63c5e33ae85b0dbf8e528016cd4ebd`.
- A clean build from the submitted LaTeX directory completed two passes with XeLaTeX (MiKTeX 25.12). Both the rebuilt and approved PDFs have 20 A4 pages.
- All 20 pages matched pixel for pixel at 72 dpi using PyMuPDF. Extracted page text and outbound link destinations also matched on every page.
- The second-pass document log had no warnings, missing characters, or overfull or underfull boxes. The MiKTeX wrapper issued its package-update reminder.
- The existing independent audit concerns the historical local proof. The downloaded Overleaf PDF was inspected for this submission. No new hosted compile was run during packaging.
- The approved download still displays the existing author placeholder. It was preserved in the PDF and source.
