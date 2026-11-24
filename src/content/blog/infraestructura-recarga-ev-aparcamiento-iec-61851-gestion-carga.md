---
title: "Infraestructura de recarga EV en aparcamientos: IEC 61851-1 y ITC-BT-52"
description: "Dimensionado eléctrico, modos de carga IEC 61851-1, protecciones y gestión inteligente de carga para aparcamientos con EVSE. Valores numéricos, tablas comparativas y criterios ITC-BT-52."
pubDate: 2026-11-24
keywords: ["infraestructura recarga EV aparcamiento", "IEC 61851 modos de carga", "ITC-BT-52 vehiculo electrico", "gestión carga dinámica EVSE"]
author: "Editor"
---

El despliegue masivo de EVSE (*Electric Vehicle Supply Equipment*) en aparcamientos residenciales e industriales es uno de los retos actuales con mayor impacto en el diseño de instalaciones BT. No basta con enchufar cargadores: la concurrencia de cargas, la selección correcta de protecciones y la implementación de gestión inteligente determinan si la infraestructura es viable sin ampliar la potencia contratada. Este artículo desarrolla el proceso de dimensionado desde los modos de carga definidos en IEC 61851-1:2017 hasta los criterios de protección exigidos por ITC-BT-52 y la coordinación con un sistema de gestión de carga (SIG).

La normativa de referencia en España es el **Real Decreto 1053/2014** que incorpora la **ITC-BT-52** al REBT, con guía técnica de aplicación actualizada a septiembre de 2024 (revisión 2). A nivel internacional, el estándar de equipos es **IEC 61851-1:2017/COR1:2023** (3.ª edición), que define los cuatro modos de carga y el protocolo de señalización CP.

---

## Modos de carga IEC 61851-1 y señalización CP

IEC 61851-1 establece cuatro modos de carga. La tabla siguiente resume los parámetros eléctricos y el nivel de EVSE requerido:

| Modo | Tensión | Corriente máx. | EVSE | CP signal | Uso típico |
|------|---------|----------------|------|-----------|------------|
| 1 | CA 230/400 V | 16 A | No (toma doméstica) | No | No permitido en España para aparcamientos nuevos |
| 2 | CA 230/400 V | 32 A | Cable ICCB con caja control | No | Recarga ocasional/emergencia |
| 3 | CA 230/400 V | 16–32 A (hasta 63 A trifásico) | EVSE permanente (wallbox) | Sí, PWM 1 kHz | Aparcamientos residenciales e industriales |
| 4 | CC hasta 1000 V | 400 A (CC rápida) | Cargador CC externo (CCS, CHAdeMO) | Sí + PLC/HLC | Estaciones de recarga rápida/ultrarrápida |

**Señal de piloto de control (CP)** — el mecanismo de coordinación entre el EVSE y el vehículo en modo 3 es una señal PWM de ±12 V a 1 kHz en el pin CP del conector IEC 62196-2 (Tipo 2). Los estados se definen por nivel de tensión:

- **Estado A** (+12 V, sin PWM): EVSE sin vehículo conectado.
- **Estado B** (+9 V): vehículo conectado, no listo para cargar.
- **Estado C** (+6 V): vehículo listo, solicita energía sin necesidad de ventilación.
- **Estado D** (+3 V): igual que C, con ventilación requerida (normalmente baterías de Pb en vehículos industriales).

El ciclo de trabajo (*duty cycle*, D) del PWM codifica la corriente máxima disponible según el EVSE:
- Para D ≤ 51 %: **I_máx = D × 0,6 A**
- Para 51 % < D ≤ 97 %: **I_máx = (D − 64) × 2,5 + 20 A**

Así, D = 50 % → I = 30 A; D = 70 % → I = 15 A. Esta codificación es la base sobre la que actúa el SIG para limitar la corriente de cada punto dinámicamente.

---

## Dimensionado eléctrico según ITC-BT-52

La ITC-BT-52 distingue entre *punto de recarga* (toma instalada operativa) y *preinstalación* (canalización y cuadro preparados, sin EVSE). Las exigencias mínimas vigentes:

- **Edificios no residenciales nuevos con >10 plazas**: preinstalación para el 100 % de las plazas.
- **Edificios residenciales nuevos o con reforma con >20 plazas**: preinstalación para el 100 % de las plazas.
- **Punto de recarga mínimo**: al menos 1 por cada 40 plazas, con potencia de cálculo de **3680 W** (16 A, 230 V monofásico) por punto.

Para la previsión de carga del cuadro de aparcamiento, la guía técnica del Ministerio emplea:

> **P_prevista = N_plazas × 10 % × 3680 W**

Ejemplo para un aparcamiento de 100 plazas: P_prevista = 100 × 0,10 × 3680 = **36,8 kW**.

Este es el mínimo de previsión. Para instalaciones reales con EVSE en modo 3 a 32 A por punto, el factor de coincidencia (FC) es el parámetro crítico. Con FC = 0,25 (simultáneamente activos el 25 % de los puntos):

> **I_feeder = N_puntos × I_unitaria × FC**
>
> Para 20 puntos de 32 A: I_feeder = 20 × 32 × 0,25 = **160 A**

**Sección de cable (IEC 60364-5-52 / UNE-HD 60364-5-52):**

| Escenario | Corriente de diseño | Sección mínima Cu | Designación tipo |
|-----------|--------------------|--------------------|-----------------|
| 1 punto monofásico 16 A | 16 A | 2,5 mm² | 2×2,5 Y (PVC en tubo) |
| 1 punto trifásico 32 A | 32 A | 6 mm² | 5×6 RV-K |
| 1 punto trifásico 63 A | 63 A | 25 mm² | 5×25 RV-K |
| Alimentador 20 puntos (FC=0,25) | 160 A | 70 mm² Cu | 5×70 RV-K |
| Alimentador 50 puntos (FC=0,20) | 50×32×0,20=320 A | 150 mm² Cu | 5×150 RV-K |

La caída de tensión máxima admisible según ITC-BT-19 para derivaciones individuales es del 1,5 %. Para alimentadores de aparcamiento de longitud significativa (>50 m), verificar ΔU con la fórmula:

> **ΔU% = √3 × I × L × (R·cosφ + X·sinφ) × 100 / (U_n × S)**

donde R es la resistividad del conductor (cobre: 0,0179 Ω·mm²/m a 20 °C) y X ≈ 0,08 Ω/km para cables RV-K según GElectrical/UNE-HD 60364-5-52.

---

## Protecciones individuales por punto de carga

La ITC-BT-52 establece que cada punto de recarga debe contar con protección propia. La selección correcta depende del tipo de EVSE:

**Interruptor magnetotérmico (MCB):**
- Curva **C** para EVSE en modo 3 (corriente de pico limitada por el vehículo, sin transitorios de conmutación elevados).
- Calibre para modo 3 monofásico 32 A: MCB C32 (*I_n* = 32 A, *P_cc* ≥ 6 kA — verificar Icc en el punto según IEC 60909).
- Calibre para modo 3 trifásico 32 A/fase: MCB-3P C32.

**Dispositivo diferencial (IEC 61008-1 / IEC 62423):**

| Tipo de EVSE | Falla DC esperada | Diferencial requerido |
|-------------|-------------------|----------------------|
| Modo 3 CA puro (wallbox AC) | No (CA senoidal) | Tipo AC o A, 30 mA |
| Modo 3 con electrónica de potencia (rectificador interno) | Posible CC liso ≤ 6 mA | Tipo A, 30 mA |
| Modo 4 (cargador CC externo, CCS/CHAdeMO) | CC liso > 6 mA | **Tipo B, 30 mA (IEC 62423)** |

El tipo A detecta corriente diferencial CA senoidal y pulsante rectificada semiciclo. El tipo B detecta además corriente diferencial CC lisa. Para EVSE modernos con convertidores CA/CC integrados que pueden inyectar componente continua, la ITC-BT-52 permite tipo A solo si el fabricante del EVSE garantiza que la corriente diferencial CC no supera 6 mA (según IEC 61851-1 Anexo B). En la duda, especificar tipo B.

Adicionalmente, la ITC-BT-52 exige para instalaciones de más de **5 estaciones de recarga** un análisis de armónicos y sobretensiones. Los rectificadores de los EVSE generan armónicos de orden 5, 7, 11 y 13. Con THDi > 20 %, verificar el neutro sobredimensionado (sección igual a fase en circuitos con carga no lineal significativa).

---

## Gestión inteligente de carga: SIG y OCPP

El Sistema Inteligente de Gestión (SIG) es obligatorio en instalaciones con múltiples puntos cuando existe riesgo de superar la potencia contratada. Su función principal: ajustar la señal CP (ciclo de trabajo) de cada EVSE en tiempo real para que la suma de corrientes no exceda *I_máx_contratada*.

**Modos de gestión:**

| Modalidad | Principio | Ventaja | Limitación |
|-----------|-----------|---------|------------|
| Estático | Reparto fijo de potencia entre puntos activos | Simple, sin comunicación | Ineficiente si hay puntos inactivos |
| Dinámico por prioridad | Puntos con prioridad alta reciben más potencia | Flexibilidad operacional | Requiere lógica de asignación |
| Dinámico igualitario | Potencia disponible se divide entre activos | Equidad, máxima utilización | No diferencia necesidades |
| Dinámico por demanda | Integración con EMS/SCADA del edificio | Óptimo energético | Mayor coste y complejidad |

El protocolo estándar para la comunicación entre EVSE y sistema de gestión backend es **OCPP (Open Charge Point Protocol)**, normalizado como **IEC 63584:2024** (OCPP 2.0.1). Para la integración con el sistema de gestión de energía local del edificio (EMS), la norma reciente es **IEC 63380-1:2025**.

La gestión dinámica actúa modificando el duty cycle del CP. Un SIG que detecta sobrecarga del alimentador puede reducir todos los EVSEs activos de D = 53 % (I = 30 A) a D = 36 % (I = 21,6 A) en <100 ms, sin interrumpir la sesión de carga del vehículo.

---

## Criterios de selección en obra

**Criterio 1 — Modo de carga por potencia y tiempo de estacionamiento:**

| Tiempo de estacionamiento | Potencia recomendada | Modo | Conector |
|--------------------------|---------------------|------|----------|
| > 8 h (residencial, nocturno) | 7,4 kW (32 A, 1F) | 3 | IEC 62196-2 Tipo 2 |
| 2–8 h (parking diurno) | 11–22 kW (3F 16/32 A) | 3 | IEC 62196-2 Tipo 2 |
| < 1 h (autovía, hub) | 50–350 kW (CC) | 4 | CCS Combo 2 / CHAdeMO |

**Criterio 2 — Tipo de diferencial:**
1. ¿El EVSE es modo 4 (CC externo)? → **Tipo B obligatorio**.
2. ¿El EVSE modo 3 incluye rectificador con posible fuga DC > 6 mA? → **Tipo B recomendado**.
3. ¿EVSE modo 3 con certificado IEC 61851-1 Anexo B de limitación a 6 mA DC? → **Tipo A admisible** (con 30 mA).

**Criterio 3 — Gestión de carga:**
- 1–4 puntos, potencia contratada suficiente → sin SIG.
- 5–20 puntos → SIG estático o dinámico OCPP básico.
- > 20 puntos o integración con FV/BESS → SIG dinámico con IEC 63380-1 (EMS local).

**Criterio 4 — Calibre del MCB de alimentador principal:**

> **I_n ≥ I_feeder / 0,8** (factor de utilización del MCB según IEC 60947-2)
>
> Para I_feeder = 160 A → MCB mínimo 200 A (MCCB con Icu ≥ Icc_punto).

---

## Conclusión

El dimensionado de infraestructura de recarga EV no es un ejercicio de enchufar wallboxes a un cuadro existente. Requiere calcular el feeder con factor de coincidencia real, seleccionar el diferencial correcto según el tipo de EVSE (tipo A o B), y dimensionar el SIG para evitar rebasar la potencia contratada. Los puntos críticos para obra:

1. Verificar si el aparcamiento supera los umbrales de preinstalación de ITC-BT-52 (>10 plazas no residencial, >20 residencial).
2. Dimensionar el alimentador con I_feeder = N × I_unit × FC (FC típico 0,20–0,30 para aparcamientos de larga duración).
3. Especificar diferencial tipo B para EVSE modo 4 y para modo 3 sin garantía de limitación DC.
4. Implementar SIG con OCPP (IEC 63584:2024) desde 5 puntos para evitar ampliación de acometida.
5. Para >20 puntos con generación FV o BESS, integrar con EMS local según IEC 63380-1:2025.
