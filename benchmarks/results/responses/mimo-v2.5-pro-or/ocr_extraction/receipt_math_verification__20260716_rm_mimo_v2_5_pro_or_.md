# MiMo-V2.5 Pro — ocr_extraction/receipt_math_verification

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 8.57 | quality: 10.0
- latency_total: 27.339s | tokens_per_second: 51.0
- input_tokens: 597 | output_tokens: 1395
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con datos exactos y útil para un emprendedor, aunque carece de profundidad más allá de la verificación básica.

## Respuesta completa

{
  "items": [
    {"descripcion": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900, "precio_total": 37800},
    {"descripcion": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500, "precio_total": 7500},
    {"descripcion": "Pisco sour", "cantidad": 3, "precio_unitario": 6900, "precio_total": 20700},
    {"descripcion": "Postre brownie", "cantidad": 1, "precio_unitario": 5800, "precio_total": 5800},
    {"descripcion": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200, "precio_total": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": [
    "El subtotal facturado (73000) no coincide con la suma de los ítems (75000). Diferencia: 2000."
  ]
}