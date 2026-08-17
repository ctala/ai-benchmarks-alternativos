# Qwen 3.8 27B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 104.418s | tokens_per_second: 19.6
- input_tokens: 255 | output_tokens: 2048

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

We need answer in Spanish. User asks: "Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:
- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?"

We need act as unit economics analyst, recalc founder numbers, many plans die in arithmetic. Need likely say no, not yet. Need compute LTV correctly: monthly gross profit = 35*0.7 = $24.5. Average lifetime = 1/churn = 12.5 months if constant monthly churn, not 24. LTV gross profit = 24.5*12.5 = $306.25. LTV/CAC = 306.25/290 = 1.06. Even if using 24 months: 24.5*24 = 588, /290=2.03 not 2.9 because ignored margin. If use revenue LTV 840/290=2.9 but that's not profit. Payback period? CAC / monthly gross profit = 290/24.5 = 11.84 months. With 8% churn, by time payback many customers churn? Need maybe compute probability survive to month 12: (1-0.08)^11? If payback at 11.8 months, survival to 12 ~0.389? Actually (0.92)^11=0.399? Let's compute. 0.92^10=0.434, *0.92=0.399. So only 40% still alive at payback, but expected cash flows account for churn. Need maybe calculate net present value? If no discount, LTV 306, CAC 290, margin 16.25 per customer, 5.6% return on CAC. If discount, negative likely. Also if 10k ad spend: new customers = 10000/290 = 34.48 ~34 customers. Monthly gross profit from new cohort month 1: 34.48*24.5 = $844.8. But churn 8% means next month fewer. Need cash flow: initial ad spend -10000. Month 1 gross profit from new customers? If customers acquired at start, they pay? SaaS monthly. If CAC paid upfront and first month revenue? Usually CAC includes spend to acquire, maybe first month revenue after. Need model. At 8% churn, expected active customers after t months = N*(1-0.08)^t maybe if churn after month. Gross profit per active customer 24.5. Cumulative gross profit over lifetime = N*306.25. For 34.48, total gross profit = 10562.5, net over lifetime = 562.5 (5.6%). But timing: payback cohort? cumulative gross profit after m months = N*24.5*sum_{t=0}^{m-1}0.92^t (if first month full). Need solve for 10000: 34.48*24.5*sum = 844.8*sum. Need sum=11.84. Sum geometric = (1-0.92^m)/0.08. Solve (1-0.92^m)/0.08=11.84 => 1-0.92^m=0.9472 => 0.92^m=0.0528 => m=ln(0.0528)/ln(0.92)=(-2.941)/(-0.08338)=35.3 months. So cohort payback ~35 months, not 12. That's because expected cash flows decline due churn. Wait LTV/CAC 1.056, positive but payback long. If discount at even 5% monthly? NPV likely negative. Let's compute maybe. Discount rate? Could mention if discount 5% monthly, LTV = 24.5 * sum_{t=0}∞ (0.92/1.05)^t = 24.5 / (1 - 0.87619) = 24.5 / 0.12381 = 197.9, below CAC. At 3% monthly: factor 0.92/1.03=0.8932, LTV=24.5/(0.1068)=229.4. At 1% monthly: 0.9109, LTV=24.5/(0.0891)=275. So need very low discount to be positive. But maybe not necessary.

Need address "LTV/CAC = 2,9, que está por encima de 3 más o menos" Actually 2.9 is below 3, not above. But more importantly using revenue not gross profit and wrong lifetime. Need be direct: No, no le doy. Or "no, no con esos números". Need recalc.

Let's structure:
- Start: No. Ese plan se muere en la aritmética.
- Error 1: LTV no es ingresos, es margen bruto.
- Error 2: lifetime no es 24 meses con churn 8%; expected lifetime = 1/0.08 = 12.5 months. (If "se queda unos 2 años" inconsistent with 8% monthly; 8% monthly means median? Let's compute median? If exponential monthly, probability survive 24 = 0.92^24 = 0.134, so only 13% alive at 24; median ~ ln(0.5)/ln(0.92)=8.32 months. So "2 years" is not average. Could mention: 8% churn => average 12.5 months; 24 months is not average, it's a tail. If actual average is 24, churn should be ~4.2% monthly. Need maybe: if you truly have 24-month average lifetime, monthly churn ~1/24 = 4.17%, not 8%. But with 8%, average 12.5.
- Correct LTV (undiscounted) = 35*0.70*(1/0.08)=35*0.7*12.5=$306.25.
- LTV/CAC = 306.25/290 = 1.06. Not 2.9. Even if you use 24 months and margin: 35*0.7*24=588; /290=2.03. Still not 3 and not enough to justify aggressive scaling if payback long.
- If you use revenue LTV 840/290=2.9, that's revenue multiple, not profit. You need gross profit to cover CAC.
- Payback: CAC / monthly gross profit = 290/24.5=11.8 months if customer never churns. With 8% churn, expected cohort payback ~35 months (or you can say more than 2 years). Let's verify: If first month gross profit N*24.5. Need 10k spend. New customers = 34.48. Month 1 gross profit = 844.8. Because churn, cumulative to recover 10k ~35 months. At month 35, expected active = 34.48*0.92^35. 0.92^35 = exp(35*-0.08338)=exp(-2.918)=0.054. Active ~1.86, gross profit ~45.6/month. So long tail.
- NPV: with any reasonable discount, likely negative. Example 5% monthly discount: LTV ~198 < CAC; NPV per customer negative ~ -92. If 10k, expected loss ~ -3.2k? Let's compute NPV per customer at 5%: 197.86 - 290 = -92.14; *34.48 = -3177. At 3%: 229