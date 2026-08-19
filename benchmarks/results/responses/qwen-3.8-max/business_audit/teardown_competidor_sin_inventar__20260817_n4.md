# Qwen 3.8 Max — business_audit/teardown_competidor_sin_inventar

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 4.03 | quality: 4.0
- latency_total: 49.262s | tokens_per_second: 41.6
- input_tokens: 231 | output_tokens: 2050

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

We need answer in Spanish. User asks competitive teardown with limited public info. We must distinguish known vs inferred, mark certainty. Need probably provide estimates of revenue, health, competition strategy. Need be careful: cannot know exact revenue. Need maybe scenario modeling. Need mention assumptions: 2,400 members could be total registered, active paying? $39/mes visible. Public feed 3 posts/week. Founder 60k followers. 12 courses listed unknown completion. Need estimate monthly recurring revenue (MRR). Need ranges: if all 2,400 paying at $39 = $93,600/mo, $1.12M/yr gross. But likely not all paying; maybe free members, churn, discounts, annual, trials. Need infer. Could use public '2.400 miembros' maybe social proof; if displayed as paid members? Unknown. Need mark certainty: known facts vs inferences. Need provide methodology and sensitivity table. Need competitive strategy: differentiate, positioning, funnel, content, offer, pricing, retention, community, courses. Need maybe red flags / risks. Need ask for more data? Could include hypotheses and what to validate.

Need satisfy "Eres analista competitivo. Distingues SIEMPRE entre lo que sabes y lo que estás infiriendo, y marcas tu nivel de certeza." So structure: 1) Hechos observados (certeza alta). 2) Inferencias (baja/media/alta). 3) Modelos de facturación with scenarios. Need calculate.

Let's compute. Price $39/mes. If 2,400 paying: monthly $93,600. Annual $1,123,200. If some annual? unknown. If 10% annual at maybe $390 (2 months free?) etc. But no visible annual. Could ignore or mention. Need estimate paying members from 2,400. The phrase "Muestra '2.400 miembros' en la portada." Could be total members not paying. If membership platform, could show number of members maybe all members including free? Need infer. If paid community, likely paying? But could include free trial, free tier, alumni, churned? Need not assume.

Need produce revenue ranges: Conservative, Base, Optimistic.
Need choose plausible conversion from followers to paid. Founder 60k followers. Typical conversion to paid community maybe 0.5%-3% of audience, or if 2,400 paying, that's 4% of 60k (high but possible if niche engaged). If 2,400 total members, paid could be 300-1,500. Let's create scenarios:
- Pesimista/conservador: 250-600 paying. MRR $9.75k-$23.4k; ARR $117k-$281k.
- Base: 800-1,200 paying. MRR $31.2k-$46.8k; ARR $374k-$562k.
- Optimista: 1,800-2,400 paying. MRR $70.2k-$93.6k; ARR $842k-$1.123M.
Maybe if 2,400 is displayed as members and no free tier, maybe high certainty that paying? But not necessarily. Need label.

Could also estimate revenue using audience size: 60k followers, conversion to paid membership: low 0.5%=300, base 1.5%=900, high 3%=1800. At $39: $11.7k, $35.1k, $70.2k MRR. If 4%=2400, $93.6k. This aligns.

Need business health: Need metrics unknown: churn, LTV, CAC, engagement, content cadence, course completion, founder dependency. We can infer from public signals: 3 posts/week is moderate/consistent, suggests active content ops. 12 courses listed could indicate library breadth but unknown depth/completion. Founder 60k followers suggests distribution asset but key-person risk. Price $39 is low-mid B2C/prosumer; needs volume and retention. If MRR under $30k, may be founder-led modest business; if $70k+, likely small team. Health depends on churn: monthly churn 5% means need 5% new members just to maintain. Need calculate required new members for scenarios. For 2,400 paying at 5% churn: 120 new/mo to maintain; at $39 = $4,680 new MRR needed. At 10% churn: 240 new/mo. If 800 paying at 7% churn: 56 new/mo. Need mention.

Need maybe estimate costs: platform, content production, community management, ads, founder time. Margins likely high gross (digital), but net depends on team/ads. If $93k MRR could support small team; if $20k MRR lean. Need not overstate.

Need how compete: Not attack head-on if they have audience. Differentiate: niche sharper, outcome-specific, higher-ticket, done-with-you, B2B, local/language, vertical automation, templates, accountability, certification, ROI. Build funnel: lead magnet, email, community free, challenge, webinar, case studies. Pricing: maybe $79-$199 if outcome stronger, or annual. Content: focus on proof, implementation, use cases, not generic posts. Retention: onboarding, quick wins, office hours, templates, community rituals. Need validation: scrape? manually observe: free trial? ask members? check social comments, testimonials, job postings, platform badges, course updates, refund policy, affiliates. Need mention legal/ethical: only public info, no scraping private, no fake accounts? Could use public pages, Wayback, LinkedIn, job ads, reviews. Need maybe provide "teardown" with table: señal, lo que sé, lo que infiero, certeza, implicación.

Need final answer in Spanish. Need include explicit certainty levels: Alta, Media, Baja. Need state cannot know exact facturación; only ranges. Need maybe say "No puedo afirmar". Need include formulas.

Let's craft thorough answer.

Potential structure:
1. Resumen ejecutivo: No se puede saber facturación exacta. Rango probable. Business likely viable but dependent on churn and founder audience. Competition strategy: don't clone; pick wedge.
2. Datos observados (certeza alta): list.
3. Inferencias con certeza:
- 2,400 members may be total or paying; if paid, max MRR 93.6k. If total, paying maybe 20-80%. etc.
- $39/mes likely entry price; no annual visible. Could be only plan.
- 3 posts/week indicates content engine but not necessarily engagement.
- Founder 60k is distribution, but conversion unknown.
- 12 courses listed: breadth, but unknown completion/quality.
4. Revenue model:
Assumptions: paying members = 2,400 * paid_share. Price net = $39 (ignore fees, annual). Table scenarios:
Conservador: paid_share 15-30% => 360-720; MRR 14k-28k; ARR 168k-337k? Wait if 15% of 2400 = 360 *39=14,040; 30%=720*39=28,080; ARR 168,480-336,960. But earlier I had 250-600. Could set.
Base: 35-60% => 840-1440; MRR 32.8k-56.2k; ARR 393k-674k.
Optimista: 75-100% => 1800-2400; MRR 70.2k-93.6k; ARR 842k-1.123M.
But if 2,400 is explicitly paid members, then base/optimistic maybe high. Need present as "si 'miembros' = paid". Could present two models: A) 2,400 all paying (techo máximo). B) more realistic total members.

Maybe use a sensitivity table with paying members: 300/600/900/1,200/1,800/2,400. MRR/ARR. Include fees? Payment processing 3% + platform. Could mention net revenue after fees ~ -3-6%. If annual discounts, effective ARPU lower.

Need include "facturación bruta mensual" and "neta aproximada". For $39, Stripe/PayPal ~2.9%+0.30 => effective $37.5? $39 - ($1.13+$0.30?) 2.9% of 3