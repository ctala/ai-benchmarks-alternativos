# Tencent Hy4 — noticias_redaccion/ley_ia_europea

- model_id: `tencent/hy4`
- success: True  | final: 7.44 | quality: 8.5
- latency_total: 99.707s | tokens_per_second: 120.4
- input_tokens: 957 | output_tokens: 12006

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor de contenido para un founder hispanohablante que publica noticias y análisis para emprendedores de América Latina y España. Escribes en español neutro, claro y directo, con subtítulos en Markdown (##).

**user:**

Es para el blog de una startup latinoamericana de software que vende a clientes en España.

Escribe la nota en español neutro, de 900 a 1.300 palabras, solo con datos de la fuente.

FUENTE:
El Reglamento de Inteligencia Artificial de la Unión Europea, conocido como Ley de IA, entró en vigor el 1 de agosto. Es la primera norma integral sobre inteligencia artificial aprobada por una gran economía y se aplicará por etapas a lo largo de los próximos años.

La ley clasifica los sistemas de IA según su nivel de riesgo. Los de riesgo inaceptable quedan prohibidos: por ejemplo, los sistemas de puntuación social de personas o ciertos usos de reconocimiento de emociones en el trabajo y en la escuela. Los de alto riesgo, como los que se usan para seleccionar personal, otorgar créditos o en infraestructura crítica, deberán cumplir requisitos de calidad de datos, documentación, supervisión humana y ciberseguridad.

Para los sistemas de riesgo limitado, como los asistentes conversacionales, la principal obligación es de transparencia: la persona debe saber que está interactuando con una máquina. Los contenidos generados o manipulados con IA, como las imágenes o videos falsos de personas reales, deberán identificarse como tales.

La norma también incluye reglas específicas para los modelos de IA de uso general, que son la base de muchos productos actuales.

Esas obligaciones incluyen preparar documentación técnica, informar sobre los datos usados en el entrenamiento y respetar las normas europeas de derechos de autor. Los modelos considerados de riesgo sistémico, por su capacidad y su alcance, tendrán obligaciones adicionales de evaluación y mitigación de riesgos.

El texto fue propuesto por la Comisión Europea y pasó por una larga negociación entre la Comisión, el Parlamento Europeo y el Consejo, que reúne a los gobiernos de los Estados miembros. Durante ese proceso, la aparición de asistentes conversacionales de uso masivo llevó a los legisladores a incorporar las reglas para los modelos de uso general, que no figuraban en la propuesta original.

Las empresas tecnológicas y algunas asociaciones de startups advirtieron durante la negociación que reglas demasiado estrictas podían frenar la innovación en Europa y favorecer a los competidores de otras regiones. Los defensores de la norma sostienen que unas reglas claras dan seguridad jurídica a las empresas y generan confianza en los usuarios.

Cada Estado miembro debe designar autoridades nacionales encargadas de vigilar el cumplimiento. En España se creó la Agencia Española de Supervisión de la Inteligencia Artificial, con sede en A Coruña.

Las sanciones pueden ser altas. Para las prácticas prohibidas, las multas pueden llegar a 35 millones de euros o al 7% del volumen de negocio anual mundial de la empresa, la cifra que resulte mayor.

La ley se aplica a las empresas que ofrecen sistemas de IA en el mercado europeo, aunque estén fuera de la Unión. Eso incluye a startups latinoamericanas que venden software con funciones de IA a clientes en España o en otros países europeos.

Para una startup que vende software, el primer paso práctico es identificar en qué categoría de riesgo cae cada uno de sus productos, porque de eso dependen las obligaciones. Un asistente de atención al cliente no exige lo mismo que una herramienta que filtra candidatos para un puesto de trabajo.

La Comisión Europea creó una Oficina de IA para supervisar la aplicación de la norma y prevé espacios controlados de pruebas para que las pymes y startups puedan probar sus sistemas con acompañamiento de las autoridades.


## Respuesta completa

## La Ley de IA de la Unión Europea ya está en vigor: qué cambia para las startups latinoamericanas que venden en España

El Reglamento de Inteligencia Artificial de la Unión Europea, conocido como Ley de IA, entró en vigor el 1 de agosto. No es un borrador en consulta ni una actualización menor: es la primera norma integral sobre inteligencia artificial aprobada por una gran economía. Para quienes construimos software desde América Latina y tenemos clientes al otro lado del Atlántico, el titular deja de ser una noticia regulatoria lejana y pasa a formar parte del trabajo diario del equipo de producto.

La aplicación no llegará toda de una vez. La ley se aplicará por etapas a lo largo de los próximos años. Sin embargo, la fecha del 1 de agosto ya fija el punto de partida. A partir de ese momento, el marco existe, las categorías están definidas y las autoridades empiezan a organizarse. Esperar a que avance cada etapa para leer el texto es un error de cálculo: la clasificación de lo que hoy ya se ofrece en el mercado debe hacerse con el texto que entró en vigor.

## El alcance no se detiene en las fronteras europeas

Uno de los puntos que más nos importa en este blog es el alcance. La ley se aplica a las empresas que ofrecen sistemas de IA en el mercado europeo, aunque estén fuera de la Unión. La fuente es explícita y nos incluye: eso comprende a startups latinoamericanas que venden software con funciones de IA a clientes en España o en otros países europeos.

El criterio que menciona el texto es ofrecer el sistema en el mercado europeo, y la propia norma aclara que esto aplica aunque la empresa esté fuera de la Unión. Si el cliente está en España, el software que se le entrega entra en el mapa de obligaciones. La función de IA que se ofrece a un cliente español pasa a leerse también desde la categoría de riesgo que le corresponde dentro del Reglamento. Para una startup de la región, la conversación sobre cumplimiento no se delega al socio europeo: empieza en el propio roadmap.

## El primer paso práctico: clasificar cada producto

Para una startup que vende software, el primer paso práctico es identificar en qué categoría de riesgo cae cada uno de sus productos. La frase parece simple, pero es el eje de todo: de eso dependen las obligaciones.

La ley clasifica los sistemas de IA según su nivel de riesgo. No trata igual a todos los módulos de una misma plataforma. Un asistente de atención al cliente no exige lo mismo que una herramienta que filtra candidatos para un puesto de trabajo. Por eso el trabajo inicial no es una declaración general de la empresa, sino un inventario producto por producto, función por función. El equipo debe sentarse frente a lo que ya está desplegado y preguntarse, en cada caso, en qué escalón de la clasificación se sitúa. Solo después de esa respuesta se puede saber si aplica una prohibición, un paquete de requisitos, una obligación de transparencia o las reglas específicas de los modelos de uso general.

## Riesgo inaceptable: la línea de lo prohibido

En el extremo superior de la clasificación están los sistemas de riesgo inaceptable. Estos quedan prohibidos. La norma no les impone condiciones de operación ni les pide documentación adicional: directamente los saca del mercado europeo.

La fuente menciona dos ejemplos concretos. El primero son los sistemas de puntuación social de personas. El segundo son ciertos usos de reconocimiento de emociones en el trabajo y en la escuela. La precisión importa: el texto habla de «ciertos usos» y de dos ámbitos específicos, el laboral y el educativo. Para una startup que esté revisando funcionalidades ligadas a esos ámbitos, este es el primer filtro que debe aplicar al identificar en qué categoría de riesgo cae el producto. Si el sistema se ubica aquí, no hay ruta de adecuación descrita en la norma: la condición es que queda prohibido.

## Alto riesgo: cuatro frentes de exigencia

Un escalón más abajo aparecen los sistemas de alto riesgo. La fuente los ilustra con tres casos: los que se usan para seleccionar personal, los que se usan para otorgar créditos y los que operan en infraestructura crítica. Volvemos al ejemplo del principio: la herramienta que filtra candidatos para un puesto de trabajo pertenece a este grupo, y por eso no se parece en nada al asistente de atención al cliente.

Estos sistemas deberán cumplir requisitos de calidad de datos, documentación, supervisión humana y ciberseguridad. Son cuatro exigencias distintas que se acumulan. El texto las enumera como requisitos que se deberán cumplir, no como recomendaciones opcionales. La calidad de datos es un frente. La documentación es otro. La supervisión humana es otro. La ciberseguridad es otro. Cada uno pasa a formar parte del paquete que el sistema tiene que atender.

Para un equipo pequeño, la lectura operativa es que el cumplimiento no se agota en una sola acción: se deben atender los cuatro puntos enumerados y sostenerlos frente a las autoridades nacionales encargadas de vigilar el cumplimiento, de las que hablaremos más adelante. Cuando el producto cae en esta categoría, la lista de tareas del equipo de ingeniería y del equipo legal se amplía de forma concreta.

## Riesgo limitado: transparencia y etiquetado

Después están los sistemas de riesgo limitado. Aquí la fuente sitúa a los asistentes conversacionales, que son, justamente, el caso del asistente de atención al cliente mencionado como punto de partida del inventario.

Para este nivel, la principal obligación es de transparencia: la persona debe saber que está interactuando con una máquina. No se pide aquí el paquete de calidad de datos, documentación, supervisión humana y ciberseguridad que sí se exige en alto riesgo; se pide que el usuario reciba esa información. La obligación se dirige a lo que la persona debe saber, y el sistema tiene que garantizarlo.

La misma lógica se extiende a los contenidos. Los contenidos generados o manipulados con IA, como las imágenes o videos falsos de personas reales, deberán identificarse como tales. La regla no se limita a la conversación del asistente: alcanza también a piezas visuales. Si el producto entrega una imagen o un video de ese tipo, tiene que señalar su condición. De nuevo, el criterio es informar a la persona que está del otro lado, tal como lo formula la norma para los sistemas de riesgo limitado.

## Modelos de uso general y riesgo sistémico

La norma también incluye reglas específicas para los modelos de IA de uso general, que son la base de muchos productos actuales. Este bloque merece atención propia, porque no depende únicamente de la aplicación final que ve el cliente, sino del modelo sobre el que se construye el software.

Esas obligaciones incluyen preparar documentación técnica, informar sobre los datos usados en el entrenamiento y respetar las normas europeas de derechos de autor. Son tres capas que el texto enumera: la documentación técnica, la información sobre los datos de entrenamiento y el respeto a las normas europeas de derechos de autor. Para una startup que integra o desarrolla sobre estos modelos, esos son los tres puntos que deben quedar cubiertos.

Hay además un subgrupo dentro de este bloque. Los modelos considerados de riesgo sistémico, por su capacidad y su alcance, tendrán obligaciones adicionales de evaluación y mitigación de riesgos. El criterio para distinguirlos lo dan dos dimensiones que menciona la fuente: la capacidad y el alcance. Cuando el modelo entra en esa categoría, a la documentación técnica, a la información sobre los datos usados en el entrenamiento y a las normas europeas de derechos de autor se les suman la evaluación de riesgos y la mitigación de esos riesgos. El texto las define como obligaciones adicionales, no como un reemplazo de las anteriores.

## Una ley que cambió mientras se negociaba

El texto fue propuesto por la Comisión Europea y pasó por una larga negociación entre la Comisión, el Parlamento Europeo y el Consejo, que reúne a los gobiernos de los Estados miembros. El recorrido involucró a las tres instituciones y, a través del Consejo, a los gobiernos nacionales. No fue un trámite corto: la fuente lo describe como una larga negociación.

Durante ese proceso ocurrió algo que explica por qué existe el bloque anterior. La aparición de asistentes conversacionales de uso masivo llevó a los legisladores a incorporar las reglas para los modelos de uso general, que no figuraban en la propuesta original. La norma se modificó durante ese mismo proceso a partir de ese cambio tecnológico. Las reglas sobre documentación técnica, datos de entrenamiento, derechos de autor y riesgo sistémico no estaban en el punto de partida y quedaron incorporadas en el texto que finalmente entró en vigor el 1 de agosto. Para quienes emprendemos en software, el dato es concreto: el marco que se aplicará por etapas es distinto del que se propuso al inicio.

## El debate: innovación frente a seguridad jurídica

La negociación también dejó dos posturas enfrentadas que conviene conocer, porque siguen presentes en cómo se lee la ley desde el ecosistema emprendedor.

Las empresas tecnológicas y algunas asociaciones de startups advirtieron durante la negociación que reglas demasiado estrictas podían frenar la innovación en Europa y favorecer a los competidores de otras regiones. Es una advertencia que nos toca de cerca: una startup latinoamericana es, literalmente, un competidor de otra región, pero que en este caso vende dentro del mercado europeo y por eso queda alcanzada por las mismas reglas, según el alcance que ya revisamos.

Del otro lado, los defensores de la norma sostienen que unas reglas claras dan seguridad jurídica a las empresas y generan confianza en los usuarios. La fuente recoge las dos posiciones: la advertencia sobre el freno a la innovación y la defensa de la seguridad jurídica y la confianza. Para un founder, la seguridad jurídica se traduce en saber de antemano qué se espera de cada categoría de riesgo, y la confianza del usuario se conecta directamente con la transparencia exigida a los asistentes conversacionales y a los contenidos generados o manipulados con IA.

## Quién vigila: A Coruña, los Estados miembros y la Oficina de IA

El cumplimiento no depende de una sola oficina. Cada Estado miembro debe designar autoridades nacionales encargadas de vigilar el cumplimiento. En España se creó la Agencia Española de Supervisión de la Inteligencia Artificial, con sede en A Coruña. Para nuestros clientes españoles —y para nosotros, que les vendemos software con funciones de IA— ese es el nombre propio que aparece en el mapa local.

A nivel de la Unión, la Comisión Europea creó una Oficina de IA para supervisar la aplicación de la norma. Su rol se suma al de las autoridades nacionales: unas vigilan el cumplimiento en cada Estado miembro y la otra supervisa la aplicación del Reglamento. La misma Comisión que propuso el texto y participó en la negociación queda ahora a cargo de esa supervisión.

La Comisión Europea prevé además espacios controlados de pruebas para que las pymes y startups puedan probar sus sistemas con acompañamiento de las autoridades. Este punto es especialmente relevante para nuestro tamaño. La fuente lo vincula expresamente a pymes y startups y lo describe como un esquema para probar sistemas con acompañamiento. No aparece en el texto como una exención de las obligaciones, sino como una previsión dentro de la aplicación de la norma, junto a la supervisión de la Oficina de IA y de las autoridades nacionales.

## Las sanciones: la cifra que resulte mayor

El cierre del esquema es económico, y las cifras no son simbólicas. Las sanciones pueden ser altas. Para las prácticas prohibidas —las de riesgo inaceptable, como los sistemas de puntuación social de personas o ciertos usos de reconocimiento de emociones en el trabajo y en la escuela—, las multas pueden llegar a 35 millones de euros o al 7% del volumen de negocio anual mundial de la empresa, la cifra que resulte mayor.

Conviene leer la fórmula con calma. El texto habla del volumen de negocio anual mundial y especifica que se aplica la cifra que resulte mayor entre el monto en euros y ese porcentaje. Para una startup que vende a clientes en España desde Latinoamérica, el cálculo toma el negocio anual mundial de la empresa, no solo el contrato europeo. Es el recordatorio más contundente de que la clasificación inicial define qué obligaciones aplican y qué exposición se asume ante el régimen de sanciones.

## Lo que se lleva el equipo de producto

Volvemos al punto de partida. El Reglamento de Inteligencia Artificial de la Unión Europea entró en vigor el 1 de agosto, es la primera norma integral sobre inteligencia artificial aprobada por una gran economía y se aplicará por etapas a lo largo de los próximos años. Alcanza a las empresas que ofrecen sistemas de IA en el mercado europeo, aunque estén fuera de la Unión, y eso incluye a startups latinoamericanas que venden software con funciones de IA a clientes en España o en otros países europeos.

El primer paso práctico sigue siendo el mismo: identificar en qué categoría de riesgo cae cada uno de sus productos, porque de eso dependen las obligaciones. Un asistente de atención al cliente, como asistente conversacional de riesgo limitado, pide transparencia para que la persona sepa que interactúa con una máquina, y pide identificar los contenidos generados o manipulados con IA. Una herramienta que filtra candidatos para un puesto de trabajo, como sistema de alto riesgo, pide calidad de datos, documentación, supervisión humana y ciberseguridad. Un modelo de uso general pide documentación técnica, información sobre los datos usados en el entrenamiento y respeto a las normas europeas de derechos de autor. Un modelo de riesgo sistémico suma evaluación y mitigación de riesgos por su capacidad y su alcance. Y los sistemas de riesgo inaceptable quedan prohibidos.

Con ese inventario hecho, el resto del mapa ya tiene nombres: las autoridades nacionales de cada Estado miembro, la Agencia Española de Supervisión de la Inteligencia Artificial con sede en A Coruña, la Oficina de IA de la Comisión Europea y los espacios controlados de pruebas previstos para pymes y startups. La norma se propuso desde la Comisión, se negoció con el Parlamento Europeo y el Consejo, incorporó en el camino las reglas para modelos de uso general que no figuraban en la propuesta original y todavía se desplegará por etapas. Pero la tarea de hoy, para un equipo de software de la región con clientes en España, es mucho más concreta: abrir el listado de productos y escribir, al lado de cada uno, su nivel de riesgo.