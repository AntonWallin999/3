import plotly.graph_objects as go
import numpy as np
import os, webbrowser

# ==========================================================
# 1. PARAMETRAR — Gyllene puls
# ==========================================================
phi = 1.61803398875           # gyllene snittet
r0 = 1.0                      # grundradie
n = 60                        # upplösning
theta = np.linspace(0, np.pi, n)
phi_ang = np.linspace(0, 2*np.pi, n)
theta, phi_ang = np.meshgrid(theta, phi_ang)

# Grundkoordinater (enhets-sfär)
x0 = np.sin(theta) * np.cos(phi_ang)
y0 = np.sin(theta) * np.sin(phi_ang)
z0 = np.cos(theta)

# ==========================================================
# 2. SKAPA ANIMERADE FRAMES — pulserande och roterande
# ==========================================================
frames = []
steps = 60
for k in range(steps):
    # Pulsens fas: gyllene spiral (log-periodisk)
    t = k / steps * 2*np.pi
    r = r0 * (1 + 0.25 * np.sin(t * phi))
    x = r * x0
    y = r * y0
    z = r * z0

    frames.append(go.Frame(
        data=[go.Surface(
            x=x, y=y, z=z,
            surfacecolor=np.sin(3*theta + t) * np.cos(3*phi_ang - t),
            colorscale="Rainbow",
            opacity=0.7,
            showscale=False
        )],
        layout=dict(
            scene_camera=dict(
                eye=dict(
                    x=2*np.cos(t),
                    y=2*np.sin(t),
                    z=1.2
                )
            )
        )
    ))

# ==========================================================
# 3. STATISKA OBJEKT — kub och cirklar
# ==========================================================
cube_lines = []
for s in [-1, 1]:
    for axis in range(3):
        v = np.array([[s if i == axis else c for i in range(3)]
                      for c in np.linspace(-1, 1, 2)])
        cube_lines.append(go.Scatter3d(
            x=v[:, 0], y=v[:, 1], z=v[:, 2],
            mode="lines",
            line=dict(color="black", width=3),
            showlegend=False
        ))

t = np.linspace(0, 2*np.pi, 200)
circles = [
    go.Scatter3d(x=np.cos(t), y=np.sin(t), z=np.zeros_like(t),
                 mode="lines", line=dict(color="red", width=3),
                 name="XY-plan"),
    go.Scatter3d(x=np.cos(t), y=np.zeros_like(t), z=np.sin(t),
                 mode="lines", line=dict(color="green", width=3),
                 name="XZ-plan"),
    go.Scatter3d(x=np.zeros_like(t), y=np.cos(t), z=np.sin(t),
                 mode="lines", line=dict(color="blue", width=3),
                 name="YZ-plan")
]

# ==========================================================
# 4. INITIAL-FIGUR (första fasen)
# ==========================================================
r_init = r0
x_init = r_init * x0
y_init = r_init * y0
z_init = r_init * z0
sphere_init = go.Surface(
    x=x_init, y=y_init, z=z_init,
    surfacecolor=np.sin(3*theta) * np.cos(3*phi_ang),
    colorscale="Rainbow", opacity=0.7, showscale=False,
    name="Sfär (resonansfält)"
)

# ==========================================================
# 5. LAYOUT & ANIMATION
# ==========================================================
fig = go.Figure(
    data=[sphere_init] + cube_lines + circles,
    frames=frames
)

fig.update_layout(
    title="🌀 Kub & Sfär v2 — Pulsande gyllene resonans",
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode="cube"
    ),
    updatemenus=[{
        "type": "buttons",
        "buttons": [
            {"label": "▶ Starta puls", "method": "animate",
             "args": [None, {"frame": {"duration": 80, "redraw": True},
                             "fromcurrent": True, "mode": "immediate"}]},
            {"label": "⏸ Pausa", "method": "animate",
             "args": [[None], {"frame": {"duration": 0},
                               "mode": "immediate"}]}
        ],
        "x": 0.05, "y": 0
    }],
    paper_bgcolor="white",
    showlegend=True
)

# ==========================================================
# 6. VISA, SPARA, ÖPPNA
# ==========================================================
fig.show()
outfile = os.path.abspath("Coherent_Field_Visualizer_v2.html")
fig.write_html(outfile)
webbrowser.open("file://" + outfile)