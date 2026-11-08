# Ministral 14B — ocr_extraction/receipt_math_verification

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 7.28 | quality: 7.5
- latency_total: 13.704s | tokens_per_second: 41.6
- input_tokens: 371 | output_tokens: 570

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
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "precio_total": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "precio_total": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "precio_total": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "precio_total": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "precio_total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 74800,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    {
      "descripcion": "El subtotal facturado ($73.000) no coincide con el subtotal calculado ($74.800).",
      "detalle": "La suma de los items ($37.800 + $7.500 + $20.700 + $5.800 + $3.200) da $74.800, no $73.000."
    },
    {
      "descripcion": "La propina sugerida ($7.300) no está calculada correctamente sobre el subtotal real.",
      "detalle": "El 10% de $74.800 es $7.480, no $7.300."
    },
    {
      "descripcion": "El total facturado ($80.300) no coincide con la suma del subtotal real y la propina correcta.",
      "detalle": "La suma correcta debería ser $74.800 + $7.480 = $82.280."
    }
  ]
}
```