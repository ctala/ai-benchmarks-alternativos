# Kimi K2 — ocr_extraction/receipt_math_verification

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 7.97 | quality: 8.75
- latency_total: 18.308s | tokens_per_second: 31.7
- input_tokens: 336 | output_tokens: 580
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con cálculos correctos y detallados, proporcionando una utilidad práctica al identificar errores en el recibo.

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
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "Subtotal incorrecto: se facturó $73.000 pero la suma de items es $75.000 (diferencia de -$2.000)",
    "Propina incorrecta: se sugirió $7.300 (10% de $73.000) pero debería ser $7.500 (10% de $75.000)",
    "Total incorrecto: se muestra $80.300 pero debería ser $82.500 (subtotal $75.000 + propina $7.500)"
  ]
}
```

**Detalle de cálculos:**
| Item | Cálculo | Total |
|------|---------|-------|
| 2× Lomo vetado | 2 × $18.900 | $37.800 |
| 1× Ensalada cesar | 1 × $7.500 | $7.500 |
| 3× Pisco sour | 3 × $6.900 | $20.700 |
| 1× Postre brownie | 1 × $5.800 | $5.800 |
| 1× Agua mineral | 1 × $3.200 | $3.200 |
| **Suma real** | | **$75.000** |

El restaurante tiene un **error de $2.000 a favor del cliente** (subtotal menor al real).