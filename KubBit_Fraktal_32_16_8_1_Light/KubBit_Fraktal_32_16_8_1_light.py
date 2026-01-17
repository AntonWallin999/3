# ============================================================
# RP9 — Rekursiv skalbar Kubbit (8^n moduler)
# ============================================================

import plotly.graph_objects as go
import numpy as np
import os
import webbrowser

# ------------------------------------------------------------
# 1. KANONISK MODUL (EN KUB-MALL)
# ------------------------------------------------------------

def rp9_module(center=(0,0,0), scale=1.0, opacity=1.0):
    cx, cy, cz = center
    s = scale
    traces = []

    # Kubhörn
    v = np.array([
        [-1,-1,-1],[ 1,-1,-1],[ 1, 1,-1],[-1, 1,-1],
        [-1,-1, 1],[ 1,-1, 1],[ 1, 1, 1],[-1, 1, 1]
    ]) * s + np.array(center)

    edges = [
        (0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7)
    ]

    # Kanter
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

    # Diagonaler till centrum
    for p in v:
        traces.append(go.Scatter3d(
            x=[cx, p[0]],
            y=[cy, p[1]],
            z=[cz, p[2]],
            mode="lines",
            line=dict(color="blue", width=2, dash="dot"),
            opacity=min(1.0, opacity + 0.15),
            showlegend=False
        ))

    # Resonanscirklar (XY + XZ)
    t = np.linspace(0, 2*np.pi, 180)
    radii = [0.25*s, 0.5*s, 0.75*s]

    for r in radii:
        traces.append(go.Scatter3d(
            x=cx + r*np.cos(t),
            y=cy + r*np.sin(t),
            z=np.full_like(t, cz),
            mode="lines",
            line=dict(color="crimson", width=3),
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
# 2. REKURSIV KUBBIT
# ------------------------------------------------------------

def build_recursive_kubbit(
    center=(0,0,0),
    scale=6.0,
    depth=0,
    max_depth=2,
    inner_scale_factor=0.48
):
    traces = []

    # Opacity-schema (släpper igenom MER än innan)
    opacity_map = [0.95, 0.75, 0.55, 0.4]
    opacity = opacity_map[min(depth, len(opacity_map)-1)]

    # Rita aktuell nivå
    traces += rp9_module(
        center=center,
        scale=scale,
        opacity=opacity
    )

    if depth >= max_depth:
        return traces

    # Förskjutning för 2×2×2
    offset = scale * inner_scale_factor

    for dx in (-offset, offset):
        for dy in (-offset, offset):
            for dz in (-offset, offset):
                traces += build_recursive_kubbit(
                    center=(center[0]+dx, center[1]+dy, center[2]+dz),
                    scale=scale * inner_scale_factor,
                    depth=depth + 1,
                    max_depth=max_depth,
                    inner_scale_factor=inner_scale_factor
                )

    return traces

# ------------------------------------------------------------
# 3. RENDERING
# ------------------------------------------------------------

fig = go.Figure(
    data=build_recursive_kubbit(
        center=(0,0,0),
        scale=6.0,
        depth=0,
        max_depth=2,          # ← ändra till 3 om du vågar
        inner_scale_factor=0.48
    )
)

fig.update_layout(
    title="RP9 — Rekursiv Kubbit (8ⁿ moduler, skalbar)",
    scene=dict(
        aspectmode="cube",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        camera=dict(eye=dict(x=2.4, y=2.4, z=2.4))
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

fig.show()

# ------------------------------------------------------------
# 4. SPARA
# ------------------------------------------------------------

html_file = "rp9_rekursiv_kubbit.html"
fig.write_html(html_file, include_plotlyjs="cdn", auto_open=True)

try:
    fig.write_image("rp9_rekursiv_kubbit.png", width=2400, height=2400, scale=2)
except:
    pass

print("KLART — rekursiv kubbit renderad.")
