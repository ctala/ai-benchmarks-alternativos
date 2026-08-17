# GPT-5.6 Terra Pro — ocr_extraction/receipt_math_verification

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 7.69 | quality: 8.75
- latency_total: 9.249s | tokens_per_second: 202.0
- input_tokens: 4463 | output_tokens: 1868

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
      "total_item": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total_item": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total_item": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total_item": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total_item": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    {
      "campo": "subtotal",
      "facturado": 73000,
      "calculado": 75000,
      "diferencia": 2000,
      "mensaje": "El subtotal facturado es $2.000 menor que la suma de los items."
    },
    {
      "campo": "propina",
      "facturado": 7300,
      "calculado": 7500,
      "mensaje": "La propina facturada corresponde al 10% del subtotal facturado, pero el 10% del subtotal correcto es $7.500."
    },
    {
      "campo": "total",
      "facturado": 80300,
      "calculado": 82500,
      "diferencia": 2200,
      "mensaje": "El total facturado coincide con el subtotal y propina facturados, pero no con los valores correctos calculados desde los items."
    }
  ]
}