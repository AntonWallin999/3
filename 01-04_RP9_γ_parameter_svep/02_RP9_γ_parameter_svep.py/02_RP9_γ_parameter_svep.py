# -*- coding: utf-8 -*-
# ==========================================================
# RP9–γ Parameter-svep: Självstabiliserande geometriskt flöde
# Kräver: numpy, plotly, os, webbrowser, datetime
# Genererar interaktiva visualiseringar och en rapport.html
# ==========================================================

import numpy as np
import plotly.graph_objects as go
import os, webbrowser
from datetime import datetime

# -------------------------------------------------------------
# Hjälpfunktioner
# -------------------------------------------------------------

def norm(v): 
    return float(np.linalg.norm(v))

def unit(v): 
    n = norm(v)
    return v/n if n > 0.0 else v

def skew_x():
    return np.array([[0.0,0.0,0.0],
                     [0.0,0.0,-1.0],
                     [0.0,1.0,0.0]])

def skew_y():
    return np.array([[0.0,0.0,1.0],
                     [0.0,0.0,0.0],
                     [-1.0,0.0,0.0]])

def skew_z():
    return np.array([[0.0,-1.0,0.0],
                     [1.0,0.0,0.0],
                     [0.0,0.0,0.0]])

def projector_perp(g):
    ng2 = float(np.dot(g,g))
    if ng2 == 0.0: 
        return np.eye(3)
    return np.eye(3) - np.outer(g,g)/ng2

def lambda_weights(G,M,rp9):
    b1 = abs(M[0]*G[0]); b2 = abs(M[1]*G[1]); b3 = abs(M[2]*G[2])
    base = np.array([b1+rp9,b2+rp9,b3+rp9])
    s = float(np.sum(base))
    return base/s if s != 0 else np.array([1/3,1/3,1/3])

def omega(M,rp9,G,Ax,Ay,Az):
    lam = lambda_weights(G,M,rp9)
    R1 = Ax.dot(G); R2 = Ay.dot(G); R3 = Az.dot(G)
    return lam[0]*R1 + lam[1]*R2 + lam[2]*R3, lam

def gradV(G,u,r): 
    return (float(np.dot(u,G)) - float(r)) * u

def J_feedback(G,u,r,gamma): 
    return -gamma * projector_perp(G).dot(gradV(G,u,r))

def f_rhs(G,M,rp9,gamma,u,r,Ax,Ay,Az):
    Om, lam = omega(M,rp9,G,Ax,Ay,Az)
    J = J_feedback(G,u,r,gamma)
    return Om + J, lam

def rk4(G,h,f):
    k1,lam1 = f(G)
    k2,lam2 = f(G + 0.5*h*k1)
    k3,lam3 = f(G + 0.5*h*k2)
    k4,lam4 = f(G + h*k3)
    G_next = G + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)
    return G_next, lam4

# -------------------------------------------------------------
# Grundparametrar
# -------------------------------------------------------------

M = np.array([1.0, 0.5, 0.0072973525693])   # ljus, gravitation, finstruktur
Ax, Ay, Az = skew_x(), skew_y(), skew_z()
u = unit(np.array([1.0, 1.0, 1.0]))
r = 0.0
G0 = unit(np.array([0.8, 0.2, 0.55]))
t0, dt, t1 = 0.0, 0.01, 40.0
N = int((t1 - t0) / dt)

# Svepintervall
RP9_values = np.linspace(0.1, 0.9, 9)
gamma_values = np.linspace(0.2, 1.0, 9)

# -------------------------------------------------------------
# Funktion för en körning
# -------------------------------------------------------------

def simulate(RP9, gamma):
    G = G0.copy()
    Is = np.zeros(N+1)
    Vs = np.zeros(N+1)
    Is[0] = float(np.dot(G,G))
    Vs[0] = 0.5 * (float(np.dot(u,G)) - r)**2
    non_mono = 0
    for k in range(N):
        G, lam = rk4(G, dt, lambda G_: f_rhs(G_, M, RP9, gamma, u, r, Ax, Ay, Az))
        Is[k+1] = float(np.dot(G,G))
        Vs[k+1] = 0.5 * (float(np.dot(u,G)) - r)**2
        if k > 0 and Vs[k] > Vs[k-1] + 1e-8:
            non_mono += 1
    max_I_dev = np.max(np.abs(Is - Is[0]))
    return max_I_dev, Vs[-1], non_mono

# -------------------------------------------------------------
# Kör parameter-svepet
# -------------------------------------------------------------

heat_I = np.zeros((len(gamma_values), len(RP9_values)))
heat_V = np.zeros_like(heat_I)
heat_NM = np.zeros_like(heat_I)

for ig, gamma in enumerate(gamma_values):
    for ir, rp in enumerate(RP9_values):
        dI, Vf, Nm = simulate(rp, gamma)
        heat_I[ig, ir] = dI
        heat_V[ig, ir] = Vf
        heat_NM[ig, ir] = Nm
        print(f"RP9={rp:.2f}, gamma={gamma:.2f} -> ΔI={dI:.2e}, V_end={Vf:.3e}, Nm={Nm}")

# -------------------------------------------------------------
# Representativ bana (mittenvärden)
# -------------------------------------------------------------

RP9_mid = RP9_values[len(RP9_values)//2]
gamma_mid = gamma_values[len(gamma_values)//2]
G = G0.copy()
Gs = np.zeros((N+1,3))
Gs[0] = G
for k in range(N):
    G,_ = rk4(G, dt, lambda G_: f_rhs(G_, M, RP9_mid, gamma_mid, u, r, Ax, Ay, Az))
    Gs[k+1] = G

# -------------------------------------------------------------
# Visualiseringar
# -------------------------------------------------------------

out_dir = os.path.abspath("parameter_scan_outputs")
os.makedirs(out_dir, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# --- 1) 3D-bana ---
phi = np.linspace(0.0, 2*np.pi, 80)
theta = np.linspace(0.0, np.pi, 40)
xx = np.outer(np.cos(phi), np.sin(theta))
yy = np.outer(np.sin(phi), np.sin(theta))
zz = np.outer(np.ones_like(phi), np.cos(theta))

surf = go.Surface(x=xx, y=yy, z=zz, opacity=0.15, showscale=False)
traj = go.Scatter3d(x=Gs[:,0], y=Gs[:,1], z=Gs[:,2], mode="lines", name="G(t)", line=dict(color="crimson"))
fig3d = go.Figure([surf, traj])
fig3d.update_layout(
    title=f"Exempelbana RP9={RP9_mid:.2f}, γ={gamma_mid:.2f}",
    scene=dict(xaxis_title="Gx", yaxis_title="Gy", zaxis_title="Gz")
)
html3d = os.path.join(out_dir, "traj3d_" + timestamp + ".html")
fig3d.write_html(html3d, include_plotlyjs="cdn")
fig3d.show()

# --- 2) Heatmaps ---
def heatmap(data, title, zlabel):
    fig = go.Figure(data=go.Heatmap(z=data, x=RP9_values, y=gamma_values, colorscale="Viridis"))
    fig.update_layout(title=title, xaxis_title="RP9", yaxis_title="γ",
                      coloraxis_colorbar=dict(title=zlabel))
    return fig

figI = heatmap(heat_I, "Max |ΔI|", "ΔI")
figV = heatmap(heat_V, "Slutligt Lyapunovvärde V(t₁)", "V_end")
figN = heatmap(heat_NM, "Antal icke-monotona V-steg", "count")

htmlI = os.path.join(out_dir, "heat_I_" + timestamp + ".html")
htmlV = os.path.join(out_dir, "heat_V_" + timestamp + ".html")
htmlN = os.path.join(out_dir, "heat_N_" + timestamp + ".html")
figI.write_html(htmlI, include_plotlyjs="cdn")
figV.write_html(htmlV, include_plotlyjs="cdn")
figN.write_html(htmlN, include_plotlyjs="cdn")

figI.show()
figV.show()
figN.show()

# -------------------------------------------------------------
# Rapport (HTML)
# -------------------------------------------------------------

report_path = os.path.join(out_dir, "RP9_gamma_report_" + timestamp + ".html")

sections = []
sections.append("<h1>RP9–γ Parameter-svep: Självstabiliserande Geometriskt Flöde</h1>")
sections.append("<p>Simulationstid t ∈ [0, 40], dt = 0.01. G₀ normaliserad.<br>"
                "Varje körning mäter ΔI, slutligt V och antal icke-monotona steg.</p>")
sections.append(f"<p>Totalt {len(RP9_values)*len(gamma_values)} simuleringar.<br>"
                f"Max avvikelse ΔI ≈ {np.max(heat_I):.2e}.</p>")
sections.append(f"<p>Resultat sparade i: <b>{out_dir}</b></p>")
sections.append("<ul>"
                f"<li><a href='{os.path.basename(html3d)}'>3D-bana</a></li>"
                f"<li><a href='{os.path.basename(htmlI)}'>ΔI Heatmap</a></li>"
                f"<li><a href='{os.path.basename(htmlV)}'>V(t₁) Heatmap</a></li>"
                f"<li><a href='{os.path.basename(htmlN)}'>Icke-monotona steg</a></li>"
                "</ul>")

with open(report_path, "w", encoding="utf-8") as f:
    f.write("<html><head><meta charset='utf-8'><title>RP9–γ Report</title></head><body>")
    f.write("\n".join(sections))
    f.write("</body></html>")

print("==========================================================")
print("Rapport skapad:", report_path)
print("HTML-filer sparade i:", out_dir)
print("==========================================================")

webbrowser.open("file://" + report_path)
