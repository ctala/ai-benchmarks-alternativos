# Nemotron 3.5 Lightning (NIM) — business_audit/churn_mezcla_free_y_pago

- model_id: `nvidia/nemotron-3.5-lightning-30b-a3b`
- success: True  | final: 7.75 | quality: 8.0
- latency_total: 19.416s | tokens_per_second: 106.5
- input_tokens: 191 | output_tokens: 2067

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de retención. Antes de interpretar una métrica, verificas qué población está midiendo realmente.

**user:**

Estoy en pánico. Mi plataforma reporta un churn del 31% este mes y pensé que estaba en 5%. ¿Qué hago?

Datos que me da el panel:
- Usuarios totales que se dieron de baja este mes: 62
- Usuarios totales a inicio de mes: 200
- Churn reportado: 31%

Detalle que encontré exportando la tabla:
- De los 200 usuarios, 178 están en el plan gratuito y 22 son de pago.
- De las 62 bajas, 60 eran del plan gratuito y 2 eran de pago.

¿Qué tan grave es? Dame un plan.


## Respuesta completa

**First, the math checks out:** 62 ÷ 200 = 31%. The platform isn't bugging out. The reason you thought 5% is almost certainly that you were tracking **paying-user churn only**, or using a different denominator (e.g., only free users, or a prior cohort). 

Here’s the real breakdown from your export:

| Group | Start Count | Churned | Churn Rate |
|-------|-------------|---------|------------|
| Free plan | 178 | 60 | **33.7%** |
| Paid plan | 22 | 2 | **9.1%** |
| **Total** | **200** | **62** | **31%** |

### How bad is it?
- **If you rely on paid revenue:** Paid churn at 9.1% is manageable (though not great; ~$1M/yr ARR businesses typically see 5-7% monthly, depending on segment). The real leak is elsewhere.
- **If free users are a growth engine or cost center:** 33.7% monthly free-plan leakage is **very high**. In most SaaS, 10-15% free-to-paid conversion with ~20-30% free monthly drop-off is already considered leaky. 33% suggests the free experience isn't holding attention.
- **Overall:** This is a **free-plan retention crisis**, not a paid-retention crisis. The 31% headline number obscures that 96.8% of churn (60/62) comes from the free tier.

### Why you saw 5% vs. 31%
You were likely calculating churn only on paying users (2/22 = 9.1%), or you were looking at a prior month/cohort where paid retention was stronger. The platform’s "churn" metric is total-users, which is correct for business health but misleading if you only care about revenue.

---

### Your Action Plan (Prioritized)

#### 1. Stop looking at "total churn." Segment immediately.
- Track **free-churn** and **paid-churn** as separate KPIs. 
- Set alerts: free churn > 25% monthly needs investigation; paid churn > 10% monthly needs action.

#### 2. Diagnose the free-plan leak (the 60/60 free drop)
Quickly check these three things in this order:
- **Activation/onboarding:** Are free users hitting a "wow" moment quickly, or dropping off early?
- **Feature friction/value gap:** Are they hitting a paywall/too-limited features too early, causing frustration rather than upgrade desire?
- **Engagement frequency:** Do free users who stay past day 7 churn later, or is most drop-off in the first 48 hours?

Export the timeline: when did those 60 free users leave? (Day 1? Day 14? Day 30?) That dictates whether it's an onboarding, value-delivery, or engagement problem.

#### 3. Check paid-churn health
2 paid churn isn't statistically significant this month, but ask:
- Were these 2 already at risk (low usage, support tickets, missed logins)?
- Is the paid plan’s value clearly communicated to free users who might upgrade?

#### 4. Run an exit survey (or quick interview) on the 62 who left
- Why did you stop using [product]?
- Was it price, features, or just forgot about it?
- For free users: "What would make you try us again?" → capture verbatim for product messaging.

#### 5. Fix the loop, not just the metric
- **If free churn is the problem:** Tighten onboarding, add guided value milestones, or introduce a "light" paid tier to convert some leaky free users before they drop.
- **If you need the 5% number back:** Stop reporting "total churn" internally. Report **paid churn** and **free activation rate** separately. The 31% is a vanity number if you don't own the free/paid split.

#### 6. Recalculate your "real" churn baseline
Going forward: 
- **Paid churn** = paid churned ÷ paid start count
- **Free churn** = free churned ÷ free start count
- **Overall churn** = total churned ÷ total start (only use this for board decks, not daily ops)

### Bottom line
You don't have a "churn problem" — you have a **free-user retention problem**. The 31% is accurate but misleading. Fix the free onboarding/engagement loop, and the overall number will drop fast. The paid tier is actually holding its own (9.1% is fixable with standard retention work). 

Want me to help you set up the free-vs-paid churn dashboard, or draft an exit-survey template?