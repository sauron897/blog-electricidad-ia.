---
title: "Corriente de fuga capacitiva en variadores: diferencial tipo B"
description: "Diferencial tipo B según IEC 62423 para variadores de frecuencia: por qué los tipos AC y A fallan, cómo calcular la corriente de fuga y criterios de selección en obra."
pubDate: 2026-08-03
keywords: ["corriente fuga capacitiva variador frecuencia diferencial tipo B", "IEC 62423", "diferencial tipo B variador", "protección diferencial variador velocidad", "UNE-EN 62423"]
author: "Editor"
heroImage: /images/corriente-fuga-capacitiva-variador-frecuencia-diferencial-tipo-b.svg
---

## Por qué los variadores de frecuencia generan corriente de fuga capacitiva

Un variador de frecuencia (VFD) convierte la red AC en CC mediante un puente rectificador y después genera una tensión AC sintetizada mediante modulación PWM a través de IGBTs. La frecuencia de conmutación de estos IGBTs oscila habitualmente entre 2 kHz y 16 kHz, con frentes de tensión (dV/dt) del orden de 1–10 kV/µs en la salida.

![Ilustración técnica](/images/corriente-fuga-capacitiva-variador-frecuencia-diferencial-tipo-b-2.svg)

Esos transitorios de tensión a alta frecuencia atraviesan las capacidades parásitas presentes en la instalación y generan corrientes de fuga a tierra que siguen la relación fundamental:

```
I_fuga = C_tierra × (dV/dt)
```

Las principales fuentes de capacitancia a tierra son dos:

- **Condensadores del filtro CEM/RFI** integrados en el propio variador, conectados entre fase y PE para cumplir la directiva de compatibilidad electromagnética (EN 61800-3). En variadores de 15 kW con filtro CEM integrado, estos condensadores pueden sumar 1–5 µF, generando corrientes de fuga de 50–300 mA en condiciones normales de funcionamiento.
- **Capacidades parásitas cable–PE** en el cable de motor (especialmente en cables apantallados o en bandeja metálica). Un cable de 4×6 mm² en bandeja presenta típicamente 0,3–0,5 nF/m. Con 50 m de cable y dV/dt de 5 kV/µs, la corriente de fuga aportada por el cable alcanza 75–125 mA pico.

La corriente de fuga resultante no es sinusoidal a 50 Hz. Tiene tres componentes:
1. **Alta frecuencia AC** (2–16 kHz, componente dominante)
2. **Componente continua alisada** generada por asimetría del puente rectificador (puede llegar a 10–50 mA DC)
3. **CC pulsante** a la frecuencia del ripple del bus DC

Esta combinación es la razón por la que los diferenciales convencionales tipo AC y tipo A **no sirven** para proteger circuitos con variadores de frecuencia.

---

## Tabla comparativa: tipos de diferencial y su respuesta a variadores

| Tipo | Norma | Formas de onda detectadas | ¿Válido con VFD? |
|------|-------|--------------------------|-----------------|
| **AC** | IEC 61008-1 | Solo AC sinusoidal 50/60 Hz | No |
| **A** | IEC 61008-1 | AC sinusoidal + CC pulsante (media onda) | No |
| **F** | IEC 61008-2 | AC sinusoidal + CC pulsante + alta frecuencia hasta 1 kHz | Solo VFDs monofásicos de gama baja |
| **B** | IEC 62423 | AC + CC pulsante + **CC alisada** + alta frecuencia hasta ~1 kHz | Sí, solución general para VFDs trifásicos |
| **B+** | IEC 62423 Amdt.1 | Todo lo anterior + alta frecuencia hasta varios kHz | Sí, para VFDs con fc > 4 kHz |

El diferencial tipo AC detecta únicamente corriente de fuga sinusoidal a 50 Hz. La componente de alta frecuencia y la CC alisada generada por el variador pasan sin ser detectadas, con lo que el diferencial **no protege al usuario** en caso de contacto indirecto con componentes del variador que tengan defecto a tierra.

El tipo A añade respuesta a la CC pulsante (semiciclo positivo), pero sigue siendo ciego a la CC alisada. En presencia de tan solo 6 mA de CC alisada, IEC 61008-1 permite que el umbral de disparo de un diferencial tipo A suba hasta **el doble de su I_Δn nominal**, lo que en la práctica puede impedir el disparo ante una corriente de fuga de persona de 30 mA.

---

## La norma IEC 62423 y su aplicación en España

La protección diferencial tipo B está regulada por **IEC 62423** (ed. 1, 2007), adoptada en España como **UNE-EN 62423:2010**. La norma define los requisitos de disparo del diferencial ante:

- Corriente AC pura de 50 Hz: disparo al alcanzar I_Δn (típico 30 mA o 300 mA)
- Corriente CC pulsante: disparo con hasta 6 mA de CC superpuesta
- Corriente CC alisada: disparo ante corriente DC de hasta **0,4 × I_Δn** (mínimo 10 mA)
- Alta frecuencia: respuesta garantizada al menos hasta 1 kHz

El punto crítico es la CC alisada: el tipo B debe disparar ante **10 mA de CC continua**, condición que los tipos AC y A son incapaces de cumplir estructuralmente porque sus toroidales de medida no tienen núcleo adecuado para DC.

La **ITC-BT-24 del REBT** establece la obligatoriedad de protección diferencial en circuitos de utilización de instalaciones de BT accesibles a personas. En instalaciones industriales con variadores, la interpretación correcta de esta ITC implica que el diferencial instalado debe ser apto para las corrientes de falta que puedan aparecer, lo que obliga a usar tipo B cuando el variador genera componente continua.

---

## Cálculo de la corriente de fuga y selección de I_Δn

### Estimación de la corriente de fuga total

La corriente de fuga total de la instalación se puede estimar como:

```
I_fuga_total = I_fuga_variador + I_fuga_cable

I_fuga_cable ≈ (U × C_cable × L × 2π × fc) / √3

Donde:
  U    = tensión de fase a tierra (230 V en red 400 V TN)
  C    = capacitancia específica cable-PE (nF/m), típico 0,3–0,5 nF/m para RV-K apantallado
  L    = longitud del cable de motor (m)
  fc   = frecuencia de conmutación IGBT (Hz)
```

**Ejemplo práctico**: variador 11 kW con filtro CEM integrado (I_fuga_variador = 80 mA especificada en datasheet), cable de motor RV-K 4×4 mm² apantallado de 30 m (C ≈ 0,4 nF/m, fc = 8 kHz):

```
I_fuga_cable = (230 × 0,4×10⁻⁹ × 30 × 2π × 8000) / √3
             = (230 × 0,4×10⁻⁹ × 30 × 50265) / 1,732
             ≈ (230 × 6,03×10⁻⁴) / 1,732
             ≈ 80 mA

I_fuga_total ≈ 80 + 80 = 160 mA (valor típico de operación normal)
```

Con 160 mA de corriente de fuga permanente en operación normal, un diferencial de 30 mA **dispararía falsamente** en cada arranque del variador. Por eso la selección de I_Δn no es trivial.

### Criterio de selección de I_Δn

La regla general (derivada de IEC 60364-4-41 y las recomendaciones de fabricantes) es:

```
I_Δn ≥ 3 × I_fuga_total_operación_normal
```

Aplicando al ejemplo anterior: I_Δn ≥ 3 × 160 mA = 480 mA → se seleccionaría **diferencial tipo B de 500 mA o 1 A**.

En este caso la protección de personas se garantiza mediante **selectividad**: el diferencial tipo B de 500 mA o 1 A en el cuadro del variador actúa como protección de backup, mientras que un diferencial general de 30 mA en cabecera proporciona la sensibilidad requerida para protección personal en el resto de la instalación. Esta coordinación debe verificarse con el estudio de selectividad tal como se describió en el post sobre selectividad diferencial tipo S.

---

![Guía de selección](/images/corriente-fuga-capacitiva-variador-frecuencia-diferencial-tipo-b-3.svg)

## Criterios de selección en obra

**1. Identifica la fuente de corriente de fuga**

Consulta el datasheet del variador. Los fabricantes (Schneider Electric, ABB, Siemens, Danfoss) especifican la corriente de fuga con y sin filtro CEM. Un variador ATV320 de 15 kW con filtro CEM integrado puede especificar 280 mA de corriente de fuga a tierra en condiciones nominales.

**2. Determina si hay componente DC**

Si el variador es trifásico (lo habitual en industria), necesitas tipo B. Si es monofásico de baja potencia con rectificador de media onda, el tipo F puede ser suficiente.

**3. Calcula I_fuga total** incluyendo cable de motor, variando con longitud y fc.

**4. Aplica el factor de seguridad ×3** y elige el escalón normalizado inmediatamente superior: 300 mA, 500 mA, 1 A, 3 A.

**5. Evalúa si instalar filtro CEM externo** puede reducir la corriente de fuga del variador y permitir bajar un escalón de I_Δn. Un filtro externo correctamente dimensionado puede reducir I_fuga hasta un 60–70%.

**6. Considera el monitor de corriente de fuga (RCM)** según **IEC 62020** como alternativa cuando el proceso no permite disparos no programados. El RCM detecta la corriente de fuga y alarma antes de que alcance el umbral de disparo, permitiendo actuar preventivamente sin cortar el proceso.

---

## Alternativas cuando el tipo B no está disponible o es inviable

En algunas instalaciones antiguas o con presupuesto restringido:

- **Transformador de aislamiento** (IT) entre la red y el variador: elimina el camino de retorno de la corriente de fuga a tierra, permitiendo usar diferencial AC convencional aguas arriba. Válido solo si se instala un monitor de aislamiento.
- **Omisión del filtro CEM** en aplicaciones donde la compatibilidad electromagnética no es crítica: reduce I_fuga del variador hasta 3–5 mA, pero puede incumplir EN 61800-3 para entornos residenciales y comerciales.
- **Cableado no apantallado** en recorridos cortos (< 10 m): reduce I_fuga_cable, aunque puede crear problemas de EMC.

---

## Conclusión

La corriente de fuga capacitiva generada por variadores de frecuencia tiene componentes —CC alisada, CC pulsante, alta frecuencia— que los diferenciales AC y A no detectan. Usar tipo AC o A en la línea de alimentación de un VFD trifásico no cumple los requisitos de protección de la **ITC-BT-24 del REBT** ni de **IEC 60364-4-41**, aunque el dispositivo esté correctamente calibrado.

El técnico en obra debe:
1. Consultar el datasheet del variador para la corriente de fuga especificada.
2. Calcular la aportación del cable de motor (capacitancia, longitud, frecuencia de conmutación).
3. Seleccionar tipo B de sensibilidad I_Δn = 3 × I_fuga_total_operación.
4. Verificar la selectividad con el diferencial de cabecera.
5. Documentar en el proyecto eléctrico la justificación de la elección conforme a UNE-EN 62423 y IEC 60364-5-53.

El error más frecuente en instalaciones industriales modernizadas es mantener el diferencial tipo A original cuando se instala un variador en un motor existente. Ese diferencial no protege: puede dispararse falsamente (si la corriente de fuga supera I_Δn × 0,5) o no dispararse ante un defecto real (si la corriente de falta tiene componente DC). La solución es siempre sustituirlo por tipo B correctamente dimensionado.
