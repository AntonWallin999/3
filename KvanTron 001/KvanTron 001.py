# ============================================================
# Project: A Correct Relation to Information
# Subproject: Establish M.P.S_010
# Visualization: KvanTron 001
# License: (CC BY-NC-ND)
# Created by: Anton Wallin
# ============================================================

import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import os
from math import pi, sin, cos, sqrt

# ============================================================
# KONSTANTER
# ============================================================
phi = (1.0 + sqrt(5.0)) / 2.0
scale_1_5 = 1.5
base_radius = 0.5
num_layers = 4
max_depth = 2
spiral_range = np.linspace(-3.0, 3.0, 200)
frequency = 1.0

# ============================================================
# FIBONACCI
# ============================================================
def fibonacci(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return np.array(seq[:n], dtype=float)

fib_seq = fibonacci(num_layers)
pi_exp = np.array([pi ** (i / 2.0) for i in range(num_layers)])
Vn = ((phi * fib_seq / 2.0) ** 3.0) * pi_exp

# ============================================================
# GEOMETRIHJÄLP
# ============================================================
def make_cube_vertices(center, scale):
    o = scale / 2.0
    cx, cy, cz = center
    return np.array([
        [cx-o, cy-o, cz-o], [cx+o, cy-o, cz-o],
        [cx+o, cy+o, cz-o], [cx-o, cy+o, cz-o],
        [cx-o, cy-o, cz+o], [cx+o, cy-o, cz+o],
        [cx+o, cy+o, cz+o], [cx-o, cy+o, cz+o]
    ])

def make_cube_edges(v, color, width=2, name=None):
    edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
    out = []
    for i,j in edges:
        out.append(go.Scatter3d(
            x=[v[i][0], v[j][0]],
            y=[v[i][1], v[j][1]],
            z=[v[i][2], v[j][2]],
            mode="lines",
            line=dict(color=color, width=width),
            name=name if i == 0 else None,
            hoverinfo="none"
        ))
    return out

def make_sphere(center, r, color, opacity):
    u,v = np.mgrid[0:2*pi:30j, 0:pi:15j]
    x = r*np.cos(u)*np.sin(v) + center[0]
    y = r*np.sin(u)*np.sin(v) + center[1]
    z = r*np.cos(v) + center[2]
    return go.Surface(
        x=x,y=y,z=z,
        colorscale=[[0,color],[1,color]],
        showscale=False,
        opacity=opacity
    )

# ============================================================
# FRAKTALKUB
# ============================================================
def draw_fractal(center, size, depth, max_depth, traces):
    if depth > max_depth:
        return
    verts = make_cube_vertices(center, size)
    traces.extend(make_cube_edges(verts, "red" if depth % 2 == 0 else "blue", width=3))
    traces.append(make_sphere(center, size/2.0, "cyan", 0.2))
    for dx in (-size/2.0, size/2.0):
        for dy in (-size/2.0, size/2.0):
            for dz in (-size/2.0, size/2.0):
                draw_fractal(
                    (center[0]+dx, center[1]+dy, center[2]+dz),
                    size/2.0, depth+1, max_depth, traces
                )

# ============================================================
# SPIRALER
# ============================================================
def make_spiral(t, r, freq, axis):
    if axis == "z":
        return r*np.cos(freq*t), r*np.sin(freq*t), t
    if axis == "x":
        return t, r*np.cos(freq*t), r*np.sin(freq*t)
    if axis == "y":
        return r*np.cos(freq*t), t, r*np.sin(freq*t)

# ============================================================
# FIGUR
# ============================================================
fig = go.Figure()

# Central punkt
fig.add_trace(go.Scatter3d(
    x=[0],y=[0],z=[0],
    mode="markers",
    marker=dict(size=6,color="white"),
    name="Kvantpunkt"
))

# Central kub
center_cube = make_cube_vertices((0,0,0), 2)
fig.add_traces(make_cube_edges(center_cube, "red", 4, "Central Cube"))

# Hörn-sfärer
for v in center_cube:
    fig.add_trace(make_sphere(v, base_radius, "blue", 0.15))

# Z-lager
for i,v in enumerate(Vn):
    s = (v ** (1/3.0)) * scale_1_5
    fig.add_traces(make_cube_edges(
        make_cube_vertices((0,0,0), s),
        "rgba(120,170,255,0.5)", 2, f"Z-layer {i+1}"
    ))

# Fraktal
fractal_traces = []
draw_fractal((0,0,0), 1.0, 0, max_depth, fractal_traces)
fig.add_traces(fractal_traces)

# KvanTron-sfär
fig.add_trace(make_sphere((0,0,0), 0.4, "cyan", 0.5))

# Spiraler
for axis,col in zip(["z","x","y"],["red","green","purple"]):
    x,y,z = make_spiral(spiral_range, base_radius*phi, frequency, axis)
    fig.add_trace(go.Scatter3d(
        x=x,y=y,z=z,
        mode="lines",
        line=dict(color=col,width=2),
        name=f"{axis}-spiral"
    ))

# ============================================================
# LAYOUT + EXPORT
# ============================================================
fig.update_layout(
    title="KvanTron 001 — M.P.S",
    template="plotly_dark",
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode="cube"
    ),
    margin=dict(l=0,r=0,t=50,b=0),
    showlegend=True
)

out = "KvanTron_001.html"
pio.write_html(fig, out, include_plotlyjs=True, full_html=True, auto_open=True)
print("KLART – HTML skapad:", os.path.abspath(out))
