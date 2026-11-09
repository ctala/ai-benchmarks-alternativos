Eres el asistente de administración y finanzas de Imprenta Cordillera SpA. En `/app` tienes
la cartola bancaria de octubre 2026 (`cartola.csv`), las facturas emitidas
(`facturas.csv`), la cartera de clientes (`clientes.csv`), el dólar observado
(`tipo_cambio.csv`) y la política de conciliación (`politica-conciliacion.md`), que se
cumple completa.

Concilia la cartola contra las facturas y escribe el resultado en `/app/conciliacion.json`
con este esquema:

```json
{
  "facturas": [
    {"folio": "F-0000", "estado": "pagada | parcial | pendiente", "saldo": 0, "moneda": "CLP | USD"}
  ],
  "no_conciliados": [
    {"id_mov": "M-00", "motivo": "texto breve"}
  ]
}
```

- `facturas` lleva **una entrada por cada factura** de `facturas.csv`; `saldo` va en la
  moneda de la factura, como número.
- `no_conciliados` lleva cada movimiento de la cartola que no aplicaste a ninguna factura.
