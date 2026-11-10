# Nemotron 3 Nano 30B — noticias_redaccion/deepseek_caida_nvidia

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 7.8 | quality: 7.88
- latency_total: 5.876s | tokens_per_second: 298.5
- input_tokens: 706 | output_tokens: 1754

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

## Resumen del impacto en el mercado  

Las acciones de **Nvidia** cayeron alrededor de **17 %** en una sola sesión, lo que supuso la pérdida de **casi 600 mil millones de dólares** en valor de mercado. Este movimiento se produjo después de que la startup china **DeepSeek** presentara un modelo de inteligencia artificial que alcanzó un rendimiento comparable al de los sistemas más avanzados de EE. UU., pero con un gasto de entrenamiento mucho menor.  

## Costos de entrenamiento de DeepSeek  

Según el informe técnico publicado por la compañía, el **último entrenamiento** del modelo tuvo un coste de **aproximadamente 5,6 millones de dólares** en tiempo de cómputo. Para llevar a cabo ese entrenamiento se emplearon **2 048 chips Nvidia H800**, una variante diseñada para cumplir con las restricciones de exportación estadounidenses.  

## Técnicas que redujeron el gasto  

DeepSeek describió varios métodos de ingeniería que permitieron abaratar el proceso:  

- **Arquitectura de activación esparsa**: solo una parte del modelo se activa para cada solicitud, lo que disminuye el consumo de recursos.  
- **Optimizaciones en el entrenamiento**: técnicas que hacen más eficiente el uso de los chips disponibles, reduciendo el tiempo y el número de operaciones necesarias.  

Investigadores de otros países señalaron que los documentos de DeepSeek eran detallados y que algunas de estas ideas podrían ser adoptadas por otros laboratorios para mejorar su propia eficiencia.  

## Reacción de la industria  

La noticia generó diversas reacciones entre los principales actores tecnológicos:  

- **OpenAI** anunció que estaba revisando si sus propios modelos habían sido usados indebidamente para entrenar sistemas competidores.  
- Algunos comentaristas aplaudieron el trabajo de DeepSeek, mientras que otros cuestionaron la transparencia sobre los recursos realmente empleados.  
- Analistas financieros y de mercado debatieron si los resultados indicarían una disminución en la demanda de los procesadores más costosos de Nvidia, o, por el contrario, abrirían la puerta a un mayor uso global de la computación necesaria para IA.  

## Implicaciones para las pymes  

Para las pequeñas y medianas empresas que utilizan inteligencia artificial, el episodio ofrece varios aprendizajes prácticos:  

- **Competencia en precios**: La aparición de modelos de alta calidad a bajo costo está presionando a los proveedores a reducir sus tarifas, lo que puede traducirse en precios más accesibles para los usuarios finales.  
- **Modelos abiertos**: DeepSeek liberó su modelo con **pesos abiertos**, lo que permite a cualquier empresa descargarlo y ejecutarlo en su propia infraestructura. Esta opción brinda mayor control sobre gastos y sobre el manejo de datos sensibles.  
- **Ahorro en infraestructura**: Al poder entrenar o ejecutar modelos con menos chips avanzados, las pymes pueden reducir la inversión en hardware costoso y, en su lugar, optar por soluciones basadas en la nube o en clusters más modestos.  

## Debate sobre controles de exportación  

La publicación del modelo de DeepSeek reabrió el debate sobre las **restricciones de exportación de chips avanzados** impuestas por EE. UU. Estas medidas, justificadas por motivos de seguridad nacional, limitan la venta de los procesadores más potentes a China.  

- Algunos expertos argumentan que las restricciones están impulsando a las empresas chinas a desarrollar **soluciones más eficaces**, tal como demostró DeepSeek.  
- Otros sostienen que dichas barreras deberían **endurecerse** para evitar que la tecnología de punta sea utilizada fuera del ámbito permitido.  

En cualquier caso, el caso ha puesto de relieve la interdependencia entre políticas comerciales, desarrollo tecnológico y competitividad global.  

## Qué significa para la adopción de modelos abiertos  

El hecho de que DeepSeek haya puesto a disposición su modelo con **pesos abiertos** ha generado un interés inmediato en el mercado:  

- En pocos días, la aplicación de asistente de DeepSeek alcanzó los primeros puestos en las listas de descargas en varios países.  
- La disponibilidad de un modelo de alto rendimiento sin costo de licencia permite a empresas y desarrolladores experimentar, personalizar y desplegar soluciones de IA bajo sus propias condiciones de seguridad y cumplimiento normativo.  

## Conclusión práctica para las pymes  

Para una pyme que busca aprovechar la inteligencia artificial sin comprometer su presupuesto, el escenario actual ofrece oportunidades concretas:  

1. **Evaluar modelos de código abierto**: La opción de descargar y ejecutar modelos como el de DeepSeek permite evitar licencias costosas y mantener los datos bajo control interno.  
2. **Optimizar el uso de recursos**: Las técnicas de activación esparsa y de entrenamiento eficiente demostradas por DeepSeek pueden inspirar la adopción de herramientas que reduzcan el consumo de cómputo en entornos empresariales.  
3. **Aprovechar la caída de precios**: La presión competitiva derivada de la aparición de modelos de bajo costo está llevando a los proveedores a ofrecer planes más económicos, lo que beneficia directamente a las empresas que buscan soluciones escalables.  

En síntesis, el episodio muestra que la **eficiencia en el entrenamiento de IA** ya es una realidad tangible, y que las pymes pueden beneficiarse de ella mediante la selección cuidadosa de modelos abiertos y la adopción de estrategias de cómputo más ajustadas a sus necesidades específicas. La capacidad de entrenar o ejecutar modelos avanzados con una inversión reducida está redefiniendo las reglas del juego, y las pequeñas y medianas empresas están en una posición privilegiada para aprovechar estas ventajas.