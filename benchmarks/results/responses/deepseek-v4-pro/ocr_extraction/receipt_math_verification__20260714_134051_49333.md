# DeepSeek V4 Pro — ocr_extraction/receipt_math_verification

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 7.94 | quality: 8.75
- latency_total: 24.278s | tokens_per_second: 57.4
- input_tokens: 338 | output_tokens: 1394
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una exactitud de datos perfecta, proporcionando una verificación detallada y útil de los cálculos del recibo.

## Respuesta completa

{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "subtotal": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "subtotal": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "subtotal": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "subtotal": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "subtotal": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal impreso en el recibo es incorrecto: la suma real de los ítems es $75.000, pero se indica $73.000.",
    "El total del recibo ($80.300) es incorrecto porque se basa en un subtotal erróneo. El total correcto con 10% de propina sobre $75.000 sería $82.500."
  ]
}