import plotly.graph_objects as go
import numpy as np
import os, webbrowser

# ==========================================================
# 1. Parametrar — Gyllene helix (vertikal struktur)
# ==========================================================
phi = 1.61803398875                # Gyllene snittet
theta = np.linspace(0, 6*np.pi, 900)  # tre varv
r0 = 0.2                           # start-radie
r = r0 * phi**(theta / (2*np.pi))  # logaritmisk expansion (φ per varv)

# 45° lutning – stigning proportionell mot radien
z = r * np.tan(np.deg2rad(45))

# Kartesiska koordinater
x = r * np.cos(theta)
y = r * np.sin(theta)

# Roterar spiralen 90° så att början (blå) ligger direkt under slutet (grön)
x_rot = x * np.cos(np.pi/2) - y * np.sin(np.pi/2)
y_rot = x * np.sin(np.pi/2) + y * np.cos(np.pi/2)
x, y = x_rot, y_rot

# ==========================================================
# 2. Noder — var 0.5 varv + början + slut = 7 noder
# ==========================================================
# Värden (i radianer): 0, 0.5π, 1.0π, 1.5π, 2.0π, 2.5π, 3.0π
node_angles = np.arange(0, 6.5*np.pi, np.pi)  # inkluderar 0 och 6π
r_nodes = r0 * phi**(node_angles / (2*np.pi))
x_nodes = r_nodes * np.cos(node_angles + np.pi/2)
y_nodes = r_nodes * np.sin(node_angles + np.pi/2)
z_nodes = r_nodes * np.tan(np.deg2rad(45))

node_labels = ["Start", "0.5 varv", "1.0 varv", "1.5 varv",
               "2.0 varv", "2.5 varv", "Slut"]

node_colors = ["blue", "gold", "gold", "gold", "gold", "gold", "green"]

# ==========================================================
# 3. Skapa figur
# ==========================================================
fig = go.Figure()

# Huvudspiralen (röd linje)
fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode="lines",
    line=dict(color="crimson", width=6),
    name="Gyllene helix (√π-rörelse)"
))

# Noder (7 st)
for i in range(len(node_angles)):
    fig.add_trace(go.Scatter3d(
        x=[x_nodes[i]], y=[y_nodes[i]], z=[z_nodes[i]],
        mode="markers+text",
        text=[node_labels[i]],
        textposition="top center",
        marker=dict(size=7, color=node_colors[i]),
        name=f"Nod {node_labels[i]}"
    ))

# ==========================================================
# 4. Referensplan (för geometrisk balans)
# ==========================================================
plane = np.linspace(-1.5, 1.5, 2)
fig.add_trace(go.Surface(
    x=[[p for p in plane]*2],
    y=[plane, plane],
    z=[[0, 0], [0, 0]],
    opacity=0.1,
    showscale=False,
    colorscale=[[0, "lightgray"], [1, "lightgray"]],
    name="Referensplan"
))

# ==========================================================
# 5. Animation — rotation runt Z-axeln
# ==========================================================
frames = []
for angle in np.linspace(0, 360, 60):
    frames.append(go.Frame(layout=dict(
        scene_camera=dict(
            eye=dict(x=2*np.cos(np.radians(angle)),
                     y=2*np.sin(np.radians(angle)),
                     z=1.2)
        )
    )))
fig.frames = frames

# ==========================================================
# 6. Layoutinställningar
# ==========================================================
fig.update_layout(
    title="Gyllene Helix — 3 varv, φ-expansion, 45° lutning, 7 noder (Start–Slut)",
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode="data"
    ),
    updatemenus=[{
        "type": "buttons",
        "buttons": [
            {"label": "▶ Rotera", "method": "animate",
             "args": [None, {"frame": {"duration": 80, "redraw": True},
                             "fromcurrent": True, "mode": "immediate"}]},
            {"label": "⏸ Pausa", "method": "animate",
             "args": [[None], {"frame": {"duration": 0}, "mode": "immediate"}]}
        ],
        "x": 0.05, "y": 0
    }],
    showlegend=True,
    paper_bgcolor="white",
    plot_bgcolor="white"
)

# ==========================================================
# 7. Visa, spara, öppna
# ==========================================================
fig.show()
outfile = os.path.abspath("Gyllene_Helix_7noder.html")
fig.write_html(outfile)
webbrowser.open("file://" + outfile)
