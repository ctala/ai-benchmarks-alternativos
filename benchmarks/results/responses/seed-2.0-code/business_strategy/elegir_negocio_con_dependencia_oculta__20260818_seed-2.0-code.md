# Seed 2.0 Code — business_strategy/elegir_negocio_con_dependencia_oculta

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 39.078s | tokens_per_second: 52.4
- input_tokens: 377 | output_tokens: 2048

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


El usuario tiene que elegir entre 3 opciones, con restricciones MUY claras: 3 meses de caja, solo, 4h/día, ingresos ANTES de que se acabe. Primero, voy a alinear cada opción con sus restricciones, no con el mercado o el ticket a largo plazo.

Primero, listo las RESTRICCIONES IRRENUNCIABLES que él puso:
1. Plazo MÁXIMO 3 meses (caja se acaba entonces) → INGRESOS EFECTIVOS (no promesas, no contratos pendientes de cobro) antes de 90 días.
2. Recursos: 1 persona, 4h/día → NO proyectos que requieran 6 semanas de construcción sin ingresos paralelos, ni ciclos de venta largos.
3. Activos actuales: lo que YA TIENE, no lo que tiene que construir o conseguir.

Ahora analizo cada opción contra estas restricciones:

OPCIÓN A: Vender datos API a empresas.
- Requisitos que FALTAN: Construir el producto (6 semanas = ~42 días, PERO además ciclo de venta HISTÓRICO 5-7 MESES. Él ya sabe que de contacto a cobro son 5+ meses. Su caja es 3 MESES. Incluso si empieza a contactar HOY, no cobra antes de 5 meses. Además, tiene que gastar 6 semanas CONSTRUYENDO sin ingresos. NO CUMPLE PLAZO DE CAJA.

OPCIÓN B: Marca blanca para agencias.
- Requisitos que FALTAN: 3 casos de éxito. Hoy tiene 0. ¿Cómo consigue casos de éxito? Probablemente regalar el servicio o cobrar muy poco, lo que no le da ingresos HOY. Además, incluso si consigue los 3 casos en, digamos, 1 mes, luego tiene que vender. El ticket es $300/mes, pero ¿cuánto tiempo le toma cerrar? No lo dice, pero primero tiene que generar los activos (casos) que no tiene. También, ¿necesita adaptar la tecnología para marca blanca? Probablemente sí, aunque no lo dice, pero el punto clave es que NO TIENE LOS REQUISITOS HOY para cobrar. Incluso si se apura, los casos de éxito tardan al menos 2-3 semanas cada uno (porque el cliente tiene que usarlo y ver resultados), así que en 3 meses tal vez cierra un primer cliente, pero ¿ingresos efectivos? Dudo. NO CUMPLE PLAZO DE CAJA.

OPCIÓN C: Contenido patrocinado en medio que YA OPERA.
- Requisitos que YA TIENE: Tráfico/audiencia (activo existente), 2 MARCAS QUE LE ESCRIBIERON EL MES PASADO (no les respondió). No necesita construir NADA.
- Plazo de ingresos: ¿Cuánto tiempo le toma responder a esas 2 marcas, cerrar el trato, producir el contenido y cobrar? Vamos a desglosar con 4h/día:
  1. Día 1-2: Responder a las 2 marcas con propuesta (usa su audiencia existente, así que los datos de tráfico/audiencia los tiene ya, no hay que investigar mucho).
  2. Día 3-7: Negociar (son marcas que ya le preguntaron, así que ciclo de venta es MUY corto, no es cold outreach).
  3. Día 8-15: Producir el contenido (4h/día, una pieza de contenido patrocinado no es un producto SaaS, lo hace rápido).
  4. Cobro: Si pide pago por adelantado (lo normal en contenido patrocinado, especialmente si es un medio chico que no tiene condiciones de crédito), cobra ANTES de publicar, o al publicar. En 15-20 días tiene ingresos EFECTIVOS.
- Además: No le quita todo el tiempo, puede incluso usar el resto de las 4h/día para ir preparando otras opciones (pero el foco es cerrar estas 2 marcas primero, luego buscar más).
- Ticket: $400-800 por pieza. Si cierra las 2 marcas, cada una compra 1 pieza: $800-1600 en 20 días. Luego puede buscar más marcas (ahora con casos de éxito de estas 2), así que en 3 meses puede cobrar varios miles, suficiente para extender la caja o incluso cubrirla.

Ahora, justificarlo con sus restricciones, no con el mercado: él dijo que elige por lo que se puede EJECUTAR CON ACTIVOS ACTUALES, no por el tamaño del mercado.

También, ¿por qué descartar las otras? Porque no cumplen el plazo de caja:
- A: Ciclo de venta HISTÓRICO 5-7 meses > 3 meses de caja. Además necesita construir producto sin ingresos.
- B: Necesita 3 casos de éxito que no tiene, lo que le toma tiempo sin ingresos, luego vender.

También, agregar un paso de ejecución concreto para C en los próximos 3 meses, para que sea claro:
1. Semana 1: Responder a las 2 marcas que le escribieron, enviar propuesta con datos de audiencia (que ya tiene), pedir pago por adelantado.
2. Semana 2-3: Cerrar al menos 1 (mejor 2) trato, producir el contenido, cobrar.
3. Semana 4 en adelante: Usar los casos de éxito de estas 2 marcas para contactar a otras marcas del mismo nicho (ya tiene la audiencia, así que sabe qué marcas le interesan), cerrar más piezas.
4. Mientras tanto, puede dedicar 1h/día de las 4 a ir preparando, por ejemplo, los casos de éxito para B o el producto para A, PERO EL FOCO ES C, porque es el único que genera ingresos en plazo.

Otra cosa: El usuario es solo, 4h/día. C no requiere construcción, solo responder, negociar, producir contenido (lo que ya sabe hacer, porque opera el medio). Es el único que usa sus activos existentes (audiencia, tráfico, marcas que ya le contactaron) sin necesidad de nuevos activos.

También, el ciclo de venta de C es MUY corto porque es inbound: las marcas ya le preguntaron, no es cold outreach. En B2B (A) es outbound, ciclo largo. En B es agencias que necesitan pruebas, ciclo medio.

Otra ventaja de C: Los ingresos son recurrentes? No, pero son inmediatos. Y puede repetir: si hace 2 piezas al mes, son $800-1600/mes, lo que le da colchón para luego ir a las otras opciones. Pero él necesita ingresos ANTES de que se acabe la caja, así que inmediato es mejor.

Wait, ¿qué pasa si las 2 marcas no le compran? Pero él dijo que ya le escribieron preguntando precios, así que es un lead calificado. Incluso si solo cierra una, son $400-800 en 2 semanas, lo que le da más tiempo. Y luego puede usar esa pieza como caso de éxito para contactar a otras marcas.

También, en la opción A, el ciclo de venta es 5-7 meses DESDE EL PRIMER CONTACTO HASTA EL COBRO. Así que incluso si empieza a contactar hoy, no cobra hasta el mes 5-7, que es después de que se le acabe la caja. Además, necesita construir el producto en 6 semanas, lo que le quita tiempo de outreach. Así que A es imposible en plazo.

Opción B: Necesita 3 casos de éxito. ¿Cómo los consigue? Tiene que darle el servicio gratis a 3 agencias, o cobrar muy poco. Pero eso no le da ingresos. Y luego, cuando tenga los casos, tiene que vender a otras agencias. El ticket es $300/mes, pero ¿cuánto tiempo le toma cerrar? Incluso si cierra en 1 mes después de tener los casos, los casos le toman 2 meses, así que cobra en el mes 3, pero ¿efectivo? Probablemente no, porque los pagos mensuales son después de que se usa el servicio, o al principio, pero el ciclo de conseguir los casos es sin ingresos. Así que B no le da ingresos en los primeros 2 meses, lo que le quita caja.

Así que la única opción que cumple todas las restricciones es C.

Ahora, estructurar la respuesta:
1. Empezar con el criterio que él estableció: EJECUTAR CON ACTIVOS ACTUALES + INGRESOS ANTES DE 3 MESES (caja se acaba).
2. Analizar cada opción contra estos criterios, ordenadas de