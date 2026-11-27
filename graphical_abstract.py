"""Code-drawn graphical abstract v2 (matplotlib only; no AI image generator, no third-party artwork).
   python graphical_abstract.py            -> Elsevier preset  (1:2.5, 3320 x 1330 px)
   python graphical_abstract.py springer   -> optional Springer-style preset (check the journal's own size rule)
All numbers come from the manuscript (hindcast of 2023 on held-out blocks, Tables 3/7, Sect. 5.3, Supplementary S4)."""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon

PRESET = sys.argv[1] if len(sys.argv) > 1 else "elsevier"
W, H = {"elsevier": (13.28, 5.32), "springer": (11.0, 5.6)}[PRESET]
S = W / 13.28 * (1.0 if PRESET == "elsevier" else 0.97)       # font scale
DPI = 250
INK, MUTE, LINE = "#1f2328", "#6b7280", "#c4c8cc"
BLUE, YEL = "#dbe7fb", "#fdf0cc"
PURP, GREEN, ORG, GREY, BLACK, TEAL = "#7570b3", "#1b9e77", "#d95f02", "#9a9a9a", "#222222", "#2b6f8f"
plt.rcParams.update({"font.family": ["DejaVu Serif", "DejaVu Sans"], "axes.edgecolor": INK, "axes.linewidth": 1.2 * S})
fs = lambda v: v * S

fig = plt.figure(figsize=(W, H), dpi=DPI, facecolor="white")
bg = fig.add_axes([0, 0, 1, 1]); bg.set_xlim(0, 1); bg.set_ylim(0, 1); bg.axis("off")

# layout (figure fractions)
cols = [(0.012, 0.215), (0.250, 0.485), (0.520, 0.755), (0.790, 0.990)]
banner_y, banner_h = 0.025, 0.115
body_top, body_bot = 0.93, banner_y + banner_h + 0.04
for xs in (0.235, 0.505, 0.775):
    bg.plot([xs, xs], [banner_y + banner_h + 0.035, 0.975], color=LINE, lw=1.8 * S)

def header(i, title, sub=None):
    x0, x1 = cols[i]; cx = (x0 + x1) / 2
    bg.text(cx, 0.945, title, ha="center", va="center", fontsize=fs(19), fontweight="bold", color=INK)
    if sub: bg.text(cx, 0.855, sub, ha="center", va="center", fontsize=fs(10.2), color=MUTE)

def tag(i, text, color):
    x0, x1 = cols[i]
    bg.text((x0 + x1) / 2, banner_y + banner_h + 0.075, text, ha="center", va="center",
            fontsize=fs(12.5), fontweight="bold", color=color, linespacing=1.2)

def chart_ax(i, bottom=0.33, top=0.80, l=0.0, r=0.0):
    x0, x1 = cols[i]
    ax = fig.add_axes([x0 + l, bottom, (x1 - x0) - l - r, top - bottom], facecolor="none")
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=fs(10.5), length=3 * S, width=1.1 * S, colors=INK)
    ax.grid(axis="x" if False else "y", color="#e8e8e8", lw=0.8 * S); ax.set_axisbelow(True)
    return ax

# ---------------- Column 0: data & design ----------------
header(0, "Data & design")
x0, x1 = cols[0]
boxes = [("Landsat 2003 / 2013 / 2023\n+ terrain and climate layers\nKhatra, 2,410 km², 5 classes", BLUE, 0.605, 0.205),
         ("Hindcast 2023 from the\n2003–13 transition vs the\npersistence baseline\n(5 seeds, block bootstrap)", BLUE, 0.365, 0.205),
         ("Three models: CA-ANN-Markov,\nCNN-Markov, CNN-argmax\n+ 2033 rate scenarios", YEL, 0.150, 0.18)]
for t, c, y, h in boxes:
    bg.add_patch(FancyBboxPatch((x0 + .004, y), (x1 - x0) - .008, h, boxstyle="round,pad=0,rounding_size=0.018",
                                fc=c, ec="#555555", lw=1.8 * S, transform=bg.transData, mutation_aspect=H / W))
    bg.text((x0 + x1) / 2, y + h / 2, t, ha="center", va="center", fontsize=fs(10.3), color=INK, linespacing=1.3)
for ya in (0.605, 0.365):
    cx = (x0 + x1) / 2
    bg.add_patch(Polygon([[cx - .009, ya - .002], [cx + .009, ya - .002], [cx, ya - .032]], closed=True,
                         fc="#666666", ec="none"))
bg.text((x0 + x1) / 2, 0.80, "", ha="center")

# ---------------- Column 1: evidence (OA) ----------------
header(1, "① Evidence", "Overall accuracy (%), hindcast 2023")
ax = chart_ax(1, l=0.085, r=0.012)
names = ["Persistence\n(no change)", "CA-ANN-\nMarkov", "CNN-\nMarkov", "CNN-\nargmax"]
oa = [95.87, 95.58, 95.74, 92.66]; cc = [BLACK, PURP, PURP, GREY]
yy = range(len(oa) - 1, -1, -1)
ax.barh(list(yy), [v - 90 for v in oa], color=cc, height=0.66)
for y, v in zip(yy, oa):
    ax.text(9.2, y, f"{v:.2f}", va="center", ha="right", fontsize=fs(11.5), fontweight="bold", color=INK)
ax.set_yticks(list(yy)); ax.set_yticklabels(names, fontsize=fs(10.2))
ax.set_xlim(0, 9.3); ax.set_xticks([0, 2, 4, 6]); ax.set_xticklabels(["90", "92", "94", "96"])
ax.grid(axis="y", visible=False); ax.grid(axis="x", color="#e8e8e8", lw=0.8 * S)
ax.axvline(oa[0] - 90, color=BLACK, ls=":", lw=1.4 * S)
ax.set_xlabel("axis starts at 90%", fontsize=fs(8.5), color=MUTE, style="italic", labelpad=2)
tag(1, "No model beats\npersistence", ORG)

# ---------------- Column 2: skill (FoM) ----------------
header(2, "② Skill", "Figure of merit (FoM)")
ax = chart_ax(2, l=0.07, r=0.01, top=0.76)
fom = [0.0, 0.0266, 0.0556, 0.0028]; cc = [BLACK, PURP, TEAL, GREY]
lab = ["Base-\nline", "CA-ANN-\nMarkov", "CNN-\nMarkov", "CNN-\nargmax"]
ax.bar(range(4), fom, color=cc, width=0.64)
for i, v in enumerate(fom):
    ax.text(i, v + 0.0016, f"{v:.3f}", ha="center", fontsize=fs(11.5), fontweight="bold", color=INK)
ax.set_xticks(range(4)); ax.set_xticklabels(lab, fontsize=fs(8.8))
ax.set_ylim(0, 0.098); ax.set_yticks([0, 0.02, 0.04, 0.06])
ax.annotate("", xy=(2, 0.0745), xytext=(1, 0.0745), arrowprops=dict(arrowstyle="<->", color=INK, lw=1.6 * S))
ax.text(1.5, 0.0775, "CNN vs ANN: ΔFoM +0.016\n(95% CI 0.004 to 0.030)", ha="center", fontsize=fs(8.8), fontweight="bold", color=INK)
ax.text(-0.45, 0.047, "Fallow→Forest\nprecision 48%\nvs 33% chance", ha="left", va="center",
        fontsize=fs(8.6), color=GREEN, fontweight="bold", linespacing=1.25)
tag(2, "CNN-Markov locates\nchange best", TEAL)

# ---------------- Column 3: scenarios ----------------
header(3, "③ Scenarios", "Forest change 2023–33 (km²)")
ax = chart_ax(3, l=0.065, r=0.0, top=0.76)
vals = [40.96, 18.51, -4.17]; sds = [0.40, 0.13, 0.82]; cc = [GREEN, GREY, PURP]
ax.bar(range(3), vals, color=cc, width=0.62, yerr=sds, error_kw=dict(ecolor=INK, lw=1.4 * S, capsize=3 * S))
for i, (v, s) in enumerate(zip(vals, sds)):
    ax.text(i, v + (3.2 if v > 0 else -3.2), f"{v:+.1f}", ha="center", va="bottom" if v > 0 else "top",
            fontsize=fs(11.5), fontweight="bold", color=INK)
ax.axhline(0, color=INK, lw=1.2 * S)
ax.set_xticks(range(3)); ax.set_xticklabels(["T2 rates\n(2013–23)", "Mean\nrates", "T1 rates\n(2003–13)"], fontsize=fs(9.2))
ax.set_ylim(-12, 52); ax.set_yticks([0, 20, 40])
ax.spines["bottom"].set_visible(False); ax.tick_params(axis="x", length=0, pad=6 * S)
ax.grid(axis="y", color="#e8e8e8", lw=0.8 * S)
ax.text(2.45, 49, "Rates set\nthe quantity", ha="right", va="top", fontsize=fs(9), color=MUTE, style="italic")
tag(3, "Driven by\nassumptions", ORG)

# ---------------- Banner ----------------
bg.add_patch(FancyBboxPatch((0.012, banner_y), 0.978, banner_h, boxstyle="round,pad=0,rounding_size=0.012",
                            fc="#f2f2f2", ec="#8d8d8d", lw=2 * S, mutation_aspect=H / W))
bg.text(0.501, banner_y + banner_h / 2,
        "Persistence is hard to beat; real skill is in locating change, and 2033 maps are scenarios",
        ha="center", va="center", fontsize=fs(16 if PRESET == "elsevier" else 14.5), fontweight="bold", color=INK)

tagname = "ga_elsevier" if PRESET == "elsevier" else "ga_springer"
fig.savefig(f"{tagname}.png", dpi=DPI)
fig.savefig(f"{tagname}.tiff", dpi=DPI, pil_kwargs={"compression": "tiff_lzw"})
fig.savefig(f"{tagname}.pdf")
print(tagname, int(W * DPI), "x", int(H * DPI), "px")
