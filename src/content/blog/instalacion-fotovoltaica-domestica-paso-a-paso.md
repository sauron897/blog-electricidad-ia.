---
title: "Instalación fotovoltaica doméstica: paso a paso técnico"
description: "Guía técnica para instaladores: dimensionado de strings, sección de cable DC/AC, protecciones y normativa IEC 62548, UNE-HD 60364-7-712 y RD 244/2019."
pubDate: 2026-07-22
keywords: ["instalacion fotovoltaica domestica", "IEC 62548 cable fotovoltaico", "dimensionado string fotovoltaico", "autoconsumo fotovoltaico normativa"]
author: "Editor"
---

Una instalación fotovoltaica de autoconsumo doméstico no es un conjunto de paneles en el tejado: es un sistema eléctrico de generación que opera en paralelo con la red de distribución y que está sujeto a los mismos principios de diseño —y a más normativa específica— que cualquier instalación de baja tensión. El Real Decreto 244/2019 y la norma técnica **UNE-HD 60364-7-712** (transposición de IEC 60364-7-712) son el marco de referencia en España, y su correcta aplicación es lo que separa una instalación segura y legalizable de una que falla el primer verano o genera problemas con la distribuidora.

Este artículo aborda el proceso de diseño desde los parámetros eléctricos del módulo hasta las protecciones AC, siguiendo la secuencia que aplica un instalador habilitado en categoría B del REBT.

## Normativa aplicable: RD 244/2019, UNE-HD 60364-7-712 e IEC 62548

El marco normativo para autoconsumo fotovoltaico en España suma varias capas:

- **RD 244/2019**: régimen de autoconsumo eléctrico, modalidades (con y sin excedentes), procedimientos de conexión y compensación simplificada de excedentes.
- **REBT – ITC-BT-40**: instalaciones generadoras de baja tensión. Define requisitos de protección, seccionamiento y conexión a red para generadores de BT.
- **UNE-HD 60364-7-712:2018**: requisitos específicos para sistemas FV (transposición de IEC 60364-7-712:2017). Aplica al diseño del lado DC de la instalación.
- **IEC 62548:2016** (UNE-EN 62548): requisitos de instalación y seguridad de generadores FV. Define los coeficientes de corriente para dimensionado de cable y fusibles de string.
- **EN 50549-1:2019**: requisitos para instalaciones de generación conectadas en baja tensión, en particular la función de protección anti-islanding.
- **IEC 61215 / IEC 61730**: cualificación y seguridad de módulos FV de silicio cristalino. Los módulos deben llevar marcado CE con estas normas como base.

La **ITC-BT-23** del REBT se aplica al lado AC, concretamente en la elección del tipo de interruptor diferencial. La ITC-BT-18 regula la puesta a tierra de estructuras metálicas.

## Dimensionado del generador FV: cálculo de strings

El parámetro crítico en el lado DC es la **tensión de string**, que varía inversamente con la temperatura del módulo. A temperaturas bajas (invierno), la tensión aumenta y puede superar el límite del inversor; a temperaturas altas (verano), desciende y puede salir del rango MPPT.

**Tensión máxima de string** (verifica el límite de entrada del inversor):

```
Vstring_max = Voc_STC x [1 + gamma_Voc x (Tmin - 25)]
```

Donde:
- `Voc_STC`: tensión en circuito abierto en condiciones estándar (1000 W/m², 25 °C)
- `gamma_Voc`: coeficiente de temperatura de Voc (valor típico: -0,30 %/°C a -0,38 %/°C)
- `Tmin`: temperatura mínima histórica del emplazamiento. En España peninsular se recomienda -10 °C como valor conservador.

**Ejemplo práctico** con módulo de 430 Wp:
- Voc_STC = 41,2 V; gamma_Voc = -0,33 %/°C
- Voc a -10 °C = 41,2 x [1 + (-0,0033) x (-10 - 25)] = 41,2 x 1,1155 = **45,96 V por módulo**

Para un inversor monofásico con Vmax_DC = 600 V:
- Módulos máximos en serie = 600 / 45,96 = **13 módulos**

La **tensión mínima de string** verifica el arranque del MPPT en verano. Con temperatura de módulo estimada a 65 °C (Tambiente = 40 °C + 25 °C por irradiancia) y Vmpp_STC = 34,2 V, gamma_Vmpp = -0,40 %/°C:
- Vmpp a 65 °C = 34,2 x [1 + (-0,0040) x (65 - 25)] = 34,2 x 0,84 = **28,7 V por módulo**

Este valor multiplicado por el número de módulos en serie debe quedar dentro del rango MPPT del inversor (habitualmente 150-560 V en monofásicos de 5 kW).

## Sección de cable DC y AC según IEC 62548

### Cable DC (ramal de string)

La corriente de diseño para dimensionar los conductores del string viene dada por **IEC 62548, cláusula 8**:

```
Id_DC = 1,4 x Isc_STC
```

El factor 1,4 incorpora un margen del 1,25 por irradiancia superior a STC (hasta 1250 W/m²) más un factor de seguridad adicional. A esta corriente se aplican los factores de corrección de la UNE-HD 60364-5-52 (temperatura ambiente, agrupamiento).

| Módulo | Potencia (Wp) | Isc_STC (A) | Id_DC = 1,4 x Isc (A) | Sección Cu mínima | Cable |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Estándar | 400 | 10,5 | 14,7 | 4 mm² | H1Z2Z2-K 4 mm² |
| Alta potencia | 550 | 13,9 | 19,5 | 6 mm² | H1Z2Z2-K 6 mm² |
| Bifacial | 700 | 17,0 | 23,8 | 6 mm² | H1Z2Z2-K 6 mm² |

El cable DC debe ser de tipo **solar** conforme a **UNE-EN 50618** (designación H1Z2Z2-K): doble aislamiento XLPE, rango de temperatura -40 °C / +90 °C, resistente a UV y humedad. El uso de cable tipo H07V-K en canalizaciones exteriores DC es una no-conformidad frecuente detectada en revisiones de instalaciones.

La caída de tensión en el ramal DC debe mantenerse por debajo del **1 % del Vmpp del string** para no penalizar el rendimiento del MPPT.

### Cable AC (inversor al cuadro de protección)

Se calcula según **ITC-BT-19** y **UNE-HD 60364-5-52:2022**. La corriente nominal del inversor es el dato de partida:

```
In_inv = Pac_inv / (V_fase x cos_phi)          [monofásico]
In_inv = Pac_inv / (sqrt(3) x V_L x cos_phi)   [trifásico]
```

Para un inversor monofásico de 5 kW con cos phi = 1:
- In_inv = 5000 / 230 = **21,7 A** — sección mínima **6 mm² Cu** en instalación bajo tubo empotrado (método B2, XLPE).

La mayoría de especificaciones técnicas de acceso a red limitan la caída de tensión en el ramal de generación a **1,5 %** máximo.

## Protecciones CC y CA

### Fusibles de string (DC)

La **IEC 62548, Anexo E** detalla cuándo son obligatorios. La regla esencial:

Los fusibles de string son **necesarios** cuando existen **3 o más strings en paralelo** y la corriente máxima de retroceso admisible del módulo (típicamente 15-20 A según ficha técnica) podría ser superada por la aportación de los demás strings ante un fallo en uno de ellos.

Con 2 strings en paralelo, la corriente de retroceso es igual a Isc de un único string y no supera el límite del módulo. Con 3 o más, el cálculo es obligatorio.

Calibre del fusible cuando son necesarios:
```
1,5 x Isc_STC  ≤  In_fusible  ≤  2,4 x Isc_STC
```

### Interruptor-seccionador general DC

Obligatorio por **UNE-HD 60364-7-712, cláusula 712.462.2**: debe permitir el seccionamiento y la apertura bajo carga de toda la parte DC del generador respecto al inversor. Debe ser apto para DC y para la tensión máxima de string calculada.

### Diferencial AC: tipo A obligatorio (ITC-BT-23)

Los inversores de string **transformerless** (la mayoría de los actuales) pueden inyectar componentes de corriente continua pulsante en la red AC. La **ITC-BT-23** exige usar un interruptor diferencial **tipo A** (sensible a corriente alterna senoidal y corriente continua pulsante) o superior. Un diferencial tipo AC no detecta la corriente de fallo en estas condiciones y su uso constituye una no-conformidad con la normativa vigente.

### Protección de sobretensiones (SPD)

La **UNE-HD 60364-7-712** requiere evaluación del riesgo de sobretensión. En zonas con nivel keraunoico medio-alto, se instalan descargadores **tipo II** (varistores SPD) tanto en el lado DC (entre positivo/negativo y tierra) como en el lado AC, en la caja de protecciones del generador.

## Criterios de selección aplicables en obra

| Parámetro | Criterio de diseño | Norma |
|---|---|---|
| Tensión máxima de string | ≤ Vmax_inv, calculada a Tmin histórica | IEC 62548 |
| Corriente de diseño cable DC | 1,4 x Isc_STC x factores de corrección | IEC 62548 / UNE-HD 60364-5-52 |
| Tipo de cable DC exterior | H1Z2Z2-K (UNE-EN 50618), XLPE doble capa | UNE-HD 60364-7-712 |
| Fusibles de string | Obligatorios desde 3 strings en paralelo | IEC 62548 Anexo E |
| Calibre fusible de string | 1,5 x Isc ≤ If ≤ 2,4 x Isc | IEC 62548 |
| Diferencial AC | Tipo A como mínimo | ITC-BT-23 |
| Caída de tensión DC | < 1 % Vmpp de string | Fabricante / buena práctica |
| Caída de tensión AC | ≤ 1,5 % | Acceso a red / REBT |
| Anti-islanding | Función integrada, ensayada según EN 50549-1 | EN 50549-1 |
| Tierra de estructura | Obligatoria, conectada al sistema del edificio | ITC-BT-18 |

**Verificación eléctrica antes de conexión a red**:

1. Medir Voc de cada string y comparar con el valor calculado (tolerancia ± 3 %). Una desviación mayor indica módulos en cortocircuito, mal polarizados o con diodo bypass en fallo.
2. Verificar polaridad con voltímetro antes de conectar al inversor. Una inversión de polaridad a 400-600 V DC puede destruir la etapa de entrada del equipo.
3. Medir aislamiento del cable DC respecto a tierra con megóhmetro a 500 V DC (valor mínimo: 1 MΩ, según UNE-HD 60364-7-712, cláusula 712.6).
4. Verificar actuación del relé anti-islanding según el protocolo del fabricante antes de la puesta en servicio definitiva y de la notificación a la distribuidora.

## Conclusión

El diseño de una instalación fotovoltaica de autoconsumo doméstico requiere aplicar tres normativas en capas: el marco administrativo del RD 244/2019, los requisitos eléctricos de la UNE-HD 60364-7-712 y la IEC 62548 para el lado DC, y los requisitos de protección del REBT para el lado AC. Los errores más frecuentes en obra son el uso de cable H07V-K en tramos exteriores DC, la ausencia de diferencial tipo A, y la omisión de la verificación de tensión de string a temperatura mínima. Un generador de 5 kWp bien dimensionado produce entre 5.500 y 7.500 kWh/año dependiendo de la zona (PR de 0,78-0,84 en condiciones reales), con una vida útil de garantía de módulo de 25-30 años si la instalación eléctrica se ejecuta con criterio técnico.
