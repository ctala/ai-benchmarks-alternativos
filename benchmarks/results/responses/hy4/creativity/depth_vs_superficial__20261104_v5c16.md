# Tencent Hy4 — creativity/depth_vs_superficial

- model_id: `tencent/hy4`
- success: True  | final: 8.45 | quality: 10.0
- latency_total: 73.996s | tokens_per_second: 92.1
- input_tokens: 167 | output_tokens: 6812

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

Antes de hablar de modelos, déjame decirte algo incómodo: si estás en Santiago compitiendo contra Rappi y PedidosYa, meterle IA a las rutas o a la predicción de demanda es quemar plata para llegar al mismo sitio donde ellos llegaron el 2019. Tienen 100x tu telemetría. No les juegues en su cancha.

Lo que yo haría se mete en dos rendijas que sus algoritmos todavía ignoran: los últimos 40 metros verticales, y los 15 minutos de plancha bajo lluvia.

**La primera rendija es el lobby, no la calle.** En el eje Apoquindo–Providencia calculo que entre el 55% y 60% de tus pedidos caen en torres con conserjería. Tu GPS marca "llegó" a las 20:14, pero el *handoff* real es 20:20: son 4 a 7 minutos muertos de RUT anotado en el cuaderno, llamado al depto 1204 y espera del ascensor de carga. Todos optimizan el taco de Costanera Norte; nadie le ha tomado el tiempo al ascensor. Monta un gradient boosting de 50 KB (ni se te ocurra un LLM para esto) que cruce el delta `GPS_arrival → handoff` por dirección exacta y franja horaria. Vas a encontrar que en el cambio de turno de conserjes (14:00 y 22:00) la varianza salta +3,2 min, y que las torres de ascensor único penalizan ~90 segundos cada 10 pisos. El *move* no es recalcular la ruta: es pre-despachar un WhatsApp a la conserjería 90 segundos antes (*"Viene Diego, Depto 804, #4491, sube ya"*) y ajustar el ETA prometido **por edificio**. En 10.000 pedidos/mes son ~120 horas-repartidor recuperadas y una desviación estándar que baja de 6 a 1,8 min, sin mover una sola bicicleta.

**La segunda rendija va al revés del sentido común: usa IA para censurar el catálogo, no para personalizarlo.** Te van a decir "mete un modelo que recomiende el sushi según el historial". Error de principiante. Un martes de junio, con 2 mm/h de lluvia entre las 19:00 y 20:30, el tráfico sube ~40%, pero lo que revienta es la cocina: el prep-time de las frituras pasa de 11 a 22 min y te cancelan ~15% de las órdenes. En vez de predecir *qué quiere* el cliente, ingiere el radar de la Dirección Meteorológica, el delta de tickets de tu POS y el taco, y reescribe la oferta **hacia atrás** en vivo: escondes la milanesa con papas (18 min, se aguada en la mochila térmica) y empujas la cazuela o la empanada pre-batcheada (4 min, aguanta 30 min de taco sin perder textura). No es recomendación, es degradación controlada. La cola baja de 22 a 9 min sacrificando apenas 3 SKUs durante 45 minutos. El cliente no nota que le quitaste opciones; nota que no le cancelaste.

**El riesgo que no sale en ningún *due diligence* es la atrofia del "calle".** No hablo de sesgo, ni de privacidad, ni del costo de los tokens. Hablo de que, al automatizar el conserje y la plancha, estás externalizando el conocimiento tácito de tu flota. Hoy un *rider* senior ya sabe que *"en Apoquindo 3300 el Pedro es lento, pero en la Torre B me abren de una"*. Si la API hipa un viernes de pago a las 20:15, con lluvia y taco, te quedas sin ese instinto: el repartidor ya no sabe negociar el lobby porque el modelo lo venía haciendo por él. Deja siempre un *fallback* crudo por SMS y rota a los senior por los edificios nuevos para que el *ground truth* no se te pudra dentro del modelo.

**Y acá va la parte impopular:** para una startup chilena, la IA no tiene que hacerte más inteligente, tiene que hacerte *más aburrido*. Rappi te da 400 platos y una mentira optimista ("28 min") que falla 1 de cada 4 veces. Tú da 12 platos y una verdad exacta. Pero cuidado con el efecto lupa: si tu modelo es tan bueno que muestra "34 min" donde la competencia muestra "28", el usuario santiaguino —entrenado por años en el ETA mentiroso— te lee como **más lento** y abandona el carrito, aunque tu varianza real sea la mitad. La precisión sin re-educación de expectativas te castiga. El sistema tiene que saber mentir 2 minutos a propósito, y saber exactamente por qué lo hace.

Por eso, no contrates todavía un ML Engineer. Gasta ese sueldo en un practicante con un cronómetro, sentado dos semanas en tres conserjerías de Las Condes. El cuello de botella acá no es el algoritmo; es que nadie ha medido el ascensor.