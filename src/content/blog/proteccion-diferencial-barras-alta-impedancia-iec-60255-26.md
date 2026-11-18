---
title: "Protección diferencial alta impedancia en barras MT: ajuste y selectividad"
description: "Ajuste de la protección diferencial de alta impedancia en barras MT: tensión de estabilización, Metrosil, selectividad y criterios de selección según IEC 60255-186 e IEC 60255-26."
pubDate: 2026-11-18
keywords: ["protección diferencial barras alta impedancia IEC 60255-26", "busbar differential protection", "tensión estabilización diferencial barras", "protección barras MT selectividad"]
author: "Editor"
---

La protección diferencial de barras colectoras en media tensión es, junto con la protección de transformador, el esquema donde la velocidad de actuación tiene más impacto en la integridad de la subestación. Una falta en barras sin evacuar en menos de 100 ms puede destruir un juego de barras MT de 20 kV y dañar toda la aparamenta del cuadro. La protección diferencial de alta impedancia (High-Impedance Differential, HiZ) ofrece actuaciones por debajo de 20–30 ms con una selectividad intrínseca que no depende de comunicaciones entre IED. Este artículo detalla los fundamentos del ajuste, el cálculo de la tensión de estabilización y los criterios de selección frente a la alternativa de baja impedancia numérica.

---

## Principio de operación y por qué se diferencia del esquema de baja impedancia

El esquema HiZ conecta todos los secundarios de los TC de cada vano en paralelo y conecta ese nodo al relé a través de una resistencia estabilizadora de alto valor (típicamente 100–600 Ω). La tensión desarrollada en esa resistencia es la señal de medida.

**Estabilidad ante falta externa con saturación de TC**: en una falta externa en un vano, la corriente entera fluye desde la barra hacia la falta a través de un solo TC. Si ese TC se satura, su impedancia vista desde el circuito secundario cae aproximadamente al valor de su resistencia de devanado (R_ct). La corriente de saturación circula entonces por el lazo formado por el TC saturado y los demás TC en paralelo. Con el relé de alta impedancia, la resistencia estabilizadora impide que esa corriente de error supere la tensión de pickup: el esquema es inherentemente estable sin necesidad de calcular márgenes de inhibición por gradiente como en la protección diferencial de baja impedancia numérica.

En la protección de baja impedancia (Low-Impedance, LoZ, como ABB REB650 en modo baja impedancia o Siemens 7SS85), el IED mide las corrientes de cada TC individualmente y aplica un algoritmo de inhibición por segundo armónico y por pendiente diferencial para distinguir falta interna de saturación. Es más flexible topológicamente pero requiere comunicación de fibra entre los TC remotos y el IED central, y su ajuste involucra varias zonas con sus propias pendientes (típicamente SLOPE1 y SLOPE2 según IEC 60255-186:2024).

---

## Cálculo de la tensión de estabilización V_s

La tensión de estabilización es el parámetro de ajuste crítico del esquema HiZ. Su cálculo se basa en la condición de falta externa con máxima corriente de cortocircuito y peor saturación del TC del vano afectado.

**Fórmula general (IEC 60255-186 / BS PD 48009):**

```
V_s = I_f_max × (R_ct + 2 × R_L)
```

Donde:
- **I_f_max**: corriente máxima de cortocircuito en el punto de falta externa [A secundario]. Se obtiene dividiendo la Icc trifásica entre la relación de transformación del TC.
- **R_ct**: resistencia del devanado secundario del TC más distante o del de mayor R_ct [Ω]. Para TC de clase P según IEC 61869-2, el límite es el ALF × (R_ct + R_burden) ≤ V_knee.
- **R_L**: resistencia del conductor de piloto desde el TC hasta el relé, ida [Ω]. Se calcula como ρ × L / S con ρ = 0,0175 Ω·mm²/m para Cu a 75 °C.

**Ejemplo numérico típico en subestación MT 20 kV:**

| Parámetro | Valor |
|-----------|-------|
| Icc trifásica en barras | 16 kA |
| Relación de transformación TC | 400/5 A (factor 80) |
| I_f_max (secundario) | 16000 / 80 = 200 A |
| R_ct (TC más desfavorable) | 1,8 Ω |
| R_L (piloto 150 m, 2,5 mm² Cu) | 0,0175 × 150 / 2,5 = 1,05 Ω |
| **V_s calculada** | 200 × (1,8 + 2×1,05) = **778 V** |

El relé se ajusta a **V_set ≥ V_s × 1,05** (margen del 5 % mínimo). En este caso: V_set = 817 V. Los relés HiZ de Schneider (MiCOM P721/P723) y SEL (SEL-HZM) tienen rangos de ajuste típicos de 50 V a 1200 V en pasos de 1 V o por potenciómetro.

**Verificación de sensibilidad mínima**: La corriente de falta interna mínima detectable viene determinada por:

```
I_op_min = (I_mag_total + I_metrosil(V_set)) × (N_TC)
```

Donde I_mag_total es la suma de corrientes de magnetización de todos los TC en paralelo a la tensión V_set, e I_metrosil(V_set) es la corriente absorbida por el varistor a esa tensión (leída de la curva del Metrosil). Para una subestación con 6 vanos y TC de clase 5P20, la I_op_min típica resulta en 100–200 A primario, muy por debajo de la Icc mínima en barras.

---

## Metrosil (varistor): selección y energía absorbida

La resistencia estabilizadora forma un circuito resonante con la inductancia de los TC ante una falta interna. Las tensiones de pico pueden superar los 3–5 kV, poniendo en riesgo el aislamiento de los pilotos y el propio relé. El Metrosil (Metal Oxide Varistor, MOV, en nomenclatura GE/Alstom) o resistor no lineal se conecta en paralelo con el circuito del relé para limitar esta tensión.

**Criterio de selección del Metrosil según IEC 60255-26 (requisitos EMC del relé):**

La norma IEC 60255-26:2013 establece los niveles de rigidez dieléctrica y los ensayos de impulso que el relé debe superar. El varistor garantiza que la tensión transitoria en bornes del relé quede dentro de los límites de la clase de instalación. Para instalaciones MT clase III (IEC 61000-4-5), la tensión de cresta no debe superar 2 kV en las entradas de medida.

La energía que debe absorber el Metrosil durante una falta:

```
E_metrosil = V_pico² / (2 × R_metrosil_efectivo) × t_falta
```

Con t_falta = 100 ms (tiempo de eliminación del relé + interruptor), V_pico = 3×V_s y R_metrosil_efectivo leído de la curva de fabricante, resultan energías de 50–300 J para configuraciones típicas en 20 kV. Alstom/Schneider ofrece el Metrosil C142B (200 V_set máx.) y C142D (350 V_set máx.) como variantes estándar para su rango P72x.

---

## Comparativa: alta impedancia vs. baja impedancia numérica

| Criterio | Alta impedancia (HiZ) | Baja impedancia numérica (LoZ) |
|---|---|---|
| **Tiempo de actuación** | 10–25 ms | 15–50 ms |
| **TC requeridos** | Todos idéntica relación y clase | Diferentes relaciones admisibles (IED los normaliza) |
| **Adaptabilidad a cambios de topología** | Baja (recablear secundarios) | Alta (configuración software) |
| **Zonas de protección** | 1 zona fija | 1–8 zonas (seccionador de barra) |
| **Comunicación entre IED** | No requerida | Sí (GOOSE IEC 61850 en LoZ moderno) |
| **Coste de ingeniería** | Bajo (cálculo directo) | Medio-alto (parametrización IED) |
| **Mantenimiento de TC** | Crítico (R_ct y V_knee deben mantenerse) | Verificación periódica de fibra y IED |
| **Norma de ajuste aplicable** | IEC 60255-186, BS PD 48009 | IEC 60255-186:2024 §6.4 (LoZ) |

La elección HiZ es estándar en subestaciones con barra simple o barra con seccionador único, con topología fija y hasta 8–10 vanos. Para subestaciones con interruptor de acoplamiento, barras dobles o transferencia por barra de bypass, el esquema LoZ numérico es obligatorio por su capacidad de reconfiguración dinámica de zonas.

---

## Criterios de ajuste y selectividad en obra

La selectividad de la protección diferencial de barras HiZ es intrínseca al principio de operación (no existe zona de actuación fuera de los TC conectados al esquema), pero los siguientes criterios son determinantes para garantizar el correcto funcionamiento en servicio:

**1. Homogeneidad de los TC**: todos los TC del esquema deben tener la misma relación de transformación y clase equivalente. La discrepancia de R_ct entre TC aumenta la tensión diferencial ante falta externa y puede reducir el margen de estabilidad. Verificar R_ct con ohmímetro Kelvin en comisionado; tolerancia ≤ ±5 % respecto al valor nominal de placa.

**2. Conexión de los TC**: polaridad aditiva de todos los secundarios apuntando hacia las barras (corriente entrante positiva). Un TC con polaridad invertida convierte la falta externa en falta interna para el relé.

**3. Apertura del circuito secundario**: en esquemas HiZ, si el circuito secundario de un TC se abre con la barra energizada, la tensión inducida puede superar 1 kV y dañar el aislamiento. Interbloqueos de protección (IEC 61869-2 §7.2.9) deben impedir la apertura sin cortocircuitar previamente el TC.

**4. Verificación de V_knee**: la tensión de rodilla del TC (V_k) debe cumplir V_k ≥ 2 × V_s para garantizar que el TC no satura antes de que la tensión alcance el nivel de pickup. Esta relación se verifica con curva de excitación (prueba de magnetización) según IEC 61869-2 Anexo B.

**5. Ajuste del umbral de corriente de pickup**: el relé HiZ mide en tensión. El umbral I_set en corriente primaria equivalente se calcula como: I_set = V_set / R_estabilizadora × (N_TC). Se recomienda I_set no inferior a 20 % de la corriente nominal de la barra para evitar disparos por desequilibrios de carga.

**6. Ensayo de puesta en servicio**: inyección de corriente en un TC a la vez con la barra en servicio para verificar polaridades y ausencia de disparo (prueba de estabilidad). Posteriormente, inyección desde ambos lados de un vano para verificar actuación (prueba de operación).

---

## Conclusión

La protección diferencial de alta impedancia para barras MT combina simplicidad de ajuste, velocidad de actuación sub-ciclo y robustez ante saturación de TC con la condición de que todos los TC del esquema sean homogéneos y el circuito piloto esté bien mantenido. El parámetro central es la tensión de estabilización V_s, calculada con la Icc máxima del lado secundario y la resistencia de los conductores de piloto; el Metrosil protege al relé de los transitorios de falta interna. Para subestaciones con topologías cambiantes, la protección LoZ numérica con GOOSE IEC 61850 ofrece mayor flexibilidad a costa de mayor complejidad en la ingeniería de ajuste. La elección debe basarse en la topología de barras, el número de vanos, la vida útil prevista de la instalación y la disponibilidad de personal técnico cualificado para el mantenimiento.
