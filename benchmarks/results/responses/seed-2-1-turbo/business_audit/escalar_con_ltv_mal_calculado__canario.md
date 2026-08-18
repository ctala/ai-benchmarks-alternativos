# Seed 2.1 Turbo — business_audit/escalar_con_ltv_mal_calculado

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 38.829s | tokens_per_second: 52.7
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


El usuario es un fundador que cree que tiene LTV/CAC casi 3 y quiere meter 10k en ads, I'm the unit economics specialist reviewing the account, and I've found two critical flaws in his LTV calculation: he used gross revenue instead of gross margin, and overestimated the customer lifespan from 12.5 months to 2 years. I will explain every error clearly, then present the real LTV, LTV/CAC ratio, investment decision and outcome of spending the 10k ad budget step by step. I've clarified the correct customer lifespan calculation logic and confirmed that LTV should be calculated based on gross margin instead of gross revenue, with the basic SaaS LTV formula also finalized.

The actual LTV is calculated at $306.25, making the real LTV/CAC ratio 1.05, which is nearly 1:1. This ratio can't even cover all operational expenses, so the business loses money per acquired customer.

I will further clarify the difference between gross margin LTV and net LTV to highlight the critical error in his revenue-based LTV calculation, and explain the customer lifespan logic to help him understand why the average lifespan is 12.5 months instead of 2 years.

Spending the $10k ad budget will acquire roughly 34 customers, generating $10,412.5 in total gross margin over their average 12.5-month lifespan. After covering operational costs, the actual profit will be even lower.

The $412 gross margin surplus fails to cover fixed operational costs and personal salary, making the ad investment unprofitable. I also confirmed the actual CAC is higher if the $290 figure only covers ad platform costs, further worsening losses. Given the available data, the $10k ad investment should be rejected.

I will also provide actionable optimization paths for him to scale the business. First, I need to verify the churn rate assumption: if the 8% churn is annual instead of the stated monthly, the LTV/CAC ratio will jump to 12.7, making ad investment highly profitable. If the 8% is indeed monthly churn, the feasible optimization directions include lowering churn to 4% (still cannot reach the 3.0 healthy threshold), raising gross margin (the current 70% is already high with limited room for increase), increasing product price (the adjusted LTV/CAC ratio is only 1.5), cutting CAC to $100 (the ratio will reach 3.06 to hit the standard threshold), and launching upsell/cross-sell to boost customer lifetime value.

I will first explain why a 3.0 LTV/CAC ratio is the industry standard: it means $3 of gross margin is generated per $1 of customer acquisition cost, leaving net profit after covering operational expenses. I will also analyze the customer acquisition payback period next.
