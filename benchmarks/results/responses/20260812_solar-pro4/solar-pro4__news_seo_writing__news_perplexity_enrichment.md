# Solar Pro 4 — news_seo_writing/news_perplexity_enrichment

- model_id: `upstage/solar-pro4`
- success: True  | final: 8.86 | quality: 9.6
- latency_total: 29.301s | tokens_per_second: 68.3
- input_tokens: 559 | output_tokens: 2001
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una profundidad significativa al integrar datos adicionales de manera efectiva. La claridad y estructura son excelentes, y la utilidad práctica para un emprendedor es alta. Además, el estilo periodístico y la estructura SEO son adecuados para un artículo publicable.

## Respuesta completa

## DeepSeek V4: la apuesta open-source que redefine el costo del cómputo

DeepSeek acaba de lanzar V4, su modelo de lenguaje más reciente, bajo una licencia MIT que lo coloca en el corriente de la apertura que ha marcado los últimos ciclos del ecosistema de inteligencia artificial. La compañía, con sede en Hangzhou, China, posiciona esta versión no como un producto de servicio, sino como un modelo disponible para quien quiera ejecutarlo, adaptarlo o distribuirlo. La tarifa publicada para su uso es de $0,30 por millón de tokens de entrada, un número que, en el contexto actual de precios de APIs, despierta tanto la curiosidad técnica como la atención de quienes diseñan arquitecturas de costos.

Lo que distingue a V4 no es solo el precio de entrada, sino cómo está construido. La versión utiliza una arquitectura MoE (mixture of experts) con 236 mil millones de parámetros en total, de los cuales solo 21 mil millones se activan por token durante la inferencia. Esa diferencia entre el tamaño total del modelo y la cantidad de parámetros que realmente trabajan en cada paso es clave para entender por qué el costo por millón de tokens puede mantenerse en rangos bajos sin sacrificar capacidad. El entrenamiento se llevó a cabo con 15 billones de tokens, una escala que ha sido habitual en los modelos de última generación, pero que aquí se combina con un diseño que prioriza la eficiencia en el momento de usar el modelo, no solo en el entrenamiento.

## El detalle del cache y su impacto en la factura

Un punto que no puede pasarse por alto es el cache de tokens. DeepSeek indica que el almacenamiento en cache tiene un costo de solo $0,03 por millón de tokens, una reducción del 90 % respecto a la tarifa base. Esa cifra cambia la ecuación para aplicaciones que repiten consultas, mantienen contextos largos o reutilizan bloques de prompts estructurados. Para un equipo que diseña un flujo con múltiples pasos, la diferencia entre $0,30 y $0,03 por millón de tokens no es marginal: redefine qué tipo de interacciones son viables y cuáles se vuelven prohibitivas a escala.

Este mecanismo tiene sentido con la forma en que se construyen pipelines de producción hoy. En escenarios con reintentos, validaciones, generación de varias variantes o consultas repetitivas sobre los mismos documentos, el cache puede convertir un modelo de alto rendimiento en una herramienta con costos predecibles. La pregunta técnica ya no es solo cuánto cuesta procesar un token nuevo, sino cuánto ahorra el sistema al no volver a computar lo que ya está disponible.

## De un hedge fund a un modelo open-source

El origen de la empresa también forma parte de la historia. DeepSeek es un spin-off del fondo de cobertura High-Flyer y mantiene su operación en Hangzhou. Según los datos disponibles, la compañía ha contado con un equipo de aproximadamente 300 empleados y no ha recaudado financiamiento externo; su desarrollo ha sido autofinanciado a través de High-Flyer. Esa estructura es relevante porque explica una parte de la dinámica de lanzamiento: sin round de capital, sin presión de rentabilidad a corto plazo orientada a inversores externos, el modelo puede moverse con una lógica distinta a la de startups que necesitan demostrar métricas de crecimiento rápido.

Esto no significa que la empresa esté fuera del mercado. Al contrario, V4 compite directamente con GPT-4o y Claude Sonnet, dos de los referentes más mencionados en conversaciones de producto y de integración. La comparación no es solo nominal: pone sobre la mesa la pregunta de si un modelo open-source, con una licencia MIT y un precio estructurado en torno al millón de tokens, puede ofrecer un punto de entrada competitivo para equipos que hoy dependen de APIs propietarias.

## Por qué el precio y la licencia importan en Latinoamérica

En el ecosistema de startups de la región, el costo del inference suele ser una variable determinante desde el primer prototipo. No todas las compañías tienen acceso a créditos de nube generosos, ni pueden asumir experimentación ilimitada en etapas tempranas. Un modelo con licencia MIT reduce la fricción legal y operativa para quien quiere llevarlo a producción, ajustarlo a un caso de uso local o ejecutarlo en infraestructura propia sin depender de un contrato comercial complejo.

La tarifa de $0,30 por millón de tokens de entrada, junto con el cache a $0,03 por millón, ofrece una línea base que permite hacer cálculos más concretos. Para un equipo que está evaluando si integrar un modelo en un producto con alto volumen de lectura y reutilización de contexto, el descuento del 90 % en cache puede ser la diferencia entre un flujo viable y uno que se vuelve costoso apenas cruza cierto umbral de uso. Eso importa tanto para una startup en etapa de validación como para una empresa que ya tiene usuarios y necesita controlar la factura de IA.

## Lo que se mantiene en la mesa técnica

Hay varios elementos que vale la pena señalar sin sobreinterpretar. La arquitectura MoE con 236 mil millones de parámetros totales y 21 mil millones activos sugiere un compromiso entre capacidad y eficiencia. El entrenamiento con 15 billones de tokens sitúa al modelo en un rango de exposición comparable a otros sistemas de última generación. La combinación de estos factores con una licencia abierta y un precio publicado explica por qué V4 se lee como una alternativa directa frente a modelos propietarios como GPT-4o y Claude Sonnet.

También es útil mantener la mirada en el tamaño de la operación. Con alrededor de 300 empleados y un desarrollo autofinanciado, DeepSeek muestra una trayectoria distinta a la de compañías que escalan mediante rondas sucesivas. Eso no garantiza nada por sí solo, pero sí indica que la estrategia de lanzamiento puede estar más orientada a la adopción y al ecosistema que a una narrativa de crecimiento financiero inmediato.

## Qué significa esto para tu startup

Si estás evaluando modelos de lenguaje para un producto, V4 introduce tres variables prácticas. Primera, la licencia MIT reduce la carga legal y facilita la experimentación, especialmente si tu equipo necesita modificar, desplegar o integrar el modelo sin atravesar condiciones de licenciamiento propietario. Segunda, el precio por millón de tokens de entrada y el costo del cache permiten modelar mejor los gastos operativos, especialmente en flujos con repetición de prompts, contextos largos o múltiples iteraciones.

Tercera, la arquitectura MoE puede ser un punto de partida interesante para quienes necesitan inferir a escala sin comprometer capacidad en tareas complejas. La clave está en cómo tu caso de uso explota o no el cache, y en qué parte del flujo puede beneficiarse de una inferencia más ligera por token. Para productos con alto volumen de lectura, recuperación de contexto o generación iterativa, esa combinación de licencia, precio y cache merece un lugar en la lista de evaluación.

## Conclusión

DeepSeek V4 no llega como un anuncio aislado, sino como una propuesta que junta licencia abierta, arquitectura eficiente y precios que invitan a recalcular la ecuación del costo por token. El modelo compite en terreno que antes se asociaba más a soluciones propietarias, y lo hace desde una estructura de empresa diferente: autofinanciada, con un equipo reducido respecto a los gigantes del sector y con un lanzamiento que pone énfasis en la disponibilidad y el uso.

Eso no significa que sea la opción correcta para todos los escenarios. Significa, en cambio, que hay un nuevo punto de referencia en la conversación sobre qué cuesta usar un modelo de lenguaje, cómo se comporta cuando se diseña para reutilización y qué papel puede jugar un modelo open-source en la decisiones de producto. Para startups y equipos de tecnología en Latinoamérica, la pregunta ya no es solo qué modelo es mejor en benchmark, sino cuál se ajusta mejor a la realidad de costos, infraestructura y restricciones de despliegue de cada proyecto.

## Fuentes

- https://deepseek.com/blog/v4-release
- https://techcrunch.com/2026/03/deepseek-v4