---
title: "Arrancadores suaves y variadores IE3: IEC 60947-4-2"
description: "Criterios técnicos para elegir entre arrancador suave y variador de frecuencia en motores IE3. Corrientes de arranque, IEC 60947-4-2, torques y coordinación de protecciones en BT industrial."
pubDate: 2026-10-05
keywords: ["arrancador suave variador frecuencia IE3 seleccion IEC 60947-4-2", "soft starter IE3", "variador frecuencia motor IE3", "IEC 60947-4-2 seleccion", "arranque motor IE3 industrial"]
author: "Editor"
---

## Corriente de arranque en motores IE3: el problema de partida

Un motor trifásico de jaula de ardilla en arranque directo (DOL) absorbe una corriente de arranque (Ia) que, según la base de datos IEC / GElectrical y **IEC 60034-30-1**, alcanza entre 7 y 7,7 veces la corriente nominal (In) en motores IE3 (Premium Efficiency). El factor k de la norma para IE3 es 7,7 desde 2,2 kW en adelante:

| Potencia (kW) | Clase | In a 400 V (A) | k (Ia/In) | Ia DOL (A) | η (%) | cos φ |
|---------------|-------|----------------|-----------|------------|-------|-------|
| 7,5           | IE3   | 15,2           | 7,7       | 117        | 90,1  | 0,85  |
| 11            | IE3   | 22,1           | 7,7       | 170        | 91,2  | 0,90  |
| 22            | IE3   | 43,0           | 7,7       | 331        | 92,7  | 0,90  |
| 37            | IE3   | 71,5           | 7,7       | 550        | 93,7  | 0,90  |
| 75            | IE3   | 143,4          | 7,7       | 1.104      | 94,7  | 0,90  |

*Fuente: GElectrical / IEC 60034. In calculado como P/(√3 × 400 V × η × cos φ).*

Esta corriente genera dos efectos simultáneos: caída de tensión en la red (≥ 15% en instalaciones con Zred alta) y par de impacto mecánico que puede dañar acoplamientos, reductores y tuberías. La **ITC-BT-47 del REBT** exige limitar estas perturbaciones en función de la potencia y de la potencia de cortocircuito disponible en el punto de conexión.

La solución es un dispositivo de arranque controlado: **arrancador suave** o **variador de frecuencia**. La elección entre ambos no es de preferencia, es de ingeniería de la carga.

---

## Arrancadores suaves según IEC 60947-4-2

Un arrancador suave controla la tensión aplicada al motor durante el arranque mediante tiristores (SCR) en antiparalelo en las tres fases. Reduce la tensión inicial a un valor configurable (típicamente 30–50% × Un) y la eleva en rampa hasta Un en un tiempo ajustable (2–30 s). La norma de referencia es **IEC 60947-4-2** (*Aparamenta de BT – Arrancadores electrónicos para motores de CA*), que define:

- **Categorías de utilización AC-53a / AC-53b**: AC-53a indica funcionamiento continuo sin bypass; AC-53b incorpora bypass mecánico que cortocircuita los tiristores tras el arranque, eliminando las pérdidas en conducción (≈ 3–5 W/A).
- La notación completa es AC-53a 3-3: 10-0,5-4 (ratio corriente 3×In, 3 arranques/hora, tiempo de arranque 10 s, ciclo de trabajo 0,5 h, reposo 4 h).
- **DPCC externo obligatorio**: el arrancador suave no interrumpe cortocircuitos; requiere fusible aM o MCCB aguas arriba con Icu ≥ Icc de la instalación.

### Reducción de Ia con arrancador suave

La corriente de arranque cae proporcional al cuadrado de la tensión aplicada:

**Ia_soft = k × (U₀/Un)² × In**

Para un motor IE3 de 22 kW (In = 43 A, k = 7,7) con tensión inicial U₀ = 0,4 × Un:
- DOL: Ia = 7,7 × 43 = **331 A**
- Soft starter: Ia = 7,7 × 0,4² × 43 = **53 A** (1,23 × In)

La penalización es inmediata: el par de arranque también cae al cuadrado de la tensión. A U₀ = 0,4 × Un, el par disponible es el 16% del par nominal. Esto hace inviable el arrancador suave en cargas con par resistente elevado desde la parada (elevadores, trituradoras, compresores de pistón con válvulas cargadas).

---

## Variadores de frecuencia: IEC 61800 y compatibilidad con IE3

Un variador de frecuencia (VFD) controla tensión y frecuencia simultáneamente manteniendo el flujo magnético constante (control V/f, vectorial o DTC). Durante el arranque aplica f ≈ 0 Hz y eleva progresivamente, permitiendo par nominal desde 0 Hz sin corriente de arranque elevada. Para el mismo motor IE3 de 22 kW:

- Ia_VFD ≈ **43–65 A** (1,0–1,5 × In configurable)

La serie normativa aplicable es **IEC 61800**:
- **IEC 61800-3**: requisitos EMC, emisiones armónicas y niveles de inmunidad. Define entornos C1–C4 y obliga a filtros de red en entornos residenciales (C1/C2).
- **IEC 61800-5-1**: seguridad eléctrica y mecánica del convertidor.
- **IEC 61800-5-2**: funciones de seguridad SIL 1–3 (parada segura, STO, SS1, SLS).
- **IEC 61800-9-2**: eficiencia del sistema convertidor + motor (clases de pérdidas IE0–IE3 del conjunto).

### Compatibilidad IE3 con convertidor: IEC 60034-25

Los motores IE3 operando con VFD presentan dos efectos críticos:

1. **Estrés del aislamiento por du/dt**: los flancos de conmutación IGBT generan tensiones pico en el bobinado que superan 2 × Un en cables de longitud > 20 m. **IEC 60034-25** define dos categorías: Categoría I (du/dt < 500 V/μs, Upico ≤ 850 V para motores de 400 V) y Categoría II (du/dt < 5.000 V/μs, Upico ≤ 1.600 V). Los motores IE3 de fabricantes principales están diseñados para Categoría I de serie; con inversores de alta frecuencia de conmutación o cables largos, se requiere filtro du/dt en la salida del variador.

2. **Corrientes de rodamiento**: la corriente de modo común del inversor puede circular por los rodamientos provocando electroerosión (marcas de corriente). Para motores > 11 kW se recomienda rodamiento no conductor (lado opuesto a carga) o anillo de puesta a tierra en el árbol con escobilla.

---

## Tabla comparativa: arrancador suave vs. variador de frecuencia

| Parámetro | Arrancador suave | Variador de frecuencia |
|-----------|-----------------|----------------------|
| Norma principal | IEC 60947-4-2 | IEC 61800-3 / 5-1 |
| Control de velocidad en régimen | No | Sí (0–150% fn) |
| Corriente de arranque | 1,2–2,5 × In | ≤ 1,0–1,5 × In |
| Par en arranque | Limitado (∝ U²) | Par nominal desde 0 Hz |
| Pérdidas en régimen (con bypass) | < 0,1% Pn | 2–4% Pn |
| Armónicos en la red | Solo durante arranque | Continuos: THD-I 30–100% sin filtro |
| Coste relativo (22 kW) | 1× | 3–5× |
| Freno controlado | Solo inserción resistiva | Regenerativo o resistivo configurable |
| Número de arranques/hora | ≤ 5–10 (AC-53b) | Sin límite térmico |
| Compatibilidad EMC REBT | Directa | Requiere filtros C2/C3 según IEC 61800-3 |

---

## Criterios de selección en instalación industrial

**Aplicar arrancador suave (IEC 60947-4-2) cuando:**
- La velocidad en régimen es siempre nominal (fn): bombas centrífugas a caudal fijo, compresores de tornillo, bandas transportadoras a velocidad constante.
- El par resistente en el arranque es bajo (< 30–40% Mn): la caída cuadrática del par no impide el arranque.
- El número de arranques/hora es ≤ 5–10 (verificar la categoría AC-53b para ciclos más exigentes).
- El presupuesto es el factor dominante: un soft starter de 22 kW representa 200–600 € frente a 800–2.500 € de un VFD equivalente.

**Aplicar variador de frecuencia cuando:**
- El proceso requiere velocidad variable: HVAC en lazo PID, bombas de presión variable, extrusoras, centros de mecanizado.
- La carga exige par elevado desde 0 Hz: elevadores, grúas, AGV, cintas de alta inercia con carga inicial.
- Se requiere frenado controlado: la deceleración en rampa evita golpes de ariete en tuberías sin válvula amortiguadora adicional.
- Se persigue ahorro energético por modulación de velocidad: la ley de similitud establece P ∝ n³; reducir la velocidad un 20% disminuye el consumo un 49%.

**Cálculo de ahorro energético con VFD en bomba IE3 de 22 kW:**
- A 80% de velocidad nominal: P = 0,8³ × 22 kW = **11,3 kW**
- Ahorro respecto a velocidad nominal: 48,5%
- En 4.000 h/año a 0,12 €/kWh: **ahorro ≈ 5.150 €/año** — el VFD se amortiza en < 1 año en este escenario

---

## Coordinación de protecciones con ITC-BT-47

La **ITC-BT-47 del REBT** exige protección contra sobrecarga, cortocircuito y fallo de fase para todo arrancador de motor. Con dispositivos electrónicos:

**Con arrancador suave**: el dispositivo integra protección de sobrecarga según IEC 60947-4-2 (clase 10 o clase 20 configurable). El DPCC externo (fusible aM o MCCB) debe coordinar con el relé integrado en tipo 2. La Icc que el DPCC debe cortar es la de la instalación: el arrancador suave no limita la corriente de cortocircuito — solo actúa sobre la tensión de alimentación en régimen de arranque.

**Con variador de frecuencia**: el cortocircuito en los bornes de salida del variador queda limitado por la impedancia del convertidor y dispara la protección interna de los IGBTs (por sobretemperatura o sobreintensidad). El DPCC aguas arriba del variador (lado red) debe dimensionarse para la Icc de la instalación en ese punto. La protección de sobrecarga del motor la gestiona el variador mediante modelo térmico electrónico (clase 10 configurable).

---

## Conclusión

Para motores IE3 en BT industrial, la elección entre arrancador suave y variador de frecuencia depende del perfil de velocidad del proceso y del par resistente en el arranque. El arrancador suave según IEC 60947-4-2 es la solución correcta para cargas a velocidad constante donde solo se necesita reducir la corriente de arranque de 7,7 × In a valores < 2 × In. El variador de frecuencia (IEC 61800-3/5-1) es obligatorio cuando el proceso requiere control de velocidad en régimen, par elevado desde parada o amortización por ahorro energético. Antes de especificar el variador, verificar la categoría de aislamiento del motor según IEC 60034-25 para evitar degradación prematura del bobinado en instalaciones con cables de longitud > 20 m.
