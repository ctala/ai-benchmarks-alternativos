# Muse Spark 1.3 — strategy/business_model_validation

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.34 | quality: 10.0
- latency_total: 35.853s | tokens_per_second: 99.2
- input_tokens: 169 | output_tokens: 3557

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

Voy a ser directo: he visto este pitch 20 veces. 19 murieron. Uno de ellos se llamaba Frubana y quemó **$366M intentando exactamente lo que describes en LATAM.** Cerró México, despidió a cientos, y pivotó porque el modelo no daba.

Tu hipótesis de "pierden tiempo llamando" es de gringo con MacBook, no de taquero en CDMX. No tienes un problema de tecnología. Tienes un problema de márgenes, confianza, crédito y logística.

Aquí va el teardown:

### 1. Los 5 riesgos principales (los que te matan)

**1. Desintermediación brutal. Tu take rate es un impuesto que nadie quiere pagar.**
Restaurantes pequeños operan con 10-15% de margen neto. Proveedores de abasto operan con 8-12%. ¿De dónde sale tu 15%? En cuanto conectas a Juan del restaurante con Pedro del tomate, se pasan el WhatsApp y te bypasean a la segunda compra. Te conviertes en un directorio gratuito muy caro.

Pregunta de VC: ¿Cuál es tu tasa de repeat a 60 días sin subsidios? Si es <70%, estás muerto.

**2. Unit economics imposibles.**
Haz la matemática: Ticket promedio restaurante pequeño en LATAM: $150 - $300 USD por pedido, 2-3x por semana. Digamos $800/mes por restaurante.
Tu 15% = $120/mes bruto por restaurante.
Réstale: CAC, soporte por WhatsApp (porque te van a llamar igual), devoluciones por producto podrido, cobranza, pasarela de pago (3.5%), logística de última milla. Te quedan -$50.
Para llegar a $1M ARR necesitas $6.6M en GMV. Eso son ~825 restaurantes comprando perfecto cada mes sin churn. Con un churn mensual del 15% (normal en este segmento), necesitas adquirir 150+ restaurantes nuevos al mes solo para no decrecer.

**3. No resuelves el problema real. El problema no es "llamar", es crédito y calidad.**
El dueño no llama a 5 proveedores porque le encante. Lo hace porque: uno le fía a 15 días, otro le da mejor calibre de aguacate, otro le llega a las 5am. Tu app no compite contra llamadas. Compite contra **el fiado, el compadrazgo y el "te lo repongo mañana".** Si no ofreces crédito informal sin buró y no absorbes la merma, no eres mejor que Don Chucho que lleva 10 años surtiéndole.

**4. Chicken-and-egg con oferta basura.**
Proveedores locales: 80% no tienen inventario digital, ni facturación, ni flota, ni foto decente. Les pides subir catálogo y te mandan a volar. Les vas a tener que rogar, subsidiar, y hacerles el onboarding a mano. Y cuando por fin entran, incumplen: llegan tarde, traen 8kg en vez de 10kg, calidad inconsistente. ¿A quién culpa el restaurante? A ti. Te conviertes en su call center de quejas.

**5. Frecuencia alta, pero lealtad cero. Te cambian por $0.10.**
Esto no es Uber Eats. Aquí el comprador es un cocinero obsesionado con el precio del jitomate. Si tu proveedor sube $0.20/kg, se van con el de la esquina. No hay lock-in. Tu CAC se paga en 4-6 meses, pero tu vida promedio del cliente es de 2.5 meses. Estás comprando clientes que pierden dinero.

### 2. Por qué podría NO funcionar en LATAM específicamente

1.  **WhatsApp ya ganó.** No necesitan tu app. Ya tienen grupos con proveedores, notas de voz, fotos del producto en el mercado a las 4am. Es gratis, instantáneo y no cobra 15%.
2.  **El fiado manda.** En México, Colombia, Perú, el 60-70% de estas transacciones son a crédito informal: "págame el viernes". ¿Vas a financiar capital de trabajo a restaurantes que no son sujetos de crédito? Si no lo haces, no te usan. Si lo haces, te quiebran los impagos.
3.  **Informalidad fiscal.** Ni el restaurante quiere factura de todo (para no pagar ISR), ni el proveedor puede facturar. Tu marketplace que retiene 15% y exige factura electrónica rompe el trato implícito.
4.  **Logística es un infierno.** Tráfico CDMX/Bogotá/Lima, sin cadena de frío, robos en ruta, centrales de abasto (Corabastos, Central de Abastos CDMX) que ya son ultra-eficientes en precio y cierran a las 3am. No puedes competir con ese costo.
5.  **Relación > Conveniencia.** En LATAM se compra a quien se conoce. "Es mi primo", "es de mi pueblo". No vas a romper 10 años de confianza con un UI bonito.
6.  **Ticket demasiado bajo y fragmentado.** No es USA con Sysco. Son miles de tienditas comprando $20 de cilantro hoy y $30 de pollo mañana. El costo de servirlos te mata.

Frubana, Alima, etc. ya demostraron esto con cientos de millones. ¿Qué sabes tú que ellos no sabían?

### 3. Qué tendría que ser VERDAD para que funcione (Key Assumptions)

Si una sola de estas es falsa, mueres. Todas tienen que ser verdaderas:

1.  Que el restaurante está dispuesto a pagar 12-15% MÁS por el mismo producto solo por no llamar. (Yo creo que es falso. Quieren pagar 10% MENOS).
2.  Que puedes lograr densidad hiperlocal: >30 restaurantes activos en un radio de 3km pidiendo al mismo pool de 5 proveedores, 3x por semana.
3.  Que el proveedor cumple >98% OTIF (on-time, in-full, calidad) sin que tú pongas la logística. Si tú pones la logística, tu margen desaparece.
4.  Que la tasa de leakage <20% después del 3er pedido. Es decir, no te bypasean.
5.  Que cobras por adelantado o a max 7 días sin impago >3%. Sin convertirte en banco.
6.  Que tu CAC < $80 USD y tu payback < 90 días. Con fondas que cierran cada 8 meses.

Ve y valida cada una con datos, no con encuestas de "¿usarías esto?". Nadie te dice la verdad en encuestas.

### 4. Escenario donde fracasas RÁPIDO (90 días)

Mes 1: Consigues 25 restaurantes piloto en una colonia. Felices. Haces todo manual por WhatsApp. GMV sube.
Mes 2: 12 de ellos ya contactaron directo al proveedor y negocian 8% más barato sin ti. Otros 5 se quejan porque el proveedor llegó 2 horas tarde y el pescado venía caliente. Tú pones la cara, reembolsas de tu bolsillo.
Mes 3: Te quedan 8 activos. Los proveedores te exigen volumen o se van. Los restaurantes te exigen crédito o se van. Estás subsidiando entregas, quemando caja en repartidores, y eres el jamón del sándwich. Churn 60%. Te das cuenta que no eres un marketplace, eres un coyote con una landing page.

Por qué: resolviste el descubrimiento, pero el valor está en **crédito + cumplimiento logístico**, que es lo más caro y difícil de escalar.

### 5. Si solo tuvieras $10K, qué haría yo (cero código)

Prohibido construir una app. Si escribes una línea de código, ya perdiste.

**$0 en desarrollo. Todo en validación concierge en UN barrio, UN producto.**

Semana 1-2 ($1,500): Elige 1 micro-nicho doloroso. No "ingredientes". Elige: "verdura fresca para fondas en la Roma/Condesa" o "pollo para pollerías en Kennedy, Bogotá". 10 restaurantes en 10 cuadras, 3 proveedores máximo. Nada más.

Semana 3-8 ($6,000): Sé el marketplace manual. Crea un grupo de WhatsApp Business + Google Sheet. Tú tomas pedidos a las 8pm, compras a las 4am en la central, coordinas entrega. Cobra el 15% REAL desde el día 1. Sin descuentos. Sin "es gratis en beta".

Mide solo esto (kill criteria):
- ¿Repiten 3x/semana por 4 semanas seguidas PAGANDO el 15%?
- ¿Qué % te bypasea en la semana 3? Si >30%, mata la idea.
- ¿Te piden crédito? ¿Cuántos días? ¿Cuántos no te pagan?
- ¿Cuál es tu costo real por entrega y por queja?

Semana 9-10 ($2,500): Intenta subir precio o quitarte del medio. Dile al restaurante: "a partir de ahora todo por este link con prepago". Si te dicen que no, no tienes negocio, tienes un servicio de mandados.

Si después de 100 transacciones manuales no tienes 15 restaurantes que lloren si les quitas el servicio Y te dejan >$50 de contribución marginal cada uno después de logística e impagos, **no levantes capital. Mata la idea.**

Mi apuesta: con $10K descubrirás que lo que quieren no es un marketplace. Quieren a alguien que les fíe y les responda cuando el tomate sale mal. Eso es una fintech de crédito + logística, no un app de pedidos. Y eso cuesta $10M, no $10K.

¿Todavía crees en tu hipótesis? Tráeme: ticket promedio real, frecuencia real, tasa de repeat pagando 15% en 30 días, y costo de entrega por pedido. Sin eso, no hay pitch, hay fantasía.