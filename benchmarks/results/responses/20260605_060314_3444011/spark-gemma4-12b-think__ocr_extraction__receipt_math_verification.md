# Gemma 4 12B (Spark llama-server, reasoning) — ocr_extraction/receipt_math_verification

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 6.54 | quality: 7.04
- latency_total: 80.889s | tokens_per_second: 25.6
- input_tokens: 380 | output_tokens: 2073
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total_item": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total_item": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total_item": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total_item": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total_item": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) es incorrecto. La suma real de los ítems es $75.000 (hay una diferencia de $2.000).",
    "El total final ($80.300) es incorrecto porque se basa en un subtotal mal calculado."
  ]
}
```