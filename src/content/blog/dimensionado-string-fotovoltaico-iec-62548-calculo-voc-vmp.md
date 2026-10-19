---
title: "Dimensionado de string FV: Voc, Vmp e Isc según IEC 62548"
description: "Cálculo de strings fotovoltaicos con corrección térmica de Voc y Vmp según IEC 62548, fusibles gPV según IEC 60269-6 y coordinación con el rango MPPT del inversor."
pubDate: 2026-10-19
keywords: ["dimensionado string fotovoltaico", "IEC 62548 calculo Voc Vmp", "corrección termica modulo fotovoltaico", "fusibles string fotovoltaico IEC 60269-6", "rango MPPT inversor fotovoltaico"]
author: "Editor"
---

El dimensionado del string fotovoltaico es uno de los cálculos más críticos en el diseño de una instalación fotovoltaica conectada a red. Un error en la estimación de la tensión máxima de circuito abierto —por no aplicar la corrección térmica a la temperatura mínima del emplazamiento— puede destruir el convertidor CC/CA la primera vez que la temperatura baja de 0 °C. Un error en el dimensionado de la corriente puede hacer que la protección de string no actúe en un fallo de arco CC. Este artículo desarrolla el método de cálculo normalizado según **IEC 62548:2016** *(Requirements for photovoltaic (PV) arrays)* y su integración con **IEC 60364-7-712** e **ITC-BT-40** del REBT.

---

## Parámetros eléctricos del módulo en condiciones STC y NOCT

Los fabricantes declaran los parámetros del módulo en **condiciones STC** (Standard Test Conditions): irradiancia G = 1.000 W/m², temperatura de célula Tc = 25 °C, espectro AM1.5. Los valores de placa son:

| Parámetro | Símbolo | Unidad | Módulo PERC 420 Wp típico |
|-----------|---------|--------|---------------------------|
| Potencia pico | Pmp | Wp | 420 |
| Tensión punto de máxima potencia | Vmp | V | 34,2 |
| Corriente punto de máxima potencia | Imp | A | 12,28 |
| Tensión de circuito abierto | Voc | V | 41,4 |
| Corriente de cortocircuito | Isc | A | 13,05 |
| Coeficiente de temperatura de Voc | α\_Voc | %/°C | −0,27 |
| Coeficiente de temperatura de Vmp | α\_Vmp | %/°C | −0,30 |
| Coeficiente de temperatura de Isc | α\_Isc | %/°C | +0,05 |
| Tensión máxima del sistema | Vsys\_max | V | 1.500 |

Los coeficientes de temperatura son la clave del cálculo térmico. Para tecnología **PERC monocristalino**, α\_Voc oscila entre −0,27 y −0,30 %/°C; para **TOPCon** de última generación se sitúa entre −0,22 y −0,25 %/°C, lo que permite cadenas ligeramente más largas en climas fríos.

---

## Cálculo del número de módulos en serie: límites Voc y Vmp

### Límite máximo: Voc a temperatura mínima

La **IEC 62548 cláusula 9** exige que la tensión de circuito abierto del string calculada a la temperatura mínima de diseño del emplazamiento no supere la tensión máxima admisible del inversor ni la tensión del sistema declarada por el módulo.

**Fórmula:**

```
Voc_cold = Voc_STC × [1 + (α_Voc / 100) × (Tmin − 25)]
Nmax = floor(Vinv_max / Voc_cold)
```

**Ejemplo** — Emplazamiento: meseta castellana, Tmin diseño = −15 °C; inversor Vinv\_max = 1.000 V CC:

```
Voc_cold = 41,4 × [1 + (−0,27/100) × (−15 − 25)]
         = 41,4 × [1 + (−0,0027) × (−40)]
         = 41,4 × 1,108
         = 45,87 V/módulo

Nmax = floor(1.000 / 45,87) = floor(21,8) = 21 módulos
```

Con 21 módulos en serie: Voc\_string\_cold = 21 × 45,87 = **963,3 V** < 1.000 V ✓

### Límite mínimo: Vmp a temperatura máxima

El inversor debe poder arrancar el MPPT incluso cuando los módulos están calientes y su Vmp cae. La temperatura máxima de célula bajo irradiancia plena se estima:

```
Tc_max = Tamb_max + (NOCT − 20) × (G / 800)
```

Para Tamb\_max = 40 °C, NOCT = 45 °C, G = 1.000 W/m²:

```
Tc_max = 40 + (45 − 20) × 1,25 = 40 + 31,25 = 71,25 °C

Vmp_hot = Vmp_STC × [1 + (α_Vmp / 100) × (Tc_max − 25)]
        = 34,2 × [1 + (−0,30/100) × (71,25 − 25)]
        = 34,2 × [1 − 0,0030 × 46,25]
        = 34,2 × 0,8613
        = 29,46 V/módulo

Nmin = ceil(Vmppt_min / Vmp_hot)
```

Si Vmppt\_min del inversor = 500 V:

```
Nmin = ceil(500 / 29,46) = ceil(16,97) = 17 módulos
```

### Número de módulos admisible

El número de módulos en serie del string debe satisfacer simultáneamente:

```
Nmin ≤ N ≤ Nmax  →  17 ≤ N ≤ 21
```

Para este ejemplo, **N = 20 módulos** es una elección con margen en ambos extremos:
- Voc\_cold (20 × 45,87 V) = **917,4 V** < 1.000 V (margen 8,3 %)
- Vmp\_hot (20 × 29,46 V) = **589,2 V** > 500 V (margen 17,8 %)

---

## Corriente de cortocircuito Isc y strings en paralelo

La corriente de cortocircuito del módulo también aumenta ligeramente con la temperatura y con la irradiancia. Para el dimensionado de la protección CC, la **IEC 62548 cláusula 10** exige aplicar un factor de 1,25 sobre la Isc nominal para considerar la irradiancia máxima posible (incluye concentración por reflexión):

```
Isc_design = 1,25 × Isc_STC = 1,25 × 13,05 = 16,3 A
```

Para un generador de **P strings en paralelo**, la corriente total en la entrada del inversor:

```
Iarray = P × Imp_STC (en operación normal MPPT)
Isc_array = P × Isc_design (para coordinación de protecciones)
```

La corriente de entrada máxima del inversor (Iinv\_max) debe satisfacer:

```
Iinv_max ≥ P × Isc_design
```

Si Iinv\_max = 50 A y Isc\_design = 16,3 A → P\_max = floor(50/16,3) = **3 strings en paralelo** como máximo por entrada MPPT.

### Corriente inversa de string

Con P strings en paralelo, si uno de los strings tiene un bypass o un fallo de polaridad, puede recibir la corriente inversa de los (P−1) strings restantes. Según **IEC 61730-2**, los módulos se ensayan a una corriente inversa de 1,35 × Isc. Si (P−1) × Isc\_design > 1,35 × Isc\_STC es obligatorio proteger cada string con fusible de string.

Para P = 3 strings: corriente inversa posible = 2 × 16,3 A = **32,6 A** >> 1,35 × 13,05 = 17,6 A → **fusibles de string obligatorios**.

---

## Protección de strings CC: fusibles gPV según IEC 60269-6

Los fusibles de string deben cumplir **IEC 60269-6:2010** (fusibles para circuitos fotovoltaicos en CC hasta 1.500 V). No es válido usar fusibles gG o aM de CA en circuitos CC fotovoltaicos, ya que la extinción del arco en CC es más difícil que en CA.

### Criterio de selección del fusible de string

La selección se realiza en tres pasos:

| Criterio | Límite | Cálculo ejemplo |
|----------|--------|-----------------|
| Corriente nominal mínima In ≥ | 1,4 × Isc\_STC del módulo | 1,4 × 13,05 = **18,3 A** → mínimo 20 A |
| Corriente nominal máxima In ≤ | Corriente inversa máxima del módulo / 1,35 | Irev\_max\_módulo / 1,35 |
| Tensión de ruptura en CC ≥ | Voc\_cold del string | 917,4 V → calibre ≥ 1.000 V CC |

Los calibres normalizados gPV disponibles en el mercado son: **10, 15, 20, 25, 30, 40, 50 A** en tensiones de 600, 1.000 y 1.500 V CC. Para nuestro ejemplo:

- In = **20 A** (primer valor estándar ≥ 18,3 A)
- Tensión de ruptura: **1.000 V CC** (≥ 917,4 V Voc\_cold)
- Categoría de uso: **gPV** (IEC 60269-6)

Los portafusibles deben ser específicos para CC fotovoltaico, con capacidad de interrupción en CC verificada. Las cajas de conexiones (junction boxes / string boxes) que agregan los strings deben llevar un seccionador CC por polo para poder aislar cada string en mantenimiento, según **IEC 60364-7-712:2017 cláusula 712.537**.

---

## Criterios de selección del inversor: rango MPPT y tensión máxima

El inversor es el elemento al que el string debe adaptarse. Los parámetros críticos para la compatibilidad son:

| Parámetro del inversor | Significado para el dimensionado | Verificación |
|------------------------|----------------------------------|-------------|
| Vmax\_entrada | Tensión máxima admisible CC | Voc\_cold ≤ Vmax |
| Vmppt\_min / Vmppt\_max | Rango de seguimiento MPPT | Vmp\_hot ≥ Vmppt\_min; Vmp\_cold ≤ Vmppt\_max |
| Imax\_entrada por MPPT | Corriente máxima CC admisible | P × Isc\_design ≤ Imax |
| Nentradas / Nmppt | Entradas independientes | Define el agrupamiento de strings |
| Potencia FV máxima | Potencia CC nominal | Σ Ppico\_strings ≤ 1,2 × Pinv (relación DC/AC) |

La **relación DC/AC** (o *oversizing ratio*) habitualmente se sitúa entre 1,1 y 1,3 en instalaciones a plena irradiancia, según el perfil de producción del emplazamiento. Un oversizing de 1,2 permite aprovechar mejor las horas con irradiancia moderada sin que el inversor recorte potencia de forma significativa.

### Configuraciones con multistring

Los inversores de string actuales ofrecen 2 a 4 entradas MPPT independientes con 2 a 3 entradas por MPPT. Esto permite conectar strings de diferente longitud, orientación o inclinación en MPPTs separados, siempre que cada MPPT opere dentro de su rango de tensión. **No se deben combinar strings de distinta longitud en el mismo MPPT** sin antes verificar que la diferencia de Vmp no supera el 5 %, ya que el seguidor operaría en un punto de compromiso que reduce la producción de ambos strings.

---

## Conclusión

El dimensionado correcto de un string fotovoltaico requiere cinco verificaciones independientes:

1. **Voc\_cold < Vinv\_max**: calculado con α\_Voc y Tmin del emplazamiento (IEC 62548 cláusula 9).
2. **Vmp\_hot > Vmppt\_min**: calculado con α\_Vmp y temperatura máxima de célula (IEC 62548 cláusula 9).
3. **P × Isc\_design ≤ Iinv\_max**: número de strings paralelo compatible con la entrada del inversor.
4. **Fusible gPV obligatorio si P ≥ 3**: calibrado según IEC 60269-6, con In ≥ 1,4 × Isc y Vrating ≥ Voc\_cold.
5. **Seccionador CC en cada string**: exigido por IEC 60364-7-712:2017 para mantenimiento seguro.

Un error en cualquiera de estos cinco puntos no es una desviación menor de normativa: es un riesgo de destrucción del equipo o de arco eléctrico en CC, que en un sistema a 1.000 V y 20 A puede mantener un arco durante minutos si no hay protección adecuada. El cálculo térmico con las temperaturas reales del emplazamiento —no los ±25 °C de STC— es la diferencia entre un sistema que opera dentro de sus límites y uno que los supera el primer invierno frío.
