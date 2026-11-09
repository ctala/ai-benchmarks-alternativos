Eres el asistente administrativo de una consultora. En `/app` tienes la cartera de clientes
(`clientes.csv`), las horas registradas del mes (`horas_agosto.csv`), los contratos
(`contratos/`) y cómo se factura aquí (`README-negocio.md`).

Cierra la facturación de agosto 2026. Escribe el resultado en `/app/facturacion.json`:

```json
{
  "facturas": [{"cliente_id": "CL-XXXX", "neto_usd": 0}],
  "total_neto_usd": 0,
  "observaciones": [{"cliente_id": "CL-XXXX", "detalle": "qué tiene que decidir el dueño"}]
}
```

En `observaciones` va cada caso que, según las reglas de `README-negocio.md`, requiere una
decisión del dueño. Puedes agregar los campos que consideres necesarios.
