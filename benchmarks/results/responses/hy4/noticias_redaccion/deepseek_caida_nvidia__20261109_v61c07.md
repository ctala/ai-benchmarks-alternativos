# Tencent Hy4 — noticias_redaccion/deepseek_caida_nvidia

- model_id: `tencent/hy4`
- success: True  | final: 8.33 | quality: 10.0
- latency_total: 209.434s | tokens_per_second: 135.2
- input_tokens: 703 | output_tokens: 28321

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

# DeepSeek, Nvidia y qué significa para las pymes que usan IA

## La caída que abrió la noticia

Las acciones del fabricante de chips Nvidia cayeron alrededor de 17 % el lunes después de que la empresa emergente china DeepSeek presentara un modelo de inteligencia artificial. Según la compañía, ese modelo igualó el rendimiento de los principales sistemas estadounidenses y costó una fracción para entrenarlo. El descenso borró cerca de 600.000 millones de dólares del valor de mercado de Nvidia en una sola sesión. Fue una de las mayores pérdidas de un solo día en la historia del mercado bursátil de Estados Unidos.

La caída se produjo después de la publicación de DeepSeek y de lo que esa publicación decía sobre el costo de entrenar modelos. DeepSeek tiene sede en Hangzhou y está respaldada por un fondo de cobertura chino.

## La cifra del informe técnico y sus límites

DeepSeek publicó un informe técnico en el que afirmaba que la ejecución final de entrenamiento de uno de sus modelos había costado unos 5,6 millones de dólares en tiempo de cómputo y había usado 2.048 chips Nvidia H800. Los H800 son una versión de los procesadores de Nvidia diseñada para cumplir con las restricciones estadounidenses a la exportación.

Expertos señalaron rápidamente que esa cifra solo cubría la ejecución final de entrenamiento. Quedaban fuera la investigación, los experimentos anteriores y el costo del propio hardware. Incluso así, el número cuestionó la creencia generalizada de que construir modelos de frontera exige miles de millones de dólares en chips.

Esa distinción no frenó la lectura de mercado. Los inversores temieron que, si es posible entrenar modelos potentes con menos chips, la demanda de los procesadores más caros de Nvidia podría ralentizarse. Otros analistas sostuvieron lo contrario: los modelos más baratos tienden a aumentar el uso total, y ese uso total, al final, requiere más capacidad de cómputo. La fuente recoge ambas interpretaciones.

## Quién fundó DeepSeek y cómo trabajó

La compañía fue fundada por Liang Wenfeng, quien también cofundó el fondo cuantitativo de cobertura que la financia. Según personas familiarizadas con la compañía, DeepSeek contrató a muchos investigadores jóvenes de universidades chinas y se centró en la investigación más que en construir productos comerciales rápidamente.

Ese énfasis aparece también en su documentación técnica. DeepSeek describió varias técnicas de ingeniería que le ayudaron a reducir costos. Entre ellas, una arquitectura que activa solo una parte del modelo para cada solicitud y métodos que hacen más eficiente el entrenamiento en los chips de los que disponía. Investigadores de otros países dijeron que los artículos eran detallados y que algunas de las ideas podrían ser adoptadas por otros laboratorios.

## Pesos abiertos y adopción en días

El modelo de razonamiento de DeepSeek se publicó con pesos abiertos, lo que significa que cualquier empresa puede descargarlo y ejecutarlo en su propia infraestructura. En cuestión de días, la aplicación de asistente de la compañía subió a lo más alto de las listas de descargas en varios países.

La definición de pesos abiertos que ofrece la fuente indica dos acciones posibles para cualquier empresa: descargar el modelo y ejecutarlo en su propia infraestructura. Esa misma posibilidad aparece cuando la fuente habla de negocios que quieren controlar costos o mantener sus datos dentro de la compañía.

## El debate por los controles a la exportación

La publicación también reabrió el debate sobre los controles estadounidenses a la exportación. Estados Unidos ha limitado la venta de sus chips más avanzados a China, con el argumento de que podrían usarse con fines militares. Los H800, usados en la ejecución final de entrenamiento descrita en el informe, son una versión de los procesadores de Nvidia diseñada para cumplir con esas restricciones.

Las lecturas fueron opuestas. Algunos comentaristas dijeron que los resultados de DeepSeek mostraban que las restricciones estaban empujando a las empresas chinas a volverse más eficientes. Otros dijeron que esos mismos resultados demostraban que los controles debían endurecerse aún más. La fuente recoge ambas posiciones dentro del debate reabierto.

## Reacciones de la industria tecnológica

Varios líderes tecnológicos estadounidenses reaccionaron públicamente a la noticia. Unos elogiaron el trabajo de DeepSeek. Otros cuestionaron si la compañía había divulgado todos los recursos que utilizó. OpenAI, por su parte, dijo que estaba revisando si sus modelos se habían usado de forma indebida para entrenar sistemas competidores.

La advertencia de los expertos ya había acotado esa cifra: la ejecución final de entrenamiento de uno de los modelos, con exclusión de la investigación, los experimentos anteriores y el costo del propio hardware. En el mismo episodio, la fuente registra el elogio de unos líderes tecnológicos, la pregunta de otros sobre todos los recursos utilizados y la revisión anunciada por OpenAI. La cifra, las dudas y las reacciones quedan una al lado de la otra.

## La lectura práctica para pequeñas empresas

Para las pequeñas empresas que usan IA, el episodio tuvo una lectura práctica. La competencia entre proveedores de modelos estaba empujando los precios a la baja. Y los modelos abiertos se estaban convirtiendo en una opción real para los negocios que quieren controlar costos o mantener sus datos dentro de la compañía.

Esa lectura se apoya en dos elementos ya descritos: por un lado, la posibilidad de descargar un modelo con pesos abiertos y ejecutarlo en infraestructura propia; por otro, la idea de que los modelos más baratos tienden a aumentar el uso total, lo que al final requiere más capacidad de cómputo. La fuente también señala que los inversores temían una menor demanda de los procesadores más caros de Nvidia si los modelos potentes se entrenan con menos chips, y que otros analistas defendían el efecto contrario.

El marco es ese: competencia entre proveedores, precios a la baja, modelos abiertos como opción real y dos motivos, controlar costos o mantener los datos dentro de la compañía.

## Lo que convive en la fuente

En la fuente conviven varias lecturas. El informe da unos 5,6 millones de dólares en tiempo de cómputo para la ejecución final de uno de los modelos; los expertos recuerdan que excluye investigación, experimentos anteriores y el costo del hardware. Los inversores ven riesgo de menor demanda para los procesadores más caros de Nvidia; otros analistas ven más uso total y, al final, más capacidad de cómputo. Unos comentaristas leen las restricciones como empuje a la eficiencia; otros, como razón para endurecerlas. Unos líderes elogian el trabajo; otros preguntan por los recursos utilizados, y OpenAI revisa si sus modelos se usaron de forma indebida para entrenar sistemas competidores.

Para las pequeñas empresas, la lectura práctica queda en precios a la baja y modelos abiertos como opción real.