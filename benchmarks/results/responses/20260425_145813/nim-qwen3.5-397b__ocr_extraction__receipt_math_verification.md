# Qwen 3.5 397B (NIM) — ocr_extraction/receipt_math_verification

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 6.76 | quality: 7.59
- latency_total: 32.13s | tokens_per_second: 15.1
- input_tokens: 324 | output_tokens: 486
- judge_score: 4.6 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "cantidad": 2,
      "descripcion": "Lomo vetado",
      "precio_unitario": 18900,
      "precio_total": 37800
    },
    {
      "cantidad": 1,
      "descripcion": "Ensalada cesar",
      "precio_unitario": 7500,
      "precio_total": 7500
    },
    {
      "cantidad": 3,
      "descripcion": "Pisco sour",
      "precio_unitario": 6900,
      "precio_total": 20700
    },
    {
      "cantidad": 1,
      "descripcion": "Postre brownie",
      "precio_unitario": 5800,
      "precio_total": 5800
    },
    {
      "cantidad": 1,
      "descripcion": "Agua mineral 1.5L",
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
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Falta $2.000 en el registro del subtotal.",
    "La propina sugerida ($7.300) está calculada sobre el subtotal facturado incorrecto ($73.000). El 10% real de la suma de items es $7.500.",
    "El total final ($80.300) es incorrecto porque arrastra el error del subtotal. El total real debería ser $82.500 ($75.000 + $7.500)."
  ]
}
```