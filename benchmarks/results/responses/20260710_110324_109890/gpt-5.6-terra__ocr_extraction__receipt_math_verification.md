# GPT-5.6 Terra — ocr_extraction/receipt_math_verification

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 7.52 | quality: 8.15
- latency_total: 4.265s | tokens_per_second: 134.6
- input_tokens: 314 | output_tokens: 574
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al identificar errores en el recibo y proporcionar detalles específicos sobre las discrepancias.

## Respuesta completa

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
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    {
      "tipo": "subtotal",
      "detalle": "El subtotal facturado es $73.000, pero la suma de los items es $75.000.",
      "diferencia": 2000
    },
    {
      "tipo": "propina",
      "detalle": "La propina sugerida debería ser $7.500 (10% de $75.000), no $7.300.",
      "diferencia": 200
    },
    {
      "tipo": "total",
      "detalle": "El total correcto debería ser $82.500 ($75.000 + $7.500), no $80.300.",
      "diferencia": 2200
    }
  ]
}