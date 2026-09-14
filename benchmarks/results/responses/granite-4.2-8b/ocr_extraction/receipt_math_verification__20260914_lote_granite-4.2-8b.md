# Granite 4.2 8B — ocr_extraction/receipt_math_verification

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 3.39 | quality: 2.5
- latency_total: 166.081s | tokens_per_second: 78.6
- input_tokens: 357 | output_tokens: 13057

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
      "name": "Lomo vetado",
      "quantity": 2,
      "price_per_unit": 18.9
    },
    {
      "name": "Ensalada cesar",
      "quantity": 1,
      "price_per_unit": 7.5
    },
    {
      "name": "Pisco sour",
      "quantity": 3,
      "price_per_unit": 6.9
    },
    {
      "name": "Postre brownie",
      "quantity": 1,
      "price_per_unit": 5.8
    },
    {
      "name": "Agua mineral 1.5L",
      "quantity": 1,
      "price_per_unit": 3.2
    }
  ],
  "subtotal_facturado": 73.0,
  "subtotal_calculado": 75.0,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "Subtotal facturado ($73.00) no coincide con el cálculo de los ítems (esperado $75.00).",
    "Propina sugerida facturada ($7.30) no coincide con el 10% del subtotal correcto ($75.00 → $7.50).",
    "Total facturado ($80.30) no coincide con subtotal + propina (esperado $82.50)."
  ]
}