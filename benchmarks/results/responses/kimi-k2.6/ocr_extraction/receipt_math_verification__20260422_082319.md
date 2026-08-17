# Kimi K2.6 — ocr_extraction/receipt_math_verification

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 6.06 | quality: 7.04
- latency_total: 56.304s | tokens_per_second: 48.8
- input_tokens: 334 | output_tokens: 2750
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "Subtotal incorrecto: la suma de ítems es $75.000, pero se facturó $73.000 (diferencia de $2.000).",
    "Propina incorrecta: el 10% sobre el subtotal real ($75.000) debería ser $7.500, no $7.300.",
    "Total incorrecto: con los valores correctos debería ser $82.500, no $80.300."
  ]
}
```