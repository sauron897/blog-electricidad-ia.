---
title: "Coordinación de magnetotérmicos MCB/MCCB: selectividad amperimétrica IEC 60947"
description: "Cómo lograr selectividad amperimétrica entre MCB y MCCB en cuadros BT industriales. Criterios técnicos, tablas de coordinación y límite Is según IEC 60947-2."
pubDate: 2026-09-19
keywords: ["coordinacion magnetotermicos selectividad", "selectividad amperimetrica MCB MCCB", "IEC 60947-2 coordinacion protecciones", "poder corte magnetotermico cascada", "limite selectividad Is BT"]
author: "Editor"
---

Cuando una sobreintensidad en un ramal secundario dispara el interruptor general del cuadro en vez del magnetotérmico de ese ramal, hay un fallo de coordinación. En instalaciones industriales con varios niveles de cuadros —cuadro general de baja tensión (CGBT), subcuadros de zona, cuadros de máquina— ese disparo incorrecto implica paro total de producción. La selectividad entre magnetotérmicos no es un refinamiento opcional: es un requisito funcional que la norma **IEC 60947-2** obliga a verificar mediante tablas de coordinación o cálculo.

Este artículo desarrolla los tres tipos de selectividad definidos en IEC 60947-2, con énfasis en la **selectividad amperimétrica**, los umbrales de disparo magnético y el criterio cuantitativo que permite decidir si la selectividad entre dos interruptores en serie es total o parcial.

---

## Tipos de selectividad entre interruptores automáticos según IEC 60947-2

La **IEC 60947-2** (*Low-voltage switchgear and controlgear — Part 2: Circuit-breakers*) define selectividad como la coordinación entre dispositivos de protección colocados en serie, de manera que ante un defecto aguas abajo solo actúe el dispositivo más próximo a él. La norma distingue tres mecanismos:

### Selectividad amperimétrica

Se basa en la diferencia de umbrales de disparo instantáneo (protección magnética) entre el dispositivo aguas arriba y el aguas abajo. La condición de selectividad total es:

> **Icc_punto ≤ Im_upstream**

donde:
- **Icc_punto**: corriente de cortocircuito trifásica en el nodo donde se instala el dispositivo aguas abajo, calculada según IEC 60909.
- **Im_upstream**: umbral de disparo instantáneo del dispositivo aguas arriba.

Si **Icc_punto > Im_upstream**, la selectividad es **parcial**: existe un límite de selectividad **Is < Icc_punto** por encima del cual ambos dispositivos disparan simultáneamente.

### Selectividad cronométrica

Se introduce un retardo de tiempo intencional en el dispositivo aguas arriba. En magnetotérmicos moldeados (MCCB) con unidades de disparo electrónicas, el retardo ajustable en la zona de corta temporización (STD) oscila típicamente entre 50 ms y 400 ms. Durante ese retardo, el dispositivo aguas abajo tiene tiempo de despejar la falta. Exige verificar que el interruptor aguas arriba soporte la energía pasante durante el tiempo de retardo: **I²t ≤ I²t_admisible** del bastidor.

### Selectividad energética (filiación o back-up)

El dispositivo aguas abajo, al ser un limitador de corriente (curva de limitación de energía), limita el pico de corriente y la energía pasante (I²t) que llega al dispositivo aguas arriba por debajo de su umbral de disparo magnético, aunque la corriente de cortocircuito prospectiva supere **Im_upstream**. Requiere que el par de dispositivos esté validado en tablas de filiación publicadas por el fabricante.

---

## Umbrales de disparo magnético MCB e implementación en GElectrical/IEC 60898-1

Los MCB industriales (IEC 60898-1 / UNE-EN 60898-1) tienen el umbral de disparo instantáneo fijo por curva:

| Curva | Im mínimo | Im máximo | Aplicación típica |
|-------|-----------|-----------|-------------------|
| **B** | 3 × In | 5 × In | Circuitos resistivos, largas líneas |
| **C** | 5 × In | 10 × In | Uso general, cargas con pico de arranque moderado |
| **D** | 10 × In | 20 × In | Motores, transformadores, cargas de alta corriente transitoria |

Para MCB curva C de 63 A (datos GElectrical / IEC): Im entre **315 A y 630 A**, poder de corte **10 kA** según categoría A de IEC 60898-1.

Los MCCB (IEC 60947-2) amplían el rango de forma significativa:

| Calibre In | Isc máx (GElectrical) | Umbral Im ajustable | Bastidor |
|------------|----------------------|---------------------|----------|
| 20 – 250 A | 25 kA | Fijo (TM) o 1,5 – 10 × In (electrónico) | DN0/DN1 |
| 63 – 250 A | 36 kA | 1,5 – 10 × In (TM ajustable) | DN2 |
| 320 – 630 A | 36 kA | 1,5 – 10 × In | DN3 |
| 40 – 630 A | 36 – 50 kA | 1,5 – 12 × In (electronico MTX) | DN2/DN3 |

Un MCCB 250 A con Im ajustado a 10 × In tiene umbral de disparo instantáneo en **2500 A**, suficiente para garantizar selectividad amperimétrica total sobre cualquier MCB aguas abajo cuya Icc_punto sea inferior a 2,5 kA.

---

## Cálculo de Icc en los nodos: condición necesaria para el análisis de selectividad

El análisis de selectividad requiere conocer la corriente de cortocircuito trifásica en cada nodo donde se instala la protección aguas abajo. El método de impedancias de **IEC 60909** calcula:

$$I_{cc} = \frac{c \cdot U_n}{\sqrt{3} \cdot Z_{total}}$$

donde:
- **c** = 1,05 (factor de tensión para Icc máxima en BT, tabla 1 de IEC 60909)
- **Un** = 400 V (tensión nominal de red trifásica BT)
- **Z_total** = impedancia resultante desde la fuente hasta el nodo

La impedancia total acumula: impedancia del transformador (Z_tr), de las barras del CGBT (despreciable habitualmente), y la impedancia de los cables de alimentación al subcuadro:

$$Z_{cable} = \sqrt{(R_{cable})^2 + (X_{cable})^2}$$

Para un cable Cu 3×95 mm² XLPE de 50 m (datos GElectrical / UNE-HD 60364-5-52):
- R_cable = ρ × L / S = 0,0183 × 50 / 95 = **0,0096 Ω**
- X_cable ≈ 0,08 × 10⁻³ × 50 = **0,004 Ω**
- Z_cable = **0,0104 Ω**

Con un transformador 630 kVA, Un=20/0,4 kV, Ucc=4% (IEC 60076):
- Z_tr = (Ucc/100) × (Un²/Sn) = 0,04 × (0,4²/0,63) = **0,0102 Ω**

$$I_{cc,subcuadro} = \frac{1,05 \times 400}{\sqrt{3} \times (0,0102 + 0,0104)} = \frac{420}{0,0357} \approx \mathbf{11,8 \text{ kA}}$$

Frente a un MCCB 160 A con Im = 10 × 160 = 1600 A: **Icc_punto (11,8 kA) >> Im (1,6 kA)** → selectividad amperimétrica NO garantizada en ese nodo. Se necesitaría selectividad cronométrica o energética (filiación).

---

## Criterios de selección de la estrategia de coordinación en obra

El procedimiento de diseño se aplica nodo a nodo, de la fuente hacia las cargas:

**1. Calcular Icc en cada nodo** (IEC 60909, método de impedancias). La impedancia acumula transformador + cables sucesivos. A mayor distancia del transformador, menor Icc.

**2. Verificar la condición de selectividad amperimétrica en cada par de dispositivos en serie:**

| Condición | Diagnóstico | Acción |
|-----------|-------------|--------|
| Icc_nodo ≤ Im_aguas_arriba | Selectividad **total** | No requiere acción adicional |
| Icc_nodo > Im_aguas_arriba | Selectividad **parcial** hasta Is = Im_aguas_arriba | Evaluar selectividad cronométrica o energética |
| Im_aguas_arriba no verificable | Recurrir a tablas de coordinación del fabricante | Consultar tablas de selectividad (IEC 60947-2 Anexo B) |

**3. Si se requiere selectividad cronométrica**: comprobar que el MCCB aguas arriba tiene unidad de disparo electrónica con zona de corta temporización (STD) y que su I²t admisible durante el retardo no se supera. Ejemplo: MCCB 630 A con STD de 200 ms y Isc de 50 kA necesita bastidor validado para I²t = (50000)² × 0,2 = 500 MJ/Ω.

**4. Si se aplica filiación (back-up)**: comprobar que el par exacto de dispositivos figura en las tablas de filiación del fabricante. La filiación no es deducible analíticamente; requiere ensayo conjunto conforme al Anexo B de IEC 60947-2. Un par de dispositivos no validado en tablas no puede declararse como solución de filiación, independientemente de sus curvas individuales.

**5. Requisito del REBT ITC-BT-22**: para instalaciones BT en España, cualquier dispositivo de protección contra sobreintensidades instalado en el punto de entronque de una derivación debe tener un poder de corte ≥ Icc en ese punto, o estar respaldado por un dispositivo aguas arriba de poder de corte suficiente con coordinación verificada (régimen de back-up explicitado en el proyecto).

---

## Conclusión

La selectividad amperimétrica entre MCB y MCCB exige calcular la corriente de cortocircuito en cada nodo (IEC 60909) y compararla con el umbral de disparo instantáneo del dispositivo aguas arriba. En instalaciones industriales próximas al transformador, la Icc puede superar 10–15 kA, lo que hace inviable la selectividad amperimétrica pura entre un MCB aguas abajo y cualquier dispositivo de cabecera. En esos nodos, la alternativa es la selectividad cronométrica —si el MCCB dispone de unidad electrónica con STD— o la filiación con par de dispositivos validado según tablas del fabricante bajo IEC 60947-2 Anexo B.

La herramienta operativa en proyecto es el cálculo de Icc nodo a nodo, la verificación del umbral Im de cada dispositivo y la consulta de tablas de selectividad y filiación del fabricante. Ninguna de esas tres verificaciones puede omitirse en una instalación industrial donde la continuidad de servicio sea un requisito.
