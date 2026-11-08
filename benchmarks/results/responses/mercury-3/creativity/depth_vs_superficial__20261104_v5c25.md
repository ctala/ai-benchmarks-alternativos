# Mercury 3 — creativity/depth_vs_superficial

- model_id: `inception/mercury-3`
- success: True  | final: 8.28 | quality: 9.0
- latency_total: 12.881s | tokens_per_second: 277.5
- input_tokens: 139 | output_tokens: 3574

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

Mira, te voy a ahorrar el sermón de “usa IA para optimizar rutas”. Eso ya lo hace Rappi, Uber Eats y PedidosYa, y no te va a dar ninguna ventaja. El problema real en Santiago no es el camino: es la cocina, el edificio y el costo de la última milla.

## Idea 1: Predecir la demanda por plato, no por pedido, y activar la cocina antes de que el cliente confirme

La mayoría de los modelos de forecasting predicen cuántos pedidos habrá en una zona. Eso es útil, pero no cambia el cuello de botella: el restaurante. Un plato que tarda 18 minutos en prepararse no se arregla con un mejor repartidor.

Construye un modelo que prediga, con 45 minutos de anticipación, la probabilidad de que se pida un plato específico en un restaurante específico, usando variables como clima, hora, día de la semana, eventos en el barrio y datos históricos de ese local. Luego envía esa predicción a la cocina como una “pre-orden”: que el restaurante deje los ingredientes listos, encienda el horno o precaliente la freidora.

En Santiago, el tiempo promedio de entrega ronda los 42 minutos. Si reduces el tiempo de preparación de 18 a 12 minutos, ganas 6 minutos. Eso no solo mejora la experiencia: te permite expandir tu radio de entrega sin que la comida llegue fría. Si hoy cubres un radio de 4 km, con 6 minutos extras a una velocidad promedio de 5 km/h puedes cubrir 4.5 km. El área de cobertura no crece linealmente: crece con el cuadrado del radio. Pasas de ~50 km² a ~64 km². Eso es un 28% más de mercado direccionable, sin contratar un solo repartidor extra.

## Idea 2: Cobrar según la “dificultad de entrega” de cada edificio, no según la distancia

Todos cobran por distancia. Pero en Santiago, la distancia es un mal proxy del costo real. Un delivery a un quinto piso sin ascensor en Providencia, en hora punta, puede tomar 10 minutos más que uno a un primer piso con ascensor. Y un edificio con conserje que recibe el pedido es radicalmente distinto a uno donde el repartidor tiene que esperar a que bajen.

Usa visión computacional y datos catastrales para clasificar cada edificio de Santiago: si tiene ascensor, número de pisos, si hay conserje, si el acceso es por escalera, si hay estacionamiento para moto. Combina eso con el clima (la lluvia hace que la gente no baje rápido) y con el tipo de repartidor (moto vs bicicleta). Genera un “índice de dificultad de entrega” y úsalo para dos cosas: asignar el repartidor adecuado y ajustar la tarifa de delivery.

Esto no es un cobro arbitrario: es un reflejo real del costo. Un repartidor que sube 5 pisos a pie tiene un costo de oportunidad enorme: en ese tiempo podría haber hecho otro pedido. Si cobras $300 CLP extra para ese tipo de entrega, puedes compensar al repartidor y reducir su rotación. Y si no quieres cobrarle al cliente, úsalo para priorizar qué pedidos aceptar cuando hay demanda alta. Es un modelo de “rechazo inteligente”: no aceptes pedidos que te hagan perder plata.

## El riesgo que nadie menciona: la IA va a aprender a discriminar por código postal

No el riesgo de que la IA falle. El riesgo es que funcione demasiado bien y empiece a cobrar más caro o a dar peor servicio en comunas periféricas, simplemente porque la densidad de pedidos es menor y la distancia es mayor. Eso no es malicia: es optimización. Pero en Chile, la percepción de discriminación por zona geográfica es un problema real, y la Ley de Protección al Consumidor más la presión social pueden convertir tu algoritmo en un dolor de cabeza reputacional.

Además, si entrenas con datos de competidores existentes, estás heredando sus sesgos. Rappi y Uber Eats ya tienen modelos que penalizan ciertas zonas. Si tu modelo aprende de ellos, vas a perpetuar exactamente las mismas ineficiencias que querías superar. Tu ventaja no está en los datos históricos: está en los datos que ellos no tienen, como la dificultad real de cada edificio o el comportamiento de cada cocina.

## Opinión contracorriente: no uses IA para entregar más rápido, úsala para entregar más lento

Todo el mundo asume que la velocidad es el objetivo. Es falso. La velocidad es lo que está matando la economía del delivery en Santiago. Para entregar en 30 minutos, necesitas un repartidor por pedido, rutas ineficientes y picos de demanda imposibles de cubrir. Eso es carísimo.

Usa la IA para alargar deliberadamente la ventana de entrega a 75 minutos, pero con una promesa confiable: “tu pedido llega entre las 20:15 y las 20:30”. Con esa ventana, puedes agrupar pedidos en micro-lotes por cuadra. Un repartidor lleva 4 o 5 pedidos en vez de 1. El costo por entrega cae de $2.500 CLP a $1.100 CLP. Y el cliente no pierde nada: lo que quiere no es velocidad, es saber cuándo llega su comida y que llegue caliente.

La IA aquí no sirve para predecir la ruta más rápida. Sirve para predecir qué clientes están dispuestos a esperar 75 minutos a cambio de un descuento o delivery gratis, y cómo agrupar sus pedidos para que la comida llegue caliente. Es un cambio de paradigma: de “velocidad” a “confiabilidad”. Pero requiere que estés dispuesto a ignorar la métrica que todos usan para medir el éxito, que es el tiempo de entrega promedio.

Si haces esto, no estarás compitiendo con Rappi en velocidad. Estarás compitiendo en economía unitaria. Y en un mercado donde las comisiones y los costos de reparto se comen el margen, eso es lo único que importa.