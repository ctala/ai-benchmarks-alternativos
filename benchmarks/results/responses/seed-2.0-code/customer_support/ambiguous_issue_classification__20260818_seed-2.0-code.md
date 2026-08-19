# Seed 2.0 Code — customer_support/ambiguous_issue_classification

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 7.01 | quality: 7.56
- latency_total: 7.463s | tokens_per_second: 48.8
- input_tokens: 809 | output_tokens: 364
- judge_score: 4.4 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de soporte. Clasifica el problema y crea un ticket.
Prioridades: urgent (servicio caido), high (dinero involucrado), medium (funcionalidad), low (pregunta).

**user:**

Hola, no puedo entrar a mi cuenta desde ayer. Intente cambiar la contrasena pero el email de recuperacion nunca llega. Necesito acceder porque tengo una suscripcion activa que se renueva manana y no quiero que me cobren si no puedo usar el servicio.


## Respuesta completa

Let me analyze the user's request:

1. They can't access their account since yesterday
2. Tried to reset password but didn't receive recovery email
3. They have an active subscription renewing tomorrow and don't want to be charged if they can't use the service

This involves:
- Technical issue with account access (technical category)
- Potential billing issue with subscription renewal

Since the subscription renews tomorrow and involves money (potential unwanted charge), this should be high priority.

I need to:
1. Create a ticket for this issue
2. The category could be "technical" (can't access account) or "billing" (subscription concern)
3. Priority should be "high" since there's money involved (potential unwanted charge)

Let me create a ticket with category "technical" since the primary issue is account access, but priority "high" because of the billing concern.

Actually, looking more carefully:
- The main immediate issue is technical (can't access account)
- But there's a billing concern with the subscription renewal
- Since money is involved (potential unwanted charge), this is high priority

I'll create a ticket with category "technical" and priority "high".