# Muse Glimmer 30B — news_seo_writing/news_perplexity_enrichment

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 7.52 | quality: 8.2
- latency_total: 14.299s | tokens_per_second: 152.1
- input_tokens: 489 | output_tokens: 2175
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, integrando bien la información adicional de Perplexity con el extracto original. Ofrece una estructura clara y organizada, con un estilo periodístico adecuado para SEO, aunque podría profundizar más en ciertos aspectos técnicos.

## Respuesta completa

DeepSeek publicó V4, su último modelo de IA de código abierto bajo licencia MIT. El anuncio confirma un costo de $0.30 por millón de tokens de entrada, una cifra que se suma a un conjunto de decisiones técnicas y de negocio que buscan posicionar al modelo como una alternativa accesible para desarrolladores y equipos de producto.

## DeepSeek V4 llega como modelo abierto bajo licencia MIT

La publicación de V4 se enmarca en la estrategia de DeepSeek de mantener sus modelos disponibles bajo licencia MIT. Esa licencia permite uso comercial, modificación y redistribución sin las restricciones típicas de modelos con licencias más cerradas. 

El precio anunciado para la entrada es de $0.30 por millón de tokens. A ello se suma un costo específico para el caché de tokens de $0.03 por millón, lo que representa un descuento del 90% respecto al precio base de entrada. La diferenciación de precio entre tokens de entrada y tokens cacheados apunta a uso intensivo en aplicaciones con contexto repetido, como agentes y sistemas de RAG.

## Arquitectura y entrenamiento: eficiencia con MoE

V4 utiliza una arquitectura Mixture of Experts, MoE, con 236 mil millones de parámetros totales y 21 mil millones activos por token. El diseño MoE permite mantener una capacidad total elevada mientras se limita el cómputo por inferencia a un subconjunto de expertos.

El modelo fue entrenado con 15 billones de tokens. La combinación de un conteo de entrenamiento elevado con una activación parcial de parámetros es la base que la empresa presenta para equilibrar rendimiento y costo operativo.

## Precio y modelo de uso: $0.30 por millón de tokens de entrada

El costo de $0.30 por millón de tokens de entrada se comunica como referencia directa para desarrolladores que comparan proveedores. El precio del caché de tokens a $0.03 por millón introduce una economía distinta para cargas de trabajo con ventanas de contexto largas y reutilización.

Esa estructura de precios es relevante para equipos que calculan costo por consulta en producción. El descuento aplicado al caché reduce el gasto en escenarios donde el mismo contexto se mantiene entre llamadas, un patrón común en asistentes con memoria o en pipelines de análisis documental.

## Origen de la empresa: Hangzhou y High-Flyer

DeepSeek está ubicada en Hangzhou, China, y opera como spin-off del fondo de inversión cuantitativa High-Flyer. La empresa cuenta con aproximadamente 300 empleados.

Un dato destacado en su trayectoria es que no ha recaudado funding externo. La operación está autofinanciada por High-Flyer, lo que condiciona su modelo de desarrollo y su capacidad para mantener licencias abiertas sin presión de retorno de inversión externa en el corto plazo.

## Competencia directa con GPT-4o y Claude Sonnet

En el posicionamiento público, V4 se presenta en competencia directa con GPT-4o y Claude Sonnet. La comparación se centra en la combinación de apertura de código, licencia MIT y precio por token frente a alternativas comerciales con licencias restrictivas.

La presencia de un modelo abierto con arquitectura MoE de gran escala y precios bajos por entrada y caché modifica la ecuación de decisión para equipos que evalúan construir sobre infraestructura propia o servicios gestionados.

## Qué significa esto para tu startup

Para una startup latinoamericana el anuncio implica tres variables concretas a revisar.

Primero, costo predecible de inferencia. $0.30 por millón de tokens de entrada y $0.03 por millón para caché permiten modelar gastos de producto con mayor claridad que en modelos donde el precio varía según tier o uso. Eso facilita presupuestos de MVP y pruebas de mercado sin comprometer la licencia.

Segundo, control sobre el modelo. La licencia MIT y el código abierto permiten auditar, modificar y desplegar localmente. Para startups que manejan datos sensibles o que buscan evitar dependencias de proveedores únicos, esa opción reduce riesgo operativo y de cumplimiento.

Tercero, recursos de equipo. DeepSeek opera con ~300 empleados y sin funding externo. Eso sugiere un enfoque de desarrollo enfocado en eficiencia de capital y reutilización de infraestructura de investigación. Para equipos pequeños, la lección es priorizar arquitecturas que reduzcan costo por inferencia, como MoE con pocos parámetros activos, y aprovechar caché para contextos estables.

También es necesario evaluar soporte, documentación y comunidad en español, disponibilidad de endpoints en la región y latencia. El precio por token es una parte del costo total; la ingeniería para integrar, monitorear y mantener el modelo también cuenta.

## Conclusión

DeepSeek V4 consolida una propuesta basada en apertura, precio bajo por entrada y caché, y una arquitectura MoE de 236B parámetros totales con 21B activos entrenados con 15T tokens. El origen en Hangzhou, el vínculo con High-Flyer, el tamaño de equipo de ~300 personas y la ausencia de funding externo contextualizan cómo se sostiene ese modelo.

Para el ecosistema emprendedor la pregunta no es si un modelo abierto es mejor en términos absolutos, sino qué trade-offs acepta cada startup entre costo, control, soporte y velocidad de implementación. Revisar con datos propios el comportamiento de V4 en casos de uso reales sigue siendo el paso necesario antes de cualquier decisión de arquitectura.

### Fuentes
https://deepseek.com/blog/v4-release
https://techcrunch.com/2026/03/deepseek-v4