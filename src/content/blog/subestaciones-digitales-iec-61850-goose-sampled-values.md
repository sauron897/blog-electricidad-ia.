---
title: "IEC 61850 en Subestaciones Digitales: GOOSE, Sampled Values y Arquitectura Lógica"
description: "Arquitectura de tres niveles IEC 61850, mensajes GOOSE con clases P1/P2/P3, Sampled Values a 80/256 muestras/ciclo y criterios de selección para subestaciones digitales."
pubDate: 2026-10-21
keywords: ["IEC 61850 subestaciones digitales", "GOOSE proteccion automatizacion", "Sampled Values merging unit", "IEC 61850 arquitectura logica", "bus de proceso subestacion digital"]
author: "Editor"
---

## Arquitectura de tres niveles según IEC 61850-1

IEC 61850 organiza la automatización de subestaciones en tres niveles jerárquicos, cada uno con protocolos y requisitos de latencia propios:

| Nivel | Componentes típicos | Protocolo predominante |
|---|---|---|
| **Proceso** | TI/TT digitales (MU), actuadores de interruptores | Sampled Values (SV), GOOSE |
| **Bahía** | IEDs de protección, control y medida | GOOSE, MMS/ACSI |
| **Estación** | Gateway, HMI, sistema SCADA, RTU | MMS sobre TCP/IP |

El **bus de proceso** (IEC 61850-9-2) conecta el nivel de proceso con los IEDs de bahía; el **bus de estación** (IEC 61850-8-1) conecta las bahías con el nivel de estación y con el centro de control remoto. Ambos buses corren sobre Ethernet estándar IEEE 802.3, aunque con requisitos de VLAN y QoS distintos.

La parte estructural del estándar —IEC 61850-7-2 (ACSI), IEC 61850-7-3 (Common Data Classes) e IEC 61850-7-4 (Logical Nodes)— define un modelo de datos orientado a objetos que es independiente del protocolo de comunicaciones. El mapeo a protocolos concretos se especifica en IEC 61850-8-1 (MMS para el bus de estación) e IEC 61850-9-2 (SV para el bus de proceso).

El lenguaje de configuración de subestaciones (**SCL**, definido en IEC 61850-6) usa ficheros XML con cuatro tipos principales:
- **SSD** (*System Specification Description*): especificación funcional del sistema.
- **SCD** (*Substation Configuration Description*): configuración completa de todos los IEDs y sus comunicaciones.
- **IID/CID** (*Instanced/Configured IED Description*): descripción por IED individual.
- **ICD** (*IED Capability Description*): capacidades del IED según el fabricante.

## Mensajes GOOSE: estructura, temporización y clases de rendimiento

GOOSE (*Generic Object-Oriented Substation Event*, IEC 61850-8-1) es el mecanismo de intercambio de estados y eventos entre IEDs. Se publica como trama multicast Ethernet directamente sobre la capa 2 (sin TCP/IP), lo que permite latencias en el orden de milisegundos.

**Mecanismo de retransmisión:** Tras un cambio de estado (*event*), el publicador no envía el mensaje una única vez. Transmite en ráfaga con intervalos exponencialmente crecientes para garantizar la recepción ante pérdidas de trama:

```
T₀ = 2 ms → T₁ = 2 ms → T₂ = 4 ms → T₃ = 8 ms → … → Tᵢ_max (heartbeat estable)
```

El campo `stNum` (*status number*) se incrementa en cada cambio de estado; `sqNum` (*sequence number*) se incrementa en cada retransmisión. Un suscriptor detecta pérdida de mensajes cuando `sqNum` salta más de 1 sin cambio en `stNum`.

**Clases de rendimiento según IEC 61850-5:**

| Clase | Tiempo de transferencia máximo | Aplicación típica |
|---|---|---|
| P1 | 10 ms | Distribución (protecciones no críticas) |
| P2 | 3 ms | Transmisión y distribución crítica |
| P3 | 3 ms | Protecciones de alta velocidad, transferencia de reserva |

La diferencia entre P2 y P3 reside en la disponibilidad y redundancia de red exigidas, no únicamente en el tiempo de transferencia. Los certificados de conformidad los emite DNV en base a los procedimientos de prueba GOOSE Performance de la UCAIUG (versión 1.5 en adelante). Un error habitual de diseño es asumir que cualquier switch Ethernet industrial cumple P2/P3; es obligatorio verificar el tiempo de forwarding del switch bajo carga máxima de SV y GOOSE simultáneos.

**Aplicaciones prácticas de GOOSE:**
- Transferencia de reserva automática (ATR/ARS): señal de apertura de un interruptor dispara el cierre del de reserva con latencia < 3 ms.
- Enclavamientos entre bahías: inhabilitación de cierre de seccionadores cuando la barra está energizada, sin cableado de cobre entre celdas.
- Aceleración de zona 2 en relés de distancia: al detectar fallo en protección principal, la protección de respaldo recibe GOOSE y acelera su zona 2 a tiempo mínimo.

## Sampled Values: digitalización de señales analógicas en el bus de proceso

Los Sampled Values (SV, IEC 61850-9-2) sustituyen el cableado convencional entre los secundarios de transformadores de medida (TI/TT) y los IEDs. Una **merging unit (MU)** digitaliza las señales analógicas —hasta 4 corrientes y 4 tensiones por MU— y las publica en red como tramas SV multicast.

**Tasas de muestreo definidas en IEC 61850-9-2:**

| Modo | Muestras/ciclo | Muestras/segundo (50 Hz) | Uso previsto |
|---|---|---|---|
| Protección | 80 | 4 000 S/s | Funciones de protección (PTOC, PDIS, PTOV…) |
| Medida/calidad | 256 | 12 800 S/s | Registradores de perturbaciones, analizadores de calidad |

La norma IEC 61869-9 (publicada en 2016) define una tasa de muestreo fija independiente de la frecuencia del sistema, a diferencia de IEC 61850-9-2LE donde la tasa varía con la frecuencia. Mezclar publicadores 9-2LE con suscriptores IEC 61869-9, o viceversa, es una fuente de incompatibilidad real en proyectos de modernización.

**Sincronización temporal:** Todos los MUs de una subestación deben estar sincronizados para que el suscriptor pueda alinear muestras de corrientes y tensiones de distintas bahías. IEC 61850-9-2 exige una precisión de ±1 µs. Las soluciones empleadas son:

- **PPS + IRIG-B:** señal de 1 pulso por segundo desde receptor GPS. Económico pero solo 1 µs garantizado con hardware dedicado.
- **IEEE 1588 PTP (Precision Time Protocol):** protocolo de red para sincronización a ±100 ns, preferido en subestaciones totalmente digitales. Requiere switches transparentes PTP o boundary clocks compatibles.

Un IED suscriptor que pierde sincronización debe inhibir las funciones que dependan de ángulos de fase (potencia, distancia, diferencial). La gestión de pérdida de SV debe configurarse explícitamente en cada función de protección.

## Nodos lógicos: el modelo de datos de IEC 61850-7-4

Cada función de automatización o protección se representa como un **nodo lógico (LN)** con un conjunto de atributos estandarizados. Los LN se agrupan en **dispositivos lógicos (LD)** dentro de cada IED.

Nomenclatura: `[LD].[LN_prefix][LN_class][LN_inst]`

Ejemplos de nodos lógicos más utilizados en protección:

| Clase LN | Función ANSI equivalente | Descripción |
|---|---|---|
| PTOC | 50/51 | Protección de sobreintensidad de tiempo inverso |
| PDIS | 21 | Protección de distancia |
| PSCH | 85 | Esquemas de comunicación (PLC, GOOSE) |
| PTOV | 59 | Sobretensión |
| PTUF | 81U | Baja frecuencia |
| XCBR | — | Interruptor automático (mando y supervisión) |
| XSWI | — | Seccionador |
| MMXU | — | Medida trifásica (P, Q, I, V, f, PF) |
| GGIO | — | E/S de propósito general |

La interoperabilidad entre fabricantes —uno de los objetivos centrales del estándar— se garantiza cuando cada IED describe sus LNs en el fichero ICD y la herramienta de ingeniería genera el SCD de acuerdo con IEC 61850-6.

## Criterios de selección en proyectos de subestaciones digitales

La decisión de implementar bus de proceso, bus de bahía o solución híbrida depende de varios factores técnicos y económicos:

**¿Bus de proceso completo o híbrido (hardwired + GOOSE)?**

El bus de proceso completo (SV + GOOSE para disparos) elimina prácticamente todo el cableado secundario convencional. Es óptimo en subestaciones nuevas de ≥132 kV con celdas de AT donde el cableado convencional supone costes elevados. En subestaciones de BT/MT con celdas compactas, el balance coste/beneficio puede no justificarlo; una solución híbrida (TI/TT convencionales + GOOSE para enclavamientos) es habitual.

**Selección de merging units:**
- Verificar cumplimiento de IEC 61869-9 o IEC 61850-9-2LE y consistencia en toda la subestación.
- Comprobar que la MU soporta la precisión temporal requerida (±1 µs) con la fuente de sincronización disponible.
- En subestaciones GIS, algunas MUs integran el sensor de corriente de efecto Rogowski directamente; la precisión de clase 0,2S o 5P/10P del transformador convencional debe replicarse en el sensor digital.

**Requisitos de red:**
- Switches con soporte de prioridad VLAN (802.1Q) y prioridad de tráfico (802.1p) para separar tráfico SV, GOOSE y MMS.
- Tiempo de forwarding de switch ≤ 1 ms para cumplir latencia GOOSE clase P2/P3.
- Red redundante según IEC 62439-3 (PRP o HSR) para subestaciones con requisito de disponibilidad alta; PRP (*Parallel Redundancy Protocol*) usa dos redes activas simultáneamente con conmutación en ≤ 0 ms.
- Ancho de banda: un bus de proceso con 10 MUs a 4 000 S/s y 8 bytes por muestra genera aproximadamente 2,5 Mbit/s de tráfico SV, perfectamente asumible en 100 Mbit/s, pero a 256 SPC se multiplica por 3,2.

**Cyberseguridad (IEC 62351):**
GOOSE y SV no implementan autenticación ni cifrado en sus especificaciones base. IEC 62351-6 añade autenticación HMAC-SHA256 a los mensajes GOOSE, con un overhead que puede incrementar la latencia. En subestaciones críticas es obligatorio segregar la red de automatización de cualquier red corporativa o con acceso a Internet, y monitorizar el tráfico de mensajes GOOSE contra inyección de mensajes falsos (vector de ataque documentado en el malware CrashOverride/Industroyer, que incluía un módulo específico IEC 61850).

## Conclusión

IEC 61850 no es únicamente un protocolo de comunicaciones: es un modelo de datos, un lenguaje de configuración y una arquitectura de sistema que transforma la ingeniería de subestaciones. La clave para su correcta implementación está en tres áreas: gestión de la sincronización temporal (±1 µs para SV), dimensionado de la red para latencia GOOSE clase P2/P3, y uso coherente del SCL para garantizar interoperabilidad entre IEDs de distintos fabricantes. Antes de especificar una subestación digital, verificar siempre si los IEDs seleccionados disponen de certificado UCAIUG para la clase de rendimiento GOOSE requerida, y definir explícitamente la política de fallo de SV en cada función de protección crítica.
