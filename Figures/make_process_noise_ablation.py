"""Regenerate Figures/process_noise_ablation.pdf.

Process-noise ablation on the MAD-Lab suite. Green = full KLA (learnable,
time-invariant process noise p); red = deterministic variant (p_t = 0).
With-noise baselines are the official single-block MAD results (tab:accuracy-heatmap).
Zero-noise values are from the corrected ablation run.
"""
import matplotlib.pyplot as plt
import numpy as np

labels = ["COMP", "MEM", "CR", "NR", "FR", "SC"]

# Green: full KLA (learnable process noise) -- official tab:accuracy-heatmap baseline.
kla = [85.03, 98.87, 99.95, 99.93, 45.70, 90.67]
# Red: deterministic ablation, p_t = 0 (corrected run).
kla_zero = [72.91, 100.00, 100.00, 100.00, 43.21, 75.73]

GREEN = "#2e7d32"   # full KLA
RED = "#9e9e9e"     # ablated (process noise = 0) -- neutral gray, colourblind-safe

x = np.arange(len(labels))
width = 0.4

plt.rcParams.update({"font.size": 14})
fig, ax = plt.subplots(figsize=(12, 6))

b1 = ax.bar(x - width / 2, kla, width, label="KLA-Möbius",
            color=GREEN, edgecolor="black", linewidth=0.8)
b2 = ax.bar(x + width / 2, kla_zero, width, label="KLA-Linear (process noise = 0)",
            color=RED, edgecolor="black", linewidth=0.8)

for bars in (b1, b2):
    for rect in bars:
        h = rect.get_height()
        ax.annotate(f"{h:.1f}", xy=(rect.get_x() + rect.get_width() / 2, h),
                    xytext=(0, 3), textcoords="offset points",
                    ha="center", va="bottom", fontsize=15)

ax.set_title("Process Noise Ablation", fontsize=22, fontweight="bold")
ax.set_xlabel("MADLAB Task", fontsize=19, fontweight="bold")
ax.set_ylabel("Accuracy (%)", fontsize=19, fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=16)
ax.tick_params(axis="y", labelsize=16)
ax.set_ylim(0, 134)
ax.set_yticks(range(0, 101, 20))
ax.legend(loc="upper right", fontsize=16, framealpha=1.0)
ax.grid(axis="y", linestyle="--", alpha=0.35)
ax.set_axisbelow(True)
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)

fig.tight_layout()
fig.savefig("process_noise_ablation.pdf", bbox_inches="tight")
print("wrote process_noise_ablation.pdf")
