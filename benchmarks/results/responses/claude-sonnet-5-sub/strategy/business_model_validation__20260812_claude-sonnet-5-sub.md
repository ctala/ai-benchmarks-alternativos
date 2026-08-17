# Claude Sonnet 5 (suscripción) — strategy/business_model_validation

- model_id: `claude-sonnet-5`
- success: True  | final: 8.07 | quality: 10.0
- latency_total: 90.983s | tokens_per_second: 68.0
- input_tokens: 2 | output_tokens: 6189

## Entrada exacta (lo que recibió el modelo)

**user:**

Quiero crear una app que conecta restaurantes pequenos con proveedores de ingredientes locales. El modelo es marketplace con 15% de comision por transaccion.

Mi hipotesis: los restaurantes pequenos pierden mucho tiempo llamando a multiples proveedores y quieren una solucion digital.

Actua como un VC esceperico. Hazme las preguntas dificiles que me harian en un pitch:
1. Identifica los 5 riesgos principales de este modelo
2. Por que podria NO funcionar en LATAM especificamente?
3. Que tendria que ser verdad para que funcione? (key assumptions)
4. Cual es el escenario donde fracaso rapido y por que?
5. Si solo tuviera $10K para validar, que harias?

No seas amable. Se brutalmente honesto.


## Respuesta completa

Antes de las preguntas, un dato que cambia todo: **estás describiendo un mercado con márgenes de 2-8% donde quieres cobrar 15% de comisión.** Eso no es un modelo de negocio, es una contradicción matemática que alguien tiene que absorber. Empecemos por ahí.

## 1. Los 5 riesgos que matan esto

**Riesgo 1 — Unit economics imposibles.** La distribución de alimentos opera con márgenes de 2-8%. Tu 15% no sale de la nada: o lo paga el proveedor (y le quitas más margen del que tiene, se va), o lo paga el restaurante (y ya no ahorra nada respecto a llamar directo, entonces por qué usarte). No hay tercera opción a menos que generes ahorro real vía volumen/logística — y eso es un negocio de logística, no de marketplace.

**Riesgo 2 — Desintermediación (leakage).** El día 1 el restaurante y el proveedor se conocen a través de tu plataforma. El día 15, se conocen a secas. Intercambian WhatsApp en la entrega (es físicamente inevitable, alguien tiene que recibir la mercadería) y la orden 3 en adelante va directo, sin comisión. Este es EL problema documentado de todo marketplace de servicios B2B recurrentes — Choco (Alemania) literalmente pivotó de comisión por transacción a SaaS fijo para proveedores por esto mismo.

**Riesgo 3 — Chicken-and-egg hiperlocal.** No estás construyendo un marketplace nacional, estás construyendo docenas de mini-marketplaces por barrio/comuna, porque un proveedor de Providencia no le sirve a un restaurante en Maipú. Cada zona nueva es un cold-start desde cero: sin densidad de proveedores no hay restaurantes, sin restaurantes no hay proveedores. Esto multiplica tu CAC por cada geografía, no lo divide.

**Riesgo 4 — Ownership de logística y calidad ambiguo.** ¿Eres solo un matchmaker o también manejas la entrega? Si NO controlas la entrega, cualquier tomate podrido o pedido incompleto es "problema de la plataforma" en la cabeza del restaurante, sin que tú controles la causa. Si SÍ controlas la entrega, ya no eres un marketplace de 15% de comisión — eres una empresa de distribución con capex y logística, un negocio completamente distinto, con márgenes aún peores.

**Riesgo 5 — El crédito es el producto real, no el "ahorro de tiempo".** Los restaurantes chicos compran con crédito de 15-30-60 días con "su proveedor de siempre" — esa relación de fiado es la razón por la que NO cambian de proveedor aunque llamar sea tedioso. Tu hipótesis asume que el dolor es "tiempo perdido llamando". El dolor real, si existe, probablemente es "necesito crédito y confianza", y eso no lo resuelve una app — lo resuelve capital de trabajo, que tú no tienes.

## 2. Por qué esto se rompe específicamente en LATAM

- **Informalidad.** Buena parte de la compra de insumos de un restaurante chico es con proveedores no bancarizados, sin factura, en efectivo (ferias, mayoristas informales). No hay riel de pago digital que interceptar para cobrar tu comisión.
- **WhatsApp ya es "la solución digital".** Tu hipótesis dice "pierden tiempo llamando". La realidad en LATAM es que la mayoría ya coordina por WhatsApp (texto o nota de voz), gratis, sin fricción, con la persona de confianza. Estás compitiendo contra una herramienta gratuita que ya resolvió el 80% del problema — no contra el teléfono.
- **Fiado como moat del incumbente.** La confianza construida en años con "el proveedor de la carne" es un switching cost brutal en contra tuyo, no a tu favor.
- **Formalización = riesgo fiscal para el restaurante.** Si tu marketplace deja rastro digital de transacciones, para un restaurante que opera parcialmente informal eso es un desincentivo, no un beneficio.
- **Márgenes aún más finos que en mercados desarrollados**, con inflación y volatilidad cambiaria (Argentina, Venezuela) que hace que un contrato o precio fijo pierda sentido en semanas.

## 3. Qué tendría que ser verdad (key assumptions, sin filtro)

1. El dolor real no es "llamar" sino algo más caro (precio, disponibilidad, calidad) — si no, nadie paga por resolver una molestia menor.
2. La comisión de 15% es MENOR que el valor generado (ahorro real de tiempo + mejor precio por agregación). Si no hay ahorro medible, no hay caso de negocio.
3. Puedes evitar la desintermediación — con crédito, logística consolidada, o algo que WhatsApp no pueda replicar gratis. Si tu única barrera es "conveniencia de tener todo en un lugar", no es barrera.
4. Puedes lograr densidad de oferta y demanda en UNA zona chica antes de quedarte sin plata — porque los efectos de red son locales, no nacionales.
5. El pago pasa por tu plataforma (no efectivo, no transferencia directa) — si no, no hay forma de cobrar comisión de manera confiable.
6. La frecuencia de compra es alta (diaria/semanal) — si no, nunca se forma hábito y el CAC nunca se paga.

## 4. El escenario de fracaso rápido (y es el más probable)

Onboardeas 15 restaurantes y 8 proveedores en un barrio. Las primeras 2-3 órdenes pasan por la plataforma. En la entrega física de la orden 1, el conductor del proveedor y el dueño del restaurante intercambian número de WhatsApp — es inevitable, tienen que coordinar hora y recepción. Orden 4 en adelante: van directo. Tu retención cae a cero entre la semana 3 y 6. Gastaste tu presupuesto de CAC en "presentaciones" que se pagaron una sola vez, no en un negocio recurrente. El error no se ve en el pitch deck (las primeras 3 transacciones se ven geniales), se ve recién en el dato de cohortes de la semana 6 — que para entonces ya gastaste la plata en app y no en medir esto.

## 5. Con $10K, qué haría

**No construyas la app.** Esa es la primera regla. Cero líneas de código de marketplace.

- Sé tú (o contrata a alguien por 6-8 semanas) el "matchmaker humano" vía WhatsApp para 10-15 restaurantes en UNA sola zona chica. Llamas proveedores en su nombre, consolidas pedido, cobras comisión manual por transferencia.
- La única métrica que importa: **tasa de leakage a la semana 4-6.** Si más del 50% ya está yéndose directo con el proveedor sin pasar por ti, el modelo está muerto — sin importar cuán linda quede la app.
- Testea precio real: ¿pagan 15%? ¿10%? ¿5%? No preguntes, cóbralo de verdad con dinero real cambiando de manos. Encuestas mienten, transacciones no.
- Presupuesto: casi todo a pagar tu tiempo u operación (8 semanas), cero a desarrollo, cero a paid ads, cero a branding.

Si en 6 semanas de operación manual no tienes retención real y comisión que la gente pague sin quejarse, tienes la respuesta más barata posible: que este modelo, tal como está planteado, no funciona — y te ahorraste construir una app para descubrirlo.