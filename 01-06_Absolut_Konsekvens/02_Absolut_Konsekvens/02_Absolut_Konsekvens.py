# ==========================================================
# 10B_SelfObservation_QuantumField.py
# Co-Creators Foundation © 2025
# 3D-visualisering av självobservation och fraktal koherens
# ==========================================================

import numpy as np
import plotly.graph_objects as go
import webbrowser
import os

# ----------------------------------------------------------
# 1. Grundkonstanter
# ----------------------------------------------------------
phi = 1.5   # exakt konstant enligt harmonisk struktursystemmodell
kappa = 0.12  # dämpning för självkalibrering
grid_size = 150

# ----------------------------------------------------------
# 2. Definiera koordinatsystem
# ----------------------------------------------------------
x = np.linspace(-np.pi, np.pi, grid_size)
y = np.linspace(-np.pi, np.pi, grid_size)
X, Y = np.meshgrid(x, y)
T = np.linspace(0, 40, 100)  # tidsaxel

# ----------------------------------------------------------
# 3. Beräkna fältkomponenter
# ----------------------------------------------------------
# Ljusfält – koherent våg
def light_field(t):
    return np.cos(X/phi + Y/phi - t/phi) * np.exp(-0.02*(X**2 + Y**2))

# Skuggfält – inverterad fas med avtagande Δφ(t)
def shadow_field(t):
    delta_phi = (np.pi/2) * np.exp(-kappa*t)
    return np.cos(X/phi + Y/phi + np.pi + delta_phi) * np.exp(-0.02*(X**2 + Y**2))

# Interferensfält – summan av ljus och skugga
def interference(t):
    return light_field(t) + shadow_field(t)

# ----------------------------------------------------------
# 4. Välj ett antal tidssteg för visualisering
# ----------------------------------------------------------
time_points = [0, 10, 20, 30, 40]
frames = []

for t in time_points:
    frames.append(interference(t))

# ----------------------------------------------------------
# 5. Skapa 3D-yta
# ----------------------------------------------------------
fig = go.Figure()

# Lägg till första ramen (t = 0)
fig.add_trace(go.Surface(
    z=frames[0],
    x=X, y=Y,
    colorscale='Viridis',
    showscale=False,
    opacity=0.9,
    name="Interferensfält t=0"
))

# ----------------------------------------------------------
# 6. Lägg till animerade tidsramar
# ----------------------------------------------------------
for i, t in enumerate(time_points):
    fig.add_trace(go.Surface(
        visible=False,
        z=frames[i],
        x=X, y=Y,
        colorscale='Viridis',
        showscale=False,
        opacity=0.9,
        name=f"Interferensfält t={t:.1f}"
    ))

# Gör första aktiv
fig.data[0].visible = True

# ----------------------------------------------------------
# 7. Definiera animering
# ----------------------------------------------------------
steps = []
for i, t in enumerate(time_points):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": f"🔮 Självobservation — t = {t:.1f}"}],
    )
    step["args"][0]["visible"][i] = True
    steps.append(step)

sliders = [dict(
    active=0,
    pad={"t": 50},
    steps=steps,
    currentvalue={"prefix": "Tid: "}
)]

fig.update_layout(
    title="🧩 Självobservation och Geometrisk Självkalibrering (RP9 Quantum Field)",
    scene=dict(
        xaxis_title="X (reell domän)",
        yaxis_title="Y (imaginär domän)",
        zaxis_title="Amplitude",
        xaxis=dict(showbackground=False),
        yaxis=dict(showbackground=False),
        zaxis=dict(showbackground=False),
        aspectratio=dict(x=1, y=1, z=0.5)
    ),
    margin=dict(l=0, r=0, b=0, t=60),
    sliders=sliders,
    template='plotly_white'
)

# ----------------------------------------------------------
# 8. Spara och öppna
# ----------------------------------------------------------
html_path = os.path.abspath("SelfObservation_QuantumField.html")
fig.write_html(html_path)
fig.show()
webbrowser.open("file://" + html_path)

# ----------------------------------------------------------
# 9. Avslutning
# ----------------------------------------------------------
print("3D-visualisering skapad och öppnad i webbläsaren.")
print("Fil sparad som:", html_path)
input("\n[ENTER] för att avsluta sessionen...")

# ==========================================================
# SLUT — Co-Creators Foundation / RP9 Framework
# ==========================================================
