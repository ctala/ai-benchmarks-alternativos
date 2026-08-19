# Seed 2.1 Turbo — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 7.0 | quality: 8.0
- latency_total: 47.586s | tokens_per_second: 43.0
- input_tokens: 222 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa


El usuario quiere un experimento para MATAR su hipótesis, la cual se centra en si small marketing agencies would pay $200/month for automated reporting tools. The core goal is to design a cheap, fast experiment to conclusively disprove the hypothesis instead of building a product. I’ve confirmed the hypothesis actually refers to small agencies having sufficient pain point with client reporting to pay recurrently for automation, and we should first test users’ willingness to pay instead of just interest. The low-cost solution is to run a real payment test offering manual reporting service with full refund guarantee, as people won’t pay for a tool if they won’t even pay for manual service.

I’ve clarified the three core assumptions supporting the hypothesis, and confirmed the second assumption — small agencies’ willingness to pay $200/month for reporting pain point solutions — is the weakest link to target.

To make the test as fast and low-cost as possible, I’ve defined the clear target small marketing agency segment: 1-5 person agencies managing 3-15 digital marketing clients, currently spending over 2 hours per client monthly on manual reporting.

I’ve finalized the core execution logic for the test: to avoid extra costs and speed up the process, I will skip paid traffic acquisition and instead directly reach out to agencies already complaining about reporting pain points via platforms like LinkedIn or agency-focused Facebook groups. Next, I will break down the experiment step by step, covering costs, time frames and clear failure judgment criteria.

I’ve named the test the "Manual Monthly Reporting Payment Test", a classic Wizard of Oz variant without a real product. If agencies won’t pay for the full manual reporting service, they definitely won’t pay for an automated reporting tool, which can directly invalidate the hypothesis. I’ve also refined the target agency screening criteria to 1-5 employee digital marketing agencies managing 5-15 active clients, currently spending over 1 hour per client monthly on manual reporting.

The target agencies are specified as located in Spanish-speaking countries. I’ve confirmed three ways to quickly get 20 eligible contacts: join relevant small agency communities, outreach to qualified decision-makers on LinkedIn, and ask for referrals from industry acquaintances.

I’ve confirmed that spending 4 hours per day for 2 consecutive days is sufficient to collect 20 eligible contacts, and the offer will be presented in the first outreach message to save time. I will also design a concise, direct outreach message to quickly filter out target users with the required pain point. I’ve finalized the full outreach script for both LinkedIn and small agency communities, clearly stating the service details, price and 100% unconditional refund guarantee for the first month if the service fails to save at least 3 hours of work.

The follow-up line in the outreach script will ask if the recipient is interested in the trial this month, with only 5 spots available per month to limit workload. The experiment costs $0 if using free platforms; a $50 Facebook ad budget is optional for faster contact sourcing, but not required.
