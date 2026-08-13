# DeepSeek V4 Flash 0731 — sales_outreach/campaign_optimization

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 8.95 | quality: 10.0
- latency_total: 48.28s | tokens_per_second: 169.7
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

We need answer in Spanish. Need compute metrics. Need think thoroughly. We have campaigns A B C with numbers. Need calculate CTR, CPC, CPA, conversion rate. Then decide scale/pause with numbers. Redistribute $5000. A/B tests.

Let's parse data.

Campaign A (Landing principal):
Impressions 50,000
Clicks 1,500
Signups 45
Costo $2,100
Keywords "software gestion inventario", "inventario pymes"

CTR = clicks/impressions = 1,500 / 50,000 = 3.0%
CPC = cost/clicks = 2100/1500 = $1.40
CPA = cost/signups = 2100/45 = $46.67
CVR = signups/clicks = 45/1500 = 3.0%

Campaign B (Blog content):
Impr 120,000
Clicks 4,800
Signups 24
Costo $1,800
CTR = 4800/120000 = 4.0%
CPC = 1800/4800 = $0.375
CPA = 1800/24 = $75.00
CVR = 24/4800 = 0.5%

Campaign C (Competitor):
Impr 15,000
Clicks 900
Signups 36
Costo $3,200
CTR = 900/15,000 = 6.0%
CPC = 3200/900 = $3.555... ≈ $3.56
CPA = 3200/36 = $88.89
CVR = 36/900 = 4.0%

Need answer "Cual campana debo escalar y cual pausar? Justifica con numeros". We need consider CPA, conversion rate, intent, budget. Campaign A has lowest CPA $46.67 and good CVR 3%, CTR 3%, CPC $1.40. C has high CTR 6% and CVR 4%, but CPA $88.88 highest due CPC $3.56. B has low CPC but terrible CVR 0.5%, CPA $75, high impressions. If objective signups maximize, A is best per cost. C has highest CVR but high cost per conversion; maybe need optimize (landing page, ad relevance) not necessarily pause? "escalar/pausar" maybe C pause? But C has 36 signups, more than A, despite high CPA. If only objective signups with fixed budget, C's CPA high, so maybe reduce/pause if cannot improve. B has highest CPA among? Wait B CPA 75 vs C 88.89, so B actually lower CPA than C. But B is content targeting, high CTR low cost but poor conversion. Which to pause? Let's analyze.

Total current cost = 2100+1800+3200 = $7,100 > budget $5,000. So they overspent. If budget $5,000, need allocate. Existing signups: A 45, B24, C36 = 105. Cost 7100, blended CPA = 67.62. Current average.

Need "cual escalar y cual pausar" likely:
- Escalar A: best conversion rate (tied? C 4 vs A3), lowest CPA, efficient keywords high purchase intent. We can shift budget.
- Pasar? B: very high volume but CVR 0.5%, CPA $75 (not highest though). But C has worse CPA. Need justify. Which is more "pause"? Need decide.

Let's think about "Campana B (Blog content)" has keywords informational ("como gestionar inventario", "problemas inventario restaurante") likely blog. Low CPC but low conversion. It's not necessarily bad if leads in top of funnel? But "signups" are desired. If campaign objective is signups, CPA $75 and CVR 0.5%. C campaign has highest CTR/CVR but high cost due competitor keywords. Could be "non-brand competitor" high intent. It generates 36 signups at $88.89. Which to pause? If we pause C, total signups from A+B = 69 at cost 3900, CPA 56.52. If reduce budget to 5000, can scale A maybe.

Need compute marginal if we move budget. Need redistribution.

We need propose budget allocation with total 5000. Need base scale. For maximize signups with 5000, if A CPA 46.67, B 75, C 88.89, and no saturation, all budget in A yields 107.14 signups (5000/46.67), but unrealistic because A current spend $2100 gives 45. But if linear, "escalar A" with more budget same performance yields >100 signups. But current campaigns no exact marginal beyond. Need maybe allocate all to A? But need avoid assumption? We can give a reasoned distribution: A gets $3,000 (approx 64 signups), B gets $0 or small? Hmm.

Need answer "Como redistribuiria el presupuesto de $5,000?" We need allocate 5000 among campaigns. Need maybe include "prueba/reparto".

Let's evaluate campaigns by metrics thoroughly.

A:
CTR 3%, CVR 3%, CPA $46.67. Cost per click $1.40. Total cost $2100 for 1500 clicks (wtf 1500*1.4 =2100). Signups 45. Avg order.

B:
CTR 4%, CVR 0.5%, CPC $0.375, CPA $75. Cost $1800 for 4800 clicks; 24 signups. Cost per signup high because conversion rate very low. The low CPC doesn't compensate.

C:
CTR 6%, CPC $3.56, CVR 4%, CPA $88.89. This is most expensive but visible. It has the best click-through and conversion rate, but the keyword cost (competitor) is high. If you can lower CPC (e.g. exclude irrelevant, refine negatives, only brand+competitor with high intent), it can be valuable.

Potential "pausar" B because:
- CVR 0.5% means 99.5% clicks don't sign up.
- It consumes 71.4% of impressions but only 9.0? Wait 24/105 = 22.9% of signups.
- It costs 25% of spend? 1800/7100 =25.4% but gets 22.9% signups. Actually B is not too bad on signup share vs spend. Let's compare.

Share:
- Spend: A 29.6%, B 25.4%, C 45.1%.
- Signups: A 42.9%, B 22.9%, C 34.3%.
- A overindexes; C underindexes? C signup 34.3% vs spend 45.1, CPA high. B signup share under spend slightly too. So in cost allocation, both B and C inefficient relative to A.

Which is worse? B's CPA $75 vs C's $88.89. So C has highest CPA. But "pause B" because informational keywords not converting. But C highest cost and CPA; pause C? Need nuanced.

Let's examine "Cual campana debo escalar y cual pausar" singular "escalar" and "pausar" maybe one scale, one pause. Need maybe: escalar A, pausar B, y restructurar C. The phrase "cual pausar" maybe "campana C"? Let's infer.

- Campana A: Landing principal, keywords specific product, CPA lowest, convert rate 3%, cost per click reasonable. Definitely scale.

- Campana B (blog content): informational content. It has huge impressions 120k, cheap clicks 0.375, but signups 24, CPA 75. Since content traffic maybe early stage. Need "pausar" if campaign is only for signups; can run separately in brand funnel? But given a PPC account with signup goal, low conversion 0.5% is bad. However it has cost per click very low, so its CPA $75. Not terrible. If pause B, save $1800 and maybe lose 24 signups. If allocate to A, $1800/46.67 = 38.6 signups, a winner. So pause B.

- Campana C: competitor keywords. Highest CTR and CVR? CVR 4% is best, but CPC high, CPA high. It may represent a "high intent" segment. Should not pause entirely? Maybe "pausar" if only choose one, but because it has high conversion rate (4%), it could be "optimizar" not "pausar". Need mention "No pausarla definitivamente; reducir presupuesto y optimizar" maybe.

Which to pause? Let's evaluate if you pause C, all budget to A? Let's calculate possible signups per dollar:
A: 45/2100 = 0.0214286 signups per dollar.
B: 24/1800 = 0.013333.
C: 36/3200 = 0.01125.
A clearly best. C is actually worst per dollar. But C has 34.3% of signups at 45.1% spend, so if you reduce spending on C, lose signups per dollar slightly less than B. But if objective signups per budget, A all first; B second; C third. So "pause C" or "reduce C" (if need maximize signups, pausing C would move budget to A/B? Wait if C is worst per dollar, we'd pause C first, then B second if not enough budget? Let's think.

If objective maximize signups under 5000 and can spend any amount in each campaign with constant CPA, optimal allocation: all money to A, then B, then C with lowest CPA. Actually B has lower CPA than C, so "pause C" first; if not all to A? If all to A produces 107 signups, better than combination. But if saturation, allocate. But from current data, C CPA high, thus pause C and move budget to A/B. If you have only previous budget and no scaling constraints, all in A. But you might not want to put all in one campaign due to reach/scale. Need maintain diversification.

Need maybe allocate:
- A: $3,200 (64% budget)
- C: $1,800 (36% budget)
- B: $0? Hmm if we pause B because blog content doesn't convert. But C has worse CPA, so maybe B gets.

Let's see budgets constrained $5000. We have current costs 2100, 1800, 3200. Since total overspends, need reduce. We can propose:
- Escala A: new budget $3,500 (was 2,100). Expected at CPA 46.67: 75 signups (assuming linear). Keep 1,500 in C? Actually C would be about $1,500 => ~17 signups. But is C pause? Let's think.

Alternative:
- A: $3,000
- C: $1,500
- B: $500
Total $5,000. But B has $75 CPA, not good. Maybe use B as cheap awareness but not signup? Hmm.

Need optimize distribution. We can set constraints: No campaign more than X; maybe due to "escalar" not "all in A", need maintain experiments. Let's derive a distribution from metrics.

If you allocate all to A: 5000/46.67 = 107 signups. But due to diminishing returns? In PPC, scaling a campaign can increase spend by raising bids, potentially increasing clicks but possibly lower efficiency (due to broader auctions). Need suggest "incrementally" from 2100 to 3000-3500. Then use some budget for C tests. Need mention "asumiendo eficiencia constante".

Possible redistribution:
- A: $3,100 (increase from $2,100). Expected 66 signups.
- C: $1,200 (decrease from $3,200). Expected ~13.5 signups (but adjust).
- B: $700? No.

Maybe use formula for signups with budget $5000 and "put in A until account/campaign has enough volume; allocate C as test". Need server.

Let's think of "redistribuir" if "pause C" due to worst CPA: To maximize signups within budget, all to A. But maybe mention "dado que B y C have worse CPAs, pause both? But scaling A alone too risky. Use 70% A / 30% C? But need justify.

Maybe there is "Campaña C (Competidor)" with target "alternativa a [competidor]" and "[competidor] vs". That campaign has exactly 900 clicks and 36 signups, best conversion rate and CTR. But cost per click high. It could be "escalar" not pause? Let's examine efficiency: CPA=88.9, but if you can reduce cost per click or improve CVR, it can be good. But currently not more efficient than A. The question asks "Cual campana debo escalar y cual pausar?" Maybe answer should say "Escalar A, pausar B" because A has lowest CPA; "C" has high CTR/CVR but high CPA so optimize bids not pause? But if forced pause, C? Need be clear.

Let's read user phrase: "Tengo estos resultados de mi campana de Google Ads del ultimo mes:" 
Then asks:
"1. Calcula CTR, CPC, CPA, y conversion rate de cada campana
2. Cual campana debo escalar y cual pausar? Justifica con numeros
3. Como redistribuiria el presupuesto de $5,000?
4. Que A/B tests sugeririas para el proximo mes?"

This implies among three campaigns, one should be scaled, one paused. Need identify categories:
- Campaign A Landing principal, keywords "software gestion inventario", "inventario pymes": bottom-funnel, 45 signups, CPA $46.67. 
- Campaign B Blog content, informational queries: top-funnel, high CTR and traffic but poor signups. It is not a "sort" but blog content. 
- Campaign C Competitor: "alternativa a [competidor]", "[competidor] vs": high intent buyer comparison, highest CTR and conversion rate, but high CPC. 
If objective is signups, you "escalar A", "pausar B" because although B's CPC is low, conversion rate is terrible; C has high CPA but "competitor" campaign may be worthwhile if you optimize. Let's see "justifica con numeros": 
- A: CPA $47, CVR 3.0%; generates 45 signups with 2100. 
- B: CPA $75, CVR 0.5%, 120k impressions but only 24 signups. Need 150 clicks to get one signup vs A 33.3 clicks. 
- C: CPA $89, CVR 4.0%, high-intent but clicks too expensive. If pause C? But C best CVR and CTR. Hmm.

Maybe recommendation:
1. Escalar A: increase budget/investment. It has lowest CPA ($46.7) and solid conversion, so incremental budget should also be at comparable result.
2. Pausar B (as "campaña" for signups): despite high volume and cheap clicks, conversion is 0.5%, the worst of the three; 4,800 clicks -> only 24 signups; each signup costs $75. If this content is part of a funnel, leave it running separately with objective "engagement" not "signup"; do not allocate paid budget to it if you need signups.
3. C not necessarily pause? Actually "C" is expensive: CPA $88.9, highest of all. But CTR 6% and CVR 4% indicate the page/messaging is relevant. The problem is keyword CPC $3.56. Before pause, try reduce CPC with negative keywords, ad schedule/LSAs, better quality score. If after optimization still CPA>70, pause/reduce. But user says "cual pausar" singular. Could pause C because highest CPA. But if need choose between B and C, C has worse CPA. However B's low CVR indicates inefficient in purchase intent. Which is "peor"? Let's think "marginal cost" to get one more signup: B cost/increment. But if all campaigns, we need choose pause. Maybe we need use "sales funnel" insight: B is informative and not converting, so pause as "PPC signup"; C is high intent but high cost, so you can reduce/renegotiate keyword bids. 

Would it be better to pause B because B's budget could go to A yielding more signups with same cost:
- B cost $1,800 -> 24 signups. If those $1,800 spent in A, at CPA 46.7, you'd get ~38.6 signups. That's 60% more signups for same money. That's a very strong numeric justification.
- C's cost $3,200 -> 36 signups. If spent in A, you'd get ~68.6 signups. Even stronger. But C's CVR high. 
Actually if all budget $5000 in A, expected 107 signups. That's best. But "scaling A" maybe. Which one to pause? The one with highest opportunity cost relative to A. C has biggest absolute potential? Let's compare incremental loss:
- Moving B's 1800 to A gets +14.6 signups.
- Moving C's 3200 to A gets +32.6 signups. That's more signups. But C is bigger budget. 
But if you pause C, B still has $1800, budget total $5000? Let's propose allocation: all 5000 to A vs maybe A 5000. Pause C and B. But user asks one pause maybe because want optimize. "Campaña C" worse CPA but also C has best CVR and CTR. If you optimize by pausing B and putting that into A, you get 5000? Wait current budget $5000 (but spent 7100). Need perhaps answer "I would not keep B as a signup campaign. I would pause B; keep C only if reduce spend/cost, but its high ACA makes it a candidate for pause if it doesn't control CPC."

Let's need satisfy "cual campaña debo escalar y cual pausar" perhaps "escalar: A, pausar B" with nuance "no pause C but reduce and reoptimize". But also, "Qué A/B tests sugeririas" Need ask tests:
- Landing page variants for A (headline, CTA, form length, social proof, price demonstration), because A has 3% CVR; can improve to lower CPA.
- Ads/Broad vs exact match? Compare "software inventario pymes" vs "sistema gestión de inventario" in A.
- C: Test landing pages specifically for comparison/competitor queries; maybe a comparison page with "alternativa al competidor" and matrix; test ad copy with price/differentiator unique; test negative keyword lists.
- B: Test lead magnets (e.g. downloadable guide, checklist, case study) or signup goal? If signup objective, test CTA on blog; perhaps use email gateway? 
- Also test audience/segments and devices; use "responsive search ads" etc.
- Bid optimization: Test tCPA vs Maximize Conversions in A and C. Need mention prior.

Need ensure calculations. Let's craft comprehensive.

Let's calculate exact:
Campana A:
CTR = (1500 / 50000) x 100 = 3%
CPC = 2100 / 1500 = $1.40
CVR = (45 / 1500) x 100 = 3%
CPA = 2100 / 45 = $46.6666667 -> $46.67

Campana B:
CTR = (4800 / 120000) x 100 = 4%
CPC = 1800 / 4800 = $0.375
CVR = (24 / 4800) x 100 = 0.5%
CPA = 1800 / 24 = $75

Campana C:
CTR = (900 / 15000) x 100 = 6%
CPC = 3200 / 900 = $3.5556 -> $3.56
CVR = (36 / 900) x 100 = 4%
CPA = 3200 / 36 = $88.8889 -> $88.89

Maybe include table.

Then "escale/pause" in more detail:
Best CPA A -> B -> C by thresholds. But the CVR B 0.5% means the cheapest clicks but weak page/message. The blog campaign is not efficient for signups. If goal is signups, shift budget from B to A and C? Wait current objective:
- If prioritize "lowest CPA", A first, B second, C third? Let's order:
A: CVR 3%, CPA 47, CPC 1.4
C: CVR 4%, CPA 89, CPC 3.56
B: CVR .5%, CPA 75, CPC .375
Actually CVR C best, but B has lower CPA. Which is better? If there is no willingness to pay>threshold, C has CPA 89 vs B 75. So B better. 
But if also "if can improve C" because C has high CVR and use fewer clicks to sign up. If the problem is CPC cost, because C has high CVR but high CPC. What is more "escalable"? A and C have high CVR; B has low. "Escalaria A", "pausaria B" because B is the only campaign with unacceptable conversion from clicks. But C has poor CPA despite high signup rate; not necessarily pause? Need mention "C's CPA is highest, but it has the highest conversion rate; if I could lower C's CPC via Quality Score/bid, it could be very useful. However if you only have $5000 and need fastest ROI, put no/less budget in C until lower CPA."

Maybe from a data-driven "opportunity cost" approach:

A:
- Cost per signup $47.
- "Marginal ROI": $47.
B:
- CPA $75 < A? no. 
C:
- CPA $89.

If minimizing CPA, order A > B > C. Therefore, if you have to pause one, pause C, not B. But B has terrible conversion, but its low CPC gives it acceptable-ish CPA. Yet pause B? Let's not jump.

Let's think of "presupuesto total $5,000/mes." They currently spent $7,100; need cut. If they pause C? Then budget can be spent on A/B maybe lower A/B to fit. But current A+B=3,900 under 5000. Could increase A by 1,100. If B still spends 1800, A 3200 maybe. That seems reasonable.
- If pause C: allocated A $3,200, B $1,800 (or maybe shift B off to A?).
- If pause B: allocate A $2,100? C $3,200 under 5,300? Need reduce C. Or A+C = 5,300 >5000. Need reduce C to 2900 if maintain A. That yields (A 45+B? no B; C reduced) 45 + 32.6? wait 2900/88.9 = 32.6 signups, total 77.6. More signups than pause C? If pause C: A 2100 gives 45, B 1800 gives 24 = 69; new budget add 1100 to A gives 23.57 => 92.6? Let's compute if pause C and allocate A 3200, B 1800: A signups 3200/46.7=68.6 + B 24 = 92.6. If pause B and allocate A 2100, C 2900: A 45 + C 32.6 = 77.6. If pausing C yields more signups because A better. But maybe if scale A no C? Good.

But an expert would not "pause C" if competitor strategy valuable? However the CPA is highest. If you need get leads and know account: C spend $3200 to get 36, but A with $3200 gives 68.6 signups. Pausing C and moving budget to A can improve signups. But C's conversion rate 4% means page works; just too expensive. Should reduce bid, not pause. Hmm.

Maybe there is "Campana B (Blog content)" and "Campana C (Competidor)": The names "B blog content" likely not transactional, but "signups" maybe newsletter. Competitor ads maybe comparison page and likely high quality. Blog posts content often cheap clicks but low conversion; if objective signups, "content" campaigns can still attract leads. Need ab test maybe "en B" use "lead magnet" not direct signup, etc. But not always pause.

Let's read specific request: "Tengo estos resultados de mi campana de Google Ads del ultimo mes:" then campaigns. They ask "Cual campana debo escalar y cual pausar? Justifica con numeros". It implies maybe campaigns: "A (landing principal), B(blog content), C(competitor)". They want "one to scale, one to pause" because budget. I can answer nuanced: "Escalar A; pausar B como campaña enfocada en signups (not necessarily inactive if content strategy); ajustar/renegociar C." But if need "cual pausar", choose B? Let's decide.

Let's use ROI "Signups per dollar":
- A: 45 / 2100 = 2.14% signups per dollar (i.e., 21.4 signups per 1000?). Actually 45 signups/2,100 = 0.0214
- B: 24 / 1800 = 13 signups per 1000? 0.0133, so 62% of A? 
- C: 36 / 3200 = 0.01125, 53% of A.
B has better signup per dollar than C. Thus "pause C" if stopping by efficiency? But B's CVR 0.5 is bad but "cheap clicks cause it to be decent vs C; but to maximize using budget, C pause." However if C's high click costs are because competitor terms, perhaps still "strategic" not current efficiency. The "which campaign should pause" maybe because one has worst CPA? C. But would a company want "campana competitor" paused despite 36 signups? If budget is scarce, yes if they want more signups per dollar.

Let's calculate "cost per click" C is 2.5x A and 9.5x B. That inflates CPA. But C has CVR 4% vs A 3%, so CPA is high due to CPC. If C's CPC can be lowered to say 2.00 maybe CPA = 2/0.04 = $50. Improvement through ad relevance, quality score. So not necessarily pause.

Maybe answer "No pausar C, sino ajustarla; pausar B." Need align with data:
- B is a "blog content" campaign; it uses generic informational queries. The conversion rate 0.5% shows poor purchase intent. 
- C, even with high CTS/ CTR, is the only one with 4% conversion rate; if we improve CPC (bids/quality score), it can become profitable. But pausing C would kill one clear "high-intent" channel. 
- A is best: lowest CPA and a solid combination.

But "cual pausar" then B. Need justify numbers: B takes 4,800 clicks vs A's 1,500 and only yields 24 signups vs 45; it has a conversion rate 6x lower than A/C (0.5% vs 3/4%), and in fact B's total clicks are 3.2x more than A yet produce 42% fewer conversions. Even if click is cheap, signup is $75 (51% more expensive than A). With the same $1,800 invested in A at A's CPA, you'd get ~39 signups vs 24. So pause B if objective is signups.

If C is CPA $89, should we pause? We can say "C no se debe pausar todavía, pero hay que redesifarla: reduce bids and rebuild with exact match/negatives to lower CPC; if after 2-3 weeks its CPA remains >$75, pause it because is worst in efficiency. But note in "escalar/pausar" not enough. Hmm.

Maybe maybe the user specifically expected "escalate C, pause B"? Let's think of campaign names:
A landing principal: lower CTR 3%, clicks 1500, signups 45, cost 2100. CPA 46.67.
B blog content: high impressions 120k, clicks 4800, signups 24, cost 1800. CTR 4%, CPC .38, CVR .5, CPA75.
C competitor: low impressions 15k, clicks 900, signups 36, cost 3200. CTR 6%, CPC 3.56, CVR 4, CPA 88.89.
If the business is a SaaS inventory software, competitor keywords "alternativa vs" often convert at high rate if marketplace. But C has conversion rate 4% and click-to-signup. C is "converted lovers" but expensive. B blog clicks are cheap but low quality. A has good overall.

Which campaign to scale? Should we scale "C" because CVR 4% > A, but CPA high due high CPC. If we can lower C CPC by optimizing quality score? But current cost per click false. The average order value not provided. If LTV high (e.g. $300), CPA $89 might be profitable; C may be best to scale because it has 4% conversion, high intent; scale C and optimize "Cost / click" or "bids" lower. But "escalar" means more budget; if you increase budget, Google complexity? Hmm.

Let's evaluate "which campaign should I scale?": Common heuristic with GoogleAds: campaigns with best conversion rate and CPA below target should be scaled. If CPA C is higher than target, cannot scale. But if no target, lowest CPA is A. Unless desired by "more clicks" not quality. Need not.

Need maybe incorporate "No A/B tests" with redistribution. The objective likely "signups." If no sign-up value provided, assume "more signups per dollar" is best. Then A.

Let's propose a redistribution table. Need total exactly $5,000 and expected conversions. Let's choose a pragmatic "budget redistribution": 
- A: $3,200 (was $2,100). 
- C: $1,200 (reduced from $3,200) — only if C can continue functioning at this level; need adjust bids.
- B: $600 (or $0) - maybe not needed. 
Wait if B paused, no. Need total 5000.

If we say "pause B" and "resлава A, adjust C", then budget:
- A: $3,500 (70%)
- C: $1,500 (30%)
- B: $0 (paused)
This is simple. Expected signups:
A: 3500 / 46.67 = 75.0 (if linear)
C: 1500 / 88.89 = 16.9
Total: 91.9 signups. That's > current 105? It's less because current spend 7100 has 105. If budget is 5000, cannot expect 105. Current? If current spend $7100 gives 105 signups; with $5000 all to A gives 107; with A3500 C1500 gives 92. But a distribution that maximizes expected signups with current data would be all to A: 107. If only A/C at roughly same? Let's calculate optimal ignoring diminishing returns:
- All $5000 to A yields 107.1. A $4000 C $1000 => 85.7 + 11.3 = 97.0. So all A is best. But "spread risk" means maybe A $4200 and C $800: 90 + 9 =99? Wait A $4200/46.67=90, C800/88.9=9 =>99. Actually all A 107. If want small declining? Hmm. Since CPA A low, higher share to A. But a 100% allocation to one campaign is aggressive. Need maybe say "si no hay efecto de descuento, en teoría iría el 100% a A. Pero en la práctica no lo hago por saturación; recomiendo A 70% (3,500) and C 30% (1,500) while running tests. Once A reaches its search limit/increases CPA, feed C." That balances.

Need maybe include "expected signups" with this distribution and note linear assumption. But do we need? User asked "Como redistribuiria el presupuesto"; not necessarily expected. We can include. Need be transparent: "Asumiendo eficiencias similares, con A 3500/C1500 esperarías ~75 de A y ~17 de C = 92; sin distribución all-A would be 107, so I only distribute to avoid satuting A and keep test data." That's a thoughtful answer.

But if we want to "pause B" and "optimize C" okay.

Let's consider if "C should pause" maybe our budget distribution should be:
- Pause C, A $3,200, B $1,800. But in the previous we said scale A, pause B. Contradiction.

Which campaign to pause in final? Let's decide.

Let's think what an expert would do with these data:
1. KPIs: Use sum(actual sign-ups) / total spend:
   - A: SPA = 21.4 signups / 1000? Actually signups per $k = 21.4. B = 13.3, C = 11.3. 
So A best. If the loss is profitable, demand high. Use signup as conversion; no revenue per signup. So allocate as much as possible to A. B and C have CPAs ~1.6x and 1.9x A. You don't "pause C" if it converts at 4%? yes.
But if "compare to A" opportunity cost:
- Pausing B loses 24 sign ups, but reallocating B+additional? Hmm.
- Pausing C loses 36 signups; but reallocating to A grows more.
If budget under constant, "scale A" and "pause C" because C has highest CPA. But what about B? It is not terrible? If we had to pause one, pause C. But in terms of "signups per signup" C has 36 vs 45. B has 24. If pause C and use budget elsewhere, signups increase. 
However "Campana C" name "Competitor" with high-value keyword shows best conversion rate 4% "clicks to signups" as compared to A 3%; might be expected to "escalar" because it converts best when clicked. But CPA is high because competitor keywords expensive. Usually "competitor campaigns" have high CPA but are "conquesting"; maybe should not be judged by direct conversion due to better leads? Here not.

Let's parse "Campaña C (Competidor): Impresiones: 15,000 | Clicks: 900 | Signups: 36 | Costo: $3,200 | Keywords: "alternativa a [competidor]", "[competidor] vs"." 
This campaign has high cost, high signups. It may have 36 signups. Many marketers might think "CVR 4%, best conversion rate; scale C." However pay $88 per signup vs A $47. Could "escalar C" if "competitor" clients have higher LTV? But no LTV info. We cannot without margin. We can mention if LTV is significantly > $89 (e.g., >2x payback), C could be valuable. But asked "cual debo escalar/pausar?" Could rather "with data, A, but C not necessarily pausar if its LTV justifies." Maybe (2) answer nuanced: "Funding order: A > C > B? Wait CPA order A<C? Actually B<C, but CVR C better. The final is A. Pause B. Keep C only if you can lower bid/CPC and it hits CPA target."

Let's inspect maybe "CPA" of C 88.89 vs B 75. If C is worse, why not pause C? Because "C has best conversion rate 4% and CTR 6% (search quality good) but high cost per click is because competitor names. If you optimize C's keyword match, negatives, and ad copy to boost quality score, you likely can lower CPC and unlock a high-intent channel. It already has twice the conversion rate of B and 1.3x of A. If you pause C, you're losing qualified buyers to competitor searches, but if you