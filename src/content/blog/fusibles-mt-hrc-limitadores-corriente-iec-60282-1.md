---
title: "Fusibles MT HRC: calibres, I²t y protección de transformadores IEC 60282-1"
description: "Guía técnica sobre fusibles de media tensión HRC: clasificación IEC 60282-1, calibres 6.3-200 A, criterios I²t e inrush para proteger transformadores MT/BT."
pubDate: 2026-10-24
keywords: ["fusibles MT HRC IEC 60282-1", "calibre fusible media tensión transformador", "curva tiempo corriente fusible MT", "coordinación fusible MCCB media tensión"]
author: "Editor"
---

## Por qué el fusible HRC sigue siendo la protección dominante en celdas MT/BT

En subestaciones de distribución industrial con transformadores entre 100 kVA y 2500 kVA, el conjunto interruptor-fusible es la solución más extendida para proteger el transformador en el lado de media tensión. La razón es práctica: el fusible limitador HRC (*High Rupturing Capacity*) combina en un único componente pasivo una capacidad de corte simétrico de hasta 63 kA, una energía de falta (*I²t*) limitada que protege al transformador, y un coste de ciclo de vida mucho menor que un relé de protección diferencial con interruptor automático MT.

La norma de referencia es **IEC 60282-1:2009** (*High-voltage fuses — Part 1: Current-limiting fuses*), adoptada en España como **UNE-EN 60282-1**. La guía de aplicación para transformadores fue **IEC 60787:1983**, anulada en 2007 sin sustituto directo; sus criterios de selección siguen siendo válidos y están integrados en los catálogos de fabricantes como ABB, Schneider Electric y Mersen.

---

## Clasificación IEC 60282-1: campo completo, reserva y percutor

IEC 60282-1 define tres tipos funcionales:

| Tipo | Designación | Capacidad de corte mínima | Aplicación típica |
|------|-------------|--------------------------|-------------------|
| Campo completo | *Full-range* | Desde corriente mínima de fusión hasta Isc nominal | Protección de transformadores MT/BT |
| Reserva | *Back-up* | Desde corriente mínima de corte (Imin) hasta Isc | Serie con contactor o interruptor |
| Percutor | *Striker* | — | Disparo mecánico del seccionador al fundir |

Los fusibles de **campo completo** son los que se instalan en celdas de corte con interruptor-fusible en configuración IM (interruptor con mando por percutor). Al fundir, el percutor activa mecánicamente el interruptor de la celda, abriendo los tres polos simultáneamente aunque sólo haya fundido un fusible de fase. Esto previene el servicio monofásico del transformador.

Los fusibles de **reserva** se usan en celdas con autoválvulas y en protección de motores MT (serie con contactor); no deben instalarse sin el dispositivo de corte en serie porque son incapaces de interrumpir corrientes de sobrecarga moderadas.

---

## Parámetros eléctricos clave según IEC 60282-1

**Tensión asignada (Ur)**: tensión entre fases para la que está diseñado el fusible. La serie ABB CEF está disponible en 12 kV, 24 kV y 36 kV (conforme a la red de 10 kV, 20 kV y 30 kV en España respectivamente). El fusible debe seleccionarse con Ur ≥ Un_red.

**Corriente nominal (In)**: corriente admisible en régimen permanente a 40 °C de temperatura ambiente (IEC 60282-1 §5.2). Por encima de 40 °C se aplica un factor de corrección. Para 50 °C el factor es ≈ 0,9.

**Corriente asignada de corte (Isc)**: valor eficaz de la corriente de cortocircuito simétrica máxima que puede interrumpir. Para la serie MV HRC (ABB CEF) recogida en la base de datos GElectrical: **Isc = 63 kA** para todos los calibres (6,3 A a 200 A). Esto cubre el nivel de cortocircuito en subestaciones urbanas de 20 kV con transformador de red de 25-63 MVA.

**Integral de Joule (I²t)**: mide la energía disipada durante la fusión. Se expresa en A²s y tiene dos componentes:

- *I²t de prefusión* (*prearcing*): desde el inicio de la sobrecorriente hasta que el elemento fusible se secciona. Este valor define si el fusible aguanta la corriente de irrupción del transformador.
- *I²t total*: incluye la energía del arco. Es el parámetro que se compara con el *I²t de daño* de cables y equipos a proteger.

**Tiempo virtual** (*virtual time*): cociente I²t / In², expresado en segundos. Normaliza el I²t respecto al calibre y permite comparar fusibles de distintos calibres en las curvas de selectividad.

---

## Calibres normalizados y poder de corte

Los calibres preferentes según IEC 60282-1 son: **6,3 — 10 — 16 — 20 — 25 — 31,5 — 40 — 50 — 63 — 80 — 100 — 125 — 160 — 200 A**.

Datos de la base GElectrical (ABB CEF, Ur = 24 kV, temperatura de referencia 40 °C):

| In (A) | Isc (kA sim.) | Aplicación típica 20 kV |
|--------|--------------|------------------------|
| 6,3 | 63 | Transformadores ≤ 100 kVA |
| 10 | 63 | Transformadores ≤ 160 kVA |
| 16 | 63 | Transformadores ≤ 250 kVA |
| 20 | 63 | Transformadores ≤ 400 kVA |
| 25 | 63 | Transformadores ≤ 500 kVA |
| 31,5 | 63 | Transformadores ≤ 630 kVA (Ucc 4 %) |
| 40 | 63 | Transformadores ≤ 630 kVA (Ucc 6 %) |
| 50 | 63 | Transformadores ≤ 1000 kVA |
| 63 | 63 | Transformadores ≤ 1250 kVA |
| 80 | 63 | Transformadores ≤ 1600 kVA |
| 100 | 63 | Transformadores ≤ 2000 kVA |
| 125 | 63 | Transformadores ≤ 2500 kVA |
| 160 | 63 | Transformadores ≤ 3150 kVA |
| 200 | 63 | Transformadores ≤ 4000 kVA |

Por encima de 2500-3150 kVA, la solución de fusible tiende a sustituirse por interruptor automático MT con relé de protección diferencial de transformador (IEC 60255-187-1), ya que los fusibles de calibre alto implican altos valores de I²t de prefusión que pueden dañar el propio transformador ante faltas internas graves.

---

## Criterios de selección para transformadores MT/BT

### Criterio 1 — Corriente nominal del transformador

La corriente nominal en el lado de alta tensión del transformador:

```
In_T = S / (√3 × Un)
```

Para transformadores de la base GElectrical (IEC 60076) a 20 kV, Ucc = 6 %:

| Potencia (kVA) | In_T a 20 kV (A) | Ucc (%) | Fusible recomendado (A) | Factor In_f / In_T |
|---------------|-----------------|---------|------------------------|-------------------|
| 250 | 7,22 | 6 | 16 | 2,2 |
| 400 | 11,55 | 6 | 20 | 1,7 |
| 630 | 18,19 | 6 | 40 | 2,2 |

Para transformadores a 10 kV, Ucc = 4 %:

| Potencia (kVA) | In_T a 10 kV (A) | Ucc (%) | Fusible recomendado (A) |
|---------------|-----------------|---------|------------------------|
| 250 | 14,43 | 4 | 25 |
| 400 | 23,09 | 4 | 40 |
| 630 | 36,37 | 4 | 63 |

El factor In_fusible / In_T suele estar entre **1,7 y 2,5** para fusibles de campo completo. Valores inferiores a 1,5 generan riesgo de fusión por irrupción; superiores a 3 reducen la protección contra faltas internas ligeras.

### Criterio 2 — Resistencia a la corriente de irrupción (IEC 60787)

Al energizar el transformador, la corriente de irrupción (*inrush*) puede alcanzar:
- **Pico**: 8 – 12 × In_T
- **Duración típica**: exponencial con constante τ ≈ 20–50 ms; a los 0,1 s ha decaído significativamente

El fusible debe sobrevivir sin fundir. El criterio práctico: el tiempo de prefusión del fusible a 10 × In_T debe ser ≥ 0,1 s.

Para el fusible de 40 A protegiendo un transformador de 630 kVA (In_T = 18,19 A):
- 10 × In_T = 182 A
- En la curva tiempo-corriente del fusible CEF de 40 A, el tiempo de prefusión a 182 A es típicamente > 1 s → holgura suficiente.

La corriente de irrupción pasa por el fusible pero **no lo daña** porque el I²t acumulado en 0,1 s es muy inferior al I²t de prefusión del fusible a esa corriente.

### Criterio 3 — Protección del secundario del transformador

Para faltas en el secundario BT, la corriente referida al primario MT es:

```
Icc_MT ≈ In_T / Ucc(%) × (ratio de transformación)
```

Para un transformador de 630 kVA, 20/0,4 kV, Ucc = 6 %:
- In_BT = 630.000 / (√3 × 400) = **909,3 A**
- Icc_BT_máx = In_BT / 0,06 = **15.155 A** (falta trifásica en bornes secundarios)
- Referida al primario: Icc_MT = 15.155 × (0,4 / 20) = **303 A**

A 303 A, el fusible de 40 A funde en tiempo ≈ 10 ms. El I²t total resultante es << I²t de daño del transformador (que fabricantes sitúan en el rango 10⁶–10⁷ A²s para este tamaño). La protección es eficaz.

Para faltas internas al propio transformador (entre espiras, a masa), la corriente MT puede ser menor que 303 A. En ese caso, el fusible de 40 A puede o no responder dependiendo de la gravedad de la falta; por ello en transformadores > 1000 kVA es preferible añadir la protección diferencial de transformador (Buchholz en aceite, relé diferencial de porcentaje).

---

## Principio físico: limitación de corriente y efecto de la arena de sílice

El elemento fusible es un hilo de plata (o cobre plateado) de sección calibrada embebido en arena de sílice de alta pureza. Cuando la corriente supera el umbral de fusión:

1. El hilo se funde en microsegundos, generando múltiples arcos en serie a lo largo del cartucho.
2. La arena de sílice actúa como medio de extinción: absorbe energía del arco por conducción y convección, y las partículas de sílice vitrificadas forman un camino de alta impedancia que extingue el arco antes del siguiente cruce por cero.
3. El proceso limita la corriente de cresta (*Ip_limitada*) a una fracción de la corriente de cresta prospectiva (*Ip_prospectiva*).

Para una red con Icc_sim = 63 kA (Ip_prospectiva ≈ 1,8 × √2 × 63.000 = 160 kA):
Un fusible de 40 A limita Ip a ≈ 5–8 kA, reduciendo la energía de falta en un factor > 400 respecto al cortocircuito sin limitación.

Este comportamiento se representa en las **curvas de limitación** (*cut-off current curves*) del fabricante, eje X = Icc prospectivo, eje Y = Ip limitada.

---

## Coordinación con protecciones del secundario BT

La selectividad entre el fusible MT y los MCCB del cuadro BT no es crítica en el sentido tradicional porque operan en circuitos de tensiones distintas. Lo que sí debe verificarse:

1. **El MCCB general de BT tiene mayor poder de corte que Icc_BT_máx** (15.155 A en el ejemplo). Si el MCCB sólo tiene Icu = 10 kA, la falta en bornes del transformador destruye el MCCB antes de que el fusible MT actúe.

2. **El I²t total del fusible MT referido al secundario** (× n²) debe ser ≥ I²t soportado por cables y barras BT para que el fusible MT actúe como back-up:
   - I²t_fusible_MT_referido = I²t_total_fusible × (Un_MT / Un_BT)² = I²t × (20/0,4)² = I²t × 2500
   - Este valor es generalmente mucho mayor que el I²t de daño de los cables BT, por lo que el fusible MT **no actúa** para faltas en la red BT aguas abajo del cuadro. Actúa exclusivamente para faltas entre bornes del transformador y la celda MT.

3. **Coordinación percutor–interruptor de celda**: cuando un fusible de fase funde por falta monofásica, el percutor dispara el interruptor de los tres polos en ≤ 60 ms (según hoja técnica celda RM6). Esto evita la alimentación desequilibrada del transformador.

---

## Criterios de decisión en obra: guía rápida

| Condición | Acción |
|-----------|--------|
| Un_red > Ur del fusible | Cambiar a fusible de mayor Ur |
| In_T calculado > In fusible × 0,7 | Subir un calibre (inrush) |
| Icc_red > Isc del fusible | Fusible no adecuado; usar interruptor automático |
| Potencia > 2000 kVA en 20 kV | Valorar relé diferencial + interruptor automático MT |
| Temperatura ambiente > 40 °C | Aplicar factor de corrección (×0,9 para 50 °C) |
| Falta monofásica frecuente | Verificar funcionamiento percutor + prueba mecánica |

---

## Conclusión

El fusible MT HRC según IEC 60282-1 es una protección robusta y económica para transformadores MT/BT hasta aproximadamente 2000–2500 kVA en redes de 20 kV. La selección correcta exige tres comprobaciones numéricas concretas: corriente nominal del transformador en el lado MT, resistencia a la corriente de irrupción (10 × In_T durante 0,1 s) y poder de corte frente a la Icc de red (≥ 63 kA en redes urbanas). Los calibres estandarizados IEC 60282-1 van de 6,3 A a 200 A con poderes de corte hasta 63 kA, cubriendo toda la gama de transformadores de distribución industrial. Por encima de 2500 kVA o en instalaciones con alta fiabilidad requerida, la transición a interruptor automático con relé diferencial de transformador ofrece selectividad completa y rearme sin intervención humana.
