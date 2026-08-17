# GLM 5 (NIM) — ocr_extraction/receipt_math_verification

- model_id: `z-ai/glm5`
- success: True  | final: 6.56 | quality: 7.32
- latency_total: 70.768s | tokens_per_second: 5.8
- input_tokens: 290 | output_tokens: 410
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "descripcion": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "precio_total": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "precio_total": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "precio_total": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "precio_total": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
      "cantidad": 1,
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
    "El subtotal facturado es de $73.000, pero la suma real de los items es $75.000. Existe una diferencia de $2.000 a favor del cliente.",
    "La propina del 10% ($7.300) está bien calculada en base al subtotal facturado ($73.000), pero si se calcula sobre el subtotal real debería ser $7.500.",
    "El total facturado ($80.300) es incorrecto respecto a los items consumidos. El total real debería ser $82.500 ($75.000 subtotal + $7.500 propina)."
  ]
}
```