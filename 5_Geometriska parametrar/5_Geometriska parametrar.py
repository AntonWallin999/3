import plotly.graph_objects as go
from plotly.subplots import make_subplots  # ← viktigt tillägg
import numpy as np
import os
import webbrowser

# ==========================================================
# Gemensam geometri
# ==========================================================
theta = np.linspace(0, 3*np.pi, 200)     # 1.5 varv
r = 0.6
x = r * np.cos(theta)
y = r * np.sin(theta)
z = np.sin(theta * 0.75) * 1.2           # vertikal puls
trail_color = "red"

# ==========================================================
# (1) Multi-panel-vy
# ==========================================================
fig1 = make_subplots(
    rows=1, cols=3,
    specs=[[{"type": "scatter3d"}, {"type": "scatter3d"}, {"type": "scatter3d"}]],
    column_widths=[0.33, 0.34, 0.33],
    subplot_titles=("2D-projektion – Våg", "3D-Spiral – Rörelse", "Top-down – Kors")
)

# Vänster – XZ-projektion (Y≈0)
fig1.add_trace(go.Scatter3d(
    x=x, y=[0]*len(x), z=z,
    mode="lines",
    line=dict(color=trail_color, width=4)
), row=1, col=1)

# Mitten – full spiral
fig1.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode="lines",
    line=dict(color=trail_color, width=4)
), row=1, col=2)

# Höger – top-down (XY)
fig1.add_trace(go.Scatter3d(
    x=x, y=y, z=[0]*len(x),
    mode="lines",
    line=dict(color=trail_color, width=4)
), row=1, col=3)

# Döljer axlar och justerar perspektiv
for i in range(1, 4):
    fig1.update_scenes(
        dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            aspectmode="data"
        ),
        row=1, col=i
    )

fig1.update_layout(
    title="Rot √π – Samma rörelse sedd ur tre perspektiv",
    showlegend=False,
    height=600,
    paper_bgcolor="white"
)

# Visa och spara
fig1.show()
html1 = os.path.abspath("Rot_sqrtPi_Multipanel.html")
fig1.write_html(html1)
webbrowser.open("file://" + html1)

# ==========================================================
# (2) Interaktiv 3D-vy
# ==========================================================
fig2 = go.Figure()

# Spiral
fig2.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode="lines",
    line=dict(color=trail_color, width=5),
    name="√π-rörelse"
))

# Basplan som referens
plane = np.linspace(-1, 1, 2)
fig2.add_trace(go.Surface(
    x=[[p for p in plane]*2],
    y=[plane, plane],
    z=[[0, 0], [0, 0]],
    opacity=0.1,
    showscale=False,
    colorscale=[[0, "lightgray"], [1, "lightgray"]],
    name="Referensplan"
))

# Förinställda kameror
camera_wave   = dict(eye=dict(x=2,   y=0.01, z=0.5))
camera_spiral = dict(eye=dict(x=1.8, y=1.8,  z=1.2))
camera_cross  = dict(eye=dict(x=0,   y=2.5,  z=0.1))

fig2.update_layout(
    title="Rot √π – Interaktiv 3D-vy (våg / spiral / kors)",
    scene=dict(
        aspectmode="data",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False)
    ),
    updatemenus=[{
        "type": "buttons",
        "buttons": [
            {"label": "Vågvy",    "method": "relayout", "args": [{"scene.camera": camera_wave}]},
            {"label": "Spiralvy", "method": "relayout", "args": [{"scene.camera": camera_spiral}]},
            {"label": "Korsvy",   "method": "relayout", "args": [{"scene.camera": camera_cross}]}
        ],
        "x": 0.02, "y": 0
    }],
    paper_bgcolor="white"
)

# Visa och spara
fig2.show()
html2 = os.path.abspath("Rot_sqrtPi_Interaktiv.html")
fig2.write_html(html2)
webbrowser.open("file://" + html2)
