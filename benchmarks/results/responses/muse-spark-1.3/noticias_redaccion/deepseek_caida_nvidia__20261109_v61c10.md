# Muse Spark 1.3 — noticias_redaccion/deepseek_caida_nvidia

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 7.89 | quality: 9.4
- latency_total: 47.123s | tokens_per_second: 86.2
- input_tokens: 694 | output_tokens: 4060

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

# DeepSeek, Nvidia y el costo de la IA: lo que una pyme necesita entender

La noticia sorprendió incluso a los inversores más acostumbrados a los movimientos bruscos del sector tecnológico. Las acciones del fabricante de chips Nvidia cayeron alrededor de 17% en un lunes, después de que la startup china DeepSeek publicara un modelo de inteligencia artificial que, según la compañía, igualó el rendimiento de los principales sistemas estadounidenses pero costó una fracción en entrenamiento.

La caída borró cerca de 600.000 millones de dólares del valor de mercado de Nvidia en una sola sesión, una de las mayores pérdidas en un día en la historia del mercado bursátil de Estados Unidos. Para una pyme que usa IA en atención al cliente, ventas o automatización de procesos, ese número puede parecer lejano. Pero lo que está detrás explica por qué los precios de los modelos pueden bajar y por qué aparecen nuevas opciones para controlar costos o mantener los datos en casa.

## Qué pasó en la bolsa y por qué importa para la IA

El movimiento en la bolsa no fue un ajuste menor. Una caída de cerca de 17% en un solo día para una empresa del tamaño de Nvidia implicó la pérdida de cerca de 600.000 millones de dólares en valor de mercado.

La causa directa, según la fuente, fue la publicación del modelo de DeepSeek. La empresa afirmó que su modelo igualó el desempeño de los sistemas estadounidenses líderes y que lo hizo con un costo de entrenamiento mucho menor.

Los inversores reaccionaron a una idea muy concreta: si se pueden entrenar modelos potentes con menos chips, la demanda de los procesadores más caros de Nvidia podría frenarse. Otros analistas defendieron la lectura opuesta: los modelos más baratos suelen aumentar el uso total, lo que al final exige más capacidad de cómputo.

Ese debate entre menos chips por modelo y más uso total es central para entender lo que puede pasar con los precios y la disponibilidad de la IA para empresas pequeñas y medianas.

## Quién es DeepSeek y cuánto dice haber gastado

DeepSeek es una startup con sede en Hangzhou, respaldada por un fondo de cobertura chino. Fue fundada por Liang Wenfeng, quien también cofundó el fondo de cobertura cuantitativo que la financia.

Según personas familiarizadas con la compañía, DeepSeek contrató a muchos investigadores jóvenes de universidades chinas y se concentró en la investigación en lugar de construir productos comerciales rápidamente. Ese enfoque en investigación, más que en lanzar productos comerciales a corto plazo, es parte de la explicación de cómo llegó a este resultado.

En un informe técnico, la compañía dijo que la ejecución final de entrenamiento de uno de sus modelos costó alrededor de 5,6 millones de dólares en tiempo de cómputo y utilizó 2.048 chips H800 de Nvidia, una versión de los procesadores de la compañía diseñada para cumplir con las restricciones de exportación estadounidenses.

La cifra de 5,6 millones de dólares llamó la atención porque desafió la creencia extendida de que construir modelos de frontera requiere miles de millones de dólares en chips. Aun así, los expertos aclararon rápidamente que esa cifra solo cubría la ejecución final de entrenamiento y excluía la investigación, los experimentos anteriores y el costo del propio hardware.

## Cómo explica la empresa la reducción de costos

En su documentación técnica, DeepSeek describió varias técnicas de ingeniería que le ayudaron a reducir los costos. Entre ellas mencionó una arquitectura que activa solo una parte del modelo para cada solicitud y métodos que hacen más eficiente el entrenamiento con los chips que tenía disponibles.

Investigadores de otros países dijeron que los documentos eran detallados y que algunas de las ideas podrían ser adoptadas por otros laboratorios. Es decir, no se trató solo de un anuncio comercial, sino de papeles técnicos con un nivel de detalle suficiente para que otros equipos los estudien y potencialmente los apliquen.

Para una pyme, el detalle técnico puede parecer complejo, pero la idea de fondo es simple: activar solo una parte del modelo para cada pedido y aprovechar mejor los chips disponibles puede reducir el costo del entrenamiento. Si esas ideas se extienden a otros laboratorios, la competencia entre proveedores de modelos puede aumentar y empujar los precios a la baja.

## Por qué se reabrió el debate sobre los chips y Estados Unidos

La publicación también reabrió el debate sobre los controles de exportación estadounidenses. Estados Unidos ha limitado la venta de sus chips más avanzados a China, con el argumento de que podrían usarse con fines militares.

En este caso, DeepSeek dijo haber usado 2.048 chips H800 de Nvidia, una versión de los procesadores diseñada para cumplir con las restricciones de exportación estadounidenses. Ese dato puso el tema en el centro de la discusión.

Algunos comentaristas dijeron que los resultados de DeepSeek mostraban que las restricciones estaban empujando a las empresas chinas a volverse más eficientes. Otros dijeron que demostraban que los controles debían endurecerse aún más.

Para las pymes de América Latina y España, este debate no es solo geopolítica. Si las restricciones llevan a mayor eficiencia y a nuevas formas de entrenar con menos recursos, eso puede traducirse en modelos más baratos y en más opciones disponibles en el mercado.

## Las dudas sobre los recursos realmente usados

No todas las reacciones fueron de elogio. Varios líderes tecnológicos estadounidenses reaccionaron públicamente a la noticia, algunos elogiando el trabajo y otros cuestionando si la compañía había revelado todos los recursos que utilizó.

OpenAI dijo que estaba revisando si sus modelos habían sido usados de forma indebida para entrenar sistemas competidores. Esa revisión apunta a la preocupación de que los modelos existentes puedan haberse aprovechado para entrenar sistemas rivales.

Por otro lado, los expertos insistieron en poner la cifra de 5,6 millones de dólares en contexto. Ese monto solo cubría la ejecución final de entrenamiento. No incluía la investigación, ni los experimentos anteriores, ni el costo del propio hardware.

Aun con esa aclaración, el número mantuvo su impacto. Incluso si no refleja el costo total del proyecto, desafió la idea de que solo con miles de millones de dólares en chips se pueden construir modelos de frontera. Y esa es la razón por la que los inversores se preguntaron si cambiará la demanda de los procesadores más caros.

## Qué significa que el modelo sea abierto

Uno de los puntos más relevantes para las empresas es que el modelo de razonamiento de DeepSeek fue publicado con pesos abiertos, lo que significa que cualquier empresa puede descargarlo y ejecutarlo en su propia infraestructura.

En pocos días, la aplicación de asistente de la compañía subió a los primeros puestos de las listas de descargas en varios países. Eso mostró el interés del público y también la velocidad con la que un modelo abierto puede distribuirse.

Para una pyme, el modelo de pesos abiertos abre una opción concreta: descargar el modelo y ejecutarlo en infraestructura propia. Según la lectura práctica del episodio, los modelos abiertos se están convirtiendo en una opción real para las empresas que quieren controlar costos o mantener sus datos en sus propias instalaciones.

Esa posibilidad es especialmente importante para negocios que trabajan con información sensible de clientes, que necesitan controlar dónde se procesan los datos o que quieren evitar depender por completo de un solo proveedor.

## Qué cambia en la práctica para una pyme que usa IA

Para las pequeñas empresas que ya usan IA, el episodio tuvo una lectura práctica muy clara. La competencia entre proveedores de modelos estaba empujando los precios a la baja, y los modelos abiertos se estaban volviendo una opción real para las empresas que quieren controlar costos o mantener sus datos en casa.

Si modelos potentes pueden entrenarse con menos chips, hay dos efectos posibles que las pymes deben seguir. Por un lado, la preocupación de los inversores: una menor necesidad de chips por entrenamiento podría frenar la demanda de los procesadores más caros. Por otro lado, el argumento de otros analistas: los modelos más baratos tienden a aumentar el uso total, lo que al final requiere más potencia de cómputo.

En ambos casos, el resultado para una pyme es más uso de IA a menor costo por uso, pero con mayor volumen total. La competencia entre proveedores, sumada a la disponibilidad de modelos con pesos abiertos que cualquier empresa puede descargar y ejecutar en su propia infraestructura, crea un escenario donde es posible negociar mejores precios, probar alternativas y decidir dónde conviene procesar los datos.

La lección no es que una tecnología reemplace a otra de un día para otro, sino que el costo de entrenamiento dejó de verse como una barrera fija de miles de millones de dólares en chips. Con 2.048 chips H800, una ejecución final de alrededor de 5,6 millones de dólares en tiempo de cómputo, técnicas que activan solo parte del modelo por solicitud y métodos para entrenar de forma más eficiente, una startup enfocada en investigación logró igualar el rendimiento de los sistemas líderes y llevar su asistente a lo más alto de las descargas.