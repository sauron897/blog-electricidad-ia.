---
title: "Protección de cables BT contra cortocircuito: criterio adiabático IEC 60364-4-43"
description: "Verificación térmica de cables frente a cortocircuito: ecuación adiabática I²t ≤ k²S², coeficientes k por tipo de aislamiento y coordinación según IEC 60364-4-43 e ITC-BT-22."
pubDate: 2026-10-17
keywords: ["protección cables cortocircuito criterio adiabático IEC 60364-4-43", "coeficiente k adiabático cable cobre XLPE PVC", "sección mínima cable cortocircuito", "ITC-BT-22 protección sobreintensidades cables BT"]
author: "Editor"
---

La selección de la sección de un cable por criterio de intensidad admisible (ITC-BT-19, IEC 60364-5-52) no garantiza su integridad frente a un cortocircuito. Un conductor correctamente dimensionado en régimen permanente puede quedar destruido en décimas de segundo si el dispositivo de protección no limita a tiempo la energía térmica del defecto. La verificación de la protección contra cortocircuito exige dos comprobaciones independientes y distintas a las del régimen nominal: el poder de corte del aparato y el criterio adiabático del conductor.

IEC 60364-4-43 (edición 2023, armonizada en España como UNE-HD 60364-4-43) establece los requisitos de protección contra sobreintensidades, y su sección 434 regula específicamente la protección de los conductores contra cortocircuito. El REBT español la transpone en ITC-BT-22, que en su apartado 3 exige que la energía específica pasante del dispositivo no supere la energía admisible por el conductor.

## Fundamento físico: calentamiento adiabático del conductor

Durante un cortocircuito, la potencia disipada en el conductor es **P = I²·R** por unidad de longitud. Para un conductor de cobre de 16 mm², resistencia de ≈ 1,15 Ω/km a 90 °C, con una corriente de cortocircuito de 10 kA, la potencia por metro es:

**P = (10 000)² · 1,15 × 10⁻³ = 115 000 W/m**

A esa densidad de potencia, el calor cedido al entorno —por convección y conducción hacia el aislamiento— es despreciable en comparación con el calor generado. El proceso es, con buena aproximación, **adiabático** para duraciones de cortocircuito inferiores a 5 s. Todo el calor producido eleva la temperatura del conductor.

El límite es la temperatura máxima admisible para el aislamiento durante un cortocircuito: 160 °C para PVC (frente a los 70 °C en régimen permanente) y 250 °C para XLPE/EPR (frente a los 90 °C en régimen permanente). Superar esas temperaturas durante el defecto degrada irreversiblemente el aislamiento, aunque el conductor no se funda físicamente.

El balance de energía adiabático es:

**I² · R · t = Qc · ρc · S · l · (Tf − Ti)**

donde Qc es la capacidad calorífica volumétrica del conductor (J·K⁻¹·mm⁻³), ρc la densidad, S la sección (mm²), l la longitud (m) y Tf − Ti el incremento de temperatura admisible. Como R = ρe·l/S (siendo ρe la resistividad eléctrica), la longitud se cancela y la ecuación queda en función de la sección únicamente:

**I² · t ≤ k² · S²**

Esta es la **ecuación adiabática fundamental** (IEC 60364-4-43, §434.3.1). El factor k agrupa las constantes físicas del material.

## La ecuación adiabática: parámetros y coeficiente k

Despejando la sección mínima del conductor para una energía específica pasante dada:

**S_min = √(I²·t) / k [mm²]**

Y el tiempo máximo que puede circular una corriente Icc sin dañar el cable de sección S:

**t_max = (k·S / I)² [s]**

El coeficiente k se determina a partir de las propiedades físicas del conductor (IEC 60364-5-54, Tabla B.54.1, adoptada en IEC 60364-4-43):

| Conductor | Aislamiento | Ti (°C) | Tf (°C) | **k** |
|---|---|---|---|---|
| Cobre | PVC | 70 | 160 | **115** |
| Cobre | XLPE / EPR | 90 | 250 | **143** |
| Aluminio | PVC | 70 | 160 | **76** |
| Aluminio | XLPE / EPR | 90 | 250 | **94** |
| Cobre | Goma vulcanizada (85°C) | 85 | 220 | **134** |

Para secciones superiores a 300 mm² con aislamiento PVC, la temperatura final baja a 140 °C por limitación mecánica; el valor de k cae a 103 para cobre y 68 para aluminio en ese rango.

## Verificación al inicio y al final del tramo

La protección contra cortocircuito exige verificar el cumplimiento en **dos puntos del tramo**, correspondientes a condiciones de defecto distintas:

**Verificación en el origen del tramo (Icc máxima):**

La corriente de cortocircuito máxima se produce con un defecto trifásico franco (impedancia de defecto nula) en los bornes del origen del tramo, con la red alimentando al máximo (V = 1,05·Vn según IEC 60909). Esta corriente determina si el **poder de corte** del aparato de protección es suficiente:

**Icu ≥ Icc_max** (IEC 60947-2 para MCCB; IEC 60898-1 para MCB doméstico)

Un MCB estándar IEC 60898-1 tiene Icc = 10 kA. Si la corriente de cortocircuito trifásica en el punto de instalación supera ese valor —habitual en cuadros de distribución cercanos al transformador—, es necesario un MCCB o coordinar con fusibles de respaldo.

**Verificación en el final del tramo (Icc mínima):**

La corriente de cortocircuito mínima se calcula para un defecto **fase-neutro** (en sistemas TN) o **fase-fase** (en sistemas TT/IT) al final del tramo, con la red al 95% de tensión nominal y en condiciones de máxima impedancia. Esta es la que determina si el dispositivo de protección **actúa en tiempo suficiente** para no dañar el cable:

**I²·t_disp(Icc_min) ≤ k²·S²**

donde t_disp(Icc_min) es el tiempo de actuación del dispositivo de protección a esa corriente (leído de su curva I-t).

## Energía específica pasante I²t de dispositivos MCB y fusibles

En la práctica, los fabricantes proporcionan directamente la **energía específica pasante** del dispositivo de protección, que es la integral ∫I²dt durante la apertura. Para la verificación adiabática se utiliza:

**I²t_pasante (dispositivo) ≤ k²·S² (conductor)**

Para MCB con curva C de 16 A (IEC 60898-1), la energía específica pasante a 10 kA es del orden de **10⁵ A²·s** (valor orientativo; el fabricante publica la curva I²t específica). Para un cable de cobre 2,5 mm² XLPE:

**k²·S² = 143² · 2,5² = 127 806 A²·s**

La condición se cumple si I²t_pasante ≤ 127 806 A²·s. Cuando el valor pasante supera el admisible, se puede aumentar la sección del cable, instalar un fusible de respaldo (cuya curva I²t es más favorable para protección de cables), o reducir la impedancia de la alimentación.

Para fusibles tipo gG (IEC 60269-1), la energía pasante a corrientes de cortocircuito elevadas es significativamente menor que la de un MCB equivalente, lo que hace al fusible preferible como protector de cable en instalaciones con Icc alta.

## Criterios de selección y coordinación en obra

La siguiente tabla resume los criterios de decisión para la verificación adiabática en instalaciones BT industriales y de edificios:

| Condición a verificar | Criterio | Norma de referencia |
|---|---|---|
| Poder de corte del dispositivo | Icu ≥ Icc_max en el punto de instalación | IEC 60947-2 / IEC 60898-1 |
| Energía pasante total | I²t_pasante ≤ k²·S² | IEC 60364-4-43 §434.3 |
| Actuación en Icc_min | t_disp(Icc_min) ≤ t_max = (kS/Icc_min)² | IEC 60364-4-43 §434.3.2 |
| Protección de neutro | Sección ≥ S_fase/2 si In sección reducida | ITC-BT-22 §3 / IEC 60364-4-43 §434.4 |
| Aplicación de coordinación back-up | I²t (fusible back-up) ≤ k²S² del MCCB protegido | IEC 60947-2 Anexo B |

**Reglas prácticas para el diseño:**

1. **MCB curva C ≤ 32 A + cable Cu XLPE ≥ 2,5 mm²**: en instalaciones domésticas e industriales con Icc ≤ 6 kA al final del tramo, la combinación normalizada suele verificarse por construcción, pero conviene confirmarlo cuando la longitud del tramo supera 30 m desde el cuadro.

2. **MCCB + cables de gran sección**: es imprescindible consultar la curva I²t del fabricante. Un MCCB de 250 A puede tener una energía pasante de 10⁶–10⁷ A²·s a corrientes de cortocircuito altas, lo que exige cables de 50 mm² o más para Cu XLPE.

3. **Tramos largos en instalaciones industriales**: la Icc_min al final del tramo puede caer a valores próximos a 5·In del MCB. El dispositivo puede actuar en zona de retardo (5–30 s) o incluso no actuar si Icc_min < 5·In. Verificar siempre la longitud máxima del tramo con la fórmula:

   **L_max = (k·S·V_fase) / (In_fus·√2·ρ20·(1+α·ΔT)) [m]** (simplificado para defecto fase-neutro en sistema TN)

4. **Conductores de aluminio**: el coeficiente k más bajo (76 para PVC, 94 para XLPE) implica que, a igual sección, un cable de aluminio es más vulnerable térmicamente que uno de cobre. Para las mismas condiciones de cortocircuito, el aluminio necesita una sección un 51 % mayor que el cobre (ratio k_Cu/k_Al ≈ 115/76 = 1,51 para PVC).

5. **Conductor de protección PE**: IEC 60364-5-54 e ITC-BT-18 exigen que el PE cumpla también la condición adiabática. Si el PE es de la misma sección que los conductores de fase, el coeficiente k aplicable es 115 (Cu/PVC) pero con Ti = 30 °C y Tf = 160 °C, lo que da k ≈ 143 para el conductor aislado y k ≈ 115 para el conductor desnudo empotrado en hormigón.

## Conclusión

La verificación adiabática I²t ≤ k²S² no es una formalidad de cálculo: es la comprobación que garantiza que el cable no queda dañado durante el tiempo que tarda en actuar la protección. En obra, los dos errores más frecuentes son sobredimensionar el cable para cumplir la caída de tensión sin verificar si el MCB tiene el poder de corte suficiente, y subestimar la Icc_min al final de tramos largos. El uso de las curvas I²t del fabricante del dispositivo, combinado con los valores de k de IEC 60364-4-43 Tabla B.54.1 —143 para cobre XLPE, 115 para cobre PVC—, permite una verificación rápida y rigurosa que cierra la coordinación del sistema de protecciones desde el transformador hasta el último receptor.
