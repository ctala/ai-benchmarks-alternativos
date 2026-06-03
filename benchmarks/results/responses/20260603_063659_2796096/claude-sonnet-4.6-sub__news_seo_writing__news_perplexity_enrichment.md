# Claude Sonnet 4.6 (suscripción) — news_seo_writing/news_perplexity_enrichment

- model_id: `claude-sonnet-4-6`
- success: True  | final: 7.24 | quality: 9.8
- latency_total: 45.832s | tokens_per_second: 47.1
- input_tokens: 3 | output_tokens: 2159
- judge_score: 5 | justificación: La respuesta es precisa, relevante y ofrece una buena profundidad con información detallada sobre la arquitectura MoE y el esquema de precios, todo presentado de manera clara y estructurada, lo que la hace altamente útil para un emprendedor.

## Respuesta completa

## DeepSeek V4: el modelo de código abierto con 236B parámetros que cambia el cálculo de costos en AI

DeepSeek acaba de lanzar V4, su modelo más avanzado hasta la fecha, bajo licencia MIT. El lanzamiento no pasó desapercibido: con 236 mil millones de parámetros totales, un precio de entrada de $0.30 por millón de tokens y un enfoque de financiamiento completamente atípico para la industria, este modelo obliga a repensar varias suposiciones que el ecosistema AI daba por sentadas.

Lo que hace particular a DeepSeek V4 no es solo el tamaño, sino la arquitectura que lo hace funcionar de forma eficiente.

---

## Arquitectura MoE: 236B parámetros, pero solo 21B activos a la vez

DeepSeek V4 utiliza una arquitectura Mixture of Experts (MoE), un diseño que permite tener una red neuronal muy grande en papel, pero activar solo una fracción de ella en cada inferencia. En este caso, de los 236 mil millones de parámetros totales, solo 21 mil millones se activan al procesar cada consulta.

Esto tiene implicaciones prácticas importantes. Un modelo MoE bien diseñado puede ofrecer capacidades comparables a un modelo denso mucho más grande, pero con un costo computacional significativamente menor por inferencia. Es la razón por la que el precio final puede ser competitivo: el proveedor no está corriendo 236B parámetros completos en cada llamada.

El modelo fue entrenado con 15 billones de tokens, un volumen que lo sitúa en la misma liga que los grandes modelos de frontera actuales. Para referencia, modelos como LLaMA 3 de Meta fueron entrenados con cifras similares o menores.

---

## Precio real de uso: $0.30/M de entrada, con un detalle importante

El precio estándar de $0.30 por millón de tokens de entrada ya es competitivo frente a alternativas propietarias. Pero hay un detalle que merece atención separada: el cache de tokens cuesta apenas $0.03 por millón de tokens, un 90% menos que el precio base.

Para aplicaciones que reutilizan contexto largo —como agentes que trabajan con documentos, pipelines de N8N con prompts de sistema extensos, o sistemas RAG que reinsertan el mismo contexto repetidamente— este descuento no es menor. En la práctica, una arquitectura bien diseñada que maximice el cache puede reducir el costo real por llamada a una fracción del precio nominal.

Este esquema de pricing con cache agresivo es una señal de hacia dónde está yendo la industria: los proveedores están incentivando arquitecturas stateful y el reuso de contexto como forma de diferenciarse en costo.

---

## Con qué compite y dónde se para

DeepSeek posiciona V4 como competidor directo de GPT-4o y Claude Sonnet 3.5. Ambos son modelos de referencia en tareas de razonamiento, generación de código y comprensión de documentos largos.

La licencia MIT es relevante aquí. A diferencia de modelos bajo licencias restrictivas, MIT permite uso comercial sin restricciones, modificación, redistribución y despliegue en infraestructura propia. Para empresas que necesitan control sobre sus datos o que operan en sectores regulados, esta libertad tiene valor concreto que no aparece en las comparaciones de benchmark.

El modelo ya está disponible vía OpenRouter y otros proveedores de acceso a APIs, lo que significa que equipos técnicos pueden comenzar a evaluarlo sin necesidad de infraestructura propia.

---

## La empresa detrás: sin funding externo, desde un hedge fund chino

DeepSeek es una spin-off de High-Flyer, un hedge fund cuantitativo con sede en Hangzhou, China. La empresa tiene aproximadamente 300 empleados y, según información disponible, no ha recaudado financiamiento externo: opera con capital propio del fondo.

Este modelo de financiamiento es inusual en el ecosistema AI, donde la norma han sido rondas de cientos de millones o miles de millones de dólares. OpenAI lleva recaudados más de $13 mil millones. Anthropic superó los $7 mil millones. Mistral, comparativamente pequeño, levantó más de $1 mil millones en rondas sucesivas.

DeepSeek ha construido modelos competitivos con una fracción de esos recursos y sin depender de capital de riesgo externo. Eso tiene implicaciones sobre incentivos: la empresa no tiene que responder a inversores institucionales con expectativas de retorno en plazos definidos, lo que le da más libertad para tomar decisiones técnicas de largo plazo.

La elección de publicar bajo MIT —en lugar de licencias más restrictivas o modelos completamente propietarios— también encaja con esa lógica: priorizar adopción y reputación técnica sobre monetización directa del modelo.

---

## Qué significa esto para tu startup

Si estás construyendo productos sobre APIs de lenguaje, DeepSeek V4 agrega una opción concreta al menú que vale evaluar en tres escenarios específicos:

**Costo a escala**: Si tu aplicación procesa volúmenes altos de texto con contexto reutilizable, el pricing de cache a $0.03/M puede cambiar materialmente tu estructura de costos. Calcular el porcentaje de tokens que caen en cache en tu caso de uso específico antes de comparar precios nominales.

**Control y cumplimiento**: La licencia MIT permite despliegue on-premise o en VPC privada. Para aplicaciones que manejan datos sensibles —documentos legales, información médica, datos financieros— tener la opción de correr el modelo en infraestructura propia sin restricciones de licencia es un diferenciador real.

**Evaluación técnica honesta**: El benchmark en papel no reemplaza la evaluación en tu caso de uso. Un modelo con 21B parámetros activos puede comportarse diferente a uno denso de tamaño similar en tareas muy específicas. Vale correr DeepSeek V4 contra tu conjunto de pruebas real antes de migrar workloads de producción.

Lo que no tiene sentido es ignorarlo por defecto. En un mercado donde la diferencia de precios entre modelos puede ser de 10x o más para capacidades comparables, cada nuevo lanzamiento competitivo es una oportunidad de optimización que vale al menos media hora de evaluación.

---

## Conclusión

DeepSeek V4 es un recordatorio de que el desarrollo de modelos de frontera ya no es exclusivo de las grandes empresas tecnológicas estadounidenses con acceso ilimitado a capital. Una empresa de 300 personas, financiada desde un hedge fund, sin rondas externas, publicó un modelo bajo MIT que compite directamente con los productos más avanzados de OpenAI y Anthropic.

La pregunta que queda abierta es cuánto de este patrón es replicable. ¿Es DeepSeek una anomalía o el inicio de una curva de acceso más democrática al desarrollo de modelos de frontera? La respuesta va a depender de cómo evolucionen los costos de cómputo, el acceso a datos de entrenamiento de calidad y las restricciones regulatorias que varios países están comenzando a considerar.

Por ahora, lo concreto es que los equipos técnicos tienen una opción más —competitiva en precio, abierta en licencia, con buenas credenciales técnicas— para construir sobre ella.

---

**Fuentes**
- DeepSeek Blog: https://deepseek.com/blog/v4-release
- TechCrunch: https://techcrunch.com/2026/03/deepseek-v4