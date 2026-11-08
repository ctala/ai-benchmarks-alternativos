# Mistral Large 3 675B — ocr_extraction/receipt_math_verification

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 8.17 | quality: 8.75
- latency_total: 5.452s | tokens_per_second: 137.9
- input_tokens: 371 | output_tokens: 752

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

Aquí está la respuesta en formato JSON con el análisis del recibo:

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
    "El subtotal facturado ($73.000) no coincide con la suma de los items ($75.000). La diferencia es de $2.000",
    "La propina sugerida debería ser $7.500 (10% de $75.000), pero está calculada como $7.300",
    "El total debería ser $82.500 ($75.000 + $7.500), pero está facturado como $80.300"
  ]
}
```

**Explicación de los cálculos:**
1. **Subtotal calculado:**
   - 2 × Lomo vetado: 2 × 18.900 = 37.800
   - 1 × Ensalada cesar: 7.500
   - 3 × Pisco sour: 3 × 6.900 = 20.700
   - 1 × Postre brownie: 5.800
   - 1 × Agua mineral: 3.200
   - **Total:** 37.800 + 7.500 + 20.700 + 5.800 + 3.200 = **75.000**

2. **Propina:**
   - 10% de 75.000 = 7.500 (no 7.300).

3. **Total:**
   - 75.000 + 7.500 = 82.500 (no 80.300).

**Conclusión:** Hay errores en el subtotal, la propina y el total. La diferencia en el subtotal es de $2.000, lo que afecta los cálculos posteriores.