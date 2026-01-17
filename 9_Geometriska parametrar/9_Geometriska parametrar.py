import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os, webbrowser

# ======================================
# Parametrar – exakt enligt dina krav
# ======================================
phi = 1.61803398875
theta = np.linspace(0.0, 3.0*np.pi, 720)     # 1.5 varv → 3π
r0 = 0.22
r = r0 * phi**(theta / (2.0*np.pi))          # φ-expansion per varv

# Fas: så XZ-projektionen visar tre svängningar och slutar på "upp"
phase = -np.pi
x = r * np.cos(theta + phase)
y = r * np.sin(theta + phase)

# ~45° genomsnittlig stigning (praktiskt rimlig, bibehåller 3 svängningar i XZ)
k = float(np.mean(r))                         # dz/dθ ≈ mean(r)
z = k * theta

# 2D-projektion (XZ): tre svängningar ner→upp→ner→upp
x_proj = x
z_proj = z

# ======================================
# Figur: 3D + 2D (XZ)
# ======================================
fig = make_subplots(
    rows=1, cols=2,
    specs=[[{"type":"scatter3d"}, {"type":"scatter"}]],
    column_widths=[0.62, 0.38],
    subplot_titles=("3D — Gyllene helix (1.5 varv)", "2D — XZ-projektion (tre svängningar)")
)

# 3D-helix
fig.add_trace(
    go.Scatter3d(
        x=x, y=y, z=z,
        mode="lines",
        line=dict(color="crimson", width=6),
        name="√π-rörelse (gyllene helix, 1.5 varv)"
    ),
    row=1, col=1
)

# Referensplan z=0
plane_extent = 1.8 * np.max(r)
fig.add_trace(
    go.Surface(
        x=[[ -plane_extent,  plane_extent],[ -plane_extent,  plane_extent]],
        y=[[ -plane_extent, -plane_extent],[  plane_extent,  plane_extent]],
        z=[[0.0, 0.0],[0.0, 0.0]],
        opacity=0.10, showscale=False,
        colorscale=[[0,"lightgray"],[1,"lightgray"]],
        name="Referensplan"
    ),
    row=1, col=1
)

# Start/Slut
fig.add_trace(
    go.Scatter3d(x=[x[0]], y=[y[0]], z=[z[0]],
                 mode="markers+text", text=["Start"], textposition="top center",
                 marker=dict(size=6, color="blue"), name="Start"),
    row=1, col=1
)
fig.add_trace(
    go.Scatter3d(x=[x[-1]], y=[y[-1]], z=[z[-1]],
                 mode="markers+text", text=["Slut (↑)"], textposition="top center",
                 marker=dict(size=6, color="green"), name="Slut"),
    row=1, col=1
)

# 2D XZ-projektion (tre svängningar)
fig.add_trace(
    go.Scatter(
        x=z_proj, y=x_proj, mode="lines",
        line=dict(color="crimson", width=3),
        name="XZ-projektion"
    ),
    row=1, col=2
)
# Mittlinje för att se upp/ner tydligt
fig.add_trace(
    go.Scatter(
        x=[z_proj[0], z_proj[-1]], y=[0.0, 0.0],
        mode="lines", line=dict(color="gray", width=1, dash="dash"),
        showlegend=False
    ),
    row=1, col=2
)

# Layout
fig.update_layout(
    title="Gyllene helix (1.5 varv) — Tre svängningar i XZ med φ-expansion och ~45° lutning",
    paper_bgcolor="white",
    showlegend=True
)
fig.update_scenes(
    dict(
        xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
        aspectmode="data",
        camera=dict(eye=dict(x=1.9, y=1.3, z=1.0))
    ),
    row=1, col=1
)
fig.update_xaxes(title_text="z (höjd/parametrisk längd)", showgrid=False, zeroline=False, row=1, col=2)
fig.update_yaxes(title_text="x (amplitud)", showgrid=False, zeroline=False, row=1, col=2)

# Mild kamerarotation (valfri)
frames = []
for angle in np.linspace(0.0, 360.0, 60):
    frames.append(
        go.Frame(
            layout=dict(
                scene=dict(
                    camera=dict(
                        eye=dict(
                            x=2.0*np.cos(np.radians(angle)),
                            y=2.0*np.sin(np.radians(angle)),
                            z=1.0
                        )
                    )
                )
            )
        )
    )
fig.frames = frames
fig.update_layout(
    updatemenus=[{
        "type":"buttons",
        "buttons":[
            {"label":"▶ Rotera 3D","method":"animate",
             "args":[None, {"frame":{"duration":80,"redraw":True},
                            "fromcurrent":True,"mode":"immediate"}]},
            {"label":"⏸ Pausa","method":"animate",
             "args":[[None], {"frame":{"duration":0},"mode":"immediate"}]}
        ],
        "x":0.06,"y":0.0
    }]
)

# Visa, spara, öppna
fig.show()
outfile = os.path.abspath("Gyllene_Helix_1p5_varv_tre_svangningar.html")
fig.write_html(outfile)
webbrowser.open("file://" + outfile)
print("Sparad till:", outfile)
