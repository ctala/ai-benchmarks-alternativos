# Claude Sonnet 5 — strategy/pricing_strategy

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 4.58 | quality: 5.0
- latency_total: 66.803s | tokens_per_second: 88.4
- input_tokens: 288 | output_tokens: 5904

## Entrada exacta (lo que recibió el modelo)

**user:**

Mi SaaS de gestion de inventario tiene estos datos:
- CAC actual: $120
- LTV promedio: $840 (14 meses * $60/mes)
- Churn mensual: 7%
- 200 clientes actuales
- Competidores cobran entre $29 y $149/mes
- Mi costo por usuario es ~$8/mes

Estoy considerando subir el precio de $60 a $89/mes.
Analiza:
1. Calcula el LTV/CAC ratio actual y como cambiaria
2. Estima el impacto en churn (usa benchmarks de la industria SaaS)
3. Modela 3 escenarios: optimista, realista, pesimista
4. Dame tu recomendacion con numeros concretos
5. Sugiere una estrategia de implementacion (grandfather, gradual, etc)


## Respuesta completa

# Análisis de Pricing: $60 → $89/mes

## 1. LTV/CAC actual y proyectado

**Ojo con el LTV que me diste**: $840 es LTV *bruto* (revenue), no contempla tu costo de $8/user/mes. Para decisiones de pricing conviene usar margen de contribución.

| Métrica | Actual ($60) | Nuevo ($89, sin cambio en churn) |
|---|---|---|
| Margen/cliente/mes | $52 | $81 |
| Lifetime (1/churn) | 14.3 meses | 14.3 meses (supuesto irreal) |
| LTV (margen) | $743 | $1,158 |
| LTV/CAC | **6.2x** | **9.65x** (techo teórico) |

Tu ratio actual de 6.2x ya está por encima del benchmark saludable (3x). Esto es una señal clara de que **estás dejando dinero en la mesa** — pero el techo de 9.65x asume churn constante, que es poco realista con un salto de precio del 48%.

## 2. Impacto esperado en churn

Un aumento de +48% es agresivo (no es el típico ajuste anual de 5-10%). Benchmarks de SaaS (ProfitWell, Price Intelligently) sugieren:

- **Churn shock** (cancelaciones adicionales en el mes de transición, una sola vez): correlacionado con % de aumento y calidad de comunicación/grandfathering.
- **Churn estable nuevo**: elasticidad típica de 0.3x-0.6x el % de aumento de precio se traduce en incremento de churn mensual.

Con $89 dentro del rango competitivo ($29-$149), no estás fuera de mercado — esto **limita** el downside, pero no lo elimina.

## 3. Tres escenarios (base: 200 clientes actuales, sin considerar nuevos clientes, para isolar el efecto puro)

| | Optimista | Realista | Pesimista |
|---|---|---|---|
| Churn shock (mes 1) | 5% | 12% | 25% |
| Clientes tras shock | 190 | 176 | 150 |
| Churn mensual nuevo | 6.5% | 8.5% | 11% |
| LTV (margen) | $1,247 | $956 | $737 |
| LTV/CAC | 10.4x | 8.0x | 6.1x |
| MRR mes 1 | $16,910 (+41%) | $15,664 (+31%) | $13,350 (+11%) |
| **Clientes a 12 meses** | 86 | 60 | 36 |
| **MRR a 12 meses** | $7,645 | $5,315 | $3,222 |
| MRR sin cambio (baseline $60) | $5,000 | $5,000 | $5,000 |
| vs. baseline a 12m | **+53%** | **+6%** | **-36%** |

**Lectura clave**: incluso en el escenario realista, terminas mejor que si no tocas el precio — pero el pesimista destruye valor significativo. El diferenciador entre realista y pesimista es casi enteramente **ejecución** (comunicación, grandfathering, valor percibido), no el precio en sí.

## 4. Recomendación concreta

**No hagas el salto de $60 a $89 de golpe a toda tu base de 200 clientes.** El riesgo de caer en escenario pesimista es real si no gestionas la transición.

Mi recomendación:

1. **Nuevos clientes → $89 inmediato** (o incluso probar $79 vs $89 con A/B test si tu volumen de leads lo permite). Cero riesgo de churn aquí, es pricing forward.
2. **Clientes existentes → grandfathering parcial**, no aumento abrupto. Esto te acerca al escenario optimista/realista.
3. Objetivo numérico: apuntar a un churn shock **≤12%** y churn estable **≤8.5%** (escenario realista o mejor). Si tu monitoreo muestra shock >20% en las primeras 4-6 semanas, tienes una señal de alerta temprana para ajustar.

## 5. Estrategia de implementación

**Grandfathering escalonado (recomendado):**
- Clientes actuales mantienen $60 por 90 días desde el anuncio (aviso anticipado, no sorpresa).
- Luego migración gradual: $60 → $69 (mes 4-6) → $79 (mes 7-9) → $89 (mes 10-12).
- Alternativa más simple: ofrecer **lock-in de precio actual de por vida si pasan a plan anual pagado por adelantado** (mejora cash flow y retención simultáneamente, y filtra a los clientes más comprometidos).

**Táctico adicional:**
- **Comunicación proactiva 60 días antes**, con narrativa de valor (roadmap de features, no solo "subimos precio").
- **Crear un tier intermedio** (ej. $69, features limitadas) para no perder al segmento más sensible al precio — evita churn binario "me quedo al precio nuevo o me voy".
- **Test A/B con 15-20% de la base** antes del rollout completo, para calibrar el churn shock real con tus datos, no solo benchmarks.
- **Monitoreo semanal de churn** las primeras 8 semanas post-anuncio, con plan de contingencia (pausar aumento, ofrecer descuento temporal) si el shock supera el 20%.

---

**Nota de honestidad**: estos porcentajes de churn shock/estable son estimaciones basadas en benchmarks generales de SaaS, no en datos específicos de tu vertical (inventario B2B suele ser bastante "sticky" por switching costs operativos, lo cual juega a tu favor). Te recomiendo validar con el A/B test antes de comprometer toda la base.