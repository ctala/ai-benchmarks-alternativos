# Poolside Laguna S 2.1 — ocr_extraction/receipt_math_verification

- model_id: `poolside/laguna-s-2.1`
- success: True  | final: 7.65 | quality: 7.5
- latency_total: 3.459s | tokens_per_second: 91.9
- input_tokens: 420 | output_tokens: 318
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con cálculos correctos y errores identificados adecuadamente, lo que la hace muy útil para un emprendedor.

## Respuesta completa

{
  "items": [
    {"nombre": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900},
    {"nombre": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500},
    {"nombre": "Pisco sour", "cantidad": 3, "precio_unitario": 6900},
    {"nombre": "Postre brownie", "cantidad": 1, "precio_unitario": 5800},
    {"nombre": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 81900,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal calculado ($81.900) no coincide con el subtotal facturado ($73.000)",
    "La propina sugerida (10%) debería ser $8.190, no $7.300",
    "El total debería ser $90.090, no $80.300"
  ]
}