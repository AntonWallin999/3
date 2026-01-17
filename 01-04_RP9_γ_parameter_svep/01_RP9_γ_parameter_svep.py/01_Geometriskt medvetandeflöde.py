# -*- coding: utf-8 -*-
# ==========================================================
# Geometriskt medvetandeflöde – RP9-modulerad helixsimulator
# ----------------------------------------------------------
# Innehåll:
# 1. Konstanter & initialisering
# 2. Dynamik: RP9, Lyapunov-feedback, RK4
# 3. Kör simulering
# 4. Visualisera resultat (3D-bana, V(t), λ-vikter)
# ==========================================================

import numpy as np
import plotly.graph_objects as go
import os, webbrowser
from datetime import datetime

# ==========================================================
# 1. Hjälpfunktioner
# ==========================================================

def norm(v):
    return float(np.linalg.norm(v))

def unit(v):
    n = norm(v)
    return v / n if n > 1e-12 else np.zeros_like(v)

def skew_x():
    return np.array([[0.0, 0.0, 0.0],
                     [0.0, 0.0, -1.0],
                     [0.0, 1.0,  0.0]])

def skew_y():
    return np.array([[0.0, 0.0,  1.0],
                     [0.0, 0.0,  0.0],
                     [-1.0, 0.0, 0.0]])

def skew_z():
    return np.array([[0.0, -1.0, 0.0],
                     [1.0,  0.0, 0.0],
                     [0.0,  0.0, 0.0]])

def projector_perp(g):
    ng2 = float(np.dot(g, g))
    if ng2 == 0.0:
        return np.eye(3)
    ggT = np.outer(g, g) / ng2
    return np.eye(3) - ggT

def lambda_weights(G, M, rp9):
    b1 = abs(M[0] * G[0])
    b2 = abs(M[1] * G[1])
    b3 = abs(M[2] * G[2])
    base = np.array([b1 + rp9, b2 + rp9, b3 + rp9], dtype=float)
    s = float(np.sum(base))
    if s == 0.0:
        return np.array([1/3, 1/3, 1/3])
    return base / s

def omega(M, rp9, G, Ax, Ay, Az):
    lam = lambda_weights(G, M, rp9)
    R1 = Ax.dot(G)
    R2 = Ay.dot(G)
    R3 = Az.dot(G)
    return lam[0]*R1 + lam[1]*R2 + lam[2]*R3, lam

def gradV(G, u, r):
    return (float(np.dot(u, G)) - float(r)) * u

def J_feedback(G, u, r, gamma):
    P = projector_perp(G)
    return -gamma * P.dot(gradV(G, u, r))

def f_rhs(t, G, M, rp9, gamma, u, r, Ax, Ay, Az):
    Om, lam = omega(M, rp9, G, Ax, Ay, Az)
    J = J_feedback(G, u, r, gamma)
    return Om + J, lam

def rk4_step(t, y, h, deriv):
    k1, lam1 = deriv(t, y)
    k2, lam2 = deriv(t + 0.5*h, y + 0.5*h*k1)
    k3, lam3 = deriv(t + 0.5*h, y + 0.5*h*k2)
    k4, lam4 = deriv(t + h, y + h*k3)
    y_next = y + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)
    return y_next, lam4

# ==========================================================
# 2. Parametrar
# ==========================================================

# Grundkonstanter
M = np.array([1.0, 0.5, 0.0072973525693], dtype=float)  # ljus, gravitation, finstruktur
rp9 = 0.009          # RP9-modulator (rörelsens fasrest)
gamma = 0.25         # Lyapunov-feedback
r = 1.0              # referensradie
u = np.array([1.0, 0.0, 0.0])  # riktning

# Initialisering
G0 = np.array([0.2, 0.9, 0.3], dtype=float)
t0, tmax, dt = 0.0, 200.0, 0.05

# Matrisgeneratorer
Ax, Ay, Az = skew_x(), skew_y(), skew_z()

# ==========================================================
# 3. Simulering (RK4)
# ==========================================================

ts, Gs, Vs, Lams = [], [], [], []
G = G0.copy()
t = t0

while t < tmax:
    def deriv(tt, GG):
        return f_rhs(tt, GG, M, rp9, gamma, u, r, Ax, Ay, Az)
    G, lam = rk4_step(t, G, dt, deriv)
    t += dt
    Gs.append(G)
    Lams.append(lam)
    ts.append(t)
    Vs.append(0.5 * (np.dot(u, G) - r)**2)

Gs = np.array(Gs)
Lams = np.array(Lams)
Vs = np.array(Vs)
ts = np.array(ts)

# Invariansavvikelse
I_dev = np.abs(np.linalg.norm(Gs, axis=1) - np.linalg.norm(Gs[0]))
max_I_dev = np.max(I_dev)
non_monotone_V = np.sum(np.diff(Vs) > 1e-8)

print("==========================================================")
print(" Max |I(G)-I(G0)|:", max_I_dev)
print(" Antal icke-monotona V-steg (>1e-8):", non_monotone_V)
print("==========================================================")

# ==========================================================
# 4. Visualiseringar
# ==========================================================

out_dir = os.path.abspath("simulation_outputs")
os.makedirs(out_dir, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# --- 4.1 Sfärisk bana
phi = np.linspace(0.0, 2*np.pi, 80)
theta = np.linspace(0.0, np.pi, 40)
xx = np.outer(np.cos(phi), np.sin(theta))
yy = np.outer(np.sin(phi), np.sin(theta))
zz = np.outer(np.ones_like(phi), np.cos(theta))

surf = go.Surface(x=xx, y=yy, z=zz, opacity=0.2, showscale=False, name="Sfär ||G||=1")

traj = go.Scatter3d(x=Gs[:,0], y=Gs[:,1], z=Gs[:,2], mode="lines",
                    line=dict(color="crimson", width=4), name="G(t)")
start_pt = go.Scatter3d(x=[Gs[0,0]], y=[Gs[0,1]], z=[Gs[0,2]],
                        mode="markers", marker=dict(size=6, color="green"), name="Start")
end_pt = go.Scatter3d(x=[Gs[-1,0]], y=[Gs[-1,1]], z=[Gs[-1,2]],
                      mode="markers", marker=dict(size=6, color="blue"), name="Slut")

fig3d = go.Figure(data=[surf, traj, start_pt, end_pt])
fig3d.update_layout(
    title="Geometriskt flöde på bevarad sfär: dG/dt = Ω + J",
    scene=dict(xaxis_title="Gx", yaxis_title="Gy", zaxis_title="Gz")
)
fig3d.show()
html3d = os.path.join(out_dir, f"geom_flow_3d_{timestamp}.html")
fig3d.write_html(html3d, include_plotlyjs="cdn")
webbrowser.open("file://" + html3d)

# --- 4.2 Lyapunov-potential och invarians
figV = go.Figure()
figV.add_trace(go.Scatter(x=ts, y=Vs, mode="lines", name="V(t)", line=dict(color="orange")))
figV.add_trace(go.Scatter(x=ts, y=I_dev, mode="lines", name="|I(G)-I(G0)|", line=dict(color="gray")))
figV.update_layout(
    title="Lyapunov-potential V(t) och invariansavvikelse |I(G)-I(G0)|",
    xaxis_title="Tid t", yaxis_title="Värde"
)
figV.show()
htmlV = os.path.join(out_dir, f"lyapunov_invariant_{timestamp}.html")
figV.write_html(htmlV, include_plotlyjs="cdn")
webbrowser.open("file://" + htmlV)

# --- 4.3 Lambda-vikter
figL = go.Figure()
figL.add_trace(go.Scatter(x=ts, y=Lams[:,0], mode="lines", name="λ₁ (x-rot)"))
figL.add_trace(go.Scatter(x=ts, y=Lams[:,1], mode="lines", name="λ₂ (y-rot)"))
figL.add_trace(go.Scatter(x=ts, y=Lams[:,2], mode="lines", name="λ₃ (z-rot)"))
figL.update_layout(
    title="RP9-modulerade kopplingsvikter λᵢ(t)",
    xaxis_title="Tid t", yaxis_title="λ"
)
figL.show()
htmlL = os.path.join(out_dir, f"lambda_weights_{timestamp}.html")
figL.write_html(htmlL, include_plotlyjs="cdn")
webbrowser.open("file://" + htmlL)

# ==========================================================
# 5. Sammanfattning
# ==========================================================
print("Utdatamapp:", out_dir)
print("HTML-filer sparade:")
print(" -", html3d)
print(" -", htmlV)
print(" -", htmlL)
print("[SESSION CLOSED SUCCESSFULLY]")
