---
# ==================================================
# PRIMARY — IDENTITY
# ==================================================

primary_id: "rp9_nivaklassificeringsblad"
primary_title: "RP9 — Nivåklassificeringsblad"
primary_language: "sv"
primary_version: "1.0"

# ==================================================
# PRIMARY — CLASSIFICATION
# ==================================================

primary_kind: "ground-adjacent"
primary_category: "methodology"
primary_document_role: "level_classification"

primary_reading_part: null
primary_reading_label: "LEVEL 0 / LEVEL 1 / LEVEL 2"

# ==================================================
# PRIMARY — EPISTEMIC ROLE
# ==================================================

primary_epistemic_level: 0

primary_axiomatic_introduces_axiom: false
primary_axiomatic_causal_force: "scope_lock"
primary_axiomatic_dependency:
  - axiom_R0

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
  - axiom_R0
primary_interpretation_forbids:
  - level_mixing
primary_interpretation_allows:
  - formal_review

primary_non_claims:
  - derivation
primary_invariants:
  - one_way_dependency

# ==================================================
# SECONDARY — MODEL SCOPE
# ==================================================

secondary_model_scope_description: "Defines and locks formal statement types permitted at each RP9 level."
secondary_model_scope_applies_to:
  - repository_structure
secondary_model_scope_limitations:
  - non_explanatory

secondary_model_status: "governance"

# ==================================================
# META
# ==================================================

meta_author: "Anton Wallin"
meta_alias: "Co-Creators"
meta_project: "RP9 — Relational Primacy Framework"
meta_system_identifier: "BC22/825870"

meta_document_maturity: "final"
meta_validation_condition: "classification"
meta_obsidian_compatible: true
---

# **RP9 — Nivåklassificeringsblad**

**(Formal Level Classification: LEVEL 0 / LEVEL 1 / LEVEL 2)**

## **Syfte**

Detta dokument fastställer den **formella nivåindelningen** i RP9 och specificerar  
vilken typ av påståenden som är tillåtna på respektive nivå.

Syftet är att:

- skydda grundaxiomet från sammanblandning
    
- förhindra dolda koaxiom
    
- möjliggöra granskning utan tolkningsläckage
    

---

## **LEVEL 0 — Axiom (Grund)**

### **Status**

- Exakt **ett** element
    
- Icke-deriverbart
    
- Orsak, inte resultat
    
- Ingen feedback tillåten
    

### **Innehåll**

**Axiom R0 — Relational Necessity**

> Everything that can function must be differentiated.  
> Differentiation is only possible as a relation.  
> Relation requires at least two distinct poles.

### **Tillåtet på LEVEL 0**

- Endast nödvändighetsformulering
    
- Inga objekt
    
- Inga processer
    
- Ingen geometri
    
- Ingen rörelse
    
- Inga dimensioner
    

### **Otillåtet på LEVEL 0**

- Härledning
    
- Förklaring
    
- Illustration
    
- Struktur
    
- Tillämpning
    

Om LEVEL 0 förnekas kollapsar hela systemet.

---

## **LEVEL 1 — Primära strukturella konsekvenser**

### **Status**

- Fullständigt beroende av LEVEL 0
    
- Introducerar **ingen ny grund**
    
- Beskriver **nödvändiga konsekvenser** av relationell slutenhet
    

### **Funktion**

LEVEL 1 anger **vad som måste följa** om relation enligt Axiom R0  
realiseras i en stabil, sluten struktur.

### **Egenskaper**

- Icke-generativ
    
- Icke-valfri
    
- Icke-feedback
    
- Strukturellt nödvändig
    

### **Test**

Om LEVEL 1 tas bort:

- Axiom R0 kvarstår oförändrat
    

Om Axiom R0 tas bort:

- LEVEL 1 kollapsar fullständigt
    

---

## **LEVEL 2 — Sekundära strukturer och tillämpningar**

### **Status**

- Fullt beroende av LEVEL 0 och LEVEL 1
    
- Utbytbara
    
- Kontextbundna
    

### **Innehåll**

- Modeller
    
- Visualiseringar
    
- Matematiska formalisationer
    
- Kod
    
- Tillämpningar
    
- Metaforer
    

### **Egenskaper**

- Ingen nödvändighet
    
- Ingen grundstatus
    
- Får inte påverka LEVEL 0 eller LEVEL 1
    

---

## **Enkel asymmetri (bindande)**

```
LEVEL 0  →  LEVEL 1  →  LEVEL 2
Grund        Nödvändig struktur        Valfri realisation
```

Ingen uppåtgående påverkan är tillåten.

---

## **Slutlig låsning**

Endast **LEVEL 0** innehåller ett axiom.  
LEVEL 1 och LEVEL 2 innehåller **inga axiomer**, endast konsekvenser och realisationer.


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



