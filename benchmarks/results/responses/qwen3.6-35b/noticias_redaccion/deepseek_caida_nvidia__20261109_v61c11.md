# Qwen 3.6 35B base (OpenRouter FP8) — noticias_redaccion/deepseek_caida_nvidia

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 72.256s | tokens_per_second: 76.7
- input_tokens: 703 | output_tokens: 5540

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



La industria de la inteligencia artificial acaba de demostrar que los costos y las expectativas sobre el desarrollo de modelos no son lo que parecían. Si gestionas una empresa en América Latina o España, este es un momento clave para entender cómo está cambiando el panorama y qué implica para tu adopción tecnológica. La noticia que ha movido los mercados y redefinido discusiones técnicas es clara: una startup china, DeepSeek, lanzó un modelo que iguala el rendimiento de los sistemas líderes estadounidenses, pero con un costo de entrenamiento una fracción menor. La reacción del mercado fue inmediata y contundente, y para cualquier fundador que evalúe integrar automatización, el mensaje es inequívoco: el ecosistema está entrando en una fase de disrupción donde las barreras de entrada técnicas y económicas se están redefiniendo.

## Un golpe de 600.000 millones en un día

Las acciones del fabricante de chips Nvidia cayeron cerca de un 17% un lunes, lo que borró aproximadamente 600.000 millones de dólares de su valor de mercado en una sola sesión. Esta pérdida representa una de las mayores caídas en un único día en la historia del mercado de valores de Estados Unidos. El desencadenante fue el anuncio de DeepSeek, una empresa con sede en Hangzhou respaldada por un fondo de cobertura chino, que publicó un informe técnico detallando cómo logró entrenar uno de sus modelos utilizando solo 2.048 chips Nvidia H800, una versión diseñada para cumplir con las restricciones de exportación estadounidenses. El costo computacional final de ese entrenamiento ascendió a unos 5,6 millones de dólares. Para los emprendedores, el impacto inicial es evidente: el mercado está ajustando sus proyecciones sobre cuánto se necesita invertir en hardware para competir en la vanguardia de la IA.

## Cómo DeepSeek redujo los costos de entrenamiento

La eficiencia de DeepSeek no surgió de la nada. La compañía fue fundada por Liang Wenfeng, quien también co fundó el fondo de cobertura cuantitativo que la financia. Según personas familiarizadas con la operación, la empresa contrató a numerosos investigadores jóvenes de universidades chinas y priorizó la investigación pura sobre el desarrollo rápido de productos comerciales. Esta filosofía se reflejó en su documentación técnica, donde describieron varias técnicas de ingeniería clave. Entre ellas, una arquitectura que activa solo una parte del modelo para cada solicitud, lo que optimiza el uso de recursos. Además, implementaron métodos que hacen el entrenamiento más eficiente con los chips disponibles. Investigadores de otros países reconocieron que los artículos técnicos eran detallados y que algunas de estas ideas podrían ser adoptadas por otros laboratorios, lo que sugiere un efecto multiplicador en la eficiencia del sector a nivel global.

## El debate sobre las restricciones de exportación

El lanzamiento de DeepSeek reabrió un debate de larga data sobre el control de exportaciones estadounidenses. Estados Unidos ha limitado la venta de sus chips más avanzados a China, argumentando que podrían destinarse a propósitos militares. Sin embargo, los resultados de DeepSeek han generado posturas divididas. Algunos comentaristas sostuvieron que estas restricciones están empujando a las empresas chinas a volverse más eficientes, optimizando lo que tienen disponible. Otros argumentaron que los resultados demuestran que los controles deberían endurecerse aún más. Para una pyme que planea integrar IA, este contexto geopolítico es relevante porque afecta directamente la disponibilidad de hardware, los precios de los servicios de cómputo y las estrategias de implementación a largo plazo. La competencia tecnológica ya no se mide solo en algoritmos, sino en cómo se navegan las limitaciones de infraestructura global.

## Reacciones en la industria y matices sobre el costo

La noticia provocó respuestas públicas de varios líderes tecnológicos estadounidenses. Algunos elogiaron el trabajo, mientras que otros cuestionaron si la empresa había revelado todos los recursos utilizados. OpenAI, por ejemplo, anunció que estaba revisando si sus modelos habían sido utilizados de manera indebida para entrenar sistemas competitivos. Es fundamental entender un matiz técnico que muchos análisis pasaron por alto: expertos señalaron rápidamente que la cifra de 5,6 millones de dólares solo cubría la última corrida de entrenamiento. No incluye los costos de investigación, experimentos previos ni el costo del hardware en sí. Aun así, el número desafía la creencia generalizada de que desarrollar modelos de vanguardia requiere miles de millones de dólares en chips. Esto significa que el techo de inversión inicial para acceder a capacidades avanzadas de IA está bajando, un dato crítico para presupuestos empresariales.

## Modelos abiertos y oportunidades para las pymes

DeepSeek liberó su modelo de razonamiento con pesos abiertos, lo que permite que cualquier empresa lo descargue y lo ejecute en su propia infraestructura. La adopción fue rápida: en pocos días, la aplicación de asistente de la compañía alcanzó los primeros puestos en las listas de descargas en varios países. En el mercado, los inversores mostraron preocupación ante la posibilidad de que, si los modelos potentes pueden entrenarse con menos chips, la demanda de los procesadores más caros de Nvidia podría ralentizarse. Sin embargo, otros analistas argumentaron lo contrario: los modelos más económicos tienden a aumentar el uso total, lo que a la larga requiere más capacidad de cómputo. Para las pequeñas y medianas empresas, este escenario tiene una lectura práctica inmediata. La competencia entre proveedores de modelos está presionando los precios a la baja, y los modelos abiertos se están consolidando como una opción real para negocios que buscan controlar costos o mantener sus datos dentro de su infraestructura.

## Qué significa esto para tu negocio

Si diriges una empresa en América Latina o España, la disrupción generada por este anuncio no es solo un titular de bolsa, sino un cambio estructural en cómo se despliegan las soluciones de automatización. Históricamente, la implementación de IA avanzada se asociaba a inversiones millonarias en infraestructura o a la dependencia exclusiva de proveedores extranjeros con precios altos. Ahora, la eficiencia en el entrenamiento, la arquitectura de modelos parciales y la disponibilidad de pesos abiertos ofrecen alternativas tangibles. Las pymes pueden evaluar si migrar a modelos de código abierto ejecutados en sus propios servidores reduce su dependencia y protege su información sensible. Al mismo tiempo, la presión competitiva en el sector de los modelos está traducida en menores costos de licenciamiento y acceso, lo que permite probar, iterar y escalar automatizaciones con presupuestos más ajustados.

La clave para los fundadores y directores ahora es dejar de ver la IA como un gasto de capital fijo y empezar a tratarla como un servicio modular y optimizable. Revisar tu stack tecnológico, evaluar la viabilidad de ejecutar modelos abiertos en tu infraestructura y aprovechar la caída de precios en los servicios de IA son pasos concretos que puedes tomar hoy. El mercado acaba de enviar una señal clara: la eficiencia técnica ya no es exclusiva de grandes laboratorios con fondos ilimitados. Es el momento de integrar estas herramientas con criterio, midiendo costos reales, privacidad de datos y rendimiento operativo, para que tu empresa no solo se adapte al cambio, sino que lo aproveche como ventaja competitiva.