# Nex-N2-Mini — strategy/competitor_analysis

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 6.73 | quality: 6.67
- latency_total: 42.678s | tokens_per_second: 191.9
- input_tokens: 182 | output_tokens: 8192

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un analista de estrategia para startups. Sé riguroso con los datos y honesto cuando no tengas certeza.

**user:**

Soy fundador de una startup de email marketing para pymes en LATAM. Mis 3 competidores principales son Mailchimp, Brevo (ex-Sendinblue), y una startup local llamada "EnviaMas".

Con la informacion que tengas (si no la tienes, dilo):
1. Genera una tabla comparativa con: pricing, features principales, mercado target, fortalezas, debilidades
2. Identifica 3 gaps de mercado que yo podria explotar
3. Sugiere un posicionamiento diferenciador para mi startup
4. Que deberia hacer en los proximos 90 dias?

Se especifico. No me des consejos genericos.


## Respuesta completa


We need answer in Spanish. Need be rigorous data, honest if no info. Need maybe say pricing/features change and I don't have real-time. Need maybe include caveats. Need know Mailchimp, Brevo, EnviaMas. Need generate comparative table with pricing, features, target, strengths weaknesses. Then gaps, positioning, 90-day plan specific.

Need maybe mention "con información que tengas": no browsing. Need maybe current as of 2024-06? But knowledge cutoff 2024-06, current 2026? System says current 2026 but no browsing. Need say "no tengo precios en vivo; valida en páginas". But can provide approximate public pricing known? Need be careful.

Let's gather from memory.

Mailchimp: pricing around Starter $13.99/mo up to 500 contacts? Standard $20.99, Professional $35.99, Premium custom, annual discounts. Free up to 500 contacts, 1,000 emails/mo? It changed: Free 500 contacts, 1,000 sends/mo, 3 campaigns, 24/7 support? Standard $13.99/mo monthly for up to 500 contacts (or $10.49 annual) includes 50k emails/mo, 14 contacts? Actually Mailchimp pricing: Free: 500 contacts, 1000 emails/mo. Standard: $13.99/mo (annual $10.49) includes 50k emails/mo, 14 seats, 1 seat? Professional $35.99/mo (annual $26.99) 100k, 3 seats. Premium custom 200k, 8 seats. Need maybe not exact.

Mailchimp features: email campaigns, automations, landing pages, ads, CRM, audience management, segmentation, templates, analytics, social ads, website builder, e-commerce integrations, postcards/direct mail, AI. Target SMBs, creators, e-commerce, agencies; broad global. Strengths brand, ease, ecosystem, templates, deliverability, integrations, app marketplace. Weaknesses price jumps, limited advanced localization, automation complexity, deliverability issues? less tailored LATAM, support maybe not in Spanish/Portuguese? Maybe support language.

Brevo (Sendinblue): Pricing in 2024: Free unlimited contacts, 300 emails/day. Lite $25/mo monthly up to 10k contacts, 10k emails/mo? Lite $15/mo annual, Standard $45/mo annual? Actually Brevo pricing: Free 300 emails/day. Lite $25/mo (€25) monthly, €15 annual; Standard €45/mo monthly, €25 annual; Business €65 monthly, €49 annual; Enterprise. Contacts tiers up to 10k, 20k, 30k? Email volume 10k/mo Lite, 30k Standard, 60k Business maybe. SMS/email marketing, transactional, WhatsApp, chat, CRM, marketing automation, landing pages, Facebook ads, SMS, contact center. Target SMBs, e-commerce, SaaS, agencies; Europe/LATAM. Strengths generous free, all-in-one, transactional + SMS/WhatsApp, marketing automation, multilingual, competitive pricing. Weaknesses UI complexity, deliverability variable, brand less recognized than Mailchimp in US, some features depend on add-ons, local payments/taxes maybe limited.

EnviaMas: local LATAM startup? Need know specifics. I need be honest. What is EnviaMas? Could be a local email marketing in LATAM, maybe Argentina? "EnviaMas" maybe Brazilian? Need infer. It may be a SaaS "EnviaMas" for email marketing in Brazil/Latin America? Let's search memory: EnviaMais? "Envia Mas" maybe Brazilian email marketing platform by "Envia Logística"? No, "Envia Mais" could be e-commerce shipping? In Brazil "Envia Logística" logistics. "EnviaMas" maybe "EnviaMas" from Mexico? Hmm.

User says "startup local llamada EnviaMas" in LATAM. We don't know exact. Need not hallucinate. We can say "no tengo suficiente info pública fiable; lo trataré como un competidor local pequeño/medianos; datos a validar". But they asked table with pricing/features/target/strengths/weaknesses. We can include "no confirmado" and likely based on positioning. Need maybe state "si EnviaMas es la startup local que mencionas, asumo..." But maybe bad.

Let's think of "EnviaMas" actual. In Spanish/Portuguese, "Envia Más" maybe a CRM/email marketing for "negocios locales" in Mexico. Pricing maybe "desde $299/mx"? Could be "Enviamas" a Mexican email marketing platform. I recall "EnviaMas" is an email marketing platform in Colombia? "Enviamas" offers email marketing, landing pages, automations? Maybe priced in COP. Let's not invent. We can say "precio: no disponible/variable; validar; normalmente pymes locales; features: email marketing, newsletters, landing pages, contact list, analytics; strengths: local language, support, payment methods, WhatsApp?; weaknesses: smaller ecosystem, lower trust, integrations, deliverability, brand, scale." But table should be specific. Need maybe include "a falta de info pública confirmada".

Need identify gaps in market for email marketing for SMEs in LATAM. Need be specific and exploitable. Let's brainstorm.

Market context LATAM: fragmented languages (Spanish/Portuguese), payment friction (PIX, transferencias, tarjetas, efectivo, local taxes), deliverability challenges due to spam, WhatsApp dominance, small businesses need simple operations, compliance LGPD (Brazil), LFPDPPP Mexico, Chile/Colombia? Many businesses use WhatsApp/Instagram, not email; need omnichannel. SMEs have low MRR, need low upfront, simple. Integration with commerce platforms local (Mercado Libre, Shopify, Tiendanube, Yampi, TiendaNube? WooCommerce, Paga24, Mercado Pago, Stripe, dLocal, Cuentas). Need local deliverability: IP reputation, DKIM/SPF in Spanish, support warm-up. Need "email marketing + WhatsApp" because high open rates but privacy; combine. Need "growth ops" for small teams: onboarding, templates, segmentation, lifecycle flows, compliance consent, templates for sectors (restaurants, salons, clinics, education, local retail, e-commerce). Need "prepaid/pay-as-you-go" due to cash flow. Need "local support in Spanish/Portuguese, payment local, tax invoices". Need "no lock-in" and data portability.

Potential gaps:
1) "Latam-first deliverability + compliance + local integrations": DKIM/SPF wizard, IP/domain reputation monitoring, inbox preview, unsubscribe/consent, LGPD/Mexico, local data residency, local sender authentication. Most global platforms are complex and not tuned to local sending patterns; local competitors maybe weaker.
2) "Omnichannel WhatsApp + email for conversational commerce, but not full CRM": Many LATAM SMBs rely on WhatsApp; email alone underused. Position as "email que se conecta con WhatsApp": flows triggered by purchases, abandoned carts, reactivation, follow-ups, broadcast, segmentation; use WhatsApp for high-intent, email for newsletters/promos/education; maybe use WhatsApp templates.
3) "Sectores/presets + onboarding as-a-service": SMEs don't want to learn marketing automation. Provide templates and playbooks for specific verticals (restaurants, ecommerce, clinics, gyms, schools, real estate, B2B services), with import, automation, campaign calendar, 15-min setup, support. Pricing simple.
Alternative gaps:
- Transparent pricing/pay-as-you-go/local payments/tax invoices.
- Integration with Mercado Libre/TiendaNube/Mercado Pago/WhatsApp/Instagram.
Need choose 3.

Need suggest positioning. Could be "La plataforma de email marketing hecha para pymes LATAM: campañas, automatizaciones y WhatsApp, con pagos locales, soporte en español/portugués y entregabilidad garantizada; desde $X/mes." Need differentiate from Mailchimp/Brevo/EnviaMas. Maybe "Email marketing que convierte en WhatsApp" or "email marketing con canal WhatsApp". Need avoid overclaiming deliverability guarantee. Could say "Hecha para vender por email y WhatsApp en LATAM".

Need 90-day plan. Specific. Need maybe include phases:
Days 1-15: validate and pick beachhead.
- Interview 25-40 SMEs (ecommerce, restaurants/salons/clinics, service providers) across 2-3 countries.
- Map workflows, current tools, pain points, budgets, decision criteria.
- Competitive teardown of Mailchimp, Brevo, EnviaMas: pricing, onboarding, templates, support, integrations.
- Select one ICP and country (e.g., Spanish-speaking ecommerce/service businesses 5-50 employees, $5k-50k revenue, using WhatsApp + Mercado Libre/TiendaNube).
- Build landing page with positioning and waitlist/POC.

Days 16-30: MVP/offer.
- Define MVP features: import contacts, segmentation, email templates, 3 automations (welcome, abandoned cart, reactivation), WhatsApp broadcast/CRM integration, deliverability checklist, analytics.
- Local payments (Mercado Pago, Stripe, transfer/PIX if Brazil), invoices, Spanish/Portuguese support.
- Onboarding playbook: migrate list, setup domain/DKIM/SPF, first 4 campaigns.
- Price: freemium? low-cost. Maybe "Starter $19-29/mo up to 1,000-2,000 contacts; usage-based credits; first 500 contacts free" or "pay-as-you-go". Need be specific. Need maybe not if uncertain. We can suggest.

Days 31-60: pilot.
- Recruit 20-30 design partners, 10 paying.
- Offer concierge onboarding.
- Measure activation: contacts imported, domain verified, first campaign, automation live, 2nd campaign, WhatsApp flow.
- Build integrations: WhatsApp Business API provider (Twilio/360dialog/Zenvia maybe), Mercado Pago, Stripe, Shopify/TiendaNube/WooCommerce, Google Sheets.
- Improve deliverability: dedicated IPs? For small startup maybe shared IP with domain authentication; monitor bounce/open/spam; daily sending limits; SPF/DKIM/DMARC wizard.
- Run competitor switch campaigns with migration checklist.

Days 61-90: scale.
- Convert pilots to paid; aim MRR and retention.
- Product: templates by vertical, lifecycle flows, dashboard, deliverability score, A/B test maybe.
- Go-to-market: content in Spanish/Portuguese, webinars, partner agencies, marketplaces, affiliate/referral, outbound to e-commerce directories.
- Metrics: CAC, activation >60%, paid conversion >25%, churn <5% monthly, deliverability open rate >25-35%, email send volume, support response <2h.
- Decide expand/country/vertical.

Need maybe include "90-day roadmap with deliverables and KPIs".

Need table maybe include "Pricing" with caveat. Need maybe exact approximate.

Let's structure answer:

Start with "No tengo acceso a precios/features en vivo ni datos internos de EnviaMas; la tabla usa información pública hasta 2024 y debe verificarse. Lo que sí puedo hacer es comparar hipótesis de mercado." Good.

Then table:
Columns: Competidor, Pricing (aprox.), Features principales, Target, Fortalezas, Debilidades/riesgos.

Need include EnviaMas maybe with "no confirmado". Could perhaps make "EnviaMas (local, info pública limitada)" row:
- Pricing: "No puedo confirmar; probablemente planes por contactos/envíos en moneda local; validar; si su propuesta es local, suele competir en soporte/pagos." But user asked table; maybe row with "No disponible en mi base / confirmar". Need maybe not generic. But we can be specific with placeholders. Hmm.

Could include "EnviaMas: precio: no lo tengo confirmado; asumir: planes por lista/envíos con opción local; foco en PYMEs; features: email marketing, newsletter, landing pages, automatizaciones básicas, contacto/support local; strengths: local language/payments/support, proximity; weaknesses: menor ecosistema/integrations/brand, deliverability scale, UX." That's honest.

But maybe the user expects "con información que tengas" and if not, say. Good.

Need maybe mention "Mailchimp and Brevo prices change by region/currency; EnviaMas no public info." Good.

Need maybe include "pymes en LATAM" and "market target".

Let's detail features:

Mailchimp:
- Email campaigns, templates, automations (Customer Journeys), segmentation/tags, landing pages, website builder, social/ads, content studio, analytics, e-commerce/CRM, postcards/direct mail, AI, app marketplace.
Target:
- small businesses, e-commerce, creators, agencies, international SMBs; strong in US/EU.
Strengths:
- brand, ease, templates, ecosystem, scale, deliverability/infrastructure, global integrations.
Weaknesses:
- cost escalates quickly; product bloated; fewer LATAM-specific integrations/payments; automations less simple; Spanish support maybe inconsistent; not WhatsApp-first; pricing based on contacts, hidden overages.

Brevo:
- Email/SMS/WhatsApp campaigns, transactional email, marketing automation, CRM, landing pages, chat, Facebook ads, contact center, A/B testing, segmentation, API.
Target:
- SMBs, e-commerce, SaaS, agencies, businesses needing transactional + marketing across channels; strong in Europe and emerging markets.
Strengths:
- all-in-one, pricing flexible/free, transactional + marketing, SMS/WhatsApp, automation, multilingual, API.
Weaknesses:
- complexity; deliverability depends on list hygiene/domain; support varies; brand less strong in some LATAM; local payments/tax may be less strong; UI can overwhelm.

EnviaMas:
Need perhaps "Local startup; public data limited; if it's focused on LATAM local, likely:
- Pricing: "por contactos/envíos; moneda local; confirmar".
- Features: "newsletter, landing pages, automation, CRM/contactos, analytics; maybe WhatsApp; support local."
- Target: "PYMEs locales en [country/region]; merchants who want simple Spanish support."
- Strengths: "proximity, local support, payment methods, cultural fit, maybe lower price, WhatsApp/local channels."
- Weaknesses: "smaller brand, fewer integrations, less mature automation, deliverability/infrastructure, scaling, product depth, trust/security."
Need maybe note "si EnviaMas es más pequeño, su amenaza real es en el segmento de precio/local support, no en global features."

Could maybe include "Mailchimp/Brevo global have strong deliverability; local competitor may have advantage in support and payments."

Need "gaps de mercado" with details:
1. "Latam-first deliverability + compliance + trust":
- Pain: SMEs don't know SPF/DKIM/DMARC; lists bought; Gmail/Yahoo 2024 bulk sender requirements; spam complaints; low deliverability; need local consent/LGPD.
- Exploit: wizard, deliverability score, sender reputation monitoring, pre-approved templates, domain warm-up, consent logs, unsubscribe, DMARC reports, local data.
- Why not competitors: Mailchimp/Brevo provide tools but not concierge/local compliance; EnviaMas maybe lacks depth.
2. "Omnichannel email + WhatsApp for PYMEs":
- Pain: WhatsApp is daily channel; email ignored; segmentation missing; manual broadcast.
- Exploit: use email for lifecycle/newsletter, WhatsApp for transactional/conversational; flows: welcome, abandoned cart, post-purchase, reactivation; unified contacts and segmentation.
- Why: global platforms treat WhatsApp as add-on; local may not integrate.
3. "Vertical playbooks + migration/onboarding + local payments":
- Pain: small teams don't have marketer; need "campaign calendar + templates + automation + support + pay with Mercado Pago/PIX"; no time to configure.
- Exploit: ICP-specific packages, templates, concierge setup, migration from Excel/WhatsApp, local invoices, pricing in local currency.
- Why: Mailchimp/Brevo are generalists; local competitors may not have playbooks.

Could maybe mention "gap #4: transparent pay-as-you-go" but only need 3. Maybe include as "opcional".

Need "posicionamiento diferenciador":
Maybe:
"Email marketing + WhatsApp para pymes que quieren vender sin contratar marketer: importas tu base, verificas dominio en 10 minutos, recibes plantillas/automatizaciones por rubro, pagas con métodos locales y soporte en español/portugués. No eres Mailchimp para pymes globales; eres el sistema de campañas para LATAM."
Need maybe include tagline:
"Deja de mandar correos al azar: activa ventas recurrentes con email y WhatsApp."
Need maybe include "I would not position as 'más barato que Mailchimp' because race to bottom and lower trust. Position as 'más local, más simple, más orientado a ventas/WhatsApp'." Good.

Need "90 days" specific:
Need maybe include "no construir todo; validar pago". Let's design a detailed plan with weeks.

Week 0-2: ICP + interviews + offer:
- Pick 2 verticals max: ecommerce local (TiendaNube/WooCommerce/Shopify) and servicios recurrentes (clínicas/salones/academias) or restaurants? Maybe choose one. Since user didn't specify country/vertical. We can propose "si aún no tienes ICP, haz prueba en 2 sectores." Need specific but not too generic. Maybe "elige un beachhead: pymes ecommerce/retail local con base en WhatsApp y 1,000-10,000 contactos" because email marketing fits. But maybe pyme B2B? Need maybe not assume. Could say "si tu startup aún no tiene datos de ventas, no construyas plataforma: valida con 20 design partners."

Need maybe include "30 entrevistas, 10 pruebas pagadas".
- Interview questions:
- ¿Qué canal usas para comunicar ofertas?
- ¿Cuánto pagas a email/CRM/WhatsApp?
- ¿Qué tan limpio está tu listado?
- ¿Tus clientes pagan por Mercado Pago/Stripe/PIX?
- ¿Qué te impide enviar emails?
- ¿Qué harías si te prometo recuperar ventas perdidas con emails/WhatsApp?
- Competitor teardown.

Week 2-4: MVP and landing:
- Landing page with CTA "Auditoría gratuita de entregabilidad y lista".
- Build "MVP de servicio" maybe no-code: MailerLite/Brevo? But if they want startup maybe use own? Need maybe "si no tienes infra propia, usa un proveedor white-label/API para validar; no construyas motores de email desde cero." Good. But user asked strategy; we can mention "no construyas SMTP propio en primeros 90 días; usa API/infra ya probada para reducir riesgo de deliverabilidad." Important.

- Offer:
- Starter: hasta 1,000 contactos + 5,000 envíos/mes; $19-29 USD/mes or local equivalent; first migration free.
- Growth: hasta 5,000 contacts + 20k envíos; $59-79; includes WhatsApp.
- Need maybe use "USD" and local currency. But if Brazil, PIX.
- Include "no bloqueo por contactos muertos; pagos por envíos reales".

Week 4-8: pilots:
- 20-30 design partners; 5-10 paid.
- Onboarding: import list, dedupe, consent check, SPF/DKIM/DMARC, first campaign, 2 automations (welcome, abandoned cart/reactivation), 4-week calendar.
- Metrics:
- Activation: 80% complete domain verification, 70% first campaign sent, 50% automation live.
- KPIs: open rate >25%, click >2%, unsubscribe <0.5%, bounce <2%, spam <0.1%, revenue attributed.
- Build only 2 integrations: WhatsApp Business API (Zenvia/Twilio/360dialog) and payments/local (Mercado Pago/Stripe/PIX). Then maybe Shopify/TiendaNube/WooCommerce.
- Competitive switching: "Migración de Mailchimp/Brevo en 15 min; export CSV; no perder datos; soporte".

Week 8-12: conversion and go-to-market:
- Paid conversion, testimonials/cases.
- Product: vertical templates, deliverability dashboard, campaign planner, A/B, segmentation.
- GTM:
- Outbound to directories: TiendaNube, Shopify stores, Mercado Libre sellers, coworkings, agencies; partner with agencies of performance marketing/WhatsApp.
- Webinars "Cómo recuperar ventas por email y WhatsApp"; "Checklist LGPD/DMARC".
- Referral: "trae una tienda y gana 1 mes gratis".
- Metrics:
- 30-50 paying customers? Maybe too high. Need realistic:
- 10 paid pilots -> $500-1,000 MRR? For startup maybe.
- 20-30 active paying?
- CAC payback <3 months, churn <5%, activation >60%.
- Decision:
- If vertical A has >3x activation and lower support, focus there.
- If WhatsApp integration causes complexity, keep email-only but with WhatsApp links.
- If deliverability issues, invest in infrastructure before scaling.

Need maybe include "what not to do in 90 days":
- Don't compete head-to-head with Mailchimp/Brevo on features breadth.
- Don't build transactional email, CRM full, ads, postcards.
- Don't buy IP/dedicated infrastructure too early.
- Don't offer free forever.
- Don't target enterprise.
This is useful and specific.

Need maybe include "pricing recommendation" maybe in 90 days. Let's craft.

Potential final structure:
1. Caveat.
2. Table.
3. Gaps.
4. Positioning.
5. 90-day plan with timeline, actions, KPIs, decisions.
6. "Resumen ejecutivo: enfoque recomendado."

Need maybe include "pricing" exact for Mailchimp/Brevo. Need maybe mention "aprox." and "puede variar por país/moneda/plan anual". Let's verify current pricing:
Mailchimp pricing as of 2024:
Free: up to 500 contacts, 1,000 sends/month.
Standard: $13.99/mo or $10.49 annual, up to 500 contacts, 50k sends/mo, 14 seats? Actually seats: Standard includes 1 seat? Let's see: Mailchimp pricing:
Free: up to 500 contacts; 1,000 sends/mo; 24/7 email/chat support.
Standard: $13.99/mo; up to 500 contacts; 50,000 sends/mo; 14 seats? Hmm.
Professional: $35.99/mo; up to 10,000 contacts? 100,000 sends/mo; 3 seats.
Premium: custom; up to 200,000 contacts; 300,000 sends/mo; 8 seats.
But maybe changed: Standard includes 1 seat, Professional 3, Premium 8. I should avoid seat details. Use "desde ~$14/mes; escala por contactos/envíos".

Brevo pricing:
As of 2024:
Free: 300 emails/day.
Lite: €25/mo monthly / €15 annual; 10k contacts? 10k emails/mo.
Standard: €45/mo monthly / €25 annual; 30k contacts? 30k emails/mo?
Business: €65/mo monthly / €49 annual; 60k contacts? 60k emails/mo?
Actually maybe:
- Lite: up to 10k contacts, 10k emails/month
- Standard: up to 30k contacts, 30k emails/month
- Business: up to 60k contacts, 60k emails/month
Then additional contacts/emails. Good.
Need mention "SMS/WhatsApp/transactional billed separately/add-ons" because pricing for email only.

EnviaMas: no info. Could maybe state "No tengo datos públicos fiables de pricing; no lo invento." In table, maybe "No disponible en mi base; validar directamente." That's honest.

Need maybe include "features principales" for EnviaMas as "no confirmado" too. Maybe table row:
"EnviaMas | No lo tengo confirmado; en general plataformas locales suelen cobrar por contactos/envíos en moneda local | No tengo suficientes datos públicos para listar features; si es similar a la categoría, probablemente newsletter, landing pages, contactos, reportes/automatizaciones | PYMEs locales, especialmente empresas que valoran soporte cercano | Fortalezas: cercanía, soporte, pagos/tax local, precio/relación | Debilidades: menor ecosistema/integraciones, menor marca, menor infraestructura/entregabilidad, profundidad de automatizaciones"
This is acceptable.

Need maybe maybe user asked "una startup local llamada EnviaMas" and "con información que tengas". If I don't know, say. Good.

Need maybe include "seguridad y cumplimiento":
- LGPD (Brazil), LFPDPPP (Mexico), Ley de Protección de Datos Personales (Argentina? Chile/Colombia/Perú). Need not be exhaustive. Could mention "LGPD en Brasil y normas locales de protección de datos".

Need maybe include "deliv" after Gmail/Yahoo 2024:
- Bulk senders must authenticate SPF/DKIM, DMARC, low spam rates. This matters. For LATAM, many small businesses have poor list hygiene. Good.

Need maybe include "competitor differentiation matrix":
Mailchimp = easiest global but expensive; Brevo = all-in-one and powerful; EnviaMas = local but maybe less depth. Your wedge = "LATAM-first vertical + WhatsApp + deliverability + local payments."

Need maybe include "specific 90-day plan" with deliverables:
Let's write in Spanish with bullets.

Potential final:

"Supuestos: pyme = 5-100 empleados, ventas recurrentes, base de clientes en Excel/WhatsApp/CRM básico, presupuesto < $100/mes, no marketer."

Then:
"1. Tabla comparativa"

Table:
- Mailchimp:
Pricing: Free 500 contacts/1k sends; paid from ~$14/mo annual; scales by contacts and sends; add-ons.
Features: email campaigns, templates, automations, landing pages, website builder, e-commerce, ads/social, analytics, AI, app marketplace.
Target: SMBs, creators, ecommerce, agencies, global.
Strengths: brand, ease, ecosystem, templates, integrations, deliverability.
Weaknesses: price jump, bloated, not LATAM/WhatsApp-first, fewer local payments/taxes, support can be impersonal, overpayment for small lists.
- Brevo:
Pricing: Free 300 emails/day; Lite ~€25/mo monthly / €15 annual; Standard ~€45; Business ~€65; contact tiers; SMS/WhatsApp/transactional extra.
Features: email, SMS, WhatsApp, transactional, CRM, chat, landing pages, automations, Facebook ads, API.
Target: SMBs, ecommerce, SaaS, agencies, businesses needing marketing+transactional.
Strengths: all-in-one, flexible, automation, multichannel, API, good price.
Weaknesses: complexity, deliverability responsibility, brand less strong, support varies, local compliance/payments not core.
- EnviaMas:
Pricing: "no tengo info pública fiable; validar; si local likely by contacts/envíos in local currency."
Features: "no tengo list confirmed; category likely email newsletters, lists, landing pages, reports/automation; maybe local support; no claim."
Target: pyme local/regional, maybe Spanish-speaking LATAM.
Strengths: local support, payments/tax, proximity, cultural fit, niche focus.
Weaknesses: likely smaller brand/ecosystem, fewer integrations, less mature automation/deliverability, lower scalability/trust, depends on founder-led support.

Need maybe include "ranking: Mailchimp/Brevo features; EnviaMas local."

Then "2. Gaps de mercado":
Need maybe format as "Gap | Por qué existe | Cómo explotarlo | Qué medir".
Let's include 3.

Gap 1: "Entregabilidad y cumplimiento LATAM"
- Pain: domain authentication, list quality, consent, DMARC, spam.
- Offer: "Entregabilidad LATAM: verificador SPF/DKIM/DMARC, score, monitoría, migration, list hygiene, consent log, templates compliant."
- KPIs: bounce <2%, spam <0.1%, open/click.
- Why: Mailchimp/Brevo have tools but not concierge/local; EnviaMas maybe not.

Gap 2: "Email + WhatsApp para ventas recurrentes"
- Pain: WhatsApp is high engagement; email is underused; businesses send manually.
- Offer: "Campañas por email y WhatsApp desde la misma base: welcome, abandoned cart, reactivation, post-purchase, offers."
- KPIs: revenue per campaign, WhatsApp clicks, reply rate, repeat purchase.
- Why: global platforms treat WhatsApp as add-on; local may not have lifecycle.

Gap 3: "Playbooks verticales + onboarding local"
- Pain: SMEs don't know what to send; no marketer; lists messy; payments/tax.
- Offer: "Plantillas y flujos por rubro: restaurantes, clínicas, academias, ecommerce local; import from Excel/WhatsApp; first 4 campaigns in 48h; Mercado Pago/PIX/transfer; factura."
- KPIs: activation time <48h, first campaign, paid conversion, retention.
- Why: generalist platforms lack industry-specific; local competitor may lack templates.

Could maybe include "Gap 4 optional: pricing/pay-as-you-go" but user asked 3. Maybe mention "si quieres otro gap: pricing flexible". But maybe no.

Need "3. Posicionamiento":
Potential tagline:
"La plataforma de email marketing + WhatsApp para pymes LATAM que quieren vender más sin contratar un marketer."
Subtext:
"Importa tu lista, verifica tu dominio, activa campañas y automatizaciones por rubro, paga con métodos locales y recibe soporte en español/portugués."
Need maybe include "No somos Mailchimp/Brevo; somos para el mercado local."
Need maybe "Elevator pitch" and "messaging pillars":
- "Más simple que Mailchimp/Brevo para una pyme local."
- "Más local que Mailchimp/Brevo: pagos, impuestos, soporte, LGPD/DMARC."
- "Más orientado a ventas: email + WhatsApp."
Need maybe include "avoid positioning as cheap." Good.

Need "4. 90 days":
Let's make a table with "Fase / Días / Qué hacer / Entregables / KPIs / Decisión".
Detailed:

Fase 1: Días 1-15: validar ICP y dolor
- Entrevistas 30 pymes: 10 ecommerce/TiendaNube/Shopify/WooCommerce, 10 servicios recurrentes (clínicas/salones/academias), 10 restaurantes/barbers/gyms.
- Ask for data: current monthly spend, list size, channels, pain, willingness to pay.
- Competitive teardown: 10 users trying to set up Mailchimp/Brevo and EnviaMas; time to first campaign, price, support.
- Decide beachhead: choose one country + vertical. If no data, choose ecommerce local with WhatsApp because email can recover revenue.
- Deliverable: ICP, top 5 jobs-to-be-done, competitor matrix, pricing hypothesis.
- KPIs: 30 interviews, 10 with budget, 5 willing to pay pilot.

Fase 2: Días 16-30: MVP de oferta, no full product
- Landing page with waitlist/audit.
- Offer: "Migración + 30-day revenue campaign sprint."
- Pricing pilot: Starter $29/mo or local equivalent up to 1k contacts/5k sends; Growth $59/mo up to 5k contacts/20k sends; WhatsApp add-on or included in Growth; annual? Avoid free forever.
- Use existing email infrastructure (Brevo/Mailgun/Mandrill/Amazon SES?) if own platform not ready; don't build SMTP.
- Core features: import CSV/Sheets, segmentation, templates, 3 automations, domain verification wizard, analytics, export.
- Deliverable: MVP landing + onboarding.
- KPIs: 50-100 signups, 10 booked calls, 5 pilots.

Fase 3: Días 31-60: pilotos pagados
- Recruit 20-30 design partners; require payment or refundable deposit.
- Onboarding 48h: clean list, consent, SPF/DKIM/DMARC, first campaign, 2 automations, calendar.
- Build 2 integrations: WhatsApp Business API (Zenvia/Twilio/360dialog) and payments (Mercado Pago/Stripe/PIX). Maybe TiendaNube/Shopify/WooCommerce if ecommerce.
- Metrics weekly: activation, open/click/unsub/bounce, revenue, support tickets.
- KPIs: 10 paid pilots, activation >60%, first campaign sent by 80%, paid conversion >30%, NPS >40, churn 0, bounce <2%, unsubscribe <0.5%, 3 case studies.
- Decision: If WhatsApp integration heavy, reduce to links/CTA; if email deliverability poor, focus on deliverability.

Fase 4: Días 61-90: convertir y escalar canal
- Convert pilots to paid; create templates by vertical; self-serve.
- GTM: 100 outbound/week to ICP, webinars, partner agencies, "free deliverability audit", referral.
- Product: deliverability score, automation builder, campaign planner, reporting by revenue, templates.
- Sales: close 20-30 paying customers, $1k-3k MRR maybe; depends pricing.
- KPIs: MRR, CAC, activation, retention, LTV/CAC, support response <4h, onboarding <2 days, paid conversion >25%, email volume.
- Decision: double down on vertical/channel; choose next country only after retention.

Need maybe "90-day success criteria":
- 20-30 active paying customers
- $1,000-$3,000 MRR (if $29-59)
- 2 repeatable acquisition channels
- 3 case studies
- Product-market signal: >40% of active users send 2+ campaigns/month or >30% paid after 30 days.
Need maybe include "if not, pivot".

Need maybe "Suggested first customer profile":
- "Tiendas online de 1-10 personas, 1,000-10,000 contacts, sell repeat purchases, use WhatsApp for customer service, lose revenue from abandoned carts, current spend $0-$50/mo, list in Excel."
This is specific. But maybe if user has country, adapt. We can say "si no tienes datos, empieza con este ICP."

Need maybe "pricing recommendation" more specific:
- "No freemium unlimited; use free trial/audit + paid starter."
- "Charge by active contacts and actual sends; include 30 days free migration."
- "Offer 'Recovery Revenue' package: $49/mo + usage; 15-min setup; includes 4 flows."
Potential "MVP pricing":
Starter: $25/mo up to 1,000 contacts / 5,000 sends; 1 user; 3 templates; no