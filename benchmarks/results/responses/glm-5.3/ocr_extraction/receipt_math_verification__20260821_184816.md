# GLM 5.3 — ocr_extraction/receipt_math_verification

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.38 | quality: 10.0
- latency_total: 30.328s | tokens_per_second: 90.7
- input_tokens: 325 | output_tokens: 2752

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
      "total_linea": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total_linea": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total_linea": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total_linea": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total_linea": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": true,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000): falta $2.000 (diferencia a favor del cliente).",
    "La propina ($7.300) es aritmeticamente correcta como 10% del subtotal facturado, pero esta calculada sobre un subtotal erroneo. Con el subtotal real de $75.000, la propina deberia ser $7.500.",
    "El total ($80.300) es correcto como suma de subtotal facturado + propina, pero hereda el error del subtotal. Con los valores correctos, el total deberia ser $82.500."
  ]
}
```

**Resumen:** El único error de origen está en el **subtotal**: la suma real de los ítems es **$75.000**, no $73.000 (diferencia de $2.000, aparentemente un cobro menor que beneficia al cliente). La propina y el total están bien calculados aritméticamente, pero sobre esa base incorrecta.