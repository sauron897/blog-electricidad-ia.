---
title: "Protección de motores: falta de fase y desequilibrio ANSI 46 y 47"
description: "Análisis técnico de ANSI 46 y 47 para protección de motores IE3 contra falta de fase y desequilibrio de tensión según IEC 60255, IEC 60034-26 e IEC 60947-4-1."
pubDate: 2026-11-21
keywords: ["protección motor falta de fase desequilibrio tensión", "ANSI 46 motor desequilibrio corriente", "ANSI 47 inversión de fase motor", "relé protección motor IEC 60947-4-1"]
author: "Editor"
---

## Introducción: por qué el desequilibrio y la falta de fase destruyen motores IE3

El motor de inducción trifásico de jaula de ardilla es la máquina eléctrica más extendida en la industria. Su diseño asume tensiones de alimentación simétricas y equilibradas; cualquier asimetría genera componentes de secuencia negativa que producen un par frenante interno, corrientes elevadas en el devanado más cargado y un calentamiento desproporcionado que acorta drásticamente la vida del aislamiento.

Los dos fenómenos a gestionar son el **desequilibrio de tensión** —asimetría entre las tres tensiones de línea medida en tanto por ciento— y la **falta de fase** —ausencia total de una de las tres tensiones, caso extremo de desequilibrio—. Ambos están cubiertos por las **funciones ANSI 46** (protección por desequilibrio de corriente o pérdida de fase) y **ANSI 47** (protección por inversión de fase), implementadas en relés que deben cumplir **IEC 60255** en sus partes aplicables: IEC 60255-149 para modelos térmicos e IEC 60255-181 para protecciones de frecuencia y secuencia.

---

## Desequilibrio de tensión: definición IEC, fórmula y umbrales

La norma **IEC 60034-26:2006** (*Effects of unbalanced voltages on the performance of squirrel-cage induction motors*) define el factor de desequilibrio de tensión (FDT) como:

$$
FDT (\%) = \frac{U_{máx. desviación}}{U_{media}} \times 100
$$

donde U_máx. desviación es la diferencia máxima entre cualquier tensión de línea y la media aritmética de las tres.

**Umbrales operativos:**

- **FDT < 1 %**: operación nominal sin restricción.
- **1 % ≤ FDT < 2 %**: operación con vigilancia; algunos fabricantes requieren derating del motor.
- **FDT ≥ 2 %**: IEC 60034-26 recomienda aplicar factor de reducción de carga; para FDT = 3,5 % la reducción es aproximadamente del 10 % de la potencia nominal.
- **FDT ≥ 5 %** (o ausencia de una fase): parada inmediata obligatoria.

La relación entre desequilibrio de tensión y desequilibrio de corriente es no lineal: un FDT del **1 %** puede generar un desequilibrio de corriente de **6 % a 10 %** en la fase más cargada (Fluke, basado en IEC 60034-26). Un FDT del 3,5 % eleva la temperatura del devanado en unos **25 °C**, lo que según la regla de Arrhenius para aislamientos Clase F (155 °C) reduce la vida útil del aislamiento aproximadamente un **75-80 %**.

| FDT (%) | Aumento de corriente aprox. | ΔT devanado (°C) | Reducción vida útil |
|---------|---------------------------|-------------------|---------------------|
| 1       | 6–10 %                    | 7–10              | ~25 %               |
| 2       | 12–20 %                   | 15–18             | ~50 %               |
| 3,5     | 20–35 %                   | 25–30             | 75–80 %             |
| 5       | 35–50 %                   | >40               | >90 %               |

*Fuente: IEC 60034-26:2006 e IEC 60255-149 (modelo térmico).*

---

## Falta de fase: causas, mecanismo de daño y comportamiento del motor

La pérdida de una fase puede originarse en:
- Fusible gG/aM fundido en uno de los tres conductores (asimétrico por I²t selectivo).
- Apertura de un polo del contactor por soldadura o desgaste.
- Fallo de continuidad en el cable de alimentación.
- Apertura de un relé de sobreintensidad monofásico mal coordinado.

Cuando una fase desaparece con el motor ya en marcha, el motor **no se detiene**: sigue girando alimentado por las dos fases restantes (**modo bifásico**), pero la potencia disponible cae a aproximadamente el **50–60 %** de la nominal. Las corrientes en los devanados restantes crecen entre un 70 % y un 100 % para mantener el par resistente. Si la carga no se reduce, el motor alcanza la temperatura de disparo térmico en **1 a 5 minutos** dependiendo de la clase de disparo del relé de sobrecarga.

Si la falta de fase ocurre **en arranque**, el motor no gira (par de arranque nulo en modo bifásico para un motor de jaula) y la corriente de bloqueo rotor —típicamente **6 a 6,5 × I_n** según GElectrical/IEC 60034— se mantiene indefinidamente hasta la intervención de la protección.

**Ejemplo numérico**: motor 22 kW, 400 V, 4P, IE1, cos φ = 0,90, η = 89,9 % (datos GElectrical):

$$
I_n = \frac{22.000}{\sqrt{3} \times 400 \times 0{,}90 \times 0{,}899} = \frac{22.000}{559} \approx 39{,}4 \text{ A}
$$

Con falta de fase en marcha, las dos fases activas verán corrientes de **60–70 A** (150–180 % de I_n), superando el umbral de disparo de clase 10 de un relé de sobrecarga en 90–120 s si la carga es plena.

---

## Función ANSI 46: protección por desequilibrio de corriente y pérdida de fase

**ANSI 46** mide el desequilibrio entre las corrientes de las tres fases. El criterio típico es:

$$
I_{deseq} (\%) = \frac{I_{máx} - I_{min}}{I_{media}} \times 100
$$

Los relés de protección de motor modernos (Schneider TeSys D/F, Siemens 3RB, ABB EF460) incorporan ANSI 46 con dos umbrales configurables:
- **Alarma**: 10–20 % de desequilibrio (ajustable), retardo 2–5 s.
- **Disparo**: 30–50 % de desequilibrio (típico para falta de fase), retardo 0,5–2 s.

Según **IEC 60947-4-1:2021** (*Low-voltage switchgear — electromechanical contactors and motor-starters*), Tabla 1, los relés de sobrecarga de Clase 10 y 20 que incorporan función de pérdida de fase deben disparar antes de que la temperatura del devanado supere el límite de la clase de aislamiento. Específicamente, con falta de una fase y carga al 75 % de I_n, el disparo debe producirse en un tiempo que no permita superar la temperatura nominal de clase.

**Coordinar ANSI 46 con el relé térmico integrado** es crítico: si el relé de sobrecarga tiene umbral de disparo por desequilibrio, debe ajustarse para actuar **antes** de que el modelo térmico integrado provoque un disparo por sobretemperatura, ya que la causa es diferente y el diagnóstico de fallo lo exige.

---

## Función ANSI 47: protección por inversión de fase (secuencia negativa)

**ANSI 47** detecta la inversión del orden de fase (L1-L3-L2 en lugar de L1-L2-L3). Un motor trifásico conectado con fase invertida gira en sentido contrario al previsto, lo que en equipos con carga mecánica unidireccional (bombas, compresores, ventiladores centrífugos) puede causar daños mecánicos inmediatos o cavitación.

La protección se implementa mediante la medición de la **componente de secuencia negativa** de las tensiones de alimentación. Con secuencia positiva correcta V₂ ≈ 0; con secuencia invertida V₂ = V₁. El relé dispara en 0,1–0,5 s (prácticamente instantáneo) antes de que el motor pueda acelerar en sentido contrario.

**IEC 60255-181:2020** (*Measuring relays and protection equipment — Functional requirements for frequency protection*) no cubre directamente ANSI 47, pero los relés multifunción que implementan ANSI 47 citan IEC 60255-27 para los requisitos de rendimiento eléctrico del equipo.

---

## Criterios de selección y ajuste en obra

La decisión sobre qué protecciones implementar depende de la criticidad del motor y el tipo de instalación:

| Criterio | Relé térmico básico IEC 60947-4-1 | Guardamotor con ANSI 46 integrado | Relé multifunción con ANSI 46 + 47 |
|----------|----------------------------------|----------------------------------|-------------------------------------|
| Coste | Bajo | Medio | Alto |
| Detección falta de fase | Solo por sobreintensidad | Directa, < 2 s | Directa, < 0,5 s |
| Detección desequilibrio | No (o muy limitada) | Sí, ajustable | Sí, con alarma y disparo |
| Detección inversión fase | No | No (algunos sí) | Sí, ANSI 47 |
| Aplicación recomendada | Motores ≤ 7,5 kW, no críticos | Motores 7,5–75 kW, proceso continuo | Motores > 75 kW, criticidad alta |
| Referencia normativa | IEC 60947-4-1 | IEC 60947-4-1 + IEC 60255-149 | IEC 60255-149, IEC 60255-181 |

**Ajuste del umbral de ANSI 46 en obra:**

1. Medir el FDT en el punto de alimentación del motor bajo carga nominal con analizador de red (IEC 61557-12 para requisitos del instrumento).
2. Si FDT > 1,5 %, investigar causa antes de ajustar el relé —no compensar desequilibrio de red con umbrales de disparo más laxos.
3. Umbral de alarma de desequilibrio de corriente: ajustar al 15 % (valor típico para alertar antes del daño térmico).
4. Umbral de disparo: 40 % para aplicaciones estándar; 25 % para motores IE3/IE4 en proceso crítico (clases de aislamiento F, resistencia térmica menor al desequilibrio que IE1/IE2 por mayor densidad de ranura).
5. Para ANSI 47, activar siempre en motores con carga unidireccional; en motores con carga reversible (grúas con variador), puede inhibirse si el variador gestiona la secuencia.

**Tabla de tiempos de disparo orientativos según clase (IEC 60947-4-1, Clase 10A):**

| Situación | Tiempo máximo de disparo |
|-----------|--------------------------|
| Falta de fase con carga al 100 % I_n | ≤ 10 s (Clase 10A) |
| Desequilibrio 40 % corriente | 2–5 s (ajustable) |
| Inversión de fase (ANSI 47) | 0,1–0,5 s |
| Sobreintensidad 7 × I_n (bloqueo rotor) | ≤ 5 s (Clase 10A, en frío) |

---

## Coordinación con la protección térmica de sobrecarga

El relé de sobrecarga integra un modelo térmico (IEC 60255-149) que acumula calor independientemente de si el origen es sobreintensidad, desequilibrio o falta de fase. La clave es que:

- **Sin ANSI 46**, la falta de fase en marcha puede no disparar el modelo térmico hasta alcanzar el umbral de temperatura —tiempo de 1 a 5 minutos— cuando el motor ya ha sufrido daño en el devanado.
- **Con ANSI 46**, el disparo por desequilibrio actúa antes de que el modelo térmico llegue al límite, con tiempos de 0,5 a 2 s.
- El **bloqueo de rearranque** tras un disparo ANSI 46 debe mantenerse hasta identificar la causa: un rearranque inmediato sobre una instalación con fusible fundido resulta en un nuevo disparo más rápido y mayor degradación del aislamiento.

La **ITC-BT-47** del REBT no especifica la función ANSI 46, pero exige que los motores > 0,75 kW dispongan de protección contra sobrecargas. Para motores en instalaciones industriales con proceso continuo, la interpretación habitual en inspecciones del REBT incluye la protección contra falta de fase como parte de la protección completa del motor, especialmente si está conectado a cuadros de distribución de BT con fusibles individuales por fase.

---

## Conclusión

La protección **ANSI 46** es el elemento diferencial entre un relé de sobrecarga básico y una protección de motor técnicamente correcta para instalaciones industriales. Con un FDT del 3,5 % —perfectamente posible en redes industriales con cargas desequilibradas— la vida útil del aislamiento se reduce en un 75 %, y un relé térmico sin ANSI 46 no actuará hasta que ya haya daño acumulado. La función **ANSI 47** es de implementación prácticamente obligatoria en motores con carga unidireccional, dado que el tiempo de actuación (< 0,5 s) evita cualquier movimiento mecánico en sentido incorrecto.

En instalaciones de nueva implantación con motores IE3/IE4, la selección de guardamotores con ANSI 46 integrado —cumpliendo IEC 60947-4-1 y coordinados con fusibles aM según IEC 60269-4— representa el estándar mínimo técnico justificado; para motores > 75 kW o proceso crítico, el relé multifunción con IEC 60255-149 y ajuste de umbral de desequilibrio en campo es la solución de referencia.
