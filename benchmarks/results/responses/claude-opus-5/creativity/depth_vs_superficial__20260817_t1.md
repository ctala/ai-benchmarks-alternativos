# Claude Opus 5 — creativity/depth_vs_superficial

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.85 | quality: 10.0
- latency_total: 121.694s | tokens_per_second: 61.2
- input_tokens: 247 | output_tokens: 7451

## Entrada exacta (lo que recibió el modelo)

**user:**

Un emprendedor te dice: "Estoy pensando en usar IA para mi startup de delivery de comida en Santiago. Que deberia hacer?"

Da una respuesta que demuestre PROFUNDIDAD real, no consejos genericos.
Incluye:
- Al menos 2 ideas especificas que NO sean obvias (no digas "usa IA para optimizar rutas", eso lo sabe cualquiera)
- Numeros o estimaciones concretas cuando sea posible
- Un riesgo no obvio que otros no mencionarian
- Una opinion contrarian o controversia sobre el tema

No me des una lista generica de "5 formas de usar IA". Quiero pensamiento original.


## Respuesta completa

## Primero, reencuadremos el problema

Tu problema no es falta de inteligencia. Es **varianza y densidad**.

La gente no se va de una app de delivery porque tarde 38 minutos. Se va porque prometiste 30 y llegó en 62, tres veces. El churn se explica mucho mejor por la *cola derecha* de la distribución de tiempos (el p90, el p95) que por la media. Y casi todo el mundo optimiza la media, porque es lo que sale en el dashboard.

Segundo: el ROI de cualquier modelo tuyo es función de la densidad de pedidos, no de la calidad del modelo. Bajo cierto umbral —dígamos ~2-3 pedidos por km² por hora— simplemente no hay pedidos co-ocurrentes que agrupar, y todo el aparato de ML te aporta casi nada. Con densidad alta, el mismo modelo mediocre te da 20% de eficiencia. Esto tiene una implicancia estratégica dura: **te conviene ser insultantemente pequeño geográficamente** (el corredor Providencia-Ñuñoa, 8-10 km², no "Santiago") antes de gastar un peso en IA.

Con eso en mente:

---

## Idea 1: Merchandising consciente de la oferta (no recomendación "relevante")

Todos usan ML para rankear restaurantes por *relevancia para el usuario*. Eso es un problema de e-commerce, y tú no tienes un problema de e-commerce: tienes un problema de logística con un catálogo.

Lo que casi nadie hace: rankear por **contribución marginal por minuto-repartidor**, condicionado al estado actual de la red. Si en este momento tienes tres pedidos saliendo de Manuel Montt a Ñuñoa, el sushi de Manuel Montt debería subir 15 posiciones en el feed de todos los usuarios de Ñuñoa —no porque le guste más al usuario, sino porque hace *batchable* ese viaje. Es demand shaping, no demand prediction. Las palancas son el orden del feed, el ETA que muestras, el costo de despacho dinámico por restaurante, y qué cupón le tiras a quién.

La aritmética de por qué importa tanto: con ticket promedio de ~$15.000 CLP y comisión efectiva 22-25%, tu revenue por pedido anda en $4.500-5.500 (comisión + fee al cliente). El pago al repartidor en Santiago está en el orden de $2.500-3.500 por entrega. Tu contribución por pedido está oscilando entre -$500 y +$1.000. **Estás jugando en el margen del error de redondeo.** Subir el batching de 1.15 a 1.45 pedidos por viaje te baja el costo logístico por pedido cerca de 18-20%, o sea unos $500-650 CLP. Eso es literalmente la diferencia entre contribución negativa y positiva. Ninguna mejora en "recomendaciones personalizadas" mueve la aguja ni una décima parte de eso.

## Idea 2: El cuello de botella es la cocina, y ahí hay un producto escondido

Descompón la varianza de tu tiempo de entrega. Mi apuesta, por lo que se ve en operaciones así: el tráfico explica bastante menos de lo que la gente cree, y el **tiempo de preparación del restaurante** explica la mayor parte de la cola derecha. Un restaurante que dice "15 minutos" y en el peak del viernes 21:00 demora 34 es el que te destruye el NPS y te quema capacidad de flota.

Dos cosas concretas:

**(a)** Modelo de tiempo de preparación a nivel plato × restaurante × hora × carga actual de la cocina, usado no para mostrar un ETA más bonito sino para **decidir cuándo despachar al repartidor**. Si tus repartidores esperan 5-7 minutos promedio en el local y lo bajas a 2, recuperas ~8-12% de capacidad de flota. Eso equivale a contratar 10% más repartidores gratis. En una operación de 3.000 pedidos/día eso son cientos de horas-repartidor al mes.

**(b)** Lo que casi nadie mide: un **"deliverability score" por plato**. Qué platos sobreviven 25 minutos en una mochila y cuáles generan reclamo. Papas fritas, todo lo frito y crocante, sopas, helados, cosas con salsa separada. Puedes estimarlo con la tasa de reclamo/reembolso por SKU y luego re-merchandisar el catálogo: bajar los platos que rompen, empujar los que aguantan, o forzar packaging distinto. Los reembolsos y compensaciones andan típicamente entre 3% y 6% del GMV en estas operaciones; bajarlo 2 puntos porcentuales, sobre márgenes de contribución de 3-7%, es una mejora enorme. Y ojo: acá el modelo mismo se vuelve producto vendible al restaurante ("estos 4 platos te están costando reputación en delivery, cámbiales el envase").

**Bonus (Idea 3):** deja de usar surge plano. Un surge de $800 CLP a toda la zona le paga extra al ~70% de repartidores que iba a conectarse igual. Con un modelo de elasticidad individual (probabilidad de conexión dado incentivo, historial, día, clima) puedes recortar 15-25% del gasto en incentivos con la misma oferta conectada. Pero lee el riesgo de abajo antes de hacer esto.

---

## El riesgo no obvio: tu algoritmo es evidencia legal contra ti

Este es el que nadie te va a mencionar.

En Chile rige la Ley 21.431 (plataformas digitales de servicios), que además de exigir contrato, registro y cotizaciones, **obliga a transparentar los criterios del algoritmo de asignación y prohíbe la discriminación algorítmica**. Y el nuevo régimen de datos personales (Ley 21.719, con Agencia de Protección de Datos y multas que pueden llegar a miles de UTM) incorpora derechos frente a decisiones automatizadas.

La trampa fina es esta: **mientras más sofisticado y prescriptivo hagas tu algoritmo, más construyes la prueba de subordinación y dependencia.** Tasas de aceptación obligatorias, penalizaciones por rechazar, asignación forzada, scoring que determina quién trabaja el viernes, incentivos personalizados que en la práctica dirigen la jornada: cada una de esas cosas es exactamente lo que un tribunal laboral o la Dirección del Trabajo mira para reclasificar a los repartidores como trabajadores dependientes. Con efecto retroactivo. El costo laboral efectivo sube en el orden de 30-45%, más un pasivo por cotizaciones impagas que puede aparecer justo cuando estás levantando una Serie A y aparece en el due diligence.

Traducción práctica: diseña el sistema como **recomendación con opt-out real y sin penalización**, documenta desde el día uno los criterios del algoritmo en lenguaje comprensible, y guarda versionado de modelos y decisiones. No porque sea bonito, sino porque es el artefacto que te va a pedir un fiscalizador o un abogado laboral. Casi ningún fundador escribe esto en el sprint 1 y después es carísimo retrofitearlo.

Segundo riesgo técnico, más sutil: tus modelos se envenenan solos. Si apagas zonas cuando llueve, tu modelo de demanda aprende que cuando llueve no hay demanda. Si muestras ETAs conservadores, tu modelo de tiempos aprende de una realidad que tú mismo distorsionaste. Necesitas reservar 3-5% del tráfico como *holdout* aleatorio permanente, aunque te duela. Es el costo de tener datos causales en vez de datos que solo describen tus propias decisiones pasadas.

---

## Mi opinión contrarian (dos, en realidad)

**1. Tu primera contratación técnica no debe ser un data scientist.** Debe ser alguien de operaciones que sepa SQL y que esté dispuesto a etiquetar datos a mano durante tres meses. En estas operaciones, el 80% del valor está en instrumentación —timestamps confiables de cuándo el repartidor llegó, cuándo el local aceptó, cuándo salió la comida— y en Chile esos datos casi siempre están sucios o inexistentes. Un data scientist senior sin esa base te va a entregar modelos elegantes entrenados con basura. Y para el 90% de lo que necesitas, gradient boosting más optimización clásica le gana a cualquier cosa con "LLM" en el nombre. Los LLM se pagan solos en exactamente dos lugares: soporte al cliente y ingesta/normalización de menús (que es un dolor real y aburrido: 40.000 platos con nombres inconsistentes).

**2. La parte incómoda: probablemente no deberías competir en delivery B2C.** Rappi y PedidosYa ya ganaron ese mercado en Chile y lo defienden con capital que tú no tienes; DiDi Food ya se fue de Chile, lo que dice algo. Pero dejaron un problema abierto y desatendido: miles de restaurantes pagando 25-30% de comisión, sin datos propios, sin canal propio, sin idea de qué platos les convienen en delivery. Vender la capa de inteligencia y canal propio a esos restaurantes —donde tú tienes el modelo de cocina, el deliverability score y la logística tercerizada— es un negocio con márgenes de software, no de logística. Es menos sexy que "el Rappi chileno con IA". También es mucho más probable que exista en 2028.

---

**Si tuviera que elegir tus primeros 90 días:** instrumenta los seis timestamps del ciclo de pedido con precisión de segundos, construye el histograma de varianza y descubre dónde se te va el tiempo de verdad, y ataca el tiempo de espera del repartidor en el local. Nada de modelos hasta tener eso. Ese trabajo aburrido es el que después hace que cualquier IA que construyas funcione.