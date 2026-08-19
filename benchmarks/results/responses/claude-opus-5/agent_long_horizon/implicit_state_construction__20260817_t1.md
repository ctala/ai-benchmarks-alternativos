# Claude Opus 5 — agent_long_horizon/implicit_state_construction

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 6.62 | quality: 8.5
- latency_total: 363.281s | tokens_per_second: 70.5
- input_tokens: 39120 | output_tokens: 22889

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

Clarísimo, Camila. Lo que tengo registrado:

**Tu negocio:** tienda online en Colombia.

**Portafolio (3 productos):**
| Producto | Qué es | Posicionamiento de precio |
|---|---|---|
| **Aurora** | Set de cuidado facial | Premium |
| **Sol** | Kit de maquillaje natural | Medio |
| **Luna** | Crema corporal | Entrada |

**Mercado actual:** Bogotá (único, por ahora).

**Competencia principal:** Botica Verde y Skin Lab, ambos también en Bogotá.

Con eso puedo trabajar sin volver a preguntártelo. Cuando quieras avanzar, hay tres cosas que me ayudarían a afinar cualquier plan de campaña:

1. **Objetivo prioritario** — ¿adquirir clientes nuevos, aumentar ticket promedio, o mover un producto en específico?
2. **Canales que ya usas** y presupuesto mensual aproximado en pauta.
3. **Qué tanto sabes de tu cliente actual** — ¿quién compra más hoy, y por cuál de los tres productos entra la mayoría?

¿Por dónde quieres empezar?

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Te propongo esta, construida sobre lo único que puedo afirmar con certeza de tu portafolio: que cubre rostro, maquillaje y cuerpo en tres niveles de precio.

**Propuesta de valor**

> Ayudamos a las mujeres de Bogotá a construir su rutina completa de cuidado —rostro, maquillaje y cuerpo— sin tener que saltar entre marcas ni pagar precio premium por todo. Puedes empezar por donde tu presupuesto te alcance hoy con Luna, y subir a Sol o Aurora cuando quieras, dentro de una misma línea que ya conoces y en la que confías.

**El ángulo que estoy usando:** tu ventaja estructural es la *escalera de precios dentro de un portafolio coherente*. Una marca solo premium no puede captar a quien apenas empieza; una marca solo de entrada no retiene a quien crece. Tú puedes hacer las dos cosas, y eso es difícil de copiar rápido.

**Variante más corta y más comercial**, si la quieres para bio de Instagram o encabezado de tienda:

> Tu rutina completa de cuidado, en una sola marca. Empieza por Luna, llega hasta Aurora.

**Dos advertencias honestas:**

1. Esta propuesta se sostiene en la **arquitectura** de tu portafolio, no en el producto. Si Botica Verde o Skin Lab ya tienen rangos de precio similares, deja de ser diferenciadora y solo describe tu catálogo. No sé cómo están ellos de precios, y eso lo definiría.
2. Le falta el **por qué te creen**. "Maquillaje natural" en Sol sugiere que hay algo en formulación, ingredientes u origen que no me has contado. Si ese componente existe —ingredientes colombianos, libre de crueldad animal, formulación para clima de altura de Bogotá, elaboración artesanal— es probablemente más potente que el argumento de precios, y reescribiría la propuesta alrededor de eso.

¿Hay algo en cómo están hechos tus productos que los distinga? Con eso te doy una versión mucho más difícil de imitar.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Te lo ordeno por prioridad, no como lista de opciones. Con tres productos y un solo mercado, tu riesgo real es abrir cinco canales a la vez y no tener señal en ninguno.

## Nivel 1 — Los dos que sí o sí

**1. Instagram + Meta Ads (Instagram/Facebook)**
Es donde está tu categoría en Bogotá y donde la decisión de compra en belleza se toma visualmente. Úsalo con división de trabajo por producto:

- **Luna** (entrada) → tráfico frío. Es tu producto de adquisición: precio bajo, decisión rápida, poco riesgo para quien no te conoce.
- **Sol** (medio) → retargeting de quien vio Luna o interactuó con contenido.
- **Aurora** (premium) → casi nada de tráfico frío. Va a lista de clientes existentes y públicos similares a compradoras. Vender premium a desconocidos es la forma más rápida de quemar presupuesto.

**2. WhatsApp Business**
En Colombia no es opcional, es donde se cierra la venta. Resuelve objeciones que una tienda online no resuelve sola ("¿sirve para piel mixta?", "¿cuánto tarda el envío a Chapinero?") y es tu canal de recompra más barato. Además es el vehículo natural de tu escalera de precios: la clienta que compró Luna hace seis semanas es a quien le escribes sobre Sol.

Catálogo cargado, respuestas rápidas guardadas, y etiquetas por producto comprado. Eso solo ya te da segmentación.

## Nivel 2 — Cuando el Nivel 1 tenga tracción

**3. Google Search (solo dos tipos de campaña)**
No busques volumen aquí, busca intención:
- Tu marca y tus nombres de producto — barato, y evita que Botica Verde o Skin Lab te pauten encima.
- Términos de categoría con intención de compra: "set cuidado facial Bogotá", "crema corporal natural domicilio". Volumen bajo, conversión alta.

**4. TikTok orgánico**
Alcance sin presupuesto, y tu categoría funciona muy bien en formato demostración/rutina. Lo pongo en nivel 2 porque exige constancia de contenido, no dinero. Si no puedes sostener 3-4 piezas semanales, no lo abras.

**5. Micro-influencers bogotanas (5k–30k seguidores)**
Más eficientes que perfiles grandes y muchas trabajan por canje o tarifas manejables. Aquí sí manda a **Aurora**: el premium necesita prueba social que la pauta no compra.

## Nivel 3 — Lo que yo aplazaría

**Marketplaces** (Mercado Libre, Falabella, Linio) y **Rappi**. Dan volumen rápido, sí, pero te cobran comisión sobre un portafolio donde Luna ya es de precio entrada, y —más grave— te quedas sin el dato del cliente. Tu propuesta de valor depende de que puedas seguir a alguien desde Luna hasta Aurora; en marketplace la clienta es de ellos, no tuya. Entra ahí cuando ya tengas base propia de recompra.

**Email**: no lo descarto, lo subordino. En este mercado WhatsApp le gana en apertura. Recolecta correos igual, pero no inviertas ahí primero.

## La métrica que decide todo

Sigue el **costo de adquisición contra el valor a 90 días, no contra la primera compra**. Si mides Luna por su venta inicial, va a parecer un mal negocio y la vas a apagar justo cuando es tu mejor puerta de entrada.

---

**Dos cosas que cambiarían esta priorización** y que no tengo:

- **Tu presupuesto mensual de pauta.** Por debajo de ~1,5–2 millones COP mensuales, yo concentraría *todo* en Meta Ads y WhatsApp, y borraría el Nivel 2 por ahora. Repartir poco entre muchos canales no genera aprendizaje en ninguno.
- **Qué canales ya tienes andando.** Si Instagram ya te trae ventas, el trabajo no es abrir canales sino arreglar la conversión y la recompra de lo que existe.

Dime esos dos datos y te lo convierto en una asignación concreta de presupuesto por canal y producto.

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

La respuesta honesta: la frecuencia correcta es **la máxima que puedas sostener 12 semanas seguidas sin quemarte**. Un canal con 3 publicaciones semanales constantes le gana a uno con 7 durante dos semanas y luego silencio. El algoritmo castiga la intermitencia más de lo que premia el volumen.

Con eso dicho, te doy dos escenarios.

## Cadencia mínima viable (si trabajas sola)

| Canal | Frecuencia | Formato |
|---|---|---|
| **Instagram Reels** | 3 por semana | Video vertical, 15–30 seg |
| **Instagram Stories** | 5 días por semana, 2–4 por día | Lo crudo, lo cotidiano |
| **Instagram feed (post/carrusel)** | 1–2 por semana | Educativo o prueba social |
| **WhatsApp Estados** | 3 por semana | Reciclado de Stories |
| **TikTok** | No lo abras todavía | — |

Esto es sostenible para una persona. Son unas 4–5 piezas de producción real por semana, porque Stories no se "producen", se capturan.

## Cadencia de crecimiento (si tienes ayuda o alguien de apoyo)

| Canal | Frecuencia |
|---|---|
| **Instagram Reels** | 5 por semana |
| **Instagram Stories** | Diario, 3–5 por día |
| **Instagram feed** | 2–3 por semana |
| **TikTok** | 4–5 por semana (sube los mismos Reels sin marca de agua) |
| **WhatsApp Estados** | 4–5 por semana |

## Cómo reparto tus tres productos en la semana

Aquí está el error que veo seguido: publicar por igual los tres productos. No. Tu contenido debe reflejar la función de cada uno.

De cada 10 piezas:

- **4 sobre Luna** — es tu producto de adquisición. Contenido de alcance amplio: texturas, aplicación, "cómo hidratar en el clima seco de Bogotá". Precio de entrada, decisión fácil, es tu anzuelo orgánico.
- **3 sobre Sol** — tutoriales de maquillaje natural, "look de oficina en 5 minutos", antes/después. Es el formato más compartible que tienes.
- **2 sobre Aurora** — poco volumen, mucha profundidad. Rutina completa, testimonios reales, por qué cuesta lo que cuesta. El premium se vende con confianza acumulada, no con frecuencia.
- **1 de marca** — tú, tu historia, detrás de cámaras, empaques, respuestas a preguntas. Este es el que construye la razón para creerte.

Y una regla transversal: **máximo 3 de cada 10 piezas con llamado a la venta directa**. El resto educa, entretiene o muestra. Si cada publicación pide compra, la gente deja de mirar.

## Cómo sostener esto sin morir

**Graba por lotes.** Una sesión de 3 horas cada domingo o lunes te puede dar los Reels de dos semanas. Cambio de blusa entre tomas y ya tienes variedad visual. La constancia se logra con producción por lotes, no con disciplina diaria.

**Recicla en cascada.** Un Reel bueno se convierte en: publicación de TikTok, Estado de WhatsApp, carrusel con los pasos, y Story con pregunta. Una pieza, cuatro apariciones.

**Espía la cadencia de Botica Verde y Skin Lab.** No para imitarla, sino para saber cuánto ruido hay. Si ambos publican diario, tu ventaja no va a ser volumen: va a ser que tú apareces en cámara y una marca genérica no.

## Cuándo subir la frecuencia

No subas por calendario, sube cuando se cumplan las dos condiciones:
1. Llevas 6 semanas cumpliendo la cadencia actual sin fallar.
2. Ya sabes qué formato te funciona mejor (tienes 2–3 piezas con rendimiento claramente superior).

Sin la segunda, publicar más solo multiplica contenido que no funciona.

---

Para ajustarte esto con precisión me falta un dato que no me has dado: **¿estás sola en esto o tienes quien te ayude con contenido?** Y relacionado, ¿te sientes cómoda apareciendo en cámara? Si la respuesta es que sí, tu cadencia puede ser más alta con menos esfuerzo, porque el contenido con rostro humano se produce más rápido y rinde más que el de producto en fondo blanco. Si prefieres no salir, el plan cambia y hay que resolverlo con manos, texturas y voz en off.

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Antes de entrar: de tus tres productos, dos son skincare (**Aurora** en rostro, **Luna** en cuerpo) y **Sol** es maquillaje. Lo aclaro porque el mejor contenido de skincare que puedes hacer es justamente el que los conecta, y ahí tienes una ventaja que una marca de solo cremas no tiene.

## Los formatos, en orden de rendimiento

**1. Diarios de resultado en el tiempo (14, 21 o 28 días)**
El activo más valioso de la categoría, y es gratis. Misma luz, misma hora, mismo ángulo, foto diaria. Publicas el día 1 anunciando el reto, y luego cortes semanales. Funciona porque el skincare tiene un problema de fe —nadie cree que algo sirva en un video de 20 segundos— y esto lo resuelve mostrando tiempo real.

Hazlo con **Aurora**. Es lo que justifica el precio premium.

**2. Textura y aplicación en primer plano**
Producto extendiéndose sobre piel, en cámara lenta, con sonido real y sin música. Es el contenido de mayor alcance de la categoría porque se ve, se siente y no exige leer nada. Es tu formato para **Luna**: producto de entrada, decisión rápida, tráfico frío.

Además se graba en minutos y no requiere que salga tu cara.

**3. Rutina completa en tiempo real ("me arreglo contigo")**
Aquí está tu jugada distintiva: rostro con Aurora → cuerpo con Luna → maquillaje con Sol. Es el único formato que vende los tres productos en una pieza y que hace visible tu propuesta de valor sin explicarla. Ninguna marca que solo vende cremas puede grabar esto.

**4. Educación de un solo punto**
Un video, una idea, 20 segundos. "Por qué se te descama la piel aunque te eches crema". "El orden correcto: ¿sérum antes o después de hidratante?". No mencionas producto, o lo mencionas al final sin insistir. Esto construye la autoridad que después permite vender Aurora.

**5. Prueba social cruda**
Capturas de WhatsApp de clientas (con permiso), reseñas leídas en voz alta, video de una clienta real hablando sin guion. Lo mal grabado convierte mejor que lo producido, porque se lee como verdad. Indispensable para el premium: **Aurora no se vende con pauta, se vende con testimonio**.

**6. Objeciones y mitos**
"¿Por qué Aurora cuesta lo que cuesta?" — desglosa cantidad, duración, costo por uso. "Natural no significa que no funcione". Este formato mata la fricción de precio antes de que la clienta la piense.

## Tu ángulo desaprovechado: Bogotá

Vives en una ciudad a 2.600 metros: aire seco, radiación UV alta que la gente subestima porque hace frío, piel deshidratada, cambios bruscos entre mañana y tarde. Casi nadie hace contenido de skincare específico para esas condiciones —se copia el genérico de clima tropical o de Miami.

Contenido como *"por qué tu piel se comporta distinto en Bogotá que en la costa"* o *"tu piel en época de vientos de agosto"* es imposible de replicar por una marca genérica, y a **Botica Verde** y **Skin Lab**, aunque estén en Bogotá, probablemente no se les ha ocurrido. Vale la pena que revises sus últimas 20 publicaciones para confirmarlo antes de apostar ahí.

## Lo que no funciona

- Producto sobre fondo blanco con el precio encima. Es catálogo, no contenido.
- Frases motivacionales sobre amor propio con tu logo. Cero recordación.
- Fotos de banco de imágenes con modelos que no son tus clientas. Se detecta de inmediato y te cuesta credibilidad.
- Publicar solo cuando hay promoción. Entrena a la gente a esperar descuento.

## Una precaución importante

Cuidado con el lenguaje de resultados. En Colombia los cosméticos se rigen por notificación sanitaria ante el **INVIMA**, y prometer que algo *cura* acné, *elimina* arrugas o *borra* manchas te expone a un problema regulatorio y, peor, a devoluciones de clientas decepcionadas. Habla de *apariencia*, *sensación*, *hidratación*, *luminosidad*. Es más creíble y no te mete en líos.

## El límite de lo que puedo darte hoy

El formato con mayor potencial en skincare es el de **ingredientes y formulación** —de dónde viene, cómo se hace, qué lleva y qué no. Es lo que convierte una crema en una marca. No te lo desarrollé porque sigo sin saber cómo están hechos tus productos; te lo pregunté cuando armamos la propuesta de valor y quedó pendiente. Si Aurora tiene ingredientes andinos, si Luna se formuló para clima seco, si hay laboratorio propio o elaboración artesanal, ese material solo puede salir de ti y probablemente sea tu contenido más fuerte.

Si me cuentas eso, te armo un calendario de 4 semanas con piezas concretas por día, ya repartidas entre Aurora, Sol y Luna con la proporción 4-3-2-1 que definimos.

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Te lo planteo con un principio: **no se le gana a una guerra de precios peleándola, se le gana haciendo que tus precios no sean comparables.** Botica Verde y Skin Lab solo pueden competirte por precio si la clienta puede poner tu producto al lado del suyo y ver dos cifras equivalentes. Todo lo que sigue busca romper esa comparación.

## Las capas de diferenciación, de la más frágil a la más defendible

| Capa | Qué tan copiable | Tiempo en que te copian |
|---|---|---|
| Precio y promoción | Total | Días |
| Empaque y estética | Alta | Semanas |
| Formatos de contenido | Alta | 1–2 meses |
| Especialización de nicho | Media | 6+ meses |
| Servicio y experiencia postventa | Media-baja | Requiere cambiar su operación |
| Marca personal (tú) | **Imposible** | Nunca |
| Comunidad y datos propios de clientas | **Imposible** | Nunca |

La conclusión práctica: cada peso de esfuerzo que pongas en las tres últimas filas rinde más que diez en las tres primeras.

---

## 1. Vende arquitectura, no productos sueltos

Tu ventaja más inmediata es que tienes **rostro, maquillaje y cuerpo en tres niveles de precio**. Eso te permite algo que un producto individual no puede: vender **combinaciones**.

Arma paquetes con nombre propio:

- **"Rutina completa"** → Aurora + Sol + Luna
- **"Empieza aquí"** → Luna + Sol
- **"Solo rostro"** → Aurora + Luna

En el momento en que vendes un paquete, la clienta ya no compara "tu crema contra su crema". Compara una rutina armada contra tres compras separadas de marcas distintas. **Nadie puede igualar el precio de una combinación que no tiene.**

Y esto es lo importante: el paquete te sube el ticket promedio sin bajar el precio de nada. Es lo contrario a un descuento.

## 2. Estrecha el nicho hasta que ellos no puedan seguirte

Botica Verde y Skin Lab probablemente le hablan a "mujeres que quieren cuidar su piel". Es un mercado que se gana con presupuesto, y ahí perderías.

Tu jugada es elegir un segmento tan definido que atenderlo bien te haga la opción obvia, y que para ellos moverse hacia allá implique abandonar su base actual. Opciones que encajan con tu portafolio:

- **Piel en clima de altura.** Bogotá a 2.600 metros: aire seco, radiación alta, deshidratación. Ya te lo mencioné para contenido, pero como posicionamiento es más fuerte: *"formulado y pensado para tu piel en Bogotá"*.
- **La mujer que quiere verse arreglada sin maquillaje evidente.** Aquí Sol es el ancla y el skincare es el soporte: la piel cuidada es lo que permite usar poco maquillaje. Es un discurso que integra tus tres productos de forma natural.
- **Primera rutina real.** Mujeres de 22–30 que salieron del jabón y el agua y no saben por dónde empezar. Luna es la puerta, y tú eres quien las guía. Ese acompañamiento es tu producto real.

Elige **uno**. Un nicho a medias no es un nicho.

## 3. Compite en experiencia, que es donde una tienda pequeña gana

Esto es lo que casi nadie hace bien y no cuesta dinero, cuesta atención:

**Antes de comprar** — Diagnóstico por WhatsApp. Cinco preguntas y le recomiendas qué producto le sirve y cuál *no* le sirve. Decirle a alguien "todavía no compres Aurora, empieza con Luna" genera más confianza que cualquier anuncio, y además protege tu tasa de devoluciones.

**Al recibir** — Nota escrita a mano con su nombre. Instrucciones claras de cómo y en qué orden usar lo que compró. Una muestra pequeña de otro producto de la línea: es tu mejor herramienta para mover a alguien de Luna hacia Sol o Aurora.

**Después** — Mensaje al día 7 preguntando cómo va, no vendiendo. Mensaje al día 25 con recordatorio de recompra. Esto es lo que convierte una venta en una clienta, y la recompra es el terreno donde una marca sin identidad no puede competir.

## 4. Tú eres el diferenciador que no pueden clonar

"Botica Verde" y "Skin Lab" suenan a marca, no a persona. Si tú apareces —tu cara, tu criterio, tus decisiones, por qué escogiste vender esto— construyes algo que ellos tendrían que inventar desde cero.

La gente no le es leal a una crema. Le es leal a alguien en quien confía.

Esto pesa especialmente en **Aurora**: un precio premium necesita una razón humana. "Es caro porque X" dicho por una persona con nombre funciona; dicho por un logo, no.

---

## Qué hacer cuando ellos bajen precios

Va a pasar. El protocolo:

**No igualar.** Si igualas una vez, entrenas a tus clientas a esperar tu descuento y destruyes el margen de Aurora de forma permanente.

**Agregar valor en lugar de restar precio.** Envío gratis, producto adicional, muestra, asesoría, tamaño extra. El costo para ti es menor y no toca tu precio de lista.

**Usar descuentos solo con condición y fecha.** Nunca "20% en todo". Sí "envío gratis en tu segunda compra" o "10% si armas la rutina completa". El descuento condicionado premia comportamiento; el descuento abierto solo regala margen.

**Blindar Aurora.** Ese producto no se descuenta nunca. Si alguna vez necesitas agresividad en precio, hazla en Luna, que es tu producto de adquisición y su función es que la clienta entre.

---

## Lo que necesitas averiguar tú (y es rápido)

Todo lo anterior asume cosas sobre Botica Verde y Skin Lab que no sé. Antes de comprometerte con un ángulo, dedica dos horas a esto y llénalo:

| Qué revisar | Botica Verde | Skin Lab |
|---|---|---|
| Rango de precios (más bajo / más alto) | | |
| ¿Cubren rostro, maquillaje y cuerpo? | | |
| ¿A quién le hablan explícitamente? | | |
| ¿Aparece una persona o solo la marca? | | |
| ¿Venden paquetes o solo unidades? | | |
| ¿Mencionan Bogotá o el clima? | | |
| ¿Qué dicen las reseñas negativas? | | |

La última fila es la más útil de todas. **Sus quejas recurrentes son tu posicionamiento gratis.** Si a ambos les reclaman demoras de envío, tu diferencial es entrega en 24 horas en Bogotá. Si les reclaman que nadie responde, el tuyo es asesoría real por WhatsApp. Esas son diferencias que la clienta percibe *antes* de comparar precios.

Si me pasas esa tabla llena, te digo cuál de los tres nichos del punto 2 está libre y cuál ya está ocupado — y con eso queda cerrada la propuesta de valor que dejamos a medias al principio.

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Te lo armo con un criterio de fondo: **un primer trimestre no se mide por rentabilidad, se mide por aprendizaje.** Si evalúas el trimestre 1 con la vara de "¿ya gané plata?", vas a apagar cosas que apenas estaban dando señal. Lo que tienes que salir a comprobar en 90 días es: qué producto adquiere mejor, cuánto cuesta traer una clienta, y si la clienta vuelve.

Y una restricción práctica: **máximo 8 KPIs.** Más que eso, con una sola persona operando, no se miden — se anotan y se olvidan.

---

## Los 3 KPIs que mandan (si solo pudieras medir tres)

| KPI | Cómo se calcula | Por qué es este |
|---|---|---|
| **CAC** (costo de adquisición) | Pauta total del mes ÷ clientas nuevas del mes | Es tu techo de crecimiento. Sin esto, no sabes si escalar o frenar |
| **Valor a 90 días por clienta** | Ingreso total generado por una cohorte ÷ número de clientas de esa cohorte | Es el número que justifica a Luna. Sin él, Luna parece mal negocio |
| **Tasa de recompra a 60–90 días** | Clientas con 2+ compras ÷ clientas totales de la cohorte | Es la prueba de si tu escalera Luna → Sol → Aurora existe de verdad o es solo una idea bonita |

Si al final del trimestre solo tienes estos tres bien medidos, el trimestre fue un éxito.

---

## El tablero completo: 8 KPIs en cuatro niveles

### Nivel negocio (2)
- **Ventas totales del mes** y **ticket promedio**. El ticket promedio es el que te dice si los paquetes ("Rutina completa", "Empieza aquí") están funcionando. Si lanzas paquetes y el ticket no se mueve, no se están vendiendo, aunque existan en la tienda.

### Nivel producto (2)
- **Mezcla de ventas por producto** (% de unidades de Aurora / Sol / Luna).
- **Producto de primera compra** — cuál es la puerta de entrada real.

Este segundo es el más subestimado de la lista. Tu estrategia entera asume que Luna es la puerta y Aurora el destino. **Puede que estés equivocada**, y solo un trimestre de datos lo dice. Si resulta que Sol es la puerta de entrada más frecuente, hay que reconstruir la pauta y el contenido alrededor de eso.

### Nivel canal (2)
- **CAC por canal** (Meta separado de Google separado de influencers).
- **Tasa de conversión de la tienda** (visitas → compras).

La conversión de tienda va aquí y no en "negocio" por una razón: si está por debajo de ~1%, tu problema no es de canales ni de contenido, es de tienda —fotos, precios visibles, costo de envío, medios de pago, velocidad en celular. Y en ese caso, meter más pauta es echar agua en un balde roto.

### Nivel contenido y WhatsApp (2)
- **Alcance de no-seguidores** en Instagram/TikTok (no seguidores nuevos, no likes). Es la única métrica orgánica que predice crecimiento real.
- **Tasa de cierre en WhatsApp** — conversaciones iniciadas ÷ conversaciones que terminan en venta.

Esta última la incluyo porque en tu caso WhatsApp no es soporte, es punto de venta. Si entran 100 conversaciones y cierras 12, ahí hay un problema de guion o de tiempos de respuesta que vale más plata que cualquier optimización de anuncio.

---

## Qué mirar mes a mes (no todo se mide desde el día 1)

**Mes 1 — Instalar medición, no juzgar resultados**

No tomes ninguna decisión de apagar o escalar este mes. Lo que tiene que quedar listo:
- Pixel de Meta funcionando y eventos de compra registrando bien
- Un registro de dónde llegó cada clienta nueva (así sea a mano, en una hoja)
- Etiquetas en WhatsApp por producto comprado
- Base de referencia: cuánto vendes y a qué ticket, para tener contra qué comparar

KPIs a mirar: conversión de tienda, alcance de no-seguidores, tasa de cierre en WhatsApp.

**Mes 2 — Primeras lecturas de canal**

Ya hay volumen para leer CAC por canal y mezcla de producto. Aquí sí puedes cortar creativos y públicos que claramente no funcionan. Lo que **todavía no** puedes juzgar: si Luna vale la pena. Es demasiado pronto, no ha habido tiempo de recompra.

**Mes 3 — El mes de la verdad**

Aquí llegan las cohortes del mes 1 a los 60–90 días. Recién ahora puedes responder la pregunta central: **¿la clienta que entró por Luna volvió y compró Sol o Aurora?** Ese dato es el que valida o tumba toda la estrategia de escalera de precios que armamos.

---

## Rangos de referencia (úsalos con cuidado)

No son metas ni promesas, son órdenes de magnitud para que sepas si estás muy lejos de lo normal:

| Métrica | Zona de alarma | Zona aceptable | Zona buena |
|---|---|---|---|
| Conversión de tienda | < 1% | 1,5% – 2,5% | > 3% |
| Recompra a 90 días | < 10% | 15% – 25% | > 30% |
| Cierre en WhatsApp | < 10% | 20% – 30% | > 35% |
| CAC vs. valor a 90 días | CAC > valor | CAC ≈ ⅓ del valor | CAC < ¼ del valor |

La última fila es la más importante y la más malinterpretada: **es normal y saludable que la primera compra de Luna no cubra el CAC.** Lo que tiene que cubrirlo es el valor acumulado a 90 días. Si mides Luna contra su venta inicial, la vas a matar.

---

## Umbrales de decisión (decídelos ahora, no en el momento)

Escribe estos números antes de empezar, porque en caliente uno se enamora de las campañas:

- **Apagar un creativo:** menos de X conversiones después de gastar 3–4 veces tu ticket promedio.
- **Escalar un público:** CAC estable por debajo de tu objetivo durante 2 semanas seguidas. Subes presupuesto máximo 20–30% cada 3 días, no de golpe.
- **Detenerte a revisar la tienda:** conversión bajo 1% con tráfico decente. Pausa la pauta en lugar de subirla.
- **Reconsiderar el nicho:** si al mes 3 la recompra sigue bajo 10%, el problema no es adquisición — es que el producto o la experiencia no está enamorando a nadie.

---

## Lo que NO deberías medir este trimestre

- **Seguidores.** No pagan nada. Mide alcance de no-seguidores.
- **Likes y comentarios como fin.** Sirven como diagnóstico de un creativo, no como resultado del negocio.
- **ROAS diario.** En volúmenes pequeños el ruido diario te va a hacer tomar decisiones absurdas. Lee ROAS semanal, mínimo.
- **Todo lo de Botica Verde y Skin Lab como KPI.** Su actividad es información de contexto para la tabla comparativa que te dejé, no una métrica tuya. Medir competencia semana a semana solo genera ansiedad y te empuja a reaccionar en precio, que es justo lo que quieres evitar.

---

## Formato: una sola hoja, dos ritmos

**Revisión semanal (15 minutos, lunes):** ventas de la semana, gasto en pauta, conversaciones de WhatsApp y cuántas cerraron, qué pieza de contenido tuvo mejor alcance.

**Revisión mensual (1 hora, primer día del mes):** los 8 KPIs completos, mezcla por producto, CAC por canal, y la cohorte del mes anterior. Aquí se toman las decisiones de presupuesto.

Una hoja de cálculo basta. No compres herramientas de analítica este trimestre.

---

## Lo que me falta para ponerle números a esto

Te di rangos genéricos porque hay dos datos que sigo sin tener y que convertirían esta lista en metas concretas:

1. **Presupuesto mensual de pauta.** Sin eso no puedo calcular tu CAC objetivo ni decirte cuántas clientas nuevas es realista esperar en 90 días.
2. **Los precios reales de Aurora, Sol y Luna, y su margen.** Sé el posicionamiento de cada uno, pero no las cifras. El margen de Luna define cuánto puedes gastar para adquirir una clienta, y el precio de Aurora define cuánto vale que suba la escalera. Con eso te calculo el CAC máximo tolerable por producto.

Si me das esos dos, te cambio los rangos por metas numéricas para cada mes del trimestre — y de paso queda listo el reparto de presupuesto por canal que quedó pendiente.

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

# Campaña de 4 semanas — **Aurora**

*(set de cuidado facial, tu producto premium — Bogotá)*

---

## Premisa de la que parte todo el plan

**Aurora no se vende por alcance, se vende por confianza acumulada.** Eso cambia la mecánica: una campaña de 4 semanas para un producto premium no es un embudo de adquisición fría, es una **secuencia de convencimiento** que se apoya en gente que ya te conoce.

Dos consecuencias prácticas:

1. El peso del presupuesto va a **públicos cálidos** (quienes ya compraron Luna o Sol, quienes te siguen, quienes vieron contenido), no a desconocidos.
2. En 4 semanas **no vas a poder medir recompra ni valor a 90 días** de Aurora. Lo digo desde ahora para que no evalúes la campaña con la métrica equivocada: se mide por **conversaciones calificadas y conversión de público cálido**, no por volumen de clientas nuevas.

Y una regla que no se rompe: **Aurora no se descuenta.** La mecánica de conversión no es precio, es acceso y acompañamiento.

---

## 1. Objetivo

**Objetivo principal**
Vender **Aurora** a la base cálida existente y validar cuál argumento (autoridad, prueba social o precio-por-uso) mueve la aguja en premium.

**Objetivos secundarios**
- Activar la escalera: convertir compradoras de **Luna** y **Sol** en compradoras de **Aurora**.
- Construir el activo que **Aurora** necesita a largo plazo: un banco de testimonios y un diario de resultados propio.
- Subir el ticket promedio vía el paquete **"Rutina completa"** (Aurora + Sol + Luna) sin tocar el precio de lista de Aurora.

**Objetivo declarado como número**
Como no tengo tu presupuesto ni el precio de **Aurora**, te doy la fórmula para que la llenes hoy:

> Meta de unidades de Aurora = (presupuesto de pauta del mes ÷ CAC máximo tolerable) × tasa de cierre esperada en WhatsApp

Con **CAC máximo tolerable de Aurora = 25–30% de su precio de venta** como techo prudente para un premium en primera compra.

---

## 2. Audiencia

Tres segmentos, en orden estricto de prioridad y de presupuesto:

| # | Segmento | Quién es | % del presupuesto | Por qué |
|---|---|---|---|---|
| **A1** | **Clientas de Luna y Sol** | Ya compraron, ya confían, ya tienen el producto en casa | **40%** | Es el público más barato y el que valida tu escalera de precios. Aquí Aurora no es un riesgo, es un ascenso |
| **A2** | **Cálidos sin comprar** | Seguidores, quienes vieron +50% de tus Reels, visitantes de la tienda últimos 90 días, conversaciones de WhatsApp sin cierre | **40%** | Ya te conocen pero no dieron el paso. El freno casi siempre es precio o duda de eficacia — ambos se resuelven con argumento, no con descuento |
| **A3** | **Frío calificado** | Mujeres 28–45, Bogotá, interés en skincare / cosmética natural / dermatología estética. Y **públicos similares (1–2%) construidos sobre tus compradoras**, no sobre seguidores | **20%** | Es el más caro y el que menos convierte en premium. Va aquí solo para no secar el embudo, no para cargar la campaña |

**Perfil de la compradora de Aurora (hipótesis a validar en las 4 semanas):**
Mujer de 28–45 en Bogotá, con ingreso propio, que ya pasó la etapa de probar cremas al azar y busca **una rutina que funcione y no tener que pensar más en el tema**. Le importa el resultado y la practicidad, no la novedad. Compara antes de comprar, y pregunta antes de pagar — por eso WhatsApp es decisivo.

**A quién NO le hablas en esta campaña:** a quien busca su primera crema y a quien pregunta por lo más económico. Esa persona entra por **Luna**, y meterla en la campaña de **Aurora** solo te sube el costo y te ensucia los datos.

---

## 3. Canales y rol de cada uno

| Canal | Rol en la campaña de Aurora | Peso |
|---|---|---|
| **Instagram (orgánico: Reels + Stories)** | Motor de argumento. Aquí se construye la razón para creer en Aurora | Alto |
| **Meta Ads (retargeting)** | Músculo principal de conversión, sobre A1 y A2 | **Alto — la mayor parte del presupuesto** |
| **WhatsApp Business** | **Donde se cierra Aurora.** Diagnóstico, objeciones, cierre. Ningún premium se vende sin conversación | Crítico |
| **Meta Ads (frío)** | Solo A3, presupuesto contenido, para alimentar retargeting de las semanas 3 y 4 | Bajo |
| **Micro-influencers bogotanas (2–3, de 5k–30k)** | Prueba social externa. Se contactan en semana 1, publican en semana 3 | Medio |
| **Google Search (marca)** | Defensivo: que quien busque "Aurora" + tu marca te encuentre y no aterrice en Botica Verde o Skin Lab | Bajo pero obligatorio |
| **Email** | Refuerzo de los envíos de WhatsApp, mismo mensaje | Bajo |

**Fuera de esta campaña:** marketplaces y TikTok pago. Aurora en marketplace pierde margen y pierde el dato de la clienta, que es justo lo que necesitas para la escalera.

---

## 4. Mensaje principal

**Mensaje central de la campaña**

> **Aurora no es una crema más. Es la rutina de rostro completa que deja de hacerte adivinar.**
> Pensada para lo que tu piel enfrenta en Bogotá: aire seco, radiación alta, cambios de clima en el mismo día.

**Bajadas por segmento**

| Segmento | Mensaje |
|---|---|
| **A1 (clientas de Luna/Sol)** | *"Ya conoces cómo trabajamos. Aurora es el paso que le faltaba a tu rutina."* |
| **A2 (cálidos)** | *"Llevas tiempo mirando Aurora. Cuéntame cómo está tu piel y te digo si es para ti — o si todavía no."* |
| **A3 (frío)** | *"Tu piel se comporta distinto en Bogotá. Aurora está pensada para eso."* |

**Los tres pilares de prueba** (cada pieza de la campaña debe apoyarse en uno):

1. **Autoridad** — sabes de piel y lo demuestras explicando, no vendiendo.
2. **Prueba social** — clientas reales, diario de resultados, testimonios sin producción.
3. **Precio por uso** — desglose honesto: cuánto dura Aurora, cuántas aplicaciones, cuánto cuesta al día. Es el argumento que desarma la objeción de precio sin bajarlo.

**Cuidado con el lenguaje:** apariencia, sensación, hidratación, luminosidad. Nunca *cura*, *elimina* ni *borra*. Regulación INVIMA, y además es más creíble.

**Mecánica de conversión (en lugar de descuento):**
- **"Diagnóstico Aurora"** por WhatsApp: 5 preguntas y le dices si Aurora le sirve — incluso si la respuesta es *"todavía no, empieza con Luna"*. Esa honestidad es la que cierra premium.
- **Paquete "Rutina completa"** (Aurora + Sol + Luna) a precio de paquete: sube el ticket y hace que Aurora no sea comparable contra el producto suelto de nadie.
- Valor agregado, nunca precio: envío en 24h en Bogotá, guía impresa de uso, muestra de Sol o Luna, nota escrita a mano.

---

## 5. Las 4 semanas

### Semana 1 — Autoridad (cero venta directa)

**Objetivo:** ganar el derecho a hablar de un producto caro y llenar los públicos de retargeting.

| Frente | Acciones |
|---|---|
| Orgánico | 3 Reels educativos de un solo punto: *"por qué tu piel se descama aunque te eches crema"*, *"el orden correcto de una rutina"*, *"lo que el clima de Bogotá le hace a tu piel"*. Sin mencionar Aurora, o mencionarla al final sin insistir |
| Stories | Arranca el **diario de resultados de Aurora** — día 1, misma luz, misma hora. Corre las 4 semanas completas |
| Meta Ads | Solo A3 frío con los Reels educativos, presupuesto bajo. Objetivo: video views / tráfico, **no** conversión |
| WhatsApp | Deja listas las respuestas guardadas del "Diagnóstico Aurora" y etiqueta tu base por producto ya comprado |
| Influencers | Contacta 4–5 micro-influencers bogotanas, cierra 2–3. Envía Aurora esta semana para que publiquen en semana 3 |
| Google | Activa campaña de marca (tu nombre + "Aurora") |

**No vendas esta semana.** El público cálido de las semanas 3 y 4 se construye aquí.

---

### Semana 2 — Prueba y demostración

**Objetivo:** hacer visible que Aurora funciona y qué contiene.

| Frente | Acciones |
|---|---|
| Orgánico | 2 Reels de textura y aplicación de **Aurora** en primer plano, sonido real, sin música. 1 Reel *"me arreglo contigo"*: Aurora en rostro → Luna en cuerpo → Sol en maquillaje (la pieza que muestra tu portafolio completo sin explicarlo) |
| Stories | Corte semanal del diario (día 7). Caja de preguntas: *"¿qué te frena de Aurora?"* — las respuestas son tu guion de la semana 3 |
| Meta Ads | Abre **retargeting sobre A2** con las piezas de textura y la rutina completa. Mantén A3 frío al mismo nivel bajo |
| WhatsApp | Primer envío a **A1**: clientas de Luna y Sol. Mensaje personal, no masivo: *"vi que compraste Luna hace unas semanas, ¿cómo te ha ido?"* → y de ahí a Aurora |
| Prueba social | Pide testimonio a 3–5 clientas actuales de Aurora. Capturas de WhatsApp con permiso, o video corto sin guion |

---

### Semana 3 — Conversión (la semana fuerte)

**Objetivo:** cerrar. Es la semana con más presupuesto y más presión de mensaje.

| Frente | Acciones |
|---|---|
| Mecánica | Lanza el **"Diagnóstico Aurora"** como llamado a la acción central en todos los canales. CTA único: *"escríbeme y te digo si Aurora es para ti"* |
| Oferta | Abre el paquete **"Rutina completa"** (Aurora + Sol + Luna) con fecha de cierre real al final de la semana 4 |
| Orgánico | 1 Reel de **precio por uso** de Aurora (cuánto dura, cuánto cuesta al día, qué incluye el set). 1 Reel de objeciones: *"por qué Aurora cuesta lo que cuesta"*. 1 Reel de testimonio de clienta real |
| Stories | Corte del diario (día 14 — el primero con diferencia visible). Testimonios recibidos. Recordatorio del diagnóstico |
| Meta Ads | **Máximo presupuesto sobre A1 y A2.** Creativos: testimonio, precio por uso, paquete. A3 frío sigue bajo |
| Influencers | Publican esta semana. Coordina que su contenido caiga entre miércoles y viernes |
| WhatsApp | Segundo envío a A1 con el paquete. Seguimiento uno a uno de todos los diagnósticos abiertos y sin cerrar |
| Email | Réplica del mensaje de WhatsApp |

---

### Semana 4 — Cierre y reactivación

**Objetivo:** convertir a los indecisos y recuperar conversaciones abiertas.

| Frente | Acciones |
|---|---|
| Orgánico | Cierre del diario (día 21–28): la pieza completa, antes y después. Es tu activo más valioso y te sirve todo el año. 1 Reel de preguntas frecuentes sobre Aurora |
| Stories | Últimos días del paquete. Testimonios de quienes compraron durante la campaña |
| Meta Ads | Retargeting agresivo pero **corto**: quienes visitaron la página de Aurora y no compraron en los últimos 14 días. Mensaje de cierre de paquete |
| WhatsApp | Barrido de **todas** las conversaciones sin cierre de las semanas 2 y 3. Este barrido suele ser la fuente #1 de ventas de la semana |
| Cierre | Se cierra el paquete en la fecha anunciada. **Cúmplelo** — si lo extiendes, entrenas a tus clientas a no creerte las fechas |
| Análisis | Consolida datos y decide qué se queda en operación permanente |

---

## 6. Reparto de presupuesto de pauta

Por porcentaje, para que aplique a cualquier monto:

| | S1 | S2 | S3 | S4 |
|---|---|---|---|---|
| **% del total** | 15% | 25% | **35%** | 25% |
| A1 clientas | — | 35% | 45% | 40% |
| A2 cálidos | — | 45% | 40% | 50% |
| A3 frío | 100% | 20% | 15% | 10% |

**Si tu presupuesto mensual es menor a ~1,5 millones COP:** elimina A3 por completo y corre la campaña solo sobre A1 y A2. Con poco presupuesto, público frío en premium es dinero quemado.

---

## 7. Métricas de éxito

### Las 4 que definen si la campaña funcionó

| KPI | Cómo se mide | Referencia |
|---|---|---|
| **Unidades de Aurora vendidas** | Conteo directo | Contra tu promedio mensual previo de Aurora — ese es el único punto de comparación válido |
| **CAC de Aurora** | Pauta total ÷ compradoras nuevas de Aurora | Techo: 25–30% del precio de Aurora |
| **Tasa de cierre del Diagnóstico Aurora** | Diagnósticos cerrados en venta ÷ diagnósticos iniciados | Aceptable 20–30% / bueno >35% |
| **Migración desde Luna y Sol** | Compradoras de Aurora que ya eran clientas ÷ total de compradoras de Aurora | **Esta es la métrica estratégica.** Valida tu escalera de precios completa |

### Secundarias (diagnóstico, no juicio)

| KPI | Qué te dice |
|---|---|
| Diagnósticos iniciados por semana | Si el mensaje genera intención |
| Ticket promedio del período | Si el paquete "Rutina completa" está moviendo la aguja |
| % de ventas de Aurora dentro del paquete vs. suelta | Si conviene mantener el paquete después |
| Conversión de la página de Aurora | Si el problema es tráfico o es la página |
| Alcance de no-seguidores | Si el contenido está saliendo de tu burbuja |
| CAC por segmento (A1 / A2 / A3) | **Dónde poner el presupuesto el próximo mes** |

### Guardrails — si esto pasa, hay que parar y revisar

| Señal | Qué significa | Qué haces |
|---|---|---|
| Conversión de la página de Aurora <1% con tráfico decente | El problema es la página, no la pauta | Pausa el presupuesto y arregla fotos, descripción, envío, medios de pago |
| CAC de A3 frío >2× el de A2 al final de la semana 2 | Frío no funciona para premium en tu caso | Apaga A3 y pásalo a A1/A2 |
| Muchos diagnósticos, poco cierre (<10%) | El freno es precio o el guion de WhatsApp | Refuerza precio-por-uso y prueba social, revisa tiempos de respuesta |
| Cero migración desde Luna/Sol al final de la semana 3 | La escalera no está funcionando como asumimos | Es el hallazgo más importante de la campaña. Replantear el rol de Luna |
| Presión interna por descontar Aurora | — | **No.** Si necesitas agresividad de precio, hazla en Luna |

### Lo que NO mides en estas 4 semanas
Recompra de Aurora, valor a 90 días, seguidores nuevos, likes, ROAS diario. Muy pronto o irrelevante.

---

## 8. Lo que sigue pendiente y sí cambia este plan

Te entregué el plan completo y ejecutable, pero hay tres vacíos que arrastramos de nuestras conversaciones anteriores:

1. **Presupuesto mensual de pauta** → convierte los porcentajes en pesos y la fórmula del objetivo en una meta de unidades.
2. **Precio y margen de Aurora** → define tu CAC máximo real, en lugar del rango de 25–30% que usé como supuesto.
3. **Cómo está hecha Aurora** — ingredientes, formulación, origen, laboratorio. Te lo pregunté cuando armamos tu propuesta de valor y cuando hablamos de contenido de skincare, y quedó pendiente las dos veces.

El tercero es el que más pesa aquí. **El mensaje que te di se sostiene en autoridad, prueba social y precio por uso — los tres argumentos disponibles cuando no se puede hablar de formulación.** Para un producto premium, el argumento más fuerte casi siempre es *qué lleva y por qué*. Si Aurora tiene ingredientes andinos, algo formulado específicamente para clima de altura, o elaboración artesanal, ese es el eje que reescribiría el mensaje central y las piezas de la semana 2.

Y falta la tabla comparativa de **Botica Verde** y **Skin Lab**. Si alguno de los dos ya tiene un set facial premium con el mismo argumento de "pensado para Bogotá", el ángulo climático deja de ser tuyo y hay que cambiarlo antes de la semana 1.

Dime esos datos y ajusto el plan con cifras concretas y el mensaje afinado.


## Respuesta completa

# Campaña de 4 semanas — **Aurora**

*(set de cuidado facial, tu producto premium — Bogotá)*

---

## Premisa de la que parte todo el plan

**Aurora no se vende por alcance, se vende por confianza acumulada.** Eso cambia la mecánica: una campaña de 4 semanas para un producto premium no es un embudo de adquisición fría, es una **secuencia de convencimiento** que se apoya en gente que ya te conoce.

Dos consecuencias prácticas:

1. El peso del presupuesto va a **públicos cálidos** (quienes ya compraron Luna o Sol, quienes te siguen, quienes vieron contenido), no a desconocidos.
2. En 4 semanas **no vas a poder medir recompra ni valor a 90 días** de Aurora. Lo digo desde ahora para que no evalúes la campaña con la métrica equivocada: se mide por **conversaciones calificadas y conversión de público cálido**, no por volumen de clientas nuevas.

Y una regla que no se rompe: **Aurora no se descuenta.** La mecánica de conversión no es precio, es acceso y acompañamiento.

---

## 1. Objetivo

**Objetivo principal**
Vender **Aurora** a la base cálida existente y validar cuál argumento (autoridad, prueba social o precio-por-uso) mueve la aguja en premium.

**Objetivos secundarios**
- Activar la escalera: convertir compradoras de **Luna** y **Sol** en compradoras de **Aurora**.
- Construir el activo que **Aurora** necesita a largo plazo: un banco de testimonios y un diario de resultados propio.
- Subir el ticket promedio vía el paquete **"Rutina completa"** (Aurora + Sol + Luna) sin tocar el precio de lista de Aurora.

**Objetivo declarado como número**
Como no tengo tu presupuesto ni el precio de **Aurora**, te doy la fórmula para que la llenes hoy:

> Meta de unidades de Aurora = (presupuesto de pauta del mes ÷ CAC máximo tolerable) × tasa de cierre esperada en WhatsApp

Con **CAC máximo tolerable de Aurora = 25–30% de su precio de venta** como techo prudente para un premium en primera compra.

---

## 2. Audiencia

Tres segmentos, en orden estricto de prioridad y de presupuesto:

| # | Segmento | Quién es | % del presupuesto | Por qué |
|---|---|---|---|---|
| **A1** | **Clientas de Luna y Sol** | Ya compraron, ya confían, ya tienen el producto en casa | **40%** | Es el público más barato y el que valida tu escalera de precios. Aquí Aurora no es un riesgo, es un ascenso |
| **A2** | **Cálidos sin comprar** | Seguidores, quienes vieron +50% de tus Reels, visitantes de la tienda últimos 90 días, conversaciones de WhatsApp sin cierre | **40%** | Ya te conocen pero no dieron el paso. El freno casi siempre es precio o duda de eficacia — ambos se resuelven con argumento, no con descuento |
| **A3** | **Frío calificado** | Mujeres 28–45, Bogotá, interés en skincare / cosmética natural / dermatología estética. Y **públicos similares (1–2%) construidos sobre tus compradoras**, no sobre seguidores | **20%** | Es el más caro y el que menos convierte en premium. Va aquí solo para no secar el embudo, no para cargar la campaña |

**Perfil de la compradora de Aurora (hipótesis a validar en las 4 semanas):**
Mujer de 28–45 en Bogotá, con ingreso propio, que ya pasó la etapa de probar cremas al azar y busca **una rutina que funcione y no tener que pensar más en el tema**. Le importa el resultado y la practicidad, no la novedad. Compara antes de comprar, y pregunta antes de pagar — por eso WhatsApp es decisivo.

**A quién NO le hablas en esta campaña:** a quien busca su primera crema y a quien pregunta por lo más económico. Esa persona entra por **Luna**, y meterla en la campaña de **Aurora** solo te sube el costo y te ensucia los datos.

---

## 3. Canales y rol de cada uno

| Canal | Rol en la campaña de Aurora | Peso |
|---|---|---|
| **Instagram (orgánico: Reels + Stories)** | Motor de argumento. Aquí se construye la razón para creer en Aurora | Alto |
| **Meta Ads (retargeting)** | Músculo principal de conversión, sobre A1 y A2 | **Alto — la mayor parte del presupuesto** |
| **WhatsApp Business** | **Donde se cierra Aurora.** Diagnóstico, objeciones, cierre. Ningún premium se vende sin conversación | Crítico |
| **Meta Ads (frío)** | Solo A3, presupuesto contenido, para alimentar retargeting de las semanas 3 y 4 | Bajo |
| **Micro-influencers bogotanas (2–3, de 5k–30k)** | Prueba social externa. Se contactan en semana 1, publican en semana 3 | Medio |
| **Google Search (marca)** | Defensivo: que quien busque "Aurora" + tu marca te encuentre y no aterrice en Botica Verde o Skin Lab | Bajo pero obligatorio |
| **Email** | Refuerzo de los envíos de WhatsApp, mismo mensaje | Bajo |

**Fuera de esta campaña:** marketplaces y TikTok pago. Aurora en marketplace pierde margen y pierde el dato de la clienta, que es justo lo que necesitas para la escalera.

---

## 4. Mensaje principal

**Mensaje central de la campaña**

> **Aurora no es una crema más. Es la rutina de rostro completa que deja de hacerte adivinar.**
> Pensada para lo que tu piel enfrenta en Bogotá: aire seco, radiación alta, cambios de clima en el mismo día.

**Bajadas por segmento**

| Segmento | Mensaje |
|---|---|
| **A1 (clientas de Luna/Sol)** | *"Ya conoces cómo trabajamos. Aurora es el paso que le faltaba a tu rutina."* |
| **A2 (cálidos)** | *"Llevas tiempo mirando Aurora. Cuéntame cómo está tu piel y te digo si es para ti — o si todavía no."* |
| **A3 (frío)** | *"Tu piel se comporta distinto en Bogotá. Aurora está pensada para eso."* |

**Los tres pilares de prueba** (cada pieza de la campaña debe apoyarse en uno):

1. **Autoridad** — sabes de piel y lo demuestras explicando, no vendiendo.
2. **Prueba social** — clientas reales, diario de resultados, testimonios sin producción.
3. **Precio por uso** — desglose honesto: cuánto dura Aurora, cuántas aplicaciones, cuánto cuesta al día. Es el argumento que desarma la objeción de precio sin bajarlo.

**Cuidado con el lenguaje:** apariencia, sensación, hidratación, luminosidad. Nunca *cura*, *elimina* ni *borra*. Regulación INVIMA, y además es más creíble.

**Mecánica de conversión (en lugar de descuento):**
- **"Diagnóstico Aurora"** por WhatsApp: 5 preguntas y le dices si Aurora le sirve — incluso si la respuesta es *"todavía no, empieza con Luna"*. Esa honestidad es la que cierra premium.
- **Paquete "Rutina completa"** (Aurora + Sol + Luna) a precio de paquete: sube el ticket y hace que Aurora no sea comparable contra el producto suelto de nadie.
- Valor agregado, nunca precio: envío en 24h en Bogotá, guía impresa de uso, muestra de Sol o Luna, nota escrita a mano.

---

## 5. Las 4 semanas

### Semana 1 — Autoridad (cero venta directa)

**Objetivo:** ganar el derecho a hablar de un producto caro y llenar los públicos de retargeting.

| Frente | Acciones |
|---|---|
| Orgánico | 3 Reels educativos de un solo punto: *"por qué tu piel se descama aunque te eches crema"*, *"el orden correcto de una rutina"*, *"lo que el clima de Bogotá le hace a tu piel"*. Sin mencionar Aurora, o mencionarla al final sin insistir |
| Stories | Arranca el **diario de resultados de Aurora** — día 1, misma luz, misma hora. Corre las 4 semanas completas |
| Meta Ads | Solo A3 frío con los Reels educativos, presupuesto bajo. Objetivo: video views / tráfico, **no** conversión |
| WhatsApp | Deja listas las respuestas guardadas del "Diagnóstico Aurora" y etiqueta tu base por producto ya comprado |
| Influencers | Contacta 4–5 micro-influencers bogotanas, cierra 2–3. Envía Aurora esta semana para que publiquen en semana 3 |
| Google | Activa campaña de marca (tu nombre + "Aurora") |

**No vendas esta semana.** El público cálido de las semanas 3 y 4 se construye aquí.

---

### Semana 2 — Prueba y demostración

**Objetivo:** hacer visible que Aurora funciona y qué contiene.

| Frente | Acciones |
|---|---|
| Orgánico | 2 Reels de textura y aplicación de **Aurora** en primer plano, sonido real, sin música. 1 Reel *"me arreglo contigo"*: Aurora en rostro → Luna en cuerpo → Sol en maquillaje (la pieza que muestra tu portafolio completo sin explicarlo) |
| Stories | Corte semanal del diario (día 7). Caja de preguntas: *"¿qué te frena de Aurora?"* — las respuestas son tu guion de la semana 3 |
| Meta Ads | Abre **retargeting sobre A2** con las piezas de textura y la rutina completa. Mantén A3 frío al mismo nivel bajo |
| WhatsApp | Primer envío a **A1**: clientas de Luna y Sol. Mensaje personal, no masivo: *"vi que compraste Luna hace unas semanas, ¿cómo te ha ido?"* → y de ahí a Aurora |
| Prueba social | Pide testimonio a 3–5 clientas actuales de Aurora. Capturas de WhatsApp con permiso, o video corto sin guion |

---

### Semana 3 — Conversión (la semana fuerte)

**Objetivo:** cerrar. Es la semana con más presupuesto y más presión de mensaje.

| Frente | Acciones |
|---|---|
| Mecánica | Lanza el **"Diagnóstico Aurora"** como llamado a la acción central en todos los canales. CTA único: *"escríbeme y te digo si Aurora es para ti"* |
| Oferta | Abre el paquete **"Rutina completa"** (Aurora + Sol + Luna) con fecha de cierre real al final de la semana 4 |
| Orgánico | 1 Reel de **precio por uso** de Aurora (cuánto dura, cuánto cuesta al día, qué incluye el set). 1 Reel de objeciones: *"por qué Aurora cuesta lo que cuesta"*. 1 Reel de testimonio de clienta real |
| Stories | Corte del diario (día 14 — el primero con diferencia visible). Testimonios recibidos. Recordatorio del diagnóstico |
| Meta Ads | **Máximo presupuesto sobre A1 y A2.** Creativos: testimonio, precio por uso, paquete. A3 frío sigue bajo |
| Influencers | Publican esta semana. Coordina que su contenido caiga entre miércoles y viernes |
| WhatsApp | Segundo envío a A1 con el paquete. Seguimiento uno a uno de todos los diagnósticos abiertos y sin cerrar |
| Email | Réplica del mensaje de WhatsApp |

---

### Semana 4 — Cierre y reactivación

**Objetivo:** convertir a los indecisos y recuperar conversaciones abiertas.

| Frente | Acciones |
|---|---|
| Orgánico | Cierre del diario (día 21–28): la pieza completa, antes y después. Es tu activo más valioso y te sirve todo el año. 1 Reel de preguntas frecuentes sobre Aurora |
| Stories | Últimos días del paquete. Testimonios de quienes compraron durante la campaña |
| Meta Ads | Retargeting agresivo pero **corto**: quienes visitaron la página de Aurora y no compraron en los últimos 14 días. Mensaje de cierre de paquete |
| WhatsApp | Barrido de **todas** las conversaciones sin cierre de las semanas 2 y 3. Este barrido suele ser la fuente #1 de ventas de la semana |
| Cierre | Se cierra el paquete en la fecha anunciada. **Cúmplelo** — si lo extiendes, entrenas a tus clientas a no creerte las fechas |
| Análisis | Consolida datos y decide qué se queda en operación permanente |

---

## 6. Reparto de presupuesto de pauta

Por porcentaje, para que aplique a cualquier monto:

| | S1 | S2 | S3 | S4 |
|---|---|---|---|---|
| **% del total** | 15% | 25% | **35%** | 25% |
| A1 clientas | — | 35% | 45% | 40% |
| A2 cálidos | — | 45% | 40% | 50% |
| A3 frío | 100% | 20% | 15% | 10% |

**Si tu presupuesto mensual es menor a ~1,5 millones COP:** elimina A3 por completo y corre la campaña solo sobre A1 y A2. Con poco presupuesto, público frío en premium es dinero quemado.

---

## 7. Métricas de éxito

### Las 4 que definen si la campaña funcionó

| KPI | Cómo se mide | Referencia |
|---|---|---|
| **Unidades de Aurora vendidas** | Conteo directo | Contra tu promedio mensual previo de Aurora — ese es el único punto de comparación válido |
| **CAC de Aurora** | Pauta total ÷ compradoras nuevas de Aurora | Techo: 25–30% del precio de Aurora |
| **Tasa de cierre del Diagnóstico Aurora** | Diagnósticos cerrados en venta ÷ diagnósticos iniciados | Aceptable 20–30% / bueno >35% |
| **Migración desde Luna y Sol** | Compradoras de Aurora que ya eran clientas ÷ total de compradoras de Aurora | **Esta es la métrica estratégica.** Valida tu escalera de precios completa |

### Secundarias (diagnóstico, no juicio)

| KPI | Qué te dice |
|---|---|
| Diagnósticos iniciados por semana | Si el mensaje genera intención |
| Ticket promedio del período | Si el paquete "Rutina completa" está moviendo la aguja |
| % de ventas de Aurora dentro del paquete vs. suelta | Si conviene mantener el paquete después |
| Conversión de la página de Aurora | Si el problema es tráfico o es la página |
| Alcance de no-seguidores | Si el contenido está saliendo de tu burbuja |
| CAC por segmento (A1 / A2 / A3) | **Dónde poner el presupuesto el próximo mes** |

### Guardrails — si esto pasa, hay que parar y revisar

| Señal | Qué significa | Qué haces |
|---|---|---|
| Conversión de la página de Aurora <1% con tráfico decente | El problema es la página, no la pauta | Pausa el presupuesto y arregla fotos, descripción, envío, medios de pago |
| CAC de A3 frío >2× el de A2 al final de la semana 2 | Frío no funciona para premium en tu caso | Apaga A3 y pásalo a A1/A2 |
| Muchos diagnósticos, poco cierre (<10%) | El freno es precio o el guion de WhatsApp | Refuerza precio-por-uso y prueba social, revisa tiempos de respuesta |
| Cero migración desde Luna/Sol al final de la semana 3 | La escalera no está funcionando como asumimos | Es el hallazgo más importante de la campaña. Replantear el rol de Luna |
| Presión interna por descontar Aurora | — | **No.** Si necesitas agresividad de precio, hazla en Luna |

### Lo que NO mides en estas 4 semanas
Recompra de Aurora, valor a 90 días, seguidores nuevos, likes, ROAS diario. Muy pronto o irrelevante.

---

## 8. Lo que sigue pendiente y sí cambia este plan

Te entregué el plan completo y ejecutable, pero hay tres vacíos que arrastramos de nuestras conversaciones anteriores:

1. **Presupuesto mensual de pauta** → convierte los porcentajes en pesos y la fórmula del objetivo en una meta de unidades.
2. **Precio y margen de Aurora** → define tu CAC máximo real, en lugar del rango de 25–30% que usé como supuesto.
3. **Cómo está hecha Aurora** — ingredientes, formulación, origen, laboratorio. Te lo pregunté cuando armamos tu propuesta de valor y cuando hablamos de contenido de skincare, y quedó pendiente las dos veces.

El tercero es el que más pesa aquí. **El mensaje que te di se sostiene en autoridad, prueba social y precio por uso — los tres argumentos disponibles cuando no se puede hablar de formulación.** Para un producto premium, el argumento más fuerte casi siempre es *qué lleva y por qué*. Si Aurora tiene ingredientes andinos, algo formulado específicamente para clima de altura, o elaboración artesanal, ese es el eje que reescribiría el mensaje central y las piezas de la semana 2.

Y falta la tabla comparativa de **Botica Verde** y **Skin Lab**. Si alguno de los dos ya tiene un set facial premium con el mismo argumento de "pensado para Bogotá", el ángulo climático deja de ser tuyo y hay que cambiarlo antes de la semana 1.

Dime esos datos y ajusto el plan con cifras concretas y el mensaje afinado.