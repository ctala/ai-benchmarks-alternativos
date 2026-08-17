# Seed 2.1 Turbo — business_audit/escalar_con_ltv_mal_calculado

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.4 | quality: 10.0
- latency_total: 45.639s | tokens_per_second: 44.9
- input_tokens: 249 | output_tokens: 2048

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


El usuario es un fundador que cree que su LTV/CAC es ~ 2.9, nearly 3, and plans to invest 10k in advertising. As the unit economics analyst checking the arithmetic, I've found his 2-year LTV assumption is inconsistent with the 8% monthly churn rate, and will clarify this issue first.

I've identified a second error in his LTV calculation: he used total revenue instead of gross margin. I've confirmed that with 8% monthly churn, the average customer lifetime is 12.5 months, not 24 months as he claimed.

It has been clarified that the constant churn assumption applied in the calculation also needs to be verified. After adjusting for the 70% gross margin, the correct LTV is $306.25, which is very close to the $290 CAC.

The actual LTV/CAC ratio is only 1.05, far below the founder's estimate of 2.9. I also found two more issues: the CAC calculation didn't include additional acquisition costs, and constant churn assumption doesn't hold as churn is usually higher in the initial onboarding stage, further worsening the unit economics.

I've confirmed that the time value of money should be considered when calculating LTV. For startups, a reasonable monthly discount rate is 2%, and I've clarified the correct formulas for discounted LTV under two different payment scenarios.

At a 2% monthly discount rate, the discounted LTV is $245, lower than the $290 CAC, meaning we lose money per customer. I also found that unincluded support and onboarding costs will further reduce the actual gross margin.

I've noted the founder claims his business is profitable, but we need to clarify whether this refers to unit-level or company-level profitability. I also found he incorrectly calculated his 2-year customer lifetime, likely due to confusing monthly and annual churn rates.

I've confirmed the correct annual churn rate is roughly 63% when the monthly churn is 8%, meaning only 37% of customers remain after a full year and just 13% after two years, so a 2-year average customer lifetime is completely inconsistent with the given churn data. I've also noted that even with his incorrect calculation, his LTV/CAC ratio never actually reaches 3, and the real ratio is only 1.05, turning negative when the time value of money is factored in. I'm now structuring my response, with the core conclusion being he should not invest the planned $10k in advertising due to critical calculation errors and unconsidered factors further worsening unit economics, and I've sorted out the explanation for the first error related to customer lifetime calculation.
