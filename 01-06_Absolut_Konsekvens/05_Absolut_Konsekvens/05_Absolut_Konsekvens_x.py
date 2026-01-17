# -*- coding: utf-8 -*-
# ==========================================================
# 05_Absolut_Konsekvens_Interactive.py
# Co-Creators Foundation © 2025
# Dynamiskt fraktalt resonansnätverk (RP9) – interaktiv version
# ==========================================================

import numpy as np
import plotly.graph_objects as go
import os, webbrowser

# ----------------------------------------------------------
# 1. Grundkonstanter
# ----------------------------------------------------------
phi = 1.5       # exakt RP9-konstant (avsiktligt konstant enligt modellen)
kappa = 0.08    # återkopplingskoefficient
nodes = 60      # antal noder
frames = 120    # antal frames i animation
dt = 0.05       # tidssteg

np.random.seed(42)

# ----------------------------------------------------------
# 2. Initiera noder i ett 3D-fraktalt fält
# ----------------------------------------------------------
angles = np.linspace(0, 2*np.pi, nodes, endpoint=False)
radii = (1 / phi) ** (np.arange(nodes) / 10)
x = radii * np.cos(angles)
y = radii * np.sin(angles)
z = np.sin(angles * phi) * 0.5
positions = np.stack((x, y, z), axis=1)

# ----------------------------------------------------------
# 3. Skapa kopplingsmatris (resonansnät)
# ----------------------------------------------------------
dist = np.linalg.norm(positions[:, None, :] - positions[None, :, :], axis=-1)
dist += np.eye(nodes)
coupling_matrix = np.exp(-phi * dist)
np.fill_diagonal(coupling_matrix, 0)
coupling_matrix /= coupling_matrix.max()

# ----------------------------------------------------------
# 4. Initiera fasrörelse
# ----------------------------------------------------------
phases = np.random.uniform(0, 2*np.pi, nodes)

def update_phases(phases, dt):
    dphi = np.zeros_like(phases)
    for i in range(nodes):
        diff = np.sin(phases - phases[i])
        dphi[i] = np.sum(coupling_matrix[i] * diff)
    dphi -= kappa * phases
    return phases + dphi * dt

# ----------------------------------------------------------
# 5. Generera tidsutveckling
# ----------------------------------------------------------
frames_data = []
ph = phases.copy()
for t in range(frames):
    ph = update_phases(ph, dt)
    color = np.cos(ph)
    z_dynamic = z + 0.2 * np.sin(ph * phi)
    frames_data.append((x, y, z_dynamic, color))

# ----------------------------------------------------------
# 6. Skapa 3D-visualisering
# ----------------------------------------------------------
fig = go.Figure()

# Kopplingar (edges)
edges_x, edges_y, edges_z = [], [], []
for i in range(nodes):
    for j in range(i+1, nodes):
        if coupling_matrix[i, j] > 0.5:
            edges_x += [x[i], x[j], None]
            edges_y += [y[i], y[j], None]
            edges_z += [z[i], z[j], None]

fig.add_trace(go.Scatter3d(
    x=edges_x, y=edges_y, z=edges_z,
    mode='lines',
    line=dict(color='rgba(100,100,255,0.25)', width=1),
    hoverinfo='none',
    name='Kopplingar'
))

# Startpunkter
x0, y0, z0, c0 = frames_data[0]
nodes_trace = go.Scatter3d(
    x=x0, y=y0, z=z0,
    mode='markers',
    marker=dict(size=6, color=c0, colorscale='Turbo', opacity=0.9),
    name='Noder'
)
fig.add_trace(nodes_trace)

# ----------------------------------------------------------
# 7. Skapa animation frames
# ----------------------------------------------------------
fig.frames = [
    go.Frame(
        data=[go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(size=6, color=c, colorscale='Turbo', opacity=0.9)
        )],
        name=f"frame{t}"
    )
    for t, (x, y, z, c) in enumerate(frames_data)
]

# ----------------------------------------------------------
# 8. Layout & interaktiv kontroll
# ----------------------------------------------------------
fig.update_layout(
    title="🔗 Fraktalt Resonansnätverk — Absolut Konsekvens (RP9)",
    template='plotly_dark',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='cube',
        bgcolor='black'
    ),
    updatemenus=[{
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 80, "redraw": True},
                                "fromcurrent": True,
                                "transition": {"duration": 0}}],
                "label": "▶ Start",
                "method": "animate"
            },
            {
                "args": [[None], {"frame": {"duration": 0}, "mode": "immediate"}],
                "label": "⏸ Stop",
                "method": "animate"
            }
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 87},
        "showactive": True,
        "type": "buttons",
        "x": 0.1,
        "xanchor": "right",
        "y": 0,
        "yanchor": "top"
    }]
)

# ----------------------------------------------------------
# 9. Export & öppning
# ----------------------------------------------------------
out_path = os.path.abspath("Fractal_Resonance_Absolut_Konsekvens.html")
fig.write_html(out_path, include_plotlyjs="cdn", auto_open=True)
fig.show()
webbrowser.open("file://" + out_path)

print("\n[OK] Interaktiv visualisering skapad.")
print("Filen finns sparad i:", out_path)
input("\nTryck [ENTER] för att avsluta sessionen...")