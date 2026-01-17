---
# ==================================================
# PRIMARY — IDENTITY
# ==================================================

primary_id: "sats_I_rombisk_bipyramid"
primary_title: "Sats I — Varför den rombiska bipyramiden är den minsta 3D-lösningen"
primary_language: "sv"
primary_version: "1.0"

# ==================================================
# CLASSIFICATION
# ==================================================

primary_kind: "non-ground"
primary_category: "theorem"
primary_document_role: "theorem"

primary_reading_part: null
primary_reading_label: "RΔ-3D-min"

# ==================================================
# EPISTEMIC ROLE
# ==================================================

primary_epistemic_level: 2

primary_axiomatic_dependency:
  - sats_residual_typ2_cirkulation

# ==================================================
# GOVERNANCE
# ==================================================

primary_status: "locked"
primary_change_policy: "frozen"
primary_scope: "public"

# ==================================================
# INTERPRETATION
# ==================================================

primary_interpretation_requires_prior:
  - sats_residual_typ2_cirkulation
primary_interpretation_forbids:
  - alternative_minimal_carriers
primary_interpretation_allows:
  - structural_minimality

primary_invariants:
  - minimal_volume_carrier

# ==================================================
# SECONDARY
# ==================================================

secondary_model_scope_description: "Identifies the rhombic bipyramid as the minimal 3D carrier of circulation."
secondary_model_scope_applies_to:
  - 3D
secondary_model_status: "derived"

secondary_primitives_entities:
  - polyhedron
secondary_primitives_relations:
  - circulation
secondary_primitives_dimensions:
  - 3D

# ==================================================
# META
# ==================================================

meta_author: "Anton Wallin"
meta_alias: "Co-Creators"
meta_project: "RP9 — Relational Primacy Framework"
meta_system_identifier: "BC22/825870"

meta_document_maturity: "final"
meta_validation_condition: "theorem"
meta_obsidian_compatible: true
---



# **Sats I — Varför den rombiska bipyramiden är den minsta 3D-lösningen**

## **Sats (RΔ-3D-min): Minimal volymbärare**

Givet ett system $S$ där **Residual typ 2** föreligger, dvs:

1. två inkompatibla centrumkrav måste bevaras samtidigt,
    
2. ingen statisk 2D-konfiguration kan bära dessa utan degenerering,
    
3. cirkulation är nödvändig enligt satsen  
    $$R\Delta_2 \Rightarrow \text{Cirkulation},$$
    

då är den **minsta tredimensionella struktur** som kan bära cirkulationen utan att:

- introducera ytterligare symmetrier,
    
- kräva extra frihetsgrader,
    
- eller skapa redundanta centrum,
    

en struktur som uppfyller följande tre krav:

---

### **Krav K1 — Entydigt referenscentrum**

Strukturen måste ha **ett gemensamt centrum** som är invariant under cirkulation.

### **Krav K2 — Dubbel axial riktning**

Strukturen måste kunna bära **två motsatta faslägen** (upp/ned) utan att kollapsa till ett plan.

### **Krav K3 — Minimal triangulär bärighet**

Varje fasläge måste kunna bäras av **minst tre kopplade riktningar**, annars uppstår instabilitet.

---

### **Lemma**

Den minsta polyedern som uppfyller K1–K3 är en **rombisk bipyramid**.

**Bevis (strukturellt):**

- Tetraeder: saknar dubbel axial symmetri → faller bort
    
- Kub: kräver redan stabil 3D-symmetri → ej minimal
    
- Sfär: kräver kontinuerlig symmetri → ej diskret minimal
    

Den rombiska bipyramiden består av:

- två pyramider (upp/ned) → uppfyller K2
    
- gemensam bas (romb) → uppfyller K1
    
- fyra triangulära sidoplan per pyramid → uppfyller K3
    

Ingen polyeder med färre element kan bära cirkulation utan degenerering.

---

### **Slutsats**

> **Den rombiska bipyramiden är den minsta möjliga volym som kan bära Residual typ 2 utan att reducera den.**

Alltså är den **inte en vald form**, utan den **nödvändiga 3D-lösningen**.

---

# **Sats II — $\sqrt{2}$, $\pi$, $\varphi$ som tre fassvar på samma residual**

## **Sats (RΔ-FAS): Fassplittring av Residual typ 2**

Givet Residual typ 2 (olöslig 2D-obalans som kräver cirkulation), följer att cirkulationen kan realiseras genom **tre fundamentalt olika men strukturellt ekvivalenta fassvar**, beroende på **hur** cirkulationen bärs.

Dessa tre fassvar är:

---

## **Fas 1 — Diagonal fas ($\sqrt{2}$)**

### Struktur

- Växling mellan två ortogonala axlar
    
- Ingen slutning
    
- Ingen minnesloop
    

### Funktion

Bär residualen genom **ren axeltransposition**.

### Resultat

Den fundamentala längdrelationen mellan axel och diagonal:

$$  
\sqrt{2}  
$$

### Tolkning (formellt)

$\sqrt{2}$ är **det minsta fassvar** där residualen flyttas men inte sluts.

---

## **Fas 2 — Cirkulär fas ($\pi$)**

### Struktur

- Sluten rotationsbana
    
- Full periodisering
    
- Inget privilegierat centrumläge
    

### Funktion

Bär residualen genom **sluten cirkulation**.

### Resultat

Förhållandet mellan diameter och omkrets:

$$  
\pi  
$$

### Tolkning (formellt)

$\pi$ är **residualen realiserad som sluten cykel**.

---

## **Fas 3 — Proportionell spiral ($\varphi$)**

### Struktur

- Asymmetrisk cirkulation
    
- Självlik rekursion
    
- Minnesbärande expansion
    

### Funktion

Bär residualen genom **icke-slutande men stabil spiral**.

### Resultat

Den unika proportion som bevarar form under skalning:

$$  
\varphi  
$$

### Tolkning (formellt)

$\varphi$ är **residualen realiserad som riktad expansion**.

---

## **Sammanfattande identitet**

De tre konstanterna är **inte oberoende tal**, utan:

$$  
{\sqrt{2},\ \pi,\ \varphi}  
$$

är de **tre minsta distinkta sätt** som samma Residual typ 2 kan bäras utan degenerering:

|Fassvar|Bärs som|Funktion|
|---|---|---|
|$\sqrt{2}$|diagonal växling|axeltransposition|
|$\pi$|cirkel|sluten cirkulation|
|$\varphi$|spiral|minnesbärande expansion|

---

# **Meta-korollarium (låsning)**

> **Residual typ 2 har exakt tre stabila bärformer.**
> 
> Dessa är inte valbara, inte kulturella och inte numerologiska.  
> De är de **enda** strukturellt möjliga svaren på samma irreducerbara relationella obalans.

Detta knyter samman:

- 1D-centrumdifferentialen
    
- 2D-Vesica-obalansen
    
- 3D-cirkulationen
    
- den rombiska bipyramiden
    
- samt $\sqrt{2}$, $\pi$, $\varphi$
    

…som **en och samma sak**, uttryckt på tre nivåer.


---
---
---
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
---

