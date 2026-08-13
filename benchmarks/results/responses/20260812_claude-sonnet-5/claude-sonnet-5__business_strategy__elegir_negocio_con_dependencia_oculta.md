# Claude Sonnet 5 — business_strategy/elegir_negocio_con_dependencia_oculta

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 29.233s | tokens_per_second: 70.1
- input_tokens: 511 | output_tokens: 2048

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

**Agarrás C. No es una decisión reñida, es la única que sobrevive al filtro real: tiempo-hasta-cobro vs. runway.**

Hagamos la cuenta de "qué falta antes de facturar" en cada una, no de cuán grande es el mercado:

**Opción A:** 6 semanas de construcción + 5-7 meses de ciclo de venta B2B = 7 a 8.5 meses mínimo antes de ver un peso. Vos tenés 3 meses de caja. Esto no es "difícil", es aritméticamente imposible como apuesta principal ahora. El tamaño del mercado y el ticket son irrelevantes si te morís antes de cobrar el primero.

**Opción B:** necesitás 3 casos de éxito documentados que hoy no existen. Conseguir un piloto, que lo use, que dé resultado, documentarlo — eso son semanas por caso, mínimo 2-3 meses para tener el *material de venta*, y ahí recién empezás a vender. Tampoco entra en la ventana.

**Opción C:** no hay que construir nada, la audiencia y el tráfico ya existen (activo ya montado), y tenés demanda inbound ya validada — dos marcas te preguntaron precio el mes pasado y no respondiste. La distancia entre "hoy" y "primer cobro" se mide en días, no en meses. Es la única opción donde el problema no es generar demanda sino no dejarla morir.

**Qué hacer, en orden:**

1. Esta semana: respondé a esas 2 marcas, armá un paquete simple ($400-800/pieza), cerrá y facturá.
2. Con el tiempo que sobra de tus 4h/día (esto no debería llevarte más de 1-1.5h diarias), prospectá 5-10 marcas del mismo perfil que las que llegaron inbound.
3