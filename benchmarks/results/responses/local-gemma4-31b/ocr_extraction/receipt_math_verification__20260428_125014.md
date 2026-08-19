# Gemma 4 31B (DGX Spark Q4_K_M) — ocr_extraction/receipt_math_verification

- model_id: `gemma4:31b`
- success: True  | final: 6.46 | quality: 7.04
- latency_total: 138.876s | tokens_per_second: 10.9
- input_tokens: 384 | output_tokens: 1508
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
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73,000) es incorrecto. La suma real de los items es $75,000."
  ]
}
```