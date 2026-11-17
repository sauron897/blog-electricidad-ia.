---
title: "Condensadores FP en BT: resonancia armónica y fusibles IEC 60831"
description: "Protección de baterías de condensadores BT contra resonancia armónica, fusibles y reactores desintonizadores según IEC 60831-1. Criterios numéricos para técnicos."
pubDate: 2026-11-17
keywords: ["condensadores FP BT resonancia armónica IEC 60831-1", "batería condensadores baja tensión protección", "reactor desintonizador condensadores", "resonancia armónica condensadores industriales"]
author: "Editor"
---

## Por qué los condensadores de corrección del FP fallan en instalaciones con armónicos

Un banco de condensadores de corrección del factor de potencia en BT no opera en aislamiento: comparte la red con transformadores, cables y cargas no lineales (variadores, rectificadores, SAI). La combinación de la capacidad del banco con la reactancia inductiva de la red crea un circuito LC cuya **frecuencia de resonancia paralela** puede coincidir con un armónico dominante de la instalación.

Cuando eso ocurre, la impedancia del paralelo LC tiende a infinito en esa frecuencia. La tensión armónica se amplifica, la corriente por el condensador se dispara —puede multiplicarse por 5 o más respecto a la corriente fundamental— y los fusibles o el propio dieléctrico del condensador ceden. El resultado habitual es un fallo prematuro del banco o disparos repetidos sin causa aparente en la protección.

La norma **IEC 60831-1** (adoptada en Europa como EN 60831-1 y referenciada en IEC 60364-5-55 para condensadores de instalación fija) fija los valores de corriente máxima admisible y las tolerancias de capacidad que condicionan el dimensionado de las protecciones. No prescribe el método de mitigación de armónicos, pero los valores que establece son el límite de diseño que debe respetarse con o sin reactor.

## Cálculo de la frecuencia de resonancia y orden resonante

La frecuencia de resonancia paralela entre el banco de condensadores (Q_c en kVAr) y la impedancia de cortocircuito de la red vista desde los bornes del banco es:

$$f_r = f_1 \cdot \sqrt{\frac{S_{cc}}{Q_c}}$$

donde:
- **f₁** = 50 Hz (frecuencia fundamental de la red)
- **S_cc** = potencia de cortocircuito en el punto de conexión (kVA), calculada según IEC 60909 a partir de la impedancia equivalente de la red
- **Q_c** = potencia reactiva del banco (kVAr)

El **orden armónico resonante** h_r = f_r / f₁ indica qué armónico queda amplificado:

| S_cc (kVA) | Q_c (kVAr) | h_r | f_r (Hz) |
|-----------|-----------|-----|---------|
| 630       | 50        | 3,55| 177,5   |
| 630       | 100       | 2,51| 125,5   |
| 1 000     | 50        | 4,47| 223,5   |
| 1 000     | 100       | 3,16| 158,2   |
| 1 600     | 100       | 4,0 | 200,0   |
| 1 600     | 200       | 2,83| 141,5   |

Los valores de h_r entre 3 y 5 son críticos porque coinciden con los armónicos 3.º (150 Hz), 5.º (250 Hz) y 7.º (350 Hz) que son típicos de rectificadores trifásicos en puente de diodo. Una instalación con un transformador de 630 kVA y un banco de 100 kVAr tiene h_r ≈ 2,5: próxima a la 3.ª armónica. Si hay cargas que generan ese armónico (motores con arrancadores no controlados, electrónica de consumo), el banco puede sufrir sobrecorriente permanente.

## Límites de IEC 60831-1 para corriente y tensión

**IEC 60831-1 cláusula 6.3** establece que los condensadores deben soportar de forma continua:

- **1,10 × U_n** (tensión nominal): el condensador debe operar con tensión eficaz 10 % superior a su tensión de placa.
- **1,30 × I_n** (corriente nominal): corriente eficaz continua 30 % superior a la correspondiente a U_n y Q_n.

La corriente nominal de un condensador trifásico de Q_c kVAr en un sistema trifásico a U_n kV es:

$$I_n = \frac{Q_c}{\sqrt{3} \cdot U_n}$$

Ejemplo: banco de 50 kVAr, 400 V → I_n = 50 / (1,732 × 0,4) = **72,2 A**

La corriente máxima continua admisible por IEC 60831-1 es 1,30 × 72,2 = **93,9 A**.

**Para el dimensionado de protecciones**, IEC 60831-1 cláusula 6.4 diferencia dos rangos según la tolerancia de capacidad:

| Rango de Q_c | Tolerancia C (IEC 60831-1) | I_máx protección |
|-------------|--------------------------|-----------------|
| Q_c ≤ 100 kVAr | +10 % / −5 % | 1,43 × I_n |
| Q_c > 100 kVAr | +5 % / −5 % | 1,36 × I_n |

El factor 1,43 resulta de combinar la tolerancia de capacidad (+10 %), la sobretensión continua admisible (1,10 × U_n, que eleva la corriente otro 10 % ya que I ∝ U/Z_c) y un margen de seguridad de 1,30 según el estándar: 1,10 × 1,10 × 1,30 ≈ 1,43.

**Consecuencia práctica**: el fusible o relé de protección del banco debe calibrarse para disparar **por encima** de 1,43 × I_n (banco pequeño) pero **por debajo** del límite de daño del condensador. En la práctica, se seleccionan fusibles tipo gG calibrados al 1,6 × I_n a 1,8 × I_n para absorber las corrientes de inserción (inrush) sin disparar en la maniobra, comprobando que no superen el I²t límite del condensador.

## Reactores desintonizadores: parámetro p y selección

La solución habitual para evitar la resonancia sin redimensionar el banco es instalar un **reactor desintonizador en serie** con cada escalón del banco. El reactor eleva la impedancia total del brazo condensador en la frecuencia de resonancia potencial, desplazando h_r a un valor no entero entre dos armónicos dominantes.

El parámetro de desintonía **p** se define como:

$$p = \frac{X_L}{X_C} = \frac{Q_L}{Q_C}$$

La frecuencia de sintonía del brazo LC resultante (donde la impedancia es nula y el sistema absorbe en lugar de amplificar) es:

$$f_{sin} = \frac{f_1}{\sqrt{p}}$$

Los valores normalizados más habituales en BT:

| p (%) | f_sintonía (Hz) | Protege principalmente contra |
|-------|----------------|-------------------------------|
| 5,67  | 210            | 5.ª armónica (250 Hz), margen estrecho |
| 7,0   | 189            | Entre 3.ª y 5.ª, estándar industrial |
| 14,0  | 134            | 3.ª armónica (150 Hz), cargas con THD alto |

**El valor p = 7 % (189 Hz) es el más extendido** porque sitúa la sintonía entre el 3.º y el 5.º armónico, garantizando que la impedancia del brazo sea inductiva (Z > 0) para todos los armónicos ≥ 5.ª, impidiendo que el banco absorba corriente de esos órdenes. No "filtra" el 5.º armónico (para eso haría falta p ≈ 4 %) pero evita la resonancia con él.

**Efecto del reactor sobre la tensión en el condensador**: con un reactor de p = 7 %, la tensión a frecuencia fundamental sobre el condensador es mayor que la tensión de red por el factor 1/(1 − p):

$$U_C = \frac{U_{red}}{1 - p} = \frac{400}{1 - 0{,}07} = 430 \text{ V}$$

Esto significa que un banco nominal 400 V con reactor del 7 % requiere condensadores con tensión de placa **440 V o 480 V** según disponibilidad del fabricante. El técnico que sustituye un condensador de 400 V sin reactor por otro de igual tensión en un banco desintonizado comete un error que provoca sobretensión permanente del 7 % sobre el límite de placa.

## Dimensionado del conductor de alimentación del banco

El conductor entre el cuadro y el banco ve tanto la corriente fundamental (a 50 Hz) como las corrientes armónicas que el banco absorbe. IEC 60364-5-52 y la norma IEC 60831-1 no fijan directamente el criterio, pero la práctica habitual (recogida en ABB CT8 y en CIRCUTOR) es aplicar factores multiplicadores sobre I_n en función del THD medido:

| THD de tensión (%) | Factor de dimensionado conductor |
|-------------------|----------------------------------|
| < 8 %             | 1,50 × I_n                       |
| 8 % – 15 %        | 1,60 × I_n                       |
| > 15 %            | 1,70 × I_n                       |

Para el ejemplo del banco de 50 kVAr (I_n = 72,2 A) en una instalación con THD del 10 %, el conductor debe dimensionarse para 72,2 × 1,60 = **115,5 A**. Según IEC 60364-5-52 tabla B.52.4, para cable RV-K 0,6/1 kV instalado en bandeja ventilada (método F), eso corresponde a sección **50 mm²** en Cu.

## Criterios de selección y diagnóstico en obra

El siguiente árbol de decisión resume los criterios aplicables antes de instalar o sustituir un banco de condensadores en BT industrial:

**1. Medir THD antes de instalar el banco**

Usar un analizador de red durante al menos 7 días (periodo de representatividad según EN 50160). Si el THD de tensión supera el 5 % o la corriente de algún armónico supera el 10 % de la fundamental, es obligatorio un reactor desintonizador.

**2. Calcular h_r con la S_cc real**

Pedir la S_cc al distribuidor (certificado de suministro) o calcularla desde la impedancia del transformador y la red aguas arriba según IEC 60909. Si h_r cae entre 3,5 y 5,5 o entre 2,5 y 3,5, el banco sin reactor queda en zona de riesgo.

**3. Seleccionar p según el perfil armónico**

- Cargas con rectificadores en puente (variadores, SAI): p = 7 % (189 Hz) es suficiente
- Cargas con rectificadores monofásicos o 3.ª armónica dominante: p = 14 % (134 Hz)
- Ausencia de armónicos comprobada con medición: p = 0 % (sin reactor, solo si S_cc/Q_c > 25)

**4. Verificar tensión de placa del condensador**

Con p = 7 %: tensión en bornes del condensador = U_red / (1 − 0,07). Para U_red = 400 V → 430 V. Seleccionar condensadores de **440 V mínimo**.

**5. Calibrar fusibles**

Fusible tipo gG, calibre ≥ 1,6 × I_n (para absorber inrush en la inserción) y ≤ 1,43 × I_n de la siguiente escala normalizada disponible. Si los dos criterios entran en conflicto (inrush elevado), evaluar fusibles tipo aR específicos para condensadores o contactores con resistencias de preinserción.

**6. Verificar conductor**

Aplicar el factor de THD de la tabla anterior. Comprobar que la caída de tensión en el ramal del banco a corriente máxima (1,43 × I_n) no excede el 1,5 % según IEC 60364-5-52.

## Conclusión

La protección de un banco de condensadores en BT no termina en calibrar el fusible según la corriente nominal. La interacción con la red determina si el banco entrará en resonancia, y la norma IEC 60831-1 marca los márgenes de corriente y tensión que no deben superarse de forma continua. El reactor desintonizador con p = 7 % es la solución estándar para instalaciones industriales con THD moderado, pero obliga a reclasificar la tensión del condensador y redimensionar el conductor. Un estudio previo de armónicos con medición real —no estimada— es el único criterio fiable para elegir el parámetro p correcto y evitar fallos prematuros del banco.
