---
title: "Alumbrado de emergencia BT: ITC-BT-28, UNE-EN 60598-2-22 y EN 1838"
description: "Guía técnica para ingenieros: tipos de alumbrado de emergencia, requisitos fotométricos según EN 1838, criterios de selección de luminarias y verificación según ITC-BT-28."
pubDate: 2026-11-11
keywords: ["iluminacion emergencia", "alumbrado evacuacion ITC-BT-28", "UNE-EN 60598-2-22", "EN 1838 lux emergencia", "alumbrado antipánico"]
author: "Editor"
---

El alumbrado de emergencia en instalaciones BT está regulado en España por tres fuentes normativas que el proyectista debe conocer y saber combinar: la ITC-BT-28 del REBT (que define los requisitos eléctricos y de instalación), la UNE-EN IEC 60598-2-22 (que rige la fabricación y el marcado de las luminarias) y la EN 1838:2013 (que establece los requisitos fotométricos de los sistemas). Superpone a ellas el DB-SUA 4 del CTE en edificios, donde arquitecto e ingeniero eléctrico comparten responsabilidad. Este artículo desarrolla los criterios técnicos que determinan la selección, el diseño y la verificación del sistema.

## Marco normativo: ITC-BT-28, EN 1838 y CTE DB-SUA 4

La ITC-BT-28 del REBT (Real Decreto 842/2002) aplica a **locales de pública concurrencia**: teatros, cines, hoteles, hospitales, establecimientos comerciales, parkings y similares. Su sección 2.3 exige alumbrado de emergencia en:

- Recorridos de evacuación, escaleras y salidas.
- Locales con riesgo de pánico (superficie ≥ 100 m² o más de 50 personas en centros de trabajo, según INSST NTP-889 referenciada).
- Cuadros de distribución, equipos de lucha contra incendios y primeros auxilios de uso manual.
- Zonas con grupos electrógenos, SAI o cuadros de mando de instalaciones de seguridad.

La **EN 1838:2013** (adoptada como UNE-EN 1838:2014) define tres tipos de alumbrado de emergencia y sus requisitos fotométricos. No es una norma de producto: se complementa con la UNE-EN IEC **60598-2-22:2023** (antigua ed. 2014+A1:2020), que regula la construcción de las luminarias: clase I o II, IP mínimo, marcado de duración y flujo de emergencia (en lúmenes), y los ensayos de tipo y rutina.

El **DB-SUA 4** del CTE (Código Técnico de la Edificación) es obligatorio para edificios sometidos a licencia de obras y suele ser el documento que más exige al proyectista, ya que sus umbrales fotométricos son más exigentes que los de EN 1838 en algunos puntos.

## Tipos de alumbrado de emergencia según EN 1838

| Tipo | Función | Iluminancia mínima (EN 1838) | Tiempo de cambio |
|---|---|---|---|
| **Alumbrado de evacuación** | Rutas hacia salidas | 1 lux en eje de ruta (ancho ≤ 2 m) | ≤ 5 s |
| **Alumbrado antipánico** | Zonas abiertas, previene desorientación | 0,5 lux en zona central (excluyendo borde 0,5 m) | ≤ 5 s |
| **Alumbrado de zona de alto riesgo** | Puestos de trabajo peligrosos | ≥ 10 % de la iluminancia de tarea, mín. 15 lux | ≤ 0,5 s |

La **uniformidad** del alumbrado de evacuación se limita a una relación máxima E_máx / E_mín ≤ 40:1. Para zonas antipánico la relación máxima E_máx / E_mín es también 40:1.

El alumbrado de **señalización** (señales de salida y de equipos de extinción) se regula por la norma de señales de seguridad (ISO 7010 y EN ISO 7010). En instalaciones españolas el DB-SUA 4 remite a CTE DB-SI para la señalización de recorridos.

### Requisitos adicionales EN 1838

- Las luminarias deben instalarse a una altura ≥ 2 m sobre el suelo para limitar el deslumbramiento fisiológico (tabla de intensidades máximas de EN 1838 según ángulo).
- En rutas de evacuación con ancho > 2 m, se trata como dos bandas de 2 m o como alumbrado antipánico.
- El primer punto de luz debe situarse a ≤ 2 m de cada salida, cambio de dirección, escalón, equipo contra incendios o cuadro eléctrico.

## Requisitos de la ITC-BT-28 sobre la instalación eléctrica

La ITC-BT-28 impone condiciones sobre el circuito y la fuente:

- **Autonomía mínima**: 1 hora (coincide con CTE DB-SUA 4 para la mayoría de usos; hospitales, residencias y hoteles de categoría especial requieren 2 h según CTE).
- **Circuito independiente**: el alumbrado de emergencia debe ser un circuito específico, no controlable por los interruptores generales del alumbrado normal. El conductor de fase debe ser de color distinto del de los circuitos normales o estar identificado.
- **Alimentación automática**: la conmutación al modo emergencia debe ser automática ante fallo de la tensión de red (caída por debajo del 70 % de la tensión nominal o interrupción > 0,5 s).
- **Luminarias de tipo no permanente** (NC) o **permanente** (C): las primeras solo encienden en emergencia; las segundas están siempre encendidas. La UNE-EN IEC 60598-2-22 define los ensayos diferenciados para cada modo.
- **IP**: la norma no especifica un IP mínimo genérico, pero la ITC-BT-30 (locales con riesgo de incendio o explosión) y el CTE exigen IP 44 o superior en entornos con polvo, humedad o exposición a proyecciones.

## Selección de luminarias: parámetros clave según UNE-EN IEC 60598-2-22

Los parámetros que el técnico debe verificar en la hoja de producto, siempre conforme a UNE-EN IEC 60598-2-22, son:

| Parámetro | Descripción | Valor típico / requisito |
|---|---|---|
| **Flujo de emergencia (Φ_em)** | Lúmenes declarados en modo emergencia (marcado en la luminaria) | 70 – 500 lm según zona |
| **Duración de emergencia** | Tiempo garantizado al flujo declarado | 1 h mínimo (ITC-BT-28) |
| **Tiempo de conmutación** | Desde fallo red hasta luz de emergencia | ≤ 5 s (evacuación/antipánico) |
| **Tensión de batería** | Ni-Cd o LiFePO₄ sellada | 3,6 V (Ni-Cd) / 3,2 V (LFP) por celda |
| **Vida de batería** | Garantía mínima declarada por fabricante | ≥ 4 años (EN IEC 60598-2-22) |
| **IP** | Protección mecánica y contra agua | IP20 mínimo; IP44 en zonas húmedas |
| **Factor de mantenimiento (FM)** | Degradación del flujo a lo largo de la vida útil | 0,67 – 0,8 según tecnología LED |

El flujo de emergencia declarado por el fabricante ya incluye el rendimiento de la óptica y el estado de la batería a fin de su vida. El proyectista debe comprobar que con ese flujo se alcanzan los niveles de EN 1838 en el peor punto de la ruta, calculados mediante el **método de puntos** (iluminancia directa sumada de cada luminaria visible desde el punto).

### Cálculo simplificado de separación entre luminarias

Para una ruta de evacuación lineal de 2 m de ancho, la separación máxima entre luminarias se puede estimar con la fórmula:

```
d_max = √(Φ_em × η_pared / (E_min × FM))
```

Donde:
- **Φ_em**: flujo de emergencia de la luminaria (lm)
- **η_pared**: factor de reflexión del techo y paredes (típico 0,5 en pasillos)
- **E_min**: iluminancia mínima exigida (1 lux en eje de ruta)
- **FM**: factor de mantenimiento (usar 0,7 para LED con batería Ni-Cd a fin de vida)

Ejemplo: luminaria de 100 lm de emergencia, η = 0,5, FM = 0,7, E_min = 1 lux:

```
d_max = √(100 × 0,5 / (1 × 0,7)) ≈ √71 ≈ 8,4 m
```

En la práctica, la separación real se fija entre 6 y 7 m para garantizar uniformidad E_máx/E_mín ≤ 40:1 y cubrir las necesidades de reflexión real (no perfectamente lambertiana).

## Criterios de selección según tipo de instalación

| Tipo de local | Autonomía | Flujo recomendado | IP | Observaciones |
|---|---|---|---|---|
| Pasillo oficina o comercio | 1 h | 70 – 150 lm | IP20 | Tipo no permanente, NC |
| Escalera protegida | 1 h | 100 – 200 lm | IP20 | Punto en cada rellano |
| Aparcamiento cubierto | 1 h | 150 – 300 lm | IP44 | Humedad y polvo |
| Hospital, quirófano | 2 h | 200 – 500 lm | IP44 | Alumbrado zona alto riesgo ≥ 15 lux |
| Local CPI o extintores | 1 h | 100 lm mínimo | IP20 | Obligatorio 5 lux sobre equipo |
| Cuadro eléctrico BT | 1 h | 100 lm mínimo | IP20 | 5 lux sobre frente de cuadro |

## Verificación y mantenimiento

La UNE-EN 62034:2012 (sistemas de alumbrado de emergencia con autotest) permite luminarias con autotest integrado que registra las pruebas y alarmas en la propia luminaria o en un sistema centralizado. Para instalaciones sin autotest:

- **Ensayo funcional mensual**: verificación visual de encendido (1-2 s con corte de alimentación). Registrar en libro de mantenimiento.
- **Ensayo de duración anual**: desconexión de la red durante 1 hora completa para comprobar que se mantiene el flujo declarado. Verificar iluminancia en puntos críticos con luxómetro.
- **Sustitución de batería**: cada 4 años como mínimo, o antes si el ensayo anual falla.

La ITC-BT-28 no detalla el protocolo de mantenimiento, pero la GUÍA-BT-28 del Ministerio de Industria (disponible en plcmadrid.es) lo recoge y remite al Reglamento de Instalaciones de Protección contra Incendios (RIPCI, RD 513/2017) para la parte de señalización de evacuación.

## Conclusión

El diseño de alumbrado de emergencia requiere que el ingeniero maneje simultáneamente tres normas con distinto alcance: la ITC-BT-28 para la instalación eléctrica, la EN 1838 para los valores fotométricos mínimos, y la UNE-EN IEC 60598-2-22 para validar las características del producto. Los pasos clave son: calcular la separación entre luminarias para garantizar ≥ 1 lux en rutas de evacuación y ≥ 0,5 lux en zonas antipánico con uniformidad ≤ 40:1; seleccionar luminarias con autonomía ≥ 1 h (o 2 h en hospitales) y factor de mantenimiento declarado; verificar IP según condiciones ambientales; y establecer un plan de ensayos con registro documental. Para locales sujetos al CTE (edificios de nueva construcción o reforma), el DB-SUA 4 es el documento de verificación obligatorio y prevalece sobre la ITC-BT-28 cuando impone condiciones más estrictas.
