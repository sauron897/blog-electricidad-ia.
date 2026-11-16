---
title: "Termografía infrarroja en instalaciones eléctricas: ISO 18434-1 y severidad NFPA 70B"
description: "Protocolo de inspección termográfica según ISO 18434-1, clasificación de defectos por ΔT y criterios de severidad NFPA 70B para instalaciones eléctricas BT/MT."
pubDate: 2026-11-16
keywords: ["termografía infrarroja instalaciones eléctricas", "ISO 18434-1 termografía", "clasificación defectos ΔT severidad", "mantenimiento predictivo termografía BT MT"]
author: "Editor"
---

## Introducción

La termografía infrarroja es hoy la técnica de mantenimiento predictivo con mayor coste-eficacia para instalaciones eléctricas BT y MT. A diferencia del análisis de vibraciones o la ultrasonografía, puede ejecutarse bajo tensión y con la instalación en servicio, sin parada del proceso. Su base física es directa: cualquier defecto eléctrico —mala conexión, desequilibrio de carga, aislamiento deteriorado, condensadores desequilibrados— disipa energía como calor proporcional a R·I², generando un gradiente de temperatura detectable antes de que se produzca la avería.

La norma de referencia para el procedimiento general de inspección es **ISO 18434-1:2008** ("Condition monitoring and diagnostics of machines — Thermography — Part 1: General procedures"), confirmada en 2023. Los criterios de clasificación de severidad más extendidos en instalaciones eléctricas provienen de **NFPA 70B** (edición 2023, ahora normativa en EEUU) y de **ANSI/NETA MTS** (Table 100.18). En Europa, la guía **IEC 60300-3-11** enmarca el proceso de toma de decisiones en mantenimiento centrado en fiabilidad, dentro del cual se integra la termografía como técnica de condición.

La carga mínima requerida, la corrección de emisividad y la geometría de inspección son los tres puntos donde más fallan las inspecciones en campo. Este artículo los cubre con los valores numéricos necesarios para que los resultados sean defendibles en un informe técnico.

---

## Fundamento físico: emisividad y ley de Stefan-Boltzmann

Una cámara de infrarrojos mide la **radiación emitida** por una superficie. La potencia radiada por unidad de área sigue la ley de Stefan-Boltzmann:

```
P = ε · σ · T⁴
```

donde σ = 5,67 × 10⁻⁸ W/(m²·K⁴) y ε es la emisividad de la superficie (adimensional, 0 ≤ ε ≤ 1). La cámara convierte la radiación medida en temperatura aparente T_ap asumiendo un ε programado. Si el ε real difiere del programado, la temperatura indicada es incorrecta. El error puede superar los 50 °C en metales brillantes.

| Material | Condición | Emisividad ε |
|---|---|---|
| Cobre desnudo | Brillante (nuevo) | 0,03 – 0,05 |
| Cobre | Oxidado | 0,70 – 0,80 |
| Aluminio | Anodizado / pintado | 0,80 – 0,95 |
| Aluminio | Brillante (nuevo) | 0,04 – 0,06 |
| PVC (aislamiento cable) | — | 0,91 – 0,95 |
| XLPE (aislamiento cable) | — | 0,90 – 0,94 |
| Resina epoxi (barra encapsulada) | — | 0,80 – 0,90 |
| Cinta de alta emisividad | Adhesiva | ≈ 0,95 |

**Consecuencia práctica:** inspeccionar barras de cobre desnudo brillante (ε < 0,05) produce temperaturas aparentes muy alejadas de la real. La solución estándar es aplicar **cinta de alta emisividad** (ε ≈ 0,95) sobre el punto de medida antes de la inspección, o usar la temperatura diferencial entre fases bajo la misma carga, donde el error sistemático de ε se cancela si ambas fases tienen el mismo acabado.

---

## Protocolo de inspección según ISO 18434-1

### Condiciones previas: carga mínima del 40 %

La termografía no es válida si el circuito trabaja por debajo del **40 % de la carga nominal** (ISO 18434-1, apartado 7.4). Por encima del 60 % los gradientes son fiables. El fundamento es la dependencia cuadrática del calor generado en las resistencias de contacto:

```
Q = Rc · I²
```

A 40 % de carga: Q = Rc · (0,4 · In)² = 0,16 · Rc · In². Es decir, solo el 16 % del calor de plena carga. Un defecto que producirá ΔT = 40 °C a plena carga genera apenas ΔT ≈ 6,4 °C a 40 % de carga, por debajo del umbral detectable con la mayoría de cámaras de campo.

Cuando no es posible operar por encima del 40 %, se aplica la **corrección de temperatura diferencial por carga**:

```
ΔT_corr = ΔT_med · (In / Imed)²
```

donde In es la corriente nominal e Imed la corriente medida durante la inspección.

### Geometría de inspección

- **Ángulo de incidencia** ≤ 30° respecto a la normal de la superficie. Por encima de este ángulo, la emisividad efectiva decrece por el efecto coseno y la temperatura aparente puede subestimarse hasta 10 °C en superficies mate, más en metales.
- **Distancia de trabajo**: viene determinada por el **IFOV** (*Instantaneous Field of View*) de la cámara y el tamaño del defecto. Para resolver un punto de 10 mm el IFOV debe ser ≤ 10 mm a la distancia de trabajo. Ejemplo: cámara de 320 × 240 px con óptica de 25°, IFOV ≈ 1,36 mrad → resolución de 1 mm a 0,73 m de distancia; para 10 mm de resolución mínima, se puede trabajar hasta 7,3 m.
- **Estado térmico estacionario**: esperar ≥ 15 min tras un cambio de carga antes de capturar imágenes. Transformadores de distribución y motores de alta masa térmica pueden requerir > 30 min.

---

## Clasificación de defectos por temperatura diferencial ΔT

La clasificación de severidad se basa en el **ΔT respecto a un componente de referencia** bajo la misma carga —por ejemplo, la misma fase en un circuito trifásico equilibrado— o respecto a la temperatura ambiente cuando no existe referencia comparable.

### Tabla 1 — Clasificación por ΔT sobre componente de referencia (NFPA 70B / NETA MTS)

| Clase | ΔT sobre referencia | Prioridad | Acción recomendada |
|---|---|---|---|
| 1 | 1 – 10 °C | Baja | Monitorizar; reparar en próxima parada programada |
| 2 | 11 – 30 °C | Media | Reparar en la próxima parada planificada (< 3 meses) |
| 3 | 31 – 60 °C | Alta | Programar reparación urgente (< 2 semanas) |
| 4 | > 60 °C | Crítica | Desconexión inmediata o reducción de carga hasta reparar |

### Tabla 2 — Clasificación por ΔT sobre temperatura ambiente

| Clase | ΔT sobre T_ambiente | Prioridad |
|---|---|---|
| 1 | < 15 °C | Baja |
| 2 | 15 – 40 °C | Media |
| 3 | 40 – 70 °C | Alta |
| 4 | > 70 °C | Crítica |

**Límites adicionales por tipo de equipo:**

- **Transformadores en aceite (IEC 60076-2):** temperatura máxima del devanado = temperatura media del aceite + 65 K de gradiente. Para aceite a 80 °C en servicio, el bobinado no debe superar 145 °C. Desde el exterior, la termografía detecta variaciones en la carcasa o radiadores, no directamente el bobinado.
- **Motores IE3, aislamiento clase F (IEC 60034-1):** temperatura máxima del bobinado = 155 °C; margen de seguridad de 10 K → T_max = 145 °C. En la carcasa, una temperatura superficial > 90 °C (con T_ambiente = 25 °C, ΔT > 65 °C) es indicativa de posible sobrecarga. Verificar con relé de sobreintensidad térmica.
- **Cables BT bajo ITC-BT-19 / IEC 60364-5-52:** Iz (intensidad admisible) está dada para T_max del conductor = 70 °C en PVC, 90 °C en XLPE. Una cámara que detecta temperatura superficial de cable XLPE > 75 °C (ambiente 25 °C) indica corriente próxima o superior a Iz.

---

## Causas típicas y patrones de diagnóstico

| Defecto | Patrón termográfico | Causa raíz probable |
|---|---|---|
| Conexión floja en embarrado BT | Punto caliente localizado en tornillo o terminal | Incremento de resistencia de contacto Rc → Q = Rc · I² |
| Fase desequilibrada en cuadro trifásico | Una fase 15–40 °C más caliente que las otras dos | Desequilibrio de carga o conexión de mayor resistencia |
| Cable sobrecargado | Gradiente térmico uniforme a lo largo del conductor | I > Iz (ITC-BT-19 / IEC 60364-5-52) |
| Condensador de batería FP descompensado | Escalón o celda más fría que el resto | Condensador fuera de servicio o deteriorado |
| MCB con elevada R_int | Carcasa más caliente que MCBs adyacentes bajo igual corriente | Fatiga de contactos por cortocircuitos repetidos |
| Cable MT XLPE con defecto dieléctrico | Zona caliente difusa en trazado (con sensor fibra óptica distribuida) | Descarga parcial por envejecimiento; verificar con medida de descargas parciales (IEC 60270) |

---

## Criterios de selección de cámara termográfica para inspecciones eléctricas

| Parámetro | Mínimo aceptable | Recomendado (industrial BT/MT) |
|---|---|---|
| Resolución del detector | 160 × 120 px | 320 × 240 px o superior |
| NETD | ≤ 100 mK | ≤ 50 mK |
| Rango de temperatura | –20 °C a 350 °C | –20 °C a 650 °C |
| Exactitud | ±3 °C o ±3 % | ±2 °C o ±2 % |
| Óptica intercambiable | No necesaria | Sí (macro, teleobjetivo) |

La exactitud de ±2 °C o ±2 % (lo que sea mayor) está especificada por ISO 18434-1 como requisito mínimo para inspecciones que generen informes de mantenimiento.

Para **inspecciones bajo tensión en MT** (1 kV a 36 kV), la cámara no sustituye los requisitos de seguridad: distancia de trabajo conforme a **IEC 60900** y EPI aislante de clase correspondiente. La inspección termográfica en BT con tensiones hasta 1 kV requiere guantes clase 00 o clase 0 según el nivel de riesgo de arco (NFPA 70E / IEC 61482-1-2).

---

## Flujo de trabajo recomendado para inspecciones periódicas

1. **Revisión previa de documentación:** planos de cuadros, corrientes nominales, histórico de incidencias. Define los puntos críticos prioritarios.
2. **Verificación de carga:** confirmar I_med ≥ 40 % I_n en cada circuito a inspeccionar; registrar corrientes con pinza amperimétrica y anotar junto al termograma.
3. **Configurar ε en la cámara:** aplicar cinta de alta emisividad (ε ≈ 0,95) sobre metales brillantes para medida absoluta; para ΔT relativo entre fases, el error de ε se cancela parcialmente.
4. **Captura de imágenes:** ángulo ≤ 30°, estado estacionario, documentar coordenadas de cada imagen y hora de captura.
5. **Clasificación de severidad:** asignar Clase 1–4 a cada excepción; usar Tabla 1 (ΔT sobre referencia) como primera opción.
6. **Informe:** fotografía visible + termograma en paleta isotérmica + ΔT medido + clase de severidad + acción recomendada. ISO 18434-1 especifica el contenido mínimo.
7. **Re-verificación tras reparación:** confirmar reducción de ΔT a Clase 1 o inferior bajo condiciones de carga equivalentes.

**Frecuencia mínima:** NFPA 70B (edición 2023) exige inspección termográfica al menos cada **12 meses** para los activos designados en el programa de mantenimiento eléctrico (EMP). En instalaciones de alta criticidad (hospitales, centros de datos, procesos continuos), la frecuencia recomendada es semestral.

---

## Conclusión

La termografía infrarroja proporciona resultados fiables en instalaciones eléctricas BT/MT siempre que se respeten tres condiciones: carga operativa ≥ 40 % de la nominal, ángulo de incidencia ≤ 30° y emisividad correctamente configurada o corregida. La clasificación de severidad en cuatro clases (ΔT 1–10 / 11–30 / 31–60 / >60 °C respecto a referencia) según NFPA 70B y ANSI/NETA MTS traduce directamente la temperatura medida en urgencia de acción, desde monitorización hasta desconexión inmediata. Integrar la termografía en un plan de mantenimiento eléctrico documentado permite además cumplir los requisitos de verificación periódica de instalaciones BT establecidos en **IEC 60364-6** e **ITC-BT-5** del REBT.
