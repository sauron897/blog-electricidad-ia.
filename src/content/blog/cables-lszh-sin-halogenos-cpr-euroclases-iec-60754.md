---
title: "Cables LSZH sin halógenos: Euroclases CPR e IEC 60754"
description: "Clasificación CPR, Euroclases y selección técnica de cables LSZH según IEC 60754, IEC 61034, IEC 60332 e ITC-BT-28. Valores de ensayo, tablas comparativas y criterios para obra."
pubDate: 2026-11-23
keywords: ["cables LSZH sin halógenos", "IEC 60754", "CPR Euroclases cables", "IEC 61034 emisión humos", "ITC-BT-28 cable sin halógenos"]
author: "Editor"
---

Los cables sin halógenos LSZH (*Low Smoke Zero Halogen*) llevan décadas en catálogos, pero con la entrada en vigor del Reglamento de Productos de Construcción CPR (Reglamento UE 305/2011) y la norma armonizada **EN 50575** la etiqueta "LSZH" por sí sola ha quedado técnicamente insuficiente. Lo que importa ahora es la **Euroclase de reacción al fuego** del cable, que sustituye a la mera declaración de ensayo IEC como criterio normativo en la UE.

Este artículo expone los fundamentos de los ensayos IEC 60754, IEC 61034 e IEC 60332, cómo se articulan con las Euroclases CPR y qué Euroclase exige cada tipo de instalación según ITC-BT-28 y la reglamentación de edificios en España.

---

## Las tres normas IEC de base y sus límites de ensayo

La caracterización de comportamiento al fuego de un cable LSZH descansa en tres familias de ensayo IEC, complementarias e independientes:

### IEC 60754 — Emisión de gases halogenados y corrosividad

**IEC 60754-1** mide el contenido de ácido clorhídrico (HCl) desprendido al quemar los materiales aislantes y de cubierta. El criterio de conformidad exige que la emisión de HCl no supere **5 mg/g** de masa del cable ensayado. Un cable se denomina formalmente "libre de halógenos" solo si supera este ensayo.

**IEC 60754-2** evalúa la acidez y la conductividad de los gases de combustión disueltos en agua:
- pH mínimo: **≥ 4,3**
- Conductividad máxima: **≤ 10 µS/mm**

Algunos productos de alta especificación declaran conductividades de 2,5 µS/mm o inferiores; eso es un valor de producto, no el límite de la norma. La conductividad elevada de los gases de cables PVC convencionales puede superar los 1000 µS/mm, lo que corroe equipos y dificulta la extinción con agua nebulizada.

### IEC 61034 — Densidad de humo (transmisión de luz)

La norma mide la opacidad del humo en una cámara de 3 m³ mediante la transmitancia de un haz de luz. El criterio es:

- **Transmitancia mínima: ≥ 60 %** (cámara de 3 m³, cable en gavilla)

Productos de alto rendimiento alcanzan transmitancias ≥ 80 %, que se corresponden aproximadamente con visibilidades de escape superiores a 10 m en un pasillo real.

### IEC 60332 — Propagación de llama

Tres partes con criterios distintos:

| Norma | Configuración | Criterio de aprobación |
|---|---|---|
| IEC 60332-1-2 | Cable individual, vertical | Zona carbonizada ≤ 50 mm sobre el quemador |
| IEC 60332-2-2 | Cable delgado individual | Zona carbonizada limitada |
| IEC 60332-3-24 | Gavilla de cables, carga 7 L/m | Zona carbonizada ≤ 2,5 m desde el quemador inferior |
| IEC 60332-3-25 | Gavilla, carga 3,5 L/m | Zona carbonizada ≤ 1,5 m |

La clave en instalaciones con bandejas de cables es **IEC 60332-3**: un cable que supera IEC 60332-1 (cable individual) puede propagar llama en gavilla si no ha sido ensayado en la configuración de carga correcta.

---

## Sistema CPR y las Euroclases de reacción al fuego

El Reglamento CPR (305/2011/UE), desarrollado para cables por la norma armonizada **EN 50575:2016+A1:2022**, establece siete Euroclases con subclasificaciones de humo (s), goteo (d) y acidez (a):

| Euroclase | Propagación de llama | Calor liberado | Referencia ensayo |
|---|---|---|---|
| **Aca** | No propagante (no combustible) | — | EN 50575, ISO 1716 |
| **B1ca** | Muy limitada | FIGRA ≤ 2500 W/s | EN 50399 + EN 60332-3-24 |
| **B2ca** | Limitada | FIGRA ≤ 10 000 W/s | EN 50399 + EN 60332-3-24 |
| **Cca** | Media | FIGRA ≤ 40 000 W/s | EN 50399 + EN 60332-3-24 |
| **Dca** | Peor que Cca | — | EN 50399 |
| **Eca** | Solo cable individual | Supera EN 60332-1-2 | EN 60332-1-2 |
| **Fca** | No clasificado | — | — |

Los sufijos se declaran independientemente:

- **s1a / s1b / s2 / s3** — densidad de humo y transmitancia (s1a: transmitancia ≥ 80 %, s1b: ≥ 60 %, s2: < 60 %)
- **d0 / d1 / d2** — goteo inflamado (d0: ninguno, d2: libre)
- **a1 / a2 / a3** — acidez de gases (a1: pH ≥ 4,3 y conductividad ≤ 2,5 µS/mm, a2: ≤ 10 µS/mm)

Un cable declarado **Cca-s1b,d1,a1** es el estándar mínimo habitual en edificios de pública concurrencia en España para circuitos no críticos.

> **Nota de coherencia con IEC**: la Euroclase "a1" exige conductividad ≤ 2,5 µS/mm, más restrictiva que el límite general de IEC 60754-2 (10 µS/mm). Un cable con declaración IEC 60754-2 aprobada puede no alcanzar sufijo "a1" si su conductividad está entre 2,5 y 10 µS/mm.

---

## Obligatoriedad en España: ITC-BT-28, CTE y RD 842/2002

### ITC-BT-28: locales de pública concurrencia

La **ITC-BT-28** del REBT (Real Decreto 842/2002) exige en los circuitos de instalaciones de locales de pública concurrencia (teatros, cines, discotecas, hospitales, superficies comerciales > 300 m², etc.) que los cables cumplan **libre de halógenos con baja emisión de humos y gases tóxicos**. En la práctica, esto se ha traducido en la exigencia de designación **H07Z1-K** (flexible, 450/750 V) o **RZ1-K (AS)** (0,6/1 kV) en instalaciones fijas.

Con la aplicación del CPR desde julio de 2017 (período transitorio cerrado), la exigencia ya no es "LSZH" como característica de material sino una **Euroclase mínima certificada en la Declaración de Prestaciones (DoP)**:

| Tipo de local (ejemplos) | Euroclase mínima orientativa |
|---|---|
| Edificios de pública concurrencia (ITC-BT-28) | **Cca-s1b,d1,a1** |
| Túneles viarios > 500 m | **B2ca-s1a,d1,a1** |
| Edificios residenciales (uso general) | **Dca-s2,d2,a3** |
| Locales industriales con riesgo de incendio (ITC-BT-29) | **Cca** o superior según evaluación de riesgo |
| Infraestructuras críticas (centros de datos, hospitales zona UCI) | **B1ca-s1a,d0,a1** recomendado |

> Los valores de Euroclase orientativa proceden de las guías de aplicación del CPR en España (AENOR, CEPCO). La normativa de edificios (CTE DB-SI) no prescribe directamente Euroclases de cables, sino que remite a su normativa sectorial específica.

### Identificación en el cable

La EN 50575 obliga a que la Euroclase figure **serigrafiada en la cubierta** del cable o en el embalaje como parte de la Declaración de Prestaciones CPR. La verificación en obra es directa: la cubierta debe mostrar el código Euroclase completo (p. ej. `Cca-s1b,d1,a1 EN50575`).

---

## Criterios de selección técnica en obra

La selección correcta sigue este orden de decisión:

1. **Determinar la Euroclase exigida** según tipo de local y normativa aplicable (ITC-BT-28, reglamentación de protección contra incendios, CTE DB-SI, pliegos de cliente).

2. **Verificar la designación del cable**:
   - Cables flexibles 450/750 V: **H07Z1-K** (sección 1,5–240 mm²) o **ES07Z1-K** (designación española)
   - Cables unipolares y multipolares 0,6/1 kV: **RZ1-K (AS)** o **RZ1-OL** para enterrado
   - Cables de control y señal: **SZ1-K** o equivalente con declaración CPR

3. **Comprobar la DoP del fabricante**: la Declaración de Prestaciones (disponible en web del fabricante o marcado CE del embalaje) confirma Euroclase, número de norma y organismo notificado. No es suficiente con que el catálogo indique "LSZH".

4. **Revisar coherencia con IEC 60332-3**: en instalaciones con bandejas de cables de alta carga (> 7 L/m), exigir que el cable haya superado **IEC 60332-3-24** además de la Euroclase CPR, ya que el CPR evalúa con la misma carga pero el informe del fabricante puede detallar el comportamiento a otras configuraciones de densidad.

5. **Temperatura de servicio**: los cables XLPE (aislamiento de polietileno reticulado libre de halógenos, designación `Z1`) admiten 90 °C en servicio permanente y 250 °C en cortocircuito. Los cables EPR (caucho etileno-propileno) alcanzan 90 °C o 110 °C según clase. Verificar que la Imax del tramo no supera la capacidad del cable a la temperatura real del canal.

6. **Segregación con otros tipos de cable**: los cables PVC en la misma bandeja pueden liberar HCl y degradar los LSZH adyacentes en caso de incendio. En instalaciones mixtas, la segregación física o el uso exclusivo de cables LSZH en toda la bandeja es la práctica recomendada.

---

## Conclusión

La denominación LSZH describe propiedades materiales; la **Euroclase CPR** es la declaración de prestaciones de producto legalmente válida en la UE desde 2017. Para un técnico en obra, el flujo es:

1. Leer la Euroclase exigida en el proyecto o en la normativa del local.
2. Exigir al proveedor la **DoP** con esa Euroclase o superior.
3. Verificar la serigrafía del cable antes de tender.
4. Documentar la clase en el certificado de instalación.

Los ensayos IEC 60754, IEC 61034 e IEC 60332 siguen siendo la referencia de ingeniería para comparar materiales y especificar con precisión en proyectos internacionales o contratos donde el CPR no aplica directamente, pero dentro del mercado UE el CPR es el único criterio de conformidad de producto.
