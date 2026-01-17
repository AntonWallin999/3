# ============================================================
# Project: A Correct Relation to Information
# Subproject: Establish M.P.S_010
# ID (002)
# Code Block Nr: 41
# Code Block Name: Prime Flower 3D
# Focus: Golden Ratio / 6 Torsos / 3D
# License: (CC BY-NC-ND)
# Created by: Anton Wallin
# Sigil: - = ( o ) = -
# ============================================================

import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import os

# ============================================================
# PRIMTAL
# ============================================================
def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        lim = int(np.sqrt(num)) + 1
        for i in range(2, lim):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return np.array(primes, dtype=float)

# ============================================================
# DATA
# ============================================================
prime_count = 1000
primes = generate_primes(prime_count)

theta = primes * np.pi / 180.0
r = np.sqrt(primes)

# Z-axel
z_up = r
z_down = -r

# ============================================================
# FIGUR
# ============================================================
fig = go.Figure()

# Lodräta torsos (Z)
fig.add_trace(go.Scatter3d(
    x=r * np.cos(theta),
    y=r * np.sin(theta),
    z=z_up,
    mode="markers",
    marker=dict(size=3, color="blue", opacity=0.8),
    name="Prime Flower (Uppåt)"
))

fig.add_trace(go.Scatter3d(
    x=r * np.cos(theta),
    y=r * np.sin(theta),
    z=z_down,
    mode="markers",
    marker=dict(size=3, color="red", opacity=0.8),
    name="Prime Flower (Nedåt)"
))

# Vågräta torsos – X-axel
fig.add_trace(go.Scatter3d(
    x=r,
    y=r * np.cos(theta),
    z=r * np.sin(theta),
    mode="markers",
    marker=dict(size=3, color="green", opacity=0.8),
    name="Prime Flower (Vänster)"
))

fig.add_trace(go.Scatter3d(
    x=-r,
    y=r * np.cos(theta),
    z=r * np.sin(theta),
    mode="markers",
    marker=dict(size=3, color="orange", opacity=0.8),
    name="Prime Flower (Höger)"
))

# Vågräta torsos – Y-axel
fig.add_trace(go.Scatter3d(
    x=r * np.cos(theta),
    y=r,
    z=r * np.sin(theta),
    mode="markers",
    marker=dict(size=3, color="purple", opacity=0.8),
    name="Prime Flower (Framåt)"
))

fig.add_trace(go.Scatter3d(
    x=r * np.cos(theta),
    y=-r,
    z=r * np.sin(theta),
    mode="markers",
    marker=dict(size=3, color="cyan", opacity=0.8),
    name="Prime Flower (Bakåt)"
))

# ============================================================
# LAYOUT
# ============================================================
fig.update_layout(
    title="Prime Flower 3D — 6 Torsos (M.P.S_010)",
    template="plotly_dark",
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode="data",
        bgcolor="black"
    ),
    paper_bgcolor="black",
    plot_bgcolor="black",
    legend=dict(font=dict(color="white")),
    margin=dict(l=0, r=0, t=50, b=0)
)

# ============================================================
# EXPORT → HTML
# ============================================================
output_file = "MPS_010_Prime_Flower_3D_6_Torsos.html"
pio.write_html(
    fig,
    file=output_file,
    include_plotlyjs=True,
    full_html=True,
    auto_open=True
)

print("KLART – HTML skapad:", os.path.abspath(output_file))
