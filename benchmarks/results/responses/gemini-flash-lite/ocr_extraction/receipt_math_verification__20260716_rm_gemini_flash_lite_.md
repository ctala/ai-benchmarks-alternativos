# Gemini 2.5 Flash Lite — ocr_extraction/receipt_math_verification

- model_id: `google/gemini-2.5-flash-lite`
- success: True  | final: 8.82 | quality: 8.75
- latency_total: 1.614s | tokens_per_second: 291.9
- input_tokens: 364 | output_tokens: 471
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una exactitud de datos perfecta, proporcionando una verificación detallada y útil de los cálculos del recibo.

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
    "El subtotal facturado ($73.000) no coincide con el subtotal calculado ($75.000).",
    "La propina sugerida ($7.300) se calculó sobre un subtotal incorrecto. El subtotal correcto es $75.000, por lo que la propina del 10% debería ser $7.500.",
    "El total facturado ($80.300) es incorrecto debido a los errores en el subtotal y la propina."
  ]
}
```