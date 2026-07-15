# Claude Fable 5 — ocr_extraction/receipt_math_verification

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.22 | quality: 8.75
- latency_total: 13.972s | tokens_per_second: 72.1
- input_tokens: 462 | output_tokens: 1008
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una buena profundidad al identificar errores y su impacto, y es útil para un emprendedor al destacar discrepancias financieras.

## Respuesta completa

```json
{
  "items": [
    {
      "cantidad": 2,
      "descripcion": "Lomo vetado",
      "precio_unitario": 18900,
      "precio_total": 37800
    },
    {
      "cantidad": 1,
      "descripcion": "Ensalada cesar",
      "precio_unitario": 7500,
      "precio_total": 7500
    },
    {
      "cantidad": 3,
      "descripcion": "Pisco sour",
      "precio_unitario": 6900,
      "precio_total": 20700
    },
    {
      "cantidad": 1,
      "descripcion": "Postre brownie",
      "precio_unitario": 5800,
      "precio_total": 5800
    },
    {
      "cantidad": 1,
      "descripcion": "Agua mineral 1.5L",
      "precio_unitario": 3200,
      "precio_total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma real de los items ($75.000). Hay una diferencia de $2.000 a favor del cliente.",
    "La propina de $7.300 es el 10% del subtotal facturado ($73.000), pero como ese subtotal es incorrecto, la propina correcta seria $7.500 (10% de $75.000).",
    "El total de $80.300 es internamente consistente con el subtotal facturado ($73.000 + $7.300), pero el total correcto seria $82.500 ($75.000 + $7.500)."
  ]
}
```

**Resumen de la verificación:**

- **Suma de items:** $37.800 + $7.500 + $20.700 + $5.800 + $3.200 = **$75.000**
- El recibo tiene un **error de $2.000 en el subtotal** (cobró de menos)
- La propina y el total son matemáticamente consistentes con el subtotal erróneo, pero heredan el error original
- El cliente pagó **$2.200 menos** de lo que correspondía ($82.500 vs $80.300)