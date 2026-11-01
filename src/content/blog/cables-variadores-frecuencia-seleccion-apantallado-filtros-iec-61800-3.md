---
title: "Cables para variadores de frecuencia: selección y du/dt según IEC 61800-3"
description: "Guía técnica para ingenieros: selección de cables de motor con VFD, apantallado, corrientes capacitivas, filtros du/dt y categorías EMC según IEC 61800-3 e IEC 60364-5-52."
pubDate: 2026-11-01
keywords: ["cables variadores frecuencia seleccion IEC 61800-3", "cable motor VFD apantallado", "filtro du/dt variador frecuencia", "corriente fuga capacitiva VFD cable", "IEC 61800-3 categoria EMC cable"]
author: "Editor"
---

## Por qué el cable de motor con VFD no es un cable convencional

Un variador de frecuencia (VFD) no entrega una tensión sinusoidal al motor: genera pulsos de tensión mediante conmutación IGBT a frecuencias típicamente entre 2 y 16 kHz, con tiempos de subida (rise time) de 0,1 a 2 µs. Este régimen impone al cable de motor exigencias que un cable estándar de instalación —incluso uno homologado bajo IEC 60364-5-52— no satisface sin consecuencias.

Los tres fenómenos determinantes son la sobretensión reflejada por efecto de onda estacionaria (*reflected wave*), la corriente de fuga capacitiva de alta frecuencia y las emisiones EMC conducidas. El dimensionado correcto del cable, su tipo de apantallado y la necesidad de filtros se derivan de cuantificar estos tres efectos para la instalación concreta.

## Efecto de onda reflejada: sobretensiones en bornes del motor

Cuando el frente de tensión del VFD viaja por el cable y alcanza los bornes del motor (carga de alta impedancia a alta frecuencia), la desadaptación de impedancias genera una onda reflejada que se suma al impulso incidente. En el caso extremo —cable largo y tiempo de subida corto—, la tensión en bornes puede alcanzar hasta 2 × Vbus en DC, que para un VFD de 400 V AC equivale a una cresta de 1.130 V (Vbus ≈ 565 V × 2).

La distancia crítica a partir de la cual aparece la reflexión completa es:

```
L_crítica = (v_prop × t_rise) / 2
```

Con velocidad de propagación típica en cables XLPE de `v_prop ≈ 150 m/µs` y un rise time de 0,5 µs:

```
L_crítica = (150 × 0,5) / 2 = 37,5 m
```

Por encima de esta longitud, la sobretensión en bornes alcanza el máximo teórico. Cables con XLPE o EPR de baja capacitancia distribuida propagan el frente más rápido (mayor velocidad de fase); los cables de PVC tienen velocidad de propagación menor (~130 m/µs) y una longitud crítica ligeramente mayor.

**Referencia normativa**: IEC 61800-2:2021 establece los límites de tensión de cresta en bornes del motor (Vpk máx = 1.600 V para instalaciones alimentadas desde red de 400 V) y es el documento de referencia para los fabricantes de VFD a la hora de fijar las longitudes máximas de cable sin filtro.


## Corriente de fuga capacitiva: impacto en diferenciales y sobrecarga de IGBT

La capacitancia conductor-pantalla de un cable apantallado genera una corriente capacitiva de alta frecuencia que circula por la pantalla hacia tierra y regresa al variador por el conductor de protección (PE). Esta corriente no pasa por el motor, pero satura los módulos IGBT del variador y dispara diferenciales tipo AC o tipo A si estos no están diseñados para frecuencias por encima de 50 Hz.

La corriente de fuga capacitiva en régimen permanente se estima como:

```
I_fuga = C' × L × (dv/dt) × (2π × f_conm)
```

Donde:
- `C'` = capacitancia por unidad de longitud (nF/m)
- `L` = longitud del cable (m)
- `dv/dt` = gradiente de tensión del frente IGBT (V/µs)
- `f_conm` = frecuencia de conmutación (Hz)

Con un cable apantallado de cobre XLPE 4×16 mm² (C' ≈ 0,18 nF/m según IEC 60364-5-52/GElectrical), longitud 100 m, dv/dt = 1.000 V/µs y f_conm = 4 kHz:

```
I_fuga ≈ 0,18×10⁻⁹ × 100 × 1×10⁶ × 2π × 4.000 ≈ 452 mA_pk
```

Para instalaciones con VFD de potencia media (>5,5 kW) y cables superiores a 50 m, la corriente de fuga capacitiva supera la sensibilidad nominal de los diferenciales de 300 mA. **IEC 62955:2018** y el apéndice A de **IEC 60364-4-41** exigen diferencial de tipo B (sensible a continua pulsante y alterna de alta frecuencia hasta 20 kHz) en circuitos con VFD. La **ITC-BT-52** del REBT refuerza esta exigencia para puntos de recarga de vehículo eléctrico con cargador activo; el mismo principio aplica a cualquier circuito trifásico con VFD de potencia.

## Categorías EMC según IEC 61800-3: C1 a C4

IEC 61800-3:2017 clasifica los variadores en cuatro categorías de entorno y emisión que determinan el filtro EMC mínimo y la longitud de cable admisible:

| Categoría | Entorno         | Descripción                                               | Long. cable típica sin filtro adicional |
|-----------|-----------------|-----------------------------------------------------------|----------------------------------------|
| C1        | Doméstico       | Red pública, uso residencial. Emisiones muy bajas.        | ≤ 10 m (apantallado)                   |
| C2        | Industrial 1ª   | No conectado a red pública sin acción profesional. Filtro EMC obligatorio. | ≤ 25 m (apantallado)        |
| C3        | Industrial 2ª   | Tensiones >1.000 V o corriente >400 A en mismo cuadro. Restricciones EMC menores. | ≤ 100 m (apantallado)  |
| C4        | Complejo        | Instalaciones complejas, plan de compatibilidad EMC requerido. | Sin límite definido, análisis caso a caso |

Para categoría C3 —la más habitual en industria en España— la **longitud máxima de cable sin filtro de salida es de 100 m** con cable apantallado y filtro EMC integrado en el variador. Por encima de este umbral, o si el time de subida del VFD es < 1 µs, se requiere filtro du/dt o filtro sinusoidal.

## Criterios de selección del cable de motor con VFD

### Sección del conductor

La sección se calcula por criterio térmico según IEC 60364-5-52 con el método de intensidades admisibles (tabla B.52.1 e ITC-BT-19), idéntico al de instalaciones convencionales. Sin embargo, hay dos factores adicionales:

1. **Factor de corrección por armónicos**: La corriente de salida del VFD contiene componentes armónicas que elevan las pérdidas por efecto Joule en el cobre. Para THD de corriente > 15%, aplica un factor de corrección de 0,86 sobre la intensidad admisible (IEC 60364-5-52, cláusula 523.6).
2. **Corriente nominal del VFD vs. corriente del motor**: La sección debe soportar la corriente de salida máxima del variador, que puede ser 1,5 × In durante los acelerones, no solo la In del motor.

### Tipo de cable

| Tipo de cable               | C' típica (nF/m) | Apantallado | Recomendado para VFD |
|-----------------------------|------------------|-------------|----------------------|
| PVC sin pantalla (NYY)       | 0,10–0,15        | No          | Solo < 10 m, C3/C4  |
| XLPE sin pantalla (2XWY)     | 0,09–0,18        | No          | Solo < 25 m, C3/C4  |
| XLPE apantallado (VFD cable) | 0,15–0,30        | Sí (Al o Cu) | Recomendado siempre |
| XLPE ap. baja capacitancia   | 0,06–0,10        | Sí (Cu trenzado) | Óptimo > 50 m   |

Los cables de baja capacitancia distribuida reducen la corriente de fuga y permiten cumplir categoría C2/C3 a mayores longitudes. Fabricantes como Prysmian (PROTODRIVE), Lapp (ÖLFLEX SERVO FD) o Nexans ofrecen referencias específicas con C' < 100 pF/m.

### Apantallado y conexionado de la pantalla

El apantallado debe ser de **cobertura ≥ 85%** (trenzado de cobre o aluminio en espiral de alta cobertura). La conexión de la pantalla es **bifilar (ambos extremos a PE)** para el retorno de corrientes de alta frecuencia según IEC 61800-5-2. Conectar la pantalla solo en un extremo es válido para EMC conductivo pero no controla la corriente de fuga capacitiva.

Los conductores de tierra y pantalla deben ser de sección ≥ 50% de la fase, con un mínimo de 4 mm² Cu para cables de potencia según IEC 61439-1 cláusula 8.6.3.


## Filtros du/dt y sinusoidales: cuándo son obligatorios

### Filtro du/dt

Limita el gradiente de tensión de salida a valores típicos de 500 V/µs, reduciendo las sobretensiones reflejadas en el motor. No modifica la forma de onda de corriente. Se requiere cuando:

- La longitud del cable supera la longitud crítica (calculada antes) y la potencia del motor supera 2,2 kW.
- El variador opera en categoría C2 con cables > 25 m.
- El motor es de clase de aislamiento F (155°C) sin refuerzo, especialmente si es de tipo TEFC antiguo.

Las pérdidas del filtro du/dt son típicamente 0,5–1% de la potencia nominal.

### Filtro sinusoidal de salida

Genera una señal prácticamente sinusoidal en los bornes del motor. Elimina tanto las sobretensiones reflejadas como las corrientes de fuga de alta frecuencia y el ruido acústico del motor. Se justifica cuando:

- Cable de motor > 100 m en categoría C3 o > 50 m en C2.
- Motor estándar (no reforzado para VFD) con clasificación B o F.
- Requisitos de EMC en entorno muy sensible (instrumentación de precisión próxima).
- Aplicaciones con motores síncronos de imanes permanentes (PMSM).

**Penalización**: Algunos variadores reducen su potencia nominal en un 10–20% al usar filtro sinusoidal. Verificar en el datasheet del variador concreto.

### Bobina de modo común (common mode choke)

Reduce las corrientes de modo común que circulan por la pantalla y por PE, aliviando la carga sobre el diferencial y los rodamientos del motor (erosión por corrientes parásitas). Se instala en la salida del variador, en serie con los tres conductores de fase más el PE. Su uso es recomendable para potencias > 11 kW y cables > 50 m.

## Criterios de selección en obra: árbol de decisión

1. **Longitud del cable ≤ 10 m**: cable XLPE estándar, sin filtro, categoría C3 cumplida.
2. **Longitud 10–50 m**: cable apantallado VFD, filtro EMC del variador activo. Verificar límite de longitud del fabricante para C2/C3.
3. **Longitud 50–100 m**: cable apantallado VFD de baja capacitancia + filtro du/dt. Diferencial tipo B obligatorio.
4. **Longitud 100–300 m**: filtro sinusoidal de salida + cable apantallado + bobina de modo común. Recalcular sección con factor de corrección por temperatura del filtro.
5. **Longitud > 300 m**: considerar variador en proximidad del motor (topología distribuida) o transformador de aislamiento de salida.

## Conclusión

El cable de motor en instalaciones con VFD es un componente activo del sistema de accionamiento, no una conexión pasiva. Los ingenieros deben dimensionar simultáneamente: sección por criterio térmico con factor de corrección armónico (IEC 60364-5-52), tipo de apantallado en función de la categoría EMC (IEC 61800-3), longitud crítica para sobretensiones reflejadas (IEC 61800-2), y compatibilidad con el diferencial de protección (diferencial tipo B según IEC 62955). Los filtros du/dt y sinusoidales no son opciones de confort: son requisitos de ingeniería cuando la longitud del cable, el tipo de motor o la categoría EMC lo exigen.
