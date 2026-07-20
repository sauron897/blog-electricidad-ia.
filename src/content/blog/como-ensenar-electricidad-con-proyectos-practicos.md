---
title: "Enseñar electricidad con proyectos prácticos: guía técnica"
description: "Metodología ABP para docentes de FP Electrotécnica: estructura de proyectos prácticos con parámetros REBT, IEC 60364 y criterios de verificación reales en aula-taller."
pubDate: 2026-07-20
keywords: ["enseñar electricidad proyectos", "ABP electrotécnica FP", "proyectos prácticos electricidad taller", "ITC-BT verificación instalación aula", "metodología electricidad técnicos"]
heroImage: /images/como-ensenar-electricidad-con-proyectos-practicos.jpg
author: "Editor"
---

Enseñar electricidad sin conectar nada produce técnicos que resuelven circuitos en papel pero no saben por qué falla una instalación real. El aprendizaje basado en proyectos (ABP) en electrotécnica no es una moda pedagógica: es el único método que entrena simultáneamente el cálculo, la normativa y el diagnóstico. Esta guía está dirigida a docentes de FP Electrotécnica y formadores industriales que quieren estructurar proyectos de taller con rigor técnico.

El objetivo de cada proyecto no es que el alumno "aprenda haciendo" en sentido vago — es que al terminar sea capaz de justificar cada decisión con un artículo del REBT, un valor de la IEC o una medida instrumental.

## Fundamentos del ABP aplicado a instalaciones eléctricas

![Ilustración técnica](/images/como-ensenar-electricidad-con-proyectos-practicos-2.jpg)

El ABP en electrotécnica tiene una diferencia crítica respecto al ABP genérico: el producto entregable del alumno debe ser **verificable instrumentalmente**. No basta con que el circuito funcione — debe cumplir:

- **Resistencia de aislamiento** ≥ 0,5 MΩ entre conductores activos y tierra (IEC 60364-6, tabla 6A, para circuitos ≤ 500 V)
- **Continuidad del conductor de protección** con resistencia ≤ 1 Ω en el punto de uso (ITC-BT-19, apartado 2.2.4)
- **Impedancia de bucle de fallo** tal que la corriente de cortocircuito supere el umbral de disparo del magnetotérmico dentro del tiempo máximo según IEC 60364-4-41

Esta exigencia convierte el taller en un entorno de verificación real, no una maqueta. El alumno mide, no solo conecta.

### Los tres niveles de complejidad

Un proyecto de electrotécnica bien diseñado tiene tres niveles de entregable:

| Nivel | Entregable | Norma de referencia | Competencia desarrollada |
|:---:|---|---|---|
| 1 | Esquema unifilar + lista de materiales | ITC-BT-15, ITC-BT-25 | Cálculo y documentación |
| 2 | Montaje físico en panel o maqueta | ITC-BT-19, ITC-BT-24 | Ejecución conforme a normativa |
| 3 | Acta de verificación con medidas reales | IEC 60364-6 (UNE-HD 60364-6) | Diagnóstico y puesta en servicio |

El error más común en los talleres es quedarse en el nivel 2: el alumno monta y conecta, pero nunca aprende a verificar. Un técnico que no sabe usar un Megger ni un comprobador de bucle de fallo no está cualificado para la puesta en servicio — y las ITCs lo exigen explícitamente.

---

## Proyecto tipo 1: instalación de vivienda unifamiliar según ITC-BT-25

Este es el proyecto de referencia para FP de grado medio (Instalaciones Eléctricas y Automáticas) y cubre la totalidad de la ITC-BT-25.

### Parámetros de diseño obligatorios

La vivienda de referencia debe definirse con **grado de electrificación básico o elevado** según ITC-BT-10:

- **Básico**: previsión de carga 5.750 W (230 V, 25 A)
- **Elevado**: previsión de carga 9.200 W (230 V, 40 A)

Para grado elevado, ITC-BT-25 impone al menos los circuitos siguientes:

| Circuito | Uso | Sección mínima Cu | PIA |
|---|---|:---:|:---:|
| C1 — Alumbrado | Iluminación | 1,5 mm² | 10 A |
| C2 — Tomas generales | Toma 16 A | 2,5 mm² | 16 A |
| C3 — Cocina/horno | Toma 25 A | 6 mm² | 25 A |
| C4 — Lavadora/lavavajillas/termo | Toma 16 A | 4 mm² | 20 A |
| C5 — Baño y cocina (tomas 16 A) | Toma 16 A | 2,5 mm² | 16 A |
| C8 — Calefacción eléctrica | Calefacción | 6 mm² | 25 A |
| C9 — Aire acondicionado | Motor | 6 mm² | 25 A |

El alumno debe **calcular la caída de tensión** en cada circuito. ITC-BT-19 limita la caída a ≤ 3% desde el origen de la instalación interior hasta cualquier punto de utilización:

```
ΔU (%) = (2 × L × I) / (γ × S × U) × 100
```

donde γ = 56 m/(Ω·mm²) para cobre, L en metros, I en amperios, S en mm², U = 230 V.

Ejemplo para C3 (P = 5.400 W → I = 23,5 A, L = 15 m, S = 6 mm²):

```
ΔU = (2 × 15 × 23,5) / (56 × 6 × 230) × 100 = 0,91 % → cumple ≤ 3%
```

### Selección del interruptor diferencial

ITC-BT-24 exige protección diferencial en toda instalación de vivienda. La selección debe cumplir IEC 61008-1 (UNE-EN 61008-1):

- **Sensibilidad 30 mA**: circuitos con presencia de personas — protección directa contra contacto
- **Sensibilidad 300 mA**: cabecera general — protección contra incendios
- **Tipo AC**: cargas puramente sinusoidales
- **Tipo A**: obligatorio cuando hay electrónica de potencia (variadores, cargadores, LED drivers) — detecta corrientes de falta pulsantes y con componente continua

El proyecto debe incluir la **coordinación temporal**: el tiempo de disparo del diferencial selectivo de cabecera (tipo S, ≥ 0,06 s de retardo) debe ser superior al del diferencial de grupo (tipo estándar, disparo instantáneo < 0,04 s), garantizando selectividad vertical.

---

## Proyecto tipo 2: cuadro de mando con arranque directo de motor trifásico

Para FP de grado superior (Sistemas Electrotécnicos y Automatizados), el proyecto de referencia es un cuadro de distribución BT con motor trifásico de jaula.

El alumno dimensiona la protección del motor según **IEC 60947-4-1** (UNE-EN 60947-4-1). Ejemplo con motor 7,5 kW, 400 V, cosφ = 0,85, η = 90 %:

```
In = P / (√3 × U × cosφ × η) = 7.500 / (1,732 × 400 × 0,85 × 0,90) = 14,2 A
```

Selección de protecciones:

| Elemento | Parámetro de ajuste | Criterio normativo |
|---|---|---|
| Relé térmico | 1,0 × In a 1,15 × In → 14,2 – 16,3 A | IEC 60947-4-1, cl. 8.2 |
| Contactor | Categoría AC-3 (arranque directo jaula) | IEC 60947-4-1, tabla 2 |
| Fusibles gG o guardamotor | ≤ 2,5 × In para coordinación tipo 2 | IEC 60947-4-1, anexo B |
| PIA de cabecera (curva D) | In ≥ 1,25 × In_motor | IEC 60898-1, curva D |

La complejidad de este proyecto es la **selectividad**: el PIA general del cuadro no debe disparar antes que la protección de rama. Esto exige verificar que la corriente de cortocircuito en el embarrado supera el umbral magnético del guardamotor (típicamente 12 × In_guardamotor), pero que la curva I²t del PIA general no alcanza la energía de fusión de la protección de rama.

---

## Proyecto tipo 3: verificación y acta de puesta en servicio (IEC 60364-6)

Este proyecto no tiene montaje nuevo: el alumno recibe una instalación (con fallos introducidos deliberadamente) y debe emitir una **acta de verificación** conforme a IEC 60364-6 / UNE-HD 60364-6.

### Medidas obligatorias

**1. Resistencia de aislamiento (Megger 500 V CC)**

Según IEC 60364-6, tabla 6A:

| Tensión nominal del circuito | Tensión de ensayo (CC) | Resistencia mínima |
|:---:|:---:|:---:|
| ≤ 50 V (MBTS/MBTP) | 250 V | 0,25 MΩ |
| ≤ 500 V | 500 V | 0,5 MΩ |
| > 500 V | 1.000 V | 1,0 MΩ |

Se mide entre: L-N (cargas desconectadas), L-PE y N-PE. Un valor < 1 MΩ en instalación nueva indica humedad, daño mecánico del aislante o conexión incorrecta de tierra.

**2. Impedancia de bucle de fallo Zs**

La impedancia del bucle fase-PE determina si el magnetotérmico disparará dentro del tiempo máximo de IEC 60364-4-41. Para un PIA 16 A curva C en un esquema TT:

```
I_inst = 10 × In = 10 × 16 = 160 A
Zs_máx = U₀ / I_inst = 230 / 160 = 1,44 Ω
```

Si el comprobador de bucle mide Zs > 1,44 Ω, el magnetotérmico no garantiza desconexión en tiempo seguro — se requiere diferencial 30 mA o corrección del circuito de tierra.

**3. Continuidad del conductor de protección (CPE)**

Resistencia entre el borne de tierra del cuadro y cada masa metálica accesible: ≤ 1 Ω. Valores superiores indican conexión deficiente o conductor seccionado.

---

## Criterios de diseño de un proyecto pedagógicamente eficaz

![Guía de selección](/images/como-ensenar-electricidad-con-proyectos-practicos-3.jpg)

Un proyecto de taller es eficaz cuando obliga al alumno a tomar decisiones técnicas justificadas. Criterios para el docente:

**Una sola variable de decisión por sesión.** No pidas que el alumno elija sección, calcule caída de tensión, seleccione el diferencial y monte el circuito en la misma sesión. Cada sesión tiene una decisión técnica como objetivo de aprendizaje.

**Introduce fallos conocidos y controlados.** Una instalación con neutro y PE invertidos, o con un conductor de protección discontinuo, obliga al alumno a medir y diagnosticar — no solo a montar. Esto entrena la competencia más escasa en técnicos junior.

**Exige documentación como entregable final.** El alumno debe entregar: esquema unifilar conforme a UNE-EN 60617, memoria de cálculo con valores numéricos y acta de verificación con medidas reales. Sin documentación técnica, no hay proyecto.

**Evalúa decisiones, no ejecución.** La evaluación no es "ha conectado correctamente" sino "¿por qué ha elegido ese calibre?" y "¿qué pasaría si pusiera el diferencial antes del magnetotérmico general?". Las preguntas de diagnóstico revelan comprensión real.

**Usa instrumentación real desde segundo año.** Un comprobador básico de continuidad no mide impedancia de bucle ni tiempo de disparo del diferencial. La introducción del Megger 500 V y el comprobador de bucle (tipo Fluke 1663 o Metrel MI3102H) diferencia a los técnicos que saben poner en servicio de los que solo montan.

---

## Conclusión

La enseñanza de electricidad mediante proyectos prácticos es efectiva cuando los proyectos exigen decisiones normativas verificables instrumentalmente. El triángulo que define un buen proyecto de taller electrotécnico es: **cálculo conforme a REBT/IEC + montaje ejecutado correctamente + verificación instrumental documentada**.

El alumno que complete los tres proyectos descritos — instalación de vivienda (ITC-BT-25), cuadro industrial con motor (IEC 60947-4-1) y acta de verificación (IEC 60364-6) — habrá desarrollado las competencias mínimas para la puesta en servicio de instalaciones BT y estará preparado para el proceso de habilitación como instalador autorizado según ITC-BT-03. La clave no es hacer más proyectos — es hacer tres bien, con toda la cadena de decisión técnica visible y evaluada.
