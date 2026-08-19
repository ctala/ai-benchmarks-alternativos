# Kimi K2.6 — ocr_extraction/receipt_math_verification

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 6.06 | quality: 7.04
- latency_total: 144.313s | tokens_per_second: 31.5
- input_tokens: 334 | output_tokens: 4542
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
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los ítems ($75.000). Existe una diferencia de $2.000 a favor del local.",
    "La propina sugerida debería ser $7.500 (10% del subtotal real de $75.000), no $7.300.",
    "El total correcto debería ser $82.500, no $80.300."
  ]
}
```