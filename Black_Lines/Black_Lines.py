# ============================================================
# Project: A Correct Relation to Information
# Subproject: Establish M.P.S_010
# ID (002)
# Code Block Nr: 18
# Code Block Name: Black Lines
# Focus: Intersection Points
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
# GEOMETRIFUNKTIONER
# ============================================================
def circle_points(center, radius, n=100):
    angles = np.linspace(0.0, 2.0*np.pi, n)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    z = np.zeros_like(x)
    return x, y, z

def intersection_points(c1, c2, r):
    (x0, y0), (x1, y1) = c1, c2
    d = np.hypot(x1 - x0, y1 - y0)
    if d > 2.0*r or d == 0.0:
        return []
    a = d / 2.0
    h = np.sqrt(r**2 - a**2)
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    rx = -(y1 - y0) * (h / d)
    ry =  (x1 - x0) * (h / d)
    return [
        (xm + rx, ym + ry, 0.0),
        (xm - rx, ym - ry, 0.0)
    ]

# ============================================================
# PARAMETRAR
# ============================================================
r = 1.0
d = r * np.sqrt(3.0)

angles = np.linspace(0.0, 2.0*np.pi, 6, endpoint=False)
hex_centers = [(d * np.cos(a), d * np.sin(a)) for a in angles]

top_center = (0.0,  d + r)
bottom_center = (0.0, -(d + r))

all_centers = hex_centers + [top_center, bottom_center]

# ============================================================
# FIGUR
# ============================================================
fig = go.Figure()

# --- Cirklar ---
for c in all_centers:
    x, y, z = circle_points(c, r)
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode='lines',
        line=dict(color='gray', width=2),
        showlegend=False
    ))

# --- Intersektioner ---
ints = []
for c1, c2 in combinations(all_centers, 2):
    pts = intersection_points(c1, c2, r)
    ints.extend(pts)

if ints:
    xs, ys, zs = zip(*ints)

    # Punkter
    fig.add_trace(go.Scatter3d(
        x=xs, y=ys, z=zs,
        mode='markers',
        marker=dict(size=4, color='black'),
        name='Intersections'
    ))

    # Svarta linjer mellan alla punkter
    for p1, p2 in combinations(ints, 2):
        fig.add_trace(go.Scatter3d(
            x=[p1[0], p2[0]],
            y=[p1[1], p2[1]],
            z=[p1[2], p2[2]],
            mode='lines',
            line=dict(color='black', width=1),
            showlegend=False
        ))

# ============================================================
# LAYOUT (VIT BAKGRUND)
# ============================================================
fig.update_layout(
    title='Intersection Structure — Black Lines',
    template='plotly_white',
    scene=dict(
        xaxis=dict(showgrid=True, zeroline=False),
        yaxis=dict(showgrid=True, zeroline=False),
        zaxis=dict(showgrid=False, zeroline=False),
        aspectmode='data',
        bgcolor='white'
    ),
    paper_bgcolor='white',
    plot_bgcolor='white',
    font=dict(color='black'),
    margin=dict(l=0, r=0, t=30, b=0)
)

# ============================================================
# EXPORT → HTML (GARANTERAD)
# ============================================================
output_file = "MPS_010_Black_Lines.html"

pio.write_html(
    fig,
    file=output_file,
    include_plotlyjs=True,
    full_html=True,
    auto_open=True
)

print("KLART – HTML skapad:", os.path.abspath(output_file))
