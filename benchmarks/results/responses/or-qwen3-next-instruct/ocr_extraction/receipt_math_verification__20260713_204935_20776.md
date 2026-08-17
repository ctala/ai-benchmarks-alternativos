# Qwen 3-Next 80B Instruct — ocr_extraction/receipt_math_verification

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 8.5 | quality: 8.75
- latency_total: 3.523s | tokens_per_second: 125.5
- input_tokens: 354 | output_tokens: 442
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al identificar errores en los cálculos del recibo.

## Respuesta completa

{
  "items": [
    {
      "descripcion": "2x Lomo vetado",
      "precio_unitario": 18900,
      "cantidad": 2,
      "total_item": 37800
    },
    {
      "descripcion": "1x Ensalada cesar",
      "precio_unitario": 7500,
      "cantidad": 1,
      "total_item": 7500
    },
    {
      "descripcion": "3x Pisco sour",
      "precio_unitario": 6900,
      "cantidad": 3,
      "total_item": 20700
    },
    {
      "descripcion": "1x Postre brownie",
      "precio_unitario": 5800,
      "cantidad": 1,
      "total_item": 5800
    },
    {
      "descripcion": "1x Agua mineral 1.5L",
      "precio_unitario": 3200,
      "cantidad": 1,
      "total_item": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000).",
    "La propina sugerida ($7.300) se calculó sobre el subtotal facturado ($73.000), pero debería basarse en el subtotal real ($75.000), lo que daría $7.500.",
    "El total facturado ($80.300) es incorrecto: debería ser $75.000 + $7.500 = $82.500."
  ]
}