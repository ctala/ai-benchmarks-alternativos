# Qwen 3.8 Max — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 8.23 | quality: 10.0
- latency_total: 59.56s | tokens_per_second: 34.4
- input_tokens: 255 | output_tokens: 2050

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

We need answer in Spanish. User asks about unit economics. Need recalc. Need analyze thoroughly.

Given: price $35/mo, churn monthly 8%, gross margin 70%, CAC $290. Founder says stays ~2 years, LTV=35*24=840, LTV/CAC=2.9, above 3? Actually 840/290=2.896. But mistakes: churn 8% monthly implies average lifetime if constant churn = 1/churn = 12.5 months, not 24. Also LTV should be gross margin revenue, not revenue, or at least contribution margin. Lifetime = 12.5 months. Expected revenue = 35 * 12.5 = 437.5. Gross profit LTV = 437.5*0.70 = 306.25. LTV/CAC = 306.25/290 = 1.06. Not healthy. If using revenue LTV/CAC = 437.5/290=1.51. If include discount? Need maybe net present value with discount rate. Also payback: CAC / (monthly gross profit per customer) = 290/(35*0.7)=290/24.5=11.84 months. Average lifetime 12.5 months, payback almost entire life, too risky. With $10k spend, at CAC 290 acquire ~34.48 customers. Cohort expected gross profit: 34.5*306=10552? Wait $10,000 / 290 = 34.48 customers. Gross profit LTV total = 34.48*306.25 = 10557. That seems just returns $557 over lifetime ignoring time, ops, fixed costs, discount, CAC paid upfront. But if CAC $290 and gross profit per month $24.5, cumulative gross profit after 12 months =? Need survival curve. With monthly churn 8%, expected months per customer = sum_{t=1}^{∞} S_t? Need define. If churn at end of month? Average months = 1/0.08 = 12.5 if continuous? Discrete: if retention 92%, expected months = sum_{m=1}∞ (0.92)^m? Actually if paying at beginning? Let's derive. If monthly churn 8%, expected lifetime months = 1/0.08 = 12.5 for constant hazard. If discrete with retention r=0.92 and active at month 0, expected number of payments maybe r/(1-r)=11.5 if pay at end, or 1/(1-r)=12.5 if pay beginning. Usually 1/churn = 12.5. We'll use approximate.

Need maybe correct LTV formula: LTV = ARPU * Gross Margin / churn = 35*0.70/0.08 = $306.25. If use net revenue retention? But no expansion. If CAC $290, contribution after CAC over lifetime = $16.25 per customer before fixed costs and time value. That's razor thin. Actually if LTV gross profit 306.25 minus CAC 290 = 16.25. Margin on ad spend? ROAS? Need monthly cash flow: Spend $10k, acquire 34 customers. Month 1 revenue 34*35=1190? gross profit 833. But CAC paid upfront. Cumulative negative for many months. Need compute cumulative cash by month maybe. With 34.48 customers, monthly gross profit initial = 34.48*24.5=844.8. Churn reduces. Cumulative gross profit approaches 10,557. Net after ad spend = 557 undiscounted. If discount at e.g. 10-15% annual, NPV negative. Also variance and CAC likely increase.

Need answer: No, no le des todavía. Need fix unit economics. Maybe if LTV/CAC > 3 using gross margin? Many use LTV/CAC with gross margin, target >3. If revenue-based LTV/CAC maybe target >3? Here revenue LTV with correct lifetime = 1.51. Gross margin LTV/CAC=1.06. Not viable. Also payback 11.8 months > typical <12 months but with 8% churn too risky; median lifetime? Median = ln(0.5)/ln(0.92)=8.31 months? Actually 0.92^m=0.5 => m=8.31. So half customers leave before 8.3 months, before paying back CAC? Payback 11.8 months, so majority leave before payback. Need compute probability of surviving to payback: 0.92^12 = 0.3677, so only ~37% survive to month 12. Expected payback not robust.

Need maybe mention if churn 8% monthly = annual retention? Annual churn = 1 - 0.92^12 = 63.3%, annual retention 36.7%. Average lifetime 12.5 months not 24. To get 24 months lifetime, churn must be ~4.17% monthly (1/24). Actually if average lifetime 24 months, churn = 1/24=4.17%. With 8%, no.

Need maybe calculate what metrics need to be: For CAC 290 and margin 70, to have LTV/CAC 3, need LTV gross profit = 870. LTV = ARPU*GM/churn = 870 => churn = 35*0.7/870 = 24.5/870 = 2.816% monthly. Or if keep churn 8%, need CAC <= LTV/3 = 306.25/3 = $102.08. Or price/ARPU increase: with churn 8, CAC 290, need ARPU*0.7/0.08 /290 >=3 => ARPU >= 3*290*0.08/0.7 = 99.43? Wait 3*290*0.08 =69.6 /0.7=99.43. Price $99/mo if same margin. Or margin increase? Need gross margin = 3*290*0.08/35 = 1.988 impossible >100. So not margin. Or combination. Need maybe include payback target: If want payback <=6 months, need monthly gross profit >= CAC/6 =48.33; at 70% margin price >=69.04, or CAC <= 6*24.5=147. If payback <=12, CAC <=294 but with churn high not enough. But target LTV/CAC more stringent.

Need answer maybe: If insist spending $10k, do a controlled experiment not scale. Need conditions: validate CAC, churn, payback, cohort cash. Set stop-loss. Maybe propose: don't scale until LTV/CAC >=3 and CAC payback <=6-9 months or at least <= half lifetime. Current expected payback 11.8 months and median life 8.3 months, so negative risk. Need maybe mention working capital: $10k ads is recovered only after ~12 months if no churn, but churn means cash hole. Need compute cumulative cash maybe: For $10k, customers 34.5. Cumulative gross profit after n months = 34.48*24.5*sum retention. If pay at beginning? Let's compute approximate months to break even on cohort? Expected cumulative gross profit per customer after n months = 24.5 * sum_{m=1}^n (0.92)^{m-1} if active at start month 1. Need solve =290. Sum = (1-0.92^n)/0.08. 24.5/0.08*(1-0.92^n)=306.25*(1-0.92^n). Set 290 => 1-0.92^n = 0.94775 => 0.92^n=0.05225 => n= ln(0.05225)/ln(0.92)=35.4 months? Wait that seems inconsistent because expected payback using expected survival is 11.84 months? Let's check. If monthly gross profit from retained cohort: month1 24.5, month2 24.5*0.92, etc. Cumulative tends to 306.25. To reach 290