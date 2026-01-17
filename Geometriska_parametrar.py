import numpy as np
import plotly.graph_objects as go
import webbrowser
import os

# ===============================
# Geometriska parametrar
# ===============================
r = 1.0                   # Radie för den inre cirkeln
square_half = r            # Halva sidan för kvadraten (ger cirkel inskriven)
theta = np.linspace(0, 2*np.pi, 400)

# Cirkelsamordningar
x_circle = r * np.cos(theta)
y_circle = r * np.sin(theta)

# Kvadratsamordningar (absolut form)
x_square = [-square_half, square_half, square_half, -square_half, -square_half]
y_square = [-square_half, -square_half, square_half, square_half, -square_half]

# Tangentpunkter A, B, C, D (cirkelns kontakt med kvadraten)
points = {
    "A": (0, r),
    "B": (r, 0),
    "C": (0, -r),
    "D": (-r, 0)
}

# ===============================
# Skapa Plotly-figur
# ===============================
fig = go.Figure()

# Kvadrat – Absolut geometri
fig.add_trace(go.Scatter(
    x=x_square, y=y_square, mode="lines",
    line=dict(color="black", width=2),
    name="Absolut form (G)"
))

# Cirkeln – Rörelse/energi
fig.add_trace(go.Scatter(
    x=x_circle, y=y_circle, mode="lines",
    line=dict(color="blue", width=2),
    name="Energi i rörelse (F)"
))

# Kontaktpunkter A–D
for label, (x, y) in points.items():
    fig.add_trace(go.Scatter(
        x=[x], y=[y],
        mode="markers+text",
        text=[label],
        textposition="top center",
        marker=dict(size=10, color="red"),
        name=f"Punkt {label}"
    ))

# Observatör (centrum)
fig.add_trace(go.Scatter(
    x=[0], y=[0],
    mode="markers+text",
    text=["O"],
    textposition="bottom center",
    marker=dict(size=12, color="green"),
    name="Observatör (O)"
))

# Energiflödeslinjer mellan O och A–D
for x, y in points.values():
    fig.add_trace(go.Scatter(
        x=[0, x], y=[0, y],
        mode="lines",
        line=dict(color="orange", width=1, dash="dot"),
        showlegend=False
    ))

# ===============================
# Layout och visning
# ===============================
fig.update_layout(
    title="Geometri i rörelse — Balans mellan form (G), energi (F) och observatör (O)",
    xaxis=dict(scaleanchor="y", scaleratio=1, showgrid=False, zeroline=False, visible=False),
    yaxis=dict(showgrid=False, zeroline=False, visible=False),
    plot_bgcolor="white",
    showlegend=True
)

# Visa direkt
fig.show()

# ===============================
# Spara och öppna i webbläsare
# ===============================
output_file = os.path.abspath("Geometri_i_rorelse.html")
fig.write_html(output_file)
webbrowser.open("file://" + output_file)