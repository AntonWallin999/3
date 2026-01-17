# ============================================================
# Project: A Correct Relation to Information
# Subproject: Establish M.P.S_010
# ID (002)
# Code Block Nr: 34
# Code Block Name: Prime Flower 2D
# Focus: Golden Ratio / Prime Points
# License: (CC BY-NC-ND)
# Created by: Anton Wallin
# ============================================================

import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import os

# ============================================================
# PARAMETRAR
# ============================================================
N_primtal = 1000
alpha = 0.5
beta = 0.3

phi = (1.0 + np.sqrt(5.0)) / 2.0
pi = np.pi

# ============================================================
# PRIMTAL (INGEN SYMPY)
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

primtal = generate_primes(N_primtal)

# ============================================================
# BALANSERINGSTER M
# ============================================================
balanseringsterm = np.diff(primtal, prepend=0.0)

# ============================================================
# POLÄRA KOORDINATER
# ============================================================
radii = (
    np.sqrt(pi) * (primtal ** alpha)
    + phi * (primtal ** beta)
    + balanseringsterm
)

theta = primtal * phi

# ============================================================
# KARTESISKA KOORDINATER
# ============================================================
x = radii * np.cos(theta)
y = radii * np.sin(theta)

# ============================================================
# FIGUR
# ============================================================
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="markers",
    marker=dict(
        size=6,
        color=primtal,
        colorscale="Plasma",
        showscale=True,
        colorbar=dict(title="Primtal"),
        line=dict(color="black", width=0.5),
        opacity=0.85
    ),
    hovertemplate=(
        "Primtal: %{marker.color:.0f}<br>"
        "x: %{x:.3f}<br>"
        "y: %{y:.3f}<extra></extra>"
    ),
    name="Prime Flower"
))

# ============================================================
# LAYOUT
# ============================================================
fig.update_layout(
    title="Prime Flower — 2D (1000 Primtal)",
    template="plotly_dark",
    xaxis=dict(title="X", zeroline=False),
    yaxis=dict(
        title="Y",
        zeroline=False,
        scaleanchor="x",
        scaleratio=1
    ),
    margin=dict(l=60, r=60, t=60, b=60)
)

# ============================================================
# EXPORT → HTML (GARANTERAD)
# ============================================================
output_file = "MPS_010_Prime_Flower_2D.html"

pio.write_html(
    fig,
    file=output_file,
    include_plotlyjs=True,
    full_html=True,
    auto_open=True
)

print("KLART – HTML skapad:", os.path.abspath(output_file))
