# Qwen 3.8 Max 0902 — noticias_redaccion/deepseek_caida_nvidia

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.81 | quality: 10.0
- latency_total: 367.988s | tokens_per_second: 47.7
- input_tokens: 741 | output_tokens: 17561

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

## Qué pasó con DeepSeek y por qué afectó a Nvidia

Las acciones de Nvidia, fabricante de chips, cayeron alrededor de 17% el lunes después de que la startup china DeepSeek lanzara un modelo de inteligencia artificial que, según afirmó, igualó el rendimiento de sistemas líderes estadounidenses y costó una fracción entrenar. La baja eliminó cerca de 600.000 millones de dólares del valor de mercado de Nvidia en una sola sesión, una de las mayores pérdidas diarias en la historia del mercado bursátil de Estados Unidos.

Para una pyme que usa herramientas de IA, el dato relevante no es solo la caída de una empresa tecnológica. El punto central es que apareció una señal de que los modelos avanzados pueden desarrollarse con menos recursos de los que se suponía. Eso puede afectar precios, opciones de implementación y control de datos.

## Quién está detrás de DeepSeek

DeepSeek tiene sede en Hangzhou y está respaldada por un fondo de cobertura chino. La compañía publicó un informe técnico donde indicó que la ejecución final de entrenamiento de uno de sus modelos costó cerca de 5,6 millones de dólares en tiempo de cómputo y utilizó 2.048 chips Nvidia H800, una versión de los procesadores de Nvidia diseñada para cumplir con las restricciones de exportación de Estados Unidos.

La empresa fue fundada por Liang Wenfeng, quien también cofundó el fondo cuantitativo que la financia. Según personas familiarizadas con la compañía, DeepSeek contrató a muchos investigadores jóvenes de universidades chinas y se concentró en la investigación más que en lanzar productos comerciales con rapidez.

## Qué mostró el informe técnico

En su documentación técnica, DeepSeek describió varias técnicas de ingeniería que ayudaron a reducir costos. Entre ellas mencionó una arquitectura que activa solo una parte del modelo para cada solicitud y métodos que hacen más eficiente el entrenamiento con los chips disponibles. Investigadores de otros países afirmaron que los documentos eran detallados y que algunas ideas podían ser adoptadas por otros laboratorios.

El caso también mostró que el costo divulgado no equivale al costo total de desarrollar un modelo. La propia cifra de DeepSeek se refirió a la ejecución final de entrenamiento, no al camino completo hasta llegar ahí. Ese camino incluye investigación, pruebas anteriores y el hardware, elementos que quedaron fuera del cálculo difundido.

Aun con esa salvedad, el informe técnico tuvo impacto porque puso en duda una idea aceptada en el sector: que los modelos más avanzados exigen gastos gigantescos en chips. Si una parte del trabajo puede hacerse con menos recursos, cambia la discusión sobre cuánto hace falta para entrar en la carrera.

## El debate sobre los controles de exportación

El lanzamiento también reabrió el debate sobre los controles de exportación de Estados Unidos. El gobierno estadounidense ha limitado la venta de sus chips más avanzados a China bajo el argumento de que podrían usarse con fines militares. Algunos comentaristas dijeron que los resultados de DeepSeek mostraban que las restricciones estaban impulsando a las empresas chinas a ser más eficientes; otros sostuvieron que los controles debían endurecerse aún más.

El componente geopolítico también quedó sobre la mesa. DeepSeek usó chips H800, una versión pensada para cumplir las restricciones de exportación de Estados Unidos. Eso alimentó dos interpretaciones opuestas: que las limitaciones estaban obligando a las empresas chinas a innovar para usar mejor lo disponible, o que los controles seguían siendo insuficientes y había que reforzarlos.

## Reacciones de empresas y expertos

Varios líderes tecnológicos de Estados Unidos reaccionaron públicamente. Algunos elogiaron el trabajo; otros cuestionaron si la compañía había revelado todos los recursos utilizados. OpenAI dijo que estaba revisando si sus modelos habían sido usados de forma indebida para entrenar sistemas competidores.

Los expertos señalaron rápido que la cifra de 5,6 millones de dólares solo cubría la ejecución final de entrenamiento y dejaba fuera la investigación, los experimentos previos y el costo del propio hardware. Aun así, el número cuestionó la creencia extendida de que construir modelos de frontera requiere miles de millones de dólares en chips.

## Modelos abiertos y presión sobre precios

El modelo de razonamiento de DeepSeek fue lanzado con pesos abiertos, lo que significa que cualquier empresa puede descargarlo y ejecutarlo en su propia infraestructura. En pocos días, la aplicación de asistencia de la compañía subió a los primeros lugares de las listas de descargas en varios países.

Los inversores se preocuparon por la posibilidad de que, si se pueden entrenar modelos potentes con menos chips, la demanda de los procesadores más caros de Nvidia se frene. Otros analistas plantearon lo contrario: los modelos más baratos tienden a aumentar el uso total y, al final, eso requiere más capacidad de cómputo.

El episodio mostró dos posturas. Por un lado, los inversores temieron una menor demanda de los chips más caros. Por otro, algunos analistas sostuvieron que los modelos más baratos pueden ampliar el uso total y requerir más capacidad de cómputo.

Para las pequeñas empresas que utilizan IA, el episodio tuvo una lectura práctica. La competencia entre proveedores de modelos estaba presionando los precios a la baja, y los modelos abiertos se estaban convirtiendo en una opción real para negocios que quieren controlar costos o mantener sus datos dentro de casa.

Para una pyme, el mensaje más directo estuvo en el efecto sobre costos y opciones. Si la competencia entre proveedores empuja los precios hacia abajo, los costos para las empresas pueden bajar. Y si los modelos abiertos ganan terreno, una empresa puede considerar ejecutarlos en su propia infraestructura, algo relevante para controlar gastos o mantener datos internos.

## Resumen del episodio

En conjunto, el caso dejó tres datos visibles: una caída de alrededor de 17% en las acciones de Nvidia, un costo final de entrenamiento de cerca de 5,6 millones de dólares y un modelo abierto que cualquier empresa podía descargar y ejecutar en su propia infraestructura, según la compañía. Además, la aplicación de asistencia de DeepSeek llegó a los primeros lugares de descargas en varios países.