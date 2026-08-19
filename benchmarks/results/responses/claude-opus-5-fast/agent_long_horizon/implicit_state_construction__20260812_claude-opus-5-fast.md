# Claude Opus 5 Fast — agent_long_horizon/implicit_state_construction

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 5.72 | quality: 7.0
- latency_total: 117.697s | tokens_per_second: 114.3
- input_tokens: 33468 | output_tokens: 13478

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

Sí, Camila, me queda claro. Resumo lo que registro para que confirmes que no distorsioné nada:

**Tu negocio**
- Tienda online con base en Colombia.
- Mercado actual: Bogotá únicamente.

**Tu portafolio (3 productos)**
| Producto | Categoría | Posicionamiento de precio |
|---|---|---|
| **Aurora** | Set de cuidado facial | Premium |
| **Sol** | Kit de maquillaje natural | Medio |
| **Luna** | Crema corporal | Entrada |

**Competencia directa**
- Botica Verde (Bogotá)
- Skin Lab (Bogotá)

Con eso ya tengo la base. Para afinar cualquier plan de campaña, cuando quieras me puedes ir sumando datos como:
- Cuál de los tres te deja mejor margen y cuál vende más hoy.
- Canales que ya usas (Instagram, TikTok, Meta Ads, marketplaces, WhatsApp).
- Presupuesto mensual aproximado y ticket promedio.
- Si tienes base de clientes recurrentes o casi todo es venta nueva.

¿Por dónde quieres empezar: una campaña puntual, diferenciación frente a esos dos competidores, o un plan general para los tres productos?

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Aquí van tres versiones de dos oraciones cada una, con ángulos distintos. Elige la que más se parezca a lo que realmente eres:

**Opción A — Enfoque "ritual completo"**
> Somos la marca bogotana que te acompaña en todo el ritual: rostro, maquillaje y cuerpo, con tres productos pensados para funcionar juntos, no por separado. Puedes entrar por donde te alcance hoy —Luna, Sol o Aurora— y subir de nivel cuando tu piel y tu bolsillo lo pidan.

**Opción B — Enfoque "escalera de acceso"**
> Creemos que el cuidado de la piel de calidad no debería empezar en un precio premium: por eso construimos un portafolio que arranca en Luna y llega hasta Aurora, sin cambiar de marca ni de estándar. Cada mujer en Bogotá encuentra su punto de entrada, y la marca crece con ella.

**Opción C — Enfoque "natural sin sacrificar resultado"**
> Hacemos cuidado facial, maquillaje y corporal de origen natural que sí se nota en la piel, sin obligarte a elegir entre ingredientes limpios y resultados reales. Tres productos, un solo criterio de formulación, y una marca que puedes conocer entera sin salir de Bogotá.

---

**Mi recomendación:** la **A** o la **B**, porque ambas apalancan algo que Botica Verde y Skin Lab difícilmente pueden copiar rápido: tener una **escalera de precios coherente dentro de un portafolio pequeño y curado**. "Natural" (opción C) es un territorio que probablemente Botica Verde ya ocupa por nombre, así que competir ahí de frente es más costoso.

Dos cosas que me ayudarían a afinarla de verdad:
1. **¿Qué te diferencia en producto?** (ingredientes, formulación local, libre de crueldad, empaque, resultados en X días)
2. **¿Cómo se posicionan Botica Verde y Skin Lab?** Uno suena más herbal/artesanal y el otro más clínico/científico —si es así, tienes un espacio libre en el medio que vale oro.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Con lo que sé de ti —venta 100% online, solo Bogotá, y una escalera de precios de Luna a Aurora— priorizaría así. La lógica de fondo: **usa el producto de entrada para captar y el premium para monetizar**, no al revés.

## Capa 1: los que no son negociables (empieza aquí)

**1. Instagram + Reels — tu vitrina principal**
Es donde vive tu categoría en Colombia y donde tu compradora compara antes de decidir. Contenido orgánico centrado en rostro y maquillaje (Aurora y Sol se venden por demostración: textura, aplicación, antes/después). Luna es más difícil de vender en video, así que úsala como gancho de oferta, no como protagonista de contenido.

**2. WhatsApp Business — tu verdadero canal de cierre**
En Colombia, el ticket premium rara vez se cierra en un checkout frío. Aurora, por precio, casi seguro necesita conversación: dudas de tipo de piel, foto del producto real, confirmación de envío. Monta catálogo, respuestas rápidas y etiquetas por producto de interés. Es el canal con mejor conversión y costo casi cero.

**3. Meta Ads (Instagram/Facebook) con geocerca en Bogotá**
Tu única plaza es Bogotá, así que toda la pauta va segmentada ahí — eso te da una ventaja de eficiencia frente a marcas nacionales que diluyen presupuesto. Estructura mínima:
- **Frío → Luna o Sol.** Precio de entrada, oferta clara, objetivo: primera compra.
- **Retargeting → Aurora.** A quien ya te compró o visitó mucho. Aurora casi nunca debe ser tu anuncio de adquisición fría; el CAC no te va a cuadrar.

## Capa 2: cuando la Capa 1 ya funciona

**4. TikTok (orgánico primero, pauta después)**
Bajo costo de alcance y formato ideal para maquillaje natural. **Sol es tu producto para TikTok**, no Aurora. Prueba 3-4 semanas de orgánico antes de meter peso.

**5. Google Search — solo marca y categoría de alta intención**
Poco volumen, pero altísima intención. Dos frentes: defender tus nombres de marca (Aurora, Sol, Luna + tu tienda) y pujar por búsquedas tipo "set cuidado facial Bogotá". También puja por **Botica Verde** y **Skin Lab**: quien busca a un competidor por nombre ya está en modo compra, y es de los tráficos más baratos que vas a encontrar.

**6. Micro-influencers bogotanas (5k–50k)**
Creadoras locales, no nacionales. Pídeles contenido con derechos de uso para pauta — vale más que el post en sí. Regalo de Sol o Luna para prueba; Aurora solo a perfiles ya validados.

**7. Email + WhatsApp de retención**
Aquí está tu margen real: quien compró Luna o Sol es tu mejor prospecto para Aurora. Flujo mínimo: bienvenida, post-compra a 15 días (cuidado del producto), y ascenso a Aurora a los 30-45 días.

## Capa 3: después, y con criterio

**Marketplaces (Mercado Libre, Falabella, Dafiti)** te dan volumen, pero comisión alta, cliente que no es tuyo y presión de precio. Si entras, hazlo **solo con Luna** como producto de captación. Nunca metas Aurora ahí: erosiona el posicionamiento premium que estás construyendo.

**Pinterest** solo si ya te sobra contenido. No lo priorizaría.

## Reparto sugerido de presupuesto

| Destino | % |
|---|---|
| Meta Ads – frío (Luna/Sol) | 45% |
| Meta Ads – retargeting (Aurora) | 25% |
| Google Search (marca + competidores) | 15% |
| Contenido / micro-influencers | 15% |

---

**El error a evitar:** repartir esfuerzo igual entre los tres productos. Aurora es tu utilidad pero tu peor producto de adquisición; Luna es tu peor margen pero tu mejor puerta de entrada. Los canales deben reflejar eso.

Para ajustar esto de verdad me sirven dos datos que aún no me has dado: **tu presupuesto mensual aproximado** y **si hoy ya tienes clientes recurrentes** o casi todo es venta nueva. Con recurrencia, la Capa 1 se inclina mucho más hacia retención y Aurora se vuelve muc

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Te doy una cadencia **sostenible**, no la ideal de manual. El error más común en marcas de 1-3 personas es arrancar con 2 posts diarios y morir en la semana 5; la consistencia vale más que el volumen.

## Instagram — tu canal principal

| Formato | Frecuencia | Rol |
|---|---|---|
| **Reels** | 3–4 / semana | Alcance nuevo. Es el único formato que te trae gente que no te conoce. |
| **Carrusel o post estático** | 1–2 / semana | Educación y confianza. Ingredientes, rutina, comparativas. |
| **Stories** | 5–7 días / semana, 3–5 por día | Cierre y calidez. Aquí es donde empujas a WhatsApp. |

Si tienes que recortar, recorta carruseles antes que Reels, y nunca recortes Stories: son lo más barato de producir y lo que más convierte en tu tipo de negocio.

**Rotación de producto sugerida en Reels (ciclo de 4 semanas):**
- 4-5 piezas de **Sol** (es el más demostrable: aplicación, look completo, "maquillaje natural en 5 minutos")
- 4-5 piezas de **Aurora** (texturas, rutina de noche, tipo de piel, resultados)
- 2-3 piezas de **Luna** (aquí sí funciona como oferta o combo, no como protagonista)
- 2-3 piezas de **marca sin producto** (tu proceso, por qué Bogotá, formulación, tu cara)

Esa última categoría es la que la mayoría omite y es justamente la que te diferencia de Botica Verde y Skin Lab, que probablemente publican solo producto.

## TikTok — solo cuando entres en Capa 2

**4–5 por semana, mínimo.** TikTok castiga la cadencia baja mucho más que Instagram; publicar 2 veces por semana ahí es casi no existir. Si no puedes sostener 4, mejor no abras el canal todavía.

La buena noticia: **el 70% puede ser reciclado de tus Reels** con otro gancho en los primeros 2 segundos. No produzcas contenido nuevo desde cero para TikTok al principio. Y como te decía, **Sol es tu producto de TikTok** — el maquillaje natural rinde ahí mucho mejor que el skincare premium.

## WhatsApp — cuidado con la frecuencia

- **Estados:** 3–4 por semana. Es tu Stories de bajo esfuerzo, mismo material.
- **Difusiones a lista:** **máximo 2 al mes.** Aquí sí hay riesgo real: WhatsApp es un canal invasivo y una difusión de más te cuesta bloqueos y reportes. Resérvalas para lanzamientos, restock o promoción con fecha límite.

## Email — cuando ya tengas lista

**2–3 al mes** de contenido/campaña, más los flujos automáticos que corren solos (bienvenida, post-compra, ascenso a Aurora). No mezcles: los automáticos no cuentan contra esa frecuencia.

## Semana tipo

| | Lun | Mar | Mié | Jue | Vie | Sáb | Dom |
|---|---|---|---|---|---|---|---|
| **Reel** | ✓ | | ✓ | | ✓ | ✓ | |
| **Carrusel** | | ✓ | | | | | ✓ |
| **Stories** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Estado WA** | | ✓ | | ✓ | | ✓ | |

## Lo que hace que esto sea sostenible: grabar por bloques

No grabes a diario. **Un bloque de 3–4 horas cada 15 días** te da 6–8 Reels. Monta la luz una sola vez, cámbiate de ropa 3 veces para que no parezca el mismo día, y graba todo de corrido. Edita en otra sesión.

Esa es la diferencia real entre sostener la cadencia y abandonarla al segundo mes.

## Versión mínima viable

Si esta semana no puedes con todo, el piso irreducible es:
- **2 Reels/semana**
- **Stories 5 días/semana**
- **1 carrusel/semana**

Con eso mantienes presencia. Por debajo de ahí, el algoritmo deja de mostrarte y el esfuerzo se pierde.

---

Dos cosas que seguirían afinando esto: **¿estás produciendo el contenido tú sola o tienes ayuda?** y **¿tienes ya banco de fotos/video de los tres productos, o hay que crearlo desde cero?** Si es desde cero, te armaría primero un plan de producción de 2 semanas antes de comprometerte a cualquier cadencia.

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Te ordeno esto por **función**, no por formato, porque en skincare el contenido que trae gente nueva casi nunca es el mismo que cierra la venta. Y en tu caso hay un matiz importante: **Aurora y Luna son skincare, pero se venden con lógicas distintas** — Aurora se vende con evidencia y educación, Luna con sensorialidad y hábito.

## 1. Contenido de alcance (traer gente que no te conoce)

**Textura en macro.** Producto en la mano, en la espátula, extendiéndose sobre la piel. Es el formato más "adictivo" de la categoría y el que mejor rinde en Reels sin que tengas que hablar. Aurora es tu mejor candidato aquí por ser un set: varias texturas distintas en un solo video.

**Mitos y errores comunes.** "3 cosas que estás haciendo mal con tu protector solar", "no, tu piel no es grasa, está deshidratada". Genera comentarios, y los comentarios son lo que empuja el alcance. Además te posiciona como criterio, no como vendedora.

**El ángulo Bogotá — y este lo subutilizan casi todas.** Estás en una ciudad a 2.600 metros: aire seco, frío, radiación UV altísima incluso nublado, y en temporada seca la piel se resiente muchísimo. Ese es contenido hipersegmentado que ni las marcas nacionales ni los importados pueden hacer con tu credibilidad:
- "Por qué tu piel se reseca más en Bogotá que en la costa"
- "Nublado en Bogotá ≠ sin sol. Lo que la altura le hace a tu piel"
- "Rutina para época seca en Bogotá"

Este ángulo además le da un trabajo claro a **Luna**, que es tu producto más difícil de hacer atractivo en video: el clima seco bogotano es literalmente su razón de existir.

## 2. Contenido de consideración (ya te vio, está evaluando)

**Rutina en orden de aplicación.** Para un set como Aurora esto es crítico: la duda real de quien compra un set es "¿en qué orden lo uso y cuánto me pongo de cada uno?". Un video que resuelve eso elimina fricción de compra y baja tus mensajes repetitivos en WhatsApp.

**Un ingrediente, un video.** Qué hace, para qué tipo de piel, en qué producto tuyo está y por qué lo elegiste. Esto es lo que construye la percepción de premium en Aurora: el precio alto necesita razones visibles.

**"Cuánto rinde y cuánto te dura".** Subestimado y potentísimo para tu premium. Si Aurora dura 3 meses, el mensaje no es el precio total: es el costo por día. Convierte una objeción de precio en un argumento de valor.

**Cómo elegir según tu tipo de piel.** Además de educar, **califica**: quien te escribe después ya llega diciendo "tengo piel mixta", y tu cierre

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Te lo planteo con una premisa: **la guerra de precios solo se evita si el cliente no puede comparar manzana con manzana.** Si tu Aurora y un set de Skin Lab se ven como "lo mismo pero más caro", el precio es lo único que queda. Así que todo lo de abajo apunta a hacer la comparación imposible.

Aviso previo: como aún no me has dicho cómo se posicionan Botica Verde y Skin Lab, trabajo con la hipótesis que te mencioné antes —Botica Verde suena herbal/artesanal, Skin Lab suena clínico/científico—. Si es al revés o ambos están en el mismo territorio, el eje 1 cambia. Confírmame eso cuando puedas.

---

## Eje 1: El territorio del medio (el más defendible)

Si la hipótesis se sostiene, hay un espacio vacío entre "natural pero sin evidencia" y "eficaz pero frío": **natural con rigor**. Ingredientes de origen natural, pero comunicados con concentraciones, tipo de piel y resultados esperados.

Ese posicionamiento es difícil de copiar porque cada competidor tendría que traicionar su propia narrativa: Botica Verde perdería su calidez artesanal al volverse técnica, y Skin Lab pierde autoridad clínica si se vuelve "natural".

## Eje 2: El portafolio como escalera (esto ya lo tienes y no lo estás usando)

Ninguno de los dos puede copiarte esto rápido, porque no es una campaña: es estructura de negocio.

Tú cubres **rostro + maquillaje + cuerpo** con tres precios distintos. Eso te permite decir algo que ellos no: *"puedes empezar en Luna y llegar a Aurora sin cambiar de marca ni de estándar"*.

Cómo se vuelve tangible:
- **Kit ritual completo** (Luna + Sol + Aurora) con un ahorro moderado. No es descuento: es acceso al sistema completo.
- **Programa de ascenso:** quien compró Luna recibe un beneficio para Sol; quien compró Sol, uno para Aurora. Recompensas de trayectoria, no rebajas.
- **Aurora nunca en promoción.** Nunca. Es tu ancla de calidad; si Aurora se descuenta, toda la escalera se desploma.

Con Sol de por medio, además tienes un argumento que un competidor solo de skincare no puede hacer: **la piel cuidada se ve mejor con menos maquillaje**. Aurora y Sol se venden mutuamente.

## Eje 3: Hiperlocalidad — Bogotá como especialidad, no como dirección

Ellos también están en Bogotá, pero apuesto a que lo usan como dato logístico, no como propuesta.

Tú puedes convertirlo en experiencia de producto: **formulada y probada para 2.600 metros**. Aire seco, radiación alta, temporada seca. Esto es defendible porque cualquier competidor que lo copie después parece imitador.

Aterrizado:
- Recomendaciones que cambian según temporada seca o de lluvias.
- Un mini-diagnóstico "tu piel en Bogotá" que te alimenta la lista y segmenta la conversación.
- Entrega y empaque pensados para la ciudad, no genéricos.

## Eje 4: La experiencia post-compra (donde casi nadie compite)

Aquí es donde una tienda pequeña gana sin gastar más:

- **Acompañamiento real por WhatsApp.** No soporte: seguimiento. Mensaje al día 15 preguntando cómo va la piel. Eso no lo hace una marca con miles de pedidos, y para ti cuesta minutos.
- **Unboxing con criterio.** Tarjeta escrita con el nombre de la clienta, orden de uso del set. Es el momento de mayor atención emocional de todo el ciclo y suele estar desaprovechado.
- **Garantía de piel.** "Si en 30 días no ves diferencia, te ayudamos a cambiar de producto dentro del portafolio." Como tienes tres productos, un cambio te retiene a la clienta en lugar de perderla — algo que una marca de un solo producto no puede ofrecer.

## Eje 5: Tú como cara visible

Botica Verde y Skin Lab son nombres. Tú eres una persona. Una fundadora que explica por qué eligió cada ingrediente crea un vínculo que ninguna marca sin rostro replica. Es tu activo más barato y el menos copiable.

---

## Cómo se refleja en precio sin bajarlo

| En vez de… | Haz esto |
|---|---|
| Descuento en Aurora | Muestra el costo por día de uso |
| Rebaja generalizada | Bundle Luna + Sol como puerta de entrada |
| Cupón de bienvenida | Muestra gratis de Luna con la primera compra |
| Black Friday agresivo | Acceso anticipado + regalo para clientas recurrentes |

**La regla:** si vas a ceder valor, cédelo en **producto o servicio**, nunca en precio de lista. Regalar Luna te cuesta el costo de producción; descontar Aurora te cuesta el posicionamiento entero.

## Y si igual te atacan por precio

Sucede: alguien pone su set facial 30% abajo. La respues

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Te propongo un marco con una premisa fuerte: **el primer trimestre no se mide por ventas, se mide por aprendizajes que ya no tengas que volver a comprar.** Si terminas marzo facturando poco pero sabiendo tu CAC real por producto y tu tasa de cierre en WhatsApp, ganaste. Si facturas bien pero no sabes de dónde vino, no puedes repetirlo.

Antes de las métricas, una advertencia sobre tu caso puntual: como todavía no me has dado presupuesto ni si tienes clientas recurrentes, dejo los objetivos en rangos. Los números que importan son los **tuyos del mes 1** — ese es tu baseline y contra eso se mide todo lo demás.

---

## Semana 0: sin esto, los KPIs son ficción

No arranques a medir sin dejar montado:

- **Pixel de Meta + API de Conversiones** (en Colombia el pixel solo pierde bastantes eventos; la API recupera atribución).
- **UTMs en todo enlace**, incluido el de tu bio y el de cada influencer.
- **Etiquetas en WhatsApp Business** por producto de interés y por estado (nuevo / cotizando / cerrado / perdido).
- **Enlaces CTWA distintos por campaña** (click-to-WhatsApp), o mínimo la pregunta "¿cómo nos encontraste?" en el primer mensaje. Sin esto, WhatsApp se vuelve un agujero negro de atribución y es justo donde vas a cerrar Aurora.
- **Una hoja de cálculo semanal.** No necesitas herramienta pagada este trimestre.

---

## Nivel 1: los 5 números de supervivencia (revisión semanal)

Estos van en una sola pantalla. Si solo puedes con cinco, son estos.

| KPI | Cómo se calcula | Por qué |
|---|---|---|
| **Margen de contribución total** | Ingresos − COGS − envío − pasarela − empaque − pauta | El único número que dice si el negocio respira. No mires facturación sola. |
| **Clientas nuevas** | Compradoras únicas por primera vez | Tu motor de crecimiento hoy. |
| **CAC blended** | Pauta total ÷ clientas

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

# Campaña "Aurora" — Plan de 4 semanas

Tu producto más caro es **Aurora**, el set de cuidado facial premium. Todo lo que sigue está construido alrededor de él.

Una advertencia estructural antes de empezar, porque define el diseño completo: **Aurora es tu peor producto de adquisición fría.** Un set premium rara vez se compra en el primer contacto, menos a un precio alto y a una marca que la compradora no conoce. Así que esta campaña **no es "vender Aurora a desconocidos"**. Es calentar, educar y cerrar. La venta fría de Aurora es la excepción, no el plan.

Y la regla que no se rompe en ninguna de las cuatro semanas: **Aurora no se descuenta.** Ni una vez. Es tu ancla de calidad y sostiene la escalera Luna → Sol → Aurora completa.

---

## 1. Objetivo

**Objetivo principal:** convertir a Aurora en compra deliberada, no impulsiva, generando volumen de conversaciones calificadas en WhatsApp que cierren dentro del trimestre.

Lo desgloso en tres niveles porque un set premium tiene ciclo largo y medir solo ventas del día 28 te va a dar una lectura falsa:

| Nivel | Meta a 4 semanas |
|---|---|
| **Primario** | Ventas de Aurora atribuidas a la campaña |
| **Secundario** | Conversaciones calificadas de Aurora abiertas en WhatsApp (aunque cierren en semana 5-7) |
| **Terciario** | Audiencia caliente construida: visitantes de página de Aurora + views 75% de video Aurora |

El terciario importa más de lo que parece: si al día 28 tienes 800 personas que consumieron contenido de Aurora sin comprar, tienes un activo de retargeting para el mes siguiente. Eso vale casi tanto como las ventas.

---

## 2. Audiencia

Ordenadas por probabilidad de cierre. El presupuesto debe reflejar ese orden, no repartirse parejo.

**A1 — Compradoras previas de Sol o Luna (prioridad máxima)**
Ya te pagaron, ya recibieron producto, ya saben que cumples. Es la audiencia natural de ascenso de la escalera. Si tienes recurrencia, aquí está el 40-50% de las ventas de Aurora del mes.

**A2 — Tráfico caliente sin compra**
Visitantes de la página de Aurora, quienes vieron +75% de tus videos de Aurora, quienes escribieron por WhatsApp y no cerraron, engagement de Instagram últimos 90 días.

**A3 — Lookalike de compradoras (1-2%)**
Construida sobre A1. Es tu mejor apuesta de frío, pero sigue siendo frío: aquí Aurora no se vende directo, se presenta.

**A4 — Intención activa en buscador**
Quien busca "set cuidado facial Bogotá", "rutina facial completa", y quien busca **Botica Verde** o **Skin Lab** por nombre. Volumen bajo, intención altísima, costo bajo.

**Perfil transversal:** mujer en Bogotá, 28-45, que ya usa skincare (no la estás iniciando en la categoría — eso es trabajo de Luna), con capacidad de gasto premium y que hoy probablemente compra marcas importadas de farmacia o a alguno de tus dos competidores.

**Segmentación geográfica:** Bogotá cerrada. Es tu ventaja de eficiencia frente a marcas nacionales que diluyen pauta en todo el país.

---

## 3. Mensaje principal

**Concepto rector:**

> **Aurora no es una crema más. Es tu rutina completa, en el orden correcto, formulada para la piel que vive a 2.600 metros.**

Tres razones por las que este ángulo y no otro:

- **"Set completo, en orden"** ataca la objeción real de un set premium: *"¿en qué orden lo uso, cuánto me pongo, y para qué sirve cada cosa?"*. Resolver eso desbloquea la compra.
- **"2.600 metros"** es tu territorio hiperlocal. Ni Botica Verde ni Skin Lab lo están usando como propuesta de producto, y quien lo copie después queda como imitador.
- **No menciona precio.** El precio se neutraliza con costo por día, no con descuento.

**Mensajes de apoyo (uno por semana, ver calendario):**

1. *"Tu piel en Bogotá no es tu piel en la costa."* — el porqué del producto
2. *"Aurora dura X meses. Son $Y al día."* — reencuadre de precio
3. *"Los tres pasos de Aurora, en el orden correcto."* — cómo se usa
4. *"Ella empezó en Luna. Hoy usa Aurora."* — prueba social + escalera

**Lo que NO decimos en toda la campaña:** "oferta", "descuento", "precio especial", "última oportunidad de ahorro". Si hay urgencia, es por **stock o cupo de acompañamiento**, jamás por precio.

---

## 4. Canales y reparto

| Canal | % pauta | Rol específico con


## Respuesta completa

# Campaña "Aurora" — Plan de 4 semanas

Tu producto más caro es **Aurora**, el set de cuidado facial premium. Todo lo que sigue está construido alrededor de él.

Una advertencia estructural antes de empezar, porque define el diseño completo: **Aurora es tu peor producto de adquisición fría.** Un set premium rara vez se compra en el primer contacto, menos a un precio alto y a una marca que la compradora no conoce. Así que esta campaña **no es "vender Aurora a desconocidos"**. Es calentar, educar y cerrar. La venta fría de Aurora es la excepción, no el plan.

Y la regla que no se rompe en ninguna de las cuatro semanas: **Aurora no se descuenta.** Ni una vez. Es tu ancla de calidad y sostiene la escalera Luna → Sol → Aurora completa.

---

## 1. Objetivo

**Objetivo principal:** convertir a Aurora en compra deliberada, no impulsiva, generando volumen de conversaciones calificadas en WhatsApp que cierren dentro del trimestre.

Lo desgloso en tres niveles porque un set premium tiene ciclo largo y medir solo ventas del día 28 te va a dar una lectura falsa:

| Nivel | Meta a 4 semanas |
|---|---|
| **Primario** | Ventas de Aurora atribuidas a la campaña |
| **Secundario** | Conversaciones calificadas de Aurora abiertas en WhatsApp (aunque cierren en semana 5-7) |
| **Terciario** | Audiencia caliente construida: visitantes de página de Aurora + views 75% de video Aurora |

El terciario importa más de lo que parece: si al día 28 tienes 800 personas que consumieron contenido de Aurora sin comprar, tienes un activo de retargeting para el mes siguiente. Eso vale casi tanto como las ventas.

---

## 2. Audiencia

Ordenadas por probabilidad de cierre. El presupuesto debe reflejar ese orden, no repartirse parejo.

**A1 — Compradoras previas de Sol o Luna (prioridad máxima)**
Ya te pagaron, ya recibieron producto, ya saben que cumples. Es la audiencia natural de ascenso de la escalera. Si tienes recurrencia, aquí está el 40-50% de las ventas de Aurora del mes.

**A2 — Tráfico caliente sin compra**
Visitantes de la página de Aurora, quienes vieron +75% de tus videos de Aurora, quienes escribieron por WhatsApp y no cerraron, engagement de Instagram últimos 90 días.

**A3 — Lookalike de compradoras (1-2%)**
Construida sobre A1. Es tu mejor apuesta de frío, pero sigue siendo frío: aquí Aurora no se vende directo, se presenta.

**A4 — Intención activa en buscador**
Quien busca "set cuidado facial Bogotá", "rutina facial completa", y quien busca **Botica Verde** o **Skin Lab** por nombre. Volumen bajo, intención altísima, costo bajo.

**Perfil transversal:** mujer en Bogotá, 28-45, que ya usa skincare (no la estás iniciando en la categoría — eso es trabajo de Luna), con capacidad de gasto premium y que hoy probablemente compra marcas importadas de farmacia o a alguno de tus dos competidores.

**Segmentación geográfica:** Bogotá cerrada. Es tu ventaja de eficiencia frente a marcas nacionales que diluyen pauta en todo el país.

---

## 3. Mensaje principal

**Concepto rector:**

> **Aurora no es una crema más. Es tu rutina completa, en el orden correcto, formulada para la piel que vive a 2.600 metros.**

Tres razones por las que este ángulo y no otro:

- **"Set completo, en orden"** ataca la objeción real de un set premium: *"¿en qué orden lo uso, cuánto me pongo, y para qué sirve cada cosa?"*. Resolver eso desbloquea la compra.
- **"2.600 metros"** es tu territorio hiperlocal. Ni Botica Verde ni Skin Lab lo están usando como propuesta de producto, y quien lo copie después queda como imitador.
- **No menciona precio.** El precio se neutraliza con costo por día, no con descuento.

**Mensajes de apoyo (uno por semana, ver calendario):**

1. *"Tu piel en Bogotá no es tu piel en la costa."* — el porqué del producto
2. *"Aurora dura X meses. Son $Y al día."* — reencuadre de precio
3. *"Los tres pasos de Aurora, en el orden correcto."* — cómo se usa
4. *"Ella empezó en Luna. Hoy usa Aurora."* — prueba social + escalera

**Lo que NO decimos en toda la campaña:** "oferta", "descuento", "precio especial", "última oportunidad de ahorro". Si hay urgencia, es por **stock o cupo de acompañamiento**, jamás por precio.

---

## 4. Canales y reparto

| Canal | % pauta | Rol específico con