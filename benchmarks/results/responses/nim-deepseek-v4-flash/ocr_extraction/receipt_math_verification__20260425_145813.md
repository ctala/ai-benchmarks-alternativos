# DeepSeek V4 Flash (NIM) — ocr_extraction/receipt_math_verification

- model_id: `deepseek-ai/deepseek-v4-flash`
- success: True  | final: 6.41 | quality: 7.04
- latency_total: 259.68s | tokens_per_second: 1.9
- input_tokens: 338 | output_tokens: 482
- judge_score: 4.2 | justificación: 

## Respuesta completa

{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "subtotal_item": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "subtotal_item": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "subtotal_item": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "subtotal_item": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "subtotal_item": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado (73.000) no coincide con la suma de los items (75.000). Hay una diferencia de 2.000.",
    "La propina sugerida (7.300) no corresponde al 10% del subtotal facturado (73.000). El 10% de 73.000 es 7.300, pero el subtotal facturado es incorrecto, por lo que la propina está mal calculada en relación al subtotal real.",
    "El total facturado (80.300) no es correcto. Si el subtotal real es 75.000 y la propina correcta al 10% serían 7.500, el total correcto sería 82.500. Con los valores actuales, 73.000 + 7.300 = 80.300, pero el subtotal base está mal."
  ]
}