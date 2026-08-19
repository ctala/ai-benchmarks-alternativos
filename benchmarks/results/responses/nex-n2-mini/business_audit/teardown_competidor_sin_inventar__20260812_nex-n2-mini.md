# Nex-N2-Mini — business_audit/teardown_competidor_sin_inventar

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 3.46 | quality: 2.0
- latency_total: 43.655s | tokens_per_second: 187.7
- input_tokens: 192 | output_tokens: 8192

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista competitivo. Distingues SIEMPRE entre lo que sabes y lo que estás infiriendo, y marcas tu nivel de certeza.

**user:**

Hazme un teardown de un competidor. Esto es TODO lo que pude ver desde fuera (su página pública):

- Comunidad de pago sobre automatización, en una plataforma tipo membresía.
- Muestra '2.400 miembros' en la portada.
- Precio visible: $39/mes. No se ve si hay plan anual ni descuentos.
- Publican 3 posts por semana en el feed público.
- El fundador tiene 60.000 seguidores en una red social.
- Tienen 12 cursos listados, no se ve cuántos están terminados.

Quiero saber cuánto factura, qué tan sano es el negocio y cómo les compito.


## Respuesta completa


We need answer Spanish. User asks competitive teardown based on public info. Need distinguish know vs infer and certainty. Need estimate revenue, health, how to compete. Need probably provide methodology, assumptions, sensitivity, maybe formula. Need not claim exact. Need maybe calculate.

We have data: paid community automation, membership platform. 2,400 members shown on homepage. Price visible $39/mo, no annual/discounts. Public posts 3/week. Founder has 60k followers on social. 12 courses listed, unknown completed. Need estimate revenue, business health, competitive strategy.

Need maybe calculate gross revenue: 2400*39=93,600/mo gross. Annualized 1.123M if stable. But membership "members" may include active paid? likely. Need subtract payment fees 3-5%, platform fees maybe 0-10%, content delivery, ops, taxes. Net before founder salary maybe 65-80k/mo? Need assumptions. Churn matters. If 2400 are active members, MRR ~$94k. With annual plan equivalent maybe if annual discount 10-20%, effective MRR lower/higher? Annual upfront affects cash not revenue. If no annual, churn high could be okay. Need maybe calculate customer count: 2400 at $39 = 93.6k. If 15-30% churn monthly? For community maybe 5-15%. Need discuss LTV. CAC? Founder social lowers CAC. Courses increase ARPU maybe if paid add-ons.

Need "cómo les compito": avoid direct war. Differentiated positioning. Offer segments, outcomes, niche, superior delivery, lower risk, community. Could target underserved subsegment, verticalize automation, implementation, templates, done-for-you, accountability, AI agents, Zapier/Make. Provide examples: "automatización para estudios contables" vs generic automation. Pricing: freemium lead, $49-79? annual, cohort, high-ticket implementation. Need compare.

Need maybe produce teardown structure:
- Snapshot: public facts table with certainty.
- Revenue model and estimates:
  1) Base case: 2,400 active paid members; $39 monthly; MRR = $93.6k; ARR = $1.12M.
  2) Conservative: 1,800 active (maybe 75% of displayed due to inactive/free? but if displayed likely active), MRR $70.2k; ARR $842k.
  3) Upside: 2,400 active + annual plan effective 33/mo (15% discount) = $79.2k; or 2,600? But no. If active members are 2400 and annual plan effective 33/mo, MRR 79k. If add courses/upsells maybe ARPU +10-25%. Need maybe estimate total revenue including course upsells: If 5-15% buy annual or course? 12 courses listed. Without pricing unknown. Could add $5-20k/mo equivalent if conversion. Need maybe not overdo.
  4) Best/realistic: 2,400 active paid + 10% annual at 20% discount + 10% course upsell ARPU? MRR 90k plus course revenue 5-15k.

Need calculate contribution:
- Gross revenue $93.6k/mo.
- Payment fees (Stripe/PayPal) ~2.9%+0.30 maybe $3k; platform $2-8k; community tool $1-5k; hosting/content $1-3k; support/moderation maybe $2-8k; ads maybe unknown; contractor/partner. EBITDA before founder salary maybe 40-65%? But membership can be high margin if founder uses own social. Maybe net profit $35-60k/mo if lean, $15-35k if heavy. Need state.
- If founder salary included, unknown. If he pulls salary, maybe profit lower.

Need health:
- Signals good:
  - 2,400 members at $39 = $94k MRR; enough to support lean team.
  - Founder 60k followers reduces acquisition cost.
  - 3 posts/week indicates ongoing content engine.
  - 12 courses = monetization breadth.
- Risk:
  - Generic "automatización" crowded; differentiation unclear.
  - 2400 displayed may include inactive/free; need verify.
  - Churn unknown; membership health depends retention.
  - Platform lock-in and commoditization.
  - Founder dependency (audience + delivery).
  - Course completion unknown; "12 courses" can signal breadth but also unfinished pipeline.
  - No annual plan visible; monthly churn risk/cashflow.
  - Community engagement unknown.
- Health score maybe 6.5/10 or 7/10 if active paid and low CAC; 5/10 if churn high/generic. Need maybe "business health: likely healthy but not obviously defensible." Need maybe use metrics.

Need maybe "what I can know vs infer" explicitly.

Need maybe "teardown" includes:
1. Positioning:
   - They sell "automation community" to makers/founders/freelancers? They have 12 courses. Position likely breadth and convenience.
   - Weakness: not outcome-specific; no visible case studies; no clear ICP; no proof of results.
2. Product architecture:
   - Membership + courses + maybe community.
   - Value prop: learn automation + network.
   - Monetization: recurring $39 + possible upsells.
3. Growth:
   - Founder-led distribution via 60k followers; 3 posts/week public feed; maybe no paid ads.
   - Conversion funnel: follower -> public content -> community -> courses/upsells.
   - Growth bottleneck: founder attention and content cadence; conversion rate unknown.
4. Economics:
   - MRR formula.
   - CAC likely low if organic; if paid ads then unknown.
   - LTV: MRR / monthly churn. If churn 5%, LTV before fees = $780; gross margin 70%; LTV $546. If churn 10%, LTV $390; gross margin 70%; LTV $273. If churn 15%, LTV $260; LTV $182. This helps assess CAC.
   - Need maybe estimate break-even CAC: at $39, if 70% gross margin, $27.3/mo contribution; at 12mo average tenure = $328. If churn 10%, expected tenure 10 mo; contribution $273. Thus paid acquisition only viable if CAC < $150-250; organic can be huge.
   - Annual plans can improve retention/cashflow; no visible annual maybe missed optimization.
5. Competitive gaps:
   - They have social proof and catalog, but not clear specialization, outcomes, cohort accountability, implementation support, templates, vertical focus.
6. How to compete:
   - Don't match $39 generic. Choose wedge:
     a) niche vertical (e.g., automation for Shopify stores, agencies, SaaS support, consultants).
     b) outcome guarantee (save 10 hours/week in 30 days).
     c) implementation/community with templates and audits.
     d) certification/curriculum with portfolio projects.
     e) high-touch tier $149-299/mo or $2k-5k implementation.
     f) annual plan and guarantee.
   - Pricing strategy:
     - Entry: free weekly automation teardown or $19 starter.
     - Core: $49-$79/mo for niche.
     - Pro: $149-$299/mo with audits/office hours.
     - Annual discount 15-20%.
   - Content strategy:
     - 5-7 posts/week? More targeted.
     - Build "proof flywheel": before/after automations, teardown, case studies, ROI calculators.
     - SEO/YouTube/LinkedIn, not just feed.
   - Product differentiation:
     - Templates, prompts, no-code stack, integrations, compliance/security.
     - Accountability cohorts, expert Q&A, office hours.
     - "Done-with-you" implementation.
   - Conversion:
     - Landing pages by use case; free audit; webinar; challenge.
     - Compare with them: "If you're tired of generic automation tips, here's vertical automation for X."
   - Moats:
     - proprietary templates, case studies, community network, data on automations, certification.

Need maybe provide "ask for more data" maybe "If you can see X/Y/Z, I can refine." But final should answer. Need maybe include caveat: no browsing; based only on info. Need maybe "2.400 miembros" could be total members not active paid; "2.400 miembros" usually on membership platforms may show count of members, likely paid? But if public, maybe active. Need mark.

Need maybe "factura" in Spanish: monthly recurring revenue (MRR), ARR. Maybe "si esos 2.400 son miembros activos y pagados": MRR 93,600 USD. "Si algunos son trial/free/inactive", lower.

Need maybe "salud" with score. Need maybe "competir" with specific matrix.

Need maybe "what they may be doing":
- Founder 60k followers, 3 posts/week = 12 posts/month. If 1% follower sees? Need not.
- If conversion from followers to paid is 0.5-2%, they can add 300-1,200 members over time. But if 2,400 members, not necessarily all from founder.
- Course catalog 12, maybe "evergreen content" monetization.

Need maybe include "red flags":
- No visible annual plan/discounts: may imply they don't optimize retention; but many hide plan details.
- No visible results/case studies in visible data.
- 12 courses not completed: possible content debt; could be a pipeline.
- "Automatización" broad category: crowded, commoditized.
- No visible pricing transparency beyond $39; maybe checkout hidden.
- Community platform maybe not own IP; churn risk.

Need maybe "teardown of competitor" maybe need use "conocido vs inferencia". We'll make table.

Need maybe "revenue ranges" with assumptions:
- Assumption A: 2,400 paid active. MRR = $93,600. Annualized revenue = $1,123,200.
- Adjust for annual plan if hidden: if 20% of members annual at 15% discount, blended MRR = 80%*39 + 20%*33.15 = $37.83; MRR = $90,792; ARR = $1.089M. If 50% annual = $84,240.
- Add courses/upsells: unknown. If 10% of members buy $199 course quarterly? Let's calculate: 240 members*199*4/year=190,080/yr=15.9k/mo; but maybe too high. If 5% buy $299/year = $35,880/yr=3k/mo. If 10% buy $299/year = $71,760/yr=6k/mo. We can include "course add-on plausible $2-15k/mo equivalent if conversion/pricing high; not enough to change order of magnitude unless high-ticket."
- If "members" includes free/trial: If 50% paid = $46.8k MRR; if 25% paid = $23.4k. But membership public "paid community" likely mostly paid.

Need maybe "health score" maybe:
- Financial health: 7/10.
- Growth health: 6/10 (good founder distribution; content cadence; no proof of paid acquisition).
- Product health: 5.5/10 (community+courses but no evidence of completion/engagement).
- Defensibility: 5/10 (generic, founder-dependent).
- Overall: 6.5/10.
Need perhaps not too many numbers.

Need maybe "how to compete" with "attack plan":
1. Pick a beachhead where their generic community is weak.
2. Build offer ladder:
   - Free: automation teardown newsletter + templates.
   - Low-ticket: $19-29/mo resource library.
   - Core: $59-99/mo niche community.
   - Pro: $199-499/mo implementation/accountability.
   - High-ticket: $2k-10k projects.
3. Content:
   - "10 automations que ahorran 20h/semana a [niche]"
   - "Case studies with exact tools and ROI"
   - "Build in public automations"
4. Sales:
   - Use founder's audience and lead magnet.
   - Run monthly challenge "automatiza tu negocio en 7 días".
   - Free diagnostic.
5. Retention:
   - Monthly outcomes, office hours, templates, accountability, user-generated wins, certification.
   - Annual plan with 2 months free.
6. Differentiation:
   - "No más teoría: implementamos tu primera automatización en 14 días."
   - "Especialistas en [vertical]."
   - "Garantía: si no ahorras X horas, cancelas."
7. Avoid:
   - Competing head-to-head on "automation community" with $39.
   - Copying 12 courses; instead fewer high-quality modules tied to use cases.
   - Overpromising.

Need maybe "questions to validate":
- Are members active paid?
- Churn/retention.
- Conversion from followers.
- Course prices/completion.
- Engagement (DAU/WAU, posts/comments).
- Referral sources.
- Tools stack.
- Case studies/testimonials.
- Annual plan.
- Support time.

Need maybe "if I had to bet" conclusion:
- Likely $80k-$100k MRR; $1M ARR; healthy enough to be a serious competitor.
- Not necessarily highly defensible; founder-led, broad category, membership churn risk.
- You can compete by niche, outcomes, implementation, proof, retention, and higher ARPU.

Need maybe maybe mention "factura" not "profit". "Facturación bruta" vs "neto". Need define "MRR" maybe "ingresos recurrentes mensuales".

Need maybe "no se ve si hay plan anual" - if hidden in checkout, still likely. Need say.

Need maybe "public posts 3/week" maybe indicates content engine but not necessarily acquisition. Need maybe "3 posts/week = 12/month; if feed public, they are likely using content to sustain top-of-funnel, but conversion unknown."

Need maybe "founder has 60k followers" - could be on LinkedIn/Twitter/X/Instagram. If high-quality B2B maybe more valuable. Need maybe "if 1-3% follow from public content convert to community, they can add 600-1,800 members over time; if follower quality low, less." Hmm maybe.

Need maybe "12 courses listed, no se ve cuántos terminados" - Could be "course library" not necessarily active; if many unfinished, could hurt perceived quality. Need mention.

Need maybe "competitor teardown" maybe include "strategic map":
- Their current likely moat: distribution (founder) + catalog + community social proof.
- Their likely weak moat: content library generic.
- Their likely bottleneck: retention and content production.
- Your opportunity: own a use case + proof.

Need maybe "scorecard" with table:
Criterion | What public data says | What it implies | Certainty
- MRR | 2,400 x $39 | $93.6k MRR if active paid | High
- ARR | MRR*12 | $1.12M ARR | Medium/High if stable
- Margins | recurring low COGS | likely 50-70% contribution before salaries | Medium
- CAC | founder 60k + posts | likely low CAC | Medium
- Product breadth | 12 courses | broad library, possible upsells | High/Medium
- Retention | unknown | unknown; health depends | Low
- Differentiation | generic | crowded | Medium
- Distribution | founder-led | scalable? founder dependency | Medium.

Need maybe "sensitivity table":
Scenario | Active paid members | Blended price | MRR | ARR | Comment
- Conservative: 1,500 / $39 = $58.5k / $702k.
- Base: 2,400 / $39 = $93.6k / $1.12M.
- Base with annual discount 20%: 2,400 / $33 = $79.2k / $950k.
- Base with course upsell: $93.6k + $5k-$15k = $98.6k-$108.6k / $1.18M-$1.30M.
Need maybe not too many.

Need maybe "net profit estimate":
- If lean:
  - Revenue 93.6k
  - Payment fees (3%): -2.8k
  - platform/community tool (3k-10k)
  - contractors/hosts/editors (5k-20k)
  - software/tools (1k-5k)
  - marketing (0-20k)
  - Profit before tax/founder salary: maybe 35k-65k (35-70%).
- If team-heavy: 15k-35k.
Need maybe mark "inferencia, not known."

Need maybe "business health":
- "Healthy enough to be taken seriously, but not necessarily 'great'." 
- "If churn is 5-8%, this is a strong business; if churn 15-25%, it's a treadmill."
- "At $39, monthly churn must be low or CAC must be near zero."
- "Need know active members, not just displayed."

Need maybe "How to compete":
Detailed plan:
- "No compitas por 'más automatizaciones'; compite por 'resultado en [segmento]'."
- Example positioning statements:
  - Competitor: "Aprende automatización con una comunidad de expertos."
  - You: "Implementamos automatizaciones listas para [contadores/consultores/ecommerce] que ahorran [X horas/semana] sin contratar devs."
- Pricing:
  - "Starter $29/mo resource library"
  - "Core $59/mo community + monthly templates"
  - "Pro $149/mo office hours/audit"
  - "Enterprise/project $2k-$5k"
- "Beachhead niches":
  - Agencies using Make/Zapier to onboard clients
  - SaaS customer support
  - E-commerce ops
  - Real estate agents
  - Consultants/freelancers
  - Solopreneurs
- "Offer":
  - 30-day implementation challenge.
  - Guarantee.
  - Templates.
  - Case studies.
  - "Automate your workflow" diagnostic.
- "Content":
  - Weekly teardown of public automations.
  - Build in public.
  - ROI calculators.
  - Comparison posts: "Zapier vs Make vs n8n" maybe but not just.
- "Acquisition":
  - Use founder's 60k? Wait user's founder maybe not. We can say "tu fundador/empresa".
  - "Repurpose case studies across LinkedIn, X, YouTube Shorts, newsletter."
  - "Partner with tools/agencies."
- "Retention":
  - "Onboarding, success paths, office hours, templates, wins, certifications."
  - "Annual plan, community events, accountability."
- "Pricing strategy vs $39":
  - "Don't undercut below $39; it trains buyers to value low. Either match at $39 with better niche or premium with proof. I recommend $49-79 core for niche and $149-299 pro."
- "Moats":
  - "Case studies, templates, implementation know-how, niche network, certifications."

Need maybe "scorecard to beat them":
- MRR: if you can reach 1,000 paid at $59 = $59k MRR; 1,500 at $79 = $118.5k.
- Breakpoints:
  - To match their $93.6k MRR: 1,500 at $62.40; 1,200 at $78; 800 at $117.
  - At $149 pro: 628 members.
This is useful. Need include maybe.

Need maybe "What to monitor":
- Member count changes, pricing, annual plan, launch new course, engagement comments, testimonials, founder posts, job postings, tech stack, reviews.
- "Signals of churn": less community activity, old posts, fewer testimonials, lower posting frequency.
- "Signals of growth": member count increase, case studies, cohorts, paid ads, affiliate program.

Need maybe "certainty levels":
- "Alta: math if assumptions hold; 2,400 and $39 visible."
- "Media: active paid membership, revenue health."
- "Baja: churn, CAC, profit, completion, conversion."
Need maybe include.

Need maybe "No exact revenue possible from public info; exact would require membership platform data." Good.

Need maybe "teardown" maybe maybe "MVP competitor profile":
- "They are a founder-led media/membership business, not a software company."
- "Their business model is likely content -> community -> courses -> upsells."
- "Their key metric is retention, not just members."
- "Their main bottleneck is content production and community quality."

Need maybe "health of business" maybe "sane" Spanish: "¿qué tan sano es?" We'll say "salud: alta si active paid and churn <10%; otherwise moderate." Need maybe "health score 6.5/10." Could be "6.5/10 sin datos de churn." Need maybe "They look financially healthy but strategically vulnerable."

Need maybe "No se ve si hay plan anual ni descuentos." We can estimate:
- If no annual: churn risk; if hidden annual with 10-20% discount, MRR lower but retention better.
- "No visible annual plan" can be a weakness in their model (less predictable ARR, higher monthly churn) and an opportunity for us (offer annual).
Need maybe "No se ve si hay descuentos" maybe "many hide in checkout; not enough to infer."

Need maybe "public posts 3/week" maybe "not a lot but enough; if they have 60k followers, 12 posts/month can maintain top-of-funnel; if feed public posts are evergreen, maybe content library."

Need maybe "12 courses listed, no se ve cuántos terminados" maybe "catalog breadth can be used as social proof; but if many incomplete, product quality may suffer."

Need maybe "founder 60k followers" maybe "distribution moat; but founder dependency is also risk; if he leaves, business may lose 60% of funnel."

Need maybe "How to compete" maybe "attack the weak points":
- Generic broad category: niche down.
- Founder-led: build brand/team not dependent solely on founder.
- Courses not completed: produce fewer, deeper, outcome-based modules.
- Monthly pricing: annual/commitment.
- Community engagement unknown: show engagement and outcomes.

Need maybe "final answer overwordiness medium" moderate but thorough. Need not ask clarifying questions; answer directly.

Need maybe include "I can't browse" not necessary but maybe "Con la info que diste". We are API no browsing. Need maybe "No puedo ver su checkout". But user knows.

Need maybe "competitor teardown" maybe in Spanish.

Let's craft final. Need no analysis. We'll produce in Spanish with headings.

Need ensure "SIEMPRE distingues entre lo que sabes y lo que infieres, y marcas nivel de certeza." We'll explicitly mark certainty in each table. Maybe "C = Alta/Media/Baja".

Potential final structure:
1. "Resumen ejecutivo"
2. "Lo que sabemos vs inferimos"
3. "Estimación de facturación"
4. "Salud del negocio"
5. "Dónde son fuertes y vulnerables"
6. "Cómo competir"
7. "Métricas para validar"

Let's draft with tables.

Need maybe mention "US dollars" since price $39. "Facturación bruta" not profit. "MRR/ARR".

Detailed calculations:
Base:
2,400 members x $39/mo = $93,600/mo MRR.
Annualized = $1,123,200 ARR.
If 10% annual at 15% discount:
90%*39=35.10; 10%*33.15=3.315; blended=38.415; MRR=92.2k. If 20% annual = 0.8*39+0.2*33.15=37.83; MRR=90.8k. If 50% annual = 0.5*39+0.5*33.15=36.075; MRR=86.6k. Could include simplified.
If 10% course upsell at $199 annual equivalent? Hmm:
"Si 10% de miembros compra un curso de $299/año: 240*$299=$71,760/yr = $5,980/mo; total $99.6k/mo." If 5% = $3k/mo. Good.

Need maybe "margen":
Contribution margin:
- Payment fees 3-5% = $2.8-4.7k.
- Tools/platform $2-10k.
- Production/editing/moderation $5-20k.
- Marketing $0-20k.
- Profit before taxes/founder salary: $35-65k/mo lean; $15-35k if team-heavy. But maybe if platform fees high, profit lower.
Need maybe "gross margin 60-80% before salaries".

Need maybe "business health":
- "Crecimiento: likely organic founder-led; 60k followers and 3 posts/week; not enough data on conversion."
- "Retención: unknown. At $39, if monthly churn >15%, they need ~360 new members/month just to maintain base. If churn 10%, 240 new members/month; if 5%, 120." This is a nice insight. Need include.
Let's compute:
- Churn 5% of 2,400 = 120/month.
- 10% = 240.
- 15% = 360.
- 20% = 480.
This is good. Need include "if paid members".
- "CAC: likely low due to founder, but if they buy ads, need CAC under $150-250 for $39/month."
- "LTV: at 70% margin, churn 10% LTV ~$273; churn 5% ~$546. Paid acquisition viable only if CAC below that." Good.

Need maybe "health score":
- "Salud financiera: 7/10; crecimiento: 6/10; retención: ?; defensibility: 5/10; overall: 6.5/10." Need maybe not too many.

Need maybe "teardown of competitor":
- "Modelo: founder-led community + course library."
- "Fase del negocio: likely beyond validation; likely operating in stable revenue stage; not venture-scale maybe but profitable."
- "Competitive threat: medium-high in generic automation; medium in niche if we specialize."

Need maybe "How to compete" maybe include "wedge options":
1. Vertical wedge: automation for X.
2. Outcome wedge: implement first automation in 14 days.
3. Tool wedge: n8n/self-hosted/Make vs Zapier; low-cost.
4. Role wedge: automation for agencies/ecommerce/consultants.
5. Community wedge: smaller curated, higher-touch.
Need maybe "avoid head-to-head."

Need maybe "Example positioning":
- "Para [ICP] que ya usan [tools], creamos flujos de automatización listos para [resultado], con soporte semanal y casos reales."
- "No es una comunidad de automatización genérica; es una clínica de automatización para [segmento]."
This is good.

Need maybe "Offer ladder":
- Free: automation audit / teardown.
- $29-49: resource library.
- $59-99: community.
- $149-299: Pro with office hours/audit.
- $2k-10k: implementation projects.
Need maybe "To match competitor's $93.6k MRR":
- 1,500 members at $62.40.
- 1,200 at $78.
- 625 at $150.
This is useful.

Need maybe "30-day action plan":
- Week 1: choose niche and offer.
- Week 2: build landing page + free diagnostic.
- Week 3: publish 10 case studies/templates.
- Week 4: run challenge and convert.
Could include.

Need maybe "What to monitor":
- Member count, price, annual plan, new courses, engagement, testimonials, founder posts, job postings, tech stack.
Need maybe "What would change my estimate":
- If 2,400 includes free/trial, revenue halves.
- If annual plan hidden, MRR lower but retention higher.
- If churn high, business less healthy.
- If courses priced high and sold, revenue higher.

Need maybe "No se ve si hay plan anual ni descuentos" maybe "No visible doesn't mean none; many hide checkout." Good.

Need maybe "No se ve cuántos cursos terminados" maybe "if many incomplete, it may be a liability; if not, it's a library."

Need maybe "teardown of competitor" maybe "their likely funnel":
1. Founder posts to 60k.
2. Public feed 3 posts/week builds authority.
3. Landing page: community $39/mo.
4. Courses list 12 as proof and upsell.
5. Retention through community and ongoing content.
Need include.

Need maybe "certainty" in each statement. We'll use "Certeza: Alta/Media/Baja".

Potential final answer:

```
Con los datos públicos, no puedo saber facturación real; sí puedo acotar.
```

Then "Resumen":
- "Lo más probable: están facturando ~$90k-$95k MRR y ~$1.1M ARR si 2,400 are paid active. Salud: buena, but not proven. Competir: no copiar; nicho + implementación + casos + pro tier."

Then table:
```
Dato | Lectura | Certeza
```

Let's write.

Need be careful: "Community de pago" but "2.400 miembros" maybe if all paid. We'll say "si son miembros activos y pagados." Certeza alta for math, medium for assumption.

Need maybe "sane business" maybe "healthy enough" not "guaranteed." Use "probablemente sano pero con puntos de riesgo."

Need maybe "no se ve si hay plan anual" maybe "if hidden annual plan, lower MRR but higher retention; not necessarily bad."

Need maybe "public posts 3/week" maybe "Cadence moderate; enough for content engine but not enough to infer high growth."

Need maybe "founder 60k followers" maybe "distribution moat; likely low CAC."

Need maybe "12 courses" maybe "broad but quality unknown; risk of content debt."

Need maybe "How to compete" maybe "scorecard" with "vulnerability -> your move":
- "Genérico -> vertical niche"
- "Base de conocimiento -> implementación/auditorías"
- "Monthly churn -> annual plan/guarantee"
- "Founder dependency -> team/process/brand"
- "12 courses incomplete -> fewer outcome-based courses"
- "No visible ROI -> case studies/ROI calculators"

Need maybe "final conclusion":
- "If you enter: target 1,000-1,500 paid in 12-18 months; at $79/mo = $79k-$118.5k MRR; with pro/implementation can surpass them faster."
- "Need not match 2,400; need match MRR with fewer higher ARPU."

Need maybe "No exact data" at end.

Need maybe "ask for data" maybe "If me pasas X, te doy modelo más fino." Good.

Need maybe "No markdown too heavy"? User likely wants analysis. We'll use clear sections.

Need maybe "final answer in Spanish." Good.

Let's craft final with enough detail.

Need ensure "Desired overwordiness medium" but user asks comprehensive. We'll provide moderate length maybe 1800-2500 words? Could be okay. Need not too long but thorough. We'll include tables and bullets.

Let's draft final:

---

**Teardown competitivo — comunidad de automatización**

**Premisa:** solo info pública. C = alta/media/baja.

**Resumen ejecutivo**
- Facturación probable: $93.6k MRR / $1.12M ARR if 2,400 active paid.
- Range plausible: $70k-$110k MRR depending active paid, annual, course upsells.
- Business health: likely financially healthy; retention and differentiation unknown.
- Weakness: generic positioning, founder dependency, churn, no visible ROI/annual plan.
- Compete: don't compete on $39 generic; niche down, implement, proof, higher ARPU.

Then "Lo que sabemos/inferimos".

Revenue:
```
Base case: 2,400 * 39 = 93,600
Annualized: 1,123,200
Conservative: 1,500 active paid = 58.5k
Upside: 2,400 * blended 37-38 with annual = 89-91k; + course upsells = 95-110k
```
Maybe "if 10% buy $299 annual course, +$6k/mo."

Need maybe "net":
```
Gross margin before founder salary: 55-75%.
Profit before tax/founder: $25k-$65k/mo. Lean maybe $45k-$65k; team-heavy $15k-$35k.
```
But perhaps too speculative; mark "inferencia".

Health:
- Strengths:
  - 2,400 social proof.
  - $94k MRR enough to support team.
  - Founder 60k lowers CAC.
  - 3 posts