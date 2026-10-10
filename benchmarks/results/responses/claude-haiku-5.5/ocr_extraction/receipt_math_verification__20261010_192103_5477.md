# Claude Haiku 5.5 — ocr_extraction/receipt_math_verification

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.28 | quality: 8.75
- latency_total: 6.135s | tokens_per_second: 228.2
- input_tokens: 464 | output_tokens: 1400

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
    {"descripcion": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900, "total": 37800},
    {"descripcion": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500, "total": 7500},
    {"descripcion": "Pisco sour", "cantidad": 3, "precio_unitario": 6900, "total": 20700},
    {"descripcion": "Postre brownie", "cantidad": 1, "precio_unitario": 5800, "total": 5800},
    {"descripcion": "Agua mineral 1.5L", "cantidad": 1, "precio_unitario": 3200, "total": 3200}
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). Diferencia: $2.000 a favor del restaurante.",
    "La propina sugerida está calculada sobre el subtotal erróneo: 10% de $73.000 = $7.300. Con el subtotal real ($75.000), la propina del 10% sería $7.500 (diferencia de $200).",
    "Como consecuencia, el TOTAL ($80.300) está sobrestimado respecto del consumo real. Con los valores correctos, el total sería $82.500 ($75.000 + $7.500). Aunque la suma aritmética de la boleta es internamente consistente ($73.000 + $7.300 = $80.300), no refleja los items consumidos. Se cobró $2.000 menos en el subtotal, pero la boleta cobra un total de $80.300 frente a $82.500 esperados, lo que implica una diferencia neta de $2.200 a favor del cliente.",
    "Recomendación: solicitar una boleta corregida o revisar la cuenta con el restaurante antes de pagar la propina."
  ]
}
```