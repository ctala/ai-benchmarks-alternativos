# Nemotron 3 Nano 30B — ocr_extraction/receipt_math_verification

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 7.06 | quality: 7.04
- latency_total: 27.21s | tokens_per_second: 92.0
- input_tokens: 384 | output_tokens: 2504
- judge_score: 4.2 | justificación: 

## Respuesta completa

{
  "items": [
    {
      "name": "Lomo vetado",
      "quantity": 2,
      "unit_price": 18900,
      "line_total": 37800
    },
    {
      "name": "Ensalada cesar",
      "quantity": 1,
      "unit_price": 7500,
      "line_total": 7500
    },
    {
      "name": "Pisco sour",
      "quantity": 3,
      "unit_price": 6900,
      "line_total": 20700
    },
    {
      "name": "Postre brownie",
      "quantity": 1,
      "unit_price": 5800,
      "line_total": 5800
    },
    {
      "name": "Agua mineral 1.5L",
      "quantity": 1,
      "unit_price": 3200,
      "line_total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73,000) no coincide con la suma de los ítems ($75,000).",
    "La propina sugerida de $7,300 corresponde al 10 % del subtotal facturado, pero el 10 % del subtotal correcto ($75,000) sería $7,500, por lo que la propina está mal calculada.",
    "El total facturado ($80,300) no coincide con el total que debería ser ($82,500) si se usa el subtotal correcto y una propina del 10 %."
  ]
}