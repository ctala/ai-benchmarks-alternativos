# Claude Opus 4.6 — ocr_extraction/receipt_math_verification

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 6.99 | quality: 7.68
- latency_total: 11.735s | tokens_per_second: 71.5
- input_tokens: 376 | output_tokens: 839
- judge_score: 4.6 | justificación: 

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
  "propina_facturada": 7300,
  "propina_calculada_sobre_subtotal_facturado": 7300,
  "propina_calculada_sobre_subtotal_real": 7500,
  "propina_correcta": false,
  "total_facturado": 80300,
  "total_calculado": 82500,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma real de los ítems ($75.000). Hay una diferencia de -$2.000.",
    "Desglose correcto: (2 × $18.900 = $37.800) + (1 × $7.500) + (3 × $6.900 = $20.700) + (1 × $5.800) + (1 × $3.200) = $75.000.",
    "La propina sugerida del 10% fue calculada sobre el subtotal erróneo ($73.000 × 10% = $7.300). Sobre el subtotal correcto debería ser $75.000 × 10% = $7.500.",
    "El total correcto debería ser $75.000 + $7.500 = $82.500, no $80.300. Diferencia total: -$2.200."
  ]
}
```

**Resumen del análisis:**

| Concepto | Facturado | Correcto | Diferencia |
|---|---|---|---|
| Subtotal | $73.000 | $75.000 | **-$2.000** |
| Propina (10%) | $7.300 | $7.500 | -$200 |
| **Total** | **$80.300** | **$82.500** | **-$2.200** |

El error raíz está en el **subtotal**: la suma real de los 5 ítems da **$75.000**, no $73.000. Esto arrastra el error a la propina y al total. En la práctica, el restaurante cobró **$2.200 menos** de lo que correspondía. 🧾