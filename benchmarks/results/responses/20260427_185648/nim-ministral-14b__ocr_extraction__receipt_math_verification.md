# Ministral 14B (NIM) — ocr_extraction/receipt_math_verification

- model_id: `mistralai/ministral-14b-instruct-2512`
- success: True  | final: 6.74 | quality: 7.55
- latency_total: 38.357s | tokens_per_second: 23.9
- input_tokens: 371 | output_tokens: 917
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900
    },
    {
      "nombre": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500
    },
    {
      "nombre": "Pisco sour",
      "cantidad": 3,
      "precio_unitario": 6900
    },
    {
      "nombre": "Postre brownie",
      "cantidad": 1,
      "precio_unitario": 5800
    },
    {
      "nombre": "Agua mineral 1.5L",
      "cantidad": 1,
      "precio_unitario": 3200
    }
  ],
  "subtotal_facturado": 73000,
  "subtotal_calculado": 68800,
  "subtotal_correcto": false,
  "propina_correcta": false,
  "total_correcto": false,
  "errores": [
    {
      "descripcion": "El subtotal facturado ($73.000) no coincide con la suma de los items ($68.800).",
      "diferencia": -4200,
      "items_corregidos": [
        {
          "nombre": "Lomo vetado",
          "precio_correcto": 18800,
          "observacion": "El precio unitario debería ser $18.800 (2x $18.800 = $37.600) en lugar de $18.900 para ajustar el subtotal"
        }
      ]
    },
    {
      "descripcion": "La propina sugerida de $7.300 esta calculada incorrectamente sobre el subtotal facturado ($73.000).",
      "propina_correcta": 6880,
      "calculo_correcto": "10% de $68.800 = $6.880 (redondeado a $6.880)"
    },
    {
      "descripcion": "El total facturado ($80.300) no coincide con el cálculo correcto ($68.800 + $6.880 = $75.680)."
    }
  ]
}
```

### Explicación de los errores:

1. **Subtotal incorrecto**:
   - La suma real de los items es **$68.800** (en lugar de $73.000).
   - El error proviene de que el precio del **Lomo vetado** debería ser **$18.800** por unidad (no $18.900) para que el subtotal sea correcto.

2. **Propina mal calculada**:
   - Se aplicó el 10% sobre el subtotal incorrecto ($73.000), obteniendo $7.300.
   - El cálculo correcto sería **10% de $68.800 = $6.880** (redondeado a $6.880).

3. **Total incorrecto**:
   - El total facturado ($80.300) no coincide con el cálculo real ($68.800 + $6.880 = $75.680).

---
**Nota**: Si se asume que el precio del **Lomo vetado** está mal escrito (sin redondeo), el error podría deberse a que el precio real es **$18.900**, pero entonces el subtotal sería **$69.500** ($37.800 + $7.500 + $20.700 + $5.800 + $3.200). En ese caso, ningún cálculo sería correcto, pero el formato JSON anterior sigue el procedimiento lógico según los datos dados. ¿Te gustaría ajustar alguna premisa?