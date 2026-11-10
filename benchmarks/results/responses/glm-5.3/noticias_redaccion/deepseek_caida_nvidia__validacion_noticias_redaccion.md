# GLM 5.3 — noticias_redaccion/deepseek_caida_nvidia

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.14 | quality: 10.0
- latency_total: 115.334s | tokens_per_second: 82.7
- input_tokens: 681 | output_tokens: 9534

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

# DeepSeek, la caída de Nvidia y lo que significa para las pymes que usan IA

Las acciones del fabricante de chips Nvidia cayeron cerca del 17% el lunes, después de que la startup china DeepSeek lanzara un modelo de inteligencia artificial que igualó el desempeño de los sistemas líderes estadounidenses con un costo de entrenamiento que, según la empresa, fue una fracción del habitual. La caída borró cerca de **600.000 millones de dólares** del valor de mercado de Nvidia en una sola sesión: una de las mayores pérdidas en un día en la historia de la bolsa de Estados Unidos.

El temblor fue bursátil, pero las ondas expansivas llegan mucho más lejos. Para cualquier pyme que ya usa IA en sus procesos o que está evaluando adoptarla, este episodio resume un cambio de época: la inteligencia artificial de vanguardia ya no parece ser territorio exclusivo de quienes pueden gastar miles de millones de dólares en chips. Esta nota repasa qué pasó, quién lo provocó y qué lecturas prácticas puede sacar tu empresa.

## Un lunes negro para el mercado tecnológico

Nvidia fabrica los procesadores con los que se entrenan los modelos de IA más avanzados, y su valor de mercado reflejaba esa posición. Por eso, cuando DeepSeek aseguró haber logrado resultados comparables gastando mucho menos, los inversores reaccionaron con preocupación: si los modelos potentes pueden entrenarse con menos chips, la demanda por los procesadores más caros de Nvidia podría desacelerarse.

No todos comparten ese pesimismo. Otros analistas argumentaron justo lo contrario: los modelos más baratos tienden a aumentar el uso total de la IA y eso, a la larga, requiere más poder de cómputo, no menos. La discusión sigue abierta y definirá en parte el rumbo del sector.

## ¿Quién está detrás de DeepSeek?

DeepSeek tiene su sede en Hangzhou, China, y está respaldada por un fondo de cobertura de ese país. Su fundador es Liang Wenfeng, quien también cofundó el fondo cuantitativo que financia a la empresa.

Según personas familiarizadas con la compañía, DeepSeek contrató a muchos investigadores jóvenes provenientes de universidades chinas y se enfocó en la investigación más que en lanzar productos comerciales rápidamente. Esa apuesta por resolver problemas técnicos de fondo, en lugar de correr tras el mercado, parece explicar parte del resultado.

## La cifra que provocó el pánico: 5,6 millones de dólares

En un informe técnico, DeepSeek detalló que la ronda final de entrenamiento de uno de sus modelos costó unos **5,6 millones de dólares** en tiempo de cómputo y utilizó 2.048 chips Nvidia H800, una versión de sus procesadores diseñada para cumplir con las restricciones de exportación de Estados Unidos.

El matiz es importante. Los expertos señalaron rápidamente que esa cifra solo cubre la ronda final de entrenamiento y excluye la investigación previa, los experimentos anteriores y el costo del propio hardware. Es decir, la inversión total fue mayor.

Aun con esa salvedad, el número golpeó una creencia extendida en la industria: que construir modelos de frontera requiere miles de millones de dólares en chips. Si el costo de entrada es menor de lo que se pensaba, la competencia tiene más puertas abiertas.

## Ingeniería eficiente, no magia

¿Cómo logró DeepSeek reducir sus costos? En su documentación técnica, la empresa describió varias técnicas de ingeniería, entre ellas:

- Una arquitectura que activa solo una parte del modelo para cada solicitud, en lugar de usar toda la red cada vez.
- Métodos que hacen el entrenamiento más eficiente con los chips que tenía disponibles.

Investigadores de otros países calificaron los documentos como detallados y señalaron que algunas de esas ideas podrían ser adoptadas por otros laboratorios. Si eso ocurre, la eficiencia dejaría de ser una ventaja exclusiva de DeepSeek para convertirse en un estándar del sector, con efectos sobre los precios para todos los usuarios.

## El debate por el control de los chips

El lanzamiento también reabrió la discusión sobre las restricciones de exportación estadounidenses. Estados Unidos ha limitado la venta de sus chips más avanzados a China, con el argumento de que podrían usarse con fines militares.

Ante los resultados de DeepSeek, las opiniones se dividieron:

- Algunos comentaristas dijeron que las restricciones estaban empujando a las empresas chinas a volverse más eficientes.
- Otros sostuvieron que el caso probaba que los controles debían endurecerse aún más.

Hay un detalle revelador en esta historia: el chip que usó DeepSeek, el H800, existe precisamente porque fue diseñado para cumplir con esas restricciones. La empresa construyó su eficiencia sobre el hardware que tenía permitido conseguir.

## Cómo reaccionaron los gigantes tecnológicos

Varios líderes tecnológicos estadounidenses reaccionaron públicamente. Algunos elogiaron el trabajo de DeepSeek; otros cuestionaron si la empresa había revelado todos los recursos que utilizó. OpenAI, por su parte, dijo que estaba revisando si sus modelos habían sido usados de manera indebida para entrenar sistemas de la competencia.

Ese cuestionamiento apunta al corazón del asunto: saber si el costo total del desarrollo fue mayor al informado. Lo confirmado, por ahora, es lo que dice el informe técnico: 5,6 millones de dólares para la ronda final de entrenamiento de uno de sus modelos.

## La clave para las pymes: modelos con pesos abiertos

Quizás el dato más relevante para una empresa pequeña no sea el golpe bursátil, sino el producto en sí. El modelo de razonamiento de DeepSeek se publicó con pesos abiertos, lo que significa que cualquier empresa puede descargarlo y ejecutarlo en su propia infraestructura.

La adopción fue inmediata: en cuestión de días, la aplicación asistente de la empresa alcanzó el primer puesto de las listas de descargas en varios países.

Para una pyme, un modelo con pesos abiertos abre dos posibilidades concretas. La primera: controlar costos, porque puede ejecutar el modelo en su propia infraestructura en lugar de depender de un proveedor externo. La segunda: mantener los datos dentro de la organización, algo especialmente valioso cuando se trata de información sensible de clientes o del negocio.

## Qué debe sacar en claro tu empresa

Para las empresas pequeñas que usan IA, el episodio tiene una lectura práctica con dos tendencias.

La primera: la competencia entre proveedores de modelos está empujando los precios a la baja. Si tu empresa paga por acceder a modelos de IA, ese giro del mercado juega a tu favor.

La segunda: los modelos abiertos se están convirtiendo en una opción real para los negocios que quieren controlar sus costos o mantener sus datos internamente. Ya no parece necesario elegir entre la IA más avanzada y el control sobre tu información.

En otras palabras: el suelo se mueve debajo de las empresas que venden acceso a modelos de IA, y ese movimiento tiende a beneficiar a quienes los compran y los usan para automatizar procesos, atender clientes o analizar información.

## Un mercado en plena redefinición

Quedan preguntas abiertas. ¿Se desacelera la demanda de chips o crece junto con el uso masivo de modelos más baratos? Los analistas están divididos. ¿Endurece Estados Unidos sus controles de exportación? Algunos lo piden; otros creen que las restricciones solo han vuelto más eficientes a las empresas chinas.

Lo que sí queda claro para una pyme: la frontera tecnológica se movió, la competencia entre proveedores presiona los precios hacia abajo y los modelos abiertos son hoy una alternativa seria. Si tu empresa está definiendo cómo incorporar IA y automatización, este es un buen momento para evaluar qué opción conviene más a tus costos y a tus datos.