# Qwen 3.8 27B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.35 | quality: 10.0
- latency_total: 48.31s | tokens_per_second: 42.4
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

We need answer in Spanish. User asks: unit economics, scaling with paid ads. Need recalc numbers. Need be careful. Let's analyze.

Given:
Price $35/month. Churn monthly 8%. Gross margin 70% after infra and payments. CAC $290.
Founder says: customer stays about 2 years, LTV = 35*24 = $840. CAC 290 -> LTV/CAC = 2.9, above 3 more or less. Wants to spend $10k in ads this month.

We need likely say no? Need recalc. LTV should be gross profit per customer over lifetime, not revenue. Lifetime = 1/churn = 1/0.08 = 12.5 months, not 24 months. If 8% monthly churn, average lifetime 12.5 months. Gross margin 70%, so monthly gross profit = 35*0.70 = $24.50. LTV (gross profit) = 24.50 * 12.5 = $306.25. If discounting? Could use no discount. Then LTV/CAC = 306.25/290 = 1.06. Not 2.9. If using revenue LTV = 35*12.5=437.5, but CAC vs revenue meaningless. If they assume 2 years, that implies monthly churn ~4.2% (1/24). But actual 8%. So plan likely fails: paying $290 to acquire a customer who returns only ~$306 gross profit over lifetime, barely positive, and payback period? CAC payback in gross profit months = 290/24.5 = 11.84 months, almost entire lifetime. With $10k ads, if CAC constant, new customers = 10,000/290 = 34.48. Additional gross profit over lifetime = 34.48*306.25 = $10,560, net profit from cohort ~$560 before working capital, ad platform inefficiencies, creative fatigue, etc. Cash flow: if spend $10k month 1, gross profit from those customers accrues $24.5 per customer/month, starting maybe month 1/2. Need fund churn and payback ~12 months. With $10k, monthly gross profit from new cohort ~$845 (34.5*24.5) if all active, declining with churn. It may take many months to recover $10k. Also if CAC is $290 and price $35, need 8.28 months of revenue to recover CAC, but gross margin makes 11.8 months. With 8% monthly churn, expected survivors after 12 months? (0.92)^12=0.367? Wait average lifetime 12.5, but survivorship at 12 months 36.7%. Payback by month 12? cumulative gross profit = 24.5 * sum_{t=1}^{12} 0.92^{t-1} maybe if start at month 0? sum = (1-0.92^12)/(0.08)= (1-0.3677)/0.08=7.904 months. *24.5=193.6. So after 12 months only $194 gross profit per customer, far below CAC. Expected total 306. Need maybe 18-20 months? Let's calculate cumulative until >290. Need sum survival. Sum infinite =12.5. To reach 290/24.5=11.836 months equivalent. Solve (1-0.92^n)/0.08 =11.836 => 1-0.92^n=0.9469 => 0.92^n=0.0531 => n=ln(0.0531)/ln(0.92)= -2.936/-0.08338=35.2 months. Wait that's if no discount and gross profit each month from survivors. But average lifetime 12.5, cumulative gross profit over infinite =306. Payback 35 months? That seems because monthly gross profit declines; to recover 290 of 306 total, need almost entire lifetime. Yes. So payback period ~35 months. That is terrible. If discounting, worse. If CAC includes only ad spend? Maybe other costs? But margin given.

Need answer: No, not with current numbers. Explain founder error: lifetime not 2 years at 8% churn; LTV must use gross profit not revenue; LTV/CAC ~1.1, not 2.9. $10k will likely destroy value unless CAC drops, churn drops, price/margin increases, or you have strategic reasons. Need maybe calculate break-even CAC: if LTV gross profit 306, max CAC for 3x is $102; for 2x $153; for 1.5x $204. Current CAC 290 only ~1.05x. To justify $10k, need LTV/CAC >= maybe 3? Need reduce CAC to ~$102 or increase LTV to $870 (if CAC 290 for 3x). How? Increase margin, price, reduce churn. For 3x with CAC 290: LTV gross profit >=870. At 70% margin and 8% churn, need monthly gross profit 870/12.5=69.6 => price 99.4. Or if price 35, margin 70, need lifetime 870/(24.5)=35.5 months => churn 1/35.5=2.82% monthly. Or combination.

Need consider if customer "se queda unos 2 años" maybe empirical average? But given churn 8% monthly, contradiction. If actual average lifetime 24 months, monthly churn should be ~4.2%, not 8%. If 8% is cohort churn? We should ask to verify. But as analyst, use provided churn. Could say if 8% is not monthly churn but something else, recalc. But based on numbers, no.

Need maybe mention payback period and cash. $10,000 ad spend: at CAC 290 -> 34 new customers. Monthly gross profit from them at start ~$845. But because churn, after 6 months maybe active ~? 34.5*(0.92^6)=34.5*0.606=20.9, gross profit $512. After 12 months ~12.7, gross profit $311. Cumulative gross profit after 12 months ~$6,670? Let's calculate: 34.48*193.6 = $6,674. So after one year, still ~$3,326 cash short from ad spend, and cohort will produce total $10,560 eventually, net $560. But with discount rate, net negative. Also if ad spend is monthly and you continue scaling, cash flow may be okay if existing base? But they say rentable and scale strong. Need evaluate incremental. If they already have customers, $10k new ads adds 34 customers, but cash outflow now, inflow over 3+ years. If no discount, NPV maybe small positive; with 10% monthly discount? Let's compute NPV: monthly gross profit 24.5, survival 0.92^{t-1}, discount r maybe 10% monthly? NPV = 24.5 * sum_{t=1}∞ (0.92/1.10)^t? Actually if cash at end month t, survival probability? Expected gross profit = 24.5*(0.92)^{t-1}. Discount factor (1+r)^-t. Sum = 24.5 * (0.92/1.10) / (1 - 0.92/1.10) =24.5*0.83636/(0.16364)=125.5. CAC 290 => NPV negative. Even at 5% monthly: factor 0.92/1.05=0.87619, sum=0.87619/0.12381=7.076, *24.5=173.4. Negative. At 2% monthly: 0.92/1.02=0.90196, sum=9.07, *24.5=222. Negative. At 0% positive 306. So with any meaningful discount