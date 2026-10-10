# Claude Fable 5.1 — ocr_extraction/receipt_math_verification

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.2 | quality: 8.75
- latency_total: 12.333s | tokens_per_second: 88.6
- input_tokens: 464 | output_tokens: 1093

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
      "total_linea": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total_linea": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total_linea": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total_linea": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total_linea": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Diferencia: $2.000 a favor del cliente (se cobró de menos).",
    "La propina de $7.300 es aritméticamente correcta como 10% del subtotal facturado ($73.000), pero al estar basada en un subtotal erróneo, el 10% real sobre $75.000 debería ser $7.500.",
    "El total de $80.300 es consistente con los valores facturados ($73.000 + $7.300), pero el total correcto según los items debería ser $82.500 ($75.000 + $7.500)."
  ]
}
```

**Resumen:** El único error de origen está en el subtotal, que suma $2.000 menos de lo que corresponde (equivalente aproximadamente a un error de digitación). La propina y el total se calcularon correctamente *a partir de ese subtotal erróneo*, por lo que arrastran la diferencia. El restaurante cobró $2.200 menos de lo debido.