---
title: "Intensidad admisible en cables enterrados BT: IEC 60364-5-52"
description: "Factores de corrección de intensidad admisible para cables enterrados según IEC 60364-5-52 e ITC-BT-07: temperatura del terreno, resistividad térmica y agrupamiento."
pubDate: 2026-09-24
keywords: ["intensidad admisible cables enterrados", "IEC 60364-5-52", "ITC-BT-07 REBT", "factores corrección cable", "cable XLPE enterrado sección"]
author: "Editor"
---

## Métodos de instalación D1 y D2 según IEC 60364-5-52

La norma IEC 60364-5-52 (equivalente a la UNE-HD 60364-5-52 en España) define los métodos de instalación y las intensidades admisibles de referencia para conductores y cables. Para líneas enterradas en baja tensión, los métodos relevantes son:

- **D1**: cable multipolar o terna de unipolares enterrados directamente en el terreno, sin tubo protector, a una profundidad de referencia de 0,7 m.
- **D2**: cable o conductores instalados en tubo enterrado (conduit), misma profundidad de referencia.

Las condiciones de referencia para las tablas de intensidad de la norma son:
- Temperatura del terreno: **20 °C**
- Resistividad térmica del terreno: **2,5 K·m/W**
- Un solo circuito activo
- Conductor de cobre, aislamiento XLPE/EPR (90 °C)

La ITC-BT-07 del REBT remite directamente a estas tablas para la selección de secciones en líneas de distribución en baja tensión enterradas.

### Intensidades de referencia IEC 60364-5-52, Tabla B.52.20 (Cu, XLPE, enterrado, método D1)

Las siguientes intensidades corresponden a cables tripolares o tetrapolares de cobre con aislamiento XLPE enterrados directamente, en condiciones de referencia:

| Sección (mm²) | Iz (A) — 1 circuito, D1 | Iz (A) — 1 circuito, D2 |
|:---:|:---:|:---:|
| 16 | 76 | 68 |
| 25 | 99 | 89 |
| 35 | 119 | 107 |
| 50 | 141 | 127 |
| 70 | 179 | 161 |
| 95 | 217 | 195 |
| 120 | 249 | 224 |
| 150 | 281 | 252 |
| 185 | 324 | 291 |
| 240 | 380 | 342 |
| 300 | 435 | 392 |

Para conductores de aluminio con aislamiento XLPE, las intensidades son aproximadamente un 22–25 % inferiores respecto al cobre de igual sección.

La diferencia entre D1 y D2 se explica por la resistencia térmica adicional del tubo (típicamente PVC o PE corrugado) entre el cable y el terreno: el tubo actúa como barrera al flujo de calor, reduciendo la disipación hacia el suelo. Por eso la intensidad admisible en D2 es sistemáticamente inferior a D1 en torno a un 10–12 % para secciones medias.

---

## Factores de corrección por temperatura del terreno (k₁)

La temperatura del terreno varía según la profundidad y la época del año. Para España, IEC 60364-5-52 tabla B.52.16 proporciona el factor multiplicador k₁ respecto a la temperatura de referencia de 20 °C:

| Temperatura del terreno (°C) | k₁ (Cu XLPE, 90 °C) |
|:---:|:---:|
| 10 | 1,07 |
| 15 | 1,04 |
| **20** | **1,00** |
| 25 | 0,96 |
| 30 | 0,93 |
| 35 | 0,89 |
| 40 | 0,85 |
| 45 | 0,80 |
| 50 | 0,76 |

La temperatura máxima del conductor es 90 °C para XLPE. El factor k₁ sigue la expresión:

```
k₁ = √[(θmax − θterreno) / (θmax − θref)]
  = √[(90 − θt) / (90 − 20)]
```

En zonas de clima mediterráneo, la temperatura del terreno a 0,7 m puede alcanzar 25–30 °C en verano. A 30 °C, la capacidad nominal del cable se reduce ya un 7 %. A 40 °C, la reducción llega al 15 %.

---

## Factores de corrección por resistividad térmica del terreno (k₂)

La resistividad térmica ρ del terreno (en K·m/W) es el parámetro que más afecta a la disipación de calor de los cables enterrados. La resistencia térmica del suelo representa entre el 50 y el 70 % de la resistencia térmica total conductor-entorno en una instalación típica.

IEC 60364-5-52 tabla B.52.17 proporciona k₂ para el método D1, referenciado a ρ = 2,5 K·m/W:

| Resistividad térmica ρ (K·m/W) | k₂ (cable tripolar XLPE) |
|:---:|:---:|
| 0,5 | 1,28 |
| 0,7 | 1,20 |
| 1,0 | 1,18 |
| 1,5 | 1,10 |
| **2,5** | **1,00** |
| 3,0 | 0,96 |
| 4,0 | 0,89 |

Los valores típicos de resistividad del terreno son:

- Terreno húmedo, arcilloso: 0,5–1,0 K·m/W → favorable, cables podrían tener más capacidad de la nominal
- Terreno ordinario húmedo: 1,0–2,0 K·m/W → próximo a la referencia
- Arena seca, gravas: 2,5–4,0 K·m/W → desfavorable, puede obligar a aumentar sección
- Pavimento asfáltico seco: 3,5–4,0 K·m/W → caso habitual en cables bajo calzada

La ITC-BT-07 del REBT no especifica directamente cómo medir la resistividad térmica del terreno, pero remite a la UNE-EN ISO 22007-2 para la medida por el método de la aguja caliente. En proyectos de líneas de distribución de media y baja tensión es recomendable determinar ρ con ensayos de campo, especialmente si el trazado atraviesa zonas de arena seca o rellenos no compactados.

---

## Factores de corrección por agrupamiento de cables (k₃)

Cuando varias ternas o cables multipolares se instalan en proximidad, el calor disipado por cada circuito eleva la temperatura de los adyacentes, reduciendo la capacidad de disipación de todos ellos. IEC 60364-5-52 tabla B.52.18 da el factor k₃ para el método D1 en función del número de circuitos y la separación entre ellos:

| Nº de circuitos | Separación nula (contacto) | Separación 0,25 m | Separación 0,5 m |
|:---:|:---:|:---:|:---:|
| 1 | 1,00 | 1,00 | 1,00 |
| 2 | 0,75 | 0,80 | 0,85 |
| 3 | 0,65 | 0,70 | 0,75 |
| 4 | 0,60 | 0,66 | 0,70 |
| 5 | 0,55 | 0,62 | 0,67 |
| 6 | 0,50 | 0,57 | 0,63 |

La separación de referencia entre ejes de circuito es 0,70 m para que no haya efecto de agrupamiento apreciable (k₃ ≈ 1,00).

En zanjas de distribución urbana, donde se instalan habitualmente 2 o 3 circuitos en contacto, el factor k₃ = 0,65–0,75 supone reducciones de capacidad de corriente del 25–35 %. Este efecto justifica el sobredimensionamiento habitual de las líneas de distribución enterradas en polígonos industriales y urbanizaciones densas.

---

## Criterios de selección y ejemplo de cálculo

La intensidad admisible corregida se obtiene aplicando los tres factores de forma acumulativa:

```
Iz_corr = Iz_ref × k₁ × k₂ × k₃
```

La sección del cable se elige de forma que:

```
Iz_corr ≥ IB  (corriente de uso del circuito)
```

Además, la sección debe cumplir simultáneamente:
1. **Criterio térmico** (capacidad de conducción) según IEC 60364-5-52
2. **Criterio de protección**: la corriente de funcionamiento del interruptor en tiempo convencional Inf ≤ 1,45 × Iz_corr (IEC 60364-4-43)
3. **Criterio de caída de tensión**: ITC-BT-07 limita la caída de tensión al 5 % en líneas de distribución desde el centro de transformación hasta el punto de utilización

### Ejemplo práctico

Línea de alimentación a un cuadro de distribución industrial: I_B = 180 A, longitud 200 m, cable RZ1-K (XLPE) de cobre, método D1, zanja con 3 circuitos en contacto. Temperatura del terreno: 28 °C. Terreno arenoso: ρ = 3,5 K·m/W.

**Paso 1 — Factores de corrección:**
- k₁ (28 °C): interpolando entre 25 °C (0,96) y 30 °C (0,93): k₁ ≈ 0,944
- k₂ (ρ = 3,5 K·m/W): interpolando entre 3,0 (0,96) y 4,0 (0,89): k₂ ≈ 0,925
- k₃ (3 circuitos en contacto): k₃ = 0,65

**Paso 2 — Iz requerida:**
```
Iz_ref ≥ IB / (k₁ × k₂ × k₃)
       = 180 / (0,944 × 0,925 × 0,65)
       = 180 / 0,568
       = 317 A
```

Con la tabla D1 de referencia, la sección que cumple Iz_ref ≥ 317 A es **185 mm²** (Iz_ref = 324 A). La sección de 150 mm² (281 A) sería insuficiente en estas condiciones.

**Paso 3 — Verificación de caída de tensión:**
Para 185 mm² Cu XLPE, resistencia a 90 °C: R = 0,106 × (1 + 0,00393 × 70) ≈ 0,135 Ω/km. Reactancia (base de datos GElectrical, método D1): X ≈ 0,08 Ω/km.

Para circuito trifásico a 400 V:
```
ΔU% = √3 × I × (R·cos φ + X·sen φ) × L / U
     = 1,732 × 180 × (0,135 × 0,85 + 0,08 × 0,527) × 0,2 / 400
     = 1,732 × 180 × (0,1148 + 0,0422) × 0,2 / 400
     = 1,732 × 180 × 0,1570 × 0,2 / 400
     ≈ 2,45 %
```

Dentro del límite del 5 % de ITC-BT-07. La sección de 185 mm² queda validada por ambos criterios.

---

## Conclusión

La selección de sección para cables BT enterrados no puede hacerse directamente con la tabla de referencia de IEC 60364-5-52 sin aplicar los factores de corrección k₁, k₂ y k₃. En condiciones reales de clima mediterráneo, terreno arenoso y zanjas compartidas, la capacidad de corriente efectiva puede quedar reducida al 50–60 % del valor tabulado. Los pasos de cálculo son:

1. Determinar I_B del circuito y las condiciones de instalación reales (método D1/D2, temperatura del terreno, ρ del suelo, número de circuitos agrupados).
2. Calcular los factores k₁ × k₂ × k₃ y obtener la Iz_ref mínima requerida.
3. Seleccionar la sección normalizada que cumpla Iz_ref de la tabla B.52.20.
4. Verificar la caída de tensión con los valores R y X del cable elegido según IEC 60364-5-52 (Anexo B) y los límites de ITC-BT-07.
5. Verificar la coordinación con la protección del circuito: Inf ≤ 1,45 × Iz_corr.

No es aceptable en proyecto profesional usar tablas sin condiciones de referencia ni aplicar factores de corrección de forma aproximada. La ITC-BT-07 exige documentar las condiciones de instalación y el cálculo justificativo como parte del proyecto de legalización.
