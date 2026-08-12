# Tencent Hy3 — customer_support/ambiguous_issue_classification

- model_id: `tencent/hy3`
- success: True  | final: 8.62 | quality: 9.6
- latency_total: 13.186s | tokens_per_second: 47.2
- input_tokens: 655 | output_tokens: 623
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, mostrando empatía y proporcionando una clasificación adecuada del problema.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de soporte. Clasifica el problema y crea un ticket.
Prioridades: urgent (servicio caido), high (dinero involucrado), medium (funcionalidad), low (pregunta).

**user:**

Hola, no puedo entrar a mi cuenta desde ayer. Intente cambiar la contrasena pero el email de recuperacion nunca llega. Necesito acceder porque tengo una suscripcion activa que se renueva manana y no quiero que me cobren si no puedo usar el servicio.


## Respuesta completa

Entiendo su situación. Tiene un problema de acceso a la cuenta (no llega el email de recuperación) y, como tiene una suscripción que se renueva mañana, hay dinero de por medio. Esto clasifica como **prioridad alta** y categoría **técnica** (acceso a cuenta).

Voy a crear el ticket de soporte correspondiente.