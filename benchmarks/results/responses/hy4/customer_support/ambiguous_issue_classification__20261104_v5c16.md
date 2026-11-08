# Tencent Hy4 — customer_support/ambiguous_issue_classification

- model_id: `tencent/hy4`
- success: True  | final: 7.52 | quality: 7.6
- latency_total: 3.987s | tokens_per_second: 66.7
- input_tokens: 622 | output_tokens: 266
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, identificando correctamente el problema técnico y el riesgo financiero, con una estructura clara y utilidad práctica para la gestión de tickets, aunque la empatía podría mejorarse.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de soporte. Clasifica el problema y crea un ticket.
Prioridades: urgent (servicio caido), high (dinero involucrado), medium (funcionalidad), low (pregunta).

**user:**

Hola, no puedo entrar a mi cuenta desde ayer. Intente cambiar la contrasena pero el email de recuperacion nunca llega. Necesito acceder porque tengo una suscripcion activa que se renueva manana y no quiero que me cobren si no puedo usar el servicio.


## Respuesta completa

Voy a clasificar el caso y crear el ticket correspondiente. Hay un problema técnico (acceso + email de recuperación) y además **dinero involucrado** (renovación mañana), por lo que la prioridad es **high** según las reglas, con categoría **technical** y escalado urgente por el riesgo de cobro inmediato.

