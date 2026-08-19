# Claude Opus 5 — business_audit/teardown_competidor_sin_inventar

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 2.5 | quality: 2.0
- latency_total: 36.979s | tokens_per_second: 55.4
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

I need to be careful here—the user is asking for a teardown but I can't determine actual revenue from what's visible. The "2,400 members" figure is the critical ambiguity since it doesn't distinguish between free and paid users, which makes it impossible to calculate real numbers. I should lay out what I can observe as facts versus what requires inference, then build the analysis from there.

The real unknowns that drive the math are whether those 2,400 are actually paying customers, what the churn looks like, whether there are annual plans or discounts affecting monthly recurring revenue, and whether there's meaningful revenue from other sources like cohorts, consulting, or affiliate programs from automation tools. The naive ceiling would be 2,400 × $39 = $93,600 MRR if everyone paid full price with no churn, but that's almost certainly not the reality. The platform itself matters too—on Skool, the displayed member count typically includes everyone who's ever joined, not just active paying members, so I need to flag that dependency when building realistic revenue scenarios.

Breaking this into three bands: a bear case where only 25-35% of the 2,400 are actively paying at an effective rate around $35 gets to $21-30k MRR; a base case of 50-65% paying at $33-37 effective lands around $40-57k MRR; and a bull case near full conversion at list price hits $85-94k MRR. The effective ARPU will be lower than $39 because of annual discounts, legacy pricing, comps, and payment failures. I can triangulate this against the 60k followers—typical creator-to-paid-community conversion is 0.5-3%, so 60k × 1-3% gives 600-1,800 paying members, which independently supports the base case of 1,000-1,500. That's good validation, though those followers are probably just one acquisition channel alongside email, YouTube, ads, and word of mouth.

On the cost side, there's the platform fee (Skool or Circle at $99-360/mo), Stripe processing around 3%, a lean team of 1-3 people, and content creation—margins probably run 60-80% before founder salary if it's solo or lean. For health signals, I'm seeing three posts per week on the public feed which shows consistency, but I can't tell if that's the founder, a team, or repurposed content, and public activity doesn't necessarily reflect what's happening inside the community. The real engagement metric—member-generated posts and comments—is hidden from view. There are 12 courses listed, but I don't know how complete they are, which creates risk: either content sprawl and abandoned courses, or a strong library moat. The value-stacking at $39 suggests they're trying to justify the price, which often correlates with churn when people join for the library, binge it, and leave.

The single visible price point of $39/mo means low ARPU and heavy volume dependency, making them vulnerable to churn spikes. No visible annual plan weakens cash flow and removes a natural churn dampener—annual plans cut effective monthly churn significantly. The founder's 60k followers and personal brand create key-person risk and acquisition dependency. Looking at churn dynamics for a $39 automation community, I'd expect 6-12% monthly churn since automation is a "solve it and leave" topic. At 8% churn, average lifetime is around 12.5 months, giving an LTV of roughly $490. They'd need to replace 100-120 members monthly just to stay flat at a 1,300 base. If they've been running for over two years and only hit 2,400 members, that growth trajectory suggests they're stuck on the treadmill.

The real ceiling depends on the actual market. Automation buyers are often businesses willing to pay much more than $39, so this could be deliberate underpricing for volume or a top-of-funnel play with a hidden backend offer—agency services, DFY, or consulting. I need to check whether there's a premium tier or backend revenue stream not visible on the public page, because if it exists, my revenue estimate is completely off.

For competing, I shouldn't try to match their library size—12 courses is commoditized and automation content decays fast as tool UIs and APIs change. The angle is positioning around current, maintained, versioned content. I should also niche down by vertical or ICP (automation for specific industries or roles beats generic), price up with implementation and office hours rather than down, build recurring reasons to stay like live builds and monthly template updates, and distribute through partnerships with tool vendors, long-tail SEO, and affiliate relationships with agencies instead of fighting their 60k followers head-on. Their churned members are my best target—people who tried and didn't get results.…