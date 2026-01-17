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
    ax_r, ay_r, az_r = np.deg2rad([ax, ay, az])

    if ax_r != 0.0:
        y, z = y * np.cos(ax_r) - z * np.sin(ax_r), y * np.sin(ax_r) + z * np.cos(ax_r)
    if ay_r != 0.0:
        x, z = x * np.cos(ay_r) + z * np.sin(ay_r), -x * np.sin(ay_r) + z * np.cos(ay_r)
    if az_r != 0.0:
        x, y = x * np.cos(az_r) - y * np.sin(az_r), x * np.sin(az_r) + y * np.cos(az_r)

    return x, y, z

def mirror_x(x, y, z):
    return -x, y, z

# ============================================================
# VV-ENHET
# ============================================================
def vv_enhet(scale=3.0, global_rot=(0.0, 0.0, 0.0), mirrored=False):
    X, Y, Z = [], [], []

    configs = [
        (scale, (0.0, 0.0, 0.0)),
        (scale / 2.0, (90.0, 0.0, 0.0)),
        (scale / 2.0, (0.0, 90.0, 0.0)),
        (scale / 3.0, (45.0, 45.0, 0.0)),
    ]

    for r, local_rot in configs:
        for shift in (-r / 2.0, r / 2.0):
            x, y = vesica_circle(r)
            z = np.zeros_like(x)
            x = x + shift

            x, y, z = rotate(x, y, z, *local_rot)
            x, y, z = rotate(x, y, z, *global_rot)

            if mirrored:
                x, y, z = mirror_x(x, y, z)

            X += list(x) + [None]
            Y += list(y) + [None]
            Z += list(z) + [None]

    return X, Y, Z

# ============================================================
# 8 INSTANSER: 4 NORMALA + 4 SPEGLADE
# ============================================================
X, Y, Z = [], [], []

rotations = [0.0, 45.0, 90.0, 135.0]

for rz in rotations:
    # normal
    x, y, z = vv_enhet(global_rot=(0.0, 0.0, rz), mirrored=False)
    X += x; Y += y; Z += z

    # speglad
    x, y, z = vv_enhet(global_rot=(0.0, 0.0, rz), mirrored=True)
    X += x; Y += y; Z += z

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
    title="RP9 — VV-enhet (D8: rotation + spegling)",
    scene=dict(
        aspectmode="data",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        camera=dict(eye=dict(x=2.25, y=2.25, z=2.25))
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

out = "vv_enhet_8_instans_speglad.html"
fig.write_html(out, include_plotlyjs=True)
print("KLART – Öppna:", os.path.abspath(out))
