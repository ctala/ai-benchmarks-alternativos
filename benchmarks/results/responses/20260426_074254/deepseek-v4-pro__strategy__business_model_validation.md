# DeepSeek V4 Pro — strategy/business_model_validation

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 6.88 | quality: 9.36
- latency_total: 120.655s | tokens_per_second: 30.5
- input_tokens: 188 | output_tokens: 3686
- judge_score: 4.6 | justificación: 

## Respuesta completa

Vale, deja el pitch deck. Actuaré como el VC más escéptico que te va a crujir en el comité. No voy a aplaudir el sueño, voy a destriparlo. Aquí van las preguntas que yo te haría, directo a la yugular.

---

**1. Identifica los 5 riesgos principales de este modelo (no me des los obvios de “ejecución”, dime los que te van a matar).**

- **Riesgo #1: Desintermediación inmediata y total.** El primer día que un restaurante recibe su pedido de tomates, la caja lleva la factura del proveedor con su WhatsApp. Ambas partes hacen cuentas: si la comisión es del 15%, el proveedor pierde margen brutal en un negocio de volúmenes y precios volátiles. El restaurante prefiere ahorrarse ese 15% pidiendo directo. La próxima transacción ocurre por fuera. Tu marketplace se convierte en un costoso lead gen desechable. ¿Cómo evitas que te salten sin quemar todo tu margen en penalizaciones inaplicables?

- **Riesgo #2: Las “micropérdidas” hacen imposible la economía unitaria.** El ticket promedio de un pequeño restaurante a un proveedor local puede ser de $30-$100. Tu comisión de 15% son $4.5-$15 brutos. De ahí tienes que pagar adquirencia, impuestos, soporte, reembolsos por producto en mal estado (putrefacción, golpes) y costo de adquisición de cliente (CAC). Si captar un restaurante te cuesta $50 en campañas o fuerza de ventas, necesitas 11 transacciones solo para recuperar el CAC, sin contar el churn. Los números no cierran a menos escala. ¿Cuál es tu CAC real y cuántas transacciones mensuales por restaurante necesitas para no destruir valor?

- **Riesgo #3: Caos logístico que te convierte en responsable de mermas y daños.** El tendero de la esquina entrega en una moto, el restaurantero revisa la cebolla y si está fea la devuelve. Tú metes la plataforma en medio y te conviertes en el árbitro de cada disputa. Pretendes ser solo un “marketplace de pedidos” pero el usuario va a exigirte que el producto llegue en el estado prometido. O montas una capa logística absurdamente costosa, o tu tasa de chargebacks y reseñas negativas te hunde. ¿Quién asume la responsabilidad cuando llega una remesa de cilantro pasado y el restaurante no puede servir su menú del día?

- **Riesgo #4: Percepción de precio inflado contra métodos actuales.** El proveedor, para defender su margen, te infla el precio un 18% para compensar tu 15% de comisión. El restaurante, que tiene un celular lleno de contactos de confianza, nota que en tu app el kilo de pechuga está más caro que por teléfono. Inmediatamente asocia tu marca con “más caro” y se desinstala la app. El ahorro de “tiempo” que prometes es intangible comparado con un sobrecosto tangible en el plato. ¿Vas a competir por precio o por conveniencia cuando la conveniencia hoy es un audio de WhatsApp?

- **Riesgo #5: El problema que dices resolver no duele tanto como crees.** La hipótesis “pierden mucho tiempo llamando” asume que ese tiempo es ineficiente. Para un cocinero de fonda, la llamada diaria al de las verduras es su ritual de control de calidad, su negociación y su crédito. “Llamar al proveedor” no son 15 minutos perdidos, son 15 minutos donde ajusta precios según la plaza, pide fiado y afianza una relación que le saca de apuros. Si digitalizas eso, le quitas flexibilidad y crédito. ¿Qué dolor real estás resolviendo que sea más fuerte que la relación personal y el crédito informal que hoy le salvan la caja?

---

**2. ¿Por qué esto podría NO funcionar en LATAM específicamente? (La trampa de copiar modelos del norte).**

Lo que tú estás trayendo es un Faire o un Choco para Pymes, pero LATAM te va a escupir por estas grietas:

- **El crédito y el “fiado” mandan.** El 80% de las transacciones entre restaurante pequeño y proveedor local manejan plazos de pago informales (semanal, quincenal). Tú metes un botón de pago con tarjeta o transferencia inmediata y matas ese flujo. Sin crédito, el restaurante no sobrevive su capital de trabajo. Si tú no financias, no compran.
- **Fragmentación extrema y desconfianza.** Los proveedores locales muchas veces son microinformales sin RUC, sin catálogo digital, que acopian en centrales de abastos. No quieren registros digitales porque eso implica facturación e impuestos. Sacarlos de la informalidad es una guerra cultural. Tu 15% es una bandera roja para Hacienda.
- **Conectividad y adopción digital en la cocina.** El chef de un pequeño restaurante no está con un tablet en la barra; está entre fuegos con las manos manchadas. El pedido lo hace al oído o con un audio de WhatsApp. Cambiar WhatsApp por un app es una fricción brutal que requiere un cambio de hábito generacional.
- **Última milla perecedera y caótica.** En ciudades como Lima, CDMX o Bogotá, el tráfico, la inseguridad y la informalidad del repartidor hacen que coordinar entregas de perecederos en ventanas de 30 minutos sea más riesgoso que en Amsterdam. Un retraso de 2 horas en la entrega de mariscos te cuesta una denuncia sanitaria. El proveedor local ya sabe cómo lidiar con ese caos; tú no.
- **La “mordida” y el sobreprecio son el negocio.** El proveedor fideliza al restaurante dándole un regalo, un descuentillo por fuera de factura, o pagando la cerveza. Tu plataforma transparente revienta ese ecosistema opaco de favores que aceita el suministro. ¿Por qué un proveedor te va a pagar 15% si hoy cierra tratos con un descuento en efectivo que no tributa?

---

**3. ¿Qué tendría que ser verdad para que esto funcione? (Key Assumptions, sin anestesia).**

Tú me estás pidiendo plata apostando a estas hipótesis. Si una sola es falsa, se acabó.

- **H1 (Valor real del tiempo):** El restaurante pequeño valora tanto el tiempo de “búsqueda y llamada” que está dispuesto a pagar un sobreprecio neto del 10-15% en la materia prima. Sin sobreprecio, no hay comisión posible. Si el ahorro en tiempo no se monetiza en más mesas servidas o menos desperdicio, es un espejismo.
- **H2 (Oferta uniforme y digitalizada):** Existe un número suficiente de proveedores locales dispuestos a mantener un catálogo de precios y stock en tiempo real, aceptar pagos electrónicos, emitir comprobante fiscal y ceder el 15% de un margen habitualmente inferior al 10%. (Spoiler: la mayoría tiene margen neto <8%, la comisión te los devora).
- **H3 (Ausencia de multihoming y trampa):** Ambos lados usan tu app solo para el primer match y no derivan inmediatamente la relación a WhatsApp. Y tú tienes herramientas (seguro de calidad, crédito puente, descuentos por volumen) lo suficientemente potentes para que el costo de saltarte sea peor que pagar la comisión a perpetuidad.
- **H4 (CAC simbiótico):** Captar un restaurante cuesta menos de $20 y el restaurante realiza más de 15 pedidos al mes por la plataforma (Lifetime Value > 3x CAC). Dado el ticket chico, necesitas densidad extrema en 2 km a la redonda; si no hay hiperlocalidad, mueres en costos de distribución.
- **H5 (Riesgo logístico externalizable):** La calidad, la merma y el tiempo de entrega son problemas que los proveedores resuelven solos, sin que tu marca se manche. Pero el usuario te va a castigar a ti con la estrella. Tendrías que tener un rating de proveedores tan fiable que haga de policía de calidad gratuita. Eso no existe.

---

**4. ¿Cuál es el escenario donde fracaso rápido y por qué?**

Fracaso rápido: **la “app directorio” sin transacciones.** Desarrollas un MVP bonito, inviertes ese dinero en un diseñador y un AdWords. Consigues 200 restaurantes registrados y 30 proveedores que ponen su lista de precios dos veces. Los pedidos iniciales son 5 en la primera semana, pero para la tercera los restaurantes ya se llevaron el WhatsApp del proveedor. Tú no tienes capa de pagos integrada (porque es complejo), así que no retienes la transacción. Los proveedores dejan de actualizar catálogo porque no reciben pedidos por la app. Los restaurantes reclaman que el apio llegó mustio y tu soporte no da abasto. Quemas $8K en anuncios y $2K en desarrollo. En tres meses, tu plataforma es un cementerio de catálogos desactualizados y conversaciones desiertas. El experimento termina con menos de 10 transacciones completadas, un churn del 90% y la revelación de que el “dolor de llamar” se curó con un grupo de WhatsApp de contactos de confianza. Cierras antes del mes 6.

**Por qué:** Porque construiste para un problema sin validar que alguien pagaría por resolverlo, y porque el marketplace sin pago integrado es un burdel donde todos se fugan con el cliente al primer contacto.

---

**5. Si solo tuviera $10K para validar, ¿qué harías? (y no me digas “crear un MVP en Bubble”).**

Con $10K te prohíbo escribir una línea de código. Esos $10K son para el experimento más sucio y real que existe: **el triángulo del concierge manual con tu propio sudor.**

Haría esto:

1. **Elige una sola categoría de producto perecedero crítico y acotado (ej. “pescados y mariscos frescos” o “verduras orgánicas”) en un radio de 5 manzanas.** Nada más.
2. **Conviértete tú en el marketplace.** Busca 3 proveedores locales reales y negocia con ellos: “Te voy a traer pedidos en firme, yo coordino la entrega, te pago de contado contra entrega, quiero un descuento del 10% sobre tu precio de mostrador. El restaurante pagará tu precio de mostrador, yo me quedo ese 10% de margen (no 15%, seamos realistas). Sin app. Sin factura digital.” Esto prueba si tú puedes capturar margen.
3. **Recluta 5-8 restaurantes a los que les lleves una hoja física con los productos del día (un PDF por WhatsApp).** Tú tomas los pedidos por WhatsApp, los centralizas, compras a los proveedores por tu cuenta y se los llevas en un horario fijo usando un repartidor de confianza a sueldo fijo o un taxi.
4. **Mide tres números con obsesión enfermiza:** a) % de pedidos recurrentes en 30 días, b) margen bruto después de pagar gasolina y mermas, c) tasa de fuga (cuántos te piden el contacto directo y te botan). Si después de 8 semanas no logras que al menos el 50% de los restaurantes pidan 3 veces por semana sin pedirte el número del proveedor, el modelo está muerto.
5. **Con $2K de los $10K, cubre los pedidos iniciales y las pérdidas de producto dañado.** El resto guárdalo para iterar el pitch con datos reales, o para devolverlo a tu bolsillo cuando veas que los tenderos te regañan por el precio y los cocineros te gritan por el sabor del pescado.

Eso es lo que yo te preguntaría y lo que te exigiría ver. Sin un cuaderno lleno de esas transacciones manuales, con las manos oliendo a pescado, no tienes nada que valga una inversión. Ahora dime, ¿tienes respuestas o quieres modificar el modelo?