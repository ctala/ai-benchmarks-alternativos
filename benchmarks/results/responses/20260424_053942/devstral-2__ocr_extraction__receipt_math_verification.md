# Devstral 2 (Dic 2025) — ocr_extraction/receipt_math_verification

- model_id: `mistralai/devstral-2512`
- success: True  | final: 7.13 | quality: 6.81
- latency_total: 4.947s | tokens_per_second: 79.2
- input_tokens: 371 | output_tokens: 392
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total_item": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total_item": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total_item": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total_item": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total_item": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal calculado (75000) no coincide con el facturado (73000)",
    "La propina sugerida (10%) debería ser 7500, no 7300",
    "El total debería ser 82500, no 80300"
  ]
}
```