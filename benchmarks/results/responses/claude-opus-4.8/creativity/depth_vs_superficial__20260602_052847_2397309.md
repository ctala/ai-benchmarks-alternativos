# Claude Opus 4.8 — creativity/depth_vs_superficial

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 7.3 | quality: 9.84
- latency_total: 27.754s | tokens_per_second: 52.5
- input_tokens: 247 | output_tokens: 1458
- judge_score: 5 | justificación: La respuesta ofrece ideas específicas y no obvias, incluye estimaciones concretas, aborda un riesgo regulatorio poco mencionado, y presenta una opinión contrarian bien fundamentada, todo de manera clara y organizada.

## Respuesta completa

Antes de tirarte ideas, una pregunta incómoda: ¿realmente tienes un problema que la IA resuelve, o estás buscando excusas para meter "IA" en tu pitch deck porque suena bien? La mayoría de startups de delivery en Chile mueren por unit economics rotos, no por falta de IA. Si tu costo de adquisición es de $8.000 CLP y tu margen por pedido es $1.200, ningún modelo de ML te salva. Dicho esto, vamos a lo bueno.

**Idea 1: Predicción de cancelaciones para no cocinar al vacío**

El problema real en Santiago no es la ruta, es que los restaurantes pequeños empiezan a preparar pedidos que después se caen (cliente que se arrepiente, dirección mal puesta en Las Condes vs. La Florida, repartidor que no llega). Cada pedido cancelado a mitad de preparación es comida tirada + costo laboral perdido.

Construye un modelo que asigne un "score de probabilidad de completarse" en el momento del pedido, usando señales como: método de pago (efectivo tiene 3-4x más tasa de cancelación que tarjeta guardada), si es cliente nuevo, hora del día, monto del pedido, y distancia. Los pedidos de bajo score esperan 90 segundos antes de mandarse a cocina o piden confirmación. Si reduces cancelaciones de comida ya preparada de un 8% a un 5%, en un restaurante que hace 100 pedidos/día con ticket de $9.000, recuperas ~$270.000 CLP/mes por local. Eso es real y medible.

**Idea 2: Pricing dinámico de la tarifa de envío según densidad de batching**

Todos piensan en surge pricing tipo Uber. Lo no obvio es lo contrario: ofrecer descuentos de envío en tiempo real cuando tu sistema detecta que un nuevo pedido puede "batchearse" con uno ya en ruta hacia la misma zona. En Santiago la geografía ayuda: barrios densos (Providencia, Ñuñoa) tienen patrones predecibles. Si puedes agrupar 2 entregas en un trayecto, tu costo marginal del segundo envío baja ~40%. Comparte parte de ese ahorro con el cliente ("Envío a $990 si pides en los próximos 8 minutos") para inducir el batch. Esto mejora densidad sin canibalizar margen.

**El riesgo no obvio:**

No es técnico, es regulatorio-reputacional. Chile tiene la Ley 21.431 (regulación de plataformas digitales de trabajo) vigente desde 2022. Si usas IA para asignar repartidores, la ley te obliga a transparencia algorítmica y a permitir que el repartidor entienda cómo se le asignan pedidos y se calcula su pago. Un modelo de "caja negra" que optimice asignación puede meterte en problemas con la Dirección del Trabajo si los repartidores alegan discriminación algorítmica. Diseña tu sistema con explicabilidad desde el día 1, no lo parchees después.

**Mi opinión contrarian:**

El delivery en Chile no necesita más IA en el corto plazo, necesita menos. Rappi, PedidosYa y Uber Eats ya tienen modelos infinitamente mejores que cualquier cosa que vas a construir con tu equipo de 3 personas, y aún así sangran plata. Tu ventaja no va a ser algorítmica, va a ser de nicho y operación física. Si yo fuera tú, gastaría el 80% del presupuesto en resolver el último kilómetro de un vertical específico (ej: comida coreana en zona oriente, o almuerzos corporativos en Sanhattan con ventana de 12:00-13:30) y solo un 20% en IA, y esa IA debería ser herramientas existentes (APIs de OpenAI para soporte al cliente, no entrenar tus propios modelos). Construir IA propia siendo seed-stage en delivery es, casi siempre, masturbación de ingenieros.

¿Cuál es tu vertical y qué números tienes hoy? Sin eso, todo lo anterior son hipótesis bonitas.