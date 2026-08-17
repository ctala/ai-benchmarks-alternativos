# Claude Opus 4.8 (suscripción) — ocr_extraction/receipt_math_verification

- model_id: `claude-opus-4-8`
- success: True  | final: 6.14 | quality: 7.68
- latency_total: 23.831s | tokens_per_second: 68.6
- input_tokens: 2028 | output_tokens: 1635
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí está el análisis del recibo:

```json
{
  "items": [
    { "nombre": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900, "precio_total": 37800 },
    { "nombre": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500, "precio_total": 7500 },
    { "nombre": "Pisco sour", "cantidad": 3, "precio_unitario": 6900, "precio_total": 20700 },
    { "nombre": "Postre brownie", "cantidad": 1, "precio_unitario": 5800, "precio_total": 5800 },
    { "nombre": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200, "precio_total": 3200 }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) está mal: la suma real de los items es $75.000. Faltan $2.000 (la boleta subfacturó).",
    "La propina sugerida ($7.300) es el 10% del subtotal MAL facturado ($73.000). Sobre el subtotal correcto ($75.000), el 10% debería ser $7.500.",
    "El TOTAL ($80.300) es coherente con los números errados de la boleta (73.000 + 7.300), pero el total correcto debería ser $82.500 ($75.000 + $7.500 de propina).",
    "Diferencia total a favor del cliente: $2.200 ($2.000 de subtotal + $200 de propina)."
  ]
}
```

**Resumen rápido:**

| Concepto | Boleta | Correcto | Estado |
|---|---|---|---|
| Subtotal | $73.000 | $75.000 | ❌ −$2.000 |
| Propina (10%) | $7.300 | $7.500 | ❌ −$200 |
| Total | $80.300 | $82.500 | ❌ −$2.200 |

La aritmética interna de la boleta es consistente (73.000 + 7.300 = 80.300), pero **parte de un subtotal mal sumado**. El error está en el subtotal: deberían ser $75.000. El restaurante cobró $2.200 de menos.