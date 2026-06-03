# Claude Haiku 4.5 (suscripción) — ocr_extraction/receipt_math_verification

- model_id: `claude-haiku-4-5`
- success: True  | final: 6.92 | quality: 7.68
- latency_total: 8.203s | tokens_per_second: 144.1
- input_tokens: 10 | output_tokens: 1182
- judge_score: 4.6 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "descripcion": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "subtotal": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "subtotal": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "subtotal": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "subtotal": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
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
    "Subtotal incorrecto: facturan $73.000 pero los items suman $75.000 (diferencia: -$2.000)",
    "Propina incorrecta: se calculó 10% sobre el subtotal equivocado. Debería ser $7.500 (10% de $75.000), no $7.300",
    "Total incorrecto: basado en el subtotal erróneo. Debería ser $82.500 ($75.000 + $7.500), no $80.300"
  ]
}
```

**Resumen del problema:**
- ❌ **Faltan $2.000 en el subtotal** (los items suman $75.000, no $73.000)
- ❌ **La propina está mal calculada** ($7.300 en lugar de $7.500)
- ❌ **El total es incorrecto** ($80.300 en lugar de $82.500)

**Recomendación:** Verificar con el restaurante si fue error en la facturación o si hay un descuento no indicado.