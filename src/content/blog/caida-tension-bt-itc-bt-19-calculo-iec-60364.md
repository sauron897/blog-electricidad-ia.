---
title: "Caída de tensión en BT: cálculo IEC 60364 e ITC-BT-19"
description: "Cálculo exacto de caída de tensión en instalaciones BT: fórmulas IEC 60364-5-52, límites ITC-BT-19, reactancias GElectrical y criterios de selección de sección."
pubDate: 2026-09-23
keywords: ["caida tension BT", "ITC-BT-19 caida tension", "calculo caida tension cable", "IEC 60364-5-52", "seccion cable caida tension"]
author: "Editor"
---

La caída de tensión es, junto con la capacidad de conducción de corriente, el segundo criterio fundamental para la selección de la sección de un conductor en BT. Muchos técnicos aplican la fórmula simplificada sin entender cuándo introduce un error significativo ni qué límites normativos aplican en cada tramo de la instalación. Este artículo resuelve ambos puntos con datos numéricos reales.

## Límites normativos: ITC-BT-19 y la cadena de caídas admisibles

El REBT (RD 842/2002) distribuye los límites de caída de tensión por tramos:

| Tramo de instalación | Normativa | Límite ΔU máx |
|---|---|---|
| Línea General de Alimentación (LGA) | ITC-BT-14 | 0,5 % |
| Derivación Individual (DI) | ITC-BT-15 | 1 % |
| Circuito interior — alumbrado | ITC-BT-19, apdo. 2.2.2 | 3 % |
| Circuito interior — fuerza / otros usos | ITC-BT-19, apdo. 2.2.2 | 5 % |

Los límites de ITC-BT-19 se calculan **desde el origen del cuadro de distribución del abonado**, no desde el transformador. La suma LGA + DI + circuito no puede superar 4,5 % (alumbrado) o 6,5 % (fuerza) contando desde el secundario del transformador.

En instalaciones industriales alimentadas directamente desde MT/BT, IEC 60364-5-52 § 5.2 permite hasta 4 % en condiciones normales y 6 % en arranque de motores si el fabricante lo avala. La norma UNE-HD 60364-5-52:2014 transpone este criterio al marco español.

## Método exacto: fórmula con resistencia y reactancia

La expresión exacta por conductor según IEC 60364-5-52 para un circuito trifásico equilibrado es:

```
ΔU = √3 × I × L × (r·cosφ + x·sinφ)  [V]
ΔU% = ΔU / U_línea × 100
```

Para circuito monofásico:

```
ΔU = 2 × I × L × (r·cosφ + x·sinφ)   [V]
ΔU% = ΔU / U_fase × 100
```

Donde:
- `I` = corriente de carga (A)
- `L` = longitud del circuito (km)
- `r` = resistencia por kilómetro del conductor (Ω/km) a la temperatura de régimen
- `x` = reactancia por kilómetro (Ω/km) — de la base de datos GElectrical / IEC
- `cosφ` = factor de potencia de la carga

### Resistividades a temperatura de servicio (fuente: IEC 60228 + IEC 60364-5-52)

| Material | Aislamiento | T_max (°C) | ρ (Ω·mm²/m) | γ (m/Ω·mm²) |
|---|---|---|---|---|
| Cu | PVC | 70 | 0,02250 | 44,4 |
| Cu | XLPE/EPR | 90 | 0,02413 | 41,4 |
| Al | PVC | 70 | 0,03608 | 27,7 |
| Al | XLPE/EPR | 90 | 0,03861 | 25,9 |

La resistencia por km de cada conductor es `r = ρ / S`, siendo `S` la sección en mm².

### Reactancias según GElectrical / UNE-HD 60364-5-52

La base de datos GElectrical (que implementa UNE-HD 60364-5-52 directamente) proporciona los siguientes valores de reactancia a 50 Hz:

| Tipo de cable | x (Ω/km) |
|---|---|
| Cu/Al PVC, en tubo o bandeja (conductores separados) | 0,17 |
| Cu/Al XLPE/EPR, multicondutor o apantallado | 0,08 |

Para secciones ≤ 50 mm², la reactancia representa menos del 5 % de la impedancia total con cosφ ≥ 0,8 y longitudes < 100 m. Por encima de 70 mm² o en cables de larga longitud, ignorar `x` introduce errores superiores al 2 % del valor calculado.

## Método simplificado: fórmula resistiva (ITC-BT-19 apdo. 3)

Para cargas resistivas o circuitos cortos donde la componente inductiva es despreciable:

```
S_mín = (2 × ρ × L × P) / (ΔU_max × U_n)        [1 fase, mm²]
S_mín = (ρ × L × P) / (ΔU_max × U_n)             [3 fases, mm²]
```

O equivalentemente con la conductividad `γ`:

```
ΔU% = (2 × P × L) / (γ × S × U_n²) × 100         [1 fase]
ΔU% = (P × L) / (γ × S × U_n²) × 100              [3 fases, U_n = tensión de línea]
```

**Ejemplo 1 — Circuito de alumbrado monofásico:**

- P = 3.600 W, cosφ = 1,0 (LED), L = 40 m, U_n = 230 V
- Cable Cu PVC 70°C, γ = 44,4 m/(Ω·mm²)
- Límite ITC-BT-19: 3 %

```
S_mín = (2 × 40 × 3.600) / (0,03 × 230 × 44,4 × 230) = 288.000 / 70.884 ≈ 4,1 mm²
```

→ Sección normalizada mínima: **6 mm²**

**Ejemplo 2 — Motor trifásico 22 kW:**

- P = 22.000 W, cosφ = 0,85, sinφ = 0,527, I = 43 A (400 V, η = 92 %)
- L = 120 m, cable Cu XLPE (r a 90°C = 0,0241/S, x = 0,08 Ω/km)
- Límite: 5 % = 20 V sobre 400 V

Para S = 16 mm²:
```
r = 0,0241 / 16 = 1,506 Ω/km → 0,1807 Ω sobre 120 m
x = 0,08 × 0,120 = 0,0096 Ω

ΔU = √3 × 43 × (0,1807 × 0,85 + 0,0096 × 0,527)
    = 74,48 × (0,1536 + 0,00506)
    = 74,48 × 0,1587 ≈ 11,82 V → ΔU% = 2,96 %  ✓
```

Para S = 10 mm²:
```
r = 0,0241 / 10 = 2,41 Ω/km → 0,2892 Ω
ΔU = 74,48 × (0,2892 × 0,85 + 0,0096 × 0,527)
    = 74,48 × (0,2458 + 0,00506) ≈ 18,73 V → ΔU% = 4,68 %  ✓ (justo)
```

En arranque directo, la corriente transitoria del motor alcanza 6×In = 258 A durante 5-10 s. En ese instante, con S = 10 mm² y L = 120 m, la caída temporal supera el 28 %: completamente inadmisible para instalaciones con alumbrado contiguo al mismo cuadro. Este es el argumento técnico para usar IEC 60947-4-1 y seleccionar arrancadores suaves o variadores cuando la longitud de alimentación supera 80-100 m.

## Factores de corrección de ampacidad (no directamente caída de tensión)

La sección mínima por caída de tensión puede ser mayor que la mínima por capacidad térmica (tabla IEC 60364-5-52 / UNE-HD 60364-5-52). En ese caso la caída de tensión es el criterio dimensionante. Algunas instalaciones industriales largas requieren secciones 2-3 veces superiores a la mínima térmica.

### Corrección de resistencia por temperatura

La resistencia del conductor varía con la temperatura real de servicio. Si el conductor opera a temperatura `T` diferente de 70°C/90°C:

```
r_T = r_ref × [1 + α × (T - T_ref)]
```

Con α = 3,93×10⁻³ K⁻¹ (cobre). En condiciones de carga parcial (50 % de Iz), T ≈ T_amb + (T_max - T_amb) × (I/Iz)² ≈ 45 °C con T_amb = 30 °C y T_max = 70 °C.

Esto reduce la resistencia real un 8-10 % respecto al valor de la tabla, por lo que el dimensionado por caída de tensión usando los valores de tabla a T_max es conservador.

## Criterios de selección de sección por caída de tensión

El proceso de decisión en obra sigue este orden:

1. **Determinar la corriente de diseño** `I_B` (incluyendo factor de simultaneidad)
2. **Calcular sección mínima térmica** S_term a partir de IEC 60364-5-52, método de instalación y factores de corrección aplicables (temperatura, agrupamiento, tipo de bandeja)
3. **Calcular sección mínima por caída de tensión** S_ΔU con la fórmula exacta para el `cosφ` real y la longitud real
4. **Tomar la mayor de las dos secciones**, y redondear a la sección normalizada IEC 60228 superior: 1,5 — 2,5 — 4 — 6 — 10 — 16 — 25 — 35 — 50 — 70 — 95 — 120 — 150 — 185 — 240 — 300 mm²
5. **Verificar que el magnetotérmico protege el conductor** según condición `I_n ≤ I_z` e `I_2 ≤ 1,45 × I_z` (IEC 60898-1, IEC 60947-2)
6. **Verificar la longitud máxima de protección** de cortocircuito: `L_max = S × U_n / (√3 × ρ × I_cc_mín)` para instalaciones TN o TT

### Longitudes máximas aproximadas por caída de tensión del 3 % (monofásico 230 V, Cu PVC, cosφ=0,9)

| Sección (mm²) | In=10A (2,3kW) | In=16A (3,7kW) | In=25A (5,75kW) | In=32A (7,4kW) |
|---|---|---|---|---|
| 1,5 | 14,5 m | 9,1 m | 5,8 m | — |
| 2,5 | 24,2 m | 15,1 m | 9,7 m | 7,6 m |
| 4 | 38,7 m | 24,2 m | 15,5 m | 12,1 m |
| 6 | 58,1 m | 36,3 m | 23,2 m | 18,2 m |
| 10 | 96,8 m | 60,5 m | 38,7 m | 30,3 m |
| 16 | 154,8 m | 96,8 m | 61,9 m | 48,4 m |
| 25 | 241,9 m | 151,2 m | 96,8 m | 75,6 m |

*Calculado con γ = 44,4 m/(Ω·mm²), componente resistiva pura, fórmula: L = (ΔU% × γ × S × U²) / (2 × P × 100)*

Para trifásico a 400 V, los valores se multiplican por aproximadamente 3 (mayor tensión de línea y menor longitud de ida-vuelta).

## Conclusión

El criterio de caída de tensión no es una comprobación final: es un criterio dimensionante que puede exigir secciones significativamente mayores que las térmicas, especialmente en circuitos largos (> 30 m en 1 fase, > 50 m en 3 fases) o con cargas inductivas (cosφ < 0,85). La fórmula simplificada es válida para cables cortos y cosφ próximo a 1; para conductores de sección ≥ 50 mm² o longitudes > 100 m, usar siempre la expresión con reactancia según IEC 60364-5-52, con los valores de x = 0,08 Ω/km (XLPE) o 0,17 Ω/km (PVC en tubo) que proporciona la base de datos UNE-HD 60364-5-52. Documentar siempre el criterio dimensionante en la memoria del proyecto: si la sección excede la mínima térmica, la razón debe quedar reflejada para el cálculo de protecciones aguas abajo.
