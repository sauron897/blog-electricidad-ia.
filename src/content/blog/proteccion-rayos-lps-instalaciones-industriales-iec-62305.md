---
title: "Protección contra rayos LPS en instalaciones industriales según IEC 62305"
description: "Diseño de sistemas LPS internos y externos para instalaciones industriales: zonas LPZ, coordinación de SPD en cascada y cálculo de riesgo según IEC 62305-2/3/4."
pubDate: 2026-11-09
keywords: ["protección rayos LPS instalaciones industriales IEC 62305", "zonas LPZ protección rayo", "SPD coordinación zonas LPZ", "sistema externo captador bajante puesta tierra IEC 62305-3", "análisis riesgo rayos IEC 62305-2"]
author: "Editor"
---

## Parámetros del rayo y por qué definen toda la protección

Un rayo no es un fenómeno homogéneo. La primera descarga negativa descendente —estadísticamente la más frecuente— tiene un pico de corriente mediana de 31 kA con tiempo de frente de 3,8 µs y tiempo de cola de 75 µs (distribución log-normal según IEC 62305-1 Tabla 1). Las descargas positivas, aunque menos frecuentes, pueden superar los 200 kA con contenido de carga mucho mayor.

Estos parámetros no son académicos: determinan directamente qué exige la norma a cada componente. El ensayo de los SPD de Clase I se realiza con la forma de onda normalizada **10/350 µs** (que reproduce la integral de corriente, es decir, la carga y la energía específica del rayo natural) mientras que el ensayo de Clase II usa **8/20 µs**, que tiene la misma cresta pero una energía 20 veces menor. Un SPD de Clase II instalado en la frontera LPZ 0→1 no absorbe el contenido energético del rayo: se destruye.

La serie IEC 62305 (transpuesta en España como **UNE-EN 62305** en sus partes 1 a 4) estructura toda la protección en torno a este principio: reducir progresivamente los parámetros electromagnéticos del rayo desde el exterior hasta el interior de la instalación.

---

## Estructura de la norma IEC 62305 y el concepto de zonas LPZ

La norma se divide en cuatro partes con roles bien diferenciados:

| Parte | Título | Contenido principal |
|-------|--------|---------------------|
| IEC 62305-1 | Principios generales | Parámetros del rayo, daños, pérdidas |
| IEC 62305-2 | Gestión del riesgo | Cálculo de riesgo anual, decisión de proteger |
| IEC 62305-3 | Daños físicos y peligro para personas | LPS externo: captadores, bajantes, tierra, distancia de separación |
| IEC 62305-4 | Sistemas eléctricos y electrónicos | LPS interno: zonas LPZ, SPD, enlaces de equipotencialidad, apantallamiento |

El concepto central de IEC 62305-4 es la **Lightning Protection Zone (LPZ)**. Cada zona se define por el nivel de amenaza electromagnética que contiene:

- **LPZ 0A**: exterior de la estructura — exposición directa a descarga y campo electromagnético completo del rayo (Iimp máximo, dB/dt máximo).
- **LPZ 0B**: exterior parcialmente protegido por el volumen de captadores — sin descarga directa, pero campo completo.
- **LPZ 1**: interior de la estructura tras SPD de Clase I en la entrada de servicios — corriente parcial atenuada, campo reducido por apantallamiento estructural.
- **LPZ 2 y superiores**: subredes internas con SPD de Clase II/III adicionales — campo y corrientes residuales mínimos compatibles con equipos sensibles (PLCs, instrumentación, comunicaciones).

La frontera entre zonas es el lugar donde **obligatoriamente** se instala el SPD correspondiente y se realiza la equipotencialidad de todos los conductores que la cruzan.

---

## LPS externo: captadores, bajantes y sistema de tierra (IEC 62305-3)

### Nivel de protección LPL y método de la esfera rodante

IEC 62305-3 define cuatro **Niveles de Protección contra el Rayo (LPL I–IV)**, cada uno con su radio de esfera rodante:

| LPL | Radio esfera rodante (m) | Corriente mínima del rayo protegido (kA) | Probabilidad de protección (%) |
|-----|--------------------------|------------------------------------------|-------------------------------|
| I | 20 | 3 | 99 |
| II | 30 | 5 | 97 |
| III | 45 | 10 | 91 |
| IV | 60 | 16 | 84 |

La geometría que supera el método de la esfera rodante requiere puntas de Franklin, conductores de cumbrera o malla de captadores. Para naves industriales con cubierta plana, el ángulo protegido depende de la altura: una punta a 10 m de altura con LPL II protege un cono de ángulo ≤ 35° (tabla en IEC 62305-3 Anexo B).

### Dimensiones mínimas de bajantes

| Material | Sección mínima conductor sólido / trenzado (mm²) | Sección cinta (mm²) |
|----------|--------------------------------------------------|---------------------|
| Cobre | 16 | 50 (2 mm espesor) |
| Aluminio | 25 | 70 |
| Acero inoxidable | 50 | 50 |
| Acero galvanizado | 50 | 50 |

El número de bajantes mínimo es 2 para cualquier estructura, con espaciado máximo de 10 m (LPL I-II) o 15 m (LPL III-IV) medidos en perímetro.

### Distancia de separación s para evitar chispazos peligrosos

Cuando los bajantes discurren junto a instalaciones metálicas (tuberías, escaleras, bandejas de cables), existe riesgo de chispazo si la diferencia de potencial supera la rigidez dieléctrica del medio. La distancia de separación mínima es:

```
s = ki × (kc / km) × l
```

Donde:
- **ki** = 0,04 (LPL I), 0,06 (LPL II), 0,1 (LPL III/IV)
- **kc** = factor de distribución de corriente (0,5 con bajante único; 0,25 con 4 bajantes simétricos)
- **km** = 0,5 (hormigón), 1,0 (aire)
- **l** = distancia vertical desde el punto de unión más próximo hasta el punto considerado (metros)

Ejemplo: una nave con LPL II, 2 bajantes simétricos (kc = 0,5), bajante en aire (km = 1,0) y el cruce de una bandeja a 6 m desde el suelo:
s = 0,06 × (0,5 / 1,0) × 6 = **0,18 m**

Si la separación real es menor, se requiere conductor de equipotencialidad entre ambos.

---

## LPS interno: coordinación de SPD en cascada (IEC 62305-4)

### Selección de SPD por frontera de zona

| Frontera LPZ | Clase SPD (IEC 61643-11) | Forma onda ensayo | Parámetro clave | Valor típico instalación industrial |
|--------------|--------------------------|-------------------|-----------------|--------------------------------------|
| 0A/0B → 1 | Clase I (Tipo 1) | 10/350 µs | Iimp por polo | ≥ 12,5 kA (LPL I, 4 polos, 50 kA total) |
| 1 → 2 | Clase II (Tipo 2) | 8/20 µs | Imax por polo | ≥ 20 kA; Uoc ≤ 2,5 kV a 230 V |
| 2 → 3 | Clase III (Tipo 3) | Onda combinada | Uoc | 1,2 kV; Up ≤ nivel de inmunidad equipo |

El criterio de selección del Iimp para Clase I se obtiene de la distribución de la corriente de rayo. Según IEC 62305-3 §8.3, para un rayo de primera descarga negativa con I = 200 kA (LPL I) y 4 conductores de alimentación + 1 de tierra, la corriente parcial por servicio es I/2 = 100 kA, distribuida entre los conductores activos: 25 kA por polo en un sistema trifásico+N. Se aconseja un margen de diseño del 50 % → Iimp ≥ 12,5 kA efectivo (25 kA declarado por el fabricante).

### Coordinación de energía en cascada y distancia mínima entre etapas

Un SPD de Clase I descarga la mayor parte de la energía pero presenta un nivel de protección Up relativamente alto (hasta 2,5 kV para 230 V). El SPD de Clase II aguas abajo limita a Up ≤ 1,5 kV. Para que la coordinación funcione, **la inductancia del cable entre ambos SPD debe absorber la diferencia de energía**: IEC 62305-4 Anexo C indica un valor mínimo de **10 µH**, equivalente aproximadamente a **10 m de cable** (L ≈ 1 µH/m para cable unipolar estándar).

Si el espacio del cuadro no permite esa separación, se emplean:
- SPD combinado Clase I+II en un solo módulo con red de desacoplamiento interna.
- Inductancia de desacoplamiento dedicada (bobina de choque) de ≥ 10 µH, Iimp compatible.

El nivel de protección Up del SPD de Clase III en el punto de utilización debe satisfacer:
```
Up ≤ 0,8 × Uw
```
Donde Uw es la tensión soportada al impulso del equipo a proteger (IEC 60664-1 Tabla F.2):
- Equipos de categoría II (electrodomésticos, PLC): Uw = 2,5 kV → Up ≤ 2,0 kV
- Equipos de categoría I (circuitos protegidos, instrumentación de señal): Uw = 1,5 kV → Up ≤ 1,2 kV

### Equipotencialidad en la frontera LPZ 1

Todos los conductores metálicos que cruzan la frontera LPZ 0→1 deben unirse al sistema de equipotencialidad en ese punto. Para líneas de alimentación, mediante el SPD. Para tuberías metálicas, mediante eclisas o latiguillos de equipotencialidad de sección ≥ 6 mm² Cu (ó ≥ 50 mm² Fe). Para cables de señal (4–20 mA, PROFIBUS, Ethernet industrial), con SPD de señal de Clase I o II según energía del rayo esperada en la frontera.

---

## Cálculo de riesgo simplificado según IEC 62305-2

La decisión de instalar LPS no es voluntaria cuando el análisis de riesgo lo requiere. IEC 62305-2 (UNE-EN 62305-2) cuantifica el riesgo anual R como suma de componentes:

```
R = RA + RB + RC + RM
```

Los componentes más relevantes para instalaciones industriales son:
- **RB**: pérdida de patrimonio por daño físico (incendio)
- **RC**: fallo de sistemas eléctricos y electrónicos internos

El riesgo tolerable RT para instalaciones industriales es típicamente **10⁻⁵/año** para pérdidas económicas, y **10⁻⁵/año** para pérdida de vidas humanas.

### Variables de entrada clave

| Variable | Significado | Valor típico España |
|----------|-------------|---------------------|
| Ng | Densidad de impactos (impactos/km²/año) | 1,0–2,5 (zona Norte/interior peninsular) |
| Ad | Área de captación de la estructura (m²) | depende de dimensiones |
| Cd | Factor de localización | 0,25 (junto a objetos más altos), 1 (aislada en campo) |
| Ct | Factor de tipo de estructura | 1 (normal) a 2 (con riesgo de explosión) |
| Ce | Factor de entorno | 0,5 (rodeada de árboles o edificios de similar altura) |

La frecuencia de impactos peligrosos directos sobre la estructura se calcula como:
```
Nd = Ng × Ad × Cd × Ce × Ct × 10⁻⁶  (impactos/año)
```

Si **Nd > Nc** (número aceptable de impactos) = 10⁻⁵ / (PT × L) donde PT y L son probabilidad de daño y pérdidas relativas —que el software de cálculo según Anexo E de IEC 62305-2 determina automáticamente— se requiere LPS.

Para una nave industrial aislada de 60 × 30 m (Ad = 2.880 m² incluyendo área de captura oblicua), Ng = 1,5, Cd = 1, Ce = 1, Ct = 1:
Nd = 1,5 × 2.880 × 1 × 1 × 1 × 10⁻⁶ = **4,32 × 10⁻³ impactos/año**

Este valor supera ampliamente Nc = 10⁻⁵, por lo que la instalación de LPS es necesaria y su nivel LPL se determina para reducir R hasta RT.

---

## Criterios de selección para el ingeniero proyectista

Los puntos de decisión en un proyecto LPS real, ordenados por relevancia práctica:

1. **¿Se requiere LPS?** → Realizar análisis de riesgo IEC 62305-2. Para instalaciones con contenido inflamable (Ct = 2) o equipos electrónicos críticos, casi siempre se requerirá LPL I o II.

2. **LPL del LPS externo** → Determinar radio de esfera rodante. Para naves industriales con cubierta metálica que actúa como jaula de Faraday natural, la propia estructura puede aprovecharse como captador y bajante si las secciones cumplen IEC 62305-3.

3. **Clase I en el origen del cuadro general (CGBT)** → Obligatorio cuando la instalación tiene LPS externo o está en zona con riesgo de rayo no despreciable (Ng > 1). Iimp mínimo según distribución de corriente, Up ≤ 2,5 kV.

4. **Clase II en cada subcuadro** → Proteger la frontera LPZ 1→2 de cada zona funcional. Coordinar Up < 1,5 kV con 10 m de cable o inductancia respecto al Clase I aguas arriba.

5. **Clase III en equipos sensibles** → PLC, variadores con tarjeta de comunicaciones, instrumentación de campo. Up ≤ 0,8 × Uw del equipo. Verificar compatibilidad de corriente con fabricante del equipo.

6. **SPD en líneas de señal** → Las líneas de comunicación (4–20 mA analógica, señales digitales) que salen de la nave o cruzan fronteras LPZ requieren SPD de señal coordinados con los de potencia (mismo potencial de referencia, equipotencialidad en cuadro).

7. **Inspección y mantenimiento** → IEC 62305-3 §8.5 exige inspección visual anual y medición de resistencia de tierra cada 5 años (< 10 Ω para LPS eficaz; < 1 Ω en instalaciones con descargadores de línea MT). Tras impacto confirmado, revisión inmediata de bajantes y SPD.

---

## Conclusión

El diseño de un LPS eficaz no se reduce a instalar pararrayos en la cubierta. La lógica de zonas LPZ de IEC 62305-4 exige pensar la instalación como capas concéntricas de protección: captador y bajante exteriores, SPD de Clase I en la frontera LPZ 0→1, Clase II en subcuadros (LPZ 1→2) y Clase III en el punto de uso (LPZ 2→3), con distancias de coordinación o inductancias de desacoplamiento entre etapas.

El cálculo de riesgo de IEC 62305-2 cuantifica si la protección es necesaria y qué nivel LPL se justifica económicamente. Para instalaciones industriales con equipos electrónicos, instrumentación o riesgo de explosión, el análisis casi invariablemente conduce a LPL I o II, con la consiguiente exigencia de Iimp ≥ 12,5 kA en el Clase I y Up ≤ 1,5 kV en el Clase II.

La compatibilidad entre SPD de distintas etapas no es automática: verificar siempre la coordinación energética según IEC 62305-4 Anexo C, y no confiar en las hojas técnicas del fabricante si no hay ensayo de coordinación normalizado entre el par de SPDs.
