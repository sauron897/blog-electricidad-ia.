---
title: "Puesta a tierra de pantallas en cables MT: bonding e IEC 60840"
description: "Criterios de bonding en pantallas de cables MT/AT XLPE según IEC 60840 e IEC 60502-2: tensión inducida, corrientes de circulación y cross-bonding con valores numéricos."
pubDate: 2026-11-19
keywords: ["puesta tierra apantallamiento cable MT IEC 60840", "corrientes circulacion pantalla cable XLPE", "cross-bonding cable media tension", "bonding pantalla cable MT IEC 60502-2"]
author: "Editor"
---

## Función de la pantalla metálica en cables XLPE de MT/AT

Los cables unipolares XLPE de media tensión (1–36 kV, cubiertos por IEC 60502-2) y los de alta tensión a partir de 36 kV (IEC 60840) incorporan una pantalla metálica —generalmente cinta de cobre o hilos helicoidales— que cumple tres funciones simultáneas:

1. **Retorno de la corriente de defecto a tierra**: en un fallo fase-pantalla, la pantalla debe conducir la corriente de defecto hasta el neutro del transformador sin perforar la cubierta exterior. IEC 60840 §12.4 exige que la pantalla soporte la corriente de cortocircuito asimétrica durante el tiempo de actuación de la protección.
2. **Homogeneización del campo eléctrico**: elimina la concentración de campo en los huecos entre conductores, garantizando el diseño dieléctrico del aislamiento.
3. **Reducción de interferencias electromagnéticas**: confina el campo alternante generado por el cable y atenúa las perturbaciones externas.

Lo que no es evidente para muchos proyectistas es que la pantalla, por ser un conductor paralelo al conductor de fase rodeado de campo magnético alterno, **tiene una FEM inducida que, si se cierra el circuito en sus dos extremos, genera corrientes circulantes que calientan el cable y reducen su capacidad de carga.** Gestionar esta tensión inducida es el objeto central del bonding.

## Tensión inducida en la pantalla: orden de magnitud y fórmula

Para un circuito trifásico de cables unipolares, la FEM inducida en la pantalla de una fase en disposición plana (flat formation) se calcula como:

```
E = ω · M · I · L
```

donde:
- ω = 2πf = 314 rad/s a 50 Hz
- M = inductancia mutua entre fase y pantalla (H/km)
- I = corriente de carga (A)
- L = longitud del tramo (km)

La inductancia mutua depende de la geometría. Para cables con separación entre ejes S y radio exterior del conductor de fase r₀:

```
M = (μ₀/2π) · ln(S/r₀)   [H/m]
```

Con separaciones habituales en MT enterrado en zanja (S = 200 mm entre ejes, cinta de cobre sobre aislamiento XLPE de 15 kV):
- r₀ ≈ 18–22 mm (cable 150–240 mm²)
- M ≈ 0,30–0,38 mH/km

Para una corriente de carga de 400 A en un tramo de 1 km en disposición plana:

```
E ≈ 314 × 0,33×10⁻³ × 400 × 1 ≈ 41 V
```

En **disposición en trébol** (trefoil formation, cables en contacto o con separación mínima), las FEM inducidas por las tres fases se anulan parcialmente entre sí, y la tensión inducida resultante se reduce a 15–20 V/(kA·km), frente a los 90–120 V/(kA·km) típicos en disposición plana para la fase exterior.

> **Referencia IEC**: IEC 60840:2020 Annex B incluye el procedimiento de cálculo de pérdidas en la pantalla λ₁ (factor de pérdidas de pantalla), integrado con IEC 60287-1-1 para la capacidad de carga del cable.

## Estrategias de conexión a tierra de la pantalla

Hay tres estrategias fundamentales, cada una con consecuencias radicalmente distintas sobre corrientes circulantes, tensión inducida y complejidad de la instalación:

| Estrategia | Tensión en extremo abierto | Corrientes circulantes | Pérdidas λ₁ | Aplicación típica |
|---|---|---|---|---|
| **Un extremo a tierra (SBJ)** | 0 V en extremo tierra; E inducida en extremo abierto | Nulas | 0 | Tramos cortos < 500 m; I < 300 A |
| **Ambos extremos a tierra (SBJ doble)** | 0 V en ambos extremos | Significativas (10–40 % de Ifase) | 0,1–0,4 | Cables cortos con alta corriente de fallo |
| **Cross-bonding** | < 50 V en puntos de transposición | Próximas a cero | < 0,02 | Cables de MT/AT de longitud media/larga |

### Un extremo a tierra (single-point bonding)

Solo se conecta a tierra en un extremo. La pantalla en el extremo no conectado permanece aislada (mediante una cubierta exterior) y adopta la tensión inducida flotante. El problema práctico es que esa tensión puede superar el límite de la cubierta exterior (típicamente 3 kV a tensión de ensayo según IEC 60502-2 §18.11) si la longitud o la corriente son elevadas.

**Límite práctico**: para 15 kV XLPE en disposición plana con I = 500 A, la tensión inducida a 1 km alcanza ~65 V. Con L = 5 km se llega a ~325 V en el extremo abierto, que ya requiere limitadores de tensión en pantalla (SVL, shield voltage limiters) según IEC 60840.

Se necesita conductor de equipotencialidad paralelo (CEP) a lo largo del tramo —con sección mínima 16 mm² Cu— para que, en caso de defecto, la corriente regrese sin imponer toda la tensión de defecto en el extremo abierto de la pantalla.

### Ambos extremos a tierra (solid bonding)

La pantalla queda cortocircuitada entre los dos terminales. No hay tensión inducida significativa, pero el circuito cerrado permite corrientes circulantes de baja frecuencia. Para un cable XLPE 150 mm² Cu (R_pantalla ≈ 0,25 Ω/km) con tramo de 1 km e I = 400 A en trébol:

```
I_pantalla ≈ E / R_pantalla ≈ 15 / 0,25 ≈ 60 A
```

Pérdida adicional en pantalla: P ≈ 60² × 0,25 × 1 = 900 W/km, lo que eleva la temperatura del cable e implica un derating de capacidad de carga. Para disposición plana la corriente circulante puede triplicarse.

### Cross-bonding (transposición de pantallas)

El tramo total se divide en tres subsecciones de longitud aproximadamente igual (L/3 cada una). Las pantallas de las tres fases se intercambian en cada junta de transposición (joint bay), de forma que cada pantalla pasa sucesivamente por las posiciones magnéticas de las tres fases.

Como la FEM inducida en cada subsección depende del campo de la fase vecina, y al transponer cada pantalla recorre los tres campos con signo alternado:

```
E_total = E₁ + E₂ + E₃ ≈ 0
(si L₁ = L₂ = L₃ y la disposición es simétrica)
```

En la práctica, con desequilibrio de longitud del 5–10 %, la tensión residual no anulada es del orden de 50–100 V en el punto de transposición, muy por debajo del límite de la cubierta exterior. Las pérdidas λ₁ caen a valores residuales (< 0,02), con un impacto prácticamente nulo en la capacidad de carga.

**Requisito normativo**: IEC 60840:2020 §12.4.3 impone que el sistema de cross-bonding incluya juntas de sección especial con bornes de pantalla accesibles, limitadores de tensión SVL (Zn-metal oxide) calibrados para la tensión de red, y caja de puesta a tierra terminal en cada extremo del tramo con conexión directa a la malla de tierra de la subestación.

## Cálculo de la corriente de cortocircuito admisible en la pantalla

Durante un defecto fase-tierra, la pantalla transporta la corriente de fallo hasta que actúa la protección. La condición adiabática de IEC 60949 establece:

```
S_pantalla ≥ I_cc · √t / k
```

donde:
- I_cc = corriente de cortocircuito (A)
- t = tiempo de actuación de la protección (s)
- k = factor de material: 143 para cobre recocido (pantalla de cinta)

**Ejemplo**: red MT de 20 kV con I_cc = 12 kA, protección de sobreintensidad de retaguardia con t = 0,5 s:

```
S_min = 12.000 × √0,5 / 143 = 12.000 × 0,707 / 143 ≈ 59 mm²
```

Una pantalla de cinta de cobre de 16 mm² (habitual en cables de distribución 15 kV) **es insuficiente** para este nivel de cortocircuito. En instalaciones industriales con I_cc elevada, se recurre a:
- Pantallas de mayor sección (35–50 mm² Cu)
- Conductor de protección paralelo (CPT, copper protective tape) adicional
- Neutro del transformador conectado a la pantalla del cable a través de un conductor de PE dedicado

> **IEC 60502-2 §12.4** fija la misma ecuación, pero limita la temperatura máxima de la pantalla a 250 °C (cobre recocido) para evitar deterioro del aislamiento XLPE, que tiene temperatura máxima de 90 °C en servicio y 250 °C en cortocircuito.

## Criterios de selección del sistema de bonding

La elección depende de cuatro parámetros: longitud del tramo, corriente de carga, nivel de cortocircuito y accesibilidad para mantenimiento.

| Parámetro | Un extremo a tierra | Ambos extremos | Cross-bonding |
|---|---|---|---|
| **Longitud tramo** | < 500 m | < 1 km | ≥ 1 km |
| **Corriente de carga** | < 300 A | Cualquiera (con derating) | Cualquiera |
| **I_cc red** | Baja (< 8 kA) | Media/alta | Media/alta |
| **Accesibilidad juntas** | No requiere juntas intermedias | No requiere | Obligatorio |
| **Coste instalación** | Bajo | Bajo–medio | Alto |
| **Pérdidas en pantalla** | Nulas | Medias–altas | Mínimas |
| **Tensión inducida** | Alta en extremo abierto | Nula | < 50 V residual |

**Regla práctica en distribución MT española (Red Eléctrica / REE, proyectos de 20 kV)**: para alimentadores en cable soterrado con secciones ≥ 150 mm² XLPE y longitudes > 800 m, el cross-bonding es la opción estándar. Para derivaciones en MT en instalaciones industriales con tramos de 50–200 m, el bonding en un solo extremo con SVL es suficiente y más económico.

**Criterio de selección del SVL (Shield Voltage Limiter)**: según IEC 60840 y la guía CIGRÉ B1.05, la tensión de conducción del SVL debe ser:
- U_c(SVL) ≥ 1,5 × U_inducida_máx (en servicio normal)
- U_c(SVL) < U_ensayo_cubierta_exterior / 1,25

Para cubiertas con U_ensayo = 10 kV, el SVL se calibra típicamente en 3,0–5,0 kV.

## Bonding en terminales de subestación: earthing del extremo de cable

En el extremo que conecta al cuadro de MT (celdas IEC 62271-200), la pantalla debe unirse a la barra de tierra de la subestación mediante un conductor de Cu ≥ 50 mm² con la menor inductancia posible (trenzado, no espiral). La inductancia parásita de esta conexión limita la eficacia del bonding en frente de onda transitoria (lightning, switching surges): un conductor de 1 m con 1 µH de inductancia limita el di/dt a ~100 kA/µs antes de saturar magnéticamente.

La ITC-BT-18 del REBT (aplicable en la parte de BT del mismo edificio) exige que la barra de tierra de la instalación de BT sea equipotencial con la pantalla de los cables MT que penetran en el edificio, para evitar diferencias de potencial peligrosas durante una descarga atmosférica o un defecto en la red MT.

## Conclusión

La puesta a tierra de pantallas en cables XLPE de MT no es un trámite de continuidad: es una decisión de diseño que afecta directamente a la capacidad de carga del cable (factor de pérdidas λ₁), a la integridad de la cubierta exterior bajo tensión inducida y a la aptitud de la pantalla para conducir la corriente de cortocircuito.

El técnico que diseña la instalación debe calcular:
1. La tensión inducida para la longitud y corriente previstas.
2. La sección mínima de pantalla para el I_cc y tiempo de protección de la red.
3. La estrategia de bonding (un extremo, doble, cross-bonding) en función de longitud, I_cc y coste.
4. La calibración del SVL si se opta por bonding en un extremo.

Los valores de reactancia (X = 0,08 Ω/km) y capacitancia de los cables XLPE de aluminio (C = 200–330 nF/km para secciones 25–300 mm² según GElectrical/IEC 60364-5-52) son la base numérica de cualquier cálculo de corriente capacitiva de fuga y de pérdidas en pantalla en instalaciones reales.
