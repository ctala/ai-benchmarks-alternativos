# Claude Opus 4.7 — news_seo_writing/news_perplexity_enrichment

- model_id: `anthropic/claude-opus-4-7`
- success: True  | final: 6.73 | quality: 8.06
- latency_total: 32.75s | tokens_per_second: 62.5
- input_tokens: 800 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y ofrece insights útiles sobre la arquitectura y precios de DeepSeek V4, con una estructura clara y adecuada para un artículo periodístico.

## Respuesta completa

# DeepSeek lanza V4: el modelo open-source chino que sacude el mercado de IA con precios agresivos

La compañía china DeepSeek anunció el lanzamiento de **DeepSeek V4**, su nueva generación de modelo de inteligencia artificial de código abierto bajo licencia MIT. La noticia llega con un dato que ya está moviendo al ecosistema global de IA: un costo de apenas **0,30 dólares por millón de tokens de entrada**, una cifra que compite directamente con los modelos comerciales más avanzados del mercado.

El anuncio, publicado en el blog oficial de la empresa y replicado por medios especializados como TechCrunch, refuerza la posición de DeepSeek como uno de los actores más disruptivos del sector, especialmente para desarrolladores y startups que buscan alternativas a los grandes proveedores estadounidenses.

## Arquitectura técnica: potencia con eficiencia

DeepSeek V4 está construido sobre una **arquitectura Mixture of Experts (MoE)**, un enfoque que se ha vuelto tendencia en la industria por su capacidad de escalar sin disparar los costos computacionales. El modelo cuenta con **236.000 millones de parámetros totales**, aunque solo **21.000 millones se activan** en cada inferencia. Esto permite obtener el rendimiento de un modelo enorme sin pagar el costo de ejecutarlo en su totalidad.

El entrenamiento se realizó sobre un corpus de **15 billones de tokens (15T)**, una cifra comparable a la de los modelos frontera de OpenAI y Anthropic. Según la información difundida por la compañía, V4 está diseñado para competir de forma directa con **GPT-4o de OpenAI y Claude Sonnet de Anthropic**, tanto en capacidades de razonamiento como en tareas de generación de código y análisis de datos.

## Precios que rompen el mercado

El aspecto que más atención ha captado es la estructura de precios. Con **0,30 dólares por millón de tokens de entrada**, DeepSeek V4 se posiciona muy por debajo de sus competidores comerciales. Pero el dato más llamativo es el **descuento del 90% en tokens cacheados**, que reduce el costo a apenas **0,03 dólares por millón de tokens**.

Esta política de caching es particularmente relevante para aplicaciones que reutilizan prompts largos, como sistemas de RAG (retrieval-augmented generation), asistentes con contexto persistente o herramientas que procesan documentos extensos de forma repetitiva. Para una startup que consume millones de tokens al mes, la diferencia frente a modelos propietarios puede representar ahorros de decenas de miles de dólares.

## Quién está detrás de DeepSeek

DeepSeek no es una startup convencional. La compañía tiene su sede en **Hangzhou, China**, y opera como un **spin-off de High-Flyer**, un fondo de cobertura cuantitativo chino con fuerte experiencia en aplicación de machine learning a mercados financieros. Este origen explica en parte su enfoque técnico y su independencia financiera.

Con apenas **300 empleados**, DeepSeek ha logrado desarrollar modelos que compiten con laboratorios que cuentan con plantillas diez veces mayores y valuaciones multimillonarias. Y lo más notable: la empresa **no ha levantado capital externo**. Está **completamente autofinanciada por High-Flyer**, un modelo poco habitual en una industria donde las rondas de miles de millones de dólares se han vuelto la norma.

Esta estructura le permite a DeepSeek tomar decisiones estratégicas sin la presión de inversionistas buscando retornos rápidos, incluyendo la de liberar sus modelos bajo licencia MIT, una de las más permisivas del ecosistema open source.

## El impacto de la licencia MIT

Publicar V4 bajo **licencia MIT** significa que cualquier empresa, incluidas las latinoamericanas, puede utilizar el modelo con fines comerciales, modificarlo, redistribuirlo e integrarlo en productos sin restricciones significativas. Esto contrasta con licencias más limitadas como la de Meta para Llama, que impone restricciones a empresas con grandes bases de usuarios.

Para el ecosistema regional, esto abre la puerta a que fintechs, healthtechs y proveedores SaaS puedan construir productos basados en un modelo frontera sin depender de APIs externas ni comprometer datos sensibles con proveedores en jurisdicciones distantes.

## Qué significa esto para tu startup

Para las startups latinoamericanas, el lanzamiento de DeepSeek V4 tiene implicaciones concretas:

- **Reducción de costos de operación:** las empresas que dependen intensivamente de LLMs para funcionalidades core, como chatbots, análisis de documentos o generación de contenido, pueden reducir su gasto en inferencia de manera significativa, especialmente si aprovechan el caching.
- **Soberanía tecnológica:** al ser open source, es posible ejecutar el modelo en infraestructura propia o en proveedores cloud regionales, lo que ayuda a cumplir con regulaciones locales de protección de datos como la LGPD en Brasil o las leyes de habeas data en varios países de la región.
- **Ventaja competitiva en mercados sensibles al precio:** en Latinoamérica, donde el ticket promedio por cliente suele ser menor que en mercados desarrollados, el costo unitario de la IA es un factor decisivo para la viabilidad del modelo de negocio.
- **Menor dependencia de un solo proveedor:** diversificar entre modelos propietarios y open source reduce el riesgo operacional ante cambios de precios, políticas o disponibilidad.

Sin embargo, también hay consideraciones importantes: