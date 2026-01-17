# ============================================================
# Project: A Correct Relation to Information
# Subproject: Establish M.P.S_010
# ID (002)
# Code Block Nr: 29
# Code Block Name: Octagonal Singularity
# Focus: Z0-Inversion / √π
# License: (CC BY-NC-ND)
# Created by: Anton Wallin
# Sigil: - = ( o ) = -
# ============================================================

import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import os

# ============================================================
# PARAMETRAR
# ============================================================
radius = 0.5
layer_gap = 2.5
base_colors = ['#FFFFFF', '#00CCFF', '#00FF99', '#FFCC00', '#FF6699']
symbolic_shapes = ['singularity', 'triangle', 'square', 'hexagon', 'octagon']

# ============================================================
# KONSTANTER
# ============================================================
sqrt_pi = np.sqrt(np.pi)   # √π
phi_adj = 1.5              # Halva–halva (avsiktlig konstant)
theta = 22.5               # Kvantrotation (grader)
z0_rotation = 90           # Z0-inversion

# ============================================================
# NODPOSITIONER
# ============================================================
def generate_layer_points(shape, count, radius_factor=1.5):
    if shape == 'singularity':
        return [(0.0, 0.0)]
    step = 2.0 * np.pi / count
    return [
        (
            np.cos(i * step) * count * radius_factor,
            np.sin(i * step) * count * radius_factor
        )
        for i in range(count)
    ]

# ============================================================
# SFÄRER
# ============================================================
def plot_sphere(x, y, z, color, opacity=0.5):
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    xs = x + radius * np.cos(u) * np.sin(v)
    ys = y + radius * np.sin(u) * np.sin(v)
    zs = z + radius * np.cos(v)
    return go.Surface(
        x=xs, y=ys, z=zs,
        showscale=False,
        opacity=opacity,
        colorscale=[[0, color], [1, color]]
    )

# ============================================================
# POLYGONKOPPLINGAR
# ============================================================
def plot_connections(points, z_level, shape_type):
    idx_map = {
        'triangle': list(range(3)) + [0],
        'square': list(range(4)) + [0],
        'hexagon': list(range(6)) + [0],
        'octagon': list(range(8)) + [0]
    }
    if shape_type not in idx_map:
        return []

    idxs = idx_map[shape_type]
    lines = []
    for i in range(len(idxs) - 1):
        lines.append(go.Scatter3d(
            x=[points[idxs[i]][0], points[idxs[i+1]][0]],
            y=[points[idxs[i]][1], points[idxs[i+1]][1]],
            z=[z_level, z_level],
            mode='lines',
            line=dict(color='white', width=3),
            hoverinfo='skip'
        ))
    return lines

# ============================================================
# √π-Z0-INVERSIONAXLAR
# ============================================================
def plot_inversion_axes(center, z_level):
    length = sqrt_pi * 3.0
    x0, y0 = center
    return [
        go.Scatter3d(
            x=[x0 - length, x0 + length],
            y=[y0, y0],
            z=[z_level, z_level],
            mode='lines',
            line=dict(color='red', width=2, dash='dot'),
            name='Z0-Inversion X'
        ),
        go.Scatter3d(
            x=[x0, x0],
            y=[y0 - length, y0 + length],
            z=[z_level, z_level],
            mode='lines',
            line=dict(color='red', width=2, dash='dot'),
            name='Z0-Inversion Y'
        )
    ]

# ============================================================
# STRUKTUR
# ============================================================
fig = go.Figure()

total_layers = 9
all_shapes = symbolic_shapes + symbolic_shapes[::-1][1:]
shape_counts = [1, 3, 4, 6, 8, 6, 4, 3, 1]

for i in range(total_layers):
    shape = all_shapes[i]
    count = shape_counts[i]
    z = i * layer_gap
    color = base_colors[min(i, len(base_colors) - 1)]
    points = generate_layer_points(shape, count)

    # Sfärer
    for px, py in points:
        fig.add_trace(plot_sphere(px, py, z, color))

    # Polygonkopplingar
    if shape != 'singularity':
        fig.add_traces(plot_connections(points, z, shape))

    # Z0-inversion på nyckellager
    if i in (0, 4, 8):
        fig.add_traces(plot_inversion_axes((0.0, 0.0), z))

# ============================================================
# LAYOUT
# ============================================================
fig.update_layout(
    title='Octagonal Singularity — Z0-Inversion & √π',
    template='plotly_dark',
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode='data',
        bgcolor='black'
    ),
    paper_bgcolor='black',
    plot_bgcolor='black',
    margin=dict(l=0, r=0, t=40, b=0)
)

# ============================================================
# EXPORT → HTML (GARANTERAD)
# ============================================================
output_file = "MPS_010_Octagonal_Singularity.html"

pio.write_html(
    fig,
    file=output_file,
    include_plotlyjs=True,
    full_html=True,
    auto_open=True
)

print("KLART – HTML skapad:", os.path.abspath(output_file))
