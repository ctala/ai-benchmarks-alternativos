# Qwen 3.6 Plus — ocr_extraction/receipt_math_verification

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.06 | quality: 8.75
- latency_total: 9.098s | tokens_per_second: 54.0
- input_tokens: 369 | output_tokens: 491

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
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "subtotal_item": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "subtotal_item": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "subtotal_item": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "subtotal_item": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "subtotal_item": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los ítems ($75.000). Diferencia: -$2.000.",
    "La propina sugerida ($7.300) está calculada sobre el subtotal incorrecto ($73.000). La propina correcta (10% de $75.000) sería $7.500.",
    "El total facturado ($80.300) es incorrecto debido al error en el subtotal y la propina. El total correcto debería ser $82.500 ($75.000 + $7.500)."
  ]
}
```