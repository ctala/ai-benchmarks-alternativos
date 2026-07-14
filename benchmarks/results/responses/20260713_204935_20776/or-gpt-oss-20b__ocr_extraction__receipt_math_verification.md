# GPT-OSS 20B — ocr_extraction/receipt_math_verification

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.45 | quality: 8.75
- latency_total: 10.548s | tokens_per_second: 115.0
- input_tokens: 373 | output_tokens: 1213
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una exactitud de datos perfecta, proporcionando una verificación detallada de los cálculos del recibo, lo que la hace altamente útil para un emprendedor.

## Respuesta completa

```json
{
  "items": [
    {
      "name": "Lomo vetado",
      "quantity": 2,
      "unit_price": 18900,
      "total_price": 37800
    },
    {
      "name": "Ensalada cesar",
      "quantity": 1,
      "unit_price": 7500,
      "total_price": 7500
    },
    {
      "name": "Pisco sour",
      "quantity": 3,
      "unit_price": 6900,
      "total_price": 20700
    },
    {
      "name": "Postre brownie",
      "quantity": 1,
      "unit_price": 5800,
      "total_price": 5800
    },
    {
      "name": "Agua mineral 1.5L",
      "quantity": 1,
      "unit_price": 3200,
      "total_price": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado (73.000) es incorrecto; el subtotal correcto es 75.000.",
    "La propina calculada (7.300) corresponde al subtotal facturado; si se usa el subtotal correcto, la propina debería ser 7.500.",
    "El total facturado (80.300) no coincide con el subtotal correcto + propina correcta; el total correcto sería 82.500."
  ]
}
```