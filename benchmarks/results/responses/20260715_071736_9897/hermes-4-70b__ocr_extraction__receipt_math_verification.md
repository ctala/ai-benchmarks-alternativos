# Hermes 4 70B — ocr_extraction/receipt_math_verification

- model_id: `nousresearch/hermes-4-70b`
- success: True  | final: 7.65 | quality: 7.5
- latency_total: 2.669s | tokens_per_second: 79.4
- input_tokens: 336 | output_tokens: 212
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con datos exactos y útil para un emprendedor, aunque carece de profundidad más allá de la verificación básica.

## Respuesta completa

{
  "items": [
    {
      "cantidad": 2,
      "item": "Lomo vetado",
      "precio": 18900
    },
    {
      "cantidad": 1,
      "item": "Ensalada cesar",
      "precio": 7500
    },
    {
      "cantidad": 3,
      "item": "Pisco sour",
      "precio": 6900
    },
    {
      "cantidad": 1,
      "item": "Postre brownie",
      "precio": 5800
    },
    {
      "cantidad": 1,
      "item": "Agua mineral 1.5L",
      "precio": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 73000,
  "subtotal_correcto": true,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": []
}