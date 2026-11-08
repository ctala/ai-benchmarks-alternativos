# Tencent Hy4 — presentation/slide_outline

- model_id: `tencent/hy4`
- success: True  | final: 8.51 | quality: 9.8
- latency_total: 29.477s | tokens_per_second: 85.3
- input_tokens: 162 | output_tokens: 2513
- judge_score: 5.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Crea el outline completo para una presentacion de 15 slides sobre el estado del proyecto "Plataforma Digital 2.0". La audiencia es el board de directores. Incluye para cada slide:
- Numero y titulo
- Bullet points del contenido (3-5 por slide)
- Tipo de visual sugerido (grafico, tabla, diagrama, imagen)
- Notas del presentador (1-2 oraciones)

La presentacion debe cubrir: estado actual, metricas de progreso, riesgos, presupuesto ejecutado vs planeado, roadmap Q2-Q3, y asks al board.


## Respuesta completa

Aquí tienes el outline profesional, estructurado con lenguaje ejecutivo y orientado a la toma de decisiones, ideal para un Board de Directores.

---

# 🎯 Presentación: Estado del Proyecto «Plataforma Digital 2.0»
**Audiencia:** Board de Directores | **Duración estimada:** 20 min + 10 min Q&A | **Formato:** 15 slides

---

| # | Título | Bullet Points | Visual Sugerido | Notas del Presentador |
|---|--------|---------------|-----------------|------------------------|
| **1** | **Portada & Contexto Estratégico** | • Plataforma Digital 2.0: motor de crecimiento 2024–2025<br>• Alineada a 3 pilares: Experiencia, Escalabilidad, Data-Driven<br>• Update trimestral al Board (Corte: 30 abril)<br>• Objetivo de la sesión: validar rumbo + aprobar asks | Imagen corporativa + línea de tiempo estratégica (2023 → 2025) | *Abrir con el “para qué” más que con el “qué”. Recordar que este proyecto es el habilitador del plan comercial.* |
| **2** | **Resumen Ejecutivo (1-pager)** | • **En verde:** 78% de alcance completado, Go-Live Fase 1 en tiempo<br>• **En ámbar:** 2 riesgos de integración con proveedor legacy<br>• **En rojo:** Ninguno crítico<br>• Presupuesto ejecutado: 62% vs 65% planeado<br>• Hoy solicitamos 2 decisiones (Slide 14) | Semáforo ejecutivo (Dashboard de 4 cuadrantes) | *Si el Board solo lee un slide, que sea este. No entrar en detalle aún; anticipar que los asks vienen al final.* |
| **3** | **Alcance & Arquitectura Entregada** | • Migración de frontend a micro-frontends (✅ 100%)<br>• API Gateway unificado (✅ 100%)<br>• Módulo de autenticación SSO (✅ 100%)<br>• Data Lake en fase de carga (🔄 70%)<br>• Módulo de recomendaciones (⏳ Q3) | Diagrama de arquitectura (capas: Cliente / API / Datos / Legacy) | *Destacar que lo ya entregado reduce el riesgo técnico de la Fase 2. Evitar jerga profunda.* |
| **4** | **Cronograma: Planeado vs Real** | • Hitos Fase 1: 6/6 entregados en fecha<br>• Desviación máxima: +3 días (entorno de staging)<br>• Fase 2 inicia 15 mayo (2 semanas de buffer)<br>• Go-Live comercial: 12 septiembre (sin cambios) | Gráfico de Gantt simplificado (barras planeado vs real) | *Enfatizar el buffer: es el primer trimestre que cerramos sin reprogramación.* |
| **5** | **Métricas de Progreso (Delivery)** | • Velocity promedio: 34 SP/sprint (target: 32)<br>• Lead time: 4.2 días (↓ 28% vs Q4)<br>• Defectos en producción: 0.4 / 1k transacciones<br>• Cobertura de tests automatizados: 86% (↑ de 61%)<br>• Disponibilidad staging: 99.5% | Gráfico de líneas (tendencia 4 meses) + KPI cards | *La caída en lead time es el dato más relevante: indica madurez del equipo, no solo velocidad.* |
| **6** | **Métricas de Negocio (Early Signals)** | • +18% conversión en flujo de checkout (piloto 10% tráfico)<br>• Tiempo de carga: 1.9s (vs 3.4s legacy)<br>• NPS piloto interno: 62 (vs 41 baseline)<br>• 0 incidentes de seguridad reportados<br>• Adopción SSO: 94% usuarios corporativos | Gráfico de barras comparativas (Legacy vs 2.0) | *Aclarar que son señales tempranas, no impacto full-P&L aún. Esto justifica acelerar el rollout.* |
| **7** | **Presupuesto: Ejecutado vs Planeado** | • Presupuesto total aprobado: USD 2.4M<br>• Ejecutado al corte: USD 1.49M (62%)<br>• Planeado al corte: USD 1.56M (65%) → **-3 pp eficiencia**<br>• Ahorro principal: licencias cloud (renegociación)<br>• Proyección cierre: USD 2.32M (↓ 3.3% vs budget) | Tabla + Gráfico de barras apiladas (Capex / Opex / Cloud) | *No es sub-ejecución por retraso, es eficiencia. Dejarlo explícito para evitar lectura negativa.* |
| **8** | **Desglose de la Eficiencia** | • Cloud: -USD 48k (commit de 12 meses negociado)<br>• QA externo: -USD 22k (automatización internalizada)<br>• Consultoría: +USD 11k (soporte integración legacy)<br>• Contingencia sin usar: USD 180k (7.5%)<br>• Reinversión propuesta → Slide 14 | Gráfico de cascada (Waterfall) de variaciones | *Mostrar que la contingencia sigue intacta es un mensaje de control, no de holgura.* |
| **9** | **Mapa de Riesgos (Top 5)** | • 🟠 R-01: Latencia API legacy (prob. Media / impacto Alto)<br>• 🟠 R-02: Disponibilidad equipo Data (prob. Media / impacto Medio)<br>• 🟡 R-03: Cambio regulatorio cookies (prob. Baja / Alto)<br>• 🟢 R-04: Adopción usuarios (mitigado con piloto)<br>• 🟢 R-05: Seguridad (auditado, sin hallazgos) | Matriz de calor (Probabilidad × Impacto) | *Solo profundizar en R-01 y R-02; los demás están monitoreados. No dramatizar.* |
| **10** | **Plan de Mitigación R-01 & R-02** | • R-01: Cache + circuit breaker en mayo (owner: CTO)<br>• R-01: Plan B → desacople temporal vía cola (listo en sandbox)<br>• R-02: Backfill con partner certificado (contrato en legal)<br>• Revisión quincenal en Steering Committee<br>• Trigger de escalamiento al Board: desvío > 10 días | Diagrama de flujo de decisión (Si → Entonces → Escalar) | *El Board valora saber cuándo será llamado. Definir el trigger evita microgestión.* |
| **11** | **Roadmap Q2 (Mayo – Junio)** | • 15 mayo: Kick-off Fase 2 + ingesta Data Lake<br>• 28 mayo: Integración legacy estabilizada<br>• 12 junio: Piloto ampliado a 35% del tráfico<br>• 30 junio: Auditoría de performance & seguridad<br>• Hito de control: Steering 28 junio | Línea de tiempo horizontal con hitos + owner | *Q2 es de consolidación, no de nuevas features. Gestionar expectativas aquí.* |
| **12** | **Roadmap Q3 (Julio – Septiembre)** | • Julio: Motor de recomendaciones (MVP)<br>• Agosto: Rollout 100% + descomisión legacy<br>• 05 sept: Dry-run completo + fallback validado<br>• **12 sept: Go-Live comercial**<br>• 30 sept: Post-implementation review al Board | Roadmap tipo “swimlane” (Tech / Data / Negocio / Change) | *Remarcar que la descomisión del legacy es donde se captura el ahorro estructural de Opex.* |
| **13** | **Impacto Esperado al Cierre (Sept)** | • Opex anualizado: -USD 310k (legacy + licencias)<br>• Conversión estimada: +12% sostenida<br>• Time-to-market nuevas features: ↓ 40%<br>• Base para productos Data-as-a-Service (2025)<br>• ROI proyectado: 2.4x en 18 meses | Gráfico de barras (Antes / Después) + callout ROI | *Conectar el proyecto con el próximo ciclo estratégico, no solo con el cierre técnico.* |
| **14** | **Asks al Board (Decisiones Requeridas)** | • ✅ **Ask 1:** Aprobar reinversión de USD 80k del ahorro en acelerar Motor de Recomendaciones (Julio → Junio)<br>• ✅ **Ask 2:** Ratificar extensión de contingencia hasta Go-Live + 30 días<br>• ℹ️ **Informativo:** Contrato partner backfill (sin impacto presupuestario)<br>• Próximo update: 28 junio (Steering) / 30 sept (Board) | Tabla de decisión (Ask / Impacto / Recomendación / Voto) | *Pedir el voto de forma explícita y separar lo informativo de lo decidible. Ir directo al grano.* |
| **15** | **Cierre & Q&A** | • Recap: En tiempo, bajo presupuesto, con señales tempranas positivas<br>• 2 decisiones hoy → desbloquean Q3 sin fricción<br>• Contacto: CTO / CFO / PMO para follow-up<br>• «Gracias. Abrimos espacio para preguntas.» | Slide minimalista con logo + icono de Q&A | *Cerrar con tono de control, no de triunfalismo. Dejar el último aire para la pregunta del CFO sobre contingencia.* |

---

## 💡 Recomendaciones de diseño para el Board
- **Regla 1-1-1:** 1 idea principal · 1 visual · 1 mensaje accionable por slide.
- **Colores:** Verde / Ámbar / Rojo consistentes en slides 2, 9 y 14 (evita reinterpretaciones).
- **Anexos (fuera del deck principal):** Detalle de SP por squad, contrato cloud, acta de auditoría, matriz RACI.
- **Pre-read:** Enviar slides 2, 7 y 14 con 24h de anticipación para agilizar la votación.

¿Quieres que te prepare también el **speaker notes extendido** para el CFO (slide 7 y 14) o una **versión en PowerPoint/Google Slides con copy listo para pegar**?