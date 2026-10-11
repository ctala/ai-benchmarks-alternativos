# Bonsai 2 27B — ocr_extraction/receipt_math_verification

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 7.75 | quality: 8.75
- latency_total: 84.18s | tokens_per_second: 38.7
- input_tokens: 409 | output_tokens: 3261

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



{
  "items": [
    {
      "cantidad": 2,
      "nombre": "Lomo vetado",
      "precio_unitario": 18900,
      "subtotal": 37800
    },
    {
      "cantidad": 1,
      "nombre": "Ensalada cesar",
      "precio_unitario": 7500,
      "subtotal": 7500
    },
    {
      "cantidad": 3,
      "nombre": "Pisco sour",
      "precio_unitario": 6900,
      "subtotal": 20700
    },
    {
      "cantidad": 1,
      "nombre": "Postre brownie",
      "precio_unitario": 5800,
      "subtotal": 5800
    },
    {
      "cantidad": 1,
      "nombre": "Agua mineral 1.5L",
      "precio_unitario": 3200,
      "subtotal": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado es 73000, pero la suma de los items es 75000.",
    "La propina sugerida es 7300; si se calcula sobre el subtotal correcto (75000) debería ser 7500.",
    "El total facturado es 80300; con el subtotal correcto y propina correcta debería ser 82500."
  ]
}