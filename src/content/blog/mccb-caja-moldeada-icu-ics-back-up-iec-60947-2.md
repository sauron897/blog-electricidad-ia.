---
title: "MCCB en instalaciones BT: Icu, Ics y coordinación Back-up según IEC 60947-2"
description: "Parámetros Icu e Ics de MCCB según IEC 60947-2: diferencias, porcentajes normalizados, categorías A y B, Icw, coordinación Back-up y criterios de selección en instalaciones industriales BT."
pubDate: 2026-10-10
keywords: ["MCCB interruptor caja moldeada IEC 60947-2", "Icu Ics poder de corte MCCB", "coordinacion back-up interruptores BT", "categorias utilizacion A B IEC 60947-2", "selectividad amperimetrica MCCB"]
author: "Editor"
---

Los interruptores automáticos de caja moldeada (MCCB) cubren el rango de calibres entre los MCB domésticos (hasta 125 A) y los interruptores abiertos de gran formato (ACB, desde ~800 A). En instalaciones industriales de BT, son el elemento de protección por excelencia en cuadros de distribución, alimentadores de motores de gran potencia, salidas de transformador y protecciones de cabecera de embarrado secundario.

La norma que los rige es la **IEC 60947-2** (*Low-voltage switchgear and controlgear – Part 2: Circuit-breakers*), adoptada en España como **UNE-EN IEC 60947-2**. Define los ensayos tipo, los parámetros de cortocircuito y las condiciones de coordinación que debe verificar todo dispositivo que se declare conforme.

## Parámetros de cortocircuito según IEC 60947-2: Icu, Ics e Icw

La norma distingue tres magnitudes relacionadas con el comportamiento ante cortocircuito:

**Icu — Capacidad de corte última asignada** (*Rated ultimate short-circuit breaking capacity*)
Es el valor máximo de corriente de cortocircuito que el dispositivo es capaz de interrumpir sin quedar inútil, pero al precio de verse degradado: tras el ensayo Icu, la norma acepta que el interruptor quede fuera de servicio permanentemente. El valor se expresa en kA (eficaz simétrico) a la tensión asignada y el factor de potencia definido en la norma (cos φ = 0,1 para I > 20 kA).

**Ics — Capacidad de corte de servicio asignada** (*Rated service short-circuit breaking capacity*)
Es la corriente máxima que el dispositivo puede interrumpir y seguir siendo operativo. Se expresa como porcentaje de Icu y puede tomar los valores normalizados del 25 %, 50 %, 75 % o 100 %. Después del ensayo Ics el interruptor debe ser capaz de transportar su corriente nominal y de operar correctamente. En aplicaciones industriales críticas se especifica Ics = 100 % Icu; en aplicaciones estándar con coordinación back-up diseñada, puede aceptarse Ics = 50 % o 75 % Icu.

**Icw — Corriente de corta duración admisible** (*Rated short-time withstand current*)
Parámetro exclusivo de los dispositivos de **categoría B**. Define la corriente que el interruptor puede soportar durante un tiempo asignado (0,05 s, 0,1 s, 0,25 s, 0,5 s o 1 s) sin disparar ni deteriorarse. Permite implementar selectividad cronométrica: el interruptor aguas arriba aguanta el cortocircuito mientras el aguas abajo lo abre.

| Parámetro | Definición | Tras el ensayo | Aplicable a |
|---|---|---|---|
| Icu | Corte último | Interruptor fuera de servicio | Cat. A y B |
| Ics | Corte de servicio | Interruptor operativo | Cat. A y B |
| Icw | Soporte corta duración | Sin disparo, operativo | Solo Cat. B |

## Categorías de utilización A y B según IEC 60947-2

La norma distingue dos categorías según la capacidad del interruptor para introducir retardo intencionado en la actuación ante cortocircuito:

**Categoría A** — Sin retardo intencional. El elemento de disparo instantáneo actúa tan pronto como la corriente supera el umbral de corte magnético (típicamente 5–10 × In para dispositivos electromecánicos, configurable en los electrónicos). No existe declaración de Icw. La mayoría de MCCB del mercado son categoría A.

**Categoría B** — Con retardo intencional y Icw declarado. El interruptor puede retardar su actuación para permitir que el dispositivo situado aguas abajo abra el circuito. Esto requiere que el bastidor del interruptor aguante el esfuerzo electrodinámico y térmico del cortocircuito durante el tiempo de retardo. Los ACB y los MCCB de alta gama con unidades de disparo electrónicas avanzadas pueden ser categoría B.

En una instalación típica con cuadro general (CGBT) y cuadros secundarios (CS):
- **CGBT** → MCCB o ACB de Categoría B con Icw ≥ Icc en ese punto, actúa tras retardo t
- **CS** → MCCB de Categoría A, actúa instantáneamente ante falta en su zona

## Calibres normalizados y niveles de Icu (GElectrical / IEC 60947-2)

Los calibres nominales IEC para MCCB son: 16, 20, 25, 32, 40, 50, 63, 80, 100, 125, 160, 200, 250, 320, 400, 500, 630, 800, 1000, 1250, 1600 A.

Los niveles de Icu más habituales en el mercado europeo, extraídos de la base de datos GElectrical (implementa IEC 60947-2 directamente):

| Familia / Bastidor | In máx (A) | Icu típico (kA) | Cat. |
|---|---|---|---|
| Legrand DPX3 160 | 160 | 16 | A |
| Schneider Compact NSXm | 160 | 16 | A |
| Legrand DPX3 250 / Schneider NSX | 250 | 25 | A |
| L&T DSINE DN2 / Legrand DPX3 1600 | 320–1600 | 36 | A/B |
| ACB industrial (referencia) | 630–6300 | 65–150 | B |

El Icu de 16 kA es el mínimo razonable en instalaciones industriales BT en España. La corriente de cortocircuito trifásico en el secundario de un transformador de 400 kVA, 20/0,4 kV, con ucc = 4 % es:

> Icc_3f = Sn / (√3 × Un × ucc) = 400 000 / (1,732 × 400 × 0,04) ≈ **14,4 kA**

Para transformadores de 630 kVA o superior, o en puntos con baja impedancia de red (línea corta desde transformador), el Icc puede superar los 20 kA, lo que exige Icu ≥ 25 kA.

## Coordinación Back-up: fundamento y requisitos normativos

La coordinación back-up (también denominada *protección de respaldo* o *asociación* en documentación de fabricante) permite instalar un MCCB con un Icu inferior a la corriente de cortocircuito en su punto de instalación, siempre que exista un interruptor aguas arriba con Icu suficiente que limite la energía de falta.

**Fundamento físico:** El interruptor aguas arriba, ante una corriente de falta elevada, inicia su apertura antes de que la corriente alcance el pico de cresta. Al generar arco eléctrico en su cámara de extinción, limita la corriente de cresta que llega al circuito de carga (*peak let-through current*). Ese valor limitado puede ser inferior al Icu del MCCB aguas abajo, aunque la corriente prospectiva en ese punto supere dicho Icu.

**Condición de validez:** La coordinación back-up debe estar verificada y publicada por el fabricante para el par específico de interruptores y el nivel de Icc correspondiente. No puede calcularse analíticamente solo; requiere los ensayos de tipo de la IEC 60947-2. Las tablas de coordinación indican el nivel máximo de Icc prospectivo en kA para el que la asociación está homologada.

**Ejemplo práctico:** En un cuadro con Icc = 30 kA en cabecera:
- Interruptor general: MCCB 250 A, Icu = 36 kA (tabla back-up verificada con el siguiente)
- Alimentadores: MCCB 100 A, Icu = 16 kA — válido para Icc presunto ≤ 30 kA si la tabla de coordinación del fabricante lo certifica para ese par específico

Sin esa tabla publicada, la instalación no puede declararse conforme a IEC 60947-2, y el responsable técnico asume la responsabilidad civil ante cualquier incidente.

## Criterios de selección de MCCB en obra

La secuencia de selección correcta en una instalación nueva:

1. **Calcular Icc máximo** en cada punto según IEC 60909 (método de impedancias). No usar estimaciones de catálogo del transformador sin verificar la impedancia real de la red de alimentación.
2. **Determinar In** a partir de la corriente de carga máxima, respetando ITC-BT-22 (factores de utilización y simultaneidad) y la protección del conductor aguas abajo.
3. **Elegir Icu ≥ Icc** en ese punto, o bien definir una coordinación back-up verificada con el interruptor aguas arriba.
4. **Verificar Ics** según criticidad del proceso: Ics = 100 % Icu para instalaciones hospitalarias, centros de datos, salas de control; Ics = 50 % en aplicaciones no críticas con back-up diseñado.
5. **Categoría B** solo cuando se requiere selectividad cronométrica y el interruptor de cabecera tiene Icw declarado ≥ Icc en su punto.
6. **Curva de disparo electrónica (LSI o LSIG):** ajustar umbral largo retardo Ir entre 0,8 y 1,0 × In; umbral corto retardo Isd por encima de la corriente de arranque o golpe de carga máximo esperado.

| Condición | Criterio de selección |
|---|---|
| Icc ≤ Icu | Uso directo sin back-up |
| Icc > Icu | Back-up con interruptor aguas arriba (verificar tabla del fabricante) |
| Selectividad cronométrica requerida | Categoría B + Icw ≥ Icc declarado |
| Instalación crítica (hospital, CPD) | Ics = 100 % Icu |
| Proceso industrial estándar | Ics = 50–75 % Icu aceptable |

## Conclusión

Especificar un MCCB sólo por su calibre nominal ignorando el Icu es uno de los errores más frecuentes en el diseño de cuadros industriales BT. Un interruptor de 100 A con Icu = 16 kA en un cuadro alimentado por un transformador de 630 kVA —donde el Icc real puede alcanzar los 21 kA— no cumple IEC 60947-2 salvo que la coordinación back-up con el interruptor de cabecera esté correctamente verificada y documentada. El protocolo mínimo es: calcular Icc según IEC 60909 → elegir Icu o definir back-up → verificar Ics según criticidad → documentar la asociación con la tabla del fabricante. Ese proceso protege la instalación y al proyectista ante cualquier incidente.
