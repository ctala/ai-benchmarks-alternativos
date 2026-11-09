# Cómo se factura aquí

- Precios en **dólares (USD)**, netos. IVA 19% sobre el neto.
- Los clientes `fee_fijo` se facturan por su **fee mensual**, independiente de las horas
  registradas. Las horas se registran igual, para control interno.
- Los `por_hora` se facturan **horas × tarifa**.
- **Contrato vigente.** Solo se factura a un cliente cuyo contrato esté vigente en el mes que
  se cierra (`contrato_hasta` en `clientes.csv`). Si un cliente sin contrato vigente tiene
  horas registradas, esas horas no se facturan y el caso va a observaciones para que el
  dueño decida.
- **Tope mensual.** Si un contrato tiene tope de horas, lo que lo exceda no se factura sin
  autorización escrita del cliente: se factura hasta el tope y el exceso va a observaciones.
- **Registros dudosos.** Si el registro de horas trae una línea que podría estar repetida
  (misma fecha, cliente, horas y detalle), con estos archivos no hay forma de confirmar si
  fueron una o dos sesiones. Puedes facturarla o no, pero en los dos casos la dejas en
  observaciones para que el dueño la confirme.
- El total neto es la suma de los netos de las facturas que emites.
