# GPT-OSS 20B (Groq) — ocr_extraction/receipt_math_verification

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.33 | quality: 6.81
- latency_total: 1.548s | tokens_per_second: 712.1
- input_tokens: 379 | output_tokens: 1102
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "quantity": 2,
      "description": "Lomo vetado",
      "unit_price": 18900,
      "total_price": 37800
    },
    {
      "quantity": 1,
      "description": "Ensalada cesar",
      "unit_price": 7500,
      "total_price": 7500
    },
    {
      "quantity": 3,
      "description": "Pisco sour",
      "unit_price": 6900,
      "total_price": 20700
    },
    {
      "quantity": 1,
      "description": "Postre brownie",
      "unit_price": 5800,
      "total_price": 5800
    },
    {
      "quantity": 1,
      "description": "Agua mineral 1.5L",
      "unit_price": 3200,
      "total_price": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "Subtotal incorrecto: calculado 75000 vs facturado 73000",
    "Propina incorrecta: calculada 7500 vs facturada 7300",
    "Total incorrecto: calculado 82500 vs facturado 80300"
  ]
}
```