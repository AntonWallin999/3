import plotly.graph_objects as go
import numpy as np
import os, webbrowser

# ==========================================================
# 1. PARAMETRAR — Kub & Sfär
# ==========================================================
r = 1.0                           # sfärens radie
n = 60                            # upplösning
theta = np.linspace(0, np.pi, n)
phi = np.linspace(0, 2*np.pi, n)
theta, phi = np.meshgrid(theta, phi)

# Sfärens koordinater
x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

# ==========================================================
# 2. GEOMETRISKA OBJEKT
# ==========================================================

# (A) Sfären – pulserande resonansfält
sphere = go.Surface(
    x=x, y=y, z=z,
    surfacecolor=np.sin(3*theta)*np.cos(3*phi),
    colorscale="Rainbow",
    opacity=0.7,
    showscale=False,
    name="Sfär (resonansfält)"
)

# (B) Kubens linjer (stabil struktur)
cube_lines = []
for s in [-1, 1]:
    for axis in range(3):
        v = np.array([[s if i == axis else c for i in range(3)] 
                      for c in np.linspace(-1, 1, 2)])
        cube_lines.append(go.Scatter3d(
            x=v[:,0], y=v[:,1], z=v[:,2],
            mode="lines",
            line=dict(color="black", width=3),
            showlegend=False
        ))

# (C) Tre cirkelplan (XY, XZ, YZ)
t = np.linspace(0, 2*np.pi, 200)
circles = []
planes = [('XY', [np.cos(t), np.sin(t), np.zeros_like(t)], "red"),
          ('XZ', [np.cos(t), np.zeros_like(t), np.sin(t)], "green"),
          ('YZ', [np.zeros_like(t), np.cos(t), np.sin(t)], "blue")]
for name, coords, color in planes:
    circles.append(go.Scatter3d(
        x=coords[0], y=coords[1], z=coords[2],
        mode="lines",
        line=dict(color=color, width=4, dash="solid"),
        name=f"Cirkeln {name}"
    ))

# ==========================================================
# 3. KOMBINATION & ANIMATION
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

# ==========================================================
# 4. LAYOUT & INTERAKTION
# ==========================================================
fig = go.Figure(data=[sphere] + cube_lines + circles)
fig.frames = frames

fig.update_layout(
    title="🧩 Kub & Sfär — Koherent Fältvisualisering",
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode="cube"
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
    paper_bgcolor="white",
    showlegend=True
)

# ==========================================================
# 5. VISA, SPARA, ÖPPNA
# ==========================================================
fig.show()
outfile = os.path.abspath("Coherent_Field_Visualizer.html")
fig.write_html(outfile)
webbrowser.open("file://" + outfile)