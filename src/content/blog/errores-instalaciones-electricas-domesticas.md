---
title: "Errores en instalaciones eléctricas domésticas"
description: "Los 7 errores más graves en instalaciones eléctricas domésticas según REBT ITC-BT, IEC 60364 y UNE-EN 60898. Diagnóstico y criterios de corrección para técnicos."
pubDate: 2026-07-23
keywords: ["errores instalaciones electricas", "errores instalacion electrica domestica", "fallos electricos domésticos REBT", "sección cable infradimensionada", "diferencial tipo A AC IEC 61008"]
author: "Editor"
---

Una instalación eléctrica doméstica defectuosa no siempre se manifiesta con un disparo o un incendio. Con frecuencia, los errores más peligrosos son silenciosos: un cable infradimensionado que trabaja al 110 % de su capacidad durante años, una toma de tierra con resistencia de 2 kΩ que no protege frente a ningún fallo de aislamiento, o un diferencial tipo AC instalado en un circuito con cargas electrónicas que genera corrientes de fuga con componente continua. Este artículo recorre los siete errores más comunes que un técnico encuentra en inspecciones y reformas de viviendas, con referencia normativa específica y criterio de corrección.

---

## 1. Sección de conductor infradimensionada respecto a la carga real

El error más frecuente en reformas y ampliaciones: añadir tomas o equipos a un circuito existente sin recalcular la sección del conductor. La tabla 52-4 de la norma **IEC 60364-5-52** (adoptada como **UNE-HD 60364-5-52**) establece la intensidad admisible según sección, tipo de aislamiento y método de instalación. En instalaciones bajo tubo empotrado (método B2), un conductor de Cu de 2,5 mm² con aislamiento XLPE admite 26 A en monofásico; con PVC, 21 A.

La **ITC-BT-19** del REBT fija las secciones mínimas para los circuitos interiores de vivienda:

| Circuito (ITC-BT-25) | Sección mínima Cu | Intensidad máx. prevista |
|---|---|---|
| Iluminación | 1,5 mm² | 10 A |
| Tomas de uso general | 2,5 mm² | 16 A |
| Cocina / horno | 6 mm² | 25 A |
| Lavadora / lavavajillas | 4 mm² | 20 A |
| Toma de 25 A (secadora, etc.) | 6 mm² | 25 A |
| Climatización | 6 mm² | 25 A |

El error diagnóstico consiste en instalar circuitos de climatización (2.000–3.500 W + picos de arranque) sobre 2,5 mm², argumentando que "el magnetotérmico es de 16 A". La **protección sobreintensidad garantiza que la corriente no supera la admisible del cable**, no al revés: si la carga máxima del circuito supera la capacidad del conductor, el magnetotérmico puede no disparar mientras el cable se calienta por encima de su temperatura máxima de servicio (70 °C para PVC, 90 °C para XLPE).

**Criterio de corrección**: recalcular Iz para la carga real más el factor de agrupamiento (tabla 52-17, IEC 60364-5-52) y sustituir el conductor si Ib > Iz, o reducir el calibre de la protección si se quiere mantener el cable.

---

## 2. Toma de tierra ausente, interrumpida o con resistencia fuera de rango

La **ITC-BT-18** establece la resistencia máxima del electrodo de puesta a tierra en función de la sensibilidad del diferencial y de la tensión de contacto admisible:

**R(Ω) × IΔn(A) ≤ Vc(V)**

Para IΔn = 30 mA y Vc = 50 V (locales secos): R ≤ 1.667 Ω
Para IΔn = 30 mA y Vc = 24 V (locales húmedos/baños): R ≤ 800 Ω

En la práctica, los técnicos encuentran tres variantes del problema:

- **Tierra inexistente**: instalaciones anteriores al REBT 1973 o con posteriores reformas deficientes. El diferencial no puede actuar ante fallos de aislamiento porque no existe retorno de la corriente de fuga.
- **Tierra conectada al neutro** (error de montaje): provoca que cualquier fuga a masa genere un cortocircuito en lugar de activar el diferencial. Especialmente peligroso con equipos de doble aislamiento.
- **Continuidad interrumpida**: el conductor de protección (CP, color amarillo-verde, ITC-BT-19) está conectado en cuadro pero cortado en algún punto del recorrido. La medida con impedancímetro de lazo de tierra (método según **IEC 61557-3**) localiza el punto de ruptura.

La verificación mínima exige medir la resistencia de lazo de tierra Zs y comprobar que Ia × Zs ≤ Vc, donde Ia es la corriente de actuación de la protección (IEC 60364-4-41, tabla 41.1).

---

## 3. Diferencial tipo AC en circuitos con cargas electrónicas

La **IEC 61008-1** (UNE-EN 61008-1) clasifica los interruptores diferenciales por el tipo de corriente de fuga que detectan:

| Tipo | Corriente de fuga detectada | Aplicación típica |
|---|---|---|
| AC | Solo sinusoidal a 50 Hz | Resistencias puras, motores simples sin variador |
| A | Sinusoidal + continua pulsante | Variadores, cargadores, electrodomésticos con electrónica |
| F | Tipo A + alta frecuencia (1–1.000 Hz) | VFD trifásicos, fuentes SMPS |
| B | AC + DC puro | Fotovoltaica, vehículo eléctrico |

El error sistemático: instalar diferencial tipo AC en viviendas modernas donde la mayoría de los equipos (placas de inducción, lavadoras inverter, cargadores, aires inverter) generan corrientes de fuga con componente continua. Un diferencial tipo AC no detecta corriente de fuga continua pulsante; puede no disparar aunque la corriente de fuga real supere 30 mA, incumpliendo la protección exigida por **ITC-BT-24**. La actualización del REBT 2025 recomienda diferencial tipo A como mínimo en todos los circuitos de vivienda con cargas electrónicas.

---

## 4. Coordinación magnetotérmico-conductor incorrecta

Un magnetotérmico de calibre superior a la capacidad del cable no protege al conductor frente a sobrecarga. La condición de coordinación según **ITC-BT-22** y **IEC 60364-4-43** exige:

- **Ib ≤ In ≤ Iz** (corriente de empleo ≤ calibre ≤ admisible del cable)
- **I2 ≤ 1,45 × Iz** (corriente de disparo a tiempo definido no supera 1,45 veces la admisible)

Ejemplo real: circuito de tomas de uso general con conductor 2,5 mm² Cu/PVC bajo tubo empotrado (Iz = 21 A, según UNE-HD 60364-5-52 tabla B.52.4) protegido con magnetotérmico **C25**. La corriente de no disparo en 1 h para un C25 (IEC 60898-1) es 1,45 × 25 = 36,25 A, muy superior a los 21 A admisibles del conductor. El cable puede calentarse sostenidamente por encima de 70 °C sin que el magnetotérmico dispare. La corrección exige bajar a **C16** (In = 16 A ≤ Iz = 21 A).

Los calibres normalizados según IEC 60898-1 son: 6, 10, 16, 20, 25, 32, 40, 50, 63 A en curvas B, C y D. Utilizar calibres intermedios no normalizados (13 A, 18 A) obliga a justificar la selección mediante ensayo del fabricante.

---

## 5. Neutro compartido entre circuitos independientes

Puentear el neutro de salida de varios magnetotérmicos en un único conductor neutro viola la **ITC-BT-22** y la **ITC-BT-19**, que exigen que cada circuito disponga de su propio conductor neutro con sección igual a la de fase. Los riesgos:

- Si el neutro compartido se interrumpe, todos los circuitos asociados quedan sin referencia. Con cargas desequilibradas, puede aparecer tensión en el neutro superior a 230 V en los receptores más ligeros.
- Impide la desconexión individual del neutro en mantenimiento, exigida en ITC-BT-22 para circuitos monofásicos donde el magnetotérmico unipolar solo corta la fase.

---

## 6. Ausencia de diferencial 30 mA en volúmenes de baños

La **ITC-BT-27** exige protección diferencial de 30 mA para todos los circuitos que alimenten tomas o equipos en los **volúmenes 1 y 2** de locales con bañera o ducha (según **IEC 60364-7-701**):

- **Volumen 0**: interior de la bañera/plato de ducha. Solo SELV ≤ 12 V AC.
- **Volumen 1**: hasta 2,25 m sobre el borde. Solo aparatos clase II IPX4, con diferencial 30 mA.
- **Volumen 2**: 0,6 m alrededor del volumen 1. Tomas SCHUKO permitidas con diferencial 30 mA.

El error habitual: cuadro con diferencial general de 300 mA (protección contra incendios) sin diferencial de 30 mA aguas abajo para los circuitos de baño. El diferencial de 300 mA no protege a las personas; su único objeto es detectar fugas de arco antes de que provoquen incendio.

---

## 7. Empalmes fuera de caja de registro

Los empalmes en conductores deben realizarse en **cajas de derivación** con grado de protección acorde al local (IP 55 en baños, IP 65 en exteriores, según **IEC 60529**), usando bornes o clemas homologadas. Los empalmes con cinta adhesiva no tienen la misma rigidez dieléctrica ni clase de temperatura que el aislamiento original del cable. La **ITC-BT-20** prohíbe expresamente las uniones con soldadura de estaño, que crea un punto de alta resistencia de contacto susceptible de oxidación progresiva y calentamiento bajo carga.

---

## Tabla de diagnóstico rápido en inspección

| Error | Señal en campo | Normativa | Corrección |
|---|---|---|---|
| Cable infradimensionado | Cable caliente, caída V > 3 % | ITC-BT-19, IEC 60364-5-52 | Sustituir conductor o reducir calibre protección |
| Tierra ausente/interrumpida | Zs infinita, Vcontacto > 50 V | ITC-BT-18, IEC 60364-4-41 | Instalar electrodo, verificar continuidad CP |
| Diferencial tipo AC con electrónica | No dispara ante fuga DC pulsante | IEC 61008-1, ITC-BT-24 | Sustituir por tipo A |
| Magnetotérmico sobredimensionado | In > Iz del conductor | ITC-BT-22, IEC 60364-4-43 | Reducir calibre hasta Ib ≤ In ≤ Iz |
| Neutro compartido | Tensión en neutro, sin interruptor de neutro | ITC-BT-22, ITC-BT-19 | Independizar neutro por circuito |
| Sin diferencial 30 mA en baños | Diferencial ≥ 300 mA en subcuadro | ITC-BT-27, IEC 60364-7-701 | Instalar diferencial 30 mA para circuitos de baño |
| Empalmes fuera de caja | Cinta adhesiva en trasdós o falso techo | ITC-BT-20 | Reubicar en caja de registro con clemas |

---

## Criterios de priorización en revisión o reforma

No todos los errores tienen el mismo peso de riesgo. El orden de intervención técnica:

1. **Prioridad máxima (riesgo vital inmediato)**: tierra ausente + circuito sin diferencial + masa accesible a tensión. Los tres juntos crean una situación en la que un fallo de aislamiento genera electrocución sin ninguna protección activa.

2. **Prioridad alta (riesgo de incendio)**: cable infradimensionado bajo carga continua, empalmes sin caja en trasdós o bajo aislante térmico.

3. **Prioridad media (riesgo latente)**: diferencial tipo AC con cargas electrónicas, magnetotérmico sobredimensionado.

4. **Prioridad de conformidad normativa**: neutro compartido, ausencia de circuitos independientes por zona (ITC-BT-25), previsión de carga para recarga de VE (ITC-BT-52, actualización REBT 2025).

---

## Conclusión

Los errores en instalaciones eléctricas domésticas no se corrigen con criterios estéticos sino con medidas instrumentales: impedancímetro de lazo (IEC 61557-3), medidor de resistencia de aislamiento (IEC 61557-2), comprobador de continuidad de tierra y analizador de corriente de fuga diferencial. La inspección visual detecta lo evidente; la verificación eléctrica es la que distingue una instalación conforme del REBT de una que simplemente "funciona hoy". Cualquier reforma que amplíe la carga instalada exige revisar la coordinación de protecciones desde la cabecera del cuadro, no solo los circuitos nuevos.
