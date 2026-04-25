# Mistral Nemo — ocr_extraction/receipt_math_verification

- model_id: `mistralai/mistral-nemo`
- success: True  | final: 6.93 | quality: 7.09
- latency_total: 8.256s | tokens_per_second: 25.9
- input_tokens: 373 | output_tokens: 214
- judge_score: 4.4 | justificación: 

## Respuesta completa

{
  "items": [
    {"nombre": "Lomo vetado", "cantidad": 2, "precio": 18900},
    {"nombre": "Ensalada cesar", "cantidad": 1, "precio": 7500},
    {"nombre": "Pisco sour", "cantidad": 3, "precio": 6900},
    {"nombre": "Postre brownie", "cantidad": 1, "precio": 5800},
    {"nombre": "Agua mineral 1.5L", "cantidad": 1, "precio": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 73000,
  "subtotal_correcto": true,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": []
}