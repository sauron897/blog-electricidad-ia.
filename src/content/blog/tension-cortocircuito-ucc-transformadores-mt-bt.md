---
title: "Tensión de cortocircuito Ucc en transformadores MT/BT"
description: "Calcula la corriente de cortocircuito en el secundario BT según IEC 60076, entiende qué es Ucc, sus valores normalizados y cómo condiciona el poder de corte de tus protecciones."
pubDate: 2026-09-17
keywords: ["tensión cortocircuito transformador", "Ucc transformador BT", "corriente cortocircuito secundario transformador", "IEC 60076", "poder de corte magnetotérmico"]
author: "Editor"
---

## Qué es la tensión de cortocircuito Ucc y por qué la encontrarás siempre en la placa del transformador

La tensión de cortocircuito (Ucc, también escrita como Uk o ε_cc según la norma) es el parámetro más relevante del transformador para el ingeniero de protecciones. Físicamente, es la tensión que hay que aplicar en el primario para que circule la corriente nominal por el secundario cuando éste está en cortocircuito. Se expresa en porcentaje de la tensión nominal y figura en la placa de características de todo transformador de distribución conforme a **IEC 60076-1**.

Lo que esa cifra te dice en obra es directo: cuánta corriente puede entregar el transformador ante un cortocircuito en sus bornas secundarias. Un Ucc bajo → más corriente de falta disponible → mayor demanda al poder de corte de tus protecciones. Un Ucc alto → limita la corriente, pero también eleva la regulación de tensión bajo carga.

El modelo de circuito equivalente descompone Ucc en dos componentes ortogonales:
- **Ucc_R (%)**: componente resistiva, proporcional a las pérdidas en el cobre (Pcc)
- **Ucc_X (%)**: componente reactiva, ligada a la inductancia de dispersión del núcleo

Siendo Ucc = √(Ucc_R² + Ucc_X²). En transformadores de distribución BT, la componente reactiva domina claramente porque Ucc_R ≈ 1–1.5% frente a Ucc ≈ 4–6%.

---

## Valores normalizados de Ucc según IEC 60076 y CENELEC HD 538

La norma **IEC 60076-5** establece los valores mínimos de Ucc en función de la potencia aparente nominal para garantizar la capacidad de soportar las fuerzas electrodinámicas del cortocircuito. La norma europea equivalente es **HD 538 S1** (en España aplicada a través del REBT para los centros de transformación).

Para transformadores de distribución MT/BT, los valores normalizados de la base de datos IEC (GElectrical) son:

| Potencia (kVA) | Tensión primaria (kV) | Ucc (%) | Ucc_R (%) | Ucc_X (%) |
|---|---|---|---|---|
| 250 | 20 / 0,4 | 6,0 | 1,44 | 5,82 |
| 400 | 20 / 0,4 | 6,0 | 1,43 | 5,83 |
| 630 | 20 / 0,4 | 6,0 | 1,21 | 5,88 |
| 250 | 10 / 0,4 | 4,0 | 1,20 | 3,82 |
| 400 | 10 / 0,4 | 4,0 | 1,33 | 3,77 |
| 630 | 10 / 0,4 | 4,0 | 1,08 | 3,86 |

Nota: los transformadores con alimentación a 10 kV presentan Ucc = 4%, mientras que los de 20 kV llevan Ucc = 6%. Este salto tiene consecuencias importantes en el nivel de cortocircuito del cuadro general BT, como se calcula en la siguiente sección.

---

## Cálculo de la corriente de cortocircuito trifásica en bornas del secundario

Asumiendo impedancia de red MT despreciable (fuente infinita — caso más desfavorable para la selección del poder de corte), la corriente de cortocircuito trifásica simétrica en las bornas del secundario es:

**I_cc3f = Sn / (√3 · Vn_BT · Ucc/100)**

Siendo:
- Sn: potencia aparente nominal del transformador (VA)
- Vn_BT: tensión nominal del secundario (V), típicamente 400 V
- Ucc: tensión de cortocircuito en tanto por uno

### Ejemplos numéricos con datos IEC

**Transformador 400 kVA — 20/0,4 kV — Ucc = 6%:**

I_cc3f = 400.000 / (1,732 × 400 × 0,06) = 400.000 / 41,57 = **9.622 A ≈ 9,6 kA**

**Transformador 630 kVA — 20/0,4 kV — Ucc = 6%:**

I_cc3f = 630.000 / (1,732 × 400 × 0,06) = 630.000 / 41,57 = **15.155 A ≈ 15,2 kA**

**Transformador 630 kVA — 10/0,4 kV — Ucc = 4%:**

I_cc3f = 630.000 / (1,732 × 400 × 0,04) = 630.000 / 27,71 = **22.733 A ≈ 22,7 kA**

El último caso es crítico: con el mismo transformador de 630 kVA pero alimentado a 10 kV, la corriente de cortocircuito sube de 15,2 kA a 22,7 kA. Un magnetotérmico con poder de corte de 15 kA, válido para el primero, sería insuficiente para el segundo.

### Impedancia del transformador referida al secundario

La impedancia total del transformador referida a 400 V es:

**Z_T = (Ucc/100) · Vn² / Sn**

Para 400 kVA, Ucc = 6%:
Z_T = 0,06 × (400)² / 400.000 = 0,06 × 0,4 = **24 mΩ**

Componentes:
- R_T = 0,0143 × 0,4 = **5,7 mΩ**
- X_T = √(24² – 5,7²) = **23,3 mΩ**

Este valor de Z_T es el que se introduce en los cálculos de cableado aguas abajo para obtener las corrientes de cortocircuito en los puntos de consumo, siguiendo el **método de las impedancias** descrito en **IEC 60909-0**.

---

## Impacto en la selección del poder de corte: interruptores y fusibles

La **ITC-BT-22 del REBT** exige que todo dispositivo de protección contra cortocircuito tenga una capacidad de corte no inferior a la corriente de cortocircuito previsible en el punto de instalación. Esto se traduce en una regla de selección directa:

**Icu_dispositivo ≥ I_cc3f_punto_instalación**

Los valores típicos de Icu de los MCB según **IEC 60898-1** son 6 kA, 10 kA y 15 kA. Para los MCCB según **IEC 60947-2**, el rango sube hasta 50–100 kA. En la práctica:

| Transformador | Ucc (%) | I_cc3f bornas BT | MCB requerido | MCCB recomendado |
|---|---|---|---|---|
| 250 kVA / 20 kV | 6 | 6,0 kA | Icu ≥ 6 kA | 10 kA clase A |
| 400 kVA / 20 kV | 6 | 9,6 kA | Icu ≥ 10 kA | 15 kA clase B |
| 630 kVA / 20 kV | 6 | 15,2 kA | Icu ≥ 15 kA | 25 kA clase C |
| 630 kVA / 10 kV | 4 | 22,7 kA | Icu ≥ 25 kA | 36 kA clase C |

**Atención**: estos valores son en bornas del secundario. A medida que te alejas del transformador, la impedancia de los cables reduce la corriente de cortocircuito. Un MCB de 6 kA puede ser válido en un subcuadro situado a 50 m del transformador de 630 kVA cuando la impedancia de los cables lo permite, pero nunca en el embarrado del CGBT.

### Cortocircuito monofásico y verificación de la protección diferencial

La corriente de cortocircuito monofásica (fase-neutro) en el secundario de un transformador Dyn11 o YNyn se calcula con la impedancia de secuencia homopolar. Para transformadores Dyn11, la impedancia homopolar referida al secundario es:

**Z_0 = Z_1 / 3** (aproximación válida para el cálculo del mínimo de cortocircuito monofásico en BT)

Esto implica que I_cc1f ≈ 0,95 × I_cc3f en bornas del secundario, lo que confirma que el cortocircuito trifásico sigue siendo el dimensionante para el poder de corte.

---

## Criterios de selección en obra: cómo usar Ucc en tu proceso de diseño

El flujo de decisión para el ingeniero es el siguiente:

1. **Identifica la potencia y la tensión primaria** del transformador de la instalación. Si alimenta desde 20 kV → Ucc ≈ 6%. Si alimenta desde 10 kV → Ucc ≈ 4%.

2. **Calcula I_cc3f en bornas BT** con la fórmula Sn / (√3 · Vn · Ucc/100). Usa el Ucc real de la placa, no el típico.

3. **Selecciona el MCCB del CGBT** con Icu ≥ I_cc3f. Añade un margen del 10–15% por posibles variaciones de Ucc entre unidades del mismo lote (IEC 60076-1 admite tolerancias de ±10% en Ucc para transformadores de distribución).

4. **Propaga el cálculo aguas abajo** sumando las impedancias de los tramos de cable con la reactancia y resistencia por metro (IEC 60364-4-43 y método IEC 60909-0). La corriente baja conforme la longitud aumenta.

5. **Verifica la actuación de las protecciones en falta franca monofásica** (mínimo de cortocircuito) para asegurar el disparo magnético de los magnetotérmicos, especialmente en derivaciones largas.

6. **Documenta el Ucc usado en el cálculo**. En una auditoría o verificación posterior, la sustitución del transformador por una unidad de diferente Ucc puede invalidar toda la coordinación de protecciones.

---

## Conclusión

La Ucc no es un dato de catálogo que se consulta una vez y se olvida: es la variable que fija el nivel de cortocircuito de toda la instalación BT aguas abajo del transformador. Un transformador de 630 kVA alimentado a 10 kV (Ucc = 4%) entrega 22,7 kA en sus bornas secundarias, mientras que el mismo trasformador a 20 kV (Ucc = 6%) se limita a 15,2 kA. Esa diferencia de 7,5 kA determina la clase del MCCB del CGBT, el tipo de fusibles de protección y la viabilidad de los MCB en los subcuadros.

Calcula siempre con el Ucc de la placa del transformador instalado, no con el valor teórico IEC. Verifica el poder de corte en bornas BT y propaga el cálculo según IEC 60909-0 hasta el último punto de protección.
