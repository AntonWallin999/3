import plotly.graph_objects as go
import numpy as np
import os
import webbrowser

# ==========================================================
# 1. Definiera koordinater för tetraedern
# ==========================================================

# Bas (triangel i XY-plan)
points = {
    "c": np.array([1, 0, 0]),        # Ljus (blå)
    "G": np.array([-0.5, np.sqrt(3)/2, 0]),  # Gravitation (grön)
    "α": np.array([-0.5, -np.sqrt(3)/2, 0]), # Finstruktur (orange)
}

# Vertex – medvetandet / √π (röd)
# Ligger ovanför triangelns centrum
centroid_base = (points["c"] + points["G"] + points["α"]) / 3
height = np.sqrt(2/3)                # Höjd för regelbunden tetraeder
sqrt_pi_vertex = np.array([centroid_base[0], centroid_base[1], height])
points["√π"] = sqrt_pi_vertex

# ==========================================================
# 2. Skapa Plotly-figuren
# ==========================================================
fig = go.Figure()

# Basens trianglar (yta)
faces = [
    ("c", "G", "α"),
    ("c", "G", "√π"),
    ("G", "α", "√π"),
    ("α", "c", "√π")
]

# Färger för varje hörn
colors = {
    "c": "blue",
    "G": "green",
    "α": "orange",
    "√π": "red"
}

# Rita varje triangel
for f in faces:
    x = [points[f[0]][0], points[f[1]][0], points[f[2]][0], points[f[0]][0]]
    y = [points[f[0]][1], points[f[1]][1], points[f[2]][1], points[f[0]][1]]
    z = [points[f[0]][2], points[f[1]][2], points[f[2]][2], points[f[0]][2]]
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode="lines",
        line=dict(width=4, color="gray"),
        showlegend=False
    ))

# Rita punkterna
for label, coord in points.items():
    fig.add_trace(go.Scatter3d(
        x=[coord[0]], y=[coord[1]], z=[coord[2]],
        mode="markers+text",
        text=[label],
        textposition="top center",
        marker=dict(size=8, color=colors[label]),
        name=label
    ))

# ==========================================================
# 3. Layout och etiketter
# ==========================================================
fig.update_layout(
    title="Medvetandets Tetraeder — balans mellan c, G, α och √π",
    scene=dict(
        xaxis=dict(showbackground=False, showticklabels=False, visible=False),
        yaxis=dict(showbackground=False, showticklabels=False, visible=False),
        zaxis=dict(showbackground=False, showticklabels=False, visible=False),
        aspectmode="data"
    ),
    plot_bgcolor="white",
    paper_bgcolor="white",
    showlegend=True
)

# ==========================================================
# 4. Visa, spara och öppna i webbläsare
# ==========================================================
fig.show()

output_file = os.path.abspath("Medvetandets_Tetraeder.html")
fig.write_html(output_file)
webbrowser.open("file://" + output_file)