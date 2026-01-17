# -*- coding: utf-8 -*-
# ==========================================================
# RP9–gamma parameter-svep med adaptiv klassificering av dynamikzoner
# Garanterar minst tre färgområden (stabil, oscill, kaotisk)
# Säkra filnamn och robust webbläsaröppning (ASCII-kompatibla)
# ==========================================================

import numpy as np
import plotly.graph_objects as go
import os, webbrowser, pathlib
from datetime import datetime

# -------------------------------------------------------------
# Hjälpfunktioner
# -------------------------------------------------------------

def norm(v):
    return float(np.linalg.norm(v))

def unit(v):
    n = norm(v)
    return v / n if n > 0.0 else v

def skew_x(): return np.array([[0,0,0],[0,0,-1],[0,1,0]], dtype=float)
def skew_y(): return np.array([[0,0,1],[0,0,0],[-1,0,0]], dtype=float)
def skew_z(): return np.array([[0,-1,0],[1,0,0],[0,0,0]], dtype=float)

def projector_perp(g):
    n2 = float(np.dot(g,g))
    if n2 == 0:
        return np.eye(3)
    return np.eye(3) - np.outer(g,g)/n2

def lambda_weights(G,M,rp9):
    b1=abs(M[0]*G[0]); b2=abs(M[1]*G[1]); b3=abs(M[2]*G[2])
    base=np.array([b1+rp9,b2+rp9,b3+rp9])
    s=float(np.sum(base))
    return base/s if s!=0 else np.array([1/3,1/3,1/3])

def omega(M,rp9,G,Ax,Ay,Az):
    lam=lambda_weights(G,M,rp9)
    return lam[0]*Ax.dot(G)+lam[1]*Ay.dot(G)+lam[2]*Az.dot(G),lam

def gradV(G,u,r): 
    return (float(np.dot(u,G))-float(r))*u

def J_feedback(G,u,r,gamma): 
    return -gamma*projector_perp(G).dot(gradV(G,u,r))

def f_rhs(G,M,rp9,gamma,u,r,Ax,Ay,Az):
    Om,lam=omega(M,rp9,G,Ax,Ay,Az)
    J=J_feedback(G,u,r,gamma)
    return Om+J,lam

def rk4(G,h,f):
    k1,_=f(G)
    k2,_=f(G+0.5*h*k1)
    k3,_=f(G+0.5*h*k2)
    k4,_=f(G+h*k3)
    return G+(h/6.0)*(k1+2*k2+2*k3+k4)

# -------------------------------------------------------------
# Parametrar
# -------------------------------------------------------------

M=np.array([1.0,0.5,0.0072973525693])
Ax,Ay,Az=skew_x(),skew_y(),skew_z()
u=unit(np.array([1.0,1.0,1.0]))
r=0.0
G0=unit(np.array([0.8,0.2,0.55]))
t0,dt,t1=0.0,0.01,40.0
N=int((t1-t0)/dt)

RP9_values=np.linspace(0.05,1.5,15)
gamma_values=np.linspace(0.05,1.5,15)

# -------------------------------------------------------------
# En körning
# -------------------------------------------------------------

def simulate(RP9,gamma):
    G=G0.copy()
    Is=np.zeros(N+1)
    Vs=np.zeros(N+1)
    Is[0]=float(np.dot(G,G))
    Vs[0]=0.5*(float(np.dot(u,G))-r)**2
    non_mono=0
    for k in range(N):
        G=rk4(G,dt,lambda G_:f_rhs(G_,M,RP9,gamma,u,r,Ax,Ay,Az))
        Is[k+1]=float(np.dot(G,G))
        Vs[k+1]=0.5*(float(np.dot(u,G))-r)**2
        if k>0 and Vs[k]>Vs[k-1]+1e-8:
            non_mono+=1
    max_I_dev=np.max(np.abs(Is-Is[0]))
    return max_I_dev,Vs[-1],non_mono

# -------------------------------------------------------------
# Kör svepet
# -------------------------------------------------------------

heat_I=np.zeros((len(gamma_values),len(RP9_values)))
heat_V=np.zeros_like(heat_I)
heat_NM=np.zeros_like(heat_I)

for ig,gamma in enumerate(gamma_values):
    for ir,rp in enumerate(RP9_values):
        dI,Vf,Nm=simulate(rp,gamma)
        heat_I[ig,ir]=dI
        heat_V[ig,ir]=Vf
        heat_NM[ig,ir]=Nm

# -------------------------------------------------------------
# Adaptiv klassificering (garanterar tre zoner)
# -------------------------------------------------------------

low_th  = np.percentile(heat_I, 33)
mid_th  = np.percentile(heat_I, 66)

class_map = np.zeros_like(heat_I)
class_map[heat_I < low_th]  = 2  # stabil
class_map[(heat_I >= low_th) & (heat_I < mid_th)] = 1  # oscill
class_map[heat_I >= mid_th] = 0  # kaos

print("==========================================================")
print("Adaptiva gränser (ΔI):")
print(f"  🟢 Stabil      < {low_th:.2e}")
print(f"  🟡 Oscillerande [{low_th:.2e}, {mid_th:.2e})")
print(f"  🔴 Kaotisk     ≥ {mid_th:.2e}")
print("==========================================================")

# -------------------------------------------------------------
# Visualisering
# -------------------------------------------------------------

out_dir=os.path.abspath("adaptive_classification_outputs")
os.makedirs(out_dir,exist_ok=True)
timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")

# färgskala
colorscale=[
    [0.0,"rgb(220,50,32)"],   # röd
    [0.33,"rgb(255,200,0)"],  # gul
    [0.66,"rgb(60,180,75)"],  # grön
    [1.0,"rgb(60,180,75)"]
]

figC=go.Figure(data=go.Heatmap(
    z=class_map,
    x=RP9_values,
    y=gamma_values,
    colorscale=colorscale,
    colorbar=dict(title="Zon",tickvals=[0,1,2],
                  ticktext=["Kaotisk","Oscillerande","Stabil"])
))
figC.update_layout(
    title="RP9–Gamma Adaptiv Klassificeringskarta (Dynamiska zoner)",
    xaxis_title="RP9",
    yaxis_title="Gamma"
)

htmlC=os.path.join(out_dir,"adaptive_classification_map_"+timestamp+".html")
figC.write_html(htmlC,include_plotlyjs="cdn")
figC.show()

# -------------------------------------------------------------
# Rapport (HTML)
# -------------------------------------------------------------

report=os.path.join(out_dir,"Adaptive_Classification_Report_"+timestamp+".html")
sections=[]
sections.append("<h1>RP9–Gamma Adaptiv Dynamikklassificering</h1>")
sections.append(f"<p><b>Gränser (ΔI):</b><br>"
                f"🟢 Stabil &lt; {low_th:.2e}<br>"
                f"🟡 Oscillerande [{low_th:.2e}, {mid_th:.2e})<br>"
                f"🔴 Kaotisk ≥ {mid_th:.2e}</p>")
sections.append("<p>Kartan använder adaptiva percentiler av ΔI för att "
                "säkerställa minst tre färgzoner.</p>")
sections.append(f"<p>Fil: {os.path.basename(htmlC)}</p>")

with open(report,"w",encoding="utf-8") as f:
    f.write("<html><head><meta charset='utf-8'><title>Adaptiv RP9–Gamma Rapport</title></head><body>")
    f.write("\n".join(sections))
    f.write("</body></html>")

print("Rapport skapad:", report)
print("==========================================================")

# -------------------------------------------------------------
# Säker webbläsaröppning (ASCII-kompatibel)
# -------------------------------------------------------------
report_uri = pathlib.Path(report).resolve().as_uri()
html_uri   = pathlib.Path(htmlC).resolve().as_uri()

print("Öppnar i webbläsare ...")
webbrowser.open_new_tab(html_uri)
webbrowser.open_new_tab(report_uri)
