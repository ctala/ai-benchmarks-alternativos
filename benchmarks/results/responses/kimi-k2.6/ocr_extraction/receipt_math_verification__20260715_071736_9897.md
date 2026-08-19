# Kimi K2.6 — ocr_extraction/receipt_math_verification

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 7.22 | quality: 8.75
- latency_total: 127.507s | tokens_per_second: 25.8
- input_tokens: 334 | output_tokens: 3295
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al identificar errores en los cálculos del recibo, lo que la hace altamente valiosa para un emprendedor.

## Respuesta completa

```json
{
  "items": [
    {"cantidad": 2, "item": "Lomo vetado", "precio_unitario": 18900, "total": 37800},
    {"cantidad": 1, "item": "Ensalada cesar", "precio_unitario": 7500, "total": 7500},
    {"cantidad": 3, "item": "Pisco sour", "precio_unitario": 6900, "total": 20700},
    {"cantidad": 1, "item": "Postre brownie", "precio_unitario": 5800, "total": 5800},
    {"cantidad": 1, "item": "Agua mineral 1.5L", "precio_unitario": 3200, "total": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los ítems ($75.000). Existe una diferencia de $2.000.",
    "La propina del 10% debería ser $7.500 sobre el subtotal real ($75.000), en lugar de $7.300.",
    "El total debería ser $82.500 (subtotal $75.000 + propina $7.500), no $80.300."
  ]
}
```