# Nemotron 3.5 Lightning — business_audit/escalar_con_ltv_mal_calculado

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 9.281s | tokens_per_second: 291.4
- input_tokens: 223 | output_tokens: 2704

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

**Short answer: No. Do not invest the $10,000 yet.**

You’ve got a common but critical unit economics mistake in your setup. Let me recalculate with the numbers you gave, and show you exactly where the plan breaks.

### 🔍 The flaw: Churn ≠ 2-year lifetime
You’re assuming an average customer stays 24 months. With **8% monthly churn**, the math is:
```
Average lifetime = 1 / churn rate = 1 / 0.08 = 12.5 months
```
Not 24. You’re overestimating lifetime by roughly 50%.

### 📊 Corrected unit economics
| Metric | Your calc | Correct calc |
|--------|-----------|--------------|
| Price/month | $35 | $35 |
| Gross margin | 70% | 70% |
| **Gross profit/month** | — | **$35 × 0.70 = $24.50** |
| Avg. customer lifetime | 24 months | **12.5 months** |
| **Gross LTV** (profit over lifetime) | $35 × 24 = $840 | **$24.50 × 12.5 = $306.25** |
| CAC (paid ads) | $290 | $290 |
| **LTV/CAC** | 840 / 290 ≈ **2.9** | **306 / 290 ≈ 1.05** |

### 💥 What the $10K ad spend actually does
At the corrected LTV/CAC of ~1.05, you’re not making $1.05 profit per dollar spent — you’re **losing ~$0.95 in gross profit for every new customer**.  
- $10,000 ads → ~34 new customers  
- Expected gross profit from those customers: 34 × $306 ≈ **$10,400**  
- But you spent $10,000 to acquire them, and you still have to cover the remaining variable costs (the 30% margin already stripped out), plus any overhead.  
- **Net result: roughly break-even at best, likely a few thousand dollars lost** before you even factor in operating expenses, refunds, or ad-platform fees.

### 🛑 Why this kills scaling plans
- **8% monthly churn is the killer.** For LTV/CAC > 3, you’d need LTV > $870. With $24.50 gross profit/month, that requires a lifetime of **~35 months**, meaning **monthly churn must drop below ~2.8%**.  
- Scaling ads with today’s numbers is pouring water into a leaky bucket. You’ll grow revenue, but profit will evaporate.

### 🧭 Recommended next steps
1. **Fix retention first.** Run diagnostics on why 8% of customers leave each month. Even bringing churn down to 6% lifts LTV to ~$408 and LTV/CAC to ~1.4.
2. **Lower CAC or increase margin.** Can you reduce ad costs to <$200? Can you raise the price or increase gross margin?
3. **Re-run the math after improvement.** If you get churn to ~4% and keep the rest equal, LTV ≈ $437, LTV/CAC ≈ 1.5. Still not >3, but at least you’re not losing money on every acquisition.
4. **Only scale ads when LTV/CAC ≥ 3** *and* you have a predictable payback period ≤ 6–9 months.

**Bottom line:** Your current unit economics lose money on every paid customer. Put the $10,000 toward retention/product-market fit, re-calculate once churn improves, and then revisit paid scale.