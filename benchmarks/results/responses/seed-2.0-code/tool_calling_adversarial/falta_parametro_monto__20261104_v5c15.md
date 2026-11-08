# Seed 2.0 Code — tool_calling_adversarial/falta_parametro_monto

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 7.57 | quality: 8.5
- latency_total: 16.073s | tokens_per_second: 69.2
- input_tokens: 768 | output_tokens: 1113
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando los detalles necesarios para proceder con la emisión de la factura, incluyendo la solicitud del monto faltante, lo que la hace altamente útil para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emítele la factura al cliente CL-2291 por la consultoría de octubre.


## Respuesta completa

Para poder emitir la factura, necesito que me proporciones el **monto total** de la consultoría de octubre. 

La herramienta `emitir_factura` requiere obligatoriamente:
- `cliente_id` (que ya proporcionaste: CL-2291)
- `monto` (el importe total de la factura)
- `concepto` (la descripción, que en este caso sería "consultoría de octubre")

Una vez que me indiques el monto, podré proceder a emitir la factura. ¿Cuál es el importe total de la consultoría?