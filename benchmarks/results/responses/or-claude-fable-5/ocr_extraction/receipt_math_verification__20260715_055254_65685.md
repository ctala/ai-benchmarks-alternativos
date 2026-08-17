# Claude Fable 5 — ocr_extraction/receipt_math_verification

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.21 | quality: 8.75
- latency_total: 13.29s | tokens_per_second: 77.0
- input_tokens: 462 | output_tokens: 1024
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una buena profundidad al identificar errores en el recibo y explicar sus implicaciones, lo que la hace altamente útil para un emprendedor.

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
    "La propina sugerida ($7.300) fue calculada sobre el subtotal erroneo. El 10% del subtotal correcto ($75.000) seria $7.500.",
    "El total facturado ($80.300) es internamente consistente con el subtotal y propina erroneos (73.000 + 7.300 = 80.300), pero el total correcto deberia ser $82.500 (75.000 + 7.500)."
  ]
}
```

**Detalle de la verificación de la suma:**

| Item | Cálculo | Total |
|---|---|---|
| Lomo vetado | 2 × $18.900 | $37.800 |
| Ensalada césar | 1 × $7.500 | $7.500 |
| Pisco sour | 3 × $6.900 | $20.700 |
| Postre brownie | 1 × $5.800 | $5.800 |
| Agua mineral | 1 × $3.200 | $3.200 |
| **Suma real** | | **$75.000** |

El recibo tiene un error de **$2.000 de menos** en el subtotal, lo que arrastra el error a la propina y al total final.