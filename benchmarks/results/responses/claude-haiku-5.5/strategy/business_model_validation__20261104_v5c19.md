# Claude Haiku 5.5 — strategy/business_model_validation

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.82 | quality: 10.0
- latency_total: 31.697s | tokens_per_second: 177.1
- input_tokens: 290 | output_tokens: 5614

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

Voy a ser directo, porque un VC te va a presionar en los mismos puntos.

## 1. Los 5 riesgos principales

**1. Desintermediación (el riesgo mortal).** El restaurante conoce al proveedor después de la primera transacción y la siguiente la hace por WhatsApp sin tu 15%. Y el proveedor puede preferir perder el 15% a cambio de conservar al cliente. Si no tienes una razón que haga que ambos sigan dentro de la plataforma (crédito, logística, facturación, garantía de precio), tu take rate dura un trimestre. Pregunta: *¿Qué te impide ser un directorio gratis que cobra por presentar?*

**2. El 15% no cabe en la economía del restaurante.** Un restaurante pequeño tiene márgenes netos de alrededor de 3-8% y un food cost de 28-35%. Si compra $1,000 al mes en insumos, pagar 15% extra son $150 que salen directo de su utilidad. El restaurante va a comparar contra "llamar y negociar" y va a ganar esa comparación si el ahorro de tiempo no vale más de lo que le cuesta. Además, ¿quién paga la comisión? Si la paga el proveedor, reduce su precio neto y se va. Si la paga el restaurante, se va. Si la pagan ambos, el modelo es frágil.

**3. El dolor puede no ser el que crees.** "Pierden tiempo llamando" es un dolor real pero de baja prioridad. Un dueño que pasa 30-45 minutos al día en pedidos valora ese tiempo quizá en $5-10 diarios. Lo que de verdad les duele suele ser: precio inconsistente, faltantes de último minuto, calidad variable, o no tener crédito a 15-30 días. Si tu solución resuelve solo la llamada, compites con WhatsApp, que es gratis y ya lo usan. Pregunta: *¿Cuántas veces en el último mes un proveedor les falló y qué hicieron?*

**4. Logística y calidad de la oferta.** Los ingredientes locales son perecederos, de calidad variable y con productores dispersos. Si no manejas entrega, eres un directorio sin control de calidad. Si la manejas, eres una empresa de logística con márgenes de distribuidor (que son bajos) y con costos de último kilómetro que pueden comerse el 15% completo. Cadena de frío, mermas, devoluciones, y quién responde cuando llega tomate podrido.

**5. Liquidez de dos lados en mercados locales.** Necesitas densidad: suficientes restaurantes y suficientes proveedores en la *misma zona* y para las *mismas categorías*. Con 30 restaurantes que piden de 12 proveedores distintos, cada proveedor recibe 2-3 pedidos por semana y se aburre. Crecer ciudad por ciudad, o barrio por barrio, cuesta caro y lento.

## 2. Por qué podría NO funcionar en LATAM específicamente

- **Informalidad en ambos lados.** Muchos proveedores locales no tienen RFC/CUIT/RUC activo, no emiten facturas electrónicas y no tienen cuenta bancaria formal. Y muchos restaurantes pequeños tampoco. Eso bloquea pagos, facturación fiscal (CFDI en México, NF-e en Brasil, factura electrónica en otros países) y tu capacidad de cobrar comisión de forma limpia.
- **Pagos en efectivo y crédito informal.** El restaurante paga cuando puede. Tu capital de trabajo se va a financiar a los proveedores o a los restaurantes. Morosidad y chargebacks van a ser un problema real.
- **Inflación y precios volátiles.** Los precios de insumos cambian semana a semana. Tu plataforma necesita actualización de precios casi en tiempo real, o pierdes confianza.
- **La confianza es personal.** "Mi proveedor de toda la vida" es una relación, no una transacción. Romper esa relación requiere que tu solución sea muy superior, no solo más cómoda.
- **Compras por WhatsApp son la infraestructura real.** Tu competencia no es otra app: es WhatsApp más la red informal de mercados y distribuidores, que cuesta cero.
- **Poder de compra del restaurante.** En México, Brasil, Colombia o Perú, el restaurante pequeño tiene poco poder de pago. Un 15% que en EE.UU. es aceptable aquí puede ser inaceptable.
- **Mercados muy distintos por país y ciudad.** Lo que funciona en CDMX no necesariamente funciona en Medellín o Lima, y tu costo de expansión se multiplica.

## 3. Qué tendría que ser verdad (key assumptions)

Cada una debe validarse con datos, no con intuición:

1. **Los restaurantes pagan por la plataforma y no la sustituyen con WhatsApp.** Medible: % de pedidos que se hacen en la app después de 60 días sin incentivos.
2. **El restaurante compra suficiente volumen.** Si el GMV por restaurante es de $300-500 al mes, el 15% son $45-75. Para que el modelo tenga sentido necesitas CAC bajo y retención alta. Asume que necesitas al menos $1,000-2,000 mensuales de GMV por cliente activo.
3. **Los proveedores aceptan el 15% sin desintermediar.** Medible: % de proveedores que siguen vendiendo por la plataforma después de 3 meses.
4. **Retención semanal.** Un restaurante que pide 1 vez al mes no te paga. Necesitas pedidos semanales o más, con el mismo proveedor repetido.
5. **Densidad suficiente por zona.** Necesitas, por ejemplo, 50 restaurantes y 20 proveedores en un radio de 3 km para que cada proveedor tenga pedidos regulares.
6. **Costo logístico y de operación menor al ~5% del GMV.** Si tu entrega o control de calidad cuesta más de lo que cobras, el modelo no escala.
7. **Tu CAC por restaurante es menor al LTV neto.** LTV neto = comisión × margen de contribución × meses de retención. Si la comisión neta es $60/mes y retienes 12 meses, tienes un LTV de ~$700. ¿Cuánto cuesta conseguir un restaurante? Si la respuesta es $200-300 por visita comercial, el número se ve, pero solo si retienes.
8. **Cobranza y crédito funcionan sin quebrar.** Morosidad menor al 2%.

## 4. El escenario de fracaso rápido

Ocurre así: consigues 40 restaurantes con visitas en persona y algunos favores de amigos. Los primeros 2 meses, hacen 3-4 pedidos cada uno, mayormente porque tú los presionas. Al tercer mes, ya tienen a su proveedor de siempre en WhatsApp, y tu plataforma se queda con pedidos de prueba. Los proveedores se quejan del 15%, algunos te piden que lo bajes, y otros simplemente no suben su catálogo porque reciben muy pocos pedidos. Cuando intentas cobrar, descubres que varios restaurantes pagan con transferencias atrasadas y dos proveedores no tienen RFC para facturar. Gastas tu runway en logística y en comisiones de adquisición, y a los 6-8 meses tienes 15 restaurantes activos, GMV de $15K mensuales, y un take rate que no cubre la operación.

La causa raíz no es la ejecución. Es que nunca probaste si el restaurante cambiaría su comportamiento real, ni si el proveedor aceptaría un intermediario sin subsidio.

## 5. Si solo tuviera $10K para validar

No construiría la app. Haría un **concierge test** (servicio manual que simula el producto):

**Semana 1-3 (~$500-800): Entrevistas y datos.**
- 25-30 entrevistas con dueños y chefs de restaurantes pequeños. Pide que te muestren sus últimos 5 pedidos y su historial de WhatsApp. Pregunta por el último error de proveedor y cuánto les costó.
- 10 entrevistas con proveedores. Pregunta cuánto venderían si tuvieran 10 clientes más, qué comisión aceptan y qué les daría crédito.
- Objetivo: confirmar o matar el dolor principal. Si el dolor principal resulta ser precio o crédito y no tiempo, pivotea antes de gastar más.

**Semana 4-10 (~$6,000-7,000): Concierge en una sola zona.**
- Elige un barrio con alta densidad de restaurantes (15-20 restaurantes).
- Recibe pedidos por WhatsApp de esos restaurantes. Tú compras a 5-8 proveedores, consolidas y entregas con una moto contratada.
- Cobra una comisión real, pero prueba variaciones: 0% vs 8% vs 15%, o una cuota fija mensual. Esto te dice cuánto pagan realmente.
- Mide: pedidos por restaurante por semana, % de repetición, margen bruto por pedido, mermas, tiempo que te toma operar, y cuántos pedidos siguen haciendo cuando dejas de presionar.

**Semana 10-12 (~$1,500): Pre-compromisos y decisión.**
- Pide a los restaurantes que paguen una suscripción o un depósito por el siguiente mes. Si no pagan, no te quieren.
- Pide a los proveedores un acuerdo de exclusividad o de comisión por 3 meses.

**Criterios de muerte (defínelos antes de empezar):**
- Menos de 8 restaurantes con 2+ pedidos semanales al mes 2.
- Menos de 60% de repetición sin tu presión.
- Margen bruto por pedido negativo después de logística.
- Cero restaurantes dispuestos a pagar por adelantado.

Si pasas esos criterios, tienes una historia de tracción real para un pitch. Si no, ahorraste meses y cientos de miles de dólares.

---

**La pregunta que te van a hacer al final:** *"¿Por qué un restaurante con un proveedor que conoce hace 10 años y un grupo de WhatsApp va a pagarte 15% por algo que ya hace gratis?"* Si no tienes una respuesta con datos de tu concierge test, todavía no tienes un pitch.