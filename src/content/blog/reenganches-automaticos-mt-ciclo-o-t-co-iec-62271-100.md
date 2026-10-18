---
title: "Reenganches automáticos en distribución MT: ciclo O-t-CO e IEC 62271-100"
description: "Ciclos de reenganche en redes MT: ciclo O-t-CO según IEC 62271-100, parámetros del relé función 79 y criterios de exclusión para líneas aéreas de 20 kV."
pubDate: 2026-10-18
keywords: ["reenganche automatico MT", "ciclo O-t-CO IEC 62271-100", "relé función 79 ANSI", "tiempo muerto reenganche distribución", "faltas transitorias líneas aéreas MT"]
author: "Editor"
---

## Introducción

El reenganche automático en redes de distribución de media tensión responde a una realidad estadística consistente en todos los estudios de campo: entre el 80 y el 90 % de las faltas en líneas aéreas MT son transitorias. Un arco causado por una descarga atmosférica, el roce de vegetación o una ave se autoextingue al interrumpir la corriente durante unos centenares de milisegundos. Reenergizar la línea sin intervención humana restaura el suministro en segundos, frente a los 20–40 minutos de una actuación manual con equipo de brigada.

En España, las redes de distribución a 20 kV operadas por las empresas distribuidoras aplican esquemas de reenganche en todos los alimentadores de línea aérea. La lógica está implementada en el relé de protección (función ANSI 79) coordinada con el interruptor automático, cuya capacidad de ciclos de maniobra queda definida en **IEC 62271-100** (UNE-EN 62271-100 en su transposición española).

## Fundamento físico: desionización del canal de arco

Cuando se produce una falta franca en una línea aérea a 20 kV, la corriente de cortocircuito ioniza el aire en la zona del arco. El interruptor automático abre el circuito y extingue el arco en el paso natural por cero de la corriente (extinción en vacío o SF₆ en menos de 1 ciclo). A partir de ese momento, el canal ionizado empieza a enfriarse y a recuperar su rigidez dieléctrica.

El tiempo mínimo necesario para que el medio recupere rigidez dieléctrica suficiente es el **tiempo de desionización** (*deionization time*). Para distribución a 20 kV, los valores típicos oscilan entre 0,2 s y 0,5 s. La fórmula simplificada de Ramey-Reid proporciona una primera estimación del tiempo mínimo:

```
t_d (s) ≈ k · √(V_kV)     con k ≈ 0,03 para líneas aéreas MT
```

Para 20 kV: t_d ≈ 0,03 · √20 ≈ 0,13 s (mínimo teórico sin margen). En la práctica se suma el tiempo de rearme de los relés aguas abajo (50–200 ms) y un margen de seguridad, resultando en un tiempo muerto mínimo del primer disparo de **0,3–1,0 s**.

A mayor corriente de falta y mayor tensión, mayor es la energía depositada en el arco y mayor el tiempo de desionización requerido. En redes MT de neutro rígido (alta Icc de tierra) los tiempos muertos deben ser más largos que en redes de neutro impedante o aislado.

## Ciclo de maniobra del interruptor según IEC 62271-100

La norma IEC 62271-100 define los ciclos de ensayo homologados para interruptores de corriente alterna. El ciclo estándar es:

```
O — t — CO — t' — CO
```

Donde:
- **O** = apertura (*Opening*)
- **CO** = cierre seguido de apertura inmediata (*Close-Open*, sin pausa deliberada entre ambas)
- **t** y **t'** = intervalos libres entre maniobras

Para interruptores de **reenganche estándar**: t = 3 min (con alternativas normalizadas de 15 s y 1 min).  
Para interruptores de **reenganche rápido**: t = 0,3 s — la secuencia más severa de la norma para la cámara de extinción.

| Parámetro | Reenganche estándar | Reenganche rápido |
|---|---|---|
| Tiempo t (IEC 62271-100) | 3 min (/ 15 s / 1 min) | 0,3 s |
| Secuencia de ensayo | O – 3 min – CO – 3 min – CO | O – 0,3 s – CO – 15 s – CO |
| Aplicación típica | AT, transformadores MT/BT | Distribución MT aérea |
| Categoría de servicio | E1 (estándar) | **E2 obligatorio** |

Un interruptor catalogado como E1 (categoría estándar) no puede someterse repetidamente al ciclo O-0,3s-CO sin degradación prematura de la cámara de extinción. Para distribución MT con reenganches rápidos es imprescindible especificar categoría **E2** al proveedor.

## Parametrización del relé de reenganche — función ANSI 79

El relé de reenganche (función ANSI 79, o *Reclosing Relay* en terminología IEC 60255-1) controla la lógica temporizada de apertura y reenganche, coordinada con las protecciones de sobreintensidad de fase (50/51) y de tierra (50N/51N). Los parámetros principales son:

### Tiempo muerto (Dead Time)

Intervalo entre la apertura del interruptor y la orden de cierre. Debe superar el tiempo de desionización del arco más el tiempo de reset de los relés aguas abajo.

- **1er disparo**: 0,3–1,0 s (reenganche rápido — para faltas transitorias por rayo o vegetación)
- **2º disparo**: 10–30 s (reenganche lento — tiempo suficiente para eliminar causas semi-permanentes)
- **3er disparo**: 30–60 s
- **4º disparo** (si se implementa): 60–120 s

### Tiempo de recuperación (Reclaim Time)

Ventana de tiempo después de un reenganche exitoso durante la cual un nuevo disparo reinicia el ciclo (sin pasar por cero el contador). Si transcurre sin nuevo disparo, el contador de disparos se pone a cero. Valores típicos: **15–60 s**.

### Enclavamiento (Lockout)

Tras el último reenganche fallido, el relé bloquea nuevos intentos y mantiene el interruptor abierto (*breaker lockout*, estado 86 en ANSI). La reposición requiere intervención manual o señal remota desde SCADA/DMS.

### Coordinación con curvas de sobreintensidad

El esquema más extendido en distribución MT española:

| Disparo | Protección activa | Curva IEC 60255-151 | Propósito |
|---|---|---|---|
| 1.º | 50/51 rápida + 50N | Muy Inversa (MI), TMS = 0,1–0,3 | Eliminar falta transitoria rápido |
| 2.º – 4.º | 51 lenta + 51N | Extremad. Inversa (EI), TMS = 0,3–0,6 | Selectividad aguas abajo |

El primer disparo usa la curva rápida para minimizar la energía de arco en el punto de falta y respetar la energía máxima que puede disipar el conductor. Los disparos sucesivos emplean la curva lenta para dar margen a que fusibles o seccionalizadores aguas abajo actúen selectivamente.

## Criterios de aplicación y exclusiones

### Aplicar reenganche en:
- Líneas aéreas MT con historial de faltas transitorias superior al 70 %
- Alimentadores rurales en zonas de alta keraunicidad (≥ 20 días de tormenta/año)
- Redes en anillo donde la pérdida de un alimentador no interrumpe suministro crítico

### Excluir el reenganche obligatoriamente en:

**1. Líneas en cable subterráneo**: las faltas en cables XLPE o EPR son prácticamente todas permanentes (inclusiones de humedad, perforación mecánica). Un reenganche sobre cable en falta prolonga el daño dieléctrico irreversible en el punto de falta y puede convertir un fallo recuperable en una rotura total del aislamiento. El relé debe inhibir la función 79 mediante señal digital si el alimentador incluye tramos en cable.

**2. Alimentadores con generación distribuida (GD) conectada**: el reenganche sobre una isla aislada puede producir un cierre fuera de sincronismo. Diferencias de fase de 60–120° entre la red y el generador en isla generan picos de corriente destructivos. Norma de aplicación: **IEC 62116** para protección antiislamiento de inversores. Inhibición obligatoria o coordinación con protección de sincronismo (función ANSI 25).

**3. Transformadores MT/BT**: la energización de un transformador en vacío tras un reenganche puede generar corrientes de magnetización de hasta 8–12 × In durante los primeros ciclos (*inrush*), que pueden falsar el relé diferencial del transformador. Si el transformador está en el extremo del alimentador, debe inhibirse el reenganche o añadirse supervisión de voltaje aguas abajo.

**4. Cargas industriales sensibles**: hornos de arco, procesos continuos o clientes con SLA de continuidad. Requiere acuerdo contractual explícito y bloqueado del reenganche vía señal de telemando.

## Ejemplo de ajuste: alimentador MT 20 kV tipo

Alimentador aéreo de distribución urbana-rural en red de 20 kV:
- Longitud: 8,5 km; conductor LA-110 (94,6 mm² Al)
- Icc máximo en cabecera: 5,1 kA (cortocircuito trifásico)
- Icc mínimo bifásico en extremo: 290 A
- Faltas históricas transitorias: 83 %
- Sin GD conectada; sin tramos en cable

| Parámetro | Ajuste aplicado |
|---|---|
| N.º de reenganches | 3 |
| Tiempo muerto 1.er disparo | 0,5 s |
| Tiempo muerto 2.º disparo | 15 s |
| Tiempo muerto 3.er disparo | 45 s |
| Tiempo de recuperación | 30 s |
| Curva 1.er disparo | IEC Muy Inversa, TMS = 0,20 |
| Curva 2.º – 3.er disparo | IEC Extrem. Inversa, TMS = 0,45 |
| Inhibición cable | Señal DI activa en tramos en cable |
| Estado tras lockout | Abierto — reposición manual SCADA |
| Interruptor (IEC 62271-100) | Categoría E2, ciclo O–0,5s–CO–15s–CO–45s–CO |

## Conclusión

El reenganche automático en distribución MT exige dominar simultáneamente la física del arco eléctrico, los límites mecánicos del interruptor según IEC 62271-100 y la parametrización del relé función 79 coordinada con las curvas de sobreintensidad. Los errores más frecuentes son reenganchar sobre cable sin inhibición selectiva, omitir la inhibición ante GD conectada o especificar un interruptor E1 para ciclos O-0,3s-CO. Con un ajuste correcto, un esquema de tres disparos recupera automáticamente entre el 75 y el 85 % de las interrupciones de una red aérea de 20 kV antes de que el equipo de brigada llegue al campo.
