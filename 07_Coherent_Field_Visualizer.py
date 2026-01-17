import plotly.graph_objects as go
import numpy as np
import os, webbrowser

# ==========================================================
# 1) PARAMETRAR – Fraktal skalnivå (Deep Dive)
# ==========================================================
phi_const = 1.61803398875     # gyllene proportion
r0, amp = 1.0, 0.25           # basradie & puls
scale_inner = 0.5             # skalning av inre nivå
amp_inner = amp * 0.8         # mindre amplitud
n = 80                        # optimerad upplösning

theta = np.linspace(0, np.pi, n)
phi = np.linspace(0, 2*np.pi, n)
theta, phi = np.meshgrid(theta, phi)

x0 = np.sin(theta) * np.cos(phi)
y0 = np.sin(theta) * np.sin(phi)
z0 = np.cos(theta)

# ==========================================================
# 2) GEOMETRISKA GRUNDER – Kub & Tetraedrar
# ==========================================================
def line(a,b,color="gray",w=2.5):
    return go.Scatter3d(
        x=[a[0],b[0]], y=[a[1],b[1]], z=[a[2],b[2]],
        mode="lines", line=dict(color=color,width=w), showlegend=False
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

hex_links=[line(tetra_up[i], tetra_down[(i+1)%4],"silver",3.5) for i in range(4)]

# ==========================================================
# 3) SFÄRFUNKTIONER – Interferens & Fasmönster
# ==========================================================
def phase_pattern(theta, phi, t, invert=False):
    base = np.sin(3*theta + t) + np.cos(5*phi - t*phi_const)
    if invert: base = -base
    return np.sin(base + np.sin(t * phi_const))  # synkad puls

# Yttre sfär
outer = go.Surface(
    x=r0*x0, y=r0*y0, z=r0*z0,
    surfacecolor=phase_pattern(theta,phi,0),
    colorscale="Turbo", cmin=-1, cmax=1,
    opacity=0.6, showscale=False,
    lighting=dict(ambient=0.8, diffuse=0.5, specular=0.4)
)

# Inre sfär (fraktal subnivå)
inner = go.Surface(
    x=scale_inner*r0*x0, y=scale_inner*r0*y0, z=scale_inner*r0*z0,
    surfacecolor=phase_pattern(theta,phi,0,invert=True),
    colorscale="Viridis", cmin=-1, cmax=1,
    opacity=0.5, showscale=False,
    lighting=dict(ambient=0.8, diffuse=0.5, specular=0.4)
)

# ==========================================================
# 4) FRAMES – Puls & Fas i två nivåer
# ==========================================================
frames=[]
steps=100
for k in range(steps):
    t = k/steps*2*np.pi
    r_outer = r0 * (1 + amp*np.sin(t*phi_const))
    r_inner = scale_inner*r0 * (1 + amp_inner*np.sin(t*phi_const + np.pi))
    frames.append(go.Frame(
        name=f"f{k}",
        data=[
            go.Surface(
                x=r_outer*x0, y=r_outer*y0, z=r_outer*z0,
                surfacecolor=phase_pattern(theta,phi,t),
                colorscale="Turbo", cmin=-1, cmax=1,
                opacity=0.6, showscale=False,
                lighting=dict(ambient=0.8, diffuse=0.5, specular=0.4)
            ),
            go.Surface(
                x=r_inner*x0, y=r_inner*y0, z=r_inner*z0,
                surfacecolor=phase_pattern(theta,phi,t,invert=True),
                colorscale="Viridis", cmin=-1, cmax=1,
                opacity=0.5, showscale=False,
                lighting=dict(ambient=0.8, diffuse=0.5, specular=0.4)
            )
        ],
        traces=[0,1],
        layout=dict(scene_camera=dict(
            eye=dict(x=2*np.cos(t/3), y=2*np.sin(t/3), z=1.2)
        ))
    ))

# Sömlös looping
frames.append(frames[0])

# ==========================================================
# 5) FIGUR
# ==========================================================
fig = go.Figure(
    data=[outer,inner]+cube+tetra+hex_links,
    frames=frames
)

fig.update_layout(
    template=None,
    title="🌌 v7 — Fraktal Skalnivå (Deep Dive): Sfär-i-Sfär Holografisk Koherens",
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode="cube"
    ),
    updatemenus=[{
        "type":"buttons",
        "buttons":[
            {"label":"▶ Starta fraktal puls","method":"animate",
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
# 6) VISA, SPARA, ÖPPNA
# ==========================================================
fig.show()
outfile = os.path.abspath("Fractal_Scale_Level_v7_opt.html")
fig.write_html(outfile)
webbrowser.open("file://" + outfile)