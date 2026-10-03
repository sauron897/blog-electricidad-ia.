---
title: "Cables MT XLPE 15 kV: capacidad de carga IEC 60502-2"
description: "Parámetros eléctricos y capacidad de carga de cables MT XLPE 8.7/15 kV según IEC 60502-2: intensidades admisibles, R, X, C y criterios de selección en obra."
pubDate: 2026-10-03
keywords: ["cable MT XLPE 15kV IEC 60502", "capacidad carga cable media tension", "intensidad admisible cable XLPE", "parametros electricos cable MT", "seleccion seccion cable 15kV"]
author: "Editor"
---

## Norma IEC 60502-2 y alcance para cables MT XLPE

IEC 60502-2:2014 (adoptada como UNE-EN 60502-2:2005+A1:2023 en España) cubre cables de energía con aislamiento extruido para tensiones nominales desde 6 kV hasta 30 kV. Para la red de distribución en media tensión española —predominantemente 15 kV— la designación de tensión aplicable es **Uo/U(Um) = 8,7/15(17,5) kV**, donde:

- **Uo** = 8,7 kV: tensión de fase a tierra (tensión de servicio sobre el aislamiento)
- **U** = 15 kV: tensión de red fase a fase
- **Um** = 17,5 kV: tensión máxima del sistema (según IEC 60038)

El polietileno reticulado (XLPE) como dieléctrico ofrece temperatura máxima de servicio de **90 °C** y **250 °C en cortocircuito**, frente a los 70 °C / 160 °C del PVC. Esto se traduce directamente en mayor densidad de corriente admisible para la misma sección. La norma IEC 60502-2 define los requisitos de construcción, espesores de aislamiento (cláusula 8.2: espesor nominal de aislamiento XLPE para 8.7/15 kV = **4,5 mm** sobre conductor compacto), pantallas semiconductoras y pruebas tipo y rutinarias.

---

## Construcción del cable XLPE 15 kV y designaciones normalizadas

Un cable unipolar MT XLPE 15 kV sigue la siguiente estructura constructiva:

1. **Conductor**: cobre estañado o aluminio, clase 2 (cableado concéntrico) según IEC 60228
2. **Pantalla semiconductora interior** (conductor screen): 0,5–1,0 mm, elimina el campo eléctrico tangencial en la interfaz conductor-aislante
3. **Aislamiento XLPE**: 4,5 mm nominal para 8.7/15 kV (IEC 60502-2, tabla 4)
4. **Pantalla semiconductora exterior** (insulation screen): separable en cables reparables, o adherida en cables de distribución
5. **Pantalla metálica**: hilos de cobre en hélice o cinta de cobre, dimensionada para la corriente de falta monofásica a tierra
6. **Cubierta exterior (PE o PVC)**: color rojo para MT en España (recomendación REE/UNESA)

Las designaciones más habituales en España según nomenclatura CENELEC / HD 620:

| Designación | Conductor | Pantalla metálica | Cubierta |
|-------------|-----------|-------------------|----------|
| HEPRZ1 | Cu, XLPE (EPR) | Hilos Cu | LSZH |
| RHZ1 | Cu, XLPE | Hilos Cu | LSZH |
| DHZ1 | Cu, XLPE | Cinta Cu | PE |
| AL HEPRZ1 | Al, XLPE (EPR) | Hilos Cu | LSZH |

Para instalación subterránea directa o en tubo, la variante con armadura (HEPRZ1 2OL, armadura de alambre de acero) proporciona protección mecánica adicional.

---

## Parámetros eléctricos: R, X, C para cálculo de líneas MT

Los tres parámetros distribuidos que determinan el comportamiento eléctrico de la línea MT son:

### Resistencia del conductor (R)

La resistencia de corriente alterna a temperatura de servicio (90 °C) se calcula desde la resistencia CC a 20 °C según IEC 60228, aplicando el coeficiente de temperatura y el factor de incremento por efecto pelicular (skin effect) y efecto de proximidad. Para frecuencia industrial (50 Hz), el factor de skin es despreciable hasta 300 mm², por lo que:

**R_CA(90 °C) ≈ R_CC(20 °C) × [1 + α₂₀ × (90 − 20)]**

Con α₂₀(Cu) = 0,00393 °C⁻¹ → factor = 1 + 0,00393 × 70 = **1,275**

| Sección (mm²) | R_CC 20°C (Ω/km) Cu | R_CA 90°C (Ω/km) Cu | R_CC 20°C (Ω/km) Al | R_CA 90°C (Ω/km) Al |
|:---:|:---:|:---:|:---:|:---:|
| 25 | 0,727 | 0,927 | 1,200 | 1,530 |
| 35 | 0,524 | 0,668 | 0,868 | 1,107 |
| 50 | 0,387 | 0,494 | 0,641 | 0,817 |
| 70 | 0,268 | 0,342 | 0,443 | 0,565 |
| 95 | 0,193 | 0,246 | 0,320 | 0,408 |
| 120 | 0,153 | 0,195 | 0,253 | 0,323 |
| 150 | 0,124 | 0,158 | 0,206 | 0,263 |
| 185 | 0,0991 | 0,126 | 0,164 | 0,209 |
| 240 | 0,0754 | 0,096 | 0,125 | 0,159 |
| 300 | 0,0601 | 0,077 | 0,100 | 0,128 |

*Fuente: IEC 60228 (conductor) + GElectrical database (verificado)*

### Reactancia inductiva (X)

La reactancia de un cable MT unipolar en tresbolillo (trefoil) para 50 Hz es:

**X = 2π × f × L = 2π × 50 × μ₀ × [1/4 + ln(s/r)] / (2π) ≈ 0,0628 × ln(2s/d) [Ω/km]**

Donde **s** = distancia entre ejes de conductores y **d** = diámetro exterior del conductor. En la práctica, para cables XLPE 15 kV en tresbolillo con distancia entre ejes igual al diámetro exterior del cable:

**X ≈ 0,08 Ω/km** (valor de base de datos GElectrical, coherente con IEC 60364-5-52)

Este valor varía entre **0,07 y 0,13 Ω/km** según la sección y configuración:
- Mayor sección → mayor diámetro conductor → mayor s/d relativo → mayor X
- Tresbolillo (trefoil): X mínimo
- Plano con separación: X hasta 1,3× mayor que tresbolillo

### Capacitancia (C) y corriente de carga capacitiva

La capacitancia de un cable MT con pantalla metálica es significativamente mayor que en una línea aérea, al tener la pantalla como retorno a distancia mínima:

**C = 2πε₀ × εr / ln(D/d) [F/m]**

Con εr(XLPE) ≈ 2,3 y geometría normalizada IEC 60502-2:

| Sección (mm²) | C (nF/km) | Ic (A/km) a 15 kV, 50 Hz |
|:---:|:---:|:---:|
| 25 | 200 | 0,544 |
| 35 | 230 | 0,626 |
| 50 | 240 | 0,653 |
| 70 | 260 | 0,707 |
| 95 | 290 | 0,789 |
| 120 | 290 | 0,789 |
| 150 | 290 | 0,789 |
| 185 | 290 | 0,789 |
| 240 | 310 | 0,843 |
| 300 | 330 | 0,898 |

*Fuente: GElectrical database (IEC 60502-2 verificado)*

La corriente capacitiva de carga **Ic = U₀ × ω × C** circula siempre en el cable aunque no haya carga activa, genera pérdidas adicionales en la pantalla y limita la longitud máxima de cable en red aislada o de alta impedancia. Para una línea de 10 km con cable 150 mm², la corriente capacitiva es **7,89 A**, que en un CT 200/5 representa un 3,9% del fondo de escala: no despreciable en relés de protección de tierra.

---

## Capacidad de carga: intensidades admisibles IEC 60502-2

IEC 60502-2 y la serie IEC 60364-5-52 definen las intensidades admisibles para condiciones de referencia:

- **Enterrado**: profundidad 0,7 m, temperatura del terreno 20 °C, resistividad térmica del suelo ρT = 1,0 K·m/W
- **Al aire**: temperatura ambiente 40 °C, en bandeja perforada o en ductero (método E)

| Sección (mm²) | Cu enterrado (A) | Cu aire (A) | Al enterrado (A) | Al aire (A) |
|:---:|:---:|:---:|:---:|:---:|
| 25 | 115 | 145 | 90 | 115 |
| 35 | 140 | 180 | 110 | 140 |
| 50 | 165 | 215 | 130 | 170 |
| 70 | 205 | 270 | 160 | 210 |
| 95 | 245 | 325 | 195 | 255 |
| 120 | 280 | 375 | 220 | 295 |
| 150 | 320 | 425 | 250 | 335 |
| 185 | 365 | 490 | 285 | 385 |
| 240 | 425 | 575 | 335 | 450 |
| 300 | 485 | 655 | 380 | 515 |

*Valores para una terna de cables unipolares XLPE 8.7/15 kV con pantalla de Cu. Factor de potencia de la pantalla incluido.*

### Factores de corrección más relevantes (IEC 60502-2, Anexo B)

| Factor | Condición | Corrección |
|--------|-----------|------------|
| Temperatura terreno 25°C | Terreno más cálido | × 0,96 |
| Temperatura terreno 30°C | Sur de España / verano | × 0,93 |
| Resistividad térmica 1,5 K·m/W | Terreno seco | × 0,88 |
| Resistividad térmica 2,0 K·m/W | Terreno muy seco | × 0,80 |
| 2 cables en paralelo | Agrupación | × 0,87 |
| 3 cables en paralelo | Agrupación | × 0,79 |
| 2 ternas enterradas | Agrupación doble | × 0,75 |

Para un cable 150 mm² Cu en terreno a 30 °C con ρT = 1,5 K·m/W: **320 × 0,93 × 0,88 = 262 A**.

---

## Criterios de selección de sección en instalaciones MT

La selección de la sección de un cable XLPE 15 kV en instalación industrial o en red de distribución sigue un procedimiento jerárquico de tres criterios, aplicados en este orden:

### 1. Criterio térmico en servicio permanente

La intensidad máxima de servicio **Is** (incluidas sobrecargas autorizadas) debe satisfacer:

**Iz ≥ Is / Πfactores_corrección**

Donde **Iz** es la intensidad admisible tabulada. Este criterio selecciona la sección mínima por calentamiento.

### 2. Criterio de cortocircuito (sección mínima por Icc)

La energía específica que debe disipar el conductor en el tiempo de eliminación de falta **tf** (tiempo de despeje del interruptor + relé):

**S_min = (Icc × √tf) / k**

Con **k(Cu, 90°C → 250°C) = 141 A·s^0,5/mm²** (IEC 60949):

Ejemplo: Icc = 12,5 kA (corriente de cortocircuito de diseño en barra MT), tf = 0,5 s (tiempo de apertura relé + interruptor):
**S_min = (12500 × √0,5) / 141 = 62,6 mm²** → sección normalizada mínima: **70 mm²**

La pantalla de cobre también debe ser verificada para la corriente de falta a tierra monofásica. Para una pantalla de hilos de Cu de 16 mm² con k_pantalla = 93:
**Ift_max = 93 × 16 / √tf**

### 3. Criterio de caída de tensión

La caída de tensión en una línea MT trifásica de longitud L (km) transportando potencia activa P (MW) a tensión U (kV) y factor de potencia cosφ:

**ΔU% = (√3 × I × L × (R·cosφ + X·sinφ) / U) × 100**

Para redes de distribución MT en España, el límite habitual es **ΔU ≤ 5%** (Criterio REE/distribuidora). Con X = 0,08 Ω/km, la reactancia es dominante en cables MT de sección ≥ 120 mm² (ya que R_CA ≤ 0,20 Ω/km). La mejora del factor de potencia en carga reduce directamente la caída de tensión en el término **R·cosφ + X·sinφ**.

---

## Conclusión

La selección de un cable XLPE 15 kV según IEC 60502-2 exige verificar tres criterios en orden: capacidad térmica en servicio permanente (con factores de corrección de temperatura del terreno y resistividad), sección mínima por cortocircuito con k = 141 A·s^0,5/mm² para Cu, y caída de tensión. La reactancia de 0,08 Ω/km y la capacitancia de 200–330 nF/km son los parámetros distribuidos más relevantes para el cálculo de flujo de potencia y la evaluación de la corriente capacitiva en redes de alta impedancia. Para instalaciones con agrupación de cables o condiciones de terreno desfavorables (ρT ≥ 1,5 K·m/W), los factores de corrección pueden reducir la capacidad de carga hasta un 20 %, haciendo necesario incrementar la sección prevista por el criterio térmico simple.
