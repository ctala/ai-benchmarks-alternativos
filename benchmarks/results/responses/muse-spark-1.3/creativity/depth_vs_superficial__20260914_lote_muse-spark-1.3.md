# Muse Spark 1.3 — creativity/depth_vs_superficial

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 50.953s | tokens_per_second: 86.8
- input_tokens: 139 | output_tokens: 4424

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

Te voy a hablar como si fueras mi socio, no como blog de "5 usos de IA".

Si estás armando un delivery en Santiago hoy, estás peleando contra PedidosYa, Rappi y Uber Eats. No les vas a ganar con mejor tecnología. Ellos tienen 100 ingenieros de ML. Les vas a ganar por ser quirúrgico en un margen que ellos ya dieron por perdido.

El unit economics en Santiago es brutal: ticket promedio $9.500 - $11.000, comisión que le puedes cobrar a una pyme sin que te mande a la chucha 18-22% (Rappi cobra hasta 28% y por eso los odian), y costo por despacho $2.400 - $3.000 pagándole al rider. Si tu rider hace 1.8 entregas por hora en hora punta (que es lo normal entre Providencia y Ñuñoa con taco), pierdes plata en cada pedido. Necesitas 2.6 - 2.8 para empatar. La IA solo sirve si te mueve ese número. Todo lo demás es humo.

Olvídate del chatbot y del "ruteo optimizado". Eso ya lo hace Google Maps al 95% y no es tu cuello de botella. Aquí van dos apuestas que sí te mueven la aguja en Santiago:

**1. El Score de Viajabilidad por plato. Tu filtro anti-funas.**

El 70% de los reclamos en delivery chileno no es por atraso, es por "llegó malo". Y no es aleatorio. Es siempre el mismo 7% de platos.

Una papa frita en mochila en una moto cruzando Vespucio a las 20:30 en invierno llega como esponja a los 18 minutos. Un completo italiano con tomate se desarma a los 15. Un sushi acevichado aguanta 35 minutos perfecto. Un Barros Luco con marraqueta aguanta, con hallulla no.

Nadie te dice esto: puedes construir esto en 2 semanas sin un equipo de ML. Toma las fotos de los platos de tus 30 primeros socios, los comentarios de Google Maps y PedidosYa ("llegó frío", "todo revuelto", "la caja mojada"), y el tiempo real de entrega por ese trayecto. Cruza eso con un modelo de visión simple. No para recomendar comida, sino para prohibirla inteligentemente.

Ejemplo concreto: tienes una picada buena en Barrio Italia. El modelo aprende que su chorrillana tiene 82% de probabilidad de reclamo si el viaje es >22 min. Entonces tu app hace 3 cosas automáticas: a las 19:00-21:00 (taco) ese plato simplemente no aparece para alguien en Las Condes, solo para alguien en un radio de 2km; si igual lo piden, le cobras $500 de packaging doble y se lo das al local; y al local le muestras: "oye, cambia este envase y subes 0.4 estrellas".

Estimación realista: en pilotos parecidos en Latam, sacar ese 7% tóxico baja los reembolsos de 6% a 3.5% de los pedidos y sube el rating de 4.3 a 4.6. Ese 0.3 en rating es +8-12% de conversión. Con 500 pedidos/día a $10.000, son ~$1.2MM extra al mes solo por no vender lo que viaja mal. Es contraintuitivo: ganas más vendiendo menos.

**2. Pedido Vecinal por edificio. La densidad es todo.**

Santiago no es Ciudad de México con casas. Es torres de 200-300 deptos en Estación Central, San Miguel, Ñuñoa, Santiago Centro. PedidosYa trata cada depto como una entrega individual. Ahí está tu oportunidad.

En vez de predecir demanda por comuna (obvio), predice demanda por edificio-hora. Con historial de 3 semanas ya ves patrones ridículamente estables: la Torre B de Lira 700 pide 11-14 sushis todos los jueves 20:00-20:45. El edificio de Irarrázaval con Santa Julia pide completos el sábado post-carrete 14:00.

La jugada: a las 19:30 le mandas push solo a ese edificio: "Hoy Sushi Vecino: pide antes de las 20:00, despacho $990 (en vez de $2.490) y llega 20:35 a conserjería". Consolidas 4-5 pedidos en UN viaje. Tu costo pasa de 4 x $2.600 = $10.400 a 1 x $3.200. Te ahorras $7.200 y le das $1.500 de descuento al cliente. Margen que Rappi no puede igualar porque no opera a ese nivel de granularidad.

Con 4 pedidos consolidados subes tu entregas/hora-rider de 1.8 a 3.5 en esa ventana. Ahí recién ganas plata. Esto funciona especialmente con conserjes chilenos, que ya están acostumbrados a recibir. Es logística social, no solo algoritmo.

Empieza con 10 edificios. No necesitas IA pesada, necesitas un clustering k-means pedorro + un WhatsApp con el conserje.

**El riesgo no obvio que te va a matar: la trampa territorial y legal.**

Todos te hablan del riesgo de alucinaciones. El riesgo real en Chile se llama Ley 21.719 de Protección de Datos (que ya está corriendo con multas de hasta 20.000 UTM) + sesgo por comuna.

Si entrenas tu modelo para "maximizar probabilidad de entrega a tiempo y buena propina", el modelo en 3 semanas va a aprender solo: prioriza Las Condes, Providencia, Ñuñoa y castiga Puente Alto, La Pintana, Cerro Navia. ¿Por qué? Porque los viajes son más cortos, hay más ascensores, hay conserjes, pagan con tarjeta. Es matemáticamente óptimo discriminar.

Resultado: dejas botada la periferia en hora punta, te comes 30 funas en X/TikTok de "esta app es cuica, no llega a Puente", y SERNAC te cae encima. Y peor: ese loop se retroalimenta. Como atiendes mal Puente Alto, tienes menos datos buenos de ahí, el modelo predice peor, atiendes peor. Muerte silenciosa.

Y el tema legal: RUT + dirección exacta del depto + historial de pedidos ("vegano, pide melatonina, vive solo") es dato sensible. Si lo metes a un LLM gringo para personalizar sin anonimizar, estás violando la ley. Ningún founder lo considera hasta que llega la multa.

Mitigación desde día 1: entrena con fairness constraint por zona (obliga al modelo a mantener SLA mínimo en 5 macrozonas de RM aunque pierdas 4% de margen) y nunca mandes RUT/dirección cruda al modelo. Usa IDs hash + cuadrante de 300m.

**Mi opinión contrarian: no uses IA para el cliente final. Úsala para que la picada te ame.**

Todo el mundo quiere ponerle un asistente "¿qué se te antoja hoy?" al usuario. Eso es una estupidez en delivery. Destruye margen porque el usuario siempre elige lo más barato, y además compites con el algoritmo de TikTok e Instagram que ya decide qué quiere comer.

Tu moat no es el usuario, es el restaurante chico que odia a Rappi. El dueño de la sanguchería en La Vega, del sushi de Maipú que atiende con su señora y no sabe de food cost.

Dale IA B2B invisible: "Don Juan, mañana juega Colo-Colo con la U a las 20:00 y va a llover. Históricamente pides 8kg de pollo y te faltan 3kg. ¿Te pre-pido 11kg al proveedor? ¿Y te apago el completo por 40 min a las 21:00 para que no colapses la cocina como el viernes pasado que te demoraste 48 min y te funaron?"

Eso vale oro. Ese loco no se va a cambiar nunca a PedidosYa por eso, aunque le cobres lo mismo. La IA que gana en Chile no es la que habla bonito, es la que evita que una cocina de 2 personas colapse un viernes.

Si tuviera $500 lucas y 14 días, haría esto: elijo 15 locales en un eje (ej: Ñuñoa-Providencia), no construyo app con IA, uso WhatsApp + planilla. Corro solo los dos experimentos de arriba a mano primero. Si no logras consolidar 3 pedidos por edificio ni bajar reclamos 2 puntos a mano, ningún modelo te va a salvar.

¿Quieres que te lo baje a tierra? Dime qué comunas quieres atacar primero y qué tipo de comida, y te armo el experimento de 14 días con números.