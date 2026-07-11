# GPT-5.6 Luna — creativity/depth_vs_superficial

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 8.3 | quality: 9.76
- latency_total: 21.659s | tokens_per_second: 132.8
- input_tokens: 139 | output_tokens: 2876
- judge_score: 5 | justificación: La respuesta ofrece ideas específicas y profundas, como el uso de un 'ETA honesto' y un 'mapa de fricción de edificios', con detalles técnicos y estimaciones concretas, lo que la hace altamente relevante, precisa y útil para un emprendedor.

## Respuesta completa

Yo no empezaría con un chatbot ni con “optimización de rutas”. En delivery, el problema más caro normalmente no es encontrar el camino más corto: es prometer una hora que la operación no puede cumplir y luego pagar el costo de la decepción.

Mi tesis para Santiago sería: **usar IA para hacer la operación más predecible, no necesariamente más sofisticada**.

## 1. Construiría un “ETA honesto”, no un ETA promedio

La mayoría de las plataformas calcula algo parecido a:

> tiempo estimado de preparación + tiempo estimado de viaje

Eso falla porque trata como constantes cosas que en Santiago son altamente variables:

- El mismo restaurante puede tardar 12 minutos un martes a las 16:00 y 38 minutos un viernes a las 20:30.
- Un edificio en Las Condes puede agregar 8 minutos por estacionamiento, conserjería y ascensor.
- En Santiago Centro, los últimos 300 metros pueden ser más impredecibles que los primeros 5 kilómetros.
- La lluvia, un partido en el Estadio Nacional o una marcha en la Alameda alteran más el ETA que una diferencia de 500 metros.

Usaría un modelo de **predicción por percentiles**, no una sola predicción. Por ejemplo:

- ETA optimista: percentil 50.
- ETA prometido: percentil 80 o 85.
- Alerta interna: si la probabilidad de llegar después del ETA supera 25%.

El modelo debería separar al menos cuatro componentes:

1. Tiempo hasta que el restaurante acepta el pedido.
2. Tiempo de preparación real, inferido de eventos de cocina, no del tiempo declarado.
3. Tiempo de espera del repartidor en el local.
4. Tiempo de acceso final: estacionamiento, ascensor, conserjería y entrega.

La interfaz podría seguir mostrando “30–40 minutos”, pero internamente la plataforma sabría que hay un 70% de probabilidad de entregar antes de 37 minutos y un 20% después de 42.

### ¿De dónde sale la ventaja?

No usaría inicialmente un modelo grande de lenguaje. Usaría gradient boosting o modelos de supervivencia con datos como:

- restaurante, hora y día;
- cantidad de ítems y modificaciones;
- tamaño de la cola de pedidos;
- tiempo entre “aceptado”, “listo” y “retirado”;
- comuna y tipo de edificio;
- lluvia y eventos masivos;
- disponibilidad real de repartidores.

Una estimación razonable para un piloto: si una operación tiene 15% de pedidos con retraso significativo y el modelo reduce esa tasa a 11%, en 1.000 pedidos diarios habría 40 incidentes menos. Si cada incidente genera, entre compensación, soporte y pérdida de repetición, unos **$2.000–$4.000 CLP**, el valor directo sería de **$80.000–$160.000 diarios**, sin contar el impacto en retención.

La métrica importante no sería “accuracy del modelo”, sino:

- error absoluto mediano del ETA;
- porcentaje entregado antes del límite prometido;
- cancelaciones posteriores a la hora prometida;
- costo de compensaciones por pedido;
- repetición del cliente a 30 días.

## 2. Crearía un “mapa de fricción de edificios”

Esta es menos obvia y posiblemente más valiosa que una mejora marginal de rutas.

En Santiago, la última parte de la entrega no es geográficamente difícil, pero sí operativamente difícil. La plataforma debería aprender, de forma agregada, características como:

- entrada correcta del edificio;
- si el acceso es por calle principal o estacionamiento;
- si hay conserjería 24/7;
- si el ascensor requiere autorización;
- si el repartidor debe llamar antes de subir;
- dónde se entrega cuando el cliente no responde;
- tiempo típico entre llegar a la dirección y marcar “entregado”.

En vez de guardar simplemente “Av. X 1234”, se puede construir una ficha operacional:

> “Torre B; entrada por calle lateral; conserjería pide número de departamento; ascensor lento entre 20:00 y 22:00; no dejar en recepción salvo autorización.”

Eso puede generarse a partir de las instrucciones escritas por repartidores, tiempos de geolocalización y confirmaciones de clientes. Un modelo de lenguaje puede normalizar esos comentarios, pero la fuente de verdad debe ser el comportamiento observado.

Si el tiempo de entrega final cae solo de 7 a 5 minutos, en 1.000 pedidos diarios son aproximadamente **33 horas operativas recuperadas por día**. Dependiendo de si el repartidor es pagado por hora, por bloque o por pedido, eso puede traducirse en capacidad para 50–100 pedidos adicionales sin aumentar proporcionalmente la flota.

La intervención no tiene que ser compleja:

- mostrar al repartidor instrucciones específicas antes de llegar;
- solicitar al cliente el número de departamento en edificios problemáticos;
- avisar al conserje mediante un flujo preacordado;
- ordenar los pedidos de una misma torre para entregarlos en una sola subida;
- dejar de aceptar pedidos con ETA falso cuando el edificio tiene una restricción conocida.

Aquí sí hay una ventaja local difícil de copiar: después de miles de entregas, el sistema tendría conocimiento operacional de los edificios, no solo de las calles.

## 3. Otra apuesta: predecir cuándo un restaurante debería rechazar pedidos

La plataforma suele premiar al restaurante que acepta todo, aunque luego se atrase y produzca reembolsos. Eso es un error de diseño.

Podría construir un modelo de **capacidad latente del restaurante**. No preguntaría únicamente “¿está abierto?”, sino:

> “Dado el número actual de pedidos, los platos solicitados, la hora y el ritmo de preparación de los últimos 20 minutos, ¿qué probabilidad hay de que este pedido salga en más de 35 minutos?”

Si la probabilidad supera, por ejemplo, 60%, el sistema podría:

- retirar temporalmente ciertos platos;
- aumentar el ETA mostrado;
- limitar el radio de entrega;
- derivar la demanda a otro restaurante;
- ofrecer solo productos de preparación rápida.

Esto parece anti-crecimiento porque reduce pedidos en ciertos momentos, pero puede mejorar el margen. Un pedido adicional que termina en devolución no vale lo mismo que un pedido perdido antes de prepararse.

Supongamos:

- ticket promedio: $18.000;
- comisión efectiva: $3.600;
- fee de despacho: $2.500;
- costo del repartidor: $3.000;
- pagos, soporte e incentivos: $1.000;
- contribución aproximada antes de costos fijos: $2.100.

Si un 10% de los pedidos atrasados termina en compensación de $3.000 y además reduce la probabilidad de recompra, un sistema que rechace 3% de la demanda en el pico pero reduzca a la mitad los incidentes puede ser económicamente superior. La plataforma no debería optimizar “cantidad de pedidos”; debería optimizar **contribución esperada por pedido y probabilidad de recompra**.

## El riesgo no obvio

El riesgo más peligroso no es que la IA se equivoque en una ruta. Es que el sistema aprenda **sesgos operacionales y los convierta en una política comercial aparentemente racional**.

Ejemplo:

- Los repartidores tardan más en ciertos edificios porque los consideran incómodos.
- El modelo aprende que esas direcciones tienen baja rentabilidad.
- La plataforma comienza a darles ETAs peores, cobrarles más o dejar de ofrecerles determinados restaurantes.
- Menos repartidores aceptan esos pedidos.
- El sistema observa que efectivamente son menos rentables y refuerza la decisión.

Eso puede crear “zonas de servicio degradado” en barrios, edificios o tipos de clientes sin que nadie haya programado una discriminación explícita. También puede ocurrir que las instrucciones de acceso revelen rutinas de conserjes, puntos de entrada o patrones de ausencia, creando un riesgo de seguridad y privacidad.

Mitigaciones concretas:

- no usar dirección exacta como sustituto de nivel socioeconómico;
- auditar ETA, tasa de aceptación y cancelación por comuna y tipo de dirección;
- anonimizar instrucciones de edificios y limitar quién puede verlas;
- no almacenar más precisión de ubicación de la necesaria;
- imponer un piso mínimo de servicio por zona;
- revisar manualmente decisiones que afecten precio o disponibilidad.

Esto además importa en Chile por la evolución de las obligaciones de protección de datos; aunque la empresa sea pequeña, no conviene diseñar una base de datos de ubicación y hábitos como si fuera información operacional inocua.

## Mi opinión contrarian

**Una startup de delivery probablemente no debería usar IA durante los primeros meses, salvo que ya tenga datos operacionales suficientes.**

Con menos de aproximadamente **300–500 pedidos diarios**, muchos modelos no estarán aprendiendo “patrones”; estarán memorizando ruido de pocos restaurantes y pocas comunas. En esa etapa, una hoja de cálculo bien diseñada, reglas explícitas de capacidad y mejores procesos con restaurantes pueden producir más valor que un equipo de machine learning.

Y tampoco intentaría ganar por “la mejor IA”. Las plataformas grandes ya pueden comprar modelos mejores. La ventaja defendible sería un dataset propio de:

- tiempos reales de preparación;
- fricciones específicas de edificios;
- confiabilidad por franja horaria;
- probabilidad de cancelación;
- costo de servir cada microzona.

Empezaría con un piloto de 6–8 semanas en Providencia, Ñuñoa y Santiago Centro, con 20–30 restaurantes y una métrica muy concreta: **reducir retrasos y contactos de soporte sin aumentar el costo por pedido**. Si no se puede demostrar una mejora en esos términos, no agregaría más IA. En delivery, la inteligencia no está en tener un modelo impresionante; está en saber exactamente qué error operativo se está comprando y cuánto vale corregirlo.