# MiMo-V2.5 (omnimodal) — ocr_extraction/receipt_math_verification

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 7.07 | quality: 7.48
- latency_total: 8.588s | tokens_per_second: 140.3
- input_tokens: 593 | output_tokens: 1205
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "descripcion": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total_item": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total_item": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total_item": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total_item": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total_item": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal está incorrecto: se facturó $73.000 pero la suma real es $75.000 (diferencia de $2.000 a favor del restaurante)",
    "El total también es incorrecto: debería ser $82.500 ($75.000 + $7.500 de propina), no $80.300",
    "La propina del 10% sobre el subtotal real sería $7.500, no $7.300"
  ]
}
```

---

### 📋 Resumen del análisis:

| Concepto | Valor en boleta | Valor real |
|----------|-----------------|------------|
| Subtotal | $73.000 | **$75.000** |
| Propina (10%) | $7.300 | **$7.500** |
| **Total** | $80.300 | **$82.500** |

⚠️ **Hay un error de $2.000 en el subtotal**, lo que afecta tanto la propina como el total. Es posible que se haya omitido un item o que algún precio esté mal registrado en el sistema. Te recomiendo verificar con el mesero o revisar la boleta fiscal si la tienes.