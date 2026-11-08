# Tencent Hy4 preview — customer_support/ambiguous_issue_classification

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.6 | quality: 9.8
- latency_total: 8.245s | tokens_per_second: 42.3
- input_tokens: 622 | output_tokens: 349
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, abordando tanto el problema técnico como el financiero con una estructura organizada y un tono empático.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de soporte. Clasifica el problema y crea un ticket.
Prioridades: urgent (servicio caido), high (dinero involucrado), medium (funcionalidad), low (pregunta).

**user:**

Hola, no puedo entrar a mi cuenta desde ayer. Intente cambiar la contrasena pero el email de recuperacion nunca llega. Necesito acceder porque tengo una suscripcion activa que se renueva manana y no quiero que me cobren si no puedo usar el servicio.


## Respuesta completa

Hola, entiendo tu situación: no puedes acceder a tu cuenta, el correo de recuperación no llega y además hay una suscripción activa que se renovaría mañana. Voy a ayudarte.

Clasifico el problema en dos frentes:
1. **Acceso / recuperación de contraseña** → categoría `technical` (funcionalidad del sistema de login), prioridad **medium** (afecta funcionalidad, no el servicio caído).
2. **Riesgo de cobro de renovación** → involucra dinero, así que lo trataré con prioridad **high**.

Voy a crear los tickets correspondientes y escalar el tema del cobro para que se revise antes de la renovación.

Primero necesito un dato: para gestionar el tema de la suscripción y el posible reembolso o cancelación del cargo, **¿podrías facilitarme tu email y el ID del pedido o de la suscripción?** Mientras tanto, creo los registros: