# Nemotron 3 Super — ocr_extraction/receipt_math_verification

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 9.85 | quality: 10.0
- latency_total: 0.574s | tokens_per_second: 519.4
- input_tokens: 319 | output_tokens: 298
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con datos exactos y útil para un emprendedor, aunque la profundidad es solo aceptable ya que no ofrece insights adicionales más allá de la verificación básica.

## Respuesta completa



{
  "items": [
    {
      "descripcion": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
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
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Diferencia de $2.000."
  ]
}