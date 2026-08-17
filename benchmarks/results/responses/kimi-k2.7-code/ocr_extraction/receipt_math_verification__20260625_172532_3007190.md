# Kimi K2.7 Code — ocr_extraction/receipt_math_verification

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 6.32 | quality: 7.04
- latency_total: 15.633s | tokens_per_second: 81.2
- input_tokens: 335 | output_tokens: 1269
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {"nombre": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900, "total_linea": 37800},
    {"nombre": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500, "total_linea": 7500},
    {"nombre": "Pisco sour", "cantidad": 3, "precio_unitario": 6900, "total_linea": 20700},
    {"nombre": "Postre brownie", "cantidad": 1, "precio_unitario": 5800, "total_linea": 5800},
    {"nombre": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200, "total_linea": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los ítems ($75.000). Diferencia: $2.000.",
    "La propina del 10% debería ser $7.500 sobre el subtotal real de $75.000, no $7.300.",
    "El total facturado ($80.300) no coincide con el total calculado correctamente ($82.500)."
  ]
}
```