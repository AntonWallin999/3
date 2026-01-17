---
primary_id: geom_4_plus_1
primary_title: "4+1-geometrin"
primary_language: sv
primary_version: "1.0"

primary_kind: non-ground
primary_category: geometric_bridge
primary_document_role: structural_model

primary_reading_part: 2
primary_reading_label: "2D brygga"

primary_epistemic_level: 2

primary_axiomatic_introduces_axiom: false
primary_axiomatic_causal_force: geometric_realization
primary_axiomatic_dependency:
  - axiom_R0

primary_status: locked
primary_change_policy: frozen
primary_scope: internal

primary_invariants:
  - vesica_piscis
  - sqrt_2
  - phi_duality
---



## 4+1-geometrin



## 1) 4+1-geometrin (halva–halva som 2-D-brygga)




* Yttercentrumen ligger i kvadrat på koordinaterna $(\pm a,\pm a)$; avståndet till origo är $L=\sqrt{a^2+a^2}=a\sqrt{2}$. Centercirkeln har radie $R_c=a\sqrt{2}$, så dess rand går genom alla fyra yttercentra (medvetet vald likhet $L=R_c$ i din konstruktion). Åtta tillståndspunkter skapas på varje radie origo$\to$yttercentrum: $(+)$ via $(x,y)=(c_x,c_y)+r\cdot\frac{(c_x,c_y)}{L}$ och $(-)$ via $(x,y)=(c_x,c_y)-r\cdot\frac{(c_x,c_y)}{L}$. Detta ger åtta lägen totalt (två per yttercirkel) i ett 4+1-läge. Halva–halva manifesteras både ortogonalt $(+)$ och diagonalt $(\times)$ som två symmetriaxlar över samma kvadratiska ram.

## 2) Sekundärt axiom (orsak $\leftrightarrow$ verkan) och två $\varphi$

* Den fundamentala dualiteten är att den inre symmetriska koden är orsak och den yttre asymmetriska expansionen är verkan: $\phi_{\text{sym}}=1.5$ (exakt) och $\phi_{\text{asym}}\approx1.61803398875$ (Golden Ratio-grenen). Detta är inte en härledning utan ett sekundärt axiom i modellen, dvs. en accepterad grundsats som driver dynamiken.
* Bryggspänningen används som en explicit länk: $\sqrt{\pi}_{\text{sym}}=\frac{\phi_{\text{sym}}}{\ln 2}$ och $\sqrt{\pi}_{\text{asym}}=\frac{\phi_{\text{asym}}}{\ln 2}$, dvs. en bro mellan de två spåren.

## 3) #symetriseras som kvadratisk kvantisering (4 samtidiga tillstånd per kod)

* Varje kod hålls i fyra samtidiga tillstånd:
  1. cirkulär/symmetrisk $\to \phi_{\text{sym}}=1.5$
  2. cirkulär/asymmetrisk $\to \phi_{\text{asym}}\approx1.618$
  3. linjär/asymmetrisk $\to$ Fibonacci-kvot $F_{n+1}/F_n\to\phi_{\text{asym}}$
  4. linjär/symmetrisk $\to$ symmetrisk sekvens med kvot $\to\phi_{\text{sym}}$
* Alla fyra potentialer bibehålls samtidigt som ett komplett spektrum. Ett tillstånd kan bestämma de andra tre (deterministisk karta), men operativt är det bättre att hålla alla fyra explicita för spårbarhet, batch-analys och konsekvent transformering.

## 4) Halva–halva som fasbrygga (21.5 $\leftrightarrow$ 21 med 7 som rotationsport)

* I fasläsningen är kodnivå och manifestation två läsningar av samma spiralflöde, där $7$ fungerar som rotationsnod/port. Detta är inte approximation vs korrekthet, utan två faslägen av samma struktur.

---

## Exakt ankare och låsning av asymmetri i 4+1-modellen

### Definiera ett mätbart asymmetrigradmått på varje radie

* Längs en given origo$\to$centrum-linje har tillstånden radier $L+r$ och $L-r$ med $L=a\sqrt{2}$. Ett dimensionslöst asymmetriförhållande är då $\kappa=\frac{L+r}{L-r}$. Detta är strikt $>1$ för $r>0$ och fångar hur mycket utåt-läget dominerar över inåt-läget.

### Låsning mot $\phi$-dualiteten

* Välj låsvillkoret $\kappa=\frac{\phi_{\text{asym}}}{\phi_{\text{sym}}}$. Då fås (löst för $r$):
  
  $r=L\cdot\frac{\kappa-1}{\kappa+1}=a\sqrt{2}\cdot\frac{\frac{\phi_{\text{asym}}}{\phi_{\text{sym}}}-1}{\frac{\phi_{\text{asym}}}{\phi_{\text{sym}}}+1}$

  Med $\phi_{\text{sym}}=1.5$ och $\phi_{\text{asym}}\approx1.61803398875$ blir $\kappa\approx1.0786893$ och därmed:

  $\frac{r}{L}\approx0.03786,\quad r\approx0.03786\,a\sqrt{2}\approx0.05357\,a$

  Detta ger ett exakt geometriskt ankare som binder asymmetrin till $\phi$-dualiteten i en halva–halva-ram.

### Alternativa lås (mot bryggspänningen)

* Använd bryggan $\sqrt{\pi}=\frac{\phi}{\ln 2}$ och lås t.ex.:

  $\frac{L+r}{L}=\frac{\sqrt{\pi}_{\text{asym}}}{\sqrt{\pi}_{\text{sym}}} \;\Rightarrow\; r=L\left(\frac{\phi_{\text{asym}}}{\phi_{\text{sym}}}-1\right)\Big/\ln 2$

  eller kräva att $(L+r)(L-r)=\text{konstant}$ per kod och sätta konstanten på $\sqrt{\pi}$-skala.

---

## Slutsats (koncis)

* 4+1-geometrin är 2-D-bryggan där halva–halva organiserar symmetri–asymmetri.
* Två $\phi$ utgör ett sekundärt axiom (orsak$\to$verkan).
* #symetriseras håller fyra samtidiga tillstånd per kod.
* Asymmetrin kan låsas exakt genom att sätta $\kappa=\frac{L+r}{L-r}$ lika med $\frac{\phi_{\text{asym}}}{\phi_{\text{sym}}}$, vilket ger ett slutet uttryck för $r$ i termer av $a$ och dualiteten.




#### DMC vs. yttercirklar: vinklar, procent och “1–2–4”

**Utgångsläge i din 4+1-struktur:**  
DMC (centrercirkeln) har radie $R=d=a\sqrt{2}$ och varje yttercirkel har radie $r$ samt centrumavstånd till origo $d=a\sqrt{2}$. De två cirklarna (DMC och en viss yttercirkel) skär varandra i en lins. På yttercirkeln är den skurna sektorvinkeln
$\theta_r = 2\arccos\!\Big(\frac{r}{2d}\Big)$, med $d=a\sqrt{2}$.

Detta låter dig räkna allt du frågar efter:

* **Singulärt (1 cirkel):** skuren vinkelandel av $360^\circ$ är $\frac{\theta_r}{2\pi}$, alltså i procent  
$\text{andel}_{1}(\%) = 100\cdot \frac{\theta_r}{2\pi} = 100\cdot \frac{\,2\arccos\!\big(\frac{r}{2d}\big)\,}{2\pi}$.

* **Binärt (2 cirklar, valfritt par):** total skuren vinkel över två cirklar är $2\theta_r$, så  
$\text{andel}_{2}(\%) = 100\cdot \frac{2\theta_r}{2\pi} = 100\cdot \frac{\,2\cdot 2\arccos\!\big(\frac{r}{2d}\big)\,}{2\pi}$.

* **Kvant (4 cirklar):** totalen är $4\theta_r$, dvs.  
$\text{andel}_{4}(\%) = 100\cdot \frac{4\theta_r}{2\pi} = 100\cdot \frac{\,4\cdot 2\arccos\!\big(\frac{r}{2d}\big)\,}{2\pi}$.

Detta svarar även mot summering i grader: $360^\circ$ (singulärt), $720^\circ$ (binärt), $1440^\circ$ (kvant) — helt styrt av samma $\theta_r$.

**Om du vill lösa för $r$ givet en målvinkel över $N\in\{1,2,4\}$ cirklar:**  
Sätt $N\theta_r=\Theta$ (i radianer eller grader) och lös
$r = 2d\cos\!\Big(\frac{\Theta}{2N}\Big)$, där $d=a\sqrt{2}$.  
Detta är den generella kompressorn från $4\to2\to1$.

---

## “Trea”-fenomenet (240° × 2 och 120° × 2)

Om du vill att två cirklar tillsammans ska bära $240^\circ$ (dvs. $2\theta_r=240^\circ$), då måste
$\theta_r = 120^\circ \Rightarrow 2\arccos\!\Big(\frac{r}{2d}\Big) = 120^\circ \Rightarrow \frac{r}{2d} = \cos 60^\circ = \frac{1}{2} \Rightarrow r = d = a\sqrt{2}$.

Precis i detta läge uppstår “tre-geometrin” i den mening som beskrivs: den binära summeringen ger $240^\circ$ och komplementet ger $120^\circ$, vilket återskapar symmetri–asymmetri-polarisering ($240$ som jämn/halva–halva och $120$ som tredelad/primär). För fyra cirklar blir totalsumman $4\theta_r=480^\circ$ när $r=d$, vilket är $240^\circ\times 2$ och konsistent med bin–bin-läsningen.

---

## Arealprocent (DMC:s avklipp på en yttercirkel)

Linsarean för två cirklar med centrumavstånd $d$ och radier $r$ (ytter) och $R$ (DMC) är
$A = r^2\arccos\!\Big(\frac{d^2+r^2-R^2}{2dr}\Big) + R^2\arccos\!\Big(\frac{d^2+R^2-r^2}{2dR}\Big) - \frac{1}{2}\sqrt{(-d+r+R)(d+r-R)(d-r+R)(d+r+R)}$.

I 4+1-geometrin gäller $R=d$, vilket förenklar till
$A = r^2\arccos\!\Big(\frac{r}{2d}\Big) + d^2\arccos\!\Big(1-\frac{r^2}{2d^2}\Big) - \frac{1}{2}\,r\sqrt{4d^2-r^2}$.

Arealandelen av en yttercirkel (i procent) blir då
$\text{areaandel}_{1}(\%) = 100\cdot \frac{A}{\pi r^2}$.  
För två respektive fyra cirklar multipliceras med $2$ respektive $4$ (symmetrin gör att zonerna inte överlappar).

---

## Sammanfattning

1. Ankarekvationen är en kompakt, exakt nyckelrelation som binder asymmetri till $\phi$-dualiteten inom halva–halva.
2. Vinkelbasen $\theta_r=2\arccos\!\big(\frac{r}{2a\sqrt{2}}\big)$ ger direkt 1–2–4 (singulärt–binärt–kvant) i grader och procent.
3. “3”:an uppträder exakt vid $r=d=a\sqrt{2}$, då $\theta_r=120^\circ$ och summor blir $240^\circ$ (med komplement $120^\circ$).
4. Areamåttet har en sluten form som följer samma parametrisering.



4+1_vinkel_och_area_aktuella.csv

Beräkningarna följer exakt:
- $d=a\sqrt{2}$
- $\theta_r=2\arccos\!\big(\frac{r}{2d}\big)$
- \% vinkel per cirkel $=\;100\cdot\frac{\theta_r}{2\pi}$
- Linsarea (med $R=d$):
  $A=r^2\arccos\!\big(\frac{r}{2d}\big)+d^2\arccos\!\big(1-\frac{r^2}{2d^2}\big)-\frac{1}{2}\,r\sqrt{4d^2-r^2}$
- \% area per cirkel $=\;100\cdot\frac{A}{\pi r^2}$




````python
# -*- coding: utf-8 -*-
"""
Interaktiv 4+1-cirkelmodell med 8 lägen (#symetriseras)
- Två sliders: a (yttercentrums kvadrathalva) och r (yttercirklars radie)
- All geometri uppdateras i realtid: centercirkel (R_c = a*√2), 4 yttercirklar, 8 tillståndspunkter (+/–)
- Exakt relationsgeometri (ingen approximation i konstruktionen)
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, CheckButtons

# -----------------------------
# Geometriska hjälp-funktioner
# -----------------------------
def central_radius(a: float) -> float:
    # $R_c = a\sqrt{2}$
    return a * math.sqrt(2.0)

def outer_centers(a: float):
    # fyra yttercentrums: $(\pm a,\pm a)$
    return [(+a, +a), (+a, -a), (-a, +a), (-a, -a)]

def state_points_for_outer_circle(cx: float, cy: float, r: float, idx: int):
    """
    Två tillstånd på varje yttercirkel längs linjen origo↔centrum:
    '+' = utåt från centrum (förlängning från origo), '-' = inåt mot origo.
    """
    L = math.hypot(cx, cy)
    ux, uy = (cx / L, cy / L) if L != 0 else (1.0, 0.0)

    x_plus  = cx + r * ux
    y_plus  = cy + r * uy
    x_minus = cx - r * ux
    y_minus = cy - r * uy

    return (x_plus, y_plus, f"C{idx}(+)"), (x_minus, y_minus, f"C{idx}(-)")

# -----------------------------
# Ritfunktion (en enda källa)
# -----------------------------
def draw_scene(ax, a, r, show_labels=True):
    ax.clear()
    ax.set_aspect("equal", adjustable="box")

    # parametrisk cirkel
    theta = np.linspace(0, 2*np.pi, 512)

    # centercirkel: $R_c=a\sqrt{2}$
    Rc = central_radius(a)
    xC = Rc * np.cos(theta)
    yC = Rc * np.sin(theta)
    ax.plot(xC, yC, color="#ff7f0e", lw=2, label="Centercirkel ($R_c=a\\sqrt{2}$)")

    # yttercirklar + centra
    centers = outer_centers(a)
    for i, (cx, cy) in enumerate(centers, start=1):
        x = cx + r * np.cos(theta)
        y = cy + r * np.sin(theta)
        ax.plot(x, y, color="#1f77b4", lw=2, label="Yttercirklar" if i == 1 else None)
        ax.plot(cx, cy, "o", color="#1f77b4")

    # åtta tillståndspunkter (+/–)
    xs_plus, ys_plus, lab_plus = [], [], []
    xs_minus, ys_minus, lab_minus = [], [], []
    for i, (cx, cy) in enumerate(centers, start=1):
        (xp, yp, lp), (xm, ym, lm) = state_points_for_outer_circle(cx, cy, r, i)
        xs_plus.append(xp);  ys_plus.append(yp);  lab_plus.append(lp)
        xs_minus.append(xm); ys_minus.append(ym); lab_minus.append(lm)

    ax.plot(xs_plus, ys_plus, "o", color="#2ca02c", ms=8, label="Tillstånd (+)")
    ax.plot(xs_minus, ys_minus, "o", color="#d62728", ms=8, label="Tillstånd (−)")

    if show_labels:
        for x,y,t in zip(xs_plus, ys_plus, lab_plus):
            ax.text(x, y, f" {t}", color="#2ca02c", va="center", ha="left", fontsize=9)
        for x,y,t in zip(xs_minus, ys_minus, lab_minus):
            ax.text(x, y, f" {t}", color="#d62728", va="center", ha="left", fontsize=9)

    # axlar och gränser
    limit = max(Rc + r, abs(a) + r) + 0.5
    ax.axhline(0, color="#888888", lw=1, alpha=0.5)
    ax.axvline(0, color="#888888", lw=1, alpha=0.5)
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_title("4+1-cirkelmodell med 8 lägen (#symetriseras)")
    ax.legend(loc="upper right")

# -----------------------------
# Interaktiv setup (Matplotlib)
# -----------------------------
# startvärden
a0 = 1.0
r0 = 1.0
show_labels0 = True

fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(left=0.1, right=0.95, bottom=0.2)

draw_scene(ax, a0, r0, show_labels=show_labels0)

# sliders
ax_a = plt.axes([0.10, 0.10, 0.80, 0.03])
ax_r = plt.axes([0.10, 0.06, 0.80, 0.03])
s_a = Slider(ax_a, "a", 0.2, 3.0, valinit=a0, valstep=0.01)
s_r = Slider(ax_r, "r", 0.2, 3.0, valinit=r0, valstep=0.01)

# checkbutton för etiketter
ax_chk = plt.axes([0.10, 0.015, 0.20, 0.04])
chk = CheckButtons(ax_chk, ["Visa etiketter"], [show_labels0])

state = {"show_labels": show_labels0}

def on_update(val):
    draw_scene(ax, s_a.val, s_r.val, show_labels=state["show_labels"])
    fig.canvas.draw_idle()

def on_toggle(label):
    state["show_labels"] = not state["show_labels"]
    draw_scene(ax, s_a.val, s_r.val, show_labels=state["show_labels"])
    fig.canvas.draw_idle()

s_a.on_changed(on_update)
s_r.on_changed(on_update)
chk.on_clicked(on_toggle)

plt.show()
````




