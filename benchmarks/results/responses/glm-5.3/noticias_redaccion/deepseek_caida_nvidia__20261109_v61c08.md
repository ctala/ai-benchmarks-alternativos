# GLM 5.3 — noticias_redaccion/deepseek_caida_nvidia

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.07 | quality: 10.0
- latency_total: 150.693s | tokens_per_second: 91.8
- input_tokens: 681 | output_tokens: 13830

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor de contenido para un founder hispanohablante que publica noticias y análisis para emprendedores de América Latina y España. Escribes en español neutro, claro y directo, con subtítulos en Markdown (##).

**user:**

Es para el blog de una agencia de automatización que explica a pymes qué pasa con los modelos de IA.

Escribe la nota en español neutro, de 900 a 1.300 palabras, solo con datos de la fuente.

FUENTE:
Shares of chipmaker Nvidia fell about 17% on Monday after Chinese startup DeepSeek released an artificial intelligence model that matched the performance of leading American systems while, according to the company, costing a fraction as much to train. The drop erased close to $600 billion of Nvidia's market value in a single session, one of the largest one-day losses in the history of the U.S. stock market.

DeepSeek, based in Hangzhou, is backed by a Chinese hedge fund. The company published a technical report saying that the final training run of one of its models cost about $5.6 million in computing time and used 2,048 Nvidia H800 chips, a version of the company's processors designed to comply with American export restrictions.

The company was founded by Liang Wenfeng, who also co-founded the quantitative hedge fund that finances it. According to people familiar with the company, it hired many young researchers from Chinese universities and focused on research rather than on building commercial products quickly.

In its technical documentation, DeepSeek described several engineering techniques that helped it reduce costs, including an architecture that activates only part of the model for each request and methods that make training more efficient on the chips it had available. Researchers in other countries said the papers were detailed and that some of the ideas could be adopted by other labs.

The release also reopened the debate over American export controls. The United States has limited the sale of its most advanced chips to China, arguing that they could be used for military purposes. Some commentators said DeepSeek's results showed that the restrictions were pushing Chinese companies to become more efficient; others said they proved that the controls needed to be tightened further.

Several American technology leaders reacted publicly to the news, some praising the work and others questioning whether the company had disclosed all the resources it used. OpenAI said it was reviewing whether its models had been used improperly to train competing systems.

Experts quickly pointed out that the figure only covered the final training run and excluded research, earlier experiments and the cost of the hardware itself. Even so, the number challenged the widespread belief that building frontier models requires billions of dollars in chips.

DeepSeek's reasoning model was released with open weights, which means any company can download it and run it on its own infrastructure. Within days, the company's assistant app climbed to the top of download charts in several countries.

Investors worried that if powerful models can be trained with fewer chips, demand for Nvidia's most expensive processors could slow. Other analysts argued the opposite: cheaper models tend to increase total usage, which in the end requires more computing power.

For small companies that use AI, the episode had a practical reading. Competition among model providers was pushing prices down, and open models were becoming a real option for businesses that want to control costs or keep their data in-house.


## Respuesta completa

# DeepSeek sacudió a Nvidia y al mercado de la IA: qué significa para tu pyme

Las acciones del fabricante de chips Nvidia cayeron cerca del **17%** el lunes, después de que la startup china DeepSeek lanzara un modelo de inteligencia artificial que iguala el rendimiento de los sistemas líderes de Estados Unidos y que, según la empresa, costó una fracción de lo que cuesta entrenar a sus rivales. El desplome borró casi **600.000 millones de dólares** del valor de mercado de Nvidia en una sola sesión: una de las mayores pérdidas en un solo día en la historia de la bolsa estadounidense.

Detrás del susto de los inversores hay una historia que importa mucho más allá de Wall Street. Para las pymes que ya usan inteligencia artificial —o que están evaluando adoptarla—, este episodio movió el mapa de precios y de opciones disponibles. Esta es una guía de lo que pasó y de cómo leerlo.

## ¿Quién es DeepSeek?

DeepSeek es una empresa con base en Hangzhou, China, respaldada por un fondo de cobertura (hedge fund) de ese país. Su fundador es Liang Wenfeng, quien además cofundó el fondo cuantitativo que financia a la compañía.

Según personas familiarizadas con la empresa, DeepSeek contrató a muchos investigadores jóvenes provenientes de universidades chinas y se concentró en la investigación, más que en construir productos comerciales rápidamente. Un perfil poco habitual: investigación primero, productos después.

## El número que sorprendió al mundo: 5,6 millones de dólares

En un informe técnico, DeepSeek afirmó que la ronda final de entrenamiento de uno de sus modelos costó unos **5,6 millones de dólares** en tiempo de cómputo, con **2.048 chips Nvidia H800**: una versión de los procesadores de la empresa diseñada para cumplir con las restricciones de exportación de Estados Unidos.

Esa cifra desafió una creencia muy extendida en la industria: que construir modelos de frontera —los más avanzados— requiere miles de millones de dólares en chips. Ese supuesto quedó, al menos por ahora, en tela de juicio.

## Cómo lograron reducir los costos

En su documentación técnica, DeepSeek describió varias técnicas de ingeniería que le permitieron abaratar el entrenamiento:

- **Una arquitectura que activa solo una parte del modelo para cada consulta**, en lugar de usar todo el sistema cada vez que alguien lo utiliza.
- **Métodos que hacen el entrenamiento más eficiente** con los chips que tenía disponibles.

Investigadores de otros países describieron los documentos como detallados y señalaron que algunas de esas ideas podrían ser adoptadas por otros laboratorios. Es decir, no parece un truco aislado: es conocimiento que puede replicarse en toda la industria.

## El asterisco: qué incluye (y qué no) esa cifra

Los expertos señalaron rápido un detalle clave: los 5,6 millones de dólares solo cubren la ronda final de entrenamiento. Quedan fuera la investigación previa, los experimentos anteriores y el costo del propio hardware.

La inversión total fue, por lo tanto, mayor. Aun así, el número fue suficiente para cuestionar la idea de que la IA de vanguardia exige presupuestos multimillonarios en chips.

## El debate político que reabrió el caso

El lanzamiento también reabrió la discusión sobre los controles de exportación de Estados Unidos. Washington ha limitado la venta de sus chips más avanzados a China, con el argumento de que podrían usarse con fines militares.

Ante los resultados de DeepSeek aparecieron dos lecturas opuestas:

- Algunos comentaristas dijeron que las restricciones estaban empujando a las empresas chinas a volverse más eficientes.
- Otros sostuvieron que el caso probaba que los controles debían endurecerse aún más.

## Las reacciones de los líderes tecnológicos

Varios líderes tecnológicos de Estados Unidos reaccionaron públicamente: algunos elogiaron el trabajo de DeepSeek; otros cuestionaron si la empresa reveló todos los recursos que utilizó. OpenAI, por su parte, dijo que está revisando si sus modelos fueron usados de manera indebida para entrenar sistemas competidores.

## Qué significa que el modelo sea de "pesos abiertos"

El modelo de razonamiento de DeepSeek se publicó con **pesos abiertos** (*open weights*). En términos prácticos, eso significa que cualquier empresa puede descargarlo y ejecutarlo en su propia infraestructura, sin depender de un proveedor externo.

El efecto fue inmediato: en cuestión de días, la aplicación asistente de DeepSeek escaló al primer lugar de las listas de descargas en varios países.

## ¿Es el fin del negocio de Nvidia?

Los inversores se preocuparon por una lógica sencilla: si es posible entrenar modelos potentes con menos chips, la demanda por los procesadores más caros de Nvidia podría frenarse.

Otros analistas argumentaron exactamente lo contrario: los modelos más baratos tienden a aumentar el uso total de la IA, y ese mayor uso termina requiriendo más poder de cómputo, no menos.

¿Quién tiene razón? Es pronto para saberlo. Lo que queda claro es que el debate sobre el impacto real de DeepSeek recién comienza.

## La lectura práctica para las pymes

Más allá del ruido bursátil, el episodio deja dos lecciones concretas para las pequeñas y medianas empresas:

1. **La competencia entre proveedores de modelos está empujando los precios hacia abajo.** Buena noticia para cualquier negocio que hoy paga por servicios de IA.
2. **Los modelos abiertos se convierten en una opción real** para las empresas que quieren controlar sus costos o mantener sus datos dentro de su propia infraestructura.

Para una pyme, esto se traduce en algo muy concreto: el costo de adoptar inteligencia artificial tiende a bajar y las alternativas se multiplican. Ya no hay una única vía para integrar IA en los procesos del negocio, y la posibilidad de mantener los datos "en casa" gana terreno.

## En resumen

DeepSeek demostró que es posible entrenar un modelo competitivo con los sistemas líderes gastando mucho menos de lo que se creía necesario. El resultado: una de las mayores pérdidas en un solo día en la historia de la bolsa de Estados Unidos para Nvidia, un debate geopolítico reabierto y los pesos abiertos en el centro de la conversación.

Para las pymes, la conclusión es práctica: los precios de la IA bajan y las opciones de implementación crecen. Si tu empresa estaba esperando una señal para avanzar con IA y automatización, este episodio ofrece una: cada vez es más barato empezar.