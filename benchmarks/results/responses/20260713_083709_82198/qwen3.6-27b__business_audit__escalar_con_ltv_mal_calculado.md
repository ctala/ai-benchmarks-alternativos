# Qwen 3.6 27B base (OpenRouter FP8) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 7.05 | quality: 8.14
- latency_total: 43.113s | tokens_per_second: 47.5
- input_tokens: 217 | output_tokens: 2048

## Respuesta completa

Here's a thinking process:

1.  **Analyze User Input:**
   - **Product/Service:** Subscription-based, $35/month per customer.
   - **Churn Rate:** 8% monthly.
   - **Gross Margin:** 70% (after infrastructure & payment processing).
   - **CAC:** $290.
   - **Founder's LTV Calculation:** $35 × 24 months = $840 (assuming 2-year lifespan).
   - **Founder's LTV/CAC Ratio:** $840 / $290 ≈ 2.9 (claims it's "close to 3").
   - **Proposed Action:** Spend $10,000 on ads this month.
   - **Question:** "¿Le doy?" (Should I go ahead?)

2.  **Identify Key Unit Economics Concepts:**
   - LTV (Lifetime Value) calculation needs to account for churn and gross margin.
   - Simple multiplication ($35 × 24) is flawed because:
     a) It ignores gross margin (LTV should be based on gross profit, not revenue).
     b) It assumes a fixed 24-month lifespan instead of using the churn rate to calculate expected lifespan.
     c) It doesn't discount future cash flows (though often ignored in early-stage, it's worth noting).
   - LTV/CAC ratio benchmark: Generally, >3 is good, but 2.9 is borderline. However, the calculation itself is wrong.
   - Payback period is also crucial for scaling with paid ads.

3.  **Recalculate Correctly:**
   - **Monthly Gross Profit per Customer:** $35 × 70% = $24.50
   - **Expected Customer Lifespan (months):** 1 / churn rate = 1 / 0.08 = 12.5 months
   - **LTV (Gross Profit Basis):** Monthly Gross Profit × Expected Lifespan = $24.50 × 12.5 = $306.25
   - **LTV/CAC Ratio:** $306.25 / $290 ≈ 1.06
   - **Payback Period:** CAC / Monthly Gross Profit = $290 / $24.50 ≈ 11.8 months (nearly the entire lifespan!)

4.  **Evaluate Against Benchmarks:**
   - LTV/CAC: 1.06 is terrible. Needs to be ≥3 for healthy scaling, ideally >4 for aggressive paid growth.
   - Payback period: ~12 months is extremely long. For SaaS/subscriptions, <12 months is acceptable, but <6-9 months is preferred for paid scaling. Here, it's almost the entire customer life, meaning you barely recover costs before they churn.
   - Founder's mistake: Used revenue instead of gross profit, assumed fixed 2 years instead of using 8% monthly churn (which implies ~12.5 months), and miscalculated the ratio.

5.  **Identify Additional Risks/Considerations:**
   - **Churn vs. Lifespan:** 8% monthly churn is high. Expected life is 12.5 months, not 24.
   - **Margin:** 70% is decent, but LTV must be calculated on gross profit.
   - **CAC:** $290 is high relative to monthly revenue ($35). It takes 8+ months of revenue just to cover CAC, and that's before considering gross margin.
   - **Scaling Risk:** Pouring $10k into ads with these unit economics will likely burn cash, increase churn pressure, and yield negative ROI.
   - **Cash Flow/Runway:** Payback period of ~12 months means cash is tied up for a year. Scaling will strain liquidity.

6.  **Formulate Response (Mental Refinement - Spanish):**
   - Start with a clear, direct answer: No, no le des aún. Los números no sostienen el escalamiento.
   - Explain the founder's miscalculations step-by-step:
     * LTV debe calcularse sobre margen bruto, no sobre ingreso.
     * La vida útil no es fija (24 meses), se deriva del churn: 1/0.08 = 12.5 meses.
     * Recalcular: LTV = $35 × 70% × 12.5 = $306.25.
     * LTV/CAC real = 306.25 / 290 ≈ 1.06 (no 2.9).
   - Highlight payback period: $290 / $24.5 = ~11.8 meses. Es decir, tardas casi un año en recuperar la inversión, y el cliente se va antes.
   - Explain why this kills paid scaling: Cash flow tension, negative ROI, churn amplifies losses.
   - Provide actionable recommendations:
     * Reduce CAC (optimize funnels, creative, targeting, consider organic/referral).
     * Increase margin or price (test $40-$45, improve onboarding/reduction of churn).
     * Lower churn (8% is high; aim for <5% monthly).
     * Run a small pilot ($1k-$2k) to validate actual cohort performance before scaling.
     * Track cohort LTV, not just blended.
   - Maintain tone: Analytical, direct, professional, unit-economics focused. "Muchos planes mueren en la aritmética" -> echo this.

7.  **Structure Response (Spanish):**
   - Direct verdict first.
   - Break down the miscalculation.
   - Show correct math.
   - Explain implications (LTV/CAC, payback, cash flow).
   - Give concrete next steps.
   - Keep it tight, no fluff.

   Draft:
   No. Con estos números, escalar con publicidad pagada te quemará cash. Tu cálculo tiene dos errores estructurales que matan la rentabilidad:

   1. **LTV se calcula sobre margen bruto, no sobre ingreso.** Un cliente no te deja $35/mes, te deja $35 × 70% = $24.50.
   2. **La vida útil no es fija.** Con un churn del 8% mensual, la expectativa de vida es 1 / 0.08 = 12.5 meses, no 24.

   🔢 **Recálculo correcto:**
   - LTV = $24.50 × 12.5 = **$306.25**
   - LTV/CAC = $306.25 / $290 ≈ **1.06** (no 2.9)
   - Payback period = $290 / $24.50 ≈ **11.8 meses**

   📉 **Qué significa esto en la práctica:**
   - Estás invirtiendo $290 para recuperar $306 en 12 meses. Margen neto por cliente: ~$16, antes de costos fijos, soporte, impuestos y riesgo de churn acelerado.
   - Un payback de ~12 meses es insostenible para escala pagada: tu cash queda inmovilizado casi un año mientras el cliente se va.
   - LTV/CAC < 1.5 es zona de pérdida. Con 1.06, cada dólar invertido en ads te devuelve menos de lo que cuesta.

   ✅ **Qué hacer antes de soltar los $10k:**
   1. **Baja el CAC o sube el LTV:** Prueba creatividades, audiencias lookalike, o cambia a $40–$45/mes si el mercado lo soporta.
   2. **Ataca el churn:** 8% mensual es alto. Implementa onboarding, check-ins a los 14/30 días, y analiza por qué se van en el primer trimestre.
   3. **Valida con cohortes, no con promedios:** Lanza $1k–$2k, mide LTV real a 3/6/9 meses por cohorte. Si no superas LTV/CAC ≥ 3 a los 6 meses, no escalese.
   4. **Calcula payback objetivo:** Para SaaS pagado, apunta a < 9 meses (idealmente < 6). Tu modelo actual está al revés.

   Muchísimos fundadores confunden ingreso con margen y asumen vida útil en lugar de usarla. Los números reales dicen: **no escalese aún**. Corrige la unidad primero, luego multiplica. ¿Quieres que revisemos un escenario con precio ajustado o churn reducido para ver el umbral exacto donde sí conviene invertir? 

8.  **Self-Correction/Verification during drafting:**
   - Check math: $35 * 0.7 = $24.5. 1/0.08 = 12.5. $24.5 * 12.5 = $306.25. Correct.
   - LTV/CAC = 306.25/2