# GLM 5.3 Flash — noticias_redaccion/deepseek_caida_nvidia

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 145.744s | tokens_per_second: 59.5
- input_tokens: 681 | output_tokens: 8675

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

# DeepSeek: el modelo "barato" que hizo perder 600.000 millones a Nvidia y lo que cambia para tu pyme

## La noticia que sacudió al sector

El fabricante de chips Nvidia, empresa que sostiene buena parte de la infraestructura del auge de la inteligencia artificial, vio caer sus acciones cerca del 17% en una sola jornada. Esa caída borró cerca de 600.000 millones de dólares de su valor de mercado y quedó entre las mayores pérdidas diarias en la historia de la bolsa estadounidense.

El detonante no fue un informe financiero ni una decisión regulatoria, sino el lanzamiento de un modelo de inteligencia artificial de DeepSeek, una startup china que, según la propia empresa, logró igualar el rendimiento de los sistemas líderes de Estados Unidos mientras costaba una fracción entrenarlo.

Para una pyme que usa IA —o que la está evaluando—, este episodio tiene lecturas prácticas que van mucho más allá de los titulares financieros.

## ¿Quién es DeepSeek?

DeepSeek tiene su base en Hangzhou, China, y está respaldada por un fondo de cobertura chino. Fue fundada por Liang Wenfeng, quien también cofundó el fondo cuantitativo que financia a la empresa.

Según personas familiarizadas con la compañía, DeepSeek contrató a muchos investigadores jóvenes provenientes de universidades chinas y apostó por la investigación por encima de la construcción rápida de productos comerciales. Esa orientación de laboratorio ayuda a explicar por qué un actor relativamente nuevo pudo producir un resultado de esta magnitud.

La reacción del mercado fue inmediata también del lado de los usuarios: en cuestión de días, la aplicación de asistente de la empresa escaló hasta el primer puesto de las listas de descargas en varios países.

## La cifra que cambió la conversación: 5,6 millones de dólares

El centro de la polémica está en el informe técnico que publicó DeepSeek. Según la empresa, la ejecución final de entrenamiento de uno de sus modelos costó unos 5,6 millones de dólares en tiempo de cómputo y utilizó 2.048 chips Nvidia H800, una versión de los procesadores de la compañía diseñada para cumplir con las restricciones de exportación de Estados Unidos.

Los expertos señalaron de inmediato un matiz clave: esa cifra cubre solo la ejecución final del entrenamiento. Excluye la investigación previa, los experimentos anteriores y el costo del hardware en sí. El costo total del proyecto, en consecuencia, fue mayor.

Aun con esas salvedades, el número desafiaba una creencia extendida en la industria: la de que construir modelos de frontera —los más potentes del mercado— exige invertir miles de millones de dólares en chips. Si un actor nuevo puede acercarse al rendimiento de los líderes con una fracción del presupuesto de cómputo, la economía de todo el sector queda bajo revisión.

## ¿Cómo lo consiguieron?

En su documentación técnica, DeepSeek describió varias técnicas de ingeniería que le permitieron reducir costos:

- **Una arquitectura que activa solo una parte del modelo para cada solicitud**, en lugar de utilizar el sistema completo en cada consulta.
- **Métodos que hacen el entrenamiento más eficiente** con los chips que la empresa tenía disponibles, pese a las restricciones de exportación.

Los investigadores de otros países que revisaron los trabajos coincidieron en que los documentos eran detallados y que algunas de estas ideas podrían ser adoptadas por otros laboratorios. Es decir, la eficiencia lograda por DeepSeek no tiene por qué quedarse en China: puede convertirse en estándar para toda la industria.

## Elogios, dudas y un debate sobre las restricciones

La reacción al lanzamiento fue inmediata y dividida. Varios líderes tecnológicos estadounidenses se pronunciaron públicamente: algunos elogiaron el trabajo y otros cuestionaron si la empresa había divulgado todos los recursos que utilizó. OpenAI, por su parte, dijo estar revisando si sus modelos habían sido usados de manera indebida para entrenar sistemas competidores.

El episodio también reabrió el debate sobre los controles de exportación estadounidenses, que limitan la venta de los chips más avanzados a China argumentando que podrían emplearse con fines militares. Frente a los resultados de DeepSeek se enfrentaron dos lecturas:

- Para algunos comentaristas, los resultados demuestran que las restricciones empujaron a las empresas chinas a volverse más eficientes.
- Para otros, prueban justo lo contrario: que los controles deben endurecerse aún más.

## Pesos abiertos: el detalle que más le importa a tu negocio

Más allá del ruido bursátil, hay un dato con impacto directo para las empresas: el modelo de razonamiento de DeepSeek se publicó con pesos abiertos. En la práctica, eso significa que cualquier empresa puede descargarlo y ejecutarlo en su propia infraestructura.

La diferencia con los modelos cerrados es sustancial. Mientras que los sistemas propietarios se utilizan a través de servicios externos, un modelo de pesos abiertos permite a una organización tener el modelo funcionando bajo su propio control. Para negocios que manejan información sensible, ese punto no es menor: se relaciona directamente con la posibilidad de mantener los datos dentro de la empresa y de gestionar los costos de uso con mayor margen.

Que esto sea viable dejó de ser una promesa teórica: el lanzamiento de DeepSeek demostró que existen alternativas de alto rendimiento en formato abierto.

## El dilema de los inversores: ¿menos chips o más demanda?

La preocupación que golpeó a Nvidia fue clara: si los modelos potentes se pueden entrenar con menos chips, la demanda de sus procesadores más caros podría desacelerarse.

Pero otros analistas argumentaron exactamente lo contrario: los modelos más baratos tienden a aumentar el uso total de la inteligencia artificial y, a la larga, un mayor uso requiere más poder de cómputo. Las dos tesis conviven hoy en el mercado, y el desenlace definirá cuánto poder de cómputo pedirá la industria en los próximos años.

## La lectura práctica para las pymes

Para las empresas pequeñas que usan IA, este episodio deja una lectura esencialmente práctica, con dos consecuencias visibles:

**1. La competencia entre proveedores empuja los precios a la baja.** Si entrenar un modelo potente cuesta una fracción de lo que se creía, la presión competitiva sobre los proveedores se intensifica. Para las pymes, esto se traduce en una tendencia hacia precios más accesibles en los servicios de IA.

**2. Los modelos abiertos son una opción real.** Ya no son una alternativa marginal para entusiastas: son una vía concreta para las empresas que quieren controlar sus costos o mantener sus datos en su propia infraestructura.

En términos operativos, esto sugiere tres preguntas que toda pyme que trabaja con IA debería hacerse:

- ¿Cuánto estoy pagando hoy por acceso a modelos de IA, y existe una alternativa más económica con calidad comparable?
- ¿Hay procesos en los que mantener los datos dentro de la empresa justifique evaluar un modelo de pesos abiertos?
- ¿Con qué rapidez están cambiando las opciones disponibles? El episodio demuestra que el mapa de proveedores y precios se mueve en cuestión de días, no de años.

Ninguna de estas preguntas tiene una respuesta única: depende de cada negocio, de sus datos y de su infraestructura. Pero el contexto cambió: la IA de alto rendimiento dejó de estar asociada de forma automática a presupuestos gigantescos.

## En resumen

El lanzamiento de DeepSeek hizo temblar a Nvidia en la bolsa y desató debates que seguirán abiertos por mucho tiempo: sobre los controles de exportación, sobre la economía del entrenamiento de modelos y sobre qué recursos usan realmente los laboratorios. Pero para las pymes el mensaje es más simple y más útil: la competencia entre proveedores de IA se intensificó, los precios tienden a bajar y los modelos abiertos se consolidaron como una opción seria para controlar costos y proteger datos. Quien esté decidiendo cómo incorporar inteligencia artificial a su negocio tiene hoy más alternativas sobre la mesa —y conviene revisarlas con esa nueva realidad en mente.