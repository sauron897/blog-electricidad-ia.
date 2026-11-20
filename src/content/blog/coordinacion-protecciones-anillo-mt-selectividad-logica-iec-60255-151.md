---
title: "Coordinación de protecciones en anillo MT: selectividad lógica IEC 60255-151"
description: "Ajuste de relés IDMT y selectividad lógica en redes MT de anillo. Curvas IEC 60255-151, señal de bloqueo ZSI, cálculo de Icc y criterios de selección en obra."
pubDate: 2026-11-20
keywords: ["coordinación protecciones anillo MT", "selectividad lógica IEC 60255-151", "curvas IDMT relé MT", "ZSI zone selective interlocking MT", "relé 67 sobreintensidad direccional"]
author: "Editor"
---

## Topología en anillo MT y problema de coordinación

En distribución de MT (1 kV < U ≤ 36 kV), el anillo normalmente abierto (NOP, *Normally Open Point*) es la configuración más habitual en distribuidoras urbanas e industriales: el anillo se alimenta desde dos subestaciones o desde dos transformadores en paralelo, con un punto de apertura que convierte la red en dos semianillos radiales. Cuando el anillo opera cerrado —distribución industrial con alta demanda de continuidad, hospitales, aeropuertos, instalaciones petroquímicas— la coordinación de protecciones se vuelve bidireccional y los métodos cronométricos puros resultan inadecuados.

El problema fundamental: en un anillo cerrado con *n* nodos, una falta en el tramo *i* provoca contribución de cortocircuito desde ambos extremos. Los relés de sobreintensidad direccional (función ANSI 67) ven la falta desde direcciones opuestas. La coordinación puramente cronométrica obliga a escalonar tiempos de disparo acumulados: si el escalón mínimo de discriminación es Δt = 0,3 s y hay cinco vanos, el relé de cabecera dispara a t = 1,5 s. Esto es incompatible con los requisitos de continuidad de suministro y con los tiempos de desconexión exigidos por IEC 60364-4-41 en sistemas MT con neutro solidamente puesto a tierra (t < 0,5 s para Uo = 20 kV en circuito TN).

## Selectividad lógica: principio y mecanismo

La selectividad lógica (también denominada *Zone Selective Interlocking*, ZSI) resuelve la limitación anterior mediante el intercambio de señales de bloqueo entre relés adyacentes, eliminando la necesidad de escalonar tiempos de retardo.

**Principio de operación:**

1. Cada relé de feeder en el anillo tiene dos salidas: función de disparo (TRIP) y señal de bloqueo (*blocking signal*, BS).
2. Cuando un relé detecta sobreintensidad superior a su umbral de pickup, activa su señal BS y la transmite al relé aguas arriba.
3. El relé aguas arriba, al recibir BS activo, retarda su disparo añadiendo un retardo de respaldo (típicamente 0,3–0,5 s adicionales).
4. El relé más cercano a la falta —que no recibe BS desde ningún relé inferior— dispara sin retardo adicional: elemento instantáneo ≈ 20–50 ms + tiempo de operación del interruptor ≈ 60–80 ms → tiempo total de despeje ≈ 80–130 ms.

Este mecanismo garantiza que solo el relé de la zona de falta actúa rápidamente, independientemente del número de escalones en el anillo.

**Señal de bloqueo según IEC 60255-151:**

IEC 60255-151 (ed. 2009, *Measuring relays and protection equipment — Part 151: Functional requirements for over/under-current protection*) define los requisitos funcionales de los relés de sobreintensidad incluyendo el mecanismo de transferencia de señales de bloqueo. La norma especifica:

- El elemento de bloqueo debe activarse en un tiempo ≤ 10 ms desde la detección de la sobreintensidad.
- La señal de bloqueo puede transmitirse por cable (señal binaria 24–250 V DC) o por protocolo de comunicación (mensajes GOOSE de IEC 61850-8-1).
- El relé aguas arriba debe aplicar el retardo de respaldo en un tiempo ≤ 2 ms desde la recepción de BS.

La implementación por **GOOSE IEC 61850** es la más común en instalaciones modernas. Los mensajes GOOSE tienen latencia típica < 4 ms (clase de rendimiento P2 según IEC 61850-5), lo que permite tiempos de bloqueo totales inferiores a 15 ms. Para instalaciones sin IEC 61850, la señal binaria cableada es la alternativa normalizada.

## Curvas IDMT y ajuste según IEC 60255-151

Las curvas de tiempo inverso (*Inverse Definite Minimum Time*, IDMT) se definen matemáticamente en IEC 60255-151 mediante la expresión general:

```
t = k · β / (M^α − 1)
```

donde:
- **t** = tiempo de operación (s)
- **k** = multiplicador de tiempo (*Time Dial Setting*, TDS)
- **M** = múltiplo de la corriente: I_falta / I_pickup
- **α, β** = constantes que definen la curva

| Curva IEC 60255-151 | α | β | Aplicación típica en MT |
|---|---|---|---|
| Normal Inverse (NI) | 0,02 | 0,14 | Alimentadores radiales, coordinación general |
| Very Inverse (VI) | 1 | 13,5 | Redes con variación de Icc alta entre nodos |
| Extremely Inverse (EI) | 2 | 80 | Coordinación con fusibles, transformadores |
| Long-time Inverse (LI) | 1 | 120 | Protección de motores síncronos grandes |

Para redes en anillo, la curva **VI (Very Inverse)** es la más empleada porque su pendiente pronunciada proporciona mayor discriminación entre la corriente de carga y la corriente de cortocircuito, facilitando el ajuste del pickup sin interferir con la carga nominal.

**Criterios de ajuste del pickup para funciones 51 (sobreintensidad no direccional) y 67 (direccional):**

```
I_pickup > 1,25 · I_nominal_línea    (evitar disparo en sobrecarga)
I_pickup < 0,80 · I_cc_min           (garantizar disparo en Icc mínimo)
I_pickup < 0,50 · I_cc_min           (margen ampliado recomendable)
```

**Ejemplo de cálculo** con cable NA2XS2Y 1×185 mm² 12/20 kV (parámetros GElectrical/IEC 60502-2):
- R = 0,161 Ω/km, X = 0,117 Ω/km → Z = 0,199 Ω/km
- Tramo de 3 km: Z_tramo = 0,597 Ω
- Icc en extremo del tramo desde subestación con Z_trafo = 0,10 Ω a 20 kV (trafo 1.000 kVA, Ucc = 6%):
  - Z_total = 0,10 + 0,597 = 0,697 Ω
  - I_cc_max = 20.000 / (√3 · 0,697) ≈ **16.600 A**
  - Con alimentación desde ambos extremos del anillo, contribución simétrica: I_cc_min ≈ **8.300 A**
- I_nominal cable: 362 A (IEC 60502-2 en servicio permanente)
- I_pickup recomendado: max(1,25 × 362; 0,50 × 8.300) = max(452; 4.150) → **I_pickup = 500 A** (ajuste normalizado próximo)
- TDS para t = 0,3 s a M = 16.600 / 500 = 33,2 con curva VI:
  - t = k × 13,5 / (M − 1) → k = 0,3 × 32,2 / 13,5 = **0,715**

## Coordinación en anillo cerrado con relés direccionales 67

En un anillo cerrado, cada protección debe distinguir la dirección del flujo de falta. La función ANSI 67 compara el ángulo de fase entre la tensión de polarización y la corriente de falta:

- **Zona hacia adelante (forward)**: 90° − θ < arg(V/I) < 90° + θ, con θ = ángulo de impedancia de la línea. Para cables MT XLPE, θ típicamente 70–80°.
- **Zona hacia atrás (reverse)**: el relé ve la corriente en sentido contrario y permanece bloqueado.

La combinación **67 + selectividad lógica ZSI** actúa en tres fases:
1. La función 67 identifica la dirección de la falta y activa el elemento de disparo solo en la dirección correcta.
2. La señal BS bloquea los relés adyacentes que ven la misma falta desde la dirección opuesta.
3. Solo los dos interruptores que encuadran el tramo afectado despegan en < 150 ms.

La función de falta a tierra direccional (67N) opera de forma análoga, usando la tensión de secuencia cero como polarización, especialmente relevante en redes con neutro compensado (bobina de Petersen) donde las corrientes de falta a tierra son reducidas (típicamente 20–50 A).

## Comparativa: selectividad cronométrica frente a lógica

| Criterio | Cronométrica | Selectividad lógica (ZSI) |
|---|---|---|
| Tiempo de despeje cabecera (5 tramos) | 1,5–2,0 s | 80–150 ms |
| Comunicación entre relés requerida | No | Sí (GOOSE o señal binaria) |
| Sensibilidad a variación de Icc | Alta | Baja |
| Aplicación en anillo cerrado | Limitada | Óptima |
| Aplicación en anillo abierto (NOP) | Válida | Recomendable |
| Fallo del canal de comunicación | No aplicable | Recae en cronométrica de respaldo |
| Coste de implantación | Bajo | Medio-alto |
| Requisito IEC 61850 | No | Recomendado (no obligatorio) |

La tabla refleja la ventaja principal de ZSI: reducir el tiempo de despeje en cabecera de 1,5–2,0 s a menos de 150 ms sin modificar el hardware de los interruptores, simplemente añadiendo el canal de señalización entre relés.

## Criterios de selección y diagnóstico en obra

**Usar selectividad lógica cuando:**
- El anillo MT opera cerrado de forma continua (doble alimentación activa simultánea).
- Hay más de tres vanos sin punto de apertura estable.
- Se requiere tiempo de despeje < 500 ms con más de dos niveles de protección coordinados.
- Existe generación distribuida conectada al anillo (flujo bidireccional de cortocircuito).
- Se exige continuidad N-1: cada tramo puede aislarse sin pérdida total del suministro.

**La cronométrica es suficiente cuando:**
- El anillo opera normalmente abierto (NOP), funcionando como dos semianillos radiales.
- Hay tres vanos o menos y el escalón Δt = 0,3 s no supera t = 1,0 s en cabecera.
- No hay infraestructura de comunicaciones o los relés existentes carecen de función 67.

**Ajuste del retardo de respaldo en ZSI:**
- Retardo en recepción de BS activo: t_BS = 0,3–0,5 s (distingue señal espuria de falta real aguas abajo).
- Tiempo de operación sin recepción de BS: t_inst ≤ 50 ms (elemento instantáneo 50).
- Retardo de respaldo si se pierde el canal de comunicación: mantener curva VI con TDS ajustado para garantizar coordinación cronométrica como red de seguridad (IEC 60255-151 cláusula 7.2.2: el relé debe mantener protección de respaldo funcional en ausencia de señal de bloqueo).

**Verificación en comisionado:**
- Inyección secundaria de corriente con rampa de tiempo para verificar curva IDMT real frente a la teórica de IEC 60255-151 (tolerancia admisible: ±5% en tiempo para M > 2).
- Prueba del canal de bloqueo: simulación de falta con BS activo para confirmar retardo de respaldo en el relé aguas arriba (IEC 60255-151 cláusula 8.1.4).
- Comprobación de direccionalidad: inyección con ángulo de polarización en zona forward y reverse para validar la selectividad de la función 67.

## Conclusión

La selectividad lógica según IEC 60255-151 es la solución técnica para redes MT en anillo cerrado donde la coordinación cronométrica compromete los tiempos de despeje y la continuidad de suministro. Su implantación correcta exige relés con función 67 y soporte de señal de bloqueo, ajuste de curvas IDMT —preferentemente VI— con pickup verificado contra los parámetros reales de impedancia de línea según IEC 60502-2, y un canal de comunicación fiable: GOOSE IEC 61850 en instalaciones nuevas o señal binaria cableada en instalaciones existentes.

Quienes gestionan redes de distribución industrial con generación distribuida conectada deben revisar sus ajustes existentes. La presencia de inversores fotovoltaicos o grupos de cogeneración modifica la contribución de Icc en cada nodo y puede invalidar la jerarquía de disparo cronométrico diseñada para flujo unidireccional.
