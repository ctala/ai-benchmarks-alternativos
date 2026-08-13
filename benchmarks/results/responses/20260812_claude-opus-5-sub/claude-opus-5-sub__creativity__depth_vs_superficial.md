# Claude Opus 5 (suscripción) — creativity/depth_vs_superficial

- model_id: `claude-opus-5`
- success: True  | final: 7.79 | quality: 10.0
- latency_total: 169.837s | tokens_per_second: 59.7
- input_tokens: 2 | output_tokens: 10141

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

Antes de responder: "usar IA en delivery" no es una decisión, es una categoría. La decisión real es en qué línea del P&L la metes. Así que partamos por ahí, porque sin eso todo lo demás son opiniones bonitas.

## El P&L de una orden en Santiago (más o menos)

Orden promedio ~CLP 14.000:

| Línea | CLP |
|---|---|
| Comisión al restaurante (25-30%) | +3.500 |
| Fee de envío + service fee al usuario | +2.000 |
| Pago al repartidor | −3.200 |
| Pasarela (~3% con Webpay crédito) | −480 |
| Soporte + refunds/mermas | −400 |
| **Contribución por orden** | **~1.400** |

Antes de marketing y antes de fijos. Con un CAC de USD 10 (~CLP 10.000) necesitas 7 órdenes solo para recuperar la adquisición de ese usuario. Ese es el negocio. Cualquier modelo que no mueva una de esas líneas es un juguete.

Ahora sí.

## Idea 1: el problema no son las rutas, es el *dwell time*

El repartidor no pierde el tiempo manejando. Lo pierde parado en el restaurante esperando que salga la comida: 6 a 11 minutos por pedido es lo típico. Si haces 2,2 entregas/hora y bajas el dwell de 9 a 4 minutos, subes a ~2,7 entregas/hora. Tu costo por entrega cae de CLP 3.200 a ~CLP 2.600. Sobre 30.000 órdenes/mes son CLP ~18M mensuales (≈USD 19K), más que todo tu equipo de datos.

La forma de atacarlo es predecir el *food-ready time* y despachar al repartidor con retraso deliberado. Hasta ahí es semi-conocido. Lo que casi nadie hace bien son dos cosas:

**Modelar la topología del cuello de botella, no el plato.** Una pizzería con 4 pedidos simultáneos no demora 4×, demora ~1,4×: el horno procesa en paralelo. Un sushi con 4 pedidos sí escala casi lineal, porque el cuello es una persona armando rolls. El feature que importa no es "qué pidió", es la cola actual de esa cocina cruzada con si su restricción es paralela o serial. Y como no vas a tener 200 órdenes por local para que converja un modelo por restaurante, esto es partial pooling / jerárquico bayesiano: el local nuevo hereda del prior de su categoría y se va despegando con data propia.

**La pérdida es asimétrica y tu loss function debería reflejarlo.** Llegar 3 minutos antes te cuesta 3 minutos de repartidor. Llegar 3 minutos tarde te cuesta comida fría, rating, y a veces refund completo. No entrenes con MSE. Entrena con pinball loss al percentil ~65-70. Ese solo cambio suele valer más que subir el R² dos puntos.

## Idea 2: uplift, no propensión (o estás regalando plata)

Si gastas CLP 8M/mes en cupones y hay campaña de retención, entre 30% y 40% de eso se lo estás dando a gente que iba a pedir igual. Son ~CLP 3M/mes quemados en descuento a compradores seguros.

El modelo correcto no es "quién tiene alta probabilidad de comprar" (eso te lleva justo a los seguros). Es un modelo de efecto incremental: quién compra **si le doy cupón** menos quién compra **si no**. Uplift / CATE, dos-modelos o T-learner para empezar.

El costo de entrada es el que nadie quiere pagar: necesitas un holdout aleatorio del 5-10% al que deliberadamente **no** le das promo, sostenido 6-8 semanas, aguantando la pérdida. Sin esa randomización no tienes contrafactual y no hay modelo causal posible, solo correlación disfrazada. La mayoría de las startups no lo hace, y por eso lleva tres años "optimizando promociones" sin saber si alguna funcionó.

## Idea 3: la que probablemente sea tu negocio real

El restaurante paga 28% + IVA al marketplace. Su canal propio le cuesta ~3% de pasarela, o ~1% si cobras por transferencia con Khipu/Fintoc. Sobre un local que factura CLP 20M/mes en delivery, la diferencia son CLP ~5M mensuales.

Un agente de WhatsApp que tome el pedido, maneje modificadores ("sin cebolla, agrega palta"), haga upsell y cierre con link de pago, cobrado a CLP 300-500K/mes, es un ROI de 10× obvio para el dueño del local. Y es un SaaS con márgenes de software en vez de un negocio de logística con 10% de contribución.

La objeción es "el marketplace le trae demanda nueva". Cierto, pero en un local establecido la mayoría de las órdenes son clientes recurrentes que ya lo conocen y usan la app solo por comodidad. Esa porción es atacable con un canal propio decente. El marketplace sirve para descubrimiento; le estás pagando 28% por gente que ya te conoce.

## El riesgo que nadie te va a mencionar

**Chile te obliga a que tu algoritmo de asignación sea explicable, por ley.**

La Ley 21.431 (plataformas digitales, vigente desde 2022) obliga a informar al trabajador los criterios de asignación de tareas y de cálculo de pagos. Si tu dispatcher es un gradient boosting con 400 features, no puedes cumplir eso, y no es una multa hipotética: es la Dirección del Trabajo. La consecuencia de diseño es fuerte: necesitas un asignador explicable **por construcción** (scoring lineal sobre features del modelo, o un sistema que emita razones), no un black box con SHAP pegado después.

Encima viene la Ley 21.719 de datos personales, con la Agencia entrando en operación. Tú almacenas dirección del domicilio, horarios en que la gente está en casa, y restricciones alimentarias que pueden calificar como dato sensible (salud, religión). Multas de hasta 20.000 UTM. Pero el golpe real no es la multa: es que si entrenaste modelos mandando esa data a APIs de terceros sin base de licitud ni contrato de encargado documentado, eso aparece en el due diligence de tu Serie A y te frena la ronda.

Y el efecto de segundo orden, que es el peor: este costo regulatorio es fijo. PedidosYa lo absorbe sin despeinarse; tú no. **La regulación de plataformas es un foso que protege al incumbente**, y lo van a defender en el Congreso precisamente por eso.

(Confirma esto con un abogado laboral, no conmigo. Estoy leyendo la norma, no ejerciendo.)

## La opinión contrarian

**Dos, y la segunda es la incómoda.**

La primera: la IA generativa es la parte *menos* valiosa de tu stack de IA. El 85% del valor está en forecasting, optimización operativa e inferencia causal, o sea técnicas de 2012-2018 que hoy nadie postea en LinkedIn. Los LLM ganan claro en exactamente dos lugares: digitalizar catálogo desde fotos de menú, y conversación (pedidos, soporte). Todo el mundo está construyendo el chatbot. Nadie está tocando el pinball loss ni el uplift.

La segunda: **si tu diferencial es la IA, no tienes negocio.** En delivery gana el que tiene densidad en 6 comunas, no el que tiene mejor modelo. Tu modelo lo replican en cuatro meses; la densidad no se replica, se compra a pérdida y con capital que tú no tienes. Buscar que la IA sea tu diferencial es el error caro, porque te lleva a construir un equipo de datos de 6 personas antes de tener volumen para que los modelos aprendan algo.

El uso correcto de la IA en tu etapa no es diferenciarte. Es **bajar tu punto de equilibrio**: llegar a break-even con 8 personas en vez de 25. Eso no va en el pitch deck, pero es lo que decide si existes en 18 meses.

## Qué haría el lunes

Antes de cualquier modelo, instrumenta 7 timestamps limpios por orden: pedido creado, aceptado por el local, repartidor asignado, repartidor llega al local, comida lista, retirada, entregada. Si no los tienes con esa granularidad —y lo más probable es que no los tengas, casi nadie los tiene— ningún modelo de los de arriba se puede entrenar. Son dos semanas de trabajo, cero IA, y desbloquean todo lo demás.

En paralelo, corre el P&L por orden **segmentado por comuna**. Apostaría a que dos o tres comunas te están destruyendo la contribución y no lo ves porque miras el promedio. Esa decisión —dejar de servir una zona— probablemente vale más plata este trimestre que cualquier modelo que entrenes este año.