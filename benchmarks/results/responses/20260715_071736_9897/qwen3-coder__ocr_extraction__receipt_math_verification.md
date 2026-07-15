# Qwen3 Coder — ocr_extraction/receipt_math_verification

- model_id: `qwen/qwen3-coder`
- success: True  | final: 7.77 | quality: 7.5
- latency_total: 2.681s | tokens_per_second: 111.5
- input_tokens: 354 | output_tokens: 299
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con datos exactos y útil para un emprendedor, aunque la profundidad es básica.

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
  "subtotal_calculado": 73000,
  "subtotal_correcto": true,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": []
}
```