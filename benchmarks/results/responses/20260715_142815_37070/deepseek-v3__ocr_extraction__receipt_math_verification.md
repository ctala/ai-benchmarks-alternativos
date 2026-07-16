# DeepSeek V3.2 — ocr_extraction/receipt_math_verification

- model_id: `deepseek/deepseek-chat`
- success: True  | final: 8.15 | quality: 8.75
- latency_total: 12.255s | tokens_per_second: 32.0
- input_tokens: 338 | output_tokens: 392
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una buena profundidad al identificar errores en los cálculos del recibo, lo que la hace muy útil para un emprendedor.

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
    "El subtotal calculado (75000) no coincide con el subtotal facturado (73000).",
    "La propina sugerida (7300) se calculó sobre un subtotal incorrecto. Debería ser 7500 (10% de 75000).",
    "El TOTAL facturado (80300) es incorrecto. Debería ser 82500 (75000 subtotal + 7500 propina)."
  ]
}
```