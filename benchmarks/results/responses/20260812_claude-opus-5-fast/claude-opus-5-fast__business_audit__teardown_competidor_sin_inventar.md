# Claude Opus 5 Fast — business_audit/teardown_competidor_sin_inventar

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 2.51 | quality: 2.0
- latency_total: 11.769s | tokens_per_second: 174.0
- input_tokens: 286 | output_tokens: 2048

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

I need to be careful about what I actually know versus what I'm inferring here. The member count of 2,400 is almost certainly misleading—on platforms like Skool or Circle, that's the total cumulative joins including free members and churned accounts, not active paying subscribers. So I should structure this by separating observable facts from unknowns, and flag where I'm making assumptions about revenue or actual engagement.

The naive calculation of 2,400 × $39 = $1.12M ARR is almost certainly an overestimate. I need to model different scenarios with realistic churn and free-tier assumptions, and identify which variables would move the needle most if I could verify them cheaply.

The key adjustments are that membership counts often include free members and churned users, effective ARPU drops significantly when accounting for annual discounts (15-20% off), founding member pricing, and platform fees (Skool takes $99/mo flat, Patreon 8-12%, plus payment processing at 2.9%+). I should also factor in involuntary churn from failed payments, typically 5-10% of MRR attempts.

I'm building out scenario ranges: a low case with 25% of members paying at $32 effective ARPU nets around $230k/yr gross, and I need to model mid and high cases to bracket the likely range.

Now I'm working through the churn dynamics — this is actually the constraint that matters most. Creator communities at this price point typically see 8-15% monthly churn, which means at 10% churn the average member lifetime is only 10 months and LTV sits around $340-390. That forces a steady-state requirement: to maintain 1,300 paying members at 10% monthly churn, they'd need 130 new paid signups every month just to stay flat. That's a real acquisition machine, and I'm inverting the math to sanity-check whether a 60k-follower account posting 3x/week can realistically hit that conversion rate.

The funnel math is tight — typical social-to-paid conversion runs 2-5%, so 130 paid signups would need 2,600-6,500 monthly leads. With 60k followers and 3 posts weekly, they're probably reaching 10-25% of their audience per post depending on platform dynamics. That's borderline and leans toward the mid-to-low revenue scenario rather than the high one.

The 12-course library is a content-heavy positioning that signals depth but carries real risks — completion rates are unknown, and the library model tends to have worse retention than cohort-based or outcome-driven approaches. Plus there…