# -*- coding: utf-8 -*-
# ==========================================================
# 06_Absolut_Konsekvens_Interactive_v2.py
# Co-Creators Foundation © 2025
# Node-lokal fraktal konvergens — RP9
# ==========================================================

import numpy as np
import plotly.graph_objects as go
import os, webbrowser

# -----------------------------
# 1) Parametrar
# -----------------------------
N        = 120
T        = 20.0
frames   = 160
dt       = T / frames
phi_RP9  = 1.5        # exakt konstant
kappa_r  = 0.25
gamma_p  = 0.06
omega0   = 0.0
np.random.seed(137)

# -----------------------------
# 2) Initiera noder i sfärkoordinater
# -----------------------------
r   = 2.8 + 0.2*np.random.randn(N)
th  = np.random.uniform(0, 2*np.pi, N)
ph  = np.random.uniform(0.2, np.pi-0.2, N)
psi = np.random.uniform(0, 2*np.pi, N)

def sph2cart(rr, tt, pp):
    x = rr * np.sin(pp) * np.cos(tt)
    y = rr * np.sin(pp) * np.sin(tt)
    z = rr * np.cos(pp)
    return x, y, z

x, y, z = sph2cart(r, th, ph)
pos0 = np.stack([x, y, z], axis=1)

# -----------------------------
# 3) Kopplingar (resonansnät)
# -----------------------------
D = np.linalg.norm(pos0[:,None,:] - pos0[None,:,:], axis=-1) + np.eye(N)
W = np.exp(-phi_RP9 * D)
np.fill_diagonal(W, 0.0)
W /= (W.sum(axis=1, keepdims=True) + 1e-12)

# -----------------------------
# 4) Dynamik
# -----------------------------
def update_step(r, th, ph, psi, dt):
    psi_loc_mean = W.dot(psi)
    dpsi = omega0 + (W.dot(np.sin(psi[None,:] - psi[:,None]))).diagonal() - gamma_p*(psi - psi_loc_mean)

    omega_th =  0.6*np.sin(psi)
    omega_ph =  0.4*np.cos(psi) / (1.0 + r)

    disson = np.abs(((psi - psi_loc_mean + np.pi) % (2*np.pi)) - np.pi)
    disson = disson / (np.max(disson) + 1e-12)

    a, b = 0.30, 0.70
    decay = kappa_r * (a + b*disson)
    r_new = r * np.exp(-decay*dt)
    th_new = (th + omega_th*dt) % (2*np.pi)
    ph_new = np.clip(ph + omega_ph*dt, 1e-3, np.pi-1e-3)
    psi_new = (psi + dpsi*dt) % (2*np.pi)
    return r_new, th_new, ph_new, psi_new

# -----------------------------
# 5) Sampla frames
# -----------------------------
traj = []
for _ in range(frames):
    x, y, z = sph2cart(r, th, ph)
    color = np.cos(psi)
    traj.append((x.copy(), y.copy(), z.copy(), color.copy()))
    r, th, ph, psi = update_step(r, th, ph, psi, dt)

# -----------------------------
# 6) Bygg figur
# -----------------------------
fig = go.Figure()

# Kopplingar
ex, ey, ez = [], [], []
thr = 0.08
x0, y0, z0, _ = traj[0]
for i in range(N):
    for j in range(i+1, N):
        if W[i,j] > thr:
            ex += [x0[i], x0[j], None]
            ey += [y0[i], y0[j], None]
            ez += [z0[i], z0[j], None]

edges_trace = go.Scatter3d(
    x=ex, y=ey, z=ez,
    mode='lines',
    line=dict(color='rgba(100,150,255,0.18)', width=1),
    hoverinfo='none',
    name='Kopplingar'
)
fig.add_trace(edges_trace)

# Startnoder
x0, y0, z0, c0 = traj[0]
nodes_trace = go.Scatter3d(
    x=x0, y=y0, z=z0,
    mode='markers',
    marker=dict(size=5.5, color=c0, colorscale='Turbo', opacity=0.95),
    name='Noder'
)
fig.add_trace(nodes_trace)

# -----------------------------
# 7) Frames (uppdatera endast nod-trace)
# -----------------------------
fig.frames = [
    go.Frame(
        data=[
            go.Scatter3d(
                x=xk, y=yk, z=zk,
                mode='markers',
                marker=dict(size=5.5, color=ck, colorscale='Turbo', opacity=0.95)
            )
        ],
        name=f"frame{k}"
    )
    for k, (xk, yk, zk, ck) in enumerate(traj)
]

# -----------------------------
# 8) Layout & kontroller
# -----------------------------
fig.update_layout(
    title="🌌 Absolut Konsekvens — Node-lokal koherensdynamik (RP9)",
    template='plotly_dark',
    scene=dict(
        xaxis=dict(title='X', backgroundcolor='black'),
        yaxis=dict(title='Y', backgroundcolor='black'),
        zaxis=dict(title='Z', backgroundcolor='black'),
        aspectmode='cube',
        bgcolor='black'
    ),
    updatemenus=[{
        "type": "buttons",
        "direction": "left",
        "x": 0.1, "y": 0,
        "xanchor": "right", "yanchor": "top",
        "showactive": True,
        "buttons": [
            {
                "label": "▶ Start",
                "method": "animate",
                "args": [None, {
                    "frame": {"duration": 70, "redraw": True},
                    "fromcurrent": True,
                    "transition": {"duration": 0}
                }]
            },
            {
                "label": "⏸ Stop",
                "method": "animate",
                "args": [[None], {"frame": {"duration": 0}, "mode": "immediate"}]
            }
        ]
    }]
)

# -----------------------------
# 9) Export & öppning
# -----------------------------
out_html = os.path.abspath("Absolut_Konsekvens_NodeLocal_v2.html")
fig.write_html(out_html, include_plotlyjs="cdn", auto_open=True)
fig.show()
webbrowser.open("file://" + out_html)

print("\n[OK] Interaktiv node-lokal visualisering skapad:", out_html)
input("\nTryck [ENTER] för att avsluta...")
