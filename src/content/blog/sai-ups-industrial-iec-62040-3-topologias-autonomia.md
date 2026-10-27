---
title: "SAI UPS industrial IEC 62040-3: topologías y autonomía"
description: "Clasificación VFI, VI y VFD según IEC 62040-3, código normalizado de topología, fórmula de cálculo de autonomía de batería y criterios de selección para instalaciones industriales."
pubDate: 2026-10-27
keywords: ["SAI UPS industrial doble conversión IEC 62040", "UPS VFI clasificación IEC 62040-3", "dimensionado autonomía batería UPS industrial", "selección SAI instalación industrial IEC 62040"]
author: "Editor"
---

En instalaciones industriales con cargas críticas —variadores de frecuencia, PLC, servidores SCADA, equipos médicos o centros de datos— la calidad de la alimentación no admite compromisos. Un SAI mal seleccionado no protege contra las perturbaciones que más dañan la carga, y un banco de baterías mal dimensionado entrega la mitad de la autonomía prometida al cabo de tres años. La serie IEC 62040 da el marco normativo completo: seguridad (IEC 62040-1), compatibilidad electromagnética (IEC 62040-2), requisitos de prestaciones y ensayos de tipo (IEC 62040-3) e instalación (IEC 62040-4). Para la ingeniería de selección y dimensionado, el documento de referencia es **IEC 62040-3**.

## Clasificación de topologías según IEC 62040-3

IEC 62040-3 clasifica los SAI estáticos por un código de tres elementos que describe la dependencia de la salida respecto a la red, la forma de onda y el comportamiento dinámico. Las tres familias principales son:

| Código IEC 62040-3 | Nombre común | Dependencia de red | Tiempo de transferencia a batería |
|--------------------|--------------|-------------------|-----------------------------------|
| **VFD** | Standby / Offline | Tensión y frecuencia | 4–12 ms |
| **VI** | Line-interactive (AVR) | Solo tensión | 2–6 ms |
| **VFI** | Doble conversión online | Ninguna | 0 ms (sin interrupción) |

**VFD** (Voltage and Frequency Dependent): en operación normal la carga se alimenta directamente de la red a través del cargador. El inversor arranca solo cuando detecta un fallo. No ofrece ninguna protección contra perturbaciones de tensión (sags, swells, armónicos) mientras la red esté presente. Adecuado únicamente para cargas TI de bajo coste en oficinas.

**VI** (Voltage Independent): incorpora un transformador AVR buck-boost que estabiliza la tensión de salida dentro del rango de entrada admisible (típicamente ±15–25% del nominal) sin conectar las baterías. Para un fallo completo de red, la transferencia al inversor es de 2–6 ms, suficiente para cargas con condensadores de bus intermedios, pero insuficiente para algunos variadores industriales con detección rápida de caída de tensión.

**VFI** (Voltage and Frequency Independent): la carga se alimenta siempre del inversor PWM. El rectificador con corrección activa del factor de potencia (PFC activo: cos φ ≥ 0,99, THDi < 3%) mantiene el bus DC constante. El inversor genera 400 V ±1% / 50,00 Hz ±0,1% con independencia total de la red. La única conmutación es la transferencia sincronizada al bypass de mantenimiento. Esta topología es la única que garantiza protección frente a los diez tipos de perturbaciones de red definidos en IEC 62040-3.

Para instalaciones industriales con variadores, PLC en proceso continuo o equipos médicos de clase B, **VFI es la única topología técnicamente admisible**.

## Código de clasificación completo y su lectura

La norma define un código extendido que un SAI trifásico de doble conversión industrial típico expresa como:

**VFI-SS-111**

- **VFI**: Voltage and Frequency Independent (doble conversión)
- **SS**: forma de onda sinusoidal tanto en modo normal como en modo batería
- Primer **1**: THDU de salida < 8% con carga lineal
- Segundo **1**: variación transitoria de tensión < ±10% ante escalón de carga de 0–100%
- Tercer **1**: variación de frecuencia de salida < ±1% en modo batería

Un SAI que en modo batería no puede mantener la sinusoide se clasifica VFI-**X**S-111, con THDU entre 8% y 16%. Este nivel puede excitar resonancias en los filtros LC internos de variadores de frecuencia. Siempre exigir el código completo al fabricante y verificarlo contra el ensayo de tipo IEC 62040-3.

## Dimensionado de autonomía: fórmula y factores de diseño

La capacidad de batería necesaria para una autonomía definida se calcula con:

```
C_Ah = (P_W × t_min) / (60 × V_bat × η_inv × DoD × K_temp × K_env)
```

| Variable | Descripción | Valor típico |
|----------|-------------|-------------|
| P_W | Potencia de la carga (W) | — |
| t_min | Autonomía requerida (min) | — |
| V_bat | Tensión del banco DC (V) | 240 V (trifásico > 20 kVA) |
| η_inv | Eficiencia del inversor | 0,92–0,96 |
| DoD | Profundidad máxima de descarga | VRLA: 0,80 / LFP: 0,90 |
| K_temp | Factor de temperatura | 1,00 a 20°C / ≈0,80 a 35°C (VRLA) |
| K_env | Factor de envejecimiento al fin de vida | 0,80 (VRLA 5 años) |

**Ejemplo resuelto**: SAI trifásico 50 kVA / factor de potencia salida 1,0 → P_W = 45.000 W. Autonomía requerida: 15 min. Banco 240 V DC. η_inv = 0,95. VRLA a 25°C, K_env = 0,80:

```
C_Ah = (45.000 × 15) / (60 × 240 × 0,95 × 0,80 × 1,00 × 0,80)
C_Ah = 675.000 / 8.736 ≈ 773 Ah al principio de vida
```

Con bloques VRLA de 12 V / 100 Ah, se necesitan 20 bloques en serie (240 V) y 8 strings en paralelo (800 Ah ≥ 773 Ah). Total: 160 bloques de batería.

**Nota sobre curvas de Peukert**: los fabricantes dimensionan con curvas de descarga reales de sus baterías, que son no lineales. Para descargas de 10–20 minutos, la capacidad entregada puede ser un 10–20% inferior a la capacidad nominal C10. El cálculo simplificado anterior es conservador, pero no sustituye al dimensionado con software del fabricante (APC Powerchute, Eaton Battery Pro, Vertiv Liebert DST).

## Comparativa VRLA vs Li-Ion LFP

| Parámetro | VRLA AGM/Gel | Li-Ion LFP |
|-----------|-------------|----------|
| Densidad energética (Wh/kg) | 25–40 | 90–120 |
| Vida ciclos (80% DoD) | 200–500 | 2.000–4.000 |
| Vida calendario a 25°C | 5–10 años | 10–15 años |
| Temperatura óptima | 20–25°C | 15–35°C |
| Degradación a 35°C | −50% vida calendar | −15% vida calendar |
| Tiempo carga 0–100% | 8–12 h | 1–3 h |
| BMS obligatorio | No | Sí (IEC 62619) |
| Coste inicial relativo | 1× | 2,5–3,5× |
| Coste total ciclo de vida (10 años) | 1× | 0,6–0,8× |
| Normativa seguridad aplicable | IEC 62040-1 | IEC 62619, UL 1973 |

La temperatura de sala de baterías es el parámetro crítico para VRLA: cada aumento de 8–10°C por encima de 25°C reduce la vida útil a la mitad. Una sala a 35°C reduce la vida de 8 años a 4 años. LFP tolera mejor las temperaturas elevadas y no emite hidrógeno durante la carga, lo que elimina el requisito de ventilación forzada de la sala (IEC 62040-1, apéndice de seguridad de sala de baterías).

## Criterios de selección para instalaciones industriales

**1. Topología**: VFI obligatorio para cualquier carga crítica industrial. VI solo es admisible en equipos de oficina con tolerancia demostrada a 2–6 ms de transferencia.

**2. Potencia activa vs. potencia aparente**: verificar el factor de potencia de salida del SAI. Un SAI de 100 kVA con cos φ salida = 0,9 entrega 90 kW. Los SAI de nueva generación tienen cos φ salida = 1,0. La potencia de la carga debe calcularse como suma de potencias activas, no VA.

**3. Compatibilidad con cargas no lineales**: los variadores de frecuencia introducen THDi de entrada de hasta el 40%. Exigir que la THDU de salida del SAI con carga no lineal al 100% sea < 5%, según el ensayo de IEC 62040-3 sección 7.3. Una THDU > 8% puede disparar las protecciones de sobrecarga del propio variador.

**4. Redundancia N+1 o 2N**: para disponibilidad ≥ 99,99% (< 53 min/año de indisponibilidad), se requiere arquitectura paralela en activo con bypass estático. El tiempo de transferencia al bypass debe ser < 20 ms sincronizados con la red, verificado en ensayo de tipo IEC 62040-3.

**5. Compatibilidad con grupo electrógeno**: el SAI debe operar con la tensión y frecuencia inestables de un generador durante el primer transitorio de carga (±10% tensión, ±2 Hz frecuencia durante los primeros 5–10 s). Exigir modo "generador" o ampliación del rango de aceptación del rectificador al ±20%.

**6. Autonomía y jerarquía de protección**: definir si el SAI cubre solo la parada ordenada (5–10 min), el tiempo de arranque del generador de emergencia (10–30 min) o la operación autónoma extendida (> 30 min). El dimensionado del banco de baterías crece de forma muy pronunciada a partir de 30 min: la solución habitual para autonomías largas es añadir módulos de baterías externos, no sobredimensionar el SAI.

## Conclusión

La clasificación VFI de IEC 62040-3 no es un argumento de venta: es la garantía normativa de que la carga está completamente desacoplada de la red en todo instante. Elegir VI o VFD en una instalación industrial para ahorrar coste implica exponer los equipos a todas las perturbaciones de la red durante el 99,9% del tiempo de operación en que no hay fallo completo.

El dimensionado de autonomía con los factores reales de temperatura, envejecimiento y DoD puede duplicar la capacidad de batería aparente. Un banco dimensionado para 15 minutos con VRLA a 25°C entregará 9–10 minutos en el año 5 si no se planifica la reposición. El análisis del coste total del ciclo de vida durante 10 años casi siempre justifica la inversión inicial en tecnología LFP cuando la temperatura de sala supera los 28°C o cuando se requieren más de dos reposiciones de baterías a lo largo de la vida de la instalación.
