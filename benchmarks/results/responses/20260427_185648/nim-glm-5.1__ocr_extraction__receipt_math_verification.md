# GLM 5.1 (NIM) — ocr_extraction/receipt_math_verification

- model_id: `z-ai/glm-5.1`
- success: True  | final: 6.56 | quality: 7.32
- latency_total: 52.2s | tokens_per_second: 8.1
- input_tokens: 290 | output_tokens: 423
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "cantidad": 2,
      "descripcion": "Lomo vetado",
      "precio_unitario": 18900,
      "precio_total": 37800
    },
    {
      "cantidad": 1,
      "descripcion": "Ensalada cesar",
      "precio_unitario": 7500,
      "precio_total": 7500
    },
    {
      "cantidad": 3,
      "descripcion": "Pisco sour",
      "precio_unitario": 6900,
      "precio_total": 20700
    },
    {
      "cantidad": 1,
      "descripcion": "Postre brownie",
      "precio_unitario": 5800,
      "precio_total": 5800
    },
    {
      "cantidad": 1,
      "descripcion": "Agua mineral 1.5L",
      "precio_unitario": 3200,
      "precio_total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado es incorrecto. La suma de los items da $75.000, pero el recibo indica $73.000 (hay una diferencia de $2.000 a favor del restaurante).",
    "El total final es incorrecto. Basado en el subtotal real de $75.000, el total debería ser $82.300 ($75.000 + $7.300), pero el recibo indica $80.300.",
    "La propina del 10% está bien calculada en función del subtotal facturado ($73.000), pero si se corrige el subtotal a $75.000, la propina sugerida debería ser $7.500."
  ]
}
```