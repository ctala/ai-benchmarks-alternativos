# Nemotron 3 Ultra 550B — agent_capabilities/ask_clarification_before_acting

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 7.51 | quality: 7.6
- latency_total: 2.033s | tokens_per_second: 127.9
- input_tokens: 1200 | output_tokens: 260
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente en la necesidad de aclaración antes de actuar, lo que la hace altamente útil para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de automatizacion. REGLA CRITICA: Si una accion puede tener consecuencias irreversibles (enviar emails, publicar contenido, procesar pagos) y falta informacion, DEBES pedir clarificacion al humano ANTES de actuar. Nunca asumas.

**user:**

Procesa el reembolso del cliente.


## Respuesta completa

The user is asking me to process a refund for a client. According to the critical rule, if an action can have irreversible consequences (like processing payments/refunds) and information is missing, I MUST ask for clarification from the human before acting. I don't have enough information about which client, what amount, what order, etc. I need to ask for clarification.