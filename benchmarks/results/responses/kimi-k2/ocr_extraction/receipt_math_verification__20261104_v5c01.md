# Kimi K2 — ocr_extraction/receipt_math_verification

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 7.76 | quality: 8.75
- latency_total: 14.554s | tokens_per_second: 41.9
- input_tokens: 336 | output_tokens: 610

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
      "precio_total": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "precio_total": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "precio_total": 20700
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "precio_total": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "precio_total": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Diferencia de $2.000",
    "La propina sugerida ($7.300) corresponde al 10% del subtotal facturado incorrecto, no del calculado. El 10% del subtotal correcto ($75.000) sería $7.500",
    "El total facturado ($80.300) es incorrecto. Con el subtotal correcto ($75.000) y propina del 10% ($7.500), el total debería ser $82.500"
  ]
}
```

**Verificación de cálculos:**

| Item | Cálculo | Total |
|------|---------|-------|
| 2x Lomo vetado | 2 × $18.900 | $37.800 |
| 1x Ensalada cesar | 1 × $7.500 | $7.500 |
| 3x Pisco sour | 3 × $6.900 | $20.700 |
| 1x Postre brownie | 1 × $5.800 | $5.800 |
| 1x Agua mineral | 1 × $3.200 | $3.200 |
| **SUMA REAL** | | **$75.000** |

El recibo tiene un **error de $2.000** en el subtotal (falta incluir el agua mineral o similar).