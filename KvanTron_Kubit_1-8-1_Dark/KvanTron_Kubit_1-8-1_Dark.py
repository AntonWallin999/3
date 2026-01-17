# ============================================================
# KvanTron KubBit 1-8-1
# Skalbar Kub-Modul + 8x Instanser
# ============================================================

import plotly.graph_objects as go
import numpy as np

# ------------------------------------------------------------
# 1. KANONISK MODUL (EN ENHET)
# ------------------------------------------------------------

def rp9_module(center=(0,0,0), scale=1.0, opacity=1.0):
    cx, cy, cz = center
    s = scale
    traces = []

    # kubhörn
    v = np.array([
        [-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],
        [-1,-1, 1],[1,-1, 1],[1,1, 1],[-1,1, 1]
    ]) * s + np.array(center)

    edges = [
        (0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7)
    ]

    for a,b in edges:
        traces.append(go.Scatter3d(
            x=[v[a][0], v[b][0]],
            y=[v[a][1], v[b][1]],
            z=[v[a][2], v[b][2]],
            mode="lines",
            line=dict(color="cyan", width=4),
            opacity=opacity,
            showlegend=False
        ))

    # centrumlinjer
    for p in v:
        traces.append(go.Scatter3d(
            x=[cx, p[0]],
            y=[cy, p[1]],
            z=[cz, p[2]],
            mode="lines",
            line=dict(color="cyan", width=2, dash="dot"),
            opacity=opacity * 0.7,
            showlegend=False
        ))

    # cirklar
    t = np.linspace(0, 2*np.pi, 180)
    radii = [s*0.25, s*0.5, s*0.75]

    for r in radii:
        traces.append(go.Scatter3d(
            x=cx + r*np.cos(t),
            y=cy + r*np.sin(t),
            z=np.full_like(t, cz),
            mode="lines",
            line=dict(color="red", width=3),
            opacity=opacity,
            showlegend=False
        ))
        traces.append(go.Scatter3d(
            x=cx + r*np.cos(t),
            y=np.full_like(t, cy),
            z=cz + r*np.sin(t),
            mode="lines",
            line=dict(color="lime", width=3),
            opacity=opacity,
            showlegend=False
        ))

    return traces

# ------------------------------------------------------------
# 2. BYGG KUBBIT (1 → 8 → 1)
# ------------------------------------------------------------

def build_kubbit(base_center=(0,0,0), outer_scale=6.0, inner_scale=1.2):
    bx, by, bz = base_center
    offset = outer_scale / 4.0
    traces = []

    for dx in (-offset, offset):
        for dy in (-offset, offset):
            for dz in (-offset, offset):
                traces += rp9_module(
                    center=(bx+dx, by+dy, bz+dz),
                    scale=inner_scale,
                    opacity=0.9
                )

    # helhetskub
    traces += rp9_module(
        center=base_center,
        scale=outer_scale,
        opacity=0.25
    )

    return traces

# ------------------------------------------------------------
# 3. RENDERING
# ------------------------------------------------------------

fig = go.Figure(
    data=build_kubbit()
)

fig.update_layout(
    title=dict(
        text="KvanTron KubBit 1-8-1",
        x=0.5,
        font=dict(color="white", size=22)
    ),
    paper_bgcolor="black",
    plot_bgcolor="black",
    scene=dict(
        bgcolor="black",
        aspectmode="cube",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        camera=dict(eye=dict(x=2.2, y=2.2, z=2.2))
    ),
    margin=dict(l=0, r=0, b=0, t=60)
)

fig.show()

# ------------------------------------------------------------
# 4. SPARA
# ------------------------------------------------------------

fig.write_html(
    "KvanTron_KubBit_1-8-1.html",
    include_plotlyjs="cdn",
    auto_open=True
)

try:
    fig.write_image(
        "KvanTron_KubBit_1-8-1.png",
        width=2200,
        height=2200,
        scale=2
    )
except:
    pass

print("KLART — KvanTron KubBit 1-8-1 genererad.")
