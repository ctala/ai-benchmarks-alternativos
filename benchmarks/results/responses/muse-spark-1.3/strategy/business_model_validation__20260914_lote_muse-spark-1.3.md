# Muse Spark 1.3 — strategy/business_model_validation

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.35 | quality: 10.0
- latency_total: 36.685s | tokens_per_second: 93.0
- input_tokens: 168 | output_tokens: 3413

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

Voy a ser directo: tu idea suena bien en un deck, pero en LATAM ya se intentó con $400M y murió. Se llamaba Frubana. Quebró haciendo exactamente esto.

Si me picheas esto, te destruyo en 10 minutos. Aquí va:

### 1. Los 5 riesgos principales de tu modelo

**1. Tu take rate del 15% es un suicidio.**
¿Quien lo paga? Un restaurante pequeño en LATAM opera con 10-15% de margen neto. Un proveedor local con 15-20%. Tu 15% no sale del aire, sale de alguien que ya no gana nada.
Si lo cobra al proveedor, sube el precio 15%. El restaurante compara con la Central de Abastos / Mercado y te deja. Si lo cobra al restaurante, te manda a la mierda en la primera compra. No eres Stripe, eres un impuesto.

Pregunta de VC: Muéstrame el P&L de un restaurante que te paga 15% más y sigue vivo.

**2. Fuga (disintermediation) del 100%.**
Conectas a Juan el taquero con Don Pedro el del jitomate. Hacen 1 pedido por tu app. Se pasan el WhatsApp. Pedido #2 va por fuera. Cero comisión para ti.
En B2B de bajo ticket y alta frecuencia, el marketplace solo sirve para el descubrimiento. Después eres irrelevante.

Pregunta de VC: ¿Cuál es tu tasa de recompra en la plataforma al mes 3 sin forzarla? Si es <70%, estás muerto.

**3. No resuelves el problema real. Tu hipótesis es gringa.**
Dices: "pierden mucho tiempo llamando a múltiples proveedores". Falso. El restaurante pequeño NO quiere 20 proveedores. Quiere 2-3 de confianza que le den: 1) precio más bajo, 2) fiado/crédito a 7-15 días, 3) entrega a las 5am y le cambian el producto podrido sin factura.
Eso no lo resuelve una app bonita. Lo resuelve la relación de 10 años y el crédito informal.

Pregunta de VC: ¿Cuántos restaurantes has visitado a las 4am? ¿Te pidieron una app o te pidieron precio y crédito?

**4. Pesadilla operativa: perecederos + proveedores informales.**
Tus suppliers no tienen inventario, ni ERP, ni repartidores, ni facturación. Tienen una camioneta vieja y un cuaderno. Tú prometes entrega digital, pero el jitomate llega podrido, tarde e incompleto. ¿Quién absorbe la merma? ¿Tú? Te fundes. ¿El restaurante? Te deja 1 estrella y vuelve a llamar a su compadre.

Pregunta de VC: ¿Quién paga cuando el pedido llega mal? Calcula tu costo de reembolso + soporte por pedido.

**5. Unit economics imposibles.**
Hagamos matemática de primaria:
Ticket promedio restaurante chico: $2,000 MXN (~$100 USD), 3x por semana = ~$1,200 USD/mes.
Tu 15% = $180 USD/mes bruto por restaurante *si* no hay fuga.
Para llegar a $50k USD de revenue necesitas ~280 restaurantes comprando perfecto cada semana. Con churn de restaurantes en LATAM (50% muere en 2 años) y CAC de venta en campo ($100-200 USD por restaurante), nunca llegas a LTV/CAC >3.

Pregunta de VC: ¿Cuál es tu CAC real puerta por puerta y cuántos meses tarda en pagarse?

### 2. Por qué podría NO funcionar en LATAM específicamente

Porque LATAM no es San Francisco:

1.  **WhatsApp YA es tu competencia y es gratis.** Todo se cierra por WhatsApp + llamada + nota de papel. No van a descargar otra app para pagar 15% más.
2.  **Efectivo y fiado mandan.** 60%+ paga contra entrega en efectivo. El proveedor le fía al restaurante porque lo conoce. Tú quieres tarjeta y prepago. No va a pasar.
3.  **Obsesión por precio, no por conveniencia.** El dueño prefiere ahorrarse $50 pesos e ir al mercado que pagar por "ahorrar tiempo". Su tiempo vale $0, su margen vale todo.
4.  **Informalidad total del lado supply.** Sin factura, sin stock en tiempo real, sin SLA. No puedes construir software confiable sobre caos operativo.
5.  **Densidad y logística.** Última milla cara, tráfico infernal, frío inexistente. No puedes agregar 20 proveedores dispersos y entregar fresco y barato.

Frubana levantó +$400M para esto en México, Brasil y Colombia y tuvo que cerrar operaciones. Choco se estrelló igual. ¿Qué sabes tú que ellos no sabían con 500 ingenieros?

### 3. Qué tendría que ser verdad para que funcione (Key Assumptions)

Si una sola de estas es falsa, quiebras. Apúntalas:

1. Que el restaurante ordene >3x por semana, ticket >$1,500 MXN, y repita >6 meses seguidos EN tu plataforma sin irse a WhatsApp.
2. Que el proveedor acepte darte 15% SIN subirle el precio al restaurante (es decir, que vea tanto volumen incremental que le compense).
3. Que estés dispuesto a NO tocar logística al inicio y que aún así la calidad sea consistente. O que subsidias logística y no te mata.
4. Que resuelves crédito: o das fiado tú (necesitas fintech, no marketplace) o los proveedores te dejan replicar el fiado en tu app.
5. Que tu CAC < $800 MXN y tu churn mensual <5%. Si no, los números jamás cierran.

Hoy no tienes prueba de NINGUNA.

### 4. Escenario donde fracasas rápido (y es el más probable)

Mes 1-2: Construyes la app. Gastas $10K en desarrollo en vez de vender.
Mes 3: Consigues 30 restaurantes piloto con descuentos. 10 proveedores que suben fotos falsas de inventario.
Mes 4: Primer caos: 40% de pedidos llegan tarde/incompletos. Reembolsos te comen el margen. Tienes que meter soporte por WhatsApp manual.
Mes 5: Restaurantes descubren al proveedor bueno y se lo saltan. Te quedas con los malos proveedores y los restaurantes quejumbrosos.
Mes 6: Proveedores se quejan del 15% y suben precios. Restaurantes comparan y ven que la Central es 20% más barata. Churn del 60%.
Te quedas sin caja, sin retención, con una app que nadie usa. Fracaso clásico de marketplace B2B.

Te vas a morir no por falta de tecnología, sino por fuga + márgenes + operación.

### 5. Si solo tuvieras $10K para validar, ¿qué haría?

**NO construyas la app. Prohíbetelo.** Si escribes una línea de código, ya perdiste.

Con $10K haría un Concierge MVP sucio en UNA colonia, 8 semanas:

**Semanas 1-2: Vende sin producto.**
Elige 1 zona densa (ej: 20 cuadras con 100 fondas). Visita 50 restaurantes. No preguntes "¿usarías una app?". Eso es basura. Ofrece: "Te traigo jitomate, cebolla y pollo mañana a las 6am 5% más barato que tu proveedor, me pagas contra entrega. ¿Sí o no?" Si menos de 20 te dicen SÍ y te dan pedido real, mata la idea.

**Semanas 3-8: Opera como coyote con WhatsApp.**
Crea un grupo de WhatsApp Business + Google Sheet. Tú eres el intermediario manual. Consigue 3-5 proveedores. Tú tomas pedidos, tú cobras, tú resuelves reclamos. Cobra el 15% REAL desde el día 1, sin subsidios.

Mide solo esto para decidir si sigues o matas:
1. Recompra semana 4 sin descuento: ¿>50% sigue pidiendo POR TI y no directo?
2. Fuga: ¿Cuántos te saltan después del pedido 2?
3. Ticket y frecuencia real, no encuestada.
4. Reclamos logísticos: ¿Puedes mantener <5% de error sin quemarte?
5. ¿Alguien te paga el 15% sin quejarse del precio?

Si después de mover $10K en producto real no tienes 20 restaurantes reordenando y pagando tu comisión felices, NO HAY NEGOCIO. Pivotea o ciérralo.

Mi veredicto como VC: Hoy no invierto. Vuelve cuando me traigas 30 restaurantes en una colonia que te pagaron el 15% durante 2 meses seguidos sin que tú subsidiaras nada. Hasta entonces, solo tienes una hipótesis bonita que Frubana ya refutó con millones.