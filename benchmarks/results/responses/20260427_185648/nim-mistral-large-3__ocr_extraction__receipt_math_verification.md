# Mistral Large 3 675B (NIM) — ocr_extraction/receipt_math_verification

- model_id: `mistralai/mistral-large-3-675b-instruct-2512`
- success: True  | final: 6.74 | quality: 7.83
- latency_total: 85.745s | tokens_per_second: 8.5
- input_tokens: 342 | output_tokens: 732
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí está la respuesta en formato JSON con el análisis del recibo:

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
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000)",
    "La propina sugerida debería ser $7.500 (10% de $75.000) en lugar de $7.300",
    "El total debería ser $82.500 ($75.000 + $7.500) en lugar de $80.300"
  ]
}
```

### Explicación de los cálculos:
1. **Subtotal calculado**:
   - 2 × Lomo vetado = 2 × 18.900 = 37.800
   - 1 × Ensalada cesar = 7.500
   - 3 × Pisco sour = 3 × 6.900 = 20.700
   - 1 × Postre brownie = 5.800
   - 1 × Agua mineral = 3.200
   **Total = 37.800 + 7.500 + 20.700 + 5.800 + 3.200 = 75.000** (no 73.000 como aparece en el recibo).

2. **Propina**:
   - 10% de 75.000 = 7.500 (no 7.300 como aparece en el recibo).

3. **Total**:
   - 75.000 + 7.500 = 82.500 (no 80.300 como aparece en el recibo).

Hay errores en todos los cálculos del recibo.