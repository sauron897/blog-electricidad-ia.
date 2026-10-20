---
title: "Grupo de conexión transformadores: Dyn11 vs Yz11 IEC 60076"
description: "Notación IEC 60076-1, desfase vectorial, impacto en cortocircuitos y armónicos de Dyn11 y Yz11. Criterios de selección para técnicos e ingenieros eléctricos."
pubDate: 2026-10-20
keywords: ["grupo conexion transformador Dyn11 IEC 60076", "grupo vectorial transformador distribución", "diferencia Dyn11 Yz11 transformador", "desfase fase transformador MT BT", "grupo conexion transformador cortocircuito"]
author: "Editor"
---

El grupo de conexión de un transformador determina la topología de los devanados, el desfase vectorial entre sus tensiones y el camino que siguen las corrientes de secuencia cero ante un fallo a tierra. Para el ingeniero de protecciones o el técnico de subestación, ignorar este parámetro equivale a coordinar protecciones sobre un modelo de fallo incorrecto. IEC 60076-1 y su adopción UNE-EN 60076-1 fijan la notación; la elección entre Dyn11, Yz11 u otros grupos tiene consecuencias directas en la Icc monofásica, en la propagación de armónicos y en la posibilidad de trabajo en paralelo.

## Notación IEC 60076-1: cómo leer el código de grupo

La codificación sigue tres bloques concatenados:

**Bloque 1 — Conexión del devanado AT (mayúscula):**
- `D` = triángulo (delta)
- `Y` = estrella (wye) sin neutro accesible
- `YN` o `Y` con neutro = estrella con neutro

**Bloque 2 — Conexión del devanado BT (minúscula):**
- `d` = triángulo
- `y` = estrella
- `yn` = estrella con neutro accesible
- `z` = zigzag
- `zn` = zigzag con neutro accesible

**Bloque 3 — Índice horario (0–11):**
Indica cuántas posiciones de reloj adelanta el vector de tensión del devanado BT respecto al AT, tomando cada hora como 30°. El índice 11 equivale a un retraso de 330° (o un adelanto de 30°).

Así, `Dyn11` se lee: devanado AT en triángulo, devanado BT en estrella con neutro accesible, desfase BT→AT de −330° (el vector de la fase A en BT apunta a las 11 en el reloj si AT apunta a las 12).

| Código | AT | BT | Desfase (°) | Neutro BT |
|--------|----|----|-------------|-----------|
| Dyn11  | △  | Y+N | 330 (−30)  | Sí |
| Dyn1   | △  | Y+N | 30          | Sí |
| Yzn11  | Y  | Z+N | 330 (−30)  | Sí |
| Dd0    | △  | △  | 0           | No |
| Yy0    | Y  | Y  | 0           | Solo si AT conectado |
| Dy11   | △  | Y  | 330         | No |

Solo pueden funcionar en paralelo transformadores con idéntico índice horario (o índices que supongan el mismo desfase resultante). Un Dyn11 y un Dyn1 tienen desfases de 30° opuestos: conectarlos en paralelo circula una corriente de circulación proporcional a 2·Un/√3 ÷ 2·Zcc, que destruye las bobinas en segundos.

## Dyn11 en distribución MT/BT: comportamiento ante fallos y armónicos

`Dyn11` es el grupo estándar de prácticamente todas las compañías distribuidoras españolas para centros de transformación de distribución (REBT ITC-BT-06 no especifica el grupo, pero los pliegos técnicos de distribución —Endesa, Iberdrola, i-de— lo exigen como estándar para CT de distribución 20 kV / 400 V).

### Secuencia cero y fallo fase-tierra

La conexión en triángulo del devanado AT actúa como camino cerrado para las corrientes de secuencia cero generadas en BT. Ante un fallo fase-tierra en el secundario:

1. La corriente de fallo (componente de secuencia cero) circula por las tres fases BT hacia el neutro.
2. En el devanado AT triangulado, estas corrientes de secuencia cero se transforman en corrientes de circulación dentro del triángulo.
3. **Resultado:** ninguna corriente de secuencia cero aparece en la red MT. El transformador actúa como barrera de secuencia cero.

Para el cálculo de Icc monofásica (fase-tierra) en el secundario de un Dyn11, la impedancia de secuencia homopolar Z₀ ≈ Z₁ (impedancia de secuencia positiva). Aplicando la red de secuencia según IEC 60909-0:

```
Icc1φ = (√3 · Un) / (Z1 + Z2 + Z0)

Con Z1 = Z2 = Z0 = Zcc del transformador:
Icc1φ ≈ Icc3φ  (dentro de ±5% según relación X/R)
```

En la práctica, para un transformador de 630 kVA, 20/0,4 kV, Ucc = 4%:

- Z₁ = Ucc/Sn × Un² = 0,04 × (400²/630.000) = **10,16 mΩ**
- Icc3φ ≈ Un / (√3 · Z₁) = 400 / (√3 × 10,16 × 10⁻³) ≈ **22,7 kA** (sin impedancia de red)
- Icc1φ ≈ 22,7 kA (Z₀ ≈ Z₁ en Dyn11)

### Armónicos de orden 3 y múltiplos

El devanado triangulado en AT proporciona un camino de baja impedancia para las corrientes de 3.º, 9.º y 15.º armónico (secuencia homopolar). Estas corrientes circulan dentro del triángulo y no se propagan a la red MT. Esto es especialmente relevante en edificios de oficinas o centros comerciales donde cargas monofásicas no lineales (fuentes conmutadas, iluminación LED, VFDs monofásicos) inyectan tercer armónico en el neutro BT.

## Yzn11: zigzag y baja impedancia de secuencia cero

El devanado zigzag se construye conectando en serie dos semidevanados de fases distintas con polaridades opuestas. Cada bobina de fase en BT está formada por mitades de dos columnas del núcleo.

**Consecuencia directa:** para corrientes de secuencia cero, los flujos de las dos semibobinas en cada columna se cancelan parcialmente. La impedancia homopolar resultante es:

```
Z₀(Yzn) ≈ Z₁ / 3  (aproximación conservadora: entre 0,3·Z₁ y 0,4·Z₁)
```

Esto implica que, ante el mismo fallo fase-tierra, la Icc1φ en el secundario de un Yzn11 es significativamente mayor que en un Dyn11:

```
Icc1φ(Yzn11) = (√3 · Un) / (Z1 + Z2 + Z0)
             ≈ (√3 · Un) / (Z1 + Z1 + Z1/3)
             = (√3 · Un) / (2,33 · Z1)
             ≈ 1,28 · Icc3φ
```

Esta mayor corriente de fallo es una ventaja cuando el sistema BT es de esquema IT y se busca que el primer fallo a tierra produzca suficiente corriente para actuar la protección de sobreintensidad de respaldo, pero es un inconveniente si los cables de tierra no están dimensionados para ello.

### Valores de Ucc normalizados (IEC 60076-3)

La tensión de cortocircuito Ucc —que determina directamente la impedancia de cortocircuito— tiene valores mínimos normalizados según la potencia:

| Potencia nominal | Ucc mínimo (IEC 60076-3) |
|-----------------|--------------------------|
| ≤ 630 kVA | 4 % |
| > 630 kVA hasta 2 500 kVA | 6 % |
| > 2 500 kVA hasta 6 300 kVA | 7 % |
| > 6 300 kVA | 8 – 12 % según diseño |

Ucc bajo → mayor Icc en bornes BT → mayor solicitación dinámica de las conexiones y mayor exigencia al poder de corte de los interruptores aguas abajo.

## Paralelo de transformadores: condiciones de grupo

Dos transformadores pueden operarse en paralelo cuando, además de igual relación de transformación y Ucc similares (diferencia ≤ 10% según IEC 60076-1), comparten el mismo índice horario. Los grupos de la misma familia son:

- **Grupo 0** (desfase 0°): Yy0, Dd0, Dz0
- **Grupo 11** (desfase −30°): Dyn11, Yz11, Yd11, Dy11
- **Grupo 1** (desfase +30°): Dyn1, Yz1
- **Grupo 5** (desfase −150°): Yd5, Dy5, Yz5

Dentro de cada grupo, la diferente topología (Dyn11 con Yd11) no introduce desfase, pero sí puede alterar las impedancias de secuencia cero: verificar con la simulación de la red de secuencia antes de conectar en paralelo unidades de distinta topología.

## Criterios de selección en obra

| Aplicación | Grupo recomendado | Justificación |
|------------|------------------|---------------|
| CT distribución urbana/industrial BT TN-S | **Dyn11** | Estándar compañías distribuidoras; aísla secuencia cero de red MT; suprime 3.º armónico |
| Alimentación de alumbrado público o cargas monofásicas intensas | **Dyn11** | Neutro robusto; circulación de armónicos homopolares en triángulo AT |
| Transformador de puesta a tierra (earthing transformer) | **Yzn11** | Z₀ baja → proporciona punto neutro en redes sin neutro existente |
| Cargas con alta distorsión 3.º armónico en BT IT | **Yzn11** | Camino de retorno de secuencia cero sin saturar el cable de neutro |
| Paralelo con transformador existente Dyn11 | **Dyn11 mismo fabricante** | Igualar Ucc y relación de transformación; verificar Z₀ si son fabricantes distintos |
| Tracción ferroviaria (reducción armónicos 12 pulsos) | **Yd5 + Dy11** | Desfase 30° entre los dos grupos elimina armónicos 5.º y 7.º en el punto de conexión |
| Generador síncrono en paralelo con red Dyn11 | **Verificar grupo del generador** | El grupo del transformador elevador del generador debe ser compatible con el grupo del sistema |

En instalaciones industriales con variadores de frecuencia (VFDs) en gran cantidad, la solución más económica no es siempre Yz11: un transformador de aislamiento Dyn11 con pantalla electrostática entre devanados (IEC 60076-1, cláusula 9) bloquea la corriente de modo común generada por los VFDs y puede ser suficiente sin recurrir al zigzag.

## Conclusión

El grupo de conexión no es un dato de placa irrelevante: determina el comportamiento del transformador ante fallos asimétricos, la circulación de armónicos de secuencia cero y las condiciones de paralelo. Para distribución MT/BT en España, Dyn11 es la opción estándar porque aísla la red MT de la secuencia cero del secundario, suprime el tercer armónico en AT y proporciona neutro BT sólido. Yz11 tiene su lugar cuando se necesita Z₀ baja en BT (transformador de puesta a tierra, redes BT IT con alta distorsión) o en pequeños transformadores donde el coste del zigzag es aceptable. Verificar siempre con IEC 60909-0 el reparto de Icc1φ según Z₀ real antes de seleccionar los dispositivos de protección en BT.
