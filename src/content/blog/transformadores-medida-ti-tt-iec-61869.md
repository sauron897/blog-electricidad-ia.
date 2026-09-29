---
title: "Transformadores de Medida TI y TT: Clases IEC 61869"
description: "Clases de precisión, factor límite de exactitud y criterios de selección de transformadores de corriente (TI) y tensión (TT) según IEC 61869-2 e IEC 61869-3 para instalaciones MT/BT."
pubDate: 2026-09-29
keywords: ["transformadores medida TI TT IEC 61869", "clase precision transformador corriente", "factor limite exactitud ALF", "carga VA transformador medida", "transformador tension MT BT"]
author: "Editor"
---

Los transformadores de medida son el eslabón crítico entre la red de alta o media tensión y los circuitos de medición y protección a 100 V / 1 A o 5 A. Un error de clase o una carga mal calculada en el secundario degrada la exactitud de los contadores de facturación, desajusta los relés de protección o provoca saturación del núcleo durante una falta. **IEC 61869** (serie completa, que sustituye a IEC 60044) establece los requisitos generales (parte 1), de los transformadores de corriente —TI— (parte 2) y de los transformadores de tensión inductivos —TT— (parte 3).

---

## Transformadores de Corriente (TI): Estructura y Parámetros Nominales

Un TI reduce la corriente de línea a un valor normalizado de **1 A o 5 A** en el secundario, con aislamiento galvánico de la red primaria. Los parámetros fundamentales que identifican a un TI son:

- **Relación nominal de transformación** (kn): p.ej. 200/5 A, 1000/1 A
- **Carga nominal (Sn)**: potencia aparente que puede conectarse al secundario manteniendo la clase de exactitud. Valores normalizados según IEC 61869-2: 2,5 – 5 – 10 – 15 – 30 VA
- **Clase de exactitud**: define el error máximo de relación y desfase en condiciones especificadas
- **Factor límite de exactitud (ALF)**: múltiplo de la corriente nominal hasta el cual se garantiza la clase en los TI de protección

### Clases de Exactitud para Medición

Para aplicaciones de medición y facturación, IEC 61869-2 define las siguientes clases:

| Clase | Error de relación máx. (100–120% In) | Aplicación típica |
|-------|--------------------------------------|-------------------|
| 0,1   | ±0,1 %                               | Patrones de laboratorio, calibración |
| 0,2   | ±0,2 %                               | Contadores de alta precisión, clase A |
| 0,2S  | ±0,2 % (desde el 1 % de In)          | Contadores con carga muy variable |
| 0,5   | ±0,5 %                               | Contadores de clase B, vatímetros |
| 0,5S  | ±0,5 % (desde el 1 % de In)          | Redes con bajo factor de carga |
| 1     | ±1 %                                 | Instrumentos de cuadro, indicadores |
| 3     | ±3 %                                 | Control, supervisión sin facturación |

Las clases **S** (IEC 61869-2, cláusula 5.6.202) mantienen el error de relación especificado entre el 1 % y el 120 % de la corriente nominal, frente a las clases estándar que sólo lo garantizan entre el 5 % y el 120 %. Son obligatorias en instalaciones con generación distribuida o carga variable, donde el período de carga mínima puede ser prolongado.

### Clases de Exactitud para Protección

Los TI de protección deben soportar las corrientes de falta sin saturar antes de que el relé actúe. IEC 61869-2 define:

| Designación | Error compuesto máx. | Factor ALF | Significado |
|-------------|---------------------|-----------|-------------|
| 5P5         | 5 %                 | 5         | Saturación a 5×In |
| 5P10        | 5 %                 | 10        | Saturación a 10×In |
| 5P20        | 5 %                 | 20        | Saturación a 20×In |
| 10P10       | 10 %                | 10        | Protecciones menos exigentes |
| 10P20       | 10 %                | 20        | Sobrecorriente de tiempo inverso |

**Lectura de la designación 5P10:** el "5" es el error compuesto máximo en porcentaje; "P" indica clase de protección; "10" es el ALF — la relación entre la corriente límite de exactitud (I_eal = ALF × In) y la corriente primaria nominal. El TI debe reproducir la corriente sin saturar hasta I_eal = 10 × In.

El **error compuesto** según IEC 61869-2, cláusula 3.4.201 incluye el error de relación, el error de desfase y los armónicos de la corriente de magnetización, todo ello integrado en valor eficaz.

### Saturación y Carga Real del Secundario

La carga real conectada al secundario (cables + relés + instrumentos) no debe superar la **carga nominal Sn**. Si se supera, el ALF efectivo se reduce según:

```
ALF_efectivo = ALF_nominal × (Sn + Zi) / (Sb + Zi)
```

Donde:
- **Sn**: carga nominal del TI (VA)
- **Sb**: carga real conectada (VA)
- **Zi**: impedancia interna del TI (VA equivalente)

**Ejemplo práctico:** Un TI 200/5 A, clase 5P20, Sn = 15 VA, Zi = 1 VA. Si la carga real es 20 VA (cables largos + relé numérico):

```
ALF_efectivo = 20 × (15 + 1) / (20 + 1) = 20 × 16/21 ≈ 15,2
```

El ALF efectivo cae de 20 a 15,2. Si la corriente de falta esperada es 18×In, el TI saturará antes de que el relé detecte correctamente la falta. La solución es reducir la resistencia de los cables secundarios (sección mínima recomendada: 4 mm² Cu para distancias > 10 m) o seleccionar un TI con mayor Sn o mayor ALF nominal.

---

## Transformadores de Tensión (TT): Tipos y Clases

Los TT reducen la tensión de red a valores normalizados de **100 V, 100/√3 V o 110/√3 V** en el secundario. IEC 61869-3 cubre los TT inductivos (electromagnéticos); IEC 61869-5 los capacitivos (CVT), utilizados en AT y MAT por sus ventajas económicas y de seguridad frente a ferrorresonancia.

### Clases de Exactitud para Medición

| Clase | Error de tensión máx. | Error de fase máx. (min) |
|-------|-----------------------|--------------------------|
| 0,1   | ±0,1 %                | ±5                       |
| 0,2   | ±0,2 %                | ±10                      |
| 0,5   | ±0,5 %                | ±20                      |
| 1     | ±1,0 %                | ±40                      |
| 3     | ±3,0 %                | no especificado          |

Los errores se garantizan entre el 80 % y el 120 % de la tensión nominal, y entre el 25 % y el 100 % de la carga nominal.

### Clases de Exactitud para Protección

| Clase | Error de tensión máx. | Factor de tensión | Tiempo (s) |
|-------|-----------------------|-------------------|------------|
| 3P    | ±3 %                  | 1,5 × Un / 1,9 × Un | continuo / 30 |
| 6P    | ±6 %                  | 1,5 × Un / 1,9 × Un | continuo / 30 |

El **factor de tensión** (IEC 61869-3, cláusula 5.3.4) define la tensión máxima que el TT puede soportar manteniendo su clase. En redes IT o con neutro impedante, donde la tensión de fase puede elevarse hasta 1,9 × Un durante una falta monofásica, debe seleccionarse el factor de tensión 1,9 con duración de 30 s mínimo.

---

## Criterios de Selección en Obra

### Para Transformadores de Corriente (TI)

1. **Definir la corriente primaria nominal** ajustada al 1,2–1,5 veces la corriente máxima de servicio. Un TI sobredimensionado opera en la zona no lineal de baja carga.
2. **Seleccionar la clase de medición** según la precisión del instrumento conectado:
   - Contador de facturación clase A (IEC 62053-11): requiere TI clase 0,2S
   - Analizador de red o vatímetro cuadro: clase 0,5 o 1
3. **Calcular la carga real** del secundario: suma de VA de relés, instrumentos y resistencia de los cables secundarios (R_cable = ρ × L / S, con ρ_Cu = 0,0175 Ω·mm²/m). Verificar que Sb ≤ Sn.
4. **Calcular el ALF efectivo** para los TI de protección y verificar que ALF_efectivo × In > Icc_min esperada en la barra.
5. **TI de doble núcleo** (uno para medición, otro para protección): evita el conflicto entre clase 0,5S (núcleo pequeño, saturación rápida) y clase 5P20 (núcleo grande, alto flujo de saturación).

### Para Transformadores de Tensión (TT)

1. **Tensión primaria**: debe coincidir con la tensión de fase o entre fases del sistema según esquema de conexión (estrella-tierra o triángulo abierto).
2. **Factor de tensión**: en redes con neutro sólido → 1,2 durante 30 s; en redes IT o con neutro impedante → 1,9 durante 30 s (IEC 61869-3, tabla 5).
3. **Carga nominal**: suma de VA de todos los instrumentos conectados al secundario, incluyendo cableado. No superar el 100 % de Sn para mantener la clase. No bajar del 25 % para evitar errores por carga excesivamente baja.
4. **Ferrorresonancia**: en redes MT con TT inductivos conectados entre fase y tierra en redes IT, verificar que la capacidad de fase a tierra del sistema (C0) sea suficientemente baja para evitar el fenómeno. Si existe riesgo, utilizar CVT según IEC 61869-5 o añadir resistencia de amortiguación en el secundario del TT abierto.

---

## Conclusión

La selección incorrecta de la clase de un TI o TT es un error que afecta a la facturación energética (pérdida de ingresos o sobrefacturación) o a la fiabilidad de las protecciones (disparo tardío o no disparo ante falta). Los puntos de control críticos son:

- **ALF efectivo** ≥ corriente de falta esperada / In (TI de protección)
- **Carga real** Sb ≤ Sn (ambos tipos)
- **Factor de tensión** acorde al tipo de red (TT de protección)
- **Clase S** cuando el factor de carga es inferior al 20 % de la corriente nominal (TI de medición)

IEC 61869-2 e IEC 61869-3, junto con UNE-EN 61869-2:2013 y UNE-EN 61869-3:2013 en transposición española, son las referencias normativas de aplicación directa en los proyectos de instalaciones de MT/BT en España.
