# Qwen 3.6 Plus — ocr_extraction/receipt_math_verification

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 105.788s | tokens_per_second: 54.8
- input_tokens: 367 | output_tokens: 5795
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al identificar errores en el cálculo del subtotal y la propina, lo que proporciona insights valiosos para un emprendedor.

## Respuesta completa

```json
{
  "items": [
    {"nombre": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900, "total_linea": 37800},
    {"nombre": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500, "total_linea": 7500},
    {"nombre": "Pisco sour", "cantidad": 3, "precio_unitario": 6900, "total_linea": 20700},
    {"nombre": "Postre brownie", "cantidad": 1, "precio_unitario": 5800, "total_linea": 5800},
    {"nombre": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200, "total_linea": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) es $2.000 menor a la suma real de los ítems ($75.000).",
    "La propina está matemáticamente bien calculada sobre el subtotal impreso (10% de $73.000 = $7.300), pero como el subtotal es incorrecto, el total final facturado ($80.300) no corresponde al valor real. El total correcto debería ser $82.500 ($75.000 + 10% propina)."
  ]
}
```