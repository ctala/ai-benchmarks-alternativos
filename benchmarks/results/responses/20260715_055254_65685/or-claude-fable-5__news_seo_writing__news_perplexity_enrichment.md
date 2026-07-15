# Claude Fable 5 — news_seo_writing/news_perplexity_enrichment

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 6.92 | quality: 8.6
- latency_total: 41.119s | tokens_per_second: 68.6
- input_tokens: 795 | output_tokens: 2821
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y ofrece una buena profundidad con insights útiles, especialmente para emprendedores, mientras mantiene claridad y un estilo periodístico adecuado.

## Respuesta completa

## DeepSeek V4: el modelo open-source que baja el precio de la IA a $0.30 por millón de tokens

DeepSeek, la empresa china de inteligencia artificial con sede en Hangzhou, lanzó V4, la nueva versión de su modelo de lenguaje de código abierto bajo licencia MIT. El anuncio llega con una cifra que captura toda la atención del mercado: $0.30 por millón de tokens de entrada, un precio que presiona directamente a los modelos comerciales líderes como GPT-4o de OpenAI y Claude Sonnet de Anthropic.

Para el ecosistema emprendedor latinoamericano, donde el costo de la infraestructura de IA suele ser una de las principales barreras de adopción, este lanzamiento merece un análisis detallado.

## Arquitectura MoE: potencia sin el costo computacional completo

DeepSeek V4 utiliza una arquitectura Mixture of Experts (MoE) con 236 mil millones de parámetros totales, de los cuales solo 21 mil millones se activan en cada inferencia. Esta es la clave técnica detrás de su precio agresivo.

En términos prácticos, la arquitectura MoE funciona como un equipo de especialistas: en lugar de que todo el modelo procese cada consulta, solo se activan los "expertos" relevantes para cada tarea. El resultado es un modelo con la capacidad de razonamiento de un sistema masivo, pero con costos de cómputo cercanos a los de un modelo mucho más pequeño.

El entrenamiento se realizó con 15 billones (trillions) de tokens, un volumen de datos que lo coloca en la misma liga que los modelos frontera de los laboratorios estadounidenses.

## El caché de tokens: donde el ahorro se multiplica

Más allá del precio base de $0.30 por millón de tokens de entrada, DeepSeek introduce un mecanismo de caché de tokens que cuesta apenas $0.03 por millón, es decir, un descuento del 90% sobre el precio estándar.

¿Por qué importa esto? Muchas aplicaciones de IA reutilizan contexto de forma constante: prompts de sistema, documentación de referencia, historiales de conversación. Cuando ese contenido ya está en caché, el costo se reduce drásticamente. Para productos como chatbots de atención al cliente, asistentes de código o herramientas de análisis de documentos —casos de uso comunes entre startups de la región—, el ahorro acumulado puede ser sustancial.

## Licencia MIT: código abierto sin letra pequeña

Un aspecto que diferencia a DeepSeek V4 de otros modelos "abiertos" del mercado es su licencia MIT, una de las más permisivas del ecosistema de software libre. Esto significa que las empresas pueden usar, modificar y comercializar productos construidos sobre el modelo sin restricciones significativas ni pagos de regalías.

La comparación es relevante: otros modelos etiquetados como abiertos incluyen cláusulas que limitan el uso comercial a partir de ciertos umbrales de usuarios o ingresos. La apuesta de DeepSeek por la apertura total es, además de una decisión técnica, una estrategia de adopción masiva.

## Quién está detrás: la anomalía de DeepSeek

La historia corporativa de DeepSeek es tan llamativa como su tecnología. La empresa nació como spin-off de High-Flyer, un hedge fund chino, y opera con un equipo de aproximadamente 300 empleados. El dato más contraintuitivo: ha recaudado $0 en financiamiento externo. Toda su operación está autofinanciada por High-Flyer.

Este modelo contrasta radicalmente con el de sus competidores. OpenAI y Anthropic han levantado decenas de miles de millones de dólares para entrenar sus modelos, mientras que DeepSeek compite en la misma categoría con una estructura de capital completamente distinta. Es un recordatorio de que en IA, la eficiencia de capital puede ser una ventaja competitiva tan importante como el tamaño del modelo.

## La competencia directa con GPT-4o y Claude Sonnet

DeepSeek posiciona V4 como competidor directo de GPT-4o y Claude Sonnet, los modelos de gama media-alta más utilizados en aplicaciones comerciales. La estrategia es clara: ofrecer un rendimiento comparable a una fracción del costo, con la ventaja adicional de que el modelo puede desplegarse en infraestructura propia gracias a su licencia abierta.

Para los laboratorios occidentales, la presión es doble. Por un lado, en precio: cada lanzamiento de DeepSeek históricamente ha provocado ajustes en las tarifas de API de sus competidores. Por otro, en el modelo de negocio: si un modelo open-source de calidad frontera está disponible gratuitamente, el valor diferencial de las APIs cerradas se erosiona.

## Qué significa esto para tu startup

Si estás construyendo productos con IA en Latinoamérica, DeepSeek V4 abre varias oportunidades concretas:

**1. Reducción inmediata de costos operativos.** A $0.30 por millón de tokens de entrada —y $0.03 con caché—, el costo de inferencia deja de ser un factor limitante para muchos casos de uso. Aplicaciones que antes eran inviables por unit economics ahora pueden tener márgenes saludables.

**2. Independencia de proveedores.** La licencia MIT permite desplegar el modelo en tu propia infraestructura o en proveedores de nube locales. Esto es especialmente relevante para startups que trabajan con datos sensibles (fintech, healthtech, legaltech) y necesitan cumplir con regulaciones de residencia de datos.

**3. Fine-tuning sin restricciones.** Puedes adaptar el modelo a tu vertical específico —español rioplatense, jerga legal mexicana, terminología médica colombiana— sin depender de las capacidades de personalización de un proveedor cerrado.

**4. Evaluación necesaria antes de migrar.** Ningún cambio de modelo debe hacerse sin benchmarks propios. Antes de migrar desde GPT-4o o Claude Sonnet, prueba V4 con tus casos de uso reales. El precio bajo solo vale si el rendimiento se sostiene en tu aplicación específica.

**5. Consideraciones geopolíticas.** El origen chino del modelo puede ser un factor a evaluar según tu mercado y tus clientes. Al ser open-source, puedes auditarlo y desplegarlo localmente, lo que mitiga parte de estas preocupaciones, pero es una conversación que conviene tener con clientes enterprise.

## Conclusión: la comoditización de la inteligencia

DeepSeek V4 confirma una tendencia que se viene consolidando: los modelos de lenguaje de alta calidad se están convirtiendo en un commodity. Cuando una empresa de 300 personas, sin financiamiento externo, puede lanzar un modelo que compite con los productos de laboratorios valuados en decenas de miles de millones de dólares —y regalarlo bajo licencia MIT—, las reglas del juego cambian.

Para las startups latinoamericanas, la pregunta ya no es si pueden costear la IA, sino qué construirán con ella. Cuando la inteligencia artificial cuesta centavos por millón de tokens, la ventaja competitiva se traslada del acceso a la tecnología hacia el conocimiento del cliente, la distribución y la ejecución. ¿Está tu startup preparada para competir en ese nuevo terreno?

## Fuentes

- [DeepSeek Blog: V4 Release](https://deepseek.com/blog/v4-release)
- [TechCrunch: DeepSeek V4](https://techcrunch.com/2026/03/deepseek-v4)