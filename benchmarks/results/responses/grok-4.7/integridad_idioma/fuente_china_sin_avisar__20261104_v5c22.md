# Grok 4.7 — integridad_idioma/fuente_china_sin_avisar

- model_id: `x-ai/grok-4.7`
- success: True  | final: 8.05 | quality: 9.65
- latency_total: 25.217s | tokens_per_second: 41.5
- input_tokens: 1449 | output_tokens: 1046

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

**Zhipu AI lanza GLM-5.2 y amplía su ventana de contexto a un millón de tokens**

La empresa china Beijing Zhipu Huazhang Technology, conocida en el mercado como Zhipu AI, anunció este martes el lanzamiento de GLM-5.2, una nueva versión de su modelo de lenguaje de gran escala. El cambio más visible es el tamaño de la ventana de contexto: pasa de 200.000 a un millón de tokens, cinco veces más que la generación anterior.

Para un lector que no sigue de cerca el desarrollo de inteligencia artificial, conviene aclarar qué significa esa cifra. Un token es una unidad con la que el modelo lee y genera texto. No equivale exactamente a una palabra —en español, una palabra puede partirse en más de un token—, pero sirve como medida del volumen de información que el sistema puede tener presente en una sola interacción. Con un millón de tokens, el modelo puede trabajar sobre documentos mucho más extensos, conversaciones largas o conjuntos de archivos sin perder de vista el material inicial con tanta facilidad como en ventanas más cortas.

La compañía también informó que el costo de inferencia —es decir, el gasto de hacer funcionar el modelo cuando un usuario o una empresa le pide una respuesta— bajó cerca de un 40 % respecto de la generación previa. Zhipu AI no detalló en el anuncio cómo se calcula ese ahorro ni en qué escenarios se midió, pero lo presentó como uno de los argumentos centrales del nuevo producto.

Según la empresa, GLM-5.2 mejora de forma notable en dos tareas que interesan sobre todo al uso profesional: la generación de código y la llamada a herramientas. La primera se refiere a la capacidad de escribir o completar programas informáticos a partir de instrucciones. La segunda permite que el modelo no solo responda en texto, sino que active funciones externas —por ejemplo, consultar una base de datos o ejecutar una acción en un sistema— cuando la tarea lo requiere. El comunicado no incluyó pruebas públicas, comparaciones con otros modelos ni cifras que permitan medir el tamaño de esa mejora.

GLM-5.2 ya está disponible en varias plataformas de nube y se ofrece como servicio de API para clientes empresariales. Una API es una interfaz que permite a otras aplicaciones conectarse al modelo sin que la empresa tenga que instalarlo por su cuenta. Zhipu AI señaló que más de 3.000 empresas utilizan ya sus servicios de modelos. La cifra corresponde al conjunto de su oferta, no necesariamente a quienes hayan adoptado esta versión en particular, y la compañía no desglosó por país ni por sector.

El anuncio llega en un momento en que varios desarrolladores de modelos compiten por ofrecer contextos más largos y precios más bajos, dos factores que pesan en la decisión de una empresa al elegir un proveedor. Para organizaciones en México, Chile, Argentina, Colombia, España u otros mercados de habla hispana, el dato relevante no es solo la cifra de tokens, sino si el servicio está disponible en las nubes que ya usan, en qué idioma rinde mejor y cuánto cuesta en la práctica. Sobre esos puntos —precios concretos, idiomas soportados, límites de uso y condiciones contractuales— el material difundido por la compañía no aporta detalles.

Zhipu AI tiene su sede en Pekín y forma parte del grupo de empresas chinas que desarrollan modelos propios, en paralelo a los grandes laboratorios de Estados Unidos y de otros países. GLM-5.2 es la continuación de esa línea. Lo que se sabe por ahora cabe en pocos puntos: más contexto, menor costo de uso declarado y mejoras afirmadas en código y herramientas, con acceso vía nube y API para empresas. El resto —rendimiento real, comparación con alternativas y condiciones para clientes fuera de China— habrá que verificarlo cuando la compañía publique documentación técnica o cuando los primeros usuarios empresariales compartan resultados.