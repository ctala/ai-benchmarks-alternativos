# Tencent Hy4 — noticias_redaccion/deepseek_caida_nvidia

- model_id: `tencent/hy4`
- success: True  | final: 7.48 | quality: 8.5
- latency_total: 86.888s | tokens_per_second: 113.1
- input_tokens: 703 | output_tokens: 9825

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor de contenido para un founder hispanohablante que publica noticias y análisis para emprendedores de América Latina y España. Escribes en español neutro, claro y directo, con subtítulos en Markdown (##).

**user:**

Es para el blog de una agencia de automatización que explica a pymes qué pasa con los modelos de IA.

Escribe la nota en español neutro, de 900 a 1.300 palabras, solo con datos de la fuente.

FUENTE:
Shares of chipmaker Nvidia fell about 17% on Monday after Chinese startup DeepSeek released an artificial intelligence model that matched the performance of leading American systems while, according to the company, costing a fraction as much to train. The drop erased close to $600 billion of Nvidia's market value in a single session, one of the largest one-day losses in the history of the U.S. stock market.

DeepSeek, based in Hangzhou, is backed by a Chinese hedge fund. The company published a technical report saying that the final training run of one of its models cost about $5.6 million in computing time and used 2,048 Nvidia H800 chips, a version of the company's processors designed to comply with American export restrictions.

The company was founded by Liang Wenfeng, who also co-founded the quantitative hedge fund that finances it. According to people familiar with the company, it hired many young researchers from Chinese universities and focused on research rather than on building commercial products quickly.

In its technical documentation, DeepSeek described several engineering techniques that helped it reduce costs, including an architecture that activates only part of the model for each request and methods that make training more efficient on the chips it had available. Researchers in other countries said the papers were detailed and that some of the ideas could be adopted by other labs.

The release also reopened the debate over American export controls. The United States has limited the sale of its most advanced chips to China, arguing that they could be used for military purposes. Some commentators said DeepSeek's results showed that the restrictions were pushing Chinese companies to become more efficient; others said they proved that the controls needed to be tightened further.

Several American technology leaders reacted publicly to the news, some praising the work and others questioning whether the company had disclosed all the resources it used. OpenAI said it was reviewing whether its models had been used improperly to train competing systems.

Experts quickly pointed out that the figure only covered the final training run and excluded research, earlier experiments and the cost of the hardware itself. Even so, the number challenged the widespread belief that building frontier models requires billions of dollars in chips.

DeepSeek's reasoning model was released with open weights, which means any company can download it and run it on its own infrastructure. Within days, the company's assistant app climbed to the top of download charts in several countries.

Investors worried that if powerful models can be trained with fewer chips, demand for Nvidia's most expensive processors could slow. Other analysts argued the opposite: cheaper models tend to increase total usage, which in the end requires more computing power.

For small companies that use AI, the episode had a practical reading. Competition among model providers was pushing prices down, and open models were becoming a real option for businesses that want to control costs or keep their data in-house.


## Respuesta completa

# Lo que el caso DeepSeek cambia para tu pyme (sin ruido y con los datos encima de la mesa)

Cuando escribimos en este blog, intentamos separar el titular de la decisión práctica. Esta semana el titular fue enorme; la decisión práctica también lo es, aunque se haya contado menos. Una startup china publicó un modelo de inteligencia artificial, el mercado reaccionó en una sola sesión y, en cuestión de días, las pequeñas empresas que usamos IA para automatizar procesos tenemos una opción nueva que antes no estaba tan clara.

Te lo resumimos con una regla que nos imponemos en la agencia: solo lo que dice el reporte y la documentación disponible. Nada de proyecciones inventadas, nada de comparaciones con productos que no aparecen en la fuente, nada de cifras redondeadas por nuestra cuenta. Vamos por partes, porque hay mucha letra pequeña detrás de un número que parece simple.

## El lunes que movió el mercado

Las acciones del fabricante de chips Nvidia cayeron alrededor de un 17 % el lunes. La caída borró cerca de 600.000 millones de dólares de su valor de mercado en una sola sesión. La propia fuente la describe como una de las mayores pérdidas en un solo día en la historia del mercado bursátil de Estados Unidos.

Conviene detenerse en la causa, porque no fue un resultado trimestral ni un cambio de directiva. El detonante fue que DeepSeek, una startup china, liberó un modelo de inteligencia artificial que igualó el rendimiento de los sistemas líderes estadounidenses. Según la propia compañía, entrenarlo costó una fracción de lo que cuestan esos sistemas.

Para una pyme, este primer bloque ya deja una idea: el valor de los proveedores de infraestructura se está leyendo en función de cuántos chips harán falta mañana, no solo de cuántos se vendieron ayer. Volveremos sobre esto al final, porque los analistas no están todos de acuerdo.

## Quién está detrás del modelo

DeepSeek tiene base en Hangzhou y está respaldada por un fondo de cobertura chino. La financiación llega de un fondo cuantitativo, tal como indica la fuente, y ese origen condiciona la forma en la que se trabajó.

La compañía la fundó Liang Wenfeng, que también cofundó ese mismo fondo cuantitativo que la financia. Según personas familiarizadas con la empresa, el equipo contrató a muchos investigadores jóvenes directamente de universidades chinas. El detalle que más nos interesa como agencia de automatización es el foco: se dedicaron a la investigación antes que a construir productos comerciales rápidamente.

Esa prioridad explica por qué el entregable inicial fue un informe técnico y una documentación detallada, y no una campaña centrada en funcionalidades de cara al usuario final. Primero el paper, después el asistente. Es una secuencia poco habitual cuando se compite por descargas, y sin embargo las descargas llegaron igual, como veremos más adelante.

## La cifra: 5,6 millones y 2.048 chips

El informe técnico dice que la ejecución final de entrenamiento de uno de sus modelos costó unos 5,6 millones de dólares en tiempo de cómputo. Para hacerlo usaron 2.048 chips Nvidia H800.

Aquí hay un matiz que la fuente subraya y que conviene no saltarse: los H800 son una versión de los procesadores de Nvidia diseñada específicamente para cumplir con las restricciones de exportación estadounidenses. Es decir, el resultado no se obtuvo con los chips más avanzados que Estados Unidos reserva fuera de China, sino con la variante permitida por ese marco regulatorio.

El número, tomado tal cual, es el que encendió todas las alarmas. Se puso frente a la creencia generalizada de que construir modelos de frontera exige miles de millones de dólares en chips. Frente a «miles de millones», «unos 5,6 millones en tiempo de cómputo». La comparación es tan directa que el mercado la descontó en la misma sesión del lunes.

Pero antes de llevar esa cifra a tu presupuesto de automatización, hay que abrir el capítulo de los expertos. Lo hacemos más abajo, con la misma literalidad.

## Cómo consiguieron reducir el costo

La documentación técnica de DeepSeek no presenta el ahorro como un golpe de suerte. Describe varias técnicas de ingeniería que ayudaron a reducir costos.

La primera es una arquitectura que activa solo una parte del modelo para cada solicitud. En lugar de poner a trabajar el sistema completo cada vez que llega una petición, se moviliza el fragmento necesario. La segunda son métodos que hacen que el entrenamiento sea más eficiente sobre los chips que tenían disponibles: esos 2.048 H800. No hablamos de hardware nuevo, sino de exprimir mejor el hardware ya presente.

Investigadores de otros países señalaron que los artículos eran detallados y que algunas de esas ideas podrían ser adoptadas por otros laboratorios. Este dato importa a una pyme aunque no entrene modelos: si las ideas se adoptan en otros laboratorios, la eficiencia deja de ser una ventaja aislada de una empresa en Hangzhou y pasa a formar parte de la forma estándar de construir sistemas. Y cuando la eficiencia se generaliza, el precio que se paga por usar esos sistemas tiende a moverse.

## La letra pequeña que todo fundador debe leer

Los expertos señalaron rápidamente algo que la fuente deja claro: la cifra de 5,6 millones de dólares cubre únicamente la ejecución final del entrenamiento.

Quedan fuera tres partidas concretas:

- La investigación previa.
- Los experimentos anteriores.
- El costo del hardware en sí mismo.

Dicho de otro modo: los 2.048 chips no están contabilizados dentro de esos 5,6 millones; lo que se contabiliza es el tiempo de cómputo de esa última corrida. Tampoco está el trabajo de los investigadores jóvenes de las universidades chinas ni las pruebas que llevaron hasta la arquitectura final.

Ahora bien —y aquí está el matiz que la propia fuente conserva—, incluso con esa acotación, el número desafió la creencia extendida de que los modelos de frontera requieren miles de millones de dólares en chips. No la derrumba del todo, pero la obliga a revisarse. Para quien dirige una empresa pequeña, la lectura es de método: cuando un proveedor te enseñe un costo de entrenamiento, pregunta qué incluye y qué excluye. La diferencia entre «ejecución final» y «proyecto completo» es la diferencia entre una partida y el conjunto del trabajo.

## Controles, dudas y reacciones

El lanzamiento reabrió el debate sobre los controles de exportación de Estados Unidos. El país ha limitado la venta de sus chips más avanzados a China con el argumento de que podrían tener un uso militar.

La fuente recoge dos lecturas opuestas entre los comentaristas. Unos dijeron que los resultados de DeepSeek demostraban que las restricciones estaban empujando a las empresas chinas a volverse más eficientes: justo lo que describen los métodos de entrenamiento sobre los H800. Otros dijeron, en cambio, que esos mismos resultados probaban que los controles debían endurecerse todavía más.

Varios líderes tecnológicos estadounidenses reaccionaron públicamente. Algunos elogiaron el trabajo. Otros cuestionaron si la compañía había revelado todos los recursos que utilizó, en línea con la advertencia de los expertos sobre los costos excluidos. OpenAI, por su parte, comunicó que estaba revisando si sus modelos se habían usado de forma indebida para entrenar sistemas competidores.

No vamos a resolver ese debate desde este blog. Lo registramos porque afecta al ritmo al que llegan las mejoras: si el marco regulatorio se aprieta o se afloja, cambia qué chips están disponibles, y de ahí vuelve a cambiar cuánto cuesta ejecutar un modelo. Para una pyme que automatiza, eso se traduce en una sola recomendación: no casarse con un proveedor único.

## Pesos abiertos: el cambio real para una empresa pequeña

Aquí está el punto que más nos interesa en la agencia. El modelo de razonamiento de DeepSeek se publicó con pesos abiertos.

La fuente lo define sin ambigüedad: significa que cualquier empresa puede descargarlo y ejecutarlo en su propia infraestructura. No es un acceso condicionado a un volumen determinado de consultas ni una licencia atada a un plan concreto; es la posibilidad de correr el modelo donde ya corre el resto de tus procesos.

En cuestión de días, la aplicación de asistente de la compañía subió a lo más alto de las listas de descargas en varios países. La adopción no fue una promesa de hoja de ruta: fue un dato de las propias listas de descargas.

¿Por qué esto es práctico y no solo técnico? La fuente lo dice al cerrar: los modelos abiertos se están convirtiendo en una opción real para las empresas que quieren controlar costos o mantener sus datos *in-house*, dentro de su propia infraestructura. Si tu automatización trata información que no quieres que salga de tu entorno, la opción ya no es elegir entre «usar IA» o «no usar IA». Es elegir dónde se ejecuta. Y si lo que te preocupa es la factura, la opción ya no es solo negociar precio con un proveedor, sino decidir si lo ejecutas tú.

## Menos chips o más cómputo: la discusión entre inversores y analistas

La reacción del lunes tiene una lógica que conviene entender bien. Los inversores se preocuparon porque, si se pueden entrenar modelos potentes con menos chips, la demanda de los procesadores más caros de Nvidia podría ralentizarse. De ahí el 17 % y los cerca de 600.000 millones de dólares borrados en una sesión.

Pero otros analistas plantearon exactamente lo contrario: los modelos más baratos tienden a aumentar el uso total, y ese uso total, al final, requiere más potencia de cómputo. No es una contradicción retórica; son dos formas de mirar la misma cadena. El inversor mira el costo por entrenamiento. El analista mira la cantidad de solicitudes que se hacen cuando el costo baja: las mismas solicitudes para las que la arquitectura de DeepSeek activa solo una parte del modelo.

Para una pyme, ambas lecturas conviven. Pagas menos por unidad, pero es probable que acabes ejecutando más unidades. Por eso el control de costos no va solo de encontrar el modelo más barato: va de saber cuántas solicitudes estás moviendo y dónde las estás ejecutando.

## La lectura práctica que nos llevamos

El episodio tiene una conclusión explícita para pequeñas empresas que usan IA, y la dejamos para el final porque es el motivo de esta nota:

La competencia entre proveedores de modelos está empujando los precios a la baja. Y los modelos abiertos son ya una opción real para controlar costos o para mantener los datos dentro de la infraestructura propia.

Todo lo demás —la caída del 17 %, los 600.000 millones, los 5,6 millones de la ejecución final, los 2.048 H800, los investigadores de Hangzhou, la revisión de OpenAI, el debate sobre los controles, la advertencia de los expertos sobre la investigación y el hardware excluidos, la subida en las listas de descargas— son las piezas que explican por qué esa conclusión es hoy más sólida que antes de este lunes.

En la agencia lo traducimos así para nuestros clientes: antes de definir cualquier automatización, revisa tres cosas con los datos que tengas delante. Qué parte del costo te están mostrando. Si el modelo se puede descargar y ejecutar en tu propia infraestructura. Y si el proveedor que elegiste sigue siendo el único capaz de hacer lo que necesitas. La respuesta a la tercera, después de este lunes, ya no es automática.