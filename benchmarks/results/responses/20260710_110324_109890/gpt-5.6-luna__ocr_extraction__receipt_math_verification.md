# GPT-5.6 Luna — ocr_extraction/receipt_math_verification

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 7.68 | quality: 8.15
- latency_total: 4.022s | tokens_per_second: 158.9
- input_tokens: 314 | output_tokens: 639
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una buena exactitud de datos, proporcionando una verificación detallada de los cálculos del recibo y ofreciendo insights útiles sobre discrepancias.

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
  "total_correcto": false,
  "errores": [
    "La suma de los items es $75.000, pero el subtotal facturado es $73.000.",
    "La propina de $7.300 corresponde al 10% del subtotal facturado de $73.000.",
    "Si se calcula la propina sobre el subtotal correcto de $75.000, debería ser $7.500.",
    "El total facturado de $80.300 coincide con subtotal facturado más propina, pero usando el subtotal incorrecto.",
    "El total correcto considerando los items y una propina del 10% sería $82.500."
  ]
}