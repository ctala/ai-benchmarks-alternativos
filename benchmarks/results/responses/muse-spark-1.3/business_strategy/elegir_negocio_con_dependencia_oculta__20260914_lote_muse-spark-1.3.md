# Muse Spark 1.3 — business_strategy/elegir_negocio_con_dependencia_oculta

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 17.004s | tokens_per_second: 107.8
- input_tokens: 318 | output_tokens: 1833

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

Agarra **C. Sin discusión.**

No es la más grande. Es la única que puedes cobrar antes de morirte.

Tienes 3 restricciones que matan a A y B:

1. **Solo, 4h/día = ~240 horas en 3 meses.** No tienes equipo para construir y vender en paralelo.
2. **3 meses de caja.** Tu *time-to-cash* tiene que ser < 90 días. Punto.
3. **Activos actuales:** 0 producto, 0 casos de éxito, pero SÍ tráfico + 2 marcas que ya te pidieron precio.

Míralo por tiempo al primer dólar:

**A - API a empresas: Te mata.**
Ticket lindo, mercado enorme, irrelevante.
6 semanas para construir = te come la mitad de tus horas. Y luego tu ciclo histórico es 5-7 meses hasta cobrar.
Primer cobro: mes 6.5 - 8.5. Tú mueres en el mes 3.

Elegir A es elegir quebrar por perseguir el TAM de la diapositiva.

**B - Marca blanca para agencias: Te mata.**
Necesitas 3 casos para vender 1. Tienes 0.
Para conseguir 1 caso tienes que: regalar trabajo, implementar, esperar resultado, documentar. Multiplica x3, solo y en 4h/día.
Mejor escenario: llegas al mes 3 recién con el material para *empezar* a vender. Cero ingresos en 90 días.

Es un callejón sin salida: necesitas clientes para tener casos, necesitas casos para tener clientes.

**C - Contenido patrocinado: Es la única ejecutable.**
0 construcción. Distribución ya la tienes. Demanda ya la tienes: 2 inbound del mes pasado a los que ni les respondiste.

Tiempo al primer cobro: días, no meses. Escribes hoy, cotizas esta semana, cobras por adelantado el 50%.

Con ticket $400-800, con cerrar 2-4 piezas al mes ya estiras caja y compras tiempo. No te hace rico, te mantiene vivo, que es tu único objetivo ahora.

Tu plan próximos 3 meses:

1. Hoy: responde a esas 2 marcas. Pide perdón por la demora y mándales media kit de 1 página + precio.
2. Semana 1: arma pack simple: 1 pieza $800, pack x3 $1,800, pago 50% adelantado. Nada complejo.
3. 100% de tus 4h a vender y publicar sponsors. Cero código.

A y B no son malas ideas. Son ideas para cuando tengas 12 meses de caja, no 3. Primero sobrevive con C, después financias B o A con esa caja.