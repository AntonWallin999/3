import plotly.graph_objects as go
import numpy as np
import os, webbrowser

# ==========================================================
# 1. PARAMETRAR – Gyllene puls och våg
# ==========================================================
phi_const = 1.61803398875
r0 = 1.0
amp = 0.35
n = 60
theta = np.linspace(0, np.pi, n)
phi = np.linspace(0, 2*np.pi, n)
theta, phi = np.meshgrid(theta, phi)
x0 = np.sin(theta) * np.cos(phi)
y0 = np.sin(theta) * np.sin(phi)
z0 = np.cos(theta)

# ==========================================================
# 2. FAST GEOMETRI – kub, tetraedrar, hex-länkar
# ==========================================================
def line(a,b,color="black",w=3):
    return go.Scatter3d(
        x=[a[0],b[0]], y=[a[1],b[1]], z=[a[2],b[2]],
        mode="lines",
        line=dict(color=color,width=w),
        showlegend=False
    )

# --- kub
cube=[]
for s in [-1,1]:
    for axis in range(3):
        v=np.array([[s if i==axis else c for i in range(3)]
                    for c in np.linspace(-1,1,2)])
        cube.append(line(v[0],v[1],"black",3))

# --- tetraedrar
tetra_up=np.array([[1,1,1],[-1,-1,1],[1,-1,-1],[-1,1,-1]])*0.7
tetra_down=np.array([[-1,-1,-1],[1,1,-1],[-1,1,1],[1,-1,1]])*0.7
edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
tetra=[]
for e in edges:
    tetra.append(line(tetra_up[e[0]],tetra_up[e[1]],"red",4))
    tetra.append(line(tetra_down[e[0]],tetra_down[e[1]],"blue",4))

# --- hex-länkar
hex_links=[]
pairs=[]
for i in range(4):
    a=tetra_up[i]; b=tetra_down[(i+1)%4]
    hex_links.append(line(a,b,"gray",4))
    pairs.append((a,b))

# ==========================================================
# 3. SFÄR – basytan för pulsen
# ==========================================================
r_init=r0
x_init=r_init*x0; y_init=r_init*y0; z_init=r_init*z0
sphere=go.Surface(
    x=x_init,y=y_init,z=z_init,
    surfacecolor=np.sin(3*theta)*np.cos(3*phi),
    colorscale="Rainbow",opacity=0.6,showscale=False,
    name="Sfär (puls)"
)

# ==========================================================
# 4. FRAMES – sfärens puls + energipulser på länkar
# ==========================================================
frames=[]
steps=100
for k in range(steps):
    t=k/steps*2*np.pi
    # --- sfärens puls
    r=r0*(1+amp*np.sin(t*phi_const))
    x=r*x0; y=r*y0; z=r*z0
    sphere_frame=go.Surface(
        x=x,y=y,z=z,
        surfacecolor=np.sin(3*theta+t)*np.cos(3*phi-t),
        colorscale="Rainbow",opacity=0.6,showscale=False
    )

    # --- energipulser längs länkarna
    link_points=[]
    for (a,b) in pairs:
        s=(np.sin(t*phi_const)+1)/2
        p=a*(1-s)+b*s
        link_points.append(go.Scatter3d(
            x=[p[0]],y=[p[1]],z=[p[2]],
            mode="markers",
            marker=dict(size=6,color="orange"),
            showlegend=False
        ))

    # --- lägg till frame
    frames.append(go.Frame(
        name=str(k),
        data=[sphere_frame]+link_points,
        traces=[0]+[i+1 for i in range(len(pairs))],  # ange vilka spår som uppdateras
        layout=dict(scene_camera=dict(
            eye=dict(x=2*np.cos(t),y=2*np.sin(t),z=1.2)
        ))
    ))

# ==========================================================
# 5. FIGUR
# ==========================================================
# dataindex 0 → sfär
# dataindex 1–len(pairs) reserveras för energipunkter
energy_markers = [go.Scatter3d(x=[0],y=[0],z=[0],
                               mode="markers",
                               marker=dict(size=6,color="orange"),
                               showlegend=False)
                  for _ in pairs]

fig=go.Figure(
    data=[sphere]+energy_markers+cube+tetra+hex_links,
    frames=frames
)

fig.update_layout(
    template=None,
    title="🌐 v5 — Koherent Energiflöde längs Hex-länkarna",
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode="cube"
    ),
    updatemenus=[{
        "type":"buttons",
        "buttons":[
            {"label":"▶ Starta puls","method":"animate",
             "args":[None,{"frame":{"duration":80,"redraw":True},
                           "fromcurrent":True,"mode":"immediate"}]},
            {"label":"⏸ Pausa","method":"animate",
             "args":[[None],{"frame":{"duration":0},"mode":"immediate"}]}
        ],
        "x":0.05,"y":0.02
    }],
    paper_bgcolor="white",
    showlegend=False
)

# ==========================================================
# 6. VISA, SPARA, ÖPPNA
# ==========================================================
fig.show()
outfile=os.path.abspath("Coherent_Field_Visualizer_v5_fixed.html")
fig.write_html(outfile)
webbrowser.open("file://"+outfile)
