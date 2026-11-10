# Gemini 3.8 Flash — noticias_redaccion/deepseek_caida_nvidia

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.32 | quality: 9.74
- latency_total: 25.32s | tokens_per_second: 143.9
- input_tokens: 693 | output_tokens: 3644

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

El sector de la inteligencia artificial ha experimentado un movimiento de gran escala que captó la atención tanto de los mercados financieros internacionales como de las empresas que siguen de cerca la evolución tecnológica. La empresa china DeepSeek presentó un modelo de inteligencia artificial capaz de igualar el rendimiento de los sistemas líderes desarrollados en Estados Unidos, asegurando haberlo conseguido a una fracción muy reducida del costo de entrenamiento tradicional.

Este anuncio provocó una sacudida inmediata en los mercados bursátiles y abrió un análisis profundo sobre los costos computacionales, la arquitectura de los modelos y las opciones disponibles para las pequeñas y medianas empresas. A continuación, se detalla lo ocurrido, las cifras técnicas reportadas y las implicaciones directas para las organizaciones que buscan automatizar sus procesos.

## El impacto en el mercado: la histórica caída de Nvidia

La primera consecuencia visible tras la presentación del modelo de DeepSeek se registró en la bolsa de valores de Estados Unidos. Las acciones del fabricante de procesadores Nvidia se desplomaron aproximadamente un 17% durante la jornada del lunes. 

Este descenso porcentual eliminó cerca de 600.000 millones de dólares del valor de mercado de Nvidia en una sola sesión bursátil. Dicha cifra representa una de las mayores pérdidas en un solo día registradas en toda la historia del mercado accionario estadounidense. El movimiento reflejó la sorpresa de los inversores ante la posibilidad de que el desarrollo de modelos de inteligencia artificial de frontera no requiera necesariamente las cantidades masivas de capital y hardware que hasta ahora se consideraban indispensables.

## El origen de DeepSeek y su estrategia de desarrollo

DeepSeek es una empresa emergente con sede en Hangzhou, China. La compañía cuenta con el respaldo financiero de un fondo de cobertura cuantitativo chino y fue fundada por Liang Wenfeng, quien también es cofundador de dicho fondo. 

De acuerdo con fuentes cercanas a la organización, la estructura y el método de trabajo de DeepSeek se apartaron del camino habitual de las empresas emergentes del sector. En lugar de orientarse de forma inmediata a la creación acelerada de productos comerciales, la empresa contrató a un gran número de jóvenes investigadores provenientes de universidades chinas y concentró sus esfuerzos principalmente en la investigación técnica. Esta estrategia enfocada en la exploración académica y el diseño computacional permitió a la firma centrarse en resolver problemas de eficiencia antes de pasar al terreno comercial.

## El reporte técnico: 5,6 millones de dólares y 2.048 chips H800

Junto con el lanzamiento de su modelo de razonamiento, DeepSeek publicó un informe técnico en el que desglosó los recursos empleados para su desarrollo. En dicho documento, la compañía indicó que la fase final de entrenamiento de uno de sus modelos demandó un costo aproximado de 5,6 millones de dólares en tiempo de computación.

Para llevar a cabo este proceso, la empresa utilizó 2.048 chips Nvidia H800. Este modelo de procesador constituye una versión diseñada específicamente para cumplir con las restricciones de exportación que el gobierno de Estados Unidos impone al comercio de tecnología hacia China. 

La cifra de 5,6 millones de dólares contrastó de manera directa con las estimaciones generalizadas en la industria, donde se asumía que construir sistemas de rendimiento similar requería presupuestos de miles de millones de dólares en infraestructura de procesamiento.

## Innovaciones en ingeniería para reducir el consumo computacional

En su documentación técnica, DeepSeek detalló diversas técnicas de ingeniería orientadas a disminuir los costos y optimizar el rendimiento de los recursos disponibles. 

Entre los elementos más destacados figura una arquitectura que activa únicamente una parte del modelo ante cada solicitud o consulta, en lugar de poner en funcionamiento la totalidad de sus parámetros en todo momento. Asimismo, el equipo implementó métodos diseñados para elevar la eficiencia del entrenamiento en los procesadores específicos con los que contaban.

Investigadores de otros países examinaron los informes publicados y señalaron que los documentos presentaban un alto nivel de detalle técnico. Diversos especialistas manifestaron que varias de las ideas y metodologías expuestas por DeepSeek podrían ser adoptadas por otros laboratorios y centros de investigación dedicados a la inteligencia artificial en todo el mundo.

## El debate sobre las restricciones de exportación

El rendimiento obtenido por DeepSeek con procesadores de menor capacidad técnica reabrió la discusión internacional en torno a los controles de exportación impuestos por el gobierno estadounidense. 

Estados Unidos ha restringido la venta de sus procesadores más avanzados a China bajo el argumento de que este tipo de hardware podría tener usos militares. A raíz de la presentación de DeepSeek, surgieron dos lecturas opuestas entre los analistas:

* Por un lado, algunos analistas señalaron que estos resultados demuestran que las restricciones comerciales están obligando a las empresas chinas a ser mucho más eficientes en el aprovechamiento de los recursos disponibles, incentivando soluciones de ingeniería que compensan la falta de hardware de última generación.
* Por otro lado, otros comentaristas sostuvieron que estos avances evidencian que las medidas de control actuales no son suficientes y que resulta necesario endurecer aún más las restricciones comerciales existentes.

## Reacciones en el sector y la postura de OpenAI

La difusión del modelo generó diversas declaraciones públicas entre los líderes del sector tecnológico estadounidense. Mientras algunos de ellos reconocieron y elogiaron el trabajo técnico realizado por DeepSeek, otros pusieron en duda si la empresa china había hecho públicos todos los recursos e insumos que realmente utilizó durante el proceso de desarrollo.

En este marco, OpenAI comunicó que se encuentra revisando si sus propios modelos fueron utilizados de forma indebida para entrenar a los sistemas de la competencia, en referencia directa al desarrollo presentado por la startup de Hangzhou.

## Precisiones técnicas sobre el costo real del modelo

Tras la divulgación del informe, analistas y expertos del sector se encargaron de contextualizar la cifra de 5,6 millones de dólares informada por DeepSeek. 

Los especialistas recalcaron que ese valor corresponde de forma exclusiva a la ejecución final del entrenamiento del modelo. Por ende, la cifra no contempla:
* El costo del hardware en sí mismo ni la adquisición de los chips.
* Las fases previas de investigación y diseño.
* Los experimentos anteriores que se llevaron a cabo antes de alcanzar la versión definitiva.

A pesar de estas aclaraciones, los analistas coincidieron en que el monto informado pone en tela de juicio la creencia arraigada en el mercado de que el desarrollo de modelos de frontera exige necesariamente inversiones multimillonarias destinadas a procesadores.

## Pesos abiertos y la adopción de la aplicación

Una característica central del modelo de razonamiento de DeepSeek es que fue publicado con pesos abiertos (*open weights*). Esta condición técnica permite que cualquier empresa u organización tenga la posibilidad de descargarlo y ejecutarlo dentro de su propia infraestructura tecnológica, sin depender de servidores de terceros.

En paralelo a la publicación técnica, la aplicación de asistencia de DeepSeek experimentó una rápida difusión entre el público. A los pocos días de su presentación, la herramienta logró ubicarse en los primeros puestos de las listas de descargas en diversos países.

## El dilema de los inversores: ¿menor demanda o mayor uso de chips?

El éxito de una arquitectura más eficiente generó dos interpretaciones encontradas entre los analistas financieros:

1. **La preocupación por una caída en las ventas:** Algunos inversores temen que, si es posible entrenar modelos avanzados con una cantidad considerablemente menor de chips, la demanda corporativa por los procesadores más costosos de Nvidia podría desacelerarse en el mediano plazo.
2. **El efecto de un mayor uso global:** Otros especialistas plantearon el escenario opuesto, argumentando que la reducción en los costos de los modelos tiende a masificar el uso total de la inteligencia artificial. Desde esta perspectiva, una mayor adopción general demandará, a largo plazo, una capacidad de cómputo aún más amplia en todo el ecosistema.

## El valor para las pequeñas empresas

Para las pequeñas empresas interesadas en automatizar sus tareas y aprovechar la inteligencia artificial, este acontecimiento aporta conclusiones de orden práctico:

* **Mayor presión en los precios:** La competencia directa entre los diferentes proveedores de modelos impulsa una reducción generalizada en las tarifas de los servicios tecnológicos.
* **Autonomía y control de costos:** La consolidación de modelos con pesos abiertos abre una alternativa viable para las pymes que necesitan gestionar sus presupuestos de forma estricta.
* **Seguridad de la información:** La posibilidad de descargar y ejecutar estos sistemas en servidores e infraestructura propia permite que las empresas mantengan sus datos de manera interna, protegiendo su información sin quedar supeditadas a plataformas externas.