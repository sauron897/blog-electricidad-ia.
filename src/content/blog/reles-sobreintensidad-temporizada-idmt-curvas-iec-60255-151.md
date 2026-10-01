---
title: "Relés IDMT: curvas y ajuste según IEC 60255-151"
description: "Guía técnica para ajuste de relés de sobreintensidad temporizada IDMT según IEC 60255-151: ecuaciones, constantes de curva, PSM, TMS y coordinación en redes MT."
pubDate: 2026-10-01
keywords: ["relé sobreintensidad temporizado IDMT", "IEC 60255-151", "curvas IDMT ajuste", "protección sobreintensidad líneas MT", "TMS PSM relé protección"]
author: "Editor"
---

Los relés de sobreintensidad de tiempo inverso (IDMT, *Inverse Definite Minimum Time*) constituyen la piedra angular de la protección de sobrecorriente en redes de distribución de media tensión. La norma IEC 60255-151:2009 (*Measuring relays and protection equipment — Part 151: Functional requirements for over/under-current protection*) estandariza las ecuaciones y constantes de cada característica, eliminando la ambigüedad que existía entre fabricantes antes de su publicación. Este artículo expone las bases matemáticas, los criterios de selección de curva y un ejemplo de ajuste para un alimentador de 20 kV.

## Ecuación característica IDMT según IEC 60255-151

La ecuación general de tiempo de actuación definida en el Anexo A de IEC 60255-151 es:

```
t(I) = TMS × [ k / ((I/Is)^α − 1) ] + c
```

Donde:
- **t(I)** — tiempo de disparo en segundos
- **TMS** — *Time Multiplier Setting*, multiplicador de tiempo (0,05 a 1,0 típico)
- **I** — corriente de falta vista por el relé (A secundario de TI)
- **Is** — corriente de arranque del relé (*pickup*, A secundario)
- **k, α, c** — constantes propias de cada tipo de curva

Para valores `I/Is < 1,05` el relé no arranca. El valor `c = 0` en la mayoría de implementaciones IEC salvo en la curva *Long Time Inverse*, donde algunos fabricantes lo aplican para representar el componente de tiempo definido mínimo.

## Las cuatro curvas normalizadas IEC 60255-151

| Curva | Designación IEC | k | α | Aplicación típica |
|---|---|---|---|---|
| Standard Inverse (SI) | Inversa estándar | 0,14 | 0,02 | Alimentadores de distribución MT, generadores |
| Very Inverse (VI) | Muy inversa | 13,5 | 1,0 | Líneas largas con Icc decreciente con la distancia |
| Extremely Inverse (EI) | Extremadamente inversa | 80 | 2,0 | Coordinación con fusibles, protección de motores |
| Long Time Inverse (LTI) | Inversa de tiempo largo | 120 | 1,0 | Faltas a tierra de alta resistencia, sobrecarga |

La curva **SI** es la más plana: a 10×Is actúa en torno a 3 s con TMS=1. La **EI**, mucho más inclinada, actúa en ~0,4 s a 10×Is con TMS=1 — la diferencia es radical a corrientes elevadas, lo que define cuándo se puede conseguir selectividad con el elemento de aguas abajo.

### Ejemplo numérico comparativo (TMS=0,3, Is=1 A)

| I/Is | t\_SI (s) | t\_VI (s) | t\_EI (s) |
|---|---|---|---|
| 2 | 10,03 | 4,05 | 3,12 |
| 5 | 2,97 | 1,13 | 0,64 |
| 10 | 1,54 | 0,43 | 0,26 |
| 20 | 1,07 | 0,21 | 0,12 |

La EI reduce el tiempo de actuación con la cuadrada de la corriente, por eso coordina mejor con fusibles tipo gG cuya energía de fusión sigue una ley I²t.

## Ajuste del relé: PSM y TMS

### PSM — *Plug Setting Multiplier*

El PSM (o *Pick-Up Setting*) determina la corriente mínima de arranque vista en el primario del transformador de intensidad (TI):

```
I_arranque_primario = PSM × I_nominal_TI_primario
```

**Criterio de arranque**: el PSM se elige para que el relé sea ciego frente a la corriente nominal del circuito (incluyendo corriente de magnetización del transformador en el transitorio de conexión), y sensible frente a la corriente mínima de falta:

```
I_carga_máxima × 1,3 < I_arranque < I_cc_min_escena × 0,8
```

Para la corriente de conexión de un transformador de distribución la ráfaga puede alcanzar 8–12×IN durante 50–100 ms. Un TMS suficientemente bajo y la característica de reset diferenciado en relés digitales (IEC 60255-151, Cláusula 8) evitan disparos intempestivos.

### TMS — *Time Multiplier Setting*

El TMS escala verticalmente la curva. Se determina a partir del CTI (*Coordination Time Interval*) respecto al relé de aguas abajo:

```
TMS_upstream = TMS_downstream + (CTI / [k / ((I/Is)^α − 1)])
```

IEC 60255-151 no fija el CTI, pero la práctica de ingeniería en España establece:
- Relés digitales modernos: **CTI = 200–250 ms** (incluye tiempo de apertura del interruptor ≈80 ms + tolerancias del relé ≈30 ms + margen ≈90 ms)
- Relés electromecánicos: **CTI = 300–400 ms** (mayor inercia de disco e histéresis)

## Criterios de selección de curva

La elección entre SI, VI y EI no es arbitraria; depende de la topología de red y el elemento de aguas abajo:

| Condición de red | Curva recomendada | Razonamiento |
|---|---|---|
| Icc cae poco con la distancia (red mallada) | SI | La diferencia de corriente entre posiciones es pequeña; curva plana maximiza diferencia de tiempos |
| Icc cae fuertemente con la distancia (línea radial larga) | VI | A corrientes bajas (falta al final de línea) da más tiempo; a corrientes altas actúa rápido |
| Coordinación aguas abajo con fusibles gG/aM | EI | Sigue ley I²t similar al fusible; permite ajuste con margen de coordinación en todo el rango |
| Protección de generador contra sobrecargas prolongadas | SI/LTI | Curva plana evita actuación intempestiva por sobrecargas temporales |
| Falta tierra en red MT con neutro impedante | LTI | Corrientes de falta pequeñas, requiere tiempo largo para evitar perturbaciones de servicio |

## Ejemplo de ajuste: alimentador 20 kV con transformador 630 kVA

**Datos de red:**
- Tensión nominal: 20 kV
- Icc máxima en embarrado AT: 5 000 A
- Icc mínima en falta bifásica al final del alimentador: 800 A
- Carga nominal del alimentador: 150 A (primario del TI)
- TI instalado: 200/1 A
- Relé de aguas abajo (BT del transformador 630 kVA): ajustado a TMS=0,10 con curva EI, Is=0,8 A (secundario), coordinado a 800 A primario

**Paso 1 — PSM del relé MT:**

```
I_arranque_min = 1,3 × 150 A = 195 A  →  PSM = 195/200 ≈ 1,0  →  Is = 1,0 A secundario
I_arranque_efectivo = 1,0 A × 200 = 200 A
```

**Paso 2 — Verificar sensibilidad:**
```
I_cc_min / I_arranque = 800 / 200 = 4,0  →  PSM efectivo en condición mínima = 4
```
Con PSM=4 el relé sí arranca en falta mínima. Para curva EI: t(4) con TMS=1 → k/((4)²−1)×1 = 80/15 = 5,33 s. Sensibilidad aceptable.

**Paso 3 — Tiempo del relé de aguas abajo a 800 A:**

El relé BT ve 800 A / (ratio TI BT: 1000/5 = 200/1) → I/Is = (800/200)/0,8 = 5. Con TMS=0,10 y curva EI:

```
t_BT = 0,10 × [80 / (5² − 1)] = 0,10 × [80/24] = 0,333 s
```

**Paso 4 — TMS del relé MT (curva EI, CTI = 250 ms):**

```
t_MT_requerido = t_BT + CTI = 0,333 + 0,250 = 0,583 s
t_MT = TMS × [80 / (5² − 1)] = TMS × 3,333 s (con I/Is_MT = 800/200 = 4 → PSM efectivo = 4/1 = 4)
```

Corrigiendo: I/Is\_MT = (800 A primario) / (200 A arranque) = 4,0:
```
t_MT = TMS × [80 / (4² − 1)] = TMS × [80/15] = TMS × 5,333
TMS = 0,583 / 5,333 = 0,109  →  Ajustar a TMS = 0,12 (margen)
```

**Paso 5 — Verificar a Icc máxima (5 000 A):**

```
I/Is_MT = 5000/200 = 25
t_MT = 0,12 × [80 / (25² − 1)] = 0,12 × [80/624] = 0,12 × 0,128 = 0,0154 s ≈ 15 ms
```

A corriente máxima el relé actúa en ~15 ms, prácticamente en zona de disparo instantáneo. Conviene añadir un elemento de disparo instantáneo (50/ANSI) ajustado por encima de la corriente de conexión del transformador (típicamente 12×IN = 12×18,2 A = 218 A en primario MT del transformador; en alimentador puede haber varios → ajustar a 70–80% de Icc mínima del nodo). IEC 60255-151 Cláusula 7 describe el elemento de sobreintensidad instantánea complementario al IDMT.

## Conclusión

El ajuste de relés IDMT según IEC 60255-151 implica tres decisiones secuenciales: selección de curva (SI, VI, EI o LTI según topología y elemento de aguas abajo), ajuste de PSM (con margen sobre corriente de carga y sensibilidad mínima sobre Icc mínima), y cálculo de TMS a partir del CTI requerido. La norma provee las constantes exactas — no usar valores aproximados de tablas antiguas. En protección de alimentadores MT con transformadores de distribución, la curva EI facilita la coordinación con fusibles BT y con relés de baja tensión ajustados a la misma familia de curvas, reduciendo el TMS del relé MT y mejorando la velocidad de actuación en faltas cercanas. El elemento instantáneo (50/ANSI) complementario es imprescindible para faltas de alta corriente junto al relé principal.
