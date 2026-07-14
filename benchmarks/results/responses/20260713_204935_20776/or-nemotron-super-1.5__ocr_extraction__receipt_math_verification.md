# Nemotron Super 49B v1.5 — ocr_extraction/receipt_math_verification

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 8.85 | quality: 10.0
- latency_total: 20.538s | tokens_per_second: 48.4
- input_tokens: 331 | output_tokens: 993
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al identificar errores en el cálculo del subtotal, lo que la hace muy útil para un emprendedor.

## Respuesta completa

```json
{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
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
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000).",
    "El total ($80.300) está basado en un subtotal incorrecto."
  ]
}
```