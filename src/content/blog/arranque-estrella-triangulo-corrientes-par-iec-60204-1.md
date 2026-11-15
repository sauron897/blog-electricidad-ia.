---
title: "Arranque estrella-triángulo: corrientes, par y criterios IEC 60204-1"
description: "Análisis técnico del arranque Y/D en motores trifásicos: reducción de Ia a 1/3, caída de par al 33%, dimensionado de los tres contactores y criterios de aplicación según IEC 60947-4-1 e ITC-BT-47."
pubDate: 2026-11-15
keywords: ["arranque estrella triangulo", "arranque Y/D motor trifasico", "corriente arranque motor IEC", "contactores arranque motor IEC 60947-4-1"]
author: "Editor"
---

El arranque estrella-triángulo (Y/D) sigue siendo el método de tensión reducida más extendido en instalaciones industriales para motores por encima de 15 kW. Sin embargo, es frecuente encontrarlo mal aplicado: motores con carga que exige par desde el primer instante, tiempos de conmutación elegidos a ojo, o contactores subdimensionados porque alguien confundió corriente de línea con corriente de devanado. Este artículo analiza el fundamento físico, los valores reales de corriente y par, y los criterios de selección con los que tomar la decisión en obra.

## Fundamento físico: por qué I_a cae a 1/3 en estrella

Un motor de jaula de ardilla diseñado para funcionar en triángulo (Δ) a 400 V recibe en cada devanado exactamente 400 V cuando está conectado en Δ a la red. Si se conecta en estrella (Y) a esa misma red de 400 V, cada devanado queda sometido a la tensión de fase: V_fase = 400/√3 ≈ 231 V.

La relación de tensiones al cuadrado explica todo lo que sigue:

- **Corriente**: la impedancia del rotor bloqueado no cambia, por lo que la corriente es proporcional a la tensión. En Y: I_arranque_Y = (1/√3)² × I_arranque_Δ = I_arranque_Δ / 3
- **Par**: el par electromagnético es proporcional a V². En Y: M_arranque_Y = (1/3) × M_arranque_Δ

Ambas magnitudes caen exactamente al mismo factor: **1/3**. Esta simetría es la clave conceptual del método y también su limitación principal.

La base de datos GElectrical (que implementa IEC 60034) proporciona el coeficiente k = I_arranque_DOL / I_nominal para cada motor. Para motores de jaula estándar de 2,2 kW en adelante, k = 6,5. Con ese valor y los datos de eficiencia y cos φ de la norma es posible calcular la corriente de arranque real:

| Potencia | η (IE1) | cos φ | I_nominal (400 V) | I_a DOL (k=6,5) | I_a Y/D |
|----------|---------|-------|-------------------|-----------------|---------|
| 22 kW    | 89,9 %  | 0,90  | 39,4 A            | 256 A           | 85 A    |
| 37 kW    | 91,2 %  | 0,90  | 65,3 A            | 424 A           | 141 A   |
| 75 kW    | 92,7 %  | 0,90  | 130 A             | 845 A           | 282 A   |

La corriente de arranque Y/D calculada con I_nominal = P / (√3 × U × η × cos φ) e I_a_YD = k × I_n / 3. Valores coherentes con IEC 60034.

## El pico transitorio en la conmutación Y→Δ

La reducción de corriente durante la fase en estrella tiene un precio: en el instante de la conmutación a triángulo se genera un **transitorio** de corriente cuya magnitud puede igualar o superar al arranque DOL si la sincronía no es correcta.

Al abrir el contactor de estrella, el motor queda girando libremente. Su FEM residual (proporcional a la velocidad en ese instante) puede estar en oposición de fase con la red si el intervalo entre la apertura de KY y el cierre de KΔ es del orden de 20–50 ms. El resultado es una diferencia de tensión que puede llegar a 2 × U_red, con el consiguiente pico de corriente que supera el arranque directo. Muchos fabricantes denominan a este efecto **transient surge** o "segundo golpe de arranque".

La solución es doble:
1. **Tiempo de pausa entre KY y KΔ**: suficientemente corto para que la FEM residual no gire demasiado en fase (< 100 ms es habitual), pero suficiente para garantizar que KY está totalmente abierto antes de cerrar KΔ. Los relés temporizadores de acción instantánea y retardo al trabajo se ajustan típicamente a 50–80 ms de intervalo muerto.
2. **Conmutación cuando el motor está próximo a la velocidad de sincronismo**: el tiempo de permanencia en estrella debe durar hasta que la corriente cae al valor en carga y el motor acelera. Si se conmuta demasiado pronto —porque el tiempo del relé es fijo y la carga es alta— el pico transitorio se suma a una corriente de arranque todavía elevada.

IEC 60947-4-1:2010+AMD1:2012 (*Low-voltage switchgear and controlgear — Part 4-1: Contactors and motor starters*) establece en el Anexo K los ensayos de coordinación de tipo 2 que debe superar un arrancador Y/D, incluyendo los ciclos de arranque con carga y la comprobación de la integridad de los contactos tras el transitorio de conmutación.

## Dimensionado de los tres contactores según IEC 60947-4-1

El esquema Y/D requiere tres contactores: línea (KM), triángulo (KΔ) y estrella (KY), todos de categoría **AC-3** según IEC 60947-4-1.

**KM — Contactor de línea**: conduce la corriente de línea tanto durante el arranque en Y como durante el funcionamiento en Δ. El caso determinante es el régimen permanente en Δ: I_KM = I_nominal. Se dimensiona para I_nominal con categoría AC-3.

**KΔ — Contactor de triángulo**: en funcionamiento normal en Δ, cada rama del triángulo conduce la corriente de devanado, que es la corriente de línea dividida por √3:

I_KΔ = I_nominal / √3 ≈ 0,577 × I_nominal

Para el motor de 37 kW del ejemplo: I_KΔ ≈ 0,577 × 65,3 A ≈ 37,7 A. Se puede usar un contactor de calibre inferior al de línea, lo que reduce coste y espacio en cuadro.

**KY — Contactor de estrella**: conduce la corriente de arranque en Y, que es I_a_YD. El caso más exigente es el primer instante del arranque:

I_KY_max = k × I_nominal / 3

Para el motor de 37 kW: I_KY_max = 6,5 × 65,3 / 3 ≈ 141 A durante el arranque en Y. Sin embargo, KY opera en un régimen de muy corta duración y nunca en régimen permanente, por lo que es habitual dimensionarlo para la misma corriente que KM con categoría AC-3, dejando margen frente al pico de conmutación.

| Contactor | Corriente de dimensionado | Categoría IEC |
|-----------|--------------------------|---------------|
| KM (línea)    | I_nominal                | AC-3          |
| KΔ (triángulo)| 0,577 × I_nominal        | AC-3          |
| KY (estrella) | I_nominal (práctica conservadora) | AC-3  |

La protección contra sobrecargas (relé térmico o electrónico) se instala en serie con KM y se ajusta a I_nominal del motor. ITC-BT-47 del REBT exige que el conductor de acometida al motor soporte al menos el **125 % de la corriente nominal** del motor (sección mínima para régimen continuo), lo que es independiente del método de arranque.

## Criterios de selección y limitaciones del método Y/D

La decisión de aplicar arranque Y/D se reduce a dos preguntas que deben responderse antes de dimensionar nada:

**1. ¿Puede el motor arrancar en vacío o con par resistente < 33 % del par nominal?**

El par de arranque en Y es exactamente 1/3 del par de arranque DOL. Si el par de arranque DOL del motor es 2,0 × M_nominal (valor típico para motores de jaula de ardilla), el par disponible en Y es 2,0/3 ≈ 0,67 × M_nominal. Esto es suficiente para:

- Bombas centrífugas (par resistente en arranque próximo a 0 N·m)
- Ventiladores y soplantes (par cuadrático: M_carga ∝ n², arranca con carga mínima)
- Compresores de tornillo con válvula de derivación abierta
- Máquinas herramienta en vacío

**No es suficiente para**:
- Cintas transportadoras cargadas (par de arranque elevado desde n=0)
- Trituradoras, molinos y agitadores de alta viscosidad
- Compresores de pistón sin alivio
- Elevadores y grúas (par estático ≈ carga total)

**2. ¿La duración del ciclo de arranque es compatible con el tiempo térmico del motor en Y?**

En estrella, la corriente es I_a_YD ≈ (k/3) × I_n. Para k = 6,5 e I_n = 65,3 A (37 kW): I_a_YD ≈ 141 A ≈ 2,16 × I_n. Este valor sobrepasa el límite de disparo del relé térmico, por lo que el tiempo de arranque en Y debe ser lo suficientemente corto para no disparar la protección. Si la carga tiene alta inercia (GD² elevado) y el arranque se prolonga más de 10–15 s en Y, el criterio térmico puede impedir la aplicación del método.

La alternativa en ambos casos es el **arrancador suave (soft-starter)** con rampa de tensión ajustable o el variador de frecuencia, que eliminan tanto el límite de par como el problema del pico transitorio de conmutación.

**Tabla resumen de criterios de aplicación**:

| Parámetro | Condición para aplicar Y/D | Alternativa si no se cumple |
|-----------|---------------------------|-----------------------------|
| Par resistente en arranque | < 0,33 × M_arranque_DOL | Arrancador suave o VFD |
| Inercia de carga (GD²) | Tiempo arranque < 10 s en Y | Arrancador suave o VFD |
| Tensión de red disponible | Motor con dos tensiones (p. ej. 230/400 V) conectado en Δ a la tensión inferior | Motor con una sola tensión |
| Ciclos de arranque/hora | < 5 arranques/hora (límite orientativo) | Arrancador electrónico |

Respecto a la normativa aplicable: **IEC 60204-1:2016** (*Safety of machinery — Electrical equipment — Part 1: General requirements*) establece en su cláusula 9.2 los requisitos de interbloqueo eléctrico entre KY y KΔ para impedir el cierre simultáneo de ambos contactores (cortocircuito bifásico en la conexión de estrella). Este interbloqueo es obligatorio y se implementa mediante contactos auxiliares normalmente cerrados de cada contactor en el circuito de mando del otro.

## Conclusión

El arranque Y/D reduce la corriente de arranque a exactamente 1/3 de la del arranque directo porque la tensión sobre cada devanado cae a 1/√3, y la corriente (y el par) son proporcionales al cuadrado de esa tensión. Para un motor de 37 kW con k = 6,5 (IEC 60034), eso supone pasar de 424 A en DOL a 141 A en Y/D, con el pico transitorio en la conmutación como riesgo adicional a gestionar mediante el tiempo de intervalo muerto del relé.

El criterio de selección definitivo no es la potencia del motor sino la forma de la curva de par resistente: aplicar Y/D a una carga con par estático elevado garantiza que el motor no arranca o que arranca calentando los devanados en la fase de baja tensión. El interbloqueo entre KY y KΔ exigido por IEC 60204-1 es una obligación de diseño, no una opción.
