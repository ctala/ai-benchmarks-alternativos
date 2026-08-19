# Nemotron 3 Ultra 550B — agent_capabilities/ask_clarification_before_acting

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 4.1 | quality: 2.67
- latency_total: 2.09s | tokens_per_second: 109.1
- input_tokens: 1173 | output_tokens: 228

## Respuesta completa

The user is asking me to process a refund for a customer. This is an action that has irreversible consequences (processing a payment/refund). According to my critical rule, I need to ask for clarification from the human before acting since there's missing information.

I need to know:
1. Which customer?
2. What order/transaction?
3. What amount?
4. Reason for refund?
5. Any other relevant details?

I should use the ask_human tool to get this information beforeproceeding.