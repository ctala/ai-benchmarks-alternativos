# Muse Wonder — strategy/business_model_validation

- model_id: `meta/muse-wonder`
- success: True  | final: 8.06 | quality: 10.0
- latency_total: 47.651s | tokens_per_second: 68.5
- input_tokens: 169 | output_tokens: 3263

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

Voy a ser directo: tu hipótesis es débil y tu comisión del 15% es, probablemente, fantasía.

"Los restaurantes pierden tiempo llamando a proveedores" no es un dolor por el que la gente pague 15%. Es una molestia. En LATAM, el dueño del restaurante *es* el que llama, su tiempo le cuesta $0 en su cabeza, y esa llamada por WhatsApp también le sirve para negociar precio, pedir fiado y reclamar calidad.

No te falta una app. Te sobra competencia gratuita: WhatsApp + el proveedor de confianza de hace 5 años.

Si entraras a mi oficina, esto es lo que te preguntaría:

### 1. Los 5 riesgos principales de este modelo

**1. Tu take rate del 15% no existe**
¿Quién lo paga?
Si lo paga el proveedor, sube el precio y el restaurante se va directo.
Si lo paga el restaurante, te va a decir que no.
Los distribuidores de alimentos trabajan con márgenes brutos de 8-20% antes de logística. ¿De verdad crees que te van a regalar casi todo su margen por traerles un restaurante pequeño, que compra poco y paga tarde?

Haz la cuenta: pedido de $150 USD. Tu 15% = $22.50. Resta pasarela de pago (3-4%), soporte, devoluciones, mermas, entregas fallidas. ¿Qué te queda?

**2. Desintermediación brutal (leakage)**
Te uso una vez, consigo el teléfono del proveedor, y nunca más paso por tu app. ¿Por qué pagaría 15% extra por el mismo tomate?
Este es el asesino #1 de marketplaces B2B. Sin logística propia, crédito o precio exclusivo, no tienes ninguna razón para quedarte en el medio.

**3. Pesadilla operativa con perecederos**
No vendes zapatos. Vendes productos que se pudren, varían en calidad, peso y precio todos los días.
¿Qué pasa cuando llegan 10kg de pollo y 2kg están mal? ¿Cuando el aguacate está verde? ¿Cuando el proveedor llega a las 11am y el restaurante lo necesitaba a las 8am para el almuerzo?
Un solo pedido fallido = el restaurante no abre bien ese día. No hay segunda oportunidad.

**4. El problema del huevo y la gallina, pero hiperlocal**
No necesitas "proveedores y restaurantes". Necesitas 15 restaurantes y 8 proveedores confiables *en la misma zona de 3km*, con catálogo completo, todos los días.
Si el restaurante tiene que seguir llamando a 3 proveedores fuera de tu app porque no tienes todo, tu propuesta de valor muere.

**5. Tus clientes son el peor segmento posible**
Restaurantes pequeños en LATAM: quiebran en masa en el primer año, compran en volúmenes bajos, negocian cada centavo, pagan tarde y muchos son informales. Tu CAC para adquirir a ambos lados va a ser más alto que lo que ese restaurante te dejará en comisión en 6 meses.

Pregunta de pitch: ¿Cuánto compra al mes un restaurante pequeño, cuánto de eso capturarías tú, y cuánto te cuesta adquirirlo? Si no tienes ese número, no tienes negocio.

### 2. Por qué específicamente NO funcionaría en LATAM

**WhatsApp ya ganó.** Ya es el CRM, el catálogo, el sistema de pedidos y de pagos informal. Gratis. No vas a competir contra "llamadas telefónicas", compites contra un hábito de 10 años.

**El fiado manda.** El proveedor actual le da crédito de 7, 15 o 30 días. ¿Tú vas a dar crédito? Si pides pago anticipado con tarjeta, perdiste. Si das crédito, te quedas sin caja y te conviertes en banco de restaurantes quebrados.

**Informalidad y facturación.** Muchos no quieren factura porque eso implica impuestos. Muchos proveedores no pueden ni emitirla. Tu marketplace formal, trazable y con comisión es exactamente lo que quieren evitar.

**La relación ES el negocio.** El proveedor no solo vende. Le guarda el mejor producto a su cliente fiel, le acepta devoluciones sin pelear, le fía, le baja el precio si el mercado bajó. Tu app estandarizada elimina justo eso que valoran.

**Logística e inseguridad.** Tráfico, zonas donde no entra cualquier repartidor, entregas en efectivo, robos. Sin flota propia, dependes del proveedor informal que no tiene ningún incentivo para priorizar tu pedido pequeño frente a su cliente grande.

Dato incómodo: Frubana levantó más de $270M USD para hacer *exactamente esto* en LATAM, con equipo, capital y logística. Terminó cerrando operaciones en varios países. ¿Qué sabes tú que ellos no?

### 3. Qué tendría que ser verdad para que funcione (Key Assumptions)

No opiniones. Hechos que tienes que probar:

1.  El dolor #1 del restaurante no es el tiempo, es precio, crédito o desabastecimiento, y tú resuelves *eso* mejor que el incumbente.
2.  Puedes consolidar al menos el 60-70% de la compra semanal de un restaurante. Si solo eres el proveedor de verduras, no importas.
3.  El proveedor puede cumplir >95% OTIF (completo y a tiempo) con calidad consistente, sin que tú tengas inventario.
4.  El restaurante repite semanalmente *sin descuentos* y sin salirse a WhatsApp directo.
5.  Hay margen suficiente para ti, el proveedor y el restaurante sin que el precio final sea más caro que el canal actual.
6.  Puedes adquirir restaurantes por menos de, digamos, $30-50 USD por métodos escalables. No con el fundador visitando uno por uno para siempre.

Si una sola falla, el modelo se cae.

### 4. El escenario donde fracasas rápido

Semana 1-4: Construyes una app bonita. Convences a 20 proveedores amigos y 40 restaurantes con $50 de crédito gratis.
Semana 5: Primeros pedidos reales. El 30% llega incompleto. Un proveedor te deja mal porque le salió un pedido grande. Los precios de tu app no coinciden con los del mercado de ese día.
Semana 6: Los restaurantes te reclaman a TI, no al proveedor. Tú absorbes reembolsos para no quemarte.
Semana 7: Los restaurantes que sí quedaron contentos le piden el número directo al proveedor para "pedir más rápido". Empieza el leakage.
Semana 8-12: Para retener, bajas tu comisión al 7%, luego al 5%, subsidias envíos. Cada pedido pierde dinero, pero tu métrica de "GMV" sube y te engañas.
Mes 4: Sin caja, sin retención real sin subsidio, sin moat. Muerto.

No moriste por falta de tecnología. Moriste por operaciones y unit economics.

### 5. Si solo tuvieras $10K para validar: NO construyas la app

Gastar en desarrollo ahora es quemar dinero. Haz esto en 6-8 semanas:

**Fase 1: Destruye tu propia hipótesis (Semana 1-2, ~$1,500)**
Ve a UNA sola zona densa. Habla con 30 dueños de restaurantes pequeños. No les vendas. Pasa una mañana con 5 de ellos viendo cómo compran.
Pregunta: ¿Cuánto compraste ayer, a quién, a qué precio, cómo pagaste, qué salió mal esta semana?
Si el problema #1 no es el que tú resuelves, pivota o mata la idea aquí.

**Fase 2: Concierge con WhatsApp (Semana 3-6, ~$5,000)**
Elige UNA categoría de alto dolor y frecuencia: ej. verduras, o proteína. No todo.
Tú eres la app. Recibes pedidos por un número de WhatsApp, los pasas a 3-5 proveedores que negociaste, coordinas entrega en Google Sheets.
Cobra comisión REAL desde el día 1. Nada de gratis.
Presupuesto: $3,000 para un operador de campo temporal, $1,000 en transporte/pruebas, $1,000 en buffer para mermas y errores (los vas a pagar tú para aprender).

**Fase 3: Mide lo único que importa (Semana 7-8, ~$1,000)**
Nada de descargas o registros. Solo esto:

**Sigue si:** >50% de restaurantes repite en la semana 4 sin descuento, hacen 2+ pedidos/semana, cumplimiento >95%, y tu margen por pedido es positivo sin subsidiar entrega.
**Mata la idea si:** Tienes que rogar para que pidan, se salen a directo, o cada pedido requiere 10 mensajes tuyos para resolverse. Eso no escala, es un trabajo mal pagado de intermediario.

Los $2,500 restantes: guárdalos. Si no pasa el test, te ahorraste construir algo que nadie quería.

**Mi veredicto como VC hoy: Paso.**

No porque el mercado sea chico — es gigante — sino porque estás proponiendo cobrar 15% por resolver un problema secundario, en el segmento más difícil, con el producto más complicado, contra WhatsApp y el crédito informal.

Demuéstrame retención semanal pagando precio real y sin fugarse. Sin eso, no tienes un marketplace. Tienes una lista de contactos cara.