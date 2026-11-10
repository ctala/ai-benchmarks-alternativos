# Muse Ember — creativity/depth_vs_superficial

- model_id: `meta/muse-ember`
- success: True  | final: 8.75 | quality: 10.0
- latency_total: 23.356s | tokens_per_second: 342.8
- input_tokens: 140 | output_tokens: 8006

## Entrada exacta (lo que recibió el modelo)

**user:**

Un emprendedor te dice: "Estoy pensando en usar IA para mi startup de delivery de comida en Santiago. Que deberia hacer?"

Da una respuesta que demuestre PROFUNDIDAD real, no consejos genericos.
Incluye:
- Al menos 2 ideas especificas que NO sean obvias (no digas "usa IA para optimizar rutas", eso lo sabe cualquiera)
- Numeros o estimaciones concretas cuando sea posible
- Un riesgo no obvio que otros no mencionarian
- Una opinion contrarian o controversia sobre el tema

No me des una lista generica de "5 formas de usar IA". Quiero pensamiento original.


## Respuesta completa

En Santiago no tienes un problema de IA. Tienes un problema de PedidosYa.

PedidosYa tiene ~75-80% del delivery en la RM, 10 años de datos de qué pide cada comuna a cada hora, y Uber Eats ya se fue en 2021 dejando el camino libre. Si tu pitch es "una app de delivery con IA que recomienda platos", vas a perder antes de lanzar.

Mi opinión contrarian: **no construyas IA visible para el cliente.** Chatbots que preguntan "¿quieres sushi?", recomendadores, fotos generadas por IA. A las 20:30, con 5°C en Providencia y hambre, nadie quiere que una IA le converse. Quiere que llegue caliente y barato.

Y PedidosYa ya ganó la guerra de datos de consumo. Tú nunca vas a tener un mejor modelo de recomendación que ellos. La única IA que tiene sentido para una startup en Santiago es la invisible: la que evita un reclamo, recupera un pedido perdido por WhatsApp, o le ahorra $3.000 CLP de comisión a un restaurante que PedidosYa está exprimiendo.

Estas son las dos únicas ideas que yo validaría:

### 1. No hagas una app. Haz una capa invisible de WhatsApp + boleta para los restaurantes que PedidosYa abandona

En Chile el delivery real no pasa por la app. Pasa por WhatsApp e Instagram DM.

Piensa en una fuente de soda en Ñuñoa, una pizzería en Maipú, un sushi de barrio en La Florida, un lomito en San Miguel. Hacen 30-60 pedidos/día por WhatsApp. El dueño está en la cocina de 12:00 a 15:00 y de 19:00 a 22:00, no contesta. Si tardas >3-5 minutos en responder, el cliente ya pidió en otro lado. Además cobra por transferencia, no emite boleta, y si el cliente pide boleta, se complica.

PedidosYa les cobra 25-30% por "ordenar" algo que ya hacen gratis. En un ticket promedio santiaguino de $11.990, eso es **$3.200 - $3.600 CLP por pedido** que se va la plataforma.

Tu producto no es un marketplace. Es un número de WhatsApp Business con IA que:

1. Responde en <10 segundos, entiende audios chilenos con ruido ("un completo asado, sin cilantro, po" - Whisper en español chileno con ruido de moto/sartén tiene 18-25% de error en crudo, no 5% como en inglés de laboratorio, por eso necesitas confirmación automática por texto)
2. Arma el pedido, manda link de pago Mach/Mercado Pago/tarjeta
3. **Emite la boleta electrónica al SII** con el RUT y giro del restaurante. Esto es clave en Chile desde la boleta obligatoria: si lo haces mal, el restaurante queda sin respaldo tributario y te demanda a ti.
4. Recién ahí imprime el ticket en la cocina

Números: Costo por pedido de WhatsApp API + LLM (tipo GPT-4o mini) = $70-120 CLP. Versus $3.200 de comisión de PedidosYa.

Tú cobras $19.990/mes fijo + $250 por pedido. Para el restaurante con 25 pedidos/día, pasa de pagar ~$2,4 millones/mes en comisiones a ~$800.000. Le ahorras $1,6M.

Para ti: 100 restaurantes x 25 pedidos x 30 días x $250 = $18,75M CLP/mes + $2M fijos. Eso es viable sin tener flota, sin CAC de app ($4.500-6.500 CLP por cliente vía Meta/Google en Santiago), sin quemar plata en repartidores.

Por qué PedidosYa no lo hará: canibaliza su propio negocio. Por qué es un moat: no es tecnología, es tener 50 restaurantes en 3 comunas que te dan sus datos de menú y te dejan conectado a su SII.

### 2. IA de "supervivencia del plato", no de rutas

Todos te dirán "optimiza rutas". Inútil. PedidosYa ya lo hace y en Santiago la ruta no es el problema. El problema es **qué plato sobrevive 35 minutos en moto en invierno.**

Un sushi crudo en enero con 32°C en Santiago, un caldo en moto por Gran Avenida con baches, una ensalada César en julio... se deshacen, se enfrían, se derraman. El reclamo no es "llegó tarde", es "llegó asqueroso". Eso genera 1 estrella y no vuelve.

En delivery en Santiago, 6-9% de los pedidos terminan en reclamo por comida fría/derramada/equivocada. Cada reclamo te cuesta $6.000 de reembolso + $2.000 de delivery gratis + perder un cliente que pedía 3 veces al mes ($13.000 ticket x 3).

Entrena un modelo ridículamente simple pero hiperlocal con 3 variables que PedidosYa promedia a nivel ciudad y tú puedes aprender por dirección:

**a) Transportabilidad del plato:** tipo de plato, envase, temperatura exterior (Dirección Meteorológica), distancia.
**b) Tiempo vertical:** En Providencia/Las Condes/Santiago Centro, 40% de las entregas son a edificios. La espera en portería/ascensor no es 2 minutos, es 7-12 minutos en un edificio en Av. Apoquindo o en un edificio antiguo sin ascensor en Santiago Centro. Si tu ETA dice 25 min y son 38, la conversión cae.
**c) Plato x zona:** No vendas ese ramen a >15 min en invierno. No vendas ese sushi a 30 min en verano.

Si el score de supervivencia es <60, tu sistema le dice al restaurante: "no lo vendas a este cliente, o cámbiale el envase, o limita tu zona a 12 min para este plato".

Bajar reclamos de 8% a 3,5% en un restaurante de 1.000 pedidos/mes = 45 reclamos menos x $8.000 = **$360.000 CLP/mes ahorrados**, más reputación. Eso sí es un diferencial que un restaurante paga, porque PedidosYa prefiere venderte el plato igual y cobrarte la comisión.

### El riesgo no obvio que nadie te menciona

No es que OpenAI te cobre más caro. Es el **riesgo laboral-algorítmico + discriminación territorial.**

Si tu IA decide quién recibe pedidos, quién es penalizado por llegar tarde, y quién es desactivado automáticamente, la Dirección del Trabajo en Chile puede argumentar subordinación. Ya hay litigios contra plataformas por esto. Si te declaran empleador, debes cotizar ~30% extra retroactivo. Una multa de 60 UTM son más de $4 millones, y eso es por repartidor.

Peor: tu modelo va a aprender solo que en ciertas comunas periféricas (Puente Alto, La Pintana, Conchalí) hay más cancelaciones, más tacos, más robos. Y va a empezar a depriorizar repartidores o clientes de ahí. Con la nueva Ley de Protección de Datos Personales chilena (21.719, aprobada en 2024), las decisiones automatizadas que afectan a personas sin revisión humana son sancionables. Y en Santiago, una captura de pantalla de "la IA de X discrimina La Pintana" te funa en X en 48 horas. Reputacionalmente, mueres.

Por eso: nada de desactivación automática. Todo castigo con revisión humana y trazabilidad. Y nunca entrenes con datos de ubicación cruda sin consentimiento explícito.

### Qué haría yo en tu lugar

Nada de marketplace nacional. Elige 3 comunas: Ñuñoa, La Florida, Maipú. Consigue 5 restaurantes que ya venden por WhatsApp. Conéctales solo la Idea 1 por 14 días. Mide: tiempo de respuesta, pedidos recuperados, boletas emitidas sin error.

Si recuperas 8 pedidos/día por restaurante que antes se perdían, ya tienes negocio. Si no, no hay IA que te salve.

La IA en delivery en Santiago no gana el cliente. Gana el restaurante que está harto de pagar 30% y el cliente que por fin recibe el completo entero.