import plotly.graph_objects as go
import numpy as np
import os
import webbrowser

# ==========================================================
# 1. Grundparametrar
# ==========================================================
points_base = {
    "c": np.array([1, 0, 0]),                          # Ljus (blå)
    "G": np.array([-0.5, np.sqrt(3)/2, 0]),            # Gravitation (grön)
    "α": np.array([-0.5, -np.sqrt(3)/2, 0])            # Finstruktur (orange)
}

centroid_base = (points_base["c"] + points_base["G"] + points_base["α"]) / 3
height_base = np.sqrt(2/3)                              # Höjd för regelbunden tetraeder

frames = 120                                            # Antal animationframes
cycles = 2                                              # Antal pulser
amplitude = 0.5                                         # Pulshöjd
z_values = height_base + amplitude * np.sin(
    np.linspace(0, 2 * np.pi * cycles, frames)
)

# ==========================================================
# 2. Färger och grundfigur
# ==========================================================
colors = {"c": "blue", "G": "green", "α": "orange", "√π": "red"}
fig = go.Figure()

# Rita basen
base_labels = list(points_base.keys())
for i in range(3):
    p1, p2 = base_labels[i], base_labels[(i + 1) % 3]
    x = [points_base[p1][0], points_base[p2][0]]
    y = [points_base[p1][1], points_base[p2][1]]
    z = [points_base[p1][2], points_base[p2][2]]
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z, mode="lines",
        line=dict(color="gray", width=4), showlegend=False
    ))

# Rita baspunkterna
for label, coord in points_base.items():
    fig.add_trace(go.Scatter3d(
        x=[coord[0]], y=[coord[1]], z=[coord[2]],
        mode="markers+text",
        text=[label],
        textposition="top center",
        marker=dict(size=8, color=colors[label]),
        name=label
    ))

# ==========================================================
# 3. Funktion för att generera tetraederns kanter och spår
# ==========================================================
def tetra_edges(z_val, trail_x, trail_y, trail_z):
    traces = []
    vertex = np.array([centroid_base[0], centroid_base[1], z_val])

    # Linjer till baspunkterna
    for label, coord in points_base.items():
        traces.append(go.Scatter3d(
            x=[coord[0], vertex[0]],
            y=[coord[1], vertex[1]],
            z=[coord[2], vertex[2]],
            mode="lines",
            line=dict(color="gray", width=2, dash="dot"),
            showlegend=False
        ))

    # Röda punktens aktuella läge
    traces.append(go.Scatter3d(
        x=[vertex[0]], y=[vertex[1]], z=[vertex[2]],
        mode="markers+text",
        text=["√π"],
        textposition="top center",
        marker=dict(size=10, color="red"),
        name="√π (medvetande)"
    ))

    # Spår (andningsspiral)
    traces.append(go.Scatter3d(
        x=trail_x, y=trail_y, z=trail_z,
        mode="lines",
        line=dict(color="red", width=2),
        opacity=0.4,
        showlegend=False
    ))

    return traces

# ==========================================================
# 4. Förberedd initial spårdata
# ==========================================================
trail_x, trail_y, trail_z = [], [], []

for z in z_values:
    trail_x.append(centroid_base[0] + 0.15 * np.cos(z * np.pi * 2))
    trail_y.append(centroid_base[1] + 0.15 * np.sin(z * np.pi * 2))
    trail_z.append(z)

# ==========================================================
# 5. Skapa frames för animationen
# ==========================================================
frames_list = []
for i, z in enumerate(z_values):
    frames_list.append(go.Frame(
        data=tetra_edges(z, trail_x[:i+1], trail_y[:i+1], trail_z[:i+1])
    ))

fig.frames = frames_list

# ==========================================================
# 6. Layout och knappar
# ==========================================================
fig.update_layout(
    title="Medvetandets Tetraeder — andningsspiral mellan c, G, α och √π",
    scene=dict(
        xaxis=dict(showbackground=False, visible=False),
        yaxis=dict(showbackground=False, visible=False),
        zaxis=dict(showbackground=False, visible=False),
        aspectmode="data"
    ),
    updatemenus=[{
        "type": "buttons",
        "buttons": [
            {"label": "▶ Starta andning",
             "method": "animate",
             "args": [None, {"frame": {"duration": 80, "redraw": True},
                             "fromcurrent": True,
                             "mode": "immediate"}]},
            {"label": "⏸ Pausa",
             "method": "animate",
             "args": [[None], {"frame": {"duration": 0}, "mode": "immediate"}]}
        ],
        "x": 0.05,
        "y": 0
    }],
    showlegend=True,
    paper_bgcolor="white",
    plot_bgcolor="white"
)

# ==========================================================
# 7. Visa, spara och öppna i webbläsare
# ==========================================================
fig.show()
output_file = os.path.abspath("Medvetandets_Tetraeder_Andningsspiral.html")
fig.write_html(output_file)
webbrowser.open("file://" + output_file)