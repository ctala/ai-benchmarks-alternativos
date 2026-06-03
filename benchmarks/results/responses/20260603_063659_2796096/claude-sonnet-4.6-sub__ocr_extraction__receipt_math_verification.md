# Claude Sonnet 4.6 (suscripción) — ocr_extraction/receipt_math_verification

- model_id: `claude-sonnet-4-6`
- success: True  | final: 6.64 | quality: 8.32
- latency_total: 24.742s | tokens_per_second: 69.3
- input_tokens: 3 | output_tokens: 1715
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una buena profundidad al identificar errores encadenados y su impacto, y es útil para un emprendedor al señalar problemas en el proceso de facturación.

## Respuesta completa

```json
{
  "items": [
    { "descripcion": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900, "precio_total": 37800 },
    { "descripcion": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500, "precio_total": 7500 },
    { "descripcion": "Pisco sour", "cantidad": 3, "precio_unitario": 6900, "precio_total": 20700 },
    { "descripcion": "Postre brownie", "cantidad": 1, "precio_unitario": 5800, "precio_total": 5800 },
    { "descripcion": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200, "precio_total": 3200 }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_facturada": 7300,
  "propina_correcta_sobre_subtotal_real": 7500,
  "propina_correcta": false,
  "total_facturado": 80300,
  "total_correcto_esperado": 82500,
  "total_correcto": false,
  "errores": [
    {
      "tipo": "ERROR_SUBTOTAL",
      "descripcion": "El subtotal facturado ($73.000) no coincide con la suma real de los items ($75.000). Diferencia de $2.000 a favor del restaurante.",
      "detalle": "37800 + 7500 + 20700 + 5800 + 3200 = 75000, no 73000"
    },
    {
      "tipo": "ERROR_PROPINA",
      "descripcion": "La propina ($7.300) se calculó sobre el subtotal incorrecto ($73.000). Sobre el subtotal real ($75.000) debería ser $7.500.",
      "diferencia": 200
    },
    {
      "tipo": "ERROR_TOTAL",
      "descripcion": "El total correcto debería ser $82.500 (subtotal $75.000 + propina $7.500). Se facturaron $80.300, un cobro de menos de $2.200.",
      "total_facturado": 80300,
      "total_correcto": 82500,
      "diferencia": 2200
    }
  ],
  "resumen": "⚠️ El subtotal está $2.000 por debajo del valor real. Paradójicamente, el cliente está pagando MENOS de lo que debería. Se recomienda revisar con el mesero Carlos."
}
```

---

### 🧮 Verificación paso a paso

| Item | Cálculo | Total |
|---|---|---|
| 2× Lomo vetado | 2 × $18.900 | $37.800 |
| 1× Ensalada césar | 1 × $7.500 | $7.500 |
| 3× Pisco sour | 3 × $6.900 | $20.700 |
| 1× Postre brownie | 1 × $5.800 | $5.800 |
| 1× Agua mineral | 1 × $3.200 | $3.200 |
| **SUBTOTAL REAL** | | **$75.000** |
| Propina 10% real | 10% × $75.000 | **$7.500** |
| **TOTAL CORRECTO** | | **$82.500** |

**Hay 3 errores encadenados**: el subtotal está $2.000 menos de lo real, lo que arrastra un error en la propina ($200 menos) y en el total ($2.200 menos). Curiosamente, en este caso **el error perjudica al restaurante**, no al cliente.