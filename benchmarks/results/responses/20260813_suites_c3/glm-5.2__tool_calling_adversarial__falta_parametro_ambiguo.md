# GLM 5.2 — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `z-ai/glm-5.2`
- success: True  | final: 6.8 | quality: 7.1
- latency_total: 5.987s | tokens_per_second: 16.4
- input_tokens: 507 | output_tokens: 98
- judge_score: 4.0 | justificación: La respuesta es precisa al reconocer la necesidad de desambiguar el cliente antes de emitir la factura, lo cual es relevante dado el contexto de múltiples clientes posibles. Ofrece un insight útil sobre la importancia de la identificación correcta del cliente, aunque no profundiza en cómo manejar la desambiguación. La claridad es excelente, con una estructura lógica y fácil de entender. La utilidad práctica es alta, ya que proporciona un paso esencial para emprendedores que podrían enfrentar situaciones similares.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

Primero necesito buscar al cliente "Rodríguez" en el CRM para obtener su ID y poder emitir la factura.