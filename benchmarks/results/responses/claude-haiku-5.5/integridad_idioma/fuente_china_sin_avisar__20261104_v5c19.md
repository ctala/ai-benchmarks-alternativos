# Claude Haiku 5.5 — integridad_idioma/fuente_china_sin_avisar

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.98 | quality: 9.41
- latency_total: 4.688s | tokens_per_second: 195.6
- input_tokens: 334 | output_tokens: 917

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

**Zhipu AI lanza GLM-5.2 con ventana de contexto de hasta 1 millón de tokens**

La empresa china Zhipu AI, con sede en Pekín, presentó GLM-5.2, la más reciente versión de su modelo de lenguaje de gran escala. El anuncio destaca dos mejoras principales: una ventana de contexto mucho más amplia y una reducción de costos de inferencia.

Según la compañía, la ventana de contexto pasó de 200.000 a 1 millón de tokens. En términos prácticos, la capacidad de contexto determina cuánta información puede procesar el modelo en una sola consulta, como documentos extensos, bases de código completas o conversaciones prolongadas. Un token equivale aproximadamente a una fracción de palabra, por lo que una ventana de un millón permite trabajar con volúmenes de texto considerablemente grandes.

Al mismo tiempo, Zhipu AI informó que el costo de inferencia, es decir, el gasto que implica ejecutar el modelo para responder consultas, se redujo alrededor de un 40% respecto a la generación anterior. Para las empresas que usan estos servicios a gran escala, este tipo de ajuste puede ser determinante a la hora de decidir qué tecnología adoptar.

La compañía también señala avances en dos áreas específicas: la generación de código y la llamada a herramientas externas. La llamada a herramientas, o *tool use*, permite que el modelo interactúe con aplicaciones, bases de datos o servicios de terceros para completar tareas, algo cada vez más valorado en los proyectos de automatización empresarial. Sin embargo, la empresa no detalló en el anuncio métricas comparativas independientes que respalden la magnitud de estas mejoras.

GLM-5.2 ya está disponible en varias plataformas de computación en la nube y se ofrece a clientes corporativos mediante una API, una interfaz que permite a los desarrolladores integrar el modelo en sus propios sistemas. De acuerdo con Zhipu AI, más de 3.000 empresas ya utilizan sus servicios de modelos.

El lanzamiento se inscribe en una carrera global por ofrecer modelos más potentes y accesibles, en la que compiten tanto empresas estadounidenses como chinas. Para los lectores de América Latina y España, el desarrollo es relevante porque amplía las opciones disponibles para empresas y desarrolladores de la región que buscan incorporar inteligencia artificial en sus operaciones. Aun así, conviene esperar evaluaciones independientes antes de dar por confirmado el alcance real de las mejoras anunciadas.