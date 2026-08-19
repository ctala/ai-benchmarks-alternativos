# Kimi K3 — ocr_extraction/receipt_math_verification

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 8.08 | quality: 10.0
- latency_total: 44.392s | tokens_per_second: 38.1
- input_tokens: 412 | output_tokens: 1692
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al identificar errores y sugerir correcciones, lo que la hace altamente valiosa para un emprendedor.

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
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma real de los items ($75.000). Diferencia: $2.000 a favor del restaurante.",
    "La propina ($7.300) es aritmeticamente correcta como 10% del subtotal facturado, pero sobre el subtotal real ($75.000) deberia ser $7.500.",
    "El total real deberia ser $82.500 ($75.000 + $7.500), no $80.300."
  ]
}
```

**Resumen de la verificación:**

| Concepto | Facturado | Calculado | ¿Correcto? |
|---|---|---|---|
| Subtotal | $73.000 | $75.000 | ❌ (faltan $2.000) |
| Propina (10%) | $7.300 | $7.300* | ⚠️ Correcta sobre el subtotal facturado, pero debería ser $7.500 sobre el real |
| Total | $80.300 | $82.500 | ❌ |

**Detalle del error:** La suma de los items es $37.800 + $7.500 + $20.700 + $5.800 + $3.200 = **$75.000**, pero el recibo indica $73.000. Curiosamente, el total facturado ($80.300) es *menor* de lo que debería cobrarse ($82.500), por lo que en este caso el error favorece al cliente. Conviene avisar al mesero para que corrijan la boleta.