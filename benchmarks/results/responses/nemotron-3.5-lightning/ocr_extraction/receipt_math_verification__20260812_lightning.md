# Nemotron 3.5 Lightning — ocr_extraction/receipt_math_verification

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 8.09 | quality: 8.75
- latency_total: 30.551s | tokens_per_second: 171.2
- input_tokens: 384 | output_tokens: 5231
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con un análisis detallado de los errores en los cálculos del recibo.

## Respuesta completa

{
  "items": [
    {"name": "Lomo vetado", "quantity": 2, "unit_price": 18900, "total_price": 37800},
    {"name": "Ensalada cesar", "quantity": 1, "unit_price": 7500, "total_price": 7500},
    {"name": "Pisco sour", "quantity": 3, "unit_price": 6900, "total_price": 20700},
    {"name": "Postre brownie", "quantity": 1, "unit_price": 5800, "total_price": 5800},
    {"name": "Agua mineral 1.5L", "quantity": 1, "unit_price": 3200, "total_price": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Diferencia: $2.000.",
    "La propina sugerida ($7.300) se calcula sobre el subtotal incorrecto; el 10% del subtotal correcto ($75.000) sería $7.500.",
    "El total facturado ($80.300) es consistente con los valores facturados, pero no refleja la suma real de items y propina ($82.500)."
  ]
}