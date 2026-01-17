import numpy as np
import plotly.graph_objects as go
import os, webbrowser

# ==========================================================
# 1. Parametrar för systemfält och observatörsfält
# ==========================================================
theta = np.linspace(0, 4*np.pi, 800)  # två varv
r = 0.6 + 0.1*np.sin(3*theta)

# Systemfält (stationär våg)
x_sys = np.linspace(-2, 2, 800)
y_sys = np.zeros_like(x_sys)
z_sys = np.sin(2*np.pi*x_sys)

# Observatörsfält (spiraliserad våg)
x_obs = r * np.cos(theta)
y_obs = r * np.sin(theta)
z_obs = np.sin(theta) + 0.5*np.cos(2*theta)

# Interferens (koherenslinje)
n = len(theta)
x_int = (x_sys[:n] + x_obs) / 2
y_int = (y_sys[:n] + y_obs) / 2
z_int = (z_sys[:n] + z_obs) / 2

# ==========================================================
# 2. Transparent sfär — den dynamiska domänen
# ==========================================================
phi = np.linspace(0, np.pi, 50)
psi = np.linspace(0, 2*np.pi, 50)
phi, psi = np.meshgrid(phi, psi)
r_sphere = 2.0
x_sphere = r_sphere * np.sin(phi) * np.cos(psi)
y_sphere = r_sphere * np.sin(phi) * np.sin(psi)
z_sphere = r_sphere * np.cos(phi)

# ==========================================================
# 3. Transparent kub — den statiska strukturen
# ==========================================================
a = 4.0  # kubens kantlängd (måste omsluta sfären)
half = a / 2

# kubens hörn
cube_edges = []
for x in [-half, half]:
    for y in [-half, half]:
        cube_edges.append(([x, x], [y, y], [-half, half]))
for x in [-half, half]:
    for z in [-half, half]:
        cube_edges.append(([x, x], [-half, half], [z, z]))
for y in [-half, half]:
    for z in [-half, half]:
        cube_edges.append(([-half, half], [y, y], [z, z]))

# ==========================================================
# 4. Koherenspunkter
# ==========================================================
diff = np.sqrt((x_sys[:n]-x_obs)**2 + (y_sys[:n]-y_obs)**2 + (z_sys[:n]-z_obs)**2)
mask = diff < np.percentile(diff, 0.5)  # topp 0.5% i fasjämvikt
x_coh, y_coh, z_coh = x_int[mask], y_int[mask], z_int[mask]

# ==========================================================
# 5. Bygg 3D-figuren
# ==========================================================
fig = go.Figure()

# --- Transparent kub ---
for edge in cube_edges:
    fig.add_trace(go.Scatter3d(
        x=edge[0], y=edge[1], z=edge[2],
        mode="lines",
        line=dict(color="gray", width=2, dash="dot"),
        name="Kubens gräns"
    ))

# --- Transparent sfär ---
fig.add_trace(go.Surface(
    x=x_sphere, y=y_sphere, z=z_sphere,
    opacity=0.08,
    colorscale=[[0, "lightblue"], [1, "lightblue"]],
    showscale=False,
    name="Sfärisk domän"
))

# --- Systemfält ---
fig.add_trace(go.Scatter3d(
    x=x_sys, y=y_sys, z=z_sys,
    mode="lines",
    line=dict(color="blue", width=4),
    name="Systemfält (stabil struktur)"
))

# --- Observatörsfält ---
fig.add_trace(go.Scatter3d(
    x=x_obs, y=y_obs, z=z_obs,
    mode="lines",
    line=dict(color="red", width=4),
    name="Observatörsfält (expanderande rörelse)"
))

# --- Koherenszon ---
fig.add_trace(go.Scatter3d(
    x=x_int, y=y_int, z=z_int,
    mode="lines",
    line=dict(color="gold", width=6),
    name="Koherenszon (fasjämvikt)"
))

# --- Koherenspunkter ---
fig.add_trace(go.Scatter3d(
    x=x_coh, y=y_coh, z=z_coh,
    mode="markers",
    marker=dict(size=5, color="gold", opacity=0.9),
    name="Hög koherens"
))

# --- Etiketter ---
fig.add_trace(go.Scatter3d(
    x=[0, 1.2, -1.2],
    y=[0, 1.0, -1.0],
    z=[1.2, 0, 0],
    text=["Koherens", "Observatör", "System"],
    mode="text",
    textfont=dict(size=14, color="black"),
    showlegend=False
))

# ==========================================================
# 6. Layout och rotation
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
    title="Kub&sfären — Stabil struktur och oscillerande domän (koherensfält)",
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
    paper_bgcolor="white"
)

# ==========================================================
# 7. Visa, spara, öppna
# ==========================================================
fig.show()
outfile = os.path.abspath("Kub_Sfar_Koherenssystem.html")
fig.write_html(outfile)
webbrowser.open("file://" + outfile)
