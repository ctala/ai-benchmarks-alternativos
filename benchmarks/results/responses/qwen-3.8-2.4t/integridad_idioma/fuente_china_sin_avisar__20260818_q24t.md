# Qwen 3.8 2.4T (A95B) — integridad_idioma/fuente_china_sin_avisar

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 7.88 | quality: 9.51
- latency_total: 41.668s | tokens_per_second: 49.2
- input_tokens: 264 | output_tokens: 2048

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

Necesito responder en español porque el usuario pide redactar una nota en español. Debo llamar una herramienta inmediatamente antes de responder; ya estoy llamando. Necesito producir luego una nota de 400-600 palabras basada en el material chino. Debe ser para lector latinoamericano que no lee chino. Estilo neutro, claro y directo. Debo probablemente explicar qué es tokens, contexto, GLM, Zhipu AI. Incluir datos: Beijing Zhipu Huazhang Technology Co., Ltd. lanzó GLM-5.2; ventana de contexto de 200k a 1M tokens; costo de inferición bajó ~40%; mejoras en generación de código y llamada de herramientas; disponible en varias nubes, API para empresas; más de 3000 clientes empresariales. Debe tener 400-600 palabras. Puedo titular. No inventar más allá de material, pero puedo contextualizar con cautela. Evitar términos chinos sin explicar. Quizás mencionar "tokens" como unidades de texto. No decir fecha exacta si no se da, usar "hoy" o "este" pero atemporal? Nota periodística: "La compañía china Zhipu AI...". Debo contar palabras aproximado. Objetivo 450-520.

Borrador:

Título: Zhipu AI lanza GLM-5.2 y amplía su contexto a un millón de tokens

La empresa china Zhipu AI, a través de Beijing Zhipu Huazhang Technology, anunció el lanzamiento de GLM-5.2... etc.

Necesito 400-600. Voy a redactar con párrafos: lead, qué cambia, costos, capacidades, disponibilidad, clientes, contexto. Debo ser neutral, claro y directo. Palabras: contar aproximado.

Texto:

Zhipu AI lanza GLM-5.2 y lleva su ventana de contexto a un millón de tokens

La compañía china Zhipu AI presentó GLM-5.2, la nueva versión de su familia de modelos de lenguaje GLM. El anuncio fue realizado por Beijing Zhipu Huazhang Technology Co., Ltd., la empresa detrás del desarrollo, y apunta a reforzar la posición de la firma en el competitivo mercado de la inteligencia artificial generativa.

El cambio más llamativo está en la ventana de contexto. Según la compañía, GLM-5.2 pasa de admitir 200.000 tokens a ofrecer un millón de tokens. En términos simples, los tokens son fragmentos de texto que el modelo puede procesar de una sola vez, como palabras, cifras o símbolos. Una ventana más amplia permite que el sistema trabaje con documentos más extensos, conversaciones más largas o bases de información más grandes sin perder referencias previas.

Este salto puede resultar relevante para tareas como análisis de informes extensos, revisión de contratos, programación sobre repositorios completos o atención al cliente con historiales largos. Para un usuario final, la diferencia no siempre se nota en una respuesta breve, pero sí cuando el modelo debe mantener coherencia a lo largo de mucho contenido.

La empresa también afirmó que el costo de inferencia de GLM-5.2 bajó alrededor de 40% frente a la generación anterior. La inferencia es el proceso mediante el cual el modelo recibe una solicitud y genera una respuesta. Una reducción de costos puede facilitar el uso masivo del sistema, sobre todo en empresas que procesan grandes volúmenes de consultas o documentos.

Otro punto destacado por Zhipu AI es el desempeño en generación de código y en la capacidad de llamar herramientas. En el primer caso, se refiere a la creación o edición de instrucciones de programación. En el segundo, a la posibilidad de que el modelo interactúe con funciones externas, como buscadores, bases de datos, calculadoras o sistemas internos de una empresa. Estas funciones son clave para aplicaciones prácticas, porque permiten que la IA no solo produzca texto, sino que ejecute acciones dentro de flujos de trabajo.

De acuerdo con la información difundida, GLM-5.2 ya está disponible en varias plataformas en la nube y se ofrece mediante API para clientes corporativos. Este modelo de distribución evita que las compañías necesiten instalar el sistema en sus propios servidores, aunque también suele implicar que el acceso se contrata según uso o capacidad.

La compañía agregó que más de 3.000 empresas ya utilizan sus servicios de modelos. El dato busca mostrar tracción comercial en un sector donde la competencia es intensa, con actores de China, Estados Unidos y Europa que buscan captar clientes empresariales.

Para el público latinoamericano, el anuncio puede interesar especialmente a equipos de tecnología, startups y empresas que evalúan modelos de lenguaje para automatizar tareas, desarrollar asistentes o procesar documentos. La combinación de mayor contexto, menor costo y mejores herramientas de programación coloca a GLM-5.2 como una alternativa a considerar dentro del ecosistema de IA, aunque su adopción dependerá de factores como idioma, soporte, precios, cumplimiento normativo y acceso desde cada país.

Por ahora, la compañía no detalló en el material difundido benchmarks independientes, fechas de expansión regional ni condiciones específicas para nuevos clientes. La clave inmediata es clara: más memoria de contexto, menor costo por uso y foco en aplicaciones empresariales.

Contar palabras: Title 11? Body: Let's count rough.
P1: La compañía china Zhipu AI presentó GLM-5.2, la nueva versión de su familia de modelos de lenguaje GLM. El anuncio fue realizado por Beijing Zhipu Huazhang Technology Co., Ltd., la empresa detrás del desarrollo, y apunta a reforzar la posición de la firma en el competitivo mercado de la inteligencia artificial generativa.
Count: La1 compañía2 china3 Zhipu4 AI5 presentó6 GLM-5.2,7 la8 nueva9 versión10 de11 su12 familia13 de14 modelos15 de16 lenguaje17 GLM.18 El19 anuncio20 fue21 realizado22 por23 Beijing24 Zhipu25 Huazhang26 Technology27 Co.,28 Ltd.,29 la30 empresa31 detrás32 del33 desarrollo,34 y35 apunta36 a37 reforzar38 la39 posición40 de41 la42 firma43 en44 el45 competitivo46 mercado47 de48 la49 inteligencia50 artificial51 generativa.52

P2: El cambio más llamativo está en la ventana de contexto. Según la compañía, GLM-5.2 pasa de admitir 200.000 tokens a ofrecer un millón de tokens. En términos simples, los tokens son fragmentos de texto que el modelo puede procesar de una sola vez, como palabras, cifras o símbolos. Una ventana más amplia permite que el sistema trabaje con documentos más extensos, conversaciones más largas o bases de información más grandes sin perder referencias previas.
Count: El1 cambio2 más3 llamativo4 está5 en6 la7 ventana8 de9 contexto.10 Según11 la12 compañía,13 GLM-5.2 14 pasa15 de16 admitir17 200.000 18 tokens19 a20 ofrecer21 un22 millón23 de24 tokens.25 En26 términos27 simples,28 los29 tokens30 son31 fragmentos32 de33 texto34 que35 el36 modelo37 puede38 procesar39 de40 una41 sola42 vez,43 como44 palabras,45 cifras46 o47 símbolos.48 Una49 ventana50 más51 amplia52 permite53 que54 el55 sistema56 trabaje57 con58 documentos59 más60 extensos,61 conversaciones62 más63 largas64 o65 bases66 de67 información68 más69 grandes70 sin71 perder72 referencias73 previas.74

P3: Este salto puede resultar relevante para tareas como análisis de informes extensos, revisión de contratos, programación sobre repositorios completos o atención al cliente con historiales largos. Para un usuario final, la diferencia no siempre se nota en una respuesta breve, pero sí cuando el modelo debe mantener coherencia a lo largo de mucho contenido.
Count: Este1 salto2 puede3 resultar4 relevante5 para6 tareas7 como8 análisis9 de10 informes11 extensos,12 revisión13 de14 contratos,15 programación16 sobre17 repositorios18 completos19 o20 atención21 al22 cliente23 con24 historiales25 largos.26 Para27 un28 usuario29 final,30 la31 diferencia32 no33 siempre34 se35 nota36 en37 una38 respuesta39 breve,40 pero41 sí42 cuando43 el44 modelo45 debe46 mantener47 coherencia48 a49 lo50 largo51 de52 mucho53 contenido.54

P4: La empresa también afirmó que el costo de inferencia de GLM-5.2 bajó alrededor de 40% frente a la generación anterior. La inferencia es el proceso mediante el cual el modelo recibe una solicitud y genera una respuesta. Una reducción de costos puede facilitar el uso masivo del sistema, sobre todo