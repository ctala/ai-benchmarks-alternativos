# Qwen 3.8 Max — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 8.23 | quality: 10.0
- latency_total: 47.763s | tokens_per_second: 42.9
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

We need answer in Spanish. User asks as founder. We are unit economics analyst, must recalc. Need likely point out errors: churn 8% monthly means average lifetime = 1/churn = 12.5 months, not 24 months. LTV gross margin? Need use gross profit LTV: ARPU $35, gross margin 70%, monthly gross profit per customer = $24.50. Lifetime value = 24.5 / 0.08 = $306.25 if simple no discount. Or maybe if using average lifetime 12.5 months * 35 * 0.70 = $306.25. If using revenue LTV = 35/0.08=437.5. CAC $290. LTV/CAC using gross profit = 1.06, not 2.9. Using revenue LTV = 1.51. Neither >3. Also payback period = CAC / monthly gross contribution = 290/24.5 = 11.84 months. With revenue = 8.29 months but should use gross profit. Since churn 8%, after 12 months retained cumulative? Need maybe cohort cash flow. Need evaluate $10k spend: acquire ~34 customers (10000/290). Immediate loss? Each customer NPV maybe positive? LTV gross profit 306 vs CAC 290, margin only $16 per customer, before other operating costs, discount, CAC paid upfront, churn stochastic, ad scaling may increase CAC, etc. Not robust. Need maybe mention if CAC is truly $290 and churn 8%, contribution after 12 months? Let's compute. If 34.48 customers, expected gross profit lifetime $10,558? 34.48*306.25=10558, minus ad spend 10000 = $558 gross contribution before ops, discount. Very thin. If use revenue, 34.48*437.5=15086, but ignore 30% costs. Need also consider monthly recurring revenue: 34.48*35=$1207 MRR added, but churn. Need maybe cohort retention: Month 0 acquire 34.5. Month 1 retained 31.7, etc. Cumulative gross profit over 24 months maybe? Let's compute if average lifetime truncated? With 8% monthly, expected active months over infinite horizon sum (1-churn)^t? Depends convention. If churn at end of month, average lifetime = 1/0.08=12.5 months. If survive 24? Probability survive 24 = 0.92^24 ≈ 0.134. So not 2 years. If they say stays about 2 years maybe inconsistent with 8% churn. To have 24 months average, churn ~4.17% monthly. Need state.

Need answer: No le des aún, or not with $10k. Need conditions: improve churn to <=? Need target LTV/CAC >=3 with 70% margin: required CAC <= LTV/3 = 306/3=102. Or if require payback <=12 months? CAC <= 24.5*12=294, payback just at 12 months. But LTV/CAC 1.06. To get LTV/CAC 3 with CAC 290, need monthly gross profit per customer = CAC*3*churn? LTV = GM*ARPU/churn. Need churn <= 24.5/(3*290)=0.02815 = 2.8% monthly. Or increase price/margin. If keep churn 8%, CAC target ~102 for 3x, or maybe 154 for 2x? Need maybe minimum viable: if LTV > CAC and payback acceptable, maybe small profitable? But with LTV $306 vs CAC $290, only $16 gross profit lifetime. Need include discount rate: NPV lower. Let's compute NPV maybe with monthly discount. If annual discount 12%, monthly ~0.95%. NPV of annuity with churn and discount: monthly gross profit 24.5, effective discount rate d = r + churn - r*churn? If payments until churn. PV = mGP * (1-p?) Need convention. If first payment at month 1 and retention probability (1-churn)^t? PV = 24.5 * sum_{t=1}∞ (0.92)^t/(1+r)^t = 24.5 * 0.92/(1+r-0.92). If r=1% monthly, PV=24.5*0.92/(0.09)=250.4 < CAC 290, negative. If first payment immediate? add 24.5 maybe 274.9 still <290. So with discount negative. Need mention.

Need maybe recalc LTV with formula and show founder's math error: using 24 months not consistent. LTV should include gross margin, not revenue. LTV/CAC 3 rule uses gross profit LTV usually. If use revenue, overstates.

Need maybe answer in direct style: "No, no metas $10k este mes". Maybe if still wants: test small, fix churn/CAC. Need perhaps propose experiment: spend e.g. $1k-2k, measure CAC, activation, churn by cohort, payback. Need define guardrails: CAC <= $100 or churn <= 3%, payback <= 6-9 months, LTV/CAC >=3 after margin, magic number? Need maybe mention paid ads can scale CAC marginal increasing. Current CAC average may rise. Need also mention cash flow: CAC upfront, revenues monthly. $10k spend acquires ~34 customers, MRR $1.2k, monthly gross profit $840 if all retained; month 1 after churn maybe $775. To recover $10k gross profit takes ~12 months, and cash needs. If churn, etc.

Need maybe calculate exact: 10000/290=34.48 customers. MRR initial $1,206.90. Gross profit monthly initially $844.83. With 8% churn, expected cumulative gross profit: month n? Lifetime $10,558 (undiscounted). Net after ads $558 before fixed costs. But if discount 10% annual? negative. Also if CAC rises 10% to $319, negative. If churn 9%, LTV = 272, negative. Sensitivity. Need maybe mention ad platform measurement issues, attribution, delayed churn.

Need maybe use table:
- Fundador: 35*24=840 revenue LTV, LTV/CAC 2.9.
- Correcto: vida esperada = 1/0.08=12.5 meses.
- LTV revenue = 35*12.5=437.5.
- LTV gross profit = 437.5*0.7=306.25.
- LTV/CAC = 306.25/290=1.06.
- Payback = 290/(35*0.7)=11.8 meses.
- If discount 12% annual, NPV ~250 (or 275) < CAC.

Need maybe include formula: LTV = ARPU * Gross Margin / Churn. If churn is monthly and stable. If contract annual? But given monthly churn. Need maybe caution: if churn is 8% of customers cancel each month, average lifetime not 24 months. To get 24 months average churn must be 1/24 = 4.17%. If actual observed average customer stays 24 months, then churn should be ~4%, not 8%. Need reconcile. If churn is logo churn vs revenue churn? Use consistent.

Need maybe answer: "No le des a $10k. Le doy a un experimento controlado". Conditions:
1) Validate cohort churn: si 8% real, no.
2) Reduce CAC to <=$100 or improve churn to <=2.8% or price/margin: Need price? With $35 price, 70% margin, to get LTV/CAC 3 at churn 8 and CAC 290, required monthly gross profit = 870? Wait CAC*3=870 LTV. LTV=0.7*price/churn. Need price = LTV*churn/0.7 = 870*0.08/0.7=99.43. So price ~ $99/mes if margin same. Or margin 100% price $69.6? Actually required ARPU = CAC*