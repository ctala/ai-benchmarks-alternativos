# Claude Opus 5 — integridad_idioma/fuente_china_sin_avisar

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.85 | quality: 9.61
- latency_total: 28.966s | tokens_per_second: 62.9
- input_tokens: 333 | output_tokens: 1822

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

La empresa china Beijing Zhipu Huazhang Technology, conocida comercialmente como Zhipu AI, presentó GLM-5.2, la nueva versión de su modelo de lenguaje de gran escala. El anuncio más llamativo es la ampliación de la ventana de contexto: pasa de 200.000 a un millón de tokens, cinco veces más que la generación anterior.

La compañía también afirma que el costo de inferencia —es decir, lo que cuesta ejecutar el modelo cada vez que responde una consulta— cayó cerca de 40 % respecto de la versión previa. Según Zhipu, GLM-5.2 muestra además mejoras significativas en generación de código y en el llamado a herramientas externas.

El modelo ya está disponible en varias plataformas de nube y se ofrece mediante servicios de API dirigidos a clientes corporativos. La empresa sostiene que más de 3.000 compañías utilizan actualmente sus servicios de modelos.

**¿Qué significa "un millón de tokens"?**

Los tokens son las unidades mínimas en que un modelo de lenguaje divide el texto: pueden ser palabras completas, fragmentos de palabras o signos de puntuación. La ventana de contexto es la cantidad de tokens que el sistema puede tener "a la vista" al mismo tiempo, sumando la instrucción del usuario, los documentos adjuntos y la propia respuesta.

Como referencia aproximada, un millón de tokens equivale a varios miles de páginas de texto. En la práctica, eso permite cargar de una sola vez expedientes legales completos, manuales técnicos extensos o repositorios de código enteros, sin necesidad de partirlos en fragmentos y volver a explicarle el contexto al modelo en cada paso. Para las empresas, esa diferencia suele traducirse en menos ingeniería de por medio y menos errores acumulados.

La mención al "llamado a herramientas" (*tool calling*) apunta en la misma dirección. Se trata de la capacidad del modelo para invocar programas externos: consultar una base de datos, ejecutar un script, buscar información en la web o completar un formulario. Es la pieza técnica sobre la que se construyen los llamados agentes de inteligencia artificial, sistemas que no solo responden preguntas, sino que ejecutan tareas de varios pasos. Junto con la generación de código, es una de las áreas donde hoy se concentra la competencia entre desarrolladores de modelos.

**Costos y clientes corporativos**

La reducción de costos de inferencia es un dato relevante para el mercado empresarial, donde el gasto no está en entrenar el modelo sino en usarlo miles o millones de veces al día. Una baja de 40 % modifica los cálculos de viabilidad de proyectos que hasta ahora resultaban demasiado caros para operar a escala.

Zhipu AI es uno de los desarrolladores chinos más visibles en el segmento de modelos de lenguaje y su familia GLM compite tanto con laboratorios locales como con las propuestas estadounidenses. La estrategia de distribución vía múltiples plataformas de nube busca precisamente facilitar la adopción en entornos corporativos, donde las empresas ya tienen contratos e infraestructura con determinados proveedores.

Conviene señalar que las cifras de mejora en código, uso de herramientas y reducción de costos provienen de la propia compañía y no de evaluaciones independientes. En un sector donde los anuncios de nuevos modelos se suceden con semanas de diferencia, las comparaciones hechas por terceros y el desempeño en usos reales suelen tardar algo más en aparecer. Por ahora, la apuesta de Zhipu es clara: contextos más largos, ejecución más barata y modelos capaces de operar herramientas por su cuenta.