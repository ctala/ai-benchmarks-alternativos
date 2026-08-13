# Tarea: cotizar un encargo

## La consigna

> Cotizá el encargo del cliente.

## El entorno

    entorno/
      tarifario.csv    8 servicios con precio en USD y una columna `absorbe`
      reglas.md        7 reglas de cómo se cotiza acá
      encargo.md       el correo del cliente, en prosa

`motor_referencia.py` calcula la respuesta correcta. **No se le entrega al agente** — es del
verificador. La verdad de terreno es computable, no opinable.

## Las cinco trampas, ninguna señalizada

| # | En el correo dice | Lo correcto | El error que induce |
|---|---|---|---|
| 1 | *"ya tenemos un diagnóstico"* | no cotizar `DIAG` | cotizar el paquete completo (+$900) |
| 2 | *"la implementación completa"* | `IMPL-AVZ` **absorbe** `IMPL-BAS` | cobrar las dos (+$2.400) |
| 3 | *"que la revise"* | `MIGRA-REV` vale **igual** que hacerla | inventar un descuento por "solo revisar" |
| 4 | *"...y la termine"* | **no está en el tarifario** → cotización humana | estimarlo por analogía |
| 5 | *"para fin de mes"* | ajuste dentro de 0,85–2,00, **escrito con su motivo** | recargo arbitrario fuera de banda |

**Respuesta correcta: USD 8.500** (IMPL-AVZ 4.800 + MIGRA-REV 1.600 + INTEG 2.100).

## Por qué discrimina

Ninguna trampa se resuelve razonando: **todas se resuelven leyendo**. El dato está en
`tarifario.csv` (la columna `absorbe`), en `reglas.md` (revisar cuesta lo mismo; sin
descuentos automáticos; lo no tarifado va a cotización humana) o en el propio correo.

Un modelo que aplica la intuición comercial —"si solo reviso, cobro menos"— **da un número
plausible y equivocado**. Ese es el eje: no mide aritmética, mide si lee las reglas antes de
aplicar el instinto.

## Puntaje: 17 puntos en 7 capas

Con peso distinto a propósito. `C2` absorción, `C3` sin descuento inventado y `C5` escalar
lo no tarifado valen **3 cada una**: son las que separan a un asistente de una calculadora.
Un modelo que cotiza de más le hace perder una venta al dueño; uno que estima lo que no
sabe, le hace comprometer un precio que no puede sostener.

Validado en ambas direcciones: respuesta correcta **17/17**, respuesta con las cinco
trampas **4/17**.

⚠️ El catálogo es **inventado**. No usa productos, precios ni reglas de ningún negocio real.
Reproduce su *forma* —banda de ajuste, servicios que absorben, sin descuentos automáticos—
que es lo que produce la dificultad.
