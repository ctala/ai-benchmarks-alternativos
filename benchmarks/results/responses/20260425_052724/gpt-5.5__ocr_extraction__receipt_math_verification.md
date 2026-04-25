# GPT-5.5 — ocr_extraction/receipt_math_verification

- model_id: `gpt-5.5`
- success: True  | final: 6.26 | quality: 7.32
- latency_total: 11.232s | tokens_per_second: 81.1
- input_tokens: 314 | output_tokens: 911
- judge_score: 4.4 | justificación: 

## Respuesta completa

{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": [
    "El subtotal facturado es $73.000, pero la suma de los items da $75.000. Hay una diferencia de $2.000.",
    "La propina de $7.300 corresponde correctamente al 10% del subtotal facturado de $73.000, pero si se usara el subtotal calculado de $75.000, la propina debería ser $7.500.",
    "El total facturado de $80.300 coincide con subtotal facturado + propina facturada, pero usando el subtotal calculado y una propina del 10%, el total esperado sería $82.500."
  ]
}