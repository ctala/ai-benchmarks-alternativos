# MiniMax M3 — ocr_extraction/receipt_math_verification

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.09 | quality: 8.24
- latency_total: 41.455s | tokens_per_second: 41.1
- input_tokens: 488 | output_tokens: 1705
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al identificar errores y sus implicaciones, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "items": [
    {
      "cantidad": 2,
      "nombre": "Lomo vetado",
      "precio_unitario": 18900,
      "subtotal_item": 37800
    },
    {
      "cantidad": 1,
      "nombre": "Ensalada cesar",
      "precio_unitario": 7500,
      "subtotal_item": 7500
    },
    {
      "cantidad": 3,
      "nombre": "Pisco sour",
      "precio_unitario": 6900,
      "subtotal_item": 20700
    },
    {
      "cantidad": 1,
      "nombre": "Postre brownie",
      "precio_unitario": 5800,
      "subtotal_item": 5800
    },
    {
      "cantidad": 1,
      "nombre": "Agua mineral 1.5L",
      "precio_unitario": 3200,
      "subtotal_item": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "Subtotal incorrecto: el subtotal facturado es $73.000 pero la suma real de los items es $75.000. Hay una diferencia de $2.000 (probablemente un item no contabilizado o un error de suma).",
    "Propina mal calculada: se calculó el 10% sobre el subtotal errado ($73.000), dando $7.300. La propina correcta sobre el subtotal real ($75.000) debería ser $7.500.",
    "Total incorrecto: el total facturado es $80.300, pero el total correcto debería ser $82.500 (subtotal $75.000 + propina $7.500).",
    "Nota: la aritmética interna del recibo es consistente (73.000 + 7.300 = 80.300), pero todos los valores derivan de un subtotal erróneo."
  ]
}
```

**Resumen:** El recibo tiene un **error en el subtotal** de **$2.000** menos. La suma correcta de los 5 ítems es **$75.000**, no $73.000. Esto arrastra un error en la propina (debería ser $7.500) y en el total final (debería ser **$82.500**). Te recomiendo revisar el recibo y pedir la corrección antes de pagar o conservar el comprobante. 🔍