# Qwen 3.5 35B — noticias_redaccion/deepseek_caida_nvidia

- model_id: `qwen/qwen3.5-35b-a3b`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 21.943s | tokens_per_second: 167.8
- input_tokens: 703 | output_tokens: 3682

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

## El terremoto de la IA: Lo que DeepSeek revela sobre costos y el futuro para las pymes

Para cualquier fundador o emprendedor que sigue el panorama tecnológico, una noticia reciente ha sacudido los cimientos del sector de la inteligencia artificial. Shares de la fabricante de chips Nvidia cayeron cerca de un 17% el lunes tras la liberación de un modelo de inteligencia artificial por parte de la startup china DeepSeek. Este evento no solo generó volatilidad financiera inmediata, sino que desafió creencias fundamentales sobre cuánto cuesta desarrollar tecnología de vanguardia. Para las pequeñas y medianas empresas (pymes) de América Latina y España, entender qué sucedió es crucial para anticipar cómo evolucionarán sus propios presupuestos y estrategias de automatización.

La magnitud del movimiento bursátil fue histórica. La caída en el valor de mercado de Nvidia borró cerca de $600 mil millones de dólares en una sola sesión, lo que representa una de las pérdidas más grandes en un solo día en la historia del mercado de valores de EE. UU. Este desplome no ocurrió por un error operativo de Nvidia, sino porque DeepSeek lanzó un sistema que igualaba el rendimiento de los sistemas líderes estadounidenses, aunque, según la propia compañía, costaba una fracción como mucho entrenarlo.

## Cómo DeepSeek redujo los costos drásticamente

Para comprender la disrupción, debemos analizar los datos técnicos publicados por DeepSeek. Con sede en Hangzhou y respaldada por un fondo de cobertura chino, la compañía publicó un informe técnico que detalla sus logros. Según este documento, la ejecución final de entrenamiento de uno de sus modelos costó aproximadamente $5,6 millones en tiempo de computación. Esta cifra utiliza 2,048 chips Nvidia H800, una versión de los procesadores diseñada específicamente para cumplir con las restricciones de exportación americanas.

La estrategia detrás de esta eficiencia no fue solo suerte, sino ingeniería deliberada. El fundador de DeepSeek, Liang Wenfeng, quien también cofundó el fondo de cobertura cuantitativo que financia la empresa, orientó la compañía hacia la investigación en lugar de construir productos comerciales rápidamente. Para lograrlo, la empresa contrató a muchos jóvenes investigadores de universidades chinas. En su documentación técnica, DeepSeek describió varias técnicas de ingeniería que ayudaron a reducir costos, incluyendo una arquitectura que activa solo una parte del modelo para cada solicitud y métodos que hacen que el entrenamiento sea más eficiente en los chips de que disponían.

Investigadores en otros países evaluaron estos documentos y señalaron que los papeles eran detallados y que algunas de las ideas podrían ser adoptadas por otros laboratorios. Esto tiene implicaciones directas: si estas técnicas se generalizan, la barrera de entrada para crear modelos potentes disminuye significativamente. Sin embargo, expertos señalaron rápidamente que la cifra mencionada solo cubría la ejecución final de entrenamiento y excluía la investigación, experimentos anteriores y el costo del propio hardware. Aun así, el número desafiaba la creencia generalizada de que construir modelos frontera requiere miles de millones de dólares en chips.

## El debate sobre controles de exportación y geopolítica

La liberación de DeepSeek también reabrió el debate sobre los controles de exportación estadounidenses. Estados Unidos ha limitado la venta de sus chips más avanzados a China, argumentando que podrían usarse con fines militares. Algunos comentaristas dijeron que los resultados de DeepSeek demostraban que las restricciones estaban empujando a las compañías chinas a volverse más eficientes; otros sostuvieron que probaron que los controles necesitaban ser reforzados aún más.

Este contexto geopolítico afecta directamente la disponibilidad de tecnología para los negocios globales. Si las regulaciones fueran a cambiar, podría haber consecuencias en el suministro de hardware necesario para la expansión de la inteligencia artificial. Por otro lado, la capacidad de DeepSeek para lograr altos rendimientos con restricciones de hardware sugiere que la innovación puede surgir incluso bajo presión regulatoria. Las empresas deben considerar que la disponibilidad de ciertos componentes críticos podría estar sujeta a decisiones políticas internacionales que escapan al control directo de una pyme.

## Modelos abiertos y reacciones de la industria

Un aspecto clave que cambia el juego para los emprendedores es que el modelo de razonamiento de DeepSeek se lanzó con pesos abiertos. Esto significa que cualquier empresa puede descargarlo y ejecutarlo en su propia infraestructura. Dentro de pocos días, la aplicación de asistente de la compañía escaló hasta los primeros lugares en las listas de descargas en varios países.

Varios líderes tecnológicos estadounidenses reaccionaron públicamente a la noticia. Algunos elogiaron el trabajo, mientras que otros cuestionaron si la empresa había revelado todos los recursos que utilizó. OpenAI dijo que estaba revisando si sus modelos habían sido utilizados indebidamente para entrenar sistemas competidores. Estas tensiones entre empresas establecidas y nuevos actores indican un mercado competitivo donde la propiedad intelectual y el uso ético de datos son temas calientes.

Además, hubo preocupación entre los inversores. Temían que si los modelos potentes pudieran entrenarse con menos chips, la demanda de los procesadores más caros de Nvidia podría ralentizarse. Sin embargo, otros analistas argumentaron lo contrario: los modelos más baratos tienden a aumentar el uso total, lo que al final requiere más potencia de computación. Esta contradicción subraya la incertidumbre sobre la demanda futura de infraestructura tecnológica.

## Lo que esto significa para tu empresa

Para las pequeñas empresas que utilizan inteligencia artificial, el episodio tuvo una lectura práctica muy clara. La competencia entre proveedores de modelos está empujando los precios a la baja, y los modelos abiertos están convirtiéndose en una opción real para las empresas que quieren controlar los costos o mantener sus datos internos.

Esto cambia la ecuación de inversión para tus proyectos de automatización. Anteriormente, muchas pymes dependían de APIs externas costosas debido a la falta de alternativas viables. Ahora, con modelos que pueden ejecutarse en infraestructura propia gracias a los pesos abiertos, tienes la oportunidad de gestionar mejor la privacidad y el gasto. Si bien el informe de DeepSeek no cubre todos los costos asociados (como el hardware físico o el tiempo de investigación previa), demuestra que no es estrictamente necesario tener un presupuesto multimillonario para acceder a capacidades avanzadas de IA.

Los fundadores deben evaluar si les conviene mantener sus datos in-house versus depender de servicios externos. La capacidad de descargar y ejecutar modelos localmente ofrece soberanía de datos que antes era difícil de conseguir. Además, al saber que la competencia de precios está en marcha, es un buen momento para negociar contratos o explorar soluciones basadas en modelos abiertos que reduzcan la dependencia de un solo proveedor de nube o chip.

En resumen, el mercado de la inteligencia artificial está madurando rápidamente. La caída de Nvidia refleja el miedo a la saturación de costos, pero también abre la puerta a una democratización del acceso. Como fundador, debes observar cómo bajan los precios de las herramientas y cuándo puedes implementar tus propias instancias. La eficiencia es ahora una prioridad global, y eso beneficia a quienes buscan optimizar sus operaciones sin sacrificar rendimiento. Mantente atento a las actualizaciones técnicas, ya que las ideas descritas en los informes de investigación podrían ser adoptadas por otros laboratorios, acelerando aún más esta tendencia hacia una IA más accesible y económica para todos los sectores.