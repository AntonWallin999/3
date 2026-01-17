# ============================================================
# Project: A Correct Relation to Information
# Subproject: Establish M.P.S_010
# ID (002)
# Code Block Nr: 22
# Code Block Name: Packed Sphere Structure
# Focus: Hexagon + 2 Quantum-4 Layers + Top & Bottom Spheres
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
def sphere_surface(center, radius, resolution=40):
    u = np.linspace(0.0, 2.0*np.pi, resolution)
    v = np.linspace(0.0, np.pi, resolution)
    x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
    y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
    z = center[2] + radius * np.outer(np.ones_like(u), np.cos(v))
    return x, y, z

def sphere_intersection_circle(c1, c2, r):
    c1 = np.array(c1, dtype=float)
    c2 = np.array(c2, dtype=float)
    d = np.linalg.norm(c2 - c1)
    if d > 2.0*r or d == 0.0:
        return None
    a = d / 2.0
    h = np.sqrt(r**2 - a**2)
    e = (c2 - c1) / d
    pc = c1 + a * e
    return pc, h, e

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
# PARAMETRAR
# ============================================================
r = 1.0
d_hex = r * np.sqrt(3.0)   # Hexagonradie

# ============================================================
# BASLAGER – HEXAGON (z = 0)
# ============================================================
angles = np.linspace(0.0, 2.0*np.pi, 6, endpoint=False)
hex_centers = [(d_hex*np.cos(a), d_hex*np.sin(a), 0.0) for a in angles]

# ============================================================
# KVADRATLAGER (Quantum-4)
# ============================================================
s = 2.0 * r
x_diff = d_hex - s/2.0
Z_offset = np.sqrt((2.0*r)**2 - x_diff**2)

quad_offsets = [
    (-s/2.0, -s/2.0),
    (-s/2.0,  s/2.0),
    ( s/2.0,  s/2.0),
    ( s/2.0, -s/2.0)
]

quad_top_centers = [(x, y,  Z_offset) for (x, y) in quad_offsets]
quad_bottom_centers = [(x, y, -Z_offset) for (x, y) in quad_offsets]

# ============================================================
# TOPP & BOTTEN-SFÄRER
# ============================================================
Z_top = Z_offset + 2.0*r
top_center = (0.0, 0.0,  Z_top)
bottom_center = (0.0, 0.0, -Z_top)

# ============================================================
# ALLA SFÄRCENTRA
# ============================================================
all_centers = (
    hex_centers +
    quad_top_centers + [top_center] +
    quad_bottom_centers + [bottom_center]
)

# ============================================================
# FIGUR
# ============================================================
fig = go.Figure()

# --- Sfärer ---
for i, c in enumerate(all_centers):
    xs, ys, zs = sphere_surface(c, r)
    fig.add_trace(go.Surface(
        x=xs, y=ys, z=zs,
        opacity=0.3,
        showscale=False,
        colorscale='Viridis',
        hoverinfo='skip'
    ))

# --- Skärningscirklar ---
for c1, c2 in combinations(all_centers, 2):
    res = sphere_intersection_circle(c1, c2, r)
    if res is None:
        continue
    pc, rad, normal = res
    cx, cy, cz = circle_points_3d(pc, rad, normal)
    fig.add_trace(go.Scatter3d(
        x=cx, y=cy, z=cz,
        mode='lines',
        line=dict(color='red', width=3),
        hoverinfo='skip',
        showlegend=False
    ))

# ============================================================
# LAYOUT
# ============================================================
fig.update_layout(
    title='Packed Sphere Structure — Hexagon + 2×Quantum-4 + Top/Bottom',
    template='plotly_dark',
    scene=dict(
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        zaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        aspectmode='data',
        bgcolor='black'
    ),
    paper_bgcolor='black',
    plot_bgcolor='black',
    margin=dict(l=0, r=0, t=50, b=0)
)

# ============================================================
# EXPORT → HTML (GARANTERAD)
# ============================================================
output_file = "MPS_010_Packed_Sphere_Structure.html"

pio.write_html(
    fig,
    file=output_file,
    include_plotlyjs=True,
    full_html=True,
    auto_open=True
)

print("KLART – HTML skapad:", os.path.abspath(output_file))
