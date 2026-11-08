# Tencent Hy4 — business_strategy/elegir_negocio_con_dependencia_oculta

- model_id: `tencent/hy4`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 49.532s | tokens_per_second: 79.7
- input_tokens: 365 | output_tokens: 3950

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres asesor de fundadores. Eliges por lo que se puede EJECUTAR con los activos actuales, no por el tamaño del mercado en una diapositiva.

**user:**

Tengo que elegir en qué me enfoco los próximos 3 meses. Soy uno solo, 4 horas al día, y necesito ingresos ANTES de que se me acabe el colchón (me quedan 3 meses de caja).

OPCIÓN A — Vender datos vía API a empresas.
  Mercado: enorme. Ticket: $500-2.000/mes por cliente.
  Requisito: contratos B2B con empresas. Mi ciclo de venta B2B histórico es de 5 a 7 meses desde el primer contacto hasta el cobro.
  Producto: habría que construirlo (~6 semanas).

OPCIÓN B — Marca blanca de mi tecnología para agencias.
  Mercado: mediano. Ticket: $300/mes.
  Requisito: necesito 3 casos de éxito documentados para que alguien me compre. Hoy tengo 0.

OPCIÓN C — Contenido patrocinado en el medio que ya opero.
  Mercado: chico. Ticket: $400-800 por pieza.
  Requisito: ya tengo el tráfico y la audiencia. Ya me escribieron 2 marcas preguntando precios el mes pasado (no les respondí).
  Producto: no hay que construir nada.

¿Cuál agarro? Justifica.


## Respuesta completa

**Agarrá la C. Y no es una decisión de mercado, es una decisión de calendario.**

Tu restricción no es "¿dónde hay más plata?", es **"¿qué puedo cobrar antes de que en el día 90 la cuenta llegue a cero?"**. Con 4 h/día y una sola persona, el TAM es ruido. Lo único que importa es el *time-to-cash* y cuántos activos del camino ya están pagos.

### Por qué A y B quedan afuera (no es pesimismo, es aritmética)

| | Activos que ya tenés | Trabajo nuevo | Primer cobro | ¿Entra en 90 días? |
|---|---|---|---|---|
| **A** — API | Ninguno cerrado | 6 semanas de build + ciclo 5–7 meses | **6,5 a 8,5 meses** | **No. Imposible por calendario.** |
| **B** — Marca blanca | 0 casos de éxito | 3 pilotos → documentar → recién ahí vender | 2–3 meses *si todo sale bien* | Circular: necesitás clientes para conseguir clientes |
| **C** — Patrocinios | Tráfico, audiencia, formato, **2 marcas que ya preguntaron precio** | Responder 2 emails | **3 a 14 días** | **Sí** |

La A te está seduciendo con la palabra "enorme". Pero tu propio dato histórico la mata: **5–7 meses desde el primer contacto hasta el cobro**, y el colchón es de 3. Aunque el producto estuviera terminado hoy, seguirías fuera de ventana. Y encima te comería 6 semanas de tus 4 h/día construyendo algo que no factura. Es la opción más cara en horas y la única con fecha de cobro conocida *posterior* a tu quiebra.

La B es peor: es la A con menos ticket, menos mercado y un prerrequisito extra. El huevo y la gallina de los 3 casos se rompe haciendo trabajo gratis, y "gratis" es un lujo que no tenés con 90 días de caja.

### Lo que estás subestimando de la C

No es "tengo un medio". Es: **dos marcas te escribieron pidiendo precios el mes pasado y no les contestaste.** Eso es demanda entrante con intención de compra ya expresada, sin prospección, sin ciclo de venta, sin producto, sin contrato B2B, sin procurement, sin legal. Es el activo más caliente de las tres opciones y lo tenías en la bandeja de entrada sin abrir.

Además, vender una pieza patrocinada **no es una venta B2B de 5–7 meses**: es inventario editorial contra un presupuesto de marketing que ya existe. Se decide en días. Tu ciclo histórico de la A no aplica acá, y confundirlos es el error que te hace dudar.

### Plan de los 90 días (con tus 4 h/día)

**Próximas 48 h — lo único urgente:**
- Respondé hoy a las 2 marcas. No con "te armo algo en unos días": con **un precio cerrado, un formato, una fecha de publicación y cobro por adelantado** (o 50% al confirmar). Con 3 meses de caja no financiás al cliente.
- Un solo SKU. Ej.: "$600 · 1 pieza · se publica el jueves · incluye newsletter + 1 post". Nada de presupuestos a medida: customizar te devora las 4 horas.
- Si una se enfrió, pedí la fecha de su próximo ciclo de presupuesto y seguí. Costo: 10 minutos.

**Mes 1:** cerrar esas 2, publicar, **cobrar**. Objetivo: 2–4 piezas. Con lo que facturás armás una lista de 20–30 marcas del mismo perfil y les escribís 30 min/día. No estás "haciendo ventas B2B", estás ofreciendo un espacio ya disponible.

**Meses 2–3:** repetir, y si se te agota el inventario **subí el precio** antes de buscar más clientes (el techo del "mercado chico" se testea con precio, no con una diapositiva). Empaquetá 2–3 piezas/mes como plan para volver recurrente lo que hoy es puntual, sin cambiar de modelo.

### El bonus que hace que no estés renunciando a nada

C te da, gratis, lo que le falta a las otras dos:

- Cada patrocinio publicado = **1 métrica + 1 frase del anunciante**. En 6 semanas tenés los **3 casos de éxito que hoy le faltan a la B**.
- La caja de C es la que **financia las 6 semanas de build de la A** sin angustia, en el mes 4 o 5, ya con la cuenta respirando.

O sea: A y B no se descartan, **se posponen y se preparan con los subproductos de C**. Elegir C no es elegir el mercado chico para siempre; es elegir el único punto de entrada que tenés hoy.

### Regla de disciplina para que no te desvíes

1. **Prohibido abrir el editor para la API en estos 90 días.** La A se anota en el mes 4, con fecha y con plata de C encima.
2. **Prohibido "armar casos de éxito" como proyecto separado.** Salen solos de publicar.
3. **Una sola métrica semanal: euros cobrados.** No facturados, no reuniones, no "contactos calientes", no líneas de código. Cobrados.

Si con C a fin del mes 1 no cubrís el burn, la respuesta es recortar burn / pedir adelantos a los patrocinadores — **no saltar a la A**. Saltar a la A sería cambiar un problema de caja por un problema de caja *más 6 semanas de trabajo no pagado*.

**Resumen:** agarrá la C porque es la única donde el cuello de botella ya está resuelto. Las otras dos te piden que construyas el camino antes de cobrar, y vos no tenés camino: tenés 90 días.