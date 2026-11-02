---
title: "Relé Buchholz: detección de fallas en transformadores según EN 50216-4"
description: "Principio de funcionamiento, tipos de fallas detectadas, valores de ajuste de alarma y disparo, y criterios de selección del relé Buchholz según EN 50216-4 e IEC 60599."
pubDate: 2026-11-02
keywords: ["relé Buchholz", "transformador potencia EN 50216-4", "protección transformador aceite", "DGA análisis gases disueltos IEC 60599"]
author: "Editor"
---

## Principio de funcionamiento del relé Buchholz

El relé Buchholz es el dispositivo de protección específico para transformadores de potencia sumergidos en aceite con depósito conservador. Su función es detectar dos fenómenos distintos que indican falla interna: la acumulación lenta de gases generados por la degradación del dieléctrico, y el desplazamiento brusco de aceite provocado por un arco eléctrico severo.

El relé se instala en la tubería inclinada (3° a 7° de pendiente hacia el relé) que conecta el tanque principal con el conservador. La inclinación es obligatoria para que los gases, al ser más ligeros que el aceite, asciendan hacia la cámara del relé en lugar de acumularse en el techo del transformador.

Internamente, el relé contiene dos elementos de actuación:

- **Flotador superior (alarma):** Cuando los gases se acumulan progresivamente en la cámara, desplazan el aceite y hacen descender el nivel. El flotador cae y acciona un microinterruptor que genera la señal de alarma.
- **Paleta basculante inferior (disparo):** Un arco interno genera una ola de aceite que circula a alta velocidad hacia el conservador. La paleta, calibrada para una velocidad de flujo determinada, gira y acciona el circuito de disparo del interruptor principal.

Este doble mecanismo permite discriminar entre fallas incipientes de baja energía (alarma sin desconexión) y fallas catastróficas que requieren desconexión inmediata.

## Fallas detectadas y gases característicos según IEC 60599

La norma **IEC 60599:2022** establece la metodología de interpretación del Análisis de Gases Disueltos (DGA) y define los gases diagnósticos para cada tipo de falla. El relé Buchholz intercepta físicamente esos gases antes de que lleguen al conservador, permitiendo su extracción y análisis en laboratorio.

| Tipo de falla | Gas predominante | Elemento activado | Urgencia |
|---|---|---|---|
| Sobrecalentamiento en aceite (< 300 °C) | CH₄, C₂H₆ | Alarma | Baja |
| Descarga parcial / corona | H₂ | Alarma | Baja-Media |
| Fallo de aislamiento en núcleo | H₂, CO | Alarma | Media |
| Cortocircuito entre espiras (incipiente) | C₂H₂, H₂ | Alarma | Alta |
| Arco eléctrico interno de alta energía | C₂H₂ + mezcla múltiple | Disparo (paleta) | Crítica |
| Ruptura de tubería o pérdida de aceite | Sin gas | Disparo (caudal) | Crítica |

La presencia de **acetileno (C₂H₂)** es el marcador más inequívoco de arco eléctrico: requiere temperaturas superiores a 1.000 °C para formarse. Un porcentaje de C₂H₂ superior al 0,1 % sobre el total de gases combustibles (TDCG) según **IEEE C57.104** o el índice de Rogers-IEC conforme a IEC 60599 debe tratarse como aviso de desconexión programada urgente.

La presencia de **CO y CO₂** simultáneamente indica degradación térmica de la celulosa (papel de aislamiento), normalmente asociada a puntos calientes en los devanados o en los conductores de salida. Una ratio CO₂/CO > 11 sugiere oxidación lenta (proceso térmico moderado); una ratio < 3 indica pirólisis activa por temperatura elevada (> 250 °C).

## Norma EN 50216-4: requisitos constructivos y de ensayo

La norma **EN 50216-4:2018** (*Transformer and reactor accessories — Part 4: Gas-operated protection relays*) es la referencia europea que gobierna el diseño, fabricación y verificación del relé Buchholz. Define:

- **Diámetros normalizados de conexión:** DN25, DN50, DN80 y DN100, correspondientes a las tuberías conservador utilizadas según la potencia nominal del transformador.
- **Presión de trabajo:** El relé debe soportar sin deformación la presión de servicio del sistema de aceite. Típicamente 100 kPa (1 bar) de presión relativa máxima en servicio normal.
- **Volumen de gas para alarma:** Ajustable entre 100 cm³ y 600 cm³ según versión. La mayoría de fabricantes (Qualitrol, Messko, Sécheron, Maschinenfabrik Reinhausen) ofrecen escalones de 150, 200, 250 y 300 cm³.
- **Velocidad de flujo para disparo:** Ajustable entre 0,5 m/s y 2,0 m/s. Los transformadores distribución (≤ 2,5 MVA) se ajustan normalmente a 0,65 m/s; los de potencia (> 10 MVA) a valores entre 0,8 y 1,5 m/s para evitar disparos intempestivos por oscilación de aceite.
- **Ensayo de verificación de caudal:** EN 50216-4 exige el ensayo con flujo de aceite a temperatura de referencia (25 °C ± 5 °C), demostrando que la paleta actúa dentro del ±15 % del caudal ajustado.
- **Temperatura de servicio:** −25 °C a +70 °C.

## Valores de ajuste típicos según potencia del transformador

Los valores siguientes son orientativos; el ajuste definitivo debe confirmar el fabricante del relé y del transformador:

| Parámetro de ajuste | ≤ 1 MVA (DN25-DN50) | 1–40 MVA (DN50-DN80) | > 40 MVA (DN80-DN100) |
|---|---|---|---|
| Volumen alarma gas (cm³) | 150–200 | 200–300 | 300–500 |
| Velocidad disparo aceite (m/s) | 0,65–0,90 | 0,65–1,0 | 0,80–1,5 |
| Inclinación tubería (°) | 3–5 | 3–7 | 5–7 |
| Pendiente mínima recomendada (%) | 5 | 5–12 | 9–12 |

Para transformadores sumergidos en aceite con aislamiento mejorado por líquido de alto punto de inflamación (ésteres naturales o sintéticos), la generación de gases es menor a igual nivel de falla; algunos fabricantes recomiendan reducir el volumen de alarma a 100–150 cm³ para mantener la misma sensibilidad.

## Criterios de selección y montaje en obra

**Compatibilidad con el transformador:** El relé Buchholz solo es aplicable a transformadores con depósito conservador. Los transformadores herméticos (sin conservador, con aleta o membrana flexible) no admiten este dispositivo; en ellos la protección equivalente es el relé de presión súbita (SPR) o el relé de presión súbita sellado, con actuación en microsegundos frente a los 20–60 ms del Buchholz mecánico.

**Diámetro de tubería:** El DN del relé debe coincidir con el brida del conservador. Un relé sobredimensionado reduce la sensibilidad al flujo; uno infradimensionado puede bloquear la circulación de aceite por expansión térmica y elevar la presión estática.

**Orientación del gasómetro:** La válvula de purga de gases debe quedar en la parte superior y accesible para la extracción periódica de muestras. Durante la puesta en servicio inicial, con la instalación aún bajo vacío o con temperatura elevada, el relé puede acumular aire por dilatación; este gas no indica falla y debe purgarse manualmente.

**Cableado de los contactos:**
- Contacto de alarma → SCADA / panel de control (aviso sin desconexión inmediata)
- Contacto de disparo → protección de disparó del interruptor principal en AT y BT (desconexión de ambos lados del transformador)

En instalaciones con **interruptor automático MT** protegido según **IEC 62271-100**, el disparo del Buchholz se conecta como protección de respaldo, adicional al relé diferencial de transformador (función ANSI 87T según IEC 60255-187-1). El relé Buchholz no sustituye al diferencial: detecta fallas que generan poco flujo (fallas incipientes) que el diferencial no puede ver porque la corriente diferencial es inferior al umbral de sensibilidad (típicamente 0,15–0,20 In).

**Coordinación con Buchholz de cuba y de cambiador de tomas:** Los transformadores de gran potencia llevan tres relés Buchholz independientes: uno en la cuba principal, uno en el cambiador de tomas en carga (OLTC), y en algunos diseños uno en el reactor de preselección. Cada relé tiene sus propios ajustes de alarma y disparo, y sus contactos deben cablearse a circuitos de protección separados, dado que una falla en el OLTC no debe necesariamente disparar la protección principal si aún puede aislarse mecánicamente.

## Diagnóstico y mantenimiento según IEC 60076-7

El mantenimiento preventivo del relé Buchholz incluye:

1. **Extracción semestral del gas acumulado:** Se extrae con jeringa a través de la válvula superior. Si el volumen es > 10 cm³ por semestre sin causa identificada (primer llenado, oscilación de temperatura), debe enviarse a análisis DGA según IEC 60567.

2. **Verificación anual del caudal de disparo:** Se inyecta aceite a la velocidad calibrada con banco de ensayo portátil. La paleta debe actuar en el rango ±15 % del valor ajustado.

3. **Inspección de contactos:** Los microinterruptores magnéticos pueden oxidarse en instalaciones costeras (salinidad). La resistencia del contacto en posición cerrado debe ser < 0,5 Ω.

4. **Verificación de la inclinación de tubería:** En transformadores con movimientos sísmicos frecuentes o asentamiento de terreno, la inclinación puede cambiar. Si la tubería queda horizontal o con pendiente hacia el tanque, los gases no fluyen al relé y la alarma no actúa.

## Conclusión

El relé Buchholz es un elemento de protección imprescindible para transformadores con conservador de aceite. Su doble mecanismo (flotador + paleta) permite discriminar entre fallas incipientes y fallos catastróficos con tiempos de respuesta de 20–300 ms para la paleta de disparo, detectando fallas internas que ninguna otra protección eléctrica puede ver en fase temprana. La selección del volumen de alarma (150–500 cm³) y la velocidad de disparo (0,65–1,5 m/s) según **EN 50216-4** debe ajustarse a la potencia del transformador y al tipo de aceite. La integración con DGA según **IEC 60599** convierte el gas extraído del relé en información diagnóstica que permite programar la intervención antes de que la falla progrese a un cortocircuito devanado-tierra, evitando la destrucción del transformador.
