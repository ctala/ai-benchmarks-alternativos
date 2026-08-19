# Claude Sonnet 5 — presentation/slide_outline

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.2 | quality: 9.8
- latency_total: 33.243s | tokens_per_second: 100.1
- input_tokens: 217 | output_tokens: 3329
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, proporcionando un esquema detallado y bien estructurado que cubre todos los aspectos solicitados para la presentación ejecutiva.

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

## **Slide 1: Portada**
**Contenido:**
- Título: "Plataforma Digital 2.0 – Estado del Proyecto"
- Subtítulo: Revisión Trimestral para el Board
- Fecha de presentación
- Presentador(es) / Sponsor ejecutivo

**Visual sugerido:** Imagen corporativa de alto impacto / logo del proyecto

**Notas del presentador:** Agradecer el tiempo del board y establecer el tono: transparencia sobre avances, riesgos y decisiones necesarias.

---

## **Slide 2: Agenda**
**Contenido:**
- Estado actual y contexto del proyecto
- Métricas de progreso y avance
- Presupuesto ejecutado vs. planeado
- Riesgos y mitigaciones
- Roadmap Q2-Q3
- Asks específicos al board

**Visual sugerido:** Diagrama de línea de tiempo horizontal con las 6 secciones

**Notas del presentador:** Marcar que la presentación durará X minutos con espacio para preguntas al final de cada bloque crítico.

---

## **Slide 3: Resumen Ejecutivo (Executive Summary)**
**Contenido:**
- Estado general: Verde/Amarillo/Rojo (semáforo)
- Principal logro del trimestre
- Principal riesgo o bloqueo
- Decisión clave que se solicitará al board

**Visual sugerido:** Dashboard tipo "scorecard" con semáforos (Alcance, Tiempo, Presupuesto, Calidad)

**Notas del presentador:** Este slide debe funcionar como "resumen de una sola mirada" en caso de que se interrumpa la reunión.

---

## **Slide 4: Contexto y Objetivos del Proyecto**
**Contenido:**
- Objetivo estratégico de la Plataforma 2.0
- Alineación con OKRs corporativos
- Alcance original vs. alcance actual
- Stakeholders clave involucrados

**Visual sugerido:** Diagrama de alineación estratégica (mapa de objetivos)

**Notas del presentador:** Reconectar brevemente el proyecto con la visión estratégica para dar marco a las decisiones que vienen después.

---

## **Slide 5: Estado Actual del Proyecto**
**Contenido:**
- Fase actual del proyecto (ej. desarrollo, UAT, piloto)
- % de avance global
- Hitos completados en el último trimestre
- Próximos hitos inmediatos

**Visual sugerido:** Gráfico de Gantt simplificado o barra de progreso por fase

**Notas del presentador:** Enfatizar los hitos cumplidos y anticipar el próximo hito crítico para generar confianza.

---

## **Slide 6: Métricas de Progreso — Avance por Workstream**
**Contenido:**
- Avance por módulo/equipo (Frontend, Backend, Integraciones, QA)
- % completado vs. plan original
- Velocity del equipo (sprints completados vs. planeados)
- Comparación trimestre anterior vs. actual

**Visual sugerido:** Gráfico de barras comparativo por workstream

**Notas del presentador:** Detallar cuál workstream está adelantado y cuál requiere atención sin entrar en detalle técnico excesivo.

---

## **Slide 7: Métricas de Calidad y Adopción**
**Contenido:**
- Resultados de pruebas (bugs críticos, cobertura de testing)
- Feedback de usuarios piloto (NPS o CSAT si aplica)
- Tasa de adopción en fase piloto
- Comparación con benchmarks de la industria

**Visual sugerido:** Gráfico de líneas (tendencia de adopción) + tabla de KPIs

**Notas del presentador:** Usar datos de adopción para mostrar validación temprana del valor de negocio, no solo avance técnico.

---

## **Slide 8: Presupuesto Ejecutado vs. Planeado**
**Contenido:**
- Presupuesto total aprobado
- Gasto acumulado a la fecha (% ejecutado)
- Desviación por categoría (personal, licencias, infraestructura, terceros)
- Proyección de gasto a cierre de proyecto

**Visual sugerido:** Gráfico de barras apiladas (planeado vs. real) + tabla de desviaciones

**Notas del presentador:** Ser directo sobre cualquier desviación >10% y tener lista la causa raíz antes de que lo pregunten.

---

## **Slide 9: Análisis de Variación Presupuestaria**
**Contenido:**
- Principales causas de sobrecosto/ahorro
- Impacto en el forecast final
- Acciones correctivas ya implementadas
- Necesidad de reasignación de fondos (si aplica)

**Visual sugerido:** Gráfico de cascada (waterfall) mostrando variaciones

**Notas del presentador:** Este slide prepara el terreno para el "ask" de presupuesto adicional si es necesario, mostrado más adelante.

---

## **Slide 10: Mapa de Riesgos**
**Contenido:**
- Top 5 riesgos activos (probabilidad x impacto)
- Riesgos nuevos vs. trimestre anterior
- Riesgos cerrados/mitigados exitosamente
- Owner de cada riesgo crítico

**Visual sugerido:** Matriz de riesgos (heat map, probabilidad vs. impacto)

**Notas del presentador:** Priorizar la conversación en los 2 riesgos de mayor impacto; el resto se puede referenciar en el apéndice.

---

## **Slide 11: Riesgo Crítico #1 — Detalle y Plan de Mitigación**
**Contenido:**
- Descripción del riesgo (ej. dependencia de proveedor externo)
- Impacto potencial en timeline/presupuesto
- Plan de mitigación y responsable
- Fecha estimada de resolución

**Visual sugerido:** Diagrama de flujo del plan de contingencia

**Notas del presentador:** Ser específico y transparente; el board valora más un plan de acción claro que la ausencia de riesgos.

---

## **Slide 12: Riesgo Crítico #2 — Detalle y Plan de Mitigación**
**Contenido:**
- Descripción del riesgo (ej. resistencia al cambio / adopción interna)
- Impacto potencial en adopción y ROI
- Plan de mitigación (change management, comunicación)
- Indicadores de seguimiento

**Visual sugerido:** Diagrama de flujo o tabla de plan de acción con fechas

**Notas del presentador:** Vincular este riesgo con el impacto en el negocio, no solo en el proyecto, para mantener la atención del board.

---

## **Slide 13: Roadmap Q2-Q3**
**Contenido:**
- Hitos clave planificados para Q2
- Hitos clave planificados para Q3
- Dependencias críticas entre fases
- Fecha estimada de go-live / lanzamiento completo

**Visual sugerido:** Timeline/Roadmap visual (línea de tiempo horizontal con hitos)

**Notas del presentador:** Conectar el roadmap con los riesgos mencionados antes, mostrando cómo las mitigaciones aseguran las fechas comprometidas.

---

## **Slide 14: Impacto Esperado en el Negocio**
**Contenido:**
- Beneficios esperados post-lanzamiento (eficiencia, ingresos, satisfacción del cliente)
- ROI proyectado y timeline de recuperación de inversión
- KPIs de éxito post-implementación
- Comparación con el business case original

**Visual sugerido:** Gráfico de proyección ROI (línea de tiempo con punto de equilibrio)

**Notas del presentador:** Reforzar el "por qué" del proyecto conectando avances técnicos con valor de negocio tangible para el board.

---

## **Slide 15: Asks al Board / Próximos Pasos**
**Contenido:**
- Ask #1: Aprobación de presupuesto adicional (si aplica) — monto y justificación
- Ask #2: Decisión sobre alcance/priorización de features
- Ask #3: Apoyo en gestión de riesgo crítico (ej. sponsorship ejecutivo para adopción)
- Fecha de próxima revisión con el board

**Visual sugerido:** Tabla resumen de "Asks" con decisión requerida y fecha límite

**Notas del presentador:** Cerrar con claridad absoluta sobre qué se necesita del board hoy, evitando ambigüedad para facilitar una decisión en la misma reunión.

---

### 💡 Recomendaciones adicionales para la ejecución:
- **Slide de respaldo (Apéndice):** Incluir detalle técnico y riesgos secundarios para responder preguntas sin saturar la presentación principal.
- **Tiempo sugerido:** 20-25 minutos de presentación + 15-20 minutos de Q&A.
- **Tono:** Datos concretos, sin tecnicismos excesivos, siempre conectando con impacto de negocio y decisiones requeridas.