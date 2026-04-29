# Gemma 4 31B (NIM) — ocr_extraction/receipt_math_verification

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 6.76 | quality: 7.04
- latency_total: 44.305s | tokens_per_second: 9.8
- input_tokens: 337 | output_tokens: 434
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "descripcion": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "subtotal": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "subtotal": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "subtotal": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "subtotal": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
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
    "El subtotal facturado ($73.000) es incorrecto; la suma real de los items es $75.000.",
    "La propina sugerida ($7.300) está calculada sobre el subtotal errado y no sobre el real ($7.500).",
    "El total final es incorrecto debido al error en el subtotal."
  ]
}
```