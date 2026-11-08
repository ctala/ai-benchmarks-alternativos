# Qwen 3.8 Max 0902 — integridad_idioma/fuente_china_sin_avisar

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.71 | quality: 9.49
- latency_total: 105.583s | tokens_per_second: 45.3
- input_tokens: 264 | output_tokens: 4788

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

*La empresa china informó que el nuevo modelo reduce el costo de inferencia y mejora la generación de código. Ya está disponible en plataformas en la nube para clientes corporativos.*

La compañía china Zhipu AI presentó GLM-5.2, una nueva versión de su modelo de lenguaje, con una ventana de contexto que pasa de 200 mil a un millón de tokens. El anuncio fue realizado por Beijing Zhipu Huazhang Technology, la empresa detrás de la familia de modelos GLM.

Para un usuario no especializado, la ventana de contexto es la cantidad de información que un modelo de inteligencia artificial puede “recordar” y procesar dentro de una misma interacción. Los tokens son unidades básicas de texto: pueden equivaler a una palabra completa o a parte de ella. Cuanto mayor es la ventana, más contenido puede analizar el sistema de una sola vez, como documentos largos, contratos, informes técnicos o fragmentos extensos de código. En la práctica, esto puede facilitar que una organización revise un expediente completo, un manual técnico o una base de código sin dividir el contenido en varias partes.

Según la compañía, GLM-5.2 también reduce el costo de inferencia en torno al 40 % respecto de la generación anterior. La inferencia es el proceso mediante el cual el modelo genera respuestas después de recibir una solicitud. Una baja en ese costo puede ser relevante para empresas que realizan grandes volúmenes de consultas, automatización de tareas o integración de IA en productos digitales.

Zhipu AI afirmó que el nuevo modelo muestra mejoras significativas en dos áreas clave: generación de código y llamada a herramientas. La primera se refiere a la capacidad de escribir, revisar o completar instrucciones de programación. La segunda, conocida en inglés como *tool calling*, permite que el modelo active funciones externas, como buscar datos, usar una calculadora, consultar una base de información o ejecutar acciones dentro de otro programa.

La empresa informó que GLM-5.2 ya está disponible en varias plataformas en la nube y que se ofrece a clientes corporativos a través de API, es decir, mediante una interfaz que permite integrar el modelo en aplicaciones, sitios web o sistemas internos. Este formato es habitual en servicios de inteligencia artificial dirigidos a compañías que no necesitan entrenar un modelo propio, sino incorporar capacidades ya desarrolladas.

De acuerdo con Zhipu AI, más de 3.000 empresas utilizan actualmente sus servicios de modelos. La cifra busca mostrar adopción empresarial en un mercado competitivo, donde los proveedores buscan diferenciarse por contexto más amplio, menores costos y mejor rendimiento en tareas prácticas.

Con GLM-5.2, la compañía apuesta por fortalecer su oferta para uso corporativo, especialmente en proyectos que requieren procesar grandes volúmenes de información y automatizar flujos de trabajo técnicos.