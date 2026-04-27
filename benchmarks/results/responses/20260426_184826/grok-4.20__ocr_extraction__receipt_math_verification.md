# Grok 4.20 — ocr_extraction/receipt_math_verification

- model_id: `x-ai/grok-4.20`
- success: True  | final: 6.91 | quality: 7.04
- latency_total: 4.064s | tokens_per_second: 84.9
- input_tokens: 431 | output_tokens: 345
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "item": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "subtotal": 37800
    },
    {
      "item": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "subtotal": 7500
    },
    {
      "item": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "subtotal": 20700
    },
    {
      "item": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "subtotal": 5800
    },
    {
      "item": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "subtotal": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal está incorrecto. La suma real de los productos es $75.000, no $73.000.",
    "La propina sugerida (10%) debería ser $7.500 sobre el subtotal correcto de $75.000.",
    "El total debería ser $82.500 ($75.000 + $7.500)."
  ]
}
```