# Nemotron 3 Base 33B (DGX Spark Q4_K_M) — ocr_extraction/receipt_math_verification

- model_id: `nemotron3:33b-q4_K_M`
- success: True  | final: 6.46 | quality: 7.04
- latency_total: 32.94s | tokens_per_second: 65.1
- input_tokens: 392 | output_tokens: 2143
- judge_score: 4.2 | justificación: 

## Respuesta completa

{
  "items": [
    { "name": "Lomo vetado", "price": 18900 },
    { "name": "Ensalada cesar", "price": 7500 },
    { "name": "Pisco sour", "price": 6900 },
    { "name": "Postre brownie", "price": 5800 },
    { "name": "Agua mineral 1.5L", "price": 3200 }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": [
    "Subtotal facturado incorrecto (suma de ítems: 75 000 vs 73 000)."
  ]
}