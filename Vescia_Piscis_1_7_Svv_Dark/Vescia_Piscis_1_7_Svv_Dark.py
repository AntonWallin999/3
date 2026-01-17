import numpy as np
import plotly.graph_objects as go
import os

# ============================================================
# GRUNDGEOMETRI
# ============================================================
def vesica_circle(r, n=64):
    t = np.linspace(0.0, 2.0 * np.pi, n)
    return r * np.cos(t), r * np.sin(t)

def rotate(x, y, z, ax, ay, az):
    ax, ay, az = np.deg2rad([ax, ay, az])

    if ax != 0.0:
        y, z = y*np.cos(ax) - z*np.sin(ax), y*np.sin(ax) + z*np.cos(ax)
    if ay != 0.0:
        x, z = x*np.cos(ay) + z*np.sin(ay), -x*np.sin(ay) + z*np.cos(ay)
    if az != 0.0:
        x, y = x*np.cos(az) - y*np.sin(az), x*np.sin(az) + y*np.cos(az)

    return x, y, z

def mirror_x(x, y, z):
    return -x, y, z

# ============================================================
# SVV – SUPERSYMMETRISK VESICA PISCIS (D8)
# ============================================================
def svv_module(center=(0,0,0), scale=3.0):
    cx, cy, cz = center
    X, Y, Z = [], [], []

    local_configs = [
        (scale, (0.0, 0.0, 0.0)),
        (scale / 2.0, (90.0, 0.0, 0.0)),
        (scale / 2.0, (0.0, 90.0, 0.0)),
        (scale / 3.0, (45.0, 45.0, 0.0)),
    ]

    base_rotations = [0.0, 45.0, 90.0, 135.0]

    for rz in base_rotations:
        for mirrored in (False, True):
            for r, local_rot in local_configs:
                for shift in (-r / 2.0, r / 2.0):
                    x, y = vesica_circle(r)
                    z = np.zeros_like(x)
                    x = x + shift

                    x, y, z = rotate(x, y, z, *local_rot)
                    x, y, z = rotate(x, y, z, 0.0, 0.0, rz)

                    if mirrored:
                        x, y, z = mirror_x(x, y, z)

                    X += list(x + cx) + [None]
                    Y += list(y + cy) + [None]
                    Z += list(z + cz) + [None]

    return X, Y, Z

# ============================================================
# 1C + 6N STRUKTUR (ALLA = SVV)
# ============================================================
X, Y, Z = [], [], []

positions = [
    (0,0,0),
    (6,0,0), (-6,0,0),
    (0,6,0), (0,-6,0),
    (0,0,6), (0,0,-6)
]

for p in positions:
    lx, ly, lz = svv_module(center=p, scale=3.0)
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
    title="RP9 — Svv.Supersymetrisk Vesica Piscis (1C + 6N)",
    scene=dict(
        aspectmode="data",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        camera=dict(eye=dict(x=2.4, y=2.4, z=2.4))
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

out = "Svv_Vesica_Piscis_1C_8N.html"
fig.write_html(out, include_plotlyjs=True)
print("KLART – Öppna:", os.path.abspath(out))
