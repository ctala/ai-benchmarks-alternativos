# Muse Spark 1.3 — creativity/depth_vs_superficial

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.33 | quality: 10.0
- latency_total: 39.28s | tokens_per_second: 96.0
- input_tokens: 140 | output_tokens: 3772

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

En Santiago no compites contra tecnología. Compites contra Rappi y PedidosYa, que te cobran 23-28% + IVA por pedido y aun así pierden plata. Si usas IA para hacer lo mismo que ellos pero más chico, mueres.

Tu única jugada es usar IA donde ellos son demasiado grandes y burocráticos para meterse. Te doy dos que he visto funcionar en delivery latam y nadie te va a decir:

**1. El detector de cocinas colapsadas, no el repartidor más rápido.**

En Santiago el problema no es el tráfico. Es la cocina. Un local de sushi en Bellavista o una sanguchería en Providencia a las 20:45 recibe 14 pedidos en 10 minutos, colapsa, y pasa de demorar 12 min a 38 min. Tú no te enteras hasta que el cliente ya está furioso y pide reembolso.

Rappi soluciona esto castigando al repartidor. Tú puedes hacerlo distinto: un modelo bien tonto que mira señales débiles por restaurante: cuánto se demora en apretar "aceptar", cuánto crece el tiempo "aceptar -> listo" vs su promedio del martes pasado, si hay 2 repartidores esperando afuera con GPS quieto.

Cuando detecta colapso, no esperas. Pausas automáticamente al local por 12 minutos, le dices al cliente la verdad *antes* de que pague: "Este local está a 30 min ahora, estos 3 similares están a 15" y le das un cupón de 1.500.

Los números: en delivery chileno la tasa de reembolso / cupón por atraso es 3,5% - 4,5% de los pedidos. Si haces 10.000 pedidos/mes con ticket promedio de $9.500, eso son $3,3 a $4,2 millones al mes quemados en reembolsos y en clientes que no vuelven. Bajar eso de 4,2% a 2,8% con pausas predictivas te ahorra ~$1,3M mensual. Te paga toda tu cuenta de OpenAI/Anthropic 20 veces. Y no necesitas ni un data scientist, necesitas guardar los timestamps que ya tienes.

**2. Cirugía de menús para picadas, por comuna.**

El 70% de tus futuros socios no son Holy Moly, son picadas de Maipú, Franklin, Patronato con fotos sacadas con un Samsung del 2019 a las 11pm y descripciones como "churrasco italiano grande". Convierten al 1,8% - 2,2%. Los top convierten al 3,5%+.

Ahí la IA sí es magia, pero no para generar logos. Para esto: tomas sus 3 fotos reales malas, las re-iluminas sin inventar ingredientes (misma mayo, mismo pan), y reescribes el menú con copy chileno por zona. Lo que vende en Las Condes ("poke bowl salmón, alto en proteína") no vende en Puente Alto ("40 piezas para el partido, alcanza pa' 4"). Haces A/B test automático por 48 horas.

Un salto de conversión de 2,1% a 2,7% suena chico. No lo es: es +28% de pedidos para ese mismo restaurante sin gastar un peso en marketing. Si ese local hacía 400 pedidos/mes contigo, ahora hace 512. Con tu comisión de 15% (para robarle el local a Rappi) son $160.000 extra por local al mes. Con 40 locales son $6,4M de ingreso incremental. Eso es cómo le ganas a Rappi: no con más restaurantes, con hacer que los chicos vendan como grandes.

**El riesgo que nadie te dice: tu IA va a aprender a ser cuica.**

Si optimizas por "rentabilidad por entrega", tu modelo en 3 semanas va a descubrir lo que todo santiaguino sabe: conviene repartir en Providencia / Ñuñoa / Las Condes y evitar San Bernardo, La Pintana, partes de Puente Alto. Porque son viajes más largos, condominios con conserje que te hace esperar 10 min, calles con pasajes que Waze no entiende.

Y va a empezar a hacer redlining sin que te des cuenta: tiempos de entrega inflados para el sur, menos repartidores asignados, promos solo para el oriente.

Eso en EE.UU. es demanda. En Chile es funa + Dirección del Trabajo + Ley 21.431 de plataformas. Esa ley dice que si tu algoritmo asigna, castiga y desactiva repartidores de forma opaca, eres empleador encubierto. Y si un periodista muestra que tu app discrimina por comuna, estás muerto. Tienes que auditar tu modelo por comuna desde el día 1, aunque te cueste 5% de margen.

**Mi opinión impopular:**

No pongas un chatbot para clientes. Por favor.

Todo founder quiere "asistente IA que te recomienda qué comer". En Santiago a las 13:10 con hambre nadie quiere conversar con un bot. Quiere apretar 2 botones y que llegue caliente. Los chatbots de delivery bajan conversión y suben el costo: cada conversación te cuesta $80-$150 en API y te agrega 40 segundos de fricción.

Usa IA para *quitarle* opciones al cliente, no para darle más. La mejor IA de delivery es autoritaria: "Son las 20:30, llueve en Macul, estos 3 locales llegan en <25 min garantizado, el resto se demora. Elige uno." Menos elección, más cumplimiento. Rappi te da 500 opciones y falla en 100. Tú dale 8 y cumple en 8.

En resumen: no construyas otra app con IA. Construye una operación por WhatsApp + web liviana que por detrás usa IA para no colapsar cocinas y para hacer vender a las picadas. Tu moat no va a ser el modelo, va a ser tener 30 locales que venden 28% más contigo que en Rappi y por eso te dan exclusividad.

¿Quieres que te modelemos los unit economics con tus números reales?