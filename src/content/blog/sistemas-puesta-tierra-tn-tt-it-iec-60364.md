---
title: "Sistemas TN, TT e IT: impedancia de bucle según IEC 60364-4-41"
description: "Análisis técnico de los esquemas de puesta a tierra TN-S, TN-C, TT e IT: cálculo de impedancia de bucle, Uf límite y coordinación de protecciones según IEC 60364-4-41 y REBT ITC-BT-24."
pubDate: 2026-09-21
keywords: ["sistemas puesta tierra TN TT IT IEC 60364", "impedancia bucle falta tierra", "REBT ITC-BT-24 contactos indirectos", "tensión contacto 50V IEC 60364-4-41"]
author: "Editor"
---

Los esquemas de puesta a tierra condicionan directamente cómo circula la corriente de falta a tierra, qué dispositivo la detecta y en qué tiempo. Elegir TN-S, TT o IT no es una decisión estética: determina la impedancia de bucle de falta, el nivel de la corriente de cortocircuito monofásico a tierra (Icc1φ) y, por tanto, si el magnetotérmico o el diferencial puede actuar dentro del tiempo máximo que fija IEC 60364-4-41 para evitar una tensión de contacto peligrosa.

Este artículo desarrolla los tres esquemas con los cálculos numéricos que necesita un técnico en obra: resistencias de bucle, condición de disparo, tiempo máximo admisible y criterios de selección del esquema.

---

## Fundamentos físicos: tensión de contacto y tiempo de desconexión

La magnitud que limita la norma no es la corriente de falta sino la **tensión de contacto UL** que puede aparecer sobre el cuerpo humano cuando toca una masa defectuosa. IEC 60364-4-41 (tabla 41.1 transpuesta como UNE-HD 60364-4-41) establece:

| Condición del entorno | UL máximo (CA) | UL máximo (CC) |
|---|---|---|
| Normal (locales secos, locales habitados) | **50 V** | 120 V |
| Condición especial (emplazamientos mojados, exteriores, locales agrícolas) | **25 V** | 60 V |

El REBT ITC-BT-24 (tabla I) adopta los mismos valores: 50 V en locales secos y 24 V en locales húmedos/mojados.

El tiempo máximo de desconexión para un sistema TN a 230/400 V en circuitos de distribución (Ra ≤ 30 Ω) es:

| Tensión nominal fase-neutro (V) | Tiempo máximo TN (s) | Tiempo máximo TT (s) |
|---|---|---|
| 120 | 0,8 | 0,3 |
| 230 | **0,4** | **0,2** |
| 400 | 0,2 | 0,07 |
| > 400 | 0,1 | 0,04 |

En circuitos terminales (enchufes, aparatos portátiles) los tiempos se reducen a la mitad respecto a los de distribución para el esquema TN: 0,2 s a 230 V. En el esquema TT la limitación se aplica mediante un RCD con Im ≤ 30 mA que garantiza siempre un disparo < 0,04 s por su propio estándar (IEC 61008-1).

---

## Esquema TN: cálculo de la impedancia de bucle de falta Zs

En el esquema TN las masas están unidas al neutro de la fuente (TN-S: conductor PE independiente; TN-C: conductor PEN combinado; TN-C-S: PEN hasta un punto y separación posterior). El bucle de falta incluye la impedancia de la fuente (transformador), el conductor de fase y el conductor de protección PE (o PEN) de retorno.

### Condición de disparo

Para que el magnetotérmico actúe en el tiempo exigido, la corriente de falta If debe superar la corriente de actuación magnética Ia del dispositivo:

```
If ≥ Ia  →  U0 / Zs ≥ Ia
→  Zs ≤ U0 / Ia
```

Donde:
- **U0** = tensión nominal fase-tierra = 230 V (red 400/230 V)
- **Zs** = impedancia total del bucle de falta (Ω)
- **Ia** = corriente mínima de disparo instantáneo del magnetotérmico

Para un MCB curva C de 16 A (IEC 60898-1), Ia = 5·In a 10·In → tomamos Ia = 5 × 16 = 80 A (umbral inferior conservador):

```
Zs ≤ 230 / 80 = 2,875 Ω
```

Para una curva B (Ia = 3·In a 5·In), con In = 16 A → Ia = 3 × 16 = 48 A:

```
Zs ≤ 230 / 48 = 4,79 Ω
```

### Cálculo de Zs para un circuito típico

La resistencia a 20 °C del cobre es ρ = 0,0175 Ω·mm²/m (IEC 60228). Para temperatura de operación se aplica el factor 1,25 (conductores a 70 °C en XLPE/PVC según IEC 60364-5-54):

```
Zs = (Zfuente + Rfase + RPE) × 1,25
```

Ejemplo: circuito de 50 m de longitud con cable 3G2,5 mm² Cu (fase + PE igual sección), transformador con Zt = 0,035 Ω:

```
Rfase = (0,0175 × 50) / 2,5 = 0,350 Ω
RPE   = (0,0175 × 50) / 2,5 = 0,350 Ω  (mismo conductor)
Zs    = (0,035 + 0,350 + 0,350) × 1,25 = 0,919 Ω
```

Con Zs = 0,919 Ω: If = 230 / 0,919 = **250 A** → supera con holgura Ia = 80 A para un C16. El sistema TN es viable a 50 m con 2,5 mm².

Para 120 m con el mismo conductor:

```
Rfase = (0,0175 × 120) / 2,5 = 0,840 Ω
RPE   = 0,840 Ω
Zs    = (0,035 + 0,840 + 0,840) × 1,25 = 2,144 Ω
If    = 230 / 2,144 = 107 A  → ¿supera C16 con Ia = 80 A? Sí.
```

A 200 m:

```
Rfase = 1,400 Ω; RPE = 1,400 Ω
Zs    = (0,035 + 1,400 + 1,400) × 1,25 = 3,543 Ω
If    = 230 / 3,543 = 64,9 A  → NO supera C16 con Ia = 80 A. Necesita curva B o sección mayor.
```

Esta es la limitación práctica del TN en circuitos largos de pequeña sección: llega un punto en que el magnetotérmico no puede actuar en tiempo sin empeorar la sección del PE o reducir la longitud protegida.

---

## Esquema TT: coordinación con diferencial RCD

En el esquema TT las masas se conectan a una toma de tierra local independiente de la del neutro de la red. La corriente de falta circula por la resistencia de la puesta a tierra de las masas (Ra) y la resistencia de tierra del neutro de la red (Rb), formando un bucle de alta impedancia.

La condición de protección según IEC 60364-4-41 (cláusula 411.5.3) y REBT ITC-BT-24 es:

```
Ra × IΔn ≤ UL
```

Donde:
- **Ra** = resistencia de la toma de tierra de las masas (Ω)
- **IΔn** = corriente diferencial nominal del RCD (A)
- **UL** = tensión límite de contacto (50 V o 25 V)

Para un diferencial de 30 mA (IΔn = 0,030 A) con UL = 50 V:

```
Ra ≤ 50 / 0,030 = 1.667 Ω
```

Para un diferencial de 300 mA (IΔn = 0,300 A) con UL = 50 V:

```
Ra ≤ 50 / 0,300 = 167 Ω
```

En la práctica, una puesta a tierra de un edificio industrial bien ejecutada tiene Ra entre 2 y 20 Ω, lo que permite usar diferenciales de 300 mA en el cuadro general (selectividad con el diferencial de 30 mA aguas abajo). El REBT ITC-BT-18 fija como límite 37 Ω para la resistencia de tierra en instalaciones de BT con tensión de 24 V y 10 Ω en locales con riesgo (ITC-BT-30).

### Ventaja del TT: independencia de Zs

En TT no se exige un Zs mínimo para el disparo del magnetotérmico: la protección contra defecto a tierra la da el RCD exclusivamente. Por eso el TT es la solución estándar en distribución pública española (REBT ITC-BT-08), donde la compañía distribuidora no garantiza la impedancia del bucle hasta el abonado.

---

## Esquema IT: supervisión continua con IMD y protocolo de primera falta

El esquema IT tiene el neutro aislado de tierra (o conectado a través de una impedancia Zn ≥ 1 kΩ típicamente). El sistema IT no es una curiosidad académica: es obligatorio en instalaciones hospitalarias de quirófanos y unidades de cuidados intensivos (IEC 60364-7-710, UNE-HD 60364-7-710) y se usa en procesos industriales donde un primer defecto no puede interrumpir la producción (plantas químicas, fermentación, data centers críticos).

### Primera falta: corriente capacitiva

Con una primera falta a tierra, la corriente de falta Idf1 circula únicamente por la capacitancia distribuida de la red hacia tierra:

```
Idf1 = U0 × √3 × Cc × ω × L
```

Donde:
- **Cc** = capacitancia de cable por km (típicamente 100-350 nF/km según GElectrical/cable_iec.csv)
- **L** = longitud total de la red en km
- **ω** = 2π × 50 Hz = 314,16 rad/s

Para una red IT con 500 m de cable de 16 mm² Cu XLPE (Cc ≈ 180 nF/km según GElectrical):

```
Cc_total = 180 nF/km × 0,5 km = 90 nF = 90 × 10⁻⁹ F
Idf1 = 230 × 1,732 × 90×10⁻⁹ × 314,16 = 11,3 mA
```

Esta corriente es insuficiente para provocar una tensión de contacto peligrosa, por eso el REBT y la IEC permiten continuar la producción con la primera falta. Sin embargo, **es obligatorio instalar un dispositivo de vigilancia de aislamiento (IMD, Insulation Monitoring Device)** que detecte esa primera falta (IEC 61557-8). El umbral de alarma habitual es Riso < 100 kΩ; el umbral de desconexión (si se programa) < 10 kΩ.

### Segunda falta: doble falta a tierra

Con dos faltas simultáneas en conductores diferentes (fases distintas), la corriente de falta es comparable a un cortocircuito bifásico. La tensión entre las dos masas defectuosas puede llegar a U = √3 × U0 / 2 = 200 V (en red 400/230 V) si las tomas de tierra son la misma. Por eso la norma IEC 60364-4-41 exige que ante segunda falta se actúe igual que en TN o TT (según si las masas tienen tierra común o no).

---

## Criterios de selección del esquema de puesta a tierra en obra

| Criterio | TN-S | TN-C | TT | IT |
|---|---|---|---|---|
| Continuidad de servicio con 1ª falta | No | No | No | **Sí** |
| Protección principal | Magnetotérmico | Magnetotérmico | RCD obligatorio | IMD + RCD/MCB en 2ª falta |
| Coste del cableado | Medio (PE separado) | Bajo (PEN) | Medio | Alto (IMD + cableado) |
| Riesgo de PEN roto | No aplica | **Alto** (tensión en masas si PEN rompe) | No aplica | No aplica |
| Uso en España BT pública | Excepcional | No permitido | **Estándar** | Hospitales, industria crítica |
| Limitación de Zs | Sí, crítica en longitudes largas | Sí | No (la da Ra × IΔn) | No aplica en 1ª falta |
| IMD requerido | No | No | No | **Obligatorio** |

**Regla práctica para selección en obra:**

1. **Instalación doméstica o edificio de viviendas** → **TT** con diferencial 30 mA en cada circuito terminal (REBT ITC-BT-25).
2. **Instalación industrial con transformador propio** → valorar **TN-S**: reduce la corriente diferencial de fuga en VFDs (evita falsas actuaciones del RCD) y permite selectividad amperimétrica pura. Verificar siempre Zs ≤ U0/Ia en cada circuito.
3. **Proceso crítico con prohibición de parada** → **IT** con IMD calibrado al Riso mínimo de la red, protocolo documentado de respuesta a primera falta (máximo 2 horas según IEC 60364-7-710 para localizar la falta).
4. **TN-C**: obsoleto para instalaciones nuevas. Prohibido en España para circuitos terminales desde REBT 2002. No usar en entornos con cargas electrónicas (desequilibrios en PEN crean tensiones peligrosas).

---

## Verificación en obra: medición de Zs con bucle de tierra

La medición práctica de Zs se realiza con un telurórnetro de bucle (instrumento de medida de impedancia de lazo, IEC 61557-3) sin desconectar la instalación. El instrumento inyecta una corriente de prueba y mide la caída de tensión. Valores de referencia:

- Zs medido ≤ 0,8 × (U0 / Ia): margen del 20 % para degradación térmica y tolerancias de fabricación del dispositivo de protección.
- Si Zs medido > U0 / Ia: el circuito no cumple IEC 60364-4-41. Soluciones: aumentar sección del PE, reducir longitud del circuito, o instalar un RCD adicional.

La medición se hace con la instalación energizada (tensión de red presente). En esquema TT, la medición de Ra se realiza con el método de tres electrodos (IEC 61557-5), desconectado de la red.

---

## Conclusión

El técnico que diseña o verifica una instalación de BT necesita saber qué sistema de tierras determina el protocolo de protección y qué cálculo lo valida. En TN, la ecuación Zs ≤ U0/Ia es el criterio de éxito: un circuito largo con sección pequeña puede no cumplirla aunque el magnetotérmico sea del calibre correcto para sobrecargas. En TT, Ra × IΔn ≤ UL traslada la garantía de protección al diferencial, independizándola de la impedancia de bucle. En IT, el IMD es la primera línea de defensa y la segunda falta debe tratarse con la misma urgencia que una falta en TN.

Los valores numéricos de este artículo son coherentes con los parámetros de resistividad del cobre (IEC 60228), los factores de corrección por temperatura de UNE-HD 60364-5-52 y los datos de capacitancia de la base GElectrical/IEC.
