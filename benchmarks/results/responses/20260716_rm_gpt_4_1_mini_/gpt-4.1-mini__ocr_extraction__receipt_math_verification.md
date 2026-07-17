# GPT-4.1 Mini — ocr_extraction/receipt_math_verification

- model_id: `gpt-4.1-mini`
- success: True  | final: 7.24 | quality: 7.5
- latency_total: 6.044s | tokens_per_second: 71.1
- input_tokens: 315 | output_tokens: 430
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con una exactitud de datos perfecta, pero carece de profundidad más allá de la verificación básica de cálculos.

## Respuesta completa

```json
{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "precio_total": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "precio_total": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "precio_total": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "precio_total": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
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
```

**Detalle de cálculos:**

- Items totales:
  - 2 x 18900 = 37800
  - 1 x 7500 = 7500
  - 3 x 6900 = 20700
  - 1 x 5800 = 5800
  - 1 x 3200 = 3200  
  Suma = 37800 + 7500 + 20700 + 5800 + 3200 = 73000

- Propina sugerida (10%): 10% de 73000 = 7300 → correcto

- Total esperado: 73000 + 7300 = 80300 → coincide con el total facturado

No se detectan errores en el recibo.