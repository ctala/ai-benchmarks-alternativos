# Muse Glimmer 30B — ocr_extraction/receipt_math_verification

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 13.005s | tokens_per_second: 193.7
- input_tokens: 365 | output_tokens: 2519
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una buena profundidad y utilidad práctica, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total_item": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total_item": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total_item": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total_item": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total_item": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "Subtotal facturado $73.000 no coincide con la suma de los items. Suma real = $75.000, diferencia de -$2.000.",
    "El TOTAL facturado $80.300 está coherente con subtotal facturado + propina $7.300, pero está basado en un subtotal incorrecto. Con los items correctos el subtotal sería $75.000, propina 10% $7.500 y total esperado $82.500."
  ]
}
```