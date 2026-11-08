# Muse Spark 1.3 — business_strategy/elegir_negocio_con_dependencia_oculta

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 16.368s | tokens_per_second: 118.9
- input_tokens: 319 | output_tokens: 1946

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

Agarra la **C. 100%. Sin dividirte.**

No porque sea la más grande. Sino porque es la única que puedes cobrar antes de morir.

Tienes 3 restricciones que matan todo lo demás:
1. **1 persona, 4h/día** = ~240 horas en 3 meses. No puedes construir Y vender.
2. **3 meses de caja.** Necesitas time-to-cobro < 90 días.
3. **0 tracción en A y B, tracción real en C.**

Míralo por tiempo hasta el primer dólar:

**OPCIÓN A — API a empresas: Te mata.**
6 semanas de construcción a full-time = con tus 4h/día son 10-12 semanas. Ya te comiste toda la caja solo construyendo.
Y luego tu ciclo histórico es 5-7 meses hasta el cobro.
Primer dólar: mes 8-10. Tú mueres en el mes 3.
El ticket de $500-2.000 es irrelevante si no vives para cobrarlo. Es el clásico error: elegir por TAM de slide.

**OPCIÓN B — Marca blanca: Te mata.**
Necesitas 3 casos de éxito y tienes 0. Eso significa:
Conseguir 2-3 agencias piloto gratis + implementar + esperar resultados + documentar = 2 meses trabajando gratis en el mejor caso.
Y *después* empiezas a vender. Primer dólar: mes 4-5.
Mueres en el mes 3, con casos a medio hacer.

**OPCIÓN C — Patrocinado: Te salva.**
Time-to-cobro: 7 días.
Producto a construir: 0.
Demanda: ya existe. 2 marcas te escribieron el mes pasado preguntando precios. Eso es inbound caliente.
Activos: ya tienes el tráfico y la audiencia.

Con 4h/día no necesitas construir, necesitas facturar. A $400-800 por pieza, con 3-4 piezas al mes ya estiras tu colchón y compras tiempo.

Tu problema de los próximos 3 meses no es escalar. Es **sobrevivir.**

Qué hacer el lunes:
1. Respóndele HOY a esas 2 marcas que ignoraste. "Perdón por la demora, ya abrí 2 espacios para este mes. Rate: $X por pieza."
2. Arma un media kit de 1 página en 2 horas: tráfico, audiencia, formatos, precio. Nada más.
3. Vende solo eso por 90 días. Nada de código. Nada de B2B largo.

A y B no son malas ideas. Son ideas para cuando tengas 12 meses de caja. La C te va a dar la caja — y los casos — para hacer la B después.

Primero sobrevive, después escala.