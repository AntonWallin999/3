# ============================================================
# Project: A Correct Relation to Information
# Subproject: Establish M.P.S_010
# ID (002)
# Code Block Nr: 14.5
# Code Block Name: Hexagonal Logic Structure
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
    angles = np.linspace(0.0, 2.0 * np.pi, n)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    z = np.zeros_like(x)
    return x, y, z

def intersection_points(c1, c2, r):
    (x0, y0), (x1, y1) = c1, c2
    d = np.hypot(x1 - x0, y1 - y0)
    if d > 2*r or d == 0:
        return []
    a = d / 2.0
    h = np.sqrt(r*r - a*a)
    xm = x0 + (x1 - x0) / 2.0
    ym = y0 + (y1 - y0) / 2.0
    rx = -(y1 - y0) * (h / d)
    ry =  (x1 - x0) * (h / d)
    return [(xm + rx, ym + ry, 0.0), (xm - rx, ym - ry, 0.0)]

# ============================================================
# PARAMETRAR
# ============================================================
r = 1.0
d = r * np.sqrt(3.0)

angles = np.linspace(0.0, 2.0 * np.pi, 6, endpoint=False)
hex_centers = [(d * np.cos(a), d * np.sin(a)) for a in angles]

top_center = (0.0, d + r)
bottom_center = (0.0, -(d + r))

all_centers = hex_centers + [top_center, bottom_center]

symbols = [
    "π",
    "Φ",
    "√π",
    "+ / −",
    "× / ÷",
    "Ω / R",
    "1",
    "0"
]

# ============================================================
# FIGUR
# ============================================================
fig = go.Figure()

# Rita cirklar
for i, c in enumerate(all_centers):
    x, y, z = circle_points(c, r)
    color = "#00BFFF" if i < 6 else "#FF4500"
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode="lines",
        line=dict(color=color, width=3),
        hoverinfo="none",
        showlegend=False
    ))

# Intersektioner
intersections = []
for c1, c2 in combinations(all_centers, 2):
    intersections.extend(intersection_points(c1, c2, r))

if intersections:
    xs, ys, zs = zip(*intersections)
    fig.add_trace(go.Scatter3d(
        x=xs, y=ys, z=zs,
        mode="markers",
        marker=dict(size=4, color="white"),
        hoverinfo="none",
        showlegend=False
    ))

# Symboler
for (cx, cy), sym in zip(all_centers, symbols):
    fig.add_trace(go.Scatter3d(
        x=[cx], y=[cy], z=[0.05],
        mode="text",
        text=[sym],
        textfont=dict(size=18, color="white"),
        showlegend=False
    ))

# ============================================================
# LAYOUT
# ============================================================
fig.update_layout(
    title="Hexagonal Logic Structure — M.P.S_010",
    template="plotly_dark",
    scene=dict(
        aspectmode="data",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        camera=dict(eye=dict(x=0.0, y=-2.8, z=2.2))
    ),
    margin=dict(l=0, r=0, t=50, b=0)
)

# ============================================================
# EXPORT → HTML
# ============================================================
output_file = "MPS_010_Hexagonal_Logic_Structure.html"
pio.write_html(
    fig,
    file=output_file,
    include_plotlyjs=True,
    full_html=True,
    auto_open=True
)

print("KLART – HTML skapad:", os.path.abspath(output_file))
