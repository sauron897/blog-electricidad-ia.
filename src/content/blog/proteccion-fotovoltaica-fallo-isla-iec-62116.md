---
title: "Protección anti-isla en FV: IEC 62116 y RD 244/2019"
description: "Análisis técnico de los métodos pasivos, activos e híbridos de protección contra fallo de isla en inversores fotovoltaicos, con criterios de IEC 62116, UNE-EN 50438 y RD 244/2019."
pubDate: 2026-11-07
keywords: ["proteccion fotovoltaica fallo isla IEC 62116", "anti-islanding inversor fotovoltaico", "proteccion isla RD 244/2019", "metodos anti-isla ROCOF AFD"]
author: "Editor"
---

## Qué es el fallo de isla y por qué es un problema de seguridad

El **fallo de isla** (*islanding*) ocurre cuando un inversor fotovoltaico continúa energizando un tramo de la red de distribución BT tras la apertura del interruptor de la empresa distribuidora. El inversor —y la carga local— quedan aislados de la red principal pero mantienen tensión y frecuencia dentro de rangos aparentemente normales.

Los riesgos asociados son directos:

- **Riesgo para operarios de la distribuidora**: un tramo aparentemente desenergizado puede estar a tensión nominal (230/400 V) sostenida por el inversor.
- **Daño al equipo del cliente**: cuando la distribuidora reengancha, la tensión de retorno puede entrar en oposición de fase con la isla, generando un transitorio de sobre-tensión que destruye inversores, transformadores y cargas.
- **Calidad de la energía**: sin referencia de red, la frecuencia y la tensión de la isla derivan libremente, causando perturbaciones en equipos sensibles.

La **UNE-EN 62116:2014** (adopción europea de IEC 62116:2014) define el procedimiento de ensayo para verificar que las medidas de prevención de isla de un inversor fotovoltaico interactivo son eficaces. El **RD 244/2019** de autoconsumo, en conjunción con **UNE-EN 50438:2014**, impone el cumplimiento de esta protección a toda instalación de autoconsumo conectada a la red de BT en España.

---

## Zona de no detección (NDZ) y el caso crítico de IEC 62116

El problema central de la protección anti-isla es la **NDZ (Non-Detection Zone)**: el conjunto de condiciones de carga en que los métodos pasivos no detectan la isla porque la potencia activa y reactiva local están casi perfectamente equilibradas con la generación del inversor. En ese equilibrio, la tensión y la frecuencia en el PCC (Punto de Conexión Común) no derivan lo suficiente como para superar los umbrales de disparo.

**Circuito de ensayo según IEC 62116**: la norma impone el caso más desfavorable. La carga del banco de ensayo es un circuito **RLC resonante** a la frecuencia nominal de red (50 Hz), con un **factor de calidad Q_f = 1** y potencia activa igual al 100 % de la potencia nominal del inversor. Bajo estas condiciones:

- El inversor alimenta exactamente la potencia activa de la carga resistiva.
- La carga inductiva y capacitiva se compensan mutuamente (resonancia).
- No hay flujo neto de potencia activa ni reactiva desde/hacia la red antes de la apertura.

Este escenario es el que maximiza la probabilidad de que el inversor no detecte la desconexión de red. La norma exige que el inversor **cese de energizar el circuito en un tiempo ≤ 2 s** tras la apertura del interruptor de red. Este es el criterio de paso/fallo del ensayo.

---

## Métodos de protección anti-isla: pasivos, activos e híbridos

### Métodos pasivos

Monitorizan parámetros en el PCC sin inyectar perturbaciones. Los más usados:

| Parámetro | Variable medida | Umbral típico (Europa, UNE-EN 50438) | Limitación |
|-----------|----------------|---------------------------------------|------------|
| Sobretensión / subtensión | V (rms) | V < 0,85·Un o V > 1,10·Un | NDZ cuando P_carga ≈ P_inv |
| Sobrefrecuencia / subfrecuencia | f (Hz) | f < 47,5 Hz o f > 51,5 Hz | NDZ cuando Q_carga ≈ 0 |
| ROCOF (Rate of Change of Frequency) | df/dt | \|df/dt\| > 1–2 Hz/s | Sensible a perturbaciones de red normales |
| ROCOV (Rate of Change of Voltage) | dV/dt | \|dV/dt\| > umbral definido por fabricante | Menos estandarizado |
| THD de tensión | Distorsión armónica | > 10 % (orientativo) | Puede activarse por cargas no lineales |

Los umbrales de frecuencia y tensión en España se coordinan con los requisitos de la **UNE-EN 50438:2014** para microgeneradores en paralelo con la red de BT, que exige tiempo de desconexión ≤ 0,5 s para desviaciones de tensión fuera de [0,85·Un; 1,10·Un] y ≤ 0,2 s para desviaciones de frecuencia fuera de [47,5 Hz; 51,5 Hz].

La debilidad intrínseca de los métodos pasivos es que, en el interior de la NDZ, ninguno de estos parámetros supera el umbral en 2 segundos.

### Métodos activos

Inyectan una perturbación deliberada para observar si la red responde o no. Los principales:

**AFD (Active Frequency Drift)**: el inversor desplaza ligeramente la forma de onda de corriente para que la frecuencia de salida derive hacia fuera del rango de red cuando no hay referencia externa. Funciona bien, pero introduce distorsión de corriente que degrada el THD.

**SMS (Slip Mode Frequency Shift)**: el inversor ajusta su ángulo de fase para que, si la red desaparece, la frecuencia derive rápidamente. Es más agresivo que el AFD en la velocidad de derivación.

**SFS (Sandia Frequency Shift)**: variante mejorada del AFD con retroalimentación positiva de frecuencia, lo que reduce la NDZ de forma más eficaz. Empleado en inversores Sandia y derivados.

**AIVV (Active Islanding detection based on Voltage Variation)**: inyecta una variación de tensión reactiva para detectar la respuesta del sistema.

Los métodos activos prácticamente eliminan la NDZ, pero su inyección de perturbaciones en la red puede provocar interacciones negativas cuando múltiples inversores los ejecutan simultáneamente.

### Métodos híbridos

Combinan un disparador pasivo (rápido, sin impacto en la red) con un método activo (activado solo cuando el pasivo sospecha isla). Este enfoque minimiza la distorsión en régimen normal y acelera la detección en el caso crítico. Es la arquitectura más común en inversores modernos que cumplen IEC 62116 con margen.

---

## IEC 62116:2014 — Procedimiento de ensayo y criterios de certificación

La norma define tres bloques de ensayo aplicables a inversores monofásicos y trifásicos:

1. **Ensayo de desconexión en condiciones nominales**: el banco RLC resonante (Q_f = 1) a potencia 100 %. Criterio: desconexión ≤ 2 s.
2. **Ensayo con variación de carga activa y reactiva**: se varía P_carga entre 50 % y 100 % de P_nominal y Q entre valores que producen ΔQ/P de ±0,05 y ±0,10. Criterio: desconexión ≤ 2 s en todos los casos.
3. **Ensayo de robustez frente a perturbaciones de red**: se verifican falsas actuaciones con perturbaciones normales de red (flicker, micro-cortes de < 100 ms). Criterio: ausencia de desconexiones intempestivas.

Un inversor que supera todos los ensayos se considera conforme con la protección anti-isla y puede certificarse bajo UNE-EN 62116.

**Nota sobre la edición**: la versión BS EN IEC 62116 de diciembre 2024 actualiza las condiciones de la fuente DC de ensayo y los criterios de incertidumbre de medida. El cuerpo principal de la norma no cambia los umbrales de 2 s ni el circuito RLC resonante.

---

## Requisitos en España: RD 244/2019 y UNE-EN 50438

### Obligación normativa

El **RD 244/2019** (BOE núm. 83, de 6 de abril de 2019) regula las condiciones técnicas de las instalaciones de autoconsumo. Su **Anexo I** exige que los inversores conectados a la red cumplan los requisitos técnicos de conexión de la distribuidora y, por extensión, los de las normas técnicas aplicables:

- **UNE-EN 50438:2014**: es la norma principal para la conexión en paralelo de microgeneradores (≤ 16 A por fase) a la red de distribución de BT. Incluye protecciones de mínima/máxima tensión, mínima/máxima frecuencia y la obligación de desconexión automática ante isla.
- **UNE-EN 62116:2014**: certificación de la eficacia de la protección anti-isla del inversor.

Para instalaciones de autoconsumo **sin excedentes**, el RD 244/2019 exige adicionalmente un **sistema anti-vertido** que impida la inyección a red. Este es un requisito diferente de la protección anti-isla: el anti-vertido evita el flujo de potencia hacia la red; la protección anti-isla evita que el inversor sostenga tensión en la red cuando ésta ha caído.

### Criterios de selección del inversor para cumplir RD 244/2019

| Requisito | Parámetro a verificar | Dónde figura |
|-----------|-----------------------|--------------|
| Protección anti-isla certificada | UNE-EN 62116 en la declaración de conformidad | Datasheet / DoC del fabricante |
| Límites de tensión de desconexión | 0,85·Un – 1,10·Un, tiempo ≤ 0,5 s | UNE-EN 50438, Tabla 1 |
| Límites de frecuencia de desconexión | 47,5 – 51,5 Hz, tiempo ≤ 0,2 s | UNE-EN 50438, Tabla 1 |
| Reenganche automático | No antes de 20 s tras la recuperación de la red | UNE-EN 50438, apartado 5.6 |
| Anti-vertido (sin excedentes) | Función IPS o similiar activada | RD 244/2019, Anexo I |

---

## Criterios de selección y diagnóstico en campo

**Al diseñar la instalación**:

1. Exigir la declaración de conformidad (DoC) del inversor con UNE-EN 62116 y UNE-EN 50438. Muchos fabricantes incluyen hojas de conformidad específicas para España con referencia a RD 244/2019.
2. Verificar que los umbrales de protección del inversor están dentro de los rangos de UNE-EN 50438, no de otras normativas nacionales (IEC/IEEE valores distintos para otras regiones).
3. Para instalaciones con más de un inversor en paralelo: verificar interoperabilidad de los métodos activos, ya que dos inversores con SFS pueden interferir entre sí y amplificar la perturbación de frecuencia en el PCC.

**En la puesta en servicio**:

4. Realizar la prueba de desconexión manual de la red y verificar que el inversor se desconecta en < 2 s (prueba simplificada en campo del ensayo IEC 62116).
5. Verificar el tiempo de reenganche: el inversor no debe reconectar antes de 20 s tras la reposición de tensión (protege contra reenganches de la distribuidora durante la isla).

**En mantenimiento y diagnóstico de falsas actuaciones**:

6. Si el inversor desconecta con red presente, revisar primero la calidad de la red en el PCC: flicker elevado (Pst > 1) o microcortes frecuentes pueden activar el ROCOF antes del tiempo de isla.
7. Medir la impedancia de red en el PCC; una red débil (alta impedancia) produce mayor ΔV/ΔI, lo que puede acercar la operación normal al umbral de disparo de los métodos pasivos.

---

## Conclusión

La protección contra fallo de isla en instalaciones fotovoltaicas conectadas a red combina obligaciones normativas claras (IEC 62116 / UNE-EN 62116, UNE-EN 50438, RD 244/2019) con un problema técnico no trivial: la NDZ, donde los métodos pasivos son ciegos. La solución industrial —métodos híbridos con disparador pasivo y perturbación activa de respaldo— es la que cumplen los inversores modernos certificados. Para el técnico o ingeniero, la clave de proyecto está en verificar la declaración de conformidad del inversor, ajustar los umbrales al código de red español y validar en campo el tiempo de desconexión ante isla, antes de que la distribuidora lo exija en la inspección de conexión.
