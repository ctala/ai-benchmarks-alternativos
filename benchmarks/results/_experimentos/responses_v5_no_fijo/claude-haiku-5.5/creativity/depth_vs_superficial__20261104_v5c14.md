# Claude Haiku 5.5 — creativity/depth_vs_superficial

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 23.612s | tokens_per_second: 166.0
- input_tokens: 249 | output_tokens: 3920

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

Antes de decidir qué IA usar, te conviene saber qué te está costando más dinero. En delivery casi nunca es la ruta. Suelen ser el tiempo ocioso del repartidor, las devoluciones por comida en mal estado y la comisión que cobran los marketplaces. Estas son mis ideas, con cifras que son estimaciones para que las valides con tus datos.

**1. Predecir cuándo el pedido estará listo, no cuándo llegará el repartidor**
La mayoría de las apps despacha al repartidor al confirmarse el pedido, y el repartidor espera en el local. Si un repartidor espera en promedio 6 minutos por pedido y haces 1.000 pedidos al día, son 100 horas-repartidor perdidas diarias. A un costo de unas CLP 5.000 por hora efectiva, eso son unos CLP 500.000 diarios sin generar nada. Un modelo que prediga el tiempo real de preparación por local, según hora, tipo de plato, carga actual y el historial de ese local, permite despachar en el momento justo. Es un problema de predicción de series de tiempo con datos que ya tienes, no de optimización de rutas.

**2. Usar las reseñas negativas como sensor de empaque y menú**
Un porcentaje de las devoluciones suele venir de platos que no sobreviven el viaje: papas fritas, sushi, salsas que se derraman, arroz que se apelmaza. Puedes entrenar un clasificador con reseñas que mencionen "llegó frío", "aplastado", "derramado" o "blando", y cruzarlo con el tipo de plato y la distancia. El resultado es una lista concreta para cada local: "cambia el envase de este plato" o "no lo vendas a más de 4 km". Si las devoluciones están en torno al 3–5% del volumen, reducirlas a la mitad puede ahorrar bastante más de lo que cuesta el modelo. Son cifras orientativas, mídelas en tu caso.

**3. Vender la IA a los restaurantes, no al cliente**
Los restaurantes en Chile pagan comisiones de entre 20% y 30% en los marketplaces grandes, y muchos pierden plata en el canal delivery sin darse cuenta. Una herramienta que calcule la rentabilidad real de cada plato en delivery (costo de insumos + comisión + envase + subsidio de envío) y sugiera precios diferenciados por canal puede ser un producto de suscripción separado. Ese ingreso no depende de tener la mejor flota.

**Riesgo no obvio: la gestión algorítmica puede convertir eficiencia en pasivo legal**
En Chile rige la Ley 21.431 sobre trabajadores de plataformas de reparto, que reconoce derechos laborales y obliga a cierta transparencia en la asignación de pedidos y en los sistemas de calificación. Si tu IA asigna pedidos según rapidez, penaliza el rechazo de viajes y desactiva a los repartidores con mala calificación, estás construyendo un sistema de control y subordinación. Esa es justamente la señal que usan los tribunales y la Dirección del Trabajo para decidir si hay relación laboral. Lo que ahorraste en optimización puede volver como multas o reclasificación masiva. Antes de programar el algoritmo, consulta con un abogado laboral qué variables puedes usar y cuáles no. Y diseña el sistema para que los criterios sean explicables.

**Opinión contraria: no deberías construir tu propio motor de despacho todavía**
La tentación es hacer algo sofisticado, pero el motor de despacho solo rinde cuando tienes densidad: muchos pedidos en pocas cuadras y en las mismas horas. Con pocos pedidos por zona, cualquier algoritmo es ruido, y una asignación manual bien hecha por una persona gana. Mi recomendación es que durante los primeros seis meses no uses IA para despacho. Úsala para predicción de preparación (idea 1) y para análisis de reseñas (idea 2), que funcionan con volúmenes bajos. Compite en nichos densos, como el almuerzo de oficina en Sanhattan o comunas específicas, en lugar de intentar superar a PedidosYa en cobertura. La ventaja no será el algoritmo, sino tener restaurantes y clientes concentrados donde el algoritmo tenga algo que aprender.

**Tres preguntas para ti antes de elegir**
- ¿Cuántos pedidos diarios haces hoy por comuna y por franja horaria?
- ¿Qué porcentaje de tu costo variable es repartidor, comisión y devoluciones? Sin ese número no sabes qué optimizar.
- ¿Tus repartidores son independientes bajo la ley de plataformas o estás planeando un modelo distinto? Esa decisión define cuánto puedes automatizar sin riesgo.