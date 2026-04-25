# GLM-5.1 — ocr_extraction/receipt_math_verification

- model_id: `z-ai/glm-5.1`
- success: True  | final: 6.46 | quality: 7.32
- latency_total: 57.21s | tokens_per_second: 36.4
- input_tokens: 318 | output_tokens: 2083
- judge_score: 4.4 | justificación: 

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
    "Error en el subtotal: La suma de los precios de los items es $75.000, pero el recibo facturó $73.000 (falta un descuento de $2.000 o hubo un error de suma).",
    "Error en la propina: La propina del 10% debería ser $7.500 calculada sobre el subtotal real ($75.000), pero se calculó sobre el subtotal incorrecto resultando en $7.300.",
    "Error en el total: El total a pagar debería ser $82.500 ($75.000 + $7.500), pero el recibo indica $80.300."
  ]
}
```