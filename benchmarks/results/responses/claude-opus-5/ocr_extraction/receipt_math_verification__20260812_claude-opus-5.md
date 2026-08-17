# Claude Opus 5 — ocr_extraction/receipt_math_verification

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.16 | quality: 10.0
- latency_total: 16.718s | tokens_per_second: 88.5
- input_tokens: 462 | output_tokens: 1479

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
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    {
      "tipo": "subtotal_incorrecto",
      "detalle": "La suma de los items es $75.000 (37.800 + 7.500 + 20.700 + 5.800 + 3.200), pero el recibo indica $73.000.",
      "diferencia": -2000,
      "observacion": "El subtotal facturado esta $2.000 POR DEBAJO de la suma real de los items (a favor del cliente)."
    },
    {
      "tipo": "propina_derivada_de_base_erronea",
      "detalle": "La propina de $7.300 es exactamente el 10% del subtotal facturado ($73.000), por lo que el calculo interno es consistente. Sin embargo, sobre el subtotal correcto ($75.000) la propina del 10% deberia ser $7.500.",
      "diferencia": -200
    },
    {
      "tipo": "total_incorrecto",
      "detalle": "El total facturado ($80.300) es aritmeticamente consistente con subtotal + propina del recibo (73.000 + 7.300), pero al arrastrar el error del subtotal el total correcto seria $82.500 (75.000 + 7.500).",
      "total_facturado": 80300,
      "total_calculado": 82500,
      "diferencia": -2200
    }
  ],
  "resumen": {
    "conclusion": "Hay un error en el subtotal: faltan $2.000 respecto a la suma de los items. Ese error se arrastra a la propina (-$200) y al total (-$2.200). El error favorece al cliente.",
    "valores_correctos": {
      "subtotal": 75000,
      "propina_10_por_ciento": 7500,
      "total": 82500
    }
  }
}
```