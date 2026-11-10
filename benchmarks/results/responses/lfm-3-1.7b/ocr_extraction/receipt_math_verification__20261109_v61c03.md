# LFM-3 1.7B — ocr_extraction/receipt_math_verification

- model_id: `liquid/lfm-3-1.7b`
- success: True  | final: 4.58 | quality: 3.75
- latency_total: 24.247s | tokens_per_second: 295.1
- input_tokens: 335 | output_tokens: 7155

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
      "item": "Lomo vetado",
      "quantity": 2,
      "price_unit": 18.90
    },
    {
      "item": "Ensalada cesar",
      "quantity": 1,
      "price_unit": 7.50
    },
    {
      "item": "Pisco sour",
      "quantity": 3,
      "price_unit": 6.90
    },
    {
      "item": "Postre brownie",
      "quantity": 1,
      "price_unit": 5.80
    },
    {
      "item": "Agua mineral 1.5L",
      "quantity": 1,
      "price_unit": 3.20
    }
  ],
  "subtotal_facturado": 73.0,
  "subtotal_calculado": 75.0,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal mostrado ($73.00) no coincide con la suma de los productos cantidad × precio unitario ($75.00).",
    "La propina sugerida ($7.30) no es el 10% del subtotal real ($7.50); correspondería al 10% del subtotal impreso ($73.00).",
    "El total indicado ($80.30) no satisface ni el subtotal real más la propina correcta ($75.00 + $7.50 = $82.50)."
  ]
}