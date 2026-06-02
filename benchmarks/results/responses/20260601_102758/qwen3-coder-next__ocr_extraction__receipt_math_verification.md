# Qwen3-Coder-Next (OpenRouter FP8) — ocr_extraction/receipt_math_verification

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 6.68 | quality: 7.09
- latency_total: 8.248s | tokens_per_second: 49.1
- input_tokens: 354 | output_tokens: 405
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "descripcion": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
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
    "El subtotal calculado ($75.000) no coincide con el subtotal facturado ($73.000)",
    "La propina sugerida se calculó sobre $73.000 en lugar de $75.000 (debería ser $7.500, no $7.300)",
    "El total facturado ($80.300) no coincide con el total esperado ($82.500)"
  ]
}
```