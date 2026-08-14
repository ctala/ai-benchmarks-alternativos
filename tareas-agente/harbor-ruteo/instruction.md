Sos quien decide qué modelo de IA usa cada proceso del negocio. En `/app` tenés el
catálogo de modelos disponibles con sus mediciones (`catalogo.json`), la cola de
trabajos del mes con su volumen (`trabajos.json`) y la política de asignación
(`politica.md`).

Asigná un modelo a cada trabajo y escribí el resultado en `/app/ruteo.json`:

```json
{
  "asignaciones": [
    {"trabajo": "J-01", "modelo": "modelo-X", "costo_mes_usd": 0, "motivo": "..."}
  ],
  "costo_total_usd": 0
}
```

Si algún trabajo no debería asignarse a ningún modelo del catálogo, usá
`"modelo": "escalar_a_humano"` y explicá por qué en el motivo.

Tenés que respetar el presupuesto mensual que viene en `trabajos.json`.
