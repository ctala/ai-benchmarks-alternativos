Sos el asistente de una consultora. En `/app` tenés el tarifario (`tarifario.csv`), las
reglas de cotización (`reglas.md`) y el encargo de un cliente (`encargo.md`).

Cotizá el encargo y escribí el resultado en `/app/cotizacion.json` con esta forma:

```json
{
  "lineas": [{"sku": "XXX", "precio_referencia": 0, "factor": 1.0, "total": 0}],
  "total_usd": 0
}
```

En `lineas` va solamente lo que se cobra. Podés agregar los campos que consideres
necesarios.
