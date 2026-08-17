# Devstral Medium — ocr_extraction/receipt_math_verification

- model_id: `mistralai/devstral-medium`
- success: True  | final: 7.01 | quality: 7.04
- latency_total: 8.687s | tokens_per_second: 43.9
- input_tokens: 371 | output_tokens: 381
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {"nombre": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900, "total": 37800},
    {"nombre": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500, "total": 7500},
    {"nombre": "Pisco sour", "cantidad": 3, "precio_unitario": 6900, "total": 20700},
    {"nombre": "Postre brownie", "cantidad": 1, "precio_unitario": 5800, "total": 5800},
    {"nombre": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200, "total": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con el subtotal calculado ($75.000).",
    "La propina sugerida (10%) no coincide con el 10% del subtotal calculado ($7.500).",
    "El total facturado ($80.300) no coincide con la suma del subtotal calculado y la propina sugerida ($82.500)."
  ]
}
```