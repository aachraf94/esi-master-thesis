"""
Generate Chapter 1 figures:
  - fig_arch_evolution.png  (Figure 1.1 — Data architecture evolution)
  - fig_c1_heatmap.png      (Figure 1.2 — C1 gap heatmap, replaces Table 1.5)

Run from any directory; outputs to this script's own directory.
"""

import os
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

OUTPUT = os.path.dirname(os.path.abspath(__file__))

# ─── Shared style ────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 9,
    'axes.spines.top': False,
    'axes.spines.right': False,
})


# ═══════════════════════════════════════════════════════════════════════════════
#  Figure 1.1 — Data Architecture Evolution: Classical DW → Lakehouse
# ═══════════════════════════════════════════════════════════════════════════════

fig, ax = plt.subplots(figsize=(13, 4.8))
ax.set_xlim(0, 13.5)
ax.set_ylim(-0.9, 5)
ax.axis('off')

BOX_H = 3.4
BOX_W = 2.8
Y0    = 0.5          # bottom y of all boxes
PAD   = 1.0          # horizontal gap between boxes

boxes = [
    {
        'x': 0.2, 'label': 'Classical DW',
        'facecolor': '#E8E8E8', 'edgecolor': '#555555',
        'props': ['Fixed schema (3NF / star)', 'Integrated history', 'SQL / OLAP only'],
        'gap':   'Schema rigidity; analytics capped at descriptive',
    },
    {
        'x': 0.2 + BOX_W + PAD, 'label': 'Data Lake',
        'facecolor': '#D6EAF8', 'edgecolor': '#2471A3',
        'props': ['Schema-on-read', 'Open formats (Parquet)', 'Any data shape accepted'],
        'gap':   'No governance, no transactional guarantees',
    },
    {
        'x': 0.2 + 2*(BOX_W + PAD), 'label': 'Lakehouse',
        'facecolor': '#D5F5E3', 'edgecolor': '#1E8449',
        'props': ['ACID table semantics', 'Unified BI + ML workloads', 'Open table layer (Delta / Iceberg)'],
        'gap':   'No modeling discipline for structural lineage',
    },
    {
        'x': 0.2 + 3*(BOX_W + PAD), 'label': 'Medallion / Delta',
        'facecolor': '#FEF9E7', 'edgecolor': '#B7950B',
        'props': ['Bronze — raw ingested data', 'Silver — cleansed & conformed', 'Gold — business-ready aggregates'],
        'gap':   'Implementation pattern within the Lakehouse',
    },
]

TRANSITION_LABELS = [
    '+ schema-on-read',
    '+ ACID & metadata layer',
    '+ zoned refinement',
]

for b in boxes:
    x, y = b['x'], Y0
    rect = mpatches.FancyBboxPatch(
        (x, y), BOX_W, BOX_H,
        boxstyle='round,pad=0.12',
        facecolor=b['facecolor'], edgecolor=b['edgecolor'], linewidth=1.8,
        zorder=2,
    )
    ax.add_patch(rect)

    # Title
    ax.text(x + BOX_W / 2, y + BOX_H - 0.3,
            b['label'], ha='center', va='center',
            fontsize=10, fontweight='bold', color='#222222', zorder=3)

    # Divider line under title
    ax.plot([x + 0.15, x + BOX_W - 0.15], [y + BOX_H - 0.6, y + BOX_H - 0.6],
            color=b['edgecolor'], linewidth=0.8, zorder=3)

    # Properties
    for k, prop in enumerate(b['props']):
        ax.text(x + 0.2, y + BOX_H - 1.0 - k * 0.68,
                prop, ha='left', va='center',
                fontsize=8, color='#333333', zorder=3)

    # Gap annotation below box
    ax.text(x + BOX_W / 2, y - 0.3,
            b['gap'], ha='center', va='top',
            fontsize=7.2, style='italic', color='#666666', wrap=True,
            zorder=3)

# Arrows with transition labels
for i, label in enumerate(TRANSITION_LABELS):
    x_from = boxes[i]['x'] + BOX_W
    x_to   = boxes[i + 1]['x']
    x_mid  = (x_from + x_to) / 2
    y_arr  = Y0 + BOX_H / 2 + 0.15

    ax.annotate(
        '', xy=(x_to + 0.05, y_arr), xytext=(x_from - 0.05, y_arr),
        arrowprops=dict(arrowstyle='->', color='#444444',
                        lw=2.0, mutation_scale=14),
        zorder=4,
    )
    ax.text(x_mid, y_arr + 0.35, label,
            ha='center', va='bottom',
            fontsize=7.8, color='#444444', zorder=4)

plt.tight_layout(pad=0.3)
out1 = os.path.join(OUTPUT, 'fig_arch_evolution.png')
plt.savefig(out1, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'Saved: {out1}')


# ═══════════════════════════════════════════════════════════════════════════════
#  Figure 1.2 — C1 Dual-Scalability Gap Assessment (heatmap)
# ═══════════════════════════════════════════════════════════════════════════════

# ✓=1  ∼=0.5  ✗=0
# Columns: Src Sch Vol His Prp  |  Mat ML Rdy Wkl Lif
data = np.array([
    [0,   0,   1,   0.5, 0,    0,   0,   1,   0,   0  ],   # Inmon / Kimball
    [1,   0,   1,   0,   0,    0.5, 0.5, 0,   0.5, 0  ],   # Data Lake
    [0.5, 0.5, 1,   0.5, 0.5,  1,   1,   1,   1,   1  ],   # Lakehouse
    [1,   1,   1,   1,   1,    0,   0,   0.5, 0,   0  ],   # Data Vault 2.0
])

architectures = ['Inmon /\nKimball', 'Data Lake', 'Lakehouse', 'Data Vault 2.0']
dims = ['Src', 'Sch', 'Vol', 'His', 'Prp', 'Mat', 'ML', 'Rdy', 'Wkl', 'Lif']
SYM = {1: '✓', 0.5: '∼', 0: '✗'}

fig, ax = plt.subplots(figsize=(10, 3.8))

# Background heatmap
im = ax.imshow(data, cmap='Greys', vmin=0, vmax=1, aspect='auto')

# Cell symbols
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        val = data[i, j]
        txt_color = 'white' if val >= 0.75 else 'black'
        ax.text(j, i, SYM[val], ha='center', va='center',
                fontsize=14, color=txt_color, fontweight='bold')

# Column ticks
ax.set_xticks(range(len(dims)))
ax.set_xticklabels(dims, fontsize=9.5)
ax.set_yticks(range(len(architectures)))
ax.set_yticklabels(architectures, fontsize=9.5)
ax.tick_params(length=0)

# Vertical divider between Structural and Analytical blocks
ax.axvline(x=4.5, color='black', linewidth=2.2)

# Column-group header labels (outside axes, in figure coords)
ax.annotate('Structural', xy=(2 / len(dims), 1.07),
            xycoords='axes fraction', ha='center',
            fontsize=10.5, fontweight='bold', annotation_clip=False)
ax.annotate('Analytical', xy=(7.5 / len(dims), 1.07),
            xycoords='axes fraction', ha='center',
            fontsize=10.5, fontweight='bold', annotation_clip=False)

# Remove spines
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout(pad=1.0)
out2 = os.path.join(OUTPUT, 'fig_c1_heatmap.png')
plt.savefig(out2, dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f'Saved: {out2}')

print('Done.')
