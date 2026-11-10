# Claude Fable 5.2 — strategy/business_model_validation

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 7.86 | quality: 10.0
- latency_total: 49.938s | tokens_per_second: 88.8
- input_tokens: 290 | output_tokens: 4435

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

# Tu pitch, visto por un VC escéptico

## 1. Los 5 riesgos principales

**1. Tu comisión del 15% no cabe en los márgenes.** Un distribuidor de alimentos opera con márgenes brutos de 15-25% y netos de un dígito. Un restaurante pequeño gana quizá 3-10% neto. ¿Quién paga el 15%? Si es el proveedor, sube precios y el restaurante lo nota. Si es el restaurante, no te usa. Las apps de delivery cobran eso porque traen demanda nueva. Tú intermedias una compra que ya existe.

**2. La desintermediación es casi segura.** La compra es recurrente, frecuente y al mismo proveedor, la peor estructura para un marketplace. Tras el primer pedido, el proveedor dice "escríbeme directo y te ahorras la comisión". ¿Qué lo impide?

**3. Puede que estés resolviendo el problema equivocado.** ¿De verdad "pierden mucho tiempo llamando"? Hoy mandan un WhatsApp en dos minutos. Sospecho que sus dolores reales son precio, crédito, calidad consistente y entregas puntuales. Tu competidor es WhatsApp, y es gratis.

**4. No controlas la experiencia, o te vuelves distribuidor.** Si el tomate llega podrido, la culpa es tuya. Si no manejas la logística, no puedes garantizar nada. Si la manejas, eres un negocio de camiones y bodegas con márgenes mínimos, no una app.

**5. La economía unitaria es mala.** Tienes que construir densidad barrio por barrio, con clientes de ticket chico que se adquieren con vendedores a pie y que quiebran con frecuencia. El CAC es alto y el LTV es corto.

## 2. Por qué podría no funcionar en LATAM

- **Informalidad fiscal:** muchas transacciones son en efectivo y sin factura. Tu plataforma deja rastro, y para muchos eso es un defecto.
- **El fiado:** los proveedores dan crédito informal a 7-30 días basado en confianza. ¿Lo vas a financiar tú? ¿Con qué capital?
- **Centrales de abasto:** muchos dueños van en persona, escogen el producto y regatean. Eso es control de calidad y de precio, no una ineficiencia.
- **WhatsApp:** ya es la capa digital, con adopción total y costo cero.
- **Pagos:** la pasarela te quita otro 3-4% de un margen que ya no existe.
- **Precedentes:** hasta donde sé, Frubana levantó más de 200 millones de dólares y aun así terminó recortando y saliendo de mercados (verifica los detalles). ¿Qué sabes tú que ellos no sabían?

## 3. Qué tendría que ser verdad

1. Hacer pedidos es un dolor top 3 para el restaurante, por encima de precio y crédito.
2. Los restaurantes quieren descubrir proveedores nuevos de forma continua. Si no, eres una herramienta de pedidos, no un marketplace.
3. Aportas algo que no se puede replicar por fuera, como crédito, mejores precios por volumen o garantía de calidad.
4. Los proveedores tienen capacidad ociosa y pagarían por clientes nuevos.
5. Los números cierran con una comisión realista. Si un restaurante compra 3.000 dólares al mes y capturas el 30%, al 15% ganas 135 dólares al mes. A un 3-5% realista ganas 27-45, con un CAC de campo de 100-300 y churn alto.
6. Ambos lados aceptan formalizar sus transacciones.

## 4. El escenario de fracaso rápido

Gastas 5 meses y tu capital en construir la app. Consigues 15 proveedores y 80 restaurantes con visitas y descuentos. Los primeros pedidos llegan, subsidiados. Al segundo mes, los proveedores sacan a sus clientes de la plataforma, o suben precios para cubrir tu comisión y el restaurante ve que su proveedor de siempre es más barato.

Tu volumen "crece" solo mientras quemas dinero en promociones, y la retención al mes 3 queda por debajo del 20%. Te quedas sin caja y sin haber sabido nunca si el problema existía, porque validaste la app y no la hipótesis.

## 5. Qué haría con $10K

No escribiría código.

**Semanas 1-2 (unos $500): entrevistas en persona.** Hablaría con 30-40 restaurantes y 10-15 proveedores. No preguntaría "¿usarías una app?", sino "cuéntame tu último problema con un proveedor" y "¿cuánto tiempo te tomó tu último pedido?". Si el dolor de pedir no sale espontáneamente, la hipótesis está muerta y te ahorraste $9.500.

**Semanas 3-8 (unos $6.000): piloto manual.** Usaría WhatsApp, una hoja de cálculo y un catálogo en PDF, en una zona y una categoría, con 10-15 restaurantes y 3-5 proveedores. Tú eres la app. Cobraría comisión real desde el primer día y probaría 15%, 5% y suscripción fija. El presupuesto va a una persona de campo a medio tiempo y a cubrir fallos de entrega.

**Reserva (unos $3.500): segunda iteración.** Serviría para probar otro ángulo si el primero falla, como crédito, compras consolidadas o un nicho premium.

**Criterios de muerte, definidos antes de empezar:**
- Menos del 40% sigue pidiendo en la semana 4.
- Capturas menos del 20% de sus compras.
- Más del 30% intenta saltarte.
- Nadie acepta pagar más del 5%.

Si pasa cualquiera de estas cosas, no hay negocio con este modelo.

## Veredicto

Hoy no invertiría. El mercado existe, pero tu hipótesis de dolor no está validada y el 15% no sobrevive a un análisis de márgenes. Si las entrevistas revelan que el dolor real es crédito o precio, ahí puede haber una empresa, pero sería otra empresa.