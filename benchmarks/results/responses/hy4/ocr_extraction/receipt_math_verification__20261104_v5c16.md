# Tencent Hy4 — ocr_extraction/receipt_math_verification

- model_id: `tencent/hy4`
- success: True  | final: 8.96 | quality: 10.0
- latency_total: 7.029s | tokens_per_second: 92.5
- input_tokens: 368 | output_tokens: 650

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
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) no coincide con la suma real de los ítems ($75.000). Diferencia: +$2.000 de menos en la boleta.",
    "La propina sugerida ($7.300) está bien calculada pero sobre el subtotal FACTURADO (10% de $73.000), no sobre el subtotal real. Si se calcula sobre el real debería ser $7.500.",
    "El TOTAL facturado ($80.300) es consecuencia del subtotal erróneo. El total correcto sería $82.500 (subtotal real $75.000 + propina 10% $7.500) o $80.500 si se mantiene la propina de $7.300 sobre el subtotal real.",
    "Detalle de la diferencia: 2×18.900=37.800 | +7.500=45.300 | +3×6.900=20.700 → 66.000 | +5.800=71.800 | +3.200=75.000 (la boleta dice 73.000)."
  ]
}
```

**Resumen rápido:** Hay un error de **$2.000 en el subtotal** (probablemente se omitió o redondeó mal el agua mineral o el brownie). La propina es matemáticamente correcta respecto al número impreso, pero el **total final está mal** porque arrastra el subtotal equivocado. ✅ Mesero Carlos, mesa 7, pago tarjeta ****4521 sin observaciones.