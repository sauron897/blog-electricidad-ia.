---
title: "Armónicos en instalaciones industriales: THD y filtros según IEC 61000"
description: "Análisis técnico de armónicos en redes industriales BT: THD, límites IEC 61000-3-2/3-12, impacto en cables y transformadores, filtros activos y pasivos."
pubDate: 2026-09-18
keywords: ["armónicos instalaciones industriales", "THD filtros activos", "IEC 61000-3-2 armónicos", "distorsión armónica total", "filtro activo variador frecuencia"]
author: "Editor"
---

## Armónicos en redes industriales: origen físico y mecanismo de generación

Un armónico es una componente de frecuencia múltiplo entero de la frecuencia fundamental (50 Hz en Europa). La corriente que circula por cualquier carga no lineal —variador de frecuencia, fuente conmutada, rectificador de potencia, balasto electrónico— no es sinusoidal pura: su forma de onda puede descomponerse, mediante la serie de Fourier, en la fundamental más una suma de armónicos de orden h = 2, 3, 5, 7, 11, 13...

En sistemas trifásicos equilibrados los armónicos de orden par se cancelan. Los armónicos de secuencia negativa (h = 5, 11, 17...) generan campo giratorio inverso en máquinas eléctricas, produciendo par frenante y calentamiento adicional. Los armónicos de secuencia cero —triplen: h = 3, 9, 15...— se suman en el neutro en lugar de cancelarse, pudiendo duplicar o triplicar la corriente de neutro respecto a la de fase en instalaciones con gran cantidad de cargas monofásicas no lineales.

La magnitud del fenómeno se cuantifica con el **THDi** (Total Harmonic Distortion en corriente):

```
THDi = √(I₂² + I₃² + I₅² + ... + Iₙ²) / I₁ × 100 %
```

Un variador de frecuencia convencional con rectificador de 6 pulsos genera un THDi típico del 80-120 % referido a su corriente fundamental. Un rectificador de 12 pulsos lo reduce a 10-15 %. Un convertidor con filtro de línea LCL puede alcanzar THDi < 5 %.

---

## Normativa aplicable: IEC 61000-3-2, IEC 61000-3-12 y EN 50160

### IEC 61000-3-2: equipos ≤ 16 A

La norma IEC 61000-3-2 (transpuesta como UNE-EN 61000-3-2) establece límites de emisión de armónicos de corriente para equipos conectados a redes públicas de BT con corriente de entrada ≤ 16 A por fase. Define cuatro clases:

| Clase | Equipos típicos |
|-------|------------------|
| A | Trifásicos equilibrados, electrodomésticos no incluidos en otras clases |
| B | Herramientas eléctricas portátiles |
| C | Equipos de iluminación |
| D | PCs, monitores, televisores < 600 W |

Límites para **Clase A** (valores absolutos en amperios):

| Armónico h | Límite (A) |
|-----------|----------|
| 3 | 2,30 |
| 5 | 1,14 |
| 7 | 0,77 |
| 9 | 0,40 |
| 11 | 0,33 |
| 13 | 0,21 |
| 15 ≤ h ≤ 39 (impares) | 0,15 × 15/h |

### IEC 61000-3-12: equipos 16 A ≤ I ≤ 75 A

Para equipos de mayor potencia, IEC 61000-3-12 introduce el concepto de **Rsce** (relación de cortocircuito): cociente entre la potencia de cortocircuito de la red en el punto de conexión y la potencia nominal del equipo.

| Rsce mínimo exigible | THDi máximo permitido |
|---------------------|----------------------|
| 33 | 120 % |
| 66 | 80 % |
| 120 | 40 % |
| 250 | 20 % |
| 450 | 12 % |

La verificación de Rsce es responsabilidad del instalador: requiere conocer la impedancia de red en el PCC (*Point of Common Coupling*) y la potencia del equipo.

### EN 50160: calidad de tensión en BT

La norma EN 50160 fija los límites de **tensión armónica** en el PCC de redes de distribución pública BT:

| Armónico de tensión | Límite (% de U₁) |
|--------------------|------------------|
| h = 3 | 5 % |
| h = 5 | 6 % |
| h = 7 | 5 % |
| h = 11 | 3,5 % |
| h = 13 | 3 % |
| h = 17 | 2 % |
| h = 19 | 1,5 % |
| h = 23, 25 | 1,5 % |
| THD tensión total | 8 % |

El incumplimiento de EN 50160 por parte de la instalación industrial puede derivar en reclamaciones de la distribuidora y sanciones reglamentarias.

---

## Impacto técnico en la instalación: cables, transformadores y condensadores

### Sobredimensionado del neutro (ITC-BT-19 y IEC 60364-5-52)

El REBT en ITC-BT-19, artículo 3, remite a UNE-HD 60364-5-52 (equivalente IEC 60364-5-52) para el dimensionado de conductores. Cuando la proporción de armónicos de orden 3 y múltiplos es elevada, el neutro puede circular corrientes superiores a la de fase. El criterio es:

- Si THDi_3 (armónico de orden 3) es > 15 %: el neutro debe dimensionarse **igual** que las fases.
- Si THDi_3 > 33 %: se recomienda dimensionar el neutro **por encima** de las fases y reducir la capacidad de las fases (ya limitantes por el neutro).

La reactancia de los cables (dato verificado en GElectrical/IEC): X = **0,08 Ω/km** para cables XLPE de sección 4-300 mm², tanto Cu como Al. A frecuencia del 5.º armónico (250 Hz), la reactancia inductiva se multiplica por 5: X₅ = 0,40 Ω/km. Para el 7.º (350 Hz): X₇ = 0,56 Ω/km. Esto supone caídas de tensión armónica significativas en tramos largos de instalación, especialmente relevante en cálculos de calidad en plantas con variadores remotos.

### Pérdidas adicionales en transformadores

Las pérdidas en el hierro del transformador por corrientes de Foucault (*eddy currents*) crecen con el cuadrado del orden armónico: P_eddy(h) = P_eddy(1) × h². Un 5.º armónico genera 25 veces más pérdidas de Foucault que la fundamental de la misma amplitud.

Para cuantificar el impacto total se usa el **factor K** (UL 1561 / IEEE C57.110), o el concepto equivalente de **factor de armónicos** según IEC:

```
K = Σ(Ih/I₁)² × h^n
```

donde n ≈ 1,7 para transformadores de distribución tipo seco.

Un transformador de distribución de 400 kVA con carga predominantemente no lineal (THDi = 40 %) puede requerir reducción de carga del 15-20 % para no superar su temperatura nominal, o bien sustitución por un transformador **tipo K** diseñado según IEC 61378-1 para cargas no lineales.

### Resonancia con baterías de condensadores

La corrección de factor de potencia mediante condensadores es incompatible con cargas armónicas sin análisis previo. La frecuencia de resonancia paralela entre la inductancia de red (L_red) y los condensadores (C) es:

```
fr = (1/2π) × √(1/L_red × C) = f₁ × √(Rsce/Q_C)
```

Si fr coincide con un armónico presente en la red (típicamente el 5.º, 7.º o 11.º), se produce amplificación resonante que puede destruir los condensadores y las protecciones. La solución estándar es instalar **filtros pasivos sintonizados** o sustituir los condensadores por reactores desintonizadores que eleven la frecuencia de resonancia a 189 Hz (3,78 × 50 Hz), dejándola entre el 3.º y el 5.º armónico.

---

## Criterios de selección de estrategia de mitigación

La elección entre filtro pasivo, filtro activo, convertidor multifase o reactor de línea depende de la potencia, el espectro armónico y la dinámica de la carga.

| Solución | THDi resultante | Potencia adecuada | Respuesta dinámica | Coste relativo |
|----------|----------------|-------------------|--------------------|-----------------|
| Reactor de línea 3 % | 35-50 % | 5-250 kW | N/A (pasivo) | Bajo |
| Filtro LC pasivo sintonizado | 10-20 % (h específico) | > 50 kW | Lenta (ciclos) | Medio |
| Convertidor 12 pulsos | 10-15 % | > 100 kW | N/A (pasivo) | Medio-alto |
| Filtro activo paralelo | < 5 % | 10-600 kW | < 20 ms (< 1 ciclo) | Alto |
| Convertidor regenerativo AFE | < 5 % | 30 kW–varios MW | < 1 ms | Muy alto |

**Reactor de línea (inductancia de entrada):** solución económica para variadores de frecuencia convencionales. Una impedancia del 3 % (referida a la base del variador) reduce el THDi de ~120 % a ~40-50 %. No elimina ningún armónico específico, simplemente limita las corrientes de pico del rectificador.

**Filtro LC pasivo:** sintonizado a un armónico específico (h = 4,7 para mitigar el 5.º; h = 6,7 para el 7.º). Muy eficiente para cargas de perfil armónico estable. Requiere análisis de impedancia de red para evitar resonancia paralela con la fuente. Según IEC 61642 (Guía de mitigación de armónicos en instalaciones industriales), debe verificarse el comportamiento ante variaciones de ±10 % de la frecuencia de sintonía.

**Filtro activo paralelo (APF):** mide en tiempo real el contenido armónico de la corriente de carga e inyecta la corriente complementaria para cancelarlo. Tiempo de respuesta < 20 ms (< 1 ciclo a 50 Hz), válido para cargas con variación rápida del perfil armónico (hornos de arco, robots industriales, ascensores). La potencia del APF es típicamente 15-25 % de la potencia de la carga no lineal. Cumple IEC 62001-1.

**Convertidor AFE (*Active Front End*):** rectificador activo en IGBT con control de corriente sinusoidal. THDi < 5 % inherente al diseño. Permite recuperación de energía a la red en modos regenerativos. Estándar de diseño: IEC 61800-3 (variadores de velocidad ajustable).

### Procedimiento de selección en obra

1. **Medición previa**: analizar con medidor de calidad de red (clase A según IEC 61000-4-30) el espectro armónico en el PCC. Obtener THDi, THDu, factor de potencia real (no el de desplazamiento cosφ).
2. **Calcular Rsce** en el punto de conexión: Rsce = S_cc / S_equipo. Si Rsce < 33, los límites de IEC 61000-3-12 son de difícil cumplimiento sin mitigación.
3. **Verificar el neutro** si hay cargas monofásicas: medir I_neutro vs I_fase. Si I_N > 0,85 × I_fase, revisar sección según IEC 60364-5-52.
4. **Comprobar condensadores existentes**: si hay baterías de condensadores, calcular fr y verificar que no está en ningún armónico significativo del espectro medido (con margen ±10 %).
5. **Seleccionar solución** según tabla anterior y presupuesto disponible.
6. **Verificar tras instalación**: nueva medición según IEC 61000-4-30 para confirmar cumplimiento de EN 50160 (THD tensión ≤ 8 %) e IEC 61000-3-2/3-12.

---

## Conclusión

Los armónicos en instalaciones industriales no son un problema marginal: un parque de variadores de frecuencia convencionales sin mitigación puede llevar el THDi del cuadro a niveles del 80-120 %, con consecuencias directas sobre el calentamiento de cables (especialmente el neutro según IEC 60364-5-52), la vida útil del transformador de distribución y la integridad de las baterías de condensadores. La normativa IEC 61000-3-2 e IEC 61000-3-12 establece límites que el instalador debe verificar en el diseño, no tras la puesta en marcha. La medida básica —un reactor de línea del 3 %— es económica y reduce el THDi a la mitad; para instalaciones exigentes, el filtro activo paralelo garantiza THDi < 5 % con respuesta dinámica inferior a 20 ms. El primer paso siempre es medir: un analizador de red clase A según IEC 61000-4-30 da el espectro completo necesario para dimensionar correctamente la solución.
