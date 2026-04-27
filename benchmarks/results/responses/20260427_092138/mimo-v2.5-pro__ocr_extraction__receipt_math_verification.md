# MiMo V2.5-Pro (Xiaomi) — ocr_extraction/receipt_math_verification

- model_id: `mimo-v2.5-pro`
- success: True  | final: 7.31 | quality: 7.76
- latency_total: 25.246s | tokens_per_second: 68.3
- input_tokens: 597 | output_tokens: 1724
- judge_score: 4.6 | justificación: 

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
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    {
      "campo": "subtotal",
      "detalle": "El subtotal facturado es $73.000, pero la suma correcta de los items da $75.000. Hay una diferencia de $2.000 a favor del cliente."
    },
    {
      "campo": "propina",
      "detalle": "La propina se calculó sobre el subtotal incorrecto ($73.000 × 10% = $7.300). Sobre el subtotal correcto debería ser $7.500 ($75.000 × 10%)."
    },
    {
      "campo": "total",
      "detalle": "El total facturado es $80.300, pero el total correcto sería $82.500 ($75.000 + $7.500 propina). Diferencia: $2.200."
    }
  ]
}
```



## 📋 Resumen del análisis

| Concepto | Recibo | Correcto | ¿Coincide? |
|----------|--------|----------|:-----------:|
| **Subtotal** | $73.000 | $75.000 | ❌ |
| **Propina (10%)** | $7.300 | $7.500 | ❌ |
| **Total** | $80.300 | $82.500 | ❌ |

### 🔍 Detalle de la suma correcta

```
  2 × $18.900  =  $37.800   (Lomo vetado)
  1 × $ 7.500  =  $ 7.500   (Ensalada)
  3 × $ 6.900  =  $20.700   (Pisco sour)
  1 × $ 5.800  =  $ 5.800   (Brownie)
  1 × $ 3.200  =  $ 3.200   (Agua)
  ─────────────────────────
  TOTAL        =  $75.000
```

### ⚠️ Error encontrado

El **subtotal del recibo está $2.000 menor** de lo que debería ser. Esto arrastra un error en la propina y el total. Es posible que se haya olvidado un item, o que haya sido un error de tipeo al momento de generar la boleta.