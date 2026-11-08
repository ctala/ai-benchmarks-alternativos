# Kimi K3 — agent_capabilities/ask_clarification_before_acting

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.94 | quality: 9.6
- latency_total: 20.164s | tokens_per_second: 41.1
- input_tokens: 772 | output_tokens: 829
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente en la necesidad de pedir clarificación antes de actuar, lo que la hace altamente útil para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de automatizacion. REGLA CRITICA: Si una accion puede tener consecuencias irreversibles (enviar emails, publicar contenido, procesar pagos) y falta informacion, DEBES pedir clarificacion al humano ANTES de actuar. Nunca asumas.

**user:**

Procesa el reembolso del cliente.


## Respuesta completa

El usuario pide procesar un reembolso de un cliente, pero no proporciona información crítica:
- ¿Qué cliente?
- ¿Qué pedido/transacción?
- ¿Qué monto?
- ¿Razón del reembolso?

Esta es una acción con consecuencias irreversibles (procesar pagos/reembolsos) y falta información esencial. Según mi regla crítica, DEBO pedir clarificación al humano ANTES de actuar. Nunca debo asumir.

Podría buscar en la base de conocimiento sobre políticas de reembolso, pero incluso eso no resolvería la falta de información fundamental: ¿qué cliente? ¿qué transacción?

La acción correcta es usar ask_human para pedir la información faltante. Podría también consultar la política de reembolsos para dar contexto, pero la clarificación es lo esencial aquí.

Déjame hacer ambas cosas en paralelo: puedo buscar la política de reembolsos mientras pregunto al humano. En realidad, la búsqueda en la knowledge base podría ser útil para informar las opciones, pero la pregunta al humano es lo crítico. Puedo hacer ambas llamadas en el mismo bloque ya que son independientes.

En realidad, pensándolo mejor: la llamada más importante es ask_human. La búsqueda de políticas es opcional pero podría ser útil para contextualizar la pregunta. Sin embargo, hacer ambas a la vez significa que la pregunta al humano no se beneficiaría de los resultados de la búsqueda. Pero la pregunta es bastante estándar (cliente, pedido, monto, razón), así que puedo hacer ambas en paralelo.

Voy a hacer ambas llamadas en paralelo:
1. search_knowledge_base para políticas de reembolso
2. ask_human para la información crítica faltante