# Llama 4 Maverick — customer_support/angry_customer_refund

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 8.71 | quality: 8.8
- latency_total: 1.676s | tokens_per_second: 54.9
- input_tokens: 731 | output_tokens: 92
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, mostrando empatía y proporcionando pasos prácticos para resolver el problema, lo que la hace altamente útil para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de soporte de una tienda online.
Reglas:
- Siempre muestra empatia antes de tomar accion
- Busca el pedido antes de procesar cualquier reembolso
- Reembolsos mayores a $100 requieren escalamiento a supervisor
- Nunca prometas algo que no puedas cumplir

**user:**

Estoy FURIOSO. Pedi un laptop hace 2 semanas (pedido #ORD-4521) y me llego rota. La pantalla tiene una grieta enorme. Quiero mi dinero de vuelta AHORA. El pedido fue de $899.


## Respuesta completa

Lo siento mucho por la experiencia que has tenido con tu pedido. Me doy cuenta de que recibir un producto dañado puede ser muy frustrante. Entiendo tu enojo y te aseguro que haré todo lo posible para ayudarte a resolver este problema de manera rápida y eficiente.

Primero, necesito verificar la información de tu pedido para proceder con tu solicitud de reembolso. [lookup_order(order_id=ORD-4521)]