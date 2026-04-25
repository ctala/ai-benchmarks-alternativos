# Gemma 4 26B MoE (3.8B activos) — ocr_extraction/receipt_math_verification

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 6.81 | quality: 7.04
- latency_total: 5.506s | tokens_per_second: 66.8
- input_tokens: 319 | output_tokens: 368
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "producto": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "subtotal": 37800
    },
    {
      "producto": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "subtotal": 7500
    },
    {
      "producto": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "subtotal": 20700
    },
    {
      "producto": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "subtotal": 5800
    },
    {
      "producto": "Agua mineral 1.5L",
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
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000).",
    "La propina sugerida (10%) está calculada sobre el subtotal erróneo ($7.300 de $73.000) en lugar del subtotal real de los productos ($7.500 de $75.000).",
    "El total final ($80.300) es incorrecto debido a los errores previos en el subtotal y la propina."
  ]
}
```