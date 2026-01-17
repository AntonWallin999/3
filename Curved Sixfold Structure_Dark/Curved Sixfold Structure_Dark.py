# ============================================================
# Project: A Correct Relation to Information
# Subproject: Establish M.P.S_010
# ID (002)
# Code Block Nr: 15
# Code Block Name: Curved Sixfold Structure
# License: (CC BY-NC-ND)
# Created by: Anton Wallin
# Sigil: - = ( o ) = -
# ============================================================

import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import os
from itertools import combinations

# ============================================================
# GEOMETRI
# ============================================================
def circle_points(center, radius, n=120):
    t = np.linspace(0.0, 2.0 * np.pi, n)
    x = center[0] + radius * np.cos(t)
    y = center[1] + radius * np.sin(t)
    z = np.zeros_like(x)
    return x, y, z

def intersection(p1, p2, r):
    (x0, y0), (x1, y1) = p1, p2
    dx, dy = x1 - x0, y1 - y0
    d = np.hypot(dx, dy)
    if d > 2*r or d == 0.0:
        return []

    a = d / 2.0
    h = np.sqrt(r*r - a*a)
    xm = x0 + dx * 0.5
    ym = y0 + dy * 0.5
    rx = -dy * (h / d)
    ry =  dx * (h / d)

    return [(xm + rx, ym + ry, 0.0), (xm - rx, ym - ry, 0.0)]

def rotate_90_cw(point):
    x, y = point
    return (y, -x)

# ============================================================
# PARAMETRAR
# ============================================================
r = 1.0
d = 0.85

centers = [
    (0.0, 0.0),
    (d, 0.0),
    (d / 2.0,  d * np.sqrt(3.0) / 2.0),
    (d / 2.0, -d * np.sqrt(3.0) / 2.0),
    (0.0,  d),
    (0.0, -d)
]

rotated_centers = [rotate_90_cw(c) for c in centers]

colors = [
    "#808080",  # gray
    "#1E90FF",  # blue
    "#00FF7F",  # green
    "#FF4040",  # red
    "#9370DB",  # purple
    "#FFA500"   # orange
]

# ============================================================
# FIGUR
# ============================================================
fig = go.Figure()

# Rita cirklar
for c, col in zip(rotated_centers, colors):
    x, y, z = circle_points(c, r)
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode="lines",
        line=dict(color=col, width=3),
        hoverinfo="none",
        showlegend=False
    ))

# Intersektionspunkter
all_ints = []
for c1, c2 in combinations(rotated_centers, 2):
    all_ints.extend(intersection(c1, c2, r))

if all_ints:
    xs, ys, zs = zip(*all_ints)
    fig.add_trace(go.Scatter3d(
        x=xs, y=ys, z=zs,
        mode="markers",
        marker=dict(size=4, color="white"),
        hoverinfo="none",
        showlegend=False
    ))

# Koppla alla intersektionspunkter (streckat nät)
for (x1, y1, _), (x2, y2, _) in combinations(all_ints, 2):
    fig.add_trace(go.Scatter3d(
        x=[x1, x2],
        y=[y1, y2],
        z=[0.0, 0.0],
        mode="lines",
        line=dict(color="white", width=1, dash="dot"),
        hoverinfo="none",
        showlegend=False,
        opacity=0.25
    ))

# ============================================================
# LAYOUT
# ============================================================
fig.update_layout(
    title="Curved Sixfold Structure — Emergent Linear Lattice (M.P.S_010)",
    template="plotly_dark",
    scene=dict(
        aspectmode="data",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        camera=dict(eye=dict(x=0.0, y=-3.0, z=2.0))
    ),
    margin=dict(l=0, r=0, t=50, b=0)
)

# ============================================================
# EXPORT → HTML
# ============================================================
output_file = "MPS_010_Curved_Sixfold_Structure.html"
pio.write_html(
    fig,
    file=output_file,
    include_plotlyjs=True,
    full_html=True,
    auto_open=True
)

print("KLART – HTML skapad:", os.path.abspath(output_file))
