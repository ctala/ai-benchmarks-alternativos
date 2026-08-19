# GPT-4.1 — ocr_extraction/receipt_math_verification

- model_id: `gpt-4.1`
- success: True  | final: 6.92 | quality: 7.5
- latency_total: 5.89s | tokens_per_second: 76.6
- input_tokens: 315 | output_tokens: 451
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con cálculos correctos y datos exactos, proporcionando utilidad práctica para un emprendedor, aunque la profundidad es básica.

## Respuesta completa

```json
{
  "items": [
    {
      "descripcion": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total": 3200
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

**Cálculos:**
- Lomo vetado: 2 x 18,900 = 37,800
- Ensalada cesar: 1 x 7,500 = 7,500
- Pisco sour: 3 x 6,900 = 20,700
- Postre brownie: 1 x 5,800 = 5,800
- Agua mineral 1.5L: 1 x 3,200 = 3,200

**Subtotal calculado:** 37,800 + 7,500 + 20,700 + 5,800 + 3,200 = 73,000

**Propina (10%):** 73,000 x 0.10 = 7,300

**Total:** 73,000 + 7,300 = 80,300

No hay errores en los cálculos.