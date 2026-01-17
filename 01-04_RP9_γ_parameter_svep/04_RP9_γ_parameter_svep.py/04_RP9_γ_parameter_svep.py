# -*- coding: utf-8 -*-
# ==========================================================
# RP9–Gamma parameter-svep med automatisk tröskelkalibrering,
# klassificering och 3D-banor för stabila zoner
# ==========================================================

import numpy as np
import plotly.graph_objects as go
import os, webbrowser, pathlib
from datetime import datetime

# -------------------------------------------------------------
# Hjälpfunktioner
# -------------------------------------------------------------
def norm(v): return float(np.linalg.norm(v))
def unit(v): n = norm(v); return v/n if n > 0.0 else v

def skew_x(): return np.array([[0,0,0],[0,0,-1],[0,1,0]],dtype=float)
def skew_y(): return np.array([[0,0,1],[0,0,0],[-1,0,0]],dtype=float)
def skew_z(): return np.array([[0,-1,0],[1,0,0],[0,0,0]],dtype=float)

def projector_perp(g):
    n2=float(np.dot(g,g))
    if n2==0: return np.eye(3)
    return np.eye(3)-np.outer(g,g)/n2

def lambda_weights(G,M,rp9):
    b1,b2,b3 = abs(M[0]*G[0]), abs(M[1]*G[1]), abs(M[2]*G[2])
    base = np.array([b1+rp9,b2+rp9,b3+rp9])
    s = float(np.sum(base))
    return base/s if s!=0 else np.array([1/3,1/3,1/3])

def omega(M,rp9,G,Ax,Ay,Az):
    lam = lambda_weights(G,M,rp9)
    return lam[0]*Ax.dot(G)+lam[1]*Ay.dot(G)+lam[2]*Az.dot(G), lam

def gradV(G,u,r): return (float(np.dot(u,G))-float(r))*u
def J_feedback(G,u,r,gamma): return -gamma*projector_perp(G).dot(gradV(G,u,r))

def f_rhs(G,M,rp9,gamma,u,r,Ax,Ay,Az):
    Om,lam = omega(M,rp9,G,Ax,Ay,Az)
    J = J_feedback(G,u,r,gamma)
    return Om+J,lam

def rk4(G,h,f):
    k1,_ = f(G)
    k2,_ = f(G+0.5*h*k1)
    k3,_ = f(G+0.5*h*k2)
    k4,_ = f(G+h*k3)
    return G+(h/6.0)*(k1+2*k2+2*k3+k4)

# -------------------------------------------------------------
# Grundparametrar
# -------------------------------------------------------------
M=np.array([1.0,0.5,0.0072973525693])
Ax,Ay,Az=skew_x(),skew_y(),skew_z()
u=unit(np.array([1.0,1.0,1.0]))
r=0.0
G0=unit(np.array([0.8,0.2,0.55]))
t0,dt,t1=0.0,0.01,40.0
N=int((t1-t0)/dt)
RP9_values=np.linspace(0.1,0.9,9)
gamma_values=np.linspace(0.2,1.0,9)

# -------------------------------------------------------------
# Simulering
# -------------------------------------------------------------
def simulate(RP9,gamma):
    G=G0.copy()
    Is=np.zeros(N+1); Vs=np.zeros(N+1)
    Is[0]=float(np.dot(G,G)); Vs[0]=0.5*(float(np.dot(u,G))-r)**2
    non_mono=0
    for k in range(N):
        G=rk4(G,dt,lambda G_:f_rhs(G_,M,RP9,gamma,u,r,Ax,Ay,Az))
        Is[k+1]=float(np.dot(G,G))
        Vs[k+1]=0.5*(float(np.dot(u,G))-r)**2
        if k>0 and Vs[k]>Vs[k-1]+1e-8: non_mono+=1
    max_I_dev=np.max(np.abs(Is-Is[0]))
    return max_I_dev,Vs[-1],non_mono,Is,Vs,G

# -------------------------------------------------------------
# Kör svepet
# -------------------------------------------------------------
heat_I=np.zeros((len(gamma_values),len(RP9_values)))
heat_V=np.zeros_like(heat_I)
heat_NM=np.zeros_like(heat_I)
class_map=np.zeros_like(heat_I)

all_dI=[]; all_Vf=[]; all_Nm=[]
for ig,gamma in enumerate(gamma_values):
    for ir,rp in enumerate(RP9_values):
        dI,Vf,Nm,Is,Vs,G=simulate(rp,gamma)
        heat_I[ig,ir]=dI; heat_V[ig,ir]=Vf; heat_NM[ig,ir]=Nm
        all_dI.append(dI); all_Vf.append(Vf); all_Nm.append(Nm)

# -------------------------------------------------------------
# Autokalibrering av trösklar
# -------------------------------------------------------------
dI_thr_stable=np.percentile(all_dI,20)
V_thr_stable=np.percentile(all_Vf,20)
Nm_thr_stable=np.percentile(all_Nm,30)

dI_thr_osc=np.percentile(all_dI,70)
V_thr_osc=np.percentile(all_Vf,70)
Nm_thr_osc=np.percentile(all_Nm,60)

print("Auto-trösklar:")
print("ΔI stable <", dI_thr_stable)
print("V stable <", V_thr_stable)
print("N_m stable <", Nm_thr_stable)

# -------------------------------------------------------------
# Klassificering
# -------------------------------------------------------------
def classify(deltaI,V_end,nonmono):
    if deltaI<dI_thr_stable and V_end<V_thr_stable and nonmono<Nm_thr_stable:
        return 2
    elif deltaI<dI_thr_osc or V_end<V_thr_osc or nonmono<Nm_thr_osc:
        return 1
    else:
        return 0

stables=[]
for ig,gamma in enumerate(gamma_values):
    for ir,rp in enumerate(RP9_values):
        dI=heat_I[ig,ir]; Vf=heat_V[ig,ir]; Nm=heat_NM[ig,ir]
        cls=classify(dI,Vf,Nm)
        class_map[ig,ir]=cls
        if cls==2: stables.append((rp,gamma))

# -------------------------------------------------------------
# Visualiseringar
# -------------------------------------------------------------
out_dir=os.path.abspath("auto_classified_outputs")
os.makedirs(out_dir,exist_ok=True)
timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")

def heatmap(data,title,zlabel,log=False):
    Z=np.log10(data+1e-12) if log else data
    fig=go.Figure(data=go.Heatmap(z=Z,x=RP9_values,y=gamma_values,colorscale="Viridis"))
    fig.update_layout(title=title,xaxis_title="RP9",yaxis_title="γ",
                      coloraxis_colorbar=dict(title=zlabel))
    return fig

colorscale=[
    [0.0,"rgb(220,50,32)"],[0.33,"rgb(255,200,0)"],[0.66,"rgb(60,180,75)"],[1.0,"rgb(60,180,75)"]
]
figC=go.Figure(data=go.Heatmap(z=class_map,x=RP9_values,y=gamma_values,colorscale=colorscale,
                               colorbar=dict(title="Zon",tickvals=[0,1,2],
                                             ticktext=["Kaotisk","Oscill.","Stabil"])))
figC.update_layout(title="Klassificeringskarta (autokalibrerad)",xaxis_title="RP9",yaxis_title="γ")

htmlC=os.path.join(out_dir,"classification_map_"+timestamp+".html")
figC.write_html(htmlC,include_plotlyjs="cdn")

heatmap(heat_I,"Max |ΔI| (log10)","ΔI",log=True).write_html(os.path.join(out_dir,"heat_I_"+timestamp+".html"),include_plotlyjs="cdn")
heatmap(heat_V,"Slutligt V (log10)","V_end",log=True).write_html(os.path.join(out_dir,"heat_V_"+timestamp+".html"),include_plotlyjs="cdn")

# -------------------------------------------------------------
# Rapport
# -------------------------------------------------------------
report=os.path.join(out_dir,"Auto_Report_"+timestamp+".html")
sections=[]
sections.append("<h1>RP9–Gamma Dynamikklassificering (Autokalibrerad)</h1>")
sections.append("<p>🟢 Stabil, 🟡 Oscillerande, 🔴 Kaotisk — trösklar baserade på percentiler.</p>")
sections.append(f"<p>Antal stabila zoner: {len(stables)}</p>")
sections.append(f"<p>ΔI-stabil &lt; {dI_thr_stable:.2e}, V-stabil &lt; {V_thr_stable:.2e}, N_m-stabil &lt; {Nm_thr_stable:.1f}</p>")
sections.append(f"<iframe src='{os.path.basename(htmlC)}' width='700' height='600' style='border:1px solid #ccc;'></iframe>")

with open(report,"w",encoding="utf-8") as f:
    f.write("<html><head><meta charset='utf-8'><title>RP9–Gamma Autokalibrerad Rapport</title></head><body>")
    f.write("\n".join(sections))
    f.write("</body></html>")

print("==========================================================")
print("Rapport skapad:", report)
print("Antal stabila zoner:", len(stables))
print("==========================================================")

report_uri=pathlib.Path(report).resolve().as_uri()
webbrowser.open_new_tab(report_uri)
