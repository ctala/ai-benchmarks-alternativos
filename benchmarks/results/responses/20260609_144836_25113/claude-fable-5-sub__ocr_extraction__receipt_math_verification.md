# Claude Fable 5 (suscripción) — ocr_extraction/receipt_math_verification

- model_id: `claude-fable-5`
- success: True  | final: 4.0 | quality: 4.12
- latency_total: 15.422s | tokens_per_second: 77.5
- input_tokens: 2 | output_tokens: 1195

## Respuesta completa

```json
{
  "items": [
    {
      "descripcion": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total_item": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total_item": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "total_item": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "total_item": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "total_item": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    "Subtotal incorrecto: la suma real de los items es $75.000 (37.800 + 7.500 + 20.700 + 5.800 + 3.200), pero la boleta indica $73.000. Diferencia de $2.000 a favor del cliente.",
    "Propina mal calculada: el 10% del subtotal real ($75.000) es $7.500, no $7.300. La propina de $7.300 es consistente con el subtotal facturado erróneo (10% de $73.000), pero arrastra el error original.",
    "Total incorrecto: el total correcto sería $82.500 ($75.000 + $7.500). La boleta cobra $80.300, es decir, $2.200 menos de lo que correspondería."
  ]
}
```

**Resumen:** la aritmética interna de la boleta es consistente (73.000 + 7.300 = 80.300), pero el error de origen está en el subtotal: los items suman $75.000, no $73.000. Eso arrastra propina y total, dejando un cobro $2.200 inferior al real.