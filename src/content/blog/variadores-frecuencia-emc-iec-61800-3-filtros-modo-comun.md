---
title: "Variadores de frecuencia y EMC: filtros IEC 61800-3"
description: "Categorías C1–C4, filtros de modo común y diferencial, longitudes de cable y prácticas de instalación EMC para variadores según UNE-EN IEC 61800-3:2023."
pubDate: 2026-11-12
keywords: ["variador frecuencia EMC IEC 61800-3", "filtros modo comun variador", "categorias EMC variador C1 C2 C3 C4", "compatibilidad electromagnetica variadores industriales", "corriente modo comun VFD cable motor"]
author: "Editor"
---

## El problema EMC de los variadores: origen físico de las perturbaciones

Un variador de frecuencia (VFD) genera perturbaciones electromagnéticas por la conmutación de sus IGBTs a frecuencias de 2 a 16 kHz. Cada flanco de tensión produce una variación dV/dt del orden de 1–10 kV/µs en la salida del inversor. Esa rampa de tensión, aplicada sobre la capacitancia parásita entre conductores activos y tierra del cable de motor (C_tierra), inyecta una corriente de modo común I_MC = C_tierra · dV/dt que circula por el PE y retorna por la red.

Para un cable XLPE trifásico de 95 mm² (C = 290 nF/km según GElectrical/IEC 60364-5-52) y un dV/dt de 5 kV/µs, la corriente de modo común pico en 50 m de cable es:

```
I_MC(pico) = 0,290 nF/m · 50 m · 5·10⁶ V/s ≈ 72,5 mA por flanco
```

A 8 kHz de frecuencia de portadora, esta corriente se repite 16.000 veces por segundo. Es la causa de:
- Desgaste del aislamiento de rodamientos (corrientes de Eddy en el eje del motor)
- Perturbaciones en comunicaciones serie RS-485/Profibus en el mismo cuadro
- Superación de los límites de emisión de la clase A/B de CISPR 11

La normativa que rige estos requisitos en instalaciones fijas es **UNE-EN IEC 61800-3:2023** (equivalente a IEC 61800-3:2022, ed. 4), que reemplazó a la UNE-EN 61800-3:2004+A1:2012.

---

## Categorías de emisión C1–C4 según IEC 61800-3

La norma define cuatro categorías en función del entorno de instalación (Entorno 1 = redes públicas con usuarios domésticos; Entorno 2 = redes industriales exclusivas):

| Categoría | Entorno | Distribución | Límite referencia | Requisito técnico del usuario |
|-----------|---------|-------------|-------------------|-------------------------------|
| C1 | 1 (residencial) | No restringida | CISPR 11 Clase B | Ninguno adicional |
| C2 | 1 (residencial) | Restringida | CISPR 11 Clase A | Instalar y poner en servicio por personal cualificado |
| C3 | 2 (industrial) | Restringida | CISPR 11 Clase A (entorno 2) | No conectar a red pública con usuarios domésticos |
| C4 | 2 (industrial) | Restringida | Sin límite de alta frecuencia normalizado | Aplicar plan EMC del fabricante; requiere evaluación del sistema |

**Categoría C3** es la más habitual en instalaciones industriales con motor > 11 kW: el variador incorpora filtro EMC integrado y cumple la clase A del Entorno 2 con cable de motor ≤ 100 m apantallado. Con cable no apantallado o longitudes mayores, la categoría se degrada a C4.

**Categoría C4** no implica que no haya limitaciones; la norma exige un "EMC plan" documentado que incluya medidas de mitigación, longitud máxima de cable, filtros externos y puesta a tierra de la pantalla en ambos extremos.

---

## Ruido de modo común vs. modo diferencial: qué filtra cada componente

El espectro de perturbaciones del VFD tiene dos componentes:

**Modo diferencial (DM):** tensiones/corrientes simétricas entre fases. Se origina en las ondulaciones de corriente del rectificador de entrada (frecuencias 6·f_red = 300 Hz y armónicos). Se atenúa con condensadores de filtro de entrada entre fases (C_X) e inductancias en serie de cada fase (L_DM).

**Modo común (CM):** tensiones/corrientes simétricas respecto a tierra. Se origina en la conmutación del inversor de salida. Se atenúa con:
- Bobina de modo común (toroide de ferrita) en el cable de motor, que presenta alta impedancia a la corriente CM sin afectar las corrientes de carga
- Condensadores C_Y (entre cada fase y tierra) en el filtro de entrada del variador
- Cable de motor apantallado con pantalla conectada a tierra en ambos extremos con prensaestopas EMC de 360°

La distinción es crítica: una reactancia trifásica convencional en la entrada del variador atenúa el modo diferencial pero no tiene efecto sobre el modo común de salida.

---

## Parámetros clave de instalación: longitud de cable y capacitancia

La capacitancia del cable de motor es el parámetro más limitante. Según los datos de GElectrical (IEC 60364-5-52), cables de cobre XLPE trifásicos en bandeja:

| Sección (mm²) | C (nF/km) | Longitud máx. recomendada sin filtro CM adicional (C3) |
|---------------|-----------|-------------------------------------------------------|
| 4 | 110 | ~100 m |
| 16 | 180 | ~80 m |
| 50 | 240 | ~60 m |
| 95 | 290 | ~50 m |
| 185 | 290 | ~45 m |

Valores típicos de fabricantes (ABB, Danfoss, Siemens) coinciden con este patrón: a mayor sección, mayor capacitancia por kilómetro por el incremento del diámetro exterior del aislamiento XLPE, y menor longitud máxima admisible sin filtro adicional en la salida del variador.

Cuando se supera la longitud máxima de C3 sin filtro adicional:
1. Se instala una reactancia de salida du/dt (limita el dV/dt a ≤ 500 V/µs)
2. O bien un filtro sinusoidal de salida (reduce la forma de onda PWM a senoidal pura, eliminando restricción de longitud y protegiendo el aislamiento del motor)

---

## Selección de filtros: criterios para ingenieros

El flujo de decisión en obra sigue esta secuencia:

**1. Determinar la categoría EMC requerida**
- ¿El punto de suministro alimenta a usuarios domésticos? → Categoría C2 mínima (filtro de entrada obligatorio)
- ¿Es una red industrial exclusiva (subestación propia)? → C3 suficiente con cable ≤ 100 m apantallado

**2. Evaluar la longitud del cable de motor**
- < Longitud máx. para la sección → el filtro integrado C3 es suficiente
- Entre longitud máx. y 150 m → añadir reactancia du/dt en salida del variador
- > 150 m o motor antiguo (aislamiento clase B, 1300 V pico máximo) → filtro sinusoidal de salida

**3. Verificar la carga del filtro frente a la corriente nominal del motor**
Para un motor IE3 de 22 kW / 400 V / cos_phi 0,9 (I_N ≈ 39 A), el filtro de entrada y la reactancia de salida se dimensionan para 1,1 · I_N = 43 A. Los catálogos de ABB (Código ACS880) o Siemens (SINAMICS G120) listan filtros en pasos normalizados: 32 A, 45 A, 60 A → seleccionar 45 A.

**4. Puesta a tierra EMC del cable de motor**
- Pantalla del cable: conectar a tierra en ambos extremos con prensaestopas EMC de 360° (no simplemente enrollar la trenza)
- En el variador: usar el terminal PE dedicado de alta frecuencia, no la barra de PE general del cuadro
- Separar el cableado de señal (encoder, termistor) del cable de potencia en bandejas distintas con separación ≥ 300 mm

**5. Reactancias de entrada frente a corrientes armónicas**
Un variador sin reactancia de entrada genera corriente armónica de entrada con THD_I hasta el 90%. Con reactancia de red (3–4% de impedancia relativa), el THD_I cae a 30–40%. Para cumplir IEC 61000-3-12 en instalaciones con potencia de cortocircuito baja, puede ser necesaria una reactancia del 5% o un filtro activo de armónicos.

---

## Tabla de comparación: filtros y su ámbito de aplicación

| Dispositivo | Modo atenuado | Posición | Coste relativo | Efecto en el motor |
|-------------|--------------|----------|----------------|-------------------|
| Filtro EMC integrado (C3) | CM y DM entrada | Integrado en variador | Referencia | Ninguno |
| Reactancia de red (3–5%) | DM entrada | Entrada variador | Bajo | Ninguno |
| Reactancia du/dt salida | CM salida (parcial) | Salida variador | Medio | Protege aislamiento |
| Filtro sinusoidal salida | CM y DM salida | Salida variador | Alto | Elimina restricción longitud |
| Bobina de modo común | CM salida | Cable motor | Bajo | Ninguno |

---

## Conclusión

La categoría C3 con filtro integrado es el punto de partida para toda instalación industrial con VFD. No es suficiente con montarla: la longitud del cable de motor, su sección, el apantallado y la puesta a tierra de la pantalla determinan si se mantiene en C3 o se degrada a C4. Cuando la longitud supera los valores de la tabla (50–100 m según sección del cable XLPE), la inversión en una reactancia du/dt (200–400 €/ud para rangos hasta 45 A) es siempre menor que el coste de un fallo de rodamientos por corrientes de eje o de una no conformidad EMC en la puesta en marcha. Documentar el plan EMC según IEC 61800-3 Anexo D es además una exigencia para la declaración CE del sistema de accionamiento completo.
