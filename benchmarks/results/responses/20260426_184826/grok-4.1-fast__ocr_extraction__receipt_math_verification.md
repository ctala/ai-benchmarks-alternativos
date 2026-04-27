# Grok 4.1 Fast — ocr_extraction/receipt_math_verification

- model_id: `x-ai/grok-4.1-fast`
- success: True  | final: 7.21 | quality: 7.04
- latency_total: 8.061s | tokens_per_second: 130.4
- input_tokens: 465 | output_tokens: 1051
- judge_score: 4.2 | justificación: 

## Respuesta completa

{
  "items": [
    {"cantidad": 2, "nombre": "Lomo vetado", "precio_unitario": 18900},
    {"cantidad": 1, "nombre": "Ensalada cesar", "precio_unitario": 7500},
    {"cantidad": 3, "nombre": "Pisco sour", "precio_unitario": 6900},
    {"cantidad": 1, "nombre": "Postre brownie", "precio_unitario": 5800},
    {"cantidad": 1, "nombre": "Agua mineral 1.5L", "precio_unitario": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": ["El subtotal facturado es $73.000, pero el calculado sumando los items es $75.000 (diferencia de $2.000)."]
}