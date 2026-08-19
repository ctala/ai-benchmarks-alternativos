# Nemotron 3.5 Lightning — business_audit/escalar_con_ltv_mal_calculado

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 9.19 | quality: 10.0
- latency_total: 5.443s | tokens_per_second: 441.1
- input_tokens: 223 | output_tokens: 2401
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, proporcionando un análisis detallado y práctico de la situación.

## Respuesta completa

### The unit economics say: **No, not yet.** — and here’s exactly why your numbers break down.

#### 1. The churn math you inverted
You assumed a 24-month lifetime, but **8% monthly churn → average lifetime = 1 / 0.08 = 12.5 months.**  
Forget the "2 years" mental model. The expected revenue per customer is:
- Gross revenue: $35 × 12.5 = **$437.50**
- Gross profit (70% margin): $437.50 × 0.7 = **$306.25**

If you force the 24-month assumption, you're implicitly assuming churn drops to ~3.6% monthly — which your current data doesn't support.

#### 2. Real LTV/CAC
| Scenario | Gross LTV | LTV/CAC |
|----------|-----------|---------|
| **Actual churn (12.5 mo)** | $306.25 | **1.06** |
| **Your 24-month assumption** | $588.00 | **2.03** |

Both are **below the ~3:1 benchmark** that indicates a healthy, scalable SaaS unit economics model. Your own "above 3 more or less" call is based on revenue LTV ($840 / $290 = 2.89), but *gross profit* is what pays the bills and funds the next cycle of ads.

#### 3. Payback period & cash flow
- Monthly gross margin per customer: $35 × 0.7 = **$24.50**
- CAC payback: $290 / $24.50 ≈ **11.8 months**
- Average customer stays: **12.5 months**

You barely recover the CAC before the customer churns. Every dollar you spend on ads is essentially break-even on margin, and you've zeroed out the operating leverage you need to grow (sales ops, support, infrastructure, etc.).

#### 4. What $10k actually does
At $290 CAC, $10,000 acquires **~34 customers**.  
- Monthly gross margin from those 34: 34 × $24.50 = **$833**
- It takes **~35 months** of *zero churn* just to recover that ad spend — and churn will eat ~8% of the base each month, meaning you'll never fully recover it.

#### Verdict
**Don't scale the ads yet.**  
Your unit economics are not just "borderline" — they're negative on gross profit, and the model only works if churn improves, CAC drops, or the price/margin jumps significantly.

**To make this work, you’d need one of the following:**
- Churn ≤ 3–4% monthly (lifetime ≥ 25 months)  
- CAC ≤ $150–$180  
- Price ≥ $49–$59/month with margin ≥ 75%  
- A proven retention mechanism that pushes LTV well above $600–$700 gross

If you want to test ads, reduce the budget to $2–$3k, track payback strictly by month 4, and optimize churn *before* doubling down. The math only works once LTV/CAC clears 3.0 on gross profit — right now it's sitting at ~1.0–2.0.