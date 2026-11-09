Eres el asistente de una consultora. En `/app` tienes el tarifario (`tarifario.csv`), las
reglas de cotización (`reglas.md`) y el encargo de un cliente (`encargo.md`).

Cotiza el encargo y escribe el resultado en `/app/cotizacion.json` con esta forma:

```json
{
  "lineas": [{"sku": "XXX", "precio_referencia": 0, "factor": 1.0, "total": 0}],
  "total_usd": 0
}
```

En `lineas` va solamente lo que se cobra. Puedes agregar los campos que consideres
necesarios.
