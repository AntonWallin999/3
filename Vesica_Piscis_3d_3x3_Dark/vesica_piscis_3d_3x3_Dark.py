import numpy as np
import plotly.graph_objects as go
import os

# ============================================================
# RELATIONELL GEOMETRI - FUNKTIONER
# ============================================================

def create_vesica_circles(r, n=200):
    """
    Skapar koordinater för en sann Vesica Piscis.
    Relation: Centrumavståndet = Radien (r).
    """
    t = np.linspace(0, 2*np.pi, n)
    # Cirkel 1: Centrum förskjutet -r/2
    x1, y1 = r * np.cos(t) - r/2, r * np.sin(t)
    # Cirkel 2: Centrum förskjutet +r/2
    x2, y2 = r * np.cos(t) + r/2, r * np.sin(t)
    return (x1, y1), (x2, y2)

def rotate_3d(x, y, z, ax, ay, az):
    """Roterar punkter i 3D kring X, Y och Z axlar (i grader)."""
    rad_x, rad_y, rad_z = np.deg2rad(ax), np.deg2rad(ay), np.deg2rad(az)
    
    # Rotation kring X
    if ax != 0:
        y, z = y*np.cos(rad_x) - z*np.sin(rad_x), y*np.sin(rad_x) + z*np.cos(rad_x)
    # Rotation kring Y
    if ay != 0:
        x, z = x*np.cos(rad_y) + z*np.sin(rad_y), -x*np.sin(rad_y) + z*np.cos(rad_y)
    # Rotation kring Z
    if az != 0:
        x, y = x*np.cos(rad_z) - y*np.sin(rad_z), x*np.sin(rad_z) + y*np.cos(rad_z)
        
    return x, y, z

def add_vesica_to_traces(traces, r, color, opacity, rotation=(0,0,0)):
    """Bygger och roterar paret av cirklar och lägger till i listan."""
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
            hoverinfo='none'
        ))

# ============================================================
# BYGG STRUKTUREN (1 → 2 → 4)
# ============================================================

all_traces = []

# Nivå 0: 1 st central Vesica (Radie 6)
add_vesica_to_traces(all_traces, 6.0, "royalblue", 1.0, (0, 0, 0))

# Nivå 1: 2 st Vesicor (Radie 3, vinkelräta)
add_vesica_to_traces(all_traces, 3.0, "crimson", 0.8, (90, 0, 0))
add_vesica_to_traces(all_traces, 3.0, "crimson", 0.8, (0, 90, 0))

# Nivå 2: 4 st Vesicor (Radie 1.5, diagonala)
diagonal_angles = [(45, 45, 0), (45, -45, 0), (-45, 45, 0), (-45, -45, 0)]
for ang in diagonal_angles:
    add_vesica_to_traces(all_traces, 1.5, "green", 0.6, ang)

# ============================================================
# RENDERING OCH EXPORT
# ============================================================

fig = go.Figure(data=all_traces)

fig.update_layout(
    title="RP9 — Sann 3D Vesica Piscis (Skaloberoende Relation)",
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

# Spara som HTML
filename = "vesica_piscis_3d.html"
fig.write_html(filename)

# Visa figuren
fig.show()

print(f"KLART! Om inget fönster öppnades: Öppna filen '{filename}' i din webbläsare.")