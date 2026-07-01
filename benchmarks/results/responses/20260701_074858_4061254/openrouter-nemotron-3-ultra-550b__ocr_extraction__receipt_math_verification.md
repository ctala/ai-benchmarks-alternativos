# Nemotron 3 Ultra 550B — ocr_extraction/receipt_math_verification

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 4.78 | quality: 3.85
- latency_total: 3.327s | tokens_per_second: 285.9
- input_tokens: 384 | output_tokens: 951

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
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Diferencia: $2.000",
    "La propina sugerida (10%) se calculó sobre el subtotal incorrecto ($7.300). Debería ser $7.500 sobre el subtotal real",
    "El total facturado ($80.300) es incorrecto. El total correcto sería $82.500 (subtotal $75.000 + propina 10% $7.500)"
  ]
}