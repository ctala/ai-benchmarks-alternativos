# MiMo V2.6 Flash — ocr_extraction/receipt_math_verification

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 8.15 | quality: 8.75
- latency_total: 17.444s | tokens_per_second: 34.0
- input_tokens: 355 | output_tokens: 593

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
    {"item": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900, "total": 37800},
    {"item": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500, "total": 7500},
    {"item": "Pisco sour", "cantidad": 3, "precio_unitario": 6900, "total": 20700},
    {"item": "Postre brownie", "cantidad": 1, "precio_unitario": 5800, "total": 5800},
    {"item": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200, "total": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma real de los items ($75.000). Hay una diferencia de $2.000 a favor del restaurante.",
    "La propina del 10% fue calculada sobre el subtotal incorrecto ($73.000 → $7.300), pero debería ser sobre el subtotal real ($75.000 → $7.500).",
    "El total facturado ($80.300) es incorrecto; el correcto sería $75.000 + $7.500 = $82.500. Hay una diferencia de $2.200."
  ]
}
```

**Resumen del análisis:**

| Concepto | Facturado | Calculado | ¿Correcto? |
|---|---|---|---|
| Subtotal | $73.000 | **$75.000** | ❌ |
| Propina (10%) | $7.300 | **$7.500** | ❌ |
| Total | $80.300 | **$82.500** | ❌ |

> ⚠️ **Se encontró un error de $2.000 en el subtotal**, lo que arrastra errores en la propina y el total. El restaurante cobró **$2.200 menos** de lo que corresponde según los precios listados.