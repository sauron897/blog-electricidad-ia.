---
title: "Corriente de cortocircuito BT: método de impedancias IEC 60909"
description: "Cálculo de Icc en instalaciones BT con el método de la fuente equivalente según IEC 60909-0: factor c, impedancias de red, transformador y cable, tipos de falta y selección de protecciones."
pubDate: 2026-09-26
keywords: ["corriente cortocircuito BT IEC 60909", "calculo Icc impedancias instalaciones BT", "método impedancias cortocircuito IEC 60909", "poder de corte magnetotérmico Icc"]
author: "Editor"
---

El cálculo de la corriente de cortocircuito es obligatorio en toda instalación eléctrica de baja tensión antes de seleccionar cualquier protección. La ITC-BT-22 del REBT exige que el poder de corte de cada dispositivo sea igual o superior a la corriente de cortocircuito prevista en su punto de instalación. Sin este dato, la selección de magnetotérmicos y MCCB es especulativa.

La norma de referencia es la **IEC 60909-0:2016** (*Short-circuit currents in three-phase a.c. systems — Part 0: Calculation of currents*), que define el método de la fuente de tensión equivalente. En España la adopta íntegramente como **UNE-EN 60909-0:2016**.

## Método de la fuente de tensión equivalente (IEC 60909-0)

El método sustituye toda la red aguas arriba del punto de falta por una única fuente de tensión de valor:

```
U_fuente = c · Un / √3
```

donde `c` es el **factor de tensión** (Tabla 1 de IEC 60909-0) y `Un` la tensión nominal de línea.

### Valores del factor c

| Nivel de tensión | Icc máximo | Icc mínimo |
|---|---|---|
| BT (≤ 1000 V), Un > 1 kV | 1,10 | 0,95 |
| MT / AT (> 1 kV) | 1,10 | 1,00 |

Para instalaciones BT en España (Un = 400 V):
- **c = 1,10** para verificar el poder de corte de protecciones (escenario más desfavorable).
- **c = 0,95** para verificar el disparo mínimo garantizado de protecciones (Icc mínimo que debe disparar el dispositivo).

El método asume que todas las cargas están desconectadas y que la tensión prefalla es exactamente `c · Un / √3`, lo que simplifica el cálculo a una suma vectorial de impedancias en serie entre la red y el punto de falta.

## Componentes de la impedancia de cortocircuito

La impedancia total Ztotal es la suma (vectorial) de tres contribuciones principales:

### 1. Red de distribución (Z_Q)

La compañía distribuidora facilita la **potencia de cortocircuito trifásica** en el punto de conexión (PCC): `S"kQ`. A partir de ella:

```
Z_Q = Un² / S"kQ
```

Ejemplo: Si la distribuidora indica `S"kQ = 350 MVA` en un PCC a 20 kV con transformador 400V/20kV:
```
Z_Q = 400² / 350×10⁶ = 160 000 / 350 000 000 = 0,000457 Ω
```
En muchas instalaciones industriales sin datos precisos se usa `S"kQ = 250–500 MVA`. Su contribución a la Z_total en BT suele ser despreciable frente a la del transformador.

### 2. Transformador MT/BT (Z_T)

La impedancia del transformador domina el cálculo en la mayoría de instalaciones BT:

```
Z_T = (u_cc / 100) × (Un_T² / S_nT)
```

La parte resistiva se obtiene de las pérdidas en el cobre (`P_kT` en W):

```
R_T = P_kT × Un_T² / (3 × S_nT²)
X_T = √(Z_T² − R_T²)
```

**Ejemplo:** Transformador 400 kVA, u_cc = 4 %, P_kT = 4 500 W, Un = 400 V:
```
Z_T = 0,04 × (400² / 400 000) = 0,04 × 0,4 = 0,0160 Ω
R_T = 4 500 × 400² / (3 × 400 000²) = 0,0015 Ω
X_T = √(0,0160² − 0,0015²) = 0,01593 Ω
```

### 3. Cables (Z_cable)

La resistencia del conductor a temperatura de servicio (IEC 60909-0 §3.3):

```
R_cable = ρ_θ × L / S
```

Con los factores de resistividad a temperatura máxima de servicio (80 °C para XLPE):
- **Cobre:** ρ₂₀ = 0,01786 Ω·mm²/m → ρ₈₀ = 0,01786 × (1 + 0,00393 × 60) = **0,02208 Ω·mm²/m**
- **Aluminio:** ρ₂₀ = 0,02830 Ω·mm²/m → ρ₈₀ = **0,03497 Ω·mm²/m**

La reactancia de los cables, según la base de datos GElectrical (UNE-HD 60364-5-52), es prácticamente constante para todos los conductores XLPE:

```
X_cable ≈ 0,08 Ω/km (Cu y Al, 1ph y 3ph, secciones 4–300 mm²)
```

Este valor se usa directamente para cualquier cable de la gama normalizada.

## Tipos de falta y fórmulas de Icc

| Tipo de falta | Fórmula | Severidad |
|---|---|---|
| Trifásica (3Ph) | `I"k3 = c·Un / (√3·|Z1|)` | Máxima en sistemas equilibrados |
| Bifásica (2Ph) | `I"k2 = (√3/2)·I"k3 = 0,866·I"k3` | 13 % inferior a I"k3 |
| Monofásica (1Ph-N) | `I"k1 = c·Un / (2·Z1 + Z0)` | Variable según Z0 |

Para cables XLPE en instalación TN, la impedancia homopolar Z0 ≈ 3–4 × Z1, por lo que `I"k1 < I"k3`. El cortocircuito trifásico es el escenario de diseño para el poder de corte.

## Ejemplo práctico: instalación industrial BT

**Instalación:** Transformador 400 kVA (u_cc = 4 %, P_kT = 4 500 W) + cable Cu XLPE 50 mm², 100 m hasta cuadro secundario.

**Cálculo de Z_T:**
```
Z_T = 0,0160 Ω;  R_T = 0,0015 Ω;  X_T = 0,01593 Ω
```

**Cálculo de Z_cable** (Cu 50 mm², 100 m a 80 °C, datos GElectrical):
```
R_cable = 0,02208 × 100 / 50 = 0,04416 Ω
X_cable = 0,08 × 0,100 = 0,00800 Ω
```

**Impedancia total:**
```
R_total = 0,0015 + 0,04416 = 0,04566 Ω
X_total = 0,01593 + 0,00800 = 0,02393 Ω
|Z_total| = √(0,04566² + 0,02393²) = √(0,002085 + 0,000573) = √0,002658 = 0,05155 Ω
```

**Corriente de cortocircuito trifásica máxima** (c = 1,10):
```
I"k3 = 1,10 × 400 / (√3 × 0,05155) = 440 / 0,08929 = 4 929 A ≈ 4,9 kA
```

**En la cabecera del transformador** (solo Z_T):
```
I"k3_cab = 1,10 × 400 / (√3 × 0,01609) = 440 / 0,02787 = 15 784 A ≈ 15,8 kA
```

Los MCB estándar del catálogo GElectrical (L&T, Legrand DX3, Schneider iC60a) tienen `Isc = 10 kA`. Son **insuficientes en cabecera** del transformador de 400 kVA. Se requiere un MCCB o fusible con poder de corte ≥ 16 kA conforme a IEC 60947-2.

## Criterios de selección de protecciones según Icc

La ITC-BT-22 §4 establece que toda protección debe tener poder de corte no inferior a la Icc prevista. La IEC 60947-2 diferencia:

| Parámetro | Definición | Condición |
|---|---|---|
| `Icu` (poder ruptura último) | Capacidad máxima de corte, sin recuperación | ≥ I"k3 en el punto |
| `Ics` (poder ruptura de servicio) | Capacidad con continuidad operativa; típicamente 50–100 % de Icu | ≥ I"k3 si se exige continuidad |
| `Icm` (corriente de cierre) | Pico de corriente asimétrico: Icm ≥ n × Icu | Aplica en MCCB; n según cos φ |

**Criterios de selección en obra:**

1. **Calcular I"k3 en cada punto** de instalación: cabecera de cuadro, inicio de subcircuito, terminales del equipo receptor.
2. **Verificar Icu ≥ I"k3_max** (c = 1,10). Nunca dimensionar por I"k mínimo.
3. **Si se usa protección en cascada** (back-up protection, IEC 60947-2 Anexo A), el conjunto {MCCB aguas arriba + MCB aguas abajo} debe estar validado conjuntamente por el fabricante con el Icc real del punto.
4. **Verificar el disparo de Icc mínima** (c = 0,95) para el relé o disparador magnético: `I"k1_min ≥ I_mag_mín`. En circuitos largos con cable de pequeña sección, la Icc mínima puede caer por debajo del umbral magnético del MCB, haciendo ineficaz la protección contra cortocircuito. En ese caso, reducir la longitud del circuito o aumentar la sección.
5. **Resistencia del conductor de protección (PE):** En esquemas TN, el bucle de falta incluye R_PE. Para neutro y PE en el mismo cable (TN-C o TN-S), añadir la resistencia del conductor PE al cálculo de Z_total del bucle de falta.

## Conclusión

El método de la fuente de tensión equivalente según IEC 60909-0 permite calcular con precisión suficiente la corriente de cortocircuito en cualquier punto de una instalación BT con impedancias en serie. Los tres datos clave son: `Z_T` del transformador (calculada de u_cc y P_kT), `Z_cable` (con ρ a temperatura de servicio y X = 0,08 Ω/km para XLPE), y el factor `c = 1,10` para dimensionar el poder de corte. La cabecera de un transformador de 400 kVA genera Icc > 15 kA, lo que exige MCCB o fusible; a 100 m con 50 mm² Cu la Icc cae a ~5 kA, donde los MCB estándar de 10 kA son suficientes. Verificar siempre en ambos extremos del circuito.
