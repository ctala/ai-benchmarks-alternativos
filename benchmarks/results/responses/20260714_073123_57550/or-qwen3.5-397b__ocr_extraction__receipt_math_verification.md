# Qwen 3.5 397B — ocr_extraction/receipt_math_verification

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 7.44 | quality: 8.75
- latency_total: 111.452s | tokens_per_second: 64.5
- input_tokens: 367 | output_tokens: 7186
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al identificar errores en los cálculos del recibo, lo que la hace altamente valiosa para un emprendedor.

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
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) es incorrecto. La suma real de los items es $75.000.",
    "La propina sugerida ($7.300) no corresponde al 10% del valor real de los items ($7.500).",
    "El total facturado ($80.300) es incorrecto debido al error en el subtotal y la propina. El total real debería ser $82.500."
  ]
}