---
title: "Relés de frecuencia en sistemas insulares: IEC 60255-181"
description: "Ajuste de mínima frecuencia y ROCOF en sistemas insulares aislados. Funciones 81U, 81O y 81R según IEC 60255-181. Deslastre de cargas escalonado."
pubDate: 2026-10-31
keywords: ["rele frecuencia sistema insular IEC 60255-181", "proteccion subfrequencia ROCOF df/dt", "deslastre cargas UFLS sistema aislado", "ajuste rele frecuencia minima"]
author: "Editor"
---

## Contexto: por qué los sistemas insulares necesitan protección de frecuencia específica

En un sistema interconectado peninsular la inercia total del sistema —suma de la energía cinética de todos los generadores síncronos— amortigua los transitorios de frecuencia ante pérdidas de generación. En Canarias, Baleares, Ceuta o Melilla esa inercia es dos órdenes de magnitud menor: pérdida de un solo grupo puede provocar una caída de frecuencia de 1–3 Hz/s (ROCOF) frente a los 0,05–0,2 Hz/s típicos de ENTSO-E continental.

Esta diferencia de comportamiento dinámico exige ajustes de relés de frecuencia mucho más agresivos que los de la red peninsular, y convierte al diseño del UFLS (Under Frequency Load Shedding) en la medida de seguridad crítica para mantener la estabilidad del sistema.

La norma que define los requisitos funcionales y de ensayo de los relés de frecuencia es la **IEC 60255-181:2019** — *Measuring relays and protection equipment — Part 181: Functional requirements for frequency protection*. Adoptada en Europa como **EN IEC 60255-181:2019**.

---

## Funciones de protección de frecuencia: 81U, 81O y 81R

La IEC 60255-181 cubre tres funciones básicas, identificadas por el código ANSI correspondiente:

| Función ANSI | Denominación | Condición de disparo |
|---|---|---|
| **81U** | Mínima frecuencia (under-frequency) | f < f_ajuste durante t ≥ t_retardo |
| **81O** | Máxima frecuencia (over-frequency) | f > f_ajuste durante t ≥ t_retardo |
| **81R** | ROCOF (df/dt) | \|df/dt\| > ajuste (Hz/s) |

La 81O es relevante en sistemas insulares con alta penetración fotovoltaica: pérdida de carga importante puede elevar la frecuencia por encima de 51–51,5 Hz. La 81R (tasa de cambio de frecuencia) actúa antes de que se alcance el umbral de mínima frecuencia, lo que permite acelerar el deslastre en sistemas de baja inercia.

### Medición de frecuencia según IEC 60255-181

La norma distingue entre:

- **Frecuencia de la señal de entrada**: el relé mide el período de la señal de tensión (o corriente) de alimentación. Precisión mínima exigida: ± 0,01 Hz en régimen permanente.
- **ROCOF**: tasa de variación calculada sobre una ventana deslizante. La ventana de medida (típicamente 20–200 ms) introduce un compromiso entre velocidad y estabilidad de la medición. Una ventana corta de 20 ms es rápida pero muy sensible al ruido armónico; una ventana de 100–200 ms filtra mejor pero retrasa la actuación.

**Precisión de ROCOF exigida por IEC 60255-181:** ± 0,1 Hz/s para ajustes de 0,5 a 10 Hz/s.

**Bloqueo por tensión mínima**: la norma exige que el relé incorpore un elemento de bloqueo por tensión mínima para evitar disparos espurios por pérdida de tensión o por distorsión severa de la señal. El umbral típico de fábrica está entre 0,1 y 0,7 U_n.

---

## Ajuste de mínima frecuencia (81U) en sistemas insulares

### Criterios de ajuste por escalones

El UFLS en sistemas insulares se diseña normalmente en tres o cuatro escalones. Cada escalón deslasta un porcentaje de la carga total para recuperar el equilibrio generación-carga y frenar la caída de frecuencia.

| Escalón | Umbral f (Hz) | Retardo t (s) | % carga deslastrada |
|---|---|---|---|
| 1 | 49,0 | 0,1–0,2 | 10–15 % |
| 2 | 48,5 | 0,1–0,2 | 10–15 % |
| 3 | 48,0 | 0,1–0,2 | 10–15 % |
| 4 | 47,5 | 0,1 | 10–20 % |

En sistemas como el de Canarias (operado por REE), los estudios de planificación ajustan estos valores a la inercia disponible y a la potencia del mayor grupo. La frecuencia mínima que el sistema puede tolerar sin perder sincronismo es típicamente **47,0–47,5 Hz** durante no más de 5–10 segundos.

**Retardo de tiempo**: el retardo de 0,1–0,2 s sirve para evitar disparos por dips de frecuencia transitorios que se recuperan solos. No obstante, en sistemas con ROCOF ≥ 2 Hz/s, un retardo de 0,2 s puede implicar una caída de 0,4 Hz adicional antes del disparo. Por eso muchos operadores de sistemas insulares usan la función 81R como primer escalón de disparo rápido.

### Bloqueo cruzado y coordinación

En instalaciones con grupos de cogeneración o fotovoltaica, el relé de frecuencia del generador del cliente debe coordinarse con el UFLS del operador de red:

- El relé 81U del generador no debe disparar antes de que el UFLS de red actúe (para no agravar el déficit de generación).
- Criterio típico: ajuste de mínima frecuencia del generador 0,5 Hz por debajo del último escalón de UFLS de red.

---

## Ajuste de ROCOF (función 81R) y ventana de medida

La función 81R es especialmente relevante en:
- Detección de islanding en sistemas de generación distribuida (IEC 62116 la menciona como uno de los métodos activos de detección).
- Primer escalón de UFLS en sistemas insulares de baja inercia.
- Protección de grupos generadores contra derivadas de frecuencia peligrosas para la mecánica del rotor.

### Valores de ajuste típicos según aplicación

| Aplicación | Ajuste df/dt (Hz/s) | Ventana de medida |
|---|---|---|
| UFLS rápido sistema insular | 1,0–2,0 | 40–60 ms |
| Detección de islanding BT/MT | 0,5–1,0 | 100–200 ms |
| Protección de grupo generador | 2,0–5,0 | 20–40 ms |
| Red continental (ENTSO-E) | 0,5 | 200–500 ms |

**Interacción ventana-ajuste**: ENTSO-E advierte que un relé de ROCOF con ventana larga puede no disparar si el df/dt inicial supera el umbral pero desciende por debajo antes de que finalice la ventana. En sistemas insulares con inercia baja, la ventana de medida debe ser corta (40–60 ms), asumiendo que la medición es más ruidosa y que se requerirán ajustes de umbral ligeramente superiores para evitar disparos intempestivos.

---

## Criterios de selección y ajuste aplicables en obra

La siguiente guía sintetiza el proceso de ajuste de relés 81U y 81R para un sistema insular:

### 1. Identificar la inercia del sistema
Calcular la constante de inercia efectiva H (en segundos):

```
H = (Σ J_i × ω²_i / 2) / S_base
```

Para sistemas insulares españoles, H típico es de **2–4 s** con grupos diesel/gas, y puede bajar a **1–2 s** con alta penetración fotovoltaica sin inercia sintética.

### 2. Simular la contingencia de mayor pérdida de generación
El ROCOF inicial tras la pérdida del mayor grupo es:

```
df/dt|₀ = –Δf_0 × f_0 / (2 × H × S_base) × ΔP
```

Donde ΔP es la potencia perdida en p.u. respecto a S_base. Con H = 3 s y ΔP = 0,25 p.u.:

```
df/dt|₀ = –50 × 0,25 / (2 × 3) = –2,08 Hz/s
```

Este valor justifica un ajuste de 81R de 1,5–2,0 Hz/s para el primer escalón de UFLS.

### 3. Seleccionar umbrales de 81U
- Primer escalón: f_nominal – 1 Hz (49,0 Hz para red 50 Hz)
- Cada escalón: –0,5 Hz adicional
- Frecuencia mínima de diseño: 47,0–47,5 Hz

### 4. Verificar la característica de temporización del relé según IEC 60255-181
La norma define la **characteristic performance accuracy** (precisión de actuación en condiciones dinámicas), que incluye:
- Variación de la tensión de alimentación: ±10 % U_n
- Variación de la temperatura de operación: –10 °C a +55 °C
- Presencia de armónicos: THD ≤ 10 %

Verificar que el relé seleccionado cumple con la clase de precisión para el rango de ajuste requerido. Algunos relés de gama baja no garantizan la precisión de ±0,01 Hz para frecuencias inferiores a 48 Hz.

### 5. Puesta en servicio
- Inyectar señal de frecuencia variable desde un generador de señal y verificar el tiempo de operación real frente al ajuste.
- Comprobar el tiempo de reinicio (reset) del relé tras la recuperación de frecuencia.
- Simular pérdida de tensión y verificar que el bloqueo por U_min funciona correctamente.

---

## Conclusión

Los relés de frecuencia en sistemas insulares requieren una estrategia de ajuste radicalmente distinta a la de redes interconectadas: umbrales más altos (primer escalón a 49,0 Hz vs. 47,5 Hz en red peninsular), retardos más cortos (0,1–0,2 s) y uso complementario de la función ROCOF con ventanas de medida de 40–60 ms. La IEC 60255-181:2019 establece los requisitos de precisión y ensayo que permiten verificar que el relé se comportará correctamente en el rango dinámico exigido.

El dimensionado del UFLS debe partir de un estudio de inercia y de simulación de la contingencia de mayor pérdida de generación. Sin ese estudio, los ajustes basados únicamente en valores genéricos de norma son insuficientes para garantizar la estabilidad del sistema insular.
