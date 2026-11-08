# Qwen 3-Next 80B Instruct — string_precision/copy_mixed_special

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 9.7 | quality: 10.0
- latency_total: 0.507s | tokens_per_second: 65.1
- input_tokens: 106 | output_tokens: 33

## Entrada exacta (lo que recibió el modelo)

**system:**

Tu UNICA tarea es copiar strings exactamente. NO expliques, NO agregues contexto. Responde SOLO con el string pedido, nada mas.

**user:**

Copia este string EXACTAMENTE, caracter por caracter. Responde SOLO con el string, sin comillas, sin explicacion:

r2-secret_KEY.2024/abc+def==ghi&jkl#mno@pqr$stu%vwx^yza


## Respuesta completa

r2-secret_KEY.2024/abc+def==ghi&jkl#mno@pqr$stu%vwx^yza