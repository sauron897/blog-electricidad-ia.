---
title: "SPD en instalaciones BT: clases y coordinación según IEC 61643-11"
description: "Guía técnica de SPD para instalaciones de baja tensión: tipos T1/T2/T3, parámetros Iimp/In/Up, coordinación en cascada e ITC-BT-23. Para ingenieros."
pubDate: 2026-09-14
keywords: ["SPD proteccion sobretensiones IEC 61643", "dispositivo proteccion sobretensiones tipo 1 2 3", "coordinacion SPD cascada baja tension", "ITC-BT-23 sobretensiones transitorias"]
author: "Editor"
---

## Introducción: por qué el SPD no es opcional en instalaciones modernas

Los Dispositivos de Protección contra Sobretensiones (SPD, *Surge Protective Device*) protegen equipos e instalaciones frente a sobretensiones transitorias de origen atmosférico o por maniobra. En España, la **ITC-BT-23 del REBT** exige su instalación en edificios con nivel de exposición significativo: edificios con sistema de protección externa contra el rayo (SPCR), zonas con índice de incidencia de rayos al suelo Ng > 2,5 descargas/km²/año, e instalaciones con equipos electrónicos sensibles.

La norma de referencia es **IEC 61643-11:2011** (adoptada como **UNE-EN 61643-11:2013** en España), que define la clasificación, los ensayos de tipo y los parámetros eléctricos de los SPD para sistemas de distribución en CA hasta 1.000 V. La IEC 61643-31 cubre los SPD para DC (fotovoltaica hasta 1.500 V). Ignorar estos dispositivos, o seleccionarlos sin coordinarlos, no solo deja la instalación desprotegida: puede causar que el propio SPD destruya la maniobra aguas abajo o que dispare el diferencial antes de actuar.

---

## Tipos de SPD: T1, T2 y T3 y sus ondas de ensayo

La clasificación de los SPD no es arbitraria: refleja la energía que cada dispositivo puede absorber y la forma de onda bajo la que se ensaya.

### Tipo 1 (Clase I — Ensayo 10/350 µs)

El SPD Tipo 1 se instala en el **cuadro general de distribución (CGD)** o a la entrada del edificio, inmediatamente aguas abajo del contador o del embarrado principal. Está diseñado para derivar la corriente de rayo parcial que puede llegar a la instalación interior a través del sistema de protección externo (bajantes, mallas) o mediante el neutro de la red.

- **Onda de ensayo**: impulso de corriente 10/350 µs (simula el rayo directo).
- **Parámetro de ensayo**: **Iimp** (corriente de impulso), valores normalizados: 12,5 kA / 25 kA / 50 kA por modo (L-N, L-PE, N-PE).
- **Requisito IEC 61643-11**: el SPD T1 debe sobrevivir a 5 impulsos sucesivos a Iimp sin degradación del nivel de protección Up.
- **Tensión de protección Up**: ≤ 4 kV según IEC 60664-1 Categoría IV (entrada de acometida). En la práctica, fabricantes ofrecen Up ≤ 2,5 kV.

### Tipo 2 (Clase II — Ensayo 8/20 µs)

El SPD Tipo 2 es el más habitual en cuadros secundarios y subcuadros. Deriva la energía residual que no absorbió el T1 o las sobretensiones inducidas por rayos cercanos y maniobras en la red.

- **Onda de ensayo**: impulso de corriente 8/20 µs (simula el rayo inducido y maniobras).
- **Parámetro de ensayo**: **In** (corriente nominal de descarga), valores normalizados: 5 / 10 / 20 / 40 kA. También se especifica **Imax** (corriente máxima de descarga), generalmente 2 × In.
- **Tensión de protección Up**: ≤ 2,5 kV (Categoría III, embarrado principal) o ≤ 1,5 kV (Categoría II, equipos de consumo).
- Uso típico: SPD 40 kA (8/20 µs) con Up ≤ 1,5 kV en cuadros de distribución de plantas.

### Tipo 3 (Clase III — Onda combinada)

El SPD Tipo 3 protege directamente los equipos electrónicos (en el punto de uso o integrado en regletas/bases de enchufe). Su energía absorbible es menor.

- **Onda de ensayo**: onda combinada 1,2/50 µs (tensión en circuito abierto) + 8/20 µs (corriente en cortocircuito), denominada **Uoc**.
- **Parámetro de ensayo**: Uoc = 6 kV / Isc = 3 kA en la onda combinada.
- **Instalación**: siempre como complemento de T1 y/o T2, nunca como única protección.

| Parámetro | SPD Tipo 1 | SPD Tipo 2 | SPD Tipo 3 |
|---|---|---|---|
| Onda de ensayo | 10/350 µs | 8/20 µs | Combinada (1.2/50 + 8/20) |
| Parámetro principal | Iimp | In / Imax | Uoc |
| Iimp / In típico | 12,5–50 kA | 5–40 kA | (Uoc = 6 kV) |
| Posición en instalación | CGD / entrada | Subcuadros | Punto de uso |
| Nivel Up máx. (IEC 60664-1) | ≤ 4 kV (Cat. IV) | ≤ 2,5 kV (Cat. III) | ≤ 1,5 kV (Cat. II) |
| Tecnología habitual | Varistor + Descargador de gas | Varistor (MOV) | Varistor / TVS |

---

## Parámetros eléctricos clave para la selección

### Tensión de trabajo continua Uc

La **tensión máxima de servicio continuo Uc** es la tensión AC eficaz que el SPD puede soportar indefinidamente sin degradarse. Debe cumplirse:

```
Uc ≥ 1,1 × U0
```

Donde U0 es la tensión de fase a neutro del sistema. Para una red 230/400 V (TN-S o TT):

- Modo L-N: Uc ≥ 1,1 × 230 V = **253 V** → se elige Uc = 275 V o 320 V.
- Modo L-PE: ídem, Uc ≥ 253 V.
- Modo N-PE: Uc ≥ 255 V (considera desequilibrios).

En sistemas IT con neutro aislado, Uc debe calcularse respecto a la tensión de red fase-fase, no fase-neutro.

### Nivel de protección Up y coordinación con Uw

El **nivel de protección Up** es la tensión de cresta que aparece en los bornes del SPD durante el ensayo. La condición fundamental de protección es:

```
Up + ΔU ≤ Uw (equipo protegido)
```

Donde ΔU es la caída de tensión en los conductores de conexión entre el SPD y el equipo. A 100 A de corriente de derivación y 0,5 m de cable de 10 mm², ΔU ≈ 300 V adicionales, lo que refuerza la importancia de minimizar la longitud de los conductores de tierra y fase del SPD (máx. 0,5 m recomendado, idealmente < 0,3 m).

Los **niveles de tensión de choque soportada Uw** para equipos según IEC 60664-1:

| Categoría IEC 60664-1 | Uw típico (230/400 V) | Aplicación |
|---|---|---|
| IV | 6 kV | Equipos en acometida (contadores, cabezas de línea) |
| III | 4 kV | Cuadros de distribución, motores, embarrados BT |
| II | 2,5 kV | Electrodomésticos, equipos con enchufe |
| I | 1,5 kV | Equipos electrónicos de consumo, PCBs protegidas |

### TOV: sobretensiones temporales

El SPD también debe soportar **Sobretensiones Temporales (TOV)**, que pueden aparecer por falta de neutro en sistemas TN o por defecto a tierra en sistemas IT. IEC 61643-11 exige que el SPD soporte la TOV sin destruirse durante el tiempo especificado (200 ms para TOV de falta de neutro). El parámetro **UT** del SPD debe ser ≥ 1,45 × U0 para sistemas TN, es decir, ≥ 334 V.

---

## Coordinación de SPD en cascada: distancias y desacoplo

La coordinación en cascada (T1 → T2 → T3) es crítica. Si dos SPD están demasiado próximos eléctricamente, el T2 actúa antes que el T1 por ser más rápido (varistor MOV < 25 ns vs. descargador de gas > 100 ns), descargando energía que no puede absorber y destruyéndose.

### Regla de los 10 metros

IEC 61643-11 Anexo C establece que entre SPD coordinados en cascada debe existir una impedancia de desacoplo equivalente a **≥ 10 m de cable** (inductancia ≈ 1 µH/m → L ≥ 10 µH entre T1 y T2). Si la distancia física es < 10 m, se debe insertar una **bobina de desacoplo** (choke) con L ≥ 1,5 µH entre T1 y T2 (o L ≥ 10 µH si el fabricante no garantiza coordinación propia).

Muchos fabricantes ofrecen pares T1+T2 con desacoplo integrado que cumplen la coordinación sin distancia mínima; en ese caso se exige certificación específica de coordinación según IEC 61643-12.

### Fusibles de protección del SPD

El SPD no protege la línea: la línea (o fusible de backup) protege al SPD. El fusible aguas arriba del SPD debe:
1. No abrir durante la descarga nominal (Iimp o In).
2. Abrir tras un cortocircuito en el SPD degradado.

IEC 61643-11 define la **corriente de cortocircuito soportada Isccr**: el SPD debe sobrevivir a una falta de la tensión de red con Isccr durante el tiempo necesario para que el fusible abra. Valores habituales: Isccr = 25 kA / 50 kA. El fusible de backup recomendado es **gG** (IEC 60269-1), calibre según tabla del fabricante (típico: 63–160 A para SPD T2 de 40 kA).

---

## Criterios de selección en obra

Antes de especificar un SPD, el técnico debe responder en este orden:

1. **¿Existe SPCR en el edificio?** → Si sí, exige T1 coordinado con el sistema de tierra del SPCR. Iimp según riesgo: mínimo Iimp = 12,5 kA por polo en edificios normales; 25 kA en edificios con estructura metálica o en zona de alta Ng.

2. **¿Cuál es el sistema de puesta a tierra?** → TN-S: SPD en modo L-N + N-PE. TT: SPD en modo L-PE + N-PE. IT: consultar fabricante para Up > Ul × √3.

3. **¿Cuáles son los equipos más sensibles?** → Determina Uw mínimo exigido y por tanto Up máximo admisible. Para PLC industriales: Up ≤ 1,5 kV. Para inversores fotovoltaicos: consultar hoja de datos (típico Up ≤ 2 kV).

4. **¿Cuál es la corriente de cortocircuito en el punto de instalación?** → Elige Isccr ≥ Icc del punto. En BT industrial puede superar 25 kA en cabecera; verificar con cálculo IEC 60909.

5. **¿Qué longitud hay entre T1 y T2?** → Si < 10 m, exige par coordinado certificado o bobina de desacoplo.

6. **¿El SPD es reemplazable con tensión presente?** → Algunos SPD modulares permiten sustituir el cartucho activo sin cortar la instalación (función "hot-swap"); valorarlo en instalaciones críticas.

| Situación | SPD mínimo recomendado | Normativa |
|---|---|---|
| Edificio sin SPCR, Ng < 2,5 | T2, In = 20 kA, Up ≤ 1,5 kV | ITC-BT-23, IEC 61643-11 |
| Edificio con SPCR | T1 + T2 coordinados, Iimp ≥ 12,5 kA | ITC-BT-23 §4, IEC 61643-12 |
| Instalación FV BT hasta 1.500 V DC | T2 DC, In ≥ 20 kA (8/20 µs) | IEC 61643-31, REBT ITC-BT-40 |
| Equipo electrónico Cat. I (< 1,5 kV Uw) | T3 + T2 aguas arriba, Up ≤ 1 kV | IEC 61643-11, IEC 60664-1 |
| CPM (caja protección medida) | T1 exterior + T2 CGD interior | Guía-BT-23 §5.2 |

---

## Conclusión

Seleccionar un SPD no es elegir el kA más alto del catálogo: es coordinar tres parámetros (Uc, Up, Iimp/In) con el sistema de tierra, la categoría de los equipos (IEC 60664-1) y la energía disponible en el punto de instalación. La ITC-BT-23 fija los casos de obligatoriedad; la IEC 61643-11 fija los ensayos que garantizan que el SPD que compras hace lo que dice. La coordinación en cascada exige al menos 10 m de cable o bobina de desacoplo entre etapas, y el par T1+T2 certificado según IEC 61643-12 es la solución más robusta en instalaciones donde la distancia no puede garantizarse. Como paso inmediato: revisa en tu próximo proyecto si el punto de instalación del T1 está dentro de los 0,5 m del embarrado de tierra del SPCR — es el error de instalación más frecuente y anula completamente la coordinación.
