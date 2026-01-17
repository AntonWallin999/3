import plotly.graph_objects as go
import numpy as np
import os, webbrowser

# ==========================================================
# 1. GRUNDGEOMETRI – SFÄR, KUB, PARAMETRAR
# ==========================================================
phi_const = 1.61803398875
r0 = 1.0
n = 60
theta = np.linspace(0, np.pi, n)
phi = np.linspace(0, 2*np.pi, n)
theta, phi = np.meshgrid(theta, phi)

x_s = r0 * np.sin(theta) * np.cos(phi)
y_s = r0 * np.sin(theta) * np.sin(phi)
z_s = r0 * np.cos(theta)

sphere = go.Surface(
    x=x_s, y=y_s, z=z_s,
    surfacecolor=np.sin(3*theta)*np.cos(3*phi),
    colorscale="Rainbow", opacity=0.6,
    showscale=False, name="Sfär (resonansfält)"
)

# ==========================================================
# 2. KUB (svarta kanter)
# ==========================================================
cube_lines = []
for s in [-1, 1]:
    for axis in range(3):
        v = np.array([[s if i == axis else c for i in range(3)]
                      for c in np.linspace(-1, 1, 2)])
        cube_lines.append(go.Scatter3d(
            x=v[:,0], y=v[:,1], z=v[:,2],
            mode="lines", line=dict(color="black", width=3),
            showlegend=False
        ))

# ==========================================================
# 3. TRE CIRKLAR (XY, XZ, YZ)
# ==========================================================
t = np.linspace(0, 2*np.pi, 200)
circles = [
    go.Scatter3d(x=np.cos(t), y=np.sin(t), z=np.zeros_like(t),
                 mode="lines", line=dict(color="red", width=2),
                 name="XY-plan"),
    go.Scatter3d(x=np.cos(t), y=np.zeros_like(t), z=np.sin(t),
                 mode="lines", line=dict(color="green", width=2),
                 name="XZ-plan"),
    go.Scatter3d(x=np.zeros_like(t), y=np.cos(t), z=np.sin(t),
                 mode="lines", line=dict(color="blue", width=2),
                 name="YZ-plan")
]

# ==========================================================
# 4. DUBBEL-TETRAEDER (merkaba)
# ==========================================================
# Koordinater för två motsatta tetraedrar
tetra_up = np.array([
    [1, 1, 1],
    [-1, -1, 1],
    [1, -1, -1],
    [-1, 1, -1]
]) * 0.7

tetra_down = np.array([
    [-1, -1, -1],
    [1, 1, -1],
    [-1, 1, 1],
    [1, -1, 1]
]) * 0.7

# Kantsamband för tetraeder
edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def tetra_traces(points, color):
    traces = []
    for e in edges:
        a,b = points[e[0]], points[e[1]]
        traces.append(go.Scatter3d(
            x=[a[0], b[0]], y=[a[1], b[1]], z=[a[2], b[2]],
            mode="lines", line=dict(color=color, width=4),
            showlegend=False
        ))
    return traces

tetra_up_traces = tetra_traces(tetra_up, "rgba(255,0,0,0.9)")      # röd
tetra_down_traces = tetra_traces(tetra_down, "rgba(0,0,255,0.9)")  # blå

# ==========================================================
# 5. HEXAGONLÄNKAR – varannan nod kopplas
# ==========================================================
links = [(0,1),(1,2),(2,3),(3,0),(0,2),(1,3)]
hex_links = []
for i in range(4):
    a = tetra_up[i]
    b = tetra_down[(i+1)%4]
    hex_links.append(go.Scatter3d(
        x=[a[0], b[0]], y=[a[1], b[1]], z=[a[2], b[2]],
        mode="lines", line=dict(color="gray", width=5),
        name="Hex-länk" if i==0 else None
    ))

# ==========================================================
# 6. MITTPLAN – genomskinlig hex-yta
# ==========================================================
hex_plane = go.Surface(
    x=[[x for x in np.linspace(-0.8,0.8,2)]*2],
    y=[[-0.8,0.8],[-0.8,0.8]],
    z=[[0,0],[0,0]],
    opacity=0.1,
    showscale=False,
    colorscale=[[0,"gray"],[1,"gray"]],
    name="Hex-plan"
)

# ==========================================================
# 7. SAMMANSTÄLLNING
# ==========================================================
fig = go.Figure(
    data=[sphere] + cube_lines + circles +
         tetra_up_traces + tetra_down_traces +
         hex_links + [hex_plane]
)

# ==========================================================
# 8. KAMERA & INTERAKTION
# ==========================================================
frames = []
for angle in np.linspace(0, 360, 60):
    frames.append(go.Frame(layout=dict(
        scene_camera=dict(
            eye=dict(
                x=2*np.cos(np.radians(angle)),
                y=2*np.sin(np.radians(angle)),
                z=1.2)
        )
    )))
fig.frames = frames

fig.update_layout(
    title="🔺 Kub & Sfär v3 — Dubbel-Tetraeder med Hexagonlänkar",
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
             "args": [[None], {"frame": {"duration": 0},
                               "mode": "immediate"}]}
        ],
        "x": 0.05, "y": 0
    }],
    paper_bgcolor="white",
    showlegend=True
)

# ==========================================================
# 9. VISA, SPARA, ÖPPNA
# ==========================================================
fig.show()
outfile = os.path.abspath("Coherent_Field_Visualizer_v3.html")
fig.write_html(outfile)
webbrowser.open("file://" + outfile)