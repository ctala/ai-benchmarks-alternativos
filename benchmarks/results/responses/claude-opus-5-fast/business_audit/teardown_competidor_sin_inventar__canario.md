# Claude Opus 5 Fast — business_audit/teardown_competidor_sin_inventar

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 2.51 | quality: 2.0
- latency_total: 12.737s | tokens_per_second: 160.8
- input_tokens: 286 | output_tokens: 2048

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

I need to be careful about distinguishing what's actually verifiable from what's speculation in this competitor analysis. The biggest red flag is treating that member count times price as direct revenue—that's way too simplistic and ignores free tiers, discounts, annual billing, churn, and whether those are active or cumulative numbers. I should make that uncertainty explicit rather than letting it slide into the analysis.

For the membership platform itself, I don't know which specific tool they're using, so I need to flag that the member count interpretation varies by platform—Skool typically shows current members, but Circle and Mighty Networks have different admin configurations. Rather than asserting platform specifics as fact, I should note what the observable data suggests and what assumptions I'm making.

The real value here is mapping out what we can actually infer from the visible signals, what's missing, and what cheap reconnaissance could collapse the uncertainty around their actual revenue and health. The public feed activity is more about operational consistency than actual member engagement, and could easily be founder-driven or pre-scheduled. The 12-course catalog is a classic red flag—lots of unfinished or "coming soon" courses tank retention. The 60k founder followers give a rough sanity check: 2,400 paying members from that audience is about a 4% conversion, which is decent for a $39/mo product but suggests they're either pulling from other channels or the follower count inflates the actual addressable market.

The real pressure point is churn. At typical 8% monthly churn for a community product, they'd need to replace 190 members just to stay flat, which at 4% conversion means constant traffic acquisition—that's why the posting cadence is so aggressive.

The unknowns that matter most: actual churn rate, how many of those 2,400 are paying versus free, real ARPU, whether they're dependent on a single founder, and what their cost structure looks like. Without those, I can't assess if this is actually healthy.

To compete, I'd attack the breadth problem—position on deep outcomes rather than shallow coverage across everything. Or go vertical: instead of generic $39 automation, offer $99-199 automation built specifically for one industry. And exploit founder dependency since they can't scale beyond what one person can deliver.…