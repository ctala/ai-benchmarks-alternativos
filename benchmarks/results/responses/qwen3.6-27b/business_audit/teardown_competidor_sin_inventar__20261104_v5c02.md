# Qwen 3.6 27B base (OpenRouter FP8) — business_audit/teardown_competidor_sin_inventar

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 2.9 | quality: 2.0
- latency_total: 61.114s | tokens_per_second: 56.1
- input_tokens: 193 | output_tokens: 3430

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista competitivo. Distingues SIEMPRE entre lo que sabes y lo que estás infiriendo, y marcas tu nivel de certeza.

**user:**

Hazme un teardown de un competidor. Esto es TODO lo que pude ver desde fuera (su página pública):

- Comunidad de pago sobre automatización, en una plataforma tipo membresía.
- Muestra '2.400 miembros' en la portada.
- Precio visible: $39/mes. No se ve si hay plan anual ni descuentos.
- Publican 3 posts por semana en el feed público.
- El fundador tiene 60.000 seguidores en una red social.
- Tienen 12 cursos listados, no se ve cuántos están terminados.

Quiero saber cuánto factura, qué tan sano es el negocio y cómo les compito.


## Respuesta completa

Como analista competitivo, estructuro este teardown separando estrictamente **lo que se confirma con tus datos** de **lo que se infiere**, marcando el nivel de certeza en cada punto. Donde falta información, lo indico explícitamente.

---
### 🔍 1. Datos confirmados (Hechos públicos)
- Modelo: Comunidad de pago sobre automatización, alojada en plataforma de membresía.
- Métrica visible: 2.400 miembros en portada.
- Precio: $39/mes. No se observa plan anual ni descuentos.
- Cadencia de contenido: 3 posts/semana en feed público.
- Audiencia del fundador: 60.000 seguidores en una red social.
- Catálogo: 12 cursos listados (estado de finalización no visible).

---
### 💰 2. Estimación de facturación
| Concepto | Valor | Certeza | Justificación |
|----------|-------|---------|---------------|
| Ingresos brutos mensuales (GMV) | ~$93.600/mes ($1.12M/año) | **Alta** (cálculo matemático) | 2.400 × $39. No refleja realidad operativa. |
| Ingresos netos estimados | ~$79.600 – $84.300/mes | **Media** | Resta comisión típica de plataforma (10-15%). No incluye impuestos, reembolsos o pagos fallidos. |
| Ingresos reales ajustados | **$50.000 – $80.000/mes** (rango probable) | **Baja-Media** | El contador "2.400" suele incluir: miembros inactivos, trials, cuentas gratuitas, o históricos sin baja automática. En comunidades típicas, el % de activos pagantes ronda 50-75%. |

📌 **Nota crítica:** Sin acceso a métricas de churn, tasa de conversión o porcentaje de activos, cualquier cifra por debajo de ~$65k/mes es especulativa.

---
### 📊 3. Salud del negocio (Diagnóstico inferido)
| Dimensión | Inferencia | Certeza | Señales públicas que la respaldan |
|-----------|------------|---------|----------------------------------|
| **Adquisición** | CAC probablemente bajo | **Media** | El fundador tiene 60k seguidores, lo que sugiere funnel orgánico propio. Sin embargo, no se sabe si convierte bien o depende de tráfico pagado. |
| **Retención/Churn** | Riesgo moderado-alto | **Baja** | No se ve plan anual ni programa de fidelización. A $39/mes, el churn típico del sector es 5-10% mensual. Sin datos de cohortes, es imposible validar. |
| **Engagement real** | Probablemente superior al feed público | **Baja** | 3 posts/semana en público es cadencia estándar. Las comunidades suelen generar valor en canales privados (DMs, grupos, lives), que no son visibles. |
| **Activos/Contenido** | Posible "content graveyard" o estructura sólida | **Baja** | 12 cursos listados sin estado de finalización. Si están incompletos, el valor percibido baja. Si están actualizados, es un moat defensivo. |
| **Rentabilidad** | Margen operativo probablemente 60-80% | **Media** | Modelos de membresía con plataforma SaaS tienen costos variables bajos. Si el CAC es orgánico y no hay equipo grande, la rentabilidad neta suele ser alta. |
| **Dependencia de clave** | Riesgo centralizado en el fundador | **Media** | 60k seguidores + voz única sugieren marca personal. Si el fundador se quema o reduce publicación, la comunidad puede decaer rápidamente. |

📌 **Veredicto de salud:** Modelo financieramente viable si la retención supera el 85% mensual y el contenido está actualizado. Vulnerable a churn silencioso, dependencia del fundador y falta de escalabilidad en LTV (sin plan anual/tiering).

---
### ⚔️ 4. Cómo competir (Estrategias accionables)
| Eje | Acción | Certeza de impacto | Por qué funciona frente a sus debilidades visibles |
|-----|--------|-------------------|--------------------------------------------------|
| **Precios y LTV** | Lanzar plan anual (-20%) + tier básico ($19) y premium ($79 con mentoring/grupos) | **Alta** | Captura segmentos que $39/mes no cubre. Aumenta LTV y reduce churn por precio. |
| **Onboarding y activación** | Sistema de "primer win en 7 días" + checklist de automatización aplicada | **Media-Alta** | Las comunidades mueren por falta de activación temprana. Si ellos no muestran onboarding, es tu ventaja. |
| **Contenido vs. Implementación** | Enfocarte en "workflows listos para copiar" + sesiones mensuales de auditoría | **Media** | 12 cursos sin estado sugieren posible saturación teórica. La automatización se compra por resultados, no por horas de video. |
| **Adquisición descentralizada** | Partnerships con herramientas (Make, n8n, Zapier) + contenido SEO técnico | **Media** | Reduce dependencia de un solo creador. Construye autoridad de marca, no de persona. |
| **Plataforma y experiencia** | Migrar a solución con menor comisión o self-hosted + integraciones nativas (Slack, Notion, CRM) | **Media-Baja** | Si usan plataforma genérica, puedes diferenciar con UX, gamificación o automatización interna del onboarding. |

📌 **Recomendación táctica inmediata:** No compitas por "más cursos". Compite por **tasa de implementación** y **visibilidad de resultados**. Publica casos de uso con métricas reales (horas ahorradas, errores reducidos, ROI). Eso desdibuja la ventaja de "2.400 miembros" si son inactivos.

---
### 🧩 5. Lo que falta para validar (Data gaps críticos)
1. % de miembros activos vs. totales (acceso a plataforma o scraping de actividad).
2. Tasa de churn mensual y LTV real (encuestas a ex-miembros o análisis de cohortes públicas si existen).
3. Estado de los 12 cursos (completados, en progreso, abandonados).
4. Canales de adquisición real (orgánico vs. paid, fuentes de tráfico).
5. Estructura de costos (equipo, herramientas, comisión exacta de plataforma).

---
**Resumen ejecutivo:**  
Facturan probablemente entre **$50k y $80k/mes netos**, con un modelo rentable pero expuesto a churn y dependencia del fundador. Tu ventaja competitiva no está en igualar su tamaño, sino en **activar更快, retener mejor y demostrar implementación real**. Si necesitas, puedo ayudarte a diseñar un experimento de validación (landing + funnel + métricas de activación) para testear tu propuesta frente a este competidor en 14 días.