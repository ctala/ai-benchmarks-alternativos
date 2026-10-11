# Bonsai 2 27B — customer_support/ambiguous_issue_classification

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 6.63 | quality: 6.8
- latency_total: 11.623s | tokens_per_second: 28.9
- input_tokens: 631 | output_tokens: 336
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, abordando adecuadamente la clasificación y creación de un ticket. Ofrece una estructura clara y utilidad práctica, aunque podría profundizar más en la resolución del problema.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de soporte. Clasifica el problema y crea un ticket.
Prioridades: urgent (servicio caido), high (dinero involucrado), medium (funcionalidad), low (pregunta).

**user:**

Hola, no puedo entrar a mi cuenta desde ayer. Intente cambiar la contrasena pero el email de recuperacion nunca llega. Necesito acceder porque tengo una suscripcion activa que se renueva manana y no quiero que me cobren si no puedo usar el servicio.


## Respuesta completa

We need respond. Need classify and create ticket. User Spanish. Problem cannot access account since yesterday, password reset email not arriving, needs access because active subscription renews tomorrow and doesn't want charged if can't use service. Need determine priority. Priority guide: urgent service down, high money involved, medium functionality, low question. This is account access + money involved (subscription renewal tomorrow). Also can't access due to email not arriving. Could be high due money involved. Need maybe create ticket category? technical? product? billing? It's technical/access account, billing concern. Need maybe lookup order? They mention active subscription but no order ID. Could process refund? No, don't know amount/order. Could escalate? The task says classify and create ticket. We can create ticket. Need include customer_email? Not required. priority high likely. summary in Spanish. category technical (can't access account / email recovery). Need maybe mention urgency: high due upcoming billing. Could create ticket. Then final say classified high. Ensure no data missing. Let's call create_ticket with category technical, priority high, summary. Maybe customer_email omitted.
