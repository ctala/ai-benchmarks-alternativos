# Claude Opus 5.5 — ocr_extraction/receipt_math_verification

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.53 | quality: 8.75
- latency_total: 10.07s | tokens_per_second: 110.3
- input_tokens: 464 | output_tokens: 1111

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
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "Subtotal incorrecto: la suma de los items es $75.000, pero la boleta indica $73.000 (diferencia de $2.000 a favor del cliente).",
    "Propina: el 10% de $73.000 = $7.300 está bien calculado sobre el subtotal facturado, pero sobre el subtotal real debería ser $7.500 (diferencia de $200).",
    "Total: $73.000 + $7.300 = $80.300 es aritméticamente consistente con la boleta, pero el total correcto debería ser $75.000 + $7.500 = $82.500 (diferencia de $2.200)."
  ]
}
```

**Notas:**
- La propina se marca como `false` porque, aunque el 10% está bien aplicado, se calculó sobre un subtotal erróneo.
- El error es a favor del cliente: se cobraron $2.200 menos de lo que correspondía.
- Una posible causa es que se omitió algún cargo o se aplicó un descuento no indicado en la boleta.