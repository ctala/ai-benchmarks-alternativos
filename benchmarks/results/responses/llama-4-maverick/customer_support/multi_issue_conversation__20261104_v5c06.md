# Llama 4 Maverick — customer_support/multi_issue_conversation

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 9.07 | quality: 9.6
- latency_total: 2.771s | tokens_per_second: 71.1
- input_tokens: 723 | output_tokens: 197
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, abordando cada problema con acciones específicas, aunque la profundidad podría mejorarse con más detalles sobre el envío express.

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

1. El pedido #ORD-7788 no ha llegado: 
    - Función: create_ticket(category='shipping', priority='medium', summary='Pedido #ORD-7788 no ha llegado')
2. Cobro doble en el pedido #ORD-7790: 
    - Función: lookup_order(order_id='ORD-7790') para verificar el pedido y luego process_refund(order_id='ORD-7790', amount=45, reason='Cobro doble')
3. La app se cierra sola al ver pedidos en iPhone: 
    - Función: create_ticket(category='technical', priority='high', summary='La app se cierra sola al ver pedidos en iPhone')
4. Consulta sobre envio express: 
    - No hay función directa para responder esta pregunta.

Para resolver al menos el problema del cobro doble hoy, primero necesito verificar el pedido #ORD-7790. 
[lookup_order(order_id='ORD-7790')]