# Claude Sonnet 5.5 — ocr_extraction/receipt_math_verification

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 7.983s | tokens_per_second: 145.3
- input_tokens: 464 | output_tokens: 1160

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
    { "descripcion": "Lomo vetado",       "cantidad": 2, "precio_unitario": 18900, "total_linea": 37800 },
    { "descripcion": "Ensalada cesar",    "cantidad": 1, "precio_unitario": 7500,  "total_linea": 7500 },
    { "descripcion": "Pisco sour",        "cantidad": 3, "precio_unitario": 6900,  "total_linea": 20700 },
    { "descripcion": "Postre brownie",    "cantidad": 1, "precio_unitario": 5800,  "total_linea": 5800 },
    { "descripcion": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200,  "total_linea": 3200 }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Diferencia: $2.000 a favor del cliente.",
    "La propina de $7.300 es el 10% exacto del subtotal facturado ($73.000), pero como ese subtotal es incorrecto, la propina debería ser $7.500 (10% de $75.000).",
    "El total facturado ($80.300) es coherente con el subtotal erróneo (73.000 + 7.300), pero el total correcto sería $82.500 (75.000 + 7.500). Diferencia: $2.200."
  ],
  "valores_correctos": {
    "subtotal": 75000,
    "propina_10_pct": 7500,
    "total": 82500
  }
}
```

**Resumen:**
- La suma de los items es 37.800 + 7.500 + 20.700 + 5.800 + 3.200 = **$75.000**, no $73.000.
- La propina está bien calculada respecto al subtotal impreso, pero hereda su error.
- El total impreso es $2.200 menor que el real ($82.500).