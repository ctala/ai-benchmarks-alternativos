# Inkling Small — noticias_redaccion/deepseek_caida_nvidia

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 51.816s | tokens_per_second: 45.7
- input_tokens: 678 | output_tokens: 2368

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

## Un terremoto en la industria de la IA: DeepSeek y la caída de Nvidia

El pasado lunes, el mundo tecnológico amaneció con una noticia que no estaba en ninguna agenda de start-ups latinoamericanas, pero que afecta directamente a cualquier pyme que use inteligencia artificial. Las acciones de Nvidia cayeron alrededor del 17 % tras el lanzamiento de un modelo de la startup china DeepSeek que, según la propia empresa, igualó el rendimiento de los sistemas líderes de Estados Unidos a una fracción del costo de entrenamiento. La caída borró casi 600.000 millones de dólares de la capitalización de mercado de Nvidia en una sola sesión, una de las mayores pérdidas de un día en la historia de la bolsa estadounidense.

Para un emprendedor que invierte en automatización o analiza herramientas de IA, el mensaje no es solo financiero: es una señal de que el mercado de modelos de lenguaje está cambiando de reglas, y que las pymes pueden beneficiarse de una competencia más agresiva.

## ¿Qué es DeepSeek y cuánto costó realmente entrenar su modelo?

DeepSeek es una startup con sede en Hangzhou, respaldada por un hedge fund chino. La empresa publicó un informe técnico que detalló los recursos de su última corrida de entrenamiento: unos 5,6 millones de dólares en tiempo de computación, utilizando 2.048 chips Nvidia H800, una versión de los procesadores diseñada para cumplir con las restricciones de exportación de Estados Unidos.

El fundador es Liang Wenfeng, quien también cofundó el fondo cuantitativo que financia a la compañía. Según personas familiarizadas con la organización, DeepSeek contrató a muchos investigadores jóvenes de universidades chinas y se centró en la investigación más que en construir productos comerciales con rapidez. Esa cultura explica por qué la empresa priorizó la eficiencia técnica antes que el lanzamiento rápido de una suite de ventas.

En su documentación técnica, DeepSeek describió varias técnicas de ingeniería que redujeron los costos: una arquitectura que activa solo parte del modelo para cada solicitud, junto con métodos que hacen más eficiente el entrenamiento en los chips disponibles. Investigadores de otros países señalaron que los documentos eran detallados y que algunas de esas ideas podrían ser adoptadas por otros laboratorios, no solo por competidores.

## El debate sobre exportaciones y el escepticismo de Silicon Valley

El lanzamiento reabrió el debate sobre los controles de exportación estadounidenses. Estados Unidos ha limitado la venta de sus chips más avanzados a China, argumentando que podrían usarse para fines militares. Algunos comentaristas dijeron que los resultados de DeepSeek demostraban que esas restricciones empujaban a las empresas chinas a ser más eficientes. Otros sostuvieron lo contrario: que los resultados probaban que los controles debían endurecerse aún más.

Varios líderes tecnológicos estadounidenses reaccionaron de forma pública. Algunos elogió el trabajo; otros cuestionaron si la empresa había revelado todos los recursos utilizados. OpenAI señaló que estaba revisando si sus modelos habían sido usados de forma indebida para entrenar sistemas competidores. La transparencia, por tanto, sigue siendo un tema abierto, aunque la información técnica publicada es suficientemente específica para ser analizada por la comunidad científica.

## La cifra de 5,6 millones: qué dice y qué no dice

Los expertos señalaron rápidamente que la cifra de 5,6 millones de dólares cubría solo la corrida final de entrenamiento. Quedaban fuera la investigación previa, los experimentos anteriores y el costo del hardware en sí. Aunque la cifra no cuenta toda la historia, sí desafió la creencia generalizada de que construir modelos de frontera requiere miles de millones de dólares en chips. Eso es relevante para las pymes porque demuestra que la curva de costos de la IA de alta gama no es lineal: la eficiencia algorítmica puede reducir la barrera de entrada mucho más de lo que se asumía.

## Pesos abiertos y una ola de descargas

El modelo de razonamiento de DeepSeek se liberó con pesos abiertos, lo que significa que cualquier empresa puede descargarlo y ejecutarlo en su propia infraestructura. En pocos días, la aplicación asistente de la compañía subió a la cima de las listas de descargas en varios países. Para una pyme, esto es una inflexión práctica: no tienes que depender exclusivamente de una API de un proveedor estadounidense para acceder a capacidades avanzadas, siempre que cuentes con la infraestructura o un proveedor de nube que te permita desplegarlo.

## Lo que los inversionistas discuten y lo que importa para tu empresa

Los inversionistas se preocupan por una posibilidad: si los modelos potentes pueden entrenarse con menos chips, la demanda de los procesadores más caros de Nvidia podría ralentizarse. Otros analistas argumentan lo contrario: los modelos más baratos tienden a aumentar el uso total, y al final eso requiere más potencia de computación, no menos.

Para las pequeñas empresas que usan IA, la lectura es más simple y directa: la competencia entre proveedores de modelos está empujando los precios hacia abajo, y los modelos abiertos se están convirtiendo en una opción real para los negocios que buscan controlar costos o mantener sus datos dentro de su propio entorno.

Si tu empresa está evaluando automatizar procesos con IA, esto implica tres cosas concretas:

1. **Revisa los precios de los proveedores actuales.** La presión competitiva significa que las tarifas de API pueden bajar o que aparecerán alternativas locales o de código abierto con calidad comparable.
2. **Evalúa el control de datos.** Un modelo de pesos abiertos te permite correr la inferencia en servidores propios o en un entorno privado de nube, algo clave si manejas datos sensibles de clientes o de operaciones internas.
3. **No confíes solo en el costo de entrenamiento publicitado.** Como los expertos señalaron, la cifra de 5,6 millones no incluye todo el ciclo de desarrollo. Si decides construir o ajustar modelos internos, calcula investigación, pruebas y mantenimiento, no solo la última corrida.

## Conclusión: eficiencia, competencia y opciones reales

Lo que ocurrió con DeepSeek no es solo una historia de acciones bursátiles o de geopolítica tecnológica. Es una evidencia de que la eficiencia en IA puede ser tan valiosa como la escala, y que los modelos abiertos pueden alterar el equilibrio entre proveedores. Para una pyme latinoamericana o española, el mensaje es práctico: los precios de la IA generativa tienden a bajar, la opción de usar modelos en tu propia infraestructura es cada vez más viable, y la competencia entre laboratorios —ya sean estadounidenses, europeos o asiáticos— juega a favor del emprendedor que busca automatizar sin perder control de sus datos ni de su presupuesto.

No se trata de elegir bando en un debate geopolítico, sino de aprovechar que el mercado de modelos de IA se está diversificando. En ese contexto, la mejor estrategia para una empresa pequeña es mantenerse informada, comparar proveedores con criterios técnicos y de privacidad, y recordar que hoy un modelo de alta calidad puede no requerir la inversión que se asumía hace un año. La automatización inteligente sigue siendo accesible; simplemente, ahora hay más puertas para entrar.