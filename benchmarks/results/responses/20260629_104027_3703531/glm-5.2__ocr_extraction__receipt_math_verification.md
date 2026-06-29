# GLM 5.2 — ocr_extraction/receipt_math_verification

- model_id: `z-ai/glm-5.2`
- success: True  | final: 6.44 | quality: 7.04
- latency_total: 29.944s | tokens_per_second: 68.3
- input_tokens: 325 | output_tokens: 2045
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
    "El subtotal facturado ($73.000) es menor que la suma real de los items ($75.000).",
    "La propina sugerida ($7.300) está calculada sobre el subtotal facturado erróneo. El 10% sobre el subtotal real debería ser $7.500.",
    "El total final indicado ($80.300) es incorrecto. Debería ser $82.500 ($75.000 subtotal + $7.500 propina)."
  ]
}
```