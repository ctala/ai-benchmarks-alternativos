# Claude Opus 5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 30.35s | tokens_per_second: 67.5
- input_tokens: 295 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

I'm recalculating the LTV with the correct churn rate—8% monthly gives a 12.5 month average lifetime, not 24 months as the founder assumed. Using gross margin, LTV comes to $306.25, which divided by the $290 CAC yields a ratio of just 1.06—essentially break-even and not viable. Even without applying margin, the ratio only reaches 1.51, which is still weak. The payback period calculation appears to be cut off, but the metrics so far paint a concerning picture. CAC will likely rise with scale due to diminishing returns, potentially hitting $350-400+, which would make the spend clearly unprofitable. The real problem: if he's already profitable on his existing base, adding $10k/mo in ad spend against only $845/mo in incremental gross profit creates a massive cash burn that compounds month-over-month. Even modeling steady state with continuous $10k/mo spend — where he'd eventually have ~431 customers generating $10,560/mo in gross profit — he'd only net $560/mo against the $10k spend, which is essentially break-even at best and negative when accounting for time value and risk.

The math shows he'd need roughly 35 months of continuous burning before hitting monthly break-even, with cumulative losses peaking very high before that point. True: to hit a 3x LTV/CAC ratio, I'd need to either drop CAC to around $102, push LTV to $870 (which requires churn down to 2.8% monthly), or raise prices. Running the sensitivity analysis, dropping churn to 3% gets me to a 2.8 ratio, while 4% churn only hits 2.1. Even pricing up to $60 with current churn only reaches 1.8. The real lever is combining moves—like 4% churn plus $50 pricing gets me to exactly 3.0. The 8% monthly churn I'm working with translates to about 63% annual churn, which is brutal for a $35 product and suggests either a product-market fit issue or a customer segment mismatch.

I should also dig into whether that $290 CAC is blended or…