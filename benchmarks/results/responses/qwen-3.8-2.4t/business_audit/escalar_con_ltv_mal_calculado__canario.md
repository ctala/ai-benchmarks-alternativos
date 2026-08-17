# Qwen 3.8 2.4T (A95B) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 8.38 | quality: 10.0
- latency_total: 24.304s | tokens_per_second: 84.3
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

We need answer in Spanish. User asks unit economics. Need analyze carefully. Need likely reject or caution. Need recalc LTV, churn, average lifetime with monthly churn 8% is 1/0.08 = 12.5 months, not 24. LTV should be gross margin? Revenue LTV = ARPU * lifetime = 35*12.5=437.5. Gross profit LTV = *0.70 = 306.25. CAC 290. LTV/CAC using revenue = 1.51, using gross profit = 1.06. Not above 3. If include discount rate, even lower. Payback: CAC / monthly gross margin = 290/(35*0.7=24.5)=11.84 months. Revenue payback = 8.29 months. With 8% churn, expected cumulative gross profit maybe discounted? Need maybe calculate NPV with monthly discount? Not given. Need point out $10k spend: expected new customers = 10000/290=34.48. Month 1 revenue = 1207, gross profit = 845, but immediate loss vs ad spend? Need cohort lifetime gross profit = 34.48*306.25 = 10558, barely above 10k, before other operating expenses, and assuming CAC remains constant, churn unchanged, no contribution from existing? Need sensitivity. Also if LTV/CAC using contribution margin after CAC? Need mention magic number? Need maybe if paid ads at scale CAC increases. Need ask for data: retention curve, cohort, payback, cash runway, incremental CAC, conversion, variable costs, discounts. But answer likely: No, todavía no metas $10k. Need fix churn or CAC or price/margin. Need thresholds: To have gross LTV/CAC >=3 with churn 8% and price 35 margin 70: required CAC <= LTV_gross/3 = (35*0.7/0.08)/3 = 306.25/3 = 102.08. Or to support CAC 290 with 3x gross LTV/CAC, churn <= (35*0.7)/(3*290)=24.5/870=2.82% monthly. Or lifetime 35.3 months. If using revenue LTV/CAC 3, required CAC <= 437.5/3=145.8. If need payback <=12 months gross margin, CAC <= 12*24.5=294; so payback just under 12 months but LTV/CAC bad. Actually payback 11.8 months maybe okay if cash and churn stable? But LTV/CAC ~1.06 gross means no profit after CAC, no cover fixed costs. Need clarify LTV should use gross profit not revenue, because revenue includes variable costs. Founder used revenue LTV and overestimated lifetime. Need mention average lifetime = 1/churn only if constant churn and no growth/other; median lower? Expected months = sum survival = 1/churn = 12.5. 2 years would require churn ~4.17% monthly? Actually 24 month average lifetime = 1/24=4.17%. If they observed 2-year retention maybe cohort not steady or churn definition? Need validate. If 8% monthly, after 24 months remaining = (0.92)^24=13.4%, not 0; average 12.5. Cumulative revenue finite = 35/0.08=437.5. Gross = 306.25. If discount rate e.g. monthly 1%, PV = GM / (churn + r) = 24.5 / 0.09 = 272.2 < CAC. If r=0.5%, 24.5/0.085=288.2. So with cost of capital, negative. Need maybe use formula: LTV_gross = ARPU * Gross Margin / churn. If churn monthly. LTV/CAC = (35*0.70/0.08)/290 = 1.06. Revenue multiple = 1.51.

Need answer: "No le des todavía". But perhaps nuanced: If current cash allows experiment and you can pause, small test not $10k? Need recommend: run controlled test e.g. $1k-$2k to measure incremental CAC and payback, not scale. Need define guardrails: CAC <= $102 for 3x gross LTV/CAC; or churn <= 2.8%; or price/margin increase. Maybe acceptable if payback < 12 and cash sufficient, but with 8% churn and CAC 290, you are almost buying dollars at parity; scaling will burn cash and not create value unless LTV improves. Need maybe calculate cash flow: Spend 10k, acquire ~34 customers. First month gross profit 34*24.5=833 (or 845 if 34.48). Need recover ad spend in ~11.8 months if no churn? With churn, expected cumulative gross profit by month n: per customer GM * (1 - (1-churn)^n)/churn? Actually cumulative expected gross profit over n months = monthly_gm * sum_{t=1}^n (1-churn)^{t-1} = GM*(1-(1-churn)^n)/churn. For 290 payback solve 24.5*(1-0.92^n)/0.08 = 290 => (1-0.92^n)=290*0.08/24.5=23.2/24.5=0.94694 => 0.92^n=0.05306 => n=ln(0.05306)/ln(0.92)= -2.936 / -0.08338 =35.2 months? Wait payback considering churn and cumulative expected gross profit: Because lifetime gross profit only 306, payback near 35 months to recover 290? But earlier simple payback CAC/monthly GM=11.8 ignores churn. Correct expected cumulative gross profit with churn: Month 1 24.5, month 2 22.54, etc. To recover 290, need many months because asymptote 306. It reaches 290 at 35 months? But average lifetime 12.5 months; some survive long. Expected payback (time when cumulative expected GP equals CAC) is 35 months, near infinite? Actually since total expected GP 306, 290 is 94.7% of total; yes 35 months. If using revenue, 35*? cumulative revenue = 35*(1-0.92^n)/0.08 = 290 => (1-0.92^n)=290*0.08/35=0.662857 => 0.92^n=0.337143 => n=13.0 months. But should use gross profit, so payback 35 months. Need highlight founder's payback maybe wrong. But some SaaS metrics use payback = CAC / (ARPU*GM) ignoring churn, but better churn-adjusted. If include churn, gross profit payback is very long. Need maybe expected months to recover CAC if customer cancels before? There's probability. But cumulative expected is fine.

Need maybe compute LTV with 2 years: If actually average observed customer stays 24 months, then implied churn is about 4% monthly (if constant), not 8%. Need reconcile. If churn 8%, not 2 years. If they mean median? With 8% monthly, median lifetime = ln(0.5)/ln(0.92)=8.3 months. 2-year average impossible unless churn declines or cohort has long tail. Need ask.

Need produce final with tables maybe. Need mention "LTV/CAC > 3 más o menos" but using gross profit LTV, not revenue. Also 2.9 is not above 3, but actually miscalculated. Need be direct.

Need maybe include recommendation for $10k: No. If still want test, split into small experiments, define stop-loss. Need maybe if $10k is small relative cash and learning budget, but not scale. Need maybe say: if you can afford to lose it for learning, run $1-2k with strict metrics; but don't scale. Need calculate expected result of $10k: 34 customers, MRR +$1,207, monthly gross profit +$845. But total lifetime gross profit ~ $10.56k, only $558 gross contribution before fixed costs, and that's over >2 years, with risk. If CAC rises or churn persists, negative.