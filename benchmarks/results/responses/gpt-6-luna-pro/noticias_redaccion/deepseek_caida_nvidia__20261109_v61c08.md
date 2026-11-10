# GPT-6 Luna Pro — noticias_redaccion/deepseek_caida_nvidia

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 8.82 | quality: 10.0
- latency_total: 22.752s | tokens_per_second: 198.4
- input_tokens: 6491 | output_tokens: 4514

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

# DeepSeek sacude el debate sobre el costo de desarrollar modelos de IA

## Una caída histórica para Nvidia

Las acciones de Nvidia cayeron cerca de un 17 % el lunes, después de que la startup china DeepSeek publicara un modelo de inteligencia artificial que, según la compañía, igualaba el rendimiento de algunos de los principales sistemas estadounidenses y había costado una fracción de lo que se suele asociar con su entrenamiento.

La caída borró cerca de 600.000 millones de dólares del valor de mercado de Nvidia en una sola sesión, una de las mayores pérdidas diarias en la historia del mercado bursátil estadounidense. El movimiento reflejó una preocupación concreta entre los inversores: si es posible entrenar modelos avanzados con menos chips, podría reducirse la demanda de los procesadores más costosos de Nvidia.

Pero esa interpretación no es la única. Algunos analistas sostienen que los modelos más baratos pueden impulsar un mayor uso de la inteligencia artificial y, con ello, aumentar la necesidad total de capacidad de cómputo. Por ahora, el episodio pone en primer plano una pregunta que también interesa a las empresas usuarias de IA: cuánto cuesta realmente desarrollar estos sistemas y qué parte de ese gasto puede reducirse.

## Qué dijo DeepSeek sobre sus costos

DeepSeek tiene su sede en Hangzhou y está respaldada por un fondo de cobertura chino. En un informe técnico, la empresa indicó que la etapa final de entrenamiento de uno de sus modelos costó alrededor de 5,6 millones de dólares en tiempo de cómputo y utilizó 2.048 chips Nvidia H800. Estos procesadores son una versión diseñada para cumplir con las restricciones estadounidenses a la exportación.

La cifra llamó la atención porque desafía la idea extendida de que desarrollar modelos de frontera exige gastar miles de millones de dólares en chips. Sin embargo, no representa el costo total de crear el modelo. Expertos señalaron que el cálculo cubre únicamente la ejecución final del entrenamiento y deja fuera la investigación, los experimentos anteriores y el costo del propio hardware.

Por eso, los 5,6 millones de dólares no deben leerse como una medida completa de lo que costó construir el sistema. Tampoco permiten, por sí solos, comparar de manera directa el gasto total de DeepSeek con el de otros laboratorios. Lo que sí muestran es que una parte específica del proceso —la ejecución final de entrenamiento, según la empresa— habría requerido menos recursos de los que muchos esperaban.

## La ingeniería detrás del resultado

En su documentación técnica, DeepSeek describió varias decisiones de ingeniería que, según explicó, ayudaron a reducir costos. Entre ellas figura una arquitectura que activa solo una parte del modelo para cada solicitud, en lugar de activar todos sus componentes cada vez. La empresa también señaló métodos para hacer más eficiente el entrenamiento con los chips disponibles.

Investigadores de otros países destacaron el nivel de detalle de los documentos y dijeron que algunas de esas ideas podrían ser adoptadas por otros laboratorios. El interés, por tanto, no se limita a la cifra de gasto anunciada: también alcanza a las técnicas que podrían ayudar a otros equipos a aprovechar mejor su infraestructura.

DeepSeek fue fundada por Liang Wenfeng, quien también cofundó el fondo cuantitativo que financia la compañía. Según personas familiarizadas con la empresa, contrató a muchos investigadores jóvenes de universidades chinas y dio prioridad a la investigación, en vez de concentrarse en lanzar productos comerciales con rapidez.

## Modelos abiertos y acceso para las empresas

El modelo de razonamiento de DeepSeek se publicó con pesos abiertos. Esto significa que otras compañías pueden descargarlo y ejecutarlo en su propia infraestructura. Para las empresas, esa característica abre una alternativa a depender únicamente de modelos ofrecidos por proveedores externos, aunque la fuente no plantea que sea la opción adecuada para todos los casos.

En cuestión de días, la aplicación de asistente de DeepSeek llegó a los primeros puestos de las listas de descargas en varios países. La rapidez con la que ganó atención también muestra que el impacto del lanzamiento no quedó limitado a los investigadores o a los mercados financieros.

Para una pyme que utiliza inteligencia artificial, la lectura práctica es más acotada y, a la vez, relevante: la competencia entre proveedores está presionando los precios a la baja y los modelos abiertos empiezan a ser una opción real para las empresas que quieren controlar costos o mantener sus datos dentro de su propia infraestructura.

Esto no significa que toda empresa deba adoptar un modelo abierto ni que el costo de entrenamiento anunciado equivalga al costo de usarlo. La cifra de DeepSeek se refiere a una etapa concreta del desarrollo. Pero el lanzamiento amplía las alternativas que las empresas pueden considerar y suma presión para que los proveedores compitan también en precio y eficiencia.

## El debate sobre los controles de exportación

El caso reabrió la discusión sobre las restricciones estadounidenses a la venta de los chips más avanzados a China. Estados Unidos ha limitado esas exportaciones con el argumento de que los procesadores podrían tener usos militares.

Las reacciones al resultado de DeepSeek fueron distintas. Algunos comentaristas dijeron que las restricciones estaban empujando a las empresas chinas a desarrollar métodos más eficientes. Otros interpretaron el avance como una señal de que los controles deberían endurecerse aún más.

También hubo respuestas públicas de líderes tecnológicos estadounidenses: algunos elogiaron el trabajo, mientras que otros cuestionaron si DeepSeek había declarado todos los recursos que utilizó. OpenAI, por su parte, dijo que estaba revisando si sus modelos habían sido usados de forma impropia para entrenar sistemas competidores. La fuente no ofrece una conclusión sobre esa revisión.

## Qué puede cambiar para las pymes

La caída de Nvidia no demuestra que la demanda de chips vaya a disminuir. Expone dos posibilidades contrapuestas: que una mayor eficiencia reduzca la necesidad de procesadores costosos, o que los modelos más baratos se utilicen más y terminen elevando la demanda total de cómputo.

Para quienes automatizan procesos en una pyme, el cambio más inmediato no es una promesa de que la IA vaya a costar una cantidad determinada. Es que se amplía la conversación sobre cómo se construyen los modelos, qué recursos requieren y qué alternativas existen para usarlos. DeepSeek puso en cuestión la idea de que solo se puede competir en IA con inversiones enormes, aunque su cifra de entrenamiento tiene límites claros.

Conviene separar tres asuntos: el costo declarado de la ejecución final, el gasto total de desarrollar un modelo y el costo de utilizarlo en una empresa. La información publicada por DeepSeek se refiere al primero. Aun con esa precisión, la aparición de modelos abiertos y la competencia entre proveedores pueden dar a las pymes más opciones para buscar costos menores o mayor control sobre sus datos.