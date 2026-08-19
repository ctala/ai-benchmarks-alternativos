# Claude Sonnet 5 — business_strategy/elegir_negocio_con_dependencia_oculta

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.36 | quality: 10.0
- latency_total: 19.093s | tokens_per_second: 67.5
- input_tokens: 511 | output_tokens: 1289

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

# Opción C. Sin duda, y no es ni cercano.

Vamos a hacer la matemática de supervivencia, no la de potencial:

## Por qué A y B están descartadas para ESTE trimestre (no para siempre)

**Opción A** tiene un ciclo de venta de 5-7 meses. Vos tenés 3 meses de caja. Aunque cerraras el trato hoy, cobrarías después de haberte quedado sin plata. Además necesitás 6 semanas de construcción de producto ANTES de poder vender. Es una opción excelente... para dentro de 6 meses, financiada con la caja que generes ahora. Metela en el roadmap, no en el sprint de supervivencia.

**Opción B** tiene una dependencia circular fatal: necesitás 3 casos de éxito para vender, y hoy tenés 0. ¿De dónde salen esos casos de éxito? De clientes. ¿Cómo conseguís clientes sin casos de éxito? No podés. Esta opción requiere que primero resuelvas OTRA cosa (probablemente con la Opción C o proyectos ad-hoc) para generar los casos. No es ejecutable en aislamiento en 3 meses.

## Por qué C es la única jugada racional

1. **Cero tiempo de construcción.** Tu producto ya existe: es tu medio y tu audiencia.
2. **Cero ciclo de venta.** Ya no tenés que prospectar ni convencer a nadie de que el problema existe. Tenés demanda entrante *inbound* sin trabajar: dos marcas ya te preguntaron precios.
3. **Ciclo de cobro:** días, no meses. Contenido patrocinado se negocia y se cobra rápido.
4. **Encaja con tu capacidad real:** 4 horas al día es exactamente el tipo de disponibilidad para producir 1-2 piezas patrocinadas por semana, no para sostener un ciclo de venta B2B enterprise en paralelo a construir producto.

## El error que estás cometiendo ahora mismo

Dejaste sin responder a dos marcas que te pidieron precios. Eso no es "una opción para evaluar", es un ingreso que dejaste sobre la mesa el mes pasado por estar mirando el tamaño de mercado de A. El tamaño del mercado de C es irrelevante si podés facturar $800-1600 esta semana con dos correos.

## Plan concreto para los 3 meses

- **Semana 1:** Respondé a esas dos marcas. Cerrá 1-2 piezas. Esto te da oxígeno inmediato y valida precio/demanda real.
- **Semanas 2-8:** Sistematizá la venta de contenido patrocinado (media kit, tarifario, proceso de originación de nuevas marcas). Objetivo: ingreso recurrente mensual que cubra tu burn rate.
- **En paralelo (si sobran horas):** Cada pieza patrocinada que hagas para una marca que use herramientas/tecnología es candidata a transformarse en un caso de éxito documentado para la Opción B. Estás matando dos pájaros: generás cash flow con C mientras construís, sin costo adicional, los insumos para B.
- **Después del mes 3:** Con caja estabilizada por C, recién ahí evaluás si invertís las 6 semanas de construcción para A, financiado por ingresos reales y no por ansiedad de colchón.

**La regla que estás violando al considerar A y B como iguales a C:** el tamaño del mercado no paga el alquiler este trimestre. La velocidad de cobro sí.