---
title: "Protección diferencial de transformador MT/BT: relé de porcentaje IEC 60255-187-1"
description: "Ajuste del relé diferencial de porcentaje para transformadores MT/BT: pendiente (slope), umbral de arranque, restricción armónica por inrush y compensación de grupo vectorial según IEC 60255-187-1 e IEC 60076."
pubDate: 2026-10-07
keywords: ["protección diferencial transformador", "relé diferencial porcentaje IEC 60255-187-1", "ajuste slope diferencial transformador", "restricción armónicos inrush transformador", "protección transformador MT BT"]
author: "Editor"
---

La protección diferencial de porcentaje es la función de protección principal de cualquier transformador de potencia en instalaciones MT/BT. A diferencia de las protecciones de sobreintensidad, que actúan como respaldo ante faltas externas, el relé diferencial detecta exclusivamente los fallos dentro de la zona protegida —los devanados, el aceite y el núcleo— con tiempos de actuación inferiores a 40 ms y sin necesidad de escalonamiento temporal.

La norma IEC 60255-187-1 (adoptada en España como UNE-EN IEC 60255-187-1:2021) sustituyó a IEC 60255-13 y establece los requisitos funcionales, las características de operación y los ensayos de tipo para protecciones diferenciales de transformadores, motores y generadores. Si diseñas o ajustas la protección de un transformador MT/BT, esta norma —junto con IEC 60076 para los parámetros del transformador— es el punto de partida obligatorio.

## Característica de porcentaje: plano Idiff–Ibias

En un relé diferencial de porcentaje, la condición de operación se define en el plano corriente diferencial / corriente de restricción (bias):

- **Idiff** = |I₁ + I₂| en p.u. de la corriente nominal del transformador (In)
- **Ibias** = (|I₁| + |I₂|) / 2, corriente de restricción

El relé opera cuando:

> Idiff > I_pick + m × Ibias

donde **I_pick** es el umbral mínimo de arranque y **m** es la pendiente (slope). La característica de dos pendientes (dual-slope), exigida implícitamente por IEC 60255-187-1 §5.2 para cubrir tanto el régimen normal como la saturación de TC en falta externa severa, divide el plano en dos zonas:

### Zona 1 — Pendiente baja (m1): régimen normal

Se aplica para Ibias de 0 hasta el punto de quiebre (breakpoint), típicamente **1,5 – 3 × In**. La pendiente m1 debe cubrir la suma de errores de los transformadores de corriente (TC) en ambos lados:

> m1 ≥ 2 × (ε_TC_HV + ε_TC_LV)

Para TC de clase 5P con error de ratio ≤ 1% y error de fase ≤ 5%:

> m1 ≥ 2 × (5% + 5%) = 20% → ajuste en **25–30%** con margen de seguridad

### Zona 2 — Pendiente alta (m2): saturación de TC en falta exterior

Se activa por encima del breakpoint, cuando el corriente de restricción alcanza niveles de cortocircuito. La corriente máxima de paso (through-fault) que debe soportar el relé sin operar es directamente función de la tensión de cortocircuito del transformador (Ucc), según IEC 60076:

| Transformador (IEC 60076 / GElectrical) | Sn | Ucc | Imax_through = In/Ucc |
|---|---|---|---|
| 63 MVA 110/20 kV | 63 MVA | 18,0 % | 5,6 × In |
| 40 MVA 110/20 kV | 40 MVA | 16,2 % | 6,2 × In |
| 25 MVA 110/20 kV | 25 MVA | 12,0 % | 8,3 × In |
| 0,63 MVA 20/0,4 kV | 630 kVA | 6,0 % | 16,7 × In |
| 0,63 MVA 10/0,4 kV | 630 kVA | 4,0 % | 25,0 × In |
| 0,25 MVA 10/0,4 kV | 250 kVA | 4,0 % | 25,0 × In |

Para el transformador de 63 MVA 110/20 kV (Ucc = 18 %):

- Imax_through = 5,6 × In
- Idiff_max debida a errores de TC al 10 % de ratio: 0,10 × 5,6 = 0,56 In
- Con m2 = 70 % y breakpoint = 2 In: Idiff_umbral(5,6 In) = 0,70 + 0,70 × (5,6 – 2) = 0,70 + 2,52 = **3,22 In**
- Margen de estabilidad: 3,22 In >> 0,56 In ✓

Para distribución con Ucc = 4 % (Imax = 25 × In) y m2 = 80 %:

- Idiff_umbral(25 In) = 0,70 + 0,80 × (25 – 2) = **19,1 In** >> Idiff_error = 2,5 In ✓

## Compensación del grupo vectorial y del regulador de tomas

Un transformador YNd11 (shift 330°) o Dyn11 (shift 30°) introduce un desfase de ±30° entre los fasores de corriente del primario y el secundario. Sin compensación, Idiff ≠ 0 incluso en vacío, y el relé operaría erróneamente.

Los relés modernos aplican compensación numérica matricial. Para un transformador Yd11 (HV = estrella, LV = triángulo, reloj 11):

- Corrección en el lado Y: I_HV_comp = (1/√3) × [Ia – Ib; Ib – Ic; Ic – Ia]

Esta transformación también elimina las corrientes de secuencia cero en faltas monofásicas externas que no penetran en la zona protegida (cuando el neutro del transformador no está directamente implicado). IEC 60255-187-1 §5.3 exige que el relé compense todos los grupos vectoriales normalizados IEC 60076-1.

El **regulador de tomas bajo carga (OLTC)** introduce errores adicionales de ±10–15 % en la relación de transformación. El umbral I_pick y la pendiente m1 deben absorberlos:

> m1 ≥ 2 × (Σ errores_TC) + desviación_OLTC_max

Para OLTC de ±10 % y TC clase 5P: m1 ≥ 20 % + 10 % = 30 % → en la práctica, m1 = **25–35 %**.

## Restricción por armónicos: inrush y sobreexcitación

### Corriente de inrush (2.º armónico)

Al energizar un transformador en vacío, la corriente de magnetización puede alcanzar 8–12 × In durante los primeros ciclos. Esta corriente aparece solo en el lado de alimentación, generando un Idiff elevado que sin restricción haría operar el relé.

La característica de esta corriente es su elevado contenido de 2.º armónico (I2h), típicamente >20 % de la fundamental. IEC 60255-187-1 §6.4 define el umbral de restricción:

- **Bloqueo por 2.º armónico**: si I2h / I1h > I2h_threshold, bloquea la función diferencial
  - Umbral típico: **15–20 %**
  - Ajuste más conservador (mayor threshold) → menor riesgo de bloqueo ante falta interna durante energizado, pero mayor riesgo de operación no deseada en transformadores modernos con hierro de baja pérdida y alta I2h

El bloqueo cruzado entre fases (cross-block) aplica la restricción de la fase con inrush a las tres fases. Algunos relés permiten desactivarlo para mejorar la sensibilidad ante faltas internas simultáneas al energizado.

### Sobreexcitación (5.º armónico)

La sobreexcitación (relación V/Hz elevada) satura el núcleo generando corriente con alto contenido de 5.º armónico (I5h). Si I5h / I1h > I5h_threshold, el relé bloquea o restringe la operación diferencial:

- Umbral típico: **30–40 %** de la fundamental
- Crítico en transformadores de generador (GSU) donde puede producirse V/Hz elevada durante arranques o pérdida de carga

## Criterios de ajuste y diagnóstico según IEC 60255-187-1

| Parámetro | Rango recomendado | Criterio |
|---|---|---|
| **I_pick** (umbral arranque) | 0,10 – 0,25 × In | ≥ 1,5 × I0_trafo; cubrir error de TC en vacío |
| **m1** (pendiente zona 1) | 15 – 35 % | ≥ 2 × Σ errores_TC + desviación_OLTC |
| **Breakpoint (Ibias_q)** | 1,5 – 3 × In | Típico 2 × In (paso de régimen normal a saturación) |
| **m2** (pendiente zona 2) | 60 – 90 % | Estabilidad hasta Imax_through = In/Ucc |
| **I2h_threshold** (inrush) | 15 – 20 % | 15 % default IEC 60255-187-1; aumentar en trafo de baja pérdida |
| **I5h_threshold** (sobreexcitación) | 30 – 40 % | 35 % default; ajustar según curva V/Hz del trafo |

**Umbral de arranque y corriente de magnetización (IEC 60076 / GElectrical)**:

| Transformador | I0 (% de In) | I_pick mínimo recomendado |
|---|---|---|
| 63 MVA 110/20 kV | 0,04 % | 0,20 × In |
| 25 MVA 110/20 kV | 0,07 % | 0,20 × In |
| 0,63 MVA 10/0,4 kV | 0,19 % | 0,20 × In |
| 0,25 MVA 10/0,4 kV | 0,24 % | 0,20 × In |
| 100 kVA 11/0,4 kV | 2,50 % | 0,15 × In |

Para todos los transformadores anteriores, I_pick = 0,15–0,20 × In es suficiente para superar I0 con margen amplio.

**Lógica de diagnóstico en comisionado**:

1. **Inyección secundaria** con la corriente de prueba correctamente compensada por grupo vectorial: verificar que el relé no opera en la zona de bloqueo y opera en la zona diferencial con las corrientes de prueba esperadas
2. **Prueba de estabilidad por falta exterior**: inyectar Imax_through en ambos lados simultáneamente (con desfase de TC correcto); verificar no operación
3. **Prueba de inrush simulado**: inyectar corriente con 20 % de 2.º armónico; verificar bloqueo. Inyectar misma corriente con 10 % de 2.º armónico; verificar operación

## Conclusión

El ajuste correcto de un relé diferencial de porcentaje para transformador MT/BT requiere combinar los parámetros reales del transformador (Ucc, I0, grupo vectorial de IEC 60076), las clases de precisión de los TC y los requisitos de IEC 60255-187-1. Los criterios clave: I_pick ≥ 0,15–0,20 × In para superar la corriente de magnetización, m1 en 25–35 % para absorber errores de TC y variación de tomas, m2 en 70–80 % para garantizar estabilidad hasta Imax_through, y umbrales de armónicos calibrados al tipo de núcleo del transformador. Antes de la puesta en servicio, la inyección secundaria con verificación por grupo vectorial es el único método fiable para confirmar que el ajuste es correcto en la instalación real.
