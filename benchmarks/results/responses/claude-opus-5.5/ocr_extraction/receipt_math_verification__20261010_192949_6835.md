# Claude Opus 5.5 — ocr_extraction/receipt_math_verification

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.4 | quality: 10.0
- latency_total: 11.452s | tokens_per_second: 101.5
- input_tokens: 464 | output_tokens: 1162

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
  "propina_facturada": 7300,
  "propina_calculada": 7500,
  "propina_correcta": false,
  "total_facturado": 80300,
  "total_calculado": 82500,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Faltan $2.000.",
    "La propina de $7.300 es exactamente el 10% del subtotal facturado, pero como ese subtotal está mal, la propina correcta sería $7.500. Faltan $200.",
    "El total de $80.300 suma bien el subtotal y la propina facturados ($73.000 + $7.300), pero arrastra el error del subtotal. El total correcto sería $82.500. Faltan $2.200."
  ]
}
```

**Resumen:** el error está en el subtotal. Se cobraron $2.000 menos de lo que suman los items, una diferencia que coincide con el precio de varios productos de la carta. Los cálculos posteriores (propina y total) están bien hechos, pero parten de un subtotal equivocado. Esta diferencia favorece al cliente: en total se cobraron $2.200 menos de lo que correspondía.