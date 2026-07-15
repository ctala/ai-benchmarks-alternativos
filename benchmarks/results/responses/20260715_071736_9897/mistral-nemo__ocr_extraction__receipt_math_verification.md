# Mistral Nemo — ocr_extraction/receipt_math_verification

- model_id: `mistralai/mistral-nemo`
- success: True  | final: 7.12 | quality: 7.5
- latency_total: 11.965s | tokens_per_second: 20.5
- input_tokens: 371 | output_tokens: 245
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con datos exactos y útil para un emprendedor, aunque carece de profundidad más allá de la verificación básica.

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
  "subtotal_calculado": 73000,
  "subtotal_correcto": true,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": []
}