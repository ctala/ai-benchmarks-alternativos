# Nemotron Nano 9B v2 — ocr_extraction/receipt_math_verification

- model_id: `nvidia/nemotron-nano-9b-v2:free`
- success: True  | final: 5.53 | quality: 5.0
- latency_total: 36.766s | tokens_per_second: 32.9
- input_tokens: 380 | output_tokens: 1209
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al identificar y explicar los errores en los cálculos del recibo.

## Respuesta completa



{
  "items": [
    {"nombre": "Lomo vetado", "precio": 18900},
    {"nombre": "Ensalada cesar", "precio": 7500},
    {"nombre": "Pisco sour", "precio": 6900},
    {"nombre": "Postre brownie", "precio": 5800},
    {"nombre": "Agua mineral 1.5L", "precio": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal calculado ($75.000) no coincide con el subtotal facturado ($73.000).",
    "La propina fue calculada en base al subtotal incorrecto (10% de $73.000 = $7.300), pero debería ser 10% de $75.000 ($7.500).",
    "El total correcto debería ser $82.500 ($75.000 + $7.500), pero se facturó $80.300."
  ]
}
