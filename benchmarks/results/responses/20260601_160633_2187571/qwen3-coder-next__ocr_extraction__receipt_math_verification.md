# Qwen3-Coder-Next (OpenRouter FP8) — ocr_extraction/receipt_math_verification

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.64 | quality: 8.15
- latency_total: 4.024s | tokens_per_second: 109.8
- input_tokens: 354 | output_tokens: 442
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al identificar errores en el cálculo del recibo, lo que la hace altamente valiosa para un emprendedor.

## Respuesta completa

```json
{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "subtotal": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "subtotal": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "subtotal": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "subtotal": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
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
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Diferencia: -$2.000.",
    "La propina sugerida ($7.300) se calculó sobre $73.000 (10%), pero debería basarse en el subtotal real de $75.000, lo que daría $7.500.",
    "El total facturado ($80.300) es incorrecto. Debería ser $75.000 + $7.500 = $82.500."
  ]
}
```