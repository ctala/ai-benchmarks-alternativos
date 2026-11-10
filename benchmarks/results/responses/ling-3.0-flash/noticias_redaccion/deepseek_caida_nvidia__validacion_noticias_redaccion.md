# Ling 3.0 Flash — noticias_redaccion/deepseek_caida_nvidia

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 7.71 | quality: 7.9
- latency_total: 25.241s | tokens_per_second: 84.5
- input_tokens: 735 | output_tokens: 2134

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

## Nvidia perdió casi 600.000 millones de dólares en un día. ¿Qué significa para las pymes?

El lunes 27 de enero, las acciones de Nvidia cayeron aproximadamente un 17 % después de que la startup china DeepSeek presentara un modelo de inteligencia artificial capaz de igualar el rendimiento de los principales sistemas estadounidenses. La pérdida bursátil eliminó cerca de 600.000 millones de dólares del valor de mercado de Nvidia en una sola sesión, una de las mayores caídas diarias en la historia del mercado bursátil estadounidense.

La razón de ese desplome no fue un problema interno de la empresa, sino un anuncio que sacudió una creencia arraigada en toda la industria: que construir modelos de IA de frontera requiere miles de millones de dólares en chips y infraestructura. DeepSeek dijo que su última corrida de entrenamiento costó unos 5,6 millones de dólares en tiempo de cómputo y utilizó 2.048 procesadores Nvidia H800, una versión diseñada para cumplir con las restricciones de exportación de Estados Unidos.

Para las pymes que están evaluando cómo adoptar la IA, el episodio tiene lecturas prácticas que vale la pena entender.

## Un modelo que compite por una fracción del costo

DeepSeek tiene su sede en Hangzhou y recibe financiación de un fondo de inversión cuantitativo chino. Su creador es Liang Wenfeng, quien también cofundó ese fondo. Según personas cercanas a la empresa, la compañía contrató a numerosos investigadores jóvenes de universidades chinas y apostó por la investigación en lugar de lanzar productos comerciales de forma acelerada.

El dato que más impactó al mercado fue el del costo de entrenamiento. Si bien expertos señalaron que esa cifra de 5,6 millones solo cubrió la corrida final de entrenamiento y no incluyó investigación previa, experimentaciones anteriores ni el costo del hardware, el número desafió la idea extendida de que los modelos de última generación solo son accesibles para grandes corporaciones.

## Cómo lo lograron

En su documentación técnica, DeepSeek describió varias técnicas de ingeniería que permitieron reducir costos. Entre ellas, una arquitectura que activa solo una parte del modelo para cada consulta y métodos que hacen el entrenamiento más eficiente con los chips disponibles.

Investigadores de otros países revisaron los documentos publicados por DeepSeek y calificaron los papers como detallados. Algunas de las ideas descritas podrían adoptarse en otros laboratorios, lo que sugiere que las prácticas de eficiencia no son exclusivas de una sola empresa.

## El modelo abierto: una oportunidad real para las pymes

El modelo de razonamiento de DeepSeek se publicó con pesos abiertos. Esto significa que cualquier empresa puede descargarlo y ejecutarlo en su propia infraestructura. En cuestión de días, la aplicación asistente de DeepSeek escaló hasta los primeros puestos de las listas de descargas en varios países.

Para una pyme, esto abre dos puertas concretas:

- **Control de costos.** Un modelo disponible de forma abierta elimina la dependencia de suscripciones costosas a servicios de terceros. La empresa puede ejecutar el modelo en su propio hardware o en la nube, pagando solo por los recursos que consuma.
- **Soberanía de datos.** Mantener los datos dentro de la propia infraestructura reduce riesgos de filtraciones y facilita el cumplimiento de normativas de protección de datos, un tema relevante tanto en América Latina como en España.

## La polémica detrás del logro

El éxito de DeepSeek reavivó el debate sobre los controles de exportación estadounidenses. Estados Unidos limita la venta de sus chips más avanzados a China argumentando que podrían usarse con fines militares. Algunos comentaristas señalaron que las restricciones obligaron a las empresas chinas a volverse más eficientes; otros opinaron que los resultados demuestran que los controles deben endurecerse.

Varios líderes de la industria tecnológica estadounidense reaccionaron públicamente. Algunos elogiaron el trabajo, mientras que otros cuestionaron si DeepSeek había revelado todos los recursos que utilizó. OpenAI, por su parte, anunció que estaba revisando si sus modelos se usaron de manera inadecuada para entrenar sistemas competidores.

## Qué significa esto para las pymes

Más allá de las cifras bursátiles y la política comercial, el episodio deja tres enseñanzas prácticas para las pequeñas y medianas empresas:

1. **La competencia entre proveedores de modelos está reduciendo precios.** Si un modelo puede entrenarse con un presupuesto mucho menor, la presión sobre los proveedores comerciales crecerá. Las pymes que comparen opciones hoy tienen margen para negociar mejor.

2. **Los modelos abiertos son una alternativa seria.** Ya no se trata solo de experimentos académicos. Las empresas pueden evaluar modelos de código abierto sin depender de un único proveedor.

3. **La eficiencia importa más que el volumen.** Las técnicas descritas por DeepSeek demuestran que optimizar cómo se usan los recursos puede reducir costos sin sacrificar rendimiento. En automatización, esto se traduce en procesos más inteligentes con menor inversión.

En resumen, el mercado bursátil reaccionó a una sola cifra: la posibilidad de que los modelos potentes ya no requieran inversiones monumentales. Para las pymes, la pregunta más relevante no es si la IA va a seguir transformando los negocios —ya lo está haciendo— sino cuánto antes pueden incorporarla de forma controlada, económica y segura.