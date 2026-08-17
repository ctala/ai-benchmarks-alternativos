# Kimi K2 — ocr_extraction/receipt_math_verification

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 7.97 | quality: 8.75
- latency_total: 14.071s | tokens_per_second: 42.8
- input_tokens: 336 | output_tokens: 602
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una buena profundidad al identificar errores en el recibo y explicar sus implicaciones, lo que la hace muy útil para un emprendedor.

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
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con el calculado ($75.000). Diferencia de $2.000.",
    "La propina sugerida ($7.300) es el 10% del subtotal facturado incorrecto, pero deberia ser $7.500 (10% de $75.000) o el recibo tiene un error de $200 si se basa en su propio subtotal.",
    "El total facturado ($80.300) es incorrecto. Deberia ser $82.500 si se usa el subtotal correcto de $75.000 + propina $7.500, o $80.300 si se acepta el subtotal de $73.000 con propina de $7.300 (aunque matematicamente 73.000 * 1.10 = 80.300, lo cual es consistente internamente pero el subtotal base esta mal)."
  ]
}
```

**Resumen del error:** El recibo tiene un error de $2.000 en el subtotal. La suma real de los ítems es **$75.000**, no $73.000. Esto afecta toda la cadena de cálculos, aunque curiosamente el total de $80.300 es matemáticamente consistente con el subtotal incorrecto de $73.000 más 10% de propina ($7.300).