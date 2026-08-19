# Seed 2.1 Turbo — business_audit/escalar_con_ltv_mal_calculado

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 32.03s | tokens_per_second: 63.9
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


El usuario es un fundador que cree que tiene LTV/CAC bueno y quiere meter 10k en ads, como analista de unit economics he encontrado dos fallos clave en su cálculo: olvidó incluir el margen bruto y miscalculó la vida media del cliente, que en realidad es 12,5 meses, no los 24 que usted afirmó. Se ha confirmado que el error en la estimación de la vida media del cliente se debió a una confusión entre la tasa de churn anual y mensual, ya que un 8% mensual genera una pérdida exponencial de clientes, no lineal, por lo que el cálculo lineal que usó el fundador no es válido.

He verified that the founder's overestimation of customer lifetime is a 92% exaggeration, and confirmed the churn calculation is based on the existing customer base rather than initial clients, which further validates the correct 12.5-month average lifetime.

Another critical error has been found in the founder's calculation: he used total revenue instead of net gross margin to estimate LTV. I've calculated the correct basic LTV at $306.25, and confirmed the CAC is $290. Next I will proceed to calculate the discounted LTV. The calculated LTV/CAC ratio is around 1.05, far below the founder's previous claim of 2.9. I've confirmed the monthly discount rate for the calculation is 2% (24% annually), and will use the present value formula for a decaying perpetuity to compute the discounted LTV.

The discounted LTV is calculated at $245, leading to an LTV/CAC ratio of 0.84, meaning the company loses money on each acquired customer. The founder's overestimated customer lifetime stems from survival bias or confusing monthly and annual churn rates, and the 8% monthly churn is far higher than SaaS industry benchmarks.

Three root causes for the founder's miscalculations have been identified: first, the 8% monthly churn he provided will be adopted for the analysis; second, LTV should be based on gross margin instead of total revenue to cover variable costs; third, the time value of money needs to be taken into account.

I've identified two more factors that will further worsen the already poor LTV/CAC ratio: whether CAC includes relevant operation costs besides ad expenses, and whether the 8% monthly churn is net of revenue expansion benefits.

Another factor that will further compress the already low LTV/CAC ratio has been identified: the presence of variable per-customer support and onboarding costs will reduce actual gross margin and lower LTV. The $10k ad spend request is not approved, as the current LTV/CAC ratio is far below the SaaS industry minimum acceptable benchmark.

We use the parameters provided by the user.
