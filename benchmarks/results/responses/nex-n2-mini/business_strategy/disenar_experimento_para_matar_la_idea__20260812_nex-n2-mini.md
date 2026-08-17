# Nex-N2-Mini — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 7.66 | quality: 8.0
- latency_total: 41.33s | tokens_per_second: 198.2
- input_tokens: 178 | output_tokens: 8192

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa


We need answer in Spanish. Need design experiment cheap fastest that can kill hypothesis: small marketing agencies pay $200/mo for tool automates client reports. User wants exactly what to do, cost, time, result that makes abandon. Need likely pre-sell/landing page? Need falsifiable. Need avoid "validation". Need "smoking gun" maybe fake door + manual concierge? Need design to kill: ask for payment commitments before building. Most cheap fast: 48-hour concierge offer to 30 agencies with payment upfront and 14-day pilot/manual. But need maybe fastest is "pre-sell at $200/mo with cancellation guarantee"? Need kill if no one pays. Need precise script, sample, criteria.

Need consider "small marketing agencies" broad. Need define segment. Experiment: target agencies 3-15 people, run paid ads/SMS/social for clients, send 5-20 reports/mo. Contact 50 owners. Offer done-for-you automated client report service for $200/mo, first month free? But if free then not kill. Need real purchase: ask for credit card, 14-day pilot at $200, cancel anytime. "If not useful, cancel and no charge after 14 days." But to kill, require paid pilot. Could also require they pay $200 now for 30-day pilot; "if not use, refund" maybe less kill. Pre-sell requires they pay now. But "pay $200/mo" means recurring. A one-time pilot maybe weaker. Need exact.

Need maybe "manual concierge" because if they won't pay for manual version, tool won't solve. But report automation can be sold as service. We don't need build.

Experiment: "Paid concierge fake-door" with a working prototype using Google Sheets/Canva/Looker Studio manually. We contact 40 agencies. Goal: 5 paid pilots at $200/mo from 50 qualified conversations. If <5 pay, kill. But if only 5 pay maybe continue. Need "most cheap and fast" maybe 3 days. Need include sample size and statistical confidence. Let's think.

Hypothesis: agencies small would pay $200/mo. Need falsify. We can test willingness to pay, not interest. Most conclusive: ask for payment upfront. Criteria: contact 100 qualified agencies; if fewer than e.g. 5 paid pilots out of 100 (5%) abandon. Or if 0-2. Need avoid false negatives due to bad outreach? Need sample enough.

Could design with a "kill switch": no building, no integrations. "I will personally deliver a report in 24h" maybe with Google Data Studio/Sheets. Offer: "Te hago el primer reporte de este mes gratis; si te sirve, pasamos a $200/mo con tarjeta y cancelable." But first free may not kill. Better: "Agenda de 15 min; te muestro demo; si te interesa, te dejo link de pago para $200/mo y te entrego primer reporte manual en 48h." Payment link. Need "exactamente qué hago".

Need maybe run both outbound and landing page? Fastest cheap: outbound direct. Landing page alone is not conclusive because no traffic. Outbound can be free/time. Need maybe paid ads not needed. Cost: $0-$100. Time: 48-72h.

Need include "elige 50-100 agencies" not broad. Need "small marketing agencies" not all. Need specify ICP. Need "agency with 3-20 people, clients in paid ads/SEO/social, sends reports monthly, uses Meta/Google/HubSpot/WordPress, can pay." Need not target huge agencies.

Need include "script" for email/LinkedIn/DM. Need include "offer" and "pricing". Need "deal-breaker" outcome. Need include "what counts as failure".

Let's formulate experiment:

Name: "Preventa de 14 días por tarjeta de crédito, entregado a mano."

Goal: determine if at least X% of qualified agencies will pay $200/mo.

Steps:
0. Define ICP and list 100 agencies (Apollo/Clay/Google Maps/LinkedIn/Facebook ad library). Cost $0-$50.
1. Build minimal sales page or Calendly and Stripe payment link. Not product, just checkout.
2. Outreach: 100 contacts, 2 touches over 24h. Script.
3. Offer: "En 48h te armamos el reporte automático de tu cliente X; si no lo usas/cancelas, te devolvemos. Primer mes $200/mo. No requiere integración: tú me das acceso/CSV; yo lo hago. Si funciona, seguimos mensual."
4. Qualify with 10-min call: How often reports? Current cost? Tools? Pain? Who pays? "¿Pagarías $200/mo today?" If yes, send payment link. If no, ask why.
5. Payment: Stripe checkout for $200. "14-day pilot, cancel anytime" or "first month $200, cancel anytime after pilot." To avoid refund abuse, maybe "first report delivered, then recurring." Need they pay to kill. Maybe $200 upfront; if not useful, refund. If they pay after seeing deliverable? Hmm.

Need decide kill criterion:
- Fail if fewer than 5 of 100 qualified agencies pay $200/mo, OR fewer than 3 pay without discount and without "I'd use it".
- More rigorous: If conversion from qualified calls to paid pilot <10% (e.g., 5 paid out of 50 qualified calls) fail.
- Also fail if any of top 5 reasons: price objection at $200, no recurring pain, "we already have template", "client doesn't value reports", "agency has no reporting budget", "they only want one-off".
- If after 100 targeted contacts, 0-2 paid, abandon. If 3-4 maybe pivot (niche/price/offer) not abandon? User asks result makes abandon. We can state "abandona si <5 paid pilots".

But maybe "most conclusive" is "sell 10 at $200/mo" with prepayment. Need not require many. If only 5% pay, enough to build? Need maybe "kill if less than 5 paid pilots" because small N. But maybe if 5 pay, not enough? Need "abandon idea if <3 paid pilots from 100 qualified contacts" maybe too low. Let's reason.

Hypothesis says "small agencies would pay $200/mo". We need test. If no one pays, fail. Need enough sample to be confident. Suppose 100 targeted agencies, 0 paid. If true willingness is 5%, probability of 0 is (0.95)^100 = 0.0059, so we can reject below 5% at 95%. If true 2%, probability of 0 = 0.133, not conclusive. If 1%, probability of at least 1 = 0.634. So 0 in 100 can reject >5% but not 2%. If true 10%, probability 0 = 0.000026. Good. If 5% true, chance of 0 0.6%. So if 0, strong evidence below 5%. If 1 paid, chance 0 or 1 with p=5% = (0.95^100)+(100*0.05*0.95^99)=0.0059+0.0312=0.037. So <2 paid rejects p>=5% at 95%. If 5 paid, cannot reject. But if p=2%, probability of >=5 is maybe 4.6%, so 5 paid rejects p=2%. Good. So "0-4 paid out of 100" could reject >2-5%. But maybe with 100 target. However outreach conversion may be low. Need count denominator: contacted vs qualified calls. If 100 contacted and only 10 qualified calls, 5 paid = 5% of calls, 5% of contacted. Good.

Maybe use "100 agencies, 2 touchpoints, 72h". Cost $0-$100. Time: 2 days. "If you get <5 paid pilots, abandon or pivot." Need exact.

But "más barato y más rápido" maybe "ask for credit card before building" is enough. Could be done in 24h. Need maybe "fake door test" with paid checkout. But fake door can be misleading if people click but don't pay. Better "manual concierge pre-sell".

Let's build robust experiment:

"Experimento de muerte: 100 contactos, 5 pagos reales de $200/mo."

Detailed:
- Day 0 morning: Define ICP and offer.
- Day 0 afternoon: Create Stripe payment link for $200/mo "Pilot 14 días / cancelable"; landing page copy with "No build; done-for-you".
- Day 0-1: Build list of 100 agencies from ICP. Use Google Maps/LinkedIn/Apollo. Ensure they send reports: job title, client type, mentions "reporting", "monthly report", "client reporting", "analytics", "dashboard"; agency size 2-25.
- Day 1-2: Send personalized outreach:
Subject: "¿Cuánto te toma armar reportes?"
Message:
"Vi que hacés [ads/SEO/social] para [sector]. ¿Cuánto tiempo les llevas armar los reportes mensuales a clientes? Estoy probando un servicio que entrega reportes automatizados a $200/mes, entregado a mano al inicio. Si te interesa, te hago el próximo reporte gratis? Actually no free. Let's script:
'Estoy validando si agencias como la tuya pagan $200/mes por reportes a clientes hechos automáticamente. Para no vender humo, lo entrego a mano durante el piloto: me pasas acceso/CSV y en 48h te devuelvo un reporte listo para cliente. Si no lo usas, cancelas. ¿Te lo muestro/quieres probarlo este mes?'"
Need include ask for payment? Maybe after interest:
"Si te sirve, te dejo checkout por $200; arrancamos con tu próximo reporte y lo cancelamos cuando quieras."
- Follow-up: "¿Sigue siendo relevante? Si no, dime si es precio/dolor/no reportes."

- Qualification questions:
1. ¿Cuántos clientes reportan?
2. ¿Cada cuánto?
3. ¿Con qué herramienta hoy?
4. ¿Qué te cuesta? (time, frustration, client churn)
5. ¿Quién decide y paga?
6. ¿Si el primer reporte sale en 48h, ¿pagas $200/mo para que se repita?
- If yes send Stripe link.
- After payment, deliver manual pilot using Looker Studio + Sheets + ChatGPT? Need no build. But if they pay, we need fulfill. For "kill" experiment, if no payments no fulfillment. If payments, deliver 1 report manually. But if goal is kill, maybe no need. But exact "what do I do" includes if they pay.

Potential issue: If we offer "first report free" then no payment. Better "paid pilot." Could offer "first report included, paid upfront." "No charge after first month unless you continue" maybe. To be fair: "Stripe $200; if after first report you don't use it, refund and no further charge." This is less risk. But if they won't pay even with refund, fail.

Need include "do not accept 'me interesa' or 'guarda info' as success." Need "no success from calls, demos, 'would use', free pilots."

Need include "kill result":
- After 100 targeted contacts and 2 follow-ups, abandon if:
A) fewer than 5 paid pilots at $200/mo, OR
B) fewer than 3 agencies say they currently spend >3 hours/month or pain enough, OR
C) paid pilots only happen if discounted < $100 or one-off.
- I would "abandon idea as stated" if 0-4 paid out of 100 targeted agencies. Maybe "pivot only if there is a consistent pattern."
Need maybe "If 5-10 paid, continue to build minimal automation."

Need maybe mention "sample size and confidence":
- If we contact 100 agencies and 0 paid, we can reject >5% WTP with 95% confidence (rough math). If 1-4, less definitive but likely. Maybe "0 paid is the clean kill; 1-4 is near-kill; 5+ continue." But user asks result that makes abandon. Could say "abandon if 0 paid; consider pivot if 1-4 with reasons." But "can kill conclusively" maybe 0 is conclusive. Need decide.

Let's think more deeply about experimental design.

Hypothesis: "small agencies would pay $200/mo for tool automates reports." The critical variable is WTP. A cheap test is "pre-sell with payment." But need be careful: "would pay $200/mo" could mean "after product exists" not "service." A pre-sell for manual service tests "agencies have pain and pay for outcome"; if they don't pay for manual, they won't pay for tool. It is a "concierge MVP" and "fake door".

Alternative: "Charge $200 now for a done-with-you report" may be even cheaper: ask for $200 deposit to deliver one report. But hypothesis is monthly recurring. A one-time $200 may overstate WTP. Better "monthly recurring paid pilot."

Could use "founder-led concierge with manual work" and "prepaid." Cost: time only. But the user asks "plata" not time? "Tiempo y plata". We'll list.

Could include "budget $50 for data list + $25 for Stripe (no upfront) + $0 domain." Maybe if no domain use Carrd $19/mo. Total $20-$100.

Need maybe include "exact copy." Let's craft in Spanish. Need maybe with "no valides con respuestas; solo dinero."

Let's design in a structured way:

Title: "Experimento de muerte: 100 agencias × $200 prepagados × 72 horas."

Objective:
- Falsify: if less than 5% of qualified agencies pay $200/mo for a paid 14-day pilot, assumption is false/not worth building.
- Success to continue: at least 5 paid pilots.

Why this kills:
- It removes feature interest; requires real money.
- It tests pain and budget, not interest.
- Manual fulfillment reveals if outcome is valuable; if they won't pay for manual, automation won't fix.

ICP:
- Agencies 3-20 people, B2B/ecommerce/local services? Need choose one segment to reduce noise. Maybe "agencias de performance (ads/SEO) con 5-30 clientes y reportes mensuales". We can say "no empieces con todas las agencias; elige un subsegmento: agencias de performance con 5-50 clientes, usan Meta/Google Ads."
- Need because "small marketing agencies" broad. We can say "define ICP in 20 min; if no segment, experiment too noisy."

Steps:
1. Prepare offer and checkout (2 hours).
- Landing page: headline "Reportes de clientes automatizados para agencias de performance — $200/mes".
- Bullets: "en 48h, reporte listo, editable, white-label, para clientes, con métricas de Meta/Google/SEO/CRM."
- Button "Probar 14 días — $200".
- Payment link: Stripe/ MercadoPago/PayPal. "Cancelable después del primer reporte; si no lo usas, te devuelvo."
- No calendar? Use Calendly.

2. List 100 agencies (2 hours).
- Sources: Google Maps, LinkedIn, Meta Ad Library, Clutch, agencies in city. Filter.
- Find 1-2 contacts (founder, account director, owner).
- Score qualification:
- 5+ clients
- reports monthly
- uses ads/analytics
- agency size 3-30
- owner accessible.
- Cost: $0-$50.

3. Outreach (1-2 days).
- Send 100 personalized emails/LinkedIn/DM. 2 touches.
- Script:
"Hi [Name], vi que [agency] trabaja con [clients]. ¿Cuánto tiempo les toma armar reportes mensuales hoy? Estoy probando un servicio para agencias de performance: reportes listos para cliente en 48h por $200/mes. Para no vender software, lo entrego a mano al inicio; si no lo usas, cancelas. ¿Te tiene sentido probarlo con tu próximo reporte?"
Follow-up:
"¿Sigue siendo dolor? Si la respuesta es no, dime por qué: precio, no hay reporte, ya lo resuelven, no es prioridad."
Maybe too "free"? "entrego a mano" not free. "Primer reporte incluido" maybe.
Need ask "¿te lo muestro o lo pagamos?" Let's make it explicit:
"Si te interesa, te paso el checkout de $200; te entrego el primer reporte en 48h y si no lo usas te devuelvo."
This makes the offer clear.

4. Calls:
- 10-15 min only if interested.
- Ask:
- "¿Qué reporte haces y cada cuánto?"
- "¿Qué herramienta usas?"
- "¿Cuánto tiempo cuesta?"
- "¿Qué pasa si no se lo das?"
- "¿Quién paga?"
- "Si te entrego uno en 48h por $200/mes, ¿quieres arrancar hoy?"
- If yes: payment link. If not: record reason.
- Do not offer discounts. If they ask discount, say "No; estoy probando precio $200. Si no te cierra, perfecto, me da dato." This is important.
- If they want free: "No; el experimento requiere pago. Si no, lo descarto."

5. Payment:
- Stripe checkout: "$200/mo; pilot 14 days; cancel anytime after first report; refund if not used." Maybe "no auto-renew until first report accepted"? Need not.

6. Fulfillment if paid:
- Ask for client source/CSV.
- Use Google Sheets + Looker Studio/Canva + ChatGPT manually. Deliver in 48h.
- But if goal kill, maybe if they pay then you continue. But for experiment, "if 5+ pay, stop building and deliver manually for 2 weeks to see retention." Need include.

7. Results:
- Track:
- contacted
- replied
- qualified
- paid
- reasons no.
- Kill threshold:
- "Abandona si de 100 agencias calificadas contactadas, menos de 5 pagan $200/mo."
- "Abandona inmediatamente si 0 pagan."
- "Considera pivotar si 1-4 pagan solo porque ya tienen un problema urgente; no construir aún."
- Need maybe "if 5+ pay, do not build yet; continue concierge 2-4 weeks to test retention at $200." But user wants before building. Could say after paid, you still don't build; you run concierge.

Need maybe include "abandon if..." with reasons:
- If objections cluster around price ($200 too high), no enough reports, reports are not a pain, they use templates, clients don't care, they need integrations more than reports, they won't pay monthly.
- If paid pilots ask for integrations/one-offs/under $200, then "tool as stated" is false.

Need maybe include "what would make you abandon after seeing paid but no retention" e.g., if they don't use after first report. But the user wants before building. Could include "if they pay but don't use, that's a second kill: not recurring." But the main experiment is prepayment. Maybe "post-payment check: if they don't open/use report, kill."

Need maybe "what if they say yes on call but don't pay?" That's failure; record as "interest without WTP."

Need maybe "minimum viable sales page copy" in Spanish:
"Reportes de clientes en 48h para agencias de performance
Nadie quiere perder domingo armando PDFs. Te entregamos un reporte mensual listo para reenviar a tus clientes, con métricas de Meta/Google/SEO, resumen ejecutivo y acciones recomendadas. $200/mes. Piloto de 14 días; cancelas cuando quieras."
Need include "manual at start" "No integraciones todavía."

Need maybe "outreach list criteria" more exact:
- "3-25 empleados"
- "servicio: performance marketing, SEO, social media"
- "tienen 10+ clientes"
- "publican casos de éxito"
- "usa HubSpot/GoHighLevel/AgencyAnalytics/ReportiQ/Metricool" maybe not necessary.

Need maybe "cost breakdown":
- Stripe: $0 upfront.
- Carrd: $19 for 2 days? Actually $19/year.
- Apollo/Clay: free trial or $0.
- Domain optional $0.
- Total: $0-$50; maybe $20-$100.
- Time: 4-6 hours setup + 2-3 hours outreach + 1 hour follow-up/calls? Total 1-3 days.
Need "most cheap and fast" maybe "24-48h".

Need maybe "script in Spanish." Let's craft.

Potential challenge: "small agencies" can be many. Need "sample size 100" not too many. Maybe "100 targeted agencies" enough. "If no payment, you're likely wrong." But if only 100 contacted, conversion from cold outreach to paid may be low due to channel. Need ensure "qualified conversations" denominator. Maybe "minimum 50 qualified calls" more robust. But time. Let's think.

If contact 100 cold, response 10%, 10 calls. If true WTP among qualified is 30%, expected 3 paid. A 5 paid threshold may be too high if only 10 qualified. But if only 10 qualified, you don't have enough. But the experiment "kill" should be based on "qualified conversations". We can set:
- Get 50 qualified conversations (not 100 cold). If after 50 qualified conversations fewer than 5 pay, fail.
But getting 50 qualified conversations from cold in 2 days is hard. Maybe with warm referrals. Could use "warm intro to 20 agency owners" etc.

Need design "as cheap/fast as possible" maybe use warm network/referrals to get conversations faster. But user didn't mention network. Could use "cold outbound to 100; if <10 qualified calls, continue or fail? The sample is not enough." Need exact.

Maybe "100 targeted contacts; stop early if after 30 qualified conversations <3 paid and objections are price/no pain." But for conclusive, need 50 qualified.

Alternative "interviews with 'paywall' at end" maybe:
- Call 20 agency owners.
- At end ask "If I could do this, would you pay $200/mo? If yes, can we set up Stripe now?" If yes, payment link.
- If yes but no payment, no.
This can kill faster. But sample 20 not conclusive. Need "fastest" maybe "20 calls, 0 paid = kill with confidence? If true WTP 20%, probability 0 paid in 20 = 0.12%, strong. But if true WTP 5%, probability 0 = 36%, not conclusive. So 20 qualified calls can kill if WTP >10% but not if 5%. But for founder, maybe enough to not build.

Could combine: "Call 30 agency owners, ask for payment; if <3 paid, kill." But user wants "concluyente". Need enough sample.

Let's formulate "kill if 0 paid after 50 qualified calls" because if true WTP 10%, P0=0.000001; if 5%, P0=0.077. Good. If 1 paid, P0/1 with p=5%=0.077+0.272=0.349, not conclusive. But 0 is conclusive for >5%. Need maybe "0 paid is clean kill." For 1-4, not conclusive but likely. But user asks result that makes abandon. We can say "abandon if 0 paid; if 1-4, run one more segment/offer but don't build." Hmm.

Maybe "most conclusive kill" is "0 paid from 100 targeted agencies" because p=5% probability 0.6%. That's strong. If only 0 paid, abandon. If 1-4, "not enough? It's not conclusive but likely; I'd pivot." But user wants "cuál sería el resultado que me hace abandonar la idea" singular. We can set "abandon if <5 paid out of 100 targeted agencies." That is a threshold. It is not mathematically conclusive if true WTP 3%; but enough? Maybe with 100, <5 paid: if true 5%, P<5 ~22%; not conclusive. But if true 2%, P<5 ~63%; not conclusive. But we don't need prove WTP >2%, just decide not build. We can say "this is a business decision, not statistical proof." But "MATAR de forma concluyente" maybe need "0 paid" is conclusive.

Let's maybe design "two-stage kill":
- Stage 1: "0 paid after 100 targeted agencies" = kill.
- Stage 2: If 1-4 paid, don't build; do one diagnostic pivot. But user wants abandon idea maybe if 1-4 paid because too few.
Need maybe include "if 0 paid, abandon immediately; if 1-4, abandon as stated and pivot only if pattern is strong." That covers.

Could also design "ask for a paid letter of intent with cancellation clause" not just checkout. But payment is better.

Need maybe "manual concierge" to avoid building. Need maybe "no integrations; use screenshots/CSV." It tests value not automation.

Need maybe "the fastest test is not a landing page; it's a checkout link and a founder-led service." Good.

Need maybe "pre-sell with a fake integration" not enough. Need "manual delivery."

Let's think of possible edge cases:
- If agencies already use AgencyAnalytics, they may not need tool. But maybe tool automates from multiple clients. Need target those with pain.
- $200/mo may be high for very small agencies. Need target agencies with enough clients. If agency has 3 clients, $200/mo per agency maybe too high; but if reports are painful, okay. Need ICP includes 10+ clients and owner personally does reports.
- If they pay $200/mo for a tool, they may need integrations. If they don't want to pay without integrations, maybe not. But pre-sell should mention "no integrations needed at pilot; CSV/access." If they require integrations before paying, hypothesis may be false.

Need maybe "script for qualifying 'small marketing agencies'". Example:
"¿Cuántos clientes tienes y cuántos reportes haces al mes?"
If <10 clients or report quarterly, exclude.
"¿Te toma más de 1h/cliente?"
If no, exclude.
"¿Pagas actualmente $200/mo por algo que te ahorra reportes?"
If no, maybe not.

Need maybe "exact landing page" with "Cancelación" to reduce friction:
"Pagas $200 hoy. Te entrego tu primer reporte en 48h. Si no lo usarías, te devuelvo y no seguimos. Si te sirve, continuamos $200/mes; cancelable cuando quieras."
This is fair.

Need maybe "what not to do":
- Don't run Facebook ads to landing page; no traffic.
- Don't ask "would you use this?"
- Don't offer free pilots.
- Don't build integrations.
- Don't use 'interested' as success.

Need maybe "result that kills":
- 0 paid after 100 targeted contacts: "abandon"
- <3 paid among 50 qualified calls: "abandon or pivot; no build"
- Paid but only after discount < $100: "kill $200 price"
- They pay but churn after first report: "kill recurring value"
Need include "hard kill: no one pays."

Let's craft final answer in Spanish with sections:
1. "Experimento: Preventa manual de $200/mo"
2. "Objetivo y criterio de abandono"
3. "Preparación"
4. "Ejecución día por día"
5. "Guion"
6. "Resultados"

Need maybe include "cost and time":
- Cost: $0-$50 (Carrd $19, Apollo free, Stripe no upfront).
- Time: 24-72 hours.
- Your time: 6-10 hours.
Need "exact amount" maybe "Cuesta $20-$100; tarda 2 días." Let's specify:
- Carrd/pro landing page: $19
- Data: $0-$50
- Payment: $0 upfront
- Total: $19-$69.
If using no domain, $0. "Máximo $70."

Need maybe "sample size 100" exact. "Contacta 100 agencias, no 30."
Need maybe "If after 100 targeted agencies and two follow-ups you have <5 paid pilots, abandon. If 0 paid, abandon immediately." The user asked "cuál sería resultado que me hace abandonar la idea." We can say "Abandónalo si menos de 5 pagan; el caso claro es 0-4." But maybe "most conclusive" is "0 paid." Need maybe "hard rule: 0 paid = kill; <5 paid = abandon as stated." Let's decide final.

Let's think of "falsabilidad":
Hypothesis: "small agencies would pay $200/mo" = if there exists a segment. If you test broad small agencies, a negative is hard to interpret due to targeting. So define "small performance agencies in [country/city] with 5-50 clients." If they don't pay, you know that segment. To "kill the idea" maybe need "no segment pays" not just one. But the user likely wants kill broad. We can say "para matar la hipótesis general, prueba 3 subsegmentos: performance, SEO, social media; or pick one and kill that segment. If you want one experiment, pick performance agencies with 10+ clients." Hmm.

The user said "las agencias de marketing pequeñas" broad. The experiment should "matarla" broadly. But broad markets need segmentation. We can propose "do not test all; pick a narrow ICP. If that fails, maybe pivot. To kill broad idea, run the same paid pre-sell to 3 subsegments." But that's more time. They want fastest. Maybe "fastest is one ICP." But if it fails, you don't know broad. However if even the pain-bright ICP doesn't pay, likely broad won't.

Maybe define ICP:
- "agencias pequeñas de performance (Meta/Google Ads/SEO) con 5-30 clientes, reportes mensuales, dueños que todavía arman reportes."
This is the segment most likely to pay. If they don't pay, kill likely.
Need maybe include "si no contactas a quienes realmente sienten dolor, el experimento no mata."

Need maybe "manual report service" with "white-label." Need "small agencies might not want reports automated; they might outsource or use templates." Payment test reveals.

Let's maybe include "exact deliverable":
"Reporte mensual listo para enviar: resumen ejecutivo, métricas de campañas, cambios recomendados, captura de gráficos, 1 página de acciones."
But avoid building.

Need maybe "what to do after payment":
- If someone pays, you need fulfill or else you learn nothing. But maybe not necessary for kill. Yet if you get 5 paid, you should not build yet; do concierge.
- But the user wants "before building" and "experiment to kill." We can include "si alguien paga, no construyas; hazlo a mano durante 2 semanas."
Need maybe "if someone pays but says 'solo si hay integraciones'—kill."

Let's write in Spanish.

Potential final structure:

```
Haz este test: "venta manual prepagada".
Objetivo: 100 agencias calificadas; 5 pagos reales de $200/mo.
Duración: 48-72h.
Costo: $20-$70.

Regla de abandono:
Abandona si <5 de 100 agencias calificadas pagan $200/mo.
Caso claro: 0 pagos = la hipótesis está muerta.
No cuentes llamadas, leads, 'me interesa', demos, free pilots.

Oferta:
"Te entrego reportes mensuales para tus clientes en 48h, white-label, por $200/mo. Piloto de 14 días. Pagas hoy; si no usas el primer reporte, te devuelvo. No hay integraciones; me pasas acceso/CSV."

Paso 1...
```

Need include "script" maybe:
Email:
```
Hola [Nombre], vi que [Agencia] trabaja con [tipo cliente].
Pregunta rápida: ¿cuánto tiempo les toma armar reportes mensuales hoy?
Estoy probando un servicio para agencias de performance: reportes listos para cliente en 48h por $200/mes. Para validar sin vender humo, lo entrego a mano al inicio; me pasas acceso/CSV y te devuelvo un reporte listo. Si no lo usarías, cancelas y te devuelvo.
¿Te tiene sentido probarlo con tu próximo reporte?
```
Follow-up:
```
¿Sigue siendo dolor? Si no, dime si es precio, ya lo resuelven, no reportan o no es prioridad.
```
Need maybe "if they ask 'free'":
```
No lo hago gratis; estoy midiendo si hay pago real. Si no te cierra, perfecto.
```
Need maybe "if they ask 'discount'":
```
No descuento; $200 es el precio de prueba.
```

Need maybe "call script":
```
¿Cuántos clientes tienes?
¿Cuántos reportes haces al mes?
¿Cuánto te toma?
¿Qué herramienta usas?
¿Qué pasa si no lo mandas?
¿Quién paga?
Si te entrego uno en 48h por $200/mes, ¿quieres arrancar hoy?
```
Need maybe "qualify out if:
- fewer than 5 clients,
- no monthly reports,
- no owner decision,
- no time pain.
```

Need maybe "data tracking table":
Columns: agency, segment, clients, reports/month, current tool, reason no, paid?
Need maybe "result:
- Paid pilots = success to continue concierge.
- No paid = kill.
- If 1-4 paid: no build; analyze if they are outliers; run one pivot (price/segment) but not tool.
```

Need maybe "mathematical confidence":
"Con 100 contactos, si la disposición a pagar real fuera 5%, la probabilidad de ver 0 pagos es ~0.6%. Si ves 