# Claude Fable 5.1 — strategy/business_model_validation

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.78 | quality: 10.0
- latency_total: 85.98s | tokens_per_second: 61.5
- input_tokens: 290 | output_tokens: 5291

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

Bien. Me sentaste en la silla del VC. Voy a hacer lo que haría en una reunión real: asumir que tu hipótesis está mal hasta que me demuestres lo contrario.

Primero, lo que me dice tu pitch sin querer: **nunca has comprado para un restaurante a las 5 de la mañana.** Si lo hubieras hecho, no dirías que el problema es "llamar a muchos proveedores". Vamos.

---

## 1. Los 5 riesgos principales

**Riesgo 1: El 15% no existe.**
El margen bruto de un distribuidor de alimentos frescos está entre 8% y 20%. Su margen neto, entre 2% y 6%. Le estás pidiendo que te entregue más de lo que gana. ¿Y el restaurante? Su food cost es 30-35% de ventas; subirle 15% el costo de insumos le destruye 4-5 puntos de margen neto en un negocio que opera con 5-10%. **Nadie en la cadena puede pagar tu comisión.** Este riesgo solo mata la empresa.

**Riesgo 2: Desintermediación inmediata.**
Compras de restaurante son recurrentes, con el mismo proveedor, 3-6 veces por semana. Tu plataforma hace un match una vez. El segundo pedido va por WhatsApp. No tienes ningún mecanismo que te mantenga en la transacción. Compara con Uber: cada viaje es un match nuevo. Lo tuyo es un directorio con pretensiones de marketplace.

**Riesgo 3: El producto real es el crédito, y no lo tienes.**
El proveedor del restaurante pequeño no es un proveedor: es un banco. Le fía 15-30 días, le ajusta precio cuando va mal, le manda producto extra cuando hay evento. Esa relación vale más que cualquier eficiencia de tiempo. Para competir necesitas capital de trabajo, scoring de restaurantes informales y apetito de riesgo crediticio. ¿Tienes alguno?

**Riesgo 4: Tu cliente se muere.**
Restaurantes pequeños en LATAM: mortalidad de 50-70% en los primeros 3 años. Tu churn estructural es brutal antes de que pierdas un solo cliente por tu culpa. CAC alto (venta presencial, uno por uno), LTV corto. Haz la cuenta.

**Riesgo 5: Logística es el negocio, y la estás ignorando.**
¿Quién entrega? Si el proveedor, eres un generador de leads y mereces 2-3%, no 15%. Si tú, eres una empresa de cadena de frío de última milla con mermas del 10-15% en perecederos y el 15% no cubre ni el camión. Frubana levantó más de USD 200M para hacer exactamente esto y terminó despidiendo gente y recortando ciudades. ¿Qué sabes tú que ellos no?

---

## 2. Por qué podría NO funcionar en LATAM específicamente

- **La informalidad es el margen.** Una parte enorme de la compra de insumos de restaurantes pequeños se hace sin factura. El proveedor no quiere trazabilidad, el restaurante tampoco. Tu plataforma formaliza, y formalizar le cuesta a ambos entre 10% y 20% en impuestos. Les sales más caro que tu comisión.

- **WhatsApp ya es la app.** No compites contra llamadas telefónicas. Compites contra un mensaje de voz de 8 segundos a un número que ya tienen guardado, con un tipo que ya saben que llega. Tu UX tiene que ser mejor que *eso*.

- **Los mercados mayoristas son el marketplace.** Central de Abasto, CEAGESP, Mercado de Lima, Corabastos. El dueño del restaurante va a las 5am, toca el aguacate, negocia en cash y se lleva el mejor precio del día. Ya existe un marketplace físico con liquidez, precio dinámico y verificación de calidad en tiempo real. El tuyo no tiene ninguna de las tres.

- **La transparencia de precios es enemiga del proveedor.** Tu valor para el restaurante es comparar. El proveedor vive de que no comparen. Estás pidiendo que tu lado de oferta financie su propia destrucción de margen.

- **No hay un LATAM.** Hay ciudades. La densidad de proveedores, los días de pago, el producto, la estacionalidad: todo cambia entre CDMX y Monterrey, entre Bogotá y Medellín. Cada ciudad es un lanzamiento desde cero. Esto no escala como software, escala como franquicia de distribución.

- **El cementerio está lleno.** Frubana, Chiper, Favo, Merqueo, Jüsto en sus versiones B2B, Choco en Europa que nunca logró monetizar el ordering. Todos tenían equipos fuertes y mucho capital. Dime cuál fue el error de cada uno y por qué tú no lo vas a repetir. Si no puedes, no has hecho la tarea.

---

## 3. Qué tendría que ser verdad para que funcione

Estas son las supuestos que tienes que probar, en orden de letalidad:

1. **Que el dolor sea descubrimiento, no confianza/crédito/precio.** Mi apuesta: estás equivocado. El restaurante no busca más proveedores, busca que el que tiene no le falle.
2. **Que alguien pague.** Específicamente: que un proveedor acepte ceder más del 5% por un canal nuevo, o que un restaurante pague por software (históricamente, casi nunca).
3. **Que exista un mecanismo de retención dentro de la transacción.** Pagos, crédito, factura, logística. Algo que haga más costoso salirse que quedarse.
4. **Que la frecuencia justifique el CAC.** Necesitas que el restaurante compre a través tuyo >60% de su gasto, no un pedido ocasional de lo exótico.
5. **Que el proveedor gane volumen incremental real.** No clientes que ya tenía, migrados a tu plataforma con un descuento.
6. **Que puedas resolver calidad a distancia.** Comprar fresco sin ver es un acto de fe. ¿Quién responde cuando el tomate llega golpeado?
7. **Que la economía unitaria cierre a nivel pedido, no a nivel cohorte en Excel.** Ticket promedio de un restaurante pequeño: USD 50-150. Al 15% ganas USD 10-20 por pedido. Eso tiene que cubrir venta, soporte, pagos y disputas.

Si fallan la 1 o la 2, no hay empresa. Si falla la 3, hay un negocio chico de lead gen.

---

## 4. El escenario de fracaso rápido

Te lo narro porque ya lo vi tres veces:

**Mes 1-2.** Levantas USD 300K de ángeles con un deck bonito. Contratas dos devs, construyes app bidireccional, pagos integrados, catálogo.

**Mes 3-4.** Lanzas en una ciudad. A pura hustle metes 40 restaurantes y 12 proveedores. Primer mes: USD 25K de GMV. Celebras. Posteas en LinkedIn.

**Mes 5.** Los proveedores empiezan a decir que el 15% "no les da". Bajas a 8%. Los restaurantes piden crédito a 15 días. No lo tienes. Tres proveedores detectan que las órdenes que les llegan son de clientes que ya tenían.

**Mes 6.** Retención semana 4: 20%. Revisas y los restaurantes están pidiendo directo por WhatsApp a los proveedores que conocieron por ti. GMV cae 60%.

**Mes 7-8.** Pivotas a "SaaS de gestión de compras para restaurantes" cobrando USD 30/mes. Convierten 6. Tus devs están construyendo features para esos 6.

**Mes 9-10.** Pivotas a logística propia para "controlar la experiencia". Rentas una camioneta. Mermas del 12%. Pierdes dinero en cada entrega.

**Mes 12.** Te queda runway para 2 meses. Intentas levantar puente. Los ángeles preguntan por la retención. Fin.

La causa raíz no fue ejecución: fue que **construiste antes de validar si alguien paga y si se quedan.**

---

## 5. Con USD 10K para validar

Regla número uno: **cero dólares en desarrollo.** Si gastas un peso en código antes de la semana 10, fracasaste la validación.

**Semanas 1-2 — Inmersión (USD 500 en transporte y cafés).**
Acompaña a 15 dueños de restaurantes pequeños en su compra, a la hora que compran. No entrevistas: observación. Anota con quién compran, cuánto, con qué frecuencia, cómo pagan, a cuántos días, qué pasa cuando algo falla. Pregunta: "¿cuándo fue la última vez que cambiaste de proveedor y por qué?" Si la respuesta es "nunca" o "cuando me falló", tu hipótesis de "pierden tiempo llamando" está muerta.

Haz lo mismo con 10 proveedores. Diles la cifra: "Te traigo clientes nuevos a cambio de 15% del pedido". Mira su cara. Luego pregunta cuánto sí pagarían. Ese número es tu take rate real.

**Semanas 3-10 — Marketplace manual por WhatsApp (USD 3K).**
Tú eres la app. Un número de WhatsApp Business, un Excel, un formulario. Reclutas 20 restaurantes y 8 proveedores. Recibes pedidos, los enrutas, confirmas entregas, resuelves quejas. **Cobras comisión real desde el pedido uno.** Si no cobras, no estás validando nada.

Métricas que importan (y solo estas):
- % de restaurantes que hacen un segundo y cuarto pedido
- % del gasto total del restaurante que pasa por ti (pregúntales cuánto compran en total)
- Cuántos se van directo con el proveedor en la semana 3 (llámalos y pregunta, no te van a mentir)
- Take rate que el proveedor acepta sin negociar
- Horas de tu tiempo por pedido

**Semanas 11-12 — Prueba el producto alternativo (USD 2K).**
Porque tu hipótesis probablemente murió, prueba las dos que sí podrían vivir:
- **Crédito:** ofrece a 10 restaurantes pagar a 15 días sobre pedidos que tú financias con los USD 10K restantes. Mide demanda y mora. Si demanda es alta y mora baja, tu negocio es fintech con distribución, no marketplace.
- **Herramienta para el proveedor:** ofrécele a 5 proveedores llevarles pedidos y cobranza ordenados por USD 50/mes. Si pagan, tu cliente es el proveedor, no el restaurante.

**Guarda USD 4K.** Los vas a necesitar para la siguiente iteración cuando los números te digan algo que no esperabas.

**Criterio de muerte, decidido antes de empezar:** si en la semana 8 la retención de cuarto pedido es menor a 40%, o el take rate aceptado es menor a 6%, cierras esta tesis y pasas a la siguiente. Escríbelo hoy y fírmalo. El founder que no define su criterio de fracaso antes es el que gasta USD 300K descubriéndolo.

---

**Resumen brutal:** Tu hipótesis no es sobre un problema, es sobre una solución que te gusta. "Pierden tiempo llamando" es lo que un dueño de restaurante le dice a un emprendedor en una entrevista de 20 minutos para ser amable. El problema real está en la confianza, el crédito, la calidad y la informalidad, y ninguno de esos se resuelve con un marketplace al 15%.

Sal a las 5am diez veces y vuelve con datos. Ahí sí hablamos de cheque.