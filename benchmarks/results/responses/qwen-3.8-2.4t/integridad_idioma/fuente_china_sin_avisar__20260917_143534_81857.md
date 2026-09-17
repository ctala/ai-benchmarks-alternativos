# Qwen 3.8 2.4T (A95B) — integridad_idioma/fuente_china_sin_avisar

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 7.86 | quality: 9.61
- latency_total: 68.825s | tokens_per_second: 49.0
- input_tokens: 264 | output_tokens: 3370

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

**Zhipu AI lanza GLM-5.2: contexto de un millón de tokens y menor costo**

La empresa china Beijing Zhipu Huazhang Technology, conocida como Zhipu AI, anunció el lanzamiento de GLM-5.2, una nueva versión de su modelo de lenguaje de gran escala. La principal novedad es la ampliación de su ventana de contexto: pasa de 200.000 a 1.000.000 de tokens. En términos simples, el sistema puede procesar y “recordar” una cantidad mucho mayor de información en una misma conversación o tarea, ya sea un documento extenso, un contrato largo, un informe técnico o una base de código completa.

El concepto de token es clave en este tipo de tecnologías. Un token puede equivaler a una palabra, una sílaba o un fragmento de texto, según el idioma y el formato. Cuanto mayor es la ventana de contexto, más contenido puede analizar el modelo sin necesidad de dividir el material en partes o perder referencias importantes. Para una empresa, esto puede traducirse en respuestas más coherentes al revisar archivos extensos o al mantener interacciones prolongadas.

Zhipu AI también informó que el costo de inferencia de GLM-5.2 se redujo alrededor de 40% frente a la generación anterior. La inferencia es el proceso mediante el cual el modelo recibe una solicitud y genera una respuesta. Este punto es relevante porque, en servicios de inteligencia artificial a gran escala, el precio por consulta o por volumen de procesamiento suele ser uno de los factores decisivos para adoptar una plataforma.

Según la compañía, GLM-5.2 muestra mejoras significativas en generación de código y en la capacidad de invocar herramientas externas. La generación de código se refiere a la creación o modificación de instrucciones de programación, mientras que la invocación de herramientas permite que el modelo se conecte con funciones externas, como buscadores, bases de datos, calculadoras o sistemas empresariales, para completar tareas más allá de simplemente producir texto.

El nuevo modelo ya está disponible en varias plataformas de nube y se ofrece a clientes empresariales mediante API, es decir, una interfaz de programación que permite integrar el modelo en aplicaciones, asistentes internos, sistemas de atención al cliente o herramientas de desarrollo. La compañía afirmó que más de 3.000 empresas ya utilizan sus servicios.

El anuncio llega en un momento de fuerte competencia en el sector de los modelos de lenguaje. Las empresas buscan no solo aumentar la calidad de las respuestas, sino también reducir costos, ampliar la memoria de contexto y facilitar la integración en flujos de trabajo reales. Para Zhipu AI, GLM-5.2 parece apuntar a ese triple objetivo: mayor capacidad de procesamiento, menor gasto operativo y más utilidad en tareas técnicas y empresariales.