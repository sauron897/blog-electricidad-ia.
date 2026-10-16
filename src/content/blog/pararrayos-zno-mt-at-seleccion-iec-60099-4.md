---
title: "Pararrayos ZnO en MT/AT: selección Ur, Uc y coordinación IEC 60099-4"
description: "Criterios de selección de pararrayos de óxido metálico ZnO en redes MT/AT: tensión asignada Ur, Uc, TOV, clases de descarga y coordinación de aislamiento según IEC 60099-4 e IEC 60071."
pubDate: 2026-10-16
keywords: ["pararrayos ZnO media tensión IEC 60099-4", "descargador sobretensiones ZnO", "coordinación aislamiento pararrayos", "tensión asignada Ur Uc pararrayos MT"]
author: "Editor"
---

## Fundamento físico del varistor de ZnO

Los pararrayos de óxido metálico de zinc (ZnO) modernos son dispositivos de resistencia no lineal sin explosores (gapless). Su elemento activo es una columna de varistores cerámicos de ZnO dopado con óxido de bismuto, manganeso y cobalto. La característica tensión-corriente sigue la ley:

**I = k · V^α**

donde el coeficiente de no linealidad α vale típicamente entre 25 y 50 para varistores de ZnO de calidad. Esto implica que un incremento del 10 % en la tensión aplicada multiplica la corriente por un factor de 12 a 60, lo que confiere al varistor un comportamiento cuasiideal: conducción prácticamente nula en condiciones nominales (corriente residual < 1 mA a Uc) y conducción masiva al superar la tensión de codo (knee-point voltage).

La ausencia de explosores elimina la tensión de arco del diseño antiguo de SiC, reduce el nivel de protección residual (Vres) y suprime el seguimiento de corriente industrial —la corriente de frecuencia de red que fluía tras cada descarga en los diseños con entrehierro—. El resultado es un nivel de protección más bajo y una vida útil superior, ambos cuantificados en IEC 60099-4.

## Parámetros clave según IEC 60099-4

La norma IEC 60099-4 (edición 2014, adoptada como UNE-EN 60099-4:2016) define los parámetros de ensayo y los criterios de aceptación. Para una selección correcta, el técnico debe manejar los siguientes valores:

| Parámetro | Símbolo | Definición |
|---|---|---|
| Tensión máxima del sistema | Us | Tensión fase-fase más elevada de la red (rms) |
| Tensión de operación continua | Uc | Tensión fase-tierra aplicada en servicio normal, Uc ≥ Us/√3 |
| Tensión asignada | Ur | Tensión rms máxima de TOV soportada 10 s; Ur ≥ k·Uc |
| TOV (sobretensión temporal) | VTOV | Tensión fase-tierra durante falta a tierra o apertura, duración tipica 0,1–10 s |
| Corriente nominal de descarga | In | 5, 10 o 20 kA cresta (impulso 8/20 μs), según clase de red |
| Clase de descarga de línea | LDC | 1–5 según IEC 60099-4 §4.6, relacionada con energía absorbible |
| Tensión residual | Vres | Tensión pico en bornes durante descarga In |
| Nivel de protección por impulso | Up | Vres a In; debe quedar ≥ 20 % por debajo del NBI del equipo protegido |

### Selección de Uc y Ur en función del tratamiento del neutro

El tratamiento del neutro es el primer criterio de selección, pues determina la TOV más desfavorable:

| Tipo de red | Factor de tierra k₁ | Uc mín | Ur mín (TOV 10 s) |
|---|---|---|---|
| Neutro rígido (TN/TT BT) | 1,0 | Us/√3 | 1,05 · Uc |
| Neutro impedante (resistencia 20 kV) | 1,4 | 1,4 · Us/√3 | 1,25 · Uc |
| Neutro aislado / resonante (Petersen) | 1,73 | Us/√3 · 1,73 | 1,40 · Uc |
| Red 20 kV típica España (IEC 60364, RED) | 1,4–1,73 | ≥ 14,4 kV (red 20 kV) | ≥ 17,5 kV |

Para una red de distribución española a 20 kV con neutro aislado:
- Us = 24 kV (tensión más elevada para 20 kV, según IEC 60038)
- Uc ≥ 24/√3 · 1,73 = **24 kV** (fase-tierra)
- Ur ≥ 1,40 · 24 = **24 kV** → se elige el escalón normalizado Ur = **24 kV**

En redes 20 kV de neutro compensado con bobina Petersen, la TOV puede mantenerse durante el tiempo de extinción del arco de falta (segundos a minutos). En este caso el tiempo de TOV a considerar es 200 s o más, y el factor de corrección de la curva TOV-tiempo del fabricante reduce el margen disponible. La norma IEC 60099-5 (guía de aplicación) da las curvas de factor de TOV f(t) para distintos materiales de varistor.

## Coordinación de aislamiento según IEC 60071-1

La coordinación de aislamiento establece la relación entre el nivel de protección del pararrayos (Up) y el nivel básico de aislamiento al impulso (NBI o BIL) del equipo protegido:

**Margen de protección MP (%) = (NBI – Up) / NBI · 100**

IEC 60071-2 exige un margen de seguridad mínimo del 20 % para subestaciones (factor de coordinación Kcd ≥ 1,25) con separación corta entre pararrayos y equipo protegido. Para instalaciones con distancia d > 5 m hay que añadir la sobretensión de reflexión en la onda viajera (incremento de 2 kV/m en la onda incidente de 1,2/50 μs).

Para un transformador 20 kV/0,4 kV con NBI = 125 kV (tabla de niveles de aislamiento IEC 60071-1, clase 24 kV):

- Se elige pararrayos 24 kV, In = 10 kA, Ur = 24 kV
- Vres (10 kA, 8/20 μs) típico para clase LDC-2: **56–65 kV** pico
- Margen de protección: (125 – 65) / 125 = **48 %** → cumple el mínimo del 20 %

Si la distancia pararrayos-transformador es 8 m, hay que añadir: Δu = 2 · 8 = 16 kV → Up efectivo = 65 + 16 = 81 kV. Margen: (125 – 81) / 125 = **35 %** → sigue siendo aceptable.

## Clase de descarga de línea y energía absorbida

La clase de descarga de línea (LDC 1 a 5) cuantifica la capacidad del pararrayos para absorber la energía almacenada en una línea de transmisión durante el cierre sobre una línea cargada (energía de maniobra). IEC 60099-4 §4.6 define el ensayo mediante impulso de corriente de larga duración (4 ms).

| Clase LDC | Energía mín. (kJ/kV de Ur) | Aplicación típica |
|---|---|---|
| 1 | — | Distribución BT, MT hasta 36 kV redes cortas |
| 2 | 0,5 | MT distribución 20-36 kV, cables cortos |
| 3 | 1,0 | Líneas MT/AT, subestaciones transformador |
| 4 | 2,0 | Líneas AT largas (110-220 kV) |
| 5 | 4,0 | Líneas de transmisión 400 kV+ |

En una subestación 20/0,4 kV alimentada por cable subterráneo de 3 km XLPE, la energía de maniobra es baja y basta LDC 2. Sin embargo, si existe un banco de condensadores de 600 kvar conectado aguas abajo, la descarga del banco puede imponer una energía de 1–2 kJ/kV; en ese caso se requiere LDC 3 y conviene consultar al fabricante la energía total absorbible (rated TOV energy handling capability, expresada en kJ).

## Criterios de selección aplicables en obra

El proceso de selección en campo sigue esta lógica de decisión:

**1. Determinar Us de la red** (según IEC 60038: 12, 17,5, 24, 36, 52, 72,5 kV para MT).

**2. Identificar el tratamiento del neutro** y calcular el factor de tierra k₁. En España las redes de distribución 20 kV operan mayoritariamente en neutro aislado o compensado → k₁ = 1,73.

**3. Calcular Uc mín:**
- Uc ≥ Us/√3 · k₁

**4. Calcular Ur mín con curva TOV-tiempo:**
- Obtener la duración de la TOV prevista (tiempo de despeje de falta con protección automática)
- Consultar la curva TOV-tiempo del fabricante para el varistor elegido
- Ur debe quedar por encima del punto (VTOV, t_falta) en esa curva

**5. Verificar nivel de protección:**
- Vres (In, 8/20 μs) + sobretensión de distancia < NBI / 1,25
- Si no se cumple, subir In (de 10 kA a 20 kA) o acercar el pararrayos al equipo

**6. Seleccionar LDC:**
- LDC 2 para redes MT distribución sin condensadores
- LDC 3 si hay condensadores, cables largos o maniobras frecuentes

**7. Comprobar la clase de contaminación:**
- Para zonas industriales o costeras, la línea de fuga mínima es 31 mm/kV (clase C3, IEC 60815-1)
- Pararrayos poliméricos (SiR) o de porcelana según condiciones de instalación

## Ensayos de tipo y rutina según IEC 60099-4

Los ensayos de tipo verifican el comportamiento del pararrayos para cada familia de diseño:

- **Ensayo de descarga de línea:** 20 impulsos de corriente de maniobra (LDC 2: impulso 30/60 μs, 2 kA cresta) → temperatura de varistor debe volver a equilibrio térmico
- **Ensayo de TOV:** aplicación de Ur durante 10 s, seguido de descarga In → sin fallo dieléctrico
- **Ensayo de presión interna:** para pararrayos poliméricos, el fiador debe abrir antes de que la presión supere 4 bar
- **Ensayo de resistencia dieléctrica a impulso de rayo:** NBI del pararrayos ≥ NBI del equipo protegido · 1,25 (regla IEC 60071-2)

Los ensayos de rutina (100 % de unidades) incluyen: medida de Uc, medida de Vres a 0,01 kA y 1 kA, y ensayo de hermeticidad para unidades encapsuladas.

## Conclusión

Seleccionar un pararrayos ZnO en MT exige ir más allá del simple catálogo de Ur: hay que calcular Uc en función del tratamiento del neutro, verificar la curva TOV-tiempo con la duración real de la falta, contrastar Up con el NBI del equipo teniendo en cuenta la distancia eléctrica, y elegir la clase LDC adecuada a la energía de maniobra del circuito. IEC 60099-4 fija los ensayos que garantizan que el dispositivo cumple estas especificaciones; IEC 60099-5 da la guía de aplicación para calcularlas. En España, las redes de distribución de Media Tensión operan habitualmente con neutro aislado o compensado Petersen, lo que impone el factor de tierra más desfavorable (k₁ = 1,73) y obliga a subir Ur respecto a redes con neutro sólidamente puesto a tierra.
