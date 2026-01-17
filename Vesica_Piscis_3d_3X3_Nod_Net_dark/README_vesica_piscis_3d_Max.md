

````markdown
# RP9 — Vesica Piscis 3D (Relationell Funktionsrymd)

Detta projekt visualiserar en **skaloberoende, relationell grundstruktur** baserad på **Vesica Piscis**, där **relationer är primära** och noder uppstår som konsekvenser av geometrisk nödvändighet.

Resultatet är en **fullständig relationsgraf** som kan tolkas som ett **infranät** eller ett **ursprungligt nätverkssubstrat** – före viktning, optimering eller riktning.

---

## Grundidé

I stället för att börja med:
- diskreta noder
- manuellt definierade kanter
- optimerade nätverksregler

börjar detta system med:

1. **Relationell geometri**
2. **Skalning**
3. **Orienteringskvantisering**
4. **Full relationell koppling**

Detta motsvarar RP9-principen:  
**relation före objekt**.

---

## Vad som visualiseras

### 1. Vesica Piscis i tre dimensioner

- Varje Vesica består av två cirklar
- Centrumavstånd = radie (exakt Vesica-relation)
- Vesicor renderas i 3D genom rotation kring ortogonala och diagonala axlar

Tre skalnivåer används:

| Nivå | Antal Vesicor | Radie |
|-----|---------------|-------|
| 0 | 1 | 6.0 |
| 1 | 2 | 3.0 |
| 2 | 4 | 1.5 |

Totalt: **7 Vesica Piscis-strukturer**

---

### 2. Orienteringsnoder (90°-kvantisering)

Varje cirkel i varje Vesica kvantiseras i:

- 0°
- 90°
- 180°
- 270°

Detta ger:
- 4 noder per cirkel
- 8 noder per Vesica

Totalt:
- **56 noder**

Dessa noder representerar **minimala orienteringslägen**, inte valda punkter.

---

### 3. Relationell funktionsgraf (alla-till-alla)

Alla noder kopplas till alla andra noder med linjära relationer.

Detta skapar:

- en **komplett relationsgraf**
- ett tätt “infranät”
- en visuell representation av hur snabbt funktionsrymden växer trots strikt geometri

Antal relationer:

- 56 noder ⇒ **1540 relationella kopplingar**

Inga relationer är filtrerade.  
Allt som är geometriskt tillåtet visas.

---

## Hur detta ska tolkas

Detta är **inte**:
- ett optimerat nätverk
- en simulering
- ett neuralt nät
- ett fysiskt fält

Detta är:

> **Ett relationssubstrat före funktionell specialisering**

Alla kända nätverksformer (neurala, tekniska, sociala, kvantmekaniska) kan förstås som **projektioner eller filtreringar** av denna struktur.

---

## Teknisk implementation

- Python 3
- NumPy
- Plotly (3D Scatter + Surface)
- Renderas som interaktiv HTML

Koden:
- är deterministisk
- innehåller inga slumpmoment
- bygger enbart på relationell geometri

---

## Körning

```bash
pip install numpy plotly
python vesica_piscis_3d.py
````

En HTML-fil (`vesica_piscis_3d.html`) skapas och öppnas automatiskt i webbläsaren.

---

## Resultat

Det som visas i visualiseringen:

* perfekt symmetri i ortogonala vyer
* inga privilegierade riktningar
* centrum uppstår relationellt, inte som vald nod
* ett komplett, skaloberoende nätverksursprung

---

## Sammanfattning

Detta projekt visar att:

> **Nätverk inte behöver konstrueras.
> De kan uppstå som konsekvens av relationell geometri.**

Vesica Piscis fungerar här som en **minsta stabil relationsgenerator** ur vilken nätverksstruktur, funktionstäthet och hierarki kan härledas.

---

## Upphov

**Koncept & implementation:** Anton Wallin
**Ramverk:** RP9 — Relational Primacy Framework

© 2026

```

---

