# -*- coding: utf-8 -*-
# ==========================================================
# 10D_Fractal_Resonance_Network_Interactive.py
# Co-Creators Foundation © 2025
# Dynamiskt, interaktivt fraktalt resonansnätverk (RP9)
# ==========================================================

import numpy as np
import plotly.graph_objects as go
import os, webbrowser

# ----------------------------------------------------------
# 1. Grundparametrar
# ----------------------------------------------------------
phi = 1.5       # exakt RP9-konstant (inte approximation)
kappa = 0.08    # återkopplingskoefficient
nodes = 60      # antal noder
frames = 120    # antal frames i animation
dt = 0.05       # tidssteg

np.random.seed(42)

# ----------------------------------------------------------
# 2. Initiering av positioner och faser
# ----------------------------------------------------------
angles = np.linspace(0, 2*np.pi, nodes, endpoint=False)
radii = (1 / phi) ** (np.arange(nodes) / 10)
x = radii * np.cos(angles)
y = radii * np.sin(angles)
z = np.sin(angles * phi) * 0.5
positions = np.stack((x, y, z), axis=1)

# Initial fas
phases = np.random.uniform(0, 2*np.pi, nodes)

# ----------------------------------------------------------
# 3. Kopplingsmatris
# ----------------------------------------------------------
dist = np.linalg.norm(positions[:, None, :] - positions[None, :, :], axis=-1)
dist += np.eye(nodes)
coupling_matrix = np.exp(-phi * dist)
np.fill_diagonal(coupling_matrix, 0)
coupling_matrix /= coupling_matrix.max()

# ----------------------------------------------------------
# 4. Dynamisk uppdatering
# ----------------------------------------------------------
def update_phases(phases, dt):
    dphi = np.zeros_like(phases)
    for i in range(nodes):
        diff = np.sin(phases - phases[i])
        dphi[i] = np.sum(coupling_matrix[i] * diff)
    dphi -= kappa * phases
    return phases + dphi * dt

# ----------------------------------------------------------
# 5. Generera data över tid (ändra även z något)
# ----------------------------------------------------------
frames_data = []
ph = phases.copy()
for t in range(frames):
    ph = update_phases(ph, dt)
    c = np.cos(ph)
    z_dynamic = z + 0.2 * np.sin(ph * phi)
    frames_data.append((x, y, z_dynamic, c))

# ----------------------------------------------------------
# 6. Skapa Plotly-figuren
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
    line=dict(color='rgba(100,100,255,0.2)', width=1),
    hoverinfo='none',
    name='Kopplingar'
))

# Startnoder
x0, y0, z0, c0 = frames_data[0]
nodes_trace = go.Scatter3d(
    x=x0, y=y0, z=z0,
    mode='markers',
    marker=dict(size=6, color=c0, colorscale='Turbo', opacity=0.9),
    name='Noder'
)
fig.add_trace(nodes_trace)

# ----------------------------------------------------------
# 7. Bygg animation frames
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
# 8. Layout & animationkontroller
# ----------------------------------------------------------
fig.update_layout(
    title="🔗 Fraktalt Resonansnätverk — Interaktiv självkalibrering (RP9)",
    template='plotly_dark',
    scene=dict(
        xaxis=dict(title='X', backgroundcolor='black'),
        yaxis=dict(title='Y', backgroundcolor='black'),
        zaxis=dict(title='Z', backgroundcolor='black'),
        aspectmode='cube'
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
# 9. Export och öppning
# ----------------------------------------------------------
out_path = os.path.abspath("Fractal_Resonance_Network_Interactive.html")
fig.write_html(out_path, include_plotlyjs="cdn", auto_open=True)
fig.show()
webbrowser.open("file://" + out_path)

print("\n[OK] Interaktiv fraktal-resonans skapad och öppnad i webbläsare.")
input("\nTryck [ENTER] för att avsluta...")
