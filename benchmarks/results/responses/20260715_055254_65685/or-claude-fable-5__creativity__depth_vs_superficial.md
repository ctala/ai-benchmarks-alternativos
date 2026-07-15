# Claude Fable 5 — creativity/depth_vs_superficial

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.89 | quality: 10.0
- latency_total: 49.553s | tokens_per_second: 62.1
- input_tokens: 247 | output_tokens: 3077
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece ideas profundas y específicas que van más allá de lo obvio, con claridad y utilidad práctica para un emprendedor, además de ser original en su enfoque.

## Respuesta completa

Primero, una advertencia honesta: si tu plan es "delivery de comida + IA" como propuesta de valor, tienes un problema más grande que la tecnología. En Santiago compites contra PedidosYa, Rappi y Uber Eats, que juntos controlan sobre el 90% del mercado y llevan años quemando plata en los problemas obvios de IA (rutas, matching, recomendaciones). No les vas a ganar en eso con un equipo de 5 personas. La pregunta correcta no es "cómo uso IA" sino "qué costo estructural puedo atacar que los grandes no pueden por su tamaño".

Dicho eso, aquí van ideas que sí tienen sentido:

**1. Ataca el tiempo de cocina, no el de ruta**

El cuello de botella real en delivery no es el trayecto: es el repartidor esperando afuera del restaurante. En Santiago un rider espera en promedio 6-10 minutos por pedido, y eso es la diferencia entre hacer 2 y 2.5 entregas por hora. Si tu costo por entrega es ~$2.500 CLP, ese salto reduce tu costo unitario en ~20%, que en un negocio donde el margen por orden es de $300-800 CLP es literalmente la diferencia entre quebrar y no.

La IA útil aquí es aburrida: un modelo (gradient boosting basta, no necesitas LLMs) que prediga el tiempo de preparación *real por restaurante, por plato, por hora del día* y despache al rider en el momento correcto. Los restaurantes mienten sistemáticamente sobre sus tiempos, y su varianza es información valiosísima que nadie usa bien: puedes penalizar en el ranking a los restaurantes impredecibles, no solo a los lentos.

**2. Onboarding de restaurantes con LLM: ataca el CAC, no la app**

Adquirir un restaurante con vendedores cuesta $150-300 USD entre visitas, negociación y digitalización del menú. Los locales pequeños de barrio (donde los grandes tienen menos penetración) muchas veces ni siquiera tienen menú digital. Un pipeline donde el dueño saca una foto al menú de papel, un LLM lo estructura, genera descripciones y fotos categorizadas, y el local está operativo en 20 minutos, te puede bajar el CAC a $20-30 USD. Ahí sí tienes una ventaja: puedes rentabilizar la cola larga de restaurantes que a Rappi no le conviene ir a buscar.

**3. Visión computacional contra el fraude de reembolsos**

En LatAm el fraude de "mi pedido no llegó / llegó incompleto" corre entre 1.5% y 3% del GMV. Foto obligatoria en entrega + un modelo que verifique coherencia (bolsa sellada, cantidad de ítems, ubicación GPS vs dirección) te recupera 1-2 puntos de margen. Nadie habla de esto porque no es sexy, pero en un negocio de márgenes de 3-5%, es enorme.

**El riesgo no obvio: gestión algorítmica de repartidores es un campo minado legal en Chile**

Chile tiene la Ley 21.431 de trabajadores de plataformas digitales, que exige *transparencia sobre los criterios del algoritmo* que asigna pedidos y evalúa a repartidores. Si tu IA de matching baja el score de un rider y le asigna menos pedidos, eso puede interpretarse como sanción encubierta o discriminación algorítmica. Ya pasó en Europa: Deliveroo fue multada en Italia porque su algoritmo "Frank" discriminaba indirectamente. Además, la nueva Ley 21.719 de protección de datos (vigente desde diciembre 2026) crea una agencia fiscalizadora con multas de hasta 4% de ingresos anuales, y perfilar usuarios con IA va a requerir bases de licitud claras. Diseña tus modelos con explicabilidad desde el día uno; retrofitear eso después es carísimo.

**Mi opinión contrarian**

La IA generativa —lo que todos quieren meter en su pitch— es lo *menos* valioso para tu caso. Un chatbot de atención al cliente o recomendaciones "personalizadas con GPT" son commodity: tus competidores las tienen mejores y al usuario le dan lo mismo. El ML valioso en delivery es invisible, aburrido y operacional: predicción de tiempos, detección de fraude, pricing de zonas. Y segundo punto incómodo: si tu startup necesita la palabra "IA" en el pitch para ser interesante, el problema es el negocio, no la tecnología. La IA debería aparecer en tu estructura de costos, no en tu landing page.

¿Cuál es tu ángulo de diferenciación real contra los incumbentes? Porque de esa respuesta depende cuál de estas ideas te sirve y cuáles son ruido.