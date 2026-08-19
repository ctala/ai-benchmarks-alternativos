# DeepSeek R1 (reasoning) — ocr_extraction/receipt_math_verification

- model_id: `deepseek/deepseek-r1`
- success: True  | final: 5.75 | quality: 6.75
- latency_total: 183.356s | tokens_per_second: 25.9
- input_tokens: 339 | output_tokens: 4746
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, identificando correctamente los errores en el subtotal, con claridad y utilidad práctica para un emprendedor, aunque carece de profundidad adicional más allá de la verificación básica.

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
  "propina_correcta": true,
  "total_correcto": true,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items. Suma calculada: $75.000 (diferencia de $2.000)."
  ]
}