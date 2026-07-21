---
title: "IA en el Aula Técnica: Guía para Docentes de FP Eléctrica"
description: "Cómo usar inteligencia artificial en el aula técnica de FP Eléctrica: herramientas concretas, casos de uso con normativa REBT e IEC, criterios de selección y limitaciones reales."
pubDate: 2026-07-21
keywords: ["inteligencia artificial aula tecnica", "IA docentes FP electricidad", "ChatGPT ingenieria electrica", "herramientas IA formacion profesional", "IA calculo electrico"]
author: "Editor"
---

La pregunta que recibe cualquier docente de FP Eléctrica hoy no es si debe usar inteligencia artificial en el aula — es qué herramientas son realmente útiles para un técnico, cuáles son ruido de marketing y cuáles tienen limitaciones que el alumno necesita conocer antes de confiar en ellas en obra.

Este artículo no es una introducción a qué es la IA. Es una guía de uso aplicado para quien ya enseña instalaciones eléctricas, cálculo de secciones, protecciones o automatización, y quiere integrar estas herramientas con criterio técnico.

## Por qué la IA interesa específicamente a la docencia electrotécnica


Los modelos de lenguaje grandes (LLMs) como GPT-4, Claude o Gemini tienen un sesgo de entrenamiento favorable para la ingeniería eléctrica: el corpus técnico disponible en internet — normativa IEC, artículos académicos de IEEE, manuales de fabricante — está razonablemente bien representado. Esto los hace más fiables en consultas de electrotécnica que en dominios con menos documentación estructurada.

Sin embargo, el rendimiento no es uniforme:

| Tipo de consulta | Fiabilidad del LLM | Riesgo principal |
|---|---|---|
| Explicar conceptos físicos (ley de Ohm, circuito RLC) | Alta | Ninguno relevante |
| Interpretar artículos normativos (ITC-BT, IEC 60364) | Media-alta | Confusión entre ediciones |
| Calcular secciones o calibres con datos concretos | Media | Errores aritméticos en cadenas largas |
| Diseñar esquemas de protección completos | Baja | Omisión de condiciones de selectividad |
| Verificar conformidad de una instalación real | No apto | Usa siempre herramienta específica |

Esta tabla es el primer material que conviene mostrar al alumno antes de que empiece a usar cualquier chatbot para resolver problemas técnicos.

## Herramientas de IA con aplicación directa en el aula

### Modelos de lenguaje para generación de materiales

**ChatGPT (GPT-4o)**, **Claude (Anthropic)** y **Gemini 2.5 Pro** son los tres con mayor masa crítica de uso docente en 2026. Todos tienen API accesible y versión gratuita con límites de contexto.

Usos prácticos en FP Eléctrica:
- Generar baterías de problemas de cálculo de intensidades admisibles según IEC 60364-5-52, con variaciones de sección, material del conductor y temperatura ambiente
- Crear casos de diagnóstico de averías: "la línea alimenta un motor de 15 kW y el diferencial dispara en arranque — describe tres causas posibles ordenadas por probabilidad"
- Redactar memorias técnicas de instalaciones-tipo en formato REBT para que el alumno las corrija e identifique errores intencionados

El prompt de partida importa. Un prompt débil produce contenido genérico; un prompt técnico produce material directamente usable:

```
Actúa como un ingeniero electricista. Genera 5 problemas de cálculo
de sección de cable para una instalación trifásica en 400 V,
método de instalación B1 según IEC 60364-5-52, conductor de cobre,
temperatura ambiente 30 °C. Para cada problema incluye la solución
con la intensidad de diseño, la intensidad admisible de la tabla
y el factor de corrección aplicado. Dificultad progresiva.
```

### Herramientas de simulación asistida por IA

**GElectrical** (open source, implementa IEC 60909-0 para cortocircuitos e IEC 60364-5-52 para secciones) combinado con consulta lateral a un LLM permite un flujo de trabajo pedagógicamente sólido:

1. El alumno define la topología en GElectrical
2. El simulador calcula las corrientes de cortocircuito según la norma
3. El LLM interpreta los resultados y sugiere ajustes de protecciones

Este flujo enseña algo importante: el LLM es el asistente de interpretación, no el motor de cálculo. El motor de cálculo certificado sigue siendo la herramienta específica.

### Generadores de materiales visuales

**Canva AI** y herramientas similares permiten generar presentaciones técnicas en minutos. La advertencia pedagógica: los esquemas eléctricos generados por IA suelen tener errores simbólicos (simbología no normalizada, referencias incorrectas a UNE-EN 60617). Usarlos como borrador para que el alumno detecte y corrija los errores convierte una limitación en un ejercicio de calidad técnica.

## Casos de uso concretos en el aula de FP Eléctrica

### Generación de supuestos de cálculo diferenciados

Un grupo de 20 alumnos puede recibir 20 versiones del mismo problema de cálculo de sección (ITC-BT-19) con datos diferentes: distancia, potencia, tensión de suministro, factor de potencia, temperatura ambiente. El docente genera los 20 enunciados con un único prompt bien estructurado en 3 minutos.

### Simulación de inspección técnica

El LLM puede adoptar el rol de inspector de la empresa distribuidora y hacer preguntas técnicas sobre una instalación descrita por el alumno. El alumno defiende sus decisiones de diseño citando normativa concreta. Es un roleplay técnico que entrena la argumentación normativa sin necesidad de una instalación real.

Ejemplo de prompt para el docente:

```
Actúa como inspector de ENDESA revisando la memoria técnica de una
instalación de grupo I (vivienda unifamiliar) de 9.200 W de potencia
prevista según ITC-BT-10. Haz preguntas técnicas específicas sobre
la sección del circuito general, el calibre del ICP y la protección
diferencial. Exige justificación normativa en cada respuesta.
```

### Redacción y revisión de protocolos de verificación

La IEC 60364-6 define los ensayos de recepción de instalaciones eléctricas. Pedir a un LLM que genere un protocolo de verificación paso a paso para una instalación de local comercial (grupo 3) es un ejercicio válido: el alumno contrasta el resultado con la norma y señala lo que falta o está mal. Los ensayos que el LLM suele omitir son la medida de la resistencia de bucle de fallo y la verificación del tiempo de disparo diferencial con corriente de prueba 5·IΔn.

## Criterios de selección de herramientas IA para docentes técnicos


No toda herramienta IA sirve para cada tipo de tarea. Estos criterios permiten elegir sin necesidad de probar todo:

| Criterio | Preguntas a responder | Herramienta adecuada |
|---|---|---|
| **Generación de texto técnico** | ¿Necesita citar normativa? ¿Longitud > 500 palabras? | Claude, GPT-4o |
| **Cálculo verificable** | ¿El resultado tiene impacto en seguridad? | GElectrical, ETAP — nunca solo LLM |
| **Imagen técnica** | ¿Simbología UNE-EN 60617 correcta? | Revisar manualmente siempre |
| **Evaluación automática** | ¿Respuestas abiertas de cálculo? | LLM con rúbrica explícita en el prompt |
| **Búsqueda normativa** | ¿Necesita la versión vigente? | Fuente primaria (AENOR, IEC e-tech) |

La regla operativa más importante: **cualquier valor numérico que el alumno vaya a usar en una instalación real debe verificarse contra la fuente normativa o la herramienta certificada**. Los LLMs tienen probabilidad no nula de error aritmético en cálculos de varias etapas, especialmente en la suma vectorial de impedancias del método IEC 60909-0.

### Integración con el currículo de FP

La Ley Orgánica 3/2022 de Ordenación e Integración de la Formación Profesional incluye la competencia digital entre las competencias clave de cada título. Los títulos de la familia Electricidad y Electrónica — CFGS Sistemas de Automatización Industrial y CFGM Instalaciones Eléctricas y Automáticas — tienen margen curricular para integrar herramientas IA como parte de la competencia de gestión de información técnica.

El marco DigCompEdu del INTEF sitúa el uso de IA docente en el área 2 (recursos digitales) y área 3 (pedagogías digitales), con énfasis en la evaluación crítica de las salidas generadas. Menos del 30 % del profesorado de FP en España se considera preparado para el uso intensivo de IA en el aula según el estudio de Digitalización Educativa 2024.

## Limitaciones que el alumno debe conocer desde el primer día

No es pedagógicamente honesto enseñar IA sin enseñar sus fallos específicos para la ingeniería eléctrica:

1. **Alucinación de valores normativos**: los LLMs pueden citar tablas de intensidades admisibles con valores incorrectos o de ediciones anteriores. La revisión 2021 de IEC 60364-5-52 introdujo cambios en los factores de corrección por temperatura que muchos LLMs no tienen correctamente representados.

2. **Error en cálculo de cortocircuito**: el método de impedancias (IEC 60909-0) implica sumas vectoriales de impedancias de red, transformador, cable y motor. Los LLMs cometen errores en la gestión de las componentes resistiva y reactiva cuando la cadena tiene más de tres elementos en serie.

3. **Desconocimiento de condiciones locales**: el LLM no sabe si la instalación está en zona ATEX, si hay restricciones de la empresa distribuidora local o si el proyecto requiere visado colegial. Estas condiciones cambian decisiones de diseño.

4. **Obsolescencia del corpus de entrenamiento**: los datos de entrenamiento tienen fecha de corte. Normativa publicada en los últimos 12-18 meses puede no estar representada correctamente.

## Conclusión

La inteligencia artificial en el aula técnica de FP Eléctrica tiene valor real cuando se usa como generador de materiales, simulador de escenarios de evaluación y asistente de interpretación normativa. No tiene valor — y es peligroso — cuando se usa como sustituto de herramientas de cálculo certificadas o como fuente primaria de normativa.

El docente que integra IA con criterio técnico enseña dos cosas simultáneamente: el contenido electrotécnico y la competencia crítica para evaluar herramientas digitales. Ambas serán necesarias para el técnico que salga del ciclo en 2026 y trabaje en instalaciones donde los errores tienen consecuencias físicas reales.

El primer ejercicio práctico sugerido: pide a un LLM que calcule la sección de un cable para una carga concreta según ITC-BT-19, luego resuelve el mismo problema con la tabla B.52.3 de IEC 60364-5-52 y compara. La diferencia entre ambos resultados, y la razón de esa diferencia, ya es una lección de ingeniería eléctrica.
