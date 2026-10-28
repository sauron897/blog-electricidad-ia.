---
title: "Protección generadores síncronos BT: ANSI 40, 46 y 51V"
description: "Funciones ANSI 40, 46 y 51V en generadores síncronos de baja tensión: principio físico, ajuste numérico y coordinación según IEC 60255. Para técnicos e ingenieros."
pubDate: 2026-10-28
keywords: ["proteccion generador sincrono ANSI IEC 60255", "ANSI 40 perdida excitacion", "ANSI 46 secuencia negativa generador", "51V sobrecorriente control tension generador BT"]
author: "Editor"
---

Los generadores síncronos de baja tensión (230/400 V, 690 V) —grupos electrógenos de emergencia, unidades de cogeneración, GD conectada al bus BT de una subestación— presentan modos de fallo específicos que las protecciones estándar de red no cubren. Las tres funciones ANSI que más se aplican en este rango de potencia (desde ~50 kVA hasta varios MVA) son la **40** (pérdida de excitación), la **46** (desequilibrio de corriente / secuencia negativa) y la **51V** (sobrecorriente temporizada con control o restricción de tensión). Las tres están normalizadas en la familia IEC 60255 y deben coordinarse entre sí y con las protecciones de la red.

---

## ANSI 40 — Pérdida de excitación (Loss of Field)

### Mecanismo físico

Cuando el campo de excitación se debilita o desaparece —por fallo del excitador, cortocircuito del devanado de campo o apertura accidental del AVR— el generador pierde la capacidad de suministrar potencia reactiva. La máquina entra en régimen asincrónico: absorbe reactiva de la red, las corrientes de inducción en el rotor disparan las pérdidas y la temperatura del núcleo y del devanado de campo sube rápidamente. En máquinas de rotor de polos lisos el calentamiento puede ser crítico en **menos de 30 s** si P > 0,3 Pu.

### Implementación y ajuste (IEC 60255-187-1)

La función 40 se implementa clásicamente como un elemento de impedancia que opera cuando el vector Z medido en bornes del generador entra en una característica circular definida en el plano R-X:

- **Centro de la característica**: −j·(Xd + Xd')/2 (en el eje −X puro)  
- **Radio**: (Xd − Xd')/2  
- **Desplazamiento (offset)**: suele fijarse en −j·Xd'/2 para evitar disparos por oscilación de potencia

Para un generador BT típico de 500 kVA, 400 V, Xd = 2,1 pu, Xd' = 0,22 pu, la característica da:

| Parámetro | Valor ejemplo |
|-----------|--------------|
| Centro en eje −jX | −j·1,16 pu |
| Radio | 0,94 pu |
| Offset en pu (base In, Vn) | −j·0,11 pu |

El temporizador de alarma se ajusta en **t₁ = 1–3 s**; el de disparo definitivo en **t₂ = 5–10 s** si el sistema puede tolerar operación asincrónica breve, o en **t₂ < 1 s** si la potencia de corto circuito de la red es baja (< 10 × Sn) y el riesgo de pérdida de estabilidad es inmediato.

---

## ANSI 46 — Desequilibrio de carga y corriente de secuencia negativa

### Mecanismo físico

Una componente de secuencia negativa I₂ en la corriente de estátor genera un campo giratorio inverso a 2f respecto al rotor. Las corrientes inducidas en la superficie del rotor —hierro macizo en cilíndricos, cabezas de bobinas de campo, cuñas de ranura— no pueden disiparse fácilmente y producen un calentamiento localizado proporcional a I₂²·t. La capacidad térmica admisible de la máquina se normaliza como:

```
K = I₂² · t   (en unidades normalizadas sobre In)
```

Los valores de K dependen del diseño del rotor:

| Tipo de máquina | K (IEC / IEEE C37.102) |
|-----------------|------------------------|
| Generador de polos lisos ≤ 800 MVA | 10 |
| Generador de polos lisos > 800 MVA | 5–8 (depende de ventilación) |
| Generador de polos salientes < 10 MVA | 40 |
| Generador de polos salientes > 10 MVA | 20–30 |

Para grupos electrógenos BT de polos salientes (< 2 MVA), K = 40 es el valor estándar de diseño.

### Ajuste según IEC 60255-26 / IEC 60255-151

El relé implementa una **alarma de desequilibrio** a un umbral I₂/In ≥ 8–10 % con retardo de 5–10 s (desequilibrio continuado de carga no simétrica, por ejemplo arranque de un gran motor monofásico), y un **disparo** mediante la curva acumulada I₂² · t = K:

- Umbral de arranque del integrador: I₂/In ≥ 5 % (filtrar ruido de medida)
- La curva IEC 60255 tipo **muy inversa** sobre I₂ se usa como respaldo si el fabricante no parametriza directamente K
- Corriente máxima continua admisible: I₂/In ≤ 0,10 (10 % de In) según IEEE C37.102

En un generador BT de 630 kVA / 400 V / In = 909 A (relación TC 1000/5 A), un desequilibrio del 12 % durante 28 s supera el umbral térmico (0,12² × 28 = 0,40 ≈ K/100 para K = 40 en pu), por lo que el relé debe disparar antes.

---

## ANSI 51V — Sobrecorriente temporizada con control de tensión

### Por qué no basta una 51 convencional

La corriente de cortocircuito de un generador síncrono cae rápidamente desde el pico subtransitorio (Icc'' ≈ Vn/Xd'' · In) hasta el valor estacionario (Icc ≈ Vn/Xd · In), que puede estar **por debajo de la corriente nominal de plena carga**. Una protección de sobreintensidad ajustada por encima de In no arrancaría ante una falla en bornes con la máquina operando bajo carga parcial.

### Las dos variantes (IEC 60255-151)

**51VC — Voltage Controlled (control de tensión):**  
El elemento de sobreintensidad se activa (se habilita) únicamente cuando la tensión medida cae por debajo de un umbral Vt_set, típicamente 70–80 % Vn. Por encima de ese umbral, el elemento queda bloqueado. El pickup de corriente se fija en 50–75 % de In.

**51VR — Voltage Restrained (restricción de tensión):**  
El pickup de corriente varía linealmente con la tensión medida entre dos extremos:
- Con V = 100 % Vn → Ip = 100–150 % In
- Con V = 0 % Vn → Ip = 25–50 % In (fijado para detectar cortocircuito con máquina demagnetizada)

| Variante | Ventaja | Inconveniente |
|----------|---------|---------------|
| 51VC | Lógica simple, ajuste único de pickup | Puede no arrancar si Vt > umbral pese a falla incipiente |
| 51VR | Cobertura continua; responde a todo el rango de Vt | Mayor complejidad de ajuste; riesgo de solapamiento con 50 |

En BT, la 51VC es más frecuente por la sencillez del ajuste. La curva IEC usada es habitualmente **muy inversa** (type B, IEC 60255-151), con TMS = 0,2–0,5 s para garantizar selectividad con las protecciones de red (normalmente ajustadas en TMS = 0,5–1,0 s).

### Ejemplo numérico de ajuste 51VC

Generador: 400 kVA, 400 V, Xd = 1,9 pu, Xd'' = 0,18 pu, In = 577 A  
TC: 600/5 A  
Falla en bornes (régimen permanente): Icc_est = In/Xd = 577/1,9 = **304 A** (< In)  
Pickup propuesto: Ip = 0,60 × In = 346 A → relación secundaria = 346/600 × 5 = **2,88 A** en TC  
Umbral de tensión de control: Vt_set = 0,75 × 400 = **300 V**  
TMS curva muy inversa IEC: 0,30 s (coordinar con fusibles del cuadro de distribución BT)

---

## Criterios de selección e integración en el esquema de protección

La elección del relé y la configuración de las tres funciones depende de:

| Criterio | Consideraciones |
|----------|----------------|
| Potencia del generador | < 500 kVA: relé multifunción compacto (ej. SEL-300G, REF615); > 1 MVA: relé dedicado con SCADA |
| Conexión a red (paralelo / isla) | En paralelo: ajuste 40 más sensible; en isla: 51VC puede relajarse porque no hay respaldo de red |
| Tipo de rotor | Polos salientes (K = 40): función 46 con mayor margen de tiempo; cilíndricos (K = 10): respuesta más rápida |
| AVR y excitador | Existencia de señal de fallo de AVR como entrada digital al relé mejora el tiempo de respuesta de la función 40 |
| Curva de capacidad | El diagrama P-Q del fabricante define la zona de operación sin excitación estable; usarla para validar el ajuste de la característica 40 |

### Secuencia de ajuste recomendada

1. Obtener del fabricante: Xd, Xd', Xd'', X₂, constante K térmica
2. Ajustar función **40** sobre la característica de reactancia de la máquina
3. Fijar función **46** con K del fabricante; si no disponible, usar K = 20 como conservador para polos salientes
4. Ajustar función **51V** (variante VC o VR) con Ip < Icc_est para garantizar arranque
5. Verificar selectividad con la protección de barras BT: la 51V debe disparar antes que la interrupción de aislamiento de la red

---

## Conclusión

Las funciones ANSI 40, 46 y 51V constituyen el núcleo mínimo de protección de cualquier generador síncrono BT conectado a red. La función 40 actúa sobre la impedancia de la máquina para detectar pérdida de campo antes de que el rotor alcance temperatura crítica; la función 46 integra el calentamiento por desequilibrio con el modelo I₂²·t = K de IEC; y la 51V resuelve el problema de la caída de Icc del generador mediante la lógica de control o restricción de tensión. Los valores de ajuste no son genéricos: dependen de las reactancias de la máquina, del tipo de rotor y de la configuración de red (paralelo o isla). El primer paso siempre es obtener los datos de placa y la hoja de parámetros del fabricante, y contrastar los ajustes del relé con el diagrama P-Q y las curvas de capacidad del generador.
