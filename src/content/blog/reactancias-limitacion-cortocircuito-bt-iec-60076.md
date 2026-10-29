---
title: "Reactancias limitadoras de cortocircuito BT: selección IEC 60076-6"
description: "Cálculo, selección e integración de reactancias limitadoras de corriente de cortocircuito en instalaciones BT industriales según IEC 60076-6 e IEC 60909. Con valores numéricos y tabla comparativa."
pubDate: 2026-10-29
keywords: ["reactancia limitacion cortocircuito BT IEC 60076", "reactor limitador cortocircuito baja tension", "IEC 60289 reactor serie", "calculo Icc BT IEC 60909"]
author: "Editor"
---

## El problema: Icc supera la Icu disponible en BT

En instalaciones BT industriales con transformadores de gran potencia o transformadores en paralelo, la corriente de cortocircuito prospectiva en la cabecera del cuadro general de baja tensión (CGBT) puede alcanzar valores entre **40 kA y 80 kA** en redes de 400 V. El problema surge cuando ese valor supera la capacidad de ruptura última (Icu) de los interruptores automáticos de caja moldeada (MCCB) o bastidor abierto (ACB) disponibles en el mercado o ya instalados.

Según IEC 60947-2, la Icu de los MCCB industriales estándar llega típicamente hasta 50 kA (a 415 V), mientras que los ACB de alto rendimiento alcanzan 100 kA. Sin embargo, en subestaciones MT/BT con transformadores de 1600–2500 kVA conectados en paralelo o con transformadores de alta potencia y baja Ucc, la Icc calculada por el método de impedancias (IEC 60909-0:2016) puede exceder esos límites o acercarse peligrosamente a ellos, sin margen de seguridad suficiente.

La solución técnica es insertar una **reactancia limitadora de corriente en serie** en el circuito, aumentando la impedancia total de bucle y reduciendo así la Icc según la relación fundamental:

```
Icc = Un / (√3 × Zk_total)
```

donde `Zk_total = Ztrafo + Zreactor + Zcables + Zbarra`.

---

## Fundamento normativo: IEC 60076-6 e IEC 60289

Los reactores de limitación de corriente están normalizados en **IEC 60076-6:2010** — "Power transformers — Part 6: Reactors". Esta parte de la familia IEC 60076 absorbió el contenido de la anterior IEC 60289:1988 y establece los requisitos de diseño, ensayo y marcado de todos los tipos de reactores de potencia, incluyendo los de limitación de corriente de cortocircuito.

Los parámetros normalizados definidos en IEC 60076-6 que debe especificar el proyectista son:

- **Corriente nominal (In)**: corriente de servicio permanente en A
- **Reactancia nominal (ur%)**: tensión de cortocircuito referida a la tensión nominal, en %. Valores típicos: 2%, 4%, 6%, 8%
- **Pérdidas en el cobre (Pk)**: en W, a corriente nominal
- **Tensión de servicio (Un)**: tensión de la red donde se inserta, en kV
- **Clase de temperatura del aislamiento**: según IEC 60085 (clase F o H en reactores de núcleo de aire)
- **Corriente de cortocircuito admisible (Icc-th)**: kA, durante 1 s o 3 s

El modelo constructivo dominante en BT es el **reactor de núcleo de aire con bobina seca encapsulada en resina** (tipo similar a transformadores dry-type clase F/H), que no requiere aceite y puede montarse dentro del cuadro eléctrico o en sala adyacente. Para BT, la inductancia típica oscila entre 0,1 mH y 2 mH por fase.

---

## Cálculo de la Icc antes y después del reactor

### Sin reactor — Ejemplo de referencia

Transformador de distribución MT/BT:
- Potencia: **1600 kVA**
- Tensión nominal secundaria: **400 V**
- Tensión de cortocircuito: **Ucc = 6%** (IEC 60076-1 para trafo estándar de distribución)

La impedancia de cortocircuito del transformador referida a BT:

```
Ztrafo = (Ucc% / 100) × (Un² / Sn)
Ztrafo = 0,06 × (400² / 1 600 000)
Ztrafo = 0,06 × 0,1 = 6 mΩ
```

La Icc trifásica máxima en barras del CGBT (despreciando impedancias de red MT y cables cortos):

```
Icc = Un / (√3 × Ztrafo)
Icc = 400 / (1,732 × 0,006) = 38,5 kA
```

Este valor puede llegar hasta **40–42 kA** considerando la impedancia de la red MT (típicamente muy pequeña frente a Ztrafo en distribución industrial convencional) y sin incluir las resistencias de cableado.

### Con reactor al 4%

Se inserta un reactor con `ur = 4%` referido a la potencia del transformador (1600 kVA):

```
Zreactor = (ur% / 100) × (Un² / Sn)
Zreactor = 0,04 × (400² / 1 600 000)
Zreactor = 0,04 × 0,1 = 4 mΩ
```

La nueva Icc:

```
Zk_total = Ztrafo + Zreactor = 6 + 4 = 10 mΩ
Icc_nueva = 400 / (1,732 × 0,010) = 23,1 kA
```

Reducción del 40%. Los MCCB con Icu ≥ 25 kA a 400 V (categoría B según IEC 60947-2) son ahora compatibles.

---

## Tabla comparativa: ur% del reactor vs. Icc resultante y caída de tensión

| Reactancia ur% | Zreactor (mΩ) | Icc resultante (kA) | Δu a plena carga (%) |
|:--------------:|:-------------:|:-------------------:|:--------------------:|
| 0% (sin reactor) | 0 | 38,5 | 0 |
| 2% | 2 | 28,9 | 2,0 |
| 4% | 4 | 23,1 | 4,0 |
| 6% | 6 | 19,2 | 6,0 |
| 8% | 8 | 16,5 | 8,0 |

*Trafo base: 1600 kVA, Ucc=6%, Un=400 V. Δu calculada a factor de potencia 0,9 lagging.*

La caída de tensión bajo carga nominal es proporcional a `ur%`, lo que constituye el principal compromiso de diseño: reducir Icc exige aceptar una caída de tensión permanente en la cabecera de la instalación. En la práctica, **valores superiores al 6% rara vez se justifican en BT**, salvo en sistemas muy específicos (buses de enlace en anillo o interconexiones de barras en subestaciones con alta densidad de potencia).

---

## Criterios de selección aplicables en obra

La selección del reactor de limitación sigue esta lógica de decisión:

**1. Calcular Icc prospectiva** mediante el método de impedancias según IEC 60909-0, sin el reactor, en el punto de conexión previsto.

**2. Determinar la Icu del interruptor disponible** aguas abajo. La diferencia entre Icc prospectiva e Icu define el margen de reducción necesario.

**3. Calcular el ur% mínimo** necesario para que la Icc caiga por debajo del 80–85% de la Icu del interruptor (margen de seguridad IEC 60947-2):

```
ur%_min = (1 - Icc_objetivo / Icc_sin_reactor) × Ucc%_trafo
```

**4. Verificar la caída de tensión** introducida. ITC-BT-19 limita la caída de tensión total desde el origen hasta el punto de utilización al 3% en alumbrado y 5% en fuerza motriz. El reactor consume parte de ese presupuesto de caída de tensión.

**5. Dimensionar la corriente nominal del reactor**: In ≥ 1,25 × I_carga_máxima_prevista.

**6. Verificar la corriente de cortocircuito admisible (Icc-th)**: el reactor debe soportar la Icc prospectiva *antes* de limitarla (la corriente inicial de cortocircuito —componente AC más componente DC— circula por el reactor durante el tiempo de apertura del interruptor aguas abajo, típicamente 20–100 ms).

**7. Localización física**: en cuadros compactos, el reactor se monta en armario adyacente o en cofret separado. Los reactores de núcleo de aire generan campo magnético que puede interferir con relés de medida próximos; respetar distancias mínimas según especificación del fabricante (tipicamente > 300 mm de equipos sensibles).

**8. Coordinación con protecciones selectivas**: al aumentar Zk, se modifica la corriente de cortocircuito para *todos* los interruptores aguas abajo. Recalcular los ajustes de disparo magnético y las curvas de fusibles después de insertar el reactor. El tiempo de actuación mínimo de los magnetotérmicos puede verse afectado si Icc baja de su umbral de disparo magnético.

---

## Integración en subestaciones con transformadores en paralelo

En configuraciones con dos o más transformadores MT/BT en paralelo sobre barras comunes (configuración habitual en subestaciones industriales de 2×1600 kVA o 2×2500 kVA), la Icc en las barras se aproxima a la suma de las Icc de cada transformador. Por ejemplo:

- 2 transformadores de 1600 kVA con Ucc=6% en paralelo: Icc ≈ 2 × 38,5 = **77 kA**

Aquí ningún MCCB estándar (Icu_max ≈ 100 kA según IEC 60947-2, clase C) da margen suficiente. La solución es insertar un reactor por cada transformador o un reactor de enlace entre las barras de los dos secundarios, conforme a la arquitectura de la subestación.

IEC 60076-6 contempla expresamente los **reactores de enlace de barras** (bus-tie reactors), cuya función es limitar la corriente de circulación entre secciones de barra cuando están acopladas. Su selección sigue los mismos parámetros (ur%, In, Icc-th), pero la corriente de diseño es la corriente de intercambio entre secciones en caso de falta.

---

## Conclusión

Las reactancias limitadoras de corriente en BT son la solución cuando la Icc prospectiva supera la Icu de los interruptores disponibles y no es viable sustituir el transformador ni replantear la topología de red. El parámetro de diseño clave es **ur% = 4–6%**, que equilibra reducción de Icc y caída de tensión asumible. La normativa aplicable es IEC 60076-6:2010 para el reactor y IEC 60909-0:2016 para el cálculo de cortocircuito; la verificación de caída de tensión debe contrastar con los límites de ITC-BT-19. Cualquier cambio de Zk obliga a recalcular los ajustes de disparo de todas las protecciones aguas abajo.
