# DeepSeek V4 Pro (0813) — sales_outreach/campaign_optimization

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.18 | quality: 10.0
- latency_total: 234.66s | tokens_per_second: 34.9
- input_tokens: 351 | output_tokens: 8192

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo estos resultados de mi campana de Google Ads del ultimo mes:

Campana A (Landing principal):
- Impresiones: 50,000 | Clicks: 1,500 | Signups: 45 | Costo: $2,100
- Keywords: "software gestion inventario", "inventario pymes"

Campana B (Blog content):
- Impresiones: 120,000 | Clicks: 4,800 | Signups: 24 | Costo: $1,800
- Keywords: "como gestionar inventario", "problemas inventario restaurante"

Campana C (Competidor):
- Impresiones: 15,000 | Clicks: 900 | Signups: 36 | Costo: $3,200
- Keywords: "alternativa a [competidor]", "[competidor] vs"

Mi presupuesto total es $5,000/mes.

1. Calcula CTR, CPC, CPA, y conversion rate de cada campana
2. Cual campana debo escalar y cual pausar? Justifica con numeros
3. Como redistribuiria el presupuesto de $5,000?
4. Que A/B tests sugeririas para el proximo mes?


## Respuesta completa

We need answer in Spanish. Need calculate metrics. Need be careful. User gives campaigns. Budget total $5,000/mes. Need calculate CTR, CPC, CPA, conversion rate each. Then recommend scale/pause based numbers. Redistribute budget. A/B tests.

We need compute.

Let's calculate.

Campaign A: Impressions 50,000; Clicks 1,500; Signups 45; Cost $2,100.
CTR = clicks/impressions = 1500/50000 = 0.03 = 3%.
CPC = cost/clicks = 2100/1500 = $1.40.
CPA = cost/signups = 2100/45 = $46.6667 ≈ $46.67.
Conversion rate = signups/clicks = 45/1500 = 0.03 = 3%. (signup rate click-to-signup)
CVR maybe signups/clicks.

Campaign B: Impressions 120,000; Clicks 4,800; Signups 24; Cost $1,800.
CTR = 4800/120000 = 0.04 = 4%.
CPC = 1800/4800 = $0.375 = $0.38.
CPA = 1800/24 = $75.00.
CVR = 24/4800 = 0.005 = 0.5%.

Campaign C: Impressions 15,000; Clicks 900; Signups 36; Cost $3,200.
CTR = 900/15000 = 0.06 = 6%.
CPC = 3200/900 = $3.5556 ≈ $3.56.
CPA = 3200/36 = $88.8889 ≈ $88.89.
CVR = 36/900 = 0.04 = 4%.

Need assess scale/pause. Need think: C has highest CTR/CVR but highest CPC/CPA. A has best CPA $46.67 and reasonable CVR 3%, CTR 3%, CPC $1.40. B has low CPC but low CVR and CPA $75. C has high CPA $88.89. Budget total $5k. They spent $7,100? Wait costs sum: 2100+1800+3200 = $7,100. But user says total budget $5,000/mes. They overspent? Need note actual spend is $7,100. But maybe budget is $5k, results from last month exceed? Need use data.

Need answer "2. Cuál campaña debo escalar y cuál pausar? Justifica con números". We need say scale A, maybe optimize C? Pause B? Let's think.

Campaign A: CPA $46.67 lowest, conversion rate 3%, CTR 3%, CPC $1.40. It's main landing. It converts signups efficiently. Scale A.

Campaign B: High impressions/clicks, low CPC, but conversion rate 0.5% and CPA $75. If goal is signups, B is inefficient vs A. Could be good for top-funnel content, but not for direct signups. If budget limited $5k, pause or reduce B. Maybe it could nurture later but not direct signup. Need justify.

Campaign C: Competitor. High CTR 6%, high conversion rate 4% (best), but very high CPC/CPA $88.89. It yields 36 signups at high cost. Could maybe optimize search terms / negatives to lower CPC? But as is, CPA highest. At $5k budget, maybe not scale C unless reduce CPC/CPA. But C has best conversion rate; if can improve CPC/CPA then scale. However current CPA $88.89 is almost double A. So maybe pause C or reduce? Need decide "escalar y pausar" singular? The question asks which to scale and which to pause. We can say scale A, pause B (or C?) based on CPA.

Let's examine budget redistribution. If we have $5,000, how allocate? Need maybe allocate majority to A. Need suggest perhaps A $3,500, C $1,000, B $500? But they ask "redistribuiria el presupuesto de $5,000". Need build data-driven.

Let's see possible returns. If allocate all to A, at CPA $46.67, $5,000 yields ~107 signups. If split A $3,500 (75 signups at $46.67), B $500 (6.7 signups at $75), C $1,000 (11.2 signups at $88.89) total ~93 signups. Better all to A? But may be diminishing returns; cannot necessarily spend all in A because search volume. A got 50k impressions, 1500 clicks with $2100. Could increase maybe not unlimited. Need not ignore diminishing returns. We can suggest shifting most to A because it has best CPA, but monitor impression share. Maybe maintain some competitor C due to high conversion and higher purchase intent? Hmm.

Let's compute actual current budget distribution? They say total budget $5,000 but spent $7,100. Maybe maybe typo? They list cost total $7,100, budget total $5,000. Need mention "Ojo: el gasto reportado suma $7,100, superior a tu presupuesto de $5,000; asumo que quieres rebalancear a $5,000." That's important.

Need maybe calculate percentages of spend: A 29.6%, B 25.4%, C 45.1%. But C gets 45% of spend for only 36 conversions. We can propose shift from C and B to A.

Potential allocation: 
- A: $3,000 (60%) → at CPA $46.67 ≈ 64 signups. But maybe scale A up.
- C: $1,200 (24%) → at CPA $88.89 ≈ 13.5 signups; optimize to lower CPA.
- B: $800 (16%) → at CPA $75 ≈ 10.7 signups; maybe test/retargeting.
Total expected ~88 signups. But if current spend $7,100 yielded 105 signups; at $5,000 maybe if same efficiency? Wait total signups 45+24+36=105; total cost $7,100; overall CPA $67.62. With $5,000, if allocate proportionally, expected 74 signups. If shift to A, maybe better.

Alternatively allocate A $2,500, C $1,500, B $1,000? Expected signups: A 53.6, C 16.9, B 13.3 = 83.8. Still less than all A. But due to saturation maybe.

Need maybe use metrics to decide budget allocation via inverse CPA weighted? We can calculate efficient allocation by minimizing CPA? Let's think.

If maximize conversions under $5,000, allocate to lowest CPA first until marginal CPA rises. Since A has lowest CPA $46.67, allocate as much as possible to A. But A cannot absorb infinite budget due to search volume. A currently spent $2,100 for 45 conversions. To scale maybe maybe double? Could probably spend more but not all $5,000. We might propose allocating ~60-70% to A. Need be practical.

We can compute "marginal signups per $1,000":
- A: 21.4 signups per $1,000 (since $46.67 CPA)
- B: 13.3 signups per $1,000
- C: 11.3 signups per $1,000

A clearly most efficient. B and C less.

Maybe "Pausar B ya que es la menos alineada a conversión directa; su CPA es 60% más alto que A y convierte 6 veces peor (0.5% vs 3%)." But C has highest CPA, though conversion rate best. "No pausaría C del todo: tiene la mayor intención (CTR 6%, CVR 4%) y es de competidor; pero está cara. Reducir su presupuesto y optimizar términos/bids. Si tengo que elegir una para pausar, pausaría B porque su rol es contenido y no signups directos."

Need maybe say "escalar A; pausar B; optimizar C." That's balanced.

Need maybe answer with table.

Let's compute exact metrics:

Campaign A:
- CTR = 3.00%
- CPC = $1.40
- CPA = $46.67
- CVR = 3.00%

Campaign B:
- CTR = 4.00%
- CPC = $0.38 (or $0.375)
- CPA = $75.00
- CVR = 0.50%

Campaign C:
- CTR = 6.00%
- CPC = $3.56 (or $3.5556)
- CPA = $88.89
- CVR = 4.00%

Note: conversion rate signups/clicks.

Need maybe compute total:
Total spend $7,100; total signups 105; overall CPA $67.62. Overall CTR = (1500+4800+900)/(50000+120000+15000)=7200/185000=3.89%. Overall CVR = 105/7200 = 1.46%. Overall CPC = 7100/7200 = $0.99. But we only need per campaign, but maybe include total for context.

Need maybe compute current distribution:
A: $2,100 / $7,100 = 29.6% of spend; 42.9% of signups (45/105).
B: $1,800 / $7,100 = 25.4%; 22.9% signups.
C: $3,200 / $7,100 = 45.1%; 34.3% signups.
This shows C over-invested.

Potential redistribution suggestion:
Option maybe:
- A: $3,000 (60%) → expected ~64 signups at current CPA.
- B: $500 (10%) → expected ~7 signups. Or $0 if pausing. 
- C: $1,500 (30%) → expected ~17 signups. 
Total expected ~88 signups at current CPAs. But if pause B: A $3,500 / C $1,500 expected 75 + 17 = 92 signups. But if pause C? A $3,500 / B $1,500 expected 75 + 20 = 95 signups. Actually B has better CPA than C ($75 vs $88.89). If only based on CPA, allocate more to B than C. But B is blog content; direct conversions poor but cheaper CPA than C. Wait B CPA $75, C CPA $88.89. So if only direct signups, C is worse than B. But C has quality? We need decide.

Let's reconcile. A best CPA $46.67. B second best CPA $75. C worst CPA $88.89. So if only maximizing signups, allocate to A then B then C. But C has high CVR; maybe high intent but expensive clicks. Its CPC is $3.56 (9.5x B's CPC, 2.5x A's CPC), so despite high CVR, CPA is high. So if we want direct signups, C is least efficient. So maybe pause C rather than B? But B's conversion rate is low but CPC is very low, so CPA $75, still lower than C. However B is blog content; maybe it's top funnel, not direct. But from direct signup cost, B beats C.

Let's compute "signups per $1,000" as above:
A: 21.4
B: 13.3
C: 11.3
So C is worst. Should pause C? But question asks "Cuál campana debo escalar y cuál pausar?" It might expect scale A, pause C because worst CPA. But maybe C is competitor campaign with highest conversion rate, maybe maybe should not pause completely but optimize. Need craft nuanced.

Let's read user's Spanish. They ask:
"1. Calcula CTR, CPC, CPA, y conversion rate de cada campana
2. Cual campana debo escalar y cual pausar? Justifica con numeros
3. Como redistribuiria el presupuesto de $5,000?
4. Que A/B tests sugeririas para el proximo mes?"

They likely want direct recommendation. Data:
- A: CPA $46.67, CVR 3%
- B: CPA $75, CVR 0.5%
- C: CPA $88.89, CVR 4%

If we just use CPA, A best, C worst, so "escalar A, pausar C". But C has highest CVR and CTR; maybe its high CPA due to high CPC. Could "pausar C" maybe waste high-intent competitor traffic? But budget limited, efficiency matters. However B is blog content with very low conversion; maybe not efficient for signups. Let's analyze deeper.

We need maybe determine which campaign to scale/pause based on objective. If objective is signups at lowest cost, A is best. Pause C? But B is a content campaign; maybe if goal is lead gen, B's CPA $75 vs C $88.89. Actually B is more cost-efficient than C. So "pausar C" would be data-driven. But B has 0.5% conversion rate, but because clicks are so cheap, it still produces signups at $75, better than C's $88.89. So C is the worst in CPA despite high CVR.

But one could argue B is top-of-funnel and could be used for retargeting; its value not just direct signups. But asked "signups" likely primary conversion. So direct CPA matters.

Need maybe compute "if you have $5,000 and reallocated based on CPA, you'd allocate more to A, then B, then C." But due to B's low conversion, maybe use B for awareness/retargeting only, not direct signups.

Let's see possible budget allocation if maximizing direct conversions with current CPAs:
We need allocate budget to lowest CPA until marginal return equal? Since CPAs constant, allocate all $5,000 to A: expected 107 signups. But impractical due to search volume/diminishing returns. Need maybe add "asumiendo que A tiene volumen disponible, destina la mayor parte ahí." If not, we can use a "weighted by spend efficiency" allocation maybe.

Could suggest redistribution:
- A: $3,000 (60%) because it's the most efficient and likely can absorb more.
- B: $1,000 (20%) maintain content/awareness; cap because CPA $75 and CVR low.
- C: $1,000 (20%) only for high-intent competitor; pause if CPA doesn't improve below $50-70.
But this yields expected signups: 64.3 + 13.3 + 11.3 = 88.9. That's better than current? Current actual got 105 with $7,100. For $5,000, expected 74 at overall CPA. So 89 is improvement.

Alternatively if we pause C: A $3,500, B $1,500: expected 75 + 20 = 95 signups. Better expected. But B may not be scalable? B had 4800 clicks, low CVR, maybe could spend more? If we allocate $1,500, CPC $0.38 -> ~3947 clicks; at 0.5% CVR -> 19.7 signups. It had $1,800 produce 24 signups. Maybe $1,500 produce 20. It's okay. But if B is content, it also generates impressions and potential retargeting. Might be worth keeping some budget.

What about A: Currently spent $2,100, 50,000 impressions. If double spend, maybe search volume constraints. We don't know impression share. But A's keywords "software gestion inventario", "inventario pymes" maybe high intent; might have more volume. Could allocate $3,000 to A. At CPC $1.40, $3,000 -> 2,143 clicks; at 3% CVR -> 64 signups. That's plausible. But if search volume limited, maybe $3,000 not fully spent. We can mention "si A tiene inventario de impresiones; si no, transfiere el remanente a B".

Need maybe also note "pausa B o C?" Let's choose one. "Escalar A, pausar C (o pausar B si solo consideras conversión directa? Wait C worst CPA)." Hmm.

Let's re-evaluate what "pausar" means. If they ask "Cuál campaña debo escalar y cuál pausar?" Maybe they expect one scale one pause. We can "Pausaría C" because worst CPA. But C has best conversion rate. In PPC, competitor campaigns can be expensive due to high CPC; might not be profitable unless high LTV. Pausing C might be right if signups are all that matter and budgets tight. But could also "pausaría B" because conversion rate is too low (0.5%) and its CPA is 60% worse than A; though C's CPA is 90% worse than A. Hmm.

Let's compute CPA relative to A:
- B vs A: $75 vs $46.67 → 60.7% higher.
- C vs A: $88.89 vs $46.67 → 90.5% higher.
So C is worse.

CTR/CVR:
- C has best conversion rate 4% (33% better than A, 8x B).
- C has best CTR 6% vs A 3% vs B 4%.
- But C's CPC is $3.56 vs A $1.40, causing high CPA.

Could maybe "Si el objetivo es signups y no branding, pausaría C; mantendría B con presupuesto bajo por su CPC bajo y posibles remarketing." But B's direct conversion rate is 0.5%. Hmm.

Let's think from a marketing funnel:
- Campaign A: high intent, good conversion, best CPA → scale.
- Campaign B: informational/educational blog. Low direct conversion but cheap traffic; useful for awareness, SEO/content promotion, retargeting. But if measured only by signups, it's mediocre.
- Campaign C: competitor conquest. High CTR, high CVR (high purchase intent), but very high CPC. This is typical: competitor keywords are expensive but convert. If you can optimize quality score, bids, and landing page to reduce CPC/CPA, maybe worth keeping. But with limited $5k, maybe pause until optimize.

The user asks "Cuál campaña debo escalar y cuál pausar?" Could answer: "Escalar A; pausar C si no puedes bajar su CPC/CPA; pausar B si el objetivo es solo conversión directa." But need be decisive.

Maybe final structure:
1. Table with metrics.
2. Diagnosis:
   - A: best CPA, good CVR; should scale.
   - B: cheap clicks, high volume, but very low CVR and CPA $75; not ideal for signups; use as top-funnel/retargeting or reduce.
   - C: best CTR/CVR but CPC/CPA too high; not scalable as-is. Pause or reduce until CPC < $2.50? Actually if C's CVR 4%, to get CPA < $50, CPC needs < $2.00. That's 44% reduction. For C to match A's $46.67, CPC needs 4%*46.67 = $1.87. Currently $3.56. Would need huge reduction. Might be unrealistic.
   - If forced to pause one, pause C because highest CPA and consumes 45% of spend for only 36 signups.
   - But maybe pause B? Wait B consumes 25% and produces 24 signups. C consumes 45% and produces 36. C is less efficient. So pause C.

Let's test expected signups if pause C and reallocate to A+B:
Current total signups 105 with $7,100. If remove C ($3,200) and reallocate that to A and B? But budget $5,000 total. If we pause C and put budget to A/B, at current CPAs:
- Suppose A gets $3,500, B gets $1,500. Expected signups: A 75, B 20 = 95. If A can absorb. That's better than keeping C under any split? Let's see if we keep C and allocate efficiently:
Given $5,000, if allocate to lowest CPA first:
- First A $2,100 -> 45 signups (but we can allocate more maybe)
- Next B $1,800 -> 24 signups
- Remaining $1,100 to C -> 12.4 signups
Total 81.4 signups. Actually if current CPAs constant, allocate to A up to $2,100? Wait A current spend $2,100 but can scale. We don't know max. But if we use current spend as max? If not scaling A beyond $2,100? Hmm.

Maybe "redistribuiría $5,000" as:
- A: $3,000 (60%)
- B: $1,000 (20%)
- C: $1,000 (20%) or $0?
Need maybe use current "cost per signup" to suggest shift from C to A. Could state "para maximizar conversiones con la data actual, el orden de prioridad es A > B > C." This is clear.

Let's calculate example allocation if "pausar C" and "escalar A":
- A: $3,500 (70%)
- B: $1,500 (30%)
- C: $0
Expected signups at same CPA:
A = 3500 / 46.67 = 75.0
B = 1500 / 75 = 20.0
Total = 95.0
CPC etc. This is higher than current projected for $5,000 if same overall CPA.

But if we need keep C for high intent:
- A: $3,000 (60%)
- B: $1,000 (20%)
- C: $1,000 (20%)
Expected: A 64.3, B 13.3, C 11.3 = 88.9

Could mention both: "mi opción principal: pausar C; si quieres conservar C por su alta CVR, dale máximo 20% y optimiza."

Need maybe include "Ojo: C es la que más presupuesto consumió ($3,200, 45%) y tiene peor CPA. Eso hay que corregir."

Need answer 4: A/B tests for next month. Need suggest specific tests per campaign.

For A (Landing principal):
- Test de landing page: página principal actual vs variante enfocada en features, social proof, CTA más visible, formulario corto.
- Test de CTA: "Prueba gratis" vs "Solicitar demo" vs "Comenzar ahora".
- Test de keywords/ads: "software gestión inventario" vs "sistema de inventario pymes"; match types, exact/phrase.
- Test de copy en ad: beneficios vs funcionalidades; incluir pricing/clear offer.
- Maybe test headline: "El software de inventario para pymes" vs "Controla tu inventario en minutos".

For B (Blog content):
- If keep: test call-to-action in content: banner, inline, exit intent, content downgrade lead magnet (e.g., checklist/plantilla) vs direct signup.
- Test different landing from blog to signup: maybe dedicated lead magnet (guía descargable) to capture email then nurture.
- Test ad copy for informational: "guía gratuita" vs "artículo".
- Maybe test audiences/placements.

For C (Competidor):
- Test ad copy: mention competitor vs generic value proposition; "Cambiar de [competidor] nunca fue tan fácil" vs "La mejor alternativa a [competidor]".
- Test landing page: competitor-comparison landing page vs main landing page.
- Test negative keywords to avoid low-intent queries.
- Test bid adjustments/quality score; maybe lower CPC by improving ad relevance.
- Could test search terms report; add negatives.

Need maybe produce "A/B tests specific to next month" with examples.

Need maybe note "no hagas demasiados test simultáneos; prioriza A/B test en A con mayor presupuesto para alcanzar significancia."

Need maybe compute current overall to identify issues:
- A gets only 29.6% of spend but 42.9% signups.
- B gets 25.4% spend, 22.9% signups.
- C gets 45.1% spend, 34.3% signups.
Could include.

Let's also compute "CVR" as signups/clicks. Sometimes "conversion rate" might be signups/impressions? But standard is clicks. We'll clarify.

Potential final answer outline in Spanish:

```
Ojo: el gasto reportado suma $7,100, no $5,000. Uso los datos para calcular; la recomendación es para un presupuesto de $5,000.

1. Métricas:
Tabla:
Campaña | CTR | CPC | CPA | Conv. Rate (clicks a signups)
A | 3.00% | $1.40 | $46.67 | 3.00%
B | 4.00% | $0.38 | $75.00 | 0.50%
C | 6.00% | $3.56 | $88.89 | 4.00%
```

Maybe include overall:
```
Total: CTR 3.89%, CPC $0.99, CPA $67.62, CVR 1.46%.
```

2. Escalar/pausar:
```
Escalar A: CPA $46.67, CVR 3%, mejor costo por signup. Pausar C como campaña de conversión directa: CPA $88.89, el más alto; consume $3,200 (45%) para 36 signups. B no la pausaría del todo si sirve como top-funnel, pero reduciría su peso: CPA $75 y CVR 0.5%. Si el objetivo es solo signups, el orden de eficiencia es A > B > C.
```
Need maybe "Pausar C" rather than B. But maybe "B" also should be paused? Let's think if "B" is blog content, might have low conversion but can contribute to retargeting. "Pausar C" maybe consuming too much. We'll phrase "si hay que pausar una: C, por peor CPA. B se puede mantener con presupuesto mínimo/retargeting."

3. Redistribución:
Option:
```
Manteniendo solo directa:
- A: $3,500 (70%) -> ~75 signups
- B: $1,500 (30%) -> ~20 signups
- C: $0
Total esperado: ~95 signups.
```
But that's if A can absorb. We need maybe include "si quieres mantener C por intención alta, baja a $1,000 y A $3,000, B $1,000; esperado ~89 signups." Could present as primary vs alternative.

Maybe do primary:
```
Recomendación principal (optimizando signups):
- A: $3,000-$3,500 (60-70%)
- B: $1,000-$1,500 (20-30%)
- C: $0-$1,000 (0-20%)
```
But user asks "Cómo redistribuiría el presupuesto de $5,000?" Need be precise.

Let's decide one distribution. Since they ask "cuál campaña pausar" we can pause C. Then redistribute $5,000 to A and B:
- A $3,500
- B $1,500
But is B getting too much? B's CPA $75 vs A's $46.67. If strict efficiency, more to A. Why allocate B $1,500? Could allocate A $4,000, B $1,000: expected signups 85.7 + 13.3 = 99.0. Actually that's even better. Wait if A can absorb $4k, expected 85.7 signups; B $1k -> 13.3; total 99.0. If all $5k A -> 107.1. But practical. Maybe allocate A $3,500, B $1,500 to maintain some top-funnel. But we can also allocate A $4,000, B $1,000.

Let's think about diminishing returns: A had $2,100; increasing to $4,000 nearly double. Could be possible if search volume. But if not, extra spend would be wasted or click costs may rise. We can say "asumiendo que hay volumen; si no, asigna el remanente a B."

Maybe better:
```
- A: $3,500 (70%) 
- B: $1,000 (20%)
- C: $500 (10%) → test/optimización
```
But if we pause C, no $500. Hmm.

Let's interpret "pausar" means completely stop. So maybe:
- A: $3,500-$4,000
- B: $1,000-$1,500
- C: $0
But they may want "pausar B" because blog content not converting. We need be confident.

Let's roll back to "Which campaign should I pause?" In PPC, with direct response, you'd pause B? Let's compare B vs C:
- B CPA $75, C PA $88.89.
- B CVR 0.5%, C CVR 4%.
- B CPC $0.38, C CPC $3.56.
- B CTR 4%, C CTR 6%.

Which is "better"? B has lower CPA, but very low conversion rate; it brings lots of cheap clicks but few signups. C has high CPA, but high conversion rate; if you can lower CPC, it can become best. However, as is, C is worse in CPA.

But there's another angle: budget. C consumed $3,200 = 64% more than A? Actually C cost $3,200, A $2,100. C produced 36 signups. If we pause C, we can move $3,200 to A and B, generating more signups at lower CPA. That seems likely recommendation.

Maybe user might expect "scale A because best CPA; pause B because lowest conversion rate?" Let's consider common PPC advice: 
- A main landing: CTR 3%, CVR 3%, CPA $46.67.
- B blog: CTR 4%, CVR 0.5%, CPA $75.
- C competitor: CTR 6%, CVR 4%, CPA $88.89.

If goal is signups, A is winner. C has best CVR but too expensive. B has cheap clicks but awful CVR. The worst CPA is C, not B. So pausing C makes numeric sense. But C is competitor; maybe maybe high intent. I'd phrase "si solo miras CPA, C es la que pausaría; B la dejaría limitada porque aporta tráfico barato y puede alimentar remarketing."

Let's maybe include a note: "Si B no tiene retargeting ni valor de marca, pausar B también es válido; en ese caso A $4,000, C $1,000 (mientras optimizas CPA)." But that may confuse.

Need maybe use "conversion rate" maybe signup rate. We'll define.

Let's maybe compute "CPA vs budget share" to show misallocation:
- A: 29.6% of spend -> 42.9% signups (positive)
- B: 25.4% spend -> 22.9% signups (slightly negative)
- C: 45.1% spend -> 34.3% signups (negative)
This strongly supports pausing C.

Need maybe suggest "incrementa A a $3,500, B $1,500, C $0" expected signups 95. But maybe if we pause C, we might lose competitor traffic. Maybe for next month test competitor campaign with lower budget.

Let's calculate expected signups for $3,500 A, $1,500 B:
- A $3,500 / $46.666 = 75 signups exactly.
- B $1,500 / $75 = 20 signups.
Total 95. 
Current if scaled to $5,000 at current overall CPA $67.62 = 73.94. So 95 is +28% vs current overall. But if comparing to current actual $7,100 105 signups, at $5,000 we get less but more efficient.

Could also propose "A $4,000, B $1,000" expected:
- A $4,000 / $46.67 = 85.71
- B $1,000 / $75 = 13.33
Total 99.05. This is higher expected signups. Why not choose this? Because maybe B has some awareness value; but if optimizing direct, allocate more to A. Let's consider if A can spend $4,000. It had 50k impressions and $2.1k. If double budget, maybe can get 95k impressions? Maybe possible. If limited by search volume, maybe not. We can say "si A tiene volumen, lleva $4,000; si no, el remanente a B."

Maybe final distribution:
```
- A: $4,000 (80%): principal, CPA más bajo.
- B: $1,000 (20%): tráfico barato, top-funnel/remarketing.
- C: $0 (pausada).
```
Expected signups ~99 (assuming A can absorb $4k). That's a simple 80/20. But is that too aggressive to scale A? We can note "validar cobertura de búsqueda; si no puedes gastar $4,000 en A, mueve a B."

Alternatively:
```
- A: $3,500 (70%)
- B: $1,500 (30%)
- C: $0
```
This gives B more budget for content; but direct signups less. Which one is more plausible for an account? A main landing is conversion; B blog content is top funnel. Since objective signups, maybe 70/30 is balanced. But the user asked "redistribuiría" not "maximizar exactamente". I can give ranges.

Let's maybe use "recomendación base: 70% A, 20% B, 10% C (solo si hay oportunidad de optimizar). Si pausas C, 70% A, 30% B."

Need maybe decide final answer. Let's craft with nuance:
- "Pausaría C por ahora (o bajaría a máximo 10% en modo prueba)."
- "Redistribución: A $3,500 (70%), B $1,500 (30%), C $0 (o $500 si quieres testear)."
But if "pausar" then $0 for C. Hm.

Let's maybe include "Mi recomendación: pausar C como conversión directa, no invertiría en C hasta que CPA < $60." This is solid.

Let's also maybe compute if C could be optimized: To achieve CPA $50 with CVR 4%, CPC must be $2.00. Currently $3.56. So need 44% reduction. Hard.

Need maybe mention "A tiene el CPC $1.40 y CVR 3% => CPA $46.67. Para C igualar eso, su CPC tendría que bajar a $1.87 (poco realista con pujas de competidor) o subir CVR a 7.6%."

Let's maybe compute: C current CVR 4%; to get CPA = A $46.67 with CPC $3.56, CVR needed = CPC/CPA = 3.56/46.67 = 7.63%. That's 91% relative improvement in CVR. Or lower CPC to $1.87. That's useful justification.

Similarly B: CVR 0.5%, CPC $0.38, CPA $75. To match A CPA, CVR needed 0.38/46.67 = 0.81%, still low but B could improve. Or CPC reduce to $0.23. Not necessary.

Need maybe construct final answer.

Let's ensure calculations:
Campaign B CTR: 4800 / 120000 = 0.04 exactly.
CPC: 1800 / 4800 = 0.375.
CPA: 1800 / 24 = 75.
CVR: 24 / 4800 = 0.005 = 0.5%.

Campaign C CTR: 900 / 15000 = 0.06.
CPC: 3200 / 900 = 3.5556.
CPA: 3200 / 36 = 88.8889.
CVR: 36 / 900 = 0.04.

Campaign A CVR: 45/1500=0.03.

Need maybe include "US$" values.

Potential A/B tests suggestions