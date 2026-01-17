Bra. Vi fortsätter konsekvent.
Här är en **separat, enkel och stabil README** för koden:

* `Fraktal_kub.py` 

Placera den **i samma mapp som koden**, t.ex.:

```
🜂 — RP9_Geo_Code`s/
└─ Fraktal_kub/
   ├─ Fraktal_kub.py
   └─ README.md
```

---

# README — Fraktal_kub.py

## *Rekursiv fraktal kub med sfärisk jämviktsvolym*

---

## Dokumentets status

Denna kod är ett **fristående visualiserings- och verifieringsskript** för RP9:s fraktala bärarstruktur.

Koden är:

* **icke-axiomatisk**
* **icke-normativ**
* **icke-generativ**

Den används enbart för att **illustrera och kontrollera stabil fraktal struktur**.

---

## Syfte

Syftet med `Fraktal_kub.py` är att:

* visa en **rekursiv 3D-kubstruktur** (2×2×2)
* kombinera:

  * kuben som bärande struktur
  * sfären som jämvikts- och fältvolym
* demonstrera att fraktal upprepning kan ske **utan kollaps**

Koden svarar på frågan:

> *Hur beter sig en kubisk fraktalstruktur när den upprepas rekursivt i tre dimensioner?*

---

## Vad koden gör

Koden:

* ritar en **central kub** med definierade hörn och ytor
* omsluter varje kub med en **sfärisk wireframe**
* upprepar strukturen rekursivt i **8 hörnpositioner**
* kontrollerar stabilitet genom:

  * konstant skalfaktor
  * symmetrisk fördelning
  * låst rekursionsdjup

Parametrar som används:

* `size` – strukturell skala
* `max_depth` – maximalt rekursionsdjup
* `center` – centrum för varje instans

---

## Vad koden inte gör (viktigt)

Koden:

* etablerar inga axiomer
* härleder inte RP9
* introducerar inga nya konstanter
* optimerar inte för fysikalisk realism

All geometri används som **illustrativ representation**, inte som orsak.

---

## Förhållande till RP9-systemet

`Fraktal_kub.py`:

* är **inte del av den nödvändiga konsekvenskedjan**
* ersätter inte:

  * ID.00–ID.05
  * ID.03 (verbal konsekvens)
  * ID.06 (visuell presentation)

Den fungerar som:

> **ett geometriskt verifieringsblad i kodform**

---

## Körning

* Kräver Python
* Använder:

  * NumPy
  * Matplotlib (3D)
* Körs lokalt och renderar ett statiskt 3D-diagram

All output ska tolkas som:

> **visualisering av redan fastställd struktur**

---

## Tolkning

* Kuben representerar **bärande struktur**
* Sfären representerar **fält / jämviktsvolym**
* Rekursionen representerar **fraktal stabilitet**

Inget element ska tolkas som:

* objekt
* partikel
* fysisk modell

---

