# Qwen 3-Next 80B Instruct (NIM) — ocr_extraction/receipt_math_verification

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 6.81 | quality: 7.32
- latency_total: 9.733s | tokens_per_second: 46.1
- input_tokens: 326 | output_tokens: 449
- judge_score: 4.4 | justificación: 

## Respuesta completa

{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total_item": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total_item": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total_item": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total_item": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total_item": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado es $73.000, pero la suma de los ítems es $75.000. Existe una discrepancia de $2.000.",
    "La propina sugerida (10%) se calculó sobre $73.000, pero debería calcularse sobre el subtotal real de $75.000, lo que daría $7.500 en lugar de $7.300.",
    "El total facturado es $80.300, pero el total correcto debería ser $82.500 ($75.000 + $7.500)."
  ]
}