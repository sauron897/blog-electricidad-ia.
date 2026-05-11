---
title: "Interruptor diferencial: fundamento técnico, tipos y criterios de selección"
description: "Análisis técnico del interruptor diferencial: principio de funcionamiento por toroide sumador, clases AC/A/F/B, sensibilidades, tiempos de disparo y criterios de selección según REBT e IEC 60755."
pubDate: 2026-05-10
keywords: ["interruptor diferencial", "IEC 60755", "REBT ITC-BT-24", "corriente de defecto", "protección diferencial"]
author: "INDUC TECH"
heroImage: /images/interruptor-diferencial.svg
readingTime: 12
---

El interruptor diferencial es el dispositivo de protección más incomprendido de una instalación eléctrica. Se sabe que "protege de las electrocuciones", pero pocos instaladores pueden explicar por qué 30 mA es el umbral estándar, qué diferencia real hay entre un tipo AC y un tipo A, o por qué un diferencial puede saltar sin haber ningún defecto real. Este artículo cubre el fundamento técnico completo.

## Principio de funcionamiento: el toroide sumador de corrientes

El diferencial no mide la corriente de fuga directamente. Lo que mide es el **desequilibrio entre la corriente de entrada y la de retorno** mediante un transformador toroidal por el que pasan todos los conductores activos del circuito (fase y neutro en monofásico; las tres fases y el neutro en trifásico).

En condiciones normales, la suma vectorial de corrientes que atraviesan el toroide es cero: toda la corriente que entra por fase vuelve por neutro. Si existe una fuga hacia tierra —a través de una persona, un aislamiento deteriorado o humedad— parte de la corriente de retorno "desaparece" del circuito. El toroide detecta ese desequilibrio e induce una tensión en el devanado secundario proporcional a la corriente diferencial **IΔ**.

Cuando IΔ supera el umbral de disparo (IΔn), el relé actúa sobre el mecanismo de apertura. El tiempo de respuesta en diferenciales estándar (tipo instantáneo) es inferior a 30 ms para corrientes de defecto ≥ 5·IΔn, según **IEC 61008-1**.

## Por qué 30 mA y no otro valor

El umbral de 30 mA no es arbitrario. Procede de la investigación sobre los efectos fisiológicos de la corriente alterna (50/60 Hz) en el cuerpo humano, recogida en **IEC TS 60479-1**:

| Corriente (mA) | Efecto fisiológico |
|---|---|
| < 0,5 | Imperceptible |
| 0,5 – 10 | Percepción, contracción muscular leve |
| 10 – 30 | Contracción intensa, dificultad para soltar el conductor |
| **30 – 50** | **Umbral de fibrilación ventricular con exposición prolongada** |
| > 75 | Fibrilación ventricular probable en < 1 s |

Un diferencial de 30 mA actúa antes de que la corriente alcance el umbral de fibrilación, asumiendo una impedancia corporal de contacto de ~1000 Ω (valor de referencia IEC 60479-1 para condiciones húmedas). En contacto directo mano-pie con la red de 230 V, la corriente de paso sería del orden de 230 mA sin protección diferencial: letal en milisegundos.

Los 10 mA se reservan para zonas de mayor riesgo (piscinas, baños con bañera) donde la impedancia de contacto cae por el agua y el margen de seguridad se reduce. Los 300 mA no protegen a personas —dejan pasar corrientes letales— pero sí previenen incendios por arco o calentamiento en conductores de distribución.

## Clases de diferencial según IEC 60755

La norma **IEC 60755** (adoptada como EN 62423 en Europa) clasifica los diferenciales por la forma de onda de corriente de defecto que son capaces de detectar:

**Clase AC**
Detecta únicamente corrientes diferenciales de tipo sinusoidal (50/60 Hz). Es el tipo histórico, suficiente para cargas resistivas e inductivas puras. **No apto para cargas con electrónica de potencia**, que generan componentes de corriente continua pulsante.

**Clase A**
Detecta corrientes alternas sinusoidales más corrientes continuas pulsantes (rectificadas en media onda o onda completa). Obligatorio en la **ITC-BT-25** del REBT para circuitos que alimenten equipos con fuentes conmutadas, variadores de frecuencia, cargadores de vehículo eléctrico y electrodomésticos con control electrónico. En la práctica, el tipo A es hoy el mínimo razonable en cualquier instalación doméstica o industrial moderna.

**Clase F**
Detecta todo lo anterior más corrientes diferenciales de frecuencias intermedias (hasta varios kHz) y corrientes compuestas. Diseñado específicamente para bombas de calor, VRF, vehículos eléctricos con carga en modo 3 y accionamientos con variador. La proliferación de estas cargas en instalaciones industriales hace que el tipo F sea cada vez más frecuente en cuadros de distribución.

**Clase B**
Detecta corrientes alternas de cualquier frecuencia, corrientes pulsantes y corrientes **continuas lisas**. Obligatorio en instalaciones fotovoltaicas, cargadores trifásicos de VE (modo 4), convertidores de frecuencia industriales y cualquier equipo que pueda generar corriente de defecto continua. Es notablemente más caro que los tipos anteriores.

La consecuencia práctica es clara: instalar un diferencial tipo AC en un circuito con variador de frecuencia o cargador de VE puede resultar en no-detección de un defecto real, porque la corriente de fuga no tiene forma sinusoidal pura.

## Selectividad diferencial: diferenciales instantáneos vs temporizados (tipo S)

En instalaciones con varios niveles de protección diferencial (cuadro general + cuadros secundarios), es imprescindible garantizar **selectividad vertical**: que ante un defecto en un circuito terminal, actúe el diferencial más cercano a la falta y no el general.

Los diferenciales estándar son **instantáneos**: actúan en < 30 ms para IΔ ≥ 5·IΔn. Los diferenciales **tipo S** (selectivos o temporizados) tienen un retardo intencional de 60–80 ms en su actuación, lo que permite que el instantáneo aguas abajo actúe primero.

El esquema típico en instalaciones industriales:

```
Diferencial general: 300 mA, tipo S (temporizado)
    └── Diferencial subcuadro: 100 mA, tipo S
            └── Diferencial circuito terminal: 30 mA, instantáneo
```

Sin esta jerarquía, cualquier fuga en un circuito terminal puede abrir el diferencial general y dejar sin servicio toda la instalación.

## Corrientes de fuga parásitas y disparos intempestivos

Un problema frecuente en instalaciones con mucha carga electrónica es el **disparo intempestivo** del diferencial sin que exista un defecto real. La causa son las **corrientes de fuga capacitivas** hacia tierra generadas por:

- Filtros EMC de fuentes conmutadas (condensadores Y entre fase y tierra)
- Cables apantallados de larga longitud
- Variadores de frecuencia con filtros integrados

Cada equipo con fuente conmutada puede aportar entre 0,5 y 5 mA de corriente de fuga. En un circuito con 10 equipos, la suma puede superar fácilmente los 30 mA aunque no haya ningún defecto.

La solución no es aumentar la sensibilidad del diferencial a 100 o 300 mA (se pierde protección a personas), sino:
1. Medir la corriente de fuga real del circuito con pinza diferencial antes de dimensionar el diferencial
2. Usar diferenciales tipo A o F con inmunidad a disparos intempestivos (marcados con **Si** según IEC 62423)
3. Segmentar el circuito para distribuir la carga de fuga entre varios diferenciales de 30 mA

## Criterios de selección: resumen práctico

| Parámetro | Criterio |
|---|---|
| **Sensibilidad** | 30 mA para protección personal; 10 mA en zonas mojadas; 300 mA solo para protección contra incendios |
| **Clase** | Tipo A como mínimo en cualquier instalación con electrónica; tipo F con bombas de calor o VE; tipo B con FV o convertidores trifásicos |
| **Temporización** | Instantáneo en circuitos terminales; tipo S en cabecera para garantizar selectividad |
| **Intensidad nominal** | ≥ intensidad nominal del magnetotérmico aguas abajo |
| **Disparos intempestivos** | Medir fuga real; considerar marca Si si hay cargas electrónicas |

## Normativa de referencia

- **REBT ITC-BT-24**: Protección contra los contactos indirectos
- **REBT ITC-BT-25**: Instalaciones interiores en viviendas — circuitos y características mínimas
- **IEC 61008-1**: Interruptores automáticos para actuar por corriente diferencial residual sin protección de sobreintensidad incorporada
- **IEC 60755 / EN 62423**: Requisitos generales para aparatos de protección diferencial
- **IEC TS 60479-1**: Efectos de la corriente sobre el cuerpo humano
