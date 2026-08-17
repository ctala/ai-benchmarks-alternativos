# Grok 4.3 — ocr_extraction/receipt_math_verification

- model_id: `x-ai/grok-4.3`
- success: True  | final: 4.57 | quality: 3.85
- latency_total: 9.79s | tokens_per_second: 106.4
- input_tokens: 439 | output_tokens: 1042

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
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma real de los ítems ($75.000). Hay un error de $2.000.",
    "La propina está calculada correctamente sobre el subtotal erróneo ($73.000).",
    "El total final ($80.300) es incorrecto porque se basa en un subtotal equivocado."
  ]
}