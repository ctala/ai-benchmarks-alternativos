# Fugu Max — noticias_redaccion/deepseek_caida_nvidia

- model_id: `sakana/fugu-max`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 12.472s | tokens_per_second: 204.5
- input_tokens: 802 | output_tokens: 2550

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

# El día que Nvidia perdió 600.000 millones de dólares: qué pasó con DeepSeek y qué significa para tu pyme

Durante meses, la conversación sobre inteligencia artificial en las empresas tuvo un supuesto de fondo: construir modelos de frontera cuesta miles de millones de dólares en chips, y eso mantiene el juego reservado a unos pocos gigantes. Ese supuesto se tambaleó esta semana.

El lunes, las acciones de Nvidia cayeron alrededor de un 17% después de que la startup china DeepSeek publicara un modelo de inteligencia artificial que igualó el rendimiento de los principales sistemas estadounidenses y que, según la propia compañía, costó una fracción de lo que cuesta entrenar esos sistemas. La caída borró cerca de 600.000 millones de dólares del valor de mercado de Nvidia en una sola sesión, una de las mayores pérdidas en un día en la historia del mercado bursátil estadounidense.

Para una pyme que está evaluando cómo usar IA en sus procesos, la noticia no es la caída de una acción. Es lo que ocurrió detrás: un modelo potente, entrenado con menos recursos de los que se creían necesarios, publicado con pesos abiertos y acompañado de un informe técnico que otros investigadores consideraron detallado.

## Qué es DeepSeek y qué publicó

DeepSeek tiene su sede en Hangzhou y está respaldada por un fondo de cobertura chino. La empresa fue fundada por Liang Wenfeng, quien también cofundó el fondo cuantitativo que la financia. Según personas familiarizadas con la compañía, contrató a muchos investigadores jóvenes de universidades chinas y se centró en la investigación en lugar de construir productos comerciales rápidamente.

La compañía publicó un informe técnico en el que señala que la ejecución final de entrenamiento de uno de sus modelos costó alrededor de 5,6 millones de dólares en tiempo de cómputo y utilizó 2.048 chips Nvidia H800, una versión de los procesadores de la empresa diseñada para cumplir con las restricciones estadounidenses a la exportación.

Además, su modelo de razonamiento se publicó con pesos abiertos. En términos prácticos: cualquier empresa puede descargarlo y ejecutarlo en su propia infraestructura. En pocos días, la aplicación asistente de la compañía escaló hasta lo más alto de las listas de descargas en varios países.

## El dato de los 5,6 millones: qué incluye y qué no

El número que recorrió el mundo fue ese: 5,6 millones de dólares. Conviene manejarlo con precisión, porque los propios expertos señalaron rápidamente sus límites.

Esa cifra cubre únicamente la ejecución final de entrenamiento. Deja fuera la investigación previa, los experimentos anteriores y el costo del hardware en sí mismo. Es decir, no es el costo total de desarrollar el modelo, sino el de una etapa concreta.

Aun así, el dato desafió la creencia extendida de que construir modelos de frontera requiere miles de millones de dólares en chips. Y esa creencia es la que sostenía, en buena medida, la idea de que solo un puñado de empresas podía competir en la primera liga.

## Cómo redujeron costos

En su documentación técnica, DeepSeek describió varias técnicas de ingeniería que le ayudaron a bajar costos. Entre ellas, una arquitectura que activa solo una parte del modelo en cada solicitud y métodos que hacen el entrenamiento más eficiente en los chips de los que disponía.

Investigadores de otros países señalaron que los documentos eran detallados y que algunas de las ideas podían ser adoptadas por otros laboratorios. Traducido al mundo de la empresa: las mejoras de eficiencia no se quedan en un cajón. Tienden a difundirse.

## La reacción de la industria

Varios líderes tecnológicos estadounidenses reaccionaron públicamente a la noticia. Algunos elogiaron el trabajo; otros cuestionaron si la compañía había divulgado todos los recursos que utilizó.

OpenAI, por su parte, dijo que estaba revisando si sus modelos habían sido utilizados de forma indebida para entrenar sistemas competidores.

## El debate sobre los controles de exportación se reabrió

El anuncio también reabrió la discusión sobre los controles estadounidenses a la exportación. Estados Unidos ha limitado la venta de sus chips más avanzados a China, argumentando que podrían usarse con fines militares.

Algunos comentaristas señalaron que los resultados de DeepSeek mostraban que las restricciones estaban empujando a las empresas chinas a ser más eficientes. Otros sostuvieron que demostraban que los controles debían endurecerse aún más. Las dos lecturas convivieron en la misma conversación, y ninguna se resolvió con el anuncio.

## El temor de los inversores y la lectura contraria

Los inversores se preocuparon de que, si se pueden entrenar modelos potentes con menos chips, la demanda de los procesadores más caros de Nvidia podría frenarse. Ese temor es, en buena medida, lo que explica la caída del 17%.

Otros analistas sostuvieron lo contrario: los modelos más baratos tienden a aumentar el uso total, lo que al final requiere más capacidad de cómputo. Es una discusión abierta, y quien afirme tener la respuesta cerrada está adivinando.

## La lectura práctica para una pyme

Para las empresas pequeñas que usan inteligencia artificial, el episodio tiene una interpretación concreta, y es la parte que más conviene retener.

Primero: la competencia entre proveedores de modelos está empujando los precios a la baja. Segundo: los modelos abiertos se están convirtiendo en una opción real para las empresas que quieren controlar costos o mantener sus datos dentro de casa.

Ese segundo punto merece atención en cualquier pyme que esté definiendo su estrategia. Durante mucho tiempo, la única vía práctica era pagar una suscripción o un consumo por uso a un proveedor externo, con los datos saliendo de la organización. Un modelo con pesos abiertos cambia esa ecuación: se puede descargar y ejecutar en la infraestructura propia. No es gratis —hay que contar hardware, personal técnico y mantenimiento—, pero deja de ser impensable para una empresa mediana.

## Lo que no conviene concluir

Hay tres atajos de lectura que conviene evitar.

El primero: creer que entrenar un modelo de frontera cuesta 5,6 millones de dólares y nada más. La cifra excluye investigación, experimentos previos y hardware, como señalaron los expertos.

El segundo: asumir que la caída de Nvidia significa que la demanda de cómputo se va a desplomar. Hay analistas que sostienen exactamente lo contrario, y el debate sigue abierto.

El tercero: dar por resuelta la discusión sobre los controles de exportación. Lo que el episodio hizo fue reabrirla, con posiciones enfrentadas y sin conclusión.

## Qué mirar ahora

Si tu empresa está eligiendo herramientas de IA este año, el episodio de DeepSeek deja tres preguntas útiles sobre la mesa.

¿Cuánto de tu operación depende de un solo proveedor de modelos? La competencia está bajando precios, y eso es margen de negociación.

¿Tus datos pueden salir de la empresa? Si la respuesta es no —por regulación, por contrato con clientes o por simple criterio—, los modelos abiertos ya son una alternativa que vale la pena al menos evaluar técnicamente.

¿Tu equipo sabe qué significa ejecutar un modelo en infraestructura propia? Porque la barrera, en muchos casos, ya no es el precio del modelo, sino la capacidad interna para montarlo y mantenerlo. Ahí es donde la automatización y la infraestructura bien diseñadas marcan la diferencia.

La caída del 17% de Nvidia fue la noticia visible. La historia de fondo es más útil para una pyme: el costo de acceder a inteligencia artificial de primer nivel está dejando de ser un club cerrado.