---
title: "Transformadores de corriente de protección: clases 5P, 10P y PX (IEC 61869-2)"
description: "Guía técnica de transformadores de corriente para protección: clases P, PR, PX, TPX según IEC 61869-2, ALF, burden y dimensionamiento para relés de 87T, 50/51 y 21."
pubDate: 2026-10-15
keywords: ["transformador corriente proteccion clase P PX IEC 61869-2", "5P20 10P20 ALF TC proteccion", "dimensionamiento TC relee diferencial", "clase PX TPX TC proteccion MT"]
author: "Editor"
---

Un transformador de corriente (TC) de protección tiene una misión diferente a uno de medida: debe mantener suficiente linealidad durante una falta —cuando la corriente primaria supera en 5 a 30 veces la corriente nominal— para que el relé cuantifique correctamente la magnitud y tome la decisión de disparo o bloqueo. Dimensionarlo mal genera disparos intempestivos por saturación asimétrica o, peor, la no-actuación de una protección diferencial durante una falta interna.

IEC 61869-2 (edición 2012, bajo revisión activa) normaliza las clases de precisión para protección, define los parámetros que deben aparecer en la placa de características y establece los ensayos de tipo. Esta guía aplica directamente al dimensionamiento de TC en instalaciones de media y alta tensión cuando se especifican o verifican los equipos.

---

## Clases de protección según IEC 61869-2

IEC 61869-2 define las siguientes clases para núcleos de protección. Son mutuamente excluyentes: cada núcleo del TC pertenece a una sola clase.

| Clase | Error compuesto límite | Remanencia | Comportamiento transitorio | Aplicación típica |
|-------|----------------------|------------|---------------------------|-------------------|
| 5P    | 5 % a corriente límite | Sin límite | No especificado | Sobreintensidad (50/51), distancia (21) |
| 10P   | 10 % a corriente límite | Sin límite | No especificado | Sobreintensidad en sistemas menos críticos |
| PR    | 5 % a corriente límite | ≤10 % de Bsat | No especificado | Diferencial cuando se exige baja remanencia |
| PX    | Definido por Vk y Rct | Sin límite | No especificado | Diferencial de transformador/barras (87T, 87B) |
| TPX   | Error de relación ≤1 % en régimen transitorio | Sin remanencia | Hasta corriente límite transitoria | Protección diferencial con cálculo transitorio |
| TPY   | Error de relación ≤1 % | ≤10 % | Sí | Diferencial de alta velocidad |
| TPZ   | Error de ángulo de fase ≤18 min | Sin remanencia | Solo falta sin componente DC | Distancia en sistemas rápidos |

**Diferencia clave entre P y PX:** la clase P se verifica mediante el error compuesto (relación de amplitud más ángulo de fase combinados) a la corriente primaria límite de precisión. La clase PX se verifica directamente mediante la tensión de codo V_k y la resistencia de devanado secundario R_ct, sin requisito explícito de error compuesto. Esto permite al diseñador del relé calcular con exactitud el margen de saturación.

---

## Parámetros de placa y marcado

Un TC de protección clase P se marca así en su placa (IEC 61869-2 cláusula 5.6):

```
400/5 A — 15 VA — 5P20 — Clase 0,5/5P20
```

Desglose:
- **400/5 A**: corriente primaria nominal / corriente secundaria nominal
- **15 VA**: potencia aparente nominal al burden nominal
- **5P20**: clase 5P con factor límite de precisión (ALF) = 20
- **Clase 0,5/5P20**: el mismo núcleo tiene dos devanados secundarios (uno 0,5 para medida, uno 5P20 para protección). En la práctica cada aplicación debe usar su núcleo correspondiente.

Para un TC clase PX la placa incluye:
- V_k (tensión de codo, mínima garantizada, en V)
- R_ct (resistencia de devanado secundario a 75 °C, en Ω)
- I_e a V_k/2 o a V_k (corriente de magnetización, en mA)
- Cociente de turns N (o error de relación máximo en %)

Ejemplo de placa PX:
```
1000/1 A — Clase PX — Vk ≥ 200 V — Rct ≤ 3,5 Ω — Ie(Vk) ≤ 30 mA
```

---

## Factor límite de precisión (ALF): definición y ALF efectivo

El ALF nominal (K_n) es la relación entre la corriente primaria límite de precisión I_PA y la corriente nominal primaria I_PR, evaluado a la potencia aparente nominal:

```
K_n = I_PA / I_PR
```

Valores normalizados de ALF según IEC 61869-2: **5, 10, 15, 20, 30**.

El ALF nominal se cumple a la carga secundaria nominal. Cuando la carga real difiere, el ALF efectivo cambia. La expresión de corrección es:

```
K_eff = K_n × (R_ct + Z_N) / (R_ct + Z_A)
```

Donde:
- R_ct: resistencia del devanado secundario del TC (Ω)
- Z_N: impedancia de carga secundaria nominal (Ω), Z_N = S_N / I²_s
- Z_A: impedancia de carga secundaria real en servicio (Ω)

**Ejemplo numérico:**
- TC: 200/5 A, 15 VA 5P20, R_ct = 0,4 Ω
- Z_N = 15 VA / 5² A² = 0,6 Ω
- Carga real: relé 5 VA + cable 3 VA → Z_A = 8 VA / 25 = 0,32 Ω

```
K_eff = 20 × (0,4 + 0,6) / (0,4 + 0,32) = 20 × 1,0 / 0,72 = 27,8
```

Con carga real inferior a la nominal, el ALF efectivo sube a 27,8 —lo que significa que el TC mantiene el error compuesto ≤5 % hasta 27,8 × 200 A = 5.560 A primarios. Si la corriente de cortocircuito máxima en ese punto es 4.000 A (20 × I_N), el TC no satura. Si la corriente de falta máxima es 8.000 A (40 × I_N), el TC saturará durante la falta.

---

## Criterios de selección por tipo de protección

### Relés de sobreintensidad temporizada (50N, 51, 51N)

- Clase **5P** o **10P** es suficiente para protecciones de sobreintensidad no-unitarias.
- Verificar que K_eff ≥ I_falta_max / I_N_TC en el punto más cercano al TC.
- Para protecciones de tierra de alta sensibilidad (In ajuste 5–10 % de I_N), considerar el error de ángulo de fase: 5P (≤60 minutos) es mejor que 10P (sin límite de ángulo).

### Relés de distancia (21)

- Clase **5P** con ALF suficiente para la zona de alcance máximo.
- IEC 60255-121 exige que el TC no sature durante al menos la mitad del tiempo de operación del relé para la falta más cercana (típicamente 30–60 ms).
- Para distancia con señal de tele-disparo (permisive overreach, POTT), la exigencia de precisión transitoria puede requerir clase **5P** con ALF ≥ 20 o clase **TPX** si el tiempo de operación es <20 ms.

### Protección diferencial de transformador (87T) y diferencial de barras (87B)

- Clase **PX** o **TPX** obligatoria cuando se utiliza relé numérico con algoritmo diferencial de porcentaje.
- Los fabricantes de relés (ABB, Siemens, GE, SEL) especifican V_k mínima en función de la corriente de falta, la resistencia de los cables secundarios R_L y la carga del relé:

```
Vk_min = K_s × I_falta_max / I_N_secundario × (R_ct + 2 × R_L + Z_relé)
```

Donde K_s es un factor de sobredimensionamiento que varía entre 2 y 4 según el algoritmo del relé.

**Ejemplo para 87T:**
- Transformador 630 kVA, 20/0,4 kV, I_N_lado_AT = 18,2 A, I²_AT = 315 A (impedancia red + Ucc = 6 %)
- TC lado AT: 25/1 A, clase PX
- R_L (cable secundario hasta panel) = 0,8 Ω; Z_relé = 0,05 Ω; R_ct = 2,1 Ω
- I_falta_max en el TC = 315 A → I_s_falta = 315 × 1/25 = 12,6 A

```
Vk_min = 2 × 12,6 × (2,1 + 2×0,8 + 0,05) = 2 × 12,6 × 3,75 = 94,5 V
```

Se especifica TC PX con V_k ≥ 100 V (margen sobre 94,5 V), R_ct ≤ 2,1 Ω.

### Diferencial de generador (87G)

- La presencia de componente DC elevada en la corriente de falta exige clase **TPX** o **TPY** para evitar saturación asimétrica.
- La constante de tiempo del cortocircuito τ = X/ωR del sistema determina el factor DC: K_DC = 1 + ω·τ. Para un generador de 10 MVA con τ = 80 ms:

```
K_DC = 1 + 2π × 50 × 0,08 = 1 + 25,1 = 26,1
```

El ALF transitorio requerido supera en más de 26 veces al requerido para el régimen permanente. La clase TPX define el factor límite de precisión transitoria I_ALprim / I_PR considerando la curva de histéresis.

---

## Verificación de la carga secundaria total

El burden total de un circuito secundario de TC de protección incluye:
1. **R_cable**: resistencia de los conductores secundarios (ida + vuelta). Para cables de 2,5 mm² a 15 m de distancia: R ≈ 2 × 15 × 0,0075 Ω/m = 0,225 Ω
2. **Z_relé**: impedancia de la entrada de corriente del relé. Los relés numéricos modernos son de baja impedancia (0,005–0,1 Ω); los relés electromecánicos de sobreintensidad pueden presentar 0,5–2 Ω a plena carga
3. **R_bornes y conexiones**: ≈0,05 Ω (estimación típica)

**Regla práctica:** el burden total nunca debe superar el burden nominal del TC si se quiere mantener el ALF nominal. Si el burden real supera el nominal, el TC se satura a menor corriente primaria —lo que implica que el relé puede ver una señal incorrecta precisamente cuando más la necesita.

---

## Selección rápida en campo: tabla de decisión

| Función de protección | Clase mínima | ALF mínimo | Observaciones |
|----------------------|-------------|------------|--------------|
| Sobreintensidad (51) | 5P o 10P | 10–20 | 5P para relés con ajuste de temporización en zona de transición |
| Sobreintensidad tierra (51N) | 5P | 10–20 | Verificar ángulo de fase si ajuste <10 % I_N |
| Distancia (21) zona 1 | 5P | 20–30 | Evaluar K_DC para faltas cercanas con τ elevado |
| Diferencial transformador (87T) | PX o TPX | Vk según cálculo | Siempre verificar Vk_min con datos del relé |
| Diferencial barras (87B) | PX o TPX | Vk según cálculo | I_falta_max puede ser muy alta; conductor sec. debe ser 4–6 mm² |
| Diferencial generador (87G) | TPX o TPY | Cálculo transitorio | K_DC puede requerir Vk > 500 V |
| Protección de distancia rápida (POTT) | 5P o TPX | 20–30 | Tiempo de operación < 20 ms → considerar TPX |

---

## Conclusión

Especificar correctamente un TC de protección exige conocer tres datos del sistema: la corriente de falta máxima en el punto de instalación, la carga total del circuito secundario y el tipo de protección que lo utiliza. Con esos datos, IEC 61869-2 ofrece el marco para calcular el ALF efectivo (clases P) o la tensión de codo mínima (clases PX), y para elegir si el comportamiento transitorio requiere clase TPX o TPY.

En obra, el error más frecuente es reutilizar núcleos de medida (clase 0,2S o 0,5) para protección en instalaciones renovadas. Un núcleo de medida está diseñado para saturar a baja corriente y proteger los instrumentos conectados; en una protección, esa saturación temprana anula la capacidad del relé para actuar en falta. La separación física de núcleos de medida y protección, exigida por IEC 61869-2 para relaciones de transformación críticas, es irrenunciable.
