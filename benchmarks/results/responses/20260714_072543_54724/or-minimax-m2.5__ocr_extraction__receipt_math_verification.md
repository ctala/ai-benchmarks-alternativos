# MiniMax M2.5 — ocr_extraction/receipt_math_verification

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 8.12 | quality: 8.75
- latency_total: 9.102s | tokens_per_second: 92.8
- input_tokens: 353 | output_tokens: 845
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al identificar errores en los cálculos del recibo.

## Respuesta completa

```json
{
  "items": [
    {"nombre": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900, "subtotal": 37800},
    {"nombre": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500, "subtotal": 7500},
    {"nombre": "Pisco sour", "cantidad": 3, "precio_unitario": 6900, "subtotal": 20700},
    {"nombre": "Postre brownie", "cantidad": 1, "precio_unitario": 5800, "subtotal": 5800},
    {"nombre": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200, "subtotal": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Hay una diferencia de $2.000.",
    "La propina calculada es sobre el subtotal incorrecto. Debería ser $7.500 (10% de $75.000), pero figura $7.300.",
    "El total debería ser $82.500 ($75.000 + $7.500), pero figura $80.300."
  ]
}
```