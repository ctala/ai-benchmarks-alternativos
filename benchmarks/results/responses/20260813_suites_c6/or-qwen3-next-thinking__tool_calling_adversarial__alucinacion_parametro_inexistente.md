# Qwen 3-Next 80B Thinking — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 3.99 | quality: 2.9
- latency_total: 9.587s | tokens_per_second: 174.2
- input_tokens: 579 | output_tokens: 1670
- judge_score: 1 | justificación: La respuesta es incorrecta y no relevante, ya que inventa un parámetro 'query' que no es parte de la instrucción original, y no aborda el requisito de filtrar por facturas impagas o ordenar por monto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

釜
{"name": "buscar_cliente", "arguments": {"query": "Andes"}}
釜