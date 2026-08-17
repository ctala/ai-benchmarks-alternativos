# Llama 4 Maverick — customer_support/multi_issue_conversation

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 9.03 | quality: 9.6
- latency_total: 3.684s | tokens_per_second: 107.2
- input_tokens: 723 | output_tokens: 395
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, abordando cada problema con acciones específicas, aunque la profundidad podría mejorarse con más detalles sobre el envío express.

## Respuesta completa

1. El pedido #ORD-7788 no ha llegado a tiempo: 
    - lookup_order(order_id="ORD-7788") para verificar el estado del pedido.
    - Si está atrasado, create_ticket(category="shipping", priority="medium", summary="Pedido #ORD-7788 no ha llegado") para reportar el problema.

2. Cobro doble por el pedido #ORD-7790:
    - lookup_order(order_id="ORD-7790") para verificar los detalles del pedido y los cargos.
    - Si se confirma el cobro doble, process_refund(order_id="ORD-7790", amount=45, reason="Cobro doble") para procesar el reembolso del cargo extra.

3. La app se cierra sola al ver pedidos en iPhone:
    - create_ticket(category="technical", priority="high", summary="App se cierra al ver pedidos en iPhone") para reportar el problema técnico.

4. Consulta sobre envío express para el próximo pedido:
    - No hay función directa para responder esta consulta, pero se puede escalar a un agente humano si es necesario.

Dado que necesitas resolver al menos el problema del cobro doble hoy, comenzaré con eso.

1. Verificar el pedido #ORD-7790: [lookup_order(order_id="ORD-7790")]
2. Procesar el reembolso si corresponde: [process_refund(order_id="ORD-7790", amount=45, reason="Cobro doble")]
3. Reportar el problema de entrega del pedido #ORD-7788: [create_ticket(category="shipping", priority="medium", summary="Pedido #ORD-7788 no ha llegado", customer_email="customer@example.com")]
4. Reportar el problema técnico con la app: [create_ticket(category="technical", priority="high", summary="App se cierra al ver pedidos en iPhone", customer_email="customer@example.com")]