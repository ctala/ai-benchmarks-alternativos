# Claude Opus 5 (suscripción) — ocr_extraction/receipt_math_verification

- model_id: `claude-opus-5`
- success: True  | final: 7.17 | quality: 8.75
- latency_total: 27.287s | tokens_per_second: 47.3
- input_tokens: 2 | output_tokens: 1291

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
    { "nombre": "Lomo vetado",        "cantidad": 2, "precio_unitario": 18900, "subtotal_item": 37800 },
    { "nombre": "Ensalada cesar",     "cantidad": 1, "precio_unitario": 7500,  "subtotal_item": 7500 },
    { "nombre": "Pisco sour",         "cantidad": 3, "precio_unitario": 6900,  "subtotal_item": 20700 },
    { "nombre": "Postre brownie",     "cantidad": 1, "precio_unitario": 5800,  "subtotal_item": 5800 },
    { "nombre": "Agua mineral 1.5L",  "cantidad": 1, "precio_unitario": 3200,  "subtotal_item": 3200 }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_facturada": 7300,
  "propina_calculada_sobre_subtotal_real": 7500,
  "propina_correcta": false,
  "total_facturado": 80300,
  "total_calculado": 82500,
  "total_correcto": false,
  "errores": [
    {
      "tipo": "subtotal_incorrecto",
      "detalle": "La suma de los items da $75.000, pero la boleta declara $73.000. Faltan $2.000.",
      "diferencia": -2000
    },
    {
      "tipo": "propina_mal_calculada",
      "detalle": "El 10% está bien aplicado sobre el subtotal impreso ($73.000 x 10% = $7.300), pero como el subtotal está mal, la propina real debería ser $7.500.",
      "diferencia": -200
    },
    {
      "tipo": "total_incorrecto",
      "detalle": "El total es internamente consistente ($73.000 + $7.300 = $80.300), pero arrastra el error del subtotal. El total correcto es $82.500.",
      "diferencia": -2200
    }
  ],
  "observaciones": [
    "Los tres errores vienen de una sola causa: el subtotal. Los cálculos posteriores son aritméticamente consistentes entre sí.",
    "El error va a FAVOR del cliente: se cobraron $2.200 menos de lo que corresponde.",
    "Posible origen: no se cargó bien un item de $2.000 o se aplicó un descuento no declarado en la boleta.",
    "La propina es sugerida, no obligatoria (Chile, Ley 21.442), así que el monto exigible real es solo el subtotal de $75.000."
  ]
}
```