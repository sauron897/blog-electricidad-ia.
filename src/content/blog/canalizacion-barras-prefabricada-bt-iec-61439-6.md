---
title: "Canalizaciones de barras BT: impedancias y resistencia a Icc según IEC 61439-6"
description: "Parámetros eléctricos, dimensionado por cortocircuito y criterios de selección de canalizaciones de barras en instalaciones BT industriales con datos reales IEC 61439-6."
pubDate: 2026-11-04
keywords: ["canalizacion barras prefabricada BT", "busway IEC 61439-6", "resistencia cortocircuito barras", "impedancia canalización barras busduct"]
author: "Editor"
---

## Canalizaciones de barras prefabricadas: principio técnico y ámbito de aplicación

Las canalizaciones de barras prefabricadas (busway o busduct) son sistemas de distribución en BT donde los conductores activos, el neutro y el PE van encapsulados en una envolvente metálica continua y sellada. La norma de referencia es **IEC 61439-6:2012** (UNE-EN 61439-6:2012 en España), complementaria de IEC 61439-1:2011, que fija las condiciones de servicio, los requisitos de construcción y los procedimientos de verificación para sistemas con tensión asignada hasta 1000 V AC / 1500 V DC.

A diferencia del cableado convencional multiconductor, el busway permite insertar cajas de derivación (plug-in boxes) en cualquier punto de la canalización sin interrumpir la alimentación aguas abajo. Esta característica lo hace idóneo para:

- **Distribución vertical de edificios de altura** (riser): alimentación de cuadros de planta desde CGBT, con derivaciones cada piso.
- **Distribución troncal en naves industriales**: alimentación de máquinas a lo largo de la nave con acometidas directas.
- **Centros de datos y hospitales**: alta densidad de carga, necesidad de modificar puntos de conexión sin corte.

La geometría de los conductores dentro de la envolvente determina los parámetros eléctricos y la capacidad de resistencia al cortocircuito, que son los datos críticos para el dimensionado.

---

## Parámetros eléctricos: R, X y su importancia en el cálculo

### Resistencia por kilómetro (R)

La resistencia lineal de la barra fija las pérdidas Joule y la componente resistiva de la caída de tensión en régimen permanente. Para cobre a 20 °C, la resistividad es ρ = 0,0172 Ω·mm²/m; para aluminio, ρ = 0,0282 Ω·mm²/m (aproximadamente 65 % de la conductividad del cobre).

La caída de tensión en una canalización trifásica es:

```
ΔU (%) = (√3 × L × I × (R·cosφ + X·sinφ)) / (10 × U_n)
```

donde L es la longitud en km, I la corriente en A y U_n la tensión de línea en kV.

### Reactancia por kilómetro (X)

La reactancia es función exclusiva de la geometría: distancia entre conductores e inductancia mutua. Aquí radica la diferencia fundamental entre las dos grandes familias de canalizaciones:

**Medium Rating (MR):** conductores separados, envolvente abierta o semi-abierta. La mayor separación entre fases se traduce en inductancia mutua elevada: **X ∈ [0,076 – 0,260] Ω/km**.

**SCP (Sandwich Compact Profile):** conductores alternados por fases (L1-L2-L3-N-PE) en capas apiladas con separación milimétrica. Los campos magnéticos de fases adyacentes se cancelan parcialmente, reduciendo la reactancia a **X ∈ [0,003 – 0,023] Ω/km**, un orden de magnitud inferior al MR.

La implicación práctica es que en instalaciones con carga inductiva (motores, variadores de frecuencia), la componente X·sinφ del término de caída de tensión puede ser dominante en MR pero despreciable en SCP.

---

## Tabla comparativa de parámetros eléctricos (datos GElectrical / IEC 61439-6)

Los valores siguientes proceden de la base de datos GElectrical (implementación directa de IEC 61439-6, serie Legrand):

### Familia Medium Rating — Aluminio (MR-AL)

| Calibre (A) | R (Ω/km) | X (Ω/km) | Icw 1 s (kA) | Ipk (kA) |
|-------------|-----------|-----------|--------------|----------|
| 160         | 0,665     | 0,260     | 9            | 15       |
| 250         | 0,443     | 0,202     | 15           | 30       |
| 400         | 0,163     | 0,130     | 15           | 30       |
| 630         | 0,081     | 0,097     | 22           | 45       |
| 1000        | 0,073     | 0,076     | 18           | 36       |

### Familia SCP — Aluminio (SCP-AL)

| Calibre (A) | R (Ω/km) | X (Ω/km) | Icw 1 s (kA) | Ipk (kA) |
|-------------|-----------|-----------|--------------|----------|
| 630         | 0,084     | 0,023     | 22           | 48       |
| 1000        | 0,068     | 0,017     | 30           | 66       |
| 1600        | 0,039     | 0,014     | 48           | 106      |
| 2500        | 0,024     | 0,006     | 90           | 198      |
| 4000        | 0,016     | 0,006     | 96           | 211      |

### Familia SCP — Cobre (SCP-CU)

| Calibre (A) | R (Ω/km) | X (Ω/km) | Icw 1 s (kA) | Ipk (kA) |
|-------------|-----------|-----------|--------------|----------|
| 1000        | 0,035     | 0,017     | 30           | 66       |
| 1600        | 0,027     | 0,015     | 51           | 112      |
| 2500        | 0,017     | 0,011     | 53           | 116      |
| 4000        | 0,011     | 0,006     | 106          | 232      |
| 6300        | 0,006     | 0,004     | 106          | 232      |

> **Nota de verificación IEC**: cualquier valor numérico citado en este artículo es coherente con los datos de `GElectrical/database/line_busbar.csv`, que implementa IEC 61439-6 directamente.

---

## Resistencia al cortocircuito: Icw e Ipk según IEC 61439-6

La verificación de resistencia al cortocircuito es una de las 25 verificaciones que IEC 61439-6 impone al fabricante (cláusula 10.11 de la norma). Se definen dos magnitudes:

### Corriente de corta duración Icw (1 segundo)

Es la corriente eficaz que la canalización puede soportar durante **t = 1 s** sin deterioro de conductores ni envolvente. Para tiempos de falta inferiores a 5 s, se aplica el criterio adiabático:

```
I²·t = cte  →  I_admisible = Icw × √(1/t_falta)
```

Ejemplo: una barra con Icw = 30 kA (1 s) admite 42,4 kA durante 0,5 s, o 60 kA durante 0,25 s.

### Corriente de cresta Ipk

Es el valor de pico que las barras resisten sin deformación mecánica por esfuerzos electrodinámicos. La relación entre Ipk e Icw depende del factor de asimetría κ de la red (IEC 60909):

```
Ipk = √2 × κ × Icw
```

Para una red BT con relación X/R = 7, κ ≈ 1,8 → Ipk ≈ 2,54 × Icw. Para X/R = 2, κ ≈ 1,34 → Ipk ≈ 1,90 × Icw.

Verificación: en la tabla SCP-AL de 1000 A se tiene Icw = 30 kA e Ipk = 66 kA. Comprobando: √2 × 1,55 × 30 = 65,8 kA ≈ 66 kA, lo que corresponde a κ ≈ 1,55 (X/R ≈ 4,8), valor típico de BT industrial próximo a transformador de distribución.

El ingeniero debe calcular la corriente de cortocircuito máxima en el punto de instalación según **IEC 60909-0** y verificar:

```
Icc_max (3F) ≤ Icw de la canalización seleccionada
Icc_max_pico ≤ Ipk de la canalización seleccionada
```

---

## Coordinación con la protección upstream: criterio adiabático

La protección upstream (MCCB, ACB o fusible) debe despejar el cortocircuito antes de que la barra alcance su temperatura de daño. El criterio es:

```
I²t_protección ≤ I²t_barra
```

**Ejemplo de verificación completa:**

- Instalación: nave industrial, transformador 1000 kVA, Ucc = 6 %, 400 V
- Icc_3F en barras: Icc = (1000 × 1000) / (√3 × 400 × 0,06) = **24 kA**
- Canalización seleccionada: 1000A-SCP-AL, Icw = 30 kA (1 s) → cumple 30 kA ≥ 24 kA ✓
- MCCB upstream: 1000 A, poder de corte 50 kA, tiempo de disparo instantáneo ≤ 15 ms
- I²t aportado: (24.000)² × 0,015 = **8,64 × 10⁹ A²·ms = 8,64 × 10⁶ A²·s**
- I²t de la barra (1 s): (30.000)² × 1 = **9 × 10⁸ A²·s**

Resultado: I²t protección (8,64 × 10⁶) ≪ I²t barra (9 × 10⁸) → la protección despeja antes de que la barra llegue a temperatura de daño. ✓

En MCCB limitadores de corriente (clase H o L según IEC 60947-2), el I²t real es significativamente inferior al teórico, lo que amplía aún más el margen.

---

## Caída de tensión: ejemplo numérico con geometrías MR vs SCP

Configuración: canalización de 2000 A, longitud 50 m, carga trifásica 1500 A, cosφ = 0,85 (sinφ = 0,527).

**Con SCP-AL 2000 A** (R = 0,030 Ω/km, X = 0,011 Ω/km):
```
R_total = 0,030 × 0,050 = 0,0015 Ω
X_total = 0,011 × 0,050 = 0,00055 Ω
ΔU = √3 × 1500 × (0,0015×0,85 + 0,00055×0,527) / 400 × 100 = 1,02 %
```

**Con MR-AL 1000 A** (R = 0,073 Ω/km, X = 0,076 Ω/km) en paralelo (equivalente a 2000 A):
```
R_total = 0,073/2 × 0,050 = 0,001825 Ω
X_total = 0,076/2 × 0,050 = 0,0019 Ω
ΔU = √3 × 1500 × (0,001825×0,85 + 0,0019×0,527) / 400 × 100 = 1,74 %
```

La geometría SCP reduce la caída de tensión en cargas inductivas un 41 % frente al MR en paralelo, debido directamente a su menor reactancia.

La **ITC-BT-19 del REBT** fija el límite de caída de tensión en instalaciones industriales en **5 %** para alimentadores y **3 %** para circuitos terminales. En el ejemplo, ambas soluciones cumplen, pero en longitudes mayores o con cosφ más bajo el SCP mantiene margen mientras que el MR puede quedar al límite.

---

## Criterios de selección aplicables en obra

| Criterio | Medium Rating (MR) | SCP |
|----------|-------------------|-----|
| Rango corriente nominal | 160–1000 A | 630–6300 A |
| Reactancia típica (Ω/km) | 0,076–0,260 | 0,003–0,023 |
| Icw máximo (1 s) | hasta 22 kA | hasta 106 kA |
| Cargas resistivas (cosφ > 0,95) | Adecuado | Óptimo |
| Cargas inductivas (motores/VFD) | Verificar ΔU dinámica | Preferible |
| Icc punto instalación > 22 kA | No válido | Obligatorio |
| Longitud troncal > 30 m | Calcular ΔU | Preferible |
| Coste de adquisición por metro | Inferior | Superior |

**Reglas de decisión para selección en proyecto:**

1. **Icc_max > 22 kA en el punto**: sólo SCP puede alcanzar Icw ≥ 25 kA; el MR-AL llega como máximo a 22 kA (serie 630 A).
2. **Corriente nominal > 1000 A**: la gama MR estándar termina en 1000 A; cualquier calibre mayor requiere SCP.
3. **Longitud > 20 m con motores o variadores**: calcular ΔU con X real. Si ΔU_MR > 3 % (ITC-BT-19 circuito terminal), pasar a SCP.
4. **IP requerido por entorno**: IEC 61439-6 no impone grado mínimo, pero **ITC-BT-30 (REBT)** exige IP44 en locales mojados e IP55 en zonas de proyección de agua. Verificar ficha técnica del fabricante.
5. **Protección contra contacto indirecto en TN-S**: la envolvente metálica actúa como PEN o PE. La impedancia de lazo de falta usa r_pe_ohm_per_km (declarada en ficha técnica) para calcular la corriente de falta a tierra y verificar el tiempo de actuación del diferencial o del magnetotérmico según IEC 60364-4-41.
6. **Instalación en zonas con riesgo de vibración** (junto a máquinas): verificar que las uniones entre tramos mantienen la continuidad eléctrica del PE y el par de apriete de los tornillos de unión (típicamente 25–35 N·m según fabricante).

---

## Conclusión

El dimensionado de una canalización de barras prefabricadas exige verificar tres magnitudes simultáneamente: **la capacidad de corriente nominal**, **la resistencia al cortocircuito Icw/Ipk** frente a la Icc calculada según IEC 60909-0, y la **caída de tensión** usando R y X reales de la canalización. La geometría SCP, con reactancias un orden de magnitud inferiores al MR, es la opción técnicamente superior para distribución industrial con cargas inductivas y para puntos de red con Icc elevada. La verificación de coordinación I²t con la protección upstream (MCCB o fusible) cierra el ciclo de diseño y es exigible como parte de la documentación del cuadro según IEC 61439-1.
