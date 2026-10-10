# Claude Haiku 5.5 — strategy/business_model_validation

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 23.177s | tokens_per_second: 169.0
- input_tokens: 290 | output_tokens: 3918

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

Voy a ser directo. Tu hipótesis, como está escrita, todavía no justifica una app.

## 1. Los 5 riesgos principales

**1. Desintermediación en el primer pedido.** Un restaurante conoce al proveedor, le paga, y en tres meses le escribe directo por WhatsApp para evitar el 15%. Es el riesgo más probable y no tienes un mecanismo serio para contenerlo. Si tu respuesta es "contratos de exclusividad", los restaurantes pequeños no firmarán nada que los ate.

**2. Huevo y gallina con doble lado.** Sin proveedores no tienes restaurantes, y sin restaurantes los proveedores no se registran. Y no es un problema de un lado: necesitas densidad geográfica en ambos. Un restaurante en una colonia sin proveedores cercanos no vuelve. Lanzar en "una ciudad" no basta; necesitas una zona.

**3. El 15% es grande sobre márgenes ya finos.** Los restaurantes pequeños operan con márgenes de ingredientes que apenas cubren merma y mano de obra. Los proveedores de productos frescos tienen márgenes de 10–25% y ya viven apretados. Un 15% encima puede significar que el precio total sube 15% o que alguien pierde su margen. Ninguno de los dos acepta eso sin pelear. Además, el take rate sobre un ticket pequeño da muy poco: si un restaurante compra $800 USD al mes, eso son $120 USD de ingreso para ti al mes. Necesitas miles de restaurantes activos solo para cubrir un equipo mínimo.

**4. Logística y perecibles.** Esto no es software puro. Tomates y pescado se dañan, los pedidos llegan tarde, faltan productos, cambian precios diario por inflación o tipo de cambio. Si tú no controlas la entrega, pierdes la confianza de ambos lados en la primera semana mala. Si la controlas, tu modelo se parece más a un distribuidor de bajo margen que a un marketplace.

**5. Churn de restaurantes.** Un porcentaje alto de restaurantes pequeños cierra o cambia de dueño en pocos años. Si tu LTV depende de retención de restaurantes, tu base se mueve constantemente.

## 2. Por qué podría NO funcionar en LATAM

- **Economía informal y cash.** Muchos proveedores no facturan, no tienen cuenta bancaria formal ni terminal. Digitalizarlos implica formalizarlos, y eso no lo haces tú.
- **Fiscalidad.** Facturación electrónica (CFDI en México, NF-e en Brasil, SUNAT en Perú) varía por país y es obligatoria. Si el marketplace no emite o no concilia bien, el restaurante no puede deducir gastos y deja de usarte.
- **Crédito informal.** El modelo real de muchos proveedores es "fiado" o pago a 15–30 días con el dueño que conoce al chef. Un marketplace con pago inmediato compite contra una relación de confianza, no contra una llamada.
- **WhatsApp como sistema operativo B2B.** Muchos restaurantes ya coordinan pedidos por WhatsApp con grupos y listas. Tu app compite contra algo gratis que ya usan. El dolor puede ser menor de lo que crees, o estar resuelto de forma suficientemente buena.
- **Inflación y volatilidad cambiaria.** En Argentina, Venezuela o Turquía los precios cambian semanalmente. Tu catálogo y tus márgenes se vuelven inestables.
- **Mercados mayoristas.** En México, la Central de Abastos o los mayoristas locales ya resuelven "conseguir ingredientes baratos" con ventaja de precio y crédito. Los restaurantes pequeños suelen ir físicamente y ver el producto antes de comprar.
- **Competencia de plataformas grandes.** Si el negocio es atractivo, las plataformas de delivery o de retail pueden replicarlo con más capital y base de clientes.

## 3. Qué tendría que ser verdad

1. Los restaurantes gastan suficiente tiempo en compras como para que el ahorro valga más que el 15% más su incomodidad. Ojo: muchos restaurantes pagarían por *precio* o *crédito* antes que por *tiempo*. Tu hipótesis podría estar equivocada en qué es el dolor.
2. Los restaurantes compran lo suficiente cada mes (digamos >$1,000 USD) para que tu comisión sea significativa.
3. Puedes conseguir proveedores con calidad consistente y precio competitivo, y que acepten tu comisión sin subir precios.
4. La desintermediación no ocurre, o cuesta más al restaurante que pagarte (por confianza, garantía, facturas, devoluciones).
5. Alcanzas densidad local rápido: suficientes proveedores y restaurantes en una zona para que el servicio sea útil desde el día uno.
6. Puedes cobrar y pagar en un plazo que no te quiebre (tú pagas al proveedor y cobras al restaurante, o viceversa, y eso tiene costo de capital).
7. El CAC de restaurantes es bajo. Un restaurante vale poco; si cuesta $200 USD adquirirlo, con $120 USD/mes de take rate, la matemática funciona apenas, y solo si no se va.

## 4. Escenario de fracaso rápido

Lanzas en una ciudad con 40 restaurantes y 15 proveedores. Los primeros 10 restaurantes usan la app dos semanas. Los proveedores se quejan de la comisión y suben precios un 8%. Los restaurantes lo notan, comparan con su mayorista, y empiezan a pedir directo por WhatsApp al proveedor que ya conocían. Al tercer mes tienes un pedido mensual por restaurante, la retención cae, y tu único ingreso es de comisiones que no alcanzan ni para cubrir a una persona de soporte. Te quedas con una app bonita, sin densidad, sin datos claros de por qué se fueron, y con proveedores que ya no confían en ti.

La causa no es técnica. Es que el valor que aportas es fácil de replicar y caro de cobrar.

## 5. Si solo tuvieras $10K

No construyas la app. Haz esto en 6–8 semanas:

**Semana 1–2: entrevistas (sin costo, ~30 entrevistas).** Habla con dueños y chefs de restaurantes pequeños. No preguntes si les gustaría una app. Pregunta cómo compraron la última semana, cuánto gastaron, qué les molestó, cuánto tiempo les tomó, cuál fue el último error de proveedor que les costó dinero. Busca si el dolor es tiempo, precio, calidad o crédito.

**Semana 2–6: servicio manual (concierge) en una zona, con 10–15 restaurantes.** Recibes sus pedidos por WhatsApp, los consolidas con 3–5 proveedores, y tú coordinas la entrega. Cobras una comisión real desde el inicio. Presupuesto aproximado: $3–4K en logística, un coordinador part-time, un par de herramientas y pagos a proveedores como capital de trabajo.

**Métricas que deciden si sigues:**
- Restaurantes que piden al menos 2 semanas seguidas sin que tú los empujes.
- Pedidos por restaurante por semana (objetivo: al menos 2 o 3).
- Porcentaje de pedidos que siguen llegando a tiempo y completos.
- Porcentaje de restaurantes que te pagan la comisión sin negociar.
- Desintermediación: cuántos restaurantes compran directo a un proveedor que conociste a través tuyo.
- Disposición a pagar: si ofreces la app de pago anticipado en la semana 6, ¿cuántos firman?

**Criterios de muerte:** si en 6 semanas no tienes al menos 8–10 restaurantes pidiendo recurrentemente, o si los proveedores no quieren pagar la comisión, cambia de hipótesis o cierra. Ese resultado también es un dato valioso.

---

**La pregunta que te haría en el pitch:** Tu hipótesis es que pierden tiempo. ¿Ya hablaste con 20 dueños de restaurantes y te confirmaron que pagarían 15% por ahorrarlo, o solo lo supones porque el problema te parece obvio?