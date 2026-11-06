---
title: "Luminotecnia industrial LED: UNE-EN 12464-1 e iluminancia"
description: "Niveles de iluminancia mantenida, UGR y Ra para instalaciones industriales LED según UNE-EN 12464-1:2022 y eficiencia VEEI del CTE DB HE-3."
pubDate: 2026-11-06
keywords: ["luminotecnia industrial LED", "UNE-EN 12464-1", "iluminancia industrial lux", "VEEI CTE HE-3", "highbay LED nave industrial"]
author: "Editor"
---

La UNE-EN 12464-1:2022 —transposición directa de la EN 12464-1:2021— es la norma de referencia para la iluminación de lugares de trabajo en interiores en España. Reemplaza la versión de 2003 y endurece varios criterios, en especial los relacionados con uniformidad y control del deslumbramiento. Para un técnico que diseña o reforma la iluminación de una nave, taller o almacén, aplicar correctamente esta norma no es opcional: el Real Decreto 486/1997 sobre lugares de trabajo y la Guía Técnica del INSST la citan como referencia normativa para cumplir el Anexo IV del RD.

Este artículo cubre los parámetros fotométricos exigidos, los valores concretos por tipo de zona industrial, el cálculo del flujo necesario con LED y los criterios de eficiencia energética del CTE DB HE-3.

---

## Parámetros fotométricos según UNE-EN 12464-1:2022

La norma define tres magnitudes obligatorias para cada zona de trabajo:

**Iluminancia mantenida (Ēm, en lux)**  
Es el valor mínimo que la instalación debe mantener durante toda su vida útil, después de aplicar el factor de mantenimiento (fm). No es el valor inicial de puesta en marcha; es el suelo bajo el que nunca debe caer el sistema. La fórmula de cálculo del flujo total necesario es:

```
Φtotal = (Ēm × S) / (ηu × fm)
```

Donde:
- S = superficie del área de trabajo (m²)
- ηu = factor de utilización del sistema (0,55–0,85 según geometría y reflectancias)
- fm = factor de mantenimiento (0,60–0,80 según nivel de contaminación y frecuencia de limpieza)

**Índice de deslumbramiento unificado (UGRL)**  
Es el límite máximo de deslumbramiento molesto, calculado según CIE 117. Valores más bajos exigen luminarias con ópticas más controladas. El UGR se verifica para la posición más desfavorable del puesto de trabajo.

**Índice de reproducción cromática (Ra)**  
Mide la fidelidad del color bajo la fuente de luz respecto a un iluminante de referencia. Para trabajos con inspección de color (control de calidad visual, mecanizado de precisión), un Ra < 80 inutiliza el criterio visual; para zonas de tránsito o almacenamiento, Ra ≥ 60 es suficiente.

---

## Valores por zona industrial: tabla según UNE-EN 12464-1:2022

Los valores de la tabla siguiente corresponden al anexo normativo de la UNE-EN 12464-1:2022, grupo "Industria, artesanía, agricultura y actividades hortícolas" (sección 5.26 y siguientes):

| Tipo de zona / actividad | Ēm (lux) | UGRL máx. | Ra mín. |
|---|---|---|---|
| Zonas de tránsito, escaleras interiores | 100 | 28 | 40 |
| Almacén: acceso ocasional (ITC-BT-44 referenciable) | 100 | 25 | 60 |
| Almacén: ocupación continua | 200 | 25 | 60 |
| Área de embalaje y expedición | 300 | 25 | 80 |
| Taller mecánico: trabajo ordinario | 300 | 25 | 80 |
| Taller mecánico: trabajo fino (tolerancias < 0,1 mm) | 500 | 22 | 80 |
| Metrología, inspección visual de piezas | 750 | 19 | 80 |
| Montaje electrónico de precisión | 1000 | 19 | 80 |
| Sala de control / cuadros eléctricos | 500 | 19 | 80 |
| Área de soldadura | 500 | 25 | 80 |
| Pintura y acabados: preparación | 750 | 25 | 90 |
| Pintura y acabados: inspección | 1000 | 19 | 90 |

> **Nota sobre uniformidad:** la norma exige también uniformidad mínima U₀ = Ēmin/Ēm ≥ 0,40 en la zona de tarea y ≥ 0,10 en la zona circundante inmediata. Las luminarias de distribución muy estrecha (IP65 highbay con óptica de haz 60°) colocadas a alturas superiores a 8 m pueden crear zonas oscuras entre puntos de luz si el espaciado no es el correcto.

---

## Eficiencia energética: VEEI y CTE DB HE-3

El Código Técnico de la Edificación, en su Documento Básico HE-3 (edición 2019 con actualización de septiembre 2022), limita el **Valor de Eficiencia Energética de la Instalación (VEEI)** definido como:

```
VEEI = (P × 100) / (S × Ēm)    [W/(m²·100lux)]
```

Donde P es la potencia total instalada (luminarias + equipos auxiliares, en vatios), S es la superficie iluminada (m²) y Ēm la iluminancia media mantenida (lux).

Los límites del CTE DB HE-3 para uso industrial son:

| Tipo de zona | VEEI límite [W/(m²·100lux)] |
|---|---|
| Almacén, archivo, sala técnica | 4,0 |
| Zonas de producción / taller | 4,0 |
| Zonas comunes, circulación | 4,0 |
| Oficinas técnicas en planta | 3,5 |
| Sala de control, CPD | 3,0 |

Un VEEI de 4,0 significa que, para mantener 300 lux en 1.000 m², la instalación no puede consumir más de:

```
P ≤ VEEI × S × Ēm / 100 = 4,0 × 1.000 × 300 / 100 = 12.000 W (12 kW)
```

Con LED highbay de 120 W y 18.000 lm (eficacia nominal 150 lm/W), se obtiene un flujo mantenido de aproximadamente 10.800 lm por luminaria (aplicando fm = 0,80 y η factor de luminaria sobre la zona de tarea = 0,70). Para 300 lux en 1.000 m² se necesitan unas 28 unidades (8.400 lm/luminaria proyectados sobre tarea, calculando Φnecesario ≈ 300 × 1.000 / (0,65 × 0,80) ≈ 577.000 lm totales, es decir 32 luminarias). La potencia total sería 32 × 120 W = 3.840 W, muy por debajo del límite de 12.000 W. El VEEI resultante sería ≈ 1,28, ampliamente bajo el límite de 4,0.

---

## Luminarias LED para uso industrial: parámetros técnicos de selección

La elección de la luminaria correcta no depende únicamente de la eficacia (lm/W). Para un entorno industrial, los criterios determinantes son:

### Eficacia luminosa real vs. nominal

La industria cita eficacias nominales del chip (hasta 220 lm/W en algunos LED de alta gama). Lo que interesa al proyectista es la **eficacia del sistema luminaria**, que incluye pérdidas en el driver (η_driver ≈ 0,88–0,93), en la óptica (η_óptica ≈ 0,85–0,92) y en el cristal o difusor:

```
η_sistema = η_chip × η_driver × η_óptica × η_cristal
```

Para luminarias highbay industriales bien diseñadas, la eficacia de sistema oscila entre **120 y 170 lm/W** (referencia: catálogos Philips Highbay Gen 5, Ledvance Damp Proof, Siteco Sina). Los valores más altos corresponden a distribuciones directas (sin difusor) con óptica de aluminio pulido.

### Protección IP e IK

| Entorno | IP mínimo | IK recomendado |
|---|---|---|
| Nave limpia, polvo ocasional | IP44 | IK06 |
| Almacén con polvo / partículas | IP65 | IK08 |
| Zona de lavado / humedad alta | IP66 | IK08 |
| Zona de impactos mecánicos | IP65 | IK10 |
| Exterior bajo marquesina | IP65 | IK08 |

Los grados IP e IK se verifican según IEC 60529 (protección IP) e IEC 62262 (protección IK). Una luminaria con IP44 en un almacén de harina o cemento fallará por acumulación de polvo en el driver en menos de 2 años.

### Temperatura de color y Ra para inspección

Para tareas de inspección visual o control de calidad, la temperatura de color influye en la percepción del contraste. La UNE-EN 12464-1:2022 no impone temperatura de color para uso industrial general, pero el CIE 97 recomienda:

- **4000 K (blanco neutro):** uso general en naves, talleres y almacenes
- **5000–6500 K (blanco frío / luz día):** inspección de colores, laboratorio, metrología
- Ra ≥ 90 obligatorio cuando se evalúa color de producto (sector textil, pintura, calidad alimentaria)

### Vida útil (L70B50) y mantenimiento de flujo

La vida útil declarada en luminarias LED industriales se expresa como **L70B50**, es decir, el tiempo (en horas) tras el cual el 50% de las unidades han caído por debajo del 70% del flujo inicial. El estándar aplicable es IEC 62717 para módulos LED y IEC 62722-2-1 para luminarias.

Para el cálculo del factor de mantenimiento fm (que entra directamente en el cálculo del flujo necesario), la norma UNE-EN 12464-1:2022 remite a la CIE 97:2005. Un ciclo de vida de 50.000 h a L70B50 con fm = 0,80 implica que a mitad de vida la instalación todavía mantiene el 86% del flujo inicial (antes de que el envejecimiento domine sobre la suciedad).

---

## Criterios de selección aplicables en obra

Antes de lanzar cualquier proyecto de iluminación industrial con LED, verifica estos puntos:

1. **Altura de montaje:** para h < 5 m, usa luminarias de tipo regleta o plafón IP65 (40–80 W, distribución amplia). Para h = 5–10 m, highbay 100–200 W con óptica 60–90°. Para h > 10 m, highbay 200–400 W con óptica simétrica estrecha (40°) o asimétrica.

2. **Cálculo de UGRL:** usa el método tabular de CIE 190 o software (DIALux Evo, Relux). Un UGRL calculado solo con la distancia al techo es incorrecto; depende del ángulo de visión desde los puestos de trabajo.

3. **Dimmers y control DALI:** el CTE DB HE-3 exige en zonas > 10 m² un sistema de control que permita ajuste de flujo y apagado automático por ausencia de personas (artículo 3.1.3). Las luminarias deben ser DALI-2 certificadas (IEC 62386) o equivalente con protocolo abierto.

4. **Factor de mantenimiento fm:** no uses siempre 0,80 por defecto. En entornos con polvo o grasa (talleres de mecanizado, hornos), fm = 0,65–0,70 y ciclo de limpieza cada 6 meses es más realista. Subestimar fm genera instalaciones que no cumplen la norma a los 2 años de puesta en marcha.

5. **Verificación de VEEI:** calcula el VEEI antes de entregar el proyecto. Incluye en P la potencia del driver (no solo la del LED), ya que el DB HE-3 exige la potencia total absorbida.

6. **Informe fotométrico UNE-EN 13032-2:** exige al fabricante los archivos fotométricos en formato LDT o IES (medidos según CIE 121) para introducir en el software de cálculo. Los folletos de producto no son suficientes para justificar cumplimiento de UGRL.

---

## Conclusión

La transición a LED en instalaciones industriales no es simplemente sustituir fuentes por otras más eficientes: exige aplicar los valores de Ēm, UGRL y Ra de la UNE-EN 12464-1:2022 según el tipo de actividad, calcular el VEEI para cumplir el DB HE-3, y dimensionar correctamente el factor de mantenimiento. Una nave con trabajo mecánico fino requiere 500 lux mantenidos, UGRL ≤ 22 y Ra ≥ 80; exigir solo el lux sin verificar UGR es una fuente habitual de reclamaciones en obra. Los LED de alta eficiencia (≥ 130 lm/W de sistema) permiten cumplir holgadamente el límite VEEI de 4,0 W/(m²·100lux) con un consumo un 50–60% inferior a las instalaciones con descarga de alta intensidad.
