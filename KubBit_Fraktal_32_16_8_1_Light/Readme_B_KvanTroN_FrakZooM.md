

# README — B_KvanTroN_FrakZooM.py

## *Rekursiv skalbar kubbit (8ⁿ moduler)*

---

## Dokumentets status

Denna kod är ett **rekursivt visualiserings- och verifieringsskript** för RP9:s fraktala 3D-struktur.

Koden är:

* **icke-axiomatisk**
* **icke-normativ**
* **icke-generativ**

Den förutsätter att RP9:s grund och konsekvenskedja redan är etablerade.

---

## Syfte

Syftet med `B_KvanTroN_FrakZooM.py` är att:

* visa hur den **kanoniska kubmodulen** kan itereras rekursivt
* realisera **8ⁿ-strukturer** (2×2×2 per nivå)
* demonstrera att fraktal upprepning kan ske:

  * utan nya roller
  * utan kollaps
  * med bevarad relationell struktur

Koden svarar på frågan:

> *Hur beter sig RP9:s kubiska struktur när den itereras rekursivt över flera nivåer?*

---

## Vad koden gör

Koden består av tre huvuddelar:

### 1. Kanonisk kub-modul (`rp9_module`)

* ritar en kub med:

  * kanter
  * centrum–hörn-diagonaler
  * resonanscirklar i XY- och XZ-plan
* modulen är **identisk på alla nivåer**, endast skalan ändras

### 2. Rekursiv sammansättning (`build_recursive_kubbit`)

* placerar modulen i **8 hörnpositioner** per nivå
* upprepar detta rekursivt upp till `max_depth`
* använder:

  * fast skalfaktor (`inner_scale_factor`)
  * kontrollerad opacitet per nivå

Detta realiserar en **8ⁿ-struktur** utan att introducera nya relationstyper.

### 3. Rendering och export

* renderar strukturen interaktivt i 3D (Plotly)
* sparar:

  * HTML-visualisering
  * PNG-bild (om miljön tillåter)

---

## Vad koden inte gör (viktigt)

Koden:

* etablerar inga axiomer
* härleder inte RP9
* bevisar inte systemet
* introducerar inga fria parametrar
* modellerar ingen fysikalisk dynamik

All matematik används uteslutande för **geometrisk visualisering**.

---

## Förhållande till RP9-systemet

`B_KvanTroN_FrakZooM.py`:

* är **inte del av den nödvändiga konsekvenskedjan**
* ersätter inte:

  * ID.00–ID.05
  * ID.03 (verbal kedja)
  * ID.06 (visuell presentation)

Den fungerar som:

> **ett kodbaserat stresstest av fraktal iteration i 3D**

---

## Körning

* Kräver Python
* Använder:

  * NumPy
  * Plotly
* Körs lokalt och öppnar automatiskt en interaktiv 3D-visualisering

Parametrar av särskilt intresse:

* `max_depth` – antal rekursionsnivåer
* `inner_scale_factor` – skalförhållande mellan nivåer

Ändring av dessa påverkar **djup**, inte **strukturtyp**.

---

## Tolkning

* Varje kub representerar **samma relationella roll**, i ny skala
* Rekursionen representerar **fraktal upprepning utan ny grund**
* Opacitetsschemat visualiserar **nivåseparation**, inte hierarki

Inget element ska tolkas som:

* objekt
* partikel
* fysisk modell

---

## Slutlig låsning

> **Om rekursionen bryter samman eller introducerar instabilitet,
> är det implementationen som är fel – inte RP9:s struktur.**

---
