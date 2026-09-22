---
title: "Compensación de Reactiva en BT: Condensadores IEC 61921"
description: "Dimensionamiento y selección de baterías de condensadores para corrección del factor de potencia en instalaciones industriales BT según IEC 61921 y UNE-EN 61921:2025."
pubDate: 2026-09-22
keywords: ["compensacion energia reactiva condensadores industriales IEC 61921", "factor de potencia BT industrial", "bateria condensadores seleccion", "reactiva inductiva instalacion industrial"]
author: "Editor"
---

## Por qué la energía reactiva penaliza la instalación

La energía reactiva (Q, en kVAr) es consecuencia directa de cargas inductivas —motores asíncronos, transformadores, balastos electromagnéticos, reactancias de HID— que necesitan campo magnético alterno para funcionar. Este intercambio de energía entre fuente y carga no realiza trabajo útil pero circula por conductores, transformadores y embarrados, produciendo caídas de tensión y pérdidas resistivas proporcionales a I².

La magnitud del problema se expresa mediante el **factor de potencia** cosφ = P/S (cociente potencia activa/aparente). En una instalación industrial sin compensar es habitual encontrar cosφ entre 0,70 y 0,82. Las tarifas eléctricas en España (PVPC y contratos en mercado libre) aplican **penalización por reactiva** cuando el factor de potencia cae por debajo de 0,95, según establece la resolución de la CNMC para peajes de acceso y el RD 1164/2001.

El efecto técnico más relevante en MT/BT es la sobreutilización de la corriente aparente: con cosφ = 0,75, un transformador de 630 kVA suministra solo 472 kW de potencia activa útil, y la corriente de línea es un 33 % mayor que si cosφ fuera 1,0. El conductor, el interruptor automático y el transformador deben dimensionarse para esa corriente aumentada.

## Fundamentos físicos de la compensación capacitiva

Los condensadores generan corriente en cuadratura adelantada respecto a la tensión (corriente capacitiva), exactamente opuesta a la corriente reactiva inductiva. Conectar una batería de condensadores en paralelo con la carga induce una **corriente reactiva local** que ya no necesita recorrer los tramos de red aguas arriba.

La potencia reactiva que proporciona un banco de condensadores trifásico con capacidad C por fase a tensión de línea V_L y frecuencia f es:

```
Q_C = 3 · ω · C · V_fase²  =  ω · C · V_L²   [VAr]
```

Para una batería trifásica en triángulo con V_L = 400 V y C = 100 µF:

```
Q_C = 2π · 50 · 100×10⁻⁶ · 400²  ≈  5026 VAr ≈ 5 kVAr
```

La potencia reactiva a instalar para elevar el factor de potencia de cosφ₁ a cosφ₂ se obtiene de:

```
Q_C = P · (tan φ₁ − tan φ₂)   [kVAr]
```

Ejemplo: P = 200 kW, cosφ₁ = 0,78, cosφ₂ = 0,97 objetivo:
- tanφ₁ = tan(arccos 0,78) = 0,801
- tanφ₂ = tan(arccos 0,97) = 0,251
- Q_C = 200 · (0,801 − 0,251) = **110 kVAr**

## Norma IEC 61921:2017 / EN IEC 61921:2025 — Requisitos de diseño

La norma **IEC 61921 Ed. 2:2017** (transpuesta como **UNE-EN IEC 61921:2025** en España) aplica a bancos de condensadores de potencia en corriente alterna de baja tensión destinados a la corrección del factor de potencia, incluyendo los equipados con aparamenta de maniobra y control para conexión/desconexión escalonada.

La norma se alinea con **IEC 61439-1** e **IEC 61439-2** para los conjuntos de aparamenta de baja tensión que albergan la batería, e incorpora requisitos de:

- **Tensión asignada** U_n: valor nominal de la instalación (habitualmente 400 V en EU), con tolerancia ±10 % según IEC 60038.
- **Corriente de pico de conexión** (*inrush current*): los condensadores sin reactancia de protección generan corrientes de cierre de hasta 100 × I_n nominal. IEC 61921 exige que el fabricante declare el valor de pico y la frecuencia de oscilación, y que el contactor de maniobra sea del tipo *capacitor duty* con resistencias de pre-inserción o inductancia serie.
- **Sobreintensidad admisible en servicio**: IEC 61921 §5.3.3 permite que el condensador funcione permanentemente con hasta 1,3 × I_n, resultado de sobretensión de red (hasta 1,1 × U_n) más contenido armónico. La corriente eficaz real en presencia de THD_U > 5 % supera la fundamental; el condensador debe dimensionarse para la corriente total incluyendo armónicos.
- **Ensayo de temperatura**: la norma define clases de temperatura de funcionamiento (–25 °C a 55 °C máximo) y ensayo de temperatura de la envolvente conforme al Anexo D.

### Tipos de batería según modalidad de compensación

| Tipo | Descripción | Aplicación típica |
|---|---|---|
| **Fija** | Un único escalón, contactores o fusibles | Cargas constantes, iluminación industrial |
| **Automática escalonada** | Regulador PF con 4–12 escalones, contactores *cap duty* | Instalaciones con variabilidad de carga |
| **Automática con tiristores** | Conexión electrónica sin arco, ciclo < 20 ms | Cargas rápidamente variables, hornos, soldadura |
| **Con reactancia antiarmónica** (detuned) | Condensador + inductor en serie, sintonizado a f_r < 5.ª armónica | Redes con THD > 5 %, presencia de variadores VFD |
| **Filtro activo** | Inversor PWM que inyecta corriente de compensación | THD > 20 %, cargas no lineales severas |

## Reactancias antiarmónicas: dimensionamiento y sintonización

En instalaciones industriales con variadores de frecuencia, UPS, fuentes conmutadas o rectificadores, el **THD de tensión** supera habitualmente el 5 %. Los condensadores sin reactancia presentan impedancia decreciente con la frecuencia (Z_C = 1/ωC), actuando como sumidero de corrientes armónicas y recalentándose.

La solución normalizada es el banco **detuned**: inductancia L en serie con cada condensador C, que forma un circuito LC resonante a una frecuencia f_r inferior a la armónica predominante. Los valores de sintonización estandarizados son:

| Factor p (%) | f_r (Hz) a 50 Hz | Protege frente a |
|---|---|---|
| p = 5,7 % | 210 Hz (~4,2.ª) | 5.ª armónica (250 Hz) |
| p = 7 % | 189 Hz (~3,8.ª) | 5.ª armónica con margen |
| p = 14 % | 134 Hz (~2,7.ª) | 3.ª y 5.ª armónicas |

El factor p = X_L/X_C × 100 determina la tensión sobre el condensador a frecuencia fundamental, que es mayor que V_red: para p = 7 %, V_C = V_red / (1 − p/100) = 400/0,93 ≈ 430 V. El condensador debe tener **tensión nominal ≥ 440 V** (siguientes escalón normalizado: 440 V o 480 V según IEC 60831-1).

La corriente total (fundamental + armónicos) en un banco detuned p = 7 % con THD_I = 25 % puede superar 1,4 × I_fundamental, por lo que el cable de alimentación y el contactor se dimensionan con margen de 1,5 × I_n del banco.

## Criterios de selección aplicables en obra

Antes de especificar una batería de condensadores, el técnico debe registrar con un **analizador de redes** (clase A según IEC 61000-4-30 para medida de calidad) los siguientes parámetros durante al menos una semana representativa:

1. **cosφ mínimo y promedio** en horas punta de producción.
2. **THD_U y espectro armónico**: si THD_U > 3 % o existe 5.ª armónica > 2 %, especificar banco detuned.
3. **Potencia reactiva máxima** (pico) y **mínima** (horas de baja carga): define la potencia total y el número de escalones.
4. **Velocidad de variación de la carga**: si Q varía > 20 % en menos de 1 s, se requieren tiristores o filtro activo.

### Árbol de decisión para tipo de banco

```
THD_U > 5 % o 5.ª arm. > 3 %?
  Sí → Banco detuned (p = 5,7 % o 7 %)
        THD > 15 %? → Filtro activo paralelo
  No → Q varía más de 20 % en < 1 s?
         Sí → Tiristores
         No → Contactor cap-duty
               Q constante? → Banco fijo
               Q variable → Banco automático escalonado
```

### Dimensionamiento del cableado

La IEC 61921 §6.2 exige que el cable de acometida al banco se dimensione para al menos **1,36 × I_n** del banco, para absorber el contenido armónico máximo previsto (1,3 × sobretensión × 1,05 tolerancia). La sección mínima se calcula con la fórmula de ITC-BT-19 tabla 1 (instalación en bandeja o tubo), con corriente de diseño I_d = 1,36 × I_n.

Ejemplo: banco de 150 kVAr, 400 V, trifásico:
```
I_n = Q / (√3 · V_L) = 150.000 / (1,732 · 400) = 216,5 A
I_d = 1,36 · 216,5 = 294,4 A → sección 150 mm² Cu (Iz = 305 A, bandeja perforada, 40°C, ITC-BT-19)
```

### Contactor *capacitor duty*

El contactor debe ser del tipo *capacitor duty* con bobina reforzada y contactos de plata-óxido de cadmio u óxido de estaño, capaz de soportar la corriente de cierre de pico sin soldadura de contactos. La corriente de cierre sin reactancia de amortiguación puede alcanzar:

```
i_pico = V_pico / Z_c(fres)  ≈  (√2 · V_L) · √(C/L_red)
```

Para un bus de 400 V con inductancia de red L_red = 50 µH y C = 450 µF de un banco de 100 kVAr:

```
i_pico ≈ 566 · √(450×10⁻⁶ / 50×10⁻⁶) = 566 · 3 = 1.698 A ≈ 7,8 × I_n
```

Con reactancia de amortiguación (p = 7 %, L = 1,4 mH), la corriente de pico se reduce a menos de 100 A, dentro de la capacidad del contactor estándar de 250 A.

## Regulador automático de factor de potencia

El regulador mide el cosφ en tiempo real (generalmente mediante un transformador de corriente en el neutro o fase del embarrado principal) y conecta o desconecta escalones de condensadores para mantener el **cosφ objetivo** (típicamente 0,95–0,98 inductivo, nunca capacitivo para evitar sobretensiones en redes débiles).

Parámetros a configurar en el regulador:
- **C/k ratio**: relación entre la potencia del primer escalón (kVAr) y la corriente en el TC (A). Valor típico 0,1–0,5.
- **Banda muerta**: tolerancia de cosφ sin actuar (±0,02 típico).
- **Tiempo de retardo**: entre 30 s y 5 min para evitar maniobras repetidas con cargas cíclicas.
- **Modo automático/manual**: posibilidad de bloquear escalones defectuosos.

## Conclusión

La compensación de energía reactiva con baterías de condensadores en BT industrial es una inversión con retorno rápido (6–18 meses típico) que reduce la penalización tarifaria, descarga el transformador y los conductores, y mejora la calidad de tensión en los cuadros de distribución. La clave de un diseño correcto es el análisis previo de armónicos: en redes industriales con variadores o rectificadores, un banco convencional sin reactancia antiarmónica se sobreestimula, recalienta y falla prematuramente. La IEC 61921:2017/EN IEC 61921:2025 y la IEC 60831-1 proporcionan los criterios de ensayo y los parámetros de dimensionamiento que el técnico debe exigir al fabricante antes de especificar el equipo. El árbol de decisión presentado en este artículo permite seleccionar el tipo de batería adecuado —fija, automática escalonada, detuned o filtro activo— en función de los datos reales de la instalación.
