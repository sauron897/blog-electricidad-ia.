---
title: "Baterías BESS en instalaciones industriales: LFP, NMC e IEC 62619"
description: "Guía técnica para ingenieros: tecnologías LFP y NMC en BESS industriales, parámetros IEC 62619, BMS, protecciones eléctricas y criterios de selección en obra."
pubDate: 2026-10-23
keywords: ["baterias almacenamiento BESS IEC 62619", "LFP NMC instalacion industrial", "BMS proteccion bateria electroquimica", "BESS seleccion ingenieria electrica"]
author: "Editor"
---

## Introducción: el BESS como elemento activo de red

Un sistema de almacenamiento de energía en baterías (BESS, *Battery Energy Storage System*) ya no es un complemento opcional en instalaciones fotovoltaicas industriales: en instalaciones de más de 100 kW conectadas a red, el BESS actúa como regulador de demanda, soporte de frecuencia y recurso de peak shaving con tiempos de respuesta por debajo de los 100 ms.

La norma de referencia para seguridad de baterías de ion litio industriales es **IEC 62619:2022** (*Safety requirements for secondary lithium cells and batteries for use in industrial applications*). Esta norma, adoptada en España como **UNE-EN IEC 62619:2022**, define requisitos para el diseño del sistema de gestión de baterías (BMS), protecciones eléctricas, gestión térmica y procedimientos de test de seguridad bajo condiciones de abuso.

Para el ingeniero eléctrico responsable del proyecto, las decisiones críticas son tres: elección de química de celda, dimensionado eléctrico del sistema y coordinación de las protecciones con la red BT/MT de la instalación.

---

## Tecnologías LFP y NMC: parámetros de ingeniería

Las dos químicas dominantes en BESS industriales son **LFP** (Litio-Hierro-Fosfato, LiFePO₄) y **NMC** (Litio-Níquel-Manganeso-Cobalto, LiNiMnCoO₂). Sus diferencias no son de marketing, sino de parámetros eléctricos y térmicos que condicionan el diseño.

### Tabla comparativa LFP vs. NMC

| Parámetro | LFP | NMC |
|---|---|---|
| Tensión nominal de celda | 3,2 V | 3,6 V |
| Tensión de carga máx. | 3,65 V | 4,20 V |
| Tensión de descarga mín. | 2,50 V | 2,80 V |
| Densidad energética volumétrica | 250–350 Wh/L | 450–700 Wh/L |
| Densidad energética másica | 120–180 Wh/kg | 200–300 Wh/kg |
| Ciclos (hasta 80% DoH) | 3.000–6.000 | 1.000–2.500 |
| Temperatura de onset térmico (DSC) | > 270 °C | 180–210 °C |
| Corriente de carga máx. (C-rate) | 1–2 C | 1–3 C |
| Rendimiento round-trip | 94–97% | 92–96% |
| SOH a 10 años típico | 75–85% | 65–75% |

La temperatura de onset térmico (temperatura a la que se inicia la reacción exotérmica irreversible, medida por calorimetría diferencial de barrido) es el parámetro de seguridad más relevante para el ingeniero: los 270 °C de LFP frente a los 180 °C de NMC implican que en caso de cortocircuito interno o sobretemperatura, LFP tiene un margen de 90 °C adicional antes de entrar en *thermal runaway*. Por este motivo, **IEC 62619:2022, cláusula 6.2** establece que los módulos con química de mayor riesgo térmico requieren sistemas adicionales de contención y detección.

En la práctica, para BESS industriales estacionarios de 100 kWh a varios MWh, LFP es la elección dominante por seguridad, ciclos de vida y coste de ciclo. NMC se reserva a aplicaciones donde la densidad energética es determinante y el espacio está fuertemente restringido.

---

## Arquitectura eléctrica del sistema BESS

Un BESS industrial estándar se organiza en cuatro niveles jerárquicos:

1. **Celda** → módulo (stack de celdas en serie/paralelo)
2. **Módulo** → rack (varios módulos con BMS de módulo)
3. **Rack** → armario (DC bus común con BMS maestro)
4. **Armario** → PCS (Power Conversion System, inversor bidireccional AC/DC)

### Tensiones de bus DC típicas

| Tamaño sistema | Tensión bus DC | Corriente DC máx. |
|---|---|---|
| 50–200 kWh | 48 V (rack LFP) | 1.000–4.000 A |
| 200 kWh–1 MWh | 600–800 V | 300–600 A |
| > 1 MWh | 1.000–1.500 V | 200–400 A |

Para BESS de 1 MWh+ conectados a red 20 kV, el esquema habitual es: baterías a 1.000 Vdc → inversor bidireccional 1.000 Vdc/400 Vac → transformador BT/MT 400 V/20 kV. La interfaz de red debe cumplir **IEC 62477-1** para el PCS y **IEC 62909-1** para el sistema completo.

---

## BMS y protecciones eléctricas según IEC 62619

El BMS es el elemento central de seguridad. Según **IEC 62619:2022, cláusula 7**, el BMS debe gestionar al menos:

- **Protección de sobretensión de celda**: disparo si U_celda > U_max (3,65 V en LFP, 4,20 V en NMC)
- **Protección de subtensión**: disparo si U_celda < U_min para prevenir daño por descarga profunda
- **Protección de sobretemperatura**: disparo de carga si T > 45 °C (carga), T > 60 °C (descarga) en condiciones estándar
- **Protección de sobreintensidad**: limitación a C-rate máximo según ficha de celda
- **Detección de cortocircuito**: tiempo de respuesta < 5 ms para evitar I²t destructivo

La **detección de fuga a tierra** (ISO/IEC 62619 cláusula 7.4) es obligatoria en buses DC no flotantes. En sistemas con bus DC aislado (configuración IT-DC), se usa un monitor de resistencia de aislamiento que debe disparar alarma cuando R_iso < 100 Ω/V respecto a tierra.

### Protecciones eléctricas externas al BMS

Además del BMS, la instalación BESS requiere protecciones eléctricas en el cuadro de acometida AC y en el bus DC:

| Protección | Dispositivo | Norma | Criterio de ajuste |
|---|---|---|---|
| Sobreintensidad DC | Fusible clase PV (gPV) | IEC 60269-6 | ≥ 1,5 × I_nominal batería |
| Desconexión DC | Seccionador DC bajo carga | IEC 60947-3 | Categoría de utilización DC-23A |
| Sobreintensidad AC (PCS) | MCCB o ACB | IEC 60947-2 | Icu ≥ Icc máx. punto de conexión |
| Diferencial AC | ID tipo B (sensible a CC pulsante) | IEC 62423 | 30 mA si < 400 V, 300 mA si MT |
| SPD bus DC | Clase II DC | IEC 61643-31 | Uc ≥ 1,2 × V_bus DC |
| SPD bus AC | Clase II AC | IEC 61643-11 | Uc ≥ 1,1 × 1,1 × Un |

El diferencial tipo B es obligatorio en el lado AC del inversor bidireccional porque los conversores de potencia generan componentes de corriente de fuga a frecuencias mixtas (DC, 50 Hz, armónicos) que inhabilitan la respuesta de los diferenciales AC convencionales (tipo A o tipo AC).

---

## Gestión térmica y requisitos de emplazamiento

La gestión térmica condiciona el rendimiento y la vida útil. El BMS controla la temperatura celda a celda; la instalación debe garantizar las condiciones de contorno.

**Rango operativo:** LFP acepta carga entre 0 °C y 45 °C. Por debajo de 0 °C, la intercalación de litio en el ánodo de grafito es incompleta y genera litio metálico (*lithium plating*), degradando de forma irreversible la capacidad. Muchos módulos LFP incorporan calentadores de celda activados por BMS cuando T < 5 °C.

**Disipación térmica:** Un BESS de 500 kWh con rendimiento round-trip del 95% disipa durante una carga/descarga completa de 1 hora: P_disipada = 500 kWh × (1 − 0,95) = 25 kWh = 25 kW durante 1 h. Para instalación en sala cerrada, el sistema HVAC debe ser capaz de extraer esos 25 kW sin superar ΔT = 5 K respecto a la temperatura de consigna.

**Separación cortafuegos:** según **IEC 62619:2022, cláusula 5.4** y las guías de NFPA 855, los armarios BESS de más de 600 kWh deben instalarse con separación cortafuegos de 1 hora o sistema de supresión automática (sprinklers o agentes gaseosos).

---

## Criterios de selección de BESS en obra

La selección de un BESS para instalación industrial sigue una lógica de árbol de decisión con cuatro parámetros determinantes:

### 1. Energía (kWh) y potencia (kW)

Definen la topología y la C-rate de operación.
- Peak shaving industrial: C-rate 0,5–1 C, ciclos diarios, alta exigencia en ciclos → **LFP**
- Reserva de emergencia (UPS): C-rate 1–2 C, pocas descargas completas anuales → NMC o LFP
- Regulación de frecuencia (FCR): C-rate hasta 2 C con descargas parciales frecuentes → LFP por longevidad

### 2. Duración de descarga (h)

- Duración 1 h: relación kWh/kW = 1; dimensiona el sistema 1C
- Duración 4 h: relación kWh/kW = 4; sistemas con mayor capacidad, coste por kWh dominante
- En España, los proyectos BESS de régimen horario en mercado mayorista tienden a 2–4 h según la lógica de arbitraje

### 3. Integración con red MT o BT

- Conexión BT (≤ 1 MVA): PCS 400 Vac, sin transformador de elevación
- Conexión MT (> 1 MVA): PCS 400 Vac + transformador de bloque 400 V/MT; verificar cortocircuito en barra MT con **IEC 60909**

### 4. Verificaciones de seguridad obligatorias antes de puesta en marcha

1. Test de aislamiento del bus DC (Meg a 2 × V_bus + 500 V durante 1 min)
2. Verificación de la curva de carga/descarga del BMS con equipo de referencia
3. Test funcional del sistema de detección de temperatura (termopar o PT100 en celda de referencia)
4. Verificación de la protección diferencial tipo B (corriente de prueba 30 mA DC)
5. Prueba de comunicación BMS-PCS-SCADA (protocolo Modbus RTU, Modbus TCP o CAN bus)

---

## Conclusión

Para el ingeniero eléctrico, el diseño de un BESS industrial no se reduce a elegir kWh. Exige conocer los parámetros de celda que determinan las protecciones (tensión de onset, C-rate máximo, ventana de tensión operativa), dimensionar el bus DC con margen para SPD y fusibles IEC 60269-6, asegurar la detección de fuga en configuración IT-DC y verificar que el diferencial AC del PCS sea tipo B según IEC 62423.

La norma IEC 62619:2022 fija el marco de requisitos de seguridad; para la interfaz con red, aplican IEC 62477-1 (PCS) y IEC 62909-1 (BESS completo). En España, la tramitación de instalaciones de almacenamiento > 1 MW requiere autorización administrativa previa según la **Ley 24/2013 del Sector Eléctrico** y el **RD 244/2019** (autoconsumo).

El diferencial de coste entre LFP y NMC en proyectos de 2026 se ha reducido significativamente, pero la ventaja en ciclos de vida y seguridad térmica de LFP mantiene su dominio en BESS estacionarios industriales para horizontes de 10–15 años.
