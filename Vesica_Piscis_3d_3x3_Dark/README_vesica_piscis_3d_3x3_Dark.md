

# README — vesica_piscis_3d.py

## *Skaloberoende 3D-visualisering av Vesica Piscis-relationen*

---

## Dokumentets status

Denna kod är ett **rent visuellt och relationellt verifieringsskript** för Vesica Piscis i tre dimensioner.

Koden är:

* **icke-axiomatisk**
* **icke-normativ**
* **icke-generativ**

Den etablerar inga grunder och förutsätter att RP9:s relationella ram redan är fastställd.

---

## Syfte

Syftet med `vesica_piscis_3d.py` är att:

* visa Vesica Piscis som **en strikt relation**, inte en figur
* demonstrera **skaloberoende stabilitet** i 3D
* visa hur samma relation kan realiseras i:

  * central orientering
  * ortogonala plan
  * diagonala orienteringar
* bekräfta att strukturen **inte kollapsar** vid rotation eller skalning

Koden svarar på frågan:

> *Hur beter sig Vesica Piscis-relationen när den lyfts till tre dimensioner och itereras i orientering och skala?*

---

## Vad koden gör

Koden är uppdelad i tydliga, relationella steg:

### 1. Relationell definition

* definierar två cirklar med:

  * identisk radie `r`
  * centrumavstånd exakt lika med `r`
* detta är den **enda relationen** i systemet

### 2. 3D-rotation

* roterar cirklarna kring X-, Y- och Z-axlar
* rotation används som **orientering**, inte transformation av relation

### 3. Strukturell uppbyggnad (1 → 2 → 4)

* **Nivå 0:**

  * 1 central Vesica (radie 6)
* **Nivå 1:**

  * 2 Vesicor, vinkelräta (radie 3)
* **Nivå 2:**

  * 4 Vesicor, diagonalt orienterade (radie 1.5)

Alla nivåer delar **samma relation**, endast skala och orientering ändras.

### 4. Rendering

* renderar strukturen i interaktiv 3D (Plotly)
* låser proportioner (`aspectmode="data"`)
* döljer axlar och koordinater
* sparar resultatet som HTML

---

## Vad koden inte gör (viktigt)

Koden:

* etablerar inte Axiom R0
* bevisar inte RP9
* introducerar inga nya relationer
* använder inga godtyckliga parametrar
* modellerar ingen fysikalisk dynamik

Rotation och skalning är **visuella operationer**, inte nya strukturer.

---

## Förhållande till RP9-systemet

`vesica_piscis_3d.py`:

* är **inte del av den nödvändiga konsekvenskedjan**
* ersätter inte:

  * ID.00–ID.05
  * ID.03 (verbal kedja)
  * ID.06 (visuell presentation)

Den fungerar som:

> **en 3D-diagnostisk visualisering av den första stabila relationella geometrin**

---

## Körning

* Kräver Python
* Använder:

  * NumPy
  * Plotly
* Körs lokalt

Vid körning:

* skapas `vesica_piscis_3d.html`
* en interaktiv visualisering öppnas i webbläsare

All output ska tolkas som:

> **visualisering av redan fastställd relation**

---

## Tolkning

* Cirklarna representerar **relationella bärare**
* Överlappet representerar **nödvändig konsekvens**
* Skalstegen representerar **iteration utan ny grund**
* Rotation representerar **orientering, inte förändring**

Inget element ska tolkas som:

* objekt
* partikel
* fysisk modell

---

## Slutlig låsning

> **Om Vesica-relationen inte förblir stabil vid rotation och skalning,
> är implementationen fel – inte relationen.**

Denna kod är ett visuellt verifieringsverktyg, inte ett argument.

---

Säg **”nästa”** och bifoga nästa fil när du är redo, så fortsätter vi tills hela
**🜂 — RP9_Geo_Code`s** är komplett dokumenterad.
