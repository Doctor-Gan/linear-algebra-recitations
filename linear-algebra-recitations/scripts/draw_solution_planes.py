#!/usr/bin/env python3
"""Regenerate the Week 1 affine-plane figure (requires NumPy and Matplotlib)."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
fig = plt.figure(figsize=(10, 4.6), facecolor="white")
s, t = np.meshgrid(np.linspace(-0.65, 0.65, 8), np.linspace(-0.65, 0.65, 8))
colors = ["#277f91", "#bd7036"]
for k, c in enumerate((0, 1)):
    ax = fig.add_subplot(1, 2, k + 1, projection="3d")
    ax.plot_surface(c-s-t, s, t, color=colors[k], alpha=0.48, edgecolor="white", linewidth=0.3)
    ax.scatter([c], [0], [0], color="#202b35", s=24, depthshade=False)
    ax.quiver(c, 0, 0, -0.48, 0.48, 0, color="#254b92", linewidth=2, arrow_length_ratio=0.16)
    ax.quiver(c, 0, 0, -0.48, 0, 0.48, color="#972d54", linewidth=2, arrow_length_ratio=0.16)
    if c:
        ax.quiver(0, 0, 0, 1, 0, 0, color="#202b35", linewidth=1.7, arrow_length_ratio=0.1)
        ax.text(0.5, 0.03, -0.12, r"$x_0$", fontsize=11)
    ax.set(xlim=(-1.4, 2.4), ylim=(-0.9, 0.9), zlim=(-0.9, 0.9),
           xlabel=r"$x_1$", ylabel=r"$x_2$", zlabel=r"$x_3$")
    ax.set_xticks([-1, 0, 1, 2]); ax.set_yticks([-0.5, 0, 0.5]); ax.set_zticks([-0.5, 0, 0.5])
    ax.tick_params(labelsize=8, pad=0)
    ax.view_init(elev=24, azim=36)
    ax.set_box_aspect((1.5, 1, 1))
    ax.set_title(r"$x_1+x_2+x_3=" + str(c) + "$", fontsize=13, pad=10)
fig.text(0.5, 0.025, "The same two independent directions, with a different starting point.",
         ha="center", fontsize=10, color="#3f4c59")
fig.subplots_adjust(left=0, right=1, bottom=0.12, top=0.91, wspace=0.02)
(root / "assets").mkdir(exist_ok=True)
fig.savefig(root / "assets" / "solution-planes.png", dpi=180, bbox_inches="tight")
plt.close(fig)
