---
title: "Relés de distancia para líneas MT: ajuste de zonas según IEC 60255-121"
description: "Principios de medida, características mho y cuadrilateral, cálculo de impedancias con datos IEC, ajuste de Zone 1-3 y factor K0 de tierra para líneas MT según IEC 60255-121."
pubDate: 2026-10-08
keywords: ["relé distancia protección líneas MT IEC 60255-121", "ajuste zonas distancia protección", "impedancia línea media tensión", "factor compensación tierra K0 distancia", "protección distancia redes malladas MT"]
author: "Editor"
---

La protección de distancia es la función de protección principal en redes de media tensión con topología mallada o en anillo, en instalaciones con generación distribuida y en cualquier feeder MT donde la selectividad amperimétrica es insuficiente. Mide la impedancia aparente vista desde el terminal del relé y opera cuando esa impedancia cae dentro de las zonas configuradas.

La norma IEC 60255-121 (adoptada en España como UNE-EN IEC 60255-121:2014) define los requisitos funcionales y de rendimiento para relés de distancia en sistemas trifásicos. No fija valores de ajuste —esos dependen de los parámetros de la red—, pero establece los criterios de verificación, precisión y temporización que cualquier relé certificado debe cumplir.

## Principio de medida de impedancia

El relé calcula la impedancia aparente a partir de los fasores de tensión y corriente en el terminal:

> Z_medida = V / I = (V_primario / n_TT) / (I_primario / n_TC)

En régimen normal de carga, Z_medida se sitúa en el cuadrante de carga (resistencia positiva elevada, reactancia baja). Ante una falta trifásica a distancia d de la barra:

> Z_falta = d × Z₁_km = d × (R₁ + jX₁) [Ω/km]

El principio de funcionamiento exige que Z_medida caiga dentro de la característica de operación configurada. Cuanto más próxima sea la falta, menor la impedancia medida, y más rápida la actuación.

**Datos de líneas aéreas 20 kV (GElectrical / IEC):**

| Conductor | R₁ (Ω/km) | X₁ (Ω/km) | Z₁ (Ω/km) | φ₁ (°) |
|---|---|---|---|---|
| 34-AL1/6-ST1A 20 kV | 0,8342 | 0,382 | 0,918 | 24,6 |
| 48-AL1/8-ST1A 20 kV | 0,5939 | 0,372 | 0,704 | 32,1 |
| 70-AL1/11-ST1A 20 kV | 0,4132 | 0,360 | 0,549 | 41,1 |
| 94-AL1/15-ST1A 20 kV | 0,306 | 0,350 | 0,464 | 48,8 |
| 149-AL1/24-ST1A 20 kV | 0,194 | 0,337 | 0,389 | 60,1 |
| 243-AL1/39-ST1A 20 kV | 0,1188 | 0,320 | 0,342 | 69,6 |

Para cable subterráneo NA2XS2Y 1×185 mm² 12/20 kV: R₁ = 0,161 Ω/km, X₁ = 0,117 Ω/km, Z₁ = 0,199 Ω/km, φ₁ = 36°. Las líneas subterráneas presentan relación R/X mayor que las aéreas y ángulo de línea menor, lo que condiciona la orientación de la característica de operación.

## Características de operación en el plano de impedancias

### Característica mho (circular)

La característica mho clásica es un círculo en el plano R-X que pasa por el origen y tiene su centro sobre la dirección del ángulo de línea φ_L. Su ecuación general:

> |Z - Z_D/2| ≤ Z_D/2

donde Z_D es el alcance de la zona. La ventaja de la mho es su inherente direccionalidad (no opera en falta inversa) y su simplicidad de ajuste. La limitación: la cobertura en resistencia de falta (R_fault) es proporcional al alcance, por lo que en líneas cortas con R_fault elevada (arco eléctrico), puede no cubrir la falta.

### Característica cuadrilateral (polígono)

Permite ajustar de forma independiente el alcance resistivo (R_reach) y el alcance reactivo (X_reach). Es la característica dominante en relés modernos (ABB REL670, Siemens 7SA87, SEL-421) porque:

- Cubre faltas con alta resistencia de arco sin ampliar innecesariamente el alcance en reactancia
- Permite ajustar el blinder de carga para evitar que el relé opere en condiciones de sobrecarga extrema
- Soporta líneas con ángulo de línea bajo (cables subterráneos con R/X ≈ 1,5)

IEC 60255-121 §5.4 exige que la característica se especifique en el plano de impedancias primarias y que la medida incluya selección de fase automática.

## Cálculo de zonas e impedancias: ejemplo 20 kV

**Sistema:** línea L1 de 15 km + línea L2 adyacente de 10 km, conductor 94-AL1/15-ST1A 20 kV.
**Parámetros de secuencia directa (GElectrical):** R₁ = 0,306 Ω/km, X₁ = 0,350 Ω/km.

**Impedancias de línea en primario:**

| Tramo | Longitud | R₁ (Ω) | X₁ (Ω) | Z₁ (Ω) |
|---|---|---|---|---|
| L1 (protegida) | 15 km | 4,59 | 5,25 | 6,96 |
| L2 (adyacente) | 10 km | 3,06 | 3,50 | 4,64 |

**Ajuste de zonas (convención estándar):**

| Zona | Alcance primario | Temporización | Criterio |
|---|---|---|---|
| Z1 | 85 % × Z_L1 = 5,92 Ω | Instantáneo (< 30 ms) | Margen para errores TC/TT y variación parámetros |
| Z2 | Z_L1 + 50% × Z_L2 = 9,28 Ω | t₂ = 0,3 – 0,5 s | Cubre 100 % de L1 + inicio de L2 |
| Z3 | Z_L1 + Z_L2 = 11,60 Ω | t₃ = 0,8 – 1,0 s | Respaldo remoto completo |
| Z_inv | −15 % × Z_L1 = −1,04 Ω | t_inv = 20 ms | Esquemas de comparación o respaldo de barra |

La Z2 debe verificarse contra el alcance Z1 del relé en el extremo remoto de L2: si Z2_local > Z1_remoto (alcance), hay riesgo de solapamiento y no selectividad. IEC 60255-121 §6.3 exige que los relés documenten esta condición de coordinación.

**Conversión a ohmios secundarios:**

Con TC 400/1 A y TT 20.000/110 V (n_TT = 181,8):

> Z_secundario = Z_primario × (n_TC / n_TT) = Z_primario × (400 / 181,8) = Z_primario × 2,20

| Zona | Z_primario (Ω) | Z_secundario (Ω) |
|---|---|---|
| Z1 | 5,92 | 13,02 |
| Z2 | 9,28 | 20,42 |
| Z3 | 11,60 | 25,52 |

**Nota crítica:** la conversión varía con cada instalación. Si los TC son 300/5 A y los TT son 20.000/100 V (n_TT = 200): factor = (300/5) / 200 = 0,30 → Z1_secundario = 5,92 × 0,30 = 1,78 Ω. Algunos relés aceptan ajuste en primario directamente (ABB REL670, SEL-421) evitando esta conversión.

## Factor de compensación de tierra K₀

Para la medida de impedancia en faltas monofásicas (Ph-E), el relé necesita compensar la diferencia entre la impedancia de secuencia cero Z₀ y la de secuencia directa Z₁. El factor de compensación de tierra K₀ (o K_E) se define según IEC 60255-121 §5.5:

> K₀ = (Z₀ − Z₁) / (3 × Z₁)

**Cálculo con datos GElectrical para 94-AL1/15-ST1A 20 kV:**

De la base de datos: R₀ = 0,306 Ω/km, X₀ = 1,050 Ω/km (con tierra de retorno)

> Z₁/km = 0,306 + j0,350 Ω
> Z₀/km = 0,306 + j1,050 Ω
> Z₀ − Z₁ = 0 + j0,700 Ω
> K₀ = j0,700 / [3 × (0,306 + j0,350)] = j0,700 / (0,918 + j1,050)
> |K₀| = 0,503 ∠ 41,2°  →  Re(K₀) = 0,379 · Im(K₀) = 0,331

En el relé se introducen |K₀| y ∠K₀, o bien los componentes Re(K₀) e Im(K₀) dependiendo del fabricante.

**Tabla K₀ para líneas aéreas 20 kV (GElectrical):**

| Conductor | R₁ | X₁ | R₀ | X₀ | \|K₀\| | ∠K₀ (°) |
|---|---|---|---|---|---|---|
| 48-AL1/8-ST1A | 0,5939 | 0,372 | 0,5939 | 1,116 | 0,567 | 31,2 |
| 94-AL1/15-ST1A | 0,306 | 0,350 | 0,306 | 1,050 | 0,503 | 41,2 |
| 149-AL1/24-ST1A | 0,194 | 0,337 | 0,194 | 1,011 | 0,525 | 41,5 |
| NA2XS2Y 1×185 12/20 kV | 0,161 | 0,117 | 0,161 | 0,351 | 0,531 | 58,8 |

**Condición de aplicación del factor K₀:** solo es válido para sistemas con neutro efectivamente puesto a tierra (directamente o mediante baja impedancia). En redes MT españolas con neutro aislado o con bobina Petersen (neutro resonante o compensado), la corriente de secuencia cero en falta monofásica es extremadamente baja (< 10 A capacitiva o compensada), y la función de distancia para faltas Ph-E no es aplicable. En estas redes, la protección diferencial de línea o los relés de falta a tierra por inyección de señal (Wattmétrico, Admittancia) son las opciones correctas para faltas monofásicas.

## Criterios de ajuste y selección según IEC 60255-121

| Criterio | Descripción técnica | Valor/regla |
|---|---|---|
| **Alcance Z1** | Subcobertura deliberada para evitar solapamiento con la Z1 del extremo remoto | 80 – 90 % de Z_L (típico 85 %) |
| **Alcance Z2** | Debe cubrir el 100 % de la línea protegida en cualquier condición de red | Z_L + 20 – 50 % Z_L2_min |
| **Z2 vs. carga** | Z2 < impedancia mínima de carga (Z_carga_min = V²_min / S_max) para evitar operación en sobrecarga | Verificar: Z_carga_min > 1,5 × Z2 |
| **Tiempo t₂** | Debe ser mayor que el tiempo de eliminación de falta de la protección primaria del ramal adyacente | t₂ ≥ t_prot_L2 + margen 100 ms |
| **Errores IEC 60255-121** | Precisión de alcance: ±5 % sobre el valor ajustado (§6.2); error de ángulo: ±2° | Verificar con inyección de prueba |
| **Blinder de carga** | En cuadrilateral: R_reach < 0,8 × R_carga_min para evitar actuación en condiciones de carga máxima | Ajustar R_reach ≤ 80 % de (V²_min / S_max) / V_n |
| **Overshooting Z1** | Tiempo de overreach al inicio de Z2 ≤ 30 ms (IEC 60255-121 §6.3); evita actuación incorrecta en coordinación con A/R | Verificar en comisionado |

**Selección de característica operativa por tipo de red:**

- **Líneas aéreas largas (> 5 km) con ángulo > 45°:** mho o cuadrilateral. La mho es suficiente si no hay generación distribuida en la línea.
- **Líneas cortas (< 3 km) o cables MT:** cuadrilateral obligatorio; la mho tiene R_reach insuficiente para cubrir faltas con arco.
- **Redes con generación distribuida (DER):** cuadrilateral con supervisión de dirección (función 21D); la inversión de potencia puede hacer que la mho opere incorrectamente en condición de oscilación o isla.
- **Esquemas de permiso o bloqueo (PUTT/POTT):** Z2 o zona inversa se usa como elemento direccional para la comunicación de disparo entre extremos; IEC 60255-121 §7 define los requisitos de respuesta temporal para estos esquemas (Δt ≤ 10 ms desde el canal).

## Conclusión

El ajuste de un relé de distancia para líneas MT requiere calcular las impedancias de secuencia directa y cero con los parámetros reales de la línea (GElectrical / IEC), escalarlas al secundario de TC y TT, y verificar la coordinación entre zonas. Los criterios clave: Z1 al 85 % para evitar solapamiento, Z2 ≥ Z_L + 20 % × Z_L2 con verificación frente a la impedancia mínima de carga, factor K₀ calculado para las secuencias reales de la línea (solo válido en sistemas con neutro puesto a tierra). En redes MT españolas con neutro aislado o resonante, la función Ph-E de la protección de distancia no opera para faltas monofásicas: se requiere protección diferencial de línea o función de falta a tierra de alta sensibilidad. La verificación en comisionado mediante inyección secundaria sobre las características configuradas es el único método para confirmar que los alcances, ángulos y temporizaciones cumplen IEC 60255-121 en la instalación real.
