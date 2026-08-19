# Nemotron 3 Super 120B (DGX Spark Q4_K_M) — ocr_extraction/receipt_math_verification

- model_id: `nemotron-3-super:120b`
- success: True  | final: 6.26 | quality: 7.04
- latency_total: 96.071s | tokens_per_second: 18.4
- input_tokens: 391 | output_tokens: 1768
- judge_score: 4.2 | justificación: 

## Respuesta completa

{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": [
    "El subtotal facturado (73000) no coincide con la suma de los items (75000)."
  ]
}