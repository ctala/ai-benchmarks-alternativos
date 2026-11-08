# Seed 2.0 Code — customer_support/multi_issue_conversation

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 4.2 | quality: 2.82
- latency_total: 1.153s | tokens_per_second: 33.8
- input_tokens: 821 | output_tokens: 39
- judge_score: 2.0 | justificación: La respuesta intenta abordar un problema, pero no resuelve directamente el problema del cliente con el cobro doble, que era la prioridad, y carece de profundidad y utilidad práctica.

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