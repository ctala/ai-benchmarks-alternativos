# Seed 2.0 Code — customer_support/multi_issue_conversation

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 6.81 | quality: 7.5
- latency_total: 15.549s | tokens_per_second: 41.3
- input_tokens: 822 | output_tokens: 642
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, abordando cada problema con pasos lógicos, aunque podría profundizar más en la resolución del problema de doble cobro.

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

Got it, let's tackle this step by step. First, the user has four issues:

1. Order #ORD-7788 is 3 days late.
2. Double charge for #ORD-7790 ($45 each).
3. App crashes on iPhone when viewing orders.
4. Inquiry about express shipping for next order.

First, for the double charge (ORD-7790), I need to check the order details maybe? Wait, the user mentioned two charges of $45 each. But to process a refund, I need the order ID, amount, reason. But first, maybe I should look up the order to confirm? Wait, the functions: lookup_order for order info. Also, the double charge is for ORD-7790, so first, maybe lookup that order to see the transactions. Also, the late order ORD-7788, need to lookup that too. Then the app issue is technical, so maybe a ticket. The express shipping inquiry is a question, but let's handle each.

Wait, the user said need to resolve at least the double charge today. Let's list the steps:

First, for ORD-7788 (late delivery): need to lookup the order to check shipping status, tracking, etc.

For ORD-7790 (double charge): lookup the order to confirm the charges, then process refund for one $45 charge.

For the app crash: that's technical, so create a ticket with category technical, priority maybe medium? Wait, the user didn't specify urgency, but it's an app issue. The summary would be "App se cierra sola al intentar ver mis pedidos en iPhone".

For express shipping inquiry: need to answer, but maybe first handle the actionable items.

Wait, let's start by looking up the two orders to get details. So first, call lookup_order for ORD-7788 and ORD-7790. Wait, can I do two lookups? Let's see, the functions: lookup_order takes order_id. So first, maybe call lookup_order for ORD-7788, then ORD-7790? Or in parallel? The system allows multiple tool calls. Let me structure:

First, lookup ORD-7788 to check shipping status. Then lookup ORD-7790 to check the charges. Then, for the app issue, create a technical ticket. For the express shipping, maybe that's a general question, but let's see.

Wait, the user's main priority is the double charge. So first, confirm the charges for ORD-7790. Let's call lookup_order for ORD-7790 first, and ORD-7788. Let's do two lookup calls.