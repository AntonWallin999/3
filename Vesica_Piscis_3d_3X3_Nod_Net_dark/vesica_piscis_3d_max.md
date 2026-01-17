import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import webbrowser
import os

# ============================================================
# FORCE RENDERER (SÄKER KÖRNING)
# ============================================================

pio.renderers.default = "browser"

# ============================================================
# RELATIONELL GEOMETRI - FUNKTIONER
# ============================================================

def create_vesica_circles(r, n=200):
    t = np.linspace(0, 2*np.pi, n)
    x1, y1 = r * np.cos(t) - r/2, r * np.sin(t)
    x2, y2 = r * np.cos(t) + r/2, r * np.sin(t)
    return (x1, y1), (x2, y2)

def rotate_3d(x, y, z, ax, ay, az):
    rad_x, rad_y, rad_z = np.deg2rad(ax), np.deg2rad(ay), np.deg2rad(az)

    if ax != 0:
        y, z = y*np.cos(rad_x) - z*np.sin(rad_x), y*np.sin(rad_x) + z*np.cos(rad_x)
    if ay != 0:
        x, z = x*np.cos(rad_y) + z*np.sin(rad_y), -x*np.sin(rad_y) + z*np.cos(rad_y)
    if az != 0:
        x, y = x*np.cos(rad_z) - y*np.sin(rad_z), x*np.sin(rad_z) + y*np.cos(rad_z)

    return x, y, z

def add_vesica_to_traces(traces, r, color, opacity, rotation=(0,0,0)):
    (c1_x, c1_y), (c2_x, c2_y) = create_vesica_circles(r)

    for cx, cy in [(c1_x, c1_y), (c2_x, c2_y)]:
        z = np.zeros_like(cx)
        rx, ry, rz = rotate_3d(cx, cy, z, *rotation)
        traces.append(go.Scatter3d(
            x=rx, y=ry, z=rz,
            mode="lines",
            line=dict(color=color, width=4),
            opacity=opacity,
            showlegend=False,
            hoverinfo="none"
        ))

# ============================================================
# TILLAGG: NODER + RELATIONER
# ============================================================

def vesica_circle_nodes(r, rotation=(0,0,0)):
    angles = [0, np.pi/2, np.pi, 3*np.pi/2]
    nodes = []

    for sign in (-1, 1):
        cx_offset = sign * r/2
        for a in angles:
            x = r * np.cos(a) + cx_offset
            y = r * np.sin(a)
            z = 0.0
            rx, ry, rz = rotate_3d(
                np.array([x]), np.array([y]), np.array([z]),
                *rotation
            )
            nodes.append([rx[0], ry[0], rz[0]])

    return nodes

def add_diagonal_connections(traces, nodes, color="white", opacity=0.15):
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            traces.append(go.Scatter3d(
                x=[nodes[i][0], nodes[j][0]],
                y=[nodes[i][1], nodes[j][1]],
                z=[nodes[i][2], nodes[j][2]],
                mode="lines",
                line=dict(color=color, width=1),
                opacity=opacity,
                showlegend=False,
                hoverinfo="none"
            ))

# ============================================================
# BYGG STRUKTUREN (1 → 2 → 4)
# ============================================================

all_traces = []
all_nodes = []

# Nivå 0
add_vesica_to_traces(all_traces, 6.0, "royalblue", 1.0, (0, 0, 0))
all_nodes.extend(vesica_circle_nodes(6.0, (0, 0, 0)))

# Nivå 1
add_vesica_to_traces(all_traces, 3.0, "crimson", 0.8, (90, 0, 0))
all_nodes.extend(vesica_circle_nodes(3.0, (90, 0, 0)))

add_vesica_to_traces(all_traces, 3.0, "crimson", 0.8, (0, 90, 0))
all_nodes.extend(vesica_circle_nodes(3.0, (0, 90, 0)))

# Nivå 2
diagonal_angles = [(45, 45, 0), (45, -45, 0), (-45, 45, 0), (-45, -45, 0)]
for ang in diagonal_angles:
    add_vesica_to_traces(all_traces, 1.5, "green", 0.6, ang)
    all_nodes.extend(vesica_circle_nodes(1.5, ang))

# ============================================================
# RELATIONELLA DIAGONALER (ALLA → ALLA)
# ============================================================

add_diagonal_connections(all_traces, all_nodes)

# ============================================================
# RENDERING & EXPORT
# ============================================================

fig = go.Figure(data=all_traces)

fig.update_layout(
    title="RP9 — Vesica Piscis 3D (Relationell Funktionsrymd)",
    template="plotly_dark",
    scene=dict(
        aspectmode="data",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        camera=dict(eye=dict(x=1.8, y=1.8, z=1.8))
    ),
    margin=dict(l=0, r=0, b=0, t=50)
)

filename = "vesica_piscis_3d.html"
fig.write_html(filename)
webbrowser.open("file://" + os.path.realpath(filename))
fig.show()

print("KLART. Vesica Piscis 3D med noder och relationell funktionsgraf renderad.")
