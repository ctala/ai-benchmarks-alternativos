# Claude Opus 5 Fast — ocr_extraction/receipt_math_verification

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.59 | quality: 8.75
- latency_total: 4.263s | tokens_per_second: 232.9
- input_tokens: 462 | output_tokens: 993

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
    "El subtotal facturado ($73.000) es $2.000 menor que la suma real de los items ($75.000). Detalle: 37.800 + 7.500 + 20.700 + 5.800 + 3.200 = 75.000.",
    "La propina del 10% está calculada sobre el subtotal erróneo: $7.300 corresponde al 10% de $73.000. Sobre el subtotal correcto ($75.000) debería ser $7.500.",
    "El total facturado ($80.300) es internamente consistente con las cifras impresas (73.000 + 7.300), pero el total correcto sería $82.500 (75.000 + 7.500). Diferencia a favor del cliente: $2.200."
  ],
  "resumen": {
    "total_facturado": 80300,
    "total_calculado": 82500,
    "diferencia": 2200,
    "beneficiado": "cliente"
  }
}
```