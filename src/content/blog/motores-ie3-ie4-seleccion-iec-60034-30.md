---
title: "Motores IE3 e IE4: selección según IEC 60034-30-1 y ahorro energético"
description: "Guía técnica de clases IE1-IE4 según IEC 60034-30-1 y Reglamento EU 2019/1781: tablas de eficiencia verificadas, cálculo de ahorro y criterios de selección en obra."
pubDate: 2026-09-20
keywords: ["motores IE3 IE4 eficiencia IEC 60034", "IEC 60034-30-1", "eficiencia motores trifasicos", "Reglamento EU 2019/1781 motores"]
author: "Editor"
---

## Clases de eficiencia IE1-IE4: marco normativo IEC 60034-30-1

La norma **IEC 60034-30-1:2014** define cinco clases de eficiencia energética para motores trifásicos de jaula de ardilla de CA, aplicable al rango 0,12 kW – 1000 kW, 50/60 Hz:

| Clase | Denominación              | Situación regulatoria (EU 2019/1781)        |
|-------|---------------------------|---------------------------------------------|
| IE1   | Standard Efficiency       | Prohibido para uso general desde julio 2021 |
| IE2   | High Efficiency           | Admitido solo con VFD como solución equiv.  |
| IE3   | Premium Efficiency        | Obligatorio 0,75-1000 kW desde julio 2021   |
| IE4   | Super Premium Efficiency  | Obligatorio 75-200 kW desde julio 2023      |
| IE5   | Ultra Premium Efficiency  | Sin obligatoriedad reglamentaria aún        |

La fuente regulatoria vigente en Europa es el **Reglamento Delegado EU 2019/1781** (que derogó el Reglamento 640/2009): exige IE3 como clase mínima para motores de uso general desde el 1 de julio de 2021, y eleva la exigencia a IE4 para el rango 75-200 kW desde el 1 de julio de 2023. Las excepciones IE2 están restringidas a motores accionados exclusivamente por variador de frecuencia (VFD), documentado en la declaración de conformidad del fabricante.

## Pérdidas internas en el motor de inducción: fundamento físico

El rendimiento η de un motor de inducción es:

**η = P_útil / P_abs = P_útil / (P_útil + ΣPérdidas)**

En un motor de 4 polos (1500 rpm a 50 Hz) a plena carga, las pérdidas se desglosan aproximadamente:

- **Pérdidas en el cobre del estátor (PCu1 = I₁² · R₁):** 30-40% del total. Para un motor de 22 kW con corriente nominal I₁ ≈ 44 A y R₁ ≈ 0,5 Ω: PCu1 ≈ 968 W.
- **Pérdidas en el hierro (PFe):** histéresis (∝ f · B^1,6) y corrientes de Foucault (∝ f² · B²) en el núcleo magnético. Representan el 15-25% del total; en motores IE3 se reduce con acero eléctrico de baja pérdida (M270-35A o mejor).
- **Pérdidas en el cobre del rotor (PCu2 = s · P_e.m.):** función del deslizamiento s = (ns − n)/ns. En régimen nominal s ≈ 0,02-0,04 para motores 4P. Para 22 kW: PCu2 ≈ 200-350 W.
- **Pérdidas mecánicas (Pmec):** rozamiento en cojinetes y ventilación forzada. 5-10% del total.
- **Pérdidas adicionales (Padd, stray losses):** inducidas por armónicos de ranura y flujos parásitos. IEC 60034-2-1:2014 define el método de ensayo para su determinación, usualmente estimadas en 0,5-1,5% de P_útil.

La mejora de IE1 a IE3 actúa sobre PCu1 (mayor sección de devanado o menor resistividad por aluminio vs. cobre) y sobre PFe (acero magnético de mayor calidad). El deslizamiento también se reduce ligeramente, lo que reduce PCu2.

## Tabla de eficiencia IEC 60034-30-1: valores verificados para motores 4P (1500 rpm)

Los valores siguientes corresponden a los datos normalizados IEC, verificados contra la base de datos GElectrical (implementación directa de IEC 60034-30-1):

| Potencia (kW) | IE1 η (%) | IE2 η (%) | IE3 η (%) | Δη IE1→IE3 (pp) |
|---------------|-----------|-----------|-----------|------------------|
| 7,5           | 86,0      | 88,7      | 90,4      | +4,4             |
| 11            | 87,6      | 89,8      | 91,4      | +3,8             |
| 15            | 88,7      | 90,6      | 92,1      | +3,4             |
| 22            | 89,9      | 91,6      | 93,0      | +3,1             |
| 30            | 90,7      | 92,3      | 93,6      | +2,9             |
| 37            | 91,2      | 92,7      | 93,9      | +2,7             |
| 55            | 92,1      | 93,5      | 94,6      | +2,5             |
| 75            | 92,7      | 94,0      | 95,0      | +2,3             |

*Fuente: GElectrical/IEC 60034-30-1 — base de datos verificada, motores 4P 50 Hz.*

Los valores IE4 no están incluidos en GElectrical; los valores típicos de catálogo para 22 kW son η ≈ 94,0% y para 75 kW η ≈ 96,0% (Siemens SIMOTICS SD IE4, ABB IE4 series), lo que supone un escalón adicional de 1,0-1,5 pp sobre IE3.

## Cálculo del ahorro energético y periodo de retorno

La potencia absorbida en función del rendimiento es:

**P_abs = P_útil / η**

**Ejemplo: motor de 22 kW, 6000 h/año de operación continua (régimen S1)**

Motor IE1 (η = 89,9 %):
- P_abs(IE1) = 22 / 0,899 = **24,47 kW**
- Energía anual = 24,47 × 6000 = **146 820 kWh/año**

Motor IE3 (η = 93,0 %):
- P_abs(IE3) = 22 / 0,930 = **23,66 kW**
- Energía anual = 23,66 × 6000 = **141 935 kWh/año**

**Ahorro anual de energía:** ΔE = 146 820 − 141 935 = **4 885 kWh/año**

A tarifa industrial de 0,12 €/kWh (valor medio España 2024):
**Ahorro económico ≈ 586 €/año**

El sobrecoste típico del motor IE3 sobre IE1 es de **300-500 €** para este rango, lo que arroja un **periodo de retorno inferior a 1 año**.

Fórmula general para el ahorro de potencia al sustituir IE1 por IE3:

**ΔP = P_útil × (1/η_IE1 − 1/η_IE3)**

Para 22 kW: ΔP = 22 × (1/0,899 − 1/0,930) = 22 × (1,1124 − 1,0753) = **0,816 kW**

Esta metodología es coherente con los procedimientos de cálculo de inversiones en eficiencia energética de **UNE-EN ISO 50001:2018** (sistemas de gestión de la energía industrial).

## Criterios de selección en obra

### 1. Cumplimiento del Reglamento EU 2019/1781

- Motores 0,75-1000 kW de uso general → **IE3 mínimo** (desde julio 2021)
- Motores 75-200 kW sin excepción → **IE4 mínimo** (desde julio 2023)
- Motor IE2 solo admitido cuando se instale exclusivamente con VFD y quede documentado en la declaración de conformidad
- Motores para aplicaciones específicas excluidas (motores sumergibles, motores de frenado integrado, motores para grúas ≤ 3 Hz) pueden quedar fuera del alcance; verificar Anexo I del Reglamento

### 2. Régimen de carga y horas de operación

| Régimen de carga           | Horas anuales  | Clase recomendada      |
|----------------------------|----------------|------------------------|
| Continua plena carga (S1)  | > 6000 h       | IE4 (o IE3 + VFD)      |
| Continua carga variable    | 4000-6000 h    | IE3 + VFD (ahorro add.)|
| Intermitente (S3/S4)       | 2000-4000 h    | IE3                    |
| Arranque infrecuente       | < 2000 h       | IE3 (obligatorio)      |

### 3. Compatibilidad con variador de frecuencia (VFD)

Los motores IE3 para accionamiento con VFD deben cumplir **IEC 60034-17**: aislamiento del devanado de Clase F o H (resistente a picos de tensión dU/dt hasta 1600 V/μs en cable ≤ 10 m), y rodamientos aislados o con anillo de cortocircuito para motores > 22 kW (corrientes inducidas por alta frecuencia de conmutación PWM). No todos los IE3 del mercado incluyen estos refuerzos de serie; verificar en la hoja técnica del fabricante el marcado "Inverter Duty" o "VFD Ready".

### 4. Clase de aislamiento y factor de servicio

Según IEC 60034-1:
- **Clase B** (Δθ max 80 K sobre 40°C ambiente): motores estándar
- **Clase F** (Δθ max 105 K): uso con VFD o ambientes con temperatura elevada
- **Clase H** (Δθ max 125 K): aplicaciones críticas, θ_ambiente > 50°C

El **factor de servicio (SF)** declarado por el fabricante define la sobrecarga admisible sin superar la clase de aislamiento. Un motor IE3 con SF = 1,15 puede funcionar al 115% de la potencia nominal de forma continua sin degradación térmica, siempre que la temperatura ambiente sea ≤ 40°C.

### 5. Motores ATEX (zonas con atmósferas explosivas)

Los motores IE3 para zonas ATEX (certificados según **IEC 60079-0** e **IEC 60079-7** para modo de protección Ex e, o **IEC 60079-1** para Ex d) presentan un sobrecoste del 40-80% respecto al equivalente estándar. Verificar que la clase de eficiencia sea compatible con la certificación de zona (Zona 1/21 o Zona 2/22) del fabricante. Para estos motores, el cálculo de retorno de inversión IE2→IE3 puede ser menos favorable, pero la obligatoriedad reglamentaria aplica igualmente.

## Conclusión

El marco IEC 60034-30-1 + Reglamento EU 2019/1781 hace obligatorio IE3 en la práctica totalidad de la obra nueva y reforma industrial desde 2021. La diferencia entre IE1 e IE3 oscila entre 2,3 pp (75 kW) y 4,4 pp (7,5 kW), con periodos de retorno de inversión inferiores a un año en regímenes de operación habituales.

Checklist de decisión en obra:
- ¿Potencia entre 75-200 kW? → verificar obligatoriedad IE4 (julio 2023)
- ¿Motor con VFD? → especificar IEC 60034-17 (aislamiento F/H, rodamientos aislados)
- ¿Zona ATEX? → verificar compatibilidad IE3 con certificación IEC 60079
- Calcular ΔP = P_útil × (1/η₁ − 1/η₂) para justificar selección ante el cliente
- Documentar la clase de eficiencia en el proyecto conforme al Reglamento EU 2019/1781
