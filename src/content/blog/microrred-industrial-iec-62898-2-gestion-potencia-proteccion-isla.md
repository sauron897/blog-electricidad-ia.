---
title: "Microrredes industriales: gestión de potencia IEC 62898-2"
description: "Arquitectura, modos de operación, protección de isla y control droop en microrredes AC industriales según IEC TS 62898-2 y 62898-3-1. Valores numéricos y criterios de selección."
pubDate: 2026-11-26
keywords: ["microrred industrial IEC 62898", "protección de isla microgrid", "control droop frecuencia tensión", "ROCOF anti-islanding DER"]
author: "Editor"
---

Una microrred industrial es un sistema eléctrico AC delimitado que integra recursos de energía distribuida (DER: fotovoltaica, baterías BESS, generadores) con cargas locales y un único punto de conexión (POC) a la red de distribución. Su valor diferencial respecto a una instalación convencional es la capacidad de operar en modo isla cuando se pierde la interconexión, garantizando el suministro a cargas críticas. La normativa de referencia es la serie IEC TS 62898, con la parte 2 (operación) y la parte 3-1 (protección y control dinámico) como documentos técnicos clave.

Este artículo describe la arquitectura funcional, los modos de operación, las protecciones de isla y el control de frecuencia y tensión. Los valores numéricos son coherentes con IEC TS 62898-2:2018+AMD1:2023, IEC TS 62898-3-1:2020+AMD1:2023 y los requisitos de conexión del RD 1183/2020 (España).

## Arquitectura funcional de la microrred AC industrial

Una microrred AC según IEC TS 62898-1 se estructura en torno a cuatro elementos:

**1. Punto de conexión (POC):** interfaz con la red de distribución. Contiene el interruptor de acoplamiento de red (IAN), que separa físicamente la microrred en la transición a modo isla. El interruptor debe cumplir IEC 60947-2 para aplicaciones en BT o IEC 62271-100 en MT, con capacidad de operación motorizada para apertura/cierre por orden del controlador de microrred (MGCC).

**2. Recursos de energía distribuida (DER):** generadores síncronos diésel o de gas, inversores fotovoltaicos, sistemas de almacenamiento BESS con convertidores VSI bidireccionales y grupos electrógenos. Cada DER conecta a la barra común a través de su propio interruptor.

**3. Cargas:** clasificadas en críticas (alimentación ininterrumpida en modo isla) y no críticas (desconectadas automáticamente en caso de déficit de generación mediante load shedding escalonado).

**4. Sistema de control de microrred (MGCC):** ejecuta la gestión de energía, el despacho de DER, el control de frecuencia y tensión, y la coordinación de protecciones. Comunicación con DER y protecciones típicamente vía IEC 61850 GOOSE o Modbus TCP.

**Parámetro de red de suministro:** para una microrred BT conectada a un transformador MT/BT de 0,63 MVA con Ucc = 4 % (IEC 60076), la impedancia de cortocircuito en barras BT es:

```
Zcc = Ucc(%) × Un² / (100 × Sn) = 0,04 × 0,4² / 0,63 = 10,16 mΩ
Icc_3f = Un / (√3 × Zcc) = 400 / (1,732 × 0,01016) ≈ 22,7 kA
```

En modo isla, sin la contribución del transformador, la corriente de cortocircuito cae drásticamente: un inversor VSI de 100 kW aporta como máximo 1,5–2 × In (≈ 180–240 A), frente a los 22 kA del modo conectado. Este cambio de orden de magnitud es el principal reto de coordinación de protecciones en microrred.

## Modos de operación: conectado a red e isla

IEC TS 62898-2 define dos modos fundamentales de operación:

| Parámetro | Modo conectado a red | Modo isla |
|-----------|---------------------|-----------|
| Referencia de frecuencia | Red de distribución (50 Hz ± tolerancia EN 50160) | MGCC + DER maestro |
| Referencia de tensión | Red de distribución | MGCC + DER maestro |
| Control de DER | Seguidor (modo PQ, potencia activa/reactiva fija) | Formador de red (*grid-forming*) |
| Corriente de falta | 5–22 kA (contribución del transformador) | 1,5–2 × In (solo inversores) |
| Protecciones activas | Sobreintensidad IEC 60947-2 / 60255-151 | Sobretensión ANSI 59, subfrecuencia ANSI 81U, impedancia ANSI 21 |
| Reenganche al sistema | — | Sincronización: ANSI 25 obligatorio |

La transición conectado → isla puede ser **planificada** (apertura controlada del IAN, transferencia suave) o **no planificada** (disparo por falta en la red de distribución). La transición no planificada exige que la protección anti-isla dispare el IAN antes de que el DER opere de forma no sincronizada con la red, cumpliendo los tiempos del RD 1183/2020: ≤ 0,5 s para elementos conectados en BT.

## Protección de isla: funciones ANSI y detección activa

La protección anti-isla impide que la microrred permanezca energizando un tramo de red sin la supervisión de la distribuidora. IEC TS 62898-3-1 clasifica los métodos de detección:

### Métodos pasivos

Monitorizan variaciones en parámetros de red sin inyectar señal de perturbación:

- **ROCOF (Rate Of Change Of Frequency) — ANSI 81R:** dispara cuando |df/dt| > umbral. En España, el RD 1183/2020 establece el umbral en **1,0 Hz/s** para instalaciones BT/MT sin acuerdo específico con el operador. El intervalo de medida recomendado por IEC TS 62898-3-1 es 100–200 ms para evitar disparos intempestivos por perturbaciones de la red.

- **Desplazamiento vectorial (Vector Shift / VS):** detecta el salto de ángulo de la tensión en el instante de apertura del IAN. Umbral típico: 6–12°. Sensible a la carga asimétrica y puede producir disparos no deseados.

- **ANSI 27/59 (subtensión/sobretensión):** según EN 50160 e IEC TS 62898-2, los umbrales de actuación son:
  - 27: U < 0,80 × Un por t > 1 s, o U < 0,45 × Un por t > 0,1 s
  - 59: U > 1,15 × Un por t > 0,2 s

- **ANSI 81U/81O (subfrecuencia/sobrefrecuencia):** umbrales mínimos según IEC TS 62898-2: 47,5 Hz (subfrecuencia, t < 0,5 s) y 51,5 Hz (sobrefrecuencia, t < 0,2 s), coherentes con EN 50160.

### Métodos activos

Inyectan una perturbación controlada y miden la respuesta del sistema:

- **Inyección de impedancia:** el inversor introduce una variación periódica de reactiva (± ΔQ) y mide la desviación de frecuencia resultante. En modo conectado, la red absorbe la perturbación sin variación apreciable de frecuencia (Δf < 0,05 Hz). En modo isla, la desviación supera el umbral de detección.

- **Desplazamiento de frecuencia activo (AFS):** empuja la frecuencia de salida del inversor hacia un extremo. En modo isla, la frecuencia se aleja del nominal y dispara ANSI 81U/81O.

La combinación **ROCOF + ANSI 27/59/81 + método activo** reduce la zona de no-detección (NDZ) a valores prácticamente nulos y es el esquema recomendado por IEC TS 62898-3-1 para microrredes industriales.

## Control droop: frecuencia y tensión en modo isla

En modo isla, sin la referencia rígida de la red, el reparto de potencia entre DER se realiza mediante control droop. IEC TS 62898-3-1 lo define en dos capas de control jerárquico:

### Control primario (droop)

Cada DER formador de red (generador síncrono o inversor VSI en modo *grid-forming*) implementa:

**Droop de frecuencia (P-f):**
```
f = f₀ − kp × (P − P₀)
kp = Δf_max / ΔP_max
```
Con Δf_max = ±1 Hz (2 % de 50 Hz) y ΔP_max = Pn del DER. Un droop del 4 % significa que la frecuencia cae 2 Hz cuando el DER asume el 100 % de su potencia nominal.

**Droop de tensión (Q-V):**
```
V = V₀ − kq × (Q − Q₀)
kq = ΔV_max / ΔQ_max
```
Con ΔV_max = ±5 % de Un (20 V en 400 V) y ΔQ_max = Qn.

### Control secundario (restauración)

El MGCC ejecuta la restauración de frecuencia y tensión al nominal mediante un integrador PI que actúa sobre el setpoint P₀, V₀ de cada DER. El tiempo de restauración es del orden de 10–60 s (mucho más lento que el droop primario de 0,1–1 s), evitando interacción entre niveles.

### Control terciario (despacho óptimo)

Gestiona el flujo de potencia hacia/desde la red de distribución, el estado de carga del BESS (SoC objetivo) y la participación óptima de los DER. Horizonte temporal: minutos.

## Criterios de selección y dimensionado para ingenieros

| Criterio | Recomendación IEC TS 62898 | Valor típico industrial |
|----------|---------------------------|------------------------|
| Capacidad BESS para modo isla | ≥ potencia de cargas críticas × tiempo de autonomía | 30 min a 2 h para cargas críticas |
| Umbral ROCOF anti-isla | 0,5–1,0 Hz/s (ajustar al sistema) | 1,0 Hz/s (RD 1183/2020 España) |
| Retardo de reconexión mínimo | ≥ 60 s (operación planificada) | 180 s (RD 1183/2020) |
| Tolerancia sincronización ANSI 25 | Δf < 0,2 Hz, ΔU < 10 %, Δφ < 20° | Δf < 0,1 Hz en BT |
| Sobrecorriente mínima detectable en isla | 1,5 × In (inversores VSI) | Proteger con ANSI 59, 27, 21 |
| Droop de frecuencia (P-f) | 2–5 % | 4 % (reparto proporcional a Pn) |
| Droop de tensión (Q-V) | 2–5 % | 3–5 % |
| Tiempo de respuesta control primario | < 1 s | 0,1–0,5 s (VSI) |

**Checklist previo a la puesta en servicio en modo isla** (IEC TS 62898-2, apartado de commissioning):

1. Verificar que el IAN abre en < 0,5 s ante disparo de anti-isla (ROCOF + 27/59/81).
2. Comprobar el reparto de potencia activa y reactiva entre DER mediante ensayo de escalón de carga (carga súbita del 20 % de Pn).
3. Registrar la desviación de frecuencia máxima ante el escalón: no debe superar ±2 Hz (IEC TS 62898-2).
4. Verificar la restauración al nominal en < 60 s con control secundario activo.
5. Ensayar la sincronización de reconexión: Δf < 0,2 Hz, ΔU < 10 %, tiempo de espera ≥ 180 s.
6. Comprobar la secuencia de load shedding: cargas no críticas deben desconectar en orden predefinido antes de que la frecuencia caiga por debajo de 48,5 Hz.

## Conclusión

El diseño de una microrred industrial requiere coordinar tres dominios técnicos simultáneamente: la protección de isla (anti-islanding con ROCOF y métodos activos), el control de potencia en modo isla (droop primario + restauración secundaria) y la coordinación de protecciones ante fallas con corrientes de cortocircuito drásticamente reducidas respecto al modo conectado. IEC TS 62898-2 y 62898-3-1 proporcionan el marco técnico completo, complementado en España por RD 1183/2020 para los requisitos de conexión. El elemento crítico de ingeniería es ajustar el ROCOF al sistema real: un umbral demasiado sensible (< 0,5 Hz/s) produce disparos intempestivos; uno demasiado laxo (> 2 Hz/s) deja ventanas de operación no sincronizada. La combinación de detección pasiva y activa con tiempos de actuación < 500 ms es el estándar mínimo para instalaciones industriales con DER inverter-based.
