---
title: "ATS/ATSE: Clases y Selección según IEC 60947-6-1"
description: "Guía técnica sobre interruptores de transferencia automática ATSE: clases CB y PC, modos open/closed transition, categorías AC-33B y criterios de selección para grupos electrógenos y SAI."
pubDate: 2026-10-22
keywords: ["interruptor transferencia automatica ATS", "ATSE IEC 60947-6-1", "grupo electrogeno transferencia", "conmutacion break before make", "clase PC clase CB ATSE"]
author: "Editor"
---

El interruptor de transferencia automática (ATSE, *Automatic Transfer Switching Equipment*) es el componente que conmuta la alimentación de una instalación entre la red de distribución y una fuente de reserva —grupo electrógeno, SAI o segunda acometida— sin intervención humana. Su correcta selección afecta directamente a la continuidad de servicio, a la coordinación con las protecciones del cuadro y a la compatibilidad con la carga. La norma de referencia es **IEC 60947-6-1** (Edición 4.0, abril 2026), que unifica los criterios de ensayo y clasificación.

## Clasificación IEC 60947-6-1: clase CB y clase PC

La norma distingue dos clases de ATSE según el dispositivo de maniobra empleado:

| Clase | Dispositivo base | Poder de corte | Aplicación típica |
|-------|-----------------|---------------|-------------------|
| **CB** (Circuit Breaker) | Interruptores automáticos IEC 60947-2 | Igual al Icu/Ics del interruptor base | BT industrial, corrientes > 630 A, Icc alta |
| **PC** (Power Contactor) | Contactores o mecanismos dedicados a transferencia | Sin poder de corte propio en cortocircuito | Hasta ~3200 A, diseño monobloc optimizado para transferencia |

La clase CB utiliza dos interruptores automáticos con enclavamiento eléctrico y mecánico. Heredan el poder de corte del MCB o MCCB base, lo que los hace adecuados cuando la corriente de cortocircuito en el punto de instalación es elevada. Sin embargo, el tiempo de transferencia es típicamente mayor (50–200 ms para los contactores de maniobra del mecanismo, más el tiempo de apertura del interruptor).

La clase PC es un equipo diseñado de cero para la función de transferencia: mecanismo biestable de acción rápida, contactos dimensionados para la categoría de utilización declarada y sin poder de corte propio en fallo franco. Si se produce un cortocircuito durante la transferencia, la protección aguas arriba debe despejarlo. Por eso es fundamental coordinar el ATSE clase PC con el fusible o magnetotérmico de cabecera.

## Modos de conmutación: Open, Delayed y Closed Transition

El modo de conmutación determina si hay interrupción de servicio durante la transferencia y si las dos fuentes se solapan:

**Open Transition (break-before-make):** La fuente 1 abre antes de cerrar sobre la fuente 2. Hay una interrupción de servicio de duración igual al tiempo mecánico de transferencia, típicamente 40–200 ms según el equipo. Es el modo estándar para grupos electrógenos sin sincronización y para la mayoría de instalaciones industriales. Compatible con cargas no sensibles a microcortes.

**Delayed Transition:** Variante de la open transition en la que se introduce un retardo programable (0,5–10 s) entre la apertura de la fuente 1 y el cierre sobre la fuente 2. Imprescindible cuando la instalación incluye motores asíncronos de gran inercia (> 30 kW), ya que evita reconectar contra la tensión residual del motor todavía girando, lo que generaría sobrecorrientes transitorias y posibles daños mecánicos.

**Closed Transition (make-before-break):** Las dos fuentes se paralelizan brevemente (< 100 ms según IEC 60947-6-1 y recomendación ASCO) antes de que la fuente 1 abra. No hay interrupción de servicio. Requiere sincronismo de tensión y fase entre ambas fuentes, lo que implica un controlador con verificación de Δf < 0,2 Hz y Δϕ < 5° entre redes. Solo es aplicable con grupos electrógenos con regulación isócrona de velocidad o cuando se transfiere entre dos alimentaciones de red. **No es válido para transferencia a SAI off-line.**

## Categorías de utilización: AC-32B, AC-33A y AC-33B

Las categorías de utilización definen la capacidad del ATSE para establecer y soportar corrientes según el tipo de carga. Son análogas a las categorías de utilización de contactores (IEC 60947-4-1) pero específicas para transferencia:

| Categoría | Tipo de carga | Corriente de establec. (múltiplo de In) | Corriente de interrup. |
|-----------|--------------|----------------------------------------|------------------------|
| AC-31A/B | Carga resistiva | 1,5 × In | 1,5 × In |
| AC-32A/B | Carga inductiva mixta (cos φ 0,65) | 3 × In | 3 × In |
| **AC-33A/B** | **Motores, transformadores, cargas combinadas** | **10 × In** | **8 × In** |

El sufijo **A** indica equipos con poder de interrupción propio (clase CB); **B** identifica equipos que transfieren en carga pero sin poder de corte en cortocircuito (clase PC).

Para instalaciones industriales con motores, **AC-33B es la categoría mínima exigible**. Seleccionar un ATSE con AC-31B en una instalación con arranque directo de motores supone que los contactos de potencia no están ensayados para la corriente de establecimiento que se produce al conectar sobre la carga, lo que acorta drásticamente su vida útil.

## Lógica de detección y secuencia de transferencia

El controlador del ATSE supervisa continuamente tensión y frecuencia de la red principal. Los umbrales de disparo son programables; los valores típicos para grupos electrógenos en instalaciones españolas:

- **Subtensión de disparo:** 85 % de Vn (198 V en redes 230/400 V) sostenida durante t₁ = 0,5–3 s (retardo antiparpadeo, para no transferir ante caídas transitorias).
- **Sobretensión de disparo:** 110 % de Vn, sostenida t₁ = 0,5–1 s.
- **Fallo de frecuencia:** ± 5 % de fn (47,5–50,5 Hz según EN 50160).

Secuencia tipo para transferencia Red → Grupo:

1. **Detección de fallo** (t₁ = 1–3 s): controlador confirma que la red está fuera de límites.
2. **Orden de arranque al grupo** (t₂ = 0 s): señal 2 hilos o J1939 al GE.
3. **Estabilización del grupo** (t₃ = 5–15 s): el controlador espera que el GE alcance tensión ≥ 90 % Vn y frecuencia ≥ 49,5 Hz. Los grupos de emergencia EN 12601 deben alcanzar condiciones de carga en < 15 s.
4. **Transferencia** (t₄ = tiempo mecánico ATSE): apertura fuente 1, cierre fuente 2.
5. **Operación en grupo**: la instalación funciona con el GE.

Secuencia de retorno Red → Grupo → Red:

1. **Detección de retorno de red** (confirmación durante t₅ = 5–30 s para evitar retornos antes de que la red se estabilice).
2. **Transferencia de retorno** (modo open o closed según configuración).
3. **Parada retardada del grupo** (t₆ = 2–5 min de enfriamiento en vacío).

## Criterios de selección en obra

La selección del ATSE debe seguir estos criterios por orden de prioridad:

**1. Corriente nominal (In):**
Debe ser ≥ Ib (corriente de la instalación en uso normal). En instalaciones con alta demanda simultánea, tomar la corriente de diseño del cuadro general, no la suma de potencias instaladas.

**2. Clase del equipo:**
- Grupo electrógeno como reserva fría (arranque en parada): clase PC con open transition. La carga no requiere suministro ininterrumpido.
- SAI como reserva caliente o segunda acometida de red: clase PC con closed transition (si hay sincronismo) o clase CB si la Icc es elevada.
- Potencias > 630 A con Icc > 50 kA: valorar clase CB con Icu adecuado.

**3. Categoría de utilización:**
- Carga predominantemente resistiva o electrónica (data centers, alumbrado): AC-32B.
- Carga mixta con motores: **AC-33B obligatorio**.
- Instalaciones con arranque directo de motores grandes: verificar que el fabricante declara la corriente de establecimiento a 10 × In para AC-33B.

**4. Modo de transferencia:**
- Motores de gran inercia (> 30 kW) sin VFD: delayed transition con t_retardo ≥ 0,5 × T_mecánico del motor.
- Cargas sensibles (hospitales, salas de control): closed transition si hay dos alimentaciones de red síncronas; open transition + SAI local si la fuente es un GE.
- Instalaciones estándar: open transition.

**5. Índice de protección y temperatura:**
- Interior de cuadro IP20 o IP30 suficiente en la mayoría de los casos.
- Exterior o ambiente húmedo: IP55 mínimo.
- Temperatura ambiente > 40 °C: aplicar factor de corrección de corriente del fabricante (típicamente −0,5 % In por cada grado sobre 40 °C).

**6. Requisitos normativos específicos:**
- **ITC-BT-28** (locales de pública concurrencia): exige fuente de alimentación de seguridad con tiempo de conmutación ≤ 15 s (categoría 3) o ≤ 0,5 s (categoría 2).
- **ITC-BT-40** (generadores de baja tensión): el ATSE debe garantizar la separación eléctrica entre red y generador cuando el generador opera en isla, para protección de personal de la compañía distribuidora.
- **EN 12601** (grupos electrógenos de emergencia): el sistema de transferencia no debe retrasar la disponibilidad del grupo más allá del tiempo declarado en la clase de potencia de emergencia (G2: 10 s, G3: sin límite).

## Verificación y ensayos según IEC 60947-6-1

Los ensayos de tipo que debe superar un ATSE según IEC 60947-6-1 incluyen:

- **Ensayo dieléctrico:** 2 kV AC durante 1 min entre circuitos de potencia y de mando, y entre polos a circuito abierto.
- **Ensayo de calentamiento:** verificación de que la elevación de temperatura en bornes no supera los límites (60 K sobre ambiente para conductores de cobre) con In declarado.
- **Ensayo de endurance (durabilidad):** número de ciclos de operación eléctrica y mecánica. Para AC-33B, IEC 60947-6-1 exige un mínimo de 1000 ciclos de operación eléctrica a la corriente de categoría.
- **Ensayo de cortocircuito condicional (Icc):** para clase PC, se verifica que el equipo soporta la corriente de cortocircuito máxima declarada cuando la protección aguas arriba (fusible o magnetotérmico) actúa. Esta corriente condicional (Iq) debe ser ≥ Icc máxima en el punto de instalación.

El marcado CE del ATSE requiere declaración de conformidad con la Directiva de Baja Tensión (2014/35/UE) y, si incluye electrónica de control, con la Directiva CEM (2014/30/UE).

## Conclusión

Seleccionar un ATSE implica ir más allá del calibre nominal: clase CB o PC según la Icc del punto de instalación, categoría AC-33B cuando hay motores en la carga, modo de conmutación adecuado a la inercia de la carga y verificación del tiempo de transferencia frente a los requisitos de las ITC-BT aplicables. La corriente condicional de cortocircuito (Iq) del ATSE clase PC debe coordinarse con la protección de cabecera igual que se haría con un contactor de categoría AC-3. Un ATSE mal seleccionado que aguante el primer año puede fallar catastróficamente en el segundo ciclo de transferencia ante un arranque de motor, precisamente cuando más se necesita.
