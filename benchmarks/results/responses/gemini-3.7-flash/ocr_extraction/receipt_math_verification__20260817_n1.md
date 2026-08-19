# Gemini 3.7 Flash — ocr_extraction/receipt_math_verification

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.06 | quality: 8.75
- latency_total: 7.402s | tokens_per_second: 154.6
- input_tokens: 364 | output_tokens: 1144

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo un recibo de restaurante:

===============================
  RESTAURANTE EL PARRILLERO
  Av. Italia 1890, Nunoa
  Boleta N° 0082341
  Fecha: 12/04/2026 21:45
===============================
Mesa: 7          Mesero: Carlos

2x Lomo vetado         $18.900 c/u
1x Ensalada cesar      $7.500
3x Pisco sour          $6.900 c/u
1x Postre brownie      $5.800
1x Agua mineral 1.5L   $3.200

-------------------------------
Subtotal:              $73.000
Propina sugerida (10%): $7.300
-------------------------------
TOTAL:                 $80.300
===============================
Pago: Tarjeta credito ****4521

Tareas:
1. Extrae todos los items con sus precios en JSON
2. Verifica si el subtotal esta correcto sumando los items
3. Verifica si la propina esta bien calculada
4. Indica si hay algun error en los calculos

Responde en JSON con formato:
{
  "items": [...],
  "subtotal_facturado": 0,
  "subtotal_calculado": 0,
  "subtotal_correcto": true/false,
  "propina_correcta": true/false,
  "total_correcto": true/false,
  "errores": []
}


## Respuesta completa

```json
{
  "items": [
    {
      "cantidad": 2,
      "descripcion": "Lomo vetado",
      "precio_unitario": 18900,
      "total": 37800
    },
    {
      "cantidad": 1,
      "descripcion": "Ensalada cesar",
      "precio_unitario": 7500,
      "total": 7500
    },
    {
      "cantidad": 3,
      "descripcion": "Pisco sour",
      "precio_unitario": 6900,
      "total": 20700
    },
    {
      "cantidad": 1,
      "descripcion": "Postre brownie",
      "precio_unitario": 5800,
      "total": 5800
    },
    {
      "cantidad": 1,
      "descripcion": "Agua mineral 1.5L",
      "precio_unitario": 3200,
      "total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) es incorrecto; la suma real de los ítems es $75.000 (diferencia de -$2.000).",
    "La propina sugerida (10%) calculada sobre el consumo real debería ser $7.500 en lugar de $7.300.",
    "El total real (subtotal real + 10% de propina) debería ser $82.500 en lugar de $80.300."
  ]
}
```