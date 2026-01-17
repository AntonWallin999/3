# ============================================================
# Project: A Correct Relation to Information
# Subproject: Establish M.P.S_010
# ID (002)
# Code Block Nr: 24
# Code Block Name: Manifest Structure (Inverted)
# Focus: Clean Lines / No Surfaces
# License: (CC BY-NC-ND)
# Created by: Anton Wallin
# Sigil: - = ( o ) = -
# ============================================================

import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
from itertools import combinations
import os

# ============================================================
# PARAMETRAR
# ============================================================
r = 1.0
z_offset_q4 = np.sqrt(2.0) * r
z_offset_singularity = 2.0 * np.sqrt(2.0) * r
d_hex = np.sqrt(3.0) * r

# ============================================================
# CENTRA & ETIKETTER
# ============================================================
angles = np.linspace(0.0, 2.0*np.pi, 6, endpoint=False)
hex_centers = [(d_hex*np.cos(a), d_hex*np.sin(a), 0.0) for a in angles]
hex_labels = ['A', 'B', 'C', 'D', 'E', 'F']

upper_q4 = [
    ( r,  r,  z_offset_q4),
    (-r,  r,  z_offset_q4),
    (-r, -r,  z_offset_q4),
    ( r, -r,  z_offset_q4)
]
upper_labels = ['π', 'φ', '√2', '1']

lower_q4 = [
    ( r,  r, -z_offset_q4),
    (-r,  r, -z_offset_q4),
    (-r, -r, -z_offset_q4),
    ( r, -r, -z_offset_q4)
]
lower_labels = ['+', '–', '×', '÷']

top_center = (0.0, 0.0,  z_offset_singularity)
bottom_center = (0.0, 0.0, -z_offset_singularity)
singularity_labels = ['Ω', '0']

all_centers = (
    hex_centers +
    upper_q4 +
    lower_q4 +
    [top_center, bottom_center]
)
all_labels = (
    hex_labels +
    upper_labels +
    lower_labels +
    singularity_labels
)

colors = (
    ['green']*6 +
    ['blue']*4 +
    ['red']*4 +
    ['white', 'white']
)

# ============================================================
# CIRKEL I 3D
# ============================================================
def circle_points_3d(center, radius, normal, n=120):
    normal = normal / np.linalg.norm(normal)
    ref = np.array([1.0, 0.0, 0.0]) if abs(normal[2]) > 0.9 else np.array([0.0, 0.0, 1.0])
    v1 = np.cross(normal, ref)
    v1 /= np.linalg.norm(v1)
    v2 = np.cross(normal, v1)
    t = np.linspace(0.0, 2.0*np.pi, n)
    pts = np.array([
        center + radius*(np.cos(a)*v1 + np.sin(a)*v2)
        for a in t
    ])
    return pts[:,0], pts[:,1], pts[:,2]

# ============================================================
# FIGUR
# ============================================================
fig = go.Figure()

# === Grundcirklar + etiketter ===
for i, (c, label) in enumerate(zip(all_centers, all_labels)):
    normal = np.array([0.0, 0.0, 1.0])
    cx, cy, cz = circle_points_3d(np.array(c, dtype=float), r, normal)

    fig.add_trace(go.Scatter3d(
        x=cx, y=cy, z=cz,
        mode='lines',
        line=dict(color=colors[i], width=3),
        hoverinfo='skip',
        showlegend=False
    ))

    fig.add_trace(go.Scatter3d(
        x=[c[0]], y=[c[1]], z=[c[2]],
        mode='text',
        text=[label],
        textfont=dict(size=18, color=colors[i], family='Arial Black'),
        showlegend=False
    ))

# === Intersektioner ===
for c1, c2 in combinations(all_centers, 2):
    c1 = np.array(c1, dtype=float)
    c2 = np.array(c2, dtype=float)
    d = np.linalg.norm(c2 - c1)
    if d > 2*r or d == 0:
        continue

    a = d / 2.0
    h = np.sqrt(r**2 - a**2)
    e = (c2 - c1) / d
    pc = c1 + a * e

    cx, cy, cz = circle_points_3d(pc, h, e)
    fig.add_trace(go.Scatter3d(
        x=cx, y=cy, z=cz,
        mode='lines',
        line=dict(color='darkred', width=2),
        hoverinfo='skip',
        showlegend=False
    ))

# ============================================================
# LAYOUT
# ============================================================
fig.update_layout(
    title='Manifest Structure — Inverted (Clean Lines)',
    template='plotly_dark',
    scene=dict(
        bgcolor='black',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        zaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        aspectmode='data'
    ),
    paper_bgcolor='black',
    plot_bgcolor='black',
    margin=dict(l=0, r=0, t=40, b=0)
)

# ============================================================
# EXPORT → HTML (GARANTERAD)
# ============================================================
output_file = "MPS_010_Manifest_Structure_Inverted.html"

pio.write_html(
    fig,
    file=output_file,
    include_plotlyjs=True,
    full_html=True,
    auto_open=True
)

print("KLART – HTML skapad:", os.path.abspath(output_file))
