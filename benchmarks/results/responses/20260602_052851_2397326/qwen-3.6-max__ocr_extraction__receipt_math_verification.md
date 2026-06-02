# Qwen 3.6 Max — ocr_extraction/receipt_math_verification

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 6.35 | quality: 8.15
- latency_total: 115.067s | tokens_per_second: 43.2
- input_tokens: 367 | output_tokens: 4972
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una buena profundidad al identificar errores en el subtotal y explicar sus implicaciones, lo que la hace muy útil para un emprendedor.

## Respuesta completa

```json
{
  "items": [
    {"nombre": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900, "precio_total": 37800},
    {"nombre": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500, "precio_total": 7500},
    {"nombre": "Pisco sour", "cantidad": 3, "precio_unitario": 6900, "precio_total": 20700},
    {"nombre": "Postre brownie", "cantidad": 1, "precio_unitario": 5800, "precio_total": 5800},
    {"nombre": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200, "precio_total": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": [
    "El subtotal facturado ($73.000) es incorrecto. La suma real de los ítems es $75.000, por lo que faltan $2.000 en la suma.",
    "Aunque la propina (10% de $73.000 = $7.300) y el total ($73.000 + $7.300 = $80.300) están matemáticamente bien calculados sobre el subtotal impreso, al ser este erróneo, los montos finales son inferiores a lo que correspondería realmente ($7.500 de propina y $82.500 de total)."
  ]
}
```