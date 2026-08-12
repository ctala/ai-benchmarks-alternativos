# Llama 4 Maverick — customer_support/multi_issue_conversation

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 9.11 | quality: 9.6
- latency_total: 4.331s | tokens_per_second: 117.3
- input_tokens: 723 | output_tokens: 508
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, abordando cada problema con acciones específicas y detalladas, lo que la hace muy útil para un emprendedor.

## Respuesta completa

1. El problema con el pedido #ORD-7788 parece estar relacionado con el envío, ya que el cliente indica que no ha llegado a pesar de que debió hacerlo hace 3 días. La categoría para este problema sería "shipping".

2. El problema con el pedido #ORD-7790 está relacionado con el cobro doble, lo que sugiere un problema de facturación. La categoría para este problema sería "billing".

3. El problema con la aplicación que se cierra sola al intentar ver los pedidos en un iPhone está relacionado con un problema técnico. La categoría para este problema sería "technical".

4. La pregunta sobre si tienen envío express para el próximo pedido es una consulta general que podría clasificarse bajo "other" o directamente responderse según las políticas de la empresa.

Para abordar al menos el problema del cobro doble hoy, se puede crear un ticket de soporte con la categoría "billing" y prioridad "high" o "urgent" dependiendo de la urgencia percibida.

Primero, se necesita verificar el estado del pedido #ORD-7790 para entender mejor el problema del cobro doble.

[lookup_order(order_id='ORD-7790')]

Una vez que se tenga la información del pedido, se puede proceder a crear un ticket de soporte para el problema de cobro doble.

[create_ticket(category='billing', priority='high', summary='Cobro doble por el pedido #ORD-7790', customer_email='email del cliente')] 

Suponiendo que el email del cliente es conocido.

Si el problema requiere una acción inmediata como un reembolso, se puede procesar el reembolso después de verificar el monto cobrado dos veces.

[process_refund(order_id='ORD-7790', amount=45, reason='Cobro doble')] 

Para los demás problemas, se pueden crear tickets de soporte adicionales:

[create_ticket(category='shipping', priority='medium', summary='Pedido #ORD-7788 no ha llegado', customer_email='email del cliente')]
[create_ticket(category='technical', priority='medium', summary='La app se cierra sola al ver pedidos en iPhone', customer_email='email del cliente')]

Y para la pregunta sobre el envío express, se puede responder directamente al cliente según las políticas de la empresa. Si es necesario escalar el caso a un agente humano, se puede hacer con la función correspondiente.

[escalate_to_human(reason='Múltiples problemas con el pedido y la aplicación', priority='urgent')]