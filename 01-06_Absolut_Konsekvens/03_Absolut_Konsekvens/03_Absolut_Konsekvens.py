# ==========================================================
# 10C_SelfCalibration_FractalHologram.py
# Co-Creators Foundation © 2025
# Fraktal-holografisk visualisering av självkalibrering
# ==========================================================

import numpy as np
import plotly.graph_objects as go
import os, webbrowser

# ----------------------------------------------------------
# 1. Grundkonstanter
# ----------------------------------------------------------
phi = 1.5        # exakt RP9-konstant (inte approximation)
kappa = 0.1       # dämpning / återkopplingskoefficient
layers = 5        # antal fraktala nivåer (skalor)
points = 300      # punkter per cirkel
frames = 80       # animationens upplösning

# ----------------------------------------------------------
# 2. Fraktal struktur – koordinater i flera skalor
# ----------------------------------------------------------
def generate_fractal_nodes(layer):
    """Returnerar koordinater för en fraktal ring i plan XY."""
    r = (1 / phi) ** layer
    theta = np.linspace(0, 2*np.pi, points)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y, r

# ----------------------------------------------------------
# 3. Fältfunktioner – ljus, skugga, fas
# ----------------------------------------------------------
def phase_field(t, layer):
    """Beräknar aktuell fas för given fraktal nivå."""
    delta_phi = (np.pi/2) * np.exp(-kappa*t) * (1/layer)
    return delta_phi

def intensity(x, y, r, t, delta_phi):
    """Intensitet som funktion av position och fasavvikelse."""
    return np.cos((x + y)/phi - t/phi + delta_phi) * np.exp(-phi*r)

# ----------------------------------------------------------
# 4. Skapa 3D-punkter för varje lager och tid
# ----------------------------------------------------------
def generate_frame(t):
    xs, ys, zs, cs = [], [], [], []
    for layer in range(1, layers+1):
        x, y, r = generate_fractal_nodes(layer)
        delta_phi = phase_field(t, layer)
        z = intensity(x, y, r, t, delta_phi)
        color = np.full_like(z, fill_value=layer)
        xs.extend(x)
        ys.extend(y)
        zs.extend(z)
        cs.extend(color)
    return np.array(xs), np.array(ys), np.array(zs), np.array(cs)

# ----------------------------------------------------------
# 5. Generera animation
# ----------------------------------------------------------
frames_data = []
for i in range(frames):
    t = i * 0.6
    x, y, z, c = generate_frame(t)
    frames_data.append((x, y, z, c, t))

# ----------------------------------------------------------
# 6. Plotly-figur
# ----------------------------------------------------------
fig = go.Figure()

# Första ramen
x0, y0, z0, c0, t0 = frames_data[0]
fig.add_trace(go.Scatter3d(
    x=x0, y=y0, z=z0,
    mode='markers',
    marker=dict(size=2.5, color=c0, colorscale='Viridis', opacity=0.8),
    name=f"t={t0:.2f}"
))

# Animationens steg
frames_plotly = []
for x, y, z, c, t in frames_data:
    frames_plotly.append(go.Frame(
        data=[go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(size=2.5, color=c, colorscale='Viridis', opacity=0.8)
        )],
        name=f"t={t:.2f}"
    ))

fig.frames = frames_plotly

# ----------------------------------------------------------
# 7. Layout och animation
# ----------------------------------------------------------
fig.update_layout(
    title="🌐 Fraktalt Hologram — Självkalibrering över skalor (RP9)",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Amplitude",
        aspectmode='cube',
        bgcolor='black'
    ),
    template='plotly_dark',
    updatemenus=[{
        "type": "buttons",
        "showactive": False,
        "buttons": [
            {"label": "▶ Start", "method": "animate",
             "args": [None, {"frame": {"duration": 80, "redraw": True},
                             "fromcurrent": True, "mode": "immediate"}]},
            {"label": "⏸ Stop", "method": "animate", "args": [[None], {"frame": {"duration": 0}, "mode": "immediate"}]}
        ]
    }]
)

# ----------------------------------------------------------
# 8. Export och öppning
# ----------------------------------------------------------
html_path = os.path.abspath("SelfCalibration_FractalHologram.html")
fig.write_html(html_path)
fig.show()
webbrowser.open("file://" + html_path)

print("Fraktalt hologram skapat och öppnat i webbläsaren.")
print("Fil sparad som:", html_path)
input("\n[ENTER] för att avsluta sessionen...")

# ==========================================================
# SLUT — Co-Creators Foundation / RP9 Framework
# ==========================================================
