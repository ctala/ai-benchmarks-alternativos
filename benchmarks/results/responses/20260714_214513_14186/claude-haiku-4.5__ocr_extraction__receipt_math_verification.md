# Claude Haiku 4.5 — ocr_extraction/receipt_math_verification

- model_id: `anthropic/claude-haiku-4.5`
- success: True  | final: 8.14 | quality: 8.75
- latency_total: 3.469s | tokens_per_second: 167.2
- input_tokens: 376 | output_tokens: 580
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al identificar errores en el cálculo del recibo, lo que la hace altamente valiosa para un emprendedor.

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
  "propina_sugerida_facturada": 7300,
  "propina_calculada_correcta": 7500,
  "propina_correcta": false,
  "total_facturado": 80300,
  "total_correcto_deberia_ser": 82500,
  "total_correcto": false,
  "errores": [
    "El subtotal es INCORRECTO: Se facturó $73.000 pero debería ser $75.000 (diferencia: -$2.000)",
    "La propina está MAL CALCULADA: Se calculó sobre $73.000 (10% = $7.300) cuando debería ser sobre $75.000 (10% = $7.500)",
    "El TOTAL es INCORRECTO: Se facturó $80.300 pero debería ser $82.500 (diferencia: -$2.200)"
  ]
}
```

**Resumen:** Hay un error de **$2.000 en el subtotal**. Los items suman $75.000, no $73.000. Esto afecta en cascada la propina y el total final.