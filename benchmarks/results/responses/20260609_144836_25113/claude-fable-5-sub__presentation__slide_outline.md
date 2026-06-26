# Claude Fable 5 (suscripción) — presentation/slide_outline

- model_id: `claude-fable-5`
- success: True  | final: 6.35 | quality: 8.34
- latency_total: 69.712s | tokens_per_second: 74.7
- input_tokens: 2 | output_tokens: 5205

## Respuesta completa

# Outline: Presentación al Board — Estado del Proyecto "Plataforma Digital 2.0"

**15 slides · 20-25 min presentación + 10 min Q&A**

> Nota: donde aparecen cifras entre corchetes `[X]`, son placeholders a completar con los datos reales del proyecto.

---

## Slide 1 — Portada: Plataforma Digital 2.0 — Reporte de Estado al Board

**Contenido:**
- Nombre del proyecto y logo corporativo
- Fecha de la presentación y período cubierto (ej. Q1 2026)
- Presentador: [nombre, cargo — ej. Director de Proyecto / CTO]
- Clasificación: Confidencial — Solo Board

**Visual:** Imagen hero del producto (screenshot o mockup de la plataforma) sobre fondo corporativo.

**Notas del presentador:** Abrir con contexto en una frase: "Hoy les traigo el estado de Plataforma Digital 2.0 al cierre de Q1, con foco en tres decisiones que necesitamos del board." Anticipar desde el inicio que habrá asks concretos al final.

---

## Slide 2 — Resumen Ejecutivo (TL;DR)

**Contenido:**
- Estado general: 🟡 En curso con desviaciones controladas (semáforo)
- Avance: [68%] del alcance completado vs [75%] planificado
- Presupuesto: [$2.4M] ejecutado de [$3.2M] aprobado ([75%])
- Fecha de lanzamiento: se mantiene / se desplaza a [fecha]
- 3 asks al board: aprobación de presupuesto adicional, decisión de alcance, contratación clave

**Visual:** Dashboard de 4 KPIs grandes con semáforos (alcance, plazo, presupuesto, riesgo).

**Notas del presentador:** Este slide es para el director que solo verá uno. Si el board recuerda una sola cosa, que sea el semáforo general y los 3 asks. No entrar en detalle aquí.

---

## Slide 3 — Recordatorio: Objetivos y Caso de Negocio

**Contenido:**
- Objetivo estratégico: migrar [X%] de clientes a la nueva plataforma para [fecha]
- Beneficios comprometidos: reducción de costos operativos [$X/año], NPS +[X] puntos
- ROI proyectado original: [X%] a 24 meses
- Alineación con plan estratégico 2025-2027 (pilar de transformación digital)

**Visual:** Diagrama simple de "antes → después" (arquitectura legacy vs Plataforma 2.0) con los 3 beneficios clave anotados.

**Notas del presentador:** 30 segundos máximo — el board aprobó esto hace [X] meses, solo refrescar el "por qué" antes de mostrar el "cómo vamos". Sirve de ancla para evaluar las desviaciones que vienen.

---

## Slide 4 — Estado Actual: Qué Está Hecho

**Contenido:**
- ✅ Módulo de autenticación y onboarding: completado y en producción
- ✅ Migración de datos fase 1: [X] registros migrados, [99.X%] integridad validada
- ✅ Integraciones core ([ERP/CRM/pagos]): 3 de 5 operativas
- 🔄 En curso: módulo de reportería y app móvil
- Piloto activo con [X] clientes / usuarios internos

**Visual:** Diagrama de módulos del producto con código de color (verde = hecho, amarillo = en curso, gris = pendiente).

**Notas del presentador:** Enfatizar que lo crítico (autenticación + datos) ya está en producción sin incidentes mayores. El piloto da evidencia temprana de adopción real, no solo avance técnico.

---

## Slide 5 — Métricas de Progreso vs Plan

**Contenido:**
- Avance de alcance: [68%] real vs [75%] plan (gap de 7 pts)
- Sprints completados: [14 de 20] con velocity promedio [X] puntos
- Hitos: [5 de 7] cumplidos en fecha; 2 desplazados [X semanas]
- Defectos críticos abiertos: [X] (tendencia a la baja desde [Y])

**Visual:** Gráfico de burn-up (alcance completado vs planificado en el tiempo) + tabla pequeña de hitos con fechas plan/real.

**Notas del presentador:** Ser transparente con el gap de 7 puntos: explicar que se origina en [causa concreta, ej. integración con sistema legacy más compleja de lo estimado], no en problemas de ejecución del equipo.

---

## Slide 6 — Métricas de Producto (Piloto)

**Contenido:**
- Usuarios activos en piloto: [X] ([X%] de los invitados)
- Adopción semanal: [X%] de usuarios regresan (retención semana 4)
- NPS del piloto: [X] vs [Y] de la plataforma actual
- Tiempo promedio de tarea clave: [-X%] vs plataforma legacy
- Top 3 feedback de usuarios y qué se hizo con cada uno

**Visual:** Gráfico de líneas de adopción semanal + tarjetas con NPS comparativo (legacy vs 2.0).

**Notas del presentador:** Este slide convierte el proyecto de "esfuerzo de TI" a "valor de negocio medible". El dato más poderoso es la reducción de tiempo de tarea — conectarlo con el ahorro operativo prometido en el caso de negocio.

---

## Slide 7 — Presupuesto: Ejecutado vs Planeado

**Contenido:**
- Presupuesto aprobado: [$3.2M] · Ejecutado a la fecha: [$2.4M] ([75%])
- Plan a la fecha: [$2.2M] → sobre-ejecución de [$200K] ([+9%])
- Desglose: desarrollo [60%], infraestructura [15%], licencias [10%], consultoría [15%]
- Forecast a término: [$3.5M] → desviación proyectada de [+$300K / +9%]

**Visual:** Gráfico de barras comparativo (plan vs real por categoría) + curva S de ejecución acumulada.

**Notas del presentador:** No esconder la sobre-ejecución: nombrarla, cuantificarla y conectarla con la causa (slide siguiente). El forecast a término es el número que el board necesita para el ask de presupuesto del slide 13.

---

## Slide 8 — Análisis de Desviaciones Presupuestarias

**Contenido:**
- Causa #1: integración con [sistema legacy] requirió [X] semanas-persona adicionales ([$150K])
- Causa #2: alza de costos de infraestructura cloud ([+X%] vs cotización original) ([$80K])
- Causa #3: extensión de consultoría de seguridad por hallazgos de auditoría ([$70K])
- Medidas de mitigación ya tomadas: renegociación de contrato cloud, reducción de alcance no crítico

**Visual:** Gráfico waterfall (puente) desde presupuesto plan → desviaciones por causa → forecast final.

**Notas del presentador:** El waterfall hace evidente que la desviación tiene 3 causas identificadas y acotadas, no una pérdida de control. Destacar que [$X] ya se recuperó con las mitigaciones.

---

## Slide 9 — Riesgos Principales

**Contenido:**
- R1 (Alto): dependencia del proveedor [X] para integración de pagos — plan B en evaluación
- R2 (Alto): rotación de talento clave (2 seniors con ofertas externas) — plan de retención activo
- R3 (Medio): cumplimiento normativo [ley de datos / regulación sectorial] — auditoría agendada
- R4 (Medio): adopción de usuarios en migración masiva — programa de change management
- R5 (Bajo): performance bajo carga peak — pruebas de stress en Q2

**Visual:** Matriz de riesgos 3×3 (probabilidad × impacto) con los 5 riesgos posicionados y flechas de tendencia.

**Notas del presentador:** Concentrar el tiempo en R1 y R2 — son los únicos que pueden mover la fecha de lanzamiento. R2 conecta directamente con el ask de contratación del slide 13.

---

## Slide 10 — Riesgos: Planes de Mitigación

**Contenido:**
- R1: negociación paralela con proveedor alternativo; decisión go/no-go el [fecha]
- R2: paquete de retención propuesto ([$X], requiere aprobación) + plan de documentación/redundancia
- R3: contratación de estudio legal especializado; entregable de compliance el [fecha]
- Owner y fecha de revisión asignados para cada riesgo
- Riesgos cerrados desde el último reporte: [2] (mostrar progreso)

**Visual:** Tabla de 4 columnas: riesgo · mitigación · owner · fecha de resolución.

**Notas del presentador:** Cerrar la sección de riesgos con sensación de control: cada riesgo tiene dueño, plan y fecha. Mencionar los riesgos cerrados demuestra que el proceso de gestión funciona.

---

## Slide 11 — Roadmap Q2: Camino al Lanzamiento

**Contenido:**
- Abril: cierre de módulo de reportería + integración de pagos (hito crítico)
- Mayo: pruebas de stress y seguridad + UAT con [X] clientes piloto adicionales
- Junio: migración masiva ola 1 ([X%] de clientes) + go-live general
- Criterios de salida del go-live: [defectos críticos = 0, NPS piloto ≥ X, performance < Xms]

**Visual:** Línea de tiempo / Gantt simplificado con hitos, dependencias críticas marcadas en rojo.

**Notas del presentador:** Subrayar que la integración de pagos (abril) es la dependencia crítica de toda la cadena — si R1 se materializa, todo el Q2 se desplaza. Por eso el go/no-go de ese riesgo es en [fecha].

---

## Slide 12 — Roadmap Q3: Escala y Captura de Valor

**Contenido:**
- Julio: migración olas 2 y 3 (llegar a [100%] de clientes)
- Agosto: apagado de plataforma legacy → inicio de captura de ahorro [$X/mes]
- Septiembre: features de fase 2 (priorizadas con feedback del piloto)
- Métricas de éxito Q3: [X%] adopción, [$X] ahorro acumulado, NPS ≥ [X]

**Visual:** Línea de tiempo continuación de Q2 + gráfico pequeño de proyección de ahorro acumulado mes a mes.

**Notas del presentador:** El mensaje clave: el apagado del legacy en agosto es donde el caso de negocio se vuelve realidad financiera. Cada mes de retraso cuesta [$X] en operación dual.

---

## Slide 13 — Asks al Board

**Contenido:**
- **Ask 1 — Presupuesto:** aprobar [$300K] adicionales (forecast a término [$3.5M], +9%) — sustentado en slide 8
- **Ask 2 — Talento:** aprobar paquete de retención de [$X] para 2 roles críticos — mitiga R2
- **Ask 3 — Decisión de alcance:** confirmar diferimiento del módulo [X] a fase 2 para proteger la fecha de go-live
- Qué pasa si no se aprueban: impacto en fecha [+X semanas] y en ahorro proyectado [-$X]

**Visual:** Tabla de 3 filas: ask · monto/decisión · impacto si se aprueba · impacto si no.

**Notas del presentador:** Este es el slide más importante de la presentación. Presentar cada ask con su trade-off explícito y pedir la decisión hoy o fecha comprometida — no salir de la sala sin un mecanismo de resolución.

---

## Slide 14 — Próximos Pasos y Gobernanza

**Contenido:**
- Próximo reporte al board: [fecha] (post hito crítico de integración de pagos)
- Comité ejecutivo quincenal: seguimiento de riesgos R1 y R2
- Go/no-go de migración masiva: [fecha], con criterios del slide 11
- Canal de escalamiento: [sponsor ejecutivo] para decisiones entre sesiones de board

**Visual:** Calendario simple de hitos de gobernanza (3 meses) con las instancias de decisión marcadas.

**Notas del presentador:** Dar tranquilidad al board sobre el ritmo de seguimiento: no tienen que esperar 3 meses para enterarse de un problema — el go/no-go y el escalamiento están definidos.

---

## Slide 15 — Cierre y Q&A

**Contenido:**
- Recap en 3 líneas: avance [68%] con valor demostrado en piloto · desviación de presupuesto [+9%] acotada y con causa identificada · 3 asks que protegen la fecha de go-live
- Lo que va bien: producto en producción, adopción del piloto, NPS
- Lo que pedimos: las 3 aprobaciones del slide 13
- Contacto y anexos disponibles (detalle financiero, backlog, resultados completos del piloto)

**Visual:** Slide limpio con los 3 mensajes clave + foto del equipo del proyecto (humaniza el cierre).

**Notas del presentador:** Cerrar con confianza: "El proyecto está en buen pie, los problemas tienen plan y dueño, y con estas 3 aprobaciones llegamos al go-live de junio." Abrir Q&A teniendo los anexos a mano para preguntas de detalle financiero.

---

### Anexos sugeridos (backup slides, no presentar)

- A1: Detalle financiero línea por línea (plan vs real vs forecast)
- A2: Registro completo de riesgos (los 5 + cerrados)
- A3: Resultados completos del piloto (encuestas, métricas de uso)
- A4: Arquitectura técnica de la plataforma
- A5: Plan detallado de migración por olas

**Tip de estructura:** la narrativa sigue el arco *contexto → evidencia → problemas → plan → decisión*. Si el tiempo se corta, los slides imprescindibles son 2, 7, 9, 13 — el resto es soporte.