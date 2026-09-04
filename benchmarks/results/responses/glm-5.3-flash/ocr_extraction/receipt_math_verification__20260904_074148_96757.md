# GLM 5.3 Flash — ocr_extraction/receipt_math_verification

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.68 | quality: 8.75
- latency_total: 3.939s | tokens_per_second: 140.1
- input_tokens: 325 | output_tokens: 552

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
    {"nombre": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900, "subtotal": 37800},
    {"nombre": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500, "subtotal": 7500},
    {"nombre": "Pisco sour", "cantidad": 3, "precio_unitario": 6900, "subtotal": 20700},
    {"nombre": "Postre brownie", "cantidad": 1, "precio_unitario": 5800, "subtotal": 5800},
    {"nombre": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200, "subtotal": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Hay una diferencia de $2.000 a favor del cliente.",
    "La propina facturada ($7.300) corresponde al 10% del subtotal incorrecto. El 10% de $75.000 sería $7.500.",
    "El total facturado ($80.300) no coincide con subtotal correcto + propina correcta ($75.000 + $7.500 = $82.500). Diferencia de $2.200 a favor del cliente."
  ]
}
```

**Resumen:** El subtotal fue calculado con $2.000 menos de lo que suman los ítems (posiblemente se omitió parte de un producto o hubo error de digitación). La propina y el total heredan ese error. Si se corrige el subtotal, el total debería ser **$82.500** en lugar de $80.300. El error favorece al cliente, por lo que conviene consultarlo con el restaurante.