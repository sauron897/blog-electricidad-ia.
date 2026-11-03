---
title: "Relés de frecuencia en sistemas insulares: ajuste según IEC 60255-181"
description: "Ajuste de relés 81U, 81O y ROCOF en sistemas insulares: parámetros IEC 60255-181, escalones de deslastre UFLS y protección anti-islamiento según normativa española."
pubDate: 2026-11-03
keywords: ["rele frecuencia sistema insular IEC 60255-181", "subfrecuencia proteccion insular UFLS", "ROCOF anti-islamiento", "deslastre carga frecuencia Canarias Baleares"]
author: "Editor"
---

Los sistemas insulares —Canarias, Baleares, Ceuta, Melilla— presentan el desafío más exigente para la protección de frecuencia: poca inercia, alta penetración renovable y ausencia de interconexión con la red peninsular. Un relé de frecuencia mal ajustado dispara en cascada ante una perturbación ordinaria, o peor, no actúa cuando hay déficit real de generación. Este artículo describe cómo ajustar funciones 81U, 81O y 81R conforme a IEC 60255-181:2019, con referencia al esquema UFLS vigente en los sistemas no peninsulares españoles.

## Alcance de IEC 60255-181 y funciones de protección de frecuencia

La norma **EN IEC 60255-181:2019** (adoptada por CENELEC) define los requisitos mínimos funcionales y de ensayo para tres funciones de protección de frecuencia, identificadas por sus códigos ANSI y nodos lógicos IEC 61850-7-4:

| Función ANSI | Nombre | Nodo lógico IEC 61850 | Descripción |
|---|---|---|---|
| **81U** | Subfrecuencia | PTUF | Dispara cuando f cae por debajo del umbral ajustado |
| **81O** | Sobrefrecuencia | PTOF | Dispara cuando f supera el umbral ajustado |
| **81R** | ROCOF (df/dt) | PFRC | Dispara cuando la tasa de cambio de frecuencia supera el ajuste |

La norma exige que los relés superen ensayos de precisión con rampa de frecuencia que comienza siempre en la frecuencia nominal del sistema (50 Hz en Europa) y alcanza los puntos 1,2×, 2,0×, 5,0× y 10× el valor de ajuste. Para ROCOF esto es crítico: si la prueba no parte de 50 Hz, el comportamiento real puede diferir del ensayado.

**Precisión mínima según IEC 60255-181:**
- Error de medida de frecuencia: ≤ ±10 mHz en condiciones nominales
- Error del umbral de actuación: ≤ ±1% del valor ajustado
- Tiempo de operación en 2×ajuste ROCOF: ≤ 60 ms
- Estabilidad ante salto de vector de fase: el relé no debe disparar ante saltos de fase < 10° (definido en la norma como "phase-angle jump stability")

## Inercia y comportamiento de frecuencia en sistemas insulares

La respuesta de frecuencia ante una pérdida de generación depende directamente de la **constante de inercia H** del sistema:

$$\frac{df}{dt}\bigg|_{t=0} = \frac{\Delta P \cdot f_0}{2 \cdot H \cdot S_{base}}$$

Donde ΔP es la potencia perdida en p.u., f₀ = 50 Hz y H es la constante de inercia media ponderada (en segundos). Valores típicos:

| Tipo de sistema | H típico (s) | df/dt inicial ante pérdida del 10% de generación |
|---|---|---|
| Red peninsular española | 5–8 s | 0,3–0,5 Hz/s |
| Sistema Canarias (Tenerife/Gran Canaria) | 2–4 s | 0,6–1,2 Hz/s |
| Instalación industrial autónoma (un generador) | 1–2 s | 1,2–2,5 Hz/s |
| Sistema con alta penetración solar FV (sin inercia sintética) | < 2 s | > 2 Hz/s |

Este diferencial explica por qué los ajustes de ROCOF para sistemas insulares difieren hasta un orden de magnitud de los empleados en redes interconectadas de alta inercia.

## Plan de deslastre de carga por subfrecuencia (UFLS)

El **BOE-A-2024-1858** (Resolución de 31 de enero de 2024, CNMC) aprobó la actualización de los planes de deslastre automático de cargas para Baleares y Canarias. Estos planes definen escalones por subfrecuencia (**Sfn**) y por derivada de frecuencia (**Dfn**).

La estructura típica de un esquema UFLS en sistema insular español es la siguiente (valores orientativos; los valores exactos de cada sistema están en la resolución CNMC):

| Escalón | Función | Umbral f (Hz) | Umbral df/dt (Hz/s) | Retardo (ms) | % carga desconectada |
|---|---|---|---|---|---|
| Sfn-1 | 81U | 49,0 | — | 0 | 10–15% |
| Sfn-2 | 81U | 48,5 | — | 0 | 10–15% |
| Sfn-3 | 81U | 48,0 | — | 0 | 10–15% |
| Dfn-1 | 81R supervisado | — | 1,0–2,0 | ≤ 100 | 10–15% |
| Dfn-2 | 81R supervisado | — | 2,0–3,0 | ≤ 100 | 10–15% |

**Supervisión de ROCOF con umbral de frecuencia:** los escalones Dfn incluyen obligatoriamente supervisión por subfrecuencia (típicamente < 49,5 Hz) para evitar deslastre por ROCOF ante cortocircuitos o maniobras de red que producen derivadas altas sin déficit de generación real. IEC 60255-181 no impone esta supervisión, pero es práctica estándar en todos los esquemas UFLS modernos.

## Función ROCOF (81R): ajuste y problemática en sistemas de alta penetración renovable

La función **ROCOF (Rate of Change of Frequency, df/dt)** detecta variaciones rápidas de frecuencia antes de que el umbral absoluto 81U se alcance, lo cual es crítico en sistemas insulares con poca inercia donde la frecuencia puede caer 1,0 Hz en menos de 500 ms.

**Parámetros de ajuste relevantes según IEC 60255-181:**

- **Umbral df/dt (Hz/s):** valor mínimo de tasa de cambio que activa el relé
- **Ventana de medida:** intervalo sobre el que se calcula df/dt (típicamente entre 20 ms y 500 ms según el fabricante; ventanas cortas dan respuesta más rápida pero más ruidosa)
- **Tiempo de operación:** retardo intencional (típicamente 0–500 ms)
- **Supervisión de frecuencia:** umbral de frecuencia por debajo del cual se habilita ROCOF (evita disparos por perturbaciones en condiciones normales)

**Ajustes típicos según aplicación:**

| Aplicación | Umbral df/dt | Tiempo retardo | Supervisión f |
|---|---|---|---|
| Anti-islamiento generación distribuida (EN 50549-1) | 1,0–2,0 Hz/s | 200–500 ms | 47,5–49,5 Hz |
| Deslastre UFLS insular escalón rápido | 1,0–2,0 Hz/s | ≤ 100 ms | < 49,5 Hz |
| Protección de generadores (desconexión de isla) | 0,5–1,0 Hz/s | 200 ms | 49,0–49,8 Hz |
| Interconexión MT con red débil | 1,0–1,5 Hz/s | 300 ms | < 49,5 Hz |

**Limitación crítica del ROCOF en inversores:** los inversores fotovoltaicos con control PLL (Phase-Locked Loop) pueden mantener artificialmente la frecuencia durante breves instantes tras el islamiento, retrasando la respuesta del relé ROCOF externo. La norma **EN 50549-1:2019** (requisitos para microinstalaciones hasta 800 W) y **EN 50549-2:2019** (hasta 50 kW) establecen los requisitos de desconexión automática que complementan IEC 60255-181 para inverters en BT/MT.

## Protección contra sobrefrecuencia (81O) en sistemas insulares con alta penetración renovable

La sobrefrecuencia ocurre cuando la generación supera a la carga, situación habitual en sistemas insulares con alta penetración solar o eólica ante una pérdida brusca de carga o un exceso de generación renovable.

Ajustes habituales para 81O en sistemas no peninsulares españoles:

| Umbral f (Hz) | Retardo | Acción |
|---|---|---|
| 50,5 Hz | 100–200 ms | Alerta, reducción de setpoint en generadores |
| 51,0 Hz | 0–100 ms | Deslastre de generación renovable |
| 51,5 Hz | 0 ms | Desconexión urgente |
| 52,0 Hz | 0 ms | Protección de máquinas (turbinas, alternadores) |

## Criterios de selección y ajuste para ingenieros

Los criterios para ajustar un esquema de protección de frecuencia en un sistema insular siguen esta lógica:

**1. Estudio de estabilidad de frecuencia previo:** antes de ajustar un relé, es imprescindible disponer de la H media ponderada del sistema y simular el peor caso de pérdida de generación. Sin esto, cualquier ajuste es empírico y potencialmente incorrecto.

**2. Coordinación entre escalones:** el tiempo entre escalones de deslastre debe ser superior al tiempo de operación del relé más el tiempo de actuación del interruptor (típicamente 60–100 ms por escalón), de lo contrario los escalones se disparan simultáneamente y el sistema pierde más carga de la necesaria.

**3. Ajuste de ventana de medida ROCOF:** ventanas cortas (20–40 ms) son más sensibles pero propensas a disparos intempestivos por cortocircuitos. Ventanas de 100–200 ms dan mejor discriminación pero reducen la velocidad de respuesta. Para sistemas con H < 2 s se recomienda ventana de 60–100 ms con supervisión de frecuencia.

**4. Verificación según IEC 60255-181:** los ensayos deben verificar al menos:
   - Tiempo de operación a 1,2× y 2,0× el umbral
   - No operación ante cortocircuito trifásico (salto de vector < 10°)
   - Comportamiento bajo tensión reducida (hasta 0,1 × V_nominal según la norma)
   - Precisión de frecuencia ±10 mHz

**5. Señalización IEC 61850:** en subestaciones digitales, la señalización de las funciones PTUF/PTOF/PFRC debe mapearse a datasets GOOSE para garantizar que el esquema UFLS opera correctamente con latencias < 4 ms por trama GOOSE clase de rendimiento P2/P3 según IEC 61850-5.

## Conclusión

La protección de frecuencia en sistemas insulares requiere un análisis dinámico previo que determine la H del sistema y los márgenes de deslastre necesarios. IEC 60255-181:2019 define los requisitos de precisión y ensayo, pero no los valores de ajuste, que dependen del estudio de estabilidad y del plan de deslastre aprobado por la autoridad regulatoria (en España, la CNMC mediante BOE). El técnico que configura estos relés debe coordinar umbral absoluto 81U, función ROCOF 81R con supervisión de frecuencia, y función 81O, garantizando que los tiempos entre escalones sean mayores que la suma de los tiempos de operación del relé más el tiempo de apertura del interruptor de cabecera.
