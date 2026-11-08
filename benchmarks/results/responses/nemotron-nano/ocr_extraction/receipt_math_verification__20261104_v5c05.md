# Nemotron 3 Nano 30B — ocr_extraction/receipt_math_verification

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 8.38 | quality: 8.75
- latency_total: 5.718s | tokens_per_second: 68.6
- input_tokens: 384 | output_tokens: 392

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
      "descripcion": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "precio_total": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "precio_total": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "precio_total": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "precio_total": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "precio_total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 84000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal registrado ($73,000) no coincide con el cálculo de los ítems ($84,000).",
    "El total registrado ($80,300) no coincide con la suma del subtotal correcto y la propina ($91,300)."
  ]
}