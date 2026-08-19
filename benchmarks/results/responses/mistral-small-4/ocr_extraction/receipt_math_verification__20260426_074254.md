# Mistral Small 4 — ocr_extraction/receipt_math_verification

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 7.31 | quality: 7.04
- latency_total: 2.771s | tokens_per_second: 141.8
- input_tokens: 383 | output_tokens: 393
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {"nombre": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900, "precio_total": 37800},
    {"nombre": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500, "precio_total": 7500},
    {"nombre": "Pisco sour", "cantidad": 3, "precio_unitario": 6900, "precio_total": 20700},
    {"nombre": "Postre brownie", "cantidad": 1, "precio_unitario": 5800, "precio_total": 5800},
    {"nombre": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200, "precio_total": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000).",
    "La propina sugerida (10%) debería ser $7.500 (10% de $75.000), pero está facturada como $7.300.",
    "El total ($80.300) es incorrecto porque se basa en un subtotal y propina erróneos."
  ]
}
```