# Claude Opus 4.7 (suscripción) — ocr_extraction/receipt_math_verification

- model_id: `claude-opus-4-7`
- success: True  | final: 6.19 | quality: 7.68
- latency_total: 20.976s | tokens_per_second: 80.1
- input_tokens: 6 | output_tokens: 1680
- judge_score: 4.6 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "descripcion": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "subtotal": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "subtotal": 7500
    },
    {
      "descripcion": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900,
      "subtotal": 20700
    },
    {
      "descripcion": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800,
      "subtotal": 5800
    },
    {
      "descripcion": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200,
      "subtotal": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 75000,
  "subtotal_correcto": false,
  "propina_correcta": true,
  "total_correcto": false,
  "errores": [
    "El subtotal facturado ($73.000) NO coincide con la suma real de los items ($75.000). Hay una diferencia de $2.000 a favor del cliente (subfacturación).",
    "La propina del 10% está bien calculada SOBRE el subtotal facturado ($73.000 × 0,10 = $7.300), pero si el subtotal estuviera correcto ($75.000) la propina debería ser $7.500.",
    "El total facturado ($80.300 = $73.000 + $7.300) es internamente consistente con el subtotal mostrado, pero el total real correcto debería ser $82.500 ($75.000 + $7.500).",
    "Diferencia total a favor del cliente: $2.200 (el restaurante está cobrando $2.200 menos de lo que corresponde)."
  ]
}
```

**Resumen del análisis:**

| Concepto | Facturado | Calculado | Diferencia |
|---|---|---|---|
| Subtotal | $73.000 | $75.000 | -$2.000 |
| Propina (10%) | $7.300 | $7.500 | -$200 |
| **Total** | **$80.300** | **$82.500** | **-$2.200** |

El error está en la suma del subtotal: 37.800 + 7.500 + 20.700 + 5.800 + 3.200 = **$75.000**, no $73.000. Probablemente olvidaron sumar uno de los pisco sour ($6.900) y el ítem más cercano ($2.000 de diferencia no calza exacto con ningún ítem, así que parece error aritmético manual del mesero/sistema, no un ítem omitido).