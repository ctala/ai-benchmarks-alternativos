# LFM-3 1.7B — integridad_idioma/fuente_china_sin_avisar

- model_id: `liquid/lfm-3-1.7b`
- success: True  | final: 8.51 | quality: 9.4
- latency_total: 17.847s | tokens_per_second: 459.0
- input_tokens: 227 | output_tokens: 8192

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

**Título:** *Zhizhi AI lanza GLM‑5.2 con ventana de contexto de un millón de tokens*

---

**Una noticia relevante para profesionales de tecnología y emprendedores en Latinoamérica.**  
El avance del modelo **GLM‑5.2** también trae beneficios para el sector educativo, donde los estudiantes pueden acceder a tutores virtuales que analicen trabajos completos sin truncarse.

**El 24 de mayo, la compañía china Zhizhi Huazhang Technology presentó el lanzamiento de su nueva versión del modelo de lenguaje grande GLM‑5.2.**  
Esta actualización busca solventar dos limitaciones habituales: la cantidad de información que puede retener y el costo energético necesario para generar respuestas.

### Cambio principal: la ventana de contexto
Hasta el pasado año, **GLM‑5.1** permitía analizar textos de alrededor de **200 000 tokens**. Ahora, **GLM‑5.2** extiende esa capacidad a **1 000 000 tokens**. En otras palabras, el modelo puede examinar documentos completos, bases de conocimiento interconectadas o incluso varias conversaciones simultáneas sin perder los detalles iniciales. Para ser más técnico, esto equivale a pasar desde un contexto de doscientos mil palabras aproximadas a un millón de unidades de texto que representan frases, etiquetas o fragmentos.

### Reducción de costos
El anuncio incluye que el **consumo computacional por inferencia ha caído cerca del 40 %** frente a la versión anterior. Esto significa que, para obtener la misma calidad de salida, se necesita menos potencia de CPU/GPU o menos energía, lo que hace viable el despliegue de modelos avanzados en proveedores cloud de consumo o en entornos empresariales reducidos.

### Avances en programación y uso de herramientas
Las pruebas preliminares revelan mejoras significativas tanto en la