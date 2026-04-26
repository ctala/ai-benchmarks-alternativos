# MiMo-V2.5 Pro — ocr_extraction/receipt_math_verification

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 7.01 | quality: 7.76
- latency_total: 14.613s | tokens_per_second: 76.7
- input_tokens: 597 | output_tokens: 1121
- judge_score: 4.6 | justificación: 

## Respuesta completa

```json
{
  "items": [
    { "descripcion": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900, "subtotal": 37800 },
    { "descripcion": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500, "subtotal": 7500 },
    { "descripcion": "Pisco sour", "cantidad": 3, "precio_unitario": 6900, "subtotal": 20700 },
    { "descripcion": "Postre brownie", "cantidad": 1, "precio_unitario": 5800, "subtotal": 5800 },
    { "descripcion": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200, "subtotal": 3200 }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) es incorrecto. La suma real de los items da $75.000 (diferencia de $2.000).",
    "La propina del 10% está bien calculada sobre el subtotal facturado ($7.300), pero debería ser $7.500 si se calcula sobre el subtotal correcto.",
    "El total facturado ($80.300) debería ser $82.500 (subtotal correcto $75.000 + propina correcta $7.500)."
  ]
}
```

---

### 📋 Resumen del análisis

| Concepto | Facturado | Correcto | Diferencia |
|---|---|---|---|
| **Subtotal** | $73.000 | $75.000 | **-$2.000** ❌ |
| **Propina (10%)** | $7.300 | $7.500 | -$200 |
| **Total** | $80.300 | $82.500 | **-$2.000** |

### ⚠️ Error principal

El subtotal facturado es **$2.000 menor** de lo que debería ser. Esto puede deberse a:
- Un descuento no especificado en el recibo
- Un error al ingresar algún item en el sistema
- Un error de caja

> **Recomendación:** Puedes preguntar al mesero Carlos o a caja si hubo algún descuento aplicado, ya que el recibo no lo indica y la diferencia es significativa.