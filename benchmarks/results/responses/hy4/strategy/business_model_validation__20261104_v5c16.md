# Tencent Hy4 — strategy/business_model_validation

- model_id: `tencent/hy4`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 62.147s | tokens_per_second: 83.6
- input_tokens: 206 | output_tokens: 5198

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

Antes de empezar: el **15%** me levantó una ceja. Y lo de *"pierden tiempo llamando"* me levantó la otra. Ya he visto morir cuatro de estos en México, Colombia y Argentina con el mismo deck. Vamos al grano, sin cortesías.

---

### 1. Los 5 riesgos principales (y ninguno es "la competencia")

1. **El 15% es confiscatorio.** Un restaurante pequeño opera con *food cost* del 30% y margen neto del 6–10%. Meterle un 15% sobre el insumo se come todo su margen. El proveedor no lo va a absorber (él vive con márgenes del 8%). Resultado: o lo subsidias tú con VC cash (humo), o se lo cobras al chef... y se abre el WhatsApp. No hay tercera opción.
2. **Disintermediación (leakage) estructural.** En Uber no conoces al conductor. Aquí, en el **primer delivery**, el repartidor le deja su número al cocinero. Se conocen, se fían, se arreglan. Tu plataforma es un costoso *blind date* que te cobra por presentarlos. No tienes *lock-in* ninguno.
3. **Estás curando un problema de consultor, no de cocinero.** El chef no "pierde" tiempo llamando: esa llamada a las 6:00 AM es su control de calidad, su negociación de precio del día y su gestión del *fiado*. Digitalizarlo le **quita poder**. Le estás pidiendo que cambie control por un formulario. Mal trade.
4. **No eres SaaS, eres cold-chain con reclamos.** Perecederos, ventanas de entrega de 45 min antes del servicio, y el tomate que llega magullado. Adivina a quién le reclaman: a ti. Un solo crédito por producto podrido se traga la comisión de 20 pedidos. Tu *unit economics* no aguanta la primera devolución.
5. **Densidad sin escala.** "Local" significa que en cada barrio reinicias la liquidez desde cero. Pagas CAC doble (traer proveedor **y** restaurante) en la Roma, otra vez en Chapinero, otra en Miraflores. El software no te da economías de escala; esto es un negocio de operaciones calle por calle disfrazado de tech.

---

### 2. Por qué en LATAM esto se estrella más rápido que en otros lados

* **El incumbente ya ganó y se llama WhatsApp.** Nota de voz + Yape/PIX/SPEI/transferencia + "Don Chuy, mándame el maduro". Tiene 20 años de PMF, CAC = $0 y take rate = 0%. Tu "solución digital" es un **downgrade**: les pides usuario, password, catálogo y tarjeta, cuando ya resolvieron con un audio de 12 segundos.
* **Rompes el pegamento financiero: el fiado.** El proveedor le da 15 o 30 días al restaurante de confianza. Tú, para capturar tu 15%, exiges pago al confirmar. Le estás quitando el capital de trabajo informal que sostiene la relación. Ningún banco te va a prefinanciar a 400 taquerías sin historial para que tú hagas de banco.
* **Informalidad fiscal.** La mitad de tus proveedores son mayoristas de tianguis/mercado con facturación parcial o nula. Meter una pasarela + comisión trazable los obliga a formalizarse. Huyen antes del onboarding.
* **Inflación / pricing intradía.** El aguacate amaneció a un precio el martes y a otro el miércoles. Tu catálogo se desactualiza en 4 horas. El chef llama **justamente** para preguntar *"¿a cómo amaneció hoy?"*. Un precio estático en LATAM es un bug fatal, no un feature.
* **Confianza > Eficiencia.** Aquí la compra es relacional, no transaccional. Le compran a Don Chuy porque les aparta el mejor corte, no porque tenga un UI bonito. Vender "ahorro de minutos" a alguien que mide su riesgo en "¿me va a quedar mal el servicio de hoy?" es no entender el oficio.

---

### 3. Qué tendría que ser verdad (si una falla, mueres)

No me des una lista de deseos. Dame binarios:

1. **Tu hipótesis inicial es falsa, y la reemplazas por esta:** el dolor no es el *tiempo*, es el **quiebre de stock**. El chef paga un sobreprecio solo si tú garantizas que a las 6:00 AM *nunca* falta el cilantro, porque un turno perdido le cuesta $500, no 20 minutos.
2. **El 15% sale del spread, no del bolsillo del chef.** El proveedor tiene sobrecapacidad muerta (camión volviendo vacío) y te la cede a mayorista − X%. Si no consigues esto, tu modelo de ingresos está muerto en el papel.
3. **Retienes un rehén: el pago o el camión.** Si la logística y el cobro pasan por ti *siempre*, no hay leakage. Si solo pasas el contacto, eres un directorio amarillo con funding.
4. **Monetizas ANTES del match, no en la transacción.** (La incómoda): tendría que ser verdad que el take rate es el modelo **equivocado**, y que el negocio real es SaaS de routing para el proveedor o *factoring* del fiado. Si te aferras al 15%, ya perdiste.
5. **Densidad quirúrgica:** en un radio de 3 km un solo vehículo hace 6 drops antes de las 7:00 AM. Si haces 2 drops, el diésel se come tu comisión.

---

### 4. El escenario de fracaso rápido (y es más feo de lo que crees)

**Mes 1:** Consigues 20 restaurantes y 5 proveedores en un barrio. Metes $50 de descuento por primer pedido. Haces $30K GMV. Mandas el update a los LPs: *"Tracción 🚀"*.

**Mes 2:** El GMV de la app cae a $4K... pero los pedidos reales en la calle siguen siendo exactamente los mismos 20.

**Por qué moriste:** El mes 1 fue novedad + subsidio. En la primera entrega, el proveedor le escribió al chef: *"Jefe, pa' la próxima me manda directo al audio y le quito el recargo de la app 😉"*. A los 14 días ya cerraron trato por fuera, con fiado incluido. Tu CAC fue $120/restaurante, tu LTV fue **2 transacciones**, tu take rate efectivo fue **1.8%**, y te quedaste con el soporte, el reclamo del tomate podrido y cero ingresos.

No fracasas por falta de adquisición. Fracasas por **leakage en el primer ciclo de recompra**. Y te das cuenta tarde porque mediste *signups* en vez de medir *reorders sin que tú los recuerdes*.

---

### 5. Con $10K, qué haría (y qué te prohíbo hacer)

**Prohibido:** Un Figma. Un landing. Un `.env`. Un dashboard. Si me vienes a los 30 días con una app construida, te corto el cheque y te pido que devuelvas el resto. Cero líneas de código.

**El plan (90 días, tú en la calle a las 5:30 AM):**

* **$0 tech.** Google Sheet + un WhatsApp Business + una camioneta/repartidor alquilado por día. Tú eres el middleware.
* **Semana 1–2 — Mata tu propia hipótesis:** Ve a 30 cocinas. No preguntes *"¿perderías tiempo?"* (te van a decir que sí por educados). Pregunta: **"¿Cuánta plata perdiste AYER porque no llegó el insumo o te llegó caro?"**. Si te responden *"me da igual, le puse cebolla"*, cierra la libreta y vete a otro problema. Cuantifica en pesos, no en minutos.
* **Semana 3–6 — El test del 15% (sin anestesia):** A 10 de esos diles: *"Mañana a las 6 te llega todo, pero te cuesta un 15% más que Don Chuy. ¿Firmas?"*. **Sin descuento. Sin subsidio. Sin coupon.** Cuenta cuántos te mandan a volar. Si menos de 7 aceptan, mata el take rate ahí mismo, en la acera, y no lo vuelvas a mencionar en un pitch.
* **Semana 7–10 — Mide el día exacto del puente:** Opera los pedidos tú. Al día 3 llama al proveedor y pregúntale cuántos le pidieron directo por fuera. Anota el **día D**. Ese número, no el GMV, es tu LTV real.
* **Semana 11–12 — El pivot casi seguro:** Con los ~$7K que te quedan (gasolina + tu sueldo de hambre), prueba cobrarle **$30/mes fijos al proveedor** por la ruta optimizada y deja la transacción en 0%. O prueba prefinanciar el fiado a 7 días con un spread. Ahí sí hay rehén.

**Criterio de kill:** Si al día 30 el reorder no entra por *tu* WhatsApp sin que tú hayas mandado el recordatorio, devuélveme los $10K.

---

**Remate, y grabátelo antes del próximo pitch:** no me digas *"es el Shopify de los ingredientes"*. En LATAM ese Shopify ya existe, tiene 20 años de PMF, cero CAC, cobra 0% y funciona con notas de voz. Tienes que demostrarme que eres el **banco** o el **camión**. Si solo eres el **directorio**, siguiente. 

¿Qué número del test del 15% te da miedo salir a medir mañana? Ese es el único que me interesa.