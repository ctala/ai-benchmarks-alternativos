# Seed 2.0 Code — customer_support/ambiguous_issue_classification

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 7.39 | quality: 7.43
- latency_total: 1.755s | tokens_per_second: 46.2
- input_tokens: 808 | output_tokens: 81
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, abordando el problema técnico y la urgencia de la suscripción. Ofrece claridad y utilidad práctica al crear un ticket, aunque carece de profundidad en la resolución del problema y empatía en el tono.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de soporte. Clasifica el problema y crea un ticket.
Prioridades: urgent (servicio caido), high (dinero involucrado), medium (funcionalidad), low (pregunta).

**user:**

Hola, no puedo entrar a mi cuenta desde ayer. Intente cambiar la contrasena pero el email de recuperacion nunca llega. Necesito acceder porque tengo una suscripcion activa que se renueva manana y no quiero que me cobren si no puedo usar el servicio.


## Respuesta completa

[tool_call] create_ticket({"category": "technical", "priority": "high", "summary": "No puede acceder a la cuenta y no recibe email de recuperacion; suscripcion se renueva manana"})