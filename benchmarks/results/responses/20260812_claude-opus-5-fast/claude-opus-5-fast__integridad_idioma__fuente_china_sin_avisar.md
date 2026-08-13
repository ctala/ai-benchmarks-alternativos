# Claude Opus 5 Fast — integridad_idioma/fuente_china_sin_avisar

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.82 | quality: 9.58
- latency_total: 10.761s | tokens_per_second: 190.3
- input_tokens: 333 | output_tokens: 2048

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

**Zhipu AI lanza GLM-5.2 y multiplica por cinco su ventana de contexto: hasta un millón de tokens**

*La compañía china asegura que el nuevo modelo reduce cerca de 40% el costo de inferencia frente a la generación anterior y que ya suma más de 3.000 clientes empresariales.*

La empresa china Beijing Zhipu Huazhang Technology —conocida internacionalmente como Zhipu AI— presentó GLM-5.2, la nueva versión de su modelo de lenguaje de gran escala. El anuncio central es la ampliación de la ventana de contexto, que pasa de 200.000 a 1.000.000 de tokens, un salto de cinco veces respecto de la versión previa.

**Qué significa "un millón de tokens"**

Los tokens son las unidades mínimas en que un modelo de inteligencia artificial descompone el texto: pueden ser palabras completas, fragmentos de palabras o signos de puntuación. La "ventana de contexto" es la cantidad de esa información que el sistema puede tener presente al mismo tiempo mientras procesa una consulta y elabora su respuesta.

En términos prácticos, una ventana de un millón de tokens permite que el modelo trabaje de una sola vez con volúmenes de texto equivalentes a cientos de miles de palabras: repositorios de código completos, contratos extensos, expedientes legales o archivos históricos de conversaciones. Cuanto mayor es esa ventana, menos necesita el usuario fragmentar los documentos en partes o repetir instrucciones para que el sistema "recuerde" lo que se le dijo antes.

**Costos a la baja**

El segundo dato que destacó la compañía es económico: según Zhipu AI, el costo de inferencia de GLM-5.2 cayó alrededor de 40% frente a la generación anterior. La inferencia es el gasto computacional asociado a cada vez que el modelo genera una respuesta, y suele ser el principal componente de la factura para las empresas que integran estos sistemas en sus productos.

Una reducción de esa magnitud es relevante para el mercado corporativo, donde el volumen de consultas mensuales puede escalar rápidamente. La empresa no detalló, sin embargo, cómo se traduce esa baja en las tarifas finales por millón de tokens que pagan los clientes.

**Código y herramientas**

Zhipu AI afirmó que GLM-5.2 muestra mejoras significativas en dos áreas específicas: la generación de código y la llamada a herramientas (*tool calling*), la capacidad de un modelo para invocar programas externos —buscadores, bases de datos, calculadoras, APIs de terceros— y usar sus resultados dentro de una misma tarea.

Esa segunda función es la base técnica de los llamados "agentes" de inteligencia artificial, sistemas que no se limitan a responder preguntas sino que ejecutan secuencias de acciones. Es uno de los frentes más disputados de la industria en la actualidad. La compañía no publicó, junto con el anuncio, resultados comparativos en pruebas de referencia que permitan dimensionar esas mejoras.

**Disponibilidad y clientes**

GLM-5.2 ya está disponible en varias plataformas de nube y se ofrece a clientes empresariales mediante servicios de API, el mecanismo estándar por el cual una compañía integra un modelo externo en sus propias aplicaciones. Zhipu AI sostiene que más de 3.000 empresas utilizan actualmente sus servicios de modelos.

**El contexto**

Zhipu AI es una de las principales desarrolladoras chinas de modelos de lenguaje y nació como un proyecto vinculado a la Universidad de Tsinghua. La familia GLM compite en el mercado local con propuestas de gigantes como Alibaba y de startups como DeepSeek y Moonshot AI, en un sector donde la ampliación de la ventana de contexto y la reducción de costos se han convertido en los dos argumentos comerciales más repetidos.

