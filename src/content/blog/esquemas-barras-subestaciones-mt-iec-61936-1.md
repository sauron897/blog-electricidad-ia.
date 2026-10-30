---
title: "Esquemas de barras en subestaciones MT: IEC 61936-1"
description: "Análisis técnico de las configuraciones de barras en subestaciones MT: barra simple, doble, anillo e interruptor y medio. Fiabilidad e Icw según IEC 61936-1 y UNE-EN IEC 61936-1:2021."
pubDate: 2026-10-30
keywords: ["esquema barras subestacion MT", "IEC 61936-1", "barra simple doble MT", "fiabilidad subestacion media tension", "barra doble interruptor medio"]
author: "Editor"
---

La elección del esquema de barras en una subestación de media tensión (MT) determina directamente su fiabilidad, flexibilidad operativa y coste de ciclo de vida. La norma **UNE-EN IEC 61936-1:2021** — que transpone la IEC 61936-1:2021 (Ed. 3) — establece las reglas comunes de diseño para instalaciones eléctricas con tensiones nominales superiores a 1 kV en corriente alterna, incluyendo los principios de disposición del aparellaje y los sistemas de barras colectoras.

Para subestaciones MT (generalmente entre 6 kV y 36 kV en España), el diseño del esquema de barras no puede disociarse de los parámetros de cortocircuito, la corriente admisible de las barras y los tiempos de operación de las protecciones. Ignorar cualquiera de estos factores equivale a diseñar para el mejor caso posible, no para la instalación real.

## Parámetros de barra colectora: corriente nominal e Icw

Antes de seleccionar una configuración de barras, es imprescindible verificar que el sistema elegido soporta la **corriente de corta duración admisible (Icw)** sin deformación permanente. Según IEC 61936-1:2021 y la norma de aparamenta IEC 62271-200, el ensayo de Icw se realiza durante 1 segundo.

Los valores de barras prefabricadas según GElectrical/IEC son representativos de los productos de aparamenta comercial:

| Denominación | Corriente nominal (A) | R (mΩ/m) | X (mΩ/m) | Icw (kA, 1 s) | Ipk (kA) |
|---|---|---|---|---|---|
| 630A-SCP-AL | 630 | 0,084 | 0,023 | 22 | 48 |
| 1250A-SCP-AL | 1250 | 0,055 | 0,015 | 45 | 99 |
| 2000A-SCP-AL | 2000 | 0,030 | 0,011 | 48 | 106 |
| 3200A-SCP-AL | 3200 | 0,019 | 0,006 | 96 | 211 |
| 1600A-SCP-CU | 1600 | 0,027 | 0,015 | 51 | 112 |
| 3200A-SCP-CU | 3200 | 0,013 | 0,007 | 102 | 224 |
| 6300A-SCP-CU | 6300 | 0,006 | 0,004 | 106 | 232 |

En subestaciones MT con Icc máximo de 20 kA (típico para redes de 20 kV de distribución urbana), una barra de aluminio SCP-AL de 630 A con Icw = 22 kA satisface el requisito. Para centros de reparto en redes de 66 kV o conexión a redes de transporte donde Icc puede alcanzar los 40 kA, es imprescindible pasar a barras de 3200 A o superiores (Icw ≥ 96 kA).

La **corriente de cresta Ipk** determina los esfuerzos electrodinámicos sobre barras y soportes. Para Icc = 20 kA (valor eficaz simétrico), el pico según IEC 60909-0 con factor de cresta κ = 1,8 resulta:

**Ipk = κ · √2 · Icc = 1,8 × 1,414 × 20 kA = 50,9 kA**

Este valor debe ser inferior al Ipk nominal de la barra elegida. Una barra SCP-AL de 1250 A soporta Ipk = 99 kA, más que suficiente para el caso anterior.

## Configuraciones de barras: tipos y análisis técnico

### 1. Barra simple

El esquema más simple: todos los circuitos conectan a una única barra mediante un interruptor y un seccionador.

**Ventajas:** mínimo coste, menor espacio, menor complejidad operativa.

**Inconveniente crítico:** cualquier falta en la barra o mantenimiento del aparellaje de barra implica la pérdida total de la subestación. El índice SAIDI (duración media de las interrupciones por cliente) se penaliza severamente con esta configuración.

**Aplicación:** centros de transformación MT/BT con un único trafo de hasta 630 kVA, donde la redundancia se provee mediante anillos de la red de distribución aguas arriba.

### 2. Barra simple seccionada

La barra se divide en dos secciones mediante un interruptor de acoplamiento (normalmente abierto). Ante una falta en una sección, solo queda sin servicio esa mitad. Con acoplador automático, el tiempo de recuperación puede ser inferior a 200 ms.

**Aplicación típica:** subestaciones de distribución urbana 20 kV con dos transformadores de potencia (uno por sección), permitiendo mantenimiento con transferencia de carga al acoplador. Es la configuración habitual en subestaciones de distribución de segunda categoría de las grandes distribuidoras en España.

**Criterio de protección:** el relé diferencial de barras (IED según IEC 61850) debe discriminar entre falta en la sección A y falta en la sección B, enviando señal TRIP solo al interruptor de la sección fallida y al acoplador.

### 3. Barra doble

Dos barras paralelas conectadas mediante un acoplador. Cada campo puede conectarse a cualquiera de las dos barras mediante un selector. Este esquema permite:
- Mantenimiento de una barra sin interrumpir el servicio.
- Separación de fuentes (generación vs. red) en barras distintas.
- Mayor flexibilidad en la gestión de cargas y flujos de potencia.

**Inconveniente:** requiere el doble de selectores que la barra simple, aumentando el coste y el riesgo de maniobra incorrecta. La norma IEC 61936-1:2021 exige señalización de posición de todos los elementos de maniobra, habitualmente implementada con contactos auxiliares conectados al sistema SCADA.

**Aplicación:** subestaciones AT/MT de REE en 220 kV y 400 kV, y en MT para industrias con continuidad de suministro nivel A (hospitales, plantas petroquímicas, industrias de proceso continuo).

### 4. Interruptor y medio (Breaker-and-a-half)

Cada par de circuitos comparte tres interruptores (1,5 interruptores por circuito). Permite mantener cualquier interruptor sin perder ningún circuito.

**Aplicación:** subestaciones AT/MAT críticas, centrales generadoras (interconexión unidad-transformador elevador), infraestructuras de transporte sensibles. En MT es excepcional por su coste.

### 5. Esquema en anillo (Ring bus / Ring Main Unit)

Todos los circuitos se conectan en anillo. En caso de falta en cualquier interruptor, el suministro se mantiene a través del camino alternativo del anillo.

**Ventaja en distribución MT:** la topología en anillo es la base de las **Unidades de Red en Anillo (RMU)** normalizadas en la distribución secundaria de 20 kV española (celdas tipo 2LVC, 3LVC o 2LVP según especificaciones de cada distribuidora).

**Limitación:** la adición de nuevos circuitos requiere interrumpir el servicio o disponer de un campo de reserva. Para más de 6 alimentadores, el anillo se vuelve complejo de operar y proteger.

**Corriente de cortocircuito en anillo:** en una falta sobre la barra del anillo, la corriente proviene de dos ramas simultáneamente. El cálculo de Icc debe considerar la contribución de ambos caminos del anillo, lo que puede elevar la corriente de falta hasta un 40% respecto al esquema radial equivalente para la misma impedancia de red.

## Tabla comparativa de configuraciones

| Esquema | Fiabilidad | Flexibilidad | Coste relativo | Aplicación típica MT |
|---|---|---|---|---|
| Barra simple | Baja | Nula | 1,0 | CT hasta 630 kVA |
| Barra simple seccionada | Media | Media | 1,3 | Distribución urbana 20 kV |
| Barra doble | Alta | Alta | 2,0 | Industria nivel A |
| Interruptor y medio | Muy alta | Muy alta | 3,5 | AT/MAT crítica |
| Anillo (RMU) | Media-Alta | Media | 1,5 | Distribución MT secundaria |

Los costes relativos son orientativos e incluyen aparellaje y obra civil; el coste unitario de un campo de MT con aparamenta bajo gas SF₆ o vacío (IEC 62271-200) oscila entre 8.000 € y 35.000 € según configuración y tensión nominal.

## Criterios de diseño según IEC 61936-1:2021

La sección 5 de IEC 61936-1:2021 establece que el diseño de la instalación debe garantizar:

**1. Nivel de aislamiento:** para 20 kV (Um = 24 kV), la tensión de ensayo al impulso tipo rayo (BIL) mínima es **125 kV de cresta**. Las distancias mínimas en el aire para 24 kV son:
- Fase-fase: 270 mm (distancia de seccionamiento en el aire)
- Fase-tierra: 220 mm

Para 36 kV (Um = 40,5 kV), el BIL es 185 kV de cresta, con distancias fase-fase ≥ 480 mm.

**2. Corriente de cortocircuito:** la instalación debe dimensionarse para la Icc máxima previsible en el punto de conexión, incluyendo la contribución de generación distribuida conectada aguas abajo. En redes de 20 kV, los valores típicos son:
- Redes urbanas densas: 16-20 kA (1 s)
- Redes suburbanas: 8-12 kA (1 s)
- Redes rurales: 3-6 kA (1 s)

**3. Segregación funcional:** IEC 61936-1 exige la separación física o funcional entre el área de operación normal y las zonas de alta tensión. En subestaciones compactas con aparamenta bajo gas SF₆ o vacío, esta segregación se obtiene con la propia envolvente metálica de la celda (metal-enclosed o metal-clad según IEC 62271-200).

**4. Sistemas de protección:** la norma remite a IEC 60255 para los relés de protección y a **IEC 61850** para la comunicación entre IEDs. Para subestaciones con barra doble o interruptor-y-medio, la protección de barras con relé diferencial de barras (función ANSI 87B) es prácticamente obligatoria y debe garantizar tiempo de actuación total ≤ 40 ms para evitar daños permanentes sobre el aparellaje.

**5. Mantenimiento sin interrupción:** la configuración mínima que permite realizar mantenimiento sobre un interruptor sin interrumpir el servicio es la barra simple seccionada con acoplador o la barra doble. Este es el requisito que la mayoría de distribuidoras en España imponen a partir de subestaciones con potencia instalada superior a 5 MVA.

## Criterios de selección en obra

La selección práctica del esquema de barras puede resumirse en la siguiente lógica de decisión:

1. **¿La carga admite interrupciones de servicio prolongadas (> 4 h)?** → Barra simple es suficiente.
2. **¿Hay dos fuentes de alimentación o dos transformadores?** → Barra simple seccionada o barra doble.
3. **¿La instalación es industrial de proceso continuo o infraestructura crítica?** → Barra doble con protección diferencial de barras (87B).
4. **¿Es una subestación de AT/MAT de transporte o generación?** → Interruptor y medio o barra doble con doble interruptor por campo.
5. **¿Es distribución secundaria MT en anillo?** → RMU con esquema de anillo.

La corriente de cortocircuito del punto de conexión, calculada según **IEC 60909-0**, es el parámetro que dicta el Icw mínimo requerido a toda la aparamenta y al sistema de barras. Este valor debe calcularse tanto para la condición de máxima contribución (máxima generación en red) como de mínima, ya que la segunda condiciona la sensibilidad de los relés de sobreintensidad.

## Conclusión

El esquema de barras en subestaciones MT no es una decisión de catálogo: requiere calcular Icc según IEC 60909, verificar Icw e Ipk de la aparamenta, definir el nivel de continuidad exigible y aplicar los criterios de IEC 61936-1:2021 en cuanto a distancias de aislamiento y segregación funcional. Para subestaciones de distribución urbana, la barra simple seccionada con acoplador automático y protección diferencial de barras es el equilibrio óptimo entre fiabilidad y coste. Para industria de proceso continuo o generación, la barra doble con función 87B es el estándar operativo.
