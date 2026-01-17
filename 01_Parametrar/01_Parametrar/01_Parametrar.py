import numpy as np
import plotly.graph_objects as go
import os, webbrowser

# ==========================================================
# 1. Parametrar
# ==========================================================
theta = np.linspace(0, 4*np.pi, 800)     # två varv
r = 0.6 + 0.1*np.sin(3*theta)            # liten modulering

# Systemfält (stationär sinusvåg)
x_sys = np.linspace(-2, 2, 800)
y_sys = np.zeros_like(x_sys)
z_sys = np.sin(2*np.pi*x_sys)

# Observatörsfält (spiraliserad våg)
x_obs = r * np.cos(theta)
y_obs = r * np.sin(theta)
z_obs = np.sin(theta) + 0.5*np.cos(2*theta)

# Interferenszon (där vågorna korsar varandra)
n = len(theta)
x_int = (x_sys[:n] + x_obs) / 2
y_int = (y_sys[:n] + y_obs) / 2
z_int = (z_sys[:n] + z_obs) / 2

# ==========================================================
# 2. Figur
# ==========================================================
fig = go.Figure()

# Systemfält
fig.add_trace(go.Scatter3d(
    x=x_sys, y=y_sys, z=z_sys,
    mode="lines",
    line=dict(color="blue", width=4),
    name="Systemfält (stabil struktur)"
))

# Observatörsfält
fig.add_trace(go.Scatter3d(
    x=x_obs, y=y_obs, z=z_obs,
    mode="lines",
    line=dict(color="red", width=4),
    name="Observatörsfält (expanderande rörelse)"
))

# Interferenszon
fig.add_trace(go.Scatter3d(
    x=x_int, y=y_int, z=z_int,
    mode="lines",
    line=dict(color="gold", width=6),
    name="Koherenszon (fasjämvikt)"
))

# Etiketter (centrala punkter)
fig.add_trace(go.Scatter3d(
    x=[0, 1.0, -1.0],
    y=[0, 0.8, -0.8],
    z=[0.8, 0, 0],
    text=["Koherens", "Observatör", "System"],
    mode="text",
    textfont=dict(size=14, color="black"),
    showlegend=False
))

# ==========================================================
# 3. Layout och rotation
# ==========================================================
frames = []
for angle in np.linspace(0, 360, 90):
    frames.append(go.Frame(layout=dict(
        scene_camera=dict(
            eye=dict(x=2*np.cos(np.radians(angle)),
                     y=2*np.sin(np.radians(angle)),
                     z=1.2)
        )
    )))
fig.frames = frames

fig.update_layout(
    title="Interferens mellan systemfält och observatörsfält — koherens i rörelse",
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
             "args": [[None], {"frame": {"duration": 0},
                               "mode": "immediate"}]}
        ],
        "x": 0.05, "y": 0
    }],
    showlegend=True,
    paper_bgcolor="white"
)

# ==========================================================
# 4. Visa, spara och öppna
# ==========================================================
fig.show()
outfile = os.path.abspath("Interferens_System_Observator.html")
fig.write_html(outfile)
webbrowser.open("file://" + outfile)