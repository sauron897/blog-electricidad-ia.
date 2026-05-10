---
title: "Cálculo de sección de cable eléctrico según ITC-BT-19"
description: "Procedimiento técnico para dimensionar conductores en BT: criterio térmico, caída de tensión y cortocircuito con fórmulas, tablas y ejemplo numérico. ITC-BT-19 y UNE-HD 60364-5-52."
pubDate: 2026-05-10
keywords: ["calculo seccion cable electrico", "ITC-BT-19 intensidades admisibles", "caida de tension formula cable", "UNE-HD 60364-5-52 secciones conductores"]
heroImage: /images/calculo-seccion-cable-electrico.png
author: "Editor"
---

Calcular la sección de un conductor no es elegir "el cable que se suele poner" ni aplicar una única fórmula. Es resolver tres criterios independientes y quedarse con la sección comercial más restrictiva. El REBT, en su **ITC-BT-19**, y la norma **UNE-HD 60364-5-52:2022** (que sustituyó definitivamente a UNE 20460-5-523) establecen el procedimiento obligatorio para instalaciones de baja tensión en España.

Ignorar alguno de los tres criterios no es una simplificación aceptable: puede resultar en un conductor que supera su temperatura máxima en régimen permanente, en una caída de tensión que degrada el par de arranque de un motor, o en un cable que funde antes de que la protección actúe ante un cortocircuito.

## Los tres criterios de selección de sección

El artículo 2 de ITC-BT-19 obliga a verificar simultáneamente:

1. **Criterio de intensidad máxima admisible (Iz)**: la corriente de servicio no puede superar la capacidad térmica del cable en sus condiciones reales de instalación.
2. **Criterio de caída de tensión (ΔU)**: la diferencia de tensión entre el origen de la instalación y el punto más lejano no puede superar los límites del REBT.
3. **Criterio de cortocircuito**: la sección debe soportar la energía específica pasante (I²·t) durante el tiempo de actuación de la protección.

La sección final es la mayor de las tres resultantes, redondeada al calibre comercial normalizado inmediatamente superior (1,5 / 2,5 / 4 / 6 / 10 / 16 / 25 / 35 / 50 mm²).

![Ilustración técnica: tres criterios de selección de sección](/images/calculo-seccion-cable-electrico-2.png)

---

## Criterio 1 — Intensidad máxima admisible (Iz)

### Tablas de referencia

Los valores base de intensidad admisible provienen de las tablas de la norma **UNE-HD 60364-5-52:2022**, referenciadas en la Guía Técnica ITC-BT-19. Los datos siguientes corresponden al **método B2** (cable multiconductor en tubo empotrado en pared), temperatura ambiente 40 °C, conductores de cobre:

| Sección (mm²) | PVC bipolar (A) | XLPE bipolar (A) | PVC tripolar (A) | XLPE tripolar (A) |
|:---:|:---:|:---:|:---:|:---:|
| 1,5 | 15 | 18 | 13 | 15 |
| 2,5 | 21 | 25 | 18 | 21 |
| 4 | 27 | 34 | 24 | 29 |
| 6 | 34 | 43 | 31 | 36 |
| 10 | 46 | 60 | 42 | 50 |
| 16 | 61 | 80 | 56 | 68 |
| 25 | 80 | 101 | 73 | 89 |
| 35 | 99 | 125 | 89 | 110 |
| 50 | 118 | 151 | 108 | 134 |

Para instalación al aire libre (**método E**), los valores son sensiblemente superiores: a 25 mm² XLPE tripolar → 131 A frente a 89 A en tubo empotrado. El método de instalación debe declararse en el proyecto y justificarse; no es intercambiable libremente.

### Factores de corrección

La corriente de servicio Ib debe cumplir: **Ib ≤ Iz_corr = Iz_base × kt × ka**

**Factor de temperatura (kt)** — tabla B.52.14 de UNE-HD 60364-5-52:

| Tª ambiente (°C) | kt PVC (70 °C máx.) | kt XLPE/EPR (90 °C máx.) |
|:---:|:---:|:---:|
| 25 | 1,08 | 1,05 |
| 35 | 1,04 | 1,02 |
| 40 | 1,00 | 1,00 |
| 45 | 0,96 | 0,98 |
| 50 | 0,91 | 0,95 |
| 60 | 0,82 | 0,89 |

**Factor de agrupamiento (ka)** — tabla B.52.17 (cables en contacto, sin separación):

| Circuitos agrupados | ka |
|:---:|:---:|
| 1 | 1,00 |
| 2 | 0,80 |
| 3 | 0,70 |
| 4–5 | 0,65 |
| 6–8 | 0,57 |
| 9–12 | 0,50 |

La revisión **2022** de la norma introdujo correcciones adicionales para bandejas de cables (tabla B.52.20). Con bandejas perforadas de múltiples circuitos, la diferencia respecto a tablas anteriores puede superar el 10 %, lo que afecta directamente al dimensionamiento en instalaciones industriales con gran densidad de cables.

---

## Criterio 2 — Caída de tensión

La ITC-BT-19 fija los límites máximos medidos desde el origen de la instalación interior hasta el punto más desfavorable:

- **Alumbrado**: ΔU ≤ 3 %
- **Fuerza (motores, tomas de uso general)**: ΔU ≤ 5 %

En instalaciones con generación propia (fotovoltaica, grupos electrógenos), el REBT permite distribuir el presupuesto total de caída de tensión entre tramos: hasta 1,5 % en la línea general de alimentación y el resto en la instalación interior.

### Fórmulas de cálculo

**Sistema monofásico o corriente continua:**

```
S_min (mm²) = (2 × L × I × cosφ) / (γ × ΔU_V)
```

**Sistema trifásico:**

```
S_min (mm²) = (√3 × L × I × cosφ) / (γ × ΔU_V)
```

Donde:
- **L** = longitud del circuito (m)
- **I** = corriente de diseño (A)
- **cosφ** = factor de potencia de la carga
- **γ** = conductividad del conductor (m/Ω·mm²):
  - Cobre a **70 °C** (aislamiento PVC): γ = **48 m/Ω·mm²**
  - Cobre a **90 °C** (aislamiento XLPE/EPR): γ = **44 m/Ω·mm²**
  - Aluminio a 70 °C: γ = 30 m/Ω·mm²
- **ΔU_V** = caída de tensión máxima admisible en voltios = (ΔU% / 100) × U_nominal

**Error frecuente en obra**: usar γ = 56 m/Ω·mm² (cobre a 20 °C) en lugar de la conductividad a temperatura de servicio. A 70 °C la conductividad del cobre cae un 14 %, lo que subestima la sección necesaria y provoca que la instalación termine con más caída de tensión de la proyectada.

---

## Criterio 3 — Sección mínima por cortocircuito

Este criterio garantiza que el conductor soporte la energía específica pasante (I²·t) durante el tiempo de actuación de la protección antes de fundir su aislamiento. La fórmula adiabática (válida para tiempos de cortocircuito menores de 5 s, según IEC 60364-4-43) es:

```
S_min (mm²) = (Icc × √t) / k
```

Donde:
- **Icc** = corriente de cortocircuito máxima en el punto de instalación (A)
- **t** = tiempo de actuación de la protección (s); para interruptores automáticos con disparo magnético, típicamente 0,01–0,02 s
- **k** = constante del conductor:
  - Cobre con aislamiento PVC: **k = 115**
  - Cobre con aislamiento XLPE/EPR: **k = 143**
  - Aluminio con PVC: k = 76

Este criterio es dominante en cabeceras de cuadro con Icc elevado (> 10 kA). En circuitos terminales a 230/400 V protegidos con magnetotérmicos de curva C o D, el criterio térmico o de caída de tensión suele resultar más restrictivo.

---

## Procedimiento completo: ejemplo numérico

**Datos del circuito:**
- Sistema trifásico 400 V
- Carga: motor de 11 kW, cosφ = 0,85, rendimiento η = 0,92
- Longitud: 35 m, instalación en tubo empotrado en pared (método B2)
- Aislamiento: PVC, temperatura ambiente 45 °C
- 3 circuitos agrupados en el mismo tubo
- Protección: interruptor automático 25 A curva C, Icc en el cuadro = 3 kA, tiempo de disparo magnético t = 0,02 s

**Paso 1 — Corriente de diseño:**

```
Ib = P / (√3 × U × cosφ × η) = 11000 / (1,732 × 400 × 0,85 × 0,92) = 20,3 A
```

**Paso 2 — Criterio térmico:**

Factores de corrección: kt (PVC, 45 °C) = 0,96 ; ka (3 circuitos agrupados) = 0,70

```
Iz_base_necesaria ≥ Ib / (kt × ka) = 20,3 / (0,96 × 0,70) = 30,2 A
```

Consultando la tabla ITC-BT-19, PVC tripolar en tubo (método B2):
- 4 mm² → 24 A ✗
- **6 mm² → 31 A ✓**

Sección por criterio térmico: **6 mm²**

**Paso 3 — Criterio caída de tensión (ΔU ≤ 5 %):**

```
ΔU_V_max = 5% × 400 V = 20 V
γ_PVC_70°C = 48 m/Ω·mm²

S_min = (√3 × 35 × 20,3 × 0,85) / (48 × 20) = 1046 / 960 = 1,09 mm²
```

Sección por criterio de caída de tensión: **1,09 mm²** → no es el criterio dominante.

**Paso 4 — Criterio cortocircuito:**

```
S_min = (3000 × √0,02) / 115 = (3000 × 0,141) / 115 = 424 / 115 = 3,7 mm²
```

Sección por criterio de cortocircuito: **3,7 mm²** → tampoco domina.

**Resultado final**: la sección más restrictiva es 6 mm² (criterio térmico). Sección comercial normalizada: **6 mm²**.

---

![Guía de selección de cable en obra](/images/calculo-seccion-cable-electrico-3.png)

## Criterios de selección en obra: guía de decisión rápida

| Situación | Criterio dominante habitual | Acción |
|---|---|---|
| Circuito largo, carga resistiva (calefacción) | Caída de tensión | Calcular S por ΔU; verificar Iz |
| Motor en arranque directo | Criterio térmico (Ib elevado) | Aplicar factores ka y kt; revisar sección comercial |
| Cabecera de cuadro, Icc > 10 kA | Cortocircuito | Calcular S adiabática; comparar con térmico |
| Cables agrupados en bandeja | Criterio térmico (ka < 1) | Verificar ka por tabla B.52.17/B.52.20 |
| Instalación en zona de alta temperatura (> 45 °C) | Criterio térmico (kt < 1) | Reducir Iz efectiva; subir sección |
| Cable de aluminio en sustitución de cobre | Criterio térmico y ΔU | Usar γ_Al = 30 m/Ω·mm² a 70 °C; sección típica +1 o +2 escalones |

En obra, el error más frecuente es resolver solo el criterio de caída de tensión y no verificar el térmico con los factores de corrección reales. Un cable de 6 mm² en tubo con cuatro circuitos agrupados (ka = 0,65) a 50 °C (kt = 0,91) tiene una Iz efectiva de solo 31 × 0,65 × 0,91 = **18,3 A**, muy por debajo de lo que podría parecer a primera vista.

## Normativa de referencia

- **REBT ITC-BT-19**: Instalaciones interiores o receptoras — prescripciones generales
- **UNE-HD 60364-5-52:2022**: Instalaciones eléctricas de baja tensión — selección e instalación de equipos eléctricos — canalizaciones
- **IEC 60364-4-43**: Protección contra sobreintensidades
- **Guía Técnica ITC-BT-19** (Ministerio de Industria): interpretación oficial con tablas de intensidades admisibles y factores de corrección
