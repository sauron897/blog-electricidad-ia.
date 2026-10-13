---
title: "Interruptores automáticos MT: vacío vs SF6 e IEC 62271-100"
description: "Principio de ruptura de arco en vacío y SF6, parámetros normalizados IEC 62271-100, ciclos de maniobra y criterios de selección para redes MT de 12–36 kV."
pubDate: 2026-10-13
keywords: ["interruptores automáticos media tensión", "IEC 62271-100", "ruptura arco vacío SF6", "capacidad de ruptura MT", "TRV tensión transitoria de restablecimiento"]
author: "Editor"
---

## Principio de extinción del arco eléctrico en MT

En un interruptor de corriente alterna, la apertura de los contactos no extingue el arco de forma instantánea: la corriente sigue circulando hasta que el medio dieléctrico entre los contactos recupera su rigidez más rápido de lo que sube la tensión transitoria de restablecimiento (TRV, *Transient Recovery Voltage*). Esa competencia entre recuperación dieléctrica y TRV define la capacidad de ruptura del aparato.

**Ruptura en vacío.** La presión de vapor en la cámara de vacío es del orden de 10⁻⁴ Pa. El arco se sustenta sobre vapor metálico emitido por los propios contactos. En el paso por cero de la corriente, la generación de vapor cesa casi de forma instantánea, la presión cae y la rigidez dieléctrica se recupera en microsegundos. El espacio de separación de contactos necesario es mínimo (4–8 mm para 12 kV), lo que permite mecanismos de actuación muy compactos. La limitación principal es la corriente de corte (*chopping current*): entre 2 y 8 A según diseño, frente a < 1 A en SF6. En cargas inductivas pequeñas (motores en vacío, transformadores sin carga) esta corriente de corte genera sobretensiones que pueden superar 3–5 p.u. y requieren filtros RC o varistores SPD clase II en el circuito.

**Ruptura en SF6.** El hexafluoruro de azufre es un gas electronegativo con una rigidez dieléctrica aproximadamente 2,5 veces la del aire a presión igual. A 0,3–0,5 MPa, la rigidez sube hasta 5–6 veces la del aire. Las moléculas SF6 capturan electrones libres del plasma del arco con alta sección eficaz, formando iones SF6⁻ y SF5⁻ de baja movilidad, lo que inhibe la conducción eléctrica. El mecanismo de soplado autopresurizado (*puffer*) dirige el gas frío sobre la columna del arco en el paso por cero, enfriándola y acelerando la extinción. La corriente de corte en SF6 es inferior a 1 A, prácticamente nula frente al nivel de vacío, lo que lo hace preferible en cargas inductivas pequeñas. El inconveniente conocido: GWP = 23 500 (horizonte 100 años) y SF6 es el gas de invernadero más potente incluido en el Protocolo de Kioto. La Directiva EU F-Gas obliga a su sustitución progresiva; los fabricantes están introduciendo mezclas limpias (g³, Clean Air) como alternativa.

---

## Parámetros normalizados según IEC 62271-100:2021

La norma IEC 62271-100 (adoptada en España como **UNE-EN IEC 62271-100:2021/A1:2024**) define los parámetros de ensayo y los valores nominales de los interruptores de CA para tensiones superiores a 1 kV.

### Tensiones asignadas para redes de distribución MT en España

| Ur (kV) | Nivel aislamiento Up (kVp) | Red típica en España |
|---------|---------------------------|----------------------|
| 7,2 | 60 | Redes 6 kV (industria) |
| 12 | 75 | Distribución 10 kV |
| 17,5 | 95 | — |
| 24 | 125 | **Distribución 20 kV** |
| 36 | 170 | **Distribución 36 kV** |
| 40,5 | 185 | Zonas con 35 kV |
| 52 | 250 | Subestaciones regionales |

Para una red de 20 kV, el factor de sobretensión temporal (TOV) de la red puede alcanzar 1,25 p.u. durante faltas a tierra en sistemas con neutro aislado o compensado, lo que justifica usar interruptores de 24 kV (Ur = 1,2 × 20 kV) en lugar de 20 kV.

### Corriente de cortocircuito de ruptura asignada (Icc)

Los valores normalizados son: **12,5 — 16 — 20 — 25 — 31,5 — 40 — 50 — 63 kA** (cresta con componente DC incluida según el factor de asimetría κ = ip / Icc√2, con κ típico de 1,6–1,7 para X/R = 14, que da ip ≈ 2,5 × Icc).

Para la selección, se debe calcular la corriente de cortocircuito máxima en el punto de instalación mediante el **método de impedancias IEC 60909-0** (ya publicado en este blog) y elegir el escalón normalizado inmediatamente superior.

### Ciclos de maniobra

IEC 62271-100 define la **secuencia de verificación de cortocircuito** como 5 secuencias CO (cierre-apertura) a plena potencia, en lugar de las anteriores 3 O + 2 CO. Para recierre automático, la secuencia estándar es:

```
O – t1 – CO – t2 – CO
```

Donde:
- **t1** (primer intervalo) = 0,3 s para recierre rápido; 3 min para recierre lento
- **t2** (segundo intervalo) = 3 min (típico)

Esta secuencia representa el escenario más exigente: el interruptor debe cortar la corriente de falta completa dos veces sin recuperación térmica plena de los contactos.

### Clases de vida útil

| Clase | Magnética/Mecánica | Operaciones mecánicas | Corriente nominal |
|-------|-------------------|----------------------|-------------------|
| M1 | Estándar | 2 000 | Cualquiera |
| M2 | Extendida | 10 000 | Cualquiera |
| E1 | Estándar | 2 000 CC a Icc nominal | — |
| E2 | Extendida | 10 000 a plena corriente | — |

La clase E2/M2 es la habitual en celdas de centros de seccionamiento y transformación (CST/CT) de distribución, donde la expectativa de vida supera los 25 años y la frecuencia de maniobra es significativa.

---

## TRV: la magnitud que decide si el arco se extingue o se reignita

La **tensión transitoria de restablecimiento** (TRV) es la diferencia de tensión que aparece instantáneamente entre los contactos tras el cruce por cero de la corriente. Si la TRV sube más rápido que la recuperación dieléctrica del espacio de contactos, el arco se reignita y la corriente de falta continúa. IEC 62271-100 parametriza la TRV de ensayo mediante:

- **uc**: tensión de cresta de la TRV (referenciada a √2 × Ur / √3 × kaf, donde kaf es el factor de amplitud de la TRV)
- **t3**: tiempo hasta la cresta de uc
- **RRRV** (*Rate of Rise of Recovery Voltage*): gradiente inicial en kV/µs

Para Ur = 24 kV, Icc = 25 kA:
- uc ≈ 55 kV (cresta)
- RRRV ≈ 2–5 kV/µs (depende del tipo de red: cable vs. línea aérea)

Las redes de cable tienen capacidad distribuida que amortigua la TRV; las líneas aéreas tienen TRV más pronunciada y de mayor frecuencia, lo que hace más exigente la ruptura en redes rurales con líneas aéreas.

---

## Conmutación capacitiva: clases C1 y C2

La apertura de cables en vacío o condensadores genera una TRV de alta frecuencia con riesgo de **reignición** (*restrike*): el interruptor interrumpe la corriente capacitiva en el primer cruce por cero y queda sometido a tensión pico de hasta 2–3 p.u. A los pocos microsegundos, si la resistencia dieléctrica de la cámara no es suficiente, hay reignición seguida de sobretensión escalada hasta 4–5 p.u.

IEC 62271-100 define dos clases para conmutación capacitiva:

| Clase | Ensayo | Reencendidos admitidos |
|-------|--------|----------------------|
| C1 | 15 disparos, 100% Icc capacitiva | 0 |
| C2 | 24 disparos, 100% Icc capacitiva | 0 |

La clase **C2** es obligatoria en:
- Interruptores que maniobran bancos de condensadores en redes MT
- Interruptores de salida de cables largos (>2 km) con alta corriente capacitiva

Los interruptores de vacío de diseño antiguo (alto *chopping current*) difícilmente superan C2 en redes inductivo-capacitivas; los modelos modernos con aleaciones Cu-Cr en los contactos han reducido el *chopping current* a < 2 A y sí superan C2.

---

## Criterios de selección aplicables en obra

Antes de especificar un interruptor MT, el proyectista debe definir los siguientes parámetros en este orden:

1. **Ur** → en función de la tensión nominal de la red y del TOV máximo durante falta a tierra (sistema TN/TT/IT en MT).
2. **Icc de ruptura** → calculado por impedancias IEC 60909-0 en el punto de instalación, tomando el escalón normalizado superior. Verificar que el IP (corriente de cresta) ≤ ip admisible del aparato.
3. **Corriente nominal In** → debe superar la corriente de plena carga del circuito (transformador, cable, embarrado).
4. **Clase C1/C2** → si el interruptor maniobra capacitores o cables en vacío, exigir C2.
5. **Ciclo de recierre** → si hay enclavamiento de recierre automático, verificar que el aparato supera la secuencia O-0,3s-CO-3min-CO a plena Icc.
6. **Clase M2/E2** → si la frecuencia de operación esperada supera 1 000 maniobras durante la vida del equipo o si la corriente de falta esperada se aproxima a Icc con frecuencia.
7. **Tecnología de gas** → si la instalación está sujeta a auditorías F-Gas o a normativa de edificios con restricciones medioambientales, especificar soluciones sin SF6 (mezcla g³ o vacío según tensión).
8. **Condiciones ambientales** → altitud > 1 000 m reduce la rigidez dieléctrica del aire exterior (factores IEC 60071-2); temperatura ambiente < -25 °C o > +40 °C requiere variantes especiales.

### Resumen de comparación vacío vs. SF6 para distribución MT 24–36 kV

| Parámetro | Vacío | SF6 / mezcla g³ |
|-----------|-------|-----------------|
| Rango de tensión típico | hasta 40,5 kV | hasta 245 kV y más |
| *Chopping current* | 2–8 A | < 1 A |
| Impacto medioambiental | Ninguno | Alto (SF6 GWP=23500) |
| Mantenimiento | Prácticamente nulo | Verificación de presión de gas |
| Tiempo de respuesta | < 40 ms | < 40 ms |
| Clase C2 capacitiva | Disponible en modelos modernos | Estándar |
| Coste | Inferior (en MT ≤ 40,5 kV) | Superior en MT |

---

## Conclusión

La selección de un interruptor automático MT no es trivial: la tecnología de ruptura (vacío o SF6), la clase de conmutación capacitiva y el ciclo de maniobra son parámetros que determinan si el aparato soporta la operación real en red. IEC 62271-100:2021 normaliza todos estos ensayos; la verificación de TRV es el criterio más exigente que diferencia las celdas de media potencia de las de alta. Para redes de distribución española a 20 y 36 kV, la tendencia es migrar hacia vacío + mezcla g³ para eliminar la dependencia del SF6, manteniendo las clases E2/M2 y C2 que garantizan 25 años de vida en servicio sin revisión de la cámara de ruptura.
