---
title: "Celdas MT Metal-Clad: Ensayos de Tipo según IEC 62271-200"
description: "Análisis técnico de los ensayos de tipo obligatorios para celdas de media tensión bajo IEC 62271-200: dielectrico, temperatura, cortocircuito, IAC y clasificacion LSC. Para ingenieros y técnicos MT."
pubDate: 2026-10-02
keywords: ["celdas MT IEC 62271-200 ensayos switchgear", "ensayos tipo aparamenta media tension", "IAC clasificacion arco interno IEC 62271", "LSC2B celdas MT compartimentacion", "switchgear metal-clad MT seleccion"]
author: "Editor"
---

## IEC 62271-200: alcance y estructura normativa para aparamenta MT

La norma IEC 62271-200 *AC metal-enclosed switchgear and controlgear for rated voltages above 1 kV and up to and including 52 kV* cubre la aparamenta bajo envolvente metálica para corriente alterna desde 1 kV hasta 52 kV incluidos. En España se adopta como UNE-EN IEC 62271-200. Su campo de aplicación abarca las celdas prefabricadas de media tensión utilizadas en subestaciones, centros de transformación de abonado y redes de distribución secundaria.

La norma establece dos categorías constructivas principales en función del grado de compartimentación de sus circuitos activos:

| Categoría | Denominación | Compartimentación |
|-----------|-------------|-------------------|
| Metal-Clad | Totalmente metálica | Compartimentos del interruptor, barra y cables, todos separados con barreras metálicas completas |
| Cubicle-Type | Tipo cubículo | Envolvente exterior metálica, sin separación metálica completa entre compartimentos |

El diseño **Metal-Clad** es el más exigente: cada compartimento —interruptor principal, barra colectora y conexiones de cable— queda físicamente aislado de los demás mediante tabiques metálicos conectados a tierra. Esto limita la propagación de un arco interno a un único compartimento y facilita el mantenimiento con tensión presente en compartimentos adyacentes.

---

## Clasificaciones de continuidad de servicio y compartimentación (LSC y PM/PI)

IEC 62271-200 introduce dos sistemas de clasificación que determinan las condiciones de trabajo con tensión:

### Categorías LSC (Loss of Service Continuity)

La clase LSC define qué partes de la instalación deben desconectarse para realizar mantenimiento o sustitución de componentes en el compartimento del interruptor:

| Clase LSC | Requisito operacional |
|-----------|----------------------|
| LSC1 | Las celdas adyacentes deben desenergizarse para acceder al compartimento del interruptor |
| LSC2A | Las celdas adyacentes pueden permanecer energizadas; la barra seccionalizada debe estar sin tensión |
| LSC2B | Las celdas adyacentes, incluida la barra colectora, pueden permanecer energizadas durante el mantenimiento |

La clase **LSC2B** es la de mayor disponibilidad y se especifica habitualmente en redes de distribución donde la continuidad de suministro es crítica. La barra colectora queda completamente aislada del compartimento de mantenimiento mediante tabiques metálicos certificados.

### Clase de tabique (PM/PI)

Los tabiques que separan compartimentos se clasifican según el material:

- **PM** (*Partition Metal*): tabiques metálicos, conectados a tierra — mayor resistencia mecánica y térmica ante un arco
- **PI** (*Partition Insulating*): tabiques de material aislante — aceptados en algunas configuraciones de menor exigencia

Una celda Metal-Clad requiere **PM** en todas las separaciones entre compartimentos activos.

---

## Ensayos de tipo obligatorios según IEC 62271-200 §6

IEC 62271-200, cláusula 6.1, lista los ensayos de tipo que el fabricante debe superar y certificar antes de comercializar la celda. No son ensayos de rutina por unidad producida; se realizan sobre prototipos representativos del diseño.

### 6.1 Ensayos dieléctricos

Se realizan conforme a la serie IEC 62271-1 (requisitos comunes de alta tensión). Los niveles de aislamiento normalizados para las tensiones asignadas más habituales son:

| Tensión asignada Ur (kV) | Tensión de sostenimiento 50 Hz, 1 min (kV ef.) | Tensión de impulso rayo Urp (kV cresta) |
|--------------------------|------------------------------------------------|-----------------------------------------|
| 7,2 | 20 | 60 |
| 12 | 28 | 75 |
| 17,5 | 38 | 95 |
| 24 | 50 | 125 |
| 36 | 70 | 170 |
| 52 | 95 | 250 |

El ensayo de frecuencia industrial se aplica durante **60 segundos** entre partes activas y tierra, y entre polos. El ensayo de impulso aplica **15 impulsos positivos y 15 negativos** de la forma normalizada 1,2/50 µs.

### 6.2 Ensayo de elevación de temperatura

Se verifica que bajo corriente nominal continua las temperaturas no superen los límites de IEC 62271-1, §4.4.2. Los límites más relevantes son:

| Elemento | Temperatura máxima (°C) | Elevación máxima sobre 40°C ambiente (K) |
|----------|------------------------|------------------------------------------|
| Contactos de cobre con plata en contacto con aire | 105 | 65 |
| Barra colectora de cobre desnuda en aire | 90 | 50 |
| Bornes accesibles al usuario | 70 | 30 |
| Aislamiento de cables en el compartimento | depende del aislante | — |

La medición se realiza con termopares o resistencia en régimen permanente, con carga de corriente nominal In durante un tiempo mínimo hasta que la variación de temperatura sea inferior a 1 K/h durante 30 minutos consecutivos.

### 6.3 Ensayo de corriente de corta duración y corriente cresta

Mide la capacidad del diseño para soportar el cortocircuito durante el tiempo de actuación de protecciones. Los parámetros asignados normalizados más comunes:

| Parámetro | Valores normalizados |
|-----------|---------------------|
| Corriente de corta duración Ik (kA ef.) | 16 — 20 — 25 — 31,5 — 40 |
| Duración asignada tk (s) | 1 s (estándar), 3 s (redes con selectividad temporizada extendida) |
| Corriente cresta ip (kA cresta) | Factor k = 2,5 × Ik para 50 Hz y X/R elevado |

Para una celda con **Ik = 25 kA** durante **1 s**, la corriente cresta asignada es **ip = 2,5 × 25 = 62,5 kA cresta**. El diseño debe soportar sin deformación permanente ni apertura de circuito la energía I²·t = (25.000)² × 1 = 625 × 10⁶ A²s.

### 6.4 Verificación del grado de protección IP

Conforme a IEC 60529. Los valores mínimos típicos según accesibilidad:

- Envolvente exterior: **IP3X** (protección contra herramientas y dedos) o **IP4X** en entornos con polvo
- Compartimento de barra bajo tensión no accesible: **IP2X** interno es suficiente si el tabique PM garantiza la separación
- Suelo de la celda (apertura para cables): **IPX1** mínimo

### 6.5 Ensayo de arco interno (IAC)

Es el ensayo de tipo más específico de IEC 62271-200 y el más costoso. Su objetivo es demostrar que en caso de arco interno, los efectos mecánicos y térmicos no causan daño a personas en las proximidades.

---

## Clasificación IAC y criterios de aceptación del ensayo de arco interno

### Designación IAC

La clasificación IAC se indica en la placa de características de la celda con cuatro parámetros:

1. **Accesibilidad**: A (frontal), B (frontal + laterales), C (frontal + laterales + posterior)
2. **Lados clasificados**: F (*front*), L (*lateral*), R (*rear*)
3. **Corriente de arco asignada** (kA)
4. **Duración del arco asignada** (s)

Ejemplo de clasificación: `IAC A-FLR 25 kA 1 s` significa que la celda resiste un arco interno de 25 kA durante 1 segundo en todos los lados accesibles (frente, laterales y posterior) desde zona de acceso tipo A (personal instruido sin equipos de protección especiales).

Los valores de corriente de arco más habituales coinciden con los de Ik: 16, 20, 25, 31,5 y 40 kA. La duración típica es **0,1 s** (tiempo de actuación de protecciones rápidas), **0,5 s** y **1 s**.

### Cinco criterios de aceptación (IEC 62271-200 Annex A)

El ensayo se supera solo si se cumplen simultáneamente los cinco criterios:

| Criterio | Descripción |
|----------|-------------|
| 1 | Las puertas y paneles de acceso no se abren, no se desprenden fragmentos peligrosos |
| 2 | No se producen perforaciones en los lados accesibles hasta 2 m de altura desde el suelo |
| 3 | Los indicadores horizontales (papel de estaño negro) situados a 0,3 m de la celda no se inflaman |
| 4 | Los indicadores verticales (papel de algodón) situados a 0,3 m de la celda no se inflaman |
| 5 | La conexión a tierra de la envolvente se mantiene efectiva durante y tras el ensayo |

Un fallo en cualquier criterio invalida la clasificación IAC para ese lado. La práctica en diseño de sala eléctrica es disponer las celdas con el lado trasero contra la pared cuando la clasificación IAC solo cubre frente y laterales (IAC A-FL).

---

## Criterios de selección de celdas MT en proyecto

La selección de la celda correcta requiere verificar, al menos, los parámetros siguientes en el orden indicado:

1. **Tensión asignada Ur**: debe ser igual o superior a la tensión de la red en el punto de instalación, incluyendo tolerancias de la red (Un × 1,1 para redes europeas 20 kV).

2. **Corriente nominal In**: debe cubrir la máxima carga prevista incluyendo simultaneidad y previsión de crecimiento. Valores habituales en distribución secundaria: 630 A o 1250 A en salidas de línea, 2000 A o 3150 A en barras principales.

3. **Corriente de corta duración Ik y duración tk**: determinado por el cortocircuito trifásico en el punto de instalación (cálculo según IEC 60909) y el tiempo de actuación de la protección de respaldo. En redes de distribución española de 20 kV, los valores típicos de cortocircuito oscilan entre 12,5 kA y 25 kA.

4. **Clase LSC**: LSC2B es obligatoria en instalaciones donde la continuidad de servicio no permite corte de barra para mantenimiento.

5. **Clasificación IAC y accesibilidad**: determinar el tipo de zona (A = sala sin personal permanente / personal instruido, B = posibilidad de personal no instruido en proximidades). La corriente y duración IAC deben coincidir con el fallo máximo posible y el tiempo de disparo de la protección de respaldo (interbloqueo de relé de protección).

6. **Grado de protección IP**: IP3X es mínimo para instalación en sala cerrada. IP54 para instalaciones en exteriores o entornos con polvo o humedad.

7. **Nivel sísmico**: en zonas con peligro sísmico, requerir ensayo sísmico adicional conforme a IEC 62271-300.

---

## Conclusión

IEC 62271-200 estructura los ensayos de tipo de celdas MT en cinco bloques: dieléctrico, temperatura, cortocircuito, IP y arco interno (IAC). La clasificación IAC —con sus cinco criterios de aceptación y su designación de corriente, duración y lados accesibles— es el diferenciador técnico más importante entre un diseño de celda convencional y uno apto para instalaciones donde la seguridad del personal en servicio es prioritaria. Para proyectos de distribución en España, la combinación **LSC2B + PM + IAC A-FL 25 kA 1 s** cubre la mayoría de subestaciones de abonado industrial y centros de transformación de red secundaria. El ingeniero proyectista debe siempre contrastar los datos de cortocircuito calculados con IEC 60909 frente a los valores IAC certificados del fabricante, verificar que la duración de arco ensayada cubre el tiempo de actuación de la protección de respaldo, y exigir el certificado de ensayo de tipo emitido por laboratorio acreditado.
