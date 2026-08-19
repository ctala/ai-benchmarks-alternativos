# Qwen 3.8 2.4T (A95B) — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 6.86 | quality: 8.0
- latency_total: 71.103s | tokens_per_second: 115.2
- input_tokens: 217 | output_tokens: 8192

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

We need answer in Spanish. User wants experiment design to kill hypothesis cheaply/fast. Need be experienced founder, focus on falsifiable test. Need exact what to do, cost, time, abandonment result. Need likely propose landing page / cold outreach / pre-sale / concierge test? Hypothesis: small marketing agencies would pay $200/mes for tool automating client reports. Need cheapest fastest kill. Could design a demand-side test: offer a paid pilot or pre-order with money, not just interest. Need avoid building product. Perhaps direct outreach to 50-100 small agencies with a concrete offer: "We will manually automate your next client report for $200/month, cancel anytime, setup this week" or "prepay first month $200 to get done-for-you reporting automation". The fastest kill: get commitments/payment. Could use landing page + cold email/LinkedIn. But to kill, need high-intent signal: credit card or signed LOI? For B2B SaaS $200/mo, likely can get 5 paying pilots. If cannot get 3-5 paid commitments from 50 targeted conversations, kill. Need exact steps.

Need think deeply: What is riskiest assumption? They have pain enough and pay $200/mo. Small agencies may not pay because reporting is annoying but not $200/mo, or they already use AgencyAnalytics, DashThis, Swydo, Whatagraph, Looker Studio. Need test against existing alternatives. The experiment should be able to fail conclusively. Need not validate. Need design that if no one pays/commits after sufficient sample, abandon. Could be "sell before build" with a fake door? Ethical? Offer manual service as if tool. Maybe "concierge MVP". Cheapest: direct outreach + Calendly + Stripe payment link. Offer: "Report automation pilot: $200 first month, we set up automated white-label client reports from your current data sources. If not save 5 hours/month, refund." Need collect payment. If can't get payments, idea dead. But maybe need define target: small marketing agencies 1-10 employees, managing >=5 recurring clients, currently spending >4h/month reporting, using GA4, Meta, Google Ads. Need sample size. 100 personalized emails/LinkedIn, 10 calls? Time 5-7 days, cost $0-$150 (domain/email tools). Need threshold: after 100 qualified contacts and 10-15 demos/calls, <3 paid pilots or <2 payments? Kill. Or if CAC too high? For kill, maybe zero payments after 50 meaningful conversations. Need be rigorous.

Need perhaps propose "micro pre-sale" with a price point. Since hypothesis says would pay $200/mes. The strongest test is ask for $200 now. Not ask "would you pay". Need exact script. Need include control: existing tools. Maybe ask for current reporting stack and if they'd switch. Need kill criteria: If you contact 60 agencies and cannot close 3 paid pilots (or 5 if more generous), kill. Need statistical? With 60 contacts, 3 payments = 5% conversion from contact; if no payments, likely low. But need enough to detect. Could set: 50 calls/demos? Need fastest. If direct outreach response rates low, need not confuse bad outreach with no demand. To make conclusive, need high-quality targeting and compelling offer. Use communities? Maybe Facebook groups, LinkedIn, Slack, agency directories. Fastest might be recruit from existing network or places where agencies hang out. Offer a "done-for-you report automation sprint" $200. If no one buys after 30 direct conversations with qualified agencies, kill. But to avoid false negative due to poor copy, maybe run two variants? Need keep cheap.

Potential experiment: "The $200 invoice test". Create a one-page offer: "Automatizo tus reportes de clientes por $200/mes. Si en 7 días no te ahorra 4+ horas, te devuelvo el dinero." Use Stripe payment link. Contact 100 small agencies via email/LinkedIn. Offer 15-min diagnostic. If they say yes, send payment link before building. If they won't pay, not valid. Could also offer manual concierge: you use existing tools/Zapier/Make/Looker Studio to deliver. This tests willingness to pay and problem severity without custom product. Cost: $0 if use free tiers; domain $10, email $5, Stripe fee, maybe Apollo/Instantly $50. Time: 1 week outreach, 1 week closing. Total 7-10 days, <$100.

Need answer with exact steps: Day 0 define ICP, list, offer. Day 1 build landing/payment. Day 2-5 outreach. Day 6-8 follow-ups/calls. Day 9 evaluate. Include scripts. Include qualification questions. Include kill metric. Need mention if response rate too low? Need ensure experiment can fail due to bad list/copy. To make it conclusive, set a minimum number of qualified conversations. If can't get 20 qualified conversations, test invalid? But user wants result that makes abandon. Need maybe separate failure modes: no qualified meetings = distribution problem not necessarily idea; no paid after meetings = demand dead. But they asked kill hypothesis. Need design so if can't get payments after enough exposure, abandon. But to avoid false negative from poor outreach, include "offer must be clear, target must have pain". Could use "problem interview + paid pilot". Maybe fastest: go where agencies already ask for reporting help: communities, Upwork? Hmm.

Alternative: "Fake door ad test"? Run ads to landing page with pricing and Buy button. Cost maybe $200, time 3 days. But clicks aren't payment. To kill, need purchase intent. Could use pricing page with "Start pilot - pay $200". If zero checkout initiations after 200 targeted visits, maybe kill. But ad targeting small agencies can be expensive and low signal. Direct sales better for B2B.

Need maybe include competitor substitution: ask them to pay $200 to switch from existing tool or manual process. If they already pay $50-$300 for AgencyAnalytics, maybe $200 is plausible. But if they don't pay current tools, no. Need test price by asking for prepayment.

Need maybe propose "3 paid LOIs with credit card authorization". For B2B, purchase order or signed pilot agreement with payment due. Could use Stripe payment link for $200. If they won't enter card, not enough. Could accept "paid pilot" with refund guarantee.

Need exact abandonment result: e.g. After 10 working days, 100 personalized outreach, 15+ qualified conversations, if <2 paid $200 pilots (or <3?) and no one agrees to a paid pilot with card, abandon. Maybe set 0-1 as kill. Need choose threshold. Hypothesis: agencies would pay $200/mes. If it's true, a compelling offer to qualified agencies should convert some. For a small sample, 3 payments from 20 demos is strong. But to kill cheaply, maybe require 3 paid commitments from first 30 qualified agencies contacted? Let's calculate. If 10% of qualified agencies buy, contacting 30 yields expected 3. If true demand is lower maybe not viable. For $200/mo B2B niche, maybe need 5% conversion from qualified conversation to paid. If cannot get 2-3 from 20-30 conversations, kill. Need define "qualified": agency with >=3 retainer clients, spends >=3h/month reporting, decision maker, no locked enterprise tool. If not enough qualified convos, need adjust distribution, but if after 100 contacts cannot get 10 qualified conversations, maybe target not reachable or pain not acute; could kill if no interest. But to be conclusive, need perhaps use a "smoke test" with a strong promise: "We'll save you 5 hours/month on client reports or refund". If they don't take meeting, maybe not enough pain. But could be bad channel.

Maybe design experiment as a sequence with gates:
1. Problem pain test: 20 discovery calls with small agencies. If <50% report spending >=4h/month and say it's a top-3 operational pain, kill? But they want cheapest/fastest to kill pay hypothesis. Willingness to pay test is stronger.
2. Offer test: after 20 qualified conversations, present $200/mo pilot with card. If <2 pay, kill.

Need maybe avoid building landing page? Could just DM/email: "I'm running a paid pilot: $200/mo, I set up automated client reports from GA/Meta/Ads. First month refundable if not save 4h. Only 5 spots. Want one?" Send Stripe link. If no one pays, kill. Cost zero. Time 5 days. But need enough sample.

Need answer likely structured: experiment name, hypothesis, riskiest assumption, design, materials, script, costs, timeline, kill criteria, what doesn't count, possible false negatives and how to avoid, decision. Need be direct and founder-like.

Need ensure "más barato y más rápido". Could say: Do not build software. Sell a manual concierge pilot using existing tools. The product can be delivered manually or with Zapier/Looker Studio templates. You're testing payment, not automation. If they won't pay for outcome, tool won't sell.

Need maybe include "No aceptes 'me interesa', 'avísame cuando esté listo', 'te lo pienso'. Solo tarjeta/pago/PO." Good.

Need cost: $0-$50. If using Stripe payment link free, Carrd free, Calendly free, Gmail, LinkedIn. Optional domain $10, email finder $20. Time: 5-7 days, 2-3 hours/day. Need exact. Could say 72 hours if you have network; 7 days if cold.

Need kill result: If after 50 personalized messages/calls to qualified agencies and at least 10 offer conversations, you get fewer than 2 paid $200 pilots (or 0-1), abandon. More severe: if 30 qualified agencies and zero paid, kill. Need choose. The user wants result that makes abandon. Let's define: "Abandona si no consigues 3 pagos reales de $200 (o compromiso de pago con tarjeta) después de hablar con 20 agencias calificadas." Is that too high? 3/20=15% conversion; maybe if true small agencies would pay, you should get at least 3? But $200/mo might be considered; 15% from warm qualified is plausible. If can't get 3, maybe not enough willingness. But to kill cheap, maybe 1 payment? Need avoid false negative. Let's set two thresholds: Hard kill: 0 paid pilots after 25 qualified offer conversations. Soft kill: <3 after 25? The user asks exact result to abandon. Need be decisive. Maybe "si después de 30 conversaciones calificadas no tienes al menos 2 pilotos pagados con tarjeta, la hipótesis está muerta." But 2/30 = 6.7%. Could be viable? For B2B SaaS, 5-10% conversion from qualified demo to paid is decent. If <2, likely weak. But if only 1, maybe still? Need kill. Could set 3 paid pilots from 20 qualified conversations as pass; if fewer, kill? That may be too harsh but user wants kill. Need maybe "resultado que me hace abandonar": 0 or 1 payment after enough. But need not be too easy false negative. Let's think as founder: The goal is to discover if wrong. The experiment should have a clear falsification criterion. If hypothesis is "small agencies would pay $200/mes", then to falsify, show a representative sample won't. Need sample size. If true proportion is e.g. 10%, with n=30, probability of 0 purchases = 0.9^30=4.2%. So if 0/30, we can reject >10% at 95%? Actually if true 10%, seeing 0 is 4.2%, so significant. If true 5%, seeing 0 is 21%, not enough. For business viability maybe need >5%. If n=50, 0 purchases rejects 5% at 92.3%? 0.95^50=7.7%. n=60 -> 4.6%. So if 0/60 qualified offers, can say less than 5% likely. But getting 60 qualified offer conversations cold in fast cheap? Hard. Maybe 30 is okay if warm. Need define kill: 0 pagos after 30 qualified offer conversations. But maybe one payment could be outlier. If <2? With n=30, if true 10%, probability <2 = P0+P1 = 0.042 + 30*0.1*0.9^29 = 0.042+0.141=18.3%, not strong. If n=50, <2 with 10% = P0 0.005 + P1 0.028 = 3.3%, strong. So kill if <2 paid after 50 qualified offer conversations. But 50 conversations may take 2 weeks. User wants fastest. Could do 30 and if 0 kill, if 1 inconclusive? But user wants abandon result. Maybe "0 pagos de $200 after 30 qualified conversations" enough to kill for a $200/mo product? Need maybe include minimum outreach to avoid false negative: 100 targeted messages to get 15-20 conversations. If no payments, kill. Hmm.

Maybe design as "Paid waitlist / deposit". Offer $200/mo with $100 refundable deposit? But hypothesis $200/mo, ask $200 first month. Better.

Need maybe consider "small agencies" might not have authority? Owner can decide quickly. $200 is low enough no procurement. So direct owner outreach.

Need exact steps:
- ICP: agencies 1-10 people, at least 5 active monthly clients, using paid ads/social/SEO, currently reporting manually or with basic spreadsheets, not already paying >$300/mo for enterprise reporting. Find in LinkedIn, Clutch, directories, Facebook groups, local associations.
- Build offer: "Piloto de automatización de reportes: $200/mes. En 5 días te entregamos reportes automáticos white-label para tus clientes desde GA4/Meta/Google Ads. Si no te ahorramos 4 horas al mes, te devolvemos el dinero." Need maybe use existing tools: Looker Studio + connectors, Zapier/Make, Google Sheets, or AgencyAnalytics trial? But don't pay. Could deliver manually first. The point is they pay for outcome. If you can't deliver with no-code, maybe still not build. But for experiment, you can fulfill using free/cheap tools.
- Create assets: one-page Carrd/Notion with offer, FAQ, Stripe payment link, Calendly. Cost 0-10.
- Outreach: 100 personalized messages over 3-5 days. Email/LinkedIn DM. Script: "Hola [nombre], vi que [agencia] trabaja con clientes en [canal]. Estoy seleccionando 5 agencias pequeñas para un piloto: automatizar sus reportes mensuales por $200/mes, con garantía de ahorro de 4 horas o reembolso. ¿Te interesa una llamada de 10 min? Si no, no pasa nada." Follow-up 2x.
- Qualification call: ask current reporting time, tools, number clients, pain, budget. If qualified, pitch: "Puedo empezar esta semana. Son $200 del primer mes. Te envío link. Si no cumplo, reembolso." Ask for payment on call or within 24h. Do not accept "maybe". Send link.
- If they hesitate, offer "deposit $50 to reserve spot" maybe still counts? But hypothesis $200, better full payment or signed invoice. Could count card authorization. But to kill, use actual money. Maybe $50 deposit not enough. Could count paid deposit as commitment but if no one pays even $50, kill. However user wants $200/mes. Use $200.
- Track metrics: messages sent, replies, qualified conversations, offers made, payments.
- Kill criteria: after 7-10 days, if you made at least 25 offers to qualified agencies and got 0 paid pilots (or <2?), abandon. Need exact. Let's decide.

Need perhaps include "mínimo para que el experimento sea válido". If you only send 10 messages and no pay, not enough. So define: Need 100 outreach -> at least 15 qualified conversations -> 10 offers. If cannot get 15 qualified conversations, the problem may be targeting/message, not willingness to pay. But user wants kill idea. Could say if after 150 personalized attempts you cannot even get 10 qualified conversations, also abandon because the pain isn't salient or channel is bad; but to avoid false negative, maybe test different copy. However they want cheapest/fastest. Maybe set: If response rate <5% and no meetings, maybe not conclusive. But kill if no one says "yes, send invoice" after 10 real conversations. Need exact.

Let's formulate: Experiment: "Piloto pagado, no software". Duration: 5 days. Cost: $0-$30. Kill: If after contacting 50 owners and having 10 qualified offer conversations, you do not get at least 2 credit-card payments for first month, abandon. Or if you cannot get 10 qualified conversations after 100 contacts, abandon? Need maybe choose one. To be fastest, 50 contacts may be doable in 2 days. But 10 qualified conversations maybe hard. Could use warm network. Maybe say if you have no network, 7 days.

Need think about what is most likely to kill: small agencies already use low-cost reporting tools. $200/mo may be too high if they have <10 clients. They may pay $50-$100. The test may reveal they won't pay $200. Could include price anchor: ask them to pay $200. If they counter lower, note. But kill if no one pays $200. If many say $50, hypothesis wrong but pivot possible. User wants kill idea, not pivot. So result: fewer than X at $200.

Need maybe include a "control offer" to distinguish if problem is price vs product. For falsification, offer at $200 and if no, maybe offer at $50? But that could validate a different hypothesis. The user wants kill this hypothesis. Could include a second variant: If they won't pay $200 but would pay $50, hypothesis dead but maybe pivot. But to keep cheap, ask one price. Maybe after rejection, ask: "¿Qué precio sería un sí?" But not count.

Need maybe include "No construyas nada; si alguien paga, entrega con Looker Studio/Zapier/hojas y un VA. Si no puedes entregar, refund. That still tests willingness to pay." But if they pay and you can't deliver? Need be ethical: tell it's a pilot with manual setup; don't lie. Offer "done-for-you setup". You can deliver with existing tools. If no one buys, no fulfillment. If someone buys, you can manually create report. Need not build 2 months.

Need maybe include exact budget: Domain $10 optional, Carrd free, Stripe free, email/LinkedIn free, maybe $20 for list building. Total <$50. Time: 2 days setup, 3 days outreach/calls, total 5 days. If cold, 7-10 days. Need maybe state "mínimo 2-3 horas/día".

Need include scripts in Spanish. Could be for email/LinkedIn and call. Need make it concise but detailed. The final answer should be direct, maybe with table.

Need consider if "agencias pequeñas" can be reached via LinkedIn? Many owners. Could use directories: Clutch, DesignRush, agency lists, Facebook groups. Need maybe say "usa tu red primero: ex-compañeros, grupos, conocidos. Si no tienes, usa directorios." Fastest is warm.

Need maybe design "Landing page with fake checkout"? But to kill, direct sales better. Could mention not to run ads; too slow/expensive. Not to survey; lies. Not to build MVP. Need maybe include "señales que no valen": likes, free signups, 'me encantaría', promises. Only money.

Need maybe include "resultado que me hace abandonar": exact: "Cierra la idea si: contactas a 50 agencias calificadas, consigues 10+ conversaciones de oferta, y obtienes 0 o 1 pago de $200. Peor aún: si no consigues 5 llamadas calificadas después de 100 mensajes personalizados, también abandona (el dolor no es lo suficientemente consciente o el canal es inviable)." But user asks singular. Could give primary kill and secondary. Need not be ambiguous. Maybe set: "Kill: 0 pagos after 20 qualified offers". But to be robust, "0/20" enough? If true 10%, probability 12%. Not super strong. But for lean, okay. Maybe "menos de 2 pagos after 25 offers". Need exact.

Let's decide final kill criterion: After 7 días, haber hecho 20 ofertas directas a agencias calificadas (decision maker, >=3 clientes, >=3h/mes reporting). Si menos de 2 pagan $200 primer mes con tarjeta/transferencia, abandonas. Is 2/20=10%; if <2, maybe weak. But if 1, could be false positive? They want kill, so if <2 kill. But is that too easy? Maybe if only 1, idea might still be viable but not enough evidence to proceed 2 months. As a founder, to avoid building, require at least 3 paid pilots. Let's set 3? For $200/mo, building 2 months might need 3-5 paying. But experiment to kill: if can't get 3 from 20 qualified, likely not enough. However 3/20=15%, maybe high. If true 10%, chance of <3 is ~32%, false kill. But we want kill cheap, maybe accept false negative? The user says wants know if wrong. Need balance. Maybe require 5 payments from 30? Hmm.

Let's think business viability. If small agencies pay $200/mo, to have a SaaS you need maybe 100 customers = $20k MRR. Conversion from qualified demo to paid maybe 10-20%. If you can't get 3 from 20 warm qualified, maybe not. But cold outreach may lower. The experiment should be able to fail conclusively. Maybe threshold: 5 paid pilots from 50 outreach. That's 10% of contacted, maybe too high. But if using warm network, possible.

Alternative: Use "preventa anual"? Ask $200? No.

Maybe the fastest kill is "offer to manually produce reports for $200/month to 10 agencies you can access. If 0/10 say yes with payment, kill." But sample small. Need enough.

Could design as "Concierge test with 20 agencies in your network". If no network, need cold. The user didn't specify network. Need give robust plan.

Need maybe include "muestra mínima: 30 conversaciones calificadas o 100 intentos". If cannot reach, not valid. But to kill, maybe if no response. Need exact.

Let's propose:
- Experiment: $200 Paid Pilot Offer (no product).
- Duration: 5 working days if warm, 10 if cold.
- Cost: $0-$40.
- Success to continue: >=3 paid first-month pilots from >=20 qualified offer conversations. (Or >=2? Need choose.)
- Kill: If after making 25 qualified offers (or 100 personalized contacts) you have <2 paid pilots, stop. If 0, definitely dead. Hmm.

Need maybe specify "No cuentes contactos si no están calificados". Qualify: owner/decision maker, agency <10 people, >=5 active clients or >=$5k MRR managed, reports monthly, currently manual or unhappy with tool. If they already use a $300 tool and happy, not ICP? Maybe they could switch, but harder. For kill, target those with pain.

Could include "oferta con garantía" to remove risk. If they still don't pay, strong kill.

Need maybe include "si alguien paga, no construyas SaaS; entrega con plantillas. If delivery impossible, refund and note. But if they pay and you can deliver manually, maybe continue concierge." But the hypothesis is tool. If manual service is okay, maybe pivot to productized service. But user wants kill tool idea. Need say if they pay for done-for-you but not software, that's a different business; for this hypothesis, maybe still relevant? They want tool that automates reports. If they pay for outcome, it validates pain but not software. But if you can deliver manually at $200/mo, maybe not need build. However to kill SaaS hypothesis, need they pay for automated tool. But before building, concierge is acceptable. If they only want human service, not tool, maybe not SaaS. Need maybe include: "Si pagan pero solo porque les haces el trabajo manualmente, eso no valida SaaS; valida servicio. Para validar herramienta, la oferta debe prometer automatización y que ellos te den acceso a sus cuentas. Si no quieren darte accesos o integrar, kill." But too nuanced.

Maybe better: Offer "setup + automated dashboard". Use existing tools white-label. They pay for automated reports, not your manual hours. If you can deliver with Looker Studio, it's still automation. Need no custom code.

Need maybe include competitive alternative: If they already use AgencyAnalytics at $79-$399, maybe $200 is plausible. But if they use free Looker Studio, maybe no. Need ask: "¿Qué usas hoy y cuánto pagas?" If they pay $0 and won't pay $200, kill.

Need maybe include exact metrics table:
- Contactados: 100
- Respuestas: target >=8
- Llamadas calificadas: target >=12
- Ofertas: target >=10
- Pagos: kill if <2; continue if >=3? Need exact.

Let's choose kill threshold: "Abandona si después de 100 mensajes personalizados y al menos 15 conversaciones calificadas, no consigues 2 pagos reales de $200 (o 1 si quieres más estricto?)." Need maybe 2 is too low? If 2/15 = 13%, maybe viable. If <2, kill. But if 1, maybe still? User wants kill. Let's say "menos de 2" means 0 or 1 kill. But if 1, maybe not conclusive. Maybe "0 pagos" is kill. But they want result that makes abandon. Could be "0 pagos after 20 offers". But if 1, maybe you'd be tempted. Need set strict: "Si no consigues 3 pagos, abandonas." That kills more. But might false kill a viable idea. As experienced founder, maybe you want high bar before spending 2 months. Need maybe require 3 paying customers to de-risk. If can't get 3 from 30 qualified, not worth. Let's set 3 paid pilots. But need sample size. 30 qualified conversations in 7 days? Maybe tough. Could be 50 outreach. Let's say "Después de hablar con 20 agencias calificadas, si no hay 3 pagos, kill." 20 qualified conversations can come from 100 contacts. Is 3/20 high? It's 15%. If true willingness is 10%, chance of >=3 is about 32%, so you might kill a 10% true hypothesis. But for a $200/mo SaaS, 10% qualified conversion might be okay. Hmm. Maybe threshold should be 2/20. If true 10%, chance >=2 = 1 - (0.9^20 + 20*0.1*0.9^19) = 1 - (0.1216 + 0.270) = 0.608. Still false kill 39%. If true 20%, chance >=2 = high. Need not statistical perfection; lean. Could require 30 conversations and 3 payments. If true 10%, chance >=3 = 1 - P0-P1-P2. P0=.042, P1=.141, P2= C30,2 .01 .9^28 = 435*.01*.052? .226? Sum .409, chance .591. Still. If true 15%, chance >=3? P0=.0076, P1=.040, P2=.102, sum .15, chance .85. So threshold 3/30 corresponds to needing ~13-15% true conversion. Maybe okay for niche B2B? But if only 5% true, maybe business not viable? 5% of qualified demos to paid could still be viable with outbound? CAC maybe high. But small agencies $200/mo, need low CAC. If 5% from qualified convos, maybe okay if warm. Hmm.

Maybe better kill criterion based on revenue: "Si no puedes conseguir 5 agencias que paguen $100 de reserva (no reembolsable?) or 3 that pay $200". But need exact.

The user asks "el experimento más barato y más rápido que pueda MATAR esta hipótesis." So we can design a high-bar test: if it passes, strong signal; if fails, kill. They don't want validation. So maybe high bar is fine. But should not be impossible. Need credible.

Maybe use "Landing page with pricing and checkout" and run highly targeted ads. Kill if conversion from landing visit to checkout <1% with 200 visits. Cost $200. But direct outreach is cheaper. Need fastest? Direct outreach can get payments in days. Ads require budget and targeting. B2B small agencies maybe on LinkedIn expensive. Not cheapest.

Could use communities: post offer in agency groups. If no one responds/pays, kill. But not controlled. Direct outreach better.

Need maybe include "offer a 100% refund if not satisfied". That reduces risk; if still no pay, kill.

Need maybe include "No mientas: di que es un piloto con setup manual/semi-automatizado". Ethical.

Let's craft final answer in Spanish with sections:
1. Experimento: Vender el piloto antes de construir.
2. Por qué mata la hipótesis: Only money counts.
3. Setup exacto (1-2 hours): one-page, Stripe, Calendly, offer.
4. ICP and list: 50-100 small agencies, owners, channels.
5. Outreach exact script (email/LinkedIn) and follow-up.
6. Call script and qualification questions.
7. Fulfillment if someone pays: use Looker Studio/Zapier/Sheets, no code; refund guarantee.
8. Cost/time: $0-$50, 5-7 days, 2-3h/day.
9. Kill criteria: exact numbers. Need decide.

Let's define kill criteria robustly:
- Minimum valid sample: 50 personalized outreach attempts to qualified agencies, producing at least 10 real offer conversations (decision maker + pain). If you can't get 10 offer conversations after 100 attempts, that itself is a kill signal? Maybe say "si no consigues 10 conversaciones calificadas, el experimento queda inconcluso por canal; pero para matar rápido, asume que la idea no tiene demanda si tampoco responden a una oferta con garantía. Repite una sola vez con otro canal; si sigue, abandona." But user wants exact result. Could set primary: "Abandona si después de 15 conversaciones calificadas no tienes al menos 2 pagos de $200." Need maybe include "si no llegas a 15 conversaciones, aumenta muestra hasta 30 contactos; si aún no, kill?" Hmm.

Maybe final: "Resultado de abandono: 0 pagos de $200 después de 20 ofertas directas a agencias calificadas (o, como máximo, 1 pago si ya hiciste 30 ofertas y el cliente no te dio acceso a sus fuentes de datos)." Too complex.

Simpler: "Kill: menos de 2 pagos reales de $200 tras 20 conversaciones calificadas." But need ensure enough outreach. Let's say: "Si tras 5 días, 100 contactos y 15+ ofertas calificadas, tienes 0-1 pagos, abandona." This is actionable.

Could set "3 pagos" as pass. But kill if <3? Need choose. Let's maybe use 3 paid pilots as threshold to continue, because building 2 months needs stronger signal. But user asks result that makes abandon. We can say: "Abandona si no consigues 3 pagos." That is clear. But if 2, maybe still? They might be tempted. To kill, set 3. Need sample: 30 qualified conversations. Time maybe 7-10 days. Cost low. Is 3 too high? For B2B $200, if you can't get 3 agencies to pay with refund guarantee, likely not. As experienced founder, I'd require 3-5 paying pilots before building. So yes.

Let's formulate:
- Muestra mínima: 30 conversaciones de oferta calificadas (not just messages). If you can't get 30, extend to 100 messages; if still <10, kill due to lack of urgency? Hmm.
- Pass: >=3 paid first-month pilots (card/transfer). If <3, kill.
But if only 15 conversations, can't kill? Need maybe "If after 100 messages you have <10 qualified conversations, also kill (or at least don't build; the problem isn't salient enough via direct channel)." But to be exact: "El resultado que te hace abandonar: 0-2 pagos después de 25 ofertas calificadas." Let's set 25 offers, 2 payments? Need decide.

Maybe use a decision table:
- 0 pagos after 20 qualified offers => MUERTO.
- 1 pago after 20 => MUERTO para SaaS de $200 (unless that one immediately refers two more, but don't count).
- >=3 pagos => sigue.
- 2 pagos => inconcluso, but user wants kill. Could say "para matar, si no llegan 3, abandona". That avoids limbo.

Let's choose: "Abandona si no consigues 3 pilotos pagados de $200 después de hablar con 20 agencias calificadas." This is simple and strict. But 20 qualified conversations from 100 contacts in 5 days? Maybe possible with warm. If cold, maybe 10 days. Need state "si no puedes conseguir 20 conversaciones calificadas en 7 días usando tu red + grupos, también es señal de abandono/invalidación: el dolor no es prioritario o el ICP no está accesible." But maybe that's another experiment.

Need maybe include "para que sea justo, la oferta debe incluir garantía de reembolso y entrega en 5 días". If no one pays even with guarantee, kill.

Need maybe include "No aceptes pagos de amigos/family; must be real agencies". Good.

Need maybe include "If someone pays, deliver using existing tools. If you can't deliver in 5 days, refund and count as failed fulfillment; but willingness to pay still signal. However if they pay but you can't automate due to data sources, maybe technical risk." But not central.

Need maybe include "What to measure: number of contacts, replies, qualified calls, offers, payment links sent, paid." Provide simple tracker.

Need maybe include "Alternative faster if you have network: send 20 DMs today". But final should be exact.

Let's draft final in Spanish with strong tone. Need mention "No valides con encuestas". Need maybe include "la hipótesis se mata con dinero, no con elogios".

Potential final structure:

- Title: