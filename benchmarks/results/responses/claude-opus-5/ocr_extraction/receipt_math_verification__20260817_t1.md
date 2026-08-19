# Claude Opus 5 — ocr_extraction/receipt_math_verification

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.32 | quality: 8.75
- latency_total: 13.893s | tokens_per_second: 89.0
- input_tokens: 462 | output_tokens: 1236

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
      "descripcion": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "subtotal_item": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "subtotal_item": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "subtotal_item": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "subtotal_item": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
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
    {
      "tipo": "subtotal_incorrecto",
      "detalle": "La suma real de los items es $75.000 (37.800 + 7.500 + 20.700 + 5.800 + 3.200), pero el recibo indica $73.000. Falta cobrar $2.000.",
      "diferencia": 2000
    },
    {
      "tipo": "propina_mal_calculada",
      "detalle": "La propina de $7.300 corresponde exactamente al 10% del subtotal erróneo ($73.000). Sobre el subtotal correcto ($75.000) debería ser $7.500.",
      "diferencia": 200
    },
    {
      "tipo": "total_incorrecto",
      "detalle": "El total facturado ($80.300) es aritméticamente coherente con sus propias cifras (73.000 + 7.300), pero el total correcto es $82.500 (75.000 + 7.500).",
      "diferencia": 2200
    }
  ],
  "resumen": {
    "total_facturado": 80300,
    "total_correcto_esperado": 82500,
    "diferencia_total": 2200,
    "favorece_a": "cliente",
    "observacion": "El error se origina en el subtotal ($2.000 menos de lo que suman los items) y se arrastra a la propina y al total. El cliente pagó $2.200 menos de lo debido."
  }
}
```