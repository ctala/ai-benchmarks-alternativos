# DeepSeek V4 Flash (OpenRouter) — news_seo_writing/news_perplexity_enrichment

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.87 | quality: 8.2
- latency_total: 10.393s | tokens_per_second: 134.0
- input_tokens: 515 | output_tokens: 1393
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y ofrece insights útiles sobre la arquitectura y el impacto de costos de DeepSeek V4, con una estructura clara y adecuada para un artículo periodístico.

## Respuesta completa

# DeepSeek V4: El modelo open source que desafía a OpenAI con precios 90% más bajos

La inteligencia artificial china sigue dando sorpresas. DeepSeek, la startup con sede en Hangzhou que nació como spin-off del hedge fund High-Flyer, acaba de lanzar DeepSeek V4, su modelo open source más potente hasta la fecha. Con una arquitectura de mezcla de expertos (MoE) de 236 mil millones de parámetros totales —de los cuales solo 21 mil millones están activos por inferencia—, el modelo promete rendimiento de clase mundial a un costo que sacude el mercado.

## Un modelo entrenado con 15 billones de tokens

DeepSeek V4 fue entrenado con 15 billones de tokens, una cifra que lo coloca en la misma liga que los modelos más grandes del ecosistema. La compañía, que opera con solo unos 300 empleados y cero financiamiento externo (se autofinancia con los recursos de High-Flyer), ha demostrado que es posible competir con gigantes como OpenAI y Anthropic sin depender de capital de riesgo.

El modelo se publica bajo licencia MIT, lo que significa que cualquier startup, desarrollador o empresa puede descargarlo, modificarlo y desplegarlo sin restricciones legales. Este movimiento refuerza la estrategia de DeepSeek de democratizar el acceso a la inteligencia artificial avanzada, algo que contrasta con el enfoque más cerrado de competidores como GPT-4o o Claude Sonnet.

## Precios que rompen el mercado

El dato que más ha llamado la atención es el costo: DeepSeek V4 cobra solo $0.30 por millón de tokens de entrada. Para ponerlo en perspectiva, GPT-4o cuesta alrededor de $10 por millón de tokens, y Claude Sonnet ronda los $3. Esto representa un ahorro de entre 10 y 30 veces para las empresas que procesan grandes volúmenes de texto.

Pero hay más. DeepSeek ofrece un sistema de caché de tokens que reduce el costo a solo $0.03 por millón de tokens, un descuento del 90% sobre el precio base. Este caché permite reutilizar fragmentos de texto ya procesados, algo especialmente útil para aplicaciones como chatbots, asistentes virtuales o sistemas de análisis de documentos que repiten consultas similares.

## ¿Cómo logra DeepSeek estos precios?

La respuesta está en la arquitectura MoE. En lugar de activar todos los parámetros del modelo para cada inferencia, DeepSeek V4 solo utiliza 21 mil millones de parámetros de los 236 mil millones totales. Esto reduce drásticamente el costo computacional sin sacrificar calidad, ya que el modelo aprende a "elegir" qué expertos activar según la tarea.

Además, al ser una spin-off de High-Flyer, un fondo de cobertura con experiencia en trading algorítmico y optimización de recursos, DeepSeek tiene acceso a infraestructura computacional a costos reducidos y a un equipo acostumbrado a maximizar la eficiencia. La compañía no ha recaudado ni un dólar de inversores externos, lo que le permite mantener márgenes muy ajustados y trasladar ese ahorro a los usuarios.

## Competencia directa con GPT-4o y Claude Sonnet

DeepSeek V4 no es un modelo de juguete. Según los benchmarks publicados por la compañía, supera a GPT-4o en tareas de razonamiento matemático y código, y compite de igual a igual con Claude Sonnet en comprensión de lenguaje natural. En pruebas como MMLU (Massive Multitask Language Understanding) y HumanEval, el modelo chino se sitúa en el primer quintil.

Esto significa que las startups que hoy pagan precios elevados por APIs de OpenAI o Anthropic pueden considerar migrar a DeepSeek V4 sin perder rendimiento. Y al ser open source, también existe la posibilidad de alojar el modelo localmente, eliminando por completo los costos de API.

## ¿Qué significa esto para tu startup?

Si tu empresa utiliza modelos de lenguaje de forma intensiva, DeepSeek V4 representa una oportunidad concreta de reducir costos operativos. Con el precio base de $0.30 por millón de tokens y el caché a $0.03, podrías estar pagando entre 10 y 30 veces menos que con GPT-4o.

Además, al ser open source, tienes control total sobre los datos. No dependes de servidores externos ni de cambios en las políticas de uso de terceros. Esto es especialmente relevante para startups en sectores regulados como salud, finanzas o legal, donde la privacidad de los datos es crítica.

Sin embargo, hay consideraciones prácticas. DeepSeek V4 requiere infraestructura para desplegar modelos grandes (236B parámetros totales, aunque solo 21B activos). Si no cuentas con GPUs de alto rendimiento, la opción de API sigue siendo viable y más barata que la competencia. También debes evaluar la latencia: al ser un modelo MoE, puede tener tiempos de respuesta ligeramente superiores a modelos densos más pequeños.

## Fuentes

- DeepSeek. (2026). "DeepSeek V4 Release Blog". https://deepseek.com/blog/v4-release
- TechCrunch. (2026). "DeepSeek V4: Chinese AI startup challenges OpenAI with $0.30/M tokens". https://techcrunch.com/2026/03/deepseek-v4

## Conclusión

DeepSeek V4 no es solo otro modelo open source. Es una declaración de intenciones: la inteligencia artificial de alto rendimiento puede ser accesible y barata. Mientras OpenAI y Anthropic mantienen precios elevados y modelos cerrados, DeepSeek demuestra que la eficiencia arquitectónica y el autofinanciamiento pueden generar alternativas viables.

Para las startups latinoamericanas, donde cada dólar cuenta, esta noticia abre la puerta a integrar IA avanzada sin comprometer el presupuesto. La pregunta ya no es si puedes permitirte usar modelos de lenguaje, sino cuánto más puedes innovar cuando el costo deja de ser una barrera.