import plotly.graph_objects as go
import numpy as np
import os, webbrowser

# ==========================================================
# 1) PARAMETRAR — Harmonisk Fusion (slutstadiet)
# ==========================================================
phi = 1.61803398875
n = 80               # optimerad upplösning
r0 = 1.0
amp = 0.15
steps = 150

theta = np.linspace(0, np.pi, n)
phi_angle = np.linspace(0, 2*np.pi, n)
theta, phi_angle = np.meshgrid(theta, phi_angle)
x0 = np.sin(theta) * np.cos(phi_angle)
y0 = np.sin(theta) * np.sin(phi_angle)
z0 = np.cos(theta)

# ==========================================================
# 2) FASINTERFERENS — Ljusfältets resonansfunktion
# ==========================================================
def fusion_field(theta, phi_angle, t):
    # tre överlagrade vågor i φ-progression
    wave = (np.sin(3*theta + t)
          + np.cos(5*phi_angle - phi*t)
          + np.sin(7*(theta+phi_angle)/2 - t*phi))
    return np.tanh(wave/2)  # fasjämnande funktion

# ==========================================================
# 3) GEOMETRISK RAM — Kub + Tetraedrar i nollbalans
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
        cube.append(line(v[0],v[1],"lightgray",1.8))

tetra=np.array([[1,1,1],[-1,-1,1],[1,-1,-1],[-1,1,-1]])*0.8
edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
tetra_lines=[line(tetra[a],tetra[b],"silver",2) for a,b in edges]

# ==========================================================
# 4) LJUSFÄLT – Sfärisk interferens med självlysande kärna
# ==========================================================
surface = go.Surface(
    x=r0*x0, y=r0*y0, z=r0*z0,
    surfacecolor=fusion_field(theta,phi_angle,0),
    colorscale="Plasma", cmin=-1, cmax=1,
    opacity=0.75, showscale=False,
    lighting=dict(ambient=0.8, diffuse=0.5, specular=0.4)
)

# Central ljuspunkt (singularitet)
core = go.Scatter3d(
    x=[0], y=[0], z=[0],
    mode="markers+text",
    text=["Ljuspunkt Φ"],
    textposition="top center",
    marker=dict(size=10, color="gold", opacity=0.9),
    showlegend=False
)

# ==========================================================
# 5) ANIMATION — Fasintegrerad fusion
# ==========================================================
frames=[]
for k in range(steps):
    t = k/steps * 4*np.pi
    field = fusion_field(theta,phi_angle,t)
    scale = r0 * (1 + amp*np.sin(t/phi))
    frames.append(go.Frame(
        name=f"f{k}",
        data=[
            go.Surface(
                x=scale*x0, y=scale*y0, z=scale*z0,
                surfacecolor=field,
                colorscale="Plasma", cmin=-1, cmax=1,
                opacity=0.75, showscale=False,
                lighting=dict(ambient=0.8, diffuse=0.5, specular=0.4)
            )
        ],
        traces=[0],
        layout=dict(scene_camera=dict(
            eye=dict(
                x=2*np.cos(t/phi),
                y=2*np.sin(t/phi),
                z=1.2 + 0.2*np.sin(t)
            )
        ))
    ))

# Sömlös looping
frames.append(frames[0])

# ==========================================================
# 6) FIGUR – Harmonisk Fusion
# ==========================================================
fig = go.Figure(
    data=[surface, core] + cube + tetra_lines,
    frames=frames
)

fig.update_layout(
    title="✨ v10 — Harmonisk Fusion: Ljusets Geometri i Självkoherens",
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode="cube"
    ),
    updatemenus=[{
        "type":"buttons",
        "buttons":[
            {"label":"▶ Initiera Fusion","method":"animate",
             "args":[None,{"frame":{"duration":60,"redraw":True},
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
outfile = os.path.abspath("Harmonisk_Fusion_v10_opt.html")
fig.write_html(outfile)
webbrowser.open("file://" + outfile)