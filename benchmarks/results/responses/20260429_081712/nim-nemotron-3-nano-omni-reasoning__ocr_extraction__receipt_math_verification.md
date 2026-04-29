# Nemotron 3 Nano Omni 30B-A3B Reasoning (NIM) — ocr_extraction/receipt_math_verification

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning`
- success: True  | final: 6.91 | quality: 7.04
- latency_total: 5.536s | tokens_per_second: 264.1
- input_tokens: 355 | output_tokens: 1462
- judge_score: 4.2 | justificación: 

## Respuesta completa

{
  "items": [
    {
      "descripcion": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "precio_total": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "precio_total": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "precio_total": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "precio_total": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
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
    "El subtotal sumado de los ítems es $75.000, pero el recibo indica $73.000.",
    "La propina sugerida (10%) sobre el subtotal correcto debería ser $7.500, no $7.300.",
    "El total calculado con subtotal y propina correctas sería $82.500, no $80.300."
  ]
}