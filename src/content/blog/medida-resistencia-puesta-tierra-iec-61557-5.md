---
title: "Medida de resistencia de tierra: métodos según IEC 61557-5 e ITC-BT-18"
description: "Guía técnica para medir resistencia de puesta a tierra con caída de potencial, método selectivo y pinzas conforme a IEC 61557-5:2019 e ITC-BT-18 del REBT."
pubDate: 2026-11-22
keywords: ["medida resistencia puesta a tierra IEC 61557-5", "método caída de potencial tierra", "telurímetro IEC 61557", "resistencia tierra ITC-BT-18", "método selectivo puesta tierra"]
author: "Editor"
---

La resistencia de puesta a tierra no es la resistencia de un conductor metálico. Es el valor que cuantifica la oposición que ofrece el volumen de terreno al paso de corriente desde el electrodo enterrado hasta un punto remoto de referencia. Este valor condiciona directamente el tiempo de desconexión de los diferenciales en esquemas TT y, por tanto, la protección contra contactos indirectos. IEC 61557-5:2019 y la ITC-BT-18 del REBT son las referencias normativas que todo técnico eléctrico debe manejar antes de conectar el telurímetro.

## Por qué no sirve un óhmetro convencional

Un multímetro en modo resistencia inyecta corriente continua entre dos bornes. Para medir la resistencia de un electrodo de tierra necesitas un circuito de retorno que, en la práctica, está constituido por el propio terreno hasta un electrodo auxiliar. El problema: cualquier tensión de red presente sobre el sistema de tierra (inevitablemente hay corrientes de fuga en instalaciones en servicio) interferiría con la medida de CC, haciéndola inútil.

Los instrumentos conformes a IEC 61557-5:2019 inyectan corriente alterna a frecuencia desplazada de 50 Hz, habitualmente entre 94 Hz y 128 Hz. Esto permite que el instrumento use filtros de paso de banda para rechazar la componente de 50 Hz (y sus armónicos) sobreimpuesta en el electrodo, obteniendo sólo la caída de tensión debida a la corriente de ensayo.

La versión 2019 de la norma actualiza la edición de 2007 e incorpora explícitamente requisitos para la medida con pinzas de inducción, incluyendo un nuevo anexo informativo sobre el método de doble pinza.

## Métodos normalizados por IEC 61557-5:2019

### Caída de potencial de 3 hilos (Fall-of-Potential)

Es el método de referencia, aplicable a cualquier tipo de electrodo. El instrumento conecta tres terminales:
- **C1 / H**: electrodo de tierra bajo ensayo (inyecta corriente de ensayo Ie)
- **C2 / S (sonda de corriente)**: electrodo auxiliar de corriente, hincado a suficiente distancia para quedar fuera de la zona de influencia
- **P2 / S (sonda de potencial)**: electrodo auxiliar de potencial, colocado entre los anteriores

El instrumento calcula R = ΔV/Ie midiendo la caída de tensión entre el electrodo ensayado (P1) y la sonda de potencial (P2).

**Regla del 61,8 %**: para un electrodo simple vertical, la sonda de potencial debe situarse al 61,8 % de la distancia entre C1 y C2. Este porcentaje deriva de la distribución de potencial logarítmica en torno a un hemielisfoide en terreno homogéneo. En la práctica, se realizan al menos tres medidas desplazando la sonda ±10 % de esa posición; si los tres valores coinciden dentro del ±5 %, la lectura central es el valor de resistencia del electrodo.

La distancia mínima entre C1 y C2 depende del tipo de electrodo:
- Pica vertical de 1 m: distancia C1–C2 ≥ 10 m
- Pica vertical de 3 m o placa: C1–C2 ≥ 20 m
- Malla de tierra de subestación (decenas de m²): C1–C2 ≥ 5 × diámetro equivalente de la malla, habitualmente 50–200 m

### Caída de potencial de 4 hilos

Añade un cuarto hilo separado entre C1 y la pinza de medida sobre el conductor de tierra. Los pares C1/C2 inyectan corriente (terminales de baja impedancia) y los pares P1/P2 miden la caída de tensión (terminales de alta impedancia). Esta configuración elimina el error introducido por la resistencia del cable de conexión a C1, relevante cuando se trabaja con cables largos (> 30 m) o conductores de pequeña sección.

### Método selectivo (con pinza de corriente)

Permite medir la resistencia de un electrodo individual **sin desconectarlo de la instalación** ni hincar picas auxiliares. El instrumento emplea dos pinzas de transformador:

1. La primera pinza induce una EMF en el conductor de tierra (inyecta la corriente de ensayo por inducción).
2. La segunda pinza mide la corriente que circula por el conductor bajo ensayo.

El cociente EMF/I da la impedancia del bucle de tierra completo. Para que el resultado equivalga a la resistencia del electrodo individual, es imprescindible que existan **otros electrodos en paralelo** que constituyan el camino de retorno. Si el electrodo está aislado eléctricamente del resto del sistema, el método no es aplicable: el bucle está abierto y la lectura es errónea (típicamente muy alta o error de medida).

Ventajas frente al método de caída de potencial: no requiere picas auxiliares, no es necesario desconectar el electrodo, y es especialmente práctico en sistemas de tierra de subestaciones con múltiples electrodos en paralelo o en anillos de tierra de edificios.

## Resistividad del terreno: método Wenner (4 electrodos)

El método Wenner no mide la resistencia de un electrodo instalado: caracteriza la **resistividad del terreno (ρ, en Ω·m)** antes de diseñar la instalación de puesta a tierra, o para diagnosticar variaciones estacionales.

Se instalan cuatro electrodos en línea recta separados una distancia **a** (uniforme). Los electrodos exteriores inyectan corriente; los interiores miden la tensión. La resistividad aparente se obtiene como:

**ρ = 2π · a · R**

donde R es la resistencia medida por el instrumento.

Valores típicos de resistividad:

| Tipo de terreno | ρ (Ω·m) |
|---|---|
| Arcilla húmeda | 10–50 |
| Tierra agrícola / jardín | 50–200 |
| Arena seca | 500–3 000 |
| Roca basáltica | 500–10 000 |
| Roca granítica | 1 000–50 000 |
| Hormigón húmedo | 50–300 |

Variando la separación **a** se obtiene la resistividad a diferentes profundidades (con a = 1 m se mide el perfil superficial; con a = 5 m se alcanza la capa a 5 m de profundidad, aproximadamente). Esta información es imprescindible para dimensionar mallas de tierra de subestaciones según IEC 60364-5-54 e IEEE Std. 80.

## Criterios de aceptación: ITC-BT-18 y IEC 60364-4-41

La ITC-BT-18 del REBT establece que en esquemas **TT** la resistencia de tierra del electrodo (RA) debe satisfacer:

**RA · Id ≤ U**

donde Id es la corriente de disparo del diferencial e Id es la corriente de defecto a tierra. U vale **50 V** para locales secos y **24 V** para locales húmedos, piscinas o exteriores.

Combinando con los calibres normalizados de diferenciales:

| Idn del diferencial | RA,máx (seco, 50 V) | RA,máx (húmedo, 24 V) |
|---|---|---|
| 10 mA | 5 000 Ω | 2 400 Ω |
| 30 mA | 1 667 Ω | 800 Ω |
| 100 mA | 500 Ω | 240 Ω |
| 300 mA | 167 Ω | 80 Ω |
| 500 mA | 100 Ω | 48 Ω |

En la práctica, el diferencial de 30 mA en instalación doméstica (seca) admite RA hasta 1 667 Ω, lo que es fácil de alcanzar con una sola pica en la mayoría de terrenos. El diferencial de 300 mA en cuadros industriales exteriores (húmedos) exige RA ≤ 80 Ω, lo que puede requerir mallas o picas en paralelo en terrenos de alta resistividad.

La ITC-BT-18 también establece la obligación de **verificar la resistencia de tierra al menos una vez al año** en instalaciones que así lo exijan (almacenes de materias inflamables, establecimientos sanitarios, instalaciones de clase I, etc.). Esta comprobación debe realizarla personal técnicamente competente y queda documentada en el libro de mantenimiento.

## Criterios de selección del método en obra

| Situación en obra | Método recomendado | Instrumento |
|---|---|---|
| Pica de nueva instalación (sin energizar) | Caída de potencial 3 hilos | Telurímetro con picas auxiliares |
| Malla de tierra de subestación | Caída de potencial 4 hilos (distancias largas) | Telurímetro con 4 terminales + cable bobina |
| Revisión periódica ITC-BT-18, instalación en servicio, múltiples electrodos | Selectivo (doble pinza) | Telurímetro con pinzas de inducción |
| Estudio previo de terreno, diseño de red de tierras | Wenner (4 electrodos) | Telurímetro con 4 clavijas y picas de 20 cm |
| Verificación de impedancia de bucle (TN) | No es medida de tierra: usar comprobador de bucle IEC 61557-3 | Loop tester |

**Requisito documental**: el instrumento debe estar calibrado conforme a IEC 61557-5:2019, con certificado de calibración trazable a patrón nacional (ENAC en España). Los registros de medida deben incluir: fecha, instrumento (modelo y número de serie), método empleado, distancia de picas, temperatura y humedad ambiental, y el valor medido en Ω.

## Errores frecuentes en la medida

**Interferencias de corriente de red**: si el electrodo está conectado a la instalación durante la medida de caída de potencial, la corriente de fuga de la red circula por las picas y distorsiona el resultado. Desconectar el borne de tierra del embarrado principal antes de medir.

**Distancia insuficiente entre picas**: el error más habitual. Si C2 está demasiado cerca, las zonas de influencia de C1 y C2 se solapan y el telurímetro lee un valor inferior al real. Respetar la regla del 61,8 % y verificar con medidas desplazadas ±10 %.

**Picas de potencial en paralelo al electrodo ensayado**: en instalaciones con red de tierras extensa, la sonda de potencial puede caer dentro de la zona de influencia de un segundo electrodo. En ese caso, el método selectivo es más fiable que el de caída de potencial.

**No contemplar variaciones estacionales**: la resistividad del terreno puede variar en un factor 3–5 entre verano seco e invierno lluvioso. Las medidas tomadas en condiciones favorables (terreno húmedo) no garantizan el cumplimiento de ITC-BT-18 todo el año. La norma recomienda realizar la comprobación anual en la época más desfavorable (máxima resistividad, habitualmente verano).

## Conclusión

La medida de la resistencia de puesta a tierra requiere seleccionar el método adecuado en función del tipo de electrodo, si la instalación está en servicio y la distancia disponible. El método de caída de potencial es el de referencia normativa para electrodos individuales; el método selectivo con pinzas es el más práctico para revisiones periódicas de sistemas complejos en servicio. En cualquier caso, el criterio de aceptación viene impuesto por la ITC-BT-18: RA · Idn ≤ 50 V (o 24 V en locales húmedos). Documentar la medida con instrumento calibrado conforme a IEC 61557-5:2019 es el único modo de acreditar el cumplimiento ante una inspección de OCA.
