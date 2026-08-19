# GPT-OSS 120B — ocr_extraction/receipt_math_verification

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.3 | quality: 8.75
- latency_total: 17.366s | tokens_per_second: 59.7
- input_tokens: 386 | output_tokens: 1037
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al identificar errores en el recibo y proporcionar cálculos correctos.

## Respuesta completa

```json
{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "precio_total": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "precio_total": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "precio_total": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "precio_total": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "precio_total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000).",
    "La propina sugerida ($7.300) no corresponde al 10 % del subtotal real ($75.000), que debería ser $7.500.",
    "El total facturado ($80.300) no coincide con la suma del subtotal real y la propina correcta ($75.000 + $7.500 = $82.500)."
  ]
}
```