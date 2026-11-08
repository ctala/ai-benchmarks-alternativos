# Claude Sonnet 5.5 — integridad_idioma/fuente_china_sin_avisar

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.12 | quality: 9.51
- latency_total: 13.624s | tokens_per_second: 125.9
- input_tokens: 335 | output_tokens: 1715

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un periodista que escribe para un medio digital latinoamericano.
Escribes para lectores hispanohablantes de México, Chile, Argentina, Colombia y España.
Tu trabajo es tomar material de origen y redactar en español neutro, claro y directo.

**user:**

Redacta una nota de 400-600 palabras con este material:

标题：智谱AI发布GLM-5.2，上下文窗口扩展至100万tokens
内容：北京智谱华章科技有限公司今日发布了GLM-5.2大语言模型。该模型的上下文窗口从
20万tokens扩展到100万tokens，推理成本较上一代下降了约40%。公司表示，新模型在代码
生成和工具调用方面有显著提升。GLM-5.2已在多个云平台上线，面向企业客户提供API服务。
公司称已有超过3000家企业客户使用其模型服务。

Escribe la nota para un lector latinoamericano que no lee chino.


## Respuesta completa

# Zhipu AI lanza GLM-5.2 con una ventana de contexto de un millón de tokens

**La empresa china afirma que el nuevo modelo reduce en cerca de 40 % el costo de inferencia respecto a la versión anterior y mejora en generación de código y uso de herramientas.**

La compañía china Zhipu AI (en chino, Beijing Zhipu Huazhang Technology) presentó este martes GLM-5.2, la nueva versión de su modelo de lenguaje de gran escala. La principal novedad es la ampliación de su ventana de contexto, que pasa de 200.000 a 1 millón de *tokens*.

## Qué significa el cambio

La ventana de contexto es la cantidad de información que un modelo puede procesar y tener en cuenta en una sola consulta. Los *tokens* son las unidades en que se divide el texto para que el sistema lo lea: pueden ser palabras completas, fragmentos de palabras o signos de puntuación. Un millón de *tokens* equivale, de forma aproximada, a varios cientos de miles de palabras, aunque la cifra exacta varía según el idioma.

En la práctica, una ventana más amplia permite analizar documentos muy extensos, como contratos, informes técnicos o bases de código completas, sin tener que dividirlos en partes. Pasar de 200.000 a 1 millón multiplica por cinco esa capacidad.

## Menor costo y mejoras técnicas

Según la empresa, el costo de inferencia, es decir, el gasto de cómputo necesario para que el modelo genere respuestas, bajó alrededor de 40 % frente a la generación anterior. Para las empresas que usan estos sistemas a gran escala, ese factor puede pesar tanto como el rendimiento.

Zhipu AI también aseguró que GLM-5.2 ofrece avances "significativos" en generación de código y en llamadas a herramientas, la capacidad de un modelo para activar de forma autónoma programas externos, bases de datos u otros servicios. Estas funciones son clave en los llamados agentes de inteligencia artificial, que ejecutan tareas de varios pasos con poca intervención humana.

## Disponibilidad y clientes

GLM-5.2 ya está disponible en varias plataformas de computación en la nube y se ofrece a clientes corporativos mediante API, la interfaz que permite integrar el modelo en aplicaciones y servicios propios. La compañía indicó que más de 3.000 empresas utilizan actualmente sus modelos.

## Datos que faltan

Las cifras mencionadas, incluida la reducción de costos, las mejoras en programación y el número de clientes, provienen de la propia empresa. La información disponible no incluye resultados de pruebas comparativas independientes, precios concretos ni la lista de plataformas en la nube donde el modelo ya funciona. Tampoco aclara si habrá versiones abiertas para desarrolladores o si el servicio llegará a mercados de habla hispana.

## Un mercado en plena competencia

El lanzamiento se produce en un sector donde las empresas tecnológicas compiten por ofrecer modelos con más memoria de contexto, menores costos y mejor desempeño en tareas de programación y automatización. Zhipu AI, con sede en Pekín, es una de las compañías chinas que desarrollan modelos de lenguaje propios para uso empresarial.

Habrá que ver si las mejoras anunciadas se confirman en evaluaciones externas y en el uso real, que serán las que determinen el peso de GLM-5.2 frente a sus competidores.