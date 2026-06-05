# Gemma 4 31B (Spark llama-server Q4_K_M) — ocr_extraction/receipt_math_verification

- model_id: `gemma-4-31B-it-Q4_K_M.gguf`
- success: True  | final: 6.52 | quality: 7.04
- latency_total: 42.346s | tokens_per_second: 9.8
- input_tokens: 377 | output_tokens: 414
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "producto": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total_item": 37800
    },
    {
      "producto": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total_item": 7500
    },
    {
      "producto": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total_item": 20700
    },
    {
      "producto": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total_item": 5800
    },
    {
      "producto": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total_item": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Hay una diferencia de $2.000.",
    "El total final es incorrecto porque se basa en un subtotal erróneo."
  ]
}
```