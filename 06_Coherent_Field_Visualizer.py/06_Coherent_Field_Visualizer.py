import plotly.graph_objects as go
import numpy as np
import os, webbrowser

# ==========================================================
# 1) PARAMETRAR – Holografisk fasinterferens
# ==========================================================
phi_const = 1.61803398875       # Gyllene snittets konstant
r0, amp = 1.0, 0.28             # Radie och pulsamplitud
n = 70                          # Optimerad upplösning (snabbare men bibehållen detalj)
theta = np.linspace(0, np.pi, n)
phi = np.linspace(0, 2*np.pi, n)
theta, phi = np.meshgrid(theta, phi)

# Basytan
x0 = np.sin(theta) * np.cos(phi)
y0 = np.sin(theta) * np.sin(phi)
z0 = np.cos(theta)

# ==========================================================
# 2) FAST GEOMETRI – Kub, Tetraedrar, Hex-länkar
# ==========================================================
def line(a, b, color="black", w=3):
    return go.Scatter3d(
        x=[a[0], b[0]], y=[a[1], b[1]], z=[a[2], b[2]],
        mode="lines", line=dict(color=color, width=w),
        showlegend=False
    )

# --- Kub
cube = []
for s in [-1, 1]:
    for axis in range(3):
        v = np.array([[s if i == axis else c for i in range(3)]
                      for c in np.linspace(-1, 1, 2)])
        cube.append(line(v[0], v[1], "gray", 2.5))

# --- Tetraedrar
tetra_up = np.array([[1,1,1],[-1,-1,1],[1,-1,-1],[-1,1,-1]]) * 0.7
tetra_down = np.array([[-1,-1,-1],[1,1,-1],[-1,1,1],[1,-1,1]]) * 0.7
edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
tetra = [line(tetra_up[a], tetra_up[b], "red", 3.5) for a,b in edges] + \
        [line(tetra_down[a], tetra_down[b], "blue", 3.5) for a,b in edges]

# --- Hex-länkar
hex_links = [line(tetra_up[i], tetra_down[(i+1)%4], "silver", 4) for i in range(4)]

# ==========================================================
# 3) SFÄR – Fasgradient med interferens
# ==========================================================
def phase_pattern(theta, phi, t):
    # Två interfererande vågor med fasskillnad och gyllene puls
    wave1 = np.sin(3*theta + t)
    wave2 = np.cos(5*phi - t * phi_const)
    return np.sin(wave1 + wave2 + np.sin(t * phi_const))  # synkad till pulsen

sphere = go.Surface(
    x=r0*x0, y=r0*y0, z=r0*z0,
    surfacecolor=phase_pattern(theta, phi, 0),
    colorscale="Turbo", cmin=-1, cmax=1,
    opacity=0.65, showscale=False,
    lighting=dict(ambient=0.8, diffuse=0.5, specular=0.4),
    name="Sfär (fasinterferens)"
)

# ==========================================================
# 4) FRAMES – pulserande och fasrörlig sfär
# ==========================================================
frames = []
steps = 90
for k in range(steps):
    t = k / steps * 2*np.pi
    r = r0 * (1 + amp * np.sin(t * phi_const))
    frames.append(go.Frame(
        name=f"frame{k}",
        data=[go.Surface(
            x=r*x0, y=r*y0, z=r*z0,
            surfacecolor=phase_pattern(theta, phi, t),
            colorscale="Turbo", cmin=-1, cmax=1,
            opacity=0.65, showscale=False,
            lighting=dict(ambient=0.8, diffuse=0.5, specular=0.4)
        )],
        traces=[0],   # Uppdaterar endast sfären
        layout=dict(scene_camera=dict(
            eye=dict(x=2*np.cos(t/2), y=2*np.sin(t/2), z=1.3)
        ))
    ))

# Loop-komplettering för jämn återgång
frames.append(frames[0])

# ==========================================================
# 5) FIGUR
# ==========================================================
fig = go.Figure(
    data=[sphere] + cube + tetra + hex_links,
    frames=frames
)

fig.update_layout(
    template=None,
    title="🌐 v6 – Holografisk Fas-Interferens: Koherent fält med gyllene puls",
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
             "args": [None, {"frame": {"duration":75, "redraw":True},
                             "fromcurrent":True, "mode":"immediate"}]},
            {"label": "⏸ Pausa", "method": "animate",
             "args": [[None], {"frame": {"duration":0}, "mode":"immediate"}]}
        ],
        "x": 0.05, "y": 0.03
    }],
    paper_bgcolor="white",
    showlegend=False
)

# ==========================================================
# 6) VISA, SPARA, ÖPPNA
# ==========================================================
fig.show()
outfile = os.path.abspath("Coherent_Field_Visualizer_v6_opt.html")
fig.write_html(outfile)
webbrowser.open("file://" + outfile)
