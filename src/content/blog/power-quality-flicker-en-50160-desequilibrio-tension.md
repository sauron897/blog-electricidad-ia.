---
title: "Power Quality: Flicker y Desequilibrio de Tensión EN 50160"
description: "Análisis técnico del flicker (Pst, Plt) y desequilibrio de tensión según EN 50160 e IEC 61000-4-15: límites, medición y efectos en instalaciones industriales."
pubDate: 2026-10-04
keywords: ["power quality flicker EN 50160", "desequilibrio tension industrial", "Pst Plt flickermetro IEC 61000-4-15", "perturbaciones tension red electrica"]
author: "Editor"
---

La norma EN 50160 define las características de tensión en los puntos de suministro de redes de distribución pública en baja y media tensión. Para el técnico que trabaja en instalaciones industriales, dos de sus parámetros resultan frecuentemente subestimados: el **flicker** y el **desequilibrio de tensión**. Ambos pueden causar averías en equipos, pérdidas energéticas significativas y problemas de compatibilidad electromagnética que el IEC resuelve con criterios cuantificados y medibles.

Este artículo cubre los fundamentos de medición, los límites normativos y los criterios de intervención que el técnico puede aplicar directamente en campo con un analizador de red.

---

## Flicker: Modelo Perceptual y Parámetros Pst / Plt

El flicker es la variación rápida de la tensión de suministro que produce variaciones perceptibles de luminosidad en las lámparas. Aunque el término proviene del mundo de la iluminación, su impacto va más allá: afecta a la estabilidad de controles electrónicos, arrancadores y fuentes de alimentación.

La medición normalizada del flicker se realiza mediante el **flickermetro** definido en **IEC 61000-4-15**, que simula la cadena perceptual humana: variación de tensión → variación del flujo luminoso de una lámpara incandescente de 60 W → respuesta del ojo-cerebro. El instrumento produce tres valores:

- **Pinst**: Flicker instantáneo perceptible (adimensional). El umbral de perceptibilidad es Pinst = 1.
- **Pst**: Severidad de flicker a corto plazo. Se evalúa sobre una ventana de **10 minutos** mediante análisis estadístico de la distribución de Pinst. Pst = 1 equivale al umbral de irritación para el 50% de los observadores.
- **Plt**: Severidad de flicker a largo plazo. Se obtiene promediando 12 valores de Pst consecutivos (2 horas):

$$P_{lt} = \sqrt[3]{\frac{1}{12}\sum_{i=1}^{12} P_{st,i}^3}$$

### Límites EN 50160 para flicker

La norma EN 50160 establece, para redes BT y MT de distribución pública:

| Parámetro | Nivel de compatibilidad | Periodo de evaluación |
|-----------|------------------------|-----------------------|
| Pst       | ≤ 1,0                  | 10 minutos            |
| Plt       | ≤ 1,0                  | 2 horas               |
| Plt semanal | ≤ 1,0 durante el 95% del tiempo | 1 semana |

El 5% restante no tiene límite superior definido, pero la norma recomienda que no supere Plt = 1,5 de forma sostenida. En instalaciones industriales conectadas a red MT, el gestor de red puede exigir niveles de emisión de flicker (límites de perturbación hacia la red) definidos en **IEC 61000-3-7** y **IEC 61000-3-11**.

### Fuentes industriales de flicker

Los equipos industriales más frecuentes que generan flicker son:

- **Hornos de arco eléctrico (EAF)**: producen variaciones de corriente de 50–200 Hz con amplitudes de hasta el 5–10% de la tensión nominal. Son la fuente más severa de flicker en redes industriales.
- **Soldadoras de resistencia**: ciclos de disparo de 20–200 ms, variación de tensión de 2–8%.
- **Accionamientos con convertidores de tiristores** (variadores de CC, rectificadores de fase): si no están correctamente filtrados, generan fluctuaciones síncronas con la frecuencia de red.
- **Motores de gran potencia** arrancados directamente (DOL): la corriente de arranque puede ser 6–8 × In, provocando una caída de tensión transitoria que excede el 10% de Un en redes de baja impedancia.

---

## Desequilibrio de Tensión: Definición IEC y Efectos en Motores

El desequilibrio de tensión en sistemas trifásicos se cuantifica mediante el **Factor de Desequilibrio de Tensión** (VUF, *Voltage Unbalance Factor*), definido por IEC 61000-2-2 y recogido en EN 50160:

$$\text{VUF} (\%) = \frac{V_2}{V_1} \times 100$$

Donde V₂ es el módulo de la componente de secuencia negativa y V₁ es el módulo de la componente de secuencia positiva del sistema trifásico, obtenidas por transformación de componentes simétricas (Fortescue).

Existe también la definición simplificada NEMA (*Percent Voltage Unbalance*, PVU), de uso frecuente en campo:

$$\text{PVU} (\%) = \frac{\text{Desviación máx. respecto al promedio}}{V_{promedio}} \times 100$$

Ambas definiciones no son equivalentes numéricamente: el VUF (IEC) da valores sistemáticamente inferiores al PVU (NEMA) para los mismos valores de tensión. En la comparación con EN 50160, utilizar siempre VUF.

### Límites EN 50160 para desequilibrio

| Parámetro | Límite | Periodo | Observación |
|-----------|--------|---------|-------------|
| VUF       | ≤ 2%   | 95% de intervalos de 10 min en 1 semana | Redes con carga monofásica |
| VUF       | ≤ 3%   | En zonas con líneas bifásicas o monofásicas parciales | Excepcional |

La norma **IEC 60034-26** (máquinas eléctricas rotativas) también fija el límite de operación continua del motor a VUF ≤ 2%. Por encima de este valor, el fabricante puede exigir una reducción de la carga (derating).

### Efectos del desequilibrio en motores de inducción IE3/IE4

El desequilibrio de tensión genera en el motor una **componente de secuencia negativa** que produce un par frenante. Los efectos son no lineales:

| VUF (%) | Desequilibrio corriente estator (aprox.) | Incremento temperatura bobinado |
|---------|------------------------------------------|---------------------------------|
| 1%      | ~6–7%                                    | +15 °C                          |
| 2%      | ~14–17%                                  | +40–50 °C                       |
| 3%      | ~22–25%                                  | +70–80 °C                       |
| 5%      | ~35–40%                                  | >100 °C (fallo acelerado)       |

La regla empírica habitual es que **1% de VUF genera 6–7% de desequilibrio en las corrientes** y una elevación de temperatura que puede reducir la vida del bobinado a la mitad si es continua (Ley de Arrhenius aplicada al aislamiento clase F: cada 10 °C duplica la velocidad de degradación).

La norma **IEC 60034-26** establece que con VUF > 2% el motor debe operarse con un factor de servicio reducido. Los fabricantes de motores IE3 e IE4 suelen suministrar curvas de derating en función del VUF.

### Causas comunes de desequilibrio en instalaciones industriales

- Cargas monofásicas de gran potencia distribuidas asimétricamente entre fases (hornos, infrarrojos, SAIs monofásicos).
- Transformadores Scott o Le Blanc para suministro bifásico.
- Baterías de condensadores no equilibradas entre fases (condensadores averiados en una fase).
- Líneas de distribución en MT con secciones o longitudes distintas por fase.

---

## Medición: Instrumentos y Puntos de Medida

La medición conforme a EN 50160 requiere un **analizador de red clase A** según **IEC 61000-4-30**, que garantiza:

- Intervalo de agregación de 10 minutos para tensión RMS (Urms(10min)).
- Cálculo de Pst y Plt conforme a IEC 61000-4-15.
- Cálculo de VUF mediante componentes simétricas, no mediante la definición simplificada NEMA.
- Registro continuo durante al menos **1 semana** para evaluación estadística del 95%.

### Criterios de selección del punto de medida

| Objetivo | Punto de medida recomendado |
|----------|--------------------------|
| Verificar calidad de suministro (responsabilidad del DSO) | Punto de conexión a la red (PCdR), bornes del transformador de distribución |
| Identificar fuente interna de perturbación | Cuadro general BT, salidas de circuitos de carga perturbadora |
| Diagnóstico de motor con sobretemperatura | Bornes del motor (U1-V1-W1) |
| Auditoría Power Quality completa | PCdR + cuadros de planta + bornes de cargas críticas |

### Interpretación de resultados: criterio de responsabilidad

La EN 50160 distingue entre:
- **Nivel de planificación**: objetivo del gestor de red para no superar en el PDR (punto de entrega de red).
- **Nivel de compatibilidad**: límite de inmunidad que los equipos conectados deben tolerar según IEC 61000-2-4 (entornos industriales, clase 2 y 3).
- **Nivel de emisión**: límite que la instalación del cliente puede verter hacia la red, regulado por IEC 61000-3-X.

Si el Plt medido en el PCdR supera 1,0 y las fuentes internas están apagadas, la responsabilidad es del DSO. Si el Plt supera 1,0 sólo con las cargas del cliente activas, la instalación tiene un problema de emisión que puede acarrear penalizaciones contractuales.

---

## Criterios de Intervención y Soluciones Técnicas

**Para flicker elevado (Plt > 1,0):**

1. **Identificación de la carga perturbadora**: medir Pst con alta resolución temporal (1-min) para identificar el patrón temporal. Los hornos de arco producen picos periódicos; las soldadoras, picos correlacionados con los ciclos de producción.
2. **Reducción en la fuente**: aumentar la impedancia de cortocircuito en el punto de conexión de la carga (transformador dedicado con Ucc elevada) reduce la variación de tensión ΔU por la misma variación de corriente ΔI.
3. **Compensación dinámica**: SVC (*Static VAr Compensator*) o STATCOM inyectan reactiva en tiempo real para compensar las fluctuaciones de tensión. Respuesta típica: <5 ms para SVC con tiristores, <1 ms para STATCOM con IGBT.
4. **Filtros activos de armónicos** si el flicker está asociado a distorsión armónica (EAF, variadores).

**Para desequilibrio de tensión (VUF > 2%):**

1. **Redistribución de cargas monofásicas** entre fases: medida de coste cero, efectiva si el origen son cargas fijas monofásicas.
2. **Balanceadores de carga estáticos** (DSTATCOM trifásico desequilibrado): inyectan corriente de secuencia negativa para anular el desequilibrio.
3. **Transformador de Steinmetz**: convierte una carga monofásica en una carga trifásica equilibrada equivalente mediante un condensador y una inductancia en triángulo.
4. **Comprobación de condensadores en batería**: un condensador abierto o degradado en una fase genera desequilibrio de tensión en el punto de conexión de la batería.

---

## Conclusión

La EN 50160 proporciona el marco de referencia para evaluar la calidad de tensión en el punto de suministro. El flicker (Plt ≤ 1,0 en el 95% del tiempo) y el desequilibrio de tensión (VUF ≤ 2% en el 95% del tiempo en intervalos de 10 min) son los dos parámetros más frecuentemente incumplidos en entornos industriales con hornos de arco, soldadoras o cargas monofásicas de gran potencia.

El técnico puede actuar de forma inmediata con un analizador clase A IEC 61000-4-30: registrar durante una semana, calcular percentiles, identificar la fuente y cuantificar el impacto económico en los motores mediante las tablas de derating de IEC 60034-26. La solución técnica óptima depende de si el origen es interno o externo al punto de medida, y de la relación coste/beneficio entre compensación estática (redistribución de fases, reposición de condensadores) y compensación dinámica (SVC, STATCOM).
