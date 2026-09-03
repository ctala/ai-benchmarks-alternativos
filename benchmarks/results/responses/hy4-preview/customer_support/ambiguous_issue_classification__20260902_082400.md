# Tencent Hy4 preview — customer_support/ambiguous_issue_classification

- model_id: `tencent/hy4-preview`
- success: True  | final: 6.32 | quality: 6.53
- latency_total: 8.168s | tokens_per_second: 37.2
- input_tokens: 619 | output_tokens: 304
- judge_score: 4.0 | justificación: La respuesta identifica correctamente los problemas y propone una acción clara, mostrando comprensión y empatía.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de soporte. Clasifica el problema y crea un ticket.
Prioridades: urgent (servicio caido), high (dinero involucrado), medium (funcionalidad), low (pregunta).

**user:**

Hola, no puedo entrar a mi cuenta desde ayer. Intente cambiar la contrasena pero el email de recuperacion nunca llega. Necesito acceder porque tengo una suscripcion activa que se renueva manana y no quiero que me cobren si no puedo usar el servicio.


## Respuesta completa

Veo dos problemas distintos aqui: uno tecnico de acceso y uno de facturacion con dinero en riesgo. Voy a crear ambos tickets.