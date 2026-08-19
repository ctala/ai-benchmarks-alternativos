# KAT Coder Air v2.5 — ocr_extraction/receipt_math_verification

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 9.14 | quality: 10.0
- latency_total: 6.597s | tokens_per_second: 191.3
- input_tokens: 367 | output_tokens: 1262

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
    {"name": "Lomo vetado", "quantity": 2, "unit_price": 18900, "total_price": 37800},
    {"name": "Ensalada cesar", "quantity": 1, "unit_price": 7500, "total_price": 7500},
    {"name": "Pisco sour", "quantity": 3, "unit_price": 6900, "total_price": 20700},
    {"name": "Postre brownie", "quantity": 1, "unit_price": 5800, "total_price": 5800},
    {"name": "Agua mineral 1.5L", "quantity": 1, "unit_price": 3200, "total_price": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Falta $2.000."
  ]
}
```