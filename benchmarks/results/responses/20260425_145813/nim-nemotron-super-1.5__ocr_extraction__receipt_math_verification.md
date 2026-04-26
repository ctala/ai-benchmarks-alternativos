# Nemotron Super 49B v1.5 (NIM) — ocr_extraction/receipt_math_verification

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 6.56 | quality: 7.04
- latency_total: 50.476s | tokens_per_second: 27.7
- input_tokens: 299 | output_tokens: 1396
- judge_score: 4.2 | justificación: 

## Respuesta completa

{
  "items": [
    {"nombre": "Lomo vetado", "precio": 18900},
    {"nombre": "Ensalada cesar", "precio": 7500},
    {"nombre": "Pisco sour", "precio": 6900},
    {"nombre": "Postre brownie", "precio": 5800},
    {"nombre": "Agua mineral 1.5L", "precio": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": ["El subtotal facturado ($73.000) es incorrecto. La suma correcta de los items es $75.000."]
}