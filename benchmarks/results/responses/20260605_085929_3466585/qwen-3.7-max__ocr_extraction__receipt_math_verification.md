# Qwen 3.7 Max — ocr_extraction/receipt_math_verification

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 6.32 | quality: 7.48
- latency_total: 22.981s | tokens_per_second: 68.7
- input_tokens: 367 | output_tokens: 1578
- judge_score: 4.4 | justificación: 

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
    "El subtotal facturado ($73.000) no coincide con la suma real de los items ($75.000). Hay una diferencia de $2.000 menos en la boleta.",
    "La propina indicada ($7.300) es el 10% del subtotal incorrecto. Sobre el subtotal real ($75.000), la propina debería ser $7.500.",
    "El total facturado ($80.300) es incorrecto. El total correcto debería ser $82.500 ($75.000 + $7.500).",
    "El cliente fue cobrado de menos por $2.200 en total."
  ]
}
```

### Resumen del análisis

| Concepto | Boleta | Correcto | Diferencia |
|---|---|---|---|
| **Subtotal** | $73.000 | $75.000 | -$2.000 |
| **Propina (10%)** | $7.300 | $7.500 | -$200 |
| **Total** | $80.300 | $82.500 | -$2.200 |

> ⚠️ **Conclusión:** Existe un error de **$2.000** en el subtotal que se arrastra a la propina y al total. Es probable que el mesero o el sistema omitiera un item o ingresara mal un precio. El restaurante dejó de percibir **$2.200** en esta boleta.