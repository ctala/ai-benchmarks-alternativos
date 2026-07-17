# GPT-5.4 Mini — ocr_extraction/receipt_math_verification

- model_id: `gpt-5.4-mini`
- success: True  | final: 8.45 | quality: 8.75
- latency_total: 2.82s | tokens_per_second: 123.4
- input_tokens: 314 | output_tokens: 348
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una exactitud de datos perfecta, proporcionando una verificación detallada de los cálculos del recibo, útil para un emprendedor.

## Respuesta completa

{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total_linea": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total_linea": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total_linea": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total_linea": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total_linea": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000).",
    "La propina sugerida del 10% debería ser $7.500, no $7.300.",
    "El total correcto, usando el subtotal calculado, debería ser $82.500, no $80.300."
  ]
}