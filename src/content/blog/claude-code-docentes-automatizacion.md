---
title: "Claude Code para docentes: automatiza tareas administrativas"
description: "Guía técnica para docentes de FP Eléctrica: cómo usar Claude Code CLI para automatizar correcciones, rúbricas, memorias y documentación bajo Ley FP 3/2022."
pubDate: 2026-08-01
keywords: ["claude code docentes automatizacion", "IA automatizacion tareas docentes FP", "claude code electrotecnia", "automatizar rubricas evaluacion FP", "inteligencia artificial docente ingenieria electrica"]
author: "Editor"
heroImage: /images/claude-code-docentes-automatizacion.svg
---

El docente de FP Eléctrica dedica entre 8 y 12 horas semanales a tareas que no son enseñar: redactar memorias de módulo, generar variantes de examen, escribir informes individuales para familias, actualizar programaciones didácticas tras cambios normativos. Claude Code, la interfaz de línea de comandos de Anthropic disponible desde mayo de 2025, convierte una parte significativa de ese tiempo en procesos automatizables con comandos concretos.

Este artículo no explica qué es la inteligencia artificial. Explica qué comandos ejecutar, qué prompts estructurar y qué criterios aplicar para que un docente de ciclos de la familia Electricidad y Electrónica recupere horas reales cada semana.

## Qué es Claude Code y en qué se diferencia del chatbot de navegador

Claude.ai (el chatbot web) es conversacional: responde consultas de una en una, sin memoria de sesión persistente ni acceso al sistema de archivos local. Claude Code es una CLI que se instala en el terminal y opera sobre el repositorio de archivos del usuario, ejecuta scripts, procesa lotes de documentos y mantiene contexto entre operaciones dentro de una sesión.

La diferencia operativa para un docente:

| Herramienta | Puede procesar 30 exámenes a la vez | Accede a archivos locales | Genera y guarda ficheros | Ejecuta scripts Python/Bash |
|---|---|---|---|---|
| Claude.ai (web) | No | No | No | No |
| Claude Code (CLI) | Sí | Sí | Sí | Sí |
| API Anthropic directa | Sí (con código propio) | Según implementación | Sí | Sí |

Claude Code actúa como un agente que lee, transforma y escribe documentos. Para un docente sin perfil de programador, la curva de entrada es baja: los comandos se escriben en lenguaje natural y Claude Code los interpreta. Para un docente con perfil técnico (FP Eléctrica, Automatización Industrial), la integración con scripts Python o Bash amplía el alcance considerablemente.

La instalación requiere Node.js ≥18 y una API key de Anthropic. El coste de uso por token es de 0,003 USD por cada 1.000 tokens de entrada en el modelo Sonnet (datos de julio de 2026). Generar una programación didáctica completa de un módulo de 224 horas consume aproximadamente 12.000-18.000 tokens: entre 0,04 y 0,06 USD por documento.

## Tareas administrativas del docente de FP que Claude Code automatiza

La Ley Orgánica 3/2022 de Ordenación e Integración de la FP establece en su artículo 40 la obligación de disponer de programaciones didácticas actualizadas y referenciadas al Catálogo Nacional de Cualificaciones Profesionales (CNCP). Cada ciclo que incorpora nuevas competencias digitales — lo que afecta a todos los títulos de la familia Electricidad y Electrónica desde la actualización de 2024 — implica reescribir secciones de programación. Claude Code puede tomar la programación vigente como entrada y regenerar las secciones afectadas manteniendo el formato institucional.

**Corrección de ejercicios con rúbrica:**

El flujo más inmediato: el docente tiene 25 respuestas escaneadas (PDF o texto plano) y una rúbrica con criterios ponderados. Claude Code procesa el lote en una sola invocación:

```
/project:path/to/examenes
Evalúa cada fichero .txt de este directorio según la rúbrica adjunta
(rubrica.md). Para cada alumno genera: nota por criterio, nota final
sobre 10, comentario de 2 líneas para el informe de familia. Exporta
como CSV. Criterio 3 (seguridad eléctrica ITC-BT-24) pondera 30%.
```

El tiempo de procesamiento para 25 exámenes es inferior a 3 minutos frente a las 2-3 horas de corrección manual.

**Generación de variantes de examen:**

Útil para evitar copia en grupos paralelos o para las convocatorias extraordinarias. Un examen base de 10 preguntas sobre sección de cable (ITC-BT-19, tabla 1) puede generar 4 variantes con datos numéricos distintos, misma dificultad y soluciones incluidas:

```
Toma examen_base.md y genera 4 variantes. Mantén la estructura y
dificultad. Varía: secciones de cable (1,5 / 2,5 / 4 / 6 mm²),
distancias (15, 20, 25, 30 m), cargas (1.500-3.500 W en pasos de 500 W).
Para cada variante incluye la solución paso a paso según IEC 60364-5-52
tabla B.52.3 e ITC-BT-15. Exporta como examen_v1.md, examen_v2.md...
```

**Redacción de informes individuales:**

La normativa de evaluación de FP (Orden EFP/844/2021 en el marco estatal, con desarrollos autonómicos) requiere informes individualizados en ciertos supuestos: módulos con resultado negativo en evaluación ordinaria, alumnos con adaptación curricular, solicitudes de revisión. Estos informes son documentos técnicos con formato regulado. Claude Code los genera desde una plantilla y los datos del alumno en menos de 30 segundos por informe.

## Flujos de trabajo reales: comandos y prompts aplicados

![Claude Code vs Claude.ai: diferencias clave para docentes](/images/claude-code-docentes-automatizacion-2.svg)

La diferencia entre un uso superficial y un uso productivo de Claude Code está en la especificidad del prompt. A continuación se muestran tres flujos verificados para el contexto de FP Eléctrica.

### Actualización de programación didáctica tras cambio normativo

Cuando el Real Decreto que actualiza un título publica nuevos resultados de aprendizaje (RA), hay que revisar la programación módulo por módulo. Claude Code puede comparar el RD anterior con el nuevo y listar los cambios que afectan a cada unidad de trabajo:

```
Lee rd_anterior.txt y rd_nuevo.txt. Identifica los resultados de
aprendizaje del módulo 'Instalaciones Eléctricas Interior' que han
cambiado, añadido o eliminado. Para cada cambio, indica qué unidades
de trabajo de programacion_modulo.md deben modificarse y sugiere
el nuevo texto normativo. Formato: tabla con columnas RA, tipo_cambio,
unidad_afectada, texto_propuesto.
```

### Generación de casos prácticos con valores reales IEC

Para el módulo de Instalaciones Eléctricas, los casos prácticos requieren datos coherentes con las tablas de intensidades admisibles de IEC 60364-5-52. Claude Code puede generar 20 supuestos distintos manteniendo coherencia con los valores normalizados de la tabla B.52.3 (instalación en tubo empotrado, temperatura 30 °C):

- Sección 1,5 mm² Cu: I_adm = 13,5 A (factor corrección 0,77 para 40 °C si aplica)
- Sección 2,5 mm² Cu: I_adm = 18 A
- Sección 4 mm² Cu: I_adm = 24 A
- Sección 6 mm² Cu: I_adm = 31 A

El prompt especifica estos límites como restricciones de validación, de modo que Claude Code no genera supuestos con valores fuera de tabla.

### Preparación de la memoria de FCT

La Formación en Centros de Trabajo requiere documentación por alumno: acuerdo de colaboración, plan de actividades, hojas de seguimiento semanal, informe final del tutor de empresa y del tutor del centro. Claude Code puede generar el juego completo para un alumno en menos de 2 minutos a partir de una ficha de datos básicos (empresa, periodo, perfil del alumno, objetivos del módulo).

## Integración con la normativa docente vigente

El marco DigCompEdu del INTEF (actualización 2024) sitúa la automatización de tareas mediante IA en el área 6 (facilitación de la competencia digital del alumnado) y en el área 2 (creación y gestión de recursos digitales). Los docentes que integran flujos de trabajo automatizados con Claude Code trabajan específicamente los descriptores 2.2 (creación de recursos digitales propios), 2.3 (gestión de recursos) y 6.3 (empoderamiento del alumnado).

La Ley FP 3/2022 introduce en su artículo 10 la orientación profesional personalizada como obligación del sistema. Generar informes individualizados de manera escalable — algo inviable manualmente con grupos de 20-25 alumnos — pasa a ser factible con Claude Code sin incrementar la carga horaria del docente.

El REGLAMENTO (UE) 2024/1689 de IA (AI Act, aplicable desde agosto de 2026) clasifica los sistemas de IA utilizados en contextos educativos para evaluación como sistemas de **riesgo alto** (Anexo III, punto 3b). Esto no prohíbe su uso, pero impone al centro la obligación de registro y evaluación de conformidad si el sistema IA toma decisiones con impacto directo en los resultados del alumno. Un flujo en el que Claude Code sugiere notas que el docente revisa y valida no activa estas obligaciones; un sistema que publica notas directamente sin revisión humana, sí.

## Criterios de selección: cuándo usar Claude Code y cuándo no

![Flujo de automatización: corrección de exámenes en lote](/images/claude-code-docentes-automatizacion-3.svg)

La adopción de Claude Code para tareas docentes no es todo-o-nada. La tabla siguiente proporciona criterios operativos:

| Tarea | Claude Code adecuado | Claude Code no adecuado | Alternativa si no aplica |
|---|---|---|---|
| Generar enunciados de problemas | Sí, con restricciones numéricas explícitas | Si los valores deben verificarse contra RD específico sin supervisión | Revisión manual del output |
| Corregir exámenes tipo test | Sí, 100% automatizable | — | — |
| Corregir cálculos de sección con verificación IEC | Sí, con validación contra tabla B.52.3 incluida en el prompt | Si no se incluye la tabla como contexto | GElectrical para verificación cruzada |
| Redactar informes de evaluación | Sí, sobre plantilla + datos del alumno | Si el informe tiene efectos jurídicos sin firma docente | El docente firma siempre |
| Actualizar programación tras cambio de RD | Sí, para identificar cambios y sugerir texto | Para aprobar oficialmente la programación | Revisión del equipo docente |
| Diseñar esquemas eléctricos | No | — | AutoCAD Electrical, EPLAN |
| Calcular corrientes de cortocircuito | No | — | GElectrical, ETAP |
| Verificar conformidad de instalación real | No | — | Herramientas certificadas + norma |

El criterio transversal: Claude Code es adecuado cuando el output es texto que un humano revisa antes de usar. No es adecuado cuando el output tiene efectos directos sobre instalaciones reales, normativa aplicable o decisiones académicas sin revisión.

**Gestión del coste:**

A 0,003 USD/1.000 tokens de entrada y 0,015 USD/1.000 tokens de salida (modelo Sonnet, julio 2026), el coste mensual de un docente que automatiza la corrección de 4 exámenes por mes (25 alumnos × 4 módulos), genera variantes de examen y redacta informes de FCT se sitúa entre 3 y 8 USD/mes, muy por debajo del valor del tiempo recuperado.

## Conclusión

Claude Code no elimina el trabajo docente — elimina el trabajo docente repetitivo. Un docente de FP Eléctrica que implemente los flujos descritos en este artículo recupera entre 4 y 8 horas semanales que actualmente se destinan a generación mecánica de documentos, corrección de respuestas cerradas y redacción de informes con estructura fija.

El primer paso práctico: instala Claude Code, toma el último examen que corregiste manualmente, escribe la rúbrica que usaste como texto plano y comprueba cuánto tiempo tarda en procesar 10 respuestas. La diferencia entre ese tiempo y las horas que invertiste es la magnitud real del problema que tienes sobre la mesa.

Para tareas con impacto en seguridad eléctrica o en decisiones académicas con efectos jurídicos, la supervisión humana es obligatoria por normativa (AI Act 2024/1689) y por sentido técnico. Para el resto de la carga administrativa, la automatización ya está disponible y no requiere perfil de programador para implementarla.
