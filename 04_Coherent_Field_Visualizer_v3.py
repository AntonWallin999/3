import plotly.graph_objects as go
import numpy as np
import os, webbrowser

# ==========================================================
# 1. Parametrar
# ==========================================================
phi_const = 1.61803398875
r0, amp = 1.0, 0.35
n = 80
theta = np.linspace(0, np.pi, n)
phi = np.linspace(0, 2*np.pi, n)
theta, phi = np.meshgrid(theta, phi)
x0 = np.sin(theta) * np.cos(phi)
y0 = np.sin(theta) * np.sin(phi)
z0 = np.cos(theta)

# ==========================================================
# 2. Hjälpfunktioner
# ==========================================================
def line(a, b, color="black", width=3):
    return go.Scatter3d(
        x=[a[0], b[0]], y=[a[1], b[1]], z=[a[2], b[2]],
        mode="lines", line=dict(color=color, width=width),
        showlegend=False
    )

# ==========================================================
# 3. Statiska objekt
# ==========================================================
cube = []
for s in [-1, 1]:
    for axis in range(3):
        v = np.array([[s if i == axis else c for i in range(3)]
                      for c in np.linspace(-1, 1, 2)])
        cube.append(line(v[0], v[1], "gray", 3))

tetra_up = np.array([[1,1,1],[-1,-1,1],[1,-1,-1],[-1,1,-1]]) * 0.7
tetra_down = np.array([[-1,-1,-1],[1,1,-1],[-1,1,1],[1,-1,1]]) * 0.7
edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
tetra = [line(tetra_up[a], tetra_up[b], "red", 4) for a,b in edges] + \
        [line(tetra_down[a], tetra_down[b], "blue", 4) for a,b in edges]

hex_links = [line(tetra_up[i], tetra_down[(i+1)%4], "gray", 4) for i in range(4)]

plane = go.Surface(
    x=[[-0.8,0.8],[-0.8,0.8]],
    y=[[-0.8,-0.8],[0.8,0.8]],
    z=[[0,0],[0,0]],
    opacity=0.1, colorscale=[[0,"gray"],[1,"gray"]],
    showscale=False
)

# ==========================================================
# 4. Sfär och frames
# ==========================================================
sphere = go.Surface(
    x=r0*x0, y=r0*y0, z=r0*z0,
    surfacecolor=np.sin(3*theta)*np.cos(3*phi),
    colorscale="Rainbow", opacity=0.6, showscale=False,
    name="Sfär (puls)"
)

frames = []
steps = 80
for k in range(steps):
    t = k / steps * 2*np.pi
    r = r0 * (1 + amp * np.sin(t * phi_const))
    frames.append(go.Frame(
        name=str(k),
        data=[go.Surface(
            x=r*x0, y=r*y0, z=r*z0,
            surfacecolor=np.sin(3*theta+t)*np.cos(3*phi-t),
            colorscale="Rainbow", opacity=0.6, showscale=False
        )],
        traces=[0],   # <—— Uppdatera trace 0 (sfären)
        layout=dict(scene_camera=dict(
            eye=dict(x=2*np.cos(t), y=2*np.sin(t), z=1.2)
        ))
    ))

# ==========================================================
# 5. Figur och animation
# ==========================================================
fig = go.Figure(
    data=[sphere] + cube + tetra + hex_links + [plane],
    frames=frames
)

fig.update_layout(
    template=None,
    title="🌐 Kub & Sfär — Pulsande merkaba i koherent fält",
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
             "args": [None, {"frame": {"duration":80, "redraw":True},
                             "fromcurrent":True, "mode":"immediate"}]},
            {"label": "⏸ Pausa", "method": "animate",
             "args": [[None], {"frame": {"duration":0}, "mode":"immediate"}]}
        ],
        "x": 0.05, "y": 0.02
    }],
    paper_bgcolor="white",
    showlegend=False
)

# ==========================================================
# 6. Visa, spara, öppna
# ==========================================================
fig.show()
outfile = os.path.abspath("Coherent_Field_Visualizer_v4_fixed.html")
fig.write_html(outfile)
webbrowser.open("file://" + outfile)
