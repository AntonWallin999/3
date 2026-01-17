import plotly.graph_objects as go
import numpy as np
import os, webbrowser

# ==========================================================
# 1) PARAMETRAR — Resonant Expansion
# ==========================================================
phi_const = 1.61803398875
r0, amp = 1.0, 0.18
n_levels = 3                 # tre sfärer i φ-progression
n = 80                       # optimerad upplösning

theta = np.linspace(0, np.pi, n)
phi = np.linspace(0, 2*np.pi, n)
theta, phi = np.meshgrid(theta, phi)
x0 = np.sin(theta) * np.cos(phi)
y0 = np.sin(theta) * np.sin(phi)
z0 = np.cos(theta)

# ==========================================================
# 2) GEOMETRISKA REFERENSER — Kub & Tetraedrar
# ==========================================================
def line(a,b,color="gray",w=2.5):
    return go.Scatter3d(
        x=[a[0],b[0]], y=[a[1],b[1]], z=[a[2],b[2]],
        mode="lines", line=dict(color=color,width=w),
        showlegend=False
    )

cube=[]
for s in [-1,1]:
    for axis in range(3):
        v=np.array([[s if i==axis else c for i in range(3)]
                    for c in np.linspace(-1,1,2)])
        cube.append(line(v[0],v[1],"lightgray",2))

tetra_up=np.array([[1,1,1],[-1,-1,1],[1,-1,-1],[-1,1,-1]])*0.7
tetra_down=np.array([[-1,-1,-1],[1,1,-1],[-1,1,1],[1,-1,1]])*0.7
edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
tetra=[line(tetra_up[a],tetra_up[b],"red",3) for a,b in edges] + \
       [line(tetra_down[a],tetra_down[b],"blue",3) for a,b in edges]

# ==========================================================
# 3) FASINTERFERENS – Harmonisk resonans
# ==========================================================
def phase_pattern(theta, phi, t, offset=0):
    wave1 = np.sin(3*theta + t + offset)
    wave2 = np.cos(5*phi - t*phi_const + offset)
    return np.sin(wave1 + wave2 + np.sin(t * phi_const))  # gyllene fasinjektion

# ==========================================================
# 4) BASNIVÅER – Tre sfärer i φ-progression
# ==========================================================
colorscales = ["Turbo", "Ice", "Viridis"]
opacities = [0.6, 0.5, 0.45]
radii = [r0, r0*phi_const, r0*phi_const**2]

spheres = [
    go.Surface(
        x=radii[i]*x0, y=radii[i]*y0, z=radii[i]*z0,
        surfacecolor=phase_pattern(theta,phi,0,offset=i*np.pi/3),
        colorscale=colorscales[i%3], cmin=-1, cmax=1,
        opacity=opacities[i], showscale=False,
        lighting=dict(ambient=0.8, diffuse=0.5, specular=0.4)
    )
    for i in range(n_levels)
]

# ==========================================================
# 5) FRAMES – Expansion i φ-rytm
# ==========================================================
frames=[]
steps=120
for k in range(steps):
    t = k/steps * 2*np.pi
    phase_sync = np.sin(t*phi_const)
    data_frames=[]
    for i in range(n_levels):
        scale = radii[i] * (1 + amp*np.sin(t + i*np.pi/3))
        data_frames.append(go.Surface(
            x=scale*x0, y=scale*y0, z=scale*z0,
            surfacecolor=phase_pattern(theta,phi,t,offset=i*np.pi/3),
            colorscale=colorscales[i%3], cmin=-1, cmax=1,
            opacity=opacities[i], showscale=False,
            lighting=dict(ambient=0.8, diffuse=0.5, specular=0.4)
        ))
    frames.append(go.Frame(
        name=f"f{k}",
        data=data_frames,
        traces=list(range(n_levels)),
        layout=dict(scene_camera=dict(
            eye=dict(
                x=2*np.cos(t/phi_const),
                y=2*np.sin(t/phi_const),
                z=1.2 + 0.15*np.sin(t)
            )
        ))
    ))

# Sömlös loop
frames.append(frames[0])

# ==========================================================
# 6) FIGUR
# ==========================================================
fig = go.Figure(
    data=spheres + cube + tetra,
    frames=frames
)

fig.update_layout(
    template=None,
    title="🌌 v9 — Resonant Expansion: Fraktal Andning i Gyllene Proportioner",
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode="cube"
    ),
    updatemenus=[{
        "type":"buttons",
        "buttons":[
            {"label":"▶ Starta expansion","method":"animate",
             "args":[None,{"frame":{"duration":70,"redraw":True},
                           "fromcurrent":True,"mode":"immediate"}]},
            {"label":"⏸ Pausa","method":"animate",
             "args":[[None],{"frame":{"duration":0},"mode":"immediate"}]}
        ],
        "x":0.05,"y":0.03
    }],
    paper_bgcolor="white",
    showlegend=False
)

# ==========================================================
# 7) VISA, SPARA, ÖPPNA
# ==========================================================
fig.show()
outfile = os.path.abspath("Resonant_Expansion_v9_opt.html")
fig.write_html(outfile)
webbrowser.open("file://" + outfile)