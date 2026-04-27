# Hermes 4 405B — ocr_extraction/receipt_math_verification

- model_id: `nousresearch/hermes-4-405b`
- success: True  | final: 6.73 | quality: 7.09
- latency_total: 7.604s | tokens_per_second: 35.1
- input_tokens: 336 | output_tokens: 267
- judge_score: 4.4 | justificación: 

## Respuesta completa

{
  "items": [
    {
      "item": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "precio_total": 37800
    },
    {
      "item": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "precio_total": 7500
    },
    {
      "item": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "precio_total": 20700
    },
    {
      "item": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "precio_total": 5800
    },
    {
      "item": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "precio_total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 73000,
  "subtotal_correcto": true,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": []
}