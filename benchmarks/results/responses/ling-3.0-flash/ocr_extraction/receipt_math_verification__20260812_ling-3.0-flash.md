# Ling 3.0 Flash — ocr_extraction/receipt_math_verification

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 8.3 | quality: 8.75
- latency_total: 12.939s | tokens_per_second: 95.5
- input_tokens: 405 | output_tokens: 1235
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al identificar errores en los cálculos del recibo.

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
    "El subtotal facturado es $73.000, pero la suma de los items da $75.000. Hay una diferencia de $2.000.",
    "La propina sugirida del 10% ($7.300) está calculada sobre el subtotal incorrecto de $73.000. El 10% correcto sobre $75.000 sería $7.500.",
    "El total facturado ($80.300) es incorrecto. El total correcto debería ser $75.000 + $7.500 = $82.500."
  ]
}prints
```