# GPT-5.4 — ocr_extraction/receipt_math_verification

- model_id: `gpt-5.4`
- success: True  | final: 6.91 | quality: 7.04
- latency_total: 4.28s | tokens_per_second: 81.1
- input_tokens: 314 | output_tokens: 347
- judge_score: 4.2 | justificación: 

## Respuesta completa

{
  "items": [
    {
      "descripcion": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total_item": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total_item": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total_item": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total_item": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total_item": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado es 73000, pero la suma de los items es 75000.",
    "La propina sugerida facturada es 7300, pero el 10% del subtotal calculado (75000) es 7500.",
    "El total facturado es 80300, pero subtotal calculado + propina correcta = 82500."
  ]
}