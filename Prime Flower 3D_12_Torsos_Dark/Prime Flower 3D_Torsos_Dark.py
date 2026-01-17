# ============================================================
# Project: A Correct Relation to Information
# Subproject: Establish M.P.S_010
# ID (002)
# Code Block Nr: 45
# Code Block Name: Prime Flower 3D
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

# ============================================================
# 6 AXIALA TORSOS (ORIGINAL)
# ============================================================
original_coords = {
    "Up":        ( r * np.cos(theta),  r * np.sin(theta),  r),
    "Down":      ( r * np.cos(theta),  r * np.sin(theta), -r),
    "Left":      ( r,  r * np.cos(theta),  r * np.sin(theta)),
    "Right":     (-r,  r * np.cos(theta),  r * np.sin(theta)),
    "Forward":   ( r * np.cos(theta),  r,  r * np.sin(theta)),
    "Backward":  ( r * np.cos(theta), -r,  r * np.sin(theta)),
}

# ============================================================
# BINBIN-TRANSFORMATION (180° inversion)
# ============================================================
def binbin_transform(x, y, z):
    return -x, -y, -z

# ============================================================
# FÄRGER
# ============================================================
original_colors = {
    "Up": "#00CCFF",
    "Down": "#FF6699",
    "Left": "#00FF99",
    "Right": "#FFCC00",
    "Forward": "#CC66FF",
    "Backward": "#FF9933",
}

inverted_colors = {
    "Up": "#006699",
    "Down": "#99334D",
    "Left": "#006644",
    "Right": "#997A00",
    "Forward": "#663399",
    "Backward": "#994D1A",
}

# ============================================================
# FIGUR
# ============================================================
fig = go.Figure()

# Originala torsos
for label, (x, y, z) in original_coords.items():
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode="markers",
        marker=dict(
            size=3,
            color=original_colors[label],
            opacity=0.85,
            line=dict(color="white", width=1)
        ),
        name=f"{label} (Original)"
    ))

# BinBin-speglade torsos
for label, (x, y, z) in original_coords.items():
    bx, by, bz = binbin_transform(x, y, z)
    fig.add_trace(go.Scatter3d(
        x=bx, y=by, z=bz,
        mode="markers",
        marker=dict(
            size=3,
            color=inverted_colors[label],
            opacity=0.85,
            line=dict(color="white", width=1)
        ),
        name=f"{label} (BinBin)"
    ))

# ============================================================
# LAYOUT
# ============================================================
fig.update_layout(
    title="Prime Flower 3D — Original + BinBin Reflected Axial Torsos",
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
output_file = "MPS_010_Prime_Flower_3D.html"
pio.write_html(
    fig,
    file=output_file,
    include_plotlyjs=True,
    full_html=True,
    auto_open=True
)

print("KLART – HTML skapad:", os.path.abspath(output_file))
