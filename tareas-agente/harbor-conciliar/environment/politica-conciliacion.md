# Política de conciliación bancaria — Imprenta Cordillera SpA

Esta política la aplica cualquiera que concilie la cuenta corriente contra las facturas
emitidas. **Se cumplen todas las reglas.**

## Archivos

- `facturas.csv`: facturas emitidas. `monto` está en la `moneda` de la factura (CLP o USD).
- `cartola.csv`: movimientos de la cuenta corriente en CLP. Positivo = abono (entra plata);
  negativo = cargo (sale plata). `rut_contraparte` es el RUT de quien transfirió.
- `clientes.csv`: clientes. Si `rut_matriz` tiene un RUT, esa empresa es filial de la que
  tiene ese RUT y ambas forman un **grupo relacionado**.
- `tipo_cambio.csv`: dólar observado por fecha (CLP por 1 USD).

## Reglas

1. **Un abono se asocia a una factura solo si se cumplen las dos condiciones:**
   a. la `descripcion` del movimiento cita el folio de la factura (`F-` y cuatro dígitos), y
   b. `rut_contraparte` es el RUT del cliente de la factura **o** el de una empresa de su
      grupo relacionado según `clientes.csv`.
   Que el monto coincida con el de una factura **no basta**. Un abono que no cumple las dos
   condiciones no se aplica a ninguna factura.
2. **Un abono que cita varios folios** se aplica a esas facturas en orden de
   `fecha_emision`, de la más antigua a la más reciente, sin importar el orden en que
   aparecen en la descripción: se salda por completo cada factura antes de pasar a la
   siguiente.
3. **Facturas en USD pagadas en CLP:** el abono se convierte a USD con el dólar observado
   **de la fecha del abono** (no el de la emisión). Si esa fecha no tiene valor en
   `tipo_cambio.csv` (fin de semana o feriado), se usa el del último día **anterior** que
   sí lo tenga.
4. **Los cargos (montos negativos) nunca son pagos de clientes,** aunque su descripción
   cite un folio: no modifican el saldo de ninguna factura.
5. **Saldo** = monto de la factura − lo abonado, en la moneda de la factura, redondeado a 2
   decimales. Si el saldo queda entre −1 y 1 (redondeo), la factura está pagada y su
   saldo es 0.
6. **Estado:** `pagada` si el saldo es 0; `parcial` si recibió algún abono y el saldo es
   mayor que 0; `pendiente` si no recibió ningún abono.
7. **Todo movimiento de la cartola que no se aplicó a ninguna factura** (cargos incluidos)
   va a la lista de no conciliados, con un motivo breve, para que lo revise contabilidad.
