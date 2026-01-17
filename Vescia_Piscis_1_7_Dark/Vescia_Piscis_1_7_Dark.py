import numpy as np
import plotly.graph_objects as go
import os

# ============================================================
# GEOMETRI
# ============================================================
def vesica_circle(r, n=64):
    t = np.linspace(0, 2*np.pi, n)
    return r*np.cos(t), r*np.sin(t)

def rotate(x, y, z, ax, ay, az):
    ax, ay, az = np.deg2rad([ax, ay, az])
    if ax:
        y, z = y*np.cos(ax)-z*np.sin(ax), y*np.sin(ax)+z*np.cos(ax)
    if ay:
        x, z = x*np.cos(ay)+z*np.sin(ay), -x*np.sin(ay)+z*np.cos(ay)
    if az:
        x, y = x*np.cos(az)-y*np.sin(az), x*np.sin(az)+y*np.cos(az)
    return x, y, z

# ============================================================
# MODUL (ENDA STRUKTUREN SOM UPPREPAS)
# ============================================================
def vesica_module(center, scale):
    cx, cy, cz = center
    lines_x, lines_y, lines_z = [], [], []

    configs = [
        (scale, "gold", (0,0,0)),
        (scale/2, "silver", (90,0,0)),
        (scale/2, "silver", (0,90,0)),
        (scale/3, "lime", (45,45,0)),
    ]

    for r, _, rot in configs:
        for shift in (-r/2, r/2):
            x, y = vesica_circle(r)
            z = np.zeros_like(x)
            x += shift
            x, y, z = rotate(x, y, z, *rot)
            lines_x += list(x+cx) + [None]
            lines_y += list(y+cy) + [None]
            lines_z += list(z+cz) + [None]

    return lines_x, lines_y, lines_z

# ============================================================
# LÄTT FRAKTAL (FAST ANTAL)
# ============================================================
X, Y, Z = [], [], []

positions = [
    (0,0,0),
    (6,0,0), (-6,0,0),
    (0,6,0), (0,-6,0),
    (0,0,6), (0,0,-6)
]

for p in positions:
    lx, ly, lz = vesica_module(p, 3.0)
    X += lx
    Y += ly
    Z += lz

# ============================================================
# RENDER
# ============================================================
fig = go.Figure(go.Scatter3d(
    x=X, y=Y, z=Z,
    mode="lines",
    line=dict(color="white", width=2),
    hoverinfo="none"
))

fig.update_layout(
    template="plotly_dark",
    title="RP9 — Vesica Piscis (HTML-optimerad)",
    scene=dict(
        aspectmode="data",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        camera=dict(eye=dict(x=2.4, y=2.4, z=2.4))
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

out = "vesica_light.html"
fig.write_html(out, include_plotlyjs=True)
print("KLART:", os.path.abspath(out))
