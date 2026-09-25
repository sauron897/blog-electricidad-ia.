---
title: "Relés de sobrecarga de motor: clases IEC 60947-4-1 y coordinación"
description: "Clases de disparo CLASS 5 a 40, coordinación tipo 1 y tipo 2 con fusibles y MCCB según IEC 60947-4-1. Criterios de selección para instalaciones industriales BT."
pubDate: 2026-09-25
keywords: ["relé sobrecarga motor IEC 60947-4-1", "coordinación tipo 2", "clases de disparo motor", "relé térmico sobrecarga", "protección motor BT"]
author: "Editor"
---

## Principio de funcionamiento y norma de referencia

El relé de sobrecarga (overload relay, OLR) protege el bobinado del motor frente a elevaciones térmicas originadas por sobrecargas persistentes, bloqueo de rotor o desequilibrio de fases. Su lógica es una integral térmica: acumula I²·t por encima del umbral de ajuste y dispara cuando el modelo de temperatura inferida supera el límite del aislamiento.

A diferencia del magnetotérmico, que cubre el rango de cortocircuito (> 8–10 × In en curva C), el relé de sobrecarga actúa entre 1,05 × In y 6–8 × In, con tiempos que van de segundos a minutos. No protege contra cortocircuitos: ese papel corresponde al DPCC (MCB, MCCB o fusible gG/aM).

La norma marco es **IEC 60947-4-1** (Aparamenta de baja tensión – Contactores y arrancadores de motores – Contactores electromecánicos y arrancadores de motores), aplicable hasta 1000 V AC / 1500 V DC. Para relés de estado sólido se añade **IEC 60947-4-2**.

En España, la **ITC-BT-47 del REBT** exige protección contra sobrecarga y fallo de fase en motores trifásicos > 0,75 kW.

---

## Clases de disparo según IEC 60947-4-1

La clase de disparo define el tiempo máximo de disparo del relé en **arranque en caliente a 7,2 × In** (múltiplo del ajuste I_r). El apartado 8.2.1.1 de IEC 60947-4-1 tabula los valores siguientes:

| Clase | t_max disparo a 7,2 × In (caliente) | t_min no disparo a 7,2 × In (frío) | Aplicación típica |
|-------|-------------------------------------|-------------------------------------|-------------------|
| 5     | 5 s                                 | 2 s                                 | Bombas de arranque rápido, servos |
| 10A   | 10 s                                | 4 s                                 | Motores con Ia ≤ 4 × In, t_arr ≤ 4 s |
| 10    | 10 s                                | 4 s                                 | Motores estándar, DOL, Ia ≤ 6 × In |
| 20    | 20 s                                | 6 s                                 | Arranques difíciles: molinos, trituradoras |
| 30    | 30 s                                | 9 s                                 | Arranques muy pesados: centrífugas, grandes ventiladores |
| 40    | 40 s                                | 12 s                                | Arranques extremos, alta inercia |

**Distinción clase 10A / clase 10**: ambas tienen el mismo límite a 7,2 × In, pero difieren en la tolerancia a sobrecargas moderadas. A 2 × In, la clase 10A no dispara en 2 min y la clase 10 no dispara en 4 min. La clase 10A es más restrictiva frente a sobrecargas de baja magnitud sostenidas, apropiada cuando el bobinado no admite temperatura elevada prolongada.

**Umbral de no disparo en sobrecarga continua**: según IEC 60947-4-1, el relé ajustado a I_r no debe disparar a 1,05 × In en una hora (para temperatura ambiente 40 °C), pero sí dispara a 1,20 × In en la hora siguiente. Esto delimita el margen operativo admisible antes de la protección.

---

## Curva I-t: relé bimetálico vs. electrónico

El relé **bimetálico** implementa la integral térmica mediante la deflexión de una lámina bimetálica. La curva es aproximadamente inversa cuadrática:

- A **1,5 × In**: disparo en 5–15 min (sobrecarga leve prolongada)
- A **3 × In**: disparo en 30–120 s (bloqueo inicial o sobrecarga grave)
- A **6 × In**: disparo en 5–20 s (rotor bloqueado sostenido)
- A **7,2 × In**: según la clase (ver tabla)

La desventaja del bimetálico es la compensación de temperatura: si la temperatura ambiente supera 40 °C, el disparo se anticipa; si baja de –5 °C, se retarda. IEC 60947-4-1 exige compensación en el rango –5 °C a +40 °C.

El relé **electrónico** (estado sólido, IEC 60947-4-2) añade:

- **Memoria térmica**: acumula el calor residual entre arranques consecutivos, impidiendo rearranques inmediatos que acumulen energía térmica excesiva.
- **Detección de desequilibrio de fases**: disparo en < 5 s si el desequilibrio supera el 40 % (o antes si el fabricante lo especifica).
- **Protección contra fallo de fase**: disparo en < 1 s si una fase cae a 0 A — obligatoria según ITC-BT-47 para motores trifásicos > 0,75 kW.
- **Compensación de temperatura**: algoritmo de corrección continua, sin necesidad de ajuste por temperatura ambiente.

La selección entre bimetálico y electrónico depende de la criticidad del proceso y del coste tolerable. Para procesos continuos con motores > 11 kW, el electrónico se justifica por el ahorro en tiempo de diagnóstico y la memoria térmica.

---

## Coordinación tipo 1 y tipo 2 con el DPCC

La coordinación define el comportamiento del conjunto **contactor + relé de sobrecarga** tras un cortocircuito. El DPCC (fusible o MCCB) limita la energía dejada pasar (I²·t); la coordinación determina el estado del conjunto después del evento. IEC 60947-4-1, apartado 8.2.5, establece dos niveles:

### Tipo 1
El contactor y el relé pueden quedar dañados e inutilizables. Se admite que requieran inspección, reparación o sustitución antes de volver a poner en servicio. El DPCC sólo garantiza que no haya peligro para personas o instalación adyacente.

- **Ventaja**: menor coste del conjunto (fusibles gG convencionales, MCCB de menor capacidad de corte).
- **Inconveniente**: tiempo de parada indeterminado hasta inspección y eventual sustitución.
- **Uso recomendado**: instalaciones no críticas, activos reemplazables sin impacto en producción.

### Tipo 2
El contactor y el relé deben quedar **aptos para uso inmediato** tras el cortocircuito. Se permiten contactos soldados siempre que sean separables sin herramienta. El operario rearma el conjunto sin cambiar ningún componente.

- **Ventaja**: tiempo de rearranque < 5 min; esencial en procesos continuos o líneas de producción.
- **Inconveniente**: mayor coste del DPCC: fusibles **aM** (motor) con menor I²·t dejada pasar, o MCCB con función limitadora. Requiere tabla de coordinación del fabricante.
- **Uso recomendado**: industria de proceso continuo, agua, HVAC crítico.

### Parámetros de coordinación tipo 2: ejemplo práctico

Para un contactor de categoría AC-3 de 37 kW / 400 V (In_motor ≈ 72 A, corriente térmica del contactor Ith = 75 A), un fabricante típico especifica en su tabla IEC 60947-4-1 Anexo B:

| DPCC | Calibre máx. para tipo 2 | Corriente de cortocircuito máx. garantizada |
|------|--------------------------|---------------------------------------------|
| Fusible aM | 100 A | 50 kA |
| MCCB (Icc lim.) | 100 A — curva D | 36 kA |
| Fusible gG | No garantiza tipo 2 | — |

Si se usan fusibles gG en lugar de aM, la energía I²·t dejada pasar es mayor, y el contactor puede quedar con contactos soldados de forma permanente: sólo se garantiza tipo 1.

---

## Criterios de selección aplicados en obra

### 1. Corriente de ajuste I_r
Ajustar al valor nominal de placa del motor (In_placa). Para motores con factor de servicio SF = 1,15 (indicado en placa), se puede ajustar hasta 1,10 × In sin riesgo de disparo falso en sobrecarga admisible.

### 2. Clase de disparo según el arranque
- **Clase 10**: la mayoría de motores de jaula en DOL (bombas centrífugas, ventiladores de tiro inducido, compresores de tornillo de arranque cargado).
- **Clase 20**: arranque cargado con Ia > 6 × In o t_arranque 10–20 s (molinos, prensas, bandas transportadoras cargadas).
- **Clase 30**: centrifugadoras, grandes volantes de inercia, arranques contra presión hidráulica elevada.
- **Clase 10A**: motores de pequeña inercia y arranque rápido donde la protección térmica del aislamiento es prioritaria sobre la tolerancia a arranques largos.

### 3. Categoría de utilización del contactor asociado
- **AC-3** (arranque directo, rotor en jaula): la más habitual. Relé clase 10 como primera opción.
- **AC-4** (arranque por inversión, frenado de contracorriente): el relé debe ser clase 20 o superior, ya que el número de operaciones por hora eleva la temperatura del bobinado.

### 4. Coordinación tipo 1 o tipo 2
La decisión depende del tiempo de parada tolerable y el coste del conjunto protección. Documentar siempre la tabla de coordinación del fabricante en el proyecto eléctrico — exigido por IEC 60364-5-55 y aconsejable para la inspección reglamentaria.

### 5. Protección contra fallo de fase
Obligatoria según ITC-BT-47 en motores trifásicos > 0,75 kW. El relé bimetálico requiere módulo de fallo de fase separado; el electrónico la integra. Con un fallo de fase, el motor continúa girando con las dos fases restantes, la corriente sube un factor √3 ≈ 1,73 en las fases activas, y el desequilibrio térmico destruye el bobinado en minutos si no hay protección.

---

## Conclusión

La clase de disparo del relé de sobrecarga debe coincidir con las condiciones de arranque del motor: elegirla demasiado baja provoca disparos intempestivos en arranque; demasiado alta deja el bobinado sin protección ante sobrecargas moderadas sostenidas. La coordinación tipo 2 es la norma en instalaciones industriales continuas donde el tiempo de rearranque es crítico — siempre respaldada por las tablas de coordinación del fabricante según IEC 60947-4-1 Anexo B y con fusibles aM o MCCB limitador compatibles. Como siguiente paso en el diseño: verificar que el poder de corte del DPCC seleccionado supera la Icc en el punto de instalación, calculada según IEC 60909 a partir de la impedancia del transformador y del cable de acometida.
