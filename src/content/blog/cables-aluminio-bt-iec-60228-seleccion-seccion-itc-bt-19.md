---
title: "Cables de aluminio en BT: IEC 60228, secciones y selección vs cobre"
description: "Criterios técnicos para seleccionar cables de aluminio en instalaciones BT: resistividad, secciones equivalentes IEC 60228, intensidades ITC-BT-07, ITC-BT-19 y cuándo es viable frente al cobre."
pubDate: 2026-11-27
keywords: ["cables aluminio BT IEC 60228", "selección sección cable aluminio", "ITC-BT-19 aluminio cobre", "intensidad admisible aluminio IEC 60364-5-52", "cable XLPE aluminio instalacion industrial"]
author: "Editor"
---

El uso de conductores de aluminio en instalaciones de baja tensión es una decisión técnica y económica que el diseñador debe justificar con criterios cuantificables, no con intuición. La diferencia de resistividad entre cobre y aluminio determina directamente la sección equivalente, el peso del cableado y la caída de tensión resultante. Este artículo expone los parámetros clave según IEC 60228, IEC 60364-5-52 y el REBT (ITC-BT-07 e ITC-BT-19), con valores numéricos verificados contra la base de datos GElectrical.

## Parámetros eléctricos del conductor de aluminio: resistividad y reactancia

La diferencia fundamental entre cobre y aluminio como conductor es la resistividad a 20 °C:

| Material | Conductividad σ (m/Ω·mm²) | Resistividad ρ (Ω·mm²/m) |
|----------|--------------------------|--------------------------|
| Cobre    | 56                       | 0,01786                  |
| Aluminio | 35                       | 0,02857                  |

La relación ρ_Al / ρ_Cu = 1,60 tiene consecuencias directas:

**Resistencia por unidad de longitud:** Para igual sección, un conductor de aluminio tiene un 60 % más de resistencia que el de cobre. Para la misma resistencia lineal, la sección en aluminio debe ser 1,6 veces mayor que en cobre.

**Reactancia de cable:** La reactancia inductiva (Ω/km) no depende del material del conductor sino de la geometría del cable y el dieléctrico. Según la base de datos GElectrical (que implementa directamente IEC 60364-5-52):
- Cables XLPE/EPR aluminio monofásicos: X = 0,08 Ω/km (independientemente de la sección)
- Cables XLPE/EPR cobre: X = 0,08–0,10 Ω/km

Los cables PVC de cobre presentan X = 0,17 Ω/km por geometría de aislante distinta. En el cálculo de impedancia de bucle para secciones ≥ 95 mm² la reactancia empieza a ser significativa frente a la resistencia.

**Temperatura de trabajo:** Los cables con aislamiento XLPE/EPR trabajan a 90 °C de temperatura máxima en el conductor; los de PVC a 70 °C. El coeficiente de temperatura de la resistividad del aluminio es α = 0,004 K⁻¹, igual al del cobre, por lo que la corrección de resistencia a temperatura de operación se aplica con la misma fórmula:

R(T) = R₂₀ · [1 + α · (T − 20)]

A 90 °C: R(90) = R₂₀ · [1 + 0,004 · 70] = R₂₀ · 1,28

## Clases de conductor aluminio según IEC 60228 y designación de cables

La norma IEC 60228 (equivalente española: UNE EN 60228) clasifica los conductores en clases según su construcción:

| Clase IEC 60228 | Descripción | Uso típico |
|-----------------|-------------|------------|
| Clase 1 | Sólido (solid) | Cables de distribución enterrada, acometidas BT |
| Clase 2 | Cableado concéntrico, rígido | Cables de energía en instalaciones fijas |
| Clase 5 | Flexible, multifilar | No aplica para aluminio (mínimo clase 2) |

**El aluminio solo se usa en clases 1 y 2.** La norma no contempla aluminio clase 5 (flexible): la fragilidad mecánica y la oxidación superficial del aluminio hacen inviable su uso en conexiones flexibles sin tratamiento especial.

Denominaciones de cables de aluminio habituales en España:
- **A2XY / A2XWY**: aluminio, aislamiento XLPE, armadura, PVC exterior (0,6/1 kV) → instalaciones enterradas ITC-BT-07
- **A2XH / AL RZ1-K(AS)**: aluminio, XLPE, cubierta LSZH → preferido en instalaciones industriales con CPR Cca o superior
- **ACWU**: aluminio, aislamiento XLPE, armadura de alambre de acero ondulado → distribución en BT exterior

La designación "A" como prefijo en la denominación europea indica conductor de aluminio (p. ej., NA2XY en normativa alemana DIN VDE 0276).

## Intensidad admisible en cables de aluminio según IEC 60364-5-52 e ITC-BT-07/ITC-BT-19

La tabla siguiente compara las intensidades admisibles de cables tripolares XLPE (3 conductores con carga) en instalación al aire a 40 °C (método B2 según IEC 60364-5-52 / UNE-HD 60364-5-52). Temperatura máxima de conductor: 90 °C.

| Sección (mm²) | I_admisible Cu XLPE (A) | I_admisible Al XLPE (A) | Ratio Al/Cu |
|---------------|--------------------------|--------------------------|-------------|
| 16            | 110                      | 87                       | 0,79        |
| 25            | 136                      | 107                      | 0,79        |
| 35            | 164                      | 130                      | 0,79        |
| 50            | 196                      | 154                      | 0,79        |
| 70            | 245                      | 192                      | 0,78        |
| 95            | 294                      | 231                      | 0,79        |
| 120           | 338                      | 268                      | 0,79        |
| 150           | 385                      | 304                      | 0,79        |
| 185           | 440                      | 348                      | 0,79        |
| 240           | 514                      | 409                      | 0,80        |

El ratio constante de ~0,79 confirma la relación teórica: I_Al ≈ I_Cu · √(σ_Al/σ_Cu) = I_Cu · √(35/56) = I_Cu · 0,79.

**Restricciones normativas de sección mínima:**
- **ITC-BT-19** (instalaciones interiores): prohíbe aluminio en secciones inferiores a **16 mm²** para conductores activos. No se admite aluminio en circuitos de alumbrado ni en distribuciones de circuitos finales con sección < 16 mm².
- **ITC-BT-07** (redes subterráneas en BT): permite aluminio desde 16 mm², con la exigencia de que las terminaciones y empalmes se realicen con conectores bimetálicos homologados (par de apriete controlado según instrucciones del fabricante para evitar fluencia).
- **IEC 60364-5-52**: restringe el aluminio a secciones ≥ 16 mm² en instalaciones fijas.

## Criterios de selección: cuándo es viable el aluminio frente al cobre

La decisión cobre vs aluminio se reduce a cuatro criterios cuantificables:

**1. Coste por metro de circuito a igual intensidad transportada**

Para transportar la misma corriente, la sección de aluminio debe ser ≈ 1,6 veces la de cobre. Sin embargo, el coste por kg del aluminio es un 65–70 % menor que el del cobre (precios de mercado Metal Bulletin). Dado que la densidad del aluminio (2,7 g/cm³) es 3,3 veces menor que la del cobre (8,9 g/cm³):

Peso relativo: Al/Cu = (S_Al · ρ_peso_Al) / (S_Cu · ρ_peso_Cu) = (1,6 · 2,7) / (1 · 8,9) = 0,48

El cable de aluminio equivalente pesa un 48 % del de cobre. Combinado con el menor coste/kg, el aluminio resulta económico en líneas de distribución en BT con secciones ≥ 50 mm² y recorridos > 50 m.

**2. Caída de tensión para sección equivalente**

Para igual sección (no sección equivalente), la resistencia lineal del aluminio es 1,6 veces la del cobre, lo que se traduce directamente en mayor caída de tensión. Para cumplir el límite del 3 % (ITC-BT-19, circuitos de fuerza) o 5 % (distribución BT, ITC-BT-15) con aluminio, el diseñador debe recalcular:

ΔU (%) = (√3 · I · L · R_Al) / V_n · 100

donde R_Al = ρ_Al / S_Al (Ω/m). Si se parte de la sección mínima admisible de 16 mm², la resistencia lineal es R_Al = 0,02857 / 16 × 10³ = 1,786 mΩ/m frente a R_Cu = 1,116 mΩ/m para 10 mm² de cobre (el equivalente habitual).

**3. Conexiones y terminaciones: punto crítico**

El aluminio oxida superficialmente generando Al₂O₃ (alúmina), capa no conductora. Todo conector en aluminio debe:
- Usar **conectores homologados para aluminio o bimetálicos Cu/Al** (cumplimiento UNE-EN 61238-1 para compresión o UNE-EN 61238-1 para tornillo)
- Aplicar **pasta inhibidora de oxidación** en la preparación del extremo antes del apriete
- Verificar el **par de apriete** según ficha técnica del conector: el aluminio fluye (creep) bajo presión constante, provocando aflojamiento del conector a lo largo del tiempo

Este punto hace inviable el aluminio en cuadros eléctricos con clema estándar y en circuitos con cambios frecuentes de conductor.

**4. Temperatura de cortocircuito (criterio adiabático)**

La temperatura máxima admisible en cortocircuito para el aislamiento XLPE es 250 °C (IEC 60364-4-43, Tabla 43A). La sección mínima adiabática se calcula con:

S_min (mm²) = I_cc · √t_cc / k

Donde k_Cu = 143 (conductor de cobre, XLPE, temperatura inicial 90 °C) y k_Al = 94 (conductor de aluminio, XLPE). El valor de k_Al es un 34 % menor que k_Cu, lo que exige una sección de aluminio proporcionalmente mayor para la misma energía de falta:

S_Al = S_Cu · (k_Cu / k_Al) = S_Cu · (143 / 94) = S_Cu · 1,52

Esto implica que, en circuitos con alta corriente de cortocircuito (Icc > 10 kA), el criterio adiabático suele determinar la sección mínima en aluminio y puede neutralizar el ahorro económico.

## Tabla de equivalencias de sección Cu–Al normalizadas IEC 60228

| Sección Cu (mm²) | Sección Al equivalente (mm²) | Sección Al normalizada IEC 60228 |
|------------------|------------------------------|----------------------------------|
| 10               | 16                           | 16 (mínimo normativo)            |
| 16               | 25                           | 25                               |
| 25               | 35                           | 35                               |
| 35               | 50                           | 50                               |
| 50               | 70                           | 70                               |
| 70               | 95–120                       | 95                               |
| 95               | 150                          | 150                              |
| 120              | 185                          | 185                              |
| 150              | 240                          | 240                              |

Las secciones normalizadas de aluminio en IEC 60228 son las mismas series que el cobre: 16, 25, 35, 50, 70, 95, 120, 150, 185, 240, 300 mm².

## Conclusión

El aluminio es una opción técnica válida en BT para líneas de distribución y acometidas industriales con sección ≥ 50 mm², recorridos > 50 m y sin restricciones de espacio en bandeja o tubo (el diámetro exterior del cable de aluminio equivalente es mayor). La decisión debe basarse en cuatro cálculos: sección por criterio térmico (IEC 60364-5-52), sección por caída de tensión (ITC-BT-19), sección por criterio adiabático (IEC 60364-4-43, con k_Al = 94) y verificación de terminaciones (UNE-EN 61238-1). En cuadros eléctricos y circuitos de control con conexiones frecuentes, el cobre sigue siendo obligado.
