# Nemotron 3 Nano Omni 30B-A3B Reasoning — ocr_extraction/receipt_math_verification

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- success: True  | final: 8.53 | quality: 8.75
- latency_total: 8.477s | tokens_per_second: 170.6
- input_tokens: 384 | output_tokens: 1446
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una clara organización y exactitud de datos, aunque la profundidad es solo aceptable ya que no ofrece insights adicionales más allá de la verificación básica.

## Respuesta completa

{
  "items": [
    {
      "description": "Lomo vetado",
      "quantity": 2,
      "unit_price": 18.900,
      "total_price": 37.800
    },
    {
      "description": "Ensalada cesar",
      "quantity": 1,
      "unit_price": 7.500,
      "total_price": 7.500
    },
    {
      "description": "Pisco sour",
      "quantity": 3,
      "unit_price": 6.900,
      "total_price": 20.700
    },
    {
      "description": "Postre brownie",
      "quantity": 1,
      "unit_price": 5.800,
      "total_price": 5.800
    },
    {
      "description": "Agua mineral 1.5L",
      "quantity": 1,
      "unit_price": 3.200,
      "total_price": 3.200
    }
  ],
  "subtotal_facturado": 73.000,
  "subtotal_calculado": 75.000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "Subtotal no coincide con la suma de los ítems",
    "Propina calculada sobre un subtotal incorrecto",
    "Total no corresponde a subtotal + propina correcta"
  ]
}