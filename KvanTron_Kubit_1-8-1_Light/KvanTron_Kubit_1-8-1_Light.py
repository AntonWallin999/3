# ============================================================
# RP9 — Skalbar Kub-Modul + 8x Instanser (Kubbit)
# ============================================================

import plotly.graph_objects as go
import numpy as np
import os
import webbrowser

# ------------------------------------------------------------
# 1. KANONISK MODUL (EN ENHET)
# ------------------------------------------------------------

def rp9_module(center=(0,0,0), scale=1.0, opacity=1.0):
    cx, cy, cz = center
    s = scale

    traces = []

    # ---- kubhörn (lokal)
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
            line=dict(color="blue", width=4),
            opacity=opacity,
            showlegend=False
        ))

    # ---- centrumlinjer (diagonaler)
    for p in v:
        traces.append(go.Scatter3d(
            x=[cx, p[0]],
            y=[cy, p[1]],
            z=[cz, p[2]],
            mode="lines",
            line=dict(color="blue", width=2, dash="dot"),
            opacity=opacity * 0.8,
            showlegend=False
        ))

    # ---- cirklar (XY + XZ)
    t = np.linspace(0, 2*np.pi, 180)
    radii = [s*0.2, s*0.4, s*0.6]

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
            line=dict(color="green", width=3),
            opacity=opacity,
            showlegend=False
        ))

    return traces

# ------------------------------------------------------------
# 2. BYGG 8 MODULER → KUBBIT
# ------------------------------------------------------------

def build_kubbit(base_center=(0,0,0), outer_scale=4.0, inner_scale=0.9):
    bx, by, bz = base_center
    offset = outer_scale / 4.0

    traces = []

    # 2×2×2 = 8 positioner
    for dx in (-offset, offset):
        for dy in (-offset, offset):
            for dz in (-offset, offset):
                traces += rp9_module(
                    center=(bx+dx, by+dy, bz+dz),
                    scale=inner_scale,
                    opacity=0.9
                )

    # yttre ram (helheten)
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
    data=build_kubbit(
        base_center=(0,0,0),
        outer_scale=6.0,
        inner_scale=1.2
    )
)

fig.update_layout(
    title="RP9 — Skalbar Kubbit (8 moduler + helhet)",
    scene=dict(
        aspectmode="cube",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        camera=dict(eye=dict(x=2.2, y=2.2, z=2.2))
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

# visa
fig.show()

# ------------------------------------------------------------
# 4. SPARA (KANONISKT)
# ------------------------------------------------------------

html_file = "rp9_kubbit_interaktiv.html"
fig.write_html(html_file, include_plotlyjs="cdn", auto_open=True)

try:
    fig.write_image("rp9_kubbit.png", width=2200, height=2200, scale=2)
except:
    pass

print("KLART — skalbar kubbit genererad.")
