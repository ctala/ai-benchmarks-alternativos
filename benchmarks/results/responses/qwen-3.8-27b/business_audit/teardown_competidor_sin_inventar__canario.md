# Qwen 3.8 27B — business_audit/teardown_competidor_sin_inventar

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 2.19 | quality: 2.0
- latency_total: 583.006s | tokens_per_second: 14.1
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

We need answer in Spanish. User asks: "Hazme un teardown de un competidor. Esto es TODO lo que pude ver desde fuera (su página pública):

- Comunidad de pago sobre automatización, en una plataforma tipo membresía.
- Muestra '2.400 miembros' en la portada.
- Precio visible: $39/mes. No se ve si hay plan anual ni descuentos.
- Publican 3 posts por semana en el feed público.
- El fundador tiene 60.000 seguidores en una red social.
- Tienen 12 cursos listados, no se ve cuántos están terminados.

Quiero saber cuánto factura, qué tan sano es el negocio y cómo les compito."

We need respond as competitive analyst, always distinguish known vs inferred, mark certainty. Need probably provide teardown: known facts, estimates, ranges, assumptions, revenue estimate, health, competitive strategy, data to collect, experiments, risks. Need be careful: cannot know exact revenue. Need calculate based on public info: 2,400 members, $39/month. If all paying monthly: 2400*39 = 93,600 MRR, ARR 1,123,200. But likely member count includes free? "Comunidad de pago" but "miembros" might paid? It says muestra '2.400 miembros' en portada. Could be total members maybe paid. Need mark uncertainty. Could be active vs cumulative, paid vs free, annual vs monthly, refunds, churn, discounts. Need provide scenarios: conservative/median/optimistic. If 2,400 are paid monthly: MRR $93.6k, ARR $1.12M. If 70% paid? $65.5k MRR, ARR $786k. If 50%: $46.8k MRR, ARR $561k. If 30%: $28.1k MRR, ARR $337k. If annual prepay maybe cash different. Need maybe include 3% platform fees? If membership platform takes 5%? Net revenue maybe 90-95%. Need maybe estimate gross margin high digital, COGS low. Need health signals: public feed 3 posts/week suggests active but not necessarily engagement. 12 courses listed not finished: content moat but maybe incomplete. Founder 60k followers: distribution advantage, but single-founder risk. Price $39/mo mid-tier. No annual plan visible: maybe less cash upfront, higher churn risk, less commitment; but easier entry. Need discuss LTV/CAC unknown. Need estimate churn? Unknown. Could infer from cadence and niche. Need not overstate. Need mark certainty: high/medium/low.

Need answer likely structured:
1. Scope and epistemic rules.
2. Known vs inferred table.
3. Revenue estimate: formula, scenarios, confidence.
4. Business health: strengths, weaknesses, red flags, moat, dependency, content, community, pricing, distribution.
5. Competitive strategy: positioning, wedge, offer, pricing, content, acquisition, retention, partnerships, product, messaging, experiments.
6. Data to collect to reduce uncertainty: social proof, testimonials, reviews, job posts, app store? platform, domain, email, pricing changes, affiliate, YouTube, podcasts, cohort, engagement, churn via surveys, competitor interviews.
7. 30/60/90 plan maybe.
8. What I would not claim.

Need be in Spanish. Need maybe include calculations. Need maybe mention "factura" could mean revenue not profit. Need distinguish MRR/ARR. Need maybe if "2.400 miembros" includes all who ever joined, not current active paid. Need maybe if membership platform displays "members" as total signups, not current subscribers. Need maybe if some are lifetime? Unknown.

Need maybe include "certeza" markers: [Alta], [Media], [Baja]. Need maybe "Lo que sé" vs "Lo que infiero". The user says "Eres analista competitivo. Distingues SIEMPRE entre lo que sabes y lo que estás infiriendo, y marcas tu nivel de certeza." So every claim should be labeled. Could use table with "Dato", "Tipo", "Certeza". Need be explicit: I don't know actual revenue, only estimate.

Need maybe include "No puedo afirmar" etc.

Need think through revenue estimate in detail.

Given:
- Paid community on membership platform.
- Displays 2,400 members on cover.
- Visible price $39/month. No annual/discounts seen.
- 3 public posts/week.
- Founder 60k followers.
- 12 courses listed, unknown completed.

Revenue: If 2,400 are current paid monthly members at $39: MRR = 93,600. ARR = 1,123,200. If platform fee 5-10%, net 84k-89k MRR? Actually 93.6*0.95=88.92; *0.90=84.24. But "factura" gross likely 93.6k MRR. If some are annual? If $39/mo billed monthly. If annual maybe $39*12=468; cash MRR equivalent same if normalized, but cash collected upfront. If no annual visible, likely monthly. If "miembros" includes free: need estimate paid ratio. Could use common community paid/free ratio? But no basis. Need mark low certainty. Could present sensitivity: 25/50/75/100% paid.

Maybe use "miembros" as paid? Since "comunidad de pago" and "precio visible" likely all members pay? But many platforms show total members including free. Need not assume. We can say if the displayed 2,400 corresponds to current paid members, high-ish? Actually medium because public count could be total. If "comunidad de pago" maybe all members are paying? But "miembros" might be paid. Mark: [Media-Alta] if we accept it's current paid. [Baja] if it's cumulative or includes free.

Need maybe estimate active vs paying: even paid members may be dormant. But revenue if subscription active. Could have churn. Need maybe estimate MRR range:
- Scenario A (best case): 2,400 current paid monthly: $93.6k MRR, $1.12M ARR.
- Scenario B (base): 70% current paid: $65.5k MRR, $786k ARR.
- Scenario C (conservative): 40% current paid: $37.4k MRR, $449k ARR.
- Scenario D (pessimistic): 20%: $18.7k MRR, $225k ARR.
Need maybe choose "rango plausible" $20k-$95k MRR, $240k-$1.1M ARR. But if all paid, upper bound. Need maybe if 2,400 is total signups and current active paid 25%, then $23.4k MRR. Need include.

Could also estimate based on founder followers: 60k followers. Conversion to paid community? If 0.1-0.5% of followers are paying? 60-300 members, $2.3k-$11.7k MRR. But community may have other channels. Not enough. Need maybe not use as primary, but as sanity check: 60k followers is decent but not enough to support 2,400 paid solely from that without other channels, events, SEO, partnerships. If 2,400 paid, that's 4% of followers; possible if highly targeted, but not impossible. Mark low.

Need health:
Strengths:
- Recurring revenue model [high from visible price]
- Public content cadence 3/week [high observed] suggests operational consistency, but not engagement [low].
- 12 courses [high listed] suggests content library, but completion unknown [low]. Could be moat or liability if outdated.
- Founder 60k [high] gives distribution and authority, but concentration risk [high inference].
- $39/mo accessible [high] but maybe low LTV if churn high [medium].
Weaknesses/risks:
- No annual plan visible [high] may indicate lower commitment, less cash upfront, maybe higher churn; or hidden. [medium]
- Public feed only 3 posts: not enough to infer engagement; could be low interaction. [low]
- 12 courses not completed: risk of product promise gap; if many unfinished, satisfaction/churn risk. [low]
- Single founder dependency: if founder stops creating, community may decay. [medium]
- Price not transparent annual/discounts: could be friction or simplicity. [low]
- Public member count could be vanity metric; if includes free or cumulative, revenue overestimated. [medium]
- Niche automation: content can be commoditized; AI changes fast; need updates. [medium]

Need maybe estimate gross margin: digital community high gross margin 70-90% after platform fees, payment, tools, labor? If founder labor not allocated, high. But if they pay contractors, lower. [medium-low]

Need maybe estimate burn? unknown. Need health score: maybe "potencialmente sano si 50%+ de 2,400 son pagadores actuales; riesgo si depende de fundador y no hay retención". Need maybe use "señales de salud" with confidence.

Need competitive strategy: How to compete. Need actionable. Need maybe position against:
- They sell access to community + courses + automation content.
- Compete on outcomes, accountability, implementation, niche, price, product, community quality.
Need maybe identify wedge:
1. Niche down: automation for specific audience (e.g., agencies, e-commerce, SaaS, local businesses, no-code, AI ops). If their community is broad, target underserved segment.
2. Outcome-based offer: "implementa X automatizaciones en 14 días" vs generic access.
3. Productized service + community: done-with-you.
4. Pricing: maybe $99/mo for implementation, or $29/mo for lightweight, or annual.
5. Content: publish proof, templates, case studies, teardowns, before/after, ROI calculators.
6. Acquisition: use founder's audience? Need build own. Leverage SEO for "how to automate X", YouTube, Twitter, LinkedIn, newsletters, partnerships, affiliates.
7. Retention: weekly live, templates, office hours, accountability, graduation, cohorts, certifications, private Slack/Discord, job board, vendor marketplace.
8. Reduce churn: annual plan, milestones, onboarding, quick wins, ROI tracking.
9. Competitor intelligence: join as member (if possible) to observe engagement, content quality, support, churn reasons, gaps. This is key. Need maybe ethically? Yes, can buy membership to analyze. Need maybe track: onboarding, public/private feed, engagement, courses completion, support, community norms, retention features, pricing changes.
10. Build switching offers: "migración gratis", templates, import, compare.
11. Exploit weaknesses: if courses unfinished, offer complete implementation; if no annual, offer annual with bonuses; if public content only, offer private community; if founder-dependent, offer team/community.

Need maybe propose 30-day experiment:
- Buy membership for 1 month, audit.
- Interview 5-10 potential customers who might use competitor: ask what they'd switch for.
- Create 3 landing pages: generic automation community, niche implementation, template pack. Test $39 vs $99.
- Publish 5 public teardowns/templates.
- Set up waitlist.
- Measure CAC, conversion, LTV.

Need maybe financial target: If you want $10k MRR at $39, need 256 members. If $99, 101 members. If $29, 345. Need maybe compare to competitor: to match $50k MRR at $39 need 1,282 members. But with niche maybe $99 need 505.

Need maybe "cuánto factura" answer: I can't know exactly. Based only public data, if 2,400 are current paying monthly, gross revenue ~$93.6k/month (~$1.12M/year). If only half are paying, ~$46.8k/month (~$561k/year). Plausible range: $20k-$95k MRR depending on paid ratio. Mark certainty low-medium. Need maybe include "facturación" could be MRR not cash if annual. Need maybe if platform fees: net 85-95%.

Need maybe "qué tan sano" answer: Potentially healthy if current paid members >800-1,200 and churn <5-8% monthly; risky if member count is cumulative/free or founder-dependent. Public signals: consistent posting is positive but not proof of engagement; 12 courses is asset but unknown quality; no annual plan may signal flexibility or weaker commitment. Need maybe define health criteria:
- MRR > $30k and churn <8%: sustainable.
- MRR $10-30k: viable but fragile.
- MRR <$10k: hobby/early.
But unknown.

Need maybe include "nivel de certeza" for each: Use tags: [SABIDO/ALTA], [INFERENCIA/MEDIA], [INFERENCIA/BAJA]. Maybe in tables.

Need maybe mention limitations: only public page, no backend, no engagement, no churn, no CAC, no testimonials, no platform, no country, no currency? Price $39 likely USD. Could be local? Need mark.

Need maybe answer in a professional teardown format. Need maybe include "Resumen ejecutivo".

Potential structure:
- Aclaración de método: lo que sé vs infiero.
- 1) Datos públicos verificados (high certainty)
- 2) Estimación de facturación (formula, scenarios, confidence)
- 3) Salud del negocio (signals, strengths, weaknesses, risks, score)
- 4) Cómo competir (positioning, offers, GTM, retention, 30/60/90)
- 5) Datos que necesito para afinar (checklist)
- 6) Conclusión.

Need maybe include calculations in Spanish with comma decimals? Use $ and maybe "MRR" and "ARR". Need maybe explain MRR: Monthly Recurring Revenue. ARR: Annualized.

Let's think deeper: Could "2.400 miembros" be on cover of membership platform like Circle, Skool, Discord, Patreon? Some platforms show "members" including free and paid. If Skool shows "members" maybe all members in community, some free? If "comunidad de pago" maybe all are paying? But could have free tier. Need mark.

Need maybe include "si el contador es de la plataforma y no del fundador, puede incluir miembros inactivos o de prueba". Good.

Need maybe estimate based on follower count: 60k followers. If 1% convert to email, 600; 10% buy? 60. But community might have 2,400 members from other sources. Need maybe use as sanity: 2,400 paid is 4% of 60k. For a niche automation audience, 4% paid is high but possible if they have multiple channels, past launches, YouTube, etc. If only 60k, maybe revenue lower. Need mark low.

Need maybe estimate engagement: 3 posts/week public. If public feed only, maybe to attract. Engagement unknown. Need maybe if 2,400 members, 3 posts/week is low? For active community, maybe enough if private activity. But public only 3/week suggests not heavy content. Need not infer.

Need maybe courses: 12 listed. If each course has 5-10 lessons, content library. But no completion. Could be "12 cursos" as modules, not finished. Need maybe if unfinished, could be a red flag for buyers expecting complete path. Need maybe competitor can market "cursos completos y actualizados".

Need maybe price: $39/month. In automation niche, could be low-to-mid. Competitors might charge $99-$299. If they charge $39, maybe volume play. Could be less sticky. Need maybe compete with premium or value.

Need maybe "cómo les compito" need not just generic; need specific attack vectors based on observed gaps:
- No annual plan visible: offer annual with 2 months free, ROI guarantee, templates.
- 12 courses unknown completion: offer "roadmap completo" with certification, updates, implementation.
- Public 3 posts/week: offer daily/weekly live, office hours, accountability, private Q&A.
- Founder 60k: hard to beat distribution; don't compete head-on initially. Niche and productize.
- $39: maybe undercut with $29? But better premium if outcomes. Or freemium with templates.
- Community of automation: likely broad. Niche: e.g., "automatización para agencias de marketing", "automatización para SaaS B2B", "automatización para e-commerce", "automatización para servicios locales", "AI operations for solo founders". Choose one. Need maybe suggest choosing based on your advantage.

Need maybe include "no competir solo por precio". Need maybe "competir por certeza de resultado".

Need maybe include "prueba rápida" with metrics:
- Landing page conversion >3% to waitlist.
- 20 interviews.
- 10 founding members at $99/mo or $990/year.
- CAC < $100, LTV > $300.
- Churn <8% monthly.

Need maybe include "si quiero atacar su base actual": create comparison page, migration offer, template pack, "audit de automatizaciones gratis", challenge 14 days.

Need maybe include "si no puedo comprar membresía": use public feed, search reviews, social mentions, app store? But if platform not public. Need maybe join to get full teardown.

Need maybe include "legal/ethical": don't scrape private, don't impersonate, use public info, disclose if you join for research. Good.

Need maybe final answer with certainty markers. Need be thorough but not too long? Desired oververbosity 9, so detailed.

Need ensure we don't claim actual revenue as fact. Use "estimación". Need maybe "No sé cuántos de esos 2.400 son pagadores actuales; por eso no puedo dar un número único con confianza." Good.

Let's draft in Spanish.

Potential final:

"Título: Teardown competitivo — Comunidad de pago de automatización"

"Método: Todo lo que no esté marcado como dato público lo trato como hipótesis. Uso etiquetas: [DATO PÚBLICO / ALTA], [INFERENCIA / MEDIA], [INFERENCIA / BAJA]."

Then table:
- Comunidad de pago en membresía: dato, high.
- 2,400 miembros en portada: dato, high that it says; but meaning low/medium.
- $39/mes: high.
- No annual visible: high that not visible; not necessarily doesn't exist.
- 3 posts/week public: high observed; engagement low.
- Fundador 60k: high; influence medium.
- 12 cursos: high listed; quality/completion low.

Revenue:
Formula: MRR = paid members * $39. ARR = MRR*12.
Scenarios table:
- 100% paid current: 2,400, $93,600 MRR, $1,123,200 ARR, certainty: high if assumption true, low overall.
- 70%: 1,680, $65,520, $786,240, medium-low.
- 50%: 1,200, $46,800, $561,600, low.
- 30%: 720, $28,080, $336,960, low.
- 15%: 360, $14,040, $168,480, low.
Maybe include "rango operativo: $15k-$95k MRR; punto medio prudente $45k-$65k MRR if 50-70% paid". Need not choose too definitive. Maybe "Si tuviera que operar con un número para planear, usaría $50k MRR como escenario base, con banda $25k-$95k, pero solo hasta validar." Mark low-medium.

Need maybe include "si hay plan anual no visible, cash flow could differ; if annual at $39*12, MRR equivalent same, but upfront cash higher and churn lower." Good.

Health:
Maybe table signals:
- Recurring model: positive [high]
- Public consistency: positive [medium]
- Content library: positive [medium]
- Distribution via founder: positive [high]
- Single-founder risk: negative [medium]
- No annual visible: ambiguous [low]
- Member count ambiguous: risk [medium]
- Course completion unknown: risk [low]
- Public engagement unknown: unknown [low]
Need maybe "health score: 6/10 potential, but uncertainty high". Could say "Potencialmente sano, pero no confirmable". Need maybe define: If 1,200+ current paid and churn <8%, likely healthy. If <500 paid, fragile. If 2,400 includes free, revenue much lower.

Need maybe "profitability": Digital membership high gross margin, but labor/content costs. If founder does all, high personal income but not scalable. If they pay team, margin lower. [low]

Competitive strategy:
Need maybe sections:
A. No atacar frontalmente al fundador con 60k si no tienes ventaja. Niche down.
B. Positioning options:
1. "Resultados en 14 días" vs "acceso a contenido".
2. "Automatización para [nicho]" vs general.
3. "Done-with-you" vs self-serve.
4. "Biblioteca completa y actualizada" vs 12 cursos unknown.
5. "Comunidad activa con office hours" vs public feed.
C. Offer stack:
- Entry: $29/mo or free templates/newsletter.
- Core: $99/mo implementation community.
- Annual: $990/year with bonuses.
- High ticket: $1,500-$5,000 audit/build.
Need maybe align with competitor $39. If they are low, you can be premium or value.
D. Acquisition:
- SEO/YouTube for specific automation use cases.
- Lead magnets: templates (Make, Zapier, n8n), calculators, checklists.
- Public teardowns, before/after.
- Partnerships with tools, communities, newsletters.
- Affiliate program.
- Founder content if you have audience.
E. Retention/churn:
- Onboarding with quick win in 7 days.
- Weekly live, office hours, template drops, certification, milestones.
- ROI dashboard, saved hours, revenue impact.
- Annual plan, loyalty discounts.
- Private channels, accountability pods.
F. Switching from competitor:
- "Migra tu stack de automatización" free audit.
- Comparison page (not defamatory): "comunidad vs implementación".
- 14-day challenge.
- Import templates, done-for-you setup.
- Guarantee.
G. 30/60/90:
- 30: buy membership, audit, 20 interviews, landing pages, lead magnet, waitlist.
- 60: launch pilot cohort 20-50, collect testimonials, refine offer, SEO/YouTube content.
- 90: scale acquisition, annual plan, partnerships, target $10k MRR.

Need maybe include metrics:
- To reach $10k MRR at $39: 257 members; at $99: 101; at $29: 345.
- To challenge $50k MRR at $99: 505 members.
- Target churn <8%, CAC < $100, LTV > $300, NPS > 40.

Need maybe "datos para reducir incertidumbre" checklist:
- ¿El contador de miembros es actual, histórico, free+paid?
- ¿Cuántos son activos 30 días?
- ¿Churn mensual?
- ¿Hay plan anual, descuentos, trials?
- ¿Calidad y completitud de cursos?
- ¿Engagement: comentarios, reacciones, DM, soporte?
- ¿Testimonios, casos, resultados?
- ¿Equipo, fundadores, dependencia?
- ¿Canal de adquisición: email, YouTube, SEO, paid?
- ¿Reseñas en Trustpilot, Reddit, Twitter, YouTube?
- ¿Ofertas de afiliados?
- ¿Dominio, emails, job postings?
- ¿Plataforma: Skool, Circle, Discord, Patreon? fees?
- ¿País/moneda?

Need maybe include "si me dejas ver 3 capturas más, afino". But user says all. Need maybe ask for more? Could include.

Need maybe ensure "distingues SIEMPRE entre lo que sabes y lo que estás infiriendo". We can make every bullet labeled. Maybe use bold tags.

Need maybe be careful with "sé" as AI: I don't actually know beyond user-provided. Could say "A partir de lo que me diste, lo que puedo tratar como dato público es...". Good.

Need maybe final conclusion: "No puedo afirmar que facturen $1.1M; solo que ese es el techo si 2,400 son suscriptores mensuales activos. Lo más probable es que esté entre $25k y $95k MRR, con incertidumbre alta. El negocio parece viable y con distribución, pero expuesto a dependencia del fundador y a la calidad/retención. Para competir, no ataquen de frente: nicho + implementación + precio premium + prueba pública + migración." Good.

Need maybe include "certeza" in final summary:
- Facturación: [INFERENCIA / BAJA-MEDIA]
- Salud: [INFERENCIA / MEDIA]
- Estrategia: [RECOMENDACIÓN / ALTA en lógica, baja en ejecución]

Need maybe mention "No se ve plan anual" could be because hidden behind checkout, not absence. Mark.

Let's consider if need use "factura" in Spain? "factura" can mean invoice. Use "facturación". Good.

Need maybe include "si el contador de 2.400 incluye miembros de prueba o gratuitos, la facturación puede ser mucho menor". Good.

Need maybe include "si es comunidad de pago, podría ser que todos los miembros paguen, pero algunas plataformas muestran 'miembros' como total de inscritos". Good.

Need maybe include "3 posts por semana en feed público" might indicate content marketing cadence, but if public only, maybe they use private for paid. Need mark.

Need maybe include "12 cursos listados, no se ve terminados" could be a moat if complete; if incomplete, a gap. Need mark.

Need maybe include "fundador 60k seguidores" is not revenue; conversion unknown. Need maybe estimate: If 1% of followers join and pay, 240 members = $9,360 MRR. If 4%, 2,400 = $93,600. So follower count alone doesn't prove 2,400 paid. Good.

Need maybe include "sanity check": 2,400 paid from 60k followers = 4% paid conversion from total followers. That's high but possible if followers are highly targeted and there are other channels. If only 60k, maybe more likely 300-1,000 paid. Mark low.

Need maybe include "si 2,400 es total histórico y actual paid 20%, MRR $18.7k". Good.

Need maybe include "no se puede evaluar churn desde fuera". Good.

Need maybe include "nivel de certeza" maybe in table:
| Conclusión | Base | Certeza |
| Facturación techo $93.6k MRR | aritmética | Alta si 2400 paid; Baja global |
| Rango plausible $15-95k MRR | supuestos | Baja-media |
| Negocio potencialmente sano | modelo recurring + contenido | Media |
| Riesgo dependencia fundador | solo un fundador visible | Media |
| Oportunidad de competir por nicho/implementation | gaps públicos | Media-alta |

Need maybe include "recomendación de acción inmediata": Buy membership for 30 days. This is important. Need maybe "auditoría de miembro" with questions:
- Onboarding: ¿te dan quick win?
- Feed privado: ¿cuántos mensajes/día, participación?
- Cursos: ¿completos, actualizados, con plantillas?
- Soporte: ¿resuelven dudas?
- Comunidad: ¿hay eventos, office hours?
- Retención: ¿hay retos, certificaciones?
- Churn: ¿por qué cancelarías?
Need maybe "no publiques capturas privadas; úsalas para estrategia".

Need maybe include "competir" maybe "no copies su modelo; explora su debilidad". Need maybe "si su comunidad es de automatización general, tú puedes ser 'automatización para X'".

Need maybe include "pricing strategy" details:
- If they are $39, you can position $99 as "implementation" not community. Or $29 as "starter templates". Need maybe avoid price war.
- Annual: $390/year (2 months free) or $468? If they don't show annual, you can offer. But if you charge $39, annual $390. If premium $99, annual $990.
- Guarantee: 14 days money back, or "si no automatizas X en 30 días, te devolvemos".

Need maybe include "message mapping":
- Their promise: access to automation community/courses.
- Your promise: "En 30 días tendrás 3 automatizaciones funcionando que te ahorran X horas / generan Y".
- Objection: "¿funcionará para mi negocio?" -> audit, templates.
- Objection: "¿tengo tiempo?" -> done-with-you, prebuilt.
- Objection: "¿ya tengo comunidad?" -> compare outcomes.

Need maybe include "GTM channels" based on automation audience:
- YouTube: "How to automate X with n8n/Make/Zapier".
- Twitter/LinkedIn: before/after, workflows.
- SEO: "n8n templates for [niche]".
- Newsletter: weekly automation teardown.
- Partnerships: tool affiliates, SaaS communities.
- Paid: maybe only after LTV known.

Need maybe include "KPIs to track":
- Waitlist conversion, CAC, activation (first template in 7 days), retention 30/60/90, NPS, revenue per member, churn.

Need maybe include "risk if you compete":
- They may have better distribution.
- Content moat if courses good.
- Community network effects.
- Price advantage.
- Founder authority.
Need maybe mitigations.

Need maybe final "veredicto":
- "No puedo confirmar facturación. Techo: $1.12M ARR. Escenario base prudente: $500k-$800k ARR? Hmm if 50-70% paid: $561k-$786k ARR. But if 30%: $337k. Maybe say "si tuviera que presupuestar para competir, asumiría que facturan entre $300k y $800k ARR, con posibilidad de $1.1M". Is that too high? Need be careful. Maybe "rango amplio: $200k-$1.1M ARR". Let's choose: "Rango plausible: $170k-$1.1M ARR; punto medio de trabajo: $500k-$800k ARR". But if 15% paid, $168k. Good. Need mark low.

Maybe use "escenario de trabajo" not actual.

Need maybe include "if 2,400 members are all paid, they could be a $1M business; that changes competitive response. If only 20% paid, it's a $200k business. Therefore first action is validate member count meaning." Good.

Need maybe include "what would make me change estimate":
- Reviews/testimonials showing active paid community.
- Job postings for community manager.
- Affiliate program.
- Public engagement high.
- Annual plan.
- Course completion.
- Founder mentions MRR.

Need maybe include "if they display 2,400 on cover, likely they care about social proof; could be paid or total." Good.

Need maybe use "teardown" term. Good.

Need maybe ensure no unsupported claims like "churn is high". Use "podría".

Let's draft final in Spanish with tables and tags. Need be concise enough but detailed.

Potential final:

```
## Resumen ejecutivo
No puedo saber con certeza cuánto facturan. Con los datos públicos, el techo aritmético es $93.600 MRR / $1.12M ARR si 2.400 son suscriptores mensuales activos. Mi rango de trabajo: $15k-$95k MRR, con mayor incertidumbre en el extremo alto. Salud: potencialmente sano, pero no confirmable; señales positivas de modelo recurring y contenido, riesgos de dependencia del fundador y métrica ambigua. Competencia: no atacar de frente; nichar, vender implementación/resultado, precio premium o paquete anual, y hacer auditoría de miembro.
```

Then method.

Need maybe include "Nivel de certeza" tags. Use [ALTA], [MEDIA], [BAJA]. Maybe define:
- ALTA: dato público o aritmética directa.
- MEDIA: inferencia razonable con supuestos.
- BAJA: hipótesis que requiere validación.

Need maybe in tables: "Tipo" and "Certeza".

Let's think if any legal issue? No.

Need maybe include "no se ve si hay plan anual" could be hidden after login. Mark: [DATO: no visible públicamente / ALTA]; [INFERENCIA: puede existir / BAJA].

Need maybe include "12 cursos listados, no se ve cuántos terminados" -> [DATO: 12 listados / ALTA]; [INFERENCIA: calidad/completitud / BAJA].

Need maybe include "3 posts por semana" -> [DATO: cadencia pública / ALTA]; [INFERENCIA: actividad real / BAJA].

Need maybe include "fundador 60k" -> [DATO / ALTA]; [INFERENCIA: capacidad de conversión / BAJA-MEDIA].

Need maybe include "comunidad de pago" -> [DATO / ALTA] but maybe free tier? [INFERENCIA / BAJA].

Revenue table:
Need calculate accurately:
2400*39=93,600. *12=1,123,200.
70%: 1680*39=65,520; *12=786,240.
50%: 1200*39=46,800; *12=561,600.
30%: 720*39=28,080; *12=336,960.
15%: 360*39=14,040; *12=168,480.
Maybe include 10%: 240*39=9,360; *12=112,320. But enough.

