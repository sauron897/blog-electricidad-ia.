---
title: "Selectividad diferencial tipo S: coordinación de protecciones en BT"
description: "Cómo coordinar interruptores diferenciales tipo S, G, A y AC en instalaciones BT. Criterios de selectividad amperimétrica y cronométrica según IEC 61008-1 e ITC-BT-24."
pubDate: 2026-08-02
keywords: ["selectividad diferencial tipo S", "coordinacion protecciones diferencial", "diferencial tipo S tipo G IEC 61008", "selectividad amperimetrica cronometrica", "ITC-BT-24 diferencial selectivo"]
author: "Editor"
---

Cuando un diferencial general dispara antes que el diferencial de circuito que tendría que haber actuado, hay un fallo de coordinación. El resultado práctico: corte total de la instalación en vez de un corte selectivo del circuito afectado. En instalaciones con varios niveles de protección diferencial —cuadro general, subcuadros, circuitos terminales— la selectividad no es opcional; es un requisito de diseño que la norma **IEC 61008-1** y la **ITC-BT-24 del REBT** exigen cumplir.

Este artículo desarrolla los mecanismos de selectividad diferencial, los tipos de dispositivos implicados, los valores numéricos que gobiernan la coordinación y el procedimiento de selección aplicable en obra.

---

## Clasificación de interruptores diferenciales según IEC 61008-1

La norma **IEC 61008-1** (*Residual current operated circuit-breakers without integral overcurrent protection for household and similar uses*) y su equivalente **UNE-EN 61008-1** clasifican los IDs según el tipo de corriente de defecto que son capaces de detectar:

| Tipo | Corrientes de defecto detectadas | Aplicación típica |
|------|----------------------------------|-------------------|
| **AC** | Corriente alterna sinusoidal | Circuitos resistivos, iluminación convencional |
| **A** | CA sinusoidal + CC pulsante (semiondasrectificadas) | Cargas con rectificadores monofásicos |
| **F** | CA + CC pulsante + CC superpuesta hasta 10 mA | Variadores monofásicos, electrodomésticos clase II |
| **B** | CA + CC pulsante + CC pura + altas frecuencias | Variadores trifásicos, vehículo eléctrico (ITC-BT-52) |
| **S** | CA sinusoidal, con retardo de disparo intencional | Diferencial de cabecera para selectividad cronométrica |
| **G** | CA sinusoidal, con retardo reducido | Nivel intermedio de selectividad |

El tipo **S** (*Selective*) y el tipo **G** (*General*) no describen una diferente capacidad de detección de corriente de falta, sino un régimen de tiempo de respuesta distinto que permite la coordinación cronométrica entre niveles.

---

## Parámetros de tiempo según IEC 61008-1 y IEC 61009-1

La norma define dos ensayos críticos de tiempo de actuación para los diferenciales:

**t₁ — Tiempo de no actuación mínimo (t_na)**: el dispositivo no debe disparar antes de este tiempo ante una corriente de defecto igual a I∆n. Es la "ventana de espera" que permite al diferencial aguas abajo actuar primero.

**t₂ — Tiempo de actuación máximo (t_a)**: el dispositivo debe haber disparado dentro de este tiempo ante 5·I∆n. Es el límite superior de actuación para garantizar protección de personas.

| Tipo | t_na a I∆n | t_a a I∆n | t_na a 2·I∆n | t_a a 5·I∆n |
|------|-----------|-----------|--------------|-------------|
| General (AC, A, F, B) | — | 300 ms | — | 40 ms |
| **S (selectivo)** | **130 ms** | **500 ms** | **60 ms** | **200 ms** |
| **G (general retardado)** | **10 ms** | **300 ms** | **5 ms** | **150 ms** |

Los valores son los máximos normalizados. Un diferencial tipo S tiene garantizado que no dispara antes de 130 ms a corriente I∆n, lo que da tiempo suficiente al diferencial aguas abajo (de tipo general, tiempo de actuación < 300 ms a I∆n) para actuar primero y abrir solo su circuito.

---

## Mecanismos de selectividad diferencial

Existen dos métodos de selectividad que pueden aplicarse de forma independiente o combinada:

### Selectividad amperimétrica (por sensibilidad)

Se basa en escalonar los valores de corriente de defecto nominal (I∆n) entre niveles. La regla práctica:

> **I∆n aguas arriba ≥ 3 × I∆n aguas abajo**

Ejemplo: si el circuito terminal lleva un diferencial de 30 mA, el subcuadro que lo alimenta debe tener uno de al menos 100 mA, y el cuadro general, uno de al menos 300 mA.

La relación de 3:1 no está explícita en IEC 61008-1 como valor único, pero deriva de la tolerancia de fabricación de I∆n (que puede ser hasta 1,5·I∆n como máximo de actuación real) y de las corrientes de fuga capacitiva acumuladas en la instalación. Con factor 3, se garantiza que ante una corriente de defecto que activa el diferencial aguas abajo (entre I∆n y 1,5·I∆n), el de aguas arriba no ha alcanzado su umbral mínimo de disparo.

**Limitación**: la selectividad amperimétrica no garantiza selectividad cronométrica. Ante una corriente de defecto alta (por ejemplo, 5·I∆n del diferencial de cabecera), ambos diferenciales intentarán disparar, y el de cabecera puede ganar si es más rápido.

### Selectividad cronométrica (por tiempo)

Consiste en instalar un diferencial tipo **S** o **G** en la cabecera, con retardo garantizado, mientras los circuitos terminales llevan diferenciales instantáneos. Ante cualquier nivel de corriente de defecto, el de cabecera espera al menos 130 ms (tipo S) antes de actuar, tiempo suficiente para que el diferencial aguas abajo, sin retardo, haya disparado.

**Condición de coordinación**:

```
t_na (aguas arriba) > t_a_máx (aguas abajo)
130 ms > 300 ms  →  NO cumple directamente
```

Aquí entra el escalonamiento real: el diferencial aguas abajo, de tipo general, tiene tiempo de actuación típico entre 10 y 100 ms (no 300 ms, que es el máximo normativo). En la práctica, con un tipo S en cabecera y un tipo AC/A en circuito, la discriminación es efectiva. Para instalaciones críticas donde se necesita certeza, se combinan ambos métodos: relación de sensibilidad 3:1 y diferencial S en cabecera.

---

## Aplicación práctica: esquema de tres niveles

Un esquema típico en instalación terciaria o industrial de baja tensión:

```
[Red BT 400/230 V]
       │
  [CGP + IGA]
       │
  ┌────┴────┐
  │  CGBT   │
  │  ID tipo S, 300 mA, 4P, 63 A  │  ← Cabecera: selectivo, retardo ≥130 ms
  └────┬────┘
       │
  ┌────┴─────────────────────┐
  │                          │
[Subcuadro 1]            [Subcuadro 2]
ID tipo A, 100 mA, 4P    ID tipo A, 100 mA, 4P   ← Nivel intermedio
  │                          │
[Circuitos terminales]   [Circuitos terminales]
ID tipo A, 30 mA, 2P     ID tipo A, 30 mA, 2P    ← Protección personal
```

Sensibilidades: 300 mA / 100 mA / 30 mA → ratio 3,3:1 entre niveles. Cronometría: tipo S en cabecera garantiza t_na ≥ 130 ms. Coordinación: doble (amperimétrica + cronométrica).

---

## Criterios de selección en obra

**1. Nivel de protección exigido por ITC-BT-24:**
- Locales con riesgo de contacto directo o entornos húmedos: I∆n ≤ 30 mA obligatorio en el diferencial del circuito terminal.
- Protección adicional en viviendas (ITC-BT-25): diferencial de 30 mA por circuito o grupo de circuitos.

**2. Tipo de carga:**
- Cargas puramente resistivas o inductivas (iluminación fluorescente convencional, calefacción): tipo AC suficiente.
- Cargas con rectificadores monofásicos (ordenadores, cargadores): tipo A mínimo.
- Variadores de frecuencia monofásicos: tipo F.
- Variadores trifásicos o cargadores de VE modo 3 (ITC-BT-52): tipo B obligatorio.

**3. Corrientes de fuga capacitiva acumuladas:**
Los cables XLPE generan corriente capacitiva de fuga proporcional a su longitud y sección. Con los datos de GElectrical (base de datos IEC), los cables XLPE de aluminio presentan capacitancias de 110–330 nF/km. En una instalación con 500 m de cable 3×95 mm² XLPE (C ≈ 290 nF/km):

```
I_fuga = V_fase × ω × C_total
I_fuga = 230 V × 2π × 50 Hz × (290×10⁻⁹ F/km × 0,5 km)
I_fuga ≈ 230 × 314 × 145×10⁻⁹ ≈ 10,5 mA
```

Esta corriente de fuga capacitiva suma en el diferencial de cabecera. Si la suma de fugas de todos los circuitos supera el umbral del diferencial general, habrá disparos intempestivos. Esto justifica usar I∆n de 300 mA en cabecera en instalaciones con cableado extenso o variadores.

**4. Compatibilidad con protecciones contra sobretensión (SPD):**
Según la norma **IEC 61643-12**, los varistores MOV de los limitadores de sobretensión pueden inyectar corriente impulsional durante una descarga atmosférica. Esta corriente puede provocar el disparo del diferencial si es de tipo AC (no inmunizado frente a impulsos). Se recomienda:
- Instalar el SPD aguas arriba del diferencial, o
- Usar un diferencial con inmunidad a impulsos certificada (marcado adicional), o
- Usar diferencial tipo S en el nivel donde está el SPD.

**5. Corriente de cortocircuito y coordinación con magnetotérmicos:**
El diferencial no protege frente a cortocircuitos (salvo el RCCB+MCB = RCBO, IEC 61009-1). Ante un cortocircuito aguas abajo, el magnetotérmico asociado debe abrir en tiempo < 10 ms (zona instantánea). El diferencial tipo S, con t_na ≥ 130 ms, no habrá actuado, lo que evita el doble disparo diferencial + magnetotérmico. Esta coordinación es intrínseca en diseños correctamente escalonados.

---

## Conclusión

La selectividad diferencial no se consigue por defecto: requiere definir explícitamente la jerarquía de sensibilidades (relación ≥3:1 entre niveles) y asignar tipo S o G a los diferenciales de cabecera para garantizar el retardo cronométrico. En instalaciones con variadores, vehículo eléctrico o cableado extenso, la elección del tipo correcto (F, B) y el cálculo de corriente de fuga capacitiva son imprescindibles para evitar disparos intempestivos. Los valores normalizados de IEC 61008-1 — t_na ≥ 130 ms para tipo S, ratio de sensibilidad ≥3:1 — son los parámetros de diseño concretos con los que trabajar, no reglas generales.
