---
title: "Cargadores EV: diferencial tipo B e IEC 62955 según ITC-BT-52"
description: "Protección diferencial en recarga VE modo 3: tipo B vs tipo A con RDC-DD según IEC 62955. Dimensionado ITC-BT-52 con corrientes, secciones y criterios de selección."
pubDate: 2026-10-25
keywords: ["cargadores ev IEC 62955", "diferencial tipo B vehículo eléctrico", "ITC-BT-52 recarga EV", "RDC-DD modo 3 IEC 62955"]
author: "Editor"
---

## Introducción

La proliferación de puntos de recarga para vehículo eléctrico (VE) en instalaciones no domésticas —aparcamientos de comunidades, polígonos industriales, centros comerciales— ha puesto sobre la mesa una cuestión que los cuadros normalizados de hace diez años no contemplan: la protección diferencial ante corrientes de falta con componente continua. El diferencial tipo A, que cubre corrientes alternas y continuas pulsantes hasta 6 mA, no garantiza el disparo ante las formas de onda reales que generan los cargadores en modo 3. La ITC-BT-52 del REBT, complementada por UNE-HD 60364-7-722, exige protección adicional que materializa la norma IEC 62955 mediante el dispositivo RDC-DD.

Este artículo desarrolla los criterios de selección de protección diferencial para puntos de recarga en modo 3, el dimensionado de conductores según ITC-BT-52, y la lógica de coordinación entre el diferencial upstream y el RDC-DD integrado. Los valores numéricos provienen de IEC 61851-1, IEC 62955:2018 y UNE-HD 60364-5-52.

## Modos de carga según IEC 61851-1: corrientes y potencias de referencia

La norma IEC 61851-1 (transpuesta como UNE-EN 61851-1) clasifica la recarga en cuatro modos. Esta clasificación determina directamente la exigencia de protección diferencial:

| Modo | Conexión | I máx. | Potencia | Control pilot |
|------|----------|--------|----------|---------------|
| 1 | Toma convencional sin protección específica | 16 A / 230 V AC | 3,7 kW mono | No |
| 2 | Schuko con ICCPD (cable con caja de control) | 16 A / 230 V AC | 3,7 kW mono | En cable |
| 3 | EVSE dedicado, conector tipo 1 o tipo 2 | 32 A / 230 V; 32 A / 400 V | 7,4 kW / 22 kW | En EVSE |
| 4 | DC fast (CHAdeMO, CCS Combo) | hasta 125 A DC | hasta 350 kW | En EVSE |

El modo 3 es el más habitual en instalaciones reguladas por ITC-BT-52. El corriente de diseño para un EVSE monofásico de 7,4 kW es **32 A a 230 V**; para uno trifásico de 22 kW, **32 A por fase a 400 V**.

El modo 1 sin cuadro de mando es admitido por IEC 61851-1 pero la ITC-BT-52 lo restringe: en instalaciones fijas para uso colectivo, el punto de conexión debe disponer al menos de corriente de diseño protegida por diferencial individual de 30 mA.

## Porqué falla el diferencial tipo A en modo 3

Los cargadores OBC (On-Board Charger) de los VE utilizan rectificadores con corrección del factor de potencia (PFC) de tipo activo. En condición de fallo de aislamiento, la corriente de defecto tiene una forma de onda compuesta: fundamental alterna + corriente continua lisa (smooth DC) procedente del puente rectificador.

El núcleo toroidal del diferencial tipo A se satura ante una **corriente continua residual suave igual o superior a 6 mA**. Una vez saturado:

- La permeabilidad del núcleo cae drásticamente.
- La inductancia de detección se reduce.
- El disparo ante el defecto de alterna superpuesto puede no producirse, incluso con corrientes de defecto de alterna de 30 mA o superiores.

Este mecanismo de fallo está documentado en IEC 62423 (diferencial tipo B) y es el fundamento técnico de la exigencia normativa de la sección 722.531.2.1 de UNE-HD 60364-7-722: en modo 3, no se admite diferencial tipo A solo.

Las dos soluciones normativas son:

1. **Diferencial tipo B** (IEC 62423): cubre corrientes AC, AC pulsante y DC lisa. Construido con núcleo de detección con devanado de compensación para componente continua. Rango de sensibilidad: 30 mA en alterna, 6 mA en CC lisa.
2. **Diferencial tipo A + RDC-DD** según **IEC 62955:2018**: el RDC-DD detecta la componente continua residual; si supera 6 mA, inhibe el EVSE antes de que el tipo A quede saturado.

## IEC 62955:2018 — Arquitectura y parámetros del RDC-DD

La norma IEC 62955 define los **Residual Direct Current Detecting Devices (RDC-DD)** específicamente para la carga en modo 3. Dos clases:

- **RDC-MD** (monitor): detecta y señaliza sin interrumpir el circuito de potencia. Apto cuando el EVSE gestiona la inhibición mediante señal de control pilot.
- **RDC-PD** (protección): detecta e interrumpe el control pilot (CP), inhibiendo la carga desde el vehículo. No actúa sobre el circuito de potencia directamente.

Parámetros clave de IEC 62955:2018:

| Parámetro | Valor |
|-----------|-------|
| Umbral de disparo (smooth DC) | 6 mA |
| Tensión máxima de aplicación | 440 V AC |
| Corriente máxima | 125 A |
| Inmunidad transitorios | IEC 61000-4-4 nivel 3 |
| Inmunidad ESD | IEC 61000-4-2 nivel 3 |

El umbral de 6 mA no es arbitrario: se fijó para que, al activarse el RDC-DD, la corriente continua remanente sea inferior al nivel de saturación del núcleo del diferencial tipo A aguas arriba, preservando su sensibilidad frente al defecto de alterna.

En la práctica, el RDC-DD puede estar **integrado en el EVSE** (debe figurar en la documentación técnica del equipo con referencia a IEC 62955) o montado externamente en el cuadro de distribución entre el diferencial tipo A y el punto de recarga.

## Dimensionado de conductores: ITC-BT-52 y UNE-HD 60364-5-52

La ITC-BT-52 exige **circuito independiente por punto de recarga**, con protección automática individual y diferencial propio de 30 mA. La intensidad de diseño es la intensidad nominal máxima del EVSE, sin factor de reducción, salvo que exista sistema de gestión activa de carga certificado.

Secciones mínimas para conductores de cobre, método de instalación B2 (cable bajo tubo empotrado en pared), temperatura ambiente 40 °C, factor de corrección θ = 0,87 según tabla B.52.14 de UNE-HD 60364-5-52:

| EVSE | I diseño | Iref tabla (Cu, 70°C) | Secc. Cu mínima | Designación habitual |
|------|----------|-----------------------|-----------------|----------------------|
| Monofásico 3,7 kW | 16 A | 18,4 A × 0,87 = 16 A | **2,5 mm²** | H07Z1-K / RZ1-K 3×2,5 |
| Monofásico 7,4 kW | 32 A | 38 A × 0,87 = 33 A | **6 mm²** | RZ1-K 3×6 |
| Trifásico 11 kW | 16 A/fase | 18,4 A × 0,87 = 16 A | **2,5 mm²** | RZ1-K 5×2,5 |
| Trifásico 22 kW | 32 A/fase | 38 A × 0,87 = 33 A | **6 mm²** | RZ1-K 5×6 |
| Trifásico 43 kW | 63 A/fase | 73 A × 0,87 = 63,5 A | **16 mm²** | RZ1-K 5×16 |

**Verificación de caída de tensión** (ITC-BT-19, límite 3% para circuitos de fuerza desde el cuadro):

Para 30 m de RZ1-K 3×6 Cu a 32 A:

```
ΔU = (2 × L × I × ρ) / S = (2 × 30 × 32 × 0,0231) / 6 = 7,39 V → 3,2%
```

En este caso supera el 3%: incrementar a **10 mm²** para tramos de 30 m a 32 A, o gestionar con caída acumulada desde el origen.

Para 20 m de 6 mm²: ΔU = 4,93 V → 2,1% → cumple.

Resistividad del cobre a 70 °C: **ρ = 0,0231 Ω·mm²/m** (IEC 60287).

## Criterios de selección en obra

| Criterio de decisión | Solución recomendada |
|----------------------|----------------------|
| EVSE con RDC-DD integrado según IEC 62955 (marcado en placa) | Diferencial tipo A 30 mA upstream |
| EVSE sin RDC-DD integrado, modo 3 | **Diferencial tipo B** o tipo A + RDC-DD externo en cuadro |
| Instalación con >10 EVSE y gestión activa de carga | Tipo B generalizado + interruptor de gestión por circuito |
| Parque mixto (cargadores de distintos fabricantes) | Tipo B: evita dependencia de certificación RDC-DD del equipo |
| Presupuesto ajustado, EVSE verificado con RDC-DD | Tipo A 30 mA + módulo RDC-DD externo (~€20-30 por punto) |
| Instalación pública o de uso intensivo | Tipo B (mayor robustez; no depende del equipo aguas abajo) |

El diferencial tipo B tiene un coste significativamente mayor (€80-200 frente a €10-15 del tipo A), pero elimina la dependencia de la certificación IEC 62955 del EVSE y simplifica el mantenimiento de la instalación a largo plazo. Para instalaciones con renovación frecuente del parque de cargadores, la diferencia de coste inicial se amortiza en la reducción de modificaciones futuras.

**Selectividad con el diferencial general del cuadro:** si el diferencial individual de cada punto es 30 mA y el general del cuadro es 300 mA tipo S (selectivo), la selectividad cromática queda garantizada para defectos monopuntuales. En instalaciones con varios EVSE en el mismo circuito, verificar que la corriente de fuga capacitiva total no supere el 30% del umbral del diferencial general (IEC 60755).

## Conclusión

La selección de la protección diferencial para puntos de recarga VE modo 3 requiere aplicar UNE-HD 60364-7-722 e IEC 62955:2018: el tipo A solo queda excluido por el riesgo de saturación ante corriente continua residual superior a 6 mA. La solución práctica es diferencial tipo B, o tipo A con RDC-DD certificado, ya integrado en el EVSE o instalado en el cuadro de distribución. El dimensionado de conductores sigue ITC-BT-52 con sección mínima de 6 mm² Cu para EVSE de 32 A, verificando la caída de tensión al 3% según ITC-BT-19 para tramos superiores a 20 m.
