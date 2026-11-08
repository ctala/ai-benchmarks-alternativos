# Qwen3-Coder-Next (OpenRouter FP8) — customer_support/multi_issue_conversation

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 5.52 | quality: 4.24
- latency_total: 1.036s | tokens_per_second: 56.0
- input_tokens: 804 | output_tokens: 58
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante al buscar los pedidos, pero carece de profundidad y no aborda directamente el problema del cobro doble, lo que limita su utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de soporte. Identifica TODOS los problemas y aborda cada uno.

**user:**

Tengo varios problemas:
1. Mi pedido #ORD-7788 debio llegar hace 3 dias y no ha llegado
2. Me cobraron dos veces por el pedido #ORD-7790 ($45 cada cargo)
3. La app se cierra sola cuando intento ver mis pedidos en el iPhone
4. Quiero saber si tienen envio express para mi proximo pedido

Necesito resolver al menos lo del cobro doble hoy.


## Respuesta completa

[tool_call] lookup_order({"order_id": "ORD-7788"})
[tool_call] lookup_order({"order_id": "ORD-7790"})