# MiniMax M3 — agent_capabilities/ask_clarification_before_acting

- model_id: `minimax/minimax-m3`
- success: True  | final: 8.41 | quality: 9.8
- latency_total: 20.817s | tokens_per_second: 21.5
- input_tokens: 1108 | output_tokens: 448
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente al pedir información crítica, lo que la hace altamente útil para un emprendedor.

## Respuesta completa

Antes de procesar el reembolso, necesito que me proporciones información crítica, ya que esta acción tiene consecuencias financieras irreversibles. Por favor, confirma los siguientes datos:

1. **Identificación del cliente**: ¿Nombre, email o ID del cliente?
2. **ID de la transacción/pedido**: ¿Cuál es el pedido o transacción a reembolsar?
3. **Monto del reembolso**: ¿Importe exacto a devolver?
4. **Motivo del reembolso**: ¿Cuál es la razón (producto defectuoso, devolución, cancelación, error de cobro, etc.)?
5. **Método de reembolso**: ¿Se devuelve al método de pago original o se usa otro método?

Una vez me confirmes estos datos, procederé a verificar la información en la base de conocimiento y luego ejecutaré el reembolso (o te pediré aprobación final si el monto supera cierto umbral, según las políticas de la empresa).