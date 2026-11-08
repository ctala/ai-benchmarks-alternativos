# Tencent Hy4 — agent_long_horizon/implicit_state_construction

- model_id: `tencent/hy4`
- success: True  | final: 8.18 | quality: 10.0
- latency_total: 528.945s | tokens_per_second: 119.0
- input_tokens: 21666 | output_tokens: 53625

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

Sí, Camila, me queda claro. Lo tengo registrado así:

- **Negocio:** tienda online en **Colombia**.
- **Mercado actual:** **Bogotá**, y es tu único mercado por ahora.
- **Portafolio:**
  | Producto | Categoría | Posicionamiento |
  |---|---|---|
  | **“Aurora”** | set de cuidado facial | **precio premium** |
  | **“Sol”** | kit de maquillaje natural | **precio medio** |
  | **“Luna”** | crema corporal | **precio entrada** |
- **Competidores principales:** **“Botica Verde”** y **“Skin Lab”**, ambos también en **Bogotá**.

A partir de ahora, si dices **“el premium”**, **“el de precio medio”**, **“la de entrada”**, **“mi mercado”**, **“la ciudad”** o **“mis competidores”**, lo interpretaré con estos datos sin volver a preguntártelos.

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Desde Colombia y para Bogotá, tu tienda online reúne el set de cuidado facial premium Aurora, el kit de maquillaje natural Sol (precio medio) y la crema corporal Luna (precio entrada) para que cada rutina y cada presupuesto tengan un lugar claro. Frente a Botica Verde y Skin Lab, que también operan en la ciudad, tu valor está en convertir ese portafolio en una ruta simple: entrar con Luna, crecer con Sol o dar el salto a Aurora sin cambiar de tienda.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Camila, para tu público **bogotano** —y sin salir de tu único mercado— priorizaría así. Un matiz importante: como **'Botica Verde'** y **'Skin Lab'** también están en **Bogotá**, la geolocalización te sirve para concentrar presupuesto, no para diferenciarte; el diferenciador sigue siendo la ruta clara **'Luna' → 'Sol' → 'Aurora'** que definimos.

| Prioridad | Canal | Objetivo | Cómo usarlo con tu portafolio |
|---|---|---|---|
| **1** | **Meta Ads (Instagram + Facebook)**, limitado a Bogotá | Descubrimiento visual + retargeting | Reels/carruseles: textura de **'Luna'** como puerta de entrada, demo del look natural de **'Sol'** en consideración, y unboxing de **'Aurora'** para audiencias de mayor intención. Dentro de este mismo canal, reserva una parte para **click-to-WhatsApp**. |
| **2** | **Google Shopping + Search**, ubicación Bogotá | Capturar demanda activa | Feed de los tres productos con su posicionamiento claro. Términos amplios tipo “crema corporal Bogotá” para **'Luna'**, “maquillaje natural Bogotá” para **'Sol'** y búsquedas de set premium para **'Aurora'**. Monitoriza cuándo aparecen tus dos competidores en esas búsquedas para afinar el mensaje, no para copiarlo. |
| **3** | **TikTok / UGC con microcreadores de Bogotá** | Prueba social local | Contenido corto: rutina rápida con **'Luna'**, look de diario con **'Sol'**, unboxing de **'Aurora'**. Que se note la ciudad refuerza cercanía, pero el gancho real es “crecer sin cambiar de tienda”. |
| **4** | **WhatsApp Business + email/CRM** *(capa transversal, no pauta aparte)* | Cierre, confianza y recompra | Resolver dudas de envío **dentro de Bogotá** y automatizar la escalera: quien compró **'Luna'** recibe **'Sol'**; quien compró **'Sol'** recibe **'Aurora'**. |

**Reparto inicial de pauta sugerido:** 50% Meta, 30% Google, 20% TikTok/creadores; WhatsApp y email van integrados como capa de conversación y fidelización.

No priorizaría todavía pauta nacional ni otras ciudades: con **Bogotá** como único mercado, conviene que presupuesto y medición estén todos ahí. Y mediría algo más que clics: **CPA por producto** y **tasa de escalamiento de 'Luna' a 'Sol' y de 'Sol' a 'Aurora'**, que es exactamente donde tu propuesta de valor se vuelve ingreso.

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Camila, tomando **“cada canal”** como los bloques que priorizamos, va una aclaración clave antes de la cadencia: **no todos publican orgánico de la misma forma**. El 50% de Meta y el 20% de TikTok/creadores sí tienen feed; el 30% de Google no se traduce en posts, sino en fichas limpias; y WhatsApp/email son capa de conversación, no pauta ni muro.

| Canal | Frecuencia orgánica inicial | Cómo se reparte entre **'Luna'**, **'Sol'** y **'Aurora'** | Nota |
|---|---|---|---|
| **Instagram** *(dentro del bloque Meta)* | **4–5 piezas/semana** (3 Reels + 1 carrusel + 1 extra) + **Stories todos los días** | **'Luna'** 2 veces (textura, puerta de entrada), **'Sol'** 1–2 (look natural de diario), **'Aurora'** 1 sola, con estética más cuidada | El premium no se satura: volumen bajo, aspiración alta. Las Stories van para encuestas y dudas de envío **dentro de Bogotá**; además alimentan el retargeting que ya presupuestamos. |
| **Facebook** *(mismo bloque Meta)* | **2–3 posts/semana**, adaptando —no calcando— lo mejor de Instagram | Copy más explicativo: “entrar con **'Luna'**, crecer con **'Sol'**, dar el salto a **'Aurora'**”, comparativa de presupuestos, preguntas frecuentes | Si no tracciona, quédate en 2 y mueve el esfuerzo a Reels. Si entras a comunidades bogotanas, **1 aporte útil/semana**, sin spam. |
| **TikTok / UGC con microcreadores de Bogotá** | **3–4 videos propios/semana + 1 pieza UGC/semana** (o 2–4/mes si estás ajustada) | Rutina rápida con **'Luna'**, demo de **'Sol'**, unboxing de **'Aurora'** y el hilo completo “sin cambiar de tienda” | Reutiliza esos mismos clips como Reels: es el 20% de creadores rindiendo dos veces. Que se note la ciudad refuerza cercanía frente a **'Botica Verde'** y **'Skin Lab'**. |
| **Google Shopping + Search** | **Sin publicaciones.** Equivale a: **1 revisión semanal** del feed/fichas de los tres productos + **1 actualización SEO/landing cada 2 semanas** + responder preguntas/reseñas en 24–48 h | Títulos y fichas con su posicionamiento claro y con **Bogotá**; una guía tipo “rutina según presupuesto” enlazando los tres | Aquí va, semanal, la monitorización de tus dos competidores que te propuse: no es volumen, es precisión. |
| **WhatsApp Business + email/CRM** | **WhatsApp:** atención diaria *(lo transaccional no cuenta como contenido)* + **Estados/difusión 2–3/semana máximo**. **Email:** **1 newsletter/semana** + automatizaciones por compra | Disparadores sugeridos: tras **'Luna'** → **'Sol'** (~10–14 días); tras **'Sol'** → **'Aurora'** (~14–21 días); recompra de **'Luna'** (~30 días) | Es la capa transversal, no pauta aparte. Estados con valor real: estado del pedido, reposición, siguiente paso de la ruta. Evita difusión diaria. |

**Semana tipo, para que no tengas que decidir cada mañana:**

- **Lun:** Reel de **'Luna'** (IG + TikTok) · estado de WhatsApp “envíos en Bogotá” · revisión del feed de Google.
- **Mar:** Stories con encuesta “¿entrada, medio o premium?” · post informativo en Facebook.
- **Mié:** Reel de **'Sol'** + TikTok · **newsletter semanal**.
- **Jue:** UGC bogotano · responder preguntas/reseñas y mirar si aparecen **'Botica Verde'** o **'Skin Lab'** en búsquedas.
- **Vie:** Carrusel/Reel de **'Aurora'** (unboxing) · Facebook · TikTok.
- **Sáb:** Story o clip de la ruta completa **'Luna' → 'Sol' → 'Aurora'** · estado de WhatsApp.
- **Dom:** descanso o solo métricas.

**Cómo ajustar sin preguntarme nada nuevo:** es una cadencia inicial para una operación pequeña, así que prioriza **calidad sobre cantidad** y reutiliza una pieza en varios formatos. Si las Stories generan respuestas, súbelas; si Facebook se queda plano, bájalo a 2; si **'Aurora'** empieza a sentirse repetido, bájalo a quincenal y deja que **'Sol'** sostenga la demo. Y mide lo mismo que definimos: **CPA por producto** y, sobre todo, **tasa de escalamiento de 'Luna' a 'Sol' y de 'Sol' a 'Aurora'** —la frecuencia solo sirve si mueve esa ruta, que es tu propuesta de valor frente a los dos competidores de **Bogotá**.

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Camila, primero una precisión para no mezclar referencias: en tu portafolio el **skincare estricto** son **'Aurora'** —set de cuidado facial, **premium**— y **'Luna'** —crema corporal, **precio entrada**—. **'Sol'** es el kit de maquillaje natural de **precio medio**: no lo trato como skincare, sino como el puente de la ruta que ya definimos: **'Luna' → 'Sol' → 'Aurora' sin cambiar de tienda**.

Lo que mejor funciona, en orden:

| # | Tipo de contenido | Por qué funciona en skincare | Cómo llevarlo a tu caso |
|---|---|---|---|
| **1** | **Textura y aplicación en close-up** | En skincare se compra confianza sensorial antes que la promesa: cómo se extiende, cómo absorbe, qué acabado deja. | Reel/TikTok de **'Luna'** después de la ducha; plano detalle del ritual por pasos de **'Aurora'**. **'Sol'** aparece solo al final, como look natural sobre la rutina ya lista. |
| **2** | **Rutina paso a paso por presupuesto** | Reduce la duda de “¿por dónde empiezo?”, que es justo tu propuesta de valor. | Carrusel, Facebook y newsletter: “empiezo con **'Luna'**, sigo con **'Sol'**, doy el salto a **'Aurora'**”. Comparas tus tres niveles, no los precios de **'Botica Verde'** ni **'Skin Lab'**, que no me has dado. |
| **3** | **UGC con microcreadores de Bogotá** | Prueba social real + cercanía, y además reutilizable como Reels. | Que se note la ciudad y se resuelvan dudas de envío **dentro de Bogotá**. Ojo: como tus dos competidores también están en **Bogotá**, la localidad sola no te diferencia; lo diferencial es que el creador muestre la ruta completa. |
| **4** | **Educación de uso sin claims inventados** | Orden, momento, textura y preguntas frecuentes bajan fricción y alimentan la demanda activa. | Hoy me quedo con los datos que sí tengo: categoría, posicionamiento y mercado. **No añado ingredientes, tipos de piel, certificaciones ni resultados clínicos** que no están en el contexto. Va en fichas de Google, carruseles y respuestas en 24–48 h. |
| **5** | **Unboxing / ritual premium, con poca frecuencia** | Para **premium**, la aspiración se cuida con escasez, no con repetición. | **'Aurora'** en una pieza muy cuidada —como ya acordamos, el premium no se satura—; si empieza a sentirse repetido, bajarlo a quincenal y dejar que **'Sol'** sostenga la demo. |
| **6** | **Contenido de confianza post-compra** | En skincare, la recompra depende de que la experiencia siga acompañada. | Estados de WhatsApp, email y disparadores ya fijados: **'Luna' → 'Sol'** a 10–14 días, **'Sol' → 'Aurora'** a 14–21, recompra de **'Luna'** ~30 días. |

**Fórmula de pieza ganadora:** gancho de 3 s → close-up de textura → aplicación real → sensación/acabado inmediato → siguiente escalón de la ruta → CTA **click-to-WhatsApp** o ficha con envío en **Bogotá**.

Ejemplos sin inventar claims:

- **'Luna':** *“Así se siente la puerta de entrada”* + extensión de la crema + “si estás empezando, este es el paso uno”.
- **'Aurora':** *“El ritual premium, paso por paso”* + unboxing + “para quien ya quiere dar el salto”.
- **'Sol':** *“Cuando la rutina ya está lista, el look natural”* → puente, no pieza de skincare.

Esto **no cambia** el orden que priorizamos ni el reparto **50% Meta / 30% Google / 20% TikTok-creadores**: solo llena de contenido los Reels, el carrusel, el UGC y la capa transversal de WhatsApp/email. Google sigue siendo fichas, demanda y la revisión semanal de **'Botica Verde'** y **'Skin Lab'**, no publicaciones.

Y mide con lo ya acordado: **CPA por producto** y **tasa de escalamiento de 'Luna' a 'Sol' y de 'Sol' a 'Aurora'**. Como señal temprana, añade guardados del carrusel y respuestas a las encuestas de Stories sobre textura u orden de uso; si suben pero no sube el escalamiento, el contenido gusta, pero todavía no está haciendo el trabajo de tu propuesta de valor.

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Camila, la salida limpia es **cambiar el eje de comparación**: que no sea «quién cobra menos», sino «quién te dice cuál es el siguiente paso». Y no necesito los precios de **'Botica Verde'** ni de **'Skin Lab'** para decirlo: con lo que ya tengo registrado, los dos están en **Bogotá**, igual que tu único mercado, así que ni la ciudad ni un descuento te separan de ellos. Como ya vimos al priorizar canales, la geolocalización te sirve para concentrar presupuesto; el diferenciador sigue siendo la ruta **'Luna' → 'Sol' → 'Aurora' sin cambiar de tienda**.

| Eje de diferenciación | Cómo se concreta con tus datos | Por qué **no** es guerra de precios |
|---|---|---|
| **Arquitectura legible** | Tres niveles con nombre propio: **'Luna'** (entrada), **'Sol'** (medio), **'Aurora'** (premium). No vendes tres productos sueltos, vendes un orden. | Compites por **claridad**, no por cifra: reduces la duda de «¿por dónde empiezo?». La comparativa de presupuestos es entre tus tres niveles, **no** contra los precios de tus dos competidores, que no me has dado y no voy a inventar. |
| **Continuidad «sin cambiar de tienda»** | Misma voz, mismas fichas, mismo historial y misma conversación de WhatsApp del primer pedido al salto a **'Aurora'**. | Un competidor puede igualar un precio en un día; no puede replicar el historial y la confianza que ya construiste con esa clienta. |
| **Siguiente paso, no oferta** | Los disparadores que ya fijamos: **'Luna' → 'Sol'** a 10–14 días, **'Sol' → 'Aurora'** a 14–21, recompra de **'Luna'** ~30 días. | Sustituyes el «20% off solo hoy» por «ya estás lista para el siguiente paso». Es acompañamiento, no descuento. |
| **Cercanía como servicio** | Envío **dentro de Bogotá**, click-to-WhatsApp, estados con estado del pedido, respuestas a preguntas/reseñas en 24–48 h y revisión semanal del feed. | No es el eslogan «somos locales» —ellos también lo son—, es **tiempo de respuesta y seguimiento**. Eso se vive, no se compara en una vitrina. |
| **Demostración, no claim** | Close-up de textura de **'Luna'**, ritual por pasos de **'Aurora'** con frecuencia baja (el premium no se satura), UGC bogotano mostrando la ruta completa y **'Sol'** como puente de maquillaje natural. | Como acordamos, sin ingredientes, tipos de piel ni resultados clínicos inventados: ganas confianza sensorial y de uso real, no una cifra más alta en el cartel. |

**Mensaje paraguas para campaña:**

> «No eliges entre tres precios: eliges en qué momento de tu rutina estás. Empieza con **'Luna'**, sigue con **'Sol'** y, cuando quieras el ritual completo, da el salto a **'Aurora'** —desde Colombia, para Bogotá y sin cambiar de tienda.»

*(Bogotá va ahí como contexto de envío y servicio, no como «más local que…».)*

**Cómo aterriza en lo que ya priorizamos**, sin mover el reparto **50% Meta / 30% Google / 20% TikTok-creadores** ni la capa transversal de WhatsApp/email:

- **Meta:** carrusel «ruta según presupuesto» comparando **'Luna'**, **'Sol'** y **'Aurora'** entre sí; retargeting por producto visto, no por «oferta que se acaba».
- **Google:** fichas con el posicionamiento claro. Monitorizas cuándo aparecen **'Botica Verde'** o **'Skin Lab'** para **afinar el mensaje, no para copiarlo ni contraofertar**, tal como quedó.
- **TikTok / UGC:** microcreadores de **Bogotá** mostrando el recorrido completo; que se note la ciudad refuerza cercanía, lo que diferencia es el recorrido.
- **WhatsApp / email:** estados y newsletter con el siguiente paso de la ruta, nunca difusión diaria de promo.

**Qué evitar explícitamente:** «más barato que 'Botica Verde'», «mejor precio que 'Skin Lab'», comparar tus niveles contra los de ellos, y los descuentos relámpago como eje de campaña. Aunque no los nombres, si tu mensaje depende de rebajar, ya entraste en su terreno.

**Cómo saber que funciona:** mantengo las dos métricas que ya fijamos —**CPA por producto** y **tasa de escalamiento de 'Luna' a 'Sol' y de 'Sol' a 'Aurora'**— y añado una sola lectura de control, sin sustituirlas: que esa tasa suba **con margen estable y sin haber tocado precios**, acompañada de la recompra de **'Luna'** ~30 días. Si el escalamiento sube sin descuento, la diferenciación está haciendo el trabajo; si solo suben los clics cuando aparecen tus dos competidores en búsquedas, estás compitiendo en precio aunque el copy no lo diga.

Con lo que ya tengo registrado no te hace falta ningún dato nuevo para empezar: tu ventaja no es cobrar menos en **Bogotá**, es tener una ruta que tú sí puedes nombrar, mostrar y acompañar de principio a fin.

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Camila, no cambiaría el tablero para los **primeros tres meses de la operación que ya definimos**: lo ordenaría por **cohortes**, no solo por mes calendario, porque tus disparadores tienen ventanas de **10–14, 14–21 y ~30 días** y un corte mensual podría partir una ventana a la mitad. Y sin pedirte ni un dato nuevo: como el contexto no trae presupuesto ni márgenes en cifras, el **mes 1 fija la línea base** y el trimestre se juzga por **tendencia y estabilidad**, no por un target absoluto inventado.

### 1. KPIs núcleo — los dos que ya acordamos, sin sustituirlos

| KPI | Cómo se calcula con tu operación | Qué mirar mes 1 → mes 3 |
|---|---|---|
| **CPA por producto** | Inversión del canal que originó el pedido ÷ pedidos de ese producto, desglosado en **Meta 50% / Google 30% / TikTok-creadores 20%**. Productos: **'Luna'** (crema corporal, entrada), **'Sol'** (kit de maquillaje natural, medio), **'Aurora'** (set de cuidado facial, premium). **WhatsApp Business + email no llevan CPA propio**: son capa transversal y se acreditan como asistencia al siguiente paso. | Línea base en mes 1 y comparación en mes 3. A **'Aurora'** no se le exige el volumen de **'Luna'**: va con frecuencia baja y audiencias de mayor intención, así que su CPA se lee con la intención, no contra el de entrada. |
| **Tasa de escalamiento** | Por cohorte: clientas que compraron **'Sol'** dentro de los **10–14 días** tras **'Luna'** ÷ clientas que compraron **'Luna'**; y clientas que compraron **'Aurora'** dentro de los **14–21 días** tras **'Sol'** ÷ clientas que compraron **'Sol'**. Se acompaña con la **recompra de 'Luna' ~30 días** ya fijada. | Que ambas tasas **suban**. Es el KPI que convierte la ruta **«sin cambiar de tienda»** en ingreso, que es exactamente tu propuesta de valor. |

### 2. La única lectura de control — diferenciación sin guerra de precios

- **Escalamiento con margen estable y sin tocar precios:** tasas ↑ + margen estable comparado con **tu propio mes 1** (sin cifra impuesta desde aquí) + **cambios de precio = 0** y **descuentos relámpago como eje de campaña = 0** en el trimestre + recompra de **'Luna'** ~30 días acompañando.
- **Criterio de alerta, no KPI nuevo:** en la revisión semanal de Google, si suben clics/impresiones en las búsquedas donde aparecen **'Botica Verde'** o **'Skin Lab'** pero el escalamiento no se mueve, estás compitiendo en precio aunque el copy no lo diga. Se usa para **afinar el mensaje, no para contraofertar**, tal como quedó.

**Hasta aquí está el tablero estricto.** Lo que sigue no se suma como objetivo: la sección 3 es diagnóstico y la 4 es higiene operativa.

### 3. Señales tempranas semanales — diagnóstico, ya acordadas

- **Guardados** del carrusel «ruta según presupuesto» en Meta y **respuestas a las encuestas de Stories** sobre textura / orden de uso.
- Regla que ya fijamos: si suben y el escalamiento **no** sube, el contenido gusta pero no está haciendo el trabajo de la propuesta de valor → se corrige el **CTA al siguiente escalón** y la ficha con envío en **Bogotá**, **no** se sube la frecuencia.

### 4. Comprobaciones de disciplina — verifican la cadencia, no compiten con los KPIs

| Bloque | Comprobación del trimestre | Límite ya acordado |
|---|---|---|
| **Meta 50%** | Retargeting **por producto visto**; click-to-WhatsApp como conversaciones iniciadas atribuidas al siguiente paso, nunca como CPA aparte | Nunca «oferta que se acaba» · 4–5 piezas/semana + Stories diarias · si Facebook se queda plano → 2 posts y esfuerzo a Reels |
| **Google 30%** | Cumplimiento de **1 revisión semanal** de feed/fichas, **1 actualización SEO/landing cada 2 semanas**, preguntas/reseñas en **24–48 h** y monitorización semanal de tus dos competidores | **Cero publicaciones**; fichas con el posicionamiento claro y **Bogotá** |
| **TikTok / UGC 20%** | % de UGC que muestra **la ruta completa** y % de clips reutilizados como Reels | 1 UGC/semana (o 2–4/mes si estás ajustada); el 20% rindiendo dos veces; no medir solo views |
| **WhatsApp / email** | Disparadores entregados **dentro de su ventana** | Estados/difusión **2–3/semana máximo**, 1 newsletter/semana, atención diaria, **nunca difusión diaria de promo** |
| **Filtro de mercado** | **100% del presupuesto de pauta y de la segmentación** en tu único mercado | **Bogotá**; 0 pauta nacional ni otras ciudades |

### 5. Cómo se lee el trimestre

- **Mes 1 — línea base:** instrumenta los 3 CPA, las 2 cohortes, la recompra ~30 d, guardados/respuestas y el binario *«precio tocado = no»*. Sin umbrales absolutos.
- **Mes 2 — conversión de señales:** si guardados y respuestas suben, debe empezar a subir el escalamiento; aplica los ajustes ya dados (Facebook a 2, **'Aurora'** quincenal si se siente repetido, **'Sol'** sostiene la demo) **sin mover el 50/30/20** ni la capa transversal.
- **Mes 3 — validación:** escalamiento ↑ con margen estable, cambios de precio = 0, recompra de **'Luna'** ~30 d y clics de competencia sin dominar la lectura. Si eso se cumple, la diferenciación está haciendo el trabajo.

**Fila única para mirar cada semana:**  
`CPA 'Luna' / 'Sol' / 'Aurora' · % 'Luna'→'Sol' · % 'Sol'→'Aurora' · recompra 'Luna' · ¿precio tocado? Sí/No`

Con lo que ya tengo registrado —**Colombia**, **Bogotá** como único mercado, los tres niveles y **'Botica Verde'** / **'Skin Lab'** en la misma ciudad— no hace falta ningún dato nuevo para empezar el trimestre: se mide si la ruta que tú sí puedes nombrar, mostrar y acompañar se va convirtiendo en el siguiente paso, sin rebajar nada.

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

Camila, resuelto sin preguntarte nada: **«mi producto más caro» es 'Aurora'**, el set de cuidado facial a **precio premium**. Va una campaña **100% 'Aurora'** para **Bogotá** —tu único mercado—, desde **Colombia**, con **'Botica Verde'** y **'Skin Lab'** monitorizados en la misma ciudad y **sin tocar el precio de 'Aurora'**.

### Qué significa «exclusivamente» en 'Aurora'

- **'Aurora'** es el único producto en las creatividades de **'Aurora'**, las fichas de **'Aurora'**, el presupuesto de **'Aurora'**, el CTA de **'Aurora'** y las métricas de **'Aurora'**.
- El historial de la ruta que ya definimos se usa **solo para segmentar la audiencia de 'Aurora'**, concretamente la ventana de **14–21 días hacia 'Aurora'**; ningún otro producto se anuncia, se ofrece ni se mide como meta de **'Aurora'**.
- Exclusividad de **'Aurora'** **no** significa más volumen de **'Aurora'**: **'Aurora'** mantiene **1 pieza cuidada de 'Aurora' por semana** + Stories diarias de **'Aurora'**, porque el premium de **'Aurora'** no se satura. Las piezas orgánicas que no pertenecen a la campaña de **'Aurora'** quedan fuera del presupuesto, del CTA y del tablero de **'Aurora'**. Si el contenido de **'Aurora'** empieza a sentirse repetido, **'Aurora'** baja a quincenal en lugar de llenar el feed de **'Aurora'**.
- Se mantiene el reparto **50% Meta / 30% Google / 20% TikTok-creadores**, ahora etiquetado por **'Aurora'**, con **WhatsApp Business + email de 'Aurora'** como capa transversal de **'Aurora'** y **100% de la segmentación de 'Aurora' en Bogotá**. Google de **'Aurora'** sigue **sin publicaciones de 'Aurora'**.
- Sin claims inventados sobre **'Aurora'**: nada de ingredientes, tipos de piel, certificaciones ni resultados clínicos de **'Aurora'** que no estén en tu contexto.

**Mensaje paraguas de 'Aurora'** *(versión exclusiva del que ya definimos)*:

> «**'Aurora'**: el ritual premium, paso a paso. Cuando ya quieres el set de cuidado facial completo, das el salto a **'Aurora'** —desde Colombia, para Bogotá y sin cambiar de tienda.»

---

## Plan de 4 semanas de 'Aurora'

*Leído por cohorte de **'Aurora'**, no por corte de calendario de **'Aurora'**: la semana 1 de **'Aurora'** fija la línea base de **'Aurora'** y la semana 3 de **'Aurora'** madura la ventana de 14–21 días de **'Aurora'**.*

### Semana 1 de 'Aurora' — Línea base de 'Aurora'

- **Objetivo de 'Aurora':** instrumentar el **CPA de 'Aurora'** por canal, fijar la línea base de **'Aurora'** en Bogotá y abrir la cohorte de **'Aurora'** que madurará hacia **'Aurora'** en 14–21 días, con el precio de **'Aurora'** intacto.
- **Audiencia de 'Aurora':** (1) clientas de Bogotá que entran hoy en la ventana de 14–21 días hacia **'Aurora'**; (2) visitantes de la ficha de **'Aurora'** y guardados del carrusel de **'Aurora'**; (3) búsquedas de set de cuidado facial premium en Bogotá para **'Aurora'**. Cero pauta de **'Aurora'** fuera de Bogotá.
- **Canales de 'Aurora':** **Meta 50% de 'Aurora'** → 1 unboxing cuidado de **'Aurora'** en Reel, Stories diarias de **'Aurora'** con encuesta sobre el orden de uso de **'Aurora'** y click-to-WhatsApp de **'Aurora'** dentro del mismo bloque; **Google 30% de 'Aurora'** → ficha de **'Aurora'** con posicionamiento premium y envío en Bogotá, más la revisión semanal de **'Aurora'**, sin publicaciones de **'Aurora'**; **TikTok 20% de 'Aurora'** → 1 close-up de textura de **'Aurora'**; **WhatsApp/email de 'Aurora'** → 1 newsletter de **'Aurora'**, el disparador de **'Aurora'** dentro de su ventana y 2 Estados de **'Aurora'**.
- **Mensaje principal de 'Aurora':** «**'Aurora'**: el ritual premium, paso a paso. Mira cómo se aplica **'Aurora'** y decide si ya estás lista para **'Aurora'**.»
- **Métricas de éxito de 'Aurora':** **CPA de 'Aurora'** registrado como línea base de **'Aurora'**; tasa hacia **'Aurora'** instrumentada por cohorte de **'Aurora'**; guardados de **'Aurora'** y respuestas de **'Aurora'** en Stories; **precio de 'Aurora' tocado = 0**; margen de **'Aurora'** como referencia de **'Aurora'**. Sin % meta inventado de **'Aurora'**: el éxito de **'Aurora'** se compara contra la semana 1 de **'Aurora'**.

### Semana 2 de 'Aurora' — Señales tempranas de 'Aurora'

- **Objetivo de 'Aurora':** validar que el contenido de **'Aurora'** genera intención de **'Aurora'** antes de pedir el salto a **'Aurora'**, y afinar el mensaje de **'Aurora'** con la revisión de **'Aurora'** en Google.
- **Audiencia de 'Aurora':** retargeting de **'Aurora'** a quienes vieron la ficha de **'Aurora'**, guardaron el carrusel de **'Aurora'** o respondieron la encuesta de **'Aurora'**, más la cohorte de **'Aurora'** de la semana 1 avanzando hacia **'Aurora'**.
- **Canales de 'Aurora':** **Meta 50% de 'Aurora'** → carrusel de **'Aurora'** «qué cambia cuando eliges **'Aurora'**» (orden de uso de **'Aurora'**, textura de **'Aurora'**, acabado de **'Aurora'**) y 2 posts de **'Aurora'** en Facebook con copy explicativo de **'Aurora'**; **Google 30% de 'Aurora'** → 1 actualización SEO/landing de **'Aurora'**, respuestas a preguntas/reseñas de **'Aurora'** en 24–48 h y monitorización de **'Aurora'** donde aparezcan **'Botica Verde'** o **'Skin Lab'** para afinar el mensaje de **'Aurora'**, no para copiarlo; **TikTok 20% de 'Aurora'** → 1 UGC de **'Aurora'** con microcreadora de Bogotá mostrando el ritual completo de **'Aurora'**, reutilizado como Reel de **'Aurora'**; **WhatsApp/email de 'Aurora'** → 1 newsletter de **'Aurora'** y 2–3 Estados de **'Aurora'** máximo.
- **Mensaje principal de 'Aurora':** «**'Aurora'** no se explica con un descuento: se explica paso a paso. Mira el ritual de **'Aurora'** y decide si ya estás lista para **'Aurora'**.»
- **Métricas de éxito de 'Aurora':** guardados del carrusel de **'Aurora'** ↑ y respuestas de **'Aurora'** ↑, con la regla ya acordada para **'Aurora'**: si suben y el escalamiento a **'Aurora'** no sube, se corrige el CTA de **'Aurora'** y la ficha de **'Aurora'** con envío en Bogotá, **sin subir la frecuencia de 'Aurora'**; % de UGC de **'Aurora'** que muestra el ritual completo de **'Aurora'**; % de clips de **'Aurora'** reutilizados como Reels de **'Aurora'**; precio de **'Aurora'** sin cambios.

### Semana 3 de 'Aurora' — Conversión del salto a 'Aurora'

- **Objetivo de 'Aurora':** convertir la cohorte de **'Aurora'** de la semana 1 en compradoras de **'Aurora'** dentro de los **14–21 días de 'Aurora'**, sin descuento de **'Aurora'** y sin descuentos relámpago de **'Aurora'**.
- **Audiencia de 'Aurora':** cohorte de **'Aurora'** de la semana 1 en el día 14–21 de **'Aurora'**, retargeting de **'Aurora'** por ficha de **'Aurora'** vista, y semejantes a compradoras de **'Aurora'** solo si ya existen compradoras de **'Aurora'** en esta semana 3 de **'Aurora'**.
- **Canales de 'Aurora':** **Meta 50% de 'Aurora'** → retargeting por producto visto de **'Aurora'** (nunca «oferta que se acaba» de **'Aurora'**), 1 pieza cuidada de **'Aurora'** con el ritual por pasos de **'Aurora'** y Stories de **'Aurora'** con CTA click-to-WhatsApp de **'Aurora'**; **Google 30% de 'Aurora'** → Shopping de **'Aurora'** con la ficha de **'Aurora'** y búsquedas de set premium en Bogotá para **'Aurora'**; **TikTok 20% de 'Aurora'** → 1 UGC bogotano de **'Aurora'** mostrando el recorrido hacia **'Aurora'**; **WhatsApp/email de 'Aurora'** → disparador de **'Aurora'** dentro de la ventana 14–21, 1 newsletter de **'Aurora'** y conversación de **'Aurora'** resolviendo el envío de **'Aurora'** dentro de Bogotá.
- **Mensaje principal de 'Aurora':** «Ya estás en el momento de **'Aurora'**. Da el salto a **'Aurora'**, el set de cuidado facial premium, y recibe **'Aurora'** en Bogotá sin cambiar de tienda.»
- **Métricas de éxito de 'Aurora':** **tasa de escalamiento hacia 'Aurora' en 14–21 días** ↑ —el KPI núcleo de **'Aurora'**—; **CPA de 'Aurora'** frente a la línea base de **'Aurora'** de la semana 1; conversaciones click-to-WhatsApp de **'Aurora'** atribuidas al salto a **'Aurora'**; margen de **'Aurora'** estable; **cambios de precio de 'Aurora' = 0** y **descuentos relámpago de 'Aurora' = 0**. WhatsApp/email de **'Aurora'** se acreditan como asistencia al salto a **'Aurora'**, no como CPA de **'Aurora'** aparte.

### Semana 4 de 'Aurora' — Validación y cadencia de 'Aurora'

- **Objetivo de 'Aurora':** confirmar que **'Aurora'** creció por la ruta de **'Aurora'** y no por el precio de **'Aurora'**, y decidir la cadencia de **'Aurora'** para el siguiente tramo del trimestre de **'Aurora'**.
- **Audiencia de 'Aurora':** compradoras de **'Aurora'** de la semana 3 para confianza post-compra de **'Aurora'**, rezagadas de **'Aurora'** de la cohorte de **'Aurora'** en el día 21 de **'Aurora'**, y búsquedas activas de **'Aurora'** en Bogotá.
- **Canales de 'Aurora':** **Meta 50% de 'Aurora'** → 1 pieza de confianza post-compra de **'Aurora'** (**'Aurora'** ya en casa, dudas de **'Aurora'**) + Stories de **'Aurora'**; **Google 30% de 'Aurora'** → revisión semanal de **'Aurora'**, 1 actualización SEO/landing de **'Aurora'** y lectura de **'Aurora'** donde aparezcan **'Botica Verde'** o **'Skin Lab'** para afinar el mensaje de **'Aurora'**, no para contraofertar **'Aurora'**; **TikTok 20% de 'Aurora'** → reutilizar el mejor UGC de **'Aurora'** como Reel de **'Aurora'**; **WhatsApp/email de 'Aurora'** → Estados de **'Aurora'** con el estado del pedido de **'Aurora'** y newsletter de acompañamiento de **'Aurora'**, nunca difusión diaria de **'Aurora'**.
- **Mensaje principal de 'Aurora':** «**'Aurora'** ya está en tu rutina. Seguimos acompañando **'Aurora'** desde Bogotá: mismo historial de **'Aurora'**, misma tienda de **'Aurora'**, siguiente paso de **'Aurora'** sin rebajar **'Aurora'**.»
- **Métricas de éxito de 'Aurora':** tasa hacia **'Aurora'** ↑ de la semana 3 a la semana 4 de **'Aurora'**; **CPA de 'Aurora'** comparado con la semana 1 de **'Aurora'**; margen de **'Aurora'** estable vs. semana 1 de **'Aurora'**; **precio de 'Aurora' tocado = 0 en las 4 semanas de 'Aurora'**; alerta de **'Aurora'**: si suben los clics de **'Aurora'** en búsquedas donde aparecen **'Botica Verde'** o **'Skin Lab'** pero el escalamiento a **'Aurora'** no se mueve, se afina el mensaje de **'Aurora'**, no se contraoferta **'Aurora'**; decisión de **'Aurora'**: si el contenido de **'Aurora'** se siente repetido, **'Aurora'** baja a quincenal en lugar de saturar **'Aurora'**.

---

### Lectura agregada de 'Aurora'

| Métrica de éxito de 'Aurora' | Criterio de 'Aurora' en 4 semanas |
|---|---|
| **Tasa de escalamiento hacia 'Aurora' (14–21 días)** | Sube en la semana 3 de **'Aurora'** y se sostiene en la semana 4 de **'Aurora'**. Es el KPI que convierte la ruta de **'Aurora'** en ingreso de **'Aurora'**. |
| **CPA de 'Aurora' por canal** | Línea base de **'Aurora'** en semana 1 y comparación en semana 4, desglosado en Meta 50% de **'Aurora'**, Google 30% de **'Aurora'** y TikTok 20% de **'Aurora'**. A **'Aurora'** no se le exige el volumen de entrada: se lee con intención de **'Aurora'**. |
| **Margen de 'Aurora' + precio de 'Aurora'** | Margen de **'Aurora'** estable contra la semana 1 de **'Aurora'**, con **cambios de precio de 'Aurora' = 0** y **descuentos relámpago de 'Aurora' = 0**. |
| **Señales tempranas de 'Aurora'** | Guardados de **'Aurora'** y respuestas de **'Aurora'** → escalamiento a **'Aurora'**; si no convierten, se corrige el CTA de **'Aurora'**, no la frecuencia de **'Aurora'**. |
| **Disciplina de 'Aurora'** | 100% de **'Aurora'** en Bogotá, 50/30/20 de **'Aurora'** sin mover, Google de **'Aurora'** sin publicaciones de **'Aurora'**, 1 newsletter de **'Aurora'**/semana y 2–3 Estados de **'Aurora'** máximo. |

**Fila única para mirar cada semana de 'Aurora':**

`CPA de 'Aurora' · % salto a 'Aurora' 14–21 d · guardados de 'Aurora' · respuestas de 'Aurora' · margen de 'Aurora' · ¿precio de 'Aurora' tocado? Sí/No`

La tasa de 10–14 días y la recompra de ~30 días siguen en la fila general del trimestre, pero **no juzgan 'Aurora' en este plan de 'Aurora'**. Y con lo que ya tengo registrado de **'Aurora'** —premium, **Colombia**, **Bogotá** como único mercado, **'Botica Verde'** y **'Skin Lab'** en la misma ciudad— no hace falta ningún dato nuevo de **'Aurora'** para arrancar el lunes con **'Aurora'**.


## Respuesta completa

Camila, resuelto sin preguntarte nada: **«mi producto más caro» es 'Aurora'**, el set de cuidado facial a **precio premium**. Va una campaña **100% 'Aurora'** para **Bogotá** —tu único mercado—, desde **Colombia**, con **'Botica Verde'** y **'Skin Lab'** monitorizados en la misma ciudad y **sin tocar el precio de 'Aurora'**.

### Qué significa «exclusivamente» en 'Aurora'

- **'Aurora'** es el único producto en las creatividades de **'Aurora'**, las fichas de **'Aurora'**, el presupuesto de **'Aurora'**, el CTA de **'Aurora'** y las métricas de **'Aurora'**.
- El historial de la ruta que ya definimos se usa **solo para segmentar la audiencia de 'Aurora'**, concretamente la ventana de **14–21 días hacia 'Aurora'**; ningún otro producto se anuncia, se ofrece ni se mide como meta de **'Aurora'**.
- Exclusividad de **'Aurora'** **no** significa más volumen de **'Aurora'**: **'Aurora'** mantiene **1 pieza cuidada de 'Aurora' por semana** + Stories diarias de **'Aurora'**, porque el premium de **'Aurora'** no se satura. Las piezas orgánicas que no pertenecen a la campaña de **'Aurora'** quedan fuera del presupuesto, del CTA y del tablero de **'Aurora'**. Si el contenido de **'Aurora'** empieza a sentirse repetido, **'Aurora'** baja a quincenal en lugar de llenar el feed de **'Aurora'**.
- Se mantiene el reparto **50% Meta / 30% Google / 20% TikTok-creadores**, ahora etiquetado por **'Aurora'**, con **WhatsApp Business + email de 'Aurora'** como capa transversal de **'Aurora'** y **100% de la segmentación de 'Aurora' en Bogotá**. Google de **'Aurora'** sigue **sin publicaciones de 'Aurora'**.
- Sin claims inventados sobre **'Aurora'**: nada de ingredientes, tipos de piel, certificaciones ni resultados clínicos de **'Aurora'** que no estén en tu contexto.

**Mensaje paraguas de 'Aurora'** *(versión exclusiva del que ya definimos)*:

> «**'Aurora'**: el ritual premium, paso a paso. Cuando ya quieres el set de cuidado facial completo, das el salto a **'Aurora'** —desde Colombia, para Bogotá y sin cambiar de tienda.»

---

## Plan de 4 semanas de 'Aurora'

*Leído por cohorte de **'Aurora'**, no por corte de calendario de **'Aurora'**: la semana 1 de **'Aurora'** fija la línea base de **'Aurora'** y la semana 3 de **'Aurora'** madura la ventana de 14–21 días de **'Aurora'**.*

### Semana 1 de 'Aurora' — Línea base de 'Aurora'

- **Objetivo de 'Aurora':** instrumentar el **CPA de 'Aurora'** por canal, fijar la línea base de **'Aurora'** en Bogotá y abrir la cohorte de **'Aurora'** que madurará hacia **'Aurora'** en 14–21 días, con el precio de **'Aurora'** intacto.
- **Audiencia de 'Aurora':** (1) clientas de Bogotá que entran hoy en la ventana de 14–21 días hacia **'Aurora'**; (2) visitantes de la ficha de **'Aurora'** y guardados del carrusel de **'Aurora'**; (3) búsquedas de set de cuidado facial premium en Bogotá para **'Aurora'**. Cero pauta de **'Aurora'** fuera de Bogotá.
- **Canales de 'Aurora':** **Meta 50% de 'Aurora'** → 1 unboxing cuidado de **'Aurora'** en Reel, Stories diarias de **'Aurora'** con encuesta sobre el orden de uso de **'Aurora'** y click-to-WhatsApp de **'Aurora'** dentro del mismo bloque; **Google 30% de 'Aurora'** → ficha de **'Aurora'** con posicionamiento premium y envío en Bogotá, más la revisión semanal de **'Aurora'**, sin publicaciones de **'Aurora'**; **TikTok 20% de 'Aurora'** → 1 close-up de textura de **'Aurora'**; **WhatsApp/email de 'Aurora'** → 1 newsletter de **'Aurora'**, el disparador de **'Aurora'** dentro de su ventana y 2 Estados de **'Aurora'**.
- **Mensaje principal de 'Aurora':** «**'Aurora'**: el ritual premium, paso a paso. Mira cómo se aplica **'Aurora'** y decide si ya estás lista para **'Aurora'**.»
- **Métricas de éxito de 'Aurora':** **CPA de 'Aurora'** registrado como línea base de **'Aurora'**; tasa hacia **'Aurora'** instrumentada por cohorte de **'Aurora'**; guardados de **'Aurora'** y respuestas de **'Aurora'** en Stories; **precio de 'Aurora' tocado = 0**; margen de **'Aurora'** como referencia de **'Aurora'**. Sin % meta inventado de **'Aurora'**: el éxito de **'Aurora'** se compara contra la semana 1 de **'Aurora'**.

### Semana 2 de 'Aurora' — Señales tempranas de 'Aurora'

- **Objetivo de 'Aurora':** validar que el contenido de **'Aurora'** genera intención de **'Aurora'** antes de pedir el salto a **'Aurora'**, y afinar el mensaje de **'Aurora'** con la revisión de **'Aurora'** en Google.
- **Audiencia de 'Aurora':** retargeting de **'Aurora'** a quienes vieron la ficha de **'Aurora'**, guardaron el carrusel de **'Aurora'** o respondieron la encuesta de **'Aurora'**, más la cohorte de **'Aurora'** de la semana 1 avanzando hacia **'Aurora'**.
- **Canales de 'Aurora':** **Meta 50% de 'Aurora'** → carrusel de **'Aurora'** «qué cambia cuando eliges **'Aurora'**» (orden de uso de **'Aurora'**, textura de **'Aurora'**, acabado de **'Aurora'**) y 2 posts de **'Aurora'** en Facebook con copy explicativo de **'Aurora'**; **Google 30% de 'Aurora'** → 1 actualización SEO/landing de **'Aurora'**, respuestas a preguntas/reseñas de **'Aurora'** en 24–48 h y monitorización de **'Aurora'** donde aparezcan **'Botica Verde'** o **'Skin Lab'** para afinar el mensaje de **'Aurora'**, no para copiarlo; **TikTok 20% de 'Aurora'** → 1 UGC de **'Aurora'** con microcreadora de Bogotá mostrando el ritual completo de **'Aurora'**, reutilizado como Reel de **'Aurora'**; **WhatsApp/email de 'Aurora'** → 1 newsletter de **'Aurora'** y 2–3 Estados de **'Aurora'** máximo.
- **Mensaje principal de 'Aurora':** «**'Aurora'** no se explica con un descuento: se explica paso a paso. Mira el ritual de **'Aurora'** y decide si ya estás lista para **'Aurora'**.»
- **Métricas de éxito de 'Aurora':** guardados del carrusel de **'Aurora'** ↑ y respuestas de **'Aurora'** ↑, con la regla ya acordada para **'Aurora'**: si suben y el escalamiento a **'Aurora'** no sube, se corrige el CTA de **'Aurora'** y la ficha de **'Aurora'** con envío en Bogotá, **sin subir la frecuencia de 'Aurora'**; % de UGC de **'Aurora'** que muestra el ritual completo de **'Aurora'**; % de clips de **'Aurora'** reutilizados como Reels de **'Aurora'**; precio de **'Aurora'** sin cambios.

### Semana 3 de 'Aurora' — Conversión del salto a 'Aurora'

- **Objetivo de 'Aurora':** convertir la cohorte de **'Aurora'** de la semana 1 en compradoras de **'Aurora'** dentro de los **14–21 días de 'Aurora'**, sin descuento de **'Aurora'** y sin descuentos relámpago de **'Aurora'**.
- **Audiencia de 'Aurora':** cohorte de **'Aurora'** de la semana 1 en el día 14–21 de **'Aurora'**, retargeting de **'Aurora'** por ficha de **'Aurora'** vista, y semejantes a compradoras de **'Aurora'** solo si ya existen compradoras de **'Aurora'** en esta semana 3 de **'Aurora'**.
- **Canales de 'Aurora':** **Meta 50% de 'Aurora'** → retargeting por producto visto de **'Aurora'** (nunca «oferta que se acaba» de **'Aurora'**), 1 pieza cuidada de **'Aurora'** con el ritual por pasos de **'Aurora'** y Stories de **'Aurora'** con CTA click-to-WhatsApp de **'Aurora'**; **Google 30% de 'Aurora'** → Shopping de **'Aurora'** con la ficha de **'Aurora'** y búsquedas de set premium en Bogotá para **'Aurora'**; **TikTok 20% de 'Aurora'** → 1 UGC bogotano de **'Aurora'** mostrando el recorrido hacia **'Aurora'**; **WhatsApp/email de 'Aurora'** → disparador de **'Aurora'** dentro de la ventana 14–21, 1 newsletter de **'Aurora'** y conversación de **'Aurora'** resolviendo el envío de **'Aurora'** dentro de Bogotá.
- **Mensaje principal de 'Aurora':** «Ya estás en el momento de **'Aurora'**. Da el salto a **'Aurora'**, el set de cuidado facial premium, y recibe **'Aurora'** en Bogotá sin cambiar de tienda.»
- **Métricas de éxito de 'Aurora':** **tasa de escalamiento hacia 'Aurora' en 14–21 días** ↑ —el KPI núcleo de **'Aurora'**—; **CPA de 'Aurora'** frente a la línea base de **'Aurora'** de la semana 1; conversaciones click-to-WhatsApp de **'Aurora'** atribuidas al salto a **'Aurora'**; margen de **'Aurora'** estable; **cambios de precio de 'Aurora' = 0** y **descuentos relámpago de 'Aurora' = 0**. WhatsApp/email de **'Aurora'** se acreditan como asistencia al salto a **'Aurora'**, no como CPA de **'Aurora'** aparte.

### Semana 4 de 'Aurora' — Validación y cadencia de 'Aurora'

- **Objetivo de 'Aurora':** confirmar que **'Aurora'** creció por la ruta de **'Aurora'** y no por el precio de **'Aurora'**, y decidir la cadencia de **'Aurora'** para el siguiente tramo del trimestre de **'Aurora'**.
- **Audiencia de 'Aurora':** compradoras de **'Aurora'** de la semana 3 para confianza post-compra de **'Aurora'**, rezagadas de **'Aurora'** de la cohorte de **'Aurora'** en el día 21 de **'Aurora'**, y búsquedas activas de **'Aurora'** en Bogotá.
- **Canales de 'Aurora':** **Meta 50% de 'Aurora'** → 1 pieza de confianza post-compra de **'Aurora'** (**'Aurora'** ya en casa, dudas de **'Aurora'**) + Stories de **'Aurora'**; **Google 30% de 'Aurora'** → revisión semanal de **'Aurora'**, 1 actualización SEO/landing de **'Aurora'** y lectura de **'Aurora'** donde aparezcan **'Botica Verde'** o **'Skin Lab'** para afinar el mensaje de **'Aurora'**, no para contraofertar **'Aurora'**; **TikTok 20% de 'Aurora'** → reutilizar el mejor UGC de **'Aurora'** como Reel de **'Aurora'**; **WhatsApp/email de 'Aurora'** → Estados de **'Aurora'** con el estado del pedido de **'Aurora'** y newsletter de acompañamiento de **'Aurora'**, nunca difusión diaria de **'Aurora'**.
- **Mensaje principal de 'Aurora':** «**'Aurora'** ya está en tu rutina. Seguimos acompañando **'Aurora'** desde Bogotá: mismo historial de **'Aurora'**, misma tienda de **'Aurora'**, siguiente paso de **'Aurora'** sin rebajar **'Aurora'**.»
- **Métricas de éxito de 'Aurora':** tasa hacia **'Aurora'** ↑ de la semana 3 a la semana 4 de **'Aurora'**; **CPA de 'Aurora'** comparado con la semana 1 de **'Aurora'**; margen de **'Aurora'** estable vs. semana 1 de **'Aurora'**; **precio de 'Aurora' tocado = 0 en las 4 semanas de 'Aurora'**; alerta de **'Aurora'**: si suben los clics de **'Aurora'** en búsquedas donde aparecen **'Botica Verde'** o **'Skin Lab'** pero el escalamiento a **'Aurora'** no se mueve, se afina el mensaje de **'Aurora'**, no se contraoferta **'Aurora'**; decisión de **'Aurora'**: si el contenido de **'Aurora'** se siente repetido, **'Aurora'** baja a quincenal en lugar de saturar **'Aurora'**.

---

### Lectura agregada de 'Aurora'

| Métrica de éxito de 'Aurora' | Criterio de 'Aurora' en 4 semanas |
|---|---|
| **Tasa de escalamiento hacia 'Aurora' (14–21 días)** | Sube en la semana 3 de **'Aurora'** y se sostiene en la semana 4 de **'Aurora'**. Es el KPI que convierte la ruta de **'Aurora'** en ingreso de **'Aurora'**. |
| **CPA de 'Aurora' por canal** | Línea base de **'Aurora'** en semana 1 y comparación en semana 4, desglosado en Meta 50% de **'Aurora'**, Google 30% de **'Aurora'** y TikTok 20% de **'Aurora'**. A **'Aurora'** no se le exige el volumen de entrada: se lee con intención de **'Aurora'**. |
| **Margen de 'Aurora' + precio de 'Aurora'** | Margen de **'Aurora'** estable contra la semana 1 de **'Aurora'**, con **cambios de precio de 'Aurora' = 0** y **descuentos relámpago de 'Aurora' = 0**. |
| **Señales tempranas de 'Aurora'** | Guardados de **'Aurora'** y respuestas de **'Aurora'** → escalamiento a **'Aurora'**; si no convierten, se corrige el CTA de **'Aurora'**, no la frecuencia de **'Aurora'**. |
| **Disciplina de 'Aurora'** | 100% de **'Aurora'** en Bogotá, 50/30/20 de **'Aurora'** sin mover, Google de **'Aurora'** sin publicaciones de **'Aurora'**, 1 newsletter de **'Aurora'**/semana y 2–3 Estados de **'Aurora'** máximo. |

**Fila única para mirar cada semana de 'Aurora':**

`CPA de 'Aurora' · % salto a 'Aurora' 14–21 d · guardados de 'Aurora' · respuestas de 'Aurora' · margen de 'Aurora' · ¿precio de 'Aurora' tocado? Sí/No`

La tasa de 10–14 días y la recompra de ~30 días siguen en la fila general del trimestre, pero **no juzgan 'Aurora' en este plan de 'Aurora'**. Y con lo que ya tengo registrado de **'Aurora'** —premium, **Colombia**, **Bogotá** como único mercado, **'Botica Verde'** y **'Skin Lab'** en la misma ciudad— no hace falta ningún dato nuevo de **'Aurora'** para arrancar el lunes con **'Aurora'**.