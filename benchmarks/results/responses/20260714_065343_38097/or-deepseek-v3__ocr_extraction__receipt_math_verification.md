# DeepSeek V3 — ocr_extraction/receipt_math_verification

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 16.262s | tokens_per_second: 18.4
- input_tokens: 271 | output_tokens: 300
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una buena exactitud de datos y utilidad práctica, aunque la profundidad podría mejorarse con más análisis.

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
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Diferencia: $2.000",
    "La propina se calculó correctamente sobre el subtotal facturado (10% de $73.000 = $7.300)",
    "El total debería ser $80.300 según el recibo, pero si se corrige el subtotal, el total con propina sería $82.500"
  ]
}
```