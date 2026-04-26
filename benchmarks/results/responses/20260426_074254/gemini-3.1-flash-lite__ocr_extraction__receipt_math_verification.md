# Gemini 3.1 Flash Lite — ocr_extraction/receipt_math_verification

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 7.31 | quality: 7.04
- latency_total: 2.4s | tokens_per_second: 197.9
- input_tokens: 365 | output_tokens: 475
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "producto": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total": 37800
    },
    {
      "producto": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total": 7500
    },
    {
      "producto": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total": 20700
    },
    {
      "producto": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total": 5800
    },
    {
      "producto": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) es incorrecto. La suma real de los items es $75.000.",
    "La propina sugerida ($7.300) es el 10% del subtotal facturado incorrecto, pero representa el 9.73% del subtotal real.",
    "El total facturado ($80.300) es incorrecto. Basado en el cálculo real (Subtotal $75.000 + Propina $7.500), el total debería ser $82.500."
  ]
}
```