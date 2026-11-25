---
title: "Paralelado de transformadores MT/BT: condiciones según IEC 60076-8"
description: "Condiciones de paralelado de transformadores de distribución MT/BT, fórmulas de reparto de carga, corriente de circulación y criterios de selección según IEC 60076-8."
pubDate: 2026-11-25
keywords: ["paralelado transformadores MT/BT IEC 60076-8", "reparto de carga transformadores", "condiciones paralelado transformador", "corriente circulación transformadores paralelo"]
author: "Editor"
---

El paralelado de transformadores de distribución permite ampliar la potencia disponible en una subestación sin sustituir el equipo existente, incrementar la redundancia N-1 y reducir las pérdidas en vacío en horas valle desconectando uno de los transformadores. Sin embargo, un acoplamiento incorrecto —por diferencia de grupo vectorial, relación de transformación o tensión de cortocircuito— genera corrientes de circulación que pueden superar la corriente nominal antes de conectar ninguna carga. Este artículo desarrolla los cuatro criterios de acoplamiento según IEC 60076-8 y las fórmulas de reparto de carga con valores numéricos de transformadores de distribución 20/0,4 kV normalizados.

## Condiciones de paralelado según IEC 60076-8

IEC 60076-8 (*Parallel operation of transformers*) establece que dos transformadores son aptos para trabajar en paralelo cuando cumplen simultáneamente los cuatro criterios siguientes:

**1. Misma relación de transformación**

La diferencia de relación de transformación entre los dos transformadores no debe superar ±0,5 % para limitar la corriente de circulación a un valor admisible. Para un transformador 20/0,4 kV, la tensión en vacío del secundario debe estar entre 399 y 401 V con la toma principal. Con cambiadores de tomas, basta alinear las mismas posiciones.

La corriente de circulación debida a diferencia de relación ΔU es:

```
Icirc = ΔU / (Zcc1 + Zcc2)
```

donde Zcc1 y Zcc2 son las impedancias de cortocircuito absolutas de cada transformador referidas al secundario, y ΔU es la diferencia de tensión en vacío entre ambas máquinas.

**Ejemplo numérico**: dos transformadores 0,4 MVA 20/0,4 kV con Ucc=6 % (cada uno). Zcc = 0,06 × (0,4²/0,4) = 0,024 Ω por transformador. Si hay un desajuste de toma de 0,5 % → ΔU = 0,005 × 400 = 2 V:

```
Icirc = 2 / (0,024 + 0,024) = 41,7 A ≈ 7,2 % de In (577 A)
```

Aceptable. Con un desajuste de 2 % la corriente de circulación sube a 167 A (29 % de In), ya inadmisible en servicio continuo.

**2. Mismo grupo vectorial**

Dos transformadores con distinto grupo vectorial generan una diferencia de fase entre sus tensiones secundarias. Un desfase de 30° (p. ej., Dyn11 con Dyn1) produce una diferencia de tensión de:

```
ΔU = 2 × V × sin(15°) = 2 × 400 × 0,259 ≈ 207 V
```

La corriente resultante, a baja impedancia de cortocircuito del transformador, es destructiva. Los grupos compatibles son los que tienen el mismo ángulo horario. Para distribución en España lo habitual es Dyn11 (grupo de conexión 11, desfase 330°), y el paralelado exige que ambos sean Dyn11 o que la diferencia de ángulo sea exactamente 0°.

| Grupo T1 | Grupo T2 | Diferencia de fase | Compatible |
|----------|----------|-------------------|------------|
| Dyn11    | Dyn11    | 0°                | ✓          |
| Dyn11    | Dyn1     | 60°               | ✗          |
| Yz11     | Yz11     | 0°                | ✓          |
| Dyn11    | Yz11     | 0°                | ✓ (misma fase) |
| YNyn0    | Dyn11    | 30°               | ✗          |

**3. Tensión de cortocircuito similar (Ucc)**

La diferencia de Ucc entre dos transformadores en paralelo determina el desequilibrio en el reparto de carga. IEC 60076-8 no fija un límite absoluto, pero la práctica de ingeniería y el estándar EN 50588-1 para distribución recomiendan que la diferencia de Ucc no supere el 10 % del valor medio para evitar que el transformador de menor impedancia quede sobrecargado antes de alcanzar la potencia total del conjunto.

**4. Misma frecuencia y secuencia de fases**

Condición obvia en la práctica pero que debe verificarse en instalaciones que conecten alimentaciones de distintas fuentes o cuadros de distribución con origen diferente.

## Fórmulas de reparto de carga

Cuando los transformadores tienen la misma relación de transformación y el mismo grupo vectorial pero diferente Ucc, la carga se reparte inversamente proporcional a su impedancia de cortocircuito en por unidad (referida a la misma base de potencia):

```
Sa = S_total × (1/Zcc_a_pu) / (1/Zcc_a_pu + 1/Zcc_b_pu)
```

donde Zcc_pu = Ucc% / 100 (asumiendo que la potencia base es la potencia nominal de cada transformador, ajustada a base común).

**Referir a base común**: si los transformadores tienen distinta potencia nominal, hay que referir todas las impedancias a la misma MVA_base (habitualmente la potencia del transformador mayor):

```
Zcc_a_pu_base = (Ucc_a% / 100) × (MVA_base / MVA_a)
Zcc_b_pu_base = (Ucc_b% / 100) × (MVA_base / MVA_b)
```

### Ejemplo con datos GElectrical / IEC 60076

Base de datos GElectrical (implementa IEC 60076) para transformadores de distribución 20/0,4 kV:

| Sn (MVA) | Ucc (%) | Pcu (% de Sn) | Pfe (kW) | I₀ (%) |
|----------|---------|---------------|----------|--------|
| 0,25     | 6,00    | 1,44          | 0,80     | 0,32   |
| 0,40     | 6,00    | 1,425         | 1,35     | 0,34   |
| 0,63     | 6,00    | 1,206         | 1,65     | 0,26   |

Paralelado de T1 (0,25 MVA, Ucc=6 %) + T2 (0,63 MVA, Ucc=6 %), base = 0,63 MVA:

```
Zcc_T1_pu_base = 0,06 × (0,63 / 0,25) = 0,1512 pu
Zcc_T2_pu_base = 0,06 × (0,63 / 0,63) = 0,06 pu
```

Reparto para carga total S_total = 0,70 MVA (dentro de la potencia del conjunto 0,88 MVA):

```
S_T1 = 0,70 × (1/0,1512) / (1/0,1512 + 1/0,06)
      = 0,70 × 6,61 / (6,61 + 16,67) = 0,70 × 0,284 = 0,199 MVA  (79,6 % de Sn_T1)
S_T2 = 0,70 × 0,716 = 0,501 MVA  (79,5 % de Sn_T2)
```

La carga se reparte proporcionalmente a la potencia nominal cuando Ucc es idéntico — el transformador de menor potencia carga al mismo porcentaje de su nominal. Si los Ucc fueran distintos (p. ej., T1 con Ucc=4 % y T2 con Ucc=6 %), el transformador de menor impedancia (T1, Ucc=4 %) recibiría más carga y podría sobrecargarse antes de que el conjunto alcance la potencia total.

## Corriente de circulación por diferencia de Ucc

Cuando dos transformadores con la misma relación de transformación pero distinta Ucc se conectan en paralelo sin carga, circula una corriente debida a la diferencia de tensión interna:

```
Icirc = ΔUcc_pu × V_base / (Zcc_T1_abs + Zcc_T2_abs)
```

donde ΔUcc_pu es la diferencia de Ucc en por unidad y Zcc_abs es la impedancia absoluta de cada transformador.

Para T1 (0,25 MVA, Ucc=6 %) y T2 (0,63 MVA, Ucc=4 %) en base 0,4 kV:

```
Zcc_T1 = 0,06 × (0,4²/0,25) = 0,06 × 0,64 = 0,0384 Ω
Zcc_T2 = 0,04 × (0,4²/0,63) = 0,04 × 0,254 = 0,01016 Ω

ΔUcc_pu = 0,06 - 0,04 = 0,02 pu → ΔV = 0,02 × 400 V = 8 V

Icirc = 8 / (0,0384 + 0,01016) = 8 / 0,04856 = 164,8 A
```

Comparado con In_T1 = 0,25 × 10⁶ / (√3 × 400) = 361 A → Icirc = 45,6 % de In_T1. Esta corriente de circulación pura, antes de conectar ninguna carga, haría necesario despejar cuadro o revisar la selección.

## Verificación de secuencia de fases y puesta en paralelo

Antes de cerrar el interruptor de acoplamiento, el protocolo normalizado exige:

1. **Comprobación de grupo vectorial**: verificar con voltímetro la diferencia de tensión entre los bornes secundarios de ambos transformadores. Con ambos secundarios sin cargar y con la misma toma principal, la lectura debe ser < 2 % de V_n (< 8 V en un sistema 400 V). Si se mide entre la fase L1 de T1 y L1 de T2 y se obtiene > 100 V, el grupo vectorial es incompatible.

2. **Sincronoscopio o comprobador de fase**: para instalaciones con interruptores automáticos de acoplamiento (ATSs o interruptores de barras), la condición de cierre se verifica mediante relé de verificación de sincronismo (función ANSI 25) ajustado a: ΔV < 10 %, Δf < 0,2 Hz, Δφ < 10°.

3. **Secuencia de maniobra**: primero conectar el interruptor general de T1, comprobar tensión en barras, después cerrar el interruptor de T2 con comprobación de sincronismo activa. Nunca cerrar T2 manualmente sin relé de verificación cuando los transformadores provienen de alimentaciones distintas.

## Criterios de selección para paralelado en obra

La tabla siguiente resume los criterios de decisión aplicables en campo antes de autorizar el acoplamiento:

| Parámetro            | Límite IEC 60076-8 / práctica  | Consecuencia si no se cumple              |
|----------------------|-------------------------------|-------------------------------------------|
| Diferencia relación  | ≤ ±0,5 %                      | Corriente de circulación > 7 % de In      |
| Grupo vectorial      | Mismo ángulo horario           | Falta de cortocircuito en el acoplamiento |
| Diferencia Ucc       | ≤ 10 % del valor medio         | Reparto desigual, sobrecarga del menor Ucc|
| Secuencia de fases   | RST = RST                     | Inversión de fases, daño a cargas motoras |
| Tensión en vacío T2  | V_T2 ≈ V_barras ± 1 %         | Requisito previo al cierre del acoplamiento|

**Regla de selección rápida**: para dos transformadores de distribución a instalar en paralelo en una subestación MT/BT nueva, seleccionar unidades del mismo fabricante, misma gama y misma potencia. Garantiza Ucc idéntico (±0,2 %), mismo grupo vectorial y misma relación de transformación. El coste adicional de esta decisión es nulo; el coste de una selección incorrecta incluye el transformador rechazado y la modificación del esquema de barras.

**Transformadores de distinta potencia en paralelo**: es técnicamente viable si Ucc son iguales (mismo %) y el grupo vectorial coincide. El reparto de carga es automáticamente proporcional a Sn, como se mostró en el ejemplo numérico anterior con 0,25 y 0,63 MVA. En la práctica, la combinación habitual en ampliaciones es un transformador existente (p. ej., 0,4 MVA) más un nuevo de igual o mayor potencia, con Ucc verificado antes de la compra.

## Pérdidas en paralelo frente a un único transformador de mayor potencia

Un factor que justifica o descarta el paralelado frente a sustitución es el balance de pérdidas. En vacío (horas valle), dos transformadores en paralelo consumen el doble de pérdidas en vacío que uno solo. Para el caso 0,25 + 0,63 MVA en paralelo:

```
Pfe_total = 0,80 kW + 1,65 kW = 2,45 kW (en vacío, ambos en servicio)
```

Un transformador único de 0,63 MVA consume solo 1,65 kW en vacío. Si el suministro opera más de 4.000 h/año en vacío, la diferencia de pérdidas puede justificar desconectar el transformador pequeño en horas de baja carga y aceptar la pérdida de redundancia.

## Conclusión

El paralelado de transformadores de distribución MT/BT es viable y eficiente cuando se verifican los cuatro criterios de IEC 60076-8 — relación de transformación, grupo vectorial, Ucc y secuencia de fases — antes del acoplamiento. Los cálculos de corriente de circulación y reparto de carga son directos y deben ejecutarse en la ingeniería básica con los datos de placa de los transformadores. Para unidades de igual potencia nominal e idéntico Ucc, el reparto es exactamente proporcional. La diferencia de Ucc entre transformadores en paralelo es el parámetro más crítico en instalaciones existentes ampliadas: una diferencia del 2 % en valor absoluto (p. ej., Ucc=4 % vs. 6 %) genera corrientes de circulación que pueden superar el 40 % de la corriente nominal del transformador de menor impedancia antes de conectar ninguna carga.
