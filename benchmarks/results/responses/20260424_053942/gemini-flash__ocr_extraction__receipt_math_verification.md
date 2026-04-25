# Gemini 2.5 Flash — ocr_extraction/receipt_math_verification

- model_id: `google/gemini-2.5-flash`
- success: True  | final: 7.33 | quality: 7.09
- latency_total: 2.116s | tokens_per_second: 129.5
- input_tokens: 365 | output_tokens: 274
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 73000,
  "subtotal_correcto": true,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": []
}
```