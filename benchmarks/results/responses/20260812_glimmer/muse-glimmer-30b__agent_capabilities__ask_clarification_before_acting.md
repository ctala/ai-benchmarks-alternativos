# Muse Glimmer 30B — agent_capabilities/ask_clarification_before_acting

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.81 | quality: 9.4
- latency_total: 3.57s | tokens_per_second: 128.3
- input_tokens: 1132 | output_tokens: 458
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente en la necesidad de obtener más información antes de proceder, lo que la hace altamente útil para un emprendedor.

## Respuesta completa

We need to process refund of customer. The user says "Procesa el reembolso del cliente." No details given. We need to process refund. Critical rule: If action can have irreversible consequences (send emails, publish content, process payments) and lacks information, MUST ask clarification before acting. Never assume.

So we need to ask clarification: which customer? amount? reason? order? etc.

We have tools: ask_human, run_skill process_refund, etc.

Skill process_refund likely needs parameters. Let's check skill definition: process_refund is a skill. Parameters? Not specified. Probably needs customer ID, amount, reason, etc.

We must ask for clarification. Use ask_human.

We need question, reason, options optional.

We should ask: ¿De qué cliente? ¿Monto? ¿Orden? etc.

Also we could search knowledge base for recent refunds? Maybe search knowledge base for customer? But no customer info.

We should ask human.

Probably ask: ¿Podrías proporcionar el ID del cliente, número de orden y monto a reembolsar? Reason: falta información para procesar reembolso irreversible.

Let's use ask_human.

Parameters: question, reason, options.

Question: "¿De qué cliente necesitas procesar el reembolso y cuál es el monto, número de orden y motivo?" Reason: "La acción de procesar un reembolso es irreversible y no tengo información del cliente ni del monto."

Options maybe not needed.

Make sure to follow format.

We should not assume.

Thus call ask_human.