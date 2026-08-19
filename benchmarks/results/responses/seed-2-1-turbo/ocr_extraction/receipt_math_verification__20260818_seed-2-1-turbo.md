# Seed 2.1 Turbo — ocr_extraction/receipt_math_verification

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 4.17 | quality: 3.75
- latency_total: 33.639s | tokens_per_second: 60.9
- input_tokens: 424 | output_tokens: 2048

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


El usuario quiere que procese el recibo del restaurante, Verification and JSON output are what I will complete. I have finished extracting all items from the restaurant receipt and their corresponding amounts. The calculated subtotal is 75,000, which is inconsistent with the 73,000 subtotal marked on the receipt. I am now checking whether the 10% service charge marked on the receipt is calculated correctly. I've confirmed that the 10% service charge marked on the receipt is calculated correctly based on the subtotal shown on the document. However, the previously calculated correct subtotal of 75,000 is indeed inconsistent with the 73,000 subtotal billed, so the billed subtotal is confirmed to be incorrect.

I've clarified the tipping calculation rule specified on the receipt: the 10% service charge is computed based on the subtotal declared by the restaurant, so the recorded 7,300 peso tip is accurate according to the store's stated calculation standard.

The 10% service charge is calculated correctly per the receipt's stated rule, so the billed total of 80,300 matches the sum of the billed subtotal and service charge. However, since the billed subtotal is wrong, the total is also incorrect. I have confirmed the output JSON will include a breakdown of all items with their name, quantity, unit price and item subtotal, plus the billed subtotal, calculated subtotal, and a false flag for the subtotal's correctness. I will also note the service charge meets the receipt's stated rule but is too low since the underlying subtotal is wrong.

I rechecked the task requirements and confirmed that the 10% service charge marked on the receipt is indeed calculated correctly based on the subtotal declared by the restaurant.

The tip should be 7,500 based on the actual correct subtotal. I'm now figuring out how to set the tip_correct field to meet the task requirements.
