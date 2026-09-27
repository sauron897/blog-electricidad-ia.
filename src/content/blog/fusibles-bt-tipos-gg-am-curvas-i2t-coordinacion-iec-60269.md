---
title: "Fusibles BT: tipos gG y aM, curvas I²t y coordinación IEC 60269"
description: "Guía técnica de fusibles gG y aM en BT: calibres normalizados según IEC 60269, curvas I²t, back-up con magnetotérmicos e ITC-BT-22. Para técnicos e ingenieros eléctricos."
pubDate: 2026-09-27
keywords: ["fusibles gG aM IEC 60269", "fusibles BT seleccion", "curvas I2t fusible", "coordinacion fusible magnetotermico", "fusibles proteccion motor aM"]
author: "Editor"
---

Los fusibles siguen siendo el elemento de protección más empleado en cuadros de distribución industrial y secundarios de transformador, especialmente en niveles de cortocircuito elevados donde un MCB no ofrece el poder de corte necesario. La norma **IEC 60269-1** (UNE-EN 60269-1 en España) define los requisitos generales; las partes -2, -3 y -4 desarrollan las especificaciones por aplicación. El REBT los regula específicamente en la **ITC-BT-22**, que exige que todo fusible instalado tenga un poder de corte superior a la corriente de cortocircuito presunta en el punto de instalación.

Este artículo aborda la clasificación, las curvas de actuación y los criterios de coordinación que necesitas para seleccionar fusibles correctamente en obra.

---

## Clasificación de fusibles según IEC 60269: categorías y designaciones

IEC 60269-1 define dos parámetros que forman la designación de todo fusible:

- **Categoría de utilización** (letra minúscula): rango de corrientes que el fusible puede interrumpir.
- **Clase de interrupción** (letra mayúscula): clase de uso prevista.

| Designación | Rango de interrupción | Aplicación principal |
|---|---|---|
| **gG** | Corrientes desde sobrecargas hasta Icc máxima | Distribución general, protección de cables |
| **gM** | Igual que gG, pero con calibres duales (In/Im) | Protección de motores con un solo fusible |
| **gR / gS** | Solo interrumpe altas corrientes (Icc) | Protección de semiconductores (rectificadores, inversores) |
| **aM** | Solo interrumpe desde 4·In hacia arriba | Protección de motors (back-up, no protege sobrecarga) |
| **gN** | Variante norteamericana (NEC 240) | No aplica en instalaciones bajo REBT |

La diferencia crítica entre **gG** y **aM** es el rango inferior de interrupción. Un fusible **aM no puede proteger contra sobrecarga**: su curva comienza a actuar a partir de ~4·In (para 10 s) y su zona de no-fusión garantizada llega hasta 2,1·In. Para protección de sobrecargas en motores debes utilizar el relé de sobrecarga térmico (o electrónico) separado y coordinado con el fusible aM según **IEC 60947-4-1 Tipo 2**.

---

## Calibres normalizados gG y capacidad de corte

La serie de valores preferidos definida en IEC 60269-2 (distribución en BT) establece los calibres normalizados. Los datos siguientes corresponden a la base de datos IEC implementada en GElectrical:

**Fusibles gG — HF (hasta 80 kA de poder de corte):**

| In (A) | Isc máx. (kA) | Formato |
|---|---|---|
| 2 | 80 | HF |
| 4 | 80 | HF |
| 6 | 80 | HF |
| 10 | 80 | HF |
| 16 | 80 | HF |
| 20 | 80 | HF |
| 25 | 80 | HF |
| 32 | 80 | HF |
| 40 | 80 | HF |
| 50 | 80 | HF |
| 63 | 80 | HF |

**Fusibles gG — DIN-HN (hasta 100 kA de poder de corte):**

| In (A) | Isc máx. (kA) | Formato |
|---|---|---|
| 63 | 100 | DIN-HN |
| 80 | 100 | DIN-HN |
| 100 | 100 | DIN-HN |
| 125 | 100 | DIN-HN |
| 160 | 100 | DIN-HN |
| 200 | 100 | DIN-HN |
| 250 | 100 | DIN-HN |
| 315 | 100 | DIN-HN |
| 400 | 100 | DIN-HN |

El poder de corte de 100 kA es significativamente superior al de cualquier MCB (típico 10 kA para calibres domésticos, hasta 50 kA en MCCB industriales), razón por la que los fusibles HRC (High Rupturing Capacity) se emplean obligatoriamente en la acometida de cuadros secundarios alimentados directamente desde el secundario de un transformador de centro de distribución, donde Icc puede superar fácilmente los 30–50 kA.

---

## Curvas I²t: energía de fusión, prerrupción y posrupción

El parámetro más importante para la coordinación de protecciones en cascada es la **energía de paso I²t** (A²·s). La curva de un fusible HRC tiene dos zonas:

**Zona de prerrupción (prefusión):**
El conductor interno comienza a fundirse hasta que se produce el arco. La energía I²t de prerrupción determina el daño térmico acumulado en el equipo protegido antes de que el fusible actúe.

**Zona de posrupción (arco):**
Desde el inicio del arco hasta la extinción. El fusible limita la corriente al valor de cresta del arco (corriente de corte prospectiva limitada).

La suma de ambas define la **I²t total** (energía de paso o "let-through energy"). Para que un fusible upstream (corriente mayor) proteja en back-up a uno downstream (corriente menor), debe cumplirse:

```
I²t_total (fusible upstream, menor calibre) < I²t_prerrupción (fusible downstream, mayor calibre)
```

En la práctica, esto se verifica con las curvas del fabricante. Para fusibles gG de la misma serie:

- Un fusible de 100 A gG tiene I²t total ≈ 10⁵–10⁶ A²·s a Icc nominal
- Un fusible de 63 A gG en el mismo punto tiene I²t prerrupción ≈ 3×10⁴–5×10⁴ A²·s

La coordinación en cascada es posible cuando hay una diferencia de al menos dos escalones de calibre entre fusibles de la misma serie gG.

---

## Coordinación fusible–magnetotérmico (protección back-up)

La **protección back-up** consiste en instalar un fusible aguas arriba de un interruptor magnetotérmico cuyo poder de corte nominal (Ics o Icu según IEC 60898-1 / IEC 60947-2) sea inferior a la Icc presunta en el punto de instalación. El fusible asume la interrupción de corrientes que el MCB no puede cortar de forma segura.

Condición de validez (IEC 60947-2 Anexo B):
1. La I²t total del fusible a la corriente de no-disparo del MCB debe ser ≤ a la I²t que puede soportar el MCB (datos del fabricante).
2. El fusible debe actuar antes de que la corriente alcance el valor máximo que el MCB puede limitar sin daño.

**Ejemplo numérico:** En un cuadro secundario con Icc presunta de 25 kA en el embarrado:
- MCB Schneider iC60a, 25 A, Curva C, Icu = 10 kA: **no puede instalarse sin back-up**
- Fusible gG 63 A, Isc = 80 kA: actúa antes de que el MCB vea la corriente completa
- Con esta combinación, el conjunto tiene poder de corte efectivo de hasta 80 kA

La combinación fusible + MCB debe estar verificada y documentada por el fabricante (ensayo de conformidad según IEC 60947-2). No se puede asumir compatibilidad entre marcas sin ese certificado.

---

## Criterios de selección en obra

### Selección de tipo (gG vs aM)

- **gG**: protección de cables y distribución general. Es el tipo por defecto en cualquier circuito de distribución sin arranque de motor.
- **aM**: solo para protección de motores en back-up con relé de sobrecarga. El relé térmico protege la sobrecarga; el fusible aM protege el cortocircuito. Obligatorio cuando la corriente de arranque (Ia = 5–7·In) haría saltar un gG antes de que el motor alcance la velocidad nominal.

### Selección de calibre (corriente nominal)

Para cables (protección gG):
- In_fusible ≤ Iz_cable (intensidad admisible según IEC 60364-5-52 / ITC-BT-07)
- In_fusible ≥ Ib (corriente de carga máxima prevista)
- ITC-BT-22 del REBT establece que: **Ib ≤ In_fusible ≤ Iz** y **If ≤ 1,6·Iz**, donde If es la corriente convencional de fusión.

Para motores (fusible aM + relé de sobrecarga):
- In_fusible_aM ≈ 1,6·In_motor hasta 2,0·In_motor para arranque directo
- Con arrancador estrella-triángulo: In_fusible_aM ≈ In_motor (la corriente de arranque pasa por los devanados en delta a 1/3 del valor directo)
- Verificar que en t=10 s la corriente de arranque no fusione el aM (usar la curva del fabricante)

### Selección de poder de corte

- Calcular Icc presunta en el punto de instalación (método de impedancias según IEC 60909)
- In_fusible debe tener Isc > Icc_presunta
- Margen de seguridad recomendado: Isc_fusible ≥ 1,25·Icc_presunta

### Resumen de criterio de decisión

| Condición | Tipo fusible | Calibre |
|---|---|---|
| Distribución general, cables | gG | Según Iz del cable |
| Motor BT con arranque directo | aM | 1,6–2,0 · In_motor |
| Motor con arranque Y/D | aM | ≈ In_motor |
| Semiconductores / inversores | gR o gS | Según ficha técnica del equipo |
| Back-up para MCB con Icu insuficiente | gG HRC | ≥ 2 escalones sobre MCB |

---

## ITC-BT-22 del REBT: requisitos para fusibles

La **ITC-BT-22** ("Protección contra sobreintensidades") del Reglamento Electrotécnico para Baja Tensión establece:

- **Art. 2.1**: Todo circuito debe estar protegido contra sobrecarga y cortocircuito. El fusible puede cumplir ambas funciones (gG) o solo cortocircuito (aM) si hay otro dispositivo para sobrecarga.
- **Art. 2.2**: La corriente convencional de fusión If_2 (corriente a la que el fusible funde en el tiempo convencional) no debe superar 1,6·In del fusible para fusibles gG según IEC 60269.
- **Art. 4**: El poder de corte mínimo del fusible es la corriente de cortocircuito presunta en el punto de instalación. En derivaciones desde cuadros con transformador propio, la Icc puede ser de varios kiloamperios → obligatorio usar fusibles HRC.
- **Art. 4.2**: En instalaciones de hasta 16 A en viviendas, se permiten fusibles tipo D (cilíndricos 10×38) con poder de corte de solo 100 A, únicamente si la Icc en ese punto es inferior.

Para calcular la Icc presunta en cualquier punto de la instalación y verificar el poder de corte necesario, aplica el método de impedancias definido en **IEC 60909-0** (desarrollado en el post anterior de esta serie sobre cortocircuito en BT).

---

## Conclusión

La selección correcta de fusibles en BT exige tres verificaciones simultáneas: el tipo de categoría (gG para distribución, aM para motores), el calibre que satisfaga simultáneamente Ib ≤ In ≤ Iz y la restricción de ITC-BT-22 sobre la corriente convencional de fusión, y el poder de corte frente a la Icc presunta del punto de instalación. Los fusibles gG de formato DIN-HN con poder de corte de 100 kA son la solución estándar para cuadros secundarios de distribución industrial alimentados desde transformador. La coordinación en cascada con MCB de menor poder de corte requiere documentación de conformidad por parte del fabricante según IEC 60947-2, y no puede asumirse sin ese ensayo. El parámetro I²t es la clave para verificar la selectividad energética en cascadas de dos o más niveles de fusibles.
