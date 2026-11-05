---
title: "Red IT en instalaciones médicas: IMD y aislamiento IEC 61557-8"
description: "Diseño y verificación de redes IT en locales médicos del Grupo 2: transformador IEC 61558-2-15, IMD según IEC 61557-8 e ITC-BT-38 del REBT."
pubDate: 2026-11-05
keywords: ["red IT instalaciones médicas", "IMD vigilancia aislamiento IEC 61557-8", "IEC 60364-7-710 locales médicos", "transformador aislamiento IEC 61558-2-15"]
author: "Editor"
---

## Por qué la red IT es obligatoria en quirófanos

En un local médico del Grupo 2 —quirófanos, unidades de cuidados intensivos, salas de hemodinámica— la probabilidad de contacto directo entre el equipo electromédico y el sistema cardiovascular del paciente exige una protección eléctrica que va más allá de la interrupción por diferencial. Un primer fallo de aislamiento en una red TN o TT corta la alimentación; en un entorno crítico, eso puede costar una vida.

La solución normativa es la **red IT** (*Isolated Terra*): un sistema sin conexión intencionada a tierra que tolera el primer fallo sin interrupción, mientras un **dispositivo de vigilancia del aislamiento** (IMD, *Insulation Monitoring Device*) detecta el fallo y emite alarma. La obligación queda recogida en **IEC 60364-7-710:2021** (transpuesta en España como **UNE-HD 60364-7-710**) y en la **ITC-BT-38** del REBT (RD 842/2002) para establecimientos sanitarios.

La distinción clave frente a otras instalaciones especiales es el concepto de **microshock**: una corriente de tan solo 150 µA introducida directamente en el miocardio a través de un catéter o electrodo intracavitario puede causar fibrilación ventricular. La red IT no evita el macroshock, pero garantiza que el primer fallo de aislamiento no interrumpa el suministro ni cree una diferencia de potencial peligrosa entre equipos conectados al paciente.

---

## Clasificación de locales médicos: Grupos 0, 1 y 2

La norma IEC 60364-7-710:2021 estratifica los locales médicos en tres grupos en función del riesgo eléctrico para el paciente (cláusula 710.3):

| Grupo | Descripción | Ejemplos | Sistema requerido |
|-------|-------------|----------|-------------------|
| **0** | Sin equipo aplicado al paciente | Pasillos, administración, salas de espera | TN o TT convencional |
| **1** | Equipo en contacto externo, no intracavitario | Consultas, salas de exploración, fisioterapia, endoscopia | TN-S o IT según análisis de riesgo |
| **2** | Equipo que puede contactar directamente con el corazón | Quirófanos, UCI, hemodinámica, radiología intervencionista | **IT obligatorio + IMD** |

La clasificación es responsabilidad del proyectista, con acuerdo de la dirección médica del centro, y debe documentarse en el proyecto (IEC 60364-7-710:2021, cláusula 710.3). En España, la ITC-BT-38 remite a esta misma clasificación para determinar qué circuitos deben alimentarse desde un cuadro IT.

---

## Transformador de aislamiento médico: IEC 61558-2-15

El elemento fundamental de la red IT médica es el **transformador de aislamiento de seguridad médica** (MITM), normado por **IEC 61558-2-15** (EN 61558-2-15 en su versión europea). Sus parámetros de diseño difieren de un transformador de aislamiento estándar en aspectos críticos:

**Potencia nominal:** La norma IEC 60364-7-710:2021 (cláusula 710.413.1.3.3) limita la potencia por circuito IT a **máximo 10 kVA en el Grupo 2**. Los valores normalizados habituales son 3,15 kVA, 5 kVA y 8 kVA. Esta limitación es intencional: reduce la energía disponible ante un segundo fallo de aislamiento en el secundario.

**Tensión de cortocircuito (Ucc):** Entre **2 % y 4 %** según IEC 61558-2-15. Un Ucc bajo maximiza la regulación de tensión bajo carga y limita la corriente de cortocircuito máxima. Para un transformador de 8 kVA, 230/230 V, Ucc = 2 %, la corriente de cortocircuito en secundario es:

```
Icc = Sn / (Ucc × Vn) = 8000 / (0,02 × 230) ≈ 1739 A
```

Este valor es el que debe soportar la protección magnetotérmica del circuito secundario IT.

**Capacitancia parásita (Cn):** La capacitancia parásita total de la red IT hacia tierra —formada por el transformador, los cables y los filtros EMI de los equipos médicos— debe mantenerse por debajo de **1 µF total** para que el IMD mida con precisión (IEC 61557-8:2014, cláusula 6.2). Un quirófano con 50 m de cableado y 15 equipos con filtros EMI puede acumular fácilmente 400–600 nF, lo que requiere verificación antes de la puesta en servicio.

**Monitorización térmica:** El transformador debe incorporar **termistor PTC o bimetálico** para señalización de sobretemperatura, conectado al IMD (IEC 60364-7-710:2021, cláusula 710.413.1.3.3). Si la temperatura del bobinado supera la clase F (155 °C) o H (180 °C), el IMD añade alarma de sobrecarga térmica.

---

## IMD: principio de medida y requisitos IEC 61557-8

El IMD mide en continuo la **resistencia de aislamiento equivalente Rf** entre los conductores activos y tierra. En una red IT sin defecto, Rf supera típicamente 1 MΩ; ante el primer fallo, desciende según la impedancia del defecto.

**Principio de medida:** Se superpone una señal de **baja frecuencia** (1–5 Hz) o **DC pulsada** sobre la tensión de alimentación, con una tensión auxiliar **≤ 25 V AC o ≤ 60 V DC** (IEC 61557-8:2014, cláusula 6.1). Este límite garantiza que la corriente de medida no sea peligrosa para el paciente aunque el conductor de medida resultara accidentalmente accesible.

**Corriente de medida:** No debe superar **1 mA** (IEC 61557-8, cláusula 6.1) —requisito específico del entorno médico para prevenir el microshock en caso de fallo del propio IMD.

**Umbrales de alarma normalizados:**

| Parámetro | Valor | Referencia normativa |
|-----------|-------|----------------------|
| Umbral de alarma principal (Rf mínima) | **50 kΩ** | IEC 60364-7-710:2021 cláusula 710.413.1.3.4 |
| Umbral de prealarma (recomendado) | 100 kΩ | IEC 61557-8 Annex A (MED-IMD) |
| Tensión auxiliar máxima | 25 V AC / 60 V DC | IEC 61557-8 cláusula 6.1 |
| Corriente de medida máxima | 1 mA | IEC 61557-8 cláusula 6.1 |
| Tiempo de respuesta máximo | ≤ 30 s | IEC 61557-8 cláusula 6.3 |
| Rango de medida mínimo | 1 kΩ – 10 MΩ | IEC 61557-8 cláusula 5 |

Cuando Rf desciende por debajo de 50 kΩ, el IMD activa **simultáneamente alarma visual y acústica** (IEC 60364-7-710:2021, cláusula 710.413.1.3.4). La alarma acústica puede silenciarse, pero la visual debe permanecer hasta que el fallo sea corregido (**alarma con enclavamiento**). Este punto falla con frecuencia en instalaciones existentes: IMDs sin enclavamiento en los que el personal de guardia silencia la alarma sin localizar ni corregir el defecto.

La alarma debe repetirse también en la **zona de control de enfermería** (nurse station) mediante un relé de repetición de alarma remota, requisito explícito de la norma (cláusula 710.413.1.3.4.b).

---

## Localización de fallos: IEC 61557-9

Una vez activada la alarma del IMD, es necesario localizar el circuito afectado. Para un quirófano con 8–12 circuitos terminales, la desconexión secuencial tardaría 30–60 minutos e interrumpiría suministros críticos. El **localizador de fallos de aislamiento** (FLM, conforme a **IEC 61557-9**) inyecta una señal de corriente conocida en cada ramal y mide la respuesta por circuito, identificando el defecto en menos de 1 minuto sin interrumpir ningún servicio.

**Requisito de coordinación:** El FLM debe operar con la misma señal de medida que el IMD. La capacitancia total Cn de la red es el factor limitante: si Cn > 1 µF, la impedancia capacitiva a la frecuencia de medida puede enmascarar el fallo resistivo. El fabricante debe certificar la compatibilidad entre IMD y FLM para el Cn de la instalación.

---

## Criterios de selección del conjunto IT médico

Para un quirófano tipo del Grupo 2 con transformador de 8 kVA, los criterios de selección son:

| Elemento | Parámetro de selección | Norma aplicable |
|----------|------------------------|-----------------|
| Transformador | 8 kVA, Ucc 2–4%, clase F o H, PTC integrado, 1 × MITM por quirófano | IEC 61558-2-15, IEC 60364-7-710 |
| IMD | Rf mínima medible ≤ 1 kΩ, alarma enclavada a 50 kΩ, V_aux ≤ 25 V AC, MED-IMD certificado IEC 61557-8 Annex A | IEC 61557-8:2014 |
| Localizador de fallos | Capacidad ≥ 8 circuitos, compatible con señal del IMD, Cn ≤ 1 µF | IEC 61557-9 |
| Panel de alarma remota | Visual + acústico en nurse station, enclavamiento de alarma | IEC 60364-7-710 cláusula 710.413.1.3.4 |
| Cuadro IT | IP43 mínimo, barras Cu sección ≥ 25 mm² para neutro aislado | IEC 61439-1, IEC 60364-7-710 |
| Monitorización de carga | Alarma si I_carga > 100% In durante > 60 s | IEC 61558-2-15 |

**Verificación previa a la puesta en servicio:**

1. **Medir Rf con todos los equipos médicos conectados** (no en vacío): los filtros EMI reducen Rf significativamente. Si Rf < 100 kΩ con la instalación sana, revisar filtros o reducir la extensión de red.
2. **Medir Cn total** con la instalación en servicio. Comparar con el límite de 1 µF (IEC 61557-8, cláusula 6.2).
3. **Comprobar el enclavamiento de alarma**: simular un defecto con resistencia de prueba de 50 kΩ entre fase y tierra, verificar que la alarma visual no se apaga hasta retirar el defecto.
4. **Verificar la alarma remota** en el panel de nurse station.
5. **Probar el localizador** con el defecto simulado en cada circuito terminal.

---

## Conclusión

La red IT médica en locales del Grupo 2 requiere un enfoque de ingeniería integral: transformador de aislamiento certificado per IEC 61558-2-15 con potencia ≤ 10 kVA y Ucc del 2–4%, un IMD con alarma enclavada a 50 kΩ según IEC 61557-8 Annex A (MED-IMD), capacitancia total de red inferior a 1 µF para garantizar la eficacia de la medida, y localizador de fallos (IEC 61557-9) para mantener la continuidad asistencial durante la búsqueda del defecto. La ITC-BT-38 del REBT y la UNE-HD 60364-7-710:2021 son las referencias normativas vinculantes en España, alineadas con la edición internacional de 2021. La verificación funcional del enclavamiento de alarma y la medida de Rf bajo carga real son los dos puntos que con más frecuencia revelan deficiencias en instalaciones ya ejecutadas.
