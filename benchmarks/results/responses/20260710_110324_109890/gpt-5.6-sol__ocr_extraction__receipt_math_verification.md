# GPT-5.6 Sol — ocr_extraction/receipt_math_verification

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 7.08 | quality: 8.15
- latency_total: 7.516s | tokens_per_second: 78.5
- input_tokens: 314 | output_tokens: 590
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al identificar errores en los cálculos del recibo.

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
    "El subtotal facturado es $2.000 menor que la suma de los items.",
    "La propina de $7.300 corresponde al 10% del subtotal facturado de $73.000, pero sobre el subtotal correcto de $75.000 debería ser $7.500.",
    "El total facturado de $80.300 coincide con el subtotal y la propina informados, pero el total correcto según los items y una propina del 10% debería ser $82.500."
  ]
}