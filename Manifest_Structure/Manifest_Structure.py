# ============================================================
# Project: A Correct Relation to Information
# Subproject: Establish M.P.S_010
# ID (002)
# Code Block Nr: 25
# Code Block Name: Manifest Structure
# Focus: Singularity – Quantum4 – Hex6 – Quantum4 – Singularity
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
# CENTRA & SYMBOLER
# ============================================================
angles = np.linspace(0, 2*np.pi, 6, endpoint=False)
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
    ['black', 'black']
)

# ============================================================
# SFÄRYTA
# ============================================================
def sphere_surface(center, radius, resolution=40):
    u = np.linspace(0, 2*np.pi, resolution)
    v = np.linspace(0, np.pi, resolution)
    x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
    y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
    z = center[2] + radius * np.outer(np.ones_like(u), np.cos(v))
    return x, y, z

# ============================================================
# SFÄR-SKÄRNING
# ============================================================
def sphere_intersection_circle(c1, c2, r):
    c1 = np.array(c1, dtype=float)
    c2 = np.array(c2, dtype=float)
    d = np.linalg.norm(c2 - c1)
    if d > 2*r or d == 0:
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
    t = np.linspace(0, 2*np.pi, n)
    pts = np.array([
        center + radius*(np.cos(a)*v1 + np.sin(a)*v2)
        for a in t
    ])
    return pts[:,0], pts[:,1], pts[:,2]

# ============================================================
# FIGUR
# ============================================================
fig = go.Figure()

# Sfärer + symboler
for i, (c, label) in enumerate(zip(all_centers, all_labels)):
    x, y, z = sphere_surface(c, r)
    fig.add_trace(go.Surface(
        x=x, y=y, z=z,
        opacity=0.3,
        colorscale=[[0, colors[i]], [1, colors[i]]],
        showscale=False,
        hoverinfo='skip'
    ))
    fig.add_trace(go.Scatter3d(
        x=[c[0]], y=[c[1]], z=[c[2]],
        mode='text',
        text=[label],
        textfont=dict(size=20, color='white', family='Arial Black'),
        showlegend=False
    ))

# Skärningscirklar
for c1, c2 in combinations(all_centers, 2):
    res = sphere_intersection_circle(c1, c2, r)
    if res is None:
        continue
    pc, rad, normal = res
    cx, cy, cz = circle_points_3d(pc, rad, normal)
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
    title='Manifest Structure — Singularity · Q4 · Hex6 · Q4 · Singularity',
    template='plotly_dark',
    scene=dict(
        bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        zaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        aspectmode='data'
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, t=50, b=0)
)

# ============================================================
# EXPORT → HTML (GARANTERAD)
# ============================================================
output_file = "MPS_010_Manifest_Structure.html"

pio.write_html(
    fig,
    file=output_file,
    include_plotlyjs=True,
    full_html=True,
    auto_open=True
)

print("KLART – HTML skapad:", os.path.abspath(output_file))
