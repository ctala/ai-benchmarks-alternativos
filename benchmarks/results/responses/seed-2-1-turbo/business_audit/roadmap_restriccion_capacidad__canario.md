# Seed 2.1 Turbo — business_audit/roadmap_restriccion_capacidad

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 7.0 | quality: 8.0
- latency_total: 42.862s | tokens_per_second: 47.8
- input_tokens: 302 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres jefe de producto de una empresa de una sola persona. Priorizas con la capacidad real del equipo, no con la ideal.

**user:**

Soy fundador solo. Tengo 6 horas al día de trabajo enfocado y ya gasto 2 de esas 6 en soporte y operación diaria que no puedo delegar todavía. Me quedan ~4h/día reales para construir. Quedan 8 semanas hasta el cierre del trimestre.

Tengo cuatro iniciativas y quiero saber qué hago:

A) Reescribir la plataforma en otro framework. Impacto estimado: alto (velocidad y todo lo futuro). Esfuerzo: ~3 meses a tiempo completo.
B) Arreglar el flujo de alta, que hoy pierde al 60% de la gente en el paso 2. Impacto: alto. Esfuerzo: ~1 semana.
C) Añadir un panel de métricas para mis clientes. Impacto: medio. Esfuerzo: ~3 semanas. Depende de que A esté terminado.
D) Grabar 10 videos de contenido. Impacto: medio. Esfuerzo: ~2 semanas.

Ordename el trimestre.


## Respuesta completa


El usuario es un fundador solo, who has 4 hours of actual construction work per day and an 8-week quarter with 4 initiatives. He already gets 2 hours of non-delegable support daily, so I’ll prioritize calculating his actual capacity first to ensure realism, and I won’t set 5 working days per week for him to leave room for unexpected support delays.

After accounting for a 20% buffer for unexpected issues, the solo founder’s effective available construction capacity is around 128 hours, equivalent to roughly 6.4 weeks of effective work, not 8 full weeks. I will now evaluate each of the 4 initiatives against this capacity, along with their dependencies, impact, ROI and risks. I’ve clarified that Initiative A’s 3-month full-time effort is defined as 8 hours of daily construction work for a single person, so it would take twice as long for the founder to complete.

I’ve confirmed that Initiative A will take at least 6 months to complete, which is far beyond the 8-week (roughly 2-month) quarter. It will only advance about 25% during the quarter and won’t deliver any value, while also crowding out time for other high-value initiatives. Though Initiative C relies on A’s completion, I still need to verify this dependency.

I’ve confirmed that a full rewrite of the platform is not a viable option right now, as it’s a long-term project that won’t deliver immediate value and would consume the entire quarter without generating revenue or reducing losses. I’m now evaluating Initiative B, and found that effort estimates are usually based on full-time work, so I need to adjust the timeline to fit the founder’s actual 4-hour daily construction work capacity.

I’ve clarified that all effort estimates must be converted to the founder’s actual working time to avoid planning errors. I’ve confirmed Initiative A’s 3-month effort is full-time based, and all other initiatives also use full-time effort as the consistent estimation standard. Assuming all initiatives use full-time effort as the estimation unit, I’ve confirmed the founder’s weekly construction capacity is 20 hours, with a conversion factor of 0.5: each full-time work week takes him 2 weeks of real time.

I’ve added a 25% buffer for unforeseen issues such as extra support demands, bugs and unexpected meetings, bringing the founder’s total planned usable construction capacity for the quarter to 120 hours.

I’ve adjusted the initiative effort calculation logic to first convert full-time hours to the founder’s actual working time before applying the 25% buffer. Initiative A will take 7-8 months to complete with buffer, only advancing 33% in the quarter without delivering tangible value, and cannot be finished, which will block the dependent Initiative C. Initiative B will take 2.5 weeks with buffer, and has a high impact as it can directly recover 60% of lost user enrollment flow.

Fixing the enrollment flow can cut user loss to 20%, doubling registered users with immediate revenue and cost reduction benefits. Initiative D will take 5 weeks with buffer, delivering moderate value via video content, but its impact is less direct than B's.
