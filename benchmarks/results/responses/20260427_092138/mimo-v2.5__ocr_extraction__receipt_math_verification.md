# MiMo V2.5 (Xiaomi) — ocr_extraction/receipt_math_verification

- model_id: `mimo-v2.5`
- success: True  | final: 7.32 | quality: 7.48
- latency_total: 12.289s | tokens_per_second: 111.5
- input_tokens: 593 | output_tokens: 1370
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "producto": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "subtotal_item": 37800
    },
    {
      "producto": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "subtotal_item": 7500
    },
    {
      "producto": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "subtotal_item": 20700
    },
    {
      "producto": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "subtotal_item": 5800
    },
    {
      "producto": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "subtotal_item": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal está incorrecto: se facturó $73.000 pero la suma real de los items es $75.000 (diferencia de -$2.000 a favor del cliente)",
    "El total facturado ($80.300) es consistente con los valores del recibo, pero debería ser $82.500 si el subtotal fuera correcto",
    "La propina del 10% está bien calculada sobre el subtotal facturado ($73.000 × 10% = $7.300)"
  ]
}
```

### 📋 Resumen del análisis

| Concepto | Recibo | Calculado |
|----------|--------|-----------|
| Subtotal | $73.000 | **$75.000** |
| Propina (10%) | $7.300 | $7.500 |
| Total | $80.300 | **$82.500** |

### 🔍 Hallazgo importante

**El recibo tiene un error a tu favor** 🎉

La suma de los items da **$75.000**, pero el restaurante cobró **$73.000**, lo que significa que te están cobrando **$2.000 menos** de lo que corresponde. 

La propina del 10% está correctamente calculada sobre el subtotal facturado ($73.000 × 10% = $7.300), y el total ($80.300) es la suma correcta de subtotal + propina según los valores impresos.

**Posible causa:** Puede ser un descuento aplicado que no se muestra explícitamente, o simplemente un error de cálculo del sistema.