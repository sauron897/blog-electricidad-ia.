---
title: "Protección motores IE3 BT: guardamotores e IEC 60947-4-1"
description: "Selección de guardamotores para motores IE3 en BT: corriente de arranque k=7,7, clases de disparo 10/20/30, coordinación Tipo 2 e ITC-BT-47 del REBT. Con valores IEC reales."
pubDate: 2026-10-14
keywords: ["guardamotor motor IE3 coordinación IEC 60947", "corriente arranque motor IE3 clase disparo", "coordinación tipo 2 IEC 60947-4-1", "protección motor asíncrono ITC-BT-47", "MPCB motor protection circuit breaker"]
author: "Editor"
---

## Corriente de arranque en motores IE3: k = 7,7 y sus consecuencias sobre la protección

El factor multiplicador de la corriente de arranque *k* (relación Iₐ/Iₙ) es mayor en motores de alta eficiencia que en IE1. Los motores IE3 (*Premium Efficiency*), al tener menor resistencia del rotor para reducir las pérdidas en el cobre, presentan un par de cortocircuito más elevado y, como consecuencia, una corriente de arranque también mayor. La base de datos GElectrical — que implementa directamente los parámetros de la serie IEC 60034 — confirma estos valores:

| Potencia | η IE1 (%) | η IE3 (%) | k IE1 | k IE3 | Iₙ IE3 a 400 V (A) | Iₐ IE3 DOL (A) |
|----------|-----------|-----------|-------|-------|---------------------|----------------|
| 11 kW    | 87,6      | 91,2      | 6,5   | 7,7   | 19,4                | 149            |
| 22 kW    | 89,9      | 92,7      | 6,5   | 7,7   | 38,1                | 293            |
| 37 kW    | 91,2      | 93,7      | 6,5   | 7,7   | 63,4                | 488            |
| 75 kW    | 92,7      | 94,7      | 6,5   | 7,7   | 127,1               | 979            |
| 110 kW   | 93,3      | 95,2      | 6,5   | 7,7   | 185,5               | 1.428          |

*(Iₙ calculada como P / (√3 × 400 V × η × cos φ), con cos φ = 0,9. Fuente: GElectrical/IEC 60034)*

La diferencia entre IE1 e IE3 no es marginal: para 22 kW, Iₐ pasa de 247 A (IE1, k=6,5) a 293 A (IE3, k=7,7), un aumento del **18,6 %**. Esto puede activar la protección magnética de un MCB sobredimensionado para el motor IE1 si no se revisa.

**Implicación directa**: sustituir un motor IE1 por IE3 sin revisar el cuadro de mando y protección es un error habitual en obra. El IEC 60947-4-1 exige que la protección de cortocircuito de la rama del motor no dispare durante el arranque normal. Si el umbral magnético del MCB/guardamotor es inferior a Iₐ del nuevo motor, habrá disparos instantáneos en cada arranque.

---

## Clases de disparo térmico según IEC 60947-4-1

El relé de sobrecarga — tanto el relé térmico independiente como la función de sobrecarga integrada en el guardamotor — se clasifica por su tiempo máximo de disparo a 7,2 × Ir en estado frío. IEC 60947-4-1 define cuatro clases:

| Clase | Tiempo de disparo a 7,2 × Ir (frío) | Condición de no disparo       | Aplicación típica                     |
|-------|--------------------------------------|-------------------------------|---------------------------------------|
| 10 A  | 2 – 10 s                             | 1,05 × Ir en caliente         | Arranques muy cortos: centrifugadoras, turbobombas |
| 10    | 4 – 10 s                             | 1,05 × Ir en caliente         | Estándar: bombas, ventiladores, compresores |
| 20    | 6 – 20 s                             | 1,05 × Ir en caliente         | Arranque con carga elevada: trituradoras, agitadores |
| 30    | 9 – 30 s                             | 1,05 × Ir en caliente         | Arranques muy prolongados: molinos, prensas de inercia |

La lógica de selección es directa: la clase debe absorber el tiempo real de arranque del motor sin disparar, al mismo tiempo que protege eficazmente contra sobrecargas en régimen. Un motor de 22 kW accionando una bomba centrífuga con tiempo de aceleración de 6 segundos entra perfectamente en clase 10. Un compresor de tornillo con aceleración de 14 segundos requiere clase 20.

**Error frecuente**: usar clase 10 A en todos los motores para obtener un disparo más rápido frente a sobrecargas. La clase 10 A solo es apropiada cuando el tiempo de arranque es inferior a 2 s. Para la mayoría de motores industriales en DOL, la clase 10 es el punto de partida correcto.

El ajuste del relé debe realizarse siempre en Ir = Iₙ nominal de la placa del motor, nunca en la corriente nominal del cable ni en el calibre del contactor.

---

## Guardamotor (MPCB) frente a contactor + relé térmico: cuándo usar cada solución

El guardamotor o *Motor Protective Circuit Breaker* (MPCB) integra en un solo bloque la función de seccionamiento, la protección magnética contra cortocircuito y la protección térmica contra sobrecarga. La alternativa clásica combina un MCB o fusibles (protección de cortocircuito), un contactor (maniobra) y un relé térmico (protección de sobrecarga) como dispositivos independientes.

| Criterio                          | Guardamotor (MPCB)                     | Contactor + Relé térmico              |
|-----------------------------------|----------------------------------------|---------------------------------------|
| Espacio en cuadro                 | Menor (1 dispositivo de maniobra)      | Mayor (3 dispositivos)                |
| Coste de adquisición              | Moderado (economía de escala)          | Menor para potencias pequeñas         |
| Poder de corte (Icu)              | Típico 50-100 kA en 400 V              | Depende del MCB/fusible escogido      |
| Clase de disparo disponible       | Normalmente clase 10                   | 10, 10A, 20, 30 según modelo          |
| Coordinación Tipo 2 certificada   | Disponible en catálogo del fabricante  | Disponible según tabla de coordinación|
| Rango de potencia habitual        | Hasta 55-75 kW (limitado por calibre)  | Sin límite práctico                   |
| Selectividad aguas arriba         | Más difícil (ajuste magnético fijo)    | Mayor flexibilidad                    |
| Maniobra y apertura visible       | Sí (seccionador integrado)             | Solo si el MCB lo permite             |

Para motores hasta 37-55 kW en instalaciones industriales con arranque directo, el guardamotor combinado con contactor ofrece la solución más compacta y normalmente suficiente. Para motores de mayor potencia, arranques prolongados (clases 20-30) o cuando se requiere una selectividad fina con el interruptor general del cuadro, la solución contactor + relé electrónico de sobrecarga es la práctica habitual.

---

## Coordinación Tipo 1 y Tipo 2: la clave para instalaciones con procesos continuos

La coordinación entre la protección de cortocircuito (MCB, MPCB o fusible) y el arrancador (contactor + relé) define el comportamiento del conjunto después de un cortocircuito. IEC 60947-4-1 establece dos categorías:

**Coordinación Tipo 1**: después de la actuación frente a un cortocircuito, el arrancador puede quedar inutilizable sin suponer riesgo para las personas. La reposición del servicio puede requerir la sustitución de contactos del contactor o del relé de sobrecarga.

**Coordinación Tipo 2**: después de la actuación frente a un cortocircuito, el contactor y el relé de sobrecarga deben poder reutilizarse sin sustitución de componentes. Se admite únicamente la soldadura leve de contactos del contactor siempre que sean separables manualmente.

La coordinación Tipo 2 es la exigible en instalaciones industriales con procesos continuos. La razón es operacional: una sustitución de componentes después de cada cortocircuito implica tiempo de parada no planificado, stock de repuestos y mano de obra técnica. En una instalación con 20-30 motores, un fallo de coordinación Tipo 1 en un evento de cortocircuito puede significar varias horas de parada de producción.

**Punto crítico en obra**: la certificación de Tipo 2 **no es genérica por fabricante**, sino específica por combinación de componentes. Una combinación MCB modelo X + contactor modelo Y + relé modelo Z a una Icc determinada solo cumple Tipo 2 si está explícitamente tabulada y ensayada según IEC 60947-4-1. Sustituir el MCB por otro modelo, incluso del mismo fabricante, puede invalidar la coordinación certificada.

La corriente de cortocircuito prospectiva del punto de instalación (Icc en bornes del arrancador) es el parámetro de entrada de las tablas. Debe calcularse aplicando el método de impedancias según IEC 60909-0 o verificarse mediante medida directa con un comprobador de bucle/Icc.

---

## ITC-BT-47 del REBT: obligaciones reglamentarias en España

La Instrucción Técnica Complementaria ITC-BT-47 del Reglamento Electrotécnico de Baja Tensión establece los requisitos mínimos para la instalación de motores en España. Los puntos técnicamente relevantes para la selección de protecciones:

- **Motores ≥ 0,75 kW**: deben disponer de protección propia e individual frente a sobrecargas y cortocircuitos, con apertura simultánea de todas las fases.
- **Calibre máximo de la protección**: para un circuito exclusivo de un motor, el dispositivo de protección contra sobrecargas debe ajustarse a un valor ≤ 1,25 × Iₙ del motor (referenciado a los datos de placa).
- **No actuación en arranque**: el dispositivo debe tolerar la corriente de arranque sin disparar en condiciones de funcionamiento normal, lo que justifica reglamentariamente el uso de curvas de disparo D en MCB o regulación magnética ajustable en guardamotores.
- **Protección de cortocircuito**: el calibre del interruptor de protección de cortocircuito no será superior a la corriente máxima admisible de cortocircuito del cable de la rama del motor (referencia: ITC-BT-19 para el cálculo de la sección).

Para motores IE3 con k = 7,7, el requisito de no actuación en arranque es más exigente. Un MCB estándar curva C calibre 40 A tiene umbral magnético en el rango 5-10 × 40 = 200-400 A. Para un motor IE3 de 22 kW (Iₐ = 293 A), el límite inferior de la curva C puede provocar disparos si el MCB tiene una tolerancia estrecha. La solución es usar curva D (umbral 10-20 × In), que garantiza que el umbral mínimo de disparo magnético (10 × 40 = 400 A) sea siempre superior a Iₐ = 293 A, con margen del 37 %.

---

## Criterios de selección aplicables en obra: procedimiento en 6 pasos

1. **Leer la placa del motor**: anotar Pₙ, Uₙ, Iₙ, clase IE, factor de servicio, clase de aislamiento.

2. **Calcular Iₐ = k × Iₙ**: para motores IE3 usar k = 7,7 (series de 2 a 4 polos, potencias ≥ 2,2 kW según IEC 60034-12). Para IE1 usar k = 6,5; para IE2 usar k = 7,0.

3. **Estimar el tiempo de arranque**: depende de la carga accionada. Referencia orientativa: bombas centrífugas 3-7 s, compresores de tornillo 8-12 s, ventiladores industriales 8-15 s, trituradoras y molinos > 15 s.

4. **Seleccionar la clase de disparo**: clase 10 para arranques hasta 10 s; clase 20 para 10-20 s; clase 30 para > 20 s.

5. **Dimensionar la protección magnética (MCB o umbral del MPCB)**: verificar que el umbral mínimo de disparo instantáneo sea estrictamente mayor que Iₐ. Para MCB: usar calibre con curva D o elegir calibre curva C tal que 10 × In_MCB > Iₐ. Para guardamotor con regulación magnética: ajustar el umbral al menos al 115 % de Iₐ.

6. **Verificar la coordinación Tipo 2**: consultar la tabla de coordinación del fabricante para la Icc del punto de instalación. Si la corriente de cortocircuito no está calculada, medirla con instrumento de bucle/Icc antes de poner en servicio. Solo las combinaciones explícitamente ensayadas y publicadas en la tabla del fabricante son válidas para declarar coordinación Tipo 2.

---

## Conclusión

La sustitución de motores IE1 por IE3 — obligatoria en nuevas instalaciones desde 2023 según el Reglamento (UE) 2019/1781 para la mayoría de potencias — no es transparente para la protección eléctrica. El aumento del factor k de 6,5 a 7,7 eleva la corriente de arranque un 18 % y puede activar la protección magnética de guardamotores o MCBs dimensionados para IE1. En toda sustitución de motor, hay que recalcular Iₐ = 7,7 × Iₙ, verificar los umbrales de disparo magnético del cuadro existente y revisar las tablas de coordinación Tipo 2. La normativa IEC 60947-4-1 y la ITC-BT-47 del REBT no son documentos de referencia pasiva: son los criterios técnicos que diferencian una instalación robusta de un motor que dispara en cada arranque.
