# Tencent Hy4 preview — integridad_idioma/fuente_china_sin_avisar

- model_id: `tencent/hy4-preview`
- success: True  | final: 7.9 | quality: 9.56
- latency_total: 160.305s | tokens_per_second: 75.5
- input_tokens: 223 | output_tokens: 12110

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

**Zhipu AI lanza GLM-5.2 y eleva a un millón de tokens su ventana de contexto**

La empresa china presentó una nueva versión de su modelo de lenguaje, con un contexto más amplio, menor costo de inferencia y mejoras en programación y automatización. El servicio ya está disponible para clientes corporativos en varias nubes.

Beijing Zhipu Huazhang Technology Co., Ltd., conocida como Zhipu AI, anunció el lanzamiento de GLM-5.2, la evolución más reciente de su familia de modelos de lenguaje de gran escala. La principal novedad es la ampliación de la ventana de contexto, que pasó de 200.000 tokens a 1 millón de tokens. En la práctica, esto permite que el modelo reciba y procese en una sola interacción una cantidad de texto mucho mayor que antes: desde informes extensos y contratos hasta repositorios de código completos o conversaciones prolongadas sin perder el hilo.

Un token es la unidad básica en la que estos sistemas dividen el texto. Por eso, una ventana de un millón de tokens equivale, a grandes rasgos, a cientos de miles de palabras o a varios libros de considerable extensión. Para las empresas, la ventaja es clara: ya no es necesario fragmentar la información en múltiples consultas, lo que reduce errores y facilita tareas como el análisis de documentos legales, la revisión técnica o la atención al cliente con historial completo.

Además del salto en capacidad, la compañía informó una reducción aproximada del 40% en el costo de inferencia respecto de la generación anterior. La inferencia es el proceso mediante el cual el modelo genera una respuesta o realiza una tarea después de recibir una instrucción. Un menor costo por inferencia resulta clave para el uso corporativo, porque permite escalar aplicaciones de inteligencia artificial sin que los costos se disparen.

Zhipu AI también destacó avances concretos en dos frentes: la generación de código y la invocación de herramientas externas —conocida en inglés como *tool calling*—. La primera se refiere a la capacidad del modelo para escribir, corregir o explicar código en distintos lenguajes de programación. La segunda le permite activar software externo, APIs o funciones específicas para completar una tarea, un aspecto central para la automatización y la integración con sistemas empresariales.

El nuevo modelo ya está disponible en varias plataformas en la nube, que ofrecen acceso mediante API (interfaz de programación de aplicaciones) a clientes corporativos. Según la empresa, más de 3.000 compañías utilizan actualmente sus servicios de modelos de lenguaje. Aunque el anuncio se enmarca en la competitiva industria china de IA, la tendencia es relevante para el resto del mundo: ventanas de contexto más amplias y costos más bajos suelen traducirse en servicios de IA más potentes y accesibles, incluso para mercados como el latinoamericano.

Con GLM-5.2, Zhipu AI se suma a la carrera global por ofrecer modelos más capaces y eficientes. El desafío ahora será ver cómo responden los desarrolladores y las empresas ante una herramienta que promete procesar más información, con mayor velocidad y a un costo menor.