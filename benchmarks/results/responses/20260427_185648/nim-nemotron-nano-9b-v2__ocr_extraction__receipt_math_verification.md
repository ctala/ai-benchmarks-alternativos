# Nemotron Nano 9B v2 (NIM) — ocr_extraction/receipt_math_verification

- model_id: `nvidia/nvidia-nemotron-nano-9b-v2`
- success: True  | final: 6.6 | quality: 7.71
- latency_total: 43.441s | tokens_per_second: 49.8
- input_tokens: 380 | output_tokens: 2165
- judge_score: 4.2 | justificación: 

## Respuesta completa



{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio": 18900
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio": 6900
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": [
    "Subtotal incorrecto: el cálculo de los items suma $75,000 (2x18900 + 1x7500 + 3x6900 + 1x5800 + 1x3200), no $73,000"
  ]
}
