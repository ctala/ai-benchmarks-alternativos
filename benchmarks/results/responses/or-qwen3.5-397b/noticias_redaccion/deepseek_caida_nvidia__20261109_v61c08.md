# Qwen 3.5 397B — noticias_redaccion/deepseek_caida_nvidia

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 8.35 | quality: 10.0
- latency_total: 66.132s | tokens_per_second: 61.0
- input_tokens: 703 | output_tokens: 4032

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

## El nuevo panorama de la inteligencia artificial para emprendedores

La industria tecnológica ha sido testigo de un movimiento significativo que está redefiniendo las expectativas sobre el costo y la accesibilidad de la inteligencia artificial. Para los emprendedores y dueños de pequeñas y medianas empresas en América Latina y España, entender este cambio es crucial, ya que impacta directamente en los costos de operación y las estrategias de automatización. Recientemente, las acciones del fabricante de chips Nvidia cayeron aproximadamente un 17% en un solo lunes. Este descenso eliminó cerca de 600.000 millones de dólares del valor de mercado de la empresa en una única sesión, marcando una de las mayores pérdidas de un día en la historia del mercado de valores de Estados Unidos.

La razón detrás de esta volatilidad no fue un fallo en los productos de Nvidia, sino el anuncio de una startup china llamada DeepSeek. Esta compañía lanzó un modelo de inteligencia artificial que igualó el rendimiento de los sistemas líderes estadounidenses. Según la empresa, lograr esto costó una fracción de lo que habitualmente se requiere para entrenar sistemas de este calibre. Este evento ha abierto un debate intenso sobre el futuro de la infraestructura necesaria para la IA y cómo las empresas pueden aprovechar estos cambios.

## El colapso bursátil de Nvidia y el surgimiento de DeepSeek

La reacción del mercado fue inmediata ante la noticia de que es posible construir modelos de frontera sin las inversiones masivas que se creían necesarias. DeepSeek, con sede en Hangzhou, está respaldada por un fondo de cobertura chino. La compañía publicó un informe técnico detallando que la ejecución final del entrenamiento de uno de sus modelos costó около 5,6 millones de dólares en tiempo de computación. Para lograr esto, utilizaron 2.048 chips Nvidia H800. Es importante destacar que esta es una versión de los procesadores de la compañía diseñada específicamente para cumplir con las restricciones de exportación estadounidenses.

La empresa fue fundada por Liang Wenfeng, quien también cofundó el fondo de cobertura cuantitativo que la financia. Según personas familiarizadas con la compañía, su estrategia se diferenció de la competencia inmediata. DeepSeek contrató a muchos investigadores jóvenes de universidades chinas y se centró en la investigación en lugar de construir productos comerciales rápidamente. Este enfoque en la innovación técnica sobre la comercialización acelerada parece haber dado frutos, desafiando la valoración actual de los proveedores de hardware más costosos del mercado.

## La ingeniería detrás de la eficiencia en costos

Para los responsables técnicos en las pymes, la pregunta clave es cómo se lograron estos resultados con menos recursos. En su documentación técnica, DeepSeek describió varias técnicas de ingeniería que ayudaron a reducir los costos significativamente. Una de ellas incluye una arquitectura que activa solo una parte del modelo para cada solicitud, en lugar de utilizar la totalidad de la red neuronal para cada interacción. Además, implementaron métodos que hacen que el entrenamiento sea más eficiente en los chips que tenían disponibles, optimizando el hardware existente en lugar de depender de la fuerza bruta computacional.

Investigadores en otros países revisaron los documentos y señalaron que los papers eran detallados. Asimismo, indicaron que algunas de las ideas presentadas podrían ser adoptadas por otros laboratorios, lo que sugiere que esta eficiencia podría replicarse en la industria. Sin embargo, expertos señalaron rápidamente que la cifra de 5,6 millones de dólares solo cubría la ejecución final del entrenamiento. Este número excluía la investigación previa, los experimentos anteriores y el costo del hardware en sí. A pesar de esta salvedad, el número desafió la creencia generalizada de que construir modelos de frontera requiere miles de millones de dólares en chips, lo cual cambia la barrera de entrada para el desarrollo de IA.

## El debate geopolítico y la reacción de la industria

El lanzamiento de este modelo también reabrió el debate sobre los controles de exportación estadounidenses. Estados Unidos ha limitado la venta de sus chips más avanzados a China, argumentando que podrían utilizarse con fines militares. Algunos comentaristas dijeron que los resultados de DeepSeek mostraron que las restricciones estaban empujando a las empresas chinas a volverse más eficientes con los recursos disponibles. Otros argumentaron que esto probaba que los controles necesitaban endurecerse aún más para mantener la ventaja tecnológica.

Varios líderes tecnológicos estadounidenses reaccionaron públicamente a la noticia. Algunos elogiaron el trabajo técnico, mientras que otros cuestionaron si la compañía había divulgado todos los recursos que utilizó para lograr tal eficiencia. OpenAI, por su parte, declaró que estaba revisando si sus modelos habían sido utilizados indebidamente para entrenar sistemas competidores. Esta tensión refleja la competencia feroz que existe actualmente entre los proveedores de modelos, lo cual beneficia indirectamente a los usuarios finales al impulsar la innovación y la transparencia técnica.

## Implicaciones prácticas para las pymes y la automatización

Para las pequeñas empresas que utilizan inteligencia artificial, este episodio tiene una lectura práctica directa que no debe ignorarse. La competencia entre los proveedores de modelos está empujando los precios a la baja. Además, los modelos abiertos se están convirtiendo en una opción real para las empresas que quieren controlar costos o mantener sus datos dentro de su propia infraestructura. El modelo de razonamiento de DeepSeek se lanzó con pesos abiertos, lo que significa que cualquier empresa puede descargarlo y ejecutarlo en su propia infraestructura sin depender exclusivamente de APIs externas.

La adopción fue rápida. En pocos días, la aplicación asistente de la compañía escaló a la parte superior de las listas de descargas en varios países. Esto demuestra una demanda latente de alternativas accesibles y potentes. En el ámbito de la inversión, existía preocupación de que si los modelos potentes pueden entrenarse con menos chips, la demanda de los procesadores más caros de Nvidia podría ralentizarse. No obstante, otros analistas argumentaron lo contrario: los modelos más baratos tienden a aumentar el uso total, lo que al final requiere más potencia computacional agregada.

Para una agencia de automatización o una pymes, esto se traduce en más opciones. La posibilidad de ejecutar modelos potentes localmente permite mantener la privacidad de los datos sensibles de los clientes, un factor crítico en sectores regulados. Además, la reducción en los costos de entrenamiento y ejecución sugiere que las herramientas de automatización basadas en IA serán más económicas de implementar en el futuro cercano. La eficiencia demostrada por DeepSeek indica que la barrera para implementar inteligencia artificial de alto nivel está disminuyendo, permitiendo que empresas con presupuestos más ajustados puedan competir con organizaciones más grandes que anteriormente tenían el monopolio de esta tecnología.

En conclusión, el mercado está entrando en una fase donde la eficiencia del software comienza a pesar tanto como la potencia del hardware. Para el emprendedor hispanohablante, esto significa que el momento de integrar automatizaciones inteligentes es ahora, aprovechando una competencia que favorece la reducción de costos y el acceso a tecnología de punta sin necesidad de inversiones multimillonarias en infraestructura propia.