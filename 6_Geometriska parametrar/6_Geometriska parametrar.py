import plotly.graph_objects as go
import numpy as np
import os, webbrowser

# ==========================================================
# 1. Parametrar — Gyllene helix
# ==========================================================
phi = 1.61803398875              # Gyllene snittet
theta = np.linspace(0, 6*np.pi, 900)  # tre varv
r0 = 0.2                         # start-radie
r = r0 * phi**(theta / (2*np.pi)) # logaritmisk expansion (φ per varv)

# 45° lutning – stigning proportionell mot radien
z = r * np.tan(np.deg2rad(45))

# Kartesiska koordinater
x = r * np.cos(theta)
y = r * np.sin(theta)

# ==========================================================
# 2. Plotly-figur
# ==========================================================
fig = go.Figure()

# Huvudspiral
fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode="lines",
    line=dict(color="crimson", width=6),
    name="Gyllene helix (√π-rörelse)"
))

# Markera början och slut
fig.add_trace(go.Scatter3d(
    x=[x[0]], y=[y[0]], z=[z[0]],
    mode="markers+text",
    text=["Start"],
    textposition="top center",
    marker=dict(size=6, color="blue"),
    name="Start"
))
fig.add_trace(go.Scatter3d(
    x=[x[-1]], y=[y[-1]], z=[z[-1]],
    mode="markers+text",
    text=["Slut"],
    textposition="top center",
    marker=dict(size=6, color="green"),
    name="Slut"
))

# ==========================================================
# 3. Lägg till lätt genomskinligt referensplan
# ==========================================================
plane = np.linspace(-1.5, 1.5, 2)
fig.add_trace(go.Surface(
    x=[[p for p in plane]*2],
    y=[plane, plane],
    z=[[0,0],[0,0]],
    opacity=0.1,
    showscale=False,
    colorscale=[[0,"lightgray"],[1,"lightgray"]],
    name="Referensplan"
))

# ==========================================================
# 4. Layout och animation (rotation kring Z)
# ==========================================================
frames = []
for angle in np.linspace(0, 360, 60):
    frames.append(go.Frame(layout=dict(
        scene_camera=dict(
            eye=dict(x=2*np.cos(np.radians(angle)),
                     y=2*np.sin(np.radians(angle)),
                     z=1.2)
        )
    )))
fig.frames = frames

fig.update_layout(
    title="Gyllene Helix — Eskalerande rotationsgeometri (φ, 45°, 3 varv)",
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode="data"
    ),
    updatemenus=[{
        "type":"buttons",
        "buttons":[
            {"label":"▶ Rotera", "method":"animate",
             "args":[None, {"frame":{"duration":80,"redraw":True},
                            "fromcurrent":True,"mode":"immediate"}]},
            {"label":"⏸ Pausa", "method":"animate",
             "args":[[None], {"frame":{"duration":0},"mode":"immediate"}]}
        ],
        "x":0.05,"y":0
    }],
    showlegend=True,
    paper_bgcolor="white",
    plot_bgcolor="white"
)

# ==========================================================
# 5. Visa, spara, öppna
# ==========================================================
fig.show()
outfile = os.path.abspath("Gyllene_Helix_45grad_3varv.html")
fig.write_html(outfile)
webbrowser.open("file://" + outfile)