# GLM-5.1 — ocr_extraction/receipt_math_verification

- model_id: `z-ai/glm-5.1`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 20.659s | tokens_per_second: 95.7
- input_tokens: 318 | output_tokens: 1976
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una buena profundidad al identificar errores en el recibo y ofrecer cálculos correctos, lo que la hace altamente útil para un emprendedor.

## Respuesta completa

```json
{
  "items": [
    {
      "producto": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "precio_total": 37800
    },
    {
      "producto": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "precio_total": 7500
    },
    {
      "producto": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "precio_total": 20700
    },
    {
      "producto": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "precio_total": 5800
    },
    {
      "producto": "Agua mineral 1.5L",
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
    "El subtotal facturado es $73.000, pero la suma real de los items es $75.000 (hay una diferencia de $2.000 menos en el recibo).",
    "Aunque la propina del 10% está bien calculada respecto al subtotal facturado ($73.000 + 10% = $7.300), el total final es incorrecto porque el subtotal de origen está mal.",
    "El total a pagar real debería ser $82.500 ($75.000 de items + $7.500 de propina sobre el valor real) o $82.300 si se mantiene la propina facturada sobre el subtotal real."
  ]
}
```