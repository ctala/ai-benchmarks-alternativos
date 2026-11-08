# Claude Opus 5.5 — ocr_extraction/receipt_math_verification

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.36 | quality: 10.0
- latency_total: 13.112s | tokens_per_second: 108.1
- input_tokens: 464 | output_tokens: 1418

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
      "total_item": 37800
    },
    {
      "cantidad": 1,
      "descripcion": "Ensalada cesar",
      "precio_unitario": 7500,
      "total_item": 7500
    },
    {
      "cantidad": 3,
      "descripcion": "Pisco sour",
      "precio_unitario": 6900,
      "total_item": 20700
    },
    {
      "cantidad": 1,
      "descripcion": "Postre brownie",
      "precio_unitario": 5800,
      "total_item": 5800
    },
    {
      "cantidad": 1,
      "descripcion": "Agua mineral 1.5L",
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
    "Subtotal incorrecto: la suma de los items es $75.000 (37.800 + 7.500 + 20.700 + 5.800 + 3.200), pero la boleta indica $73.000. Hay una diferencia de $2.000 a favor del cliente.",
    "Propina: el 10% de $73.000 ($7.300) está bien calculado, pero se aplicó sobre un subtotal erróneo. Sobre el subtotal real, la propina sugerida debería ser $7.500.",
    "Total: la suma $73.000 + $7.300 = $80.300 es aritméticamente consistente con las cifras de la boleta, pero arrastra el error del subtotal. El total correcto sería $82.500 ($75.000 + $7.500), es decir, $2.200 más que lo cobrado."
  ]
}
```

**Nota:** los campos `propina_correcta` y `total_correcto` están en `false` porque se evaluaron contra los valores reales. Las operaciones de la boleta son internamente correctas (10% de $73.000 y suma de subtotal más propina), pero parten de un subtotal mal sumado. El error es a favor del cliente: se cobraron $2.200 menos de lo que correspondía.