# Claude Sonnet 5 — presentation/slide_outline

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.14 | quality: 9.8
- latency_total: 22.43s | tokens_per_second: 91.3
- input_tokens: 217 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, cubriendo todos los aspectos solicitados con detalles útiles y estructura adecuada para una presentación ejecutiva.

## Entrada exacta (lo que recibió el modelo)

**user:**

Crea el outline completo para una presentacion de 15 slides sobre el estado del proyecto "Plataforma Digital 2.0". La audiencia es el board de directores. Incluye para cada slide:
- Numero y titulo
- Bullet points del contenido (3-5 por slide)
- Tipo de visual sugerido (grafico, tabla, diagrama, imagen)
- Notas del presentador (1-2 oraciones)

La presentacion debe cubrir: estado actual, metricas de progreso, riesgos, presupuesto ejecutado vs planeado, roadmap Q2-Q3, y asks al board.


## Respuesta completa

# Outline: Presentación "Plataforma Digital 2.0" — Board de Directores

---

## Slide 1: Portada
**Contenido:**
- Título: "Plataforma Digital 2.0 — Estado del Proyecto"
- Subtítulo: Presentación al Board de Directores
- Fecha y nombre del presentador/sponsor ejecutivo
- Periodo que cubre el reporte (ej. Q1 2025)

**Visual:** Imagen corporativa / logo del proyecto con diseño limpio

**Notas del presentador:** Agradecer al board por el tiempo y establecer el objetivo de la sesión: informar estado, riesgos y decisiones requeridas.

---

## Slide 2: Agenda
**Contenido:**
- Estado actual y resumen ejecutivo
- Métricas de progreso y avance por fases
- Presupuesto ejecutado vs. planeado
- Riesgos y mitigaciones
- Roadmap Q2-Q3
- Asks al board

**Visual:** Diagrama de flujo horizontal con los 6 puntos numerados

**Notas del presentador:** Explicar brevemente que la presentación dura X minutos y que habrá espacio para preguntas al final de cada sección crítica.

---

## Slide 3: Resumen Ejecutivo
**Contenido:**
- Estado general del proyecto: Verde / Amarillo / Rojo (semáforo)
- % de avance global vs. plan original
- Principal logro del periodo
- Principal desafío del periodo
- Decisión clave que se necesita hoy

**Visual:** Semáforo/indicador tipo dashboard (RAG status) + KPI destacado en número grande

**Notas del presentador:** Este slide es el "elevator pitch" del proyecto; si el board solo recuerda un slide, debe ser este.

---

## Slide 4: Objetivos y Alcance del Proyecto (Recordatorio)
**Contenido:**
- Objetivo estratégico de la Plataforma 2.0
- Alcance funcional (módulos incluidos)
- Fuera de alcance (para evitar ambigüedades)
- Stakeholders clave involucrados

**Visual:** Diagrama de alcance (círculo con "in scope" / "out of scope")

**Notas del presentador:** Refrescar contexto para board members que no siguieron el proyecto desde el inicio o se unieron recientemente.

---

## Slide 5: Estado Actual por Fase/Workstream
**Contenido:**
- Fase 1: Infraestructura — % completado
- Fase 2: Migración de datos — % completado
- Fase 3: Desarrollo funcional — % completado
- Fase 4: Testing y QA — % completado
- Fase 5: Go-live y adopción — % completado

**Visual:** Gráfico de barras horizontales (% avance por fase) o diagrama Gantt simplificado

**Notas del presentador:** Detallar cuál fase está adelantada, cuál en curso normal y cuál presenta atraso, sin entrar aún en causas (se cubre en riesgos).

---

## Slide 6: Métricas de Progreso — KPIs Técnicos
**Contenido:**
- Velocity del equipo (sprints completados vs. planeados)
- % de funcionalidades entregadas vs. backlog total
- Deuda técnica identificada y resuelta
- Cobertura de pruebas automatizadas
- Incidencias críticas abiertas/cerradas

**Visual:** Gráfico de líneas mostrando tendencia de velocity y burn-down chart

**Notas del presentador:** Enfatizar tendencia (mejorando/empeorando) más que el número absoluto en un solo periodo.

---

## Slide 7: Métricas de Progreso — KPIs de Negocio
**Contenido:**
- Usuarios piloto activos / adopción temprana
- Feedback cualitativo de usuarios clave
- Tiempo estimado de reducción de procesos (ej. -30% en tiempo de atención)
- Comparación con métricas del sistema legado

**Visual:** Gráfico comparativo (antes/después) tipo barras dobles

**Notas del presentador:** Conectar métricas técnicas con impacto de negocio tangible para mantener el interés del board.

---

## Slide 8: Presupuesto Ejecutado vs. Planeado — Visión General
**Contenido:**
- Presupuesto total aprobado
- Monto ejecutado a la fecha (%)
- Variación (+/-) vs. plan
- Proyección de cierre estimado

**Visual:** Gráfico de barras apiladas (planeado vs. ejecutado) o gauge chart

**Notas del presentador:** Ser transparente sobre cualquier desviación y anticipar la pregunta obvia: "¿por qué la variación?"

---

## Slide 9: Presupuesto — Detalle por Categoría
**Contenido:**
- Desarrollo/tecnología: planeado vs. ejecutado
- Consultoría externa: planeado vs. ejecutado
- Infraestructura/licencias: planeado vs. ejecutado
- Capacitación y cambio organizacional: planeado vs. ejecutado

**Visual:** Tabla comparativa con columnas (Categoría | Planeado | Ejecutado | Variación %)

**Notas del presentador:** Detallar la categoría con mayor desviación y explicar la causa raíz brevemente (ej. sobrecosto en consultoría por extensión de alcance).

---

## Slide 10: Riesgos Identificados — Matriz de Riesgos
**Contenido:**
- Riesgo 1: Retraso en integración con sistemas legados (Prob. Alta / Impacto Alto)
- Riesgo 2: Rotación de talento clave del equipo (Prob. Media / Impacto Alto)
- Riesgo 3: Resistencia al camb