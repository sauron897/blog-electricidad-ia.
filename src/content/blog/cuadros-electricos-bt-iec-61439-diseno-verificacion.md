---
title: "Cuadros eléctricos BT según IEC 61439: diseño y verificación"
description: "Diseño y verificación de cuadros de distribución BT conforme a IEC 61439-1 e IEC 61439-2: métodos de verificación, dimensionamiento de barras y criterios de selección para instalaciones industriales."
pubDate: 2026-09-30
keywords: ["cuadros electricos BT IEC 61439", "verificacion diseno cuadro BT", "barras colectoras cuadro electrico", "IEC 61439-2 PABK", "cuadro distribucion industrial"]
author: "Editor"
---

## IEC 61439: La norma que reemplazó IEC 60439 en cuadros BT

La serie IEC 61439 define los requisitos para conjuntos de aparamenta de baja tensión (Low-Voltage Switchgear and Controlgear Assemblies, LVSCA). Entró en vigor en 2009 y reemplazó completamente a IEC 60439, con un cambio de enfoque radical: de verificar el cuadro terminado a verificar el diseño, responsabilizando al fabricante del conjunto (el assembler) de demostrar conformidad antes de la fabricación.

La estructura normativa se articula en:

- **IEC 61439-1**: Reglas generales, aplicable a todos los tipos de conjuntos
- **IEC 61439-2**: Conjuntos de potencia (Power Assemblies, PABK) — cuadros industriales con Ie > 1600 A o Icc elevado
- **IEC 61439-3**: Cuadros de distribución para uso por personas no instruidas (BDC, antiguo IEC 60439-3)
- **IEC 61439-4**: Conjuntos para obra
- **IEC 61439-5**: Conjuntos para redes de distribución pública

En España, la adopción es UNE-EN IEC 61439-1:2022 y UNE-EN IEC 61439-2:2022. El REBT ITC-BT-17 exige que los cuadros generales de distribución cumplan la norma UNE-EN aplicable, lo que en la práctica remite directamente a IEC 61439-2 para cuadros industriales.

---

## Métodos de verificación en IEC 61439-1

IEC 61439-1 (cláusula 10) define tres métodos de verificación del diseño, que el assembler puede combinar para cada característica del cuadro:

| Método | Código | Descripción |
|--------|--------|-------------|
| Ensayo | T | Medición directa sobre el conjunto o un prototipo representativo |
| Cálculo | C | Derivación mediante comparación con un diseño de referencia ensayado |
| Evaluación | A | Revisión de planos, fichas técnicas de componentes, normas de componentes |

El método de ensayo (T) da la mayor certeza, pero es costoso. En la práctica, los fabricantes de sistemas de cuadros (Legrand XL³, Schneider Prisma, ABB ArTu) certifican su sistema con ensayos completos, y el assembler puede usar el método de cálculo o evaluación apoyándose en esa certificación, siempre que respete las reglas del sistema.

### Verificaciones obligatorias principales

IEC 61439-1, Tabla 1, lista 22 características que deben verificarse. Las más críticas para el diseño son:

1. **Elevación de temperatura (10.10)**: límites en °C para cada parte del cuadro
2. **Resistencia a cortocircuito (10.11)**: Icw e Ipk de las barras y conexiones
3. **Grado de protección IP (10.3)**: verificado por ensayo según IEC 60529
4. **Continuidad del circuito de protección (10.6)**: resistencia ≤ 100 mΩ entre PE y partes metálicas accesibles
5. **Distancias de aislamiento (10.9)**: líneas de fuga y distancias en aire según IEC 60664-1

---

## Elevación de temperatura: límites en IEC 61439-1

La cláusula 10.10 establece los límites de temperatura máxima en condiciones de servicio nominales (temperatura ambiente ≤ 35 °C de media, máximo 40 °C). Los límites más relevantes son:

| Componente | Temp. máxima (°C) | ΔT máximo sobre 35 °C |
|-----------|------------------|----------------------|
| Barras colectoras desnudas (Cu/Al) | 105 | 70 K |
| Terminales para conductores externos (aislamiento PVC) | 70 | 35 K |
| Partes accesibles metálicas (operación manual) | 70 (intencionadas) / 80 (accidentales) | 35 / 45 K |
| Componentes (según especificación del fabricante) | Según ficha técnica | — |

El ensayo de elevación de temperatura se realiza a corriente nominal durante el tiempo necesario para alcanzar régimen estacionario (variación < 1 K/hora), midiendo con termopares en los puntos críticos.

Para cuadros verificados por cálculo (método C), IEC 61439-1 proporciona el método simplificado de la cláusula 10.10.4, que corrige la corriente admisible en función de las pérdidas de los componentes instalados y la disipación del envolvente.

---

## Dimensionamiento de barras colectoras: datos IEC (GElectrical)

Las barras colectoras son la espina dorsal del cuadro. Deben dimensionarse para dos criterios independientes:

1. **Corriente admisible continua (Ie)**: sin superar el límite de temperatura de 105 °C
2. **Soportabilidad a cortocircuito**: sin deformación plástica ni arco entre fases durante el tiempo de actuación de la protección aguas arriba

La siguiente tabla recoge valores reales de barras de canalización prefabricada Legrand, extraídos de la base de datos GElectrical (que implementa los catálogos IEC del fabricante):

**Barras aluminio — Serie MR (Medium Rating)**

| Designación | Ie máx (A) | Icw (kA, 1s) | Ipk (kA) | R (mΩ/m) |
|-------------|-----------|-------------|---------|----------|
| 160A-MR-AL  | 160       | 9           | 15      | 0,665    |
| 250A-MR-AL  | 250       | 15          | 30      | 0,443    |
| 400A-MR-AL  | 400       | 15          | 30      | 0,163    |
| 630A-MR-AL  | 630       | 22          | 45      | 0,081    |
| 800A-MR-AL  | 800       | 22          | 45      | 0,070    |

**Barras cobre — Serie SCP (Short Circuit Protected)**

| Designación  | Ie máx (A) | Icw (kA, 1s) | Ipk (kA) | R (mΩ/m) |
|--------------|-----------|-------------|---------|----------|
| 630A-SCP-CU  | 630       | 22          | 45      | 0,082    |
| 1000A-SCP-CU | 1000      | 30          | 66      | 0,035    |
| 1600A-SCP-CU | 1600      | 51          | 112     | 0,027    |
| 2500A-SCP-CU | 2500      | 53          | 116     | 0,017    |
| 4000A-SCP-CU | 4000      | 106         | 232     | 0,011    |

El Icw (corriente de corta duración admisible) se refiere a 1 segundo. Si el tiempo de actuación de la protección es menor, puede aplicarse la corrección:

**I²t = cte** → para t < 1s: **Icw_real = Icw × √(1/t)**

Por ejemplo, una barra con Icw = 22 kA (1s) soporta 31,1 kA durante 0,5 s, o 44,0 kA durante 0,25 s.

El Ipk es el valor de cresta de la primera semionda de cortocircuito. Para sistemas con factor de asimetría κ típico (≈ 1,7 para redes industriales), se cumple que Ipk ≈ √2 × κ × Icc_rms ≈ 2,4 × Icc_rms.

---

## Grado de protección IP y forma de segregación

IEC 61439-1 no exige un IP mínimo genérico; lo determina la aplicación y la ubicación del cuadro (IEC 60364-3, tabla 51A). Los valores habituales en instalaciones industriales son:

- **IP31**: cuadros en sala eléctrica protegida (acceso solo personal autorizado)
- **IP43**: cuadros en locales donde pueda haber proyecciones de agua
- **IP54**: cuadros en exteriores o entornos con polvo
- **IP65**: cuadros en intemperie o entornos húmedos severos

La **forma de segregación** (IEC 61439-1, cláusula 7.7) define el grado de separación entre barras, salidas y compartimentos de cables:

| Forma | Descripción |
|-------|-------------|
| 1     | Sin separación interna |
| 2b    | Barras separadas de unidades funcionales; bornes de salida sin separar entre sí |
| 3b    | Barras y unidades funcionales separadas entre sí; bornes sin separar |
| 4b    | Separación completa: barras, cada unidad funcional y sus bornes en compartimentos independientes |

La Forma 4b ofrece la máxima seguridad durante el trabajo en tensión en un circuito con los adyacentes en servicio, y es obligatoria en cuadros de proceso donde se requiere mantenimiento selectivo sin parada general.

---

## Criterios de selección del cuadro para instalaciones industriales

La selección del conjunto debe resolver simultáneamente varios requisitos de la instalación:

**1. Corriente nominal de barras (Ie)**
- Calcular la corriente total de diseño: suma de circuitos con factor de simultaneidad k_s (ITC-BT-10, tabla 1 para uso industrial k_s = 0,7–0,9 según proceso)
- Seleccionar la barra inmediatamente superior de la serie normalizada (160, 250, 315, 400, 630, 800, 1000, 1250, 1600, 2000, 2500, 3200, 4000, 5000, 6300 A)

**2. Poder de corte del interruptor principal (Icu)**
- Calcular Icc trifásico en el punto de conexión: método de impedancias IEC 60909
- Verificar que el interruptor general tiene Icu ≥ Icc y las barras tienen Icw ≥ Icc durante el tiempo de disparo

**3. Temperatura y disipación**
- Estimar las pérdidas totales de los componentes (suma de pérdidas a plena carga)
- Verificar que la elevación de temperatura en el envolvente no supera los límites de la cláusula 10.10

**4. Grado de protección IP**
- Definir según la clasificación del local (IEC 60364-3) y las condiciones ambientales

**5. Forma de segregación**
- Definir según los requisitos de mantenimiento selectivo y seguridad operacional

**6. Verificación de la conformidad del assembler**
- Si el assembler usa un sistema certificado (Legrand, Schneider, ABB…): acogerse al método de cálculo/evaluación con los datos del fabricante del sistema
- Si el diseño es propio: ensayo completo del prototipo en laboratorio acreditado

---

## Conclusión

IEC 61439-1 e IEC 61439-2 desplazan la responsabilidad de la conformidad del cuadro al assembler, que debe documentar la verificación de diseño antes de fabricar. El técnico que especifica o recibe un cuadro industrial debe exigir la **declaración de conformidad del assembler** (no solo del fabricante de componentes) y verificar que los ensayos o cálculos de elevación de temperatura, soportabilidad a cortocircuito y grado de protección están respaldados por documentación técnica trazable.

Para la selección de barras, los valores de Icw e Ipk de los catálogos de los fabricantes de sistemas de canalización (Legrand XL³, Schneider Canalis, ABB Zucchini) son la referencia directa. La regla I²t = cte permite extrapolar la soportabilidad para tiempos de protección distintos de 1 s, habitualmente entre 0,1 y 0,5 s en cuadros industriales con protecciones de alta velocidad.
