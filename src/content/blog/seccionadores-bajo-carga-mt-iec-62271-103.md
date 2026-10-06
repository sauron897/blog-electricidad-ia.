---
title: "Seccionadores bajo carga en MT: tipos y selección IEC 62271-103"
description: "Tipos de seccionadores bajo carga en media tensión, capacidades de conmutación, tecnologías SF6/vacío/sólido y criterios de selección para CTs según IEC 62271-103."
pubDate: 2026-10-06
keywords: ["seccionador bajo carga MT IEC 62271-103", "switch-disconnector 15kV 24kV seleccion", "celda MT seccionamiento RMU", "capacidad corte carga media tension", "interruptor seccionador SF6 vacio solido"]
author: "Editor"
---

## Alcance y nomenclatura en IEC 62271-103

Un **seccionador bajo carga** (load break switch o switch-disconnector) es un aparato de aparamenta MT capaz de establecer y cortar corrientes en condiciones normales de explotación, incluyendo sobrecargas definidas, pero sin capacidad para interrumpir corrientes de cortocircuito. Se diferencia del interruptor automático (IEC 62271-100) en que no tiene función de protección, y del seccionador en vacío (IEC 62271-102) en que sí puede cortar corriente de carga.

La norma de referencia es **IEC 62271-103:2011** (*High-voltage switchgear and controlgear — Part 103: Switches for rated voltages above 1 kV up to and including 52 kV*), con la segunda edición IEC 62271-103:2021 que alinea terminología con IEC 62271-1:2017 en ensayos dieléctricos y categorías mecánicas. La versión UNE-EN 62271-103 transpone estas exigencias al marco normativo español.

En terminología española consolidada:
- **Interruptor de carga** (switch): capaz de cortar y establecer corriente de carga (In), pero no corriente de cortocircuito.
- **Interruptor-seccionador** (switch-disconnector): interruptor de carga cuya posición abierta cumple adicionalmente los requisitos dieléctricos de aislación propios de un seccionador: distancias de apertura certificadas, ensayo de impulso de rayo sobre la distancia entre contactos.

En las **celdas modulares tipo RMU** (Ring Main Unit), el interruptor-seccionador es el elemento estándar para las posiciones de línea en la acometida y el mallado de red. La posición de protección de transformador combina interruptor-seccionador con fusibles MT o con relé + interruptor automático.

---

## Tensiones normalizadas y corrientes asignadas

IEC 62271-103 cubre tensiones de 1 kV < Ur ≤ 52 kV. En distribución española los valores de uso habitual son:

| Ur (kV) | Um máx. (kV) | NBI (kV cresta) | NPS (kV ef.) | Uso típico en España |
|--------|-------------|-----------------|--------------|----------------------|
| 12     | 12          | 75              | 28           | Redes subterráneas urbanas 10–11 kV |
| 17,5   | 17,5        | 95              | 38           | Distribución peninsular 20 kV (más habitual) |
| 24     | 24          | 125             | 50           | Redes industriales 22 kV, algunas CCAA |
| 36     | 36          | 170             | 70           | Redes rurales 30 kV, zonas de montaña |

*Ur = tensión asignada del aparato. Um = tensión máxima del sistema (IEC 62271-1, Tabla 1). NBI = Nivel Básico de Aislamiento por impulso de rayo (1,2/50 μs). NPS = Nivel de ensayo a frecuencia industrial (50 Hz, 1 min). La red española de distribución opera a 20 kV nominal → aparato de 17,5 kV si Um_red ≤ 17,5 kV, o de 24 kV en instalaciones con margen ampliado.*

Las **corrientes asignadas normalizadas** para interruptores de carga MT son **400 A** y **630 A** (IEC 62271-103, Tabla 1). La capacidad de corte bajo carga nominal es igual a la corriente asignada de servicio normal (Ir = In), a diferencia del interruptor automático donde Icu >> In.

Las corrientes de cortocircuito resistente (Ith, durante 1 s o 3 s) normalizadas son **12,5 kA / 16 kA / 20 kA / 25 kA**. La corriente de cresta de cierre (Ipm) es **2,5 × Ith** según IEC 62271-103, Tabla 3.

---

## Tecnologías de extinción de arco

### SF6 (hexafluoruro de azufre)

Tecnología dominante desde los años 1970 en aparamenta compacta sellada. El gas SF6 a presión de 0,3–0,5 bar relativo actúa simultáneamente como dieléctrico y como agente extintor del arco eléctrico por su alta electronegatividad molecular (captura electrones libres del plasma). Propiedades clave:

- Tensión de ruptura 2,5–3 × mayor que el aire a presión atmosférica equivalente.
- Extinción de arco en el primer paso por cero de la corriente (< 10 ms), sin productos sólidos de descomposición a niveles de energía de baja tensión de corte.
- Rango de temperatura de servicio: –40 °C a +70 °C (celdas exteriores en poste).

**Restricción regulatoria**: el SF6 tiene un potencial de calentamiento global (GWP100) de 23.500 veces el CO₂. La **Directiva 2024/573/UE** (revisión del Reglamento F-Gas, vigor desde enero 2025) prohíbe la comercialización de nueva aparamenta MT sellada ≤ 52 kV que use SF6 a partir del **1 de enero de 2031** para equipos con vida útil prevista ≥ 20 años. Los fabricantes ofrecen equipos equivalentes con gases alternativos de baja GWP (3M Novec 5110, g³ de ABB con C₄F₇N + CO₂, Clean Air de Schneider con N₂ + CO₂) que alcanzan las mismas prestaciones dieléctricas con GWP < 1.

### Vacío

Los contactos se abren en una cámara de vacío sellada (presión residual < 10⁻³ Pa). El arco eléctrico se extingue en el primer paso por cero al condensarse el plasma metálico vaporizado sobre el escudo metálico interior. Propiedades clave:

- Sin gas de efecto invernadero. Cámara sellada de por vida, sin mantenimiento.
- Alta resistencia al desgaste de contactos: > 30.000 operaciones en carga (categoría M2 con holgura).
- Válido para redes de 12 kV y 17,5 kV en celdas compactas de interior.

**Limitación por TRV**: el interruptor de vacío presenta una tasa de restablecimiento de tensión (TRV, *Transient Recovery Voltage*) más elevada que el SF6 al cortar cargas inductivas con bajo cos φ (transformadores en vacío, reactancias en compensación). Esto puede generar sobretensiones de corte (voltage chopping) de hasta 3–5 × Un si el aparato no está específicamente certificado para corte de **corriente de magnetización** (magnetizing current switching). Verificar la certificación según IEC 62271-103, Apartado 6.104.

### Dieléctrico sólido (resina epoxi cicloalifática / silicona reticulada SiR)

Los contactos, junto con la cámara de vacío que los alberga, quedan embebidos en resina epoxi cicloalifática (HCEP) o elastómero de silicona reticulada. El aislamiento general es sólido; la extinción del arco sigue siendo en vacío. Ejemplo comercial: ABB SafeRing-B, Schneider RM AirSeT, Lucy Gemini-V.

- Sin gas de proceso. Sin restricciones por F-Gas 2024/573/UE.
- Índice de protección IP67 de serie (inmersión temporal), adecuado para instalaciones en zonas inundables o de alta humedad.
- Dimensiones reducidas (< 0,5 m³ para RMU de 3 posiciones a 17,5 kV / 630 A).

---

## Ensayos de tipo según IEC 62271-103

Los ensayos de tipo (type tests) que certifica el fabricante para una gama de aparatos son los siguientes. Ningún ensayo puede omitirse ni extrapolarse de otra gama sin nueva certificación.

| Ensayo | Norma de referencia | Criterio de aceptación |
|--------|---------------------|----------------------|
| Dieléctrico a 50 Hz (1 min) | IEC 62271-1, § 6.2 | Sin perforación ni contorneamiento. Valores NPS de la tabla anterior |
| Impulso de rayo (LI, 1,2/50 μs) | IEC 62271-1, § 6.2 | 3 impulsos + 3 – sobre fase y distancia de contactos. Valores NBI de la tabla anterior |
| Resistencia de contactos | IEC 62271-1, § 6.4 | R_cc ≤ valor de diseño (típico < 100 μΩ en 630 A) |
| Calentamiento a corriente nominal | IEC 62271-1, § 6.5 | ΔT bornes ≤ 65 K, aisladores externos ≤ 40 K sobre temperatura ambiente |
| Resistencia al cortocircuito (Ith, Ipm) | IEC 62271-103, § 6.101 | 3 cierres a Ipm + conducción 1 s a Ith sin daño funcional |
| Corte de corriente de carga (In) | IEC 62271-103, § 6.102 | 10 operaciones C-O a In; 5 bajo cos φ = 0,7; 5 bajo cos φ = 0,5 |
| Corte de cable-charging (Ic) | IEC 62271-103, § 6.103 | 10 operaciones a Ic normalizada (véase tabla § 6.103); sin reignición |
| Corte de corriente de magnetización | IEC 62271-103, § 6.104 | Sin sobretensiones de corte > 2 × (√2 × Ur) sobre el transformador |
| Vida mecánica | IEC 62271-103, § 6.105 | M1: ≥ 1.000 op. sin carga. M2: ≥ 2.000 op. sin degradación funcional |
| Protección (IP) | IEC 60529 | IP54 mínimo interior / IP65–IP67 exterior o GIS sellado |

El ensayo de corte de corriente de magnetización (§ 6.104) diferencia los interruptores de carga aptos para posiciones de protección de transformador de los que solo sirven para acometida de línea.

---

## Capacidades de conmutación específicas

### Corriente de carga de cable (cable-charging current)

Al abrir una línea de cable subterráneo sin carga, la capacidad del cable genera una corriente capacitiva. Para un cable XLPE de 3 km a 17,5 kV con C = 0,30 μF/km:

*Ic = (Ur / √3) × ω × C × L = (17.500 / √3) × 2π × 50 × (0,30 × 10⁻⁶ × 3) = **2,85 A***

IEC 62271-103 establece una corriente asignada de cable-charging de **40 A** para Ur = 17,5 kV (Tabla 5 de la norma). El aparato debe cortar sin reignición del arco en la apertura.

### Corriente de magnetización de transformador

Un transformador de distribución de 630 kVA, 20/0,4 kV, Ucc = 4%, Im = 0,8%:
- In_MT = 630 kVA / (√3 × 20 kV) = **18,2 A**
- Im = 0,8% × 18,2 = **0,15 A** (corriente pequeña pero con cos φ ≈ 0,02–0,05 — casi puramente inductiva)

Esta corriente diminuta con factor de potencia próximo a cero es la más difícil de cortar sin reignición. Un aparato no certificado genera sobretensiones de corte de 6–8 × Un en los bornes del transformador, degradando el aislamiento del bobinado.

### Corriente de bucle (loop switching)

En una red en anillo, cerrar o abrir el bucle implica una diferencia de ángulo entre los dos lados. La corriente de bucle típica en distribución española a 20 kV es de **100–400 A** con cos φ ≈ 0,7. El interruptor debe certificar este ensayo (IEC 62271-103, § 6.102.3) para su uso en posiciones de maniobrabilidad en anillo.

---

## Criterios de selección en instalación

**1. Tensión asignada Ur:** Seleccionar el escalón normalizado superior a la tensión máxima de servicio de la red. En España, red 20 kV (Un):
- Ur = **17,5 kV** si el distribuidor garantiza Um_red ≤ 17,5 kV (verificar Reglamento de Redes, RD 337/2014 ITC-LAT-05).
- Ur = **24 kV** cuando se requiere margen frente a sobretensiones temporales (redes con neutro aislado o resonante sin compensación Petersen).

**2. Corriente de cortocircuito resistente Ith:** Calcular Icc en el punto de instalación según **IEC 60909-0**. Para un nudo de 20 kV alimentado desde un transformador de red de 40 MVA con Ucc = 12%:

*Icc = Sn / (√3 × Un × Ucc) = 40.000 kVA / (√3 × 20 kV × 0,12) = **9.623 A ≈ 9,6 kA***

*Ipm = 2,5 × 9.623 = **24 kA cresta*** → especificar aparato con Ith ≥ 12,5 kA (1 s) e Ipm ≥ 31,25 kA.

**3. Posición funcional en la celda:**

| Posición | Función | Capacidades obligatorias |
|----------|---------|--------------------------|
| Línea / acometida | Seccionamiento de línea, corte de bucle | In, Ic (cable-charging), loop switching |
| Protección de transformador | Seccionamiento + maniobra sobre transformador vacío | In, Ic, magnetizing current, fusibles coordinados |
| Condensador / batería reactiva | Corte de banco de condensadores | In + capacitor switching certificado (§ 6.103.2) |
| Acometida motorizada / telecontrol | Seccionamiento automático con RTU | M2, vida mecánica ≥ 2.000 op., categoría eléctrica E2 |

**4. Tecnología de extinción:**

| Requisito | Tecnología recomendada |
|-----------|------------------------|
| Celdas de interior, RMU compacta, nueva obra | Vacío o dieléctrico sólido (sin restricciones F-Gas) |
| Exterior en poste o intemperie, rango –40 °C | SF6 o gas eco-eficiente (GWP < 1) |
| Instalación en zona inundable, IP67 obligatorio | Dieléctrico sólido (resina epoxi + vacío) |
| Cumplimiento anticipado Directiva 2024/573/UE | Dieléctrico sólido o vacío sin gas auxiliar |

**5. Categoría de vida mecánica:**
- **M1**: mantenimiento periódico cada 5–10 años; válido para posiciones de línea con < 50 operaciones/año.
- **M2**: sin mantenimiento funcional durante la vida útil (25 años); obligatorio en posiciones motorizadas, con RTU o en celdas de difícil acceso (soterradas, en poste alto).

---

## Conclusión

El interruptor-seccionador de carga MT según IEC 62271-103 es el elemento de conmutación de referencia en celdas de distribución de 10–36 kV. La selección exige verificar Ur frente a Um_red, Ith e Ipm calculados por IEC 60909-0, la corriente asignada de cable-charging y la certificación de corte de corriente de magnetización en posiciones de transformador. La Directiva F-Gas 2024/573/UE convierte la tecnología de vacío y dieléctrico sólido en la opción de proyecto con mayor proyección en celdas de interior; SF6 mantiene su posición en aplicaciones de exterior y redes de 36 kV. La categoría de vida mecánica M2 y la hermeticidad IP65/IP67 son determinantes en instalaciones telecontroladas o de acceso restringido.
