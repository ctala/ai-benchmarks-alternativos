# GPT-5.6 Luna — ocr_extraction/receipt_math_verification

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 9.48 | quality: 10.0
- latency_total: 4.403s | tokens_per_second: 107.4
- input_tokens: 314 | output_tokens: 473

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
      "descripcion": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "La suma de los items es $75.000, pero el subtotal facturado es $73.000.",
    "La propina facturada de $7.300 corresponde al 10% del subtotal facturado, pero el 10% del subtotal calculado sería $7.500.",
    "El total correcto considerando el subtotal calculado y una propina del 10% sería $82.500, no $80.300."
  ]
}