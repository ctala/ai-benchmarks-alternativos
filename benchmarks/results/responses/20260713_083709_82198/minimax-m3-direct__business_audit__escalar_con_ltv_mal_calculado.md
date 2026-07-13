# MiniMax M3 (directo / sub) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `MiniMax-M3`
- success: True  | final: 7.52 | quality: 8.4
- latency_total: 30.234s | tokens_per_second: 90.0
- input_tokens: 342 | output_tokens: 2720

## Respuesta completa

<think>The user is a Spanish-speaking founder asking me to validate their unit economics before approving a paid advertising growth plan. Let me carefully recalculate their numbers.

Let me think through this carefully.

**The user's claim:**
- Price: $35/month per customer
- Monthly churn: 8%
- Gross margin: 70%
- CAC: $290
- Calculation: Customer stays ~2 years, so LTV = $35 × 24 = $840
- LTV/CAC = 2.9 (claims it's above 3)
- Wants to spend $10,000 on ads this month

**Let me check each assumption:**

**1. "A customer stays ~2 years"** - This is wrong. With 8% monthly churn:
- Monthly retention rate = 92%
- Average customer lifetime = 1/churn rate = 1/0.08 = 12.5 months (not 24!)
- This is a classic mistake. The user is doing 1/8% = 12.5 months, but they said 2 years = 24 months. That's double the actual lifetime.

**2. LTV calculation** - The user is NOT applying gross margin!
- Gross LTV per customer = $35 × 12.5 months = $437.50
- Margin-adjusted LTV = $437.50 × 0.70 = $306.25

The user calculated LTV = $840, but this is wrong because:
- They used 24 months instead of 12.5 months
- They didn't apply the 70% gross margin

**3. Correct LTV/CAC ratio:**
- LTV = $306.25
- CAC = $290
- LTV/CAC = $306.25/$290 = 1.056

That's roughly 1:1, NOT 3:1. This is catastrophically bad.

The payback period is also alarming:
- Gross margin per month = $35 × 0.70 = $24.50
- Payback = $290 / $24.50 = ~11.8 months
- But average lifetime is only 12.5 months
- So basically you break even (or slightly profit) per customer over their lifetime

**4. The math also has another issue:** Some people calculate average lifetime as 1/churn, but that's actually the "expected lifetime" assuming constant churn. It's correct for steady-state. The user's mistake is using 24 months.

Wait, let me reconsider. With 8% monthly churn:
- The probability of surviving n months = (1-0.08)^n = 0.92^n
- Expected lifetime = sum from n=1 to infinity of 0.92^n = 0.92/(1-0.92) = 0.92/0.08 = 11.5 months

Hmm, two ways to compute this:
1. Discrete: 1/churn = 1/0.08 = 12.5 months (this is for continuous/approximate)
2. More precise: 0.92/0.08 = 11.5 months

Actually, the standard formula for average customer lifetime with monthly churn is:
- If churn rate c is the fraction leaving each month
- E[L] = 1/c for continuous, but for discrete monthly, it's (1-c)/c + 1 ... no wait
- Let me redo: at end of month 1, prob alive = (1-c). End of month 2, (1-c)^2. Etc.
- Expected lifetime in months = sum_{n=1}^infty (1-c)^n = (1-c)/c
- With c=0.08: 0.92/0.08 = 11.5 months

So expected lifetime is about 11.5 months, not 24 months. The user is way off.

Actually there's debate about whether to use 1/c or (1-c)/c. The "1/c" is often used as a simplification and is approximately right. The exact formula is (1-c)/c which gives a slightly lower number. Either way, it's not 24 months.

Let me also consider: should we discount future cash flows? Typically in unit economics we don't discount at early stage, but it's worth mentioning.

**5. Other concerns:**
- The CAC payback period with this math:
  - Gross margin per month = $24.50
  - Payback = $290 / $24.50 ≈ 11.8 months
  - Average customer lifetime = ~11.5-12.5 months
  - This means you're recovering CAC roughly AT the end of the customer's lifetime
  - Any additional costs (overhead, support, refunds, etc.) will put you in the red

- "I'm already profitable" claim: This needs scrutiny. If you scale with this CAC at this churn, profitability disappears. The current profitability is likely because:
  - Most revenue is from existing customers with low churn over time
  - You're not replacing customers (if you stop acquiring, the base shrinks by 8%/month)
  - To maintain, you need to acquire at 8% of base per month

- Let me compute: if base is 1000 customers, monthly churn = 80. To maintain, acquire 80.
  - Cost to maintain: 80 × $290 = $23,200/month
  - That's WAY more than the $35 × 1000 × 0.70 = $24,500 monthly gross profit
  - You're essentially losing money on acquisition for retention replacement

Actually wait, with $35/month and 70% margin = $24.50 net per customer per month. If you lose 8% per month, you're replacing customers whose cumulative future contribution equals... let me think.

Actually the simple check: if LTV ≈ CAC, then every customer acquisition roughly breaks even. So scaling doesn't add profit; it just maintains.

**6. Recommendations:**

a) Fix the LTV calculation immediately
b) Reject this growth plan or radically reduce spend
c) Find ways to:
   - Reduce churn (biggest lever)
   - Reduce CAC
   - Increase price
   - Add expansion revenue
d) Suggested targets:
   - To get LTV/CAC = 3 with current margin:
     - Need LTV = $870, with 70% margin = gross LTV of $1242
     - With $35/month, need ~35.5 months lifetime
     - That means churn of ~2.8%/month (using 1/c)
   - Or reduce CAC to ~$100 with current LTV of $306

Let me also double check the LTV formula:
- LTV (gross margin adjusted) = ARPU × Gross Margin × Customer Lifetime
- = $35 × 0.70 × 11.5 months = $281.75 (using 0.92/0.08 = 11.5)
- = $35 × 0.70 × 12.5 months = $306.25 (using 1/0.08 = 12.5)

So LTV ≈ $280-306, not $840.

LTV/CAC ≈ $290/$290 ≈ 1.0, NOT 2.9.

This is a critical finding. I need to be very clear and direct with the user, in Spanish since they wrote in Spanish.

**Format considerations:**
- The user wrote in Spanish, so I should respond in Spanish
- They seem to be a founder, not super technical. I should be clear and direct.
- I should show my math step by step
- I should give a clear verdict ("No")
- I should explain why
- I should suggest alternatives
- Use headers/structure to make it scannable
- Don't be too long-winded, but thorough on the math
- Tables might help for the comparison

Let me structure this:

1. TL;DR / Verdict upfront
2. The math mistake explained clearly
3. The correct calculation
4. What this means for scaling
5. What to do instead
6. The path to a healthy plan

Let me draft this in Spanish now. I should use a professional but direct tone - the system prompt says "Muchos planes mueren en la aritmética" - many plans die in the arithmetic. I should be firm but helpful.</think>

# No. Esos números no cierran. Hay dos errores en tu cálculo y uno de ellos te infla el LTV casi 3x.

Te lo desarmo.

---

## Error 1: La vida media del cliente no es 24 meses

Con churn mensual de 8%, la fórmula correcta de vida media esperada es:

$$\text{Vida media} = \frac{1 - \text{churn}}{\text{churn}} = \frac{0{,}92}{0{,}08} \approx 11{,}5 \text{ meses}$$

(Una aproximación común es 1/churn = 12,5 meses. Cualquiera de las dos te da **alrededor de un año**, no dos.)

**De dónde sale tu "2 años"?** Probablemente de la regla mental "duplicar el churn en meses". Pero eso sería válido si hablaras de retención acumulada al ~85% anual, no con 8% mensual.

---

## Error 2: No aplicaste el margen bruto al LTV

El LTV que importa para comparar contra CAC es el **LTV ajustado por margen**, porque el CAC lo gastas en dinero real, no en revenue.

Tu cálculo de $840 es el revenue bruto que produce un cliente en 24 meses. Pero de esos $840, el 30% se va en infraestructura y procesador. Solo te quedan $588 netos — y eso *además* está calculado sobre una vida media mal estimada.

---

## Recalculemos bien

| Concepto | Tu número | Correcto |
|---|---|---|
| Vida media del cliente | 24 meses | ~11,5 meses |
| Revenue por cliente | $840 | $35 × 11,5 = **$402,50** |
| **LTV ajustado por margen (70%)** | $840 | **~$281,75** |
| CAC | $290 | $290 |
| **LTV / CAC** | 2,9 | **~0,97** |
| Payback (con margen $24,50/mes) | — | **~11,8 meses** |
| Vida media | — | ~11,5 meses |

---

## Lo que esto significa

**LTV/CAC ≈ 1, no 3.** Estás pagando $290 para recuperar $282. Cada cliente que adquieres te deja ~$8 en rojo en valor presente, antes de overhead, soporte, devoluciones, etc.

**Payback ≈ 11,8 meses sobre una vida de ~11,5 meses.** Apenas recuperas la inversión justo cuando el cliente se va. Cualquier fricción te mete en negativo.

**El verdadero problema:** tu actual rentabilidad probablemente viene de la **base instalada que ya tienes**. Pero esa base se erosiona 8% cada mes. Para mantenerte plano, necesitas reponer 8% de clientes al mes **pagando $290 cada uno**. Eso es prácticamente un casino.

Si metes $10.000 en ads este mes, conseguís ~34 clientes. Te dejan ~$1.000 de pérdida neta antes de considerar el churn que sigue sufriendo el resto de tu base.

---

## Qué hacer, en orden de impacto

**1. Bajá el churn. Es tu palanca más grande.**
Con los demás números iguales:
- Churn 4%/mes → vida ~23 meses → LTV ~$564 → **LTV/CAC = 1,94**
- Churn 3%/mes → vida ~31 meses → LTV ~$759 → **LTV/CAC = 2,62**
- Churn 2%/mes → vida ~46 meses → LTV ~$1.127 → **LTV/CAC = 3,89** ✓

**2. Bajá el CAC o subí el precio.** Para llegar a LTV/CAC = 3 con tu churn actual, necesitás CAC ≤ $94 o un ticket de ~$108/mes.

**3. Recién después, escalá.** Un plan agresivo solo se justifica cuando LTV/CAC ≥ 3 **y** el payback es menor a la mitad de la vida media. Hoy no estás ni cerca.

---

## Reglas simples para no repetir el error

- Vida media en meses ≈ **1 / churn mensual** (o (1−churn)/churn si querés el exacto).
- LTV para comparar con CAC = **Revenue × Margen bruto × Vida media**.
- Si el payback ≥ vida media, el plan está roto por construcción.

Antes de meter los $10.000, mejor invertí esa plata en entender por qué se te van 8 de cada 100 clientes por mes. Ahí está el negocio.