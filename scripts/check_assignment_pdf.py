"""Check PDF geometry, text and destinations, and optionally render QA images."""

import argparse
import hashlib
from pathlib import Path
import re
import unicodedata

import fitz


def logical_text(text):
    return re.sub(r"\s+", " ", "".join(
        character for character in text if unicodedata.category(character) != "Cf"
    )).strip()


def check(document):
    assert len(document) == 20, f"Expected 20 pages, found {len(document)}"
    author = logical_text(document.metadata.get("author") or "")
    for expected in ("אסתר גדליה", "רוני כהן"):
        assert expected in author, f"Author absent from metadata: {expected}"
    cover = logical_text(document[0].get_text())
    for expected in ("אסתר גדליה", "רוני כהן"):
        assert expected in cover or expected[::-1] in cover, f"Author absent from cover: {expected}"
    for page in document:
        assert abs(page.rect.width - 595.28) < 0.02 and abs(page.rect.height - 841.89) < 0.02
        extracted = page.get_text()
        if page.number:
            assert extracted.splitlines()[0].strip() == f"{page.number + 1:02d}", page.number + 1
        text = logical_text(extracted)
        assert text and not re.search(
            r"VERSION\s+5|TODO|PLACEHOLDER|לאימות מול השער|\[\s*שמות המחברות\s*\]",
            text,
            re.I,
        )
        for block in page.get_text("dict", flags=fitz.TEXTFLAGS_TEXT)["blocks"]:
            for line in block["lines"]:
                for span in line["spans"]:
                    if re.search("[א-ת]", span["text"]):
                        assert "Heebo" in span["font"], (page.number + 1, span["font"])
    contents = document[1].get_links()
    targets = sorted(link["page"] + 1 for link in contents if "page" in link)
    assert targets == [3, 4, 5, 8, 11, 16, 19, 20], targets
    bibliography = [record["uri"] for record in document[19].get_links() if "uri" in record]
    assert bibliography and all(target.startswith(("https://", "http://")) for target in bibliography)
    for folio in (1, 4, 11, 12, 16, 18):
        assert document[folio - 1].get_image_info(), f"Editorial image absent from page {folio}"
    return len(set(bibliography))


def compare(document, other):
    assert len(document) == len(other)
    for number, (first, second) in enumerate(zip(document, other), 1):
        assert first.get_pixmap().samples == second.get_pixmap().samples, f"Raster mismatch on {number}"
        assert first.get_text() == second.get_text(), f"Text mismatch on {number}"
        assert first.get_links() == second.get_links() or sorted(
            (link.get("page", -1), link.get("uri", "")) for link in first.get_links()
        ) == sorted(
            (link.get("page", -1), link.get("uri", "")) for link in second.get_links()
        ), f"Link destination mismatch on {number}"


def check_source_links(document, source):
    bibliography = source / "pages/folio-20.tex"
    style = source / "style/magazine.tex"
    declared = set()
    for path in (bibliography, style):
        for uri in re.findall(r"\{(https?://[^{}\s]+)\}", path.read_text(encoding="utf-8")):
            declared.add(re.sub(r"\\([%#_&])", r"\1", uri))
    embedded = {link["uri"] for link in document[19].get_links() if "uri" in link}
    assert declared, "No declared bibliography URLs found"
    assert declared == embedded, f"Missing URLs: {declared - embedded}; extra URLs: {embedded - declared}"


def render(document, output):
    output.mkdir(parents=True, exist_ok=True)
    selections = {1: "cover", 3: "abstract", 10: "forecast", 17: "comparison", 19: "conclusion"}
    for folio, label in selections.items():
        document[folio - 1].get_pixmap(dpi=110, alpha=False).save(output / f"{label}.png")
    contact = fitz.open()
    width, height, gap = 218, 308, 10
    sheet = contact.new_page(width=4 * width + 5 * gap, height=5 * height + 6 * gap)
    sheet.draw_rect(sheet.rect, color=None, fill=(0.22, 0.21, 0.20))
    for index, page in enumerate(document):
        x = gap + (index % 4) * (width + gap)
        y = gap + (index // 4) * (height + gap)
        sheet.insert_image(fitz.Rect(x, y, x + width, y + height), pixmap=page.get_pixmap(dpi=48))
    sheet.get_pixmap(alpha=False).save(output / "contact-sheet.png")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--compare", type=Path, help="second PDF compiled from the submitted sources")
    parser.add_argument("--source", type=Path, help="LaTeX directory whose bibliography URLs must match")
    parser.add_argument("--render", type=Path, help="directory for optional PNG previews")
    args = parser.parse_args()
    with fitz.open(args.pdf) as document:
        links = check(document)
        if args.source:
            check_source_links(document, args.source)
            print("All bibliography and image-credit URLs match the source.")
        if args.compare:
            with fitz.open(args.compare) as other:
                compare(document, other)
            print("All 20 pages match the comparison PDF at 72 dpi, with identical text and destinations.")
        if args.render:
            render(document, args.render)
    print(f"20 A4 pages; correct folios; Hebrew in Heebo; cover and metadata authors.")
    print(f"8 contents destinations; {links} distinct bibliography links.")
    print(f"SHA-256 {hashlib.sha256(args.pdf.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
