# Claude Sonnet 5 (suscripción) — ocr_extraction/receipt_math_verification

- model_id: `claude-sonnet-5`
- success: True  | final: 8.38 | quality: 10.0
- latency_total: 22.597s | tokens_per_second: 57.0
- input_tokens: 2 | output_tokens: 1288

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
  "propina_correcta": true,
  "total_correcto": true,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma real de los items ($75.000). Diferencia de $2.000 a favor del restaurante.",
    "La propina (10% = $7.300) está bien calculada, pero sobre el subtotal facturado incorrecto ($73.000). Si se calcula sobre el subtotal real ($75.000), debería ser $7.500.",
    "El TOTAL ($80.300) es matemáticamente consistente con subtotal_facturado + propina_facturada, pero arrastra el error del subtotal. El total correcto debería ser $82.500 ($75.000 + $7.500 de propina 10%)."
  ]
}
```

**Resumen:** el recibo tiene un error de $2.000 en el subtotal (está subfacturado respecto a la suma real de los items), lo que hace que tanto la propina como el total final también queden $2.200 por debajo de lo que correspondería. Vale la pena pedir revisión antes de pagar.