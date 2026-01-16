
>---
># HTML 3D interactive
>#HTML #3D #Interactive #Model #Visualization #3DRendering #KvanTron
>##  KvanTron Black
>
>
>> Link 🔗- https://antonwallin999.github.io/Html/Kvantron_Fraktal_Black.html
>---

<br />

# KvanTron_black1.png
![[KvanTron_black1.png]]

<br />

---

<br />

# KvanTron_black2.png
![[KvanTron_black2.png]]


<br />

---

<br />

# Kvantron_Fraktal_Black.py
````Python
==================================================
# KvanTron — Fractal-Holographic Quantum Cube
# HIGH-QUALITY VISUAL PRESENTATION VERSION
# ==================================================

import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import webbrowser
import os

pio.renderers.default = "browser"

# ==================================================
# VISUAL THEME
# ==================================================

BG_COLOR = "black"
LINE_WIDTH_MAIN = 5
LINE_WIDTH_SUB = 3
GLOW_OPACITY = 0.22

SPECTRAL_COLORS = [
    "#ff2a2a",  # red
    "#ff8c1a",  # orange
    "#ffd11a",  # yellow
    "#3cff3c",  # green
    "#3ca0ff",  # blue
    "#7b3cff",  # indigo
    "#d43cff"   # violet
]

# ==================================================
# GEOMETRY HELPERS
# ==================================================

def line(a, b, color, width=LINE_WIDTH_MAIN, dash=None):
    return go.Scatter3d(
        x=[a[0], b[0]],
        y=[a[1], b[1]],
        z=[a[2], b[2]],
        mode="lines",
        line=dict(color=color, width=width, dash=dash),
        hoverinfo="skip"
    )

def arrow(start, vec, color):
    return go.Cone(
        x=[start[0]], y=[start[1]], z=[start[2]],
        u=[vec[0]], v=[vec[1]], w=[vec[2]],
        colorscale=[[0, color], [1, color]],
        showscale=False,
        sizemode="absolute",
        sizeref=0.18,
        anchor="tail"
    )

def circle_xy(r, color):
    t = np.linspace(0, 2*np.pi, 300)
    return go.Scatter3d(
        x=r*np.cos(t),
        y=r*np.sin(t),
        z=np.zeros_like(t),
        mode="lines",
        line=dict(color=color, width=LINE_WIDTH_SUB),
        hoverinfo="skip"
    )

def circle_xz(r, color):
    t = np.linspace(0, 2*np.pi, 300)
    return go.Scatter3d(
        x=r*np.cos(t),
        y=np.zeros_like(t),
        z=r*np.sin(t),
        mode="lines",
        line=dict(color=color, width=LINE_WIDTH_SUB),
        hoverinfo="skip"
    )

def sphere(r, color):
    u = np.linspace(0, 2*np.pi, 60)
    v = np.linspace(0, np.pi, 60)
    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones_like(u), np.cos(v))
    return go.Surface(
        x=x, y=y, z=z,
        colorscale=[[0, color], [1, color]],
        opacity=GLOW_OPACITY,
        showscale=False,
        hoverinfo="skip"
    )

# ==================================================
# CORE STRUCTURE
# ==================================================

vertices = np.array([
    [-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],
    [-1,-1, 1],[1,-1, 1],[1,1, 1],[-1,1, 1]
])

edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

center = np.array([0,0,0])

traces = []

# ==================================================
# OUTER CUBE (PRIMARY FRAME)
# ==================================================

for a,b in edges:
    traces.append(line(vertices[a], vertices[b], "#3ca0ff"))

# ==================================================
# DIAGONALS + FLOW
# ==================================================

spectral_points = []

for v in vertices:
    traces.append(line(center, v, "#3ca0ff", dash="dot"))
    traces.append(arrow(v*0.92, -v*0.55, "#3ca0ff"))

    steps = np.linspace(0.1, 0.95, 7)
    for i,t in enumerate(steps):
        p = v * t
        spectral_points.append((p, SPECTRAL_COLORS[i]))

# ==================================================
# AXIAL FLOW
# ==================================================

axes = [
    np.array([1,0,0]), np.array([-1,0,0]),
    np.array([0,1,0]), np.array([0,-1,0]),
    np.array([0,0,1]), np.array([0,0,-1])
]

for a in axes:
    traces.append(line(center, a, "#ff2a2a", dash="dot"))
    traces.append(arrow(a*0.92, a*0.55, "#ff2a2a"))

# ==================================================
# SPECTRAL NODES
# ==================================================

sx, sy, sz, sc = [],[],[],[]
for p,c in spectral_points:
    sx.append(p[0]); sy.append(p[1]); sz.append(p[2]); sc.append(c)

traces.append(go.Scatter3d(
    x=sx,y=sy,z=sz,
    mode="markers",
    marker=dict(size=7, color=sc),
    hoverinfo="skip",
    name="Spectral Nodes"
))

# ==================================================
# CENTER POINT
# ==================================================

traces.append(go.Scatter3d(
    x=[0],y=[0],z=[0],
    mode="markers",
    marker=dict(size=14, color="white"),
    hoverinfo="skip",
    name="Center"
))

# ==================================================
# FRACTAL LEVELS
# ==================================================

levels = np.linspace(1/7, 1, 7)

for i,r in enumerate(levels):
    traces.append(circle_xy(r, SPECTRAL_COLORS[i]))
    traces.append(circle_xz(r, SPECTRAL_COLORS[i]))
    traces.append(sphere(r, SPECTRAL_COLORS[i]))

# ==================================================
# FIGURE
# ==================================================

fig = go.Figure(traces)
fig.update_layout(
    title=dict(
        text="KvanTron — Fractal-Holographic Quantum Cube",
        x=0.5,
        font=dict(color="white", size=22)
    ),
    paper_bgcolor=BG_COLOR,
    plot_bgcolor=BG_COLOR,
    scene=dict(
        aspectmode="cube",
        bgcolor=BG_COLOR,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False)
    ),
    margin=dict(l=0,r=0,b=0,t=50)
)

# ==================================================
# OUTPUT
# ==================================================

html_file = "KvanTron_Presentation.html"
fig.write_html(html_file)
webbrowser.open("file://" + os.path.realpath(html_file))
fig.show()
````


