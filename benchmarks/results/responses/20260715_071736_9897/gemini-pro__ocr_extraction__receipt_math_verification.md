# Gemini 2.5 Pro — ocr_extraction/receipt_math_verification

- model_id: `google/gemini-2.5-pro`
- success: True  | final: 8.36 | quality: 10.0
- latency_total: 27.352s | tokens_per_second: 108.6
- input_tokens: 364 | output_tokens: 2971
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con datos exactos y útil para un emprendedor, aunque la profundidad es solo aceptable ya que no ofrece insights adicionales más allá de la verificación básica.

## Respuesta completa

```json
{
  "items": [
    {
      "item": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "precio_total": 37800
    },
    {
      "item": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "precio_total": 7500
    },
    {
      "item": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "precio_total": 20700
    },
    {
      "item": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "precio_total": 5800
    },
    {
      "item": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "precio_total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": [
    "El subtotal facturado ($73.000) es incorrecto. La suma real de los productos consumidos es de $75.000."
  ]
}
```