# Grok 4.7 — news_seo_writing/news_perplexity_enrichment

- model_id: `x-ai/grok-4.7`
- success: True  | final: 7.83 | quality: 9.6
- latency_total: 71.433s | tokens_per_second: 46.6
- input_tokens: 1719 | output_tokens: 3332
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, integrando efectivamente los datos adicionales con el extracto original, proporcionando insights útiles para emprendedores, aunque podría profundizar más en ciertos aspectos técnicos.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un periodista especializado en startups, tecnologia e innovacion en Latinoamerica.
Escribes para ecosistemastartup.com, un medio digital enfocado en el ecosistema emprendedor.

Reglas de redaccion:
- Escribes SIEMPRE en espanol, sin importar el idioma del input
- Tono: profesional pero accesible, informativo, con datos concretos
- Estructura: usa subtitulos H2 (## en markdown), nunca H1
- Incluye siempre una seccion "Que significa esto para tu startup"
- Cita fuentes verificables cuando menciones datos
- No inventes datos, cifras ni citas que no esten en el extracto proporcionado
- Termina con una conclusion que invite a la reflexion
- No uses cliches como "en la era digital", "revolucionario", "game changer"
- Incluye palabras clave SEO de forma natural, no forzada

**user:**

Escribe un articulo de 1,000 palabras integrando el EXTRACTO ORIGINAL con los DATOS ADICIONALES de Perplexity.

EXTRACTO ORIGINAL:
"DeepSeek released V4, their latest open-source AI model under MIT license. The model costs $0.30 per million input tokens."

DATOS ADICIONALES (de Perplexity):
- URLs fuentes: ["https://deepseek.com/blog/v4-release", "https://techcrunch.com/2026/03/deepseek-v4"]
- Puntos clave:
  * DeepSeek V4 usa arquitectura MoE con 236B parametros totales, 21B activos
  * Entrenado con 15T tokens
  * Cache de tokens cuesta solo $0.03/M (90% descuento)
  * La empresa esta en Hangzhou, China, spin-off de High-Flyer hedge fund
  * Compite directamente con GPT-4o y Claude Sonnet
- Datos adicionales:
  * DeepSeek tiene ~300 empleados
  * Recaudaron $0 en funding externo (autofinanciados por High-Flyer)

IMPORTANTE:
- Las URLs de Perplexity deben aparecer en la seccion de Fuentes
- Integra ambas fuentes coherentemente
- No pierdas datos clave de ninguna fuente


## Respuesta completa

## DeepSeek V4 llega con licencia MIT y un precio de entrada de 0,30 dolares por millon de tokens

DeepSeek publico V4, su modelo de inteligencia artificial mas reciente, como software de codigo abierto bajo licencia MIT. El dato que mas interesa a quien construye productos con modelos de lenguaje es el precio: 0,30 dolares por millon de tokens de entrada, segun el extracto de lanzamiento y la cobertura reunida para este articulo. La cifra no es un eslogan. Es un parametro concreto de inferencia que cualquier equipo puede meter en una hoja de costos.

La compania, con sede en Hangzhou, China, es un spin-off del fondo de cobertura High-Flyer. Opera con cerca de 300 empleados y, de acuerdo con los datos adicionales, no ha levantado capital externo: el proyecto se ha autofinanciado a traves de High-Flyer. Esa combinacion —modelo abierto, precio publicado y una estructura societaria poco habitual en la carrera de la inteligencia artificial— obliga a mirar V4 mas alla del anuncio.

## Que trae el modelo: MoE, 236.000 millones de parametros y 15 billones de tokens

DeepSeek V4 usa una arquitectura mixture of experts (MoE). El modelo suma 236.000 millones de parametros en total, de los cuales 21.000 millones estan activos en cada paso de inferencia. Esa diferencia importa. En un MoE no se “enciende” toda la red para cada token: el sistema enruta la consulta hacia un subconjunto de expertos. El tamano total describe la capacidad almacenada; los parametros activos describen, de forma mas cercana, el computo que se paga en cada respuesta.

El entrenamiento se hizo con 15 billones de tokens (15T). Es una escala de datos grande, pero el comunicado y las notas disponibles no detallan la composicion de ese corpus, el corte temporal ni los filtros aplicados. Conviene no leer 15T como garantia de calidad en espanol, en dominios regulatorios o en tareas especificas de una startup. Es un dato de volumen, no un benchmark.

La licencia MIT situa a V4 en el terreno del codigo abierto permisivo. En terminos generales, esa licencia permite usar, modificar y redistribuir el software, tambien con fines comerciales, manteniendo el aviso de copyright. Lo que no esta en las fuentes revisadas es el detalle operativo: pesos publicados, repositorio, limites de uso aceptable o si la API y los pesos siguen exactamente las mismas condiciones. Para un equipo legal, el siguiente paso no es celebrar la etiqueta “open source”, sino leer el texto de la licencia y los terminos del servicio que acompanen al modelo.

## El precio: 0,30 dolares de entrada y una cache a 0,03

El costo de entrada queda en 0,30 dolares por millon de tokens. La cache de tokens se cobra a 0,03 dolares por millon, un descuento del 90% respecto de ese precio de entrada. Para productos con mucho contexto repetido —historiales de chat, documentos que se reenvian, prompts de sistema largos, bases de conocimiento que no cambian en cada llamada— la cache puede pesar mas que el precio de lista.

Un calculo simple, solo con las cifras publicadas, ayuda a ordenar la conversacion interna. Un millon de tokens de entrada a tarifa completa son 0,30 dolares. El mismo millon, si entra por cache, son 0,03 dolares. La diferencia es de 0,27 dolares por millon de tokens cacheados. En un producto con millones de llamadas al mes, ese descuento deja de ser un detalle de factura y pasa a ser una decision de arquitectura: que parte del prompt es estable, que parte cambia, y como se diseña la sesion para aprovechar la cache sin degradar la respuesta.

Las fuentes usadas aqui no publican el precio de los tokens de salida, ni topes de contexto, ni latencia, ni descuentos por volumen mas alla de esa cache. Cualquier modelo financiero que asuma un costo de generacion esta inventando un numero. Tampoco hay, en el material disponible, comparaciones de precio token a token contra otros proveedores. Decir que V4 es “mas barato” en abstracto no se sostiene con lo que esta sobre la mesa. Lo que si se sostiene es el precio de entrada anunciado y el descuento de cache.

## Una empresa de Hangzhou, sin ronda externa

DeepSeek compite, segun los puntos reunidos por la cobertura, de forma directa con GPT-4o y con Claude Sonnet. Esa frase describe el segmento en el que la empresa quiere ser leida: modelos de uso general para productos que hoy evaluan esas dos referencias. No equivale a un empate en pruebas publicas. En el material integrado no hay tablas de MMLU, ni scores de codigo, ni evaluaciones en espanol. Tratar la competencia como posicionamiento de mercado, y no como resultado medido, es la lectura fiel a las fuentes.

El origen corporativo añade otra capa. Un spin-off de un hedge fund, asentado en Hangzhou, con unos 300 empleados y cero dolares de funding externo declarado, no sigue el guion de la ronda semilla, la Serie A y el crecimiento subsidiado por venture capital. La autofinanciacion puede dar margen para publicar un modelo bajo MIT y un precio agresivo de inferencia sin rendir cuentas inmediatas a un sindicato de inversores. Tambien puede significar menos presion —o una presion distinta— sobre la rentabilidad de la API.

Para quien compra capacidad de modelo desde America Latina, el dato relevante no es el relato del fondo. Es la dependencia. Un proveedor con sede en China, autofinanciado y relativamente pequeno en plantilla, concentra riesgo de continuidad, de cambios de terminos y de acceso transfronterizo. Nada en las fuentes indica que ese riesgo se haya materializado. Tampoco hay informacion sobre residencia de datos, subprocesadores o cumplimiento frente a regulaciones locales. Esos vacios forman parte de la noticia tanto como el precio.

## Que significa esto para tu startup

El primer efecto practico es de presupuesto. Si tu producto ya paga inferencia a otro proveedor, V4 entra en la comparacion con dos numeros verificables: 0,30 dolares por millon de tokens de entrada y 0,03 dolares por millon en cache. Antes de migrar, separa tu consumo real entre tokens nuevos y tokens repetidos. Una aplicacion con prompts largos y estables puede acercarse mas al precio de cache. Un agente que reescribe el contexto en cada turno puede quedarse cerca de los 0,30 dolares, mas el costo de salida que todavia no esta en estas fuentes.

El segundo efecto es de licencia. La MIT abre la puerta a integrar el modelo en un producto comercial y, si los pesos estan realmente disponibles en las condiciones anunciadas, a evaluar una corrida propia. Correr 236.000 millones de parametros, aunque solo 21.000 millones esten activos, no es un experimento de fin de semana para la mayoria de las startups latinoamericanas. La inferencia via API puede ser el camino corto; el self-hosting exige GPU, operacion y un equipo que hoy, en muchas companias de la region, no existe. La licencia permisiva no abarata el hardware.

El tercer efecto es de evaluacion, no de reemplazo automatico. Que DeepSeek situe a V4 frente a GPT-4o y Claude Sonnet no sustituye una prueba con tus propios casos: espanol rioplatense o mexicano, documentos fiscales, soporte al cliente, extraccion de datos, codigo de tu stack. Mide calidad, tasa de error y costo por tarea completada, no solo costo por token. Un modelo mas barato que falla y obliga a reintentos puede salir mas caro.

El cuarto efecto es de gobierno. Documenta de donde sale el modelo, que version usas y bajo que terminos. Con un proveedor de unos 300 personas, sin ronda externa conocida y con casa matriz en Hangzhou, conviene tener un plan de salida: otro modelo de respaldo, prompts desacoplados del proveedor y datos de clientes que no queden atrapados en una sola API. La cache barata es una ventaja; la concentracion en un solo suministro es un riesgo.

Por ultimo, no construyas la narrativa de ventas de tu startup sobre el lanzamiento de otro. “Usamos el modelo abierto de DeepSeek” no es una propuesta de valor. El valor sigue estando en el problema que resuelves, en la distribucion y en si el costo de inferencia te deja margen. V4 puede mejorar esa ecuacion. No la escribe por ti.

## Una lectura sin atajos

DeepSeek V4 junta, en un solo anuncio, piezas que no siempre viajan juntas: licencia MIT, arquitectura MoE de 236.000 millones de parametros con 21.000 millones activos, entrenamiento de 15 billones de tokens, entrada a 0,30 dolares por millon y cache a 0,03. Detras hay una empresa de Hangzhou, ligada a High-Flyer, con cerca de 300 empleados y sin funding externo declarado, que se presenta en competencia directa con GPT-4o y Claude Sonnet.

Lo que falta en el expediente publico usado aqui pesa tanto como lo que esta: precio de salida, evaluaciones comparables, condiciones exactas de los pesos y marco de datos. La reflexion util no es si este lanzamiento “cambia el juego”. Es mas estrecha y mas incomoda: con estos numeros, ¿tu costo por tarea baja de verdad, y puedes sostener el producto si ese proveedor cambia de precio, de licencia o de disponibilidad manana?

## Fuentes

- DeepSeek, nota de lanzamiento de V4: https://deepseek.com/blog/v4-release
- TechCrunch, cobertura asociada a DeepSeek V4: https://techcrunch.com/2026/03/deepseek-v4
- Extracto original integrado: lanzamiento de DeepSeek V4 como modelo de codigo abierto bajo licencia MIT, con un costo de 0,30 dolares por millon de tokens de entrada.