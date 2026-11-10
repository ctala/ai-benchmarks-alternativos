# GPT-OSS 120B — noticias_redaccion/deepseek_caida_nvidia

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 5.59 | quality: 5.25
- latency_total: 39.987s | tokens_per_second: 49.2
- input_tokens: 735 | output_tokens: 1969

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

## Introducción  

En la última semana el mercado de la inteligencia artificial (IA) recibió una sacudida que llamó la atención tanto de inversores como de pequeñas y medianas empresas (pymes). Un modelo de IA desarrollado por la startup china **DeepSeek** demostró un rendimiento comparable al de los sistemas líderes de Estados Unidos, pero con un costo de entrenamiento mucho menor. El anuncio provocó una caída del **17 %** en las acciones de **Nvidia**, borrando cerca de **600 000 millones de dólares** de su capitalización en una sola sesión, uno de los mayores descensos de un día en la historia del mercado bursátil estadounidense.  

Este artículo analiza, con datos de la fuente, qué significa este hecho para las pymes que usan IA y cómo puede influir en la evolución del sector.  

## ¿Qué es DeepSeek y cómo logró el resultado?  

DeepSeek es una startup de IA con sede en Hangzhou, China. La empresa está respaldada por un fondo de cobertura chino y fue fundada por **Liang Wenfeng**, quien también co‑fundó el fondo que la financia. Según fuentes cercanas, DeepSeek ha contratado a numerosos jóvenes investigadores de universidades chinas y se ha centrado más en la investigación que en lanzar rápidamente productos comerciales.  

En un informe técnico publicado por la compañía se detalla que la **última fase de entrenamiento** de uno de sus modelos costó **aproximadamente 5,6 millones de dólares** en tiempo de cómputo. Para lograrlo, la empresa utilizó **2 048 chips Nvidia H800**, una versión de los procesadores de Nvidia diseñada para cumplir con las restricciones de exportación estadounidenses.  

### Técnicas de reducción de costos  

El documento técnico de DeepSeek describe varias estrategias de ingeniería que permitieron bajar el gasto:  

- **Arquitectura parcial activada**: solo una parte del modelo se activa para cada solicitud, lo que reduce la carga computacional por inferencia.  
- **Métodos de entrenamiento más eficientes**: optimizaciones específicas para aprovechar al máximo los chips H800 disponibles.  

Investigadores de otros países calificaron los papers como detallados y señalaron que algunas de estas ideas podrían ser adoptadas por otros laboratorios.  

## Repercusiones en Nvidia  

El anuncio de DeepSeek provocó una reacción inmediata en el mercado: las acciones de Nvidia cayeron alrededor del **17 %**, borrando casi **600 000 millones de dólares** de su valor de mercado en una sola jornada.  

Los inversores temen que, si modelos tan potentes pueden entrenarse con menos chips, la demanda de los procesadores más costosos de Nvidia pueda desacelerarse. Sin embargo, algunos analistas argumentan que los modelos más baratos pueden **aumentar el uso total de IA**, lo que a la larga requeriría más capacidad de cómputo y, por ende, mantendría o incluso incrementará la demanda de hardware.  

## Debate sobre los controles de exportación estadounidenses  

Estados Unidos ha limitado la venta de sus chips más avanzados a China, argumentando que podrían usarse con fines militares. La aparición de DeepSeek reaviva este debate:  

- **Quienes defienden las restricciones** consideran que los resultados de DeepSeek demuestran que las medidas deben endurecerse, pues incluso con chips limitados se pueden crear modelos competitivos.  
- **Quienes critican las limitaciones** sostienen que las restricciones están impulsando a las empresas chinas a ser más eficientes y a buscar alternativas de bajo costo.  

En este contexto, varios líderes tecnológicos estadounidenses reaccionaron públicamente. Algunos elogiaron el trabajo de DeepSeek, mientras que otros cuestionaron si la compañía había revelado todos los recursos empleados. **OpenAI** indicó que está revisando si sus propios modelos fueron usados indebidamente para entrenar sistemas competidores.  

## Lo que realmente cuesta entrenar un modelo “frontera”  

Los expertos señalaron que el costo de **5,6 millones de dólares** corresponde únicamente a la **última fase de entrenamiento**. No incluye:  

- La investigación y desarrollo previo.  
- Experimentos y entrenamientos intermedios.  
- El costo del hardware (chips, servidores, etc.).  

Aun con esas exclusiones, la cifra desafía la creencia ampliamente extendida de que la construcción de modelos de última generación requiere **miles de millones de dólares** en chips.  

## Modelo abierto y adopción rápida  

DeepSeek lanzó su modelo de razonamiento con **pesos abiertos**, lo que permite a cualquier empresa descargarlo y ejecutarlo en su propia infraestructura. En cuestión de días, la aplicación de asistente basada en este modelo alcanzó los primeros lugares en las listas de descargas de varios países.  

Esta apertura tiene dos implicaciones claras para las pymes:  

1. **Acceso a tecnología de alto nivel sin costos de licencia**.  
2. **Posibilidad de mantener los datos internos**, lo que favorece la seguridad y la privacidad.  

## Qué pueden aprender las pymes de este episodio  

### 1. La competencia está reduciendo precios  

La presión entre los proveedores de modelos está empujando a la baja los precios. Para una pyme que necesita IA, esto se traduce en **opciones más asequibles** para implementar soluciones de automatización, análisis de datos o atención al cliente.  

### 2. Los modelos abiertos son una alternativa viable  

Con modelos de pesos abiertos como el de DeepSeek, las empresas pueden **evitar depender de servicios externos** y, en cambio, ejecutar la IA en sus propios servidores o en la nube que elijan. Esto reduce costos de suscripción y brinda mayor control sobre la información.  

### 3. La eficiencia del hardware importa  

Las técnicas de DeepSeek (arquitectura parcial, entrenamiento eficiente) demuestran que **optimizar el uso de los chips** puede generar ahorros sustanciales. Las pymes que desarrollen o utilicen IA deberían prestar atención a estas prácticas para maximizar el retorno de inversión en infraestructura.  

### 4. Vigilancia de regulaciones internacionales  

El debate sobre los controles de exportación de EE. UU. muestra que **las políticas gubernamentales pueden afectar la disponibilidad y el precio del hardware**. Las empresas deben mantenerse informadas sobre posibles cambios regulatorios que impacten la adquisición de GPUs u otros aceleradores.  

### 5. Evaluar el coste total de propiedad (TCO)  

Aunque el costo de entrenamiento reportado por DeepSeek es bajo, el **costo total** incluye investigación, experimentación y hardware. Las pymes deben calcular el TCO antes de decidir si entrenan sus propios modelos o adoptan soluciones preentrenadas.  

## Conclusión  

El caso de DeepSeek evidencia que el desarrollo de modelos de IA de alta calidad ya no está reservado exclusivamente a gigantes con presupuestos de cientos de millones de dólares. Con **5,6 millones de dólares** y **2 048 chips H800**, una startup china logró igualar el rendimiento de los sistemas estadounidenses, provocando una fuerte reacción en el mercado de Nvidia y reavivando el debate sobre los controles de exportación.  

Para las pymes, este episodio trae dos mensajes claros: **la competencia está haciendo que la IA sea más accesible** y **los modelos abiertos se están convirtiendo en una opción real para controlar costos y proteger datos**. Mantenerse al tanto de las innovaciones en eficiencia de entrenamiento y de la evolución de las regulaciones internacionales será clave para aprovechar al máximo estas oportunidades y seguir siendo competitivas en un entorno cada vez más automatizado.