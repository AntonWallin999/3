import plotly.graph_objects as go
import numpy as np
import os, webbrowser

# ==========================================================
# 1. Parametrar — Gyllene helix med färggradient
# ==========================================================
phi = 1.61803398875
theta = np.linspace(0, 6*np.pi, 900)      # tre varv
r0 = 0.2
r = r0 * phi**(theta / (2*np.pi))         # φ-expansion per varv
z = r * np.tan(np.deg2rad(45))            # 45° lutning

x = r * np.cos(theta)
y = r * np.sin(theta)

# Rotera 90° så att starten (röd) ligger direkt under slutet (violett)
x_rot = x * np.cos(np.pi/2) - y * np.sin(np.pi/2)
y_rot = x * np.sin(np.pi/2) + y * np.cos(np.pi/2)
x, y = x_rot, y_rot

# ==========================================================
# 2. Färggradient längs helixen (röd → violett)
# ==========================================================
def color_gradient(value):
    # Regnbågens sju färger i RGB
    colors = [
        (255, 0, 0),       # röd
        (255, 127, 0),     # orange
        (255, 255, 0),     # gul
        (0, 255, 0),       # grön
        (0, 0, 255),       # blå
        (75, 0, 130),      # indigo
        (148, 0, 211)      # violett
    ]
    steps = len(colors) - 1
    i = int(value * steps)
    f = value * steps - i
    if i >= steps:
        i = steps - 1
    c1, c2 = colors[i], colors[i + 1]
    rgb = [int(c1[j] + (c2[j] - c1[j]) * f) for j in range(3)]
    return f'rgb({rgb[0]},{rgb[1]},{rgb[2]})'

# Färglista längs spiralen
color_values = np.linspace(0, 1, len(theta))
line_colors = [color_gradient(v) for v in color_values]

# ==========================================================
# 3. Noder (sju fasta färger)
# ==========================================================
node_angles = np.arange(0, 6.5*np.pi, np.pi)  # 0 → 3 varv, 0.5-varvssteg
r_nodes = r0 * phi**(node_angles / (2*np.pi))
x_nodes = r_nodes * np.cos(node_angles + np.pi/2)
y_nodes = r_nodes * np.sin(node_angles + np.pi/2)
z_nodes = r_nodes * np.tan(np.deg2rad(45))

node_labels = ["Start", "0.5 varv", "1.0 varv", "1.5 varv",
               "2.0 varv", "2.5 varv", "Slut"]
node_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# ==========================================================
# 4. Bygg 3D-figuren
# ==========================================================
fig = go.Figure()

# Segmentera helixen i små färgade sträckor (gradient)
for i in range(len(theta) - 1):
    fig.add_trace(go.Scatter3d(
        x=x[i:i+2], y=y[i:i+2], z=z[i:i+2],
        mode="lines",
        line=dict(color=line_colors[i], width=6),
        showlegend=False
    ))

# Noder (sju regnbågsfärger)
for i in range(len(node_angles)):
    fig.add_trace(go.Scatter3d(
        x=[x_nodes[i]], y=[y_nodes[i]], z=[z_nodes[i]],
        mode="markers+text",
        text=[node_labels[i]],
        textposition="top center",
        marker=dict(size=8, color=node_colors[i]),
        name=f"Nod {node_labels[i]}"
    ))

# Centerlinje (rak, tunn, streckad)
fig.add_trace(go.Scatter3d(
    x=[x_nodes[0], x_nodes[-1]],
    y=[y_nodes[0], y_nodes[-1]],
    z=[z_nodes[0], z_nodes[-1]],
    mode="lines",
    line=dict(color="gray", width=2, dash="dot"),
    name="Centerlinje (pulsaxel)"
))

# Referensplan (balansplan)
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
# 5. Animation – rotation kring Z-axeln
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
# 6. Layout
# ==========================================================
fig.update_layout(
    title="Gyllene Helix — 3 varv, φ-expansion, 45° lutning, kontinuerlig regnbågsgradient",
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
outfile = os.path.abspath("Gyllene_Helix_RegnbagsGradient.html")
fig.write_html(outfile)
webbrowser.open("file://" + outfile)
