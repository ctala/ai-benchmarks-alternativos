# Claude Sonnet 5.5 — strategy/business_model_validation

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.26 | quality: 10.0
- latency_total: 45.339s | tokens_per_second: 108.7
- input_tokens: 290 | output_tokens: 4928

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

# Pitch con VC escéptico

## 1. Los 5 riesgos principales

**Riesgo 1: El 15% de comisión probablemente es inviable.**
Un distribuidor de alimentos opera con márgenes brutos de 10-25% y netos de 2-5%. Un 15% se come casi todo el margen del proveedor. Si se lo cobras a él, sube precios o te saca de la plataforma. Si se lo cobras al restaurante, que tiene márgenes netos de 3-9%, compra directo y te ignora. Los marketplaces B2B de commodities suelen cobrar 2-5%. Para cobrar 15% tienes que ser distribuidor (inventario, logística, crédito), y eso es otro negocio, con otro capital y otros márgenes.

**Riesgo 2: Disintermediación.**
Tu producto es, en el fondo, una introducción. Una vez que el restaurante conoce al proveedor, ¿por qué seguiría pagándote 15% si puede pedir por WhatsApp gratis? Hay una relación personal, un número de celular y cero costo de cambio. Tu take rate se erosiona a la segunda orden.

**Riesgo 3: Tu competencia real es WhatsApp, no otra app.**
El restaurante ya resolvió el problema de forma imperfecta pero gratis: un grupo de WhatsApp, un proveedor de confianza, una visita al mercado. Tu hipótesis dice que pierden tiempo, pero ese tiempo no les cuesta dinero visible. ¿Pagarían por ahorrarlo? "Quieren una solución digital" no es evidencia. Quieren precio, crédito y confiabilidad.

**Riesgo 4: Economía unitaria y densidad.**
Un restaurante pequeño compra quizá $2-6K USD al mes en insumos. Con tu 15% serían $300-900/mes de ingreso bruto por restaurante, **si** concentra todo contigo, y no lo hará. Fragmentas la compra entre 5-10 proveedores y tú capturas una parte. El CAC de llegar a restaurantes uno por uno, sumado a una alta mortalidad de restaurantes (churn estructural) y la necesidad de densidad geográfica, hace que cada ciudad sea un nuevo problema de arranque.

**Riesgo 5: Problema de dos lados sin ventaja.**
Los proveedores locales son informales, sin catálogo digital, con precios que cambian a diario (sobre todo en perecederos) y poca disciplina operativa. Si fallan una entrega, el restaurante te culpa a ti. Controlas la experiencia sin controlar la operación. ¿Y qué te impide a ti ser un buen *lead gen* y nada más?

---

## 2. Por qué podría NO funcionar en LATAM

- **El crédito es el producto real.** En LATAM los restaurantes compran a crédito informal (8-30 días) con proveedores que los conocen. Si tu plataforma exige pago inmediato, pierdes. Si ofreces crédito, eres un fintech con riesgo de cartera, y eso quema capital.
- **Cultura de relación y regateo.** El dueño va al mercado (la Central de Abastos, CEABA, el mercado mayorista) porque ve, toca, negocia y consigue "el precio de hoy". Una app con precios fijos no replica eso.
- **Informalidad.** Muchos proveedores pequeños no facturan o no quieren que su ingreso quede registrado. Una plataforma digital los expone fiscalmente. Es un incentivo en contra de que se registren.
- **Cementerio de precedentes.** Frubana, Chiper, Merqueo, Jokr y otros levantaron mucho capital para atacar el abasto B2B de alimentos. La experiencia general fue márgenes delgados, logística cara, recortes y pivotes. Si no sabes por qué ellos sufrieron y tú no, no tienes pitch. Si tu respuesta es "ellos eran distribuidores y yo soy marketplace", entonces vuelve al riesgo 1: sin distribución propia, ¿qué justifica el 15%?
- **Fragmentación extrema.** Cada ciudad tiene proveedores, regulaciones y hábitos distintos. No hay efecto de red transferible entre Guadalajara, Medellín y Lima.
- **Tamaño de ticket y de mercado en dólares.** Ticket pequeño, moneda débil, y los fondos miran retornos en USD. Un negocio de 5,000 restaurantes con $400/mes de ingreso son $24M/año de ingreso. No es un negocio de $1B, y ese es el techo que un VC necesita ver.
- **Digitalización incompleta.** Hay smartphones, pero eso no significa que el cocinero o el dueño con el delantal puesto quiera gestionar pedidos en una app nueva a las 6am.

---

## 3. Qué tendría que ser verdad (key assumptions)

| # | Supuesto | Qué lo validaría |
|---|----------|------------------|
| 1 | El dolor es suficientemente grande como para pagar | Restaurantes pagan o se comprometen *antes* de que exista el producto |
| 2 | Alguien acepta pagar una comisión alta | Probar quién paga (restaurante o proveedor) y cuánto sin que se vayan |
| 3 | El proveedor obtiene nuevos clientes, no solo comisión por clientes que ya tenía | % de GMV de clientes realmente nuevos para el proveedor |
| 4 | La retención sobrevive a la disintermediación | Repetición de pedidos *dentro* de la plataforma después de la 3ª-4ª orden |
| 5 | Los restaurantes concentran compra | Qué % de su gasto en insumos pasa por ti (>30% mínimo) |
| 6 | Puedes adquirir clientes barato | CAC < 3-4 meses de contribución |
| 7 | Los proveedores cumplen consistentemente | Tasa de entrega a tiempo y completa >90% |
| 8 | Hay densidad suficiente en una zona pequeña | Con ~50 restaurantes y ~15 proveedores en un radio chico ya hay liquidez real |
| 9 | Existe un camino de expansión del ingreso | Pagos, crédito, software de inventario, datos. Solo comisión de intermediación es un techo bajo |

El supuesto que más me preocupa es el 2 junto con el 4: **que el valor que capturas sea mayor que lo que te cuesta el usuario evadirte.**

---

## 4. El escenario de fracaso rápido

**Meses 1-3:** Haces onboarding de 30 restaurantes con descuentos y de 10 proveedores a mano. Parece tracción.

**Meses 4-6:** Los restaurantes piden una vez, comparan precios y te usan para *descubrir* proveedores. Luego piden por WhatsApp. Los proveedores, al ver la comisión, te piden precios más altos, o empiezan a darte "precios de app" inflados y precios reales por fuera. Una entrega falla, el chef te culpa, y el dueño vuelve a su método de siempre.

**Meses 7-9:** GMV estancado, retención baja, CAC subiendo. Para retener ofreces crédito o subsidias entregas, y ahí quemas caja. Bajas la comisión a 5% para competir con el canal gratis, y la economía unitaria ya no cierra.

**Meses 10-12:** Sin tracción de calidad, no hay Serie A. Los inversores preguntan por GMV recurrente, take rate real y cohortes. Los números muestran que el 15% era nominal y el efectivo es 3-4%.

**Por qué fracasas rápido:** porque estás vendiendo una introducción como si fuera una transacción recurrente, y cobras un precio que solo se justifica si controlas el flujo de pedidos, el pago y la logística. No controlas nada de eso.

---

## 5. Con $10K: qué haría

**Principio:** no construyas nada. Compra evidencia, no software.

**Semanas 1-2: entrevistas con dinero en juego (~$500)**
- 30-40 entrevistas con dueños y chefs de restaurantes pequeños. No preguntes "¿te gustaría una app?". Pregunta: ¿a quién le compraste ayer? ¿Cuánto pagaste? ¿Qué pasó la última vez que un proveedor falló? ¿Cuánto tiempo y dinero te costó?
- 10-15 entrevistas con proveedores: márgenes, crédito, cobranza, y cómo reaccionarían a una comisión.

**Semanas 3-8: servicio concierge por WhatsApp (~$5-6K)**
- Una sola zona geográfica, una sola categoría (por ejemplo, verduras y proteínas).
- 10-15 restaurantes y 5-8 proveedores. Tú eres la plataforma: recibes pedidos por WhatsApp, los consolidas, coordinas, y cobras.
- Prueba **tres esquemas de monetización** con distintos grupos: comisión al proveedor, comisión al restaurante, y suscripción fija.
- Usa ~$3-4K como capital de trabajo para cubrir pagos o pequeñas garantías (no crédito amplio).

**Qué medir (la lista que importa):**
1. ¿Cuántos piden una segunda y tercera vez sin incentivos?
2. ¿Qué % de su gasto total en insumos pasa por ti?
3. ¿Qué comisión aceptan realmente sin irse, y quién la paga?
4. ¿Cuántos proveedores te dan precios iguales a los de su canal directo?
5. ¿Qué intentan hacer para saltarte?
6. Tasa de cumplimiento de entregas.
7. Tiempo real que te toma operar un pedido (si el concierge es doloroso, el producto tendrá el mismo problema).

**Criterios de muerte definidos de antemano:**
- Menos de 50% de repetición a la 4ª semana → mata o pivota.
- Nadie paga más de 5% → el modelo de 15% está muerto.
- Más del 30% de pedidos se van por fuera → no tienes retención.

**Último ~$2K:** reserva para un pivote rápido. Probablemente descubras que el negocio real es otro: **crédito para restaurantes, consolidación de compras para ahorrar, o software de pedidos para proveedores** (SaaS que digitaliza al proveedor, que es quien tiene el dolor de cobranza y toma de pedidos).

---

## La pregunta final del VC

> "Si tu mejor cliente puede replicar el 90% de tu valor con un grupo de WhatsApp y un contacto, ¿por qué dentro de 18 meses seguiría pagándote 15%?"

Si no tienes una respuesta basada en datos (crédito, consolidación de precios, confiabilidad garantizada, información que ellos no tienen), no tienes un negocio, tienes una directorio con comisión.

Mi veredicto: la hipótesis del *problema* es plausible, pero el *modelo* (marketplace puro al 15%) es la versión más débil de esta idea. Lo valioso podría estar en una capa más profunda: financiamiento, logística compartida o herramientas para el proveedor. Valídalo con el concierge antes de escribir una línea de código.