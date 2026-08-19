# Devstral 2 123B (NIM) — ocr_extraction/receipt_math_verification

- model_id: `mistralai/devstral-2-123b-instruct-2512`
- success: True  | final: 6.56 | quality: 7.04
- latency_total: 17.336s | tokens_per_second: 26.9
- input_tokens: 371 | output_tokens: 467
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "precio_total": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "precio_total": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "precio_total": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "precio_total": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "precio_total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Hay una diferencia de $2.000",
    "La propina sugerida (10%) se calculó sobre el subtotal facturado ($7.300) en lugar del subtotal real ($7.500). Debería ser $7.500",
    "El total facturado ($80.300) es incorrecto. El total correcto debería ser $82.500 (subtotal $75.000 + propina $7.500)"
  ]
}
```