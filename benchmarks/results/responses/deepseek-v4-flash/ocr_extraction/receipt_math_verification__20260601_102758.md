# DeepSeek V4 Flash (OpenRouter) — ocr_extraction/receipt_math_verification

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.71 | quality: 8.15
- latency_total: 24.309s | tokens_per_second: 105.4
- input_tokens: 338 | output_tokens: 2563
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una exactitud de datos perfecta, y proporciona una verificación detallada de los cálculos, lo que la hace muy útil para un emprendedor.

## Respuesta completa

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
    "El subtotal registrado (73.000) no coincide con la suma de los items (75.000).",
    "La propina sugerida (7.300) es el 10% del subtotal facturado, pero debería ser el 10% del subtotal correcto (7.500).",
    "El total facturado (80.300) es incorrecto; el total correcto sería 82.500 (subtotal correcto + 10% de propina)."
  ]
}