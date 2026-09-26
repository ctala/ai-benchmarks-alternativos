# Ling 3.0 Flash VL — customer_support/ambiguous_issue_classification

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 7.86 | quality: 7.8
- latency_total: 5.237s | tokens_per_second: 129.8
- input_tokens: 731 | output_tokens: 680
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, proporcionando pasos prácticos para resolver el problema, aunque la profundidad podría mejorarse con más detalles sobre posibles soluciones técnicas.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de soporte. Clasifica el problema y crea un ticket.
Prioridades: urgent (servicio caido), high (dinero involucrado), medium (funcionalidad), low (pregunta).

**user:**

Hola, no puedo entrar a mi cuenta desde ayer. Intente cambiar la contrasena pero el email de recuperacion nunca llega. Necesito acceder porque tengo una suscripcion activa que se renueva manana y no quiero que me cobren si no puedo usar el servicio.


## Respuesta completa

Entiendo tu preocupación, es una situación complicada. Vamos a trabajar en esto. Para poder crear un ticket de soporte y ayudarte de manera efectiva, necesito algunos datos:

1. **¿Cuál es tu correo electrónico asociado a la cuenta?** (Esto me ayudará a identificar tu cuenta y el problema)
2. **¿Tienes algún ID de pedido o suscripción** que puedas proporcionarme?

Mientras tanto, según lo que describes:

- **No puedes acceder a tu cuenta** → Problema técnico
- **Tienes una suscripción activa que se renueva mañana** → Hay dinero involucrado, lo cual eleva la prioridad

Voy a clasificar esto como un problema de prioridad **alta** (alta implicación económica con la renovación de tu suscripción) en la categoría **técnica**. Pero necesito tu correo electrónico para crear el ticket. ¿Puedes proporcionármelo?