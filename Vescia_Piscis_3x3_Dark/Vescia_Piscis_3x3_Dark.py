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
        y, z = y*np.cos(ax) - z*np.sin(ax), y*np.sin(ax) + z*np.cos(ax)
    if ay:
        x, z = x*np.cos(ay) + z*np.sin(ay), -x*np.sin(ay) + z*np.cos(ay)
    if az:
        x, y = x*np.cos(az) - y*np.sin(az), x*np.sin(az) + y*np.cos(az)
    return x, y, z

# ============================================================
# ENDA MODULEN (CENTER)
# ============================================================
def vesica_module(center=(0,0,0), scale=3.0):
    cx, cy, cz = center
    X, Y, Z = [], [], []

    configs = [
        (scale, (0,0,0)),
        (scale/2, (90,0,0)),
        (scale/2, (0,90,0)),
        (scale/3, (45,45,0)),
    ]

    for r, rot in configs:
        for shift in (-r/2, r/2):
            x, y = vesica_circle(r)
            z = np.zeros_like(x)
            x = x + shift
            x, y, z = rotate(x, y, z, *rot)

            X += list(x + cx) + [None]
            Y += list(y + cy) + [None]
            Z += list(z + cz) + [None]

    return X, Y, Z

# ============================================================
# BYGG – ENDAST MITTEN
# ============================================================
X, Y, Z = vesica_module()

# ============================================================
# RENDER
# ============================================================
fig = go.Figure(go.Scatter3d(
    x=X,
    y=Y,
    z=Z,
    mode="lines",
    line=dict(color="white", width=2),
    hoverinfo="none"
))

fig.update_layout(
    template="plotly_dark",
    title="RP9 — Vesica Piscis (Central struktur)",
    scene=dict(
        aspectmode="data",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        camera=dict(eye=dict(x=2.2, y=2.2, z=2.2))
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

out = "vesica_center_only.html"
fig.write_html(out, include_plotlyjs=True)
print("KLART – Öppna:", os.path.abspath(out))
