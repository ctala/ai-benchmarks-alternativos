# Solar Pro 4 — ocr_extraction/receipt_math_verification

- model_id: `upstage/solar-pro4`
- success: True  | final: 8.38 | quality: 8.75
- latency_total: 6.883s | tokens_per_second: 56.9
- input_tokens: 409 | output_tokens: 392

## Respuesta completa

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
    "El subtotal facturado es $73.000, pero la suma real de los items es $75.000 (diferencia de $2.000)",
    "La propina sugerida del 10% debería ser $7.500 sobre el subtotal real, no $7.300",
    "El total correcto debería ser $82.500 (75.000 + 7.500), no $80.300"
  ]
}