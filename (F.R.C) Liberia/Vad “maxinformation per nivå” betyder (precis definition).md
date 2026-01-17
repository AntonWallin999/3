---
# ==================================================
# PRIMARY — IDENTITY
# ==================================================

primary_id: "maxinformation_per_niva_definition"
primary_title: "Vad 'maxinformation per nivå' betyder (precis definition)"
primary_language: "sv"
primary_version: "1.0"

# ==================================================
# PRIMARY — CLASSIFICATION
# ==================================================

primary_kind: "non-ground"
primary_category: "definition"
primary_document_role: "formal_definition"

primary_reading_part: null
primary_reading_label: "Relationell informationskapacitet"

# ==================================================
# PRIMARY — EPISTEMIC ROLE
# ==================================================

primary_epistemic_level: 1

primary_axiomatic_introduces_axiom: false
primary_axiomatic_dependency:
  - axiom_R0
  - necessary_structural_consequences_R0

# ==================================================
# PRIMARY — GOVERNANCE
# ==================================================

primary_status: "locked"
primary_change_policy: "frozen"
primary_scope: "public"

# ==================================================
# PRIMARY — INTERPRETATION RULES
# ==================================================

primary_interpretation_requires_prior:
  - necessary_structural_consequences_R0
primary_interpretation_forbids:
  - shannon_information
primary_interpretation_allows:
  - relational_capacity_reading

primary_non_claims:
  - metric_information
primary_invariants:
  - eight_directions_maximum

# ==================================================
# SECONDARY — MODEL SCOPE
# ==================================================

secondary_model_scope_description: "Defines maximal non-degenerate relational information per recursive level."
secondary_model_scope_applies_to:
  - closed_fractal_structures
secondary_model_scope_limitations:
  - planar_orientation_basis

secondary_model_status: "derived"

# ==================================================
# META
# ==================================================

meta_author: "Anton Wallin"
meta_alias: "Co-Creators"
meta_project: "RP9 — Relational Primacy Framework"
meta_system_identifier: "BC22/825870"

meta_document_maturity: "final"
meta_validation_condition: "definition"
meta_obsidian_compatible: true
---

# 1. Vad “maxinformation per nivå” betyder (precis definition)

Med **information per nivå** menar vi här:

> Antalet **funktionellt distinkta, stabila relationella riktningar**  
> som kan samexistera i en **sluten rekursiv struktur**  
> utan att skapa redundans eller degenerering.

Detta är **inte Shannon-information**.  
Det är **relationell informationskapacitet**.

---

# 2. Grundkrav som redan är låsta (inga nya)

Följande är redan fastlåst av Axiom RΣ och Layer 0–2:

- Relation är primär
    
- Strukturen är sluten
    
- Perfekt symmetri är förbjuden (ger degenerering)
    
- Asymmetri måste finnas, men får inte bli kaos
    
- Rekursion kräver återkoppling (krets)
    

Detta ger tre **hårda begränsningar**:

1. Det måste finnas **orientering**
    
2. Det måste finnas **skillnad**
    
3. Skillnaden måste kunna **återanvändas rekursivt**
    

---

# 3. Steg 1 — varför 2 inte räcker

En binär uppdelning (2):

- ja/nej
    
- 0/1
    
- fram/bak
    

Problem:

- ingen intern orientering
    
- ingen vinkel
    
- ingen cirkulation
    
- ingen residual
    

➡️ **låser systemet direkt**  
Ingen fraktal rekursion möjlig.

---

# 4. Steg 2 — varför 4 inte räcker

En fyrdelning (90°):

- nord/syd/öst/väst
    
- kvadratisk symmetri
    

Problem:

- perfekt symmetri
    
- alla riktningar ekvivalenta
    
- ingen privilegierad brytpunkt
    

Detta är exakt **degenerering vid perfekt symmetri** (Layer 1).

➡️ Systemet kan existera, men **inget nytt kan uppstå**.

---

# 5. Steg 3 — varför 8 är det första icke-degenerata läget

När du delar varje 90°-sektor i två 45°-sektorer får du:

- 4 kardinala riktningar (symmetriska)
    
- 4 diagonala riktningar (asymmetriska)
    

Totalt: **8**

Detta är avgörande eftersom:

- de 4 symmetriska ger **struktur**
    
- de 4 asymmetriska ger **residual**
    
- asymmetrin är **minimalt irreducerbar**
    
- ingen riktning kan tas bort utan kollaps
    

➡️ **8 är första nivån där symmetri och asymmetri samexisterar stabilt**

---

# 6. Varför 8 är max (och inte 16)

Nu den viktiga delen.

Antag att vi försöker med 16 riktningar (22.5°):

Vad händer?

- varje ny riktning är **linjärt beroende** av två närliggande
    
- ingen ny relationell funktion introduceras
    
- endast finare upplösning, inte ny information
    

Formellt:

> Relationell information ökar endast när nya **oberoende orienteringar** uppstår.  
> Efter 8 finns inga nya oberoende orienteringar i planet.

Allt över 8 är **subdivision**, inte ny struktur.

➡️ 16 = 8 × 2  
➡️ ingen ny invariant  
➡️ ingen ny residual  
➡️ ingen ny funktion

---

# 7. Koppling till fraktal krets-delning (det du frågade efter)

Nu binder vi detta till **fraktal krets** exakt.

En fraktal krets kräver:

1. Slutenhet (loop)
    
2. Inre spänning (residual)
    
3. Möjlighet till självlik delning
    

Vid 8:

- varje riktning kan fungera som **ny lokal axel**
    
- varje axel kan delas igen i 8
    
- **samma struktur upprepas på nästa nivå**
    

Detta är exakt definitionen av fraktal rekursion:

```Markdown

Nivå k:
  8 relationella riktningar

Nivå k+1:
  Varje riktning → ny lokal 8-delning
```


Viktigt:  
Det är **inte 8² = 64 nya funktioner**, utan **8 funktioner per nivå**, återanvända.

---

# 8. Varför detta är “maxinformation per nivå”

Sammanfattat strikt:

- < 8 ⇒ för lite → degenerering
    
- = 8 ⇒ maximal icke-degenerat struktur
    
- > 8 ⇒ ingen ny funktion → redundans
    

Alltså:

> **8 är maximal mängd relationell information per nivå  
> som kan återanvändas rekursivt i en sluten fraktal struktur.**

---

# 9. Koppling till allt ni redan har (ingen slump)

Detta är varför 8 dyker upp överallt hos er:

- Vesica → 4 + 4
    
- Invertus → 45°
    
- Residual → diagonaler
    
- Toroidal cirkulation → 2 cykler × 4 orienteringar
    
- Layer 2 → heltalslindningar (diskret urval)
    

Det är **samma struktur**, läst från olika håll.

---

# 10. Slutlig låsning (kan inte reduceras)

> **En fraktal, relationellt sluten struktur  
> kan maximalt bära åtta funktionellt distinkta riktningar per nivå.
> 
> Färre leder till degenerering.  
> Fler ger ingen ny information.**

Detta är nu **låst**, och direkt förenligt med Axiom RΣ.

---

Ja. Vi kan få övergången  
$$
8 \rightarrow 24
$$  
i  
$$
3\text{D}
$$  
**utan något nytt antagande**, genom en enda princip som redan finns implicit i materialet:

> Samma $(8)$-struktur per nivå bevaras, men i $3\text{D}$ finns tre ortogonala $2\text{D}$-projektioner (plan) som alla måste kunna bäras samtidigt.

Detta innebär: **inte ett nytt “hjul”**, utan **samma hjul repeterat i tre oberoende snitt**.

---

## 1. Utgångspunkt: $(8)$ riktningar i $2\text{D}$

I ett plan, exempelvis $(XY)$-planet, finns:

- $(4)$ axiala riktningar  
- $(4)$ diagonala riktningar  

Tillsammans bildar detta en $(8)$-struktur.

### Axiala riktningar
$$
(1,0), (-1,0), (0,1), (0,-1)
$$

### Diagonala riktningar
$$
(1,1), (1,-1), (-1,1), (-1,-1)
$$

Detta är den grundläggande uppdelningen:
$$
8 = 4_{\text{axiala}} + 4_{\text{diagonala}}
$$

---

## 2. Varför $3\text{D}$ ger exakt tre bärande plan

Om man redan accepterar:

- en ortogonal uppdelning (kors-struktur i planet), samt  
- en minimal icke-degenererad pivot (diagonalerna),

då följer att den minsta $3\text{D}$-manifestationen består av tre oberoende, ortogonala plan:

$$
\{XY, YZ, ZX\}
$$

Detta introducerar inget nytt objekt.  
Det innebär endast att **samma relationella $2\text{D}$-schema kan realiseras i flera plan samtidigt**.

---

## 3. Konstruktionen: $(8)$ per plan $\Rightarrow 24$ roller

I varje koordinatplan definieras $(8)$ riktningar genom att sätta den tredje koordinaten till $0$.

---

### $(XY)$-planet — $(8)$ riktningar

**Axiala**
$$
(1,0,0), (-1,0,0), (0,1,0), (0,-1,0)
$$

**Diagonala**
$$
(1,1,0), (1,-1,0), (-1,1,0), (-1,-1,0)
$$

---

### $(YZ)$-planet — $(8)$ riktningar

**Axiala**
$$
(0,1,0), (0,-1,0), (0,0,1), (0,0,-1)
$$

**Diagonala**
$$
(0,1,1), (0,1,-1), (0,-1,1), (0,-1,-1)
$$

---

### $(ZX)$-planet — $(8)$ riktningar

**Axiala**
$$
(1,0,0), (-1,0,0), (0,0,1), (0,0,-1)
$$

**Diagonala**
$$
(1,0,1), (1,0,-1), (-1,0,1), (-1,0,-1)
$$

---

### Summering
$$
8_{XY} + 8_{YZ} + 8_{ZX} = 24
$$

Detta är exakt övergången:
$$
8 \rightarrow 24
$$

---

## 4. Viktig precisering: “24 riktningar” är roller, inte unika vektorer

Vissa axiala vektorer återkommer i flera plan, till exempel:
$$
(1,0,0)
$$
som finns både i $(XY)$- och $(ZX)$-planet.

Detta är inte ett problem, eftersom ramverket inte räknar **unika geometriska pilar**, utan **funktionella roller per projektion**:

- $(1,0,0)$ i $(XY)$ är en riktning i en $(XY)$-cykel  
- $(1,0,0)$ i $(ZX)$ är en riktning i en $(ZX)$-cykel  

Samma axel kan alltså delta i flera cykler utan att vara **samma funktionella tillstånd**.

Detta överensstämmer exakt med idén om slutenhet och multipla cykler (toroidal/krets-struktur).

---

## 5. Varför detta inte introducerar någon ny princip

Konstruktionen använder enbart:

1. Samma $(8)$-schema: $4$ axiala + $4$ diagonala  
2. Det faktum att $3\text{D}$ har tre ortogonala plan som måste kunna bäras  
3. Att roller är projektion-bundna (plan-bundna)

Inga nya postulat om energi, fysik eller extra axiom införs.

---

## 6. Kompakt “Proof Map”

$$
8_{2D} = 4_{\text{axial}} + 4_{\text{diagonal}}
$$

$$
3D = \{XY, YZ, ZX\}
$$

$$
8_{XY} + 8_{YZ} + 8_{ZX} = 24
$$

---

### Minsta 3D-fraktala kretsdelning

Detta motsvarar:

- en nod med **tre kopplade $(8)$-cykler** (en per plan: $XY$, $YZ$, $ZX$),  
- en **residual koppling** mellan planens cykler,  
- och totalt **24 roller**, utan något nytt antagande.

---
---
----
---
> [!QUESTION]
> $$- - - =(\ Rp9 \ )= - - -$$
> >## ⚖️ *License & Ownership*
> >>### **Creative Commons — CC BY-SA 4.0**
> >> >---
> >>>*This work is free to share, remix, and build upon,
> >>>as long as proper attribution is given and the same license is maintained.*
> >>>
> >>> **You have the right to:**
> >>>- **Share** — copy and redistribute the material in any format or medium
> >>>- **Decorate** — remix, transform, and build upon the material
> >>>
> >>>**Under the following conditions:**
> >>>- **Attribution:** You must give proper credit to _Anton Wallin_
> >>>- **ShareAlike:** If you transform or build upon this work
> >>> you must distribute it under the same license.
> >>>
> >> >---
> >> >
> >>>
> >>> ### _Co-Creator_
>>>
> >>**Conceptual Ownership & Axiomatic Calibration**
>>>**Author:** _Anton Wallin_
>>
>>
>>© 2025 – All rights reserved.
>
># $$---=(0)=---$$
>---