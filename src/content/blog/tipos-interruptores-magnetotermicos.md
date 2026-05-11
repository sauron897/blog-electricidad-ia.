---
title: "Tipos de interruptores magnetotérmicos y cómo elegirlos"
description: "Guía técnica completa sobre curvas de disparo B, C y D, calibre, poder de corte y coordinación con conductores según ITC-BT-22. Con tabla comparativa y ejemplo de selección."
pubDate: 2026-05-11
keywords: ["interruptores magnetotermicos tipos", "curva B C D magnetotermico", "calibre magnetotermico como elegir", "ITC-BT-22 proteccion sobreintensidades", "poder de corte magnetotermico"]
heroImage: /images/tipos-interruptores-magnetotermicos.svg
author: "Editor"
---

El interruptor magnetotérmico —también llamado PIA (Pequeño Interruptor Automático) o automático— es el dispositivo de protección más usado en instalaciones eléctricas de baja tensión. Sin embargo, elegirlo correctamente no es trivial: una curva equivocada provoca disparos intempestivos en arranques de motor, un calibre sobredimensionado deja sin protección al cable, y un poder de corte insuficiente puede resultar en un arco eléctrico destructivo ante un cortocircuito.

Este artículo cubre el funcionamiento, los tipos de curva, y el procedimiento de selección completo según **ITC-BT-22** del REBT.

## Principio de funcionamiento: dos mecanismos de disparo

El magnetotérmico combina dos protecciones independientes en un mismo dispositivo:

**Protección térmica (elemento bimetálico)**: protege frente a sobrecargas. Una lámina bimetálica se calienta con la corriente y se curva cuando supera cierto umbral durante un tiempo suficiente. Es una protección de tiempo inverso: cuanto mayor es la sobrecorriente, más rápido dispara. Su respuesta es lenta (segundos a minutos), lo que permite aguantar picos transitorios sin interrumpir el circuito.

**Protección magnética (electroimán)**: protege frente a cortocircuitos. Un electroimán actúa instantáneamente cuando la corriente supera un múltiplo de In. La respuesta es prácticamente instantánea (< 20 ms), antes de que la energía del cortocircuito dañe el conductor o los equipos.

La **curva de disparo** define el umbral magnético (la zona de disparo instantáneo) y determina para qué tipo de carga resulta adecuado el magnetotérmico.

---

## Curvas de disparo: B, C y D

La norma **IEC 60898-1** (adoptada como UNE-EN 60898-1) define las curvas de disparo estándar. El parámetro clave es el **rango de disparo magnético**, expresado como múltiplo de la corriente nominal In:

| Curva | Disparo magnético (instantáneo) | Aplicación típica |
|:---:|:---:|---|
| **B** | 3 × In — 5 × In | Circuitos resistivos, alumbrado, líneas largas con baja Icc |
| **C** | 5 × In — 10 × In | Uso general: tomas de corriente, circuitos mixtos, pequeños motores |
| **D** | 10 × In — 20 × In | Cargas con elevada corriente de arranque: motores, transformadores, electroimanes |

La protección térmica (sobrecarga) es equivalente en las tres curvas: el magnetotérmico no dispara por debajo de 1,13 × In en tiempo indefinido y dispara en menos de 1 hora con 1,45 × In.

### Curva B — circuitos sensibles y líneas largas

La curva B dispara instantáneamente con corrientes de 3 a 5 veces In. Esta sensibilidad alta es apropiada cuando:

- La **Icc en el punto de instalación es baja** (extremo de una línea larga, instalaciones rurales o industriales alejadas del transformador). Con una Icc reducida, necesitamos un umbral magnético bajo para que el disparo se produzca dentro del tiempo de protección contra cortocircuito.
- Las cargas son puramente **resistivas o inductivas de bajo arranque**: resistencias eléctricas, alumbrado fluorescente o LED, circuitos de señalización.
- Se requiere protección de personas: circuitos de **VLTS** (muy baja tensión de seguridad) o instalaciones con mayor riesgo de contacto.

**Error frecuente con curva B**: instalarlo en un circuito con pequeño motor o arrancador electrónico. La corriente de arranque (generalmente 5–8 × In) puede cruzar el umbral magnético y provocar disparos en cada arranque.

### Curva C — uso general

Es la curva estándar para la mayoría de instalaciones domésticas e industriales de uso general. El umbral magnético de 5 a 10 × In tolera:

- Corrientes transitorias de **arranque de pequeños motores** (ventiladores, bombas monofásicas de hasta 2–3 kW)
- Picos de **corriente de magnetización** de transformadores pequeños
- **Corriente de irrupción** de lámparas incandescentes (aunque cada vez menos frecuente)

Es el tipo correcto para proteger **circuitos de tomas de uso general**, circuitos de alumbrado con cargas mixtas, y líneas que alimentan cuadros secundarios con cargas variadas.

### Curva D — motores y cargas inductivas pesadas

El umbral de 10 a 20 × In permite aguantar las corrientes de arranque directo de motores trifásicos (generalmente 5–8 × In de corriente a plena carga, pero el pico inicial puede llegar a 10–12 × In en los primeros ciclos). También es adecuada para:

- **Transformadores de alta potencia**: la corriente de magnetización en el encendido puede alcanzar 10–15 × In durante decenas de milisegundos
- **Electroimanes y solenoides**: pico de corriente al activarse
- **Grupos de UPS** y rectificadores con condensadores de filtrado: alta corriente de carga inicial

Con curva D, la protección frente a cortocircuito sigue garantizada (dispara por debajo de 20 × In), pero el umbral alto exige verificar que la **Icc mínima** en el punto de instalación supere ese valor. Si no, ante un cortocircuito de alta impedancia, la protección magnética no actuaría y solo lo haría el térmico —inaceptablemente lento para un cortocircuito real.

---

## Otros parámetros de selección

### Corriente nominal (In)

El calibre In del magnetotérmico debe cumplir simultáneamente dos condiciones según **ITC-BT-22**:

```
Ib ≤ In ≤ Iz
```

Donde:
- **Ib** = corriente de diseño del circuito (corriente de servicio)
- **Iz** = intensidad máxima admisible del conductor en sus condiciones reales (con factores de corrección)

Esto significa que el calibre no puede ser inferior a la corriente de servicio (no protegería la carga) ni superior a la capacidad del cable (dejaría el conductor sin protección térmica).

La condición adicional de disparo térmico es:

```
I₂ ≤ 1,45 × Iz
```

Donde I₂ es la corriente de disparo garantizada en 1 hora (= 1,45 × In para magnetotérmicos conformes a IEC 60898). Esta condición se cumple automáticamente cuando In ≤ Iz para dispositivos normalizados.

### Poder de corte (Icu / Ics)

El poder de corte es la **corriente de cortocircuito máxima** que el magnetotérmico puede interrumpir sin destruirse. Se expresa en kA (kiloamperios de valor eficaz simétrico). Hay dos valores:

- **Icu** (poder de corte último): máxima corriente que puede interrumpir, tras lo cual el dispositivo puede no ser apto para servicio continuado.
- **Ics** (poder de corte en servicio): corriente que puede interrumpir manteniéndose operativo para rearme inmediato. Suele ser el 50–75 % del Icu.

La **IEC 60898-1** define clases de poder de corte:

| Clase | Icu mínimo |
|:---:|:---:|
| 1500 | 1,5 kA |
| 3000 | 3 kA |
| 4500 | 4,5 kA |
| 6000 | 6 kA |
| 10000 | 10 kA |
| 15000 | 15 kA |
| 20000 | 20 kA |
| 25000 | 25 kA |

El magnetotérmico instalado debe tener un **Icu ≥ Icc máxima en el punto de instalación**. En instalaciones domésticas con transformador de 250 kVA a distancia media, la Icc en el cuadro general puede estar entre 3 y 6 kA. En cabeceras de cuadro industrial próximas al transformador, puede superar los 15–20 kA.

Instalar un magnetotérmico con Icu insuficiente es una de las infracciones más peligrosas: ante un cortocircuito grave, el dispositivo explota sin cortar la corriente, con riesgo de incendio y electrocución.

### Número de polos

| Aplicación | Polos recomendados |
|---|:---:|
| Circuito monofásico (fase + neutro) | 1P o 1P+N (corta fase; neutro fijo o seccionable) |
| Circuito monofásico con neutro seccionable | 2P |
| Circuito trifásico sin neutro | 3P |
| Circuito trifásico con neutro | 4P o 3P+N |

En instalaciones con **esquema TT** (habitual en España), el neutro está puesto a tierra en el transformador. ITC-BT-08 no obliga a cortar el neutro en protecciones de circuito, pero sí es obligatorio cortarlo en el **interruptor general** (IGA) y recomendable en circuitos donde el neutro puede estar bajo tensión por desequilibrio o fallo.

### Clase de limitación de energía

Los magnetotérmicos conformes a IEC 60898-1 se clasifican también por su capacidad limitadora de la corriente de cortocircuito:

- **Clase 1**: no limita (deja pasar la onda completa)
- **Clase 2**: limitación moderada
- **Clase 3**: alta limitación — corta antes de que la corriente alcance su cresta

Los dispositivos de clase 3 (los más habituales en gamas residencial y terciario actuales) protegen mejor los equipos aguas abajo, ya que reducen la energía específica pasante (I²·t) que llega al circuito.

---

## Procedimiento de selección: ejemplo numérico

![Guía de selección de interruptor magnetotérmico](/images/tipos-interruptores-magnetotermicos-2.png)

**Datos del circuito:**
- Motor trifásico 400 V, 7,5 kW, cosφ = 0,86, rendimiento η = 0,91, arranque directo
- Longitud de línea: 20 m, cable Cu XLPE tripolar en tubo empotrado (método B2)
- Temperatura ambiente: 40 °C, 1 solo circuito (ka = 1,00)
- Icc en el cuadro de alimentación: 8 kA

**Paso 1 — Corriente de servicio:**

```
Ib = P / (√3 × U × cosφ × η) = 7500 / (1,732 × 400 × 0,86 × 0,91) = 15,5 A
```

**Paso 2 — Sección del cable (criterio térmico):**

Con XLPE tripolar en tubo (método B2), a 40 °C (kt = 1,00), 1 circuito (ka = 1,00):
- 2,5 mm² → Iz = 21 A ✓ (21 ≥ 15,5 A)

Sección elegida: **2,5 mm² Cu XLPE**, Iz = 21 A.

**Paso 3 — Calibre del magnetotérmico:**

Condición ITC-BT-22: Ib ≤ In ≤ Iz → **15,5 A ≤ In ≤ 21 A**

Calibre comercial válido: **In = 16 A** ✓

**Paso 4 — Curva de disparo:**

Motor de arranque directo: corriente de arranque ≈ 6–7 × Ib = 6 × 15,5 = 93 A ≈ 6 × In.

- Curva B: disparo a 3–5 × In = 48–80 A → **disparo en arranque** ✗
- Curva C: disparo a 5–10 × In = 80–160 A → arranque en zona límite, posible disparo ✗
- **Curva D**: disparo a 10–20 × In = 160–320 A → tolerará el arranque ✓

**Curva elegida: D**. Verificación: Icc mínima en el punto más alejado (20 m de 2,5 mm²):

```
Icc_min ≈ 0,8 × U / (2 × ρ × L / S) = 0,8 × 230 / (2 × 0,0225 × 20 / 2,5) ≈ 1.022 A ≈ 1 kA
```

1 kA > 20 × In = 320 A → la protección magnética actuará ante cualquier cortocircuito en la línea. ✓

**Paso 5 — Poder de corte:**

Icc en el cuadro = 8 kA → elegir magnetotérmico con **Icu ≥ 10 kA** (clase 10000).

**Resultado**: PIA trifásico **3P, 16 A, curva D, Icu = 10 kA**.

---

## Errores frecuentes en la selección

**Usar curva C en todos los circuitos**: el error más habitual en instalaciones industriales. Basta con un motor de cierta potencia para que el arranque dispare el magnetotérmico, obligando a sustituirlo por uno de curva D.

**Sobredimensionar el calibre para "dar margen"**: instalar un PIA de 25 A en un circuito cuyo cable admite solo 18 A (Iz del cable con sus factores de corrección) deja el conductor sin protección térmica. El magnetotérmico solo disparará cuando la corriente supere 1,45 × 25 = 36 A, mucho más que los 18 A que el cable puede soportar de forma continuada.

**Ignorar el poder de corte**: en instalaciones industriales próximas al transformador, la Icc puede superar los 10–15 kA. Instalar magnetotérmicos domésticos (Icu = 4,5 o 6 kA) en esos cuadros es una infracción grave del REBT y un riesgo real de explosión.

**Confundir PIA con IGA**: el Interruptor General Automático (IGA) de la instalación debe ser capaz de cortar **toda** la corriente de la instalación (suma de todos los circuitos) y cumplir con la selectividad frente a los PIAs de circuito. Un PIA convencional usado como IGA no garantiza esa función.

## Normativa de referencia

- **IEC 60898-1 / UNE-EN 60898-1**: Interruptores automáticos para instalaciones domésticas y análogas para la protección contra sobreintensidades
- **REBT ITC-BT-22**: Instalaciones interiores — protección contra sobreintensidades
- **IEC 60364-4-43**: Protección contra sobreintensidades (coordinación con conductores)
- **IEC 60947-2**: Interruptores automáticos para uso industrial (MCCB/ACB)
