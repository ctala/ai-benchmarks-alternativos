# Claude Fable 5.2 — creativity/depth_vs_superficial

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 7.84 | quality: 10.0
- latency_total: 57.288s | tokens_per_second: 88.1
- input_tokens: 249 | output_tokens: 5048

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

**Mi opinión contraria primero: a tu escala, la IA para logística es casi seguro una mala inversión.**

Entre un despacho con reglas simples y uno con ML de punta hay un 3-5% de diferencia en costo de reparto. Con 500 pedidos al día a unos $2.500 por entrega, eso es cerca de $1,5M al mes, menos de la mitad del sueldo de un ingeniero de ML en Santiago. PedidosYa, Uber Eats y Rappi ganan con eso porque tienen densidad, y tú no. La IA amplifica la densidad, no la reemplaza, así que la pregunta útil es dónde te ayuda a crear densidad artificial.

## Idea 1: Moldear la demanda en vez de predecirla

Un almuerzo de $8.000 con un reparto de $2.500 no da: el 30% del ticket se va en la moto. Pero 8 almuerzos a la misma torre de El Golf o Nueva Las Condes cuestan unos $350 de reparto cada uno.

Un agente LLM por WhatsApp (no una app, en Chile nadie quiere otra) escribe a las 10:30: "¿Lo mismo del martes, el pollo con quinoa?". El corte es a las 11:15. La IA no optimiza la ruta, fabrica el lote: aprende los hábitos de cada persona y empuja a toda la torre hacia 2 o 3 cocinas. Al restaurante le llega producción planificada con una hora de aviso, y eso vale un 15-20% de descuento negociable.

El foso real aquí es integrarte con Pluxee, Edenred y Amipass, que es donde está la plata del almuerzo.

## Idea 2: Modelar los últimos 50 metros, no los últimos 5 kilómetros

Santiago es una ciudad de torres: Santiago Centro, Estación Central, Independencia, Ñuñoa, San Miguel. Estimo que el repartidor pierde 4-8 minutos entre llegar y entregar, por el conserje, el citófono o los dos ascensores para 30 pisos. En un ciclo de 28 minutos, eso es el 20-25% del tiempo, y pocos lo modelan a nivel de edificio.

Yo construiría un dataset propio por dirección: en la torre A el conserje recibe (1 minuto), en la torre B hay que subir (9 minutos a las 20:00). Sirve para tres cosas:

- **ETAs honestos:** el cliente sabe cuánto demora de verdad su edificio.
- **Avisos automáticos:** un "baja en 2 minutos" enviado en el momento preciso.
- **Precio y despacho:** cobrar y asignar según la fricción real de cada edificio.

Recortar 3 minutos por entrega te da cerca de un 10% más de pedidos por repartidor-hora, el doble o triple de lo que ganarías optimizando rutas, y con un modelo mucho más simple. Además, ese dato no lo tiene Google Maps.

## El riesgo que pocos mencionan: tu algoritmo puede convertirse en tu empleador

La Ley 21.431 distingue entre repartidores independientes y dependientes, y le da al trabajador derecho a saber cómo lo afectan las decisiones automatizadas. Mientras más sofisticada sea tu IA de despacho (asignar turnos, penalizar rechazos, rankear repartidores por desempeño), más evidencia generas de subordinación y dependencia. Un modelo que controla demasiado bien es el mejor argumento para que la Dirección del Trabajo o un tribunal reclasifique tu flota, con un 30-40% más de costo laboral y retroactivo.

Por eso, la arquitectura del modelo es una decisión legal antes que técnica. Conviene diseñarlo para que ofrezca y no ordene, y revisarlo con un abogado laboral antes de escribir código.

Hay un riesgo secundario: si un modelo de precios aprende solo a cobrar distinto por comuna, en el Chile post-2019 eso puede terminar en un reportaje de televisión.

## Advertencia sobre los números

Los números son estimaciones mías para ordenar el razonamiento, así que valídalos con tus datos. Si me cuentas tu modelo (marketplace, flota propia o dark kitchen) y tu volumen actual, puedo ser más específico.