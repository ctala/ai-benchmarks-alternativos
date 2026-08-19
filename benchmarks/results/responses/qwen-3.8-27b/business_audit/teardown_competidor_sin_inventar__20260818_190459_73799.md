# Qwen 3.8 27B — business_audit/teardown_competidor_sin_inventar

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 4.19 | quality: 4.0
- latency_total: 57.209s | tokens_per_second: 143.2
- input_tokens: 231 | output_tokens: 8192

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

We need answer in Spanish. User asks for competitor teardown from outside. Need distinguish known vs inferred, mark certainty. Need estimate revenue, business health, competition strategy. Need be careful not fabricate. Need maybe state assumptions, ranges. Need likely use data: 2,400 members, $39/month. If all paying monthly, MRR = 93,600, ARR = 1,123,200. But "2,400 miembros" could be total registered, maybe not all active/paying. If membership platform, likely paying? Need distinguish. Could be free tier? "Comunidad de pago" says paid, but 2,400 could be total members including past. Need estimate. If 2,400 paying monthly at $39, gross monthly 93.6k. Platform fees maybe 5-10% + payment processing 2.9+30c, maybe net 85-90k. If annual plans hidden? Not visible. If annual discount, ARPA lower. Need health: public feed 3 posts/week indicates operational consistency. 12 courses listed but completion unknown; content library moderate. Founder 60k followers gives distribution advantage but risk key-person dependency. Need churn unknown. Need health metrics: if community, likely high churn? Need infer. Need maybe model scenarios: optimistic, base, conservative. If 2400 are active paying: $93.6k MRR, $1.12M ARR. If 50% active paying: $46.8k MRR, $561k ARR. If 25%: $23.4k MRR, $281k ARR. If 10%: $9.36k MRR, $112k ARR. Need mention if "miembros" on membership platform often means enrolled in paid membership? But could be all signups. Need mark certainty: low/medium/high. Need maybe calculate break-even? Not enough. Need health: revenue likely not enough for big team? At $1.1M ARR could support small team. But if $280k ARR, side project. Need competition: need not copy directly. Need identify gaps: no visible annual plan/discounts? Maybe retention problem? 3 posts/week public maybe low content cadence? 12 courses may be shallow? Need propose wedge: niche down, better onboarding, outcomes, accountability, templates, ROI, cohort, employer/agency angle, enterprise? Need metrics to track, experiments. Need maybe ask for additional data? But answer should be useful.

Need structure:
- Premisas y límites: only public data, no access to churn, LTV, CAC, conversion, refunds, annual, cohort, active.
- What I know (high certainty): paid community, price $39, 2,400 displayed, 3 posts/week public, founder 60k, 12 courses listed.
- What I infer (with confidence): revenue range, business model, health, moat, risks.
- Revenue estimate: table scenarios. Need maybe use "miembros" as paying? If it says comunidad de pago and portada muestra 2.400 miembros, likely platform counts active members? But could be total. Need say if "miembros" means active paid members, high-ish confidence? But still unknown. Need maybe "si la cifra es de miembros activos de pago" then $93.6k MRR. If total lifetime, lower. Need maybe expected value? Could assign probabilities? Maybe base 60% active? Let's think.
On membership sites, "members" often active subscribers. But public page may show total members. If it's a paid community, likely "members" are paid. But could include free trial? Need mark: medium confidence that a significant portion are paying; high confidence that 2,400 is not necessarily current paying. Need perhaps provide "rango operativo" $30k-$100k MRR? Let's derive.
If 2,400 all paying monthly: MRR 93,600. If annual plans at $390/year (10% off) equivalent $32.5/mo, MRR 78,000. If 20% annual, MRR 87,360? Actually if annual $390, monthly equivalent 32.5. Mixed: 0.8*39+0.2*32.5=37.7, MRR 90,480. If 50% paying active: 46,800. If 25%: 23,400. If 10%: 9,360.
Could use "health" based on visible signals: 3 posts/week public is decent but not high; 12 courses suggests productized content but no completion; founder 60k means distribution but not brand. Need maybe "sano" means cash flow? If MRR > $50k, likely profitable if low COGS. If < $20k, maybe not sustainable unless founder-driven.
Need maybe calculate customer lifetime: at $39/mo, to cover CAC. If CAC from founder audience maybe low. If paid ads, need LTV. If churn 5% monthly, avg lifetime 20 months, LTV gross $780. If 10% churn, 10 months, $390. Need mark inference. If community has high engagement, churn lower. But no data.
Need competition: How to compete. Need propose positioning: not "another automation community". Need choose wedge: e.g., "automatización para [nicho] con resultados en 14 días", templates, implementation, accountability, ROI. Need product: $99-$299/mo? Or one-time course + community? Need pricing: If competitor $39, could compete on outcome not price. Or undercut? Better not. Need maybe offer annual? If they don't show annual, maybe retention issue; we can offer annual with guarantee. Need content: public feed 3/week; we can do daily micro-content, case studies, teardowns, before/after. Need courses: 12 courses maybe generic; we can do fewer deeper modules with completion and certification. Need distribution: founder 60k; need build own audience or partnerships. Need maybe use "public proof" and "transparency". Need maybe build waitlist, offer "audit" or "automation sprint". Need metrics: conversion, churn, NPS, activation.
Need maybe include "what to spy on" and questions: check reviews, job board, social proof, domain, app, testimonials, pricing page, cancellation, annual, refunds.
Need maybe "teardown" with sections:
1. Resumen ejecutivo
2. Datos verificables vs inferidos
3. Estimación de ingresos
4. Salud del negocio
5. Fortalezas/debilidades
6. Estrategia para competir
7. Plan 30/60/90
8. Señales a monitorear

Need ensure "Distingues SIEMPRE entre lo que sabes y lo que estás infiriendo, y marcas tu nivel de certeza." So use tags: [SABIDO], [INFERIDO - alta/media/baja]. Maybe table with certainty. Need not overstate.

Need maybe mention legal/ethics: only public data, no scraping? Not necessary.

Need maybe compute exact:
2,400 * 39 = 93,600.
Annual if $390: 2,400*390 = 936,000/year, monthly equivalent 78,000.
If 10% off annual: $390. If 20% off: $374.40, monthly equivalent 31.2, MRR 74,880.
If 50% active: 46,800.
If 25%: 23,400.
If 10%: 9,360.
If 5%: 4,680.
Could present "rango plausible": $10k-$100k MRR depending definition. But likely if public "members" active paid, $80k-$95k MRR. Need maybe "mi escenario base: 60% de los 2,400 son miembros activos de pago => $56,160 MRR, $674k ARR". But is 60% reasonable? If "members" on paid community, maybe 80-100% active. But if total signups, maybe 20-40%. Need maybe choose base 50%? Let's think.
The user says "Comunidad de pago ... Muestra '2.400 miembros' en la portada." If it's a paid community, likely the number is members of the community, maybe all paid. But could be "members" including free? They explicitly say paid. I'd say if the platform counts active paid members, revenue ~$93.6k MRR. But I must mark inference: "No sé si la cifra es de miembros activos de pago o registrados históricos." So table.
Need health: If $93.6k MRR, likely healthy if churn <8% and CAC low. If $23k MRR, fragile. Need maybe "sano" from outside: positive signals: recurring price, public content cadence, founder audience, course library. Negative: no visible annual plan/discounts (could be pricing opacity or retention weakness), 12 courses completion unknown, 3 posts/week public not enough for high engagement, key-person risk. Need maybe "probable modelo founder-led, low overhead, margin high if self-hosted/platform." Need mention platform fees: if on Circle/Skool/Mighty Networks, 5-10% + payment. If self-hosted, lower. Need maybe "cash flow likely positive unless heavy paid ads." Need mark.
Need competition: Need maybe "no compitas por precio a $39; compitas por claridad de resultado y fricción". Need maybe specific offers:
- "Automatiza tu [proceso] en 14 días" cohort $499 one-time + $49/mo? Or $99/mo.
- Template library with done-for-you workflows (n8n/Make/Zapier).
- Audit/implementation for agencies.
- Outcome-based: "si no ahorras X horas, reembolso".
- Content: public case studies, before/after, ROI calculator, live builds.
- Onboarding: first workflow in 24h.
- Retention: weekly office hours, challenges, certification, team plans.
- Distribution: founder audience? If not, use SEO, partnerships, free tools, templates, YouTube, LinkedIn, communities.
Need maybe "positioning map": Competitor: general automation community, $39, content-led, founder audience. You: niche + implementation + accountability. Need maybe "wedge: nicho con dolor caro: e-commerce, agencies, SaaS ops, real estate, finance? Need choose based on user's capability. Since no user context, propose choose one niche where you can prove ROI.
Need maybe "pricing strategy": If they $39, you can do $79-$199 if outcome. Or entry $19 trial. Or annual $588 with guarantee. Need maybe not undercut.
Need maybe "KPIs to beat": Churn <5% monthly, activation >70% in 7 days, NPS >50, CAC payback <3 months, LTV/CAC >3.
Need maybe "teardown score": Use table with dimensions: revenue visibility, retention, content, product depth, distribution, defensibility. Mark confidence.
Need maybe "what I cannot know": actual paying members, churn, CAC, LTV, refunds, annual, cohort, support load, team, margins, legal.
Need maybe "next due diligence": check Trustpilot, G2, reviews, LinkedIn, job posts, domain age, social comments, price changes, app store, YouTube, podcast, partnerships, refund policy, cancellation.
Need maybe "red flags / opportunities": No annual visible might mean they rely on monthly and maybe churn; opportunity to lock annual. 12 courses but no completion: opportunity to gamify completion. Public feed 3/week: opportunity for daily value. Founder 60k: opportunity if he is absent? Need monitor.
Need maybe "competitive moat": community network effects, content library, brand, audience. But $39 low price means weak switching costs? Actually community relationships create switching costs. Need mark.
Need maybe "financial model" with assumptions:
- ARPA: $39/mo if monthly; $32.5 if annual 10% discount.
- Platform fee: 5-10% + 2.9%+30c. Net per member maybe $34-$36.
- If 2,400 active monthly: gross $93,600; net $85k-$88k.
- If 1,200 active: $46,800 gross; net $42k-$44k.
Need maybe "break-even" unknown. But if no employees, low fixed costs, could be profitable at $10k MRR. If team, need $30k+.
Need maybe "health score" 1-10 with confidence. E.g., if active paid 2,400: health 7/10 (good but key-person and churn unknown). If only 25% active: 4/10. Need maybe "rango de salud: 4-8/10 depending active members".
Need maybe "competitive strategy" with "no copies". Need maybe "attack their weaknesses" but ethically.
Need maybe "questions to answer before competing": your ICP, proof, offer, channel. Could include.
Need final in Spanish. Need be thorough.

Let's craft final. Need include explicit certainty tags. Maybe use:
- [DATO PÚBLICO] = lo que me diste / visible.
- [INFERENCIA ALTA] = alta certeza.
- [INFERENCIA MEDIA] = plausible.
- [INFERENCIA BAJA] = hipótesis.

Need maybe avoid saying "sé" for inferences. Use "estimo".

Potential final structure:
Title: Teardown competitivo (solo datos públicos)
1. Advertencia: límites
2. Resumen ejecutivo: likely revenue range, health, how compete.
3. Tabla de hechos vs inferencias.
4. Estimación de facturación:
   - Base: if 2,400 active paid monthly: $93.6k MRR, $1.12M ARR.
   - If annual: maybe $78k-$90k MRR.
   - If "members" total/historical: scenarios 50/25/10%.
   - Net after fees.
   - Probability? Maybe assign "escenario más probable" if public count is active: 70%? But need mark. Could say "si yo tuviera que apostar, pondría 50% de probabilidad en que la mayoría son activos de pago, 30% en que es total histórico, 20% en que mezcla free/trial." But is that too speculative? It's inference. Mark low/medium. Maybe better: "No puedo asignar probabilidad robusta, pero rangos".
Need maybe include "facturación neta estimada" with fees.
5. Salud del negocio:
   - Positive: recurring, public cadence, founder audience, course library.
   - Risk: key person, no annual visible, churn unknown, content completion unknown, low price.
   - Health range: if active 2400: 7/10; if 600 active: 4/10; if 240 active: 2/10.
6. Fortalezas/debilidades (SWOT-ish)
7. Cómo competir:
   - Positioning: niche + outcome + implementation.
   - Offer architecture: entry, core, premium.
   - Pricing: not $39; maybe $99/mo or $499 cohort + $59/mo.
   - Product: templates, workflows, onboarding, certification, accountability.
   - Content: public proof, daily, case studies, live builds.
   - Distribution: partnerships, free tool, SEO, community, founder audience.
   - Retention: annual, team, challenges, ROI tracking.
8. Plan 30/60/90.
9. Señales a monitorear / due diligence.
10. Conclusion.

Need maybe include formulas:
MRR = miembros activos de pago × ARPA.
ARR = MRR × 12.
LTV bruto = ARPA / churn mensual. If churn 5%, LTV $780; 10%, $390; 15%, $260.
CAC payback = CAC / contribution margin per month. Need maybe example.
Need mark: churn is inferred.

Need maybe "qué tan sano" from outside: "No puedo afirmar rentabilidad, pero señales de caja recurrente". Need maybe "si factura >$50k MRR y no tiene equipo grande, probablemente rentable; si <$20k, puede ser negocio de fundador con márgenes altos pero frágil".

Need maybe "competitor teardown" not just financial. Need maybe "su modelo probable": founder-led paid community, content + courses, low price, broad automation audience. Need maybe "moat": audience + community. Need "vulnerabilities": generic, low price, no implementation, no annual, content not completion-oriented, key person.

Need maybe "cómo les compito" with concrete "wedge":
Option A: "Automatización para agencias de marketing" with client-facing templates, ROI, white-label.
Option B: "Automatización para e-commerce" ops, inventory, support, email.
Option C: "Automatización para SaaS ops" onboarding, billing, support.
Need choose one. Could say "elige uno donde puedas demostrar ahorro de horas/dinero".
Need maybe "offer": "Sprint de automatización: en 14 días conectas X, Y, Z; incluye 10 plantillas, 2 sesiones, garantía. Precio $499 + $79/mo mantenimiento/comunidad". Or "membership $99/mo con onboarding y plantillas".
Need maybe "public content cadence": 5 posts/week: Monday case study, Tuesday template, Wednesday live build, Thursday mistake, Friday ROI. Need maybe "public feed 3/week is their baseline; you can out-communicate with proof, not just volume".
Need maybe "courses": They have 12 courses but completion unknown. You can have 1 flagship path with completion, certification, project. Need "cohort-based" for accountability.
Need maybe "pricing psychology": Their $39 is low friction but low commitment. You can use annual $588 or $792 to improve retention. If they don't show annual, maybe they don't optimize retention or hide. You can show annual with guarantee.
Need maybe "distribution": If founder has 60k, they likely rely on his audience. You need build owned channel or partner. Need "free asset": ROI calculator, template pack, audit checklist, n8n/Make workflow library.
Need maybe "competitive messaging": "No compites contra 'automatización'; compites contra 'no sé por dónde empezar / no tengo tiempo / no veo ROI'".
Need maybe "metrics to win": conversion from free to paid >2%, activation >50% in 7 days, churn <4% monthly, NPS >50, CAC payback <4 months.
Need maybe "what to avoid": price war, generic content, copying 12 courses, building big community before product-market fit.
Need maybe "due diligence checklist":
- Check if 2,400 is active or total: look at member count changes, testimonials dates, live events, job posts, reviews.
- Check annual plan: pricing page, FAQ, sales page, email.
- Check churn: review dates, "canceló", renewal, annual.
- Check content: completion, student projects, outcomes.
- Check founder dependency: who posts, support, events.
- Check tech: platform, integrations, API.
- Check legal: refund policy, ToS.
Need maybe "señales de que factura alto": multiple team, jobs, events, affiliates, annual, testimonials, app. "Señales de que es pequeño": only founder, no team, no jobs, low engagement.

Need maybe "certainty" in each section. Could use table:
Afirmación | Tipo | Certeza | Por qué.
Examples:
- Precio $39/mes: dato público, alta.
- 2,400 miembros: dato público, alta que está publicado; baja que sean activos de pago.
- 3 posts/week: dato público, alta.
- Founder 60k: dato público, alta.
- 12 cursos: dato público, alta; baja profundidad/completados.
- MRR $93.6k: inferencia alta solo si 2400 activos de pago; media overall.
- Business healthy: inferencia media.
Need maybe final "veredicto": "Probablemente es un negocio recurrente de 1-6 cifras anuales. Si la cifra de miembros es activa, ~$1.1M ARR y sano; si es histórica, puede ser $0.3-0.6M ARR y más frágil. Tu mejor ataque no es bajar a $29, sino ofrecer resultado medible, implementación y nicho."

Need ensure no unsupported claims. Use "si", "probable", "podría".

Let's draft in Spanish with clear tags.

Potential final:
"Teardown (solo desde fuera)"
"Lo que NO puedo saber" list.
"Resumen ejecutivo" with bullet:
- [INFERENCIA MEDIA] Ingresos: entre $10k y $100k MRR; caso activo $93.6k MRR / $1.12M ARR.
- [INFERENCIA MEDIA] Salud: probablemente rentable si low overhead; riesgo key-person and churn.
- [INFERENCIA ALTA] Oportunidad: competir por nicho/outcome/implementation, no por precio.

Need maybe "facturación" table:
Escenario | Miembros activos de pago | ARPA | MRR bruto | ARR | Comentario
- Todos 2400 activos mensuales: 2400, $39, $93,600, $1,123,200, [INFERENCIA MEDIA/ALTA si count active]
- 2400 activos con 20% anual a $390: ARPA $37.7, MRR $90,480, ARR $1,085,760
- 50% activos: 1200, $39, $46,800, $561,600
- 25% activos: 600, $39, $23,400, $280,800
- 10% activos: 240, $39, $9,360, $112,320
Need maybe "neto estimado" after 5-10% + payment: multiply 0.88-0.92? Actually if platform fee 5% + Stripe 2.9%+30c: for $39, fee ~ $1.95 + $1.131 + 0.30 = $3.381, net $35.619, 91.3%. If platform 10% + Stripe: $3.9 + $1.431? Actually Stripe on net? Usually payment on gross: 2.9%+30c = $1.431, platform 10% = $3.9, total $5.331, net $33.669, 86.3%. If self-hosted only Stripe: $37.569, 96.3%. So net per member $33.7-$37.6. For 2400: $80,900-$90,300 monthly net. Could mention.
Need maybe "if annual $390, Stripe fee $11.31+0.30, platform 5-10% $19.5-$39, net $339.19-$369.39 per year, monthly equivalent $28.27-$30.78. For 2400 net MRR equivalent $67,800-$73,900. But maybe too detailed. Could keep gross.

Need maybe "health" table:
Señal | Interpretación | Certeza
- Recurring $39: predictable, low ticket [ALTA]
- 3 posts/week public: consistency, but not engagement [MEDIA]
- 12 courses: productized, but depth unknown [MEDIA]
- Founder 60k: distribution advantage, key person [MEDIA]
- No annual visible: possible retention weakness or hidden [BAJA/MEDIA]
Need maybe "health score" with scenarios.

Need maybe "cómo competir" in detail.
Need maybe include "positioning statement":
"Para [nicho] que pierde horas en [proceso], [tu marca] es una comunidad + plantillas + acompañamiento que automatiza [proceso] en [días] con ROI medible, a diferencia de [competidor] que vende acceso general a cursos de automatización."
Need maybe "offer ladder":
- Free: checklist/ROI calculator/template.
- Entry: $49/$99 template pack or 14-day sprint.
- Core: $79-$149/mo community + templates + office hours.
- Premium: $499-$1,999 implementation/audit/team.
Need maybe "if you want to directly compete at same price": $39 with better onboarding? But likely not. Could mention "solo compites a $39 si quieres volumen y puedes soportar churn; mejor subir precio con resultado".
Need maybe "retention": annual plan $588 (2 months free) or $792 (4 months free), guarantee, team seats.
Need maybe "content moat": public case studies with numbers, "antes/después", "errores", "plantillas descargables". Need "3 posts/week" they do; you can do 5 but quality.
Need maybe "distribution": founder 60k; if you have less, use partnerships, SEO, free tool, communities, YouTube/LinkedIn. Need "not rely on one founder".
Need maybe "product": "12 courses" maybe shallow; you can do "1 path, 4 modules, 10 templates, 1 certification". Need "completion" and "project".
Need maybe "community": "accountability pods", weekly challenges, template library, support.
Need maybe "metrics and experiments":
- Week 1-2: validate niche with 20 interviews, landing page.
- Week 3-4: offer pilot $499 sprint, 10 clients.
- Month 2: productize, collect testimonials, build waitlist.
- Month 3: launch membership, annual, cohort.
Need maybe "KPIs": CAC, conversion, churn, activation, NPS.

Need maybe "red flags in competitor":
- If no annual: maybe they don't have enough trust or retention.
- If 12 courses but no completion: maybe content bloat.
- If public feed 3/week but low engagement: maybe engagement not high.
- If founder 60k: if he stops, revenue stops.
Need maybe "opportunities":
- Target his customers who want implementation.
- Offer "done with you" not just "access".
- Provide ROI tracking.
- Niche down.
- Annual with guarantee.
- Better onboarding.
- Team/agency plans.
- Certification.
- Integrations with specific tools.

Need maybe "what to monitor":
- Member count changes.
- New pricing/annual.
- Launch of team plan.
- Founder posts about churn/retention.
- Job postings.
- Reviews.
- Course updates.
- Partnerships/affiliates.
Need maybe "if they add annual, they are optimizing retention; if they increase price, confidence; if member count drops, churn."

Need maybe "final recommendation": "No ataques de frente. Elige un nicho, un resultado medible, un onboarding agresivo, un precio superior, y comunica prueba. Tu objetivo no es 'ser más barato' sino 'ser la opción que hace el trabajo'."

Need ensure all in Spanish. Need maybe use currency USD. Need maybe mention "facturación" not "ingresos" maybe gross revenue. Need "factura" = gross before fees. Use "MRR bruto".

Need maybe be explicit: "No tengo acceso a su backend, entonces cualquier cifra es estimación." Good.

Let's write final with high detail. Need maybe not too long? Desired oververbosity 9, so thorough. Use tables. Need ensure certainty tags.

Let's craft carefully.

Potential final:

"Teardown competitivo: comunidad de automatización a $39/mes"

"0) Regla de lectura" with tags.

"1) Lo que sé vs lo que infiero" table.

Data:
- Paid community on membership platform [DATO PÚBLICO] high.
- 2,400 members displayed [DATO PÚBLICO] high; meaning active paid? [INFERENCIA BAJA/MEDIA].
- $39/mo [DATO PÚBLICO] high.
- No annual/discounts visible [DATO PÚBLICO] high; interpretation [INFERENCIA MEDIA].
- 3 public posts/week [DATO PÚBLICO] high.
- Founder 60k [DATO PÚBLICO] high.
- 12 courses listed [DATO PÚBLICO] high; completion [INFERENCIA BAJA].

"2) Estimación de facturación"
Formula.
Table.
Need maybe include "si la cifra 2,400 es de miembros activos de pago" scenario. Mark: [INFERENCIA MEDIA] if public count active; [INFERENCIA ALTA] calculation conditional.
Maybe:
"Condición clave: si 'miembros' = suscriptores activos de pago, la matemática es simple. Pero no está confirmado."
Table:
- 100% activos mensuales: 2400, $39, $93,600, $1,123,200, [INFERENCIA MEDIA]
- 100% activos con 20% anual: ARPA $37.7, $90,480, $1,085,760, [INFERENCIA BAJA/MEDIA]
- 50% activos: $46,800, $561,600, [INFERENCIA MEDIA]
- 25%: $23,400, $280,800, [INFERENCIA MEDIA]
- 10%: $9,360, $112,320, [INFERENCIA BAJA]
Need maybe "rango práctico: $10k-$100k MRR; caso más favorable ~$1.1M ARR; caso conservador ~$0.3M ARR." Mark.
Net fees: "Después de pasarela y plataforma, neto probablemente 85-95% del bruto si self-hosted, 80-90% si platform. En el caso 100% mensual: ~$80k-$90k neto/mes." Mark inference.

"3) Salud del negocio"
Use "No puedo decir rentabilidad exacta". Table signals.
Maybe health scenarios:
- If 2400 active: 7/10. Reason: recurring, likely profitable, but key person/churn unknown.
- If 1200 active: 5/10.
- If 600 active: 3/10.
- If 240 active: 2/10.
Mark [INFERENCIA MEDIA].
Positive/negative signals.
Need maybe "churn assumptions": If community, monthly churn 3-10%. If 5%, LTV $780. If 10%, $390. Mark [INFERENCIA BAJA]. "Con $39, necesitas churn bajo o CAC muy bajo para ser sostenible." Good.

"4) Fortalezas y debilidades" table.
Fortalezas: price low friction, founder audience, recurring, public consistency, course library.
Debilidades: generic, low price, no visible annual, completion unknown, key person, public content not proof, low switching cost? Actually community relationships. Mark.

"5) Cómo competir"
Start with "No copies: 'comunidad de automatización $39'".
Positioning:
- Choose niche with expensive problem.
- Outcome: save X hours / reduce cost / increase revenue.
- Offer: access + implementation + accountability.
Pricing:
- Don't go $29. Use $79-$149/mo or $499 cohort + $59/mo. Or entry $49 template. Annual.
Product:
- Onboarding 24h, first workflow, template library, weekly builds, certification, ROI tracker, team plan.
Content:
- Public proof: case studies, numbers, live builds, templates. 5/week.
Distribution:
- Free tool, partnerships, SEO, LinkedIn/YouTube, communities, affiliates.
Retention:
- Annual, guarantee, challenges, team, reactivation.
Need maybe "battlecard" vs competitor:
- They: "acceso a cursos". You: "resultado implementado".
- They: $39. You: $99 with guarantee.
- They: 12 cursos. You: 1 path + templates + certification.
- They: founder audience. You: owned audience + partnerships.
Need maybe "specific 30/60/90".
30: validate niche, interviews, landing, pilot offer, 10 customers.
60: productize onboarding, templates, collect ROI, waitlist, content engine.
90: launch membership, annual, cohort, partnerships, measure churn.
Need maybe "KPIs".

"6) Due diligence / señales a vigilar" list.
"7) Veredicto final".

Need maybe include "nivel de certeza" in final verdict:
- High: they have paid community, $39, public cadence, founder audience.
- Medium: likely recurring revenue in five/six figures annually; if active members, ~$1.1M ARR.
- Low: exact churn, CAC, profit, course completion.
- Recommendation high confidence: compete on niche/outcome/implementation.

Need maybe avoid too much speculation. Use "hipótesis".

Let's ensure answer directly addresses: "cuánto factura, qué tan sano es el negocio y cómo les compito." So final must answer those.

Need maybe include "facturación" not just MRR. Use "facturación bruta mensual".

Let's write final in polished Spanish.

Need maybe mention "si la plataforma muestra '2.400 miembros' en portada, muchas plataformas muestran miembros activos, pero no todas; puede ser total histórico o incluidos free." Mark.

Need maybe "No se ve plan anual" could be because not offered, hidden, or not on public page. Interpretation: possible retention optimization opportunity. Mark.

Need maybe "12 cursos listados, no se ve cuántos terminados" could be content breadth but not depth. Mark.

Need maybe "3 posts por semana en feed público" indicates minimum viable content operation, but not engagement. Mark.

Need maybe "fundador 60k seguidores" means likely CAC lower if audience converts, but also concentration risk. Mark.

Need maybe "comunidad de pago" means likely subscription, but could have one-time? They say membership platform, price visible $39/mes. So subscription.

Need maybe "healthy" maybe "cash flow". Use "sano" as "recurrencia, retención, dependencia, margen". Need maybe "no sé si es rentable".

Let's draft.

Potential final text:

"Teardown competitivo (solo datos públicos)"

