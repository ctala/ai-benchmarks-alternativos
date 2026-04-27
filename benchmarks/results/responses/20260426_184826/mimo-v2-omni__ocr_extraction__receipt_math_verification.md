# MiMo-V2-Omni (multimodal) — ocr_extraction/receipt_math_verification

- model_id: `xiaomi/mimo-v2-omni`
- success: True  | final: 6.86 | quality: 7.04
- latency_total: 16.615s | tokens_per_second: 117.1
- input_tokens: 596 | output_tokens: 1945
- judge_score: 4.2 | justificación: 

## Respuesta completa

{
  "items": [
    {"nombre": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900},
    {"nombre": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500},
    {"nombre": "Pisco sour", "cantidad": 3, "precio_unitario": 6900},
    {"nombre": "Postre brownie", "cantidad": 1, "precio_unitario": 5800},
    {"nombre": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": ["El subtotal facturado ($73,000) no coincide con la suma de los items ($75,000). Hay una diferencia de $2,000."]
}