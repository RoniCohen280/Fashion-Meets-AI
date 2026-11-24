"""Render selected 26-week, style-based MAEs from GeoStyle (ICCV 2019), Table 2.

Install matplotlib==3.10.8, then run python geostyle_mae.py.
The CSV stores proportions as published. The chart shows percentage points.
"""

import csv
from decimal import Decimal
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def main():
    directory = Path(__file__).resolve().parent
    with (directory / "geostyle_mae.csv").open(encoding="utf-8", newline="") as source:
        rows = list(csv.DictReader(source))

    models = [row["model"] for row in rows]
    errors = [Decimal(row["mae_proportion"]) * 100 for row in rows]
    ink, ivory, grey = "#1b1b1b", "#f7f5f0", "#756c65"
    plt.rcParams.update({"pdf.fonttype": 42, "font.family": "DejaVu Sans", "text.color": ink})

    figure, axes = plt.subplots(figsize=(8, 3.65), facecolor=ivory)
    figure.subplots_adjust(left=0.26, right=0.93, top=0.75, bottom=0.26)
    axes.set_facecolor(ivory)
    figure.text(0.05, 0.91, "Forecast error over 26 weeks", fontsize=20, fontfamily="DejaVu Serif")
    figure.text(0.05, 0.82, "Style prevalence in GeoStyle · selected models · lower is better", fontsize=10)

    bars = axes.barh(
        models, [float(error) for error in errors],
        color=[ink if model == "GeoStyle" else grey for model in models], height=0.56,
    )
    axes.bar_label(bars, labels=[f"{error:.2f}" for error in errors], padding=6, fontsize=10)
    axes.invert_yaxis()
    axes.set_xlim(0, 1.62)
    axes.xaxis.set_major_locator(MultipleLocator(0.25))
    axes.set_axisbelow(True)
    axes.grid(axis="x", color="#ccc4bc", linewidth=0.6)
    axes.tick_params(length=0, labelcolor=ink, labelsize=10, pad=6)
    axes.set_xlabel("Mean absolute error (percentage points)", labelpad=7, fontsize=10)
    for spine in axes.spines.values():
        spine.set_visible(False)

    figure.text(
        0.05, 0.055,
        "Source: Mall et al., GeoStyle, ICCV 2019, Table 2 (style-based trends).",
        fontsize=8,
    )
    figure.savefig(directory / "geostyle_mae.png", dpi=220)
    figure.savefig(directory / "geostyle_mae.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)


if __name__ == "__main__":
    main()
