import plotly.graph_objects as go
import numpy as np
import os
import webbrowser

# ==========================================================
# 1. Grundparametrar
# ==========================================================
# Bas (triangel i XY-plan)
points_base = {
    "c": np.array([1, 0, 0]),                          # Ljus (blå)
    "G": np.array([-0.5, np.sqrt(3)/2, 0]),            # Gravitation (grön)
    "α": np.array([-0.5, -np.sqrt(3)/2, 0])            # Finstruktur (orange)
}

# Beräkna basens centroid
centroid_base = (points_base["c"] + points_base["G"] + points_base["α"]) / 3
height_base = np.sqrt(2/3)                              # Höjd för regelbunden tetraeder

# Animationens tidsparametrar
frames = 60                    # Antal animationframes
cycles = 2                     # Antal pulser
amplitude = 0.5                # Pulshöjd
z_values = height_base + amplitude * np.sin(
    np.linspace(0, 2 * np.pi * cycles, frames)
)

# ==========================================================
# 2. Basfigur utan animation
# ==========================================================
fig = go.Figure()

# Färger för hörn
colors = {
    "c": "blue",
    "G": "green",
    "α": "orange",
    "√π": "red"
}

# Rita baslinjer mellan c–G–α
base_labels = list(points_base.keys())
for i in range(3):
    p1 = base_labels[i]
    p2 = base_labels[(i + 1) % 3]
    x = [points_base[p1][0], points_base[p2][0]]
    y = [points_base[p1][1], points_base[p2][1]]
    z = [points_base[p1][2], points_base[p2][2]]
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode="lines",
        line=dict(color="gray", width=4),
        showlegend=False
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
# 3. Lägg till initial √π-punkt och linjer till basen
# ==========================================================
def tetra_edges(z_val):
    traces = []
    vertex = np.array([centroid_base[0], centroid_base[1], z_val])
    for label, coord in points_base.items():
        traces.append(go.Scatter3d(
            x=[coord[0], vertex[0]],
            y=[coord[1], vertex[1]],
            z=[coord[2], vertex[2]],
            mode="lines",
            line=dict(color="gray", width=2, dash="dot"),
            showlegend=False
        ))
    traces.append(go.Scatter3d(
        x=[vertex[0]], y=[vertex[1]], z=[vertex[2]],
        mode="markers+text",
        text=["√π"],
        textposition="top center",
        marker=dict(size=10, color="red"),
        name="√π (medvetande)"
    ))
    return traces

# Startläge
for tr in tetra_edges(z_values[0]):
    fig.add_trace(tr)

# ==========================================================
# 4. Skapa animationens frames
# ==========================================================
frames_list = []
for z in z_values:
    frames_list.append(go.Frame(data=tetra_edges(z)))

fig.frames = frames_list

# ==========================================================
# 5. Layout, knappar och presentation
# ==========================================================
fig.update_layout(
    title="Medvetandets Tetraeder — pulserande balans mellan c, G, α och √π",
    scene=dict(
        xaxis=dict(showbackground=False, visible=False),
        yaxis=dict(showbackground=False, visible=False),
        zaxis=dict(showbackground=False, visible=False),
        aspectmode="data"
    ),
    updatemenus=[{
        "type": "buttons",
        "buttons": [
            {
                "label": "▶ Starta puls",
                "method": "animate",
                "args": [None, {"frame": {"duration": 100, "redraw": True},
                                "fromcurrent": True,
                                "mode": "immediate",
                                "transition": {"duration": 0}}]
            },
            {
                "label": "⏸ Pausa",
                "method": "animate",
                "args": [[None], {"frame": {"duration": 0}, "mode": "immediate"}]
            }
        ],
        "showactive": True,
        "x": 0.05,
        "y": 0
    }],
    showlegend=True,
    paper_bgcolor="white",
    plot_bgcolor="white"
)

# ==========================================================
# 6. Visa, spara och öppna
# ==========================================================
fig.show()
output_file = os.path.abspath("Medvetandets_Tetraeder_Animation.html")
fig.write_html(output_file)
webbrowser.open("file://" + output_file)