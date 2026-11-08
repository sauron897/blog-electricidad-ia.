---
title: "Transformador seco encapsulado: clases térmicas e IEC 60076-11"
description: "Clases térmicas F y H, clasificación E/C/F y pérdidas en vacío y carga según IEC 60076-11. Criterios de selección para ingenieros y técnicos eléctricos."
pubDate: 2026-11-08
keywords: ["transformador seco encapsulado", "IEC 60076-11", "clases térmicas transformador", "pérdidas transformador seco", "resina epoxídica transformador"]
author: "Editor"
---

## Principio constructivo del transformador seco encapsulado

El transformador de tipo seco encapsulado en resina epoxídica sustituye el baño en aceite mineral por una impregnación al vacío de los bobinados con resina catalizada a alta temperatura. El resultado es un equipo con los bobinados completamente encapsulados —alta tensión y baja tensión— en un bloque de resina de clase F o H que actúa simultáneamente como aislamiento eléctrico, elemento dieléctrico y disipador térmico por conducción.

La norma de referencia es la **IEC 60076-11:2018** (adoptada en España como **UNE-EN IEC 60076-11:2021**), que cubre transformadores de potencia de tipo seco con tensión máxima de equipo hasta **72,5 kV** y al menos un devanado que opera por encima de 1,1 kV. Complementa a la serie IEC 60076-1 en lo relativo a ensayos dieléctricos, térmicos y de comportamiento frente a ciclos de temperatura.

La construcción epoxídica al vacío elimina la necesidad de cubeto de retención, sala de transformadores con ventilación específica contra vapores de aceite y los sistemas de extinción de incendios de tipo diluvio o CO₂ obligatorios para transformadores en aceite según REBT ITC-BT-13 y el RD 337/2014. Esto los hace idóneos para edificios, hospitales, centros de datos y subestaciones interiores.

---

## Clases térmicas de aislamiento según IEC 60076-11

La clase térmica del transformador seco está determinada por el sistema de aislamiento de los bobinados, clasificado según **IEC 60085** (materiales eléctricos de aislamiento) e integrado en la IEC 60076-11 para definir la temperatura máxima admisible y la sobreelevación garantizada en servicio nominal.

| Clase térmica | Temperatura máxima del sistema (°C) | Sobreelevación máxima sobre 20 °C (K) | Temperatura del punto caliente (°C) |
|---|---|---|---|
| B | 130 | 80 | 110 |
| F | 155 | 100 | 130 |
| H | 180 | 125 | 155 |
| C | 220 | 150 (limitada por diseño) | 180+ |

Los transformadores de distribución habituales en instalaciones industriales españolas emplean mayoritariamente la **clase F** (sobreelevación de 100 K a carga nominal con refrigeración natural AN), con la **clase H** reservada para equipos con restricciones severas de espacio donde se trabaja con carga alta y ventilación forzada AF.

La IEC 60076-11 distingue también el concepto de **temperatura del punto más caliente** (*hotspot temperature*), desarrollado en detalle en la **IEC 60076-12** para cálculo de vida útil acelerada. Para un transformador clase F en régimen de sobrecarga, la temperatura en el punto caliente del bobinado puede superar los 130 °C, activando el mecanismo de degradación exponencial de la resina epoxídica según la ecuación de Arrhenius.

**Regla de Montsinger**: la velocidad de envejecimiento del aislamiento se duplica por cada incremento de 6-10 K sobre la temperatura de referencia de la clase. Un transformador clase F operando continuamente a clase H consume su vida nominal en la mitad del tiempo previsto.

---

## Clasificación ambiental, climática y frente al fuego

La IEC 60076-11 introduce una triple clasificación independiente de la clase térmica:

### Clase ambiental (E)
Define la resistencia del encapsulado a humedad, condensación y contaminación. Es determinante en la especificación técnica de proyecto:

| Clase | Condición de instalación | Aplicación típica |
|---|---|---|
| **E0** | Interior seco y limpio, sin condensación | Edificios climatizados, CPDs |
| **E1** | Condensación ocasional, contaminación limitada | Industria ligera, naves sin climatización |
| **E2** | Condensación frecuente, alta contaminación | Industria química, exterior protegido, minería |

### Clase climática (C)
Define el rango de temperatura operativa mínima:

- **C1**: temperatura ambiente mínima de servicio **-5 °C**; temperatura mínima de transporte y almacenamiento -25 °C.
- **C2**: temperatura ambiente mínima de servicio **-25 °C**; válida también para transporte y almacenamiento a -50 °C.

La clase C2 es obligatoria para instalaciones en la cornisa cantábrica, Pirineos y zonas de montaña donde la temperatura interior de la sala eléctrica puede descender de -5 °C en paradas invernales prolongadas.

### Clase de comportamiento frente al fuego (F)
Independiente de la clase térmica de aislamiento:

- **F0**: sin requisito especial frente al fuego. La resina puede propagarlo.
- **F1**: material autoextinguible, llamas se apagan al retirar la fuente. Exigible en aplicaciones indoor donde no se puede garantizar la separación de la carga combustible según la directiva de equipos en BT.

La combinación habitual en instalaciones industriales con transformadores en sala interior es **E2-C1-F1**.

---

## Pérdidas en vacío y en carga: análisis y cálculo

Las pérdidas del transformador de distribución se dividen en dos componentes con comportamientos radicalmente distintos:

### Pérdidas en vacío (Pfe)
Son constantes e independientes de la carga. Originadas por las pérdidas en el núcleo magnético: histéresis y corrientes de Foucault. El transformador las consume las 8.760 horas del año mientras está energizado.

Fórmula de referencia:

```
Pfe = i₀% × Sn / 100   [kW aproximado; más exactamente: Pfe directo de ensayo]
```

Datos GElectrical (IEC 60076), transformadores de distribución MT/BT:

| Potencia | Tensión HV/LV | vk (%) | Pfe (kW) | i₀ (%) |
|---|---|---|---|---|
| 250 kVA | 20/0,4 kV | 6 | 0,80 | 0,32 |
| 400 kVA | 20/0,4 kV | 6 | 1,35 | 0,34 |
| 630 kVA | 20/0,4 kV | 6 | 1,65 | 0,26 |
| 250 kVA | 10/0,4 kV | 4 | 0,60 | 0,24 |
| 400 kVA | 10/0,4 kV | 4 | 0,95 | 0,24 |
| 630 kVA | 10/0,4 kV | 4 | 1,18 | 0,19 |

### Pérdidas en carga (Pcu o Pk)
Proporcionales al cuadrado de la corriente (ley de Joule), se obtienen del parámetro **vkr%** (componente resistiva de la tensión de cortocircuito):

```
Pk = vkr% × Sn / 100   [kW a temperatura de referencia]
```

| Potencia | Tensión HV/LV | vkr (%) | Pk calculado (kW) |
|---|---|---|---|
| 250 kVA | 20/0,4 kV | 1,44 | **3,60** |
| 400 kVA | 20/0,4 kV | 1,43 | **5,70** |
| 630 kVA | 20/0,4 kV | 1,21 | **7,60** |
| 250 kVA | 10/0,4 kV | 1,20 | **3,00** |
| 400 kVA | 10/0,4 kV | 1,33 | **5,30** |
| 630 kVA | 10/0,4 kV | 1,08 | **6,80** |

Las pérdidas en carga del transformador seco son entre un 15-25 % superiores a las del equivalente en aceite de igual potencia, debido a que la resina epoxídica conduce peor el calor que el aceite. Este dato es relevante en el estudio energético de la instalación cuando se evalúan las tarifas 6.x con periodos punta de alta actividad.

La pérdida total a un factor de carga **β** es:

```
Ptotal(β) = Pfe + β² × Pk
```

Para un transformador 400 kVA al 75% de carga: **Ptotal = 1,35 + 0,75² × 5,70 = 1,35 + 3,21 = 4,56 kW**

---

## Criterios de selección para instalaciones industriales

### Árbol de decisión para especificación técnica

**1. Tensión de cortocircuito (vk%)**
- Distribución ≤ 630 kVA en instalación industrial BT: **vk = 4-6 %**
- Potencias > 1 MVA o exigencia de limitación de Icc: **vk = 6 %**
- El vk define la impedancia de cortocircuito y limita la corriente de falta en el cuadro receptor; afecta directamente al poder de corte exigido a los MCCB aguas abajo.

**2. Clase térmica**
- Sala de transformadores climatizada, factor de carga medio < 80 %: **clase F**, sobreelevación 100 K.
- Sala sin climatización, factor de carga > 80 % o períodos de sobrecarga según IEC 60076-12: **clase H**, sobreelevación 125 K.
- El cálculo de vida útil acelerada en sobrecarga debe seguir el Anexo A de la **IEC 60076-11**.

**3. Clase ambiental**
- Sala eléctrica en edificio de oficinas o CPD: **E0**
- Nave industrial sin HVAC, posible condensación en arranque invernal: **E1**
- Industria química, agrícola, minería o exterior protegido: **E2** (con medida de resistencia de aislamiento periódica según REBT ITC-BT-05)

**4. Clase climática**
- Instalación en zona con inviernos rigurosos (zona climática E o D según CTE DB-HE): verificar que la temperatura mínima de sala en parada supera **-5 °C** (C1) o especificar **C2**.

**5. Refrigeración**
- Refrigeración natural por convección **AN**: estándar, sin equipos auxiliares ni mantenimiento.
- Refrigeración forzada **AF** (ventiladores): permite sobrecarga del 25-40 % sobre Sn nominal; exige monitorización de temperatura con sonda PT100 en el bobinado de AT.

**6. Protección y monitorización**
- Sonda de temperatura PT100 o PTC en bobinado AT: obligatoria para clase H y para sistemas con AF.
- Relé de temperatura con dos umbrales: alarma (típico 150 °C clase F) y disparo (175 °C clase F).
- Control de humedad en sala para clase E0/E1: diferencia higrotérmica < 10 % HR antes de la energización tras parada prolongada.

---

## Conclusión

La selección de un transformador seco encapsulado exige especificar cuatro clases independientes: **clase térmica** (F o H), **clase ambiental** (E0-E2), **clase climática** (C1 o C2) y **clase de fuego** (F0 o F1), además de la tensión de cortocircuito vk que condiciona la coordinación de protecciones aguas abajo. Las pérdidas en vacío (Pfe, constantes) y en carga (Pk, proporcionales a β²) deben cuantificarse en el estudio energético; para un 630 kVA al 75 % de carga las pérdidas totales rondan los 6-7 kW según los datos IEC de GElectrical. En instalaciones interiores con restricciones de incendio, la combinación **E2-C1-F1** con sondas PT100 y relé de temperatura es el estándar de facto exigible en el pliego técnico.
