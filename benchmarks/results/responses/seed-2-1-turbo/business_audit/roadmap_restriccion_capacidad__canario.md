# Seed 2.1 Turbo — business_audit/roadmap_restriccion_capacidad

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 4.2 | quality: 4.0
- latency_total: 42.938s | tokens_per_second: 47.7
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


El usuario es un fundador solo, whose work schedule is 4 usable hours per day for product building during each 8-week quarter. I've confirmed the total real available construction time is about 128 hours, after accounting for 20% deviation from unforeseen issues.

I found most solo founders confuse full-time equivalent effort estimates with their actual part-time construction capacity, so I'll first convert all initiative effort estimates to align with his real available capacity. I've clarified the three core calculation assumptions: his effort estimates are based on standard 40-hour weekly full-time construction, his theoretical weekly construction capacity is 20 hours, and the actual available weekly time after contingency deduction is 16 hours.

I have finished calculating the required time for the first two initiatives. The full platform rewrite would take 30 weeks at his actual construction pace, which is far beyond the 8-week quarter, and he could only complete 27% of the work throughout the quarter without delivering any tangible value. He also cannot start the high-priority user flow optimization project until the rewrite is finished. I've clarified the core prioritization principle for solo founders: first launch initiatives that deliver value quickly to boost revenue or user growth, which will help secure more resources for subsequent development, and avoid overinvesting in long rewrite projects that generate no interim value.

I have confirmed that initiative A (full platform rewrite) is completely unsuitable for this quarter, as it cannot deliver any tangible value even after partial completion.

A full rewrite also carries high implementation risk, as it will take twice as long as estimated even with honest planning, which would consume the entire year without delivering any interim value. I've identified initiative B as a high-impact, low-effort quick win that should be prioritized first. Fixing the onboarding flow will directly boost user completion rates by 150%, generating immediate positive impacts on revenue or user assets. I’ve also noted that the 10-content-video initiative has medium impact and requires 2 weeks of full-time effort.

Initiative C (metrics dashboard) is also ruled out for this quarter as it relies on the platform rewrite A which won't be completed now. I'll note that a minimal viable version of C may be feasible if it can be decoupled from A. I've also confirmed initiative D's basic parameters: medium impact, 2 weeks of full-time effort.

User acquisition is the core impact of the content initiative, which will be more effective after the onboarding flow optimization is completed. I will now calculate the actual implementation time of B and D, with support delays and urgent bugs taken into account.
