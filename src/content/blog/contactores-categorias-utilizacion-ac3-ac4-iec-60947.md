---
title: "Contactores industriales: AC-3 vs AC-4 según IEC 60947-4-1"
description: "Categorías de utilización AC-3 y AC-4 en contactores industriales: diferencias técnicas, corrientes de maniobra, selección de calibre y coordinación tipo 2 según IEC 60947-4-1."
pubDate: 2026-09-28
keywords: ["contactor industrial categorias utilizacion AC-3 AC-4 IEC 60947", "seleccion contactor motor AC-3", "coordinacion tipo 2 contactor relé sobrecarga", "categoria utilizacion IEC 60947-4-1"]
author: "Editor"
---

## Categorías de utilización según IEC 60947-4-1

La norma IEC 60947-4-1 (*Low-voltage switchgear and controlgear — Part 4-1: Contactors and motor-starters*) establece las categorías de utilización de los contactores en función del tipo de carga conmutada. No es un dato de catálogo opcional: define con qué corriente hace y rompe el aparato en condiciones reales, y determina el desgaste de los contactos y la vida útil del equipo.

Para corriente alterna, las categorías principales son cuatro. El técnico que dimensiona un cuadro debe conocer qué corriente implica cada una, porque el mismo contactor tiene corrientes nominales distintas según la categoría.

| Categoría | Aplicación típica | Corriente de cierre (Imaking) | Corriente de apertura (Ibreaking) | cos φ |
|-----------|------------------|-------------------------------|-----------------------------------|-------|
| **AC-1**  | Cargas resistivas o débilmente inductivas (calefacción, baterías de condensadores) | 1 × Ie | 1 × Ie | ≥ 0,95 |
| **AC-2**  | Motores de rotor bobinado: arranque y frenado en contracorriente | 2,5 × Ie | 2,5 × Ie | 0,65 |
| **AC-3**  | Motores de jaula: arranque directo (DOL), apertura en marcha normal | 6 × Ie | 1 × Ie | 0,35 |
| **AC-4**  | Motores de jaula: jogging, plugging, inversión de marcha en plena corriente | 6 × Ie | 6 × Ie | 0,35 |

La diferencia entre AC-3 y AC-4 no está en la corriente de cierre, sino en la de apertura: en AC-3 el contactor abre con el motor girando a velocidad nominal (1×Ie), mientras que en AC-4 abre contra la corriente de arranque completa (6×Ie). Esta diferencia multiplica por varias veces la energía que debe disipar el arco en cada apertura, erosionando los contactos mucho más rápidamente.

---

## Diferencias técnicas entre AC-3 y AC-4: por qué importan los 6 × Ie

Durante el arranque directo de un motor de jaula de ardilla, la corriente de rotor bloqueado alcanza entre 5 y 7 veces la corriente nominal (según IEC 60034, el parámetro *k* del motor). A efectos de maniobra, IEC 60947-4-1 usa 6×Ie como valor de referencia para las corrientes de cierre en ambas categorías.

**En AC-3**, el ciclo normal es: cierre a 6×Ie (motor arrancando) → marcha estabilizada a 1×Ie → apertura a 1×Ie. El arco en apertura es pequeño; los contactos se erosionan lentamente. El fabricante garantiza typically 1,5 millones de ciclos mecánicos y 500.000–800.000 eléctricos a la corriente nominal de categoría.

**En AC-4**, el ciclo de jogging o plugging es: cierre a 6×Ie → apertura casi inmediata a 6×Ie. La energía del arco en apertura es proporcional a I²: con 6×Ie en la apertura, la energía es 36 veces mayor que en AC-3. Esto reduce drásticamente la vida eléctrica, típicamente a 50.000–100.000 ciclos para la misma corriente nominal AC-3.

**Consecuencia directa para el calibre**: si una aplicación requiere AC-4 con un motor de Ie = 22 A (motor 11 kW, 400 V), no basta un contactor de 25 A AC-3. La vida útil en AC-4 a 22 A exige un contactor con corriente nominal AC-4 ≥ 22 A, que normalmente corresponde a un aparato con corriente AC-3 de 65–95 A. Un ejemplo de referencia habitual: el LC1-D40 (40 A AC-3) solo permite 17 A en AC-4 a 400 V.

---

## Cálculo de corriente nominal del motor y selección del contactor

El punto de partida es la corriente nominal del motor a la tensión de red. Para un motor trifásico:

$$I_n = \frac{P}{\sqrt{3} \cdot U \cdot \cos\phi \cdot \eta}$$

**Ejemplo con datos GElectrical / IEC 60034:**

Motor 11 kW, 4 polos, IE3, 400 V:
- Eficiencia (η): 91,4 %
- cos φ: 0,86
- k (relación corriente arranque/nominal): 6,5

$$I_n = \frac{11\,000}{\sqrt{3} \times 400 \times 0{,}86 \times 0{,}914} = \frac{11\,000}{533{,}1} \approx 20{,}6 \text{ A}$$

Corriente de arranque: $I_{st} = 6{,}5 \times 20{,}6 = 133{,}9$ A (durante ~0,5–3 s en DOL)

**Para AC-3 (arranque DOL, apertura en marcha):**
- Corriente operacional Ie ≥ In_motor = 20,6 A
- Contactor normalizado: 25 A AC-3 @ 400 V → apto para motor 11 kW en AC-3

**Para AC-4 (jogging, plugging):**
- La corriente de apertura es 6 × 20,6 = 123,6 A a cos φ = 0,35
- Se necesita un contactor con Ie_AC4 ≥ 20,6 A → equivalente típico: 50–65 A AC-3 @ 400 V

La tabla siguiente muestra calibres normalizados según la equivalencia AC-3/AC-4 a 400 V (valores indicativos según IEC 60947-4-1; verificar con catálogo del fabricante):

| Potencia motor (kW) | In motor (A) | Contactor AC-3 mínimo (A) | Contactor equivalente AC-4 (A AC-3) |
|---------------------|-------------|--------------------------|--------------------------------------|
| 5,5 | ~11,6 | 12 | 25 |
| 7,5 | ~15,6 | 16 | 32 |
| 11 | ~20,6 | 25 | 50 |
| 15 | ~27,9 | 32 | 65 |
| 22 | ~40,2 | 40 | 95 |
| 37 | ~66,2 | 80 | 150 |

---

## Coordinación tipo 1 y tipo 2 con el relé de sobrecarga

IEC 60947-4-1 define dos niveles de coordinación entre el contactor y el elemento de protección contra sobrecarga (relé bimetálico o electrónico) ante un cortocircuito:

- **Tipo 1**: Tras el cortocircuito, puede ser necesario reparar o sustituir el contactor y el relé antes de rearmar. No se permite daño al cableado ni al cuadro. Es el mínimo aceptable.
- **Tipo 2**: Tras el cortocircuito, el contactor y el relé deben seguir siendo operativos sin sustitución. Se permiten leves marcas en los contactos del contactor. Requisito más exigente y habitual en instalaciones industriales continuas.

La coordinación debe ser declarada por el fabricante como un par (contactor + relé + fusible o magnetotérmico de protección de línea). No se puede verificar analíticamente en obra: hay que consultar las tablas de coordinación del catálogo.

**Un error frecuente**: usar un relé de sobrecarga con un contactor de distinto fabricante sin verificar la coordinación. IEC 60947-4-1 permite la combinación, pero exige que el conjunto haya sido ensayado. Sin esa verificación, la coordinación tipo 2 no está garantizada aunque ambos aparatos cumplan la norma individualmente.

---

## Temperatura ambiente y factor de corrección

Las corrientes nominales de los contactores están referenciadas a 40 °C de temperatura ambiente (IEC 60947-1, apartado 6.1.1). Por encima de este valor, los fabricantes especifican un factor de derating.

Ejemplo representativo: un contactor de 40 A AC-3 a 40 °C puede reducirse a 36 A a 55 °C y a 32 A a 70 °C. En instalaciones con variadores de frecuencia (habitualmente en armarios con temperatura elevada), este factor puede obligar a subir un calibre.

Adicionalmente, si el contactor trabaja en AC-4 con arranques frecuentes (>1 maniobra/minuto), el calor generado en los contactos se acumula. IEC 60947-4-1 Anexo F proporciona la metodología para calcular la temperatura de los contactos en función de la frecuencia de maniobra y la corriente.

---

## Criterios de selección en obra

1. **Identifica la categoría real de la carga.** Si el motor solo arranca y para (transportadores, bombas, compresores), es AC-3. Si el proceso requiere jogging, frenado por contracorriente o inversión frecuente de marcha (centrífugas, posicionadores), es AC-4. No elegir por defecto AC-3 sin verificarlo.

2. **Calcula la corriente nominal del motor** a la tensión de red, con los parámetros reales (η y cos φ de placa o catálogo IEC 60034). No uses tablas genéricas de potencia; el mismo kW puede dar corrientes distintas según el número de polos y la clase de eficiencia.

3. **Para AC-4, multiplica por 3 el calibre AC-3 equivalente** como regla de campo orientativa (no sustitutiva del catálogo). Un motor de 11 kW pide ~25 A AC-3; en AC-4 busca un contactor de ≥ 50 A AC-3.

4. **Verifica la coordinación tipo 2** en las tablas del fabricante, indicando el dispositivo de protección de línea (fusible gG/aM o magnetotérmico MCB/MCCB) y la corriente de cortocircuito en bornes.

5. **Aplica el factor de temperatura** si el armario supera 40 °C en operación, o si la frecuencia de maniobra es alta. Un margen del 10–15 % sobre In calculada protege contra estos efectos sin disparar el coste.

6. **No mezcles contactor y relé de distinto fabricante** sin tabla de coordinación explícita. La firma del cuadro es responsable del conjunto.

---

## Conclusión

La selección de un contactor no termina en la potencia del motor. La categoría de utilización AC-3 o AC-4 define la corriente de apertura real y, con ella, la vida eléctrica del aparato y el calibre necesario. Un contactor AC-3 de 25 A sobre un motor de jogging de 11 kW fallará prematuramente o en el primer cortocircuito. La norma IEC 60947-4-1 da las herramientas: corrientes de ensayo por categoría, coordinación tipo 1/tipo 2 y la metodología de verificación térmica para alta frecuencia de maniobra. El paso práctico en obra es siempre consultar las tablas de coordinación del fabricante con el trio contactor–relé–protección de línea antes de cerrar el esquema del cuadro.
