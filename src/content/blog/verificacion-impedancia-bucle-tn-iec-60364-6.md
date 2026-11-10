---
title: "Verificación de impedancia de bucle en sistemas TN según IEC 60364-6"
description: "Cálculo de Zs máxima, tiempos de desconexión y coordinación con MCB curva B, C y D en instalaciones TN según IEC 60364-4-41 e ITC-BT-24. Guía técnica completa."
pubDate: 2026-11-10
keywords: ["verificacion impedancia bucle TN IEC 60364-6", "tiempo desconexion ITC-BT-24", "Zs maxima magnetotermico curva C", "impedancia bucle fallo TN", "IEC 60364-4-41 proteccion contacto indirecto"]
author: "Editor"
---

## Introducción: por qué la impedancia de bucle define la seguridad en TN

En un sistema TN, la protección contra contactos indirectos se basa exclusivamente en la desconexión automática de la alimentación. No hay electrodo de tierra en el receptor —el neutro está unido a tierra en el origen— por lo que cualquier defecto fase-masa genera una corriente de cortocircuito que debe activar el dispositivo de protección dentro de un tiempo prescrito. Ese tiempo depende directamente de la impedancia total del bucle de fallo (Zs): la suma de la impedancia de la fuente, el conductor de fase y el conductor de protección hasta el punto de defecto.

La verificación de Zs es un ensayo de puesta en servicio obligatorio según **IEC 60364-6** (adoptada en España como **UNE-HD 60364-6:2016**) y su cumplimiento es la demostración objetiva de que la instalación satisface los requisitos de protección del **REBT ITC-BT-24** y de **IEC 60364-4-41 (cláusula 411.4)**. Un valor de Zs superior al límite no es un aviso menor: significa que, ante un defecto real, el dispositivo de protección podría no disparar en el tiempo exigido y el receptor quedaría a tensión de contacto peligrosa durante más de lo admisible.

---

## Fundamento físico: el bucle de fallo en TN

Cuando se produce un defecto fase-masa en un sistema TN, la corriente de fallo sigue el trayecto: transformador → conductor de fase → punto de defecto → conductor de protección (PE o PEN) → neutro del transformador → transformador. Ese circuito cerrado es el bucle de fallo.

La impedancia total del bucle es:

```
Zs = Ze + (Z_fase + Z_PE)
```

Donde:
- **Ze** = impedancia externa del bucle hasta la caja de distribución (contribución de la red y el transformador)
- **Z_fase** = impedancia del conductor de fase del circuito
- **Z_PE** = impedancia del conductor de protección del circuito

La corriente de defecto que circula es:

```
If = U0 / Zs   (aproximación para ángulo de impedancia pequeño)
```

Con U0 = 230 V en BT en España. Para que el MCB dispare en su zona electromagnética (instantánea), If debe superar la corriente de disparo instantáneo Ia. De ahí el criterio fundamental de **IEC 60364-4-41 cláusula 411.4.4**:

```
Zs ≤ U0 / Ia
```

La condición equivalente desde la tensión de contacto es que la tensión que aparece en el receptor durante el defecto (UL = If × Z_PE) no supere 50 V de forma duradera. Las tablas de tiempos de la norma derivan precisamente de este límite de 50 V.

---

## Tiempos máximos de desconexión según IEC 60364-4-41 e ITC-BT-24

**IEC 60364-4-41 tabla 41.1** establece para 230 V en sistemas TN:

| Tipo de circuito | Tiempo máximo de desconexión |
|------------------|------------------------------|
| Circuitos finales ≤ 32 A (tomas de corriente, equipos portátiles) | **0,4 s** |
| Circuitos de distribución y circuitos finales > 32 A | **5 s** |

El tiempo de 0,4 s implica que el MCB debe actuar en zona electromagnética (disparo instantáneo), ya que el disparo térmico puede tardar minutos o incluso no actuar. Para la zona instantánea de un MCB según **IEC 60898-1**:
- **Curva B**: disparo instantáneo entre 3×In y 5×In → se usa 5×In como valor de verificación (caso más desfavorable)
- **Curva C**: 5×In a 10×In → se usa 10×In
- **Curva D**: 10×In a 20×In → se usa 20×In

---

## Tabla de Zs máxima por calibre y curva de MCB

Aplicando Zs ≤ 230 / Ia, con los valores máximos de la curva (peor caso):

### Curva B (Ia = 5×In)

| In (A) | Ia (A) | **Zs máx (Ω)** |
|--------|--------|----------------|
| 10     | 50     | 4,60           |
| 16     | 80     | 2,88           |
| 20     | 100    | 2,30           |
| 25     | 125    | 1,84           |
| 32     | 160    | 1,44           |

### Curva C (Ia = 10×In)

| In (A) | Ia (A) | **Zs máx (Ω)** |
|--------|--------|----------------|
| 10     | 100    | 2,30           |
| 16     | 160    | 1,44           |
| 20     | 200    | 1,15           |
| 25     | 250    | 0,92           |
| 32     | 320    | 0,72           |

### Curva D (Ia = 20×In)

| In (A) | Ia (A) | **Zs máx (Ω)** |
|--------|--------|----------------|
| 10     | 200    | 1,15           |
| 16     | 320    | 0,72           |
| 20     | 400    | 0,58           |
| 25     | 500    | 0,46           |
| 32     | 640    | 0,36           |

La curva D con calibres medios exige Zs < 0,5 Ω, lo que en instalaciones de longitud media suele requerir secciones de PE superiores a las del conductor de fase o la instalación de un diferencial en respaldo.

---

## Procedimiento de medida en campo según IEC 60364-6

**Instrumento**: el medidor de impedancia de bucle debe cumplir **IEC 61557-3** (toma de corriente de ensayo ≥ 10 mA, generalmente 20-25 A en modo no disparo de diferencial). Los equipos modernos tipo Fluke 1664FC, Metrel MI 3102H o Kyoritsu 6016 cumplen este requisito.

**Puntos de medida requeridos** (IEC 60364-6, cláusula 643.7):
1. En el origen del cuadro (Ze)
2. En el punto más alejado de cada circuito final
3. En cualquier punto donde la sección del PE cambie

**Corrección por temperatura** (cláusula crítica): el instrumento mide la impedancia con el cable a temperatura ambiente (~20 °C), pero la norma exige que el cumplimiento se verifique a temperatura de operación. Para conductores de cobre:

```
Z(70°C) = Z(20°C) × [1 + 0,00393 × (70 − 20)] ≈ Z(20°C) × 1,197
```

En la práctica se aplica un factor de corrección de **×1,25** sobre el valor medido (margen adicional de seguridad incluido) antes de compararlo con Zs máx. Este punto es el que más frecuentemente se ignora en obra y el que provoca falsos aprobados.

**Protocolo de medida**:
1. Con la instalación sin carga, desconectar el diferencial aguas arriba (o usar instrumento con función de no disparo)
2. Medir Ze en el cuadro principal entre fase y PE/N
3. Para cada circuito, medir Zs en la toma más lejana
4. Aplicar factor 1,25 y comparar con la tabla de Zs máx del MCB de cabecera

---

## Criterios de selección y diagnóstico: qué hacer cuando Zs supera el límite

### Árbol de decisión en campo

```
Zs × 1,25 ≤ Zs_max?
     │
     ├─ SÍ → CUMPLE. Registrar en informe de verificación.
     │
     └─ NO → ¿La protección es un MCB?
                │
                ├─ SÍ → Opciones (en orden de preferencia):
                │        1. Reducir longitud del circuito
                │        2. Aumentar sección del PE
                │        3. Cambiar a curva B (menor Ia para igual In)
                │        4. Instalar diferencial 30 mA en respaldo
                │
                └─ NO (fusible) → Verificar que If ≥ Ia del fusible según IEC 60269
```

### Causas frecuentes de Zs elevada

| Causa | Efecto en Zs | Solución |
|-------|-------------|----------|
| Conductor PE de sección inferior a fase en circuito largo | ↑ Z_PE significativo | Igualar o superar sección según IEC 60364-5-54 tabla 54.2 |
| Conexión de PE mediante tornillo oxidado o latiguillos mal apretados | ↑ R de contacto variable | Revisión y apriete según Nm del fabricante |
| Transformador de alta impedancia de cortocircuito Ucc > 6% | ↑ Ze desde el origen | Instalar diferencial en cuadro principal |
| Circuito muy largo en BT con sección mínima (1,5 mm²) | ↑ Z_fase + Z_PE | Redimensionar sección; calcular caída de tensión paralelamente |

La combinación más peligrosa es un MCB de curva D en circuito de motor largo con cable de 2,5 mm² y PE de 1,5 mm²: Zs resultante puede ser ×3 el límite admisible con facilidad.

### Interacción con diferenciales

Cuando el MCB no cumple el criterio de Zs, la instalación de un diferencial de 30 mA garantiza la desconexión incluso con corrientes de fallo bajas (If ≥ 150 mA activa el diferencial; con 230 V y Zs = 1,5 Ω se obtienen ~153 mA, suficiente). Sin embargo, esto no dispensa de verificar que el diferencial mismo funciona correctamente (prueba de disparo por botón de test y medida de corriente de disparo con instrumento).

---

## Conclusión

La verificación de impedancia de bucle en sistemas TN no es un trámite administrativo: es la única manera de confirmar que la protección por desconexión automática funcionará en el tiempo exigido ante un defecto real. Los puntos clave para un técnico en obra son:

1. Usar la fórmula **Zs ≤ U0 / Ia** con el peor caso de la curva del MCB (5×In para B, 10×In para C, 20×In para D)
2. Aplicar el factor de corrección térmica ×1,25 sobre el valor medido
3. Verificar con instrumento conforme a IEC 61557-3 en el punto más alejado del circuito
4. Para MCB curva D con calibres > 16 A o circuitos largos, prever diferencial de 30 mA desde el diseño
5. Registrar todos los valores en el informe de verificación inicial (IEC 60364-6, cláusula 643) y conservarlos para inspecciones periódicas

La tabla de Zs máxima por curva y calibre es la herramienta de diagnóstico rápido que todo técnico debería tener en campo junto al medidor de bucle.
