# DeepSeek V4.1 Flash — ocr_extraction/receipt_math_verification

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.62 | quality: 8.75
- latency_total: 3.017s | tokens_per_second: 132.3
- input_tokens: 338 | output_tokens: 399

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
    {"cantidad": 2, "descripcion": "Lomo vetado", "precio_unitario": 18900, "precio_total": 37800},
    {"cantidad": 1, "descripcion": "Ensalada cesar", "precio_unitario": 7500, "precio_total": 7500},
    {"cantidad": 3, "descripcion": "Pisco sour", "precio_unitario": 6900, "precio_total": 20700},
    {"cantidad": 1, "descripcion": "Postre brownie", "precio_unitario": 5800, "precio_total": 5800},
    {"cantidad": 1, "descripcion": "Agua mineral 1.5L", "precio_unitario": 3200, "precio_total": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Diferencia de $2.000.",
    "La propina sugerida (10%) está calculada sobre el subtotal facturado ($73.000 → $7.300), pero el 10% del subtotal real ($75.000) sería $7.500.",
    "El total facturado ($80.300) no corresponde a la suma correcta: $75.000 + $7.500 = $82.500. Diferencia de $2.200."
  ]
}
```