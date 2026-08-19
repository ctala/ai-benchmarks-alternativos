# Claude Opus 5 Fast — agent_long_horizon/implicit_state_construction

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 6.77 | quality: 8.5
- latency_total: 117.354s | tokens_per_second: 195.3
- input_tokens: 40048 | output_tokens: 20670

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

Sí, Camila, clarísimo. Te lo resumo para confirmar que lo tengo bien registrado:

**Tu negocio**
- Tienda online en Colombia
- Mercado actual: Bogotá (único, por ahora)

**Tu portafolio (3 productos)**
| Producto | Categoría | Posicionamiento de precio |
|---|---|---|
| **Aurora** | Set de cuidado facial | Premium |
| **Sol** | Kit de maquillaje natural | Medio |
| **Luna** | Crema corporal | Entrada |

**Competencia directa**
- Botica Verde (Bogotá)
- Skin Lab (Bogotá)

Un par de cosas que noto de entrada y que valdrá la pena tener presentes cuando armemos campañas:

1. Tienes una **escalera de precios completa** (entrada → medio → premium), lo cual es ideal para estrategias de captación con Luna y monetización con Aurora.
2. Al ser Bogotá tu único mercado, la segmentación geográfica es simple, pero puedes afinar mucho por localidad (Chapinero, Usaquén, Suba, etc.) y por poder adquisitivo.

Para que las recomendaciones sean más precisas, cuando quieras me puedes ir contando cosas como: ticket promedio, canales que ya usas (Instagram, TikTok, Meta Ads, WhatsApp), si vendes por marketplace o web propia, y en qué se diferencian tus competidores. Pero no es necesario ahora mismo.

¿Por dónde quieres empezar? ¿Una campaña puntual, el plan general, o análisis competitivo?

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

**Propuesta de valor (versión base):**

> Ayudamos a las mujeres de Bogotá a construir una rutina de belleza completa —piel, rostro y cuerpo— con productos naturales y honestos, sin tener que elegir entre calidad y presupuesto. Desde Luna, para empezar sin fricción, hasta Aurora, para quien busca un ritual premium, cada producto está pensado para acompañarte en la etapa en la que estés.

**Variante más corta y punchy, por si la quieres para bio de Instagram o header web:**

> Belleza natural para cada etapa y cada bolsillo: de la crema diaria al ritual premium. Tres productos, una sola promesa: que tu piel se sienta cuidada de verdad.

---

**Dos supuestos que hice y que deberías validar** (porque cambian el mensaje):

1. Que tus productos son **naturales / clean beauty** — lo inferí porque Sol es explícitamente "maquillaje natural", pero no sé si Aurora y Luna comparten ese atributo.
2. Que tu ventaja competitiva frente a **Botica Verde** y **Skin Lab** es la *escalera de precios completa* (cubrir los tres niveles). Si alguno de ellos también lo hace, habría que buscar el diferenciador en otro lado: formulación, origen de ingredientes, marca personal, servicio, tiempos de entrega.

Si me confirmas esos dos puntos, afino la propuesta para que sea defendible y no genérica.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

## Priorización de canales para Bogotá

Te la organizo en tres niveles según lo que debería recibir tu presupuesto y tu tiempo.

---

### 🟢 Nivel 1 — Núcleo (aquí va el 65–70%)

**1. Instagram (orgánico + Meta Ads)**
Sigue siendo el canal natural para belleza en Bogotá. Tu escalera de precios encaja perfecto con la estructura de campañas de Meta:
- **Luna (entrada)** → campañas de conversión frías. Es tu producto de captación: bajo riesgo percibido, ideal para que alguien te compre por primera vez.
- **Sol (medio)** → retargeting a quienes vieron contenido o compraron Luna.
- **Aurora (premium)** → retargeting caliente y públicos similares (lookalike) de tus mejores compradoras. Aurora casi nunca se vende en frío; se vende cuando ya confían en ti.

**2. WhatsApp Business**
En Colombia es prácticamente un canal de ventas, no solo de soporte. Catálogo, respuestas rápidas, y sobre todo: recuperación de carritos y recompra. Para Luna y Sol, que tienen ciclo de reposición, es donde está tu margen más barato.

**3. TikTok orgánico**
Costo de producción bajo, alcance orgánico todavía generoso. Funciona muy bien para "maquillaje natural" (Sol) en formato antes/después y rutinas. No metería pauta aquí todavía; primero valida qué formatos funcionan sin pagar.

---

### 🟡 Nivel 2 — Soporte (20–25%)

**4. Google Search — solo marca y categoría de alta intención**
No compitas por "crema corporal" genérico, es carísimo. Sí puja por:
- Tu propia marca y nombres de producto (Aurora, Sol, Luna) para no perder tráfico
- **Los nombres de Botica Verde y Skin Lab** — es legal en Colombia pujar por marcas de competidores como palabra clave (no puedes usarlas en el texto del anuncio). Tráfico barato y de altísima intención.

**5. Micro-influencers bogotanas (5k–50k seguidores)**
Regalar Luna es barato y genera contenido; enviar Aurora a perfiles más selectos genera aspiracionalidad. Prioriza creadoras con audiencia concentrada en Bogotá sobre cuentas grandes y dispersas.

**6. Email**
No para captar, sino para exprimir la base que ya tienes: secuencia post-compra de Luna → Sol → Aurora. Es el canal que mejor monetiza tu escalera de precios.

---

### 🔴 Nivel 3 — Después (0–10%)

**7. Marketplaces (Mercado Libre, Falabella)**
Te dan volumen, pero comen margen y te quitan el dato del cliente. Además diluyen el posicionamiento premium de Aurora. Yo los dejaría para cuando quieras salir de Bogotá y necesites logística resuelta en otras ciudades.

**8. Pinterest / YouTube**
Buenos para SEO de largo plazo, malos para tracción inmediata. Aún no.

---

### Cómo se conecta con tu embudo

| Etapa | Canal principal | Producto héroe |
|---|---|---|
| Descubrimiento | TikTok orgánico + IG Reels | Sol / Luna |
| Consideración | Meta Ads + micro-influencers | Luna |
| Conversión | WhatsApp + Google marca | Luna → Sol |
| Recompra / upsell | Email + WhatsApp | Sol → Aurora |

---

**Una advertencia:** esta priorización asume que hoy vendes por web propia. Si ya estás vendiendo principalmente por Instagram DM o por un marketplace, el orden cambia bastante —sobre todo el peso que le doy a email y WhatsApp, que dependen de que seas dueña del dato del cliente.

Y sigue pendiente lo de antes: si **Botica Verde** o **Skin Lab** ya dominan Instagram en Bogotá con presupuestos grandes, te convendría no pelear de frente ahí y cargar más hacia TikTok y WhatsApp, donde el costo de entrada es menor. Si me cuentas cómo se mueven ellos, ajusto los porcentajes.

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

## Frecuencia de publicación orgánica

Te la doy en dos versiones: la **realista** (si estás sola o con un apoyo pequeño) y la **ideal** (si tienes equipo o agencia). Empieza por la realista y sube solo cuando la sostengas 6 semanas seguidas.

---

### Instagram

| Formato | Realista | Ideal |
|---|---|---|
| Reels | 3 / semana | 5 / semana |
| Carrusel o post estático | 2 / semana | 3 / semana |
| Stories | 4–5 días / semana, 3–5 slides | Diario, 5–8 slides |

**Cómo repartir el contenido entre tus productos.** No lo dividas en tercios iguales. Sugiero algo así:

- **~45% Sol** — el maquillaje natural es lo más "grabable": antes/después, aplicación, resultado visible. Es tu motor de alcance.
- **~30% Luna** — contenido de rutina y hábito diario. Es tu producto de captación, así que necesita presencia constante y sin fricción.
- **~15% Aurora** — poco volumen, mucha producción. Aurora no se vende por repetición sino por deseo: contenido más cuidado, ritual, textura, empaque.
- **~10% marca** — tú, el detrás de cámara, clientas reales de Bogotá. Esto es lo que te diferencia de Botica Verde y Skin Lab, que probablemente comunican como catálogo.

Las Stories son tu canal de recompra encubierta: encuestas, cajas de preguntas, "¿ya se te acabó tu Luna?". Ahí no vendes, conversas.

---

### TikTok

**Realista: 4 videos / semana. Ideal: 1 diario.**

TikTok premia volumen y consistencia más que calidad de producción, así que aquí sí conviene publicar más que en Instagram aunque el material sea más crudo. La buena noticia: puedes grabar en bloque y reciclar hacia Reels (bajando la marca de agua).

Concentra aquí a **Sol**. El formato "maquillaje natural en 60 segundos" es prácticamente nativo de la plataforma. **Luna** funciona en formato rutina de noche o "3 usos que no sabías". A **Aurora** yo le daría poco espacio orgánico en TikTok por ahora: el público de la plataforma tiene menor disposición a un ticket premium en frío.

---

### WhatsApp (canal + estados)

- **Estados: 3–4 por semana.** Mismo criterio que Stories, más comercial.
- **Difusiones o canal: máximo 1 por semana**, 2 si hay lanzamiento o promoción real.

Aquí el riesgo no es publicar poco, es publicar de más. WhatsApp es un espacio íntimo: si saturas, no te dejan de seguir, te bloquean. Y perder ese contacto es mucho más caro que perder un seguidor de Instagram.

---

### Email

- **Newsletter: cada 15 días.** Semanal solo si tienes algo que decir de verdad.
- **Automatizaciones: siempre activas** y no cuentan como frecuencia porque son individuales — bienvenida, post-compra de Luna a los 21 días sugiriendo Sol, carrito abandonado, y recordatorio de reposición según el producto.

---

### Resumen semanal

| Canal | Piezas / semana |
|---|---|
| Instagram feed (Reels + posts) | 5 |
| Instagram Stories | 4–5 días |
| TikTok | 4 |
| WhatsApp estados | 3–4 |
| WhatsApp difusión | 1 |
| Email | 0,5 |

Son unas **14–15 piezas semanales**, pero con reciclaje real son más bien **6–7 grabaciones** que se adaptan a varios formatos. Un solo día de grabación al mes, bien planeado, te puede cubrir el 70% del mes.

---

**Dos cosas antes de que arranques:**

1. **La consistencia vale más que el volumen.** 3 Reels semanales durante seis meses rinden mucho más que 7 semanales durante tres semanas y luego silencio. Si dudas, baja el número.

2. Esta distribución asume que **Sol** es tu producto con más potencial de alcance orgánico por su formato visual. Si en tu experiencia real Luna es la que más engancha —o la que más vendes—, invertiría los porcentajes: le daría a Luna el peso principal en Instagram y TikTok, y dejaría Sol como apoyo. Tú tienes el dato de qué se mueve mejor; yo estoy infiriendo desde el formato.

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

## Contenido para skincare: lo que realmente mueve la aguja

Antes de entrar: de tus tres productos, los que caen en skincare son **Aurora** (facial premium) y **Luna** (corporal, entrada). **Sol** es maquillaje y juega con otras reglas, así que lo dejo fuera salvo donde se cruzan.

---

### Los formatos, ordenados por rendimiento

**1. Textura en primer plano** ⭐ El más subestimado
Producto extendiéndose sobre piel real, absorción en tiempo real, el dedo que hunde la crema. Es hipnótico, retiene los primeros 3 segundos y no requiere que salgas en cámara. Para **Aurora** es especialmente valioso: la textura *es* el argumento premium. Nadie paga precio alto por algo que se ve como cualquier crema.

**2. Rutina en tiempo real**
"Mi rutina de noche" con pasos numerados. Funciona porque enseña *cómo* usar el producto y reduce la fricción de compra. Aquí **Luna** brilla: es el paso final, el momento de cierre del día. Y muestra que la rutina no termina en la cara — que es justo lo que necesitas para vender crema corporal, una categoría que la gente compra por reposición, no por deseo.

**3. Educación con una sola idea**
Un video, un concepto. "Por qué tu piel se descama en Bogotá." "El orden correcto: ¿sérum o crema primero?" No expliques cinco cosas; explica una bien. Este contenido genera guardados y compartidos, que es la señal que más te ayuda con el algoritmo.

**4. Antes/después honesto**
Mismo ángulo, misma luz, sin filtro, con marca de tiempo visible ("día 1 / día 28"). En skincare la audiencia está entrenada para detectar trampa. Un resultado modesto pero creíble convierte más que uno espectacular y dudoso.

**5. UGC y clientas reales**
Repostear clientas bogotanas con nombre y localidad. Es tu ventaja más difícil de copiar frente a **Botica Verde** y **Skin Lab**: si ellos comunican como catálogo, tú comunicas como vecina.

**6. Detrás de la formulación**
Ingredientes, por qué elegiste cada uno, qué dejaste fuera y por qué. Alimenta directo la promesa de "productos honestos" de tu propuesta de valor. Es el contenido que justifica el precio de **Aurora**.

---

### Tu ángulo local: el clima de Bogotá

Esto es lo que ninguna marca internacional te puede quitar y creo que es tu mejor territorio de contenido.

Bogotá está a 2.600 metros, con aire seco, temperatura baja y **radiación UV alta todo el año** por la altitud. Eso produce problemas de piel muy concretos y muy reconocibles:

- Descamación y tirantez en las mejillas
- Labios y nudillos partidos permanentemente
- Piel que se siente grasa y deshidratada al mismo tiempo
- Quemaduras solares en días nublados, que la gente no espera
- Cambio brusco de sensación al viajar a tierra caliente y volver

Contenido tipo: *"Por qué tu piel de Bogotá no funciona igual que la de Cartagena"*, *"Lo que la altura le hace a tu barrera cutánea"*, *"3 señales de que tu piel está deshidratada, no seca"*. Ahí **Luna** deja de ser "una crema más" y pasa a ser la respuesta a un problema que tu clienta siente todos los días.

---

### Reparto por producto

| Producto | Contenido que mejor le sirve | Objetivo |
|---|---|---|
| **Luna** | Rutina diaria, textura, problema/solución de clima, UGC | Volumen y captación |
| **Aurora** | Ritual, macro de textura, formulación, unboxing, antes/después largo | Deseo y justificación de precio |
| **Cruce Sol + skincare** | "Piel preparada = maquillaje que dura" | Venta cruzada natural |

Ese último punto vale oro: es la forma más orgánica de mover a alguien de un producto a otro dentro de tu escalera.

---

### Lo que no funciona (y sí se ve mucho)

- **Foto de producto sobre fondo blanco.** Cero contexto, cero razón para detenerse.
- **Listas de ingredientes sin traducir.** A nadie le importa el nombre INCI; le importa qué le va a pasar a su piel.
- **Promesas exageradas.** Además de que la audiencia desconfía, en Colombia los cosméticos están regulados por el **INVIMA** y no pueden atribuirse efectos terapéuticos o curativos. Habla de hidratación, luminosidad, confort, textura — no de curar acné, eliminar manchas o tratar enfermedades de la piel. Esto no es solo cumplimiento: los claims moderados generan menos devoluciones y menos reseñas decepcionadas.
- **Copiar el tono de una marca coreana o gringa.** Tu audiencia está en Bogotá y responde a referencias propias.

---

### Cómo se aterriza en tu semana

Recordando los 5 posts de feed semanales que definimos:

| Pieza | Tipo | Producto |
|---|---|---|
| Reel 1 | Textura / satisfying | Aurora |
| Reel 2 | Rutina o problema de clima | Luna |
| Reel 3 | Educación, una idea | Cruce Sol/skincare |
| Post 4 | UGC o testimonio | Luna |
| Post 5 | Carrusel educativo o formulación | Aurora |

---

**Un supuesto que deberías confirmarme:** estoy asumiendo que Aurora y Luna comparten el posicionamiento natural que sí es explícito en Sol. Si Aurora es más bien de perfil técnico o activo (retinol, vitamina C, ácidos), el contenido cambia bastante — pasaría a pesar mucho más la educación sobre ingredientes y la evidencia, y menos el territorio de "natural y honesto".

Y sigue pendiente lo otro: **si Botica Verde o Skin Lab ya tienen tomado el discurso del clima bogotano**, tendríamos que buscarte otro territorio. Si me cuentas cómo comunican, lo ajustamos.

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

## Diferenciación sin bajar precios

La guerra de precios la gana quien tenga más caja o mejores costos, y como no sabes cuál es la estructura de **Botica Verde** ni de **Skin Lab**, entrar ahí es apostar a ciegas. Te propongo seis territorios donde competir, ordenados de más defendible a menos.

---

### 1. El territorio del clima bogotano (tu mejor apuesta)

Ya lo mencioné como línea de contenido, pero puede ser mucho más que eso: puede ser **el eje de tu marca entera**.

La idea: no eres "otra marca natural", eres **la marca formulada para piel de altura**. 2.600 metros, aire seco, UV alta todo el año, cambio brutal cuando viajas a tierra caliente.

Cómo se hace tangible más allá del contenido:
- Un **diagnóstico corto** en tu web: "¿Cómo reacciona tu piel a Bogotá?" → recomienda Luna, Sol o Aurora según respuesta
- Lenguaje de producto adaptado: Luna no es "crema corporal", es "crema para piel que vive en clima seco de altura"
- Guía descargable: *Rutina de temporada seca vs. temporada de lluvia en Bogotá*

Es defendible porque, aunque te lo copien, tú llegaste primero y puedes ser dueña de la conversación si la sostienes 12 meses.

**Riesgo:** si te vas 100% a este territorio, complicas la expansión futura a Medellín o Cartagena. Se resuelve haciéndolo un *punto de partida* ("nacimos en Bogotá, formulamos para clima real") y no una camisa de fuerza.

---

### 2. Ser una persona, no un logo

Este es el diferenciador más barato y el que menos marcas ejecutan bien.

**Botica Verde** y **Skin Lab** suenan a marca corporativa. Tú tienes algo que ellos no pueden fabricar: eres una fundadora real, en Bogotá, con una historia de por qué armaste estos tres productos y no otros.

Concretamente:
- Firma tus emails con tu nombre, no con "el equipo de"
- Sal en cámara al menos una vez por semana
- Cuenta las decisiones difíciles: por qué Aurora cuesta lo que cuesta, qué ingrediente descartaste, qué proveedor cambiaste
- Responde tú los DMs y los WhatsApp los primeros meses

La transparencia radical de precio es especialmente potente para **Aurora**: explicar abiertamente qué parte del precio es formulación, empaque, envío. Convierte el precio alto de objeción en argumento.

---

### 3. El sistema completo, no los productos sueltos

Aquí está tu ventaja estructural real y no la estás explotando.

Tienes cobertura de **rostro (Aurora) + maquillaje (Sol) + cuerpo (Luna)** en tres niveles de precio. Eso te permite vender algo que un competidor con un solo producto estrella no puede: **una rutina resuelta**.

Formas de materializarlo:
- **Kit "Ritual completo"** — los tres productos con descuento por conjunto. Ojo: esto no es guerra de precios, es aumento de ticket. El descuento se financia con el margen del volumen, no con la erosión del precio unitario.
- **Kit "Empieza aquí"** — Luna + muestra de Aurora. Captas barato y siembras el upsell.
- **La lógica de "piel preparada"** — Aurora prepara, Sol se ve mejor, Luna cierra. Es un argumento de venta cruzada que solo tú puedes hacer con tu portafolio.
- **Suscripción de reposición** de Luna cada 45–60 días. Ingreso recurrente y un cliente que ya no compara precios cada mes.

Si Botica Verde o Skin Lab solo tienen skincare, tú eres la única que resuelve el día completo.

---

### 4. Experiencia post-compra

En belleza online colombiana el estándar de servicio es bajo, así que el listón para destacar está sorprendentemente bajo también.

- **Entrega mismo día o siguiente día en Bogotá.** Ser local es una ventaja logística; úsala. Un competidor que despacha nacional no puede igualarte en velocidad dentro de tu ciudad.
- **Seguimiento activo a los 15 días** por WhatsApp: "¿cómo te está yendo con Luna?". Genera reseñas, detecta problemas y abre el upsell sin que parezca venta.
- **Unboxing cuidado en Aurora.** Si vas a cobrar premium, la caja tiene que sostener la promesa. Es de las pocas cosas donde el gasto se percibe directamente como valor.
- **Garantía de satisfacción real.** Elimina el riesgo de la primera compra sin tocar el precio.

---

### 5. Comunidad local

Un grupo o canal de clientas bogotanas, encuentros ocasionales, clientas que aparecen en tu feed con nombre y barrio. Es lento, pero crea un costo de cambio emocional que ningún descuento de la competencia rompe fácil.

Y alimenta gratis tu mejor contenido: el UGC.

---

### 6. Nicho específico

Si quieres afilar aún más: elige un segmento y sé la mejor ahí. Piel sensible, piel madura, embarazo y lactancia, primera rutina para adolescentes. Reduce tu mercado pero te hace inevitable dentro de él.

No lo pondría como prioridad ahora — con un solo mercado y tres productos, estrechar demasiado puede ahogarte. Guárdalo para cuando tengas volumen.

---

### Qué hacer cuando el cliente compara precios

| Objeción | Respuesta que no baja el precio |
|---|---|
| "Skin Lab lo tiene más barato" | Comparar concentración, tamaño, rendimiento por uso. Precio por aplicación, no por frasco. |
| "Aurora está muy cara" | Ofrecer Luna como entrada, no descuento en Aurora. Nunca devalúes tu producto ancla. |
| "No sé si me servirá" | Garantía + diagnóstico + muestra. Es un problema de riesgo, no de precio. |
| "Está fuera de mi presupuesto" | Para eso existe Luna. Tu escalera ya resuelve esto sin tocar márgenes. |

**Regla que te sugiero fijar desde ya:** Aurora nunca entra en descuento directo. Puede entrar en kits, puede tener regalo adjunto, puede tener beneficio por recompra — pero su precio de lista no se mueve. Un premium que se descuenta deja de ser premium y es casi imposible recuperar la percepción.

---

### Por dónde empezaría

**Meses 1–2:** territorio de clima + tu cara en el contenido. Costo cero, impacto inmediato.
**Meses 2–4:** kits y lógica de sistema. Sube ticket sin subir tráfico.
**Meses 3–6:** experiencia post-compra y suscripción de Luna.
**Mes 6+:** comunidad, y nicho si los datos lo piden.

---

**Lo que necesito para afinar esto.** Toda la sección de diferenciación asume que **Botica Verde** y **Skin Lab** no están ya ocupando estos territorios. Si uno de ellos ya es "la marca de la fundadora visible" o ya habla del clima de Bogotá, cambio la recomendación completa — en ese caso te convendría más el eje de sistema completo y experiencia logística, que son más difíciles de copiar rápido.

Concretamente me sirve saber: ¿cuántos productos tiene cada uno?, ¿en qué rango de precio juegan?, ¿comunican como marca personal o corporativa?, ¿despachan nacional o solo Bogotá?

Con eso te armo un mapa de posicionamiento y vemos qué espacio está realmente libre.

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

## KPIs para tu primer trimestre

Antes del listado, un principio que te va a ahorrar mucho ruido: **el trimestre 1 no es para optimizar, es para tener línea base.** Hoy no sabes cuánto te cuesta traer una clienta ni cuántas vuelven. Sin esos dos números, cualquier decisión posterior es intuición disfrazada de dato.

Así que te lo organizo por fases y luego por métrica.

---

### Las 3 métricas que gobiernan todo

Si solo pudieras mirar tres, serían estas:

| # | Métrica | Por qué esta |
|---|---|---|
| 1 | **Margen de contribución total** (ventas − costo producto − envío − pasarela − pauta) | Es lo único que paga tu sueldo. Vender más puede empobrecerte. |
| 2 | **CAC de primera compra** | Define si tu modelo escala o solo funciona con esfuerzo manual |
| 3 | **Tasa de recompra a 90 días** | Tu portafolio de reposición (Luna, Sol) vive o muere aquí |

Todo lo demás son métricas de diagnóstico: sirven para explicar *por qué* estas tres se mueven.

---

### Fase por mes

**Mes 1 — Instrumentar y medir sin juzgar**
No tomes decisiones de canal este mes. Solo asegúrate de estar midiendo bien:
- UTMs en absolutamente todo (incluido el link de tu bio y los estados de WhatsApp)
- Código de descuento único por cada micro-influencer
- Encuesta post-compra de una sola pregunta: *"¿Cómo nos conociste?"* — es imperfecta, pero en Colombia con tanto tráfico de WhatsApp y DM suele ser más honesta que la atribución de plataforma
- Consentimiento explícito para email y WhatsApp (**Ley 1581 de 2012**, habeas data). Registra fecha y origen del consentimiento desde el día uno; después es un dolor de cabeza reconstruirlo.

**Mes 2 — Leer patrones**
Ya tienes 4–8 semanas de datos. Empiezas a ver qué canal trae clientas más baratas y qué producto entra primero.

**Mes 3 — Decidir**
Cortar lo que no funciona, doblar lo que sí. Aquí ya puedes fijar metas numéricas para el trimestre 2 con base en tu propia realidad, no en benchmarks ajenos.

---

### Métricas de negocio

| KPI | Cómo leerlo |
|---|---|
| Ingresos totales | Contexto, no decisión |
| **Ticket promedio (AOV)** | Tu palanca más barata. Subirlo no cuesta tráfico. |
| Unidades por pedido | Mide si los kits están funcionando |
| **Margen de contribución %** | Vigílalo por producto, no solo global |
| Mix de ventas por producto | Aquí está la información más valiosa del trimestre |

Sobre el **mix**: mídelo en unidades *y* en margen. Es perfectamente posible que Luna sea el 60% de tus unidades y el 20% de tu margen. Eso no está mal — Luna es captación — pero necesitas saberlo para no confundir movimiento con rentabilidad.

---

### Métricas de tu escalera de precios

Esta es la sección que no encontrarías en una plantilla genérica, y para tu negocio es la más importante:

| KPI | Qué te dice |
|---|---|
| **% de clientas nuevas que entran por Luna** | Valida (o no) tu hipótesis de producto de captación |
| **Tasa de escalada Luna → Sol o Aurora** | El corazón de tu modelo. Si esto es cercano a cero, tu escalera no es escalera, son tres productos sueltos. |
| **Días hasta la segunda compra** | Define cuándo debe dispararse tu email post-compra |
| **% de pedidos que incluyen 2+ productos** | Mide la venta cruzada |
| **% de ingresos que viene de Aurora** | Si es muy bajo, tu premium es decorativo |

Yo pondría la **tasa de escalada** como el KPI estrella de tu trimestre. Es la que valida la estrategia completa que hemos venido armando.

---

### Adquisición y pauta

| KPI | Nota |
|---|---|
| CAC por canal | Tu número más importante y el que más tarda en estabilizarse |
| **MER** (ingresos totales ÷ pauta total) | Confía más en este que en el ROAS de Meta |
| Tasa de conversión del sitio | Sepárala por dispositivo; móvil será el 85%+ |
| Costo por clic / CTR | Diagnóstico creativo, no decisión de negocio |
| % de tráfico y ventas desde Bogotá | Verifica que la segmentación geográfica esté bien puesta |

**Advertencia sobre ROAS:** Meta va a reportar más ventas de las que realmente causó, sobre todo cuando el cierre ocurre por WhatsApp. Usa el MER como termómetro real y el ROAS solo para comparar anuncios *entre sí* dentro de la misma plataforma.

Y no evalúes a **Aurora** por su ROAS en frío. Ya lo dijimos: Aurora casi no se vende en frío. Su desempeño se mide en retargeting y en recompra, no en captación.

---

### Contenido orgánico

Aquí es donde más gente mide lo que no debe. **Ignora los seguidores.**

| Canal | Qué medir | Qué ignorar |
|---|---|---|
| Instagram | Alcance de **no seguidores**, guardados, compartidos, retención a 3s | Likes, seguidores |
| TikTok | % de reproducción completa, compartidos, clics al perfil | Vistas totales |
| Stories | Toques en stickers, respuestas, clics en link | Vistas |
| WhatsApp | Tasa de respuesta, conversación → venta, **tasa de bloqueo/salida** | Número de contactos |
| Email | Clics (no aperturas), ingreso por email enviado, % de ingresos de flujos automáticos | Tasa de apertura |

Dos vigilancias especiales:

- **Tasa de bloqueo en WhatsApp.** Es tu alarma de saturación. Si sube, baja frecuencia inmediatamente — perder un contacto de WhatsApp es mucho más caro que perder un seguidor.
- **Tasa de apertura de email** ya no es confiable por la protección de privacidad de Apple. Mide clics e ingresos.

Sobre el **territorio de clima bogotano**: mídelo como línea de contenido. Compara guardados y compartidos de esas piezas contra el promedio de tu cuenta. Si en 8 semanas ese contenido no supera claramente tu media, el territorio no está conectando y hay que replantearlo antes de construir la marca entera encima.

---

### Experiencia y retención

| KPI | Meta sugerida |
|---|---|
| Tiempo de entrega en Bogotá | Es tu ventaja competitiva; mídela o no existe |
| % de pedidos entregados a tiempo | >95% |
| Tasa de devolución o reclamo | Vigila si sube tras campañas con claims fuertes |
| Reseñas obtenidas / mes | Insumo directo para tu contenido UGC |
| Respuestas al seguimiento de día 15 | Mide si ese ritual está funcionando |

---

### Tu tablero, en la práctica

**Cada lunes (10 minutos):** ventas de la semana, pauta gastada, MER, pedidos, ticket promedio, contenido con mejor retención.

**Cada mes (1 hora):** CAC por canal, margen por producto, mix de ventas, tasa de recompra, escalada entre productos, tasa de bloqueo en WhatsApp.

Una hoja de cálculo simple basta. No inviertas en herramientas de BI en el trimestre 1.

---

### Reglas de decisión para el cierre del trimestre

Para que no te quedes mirando números sin actuar:

- Si un canal tiene **CAC > margen de contribución de la primera compra** y la recompra a 90 días es baja → pausar o rediseñar
- Si la **tasa de escalada Luna → Sol/Aurora** es marginal → el problema no es el tráfico, es tu comunicación post-compra
- Si **Aurora** aporta muy poco al margen total → el problema es de deseo y contenido, no de precio. Bajarle el precio sería el error más caro que podrías cometer.
- Si el **MER** es sano pero el margen no → tu problema está en costos de envío o producto, no en marketing

---

**Lo que me falta para volver esto accionable con números concretos.** Te di la estructura, pero no puedo darte metas absolutas sin saber: tu **ticket promedio actual**, tu **margen bruto por producto**, si vendes por **web propia o cerrando por DM/WhatsApp** (cambia radicalmente qué puedes medir), y tu **presupuesto mensual de pauta**.

Con esos cuatro datos te armo el tablero con cifras objetivo reales en lugar de rangos genéricos. Y sigue en pie lo de **Botica Verde** y **Skin Lab** — cuando me cuentes cómo se mueven, te agrego dos o tres indicadores de posición competitiva.

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

## Campaña "Aurora" — Plan de 4 semanas

**Producto:** Aurora, tu set de cuidado facial premium (el de mayor precio de tu portafolio).
**Mercado:** Bogotá.
**Regla innegociable del plan:** Aurora **no entra en descuento directo** en ninguna semana. Todo el valor adicional se entrega vía experiencia, obsequio o formato de kit — nunca tocando el precio de lista.

---

## 1. Objetivo

**Objetivo principal**
Convertir a Aurora en un producto con demanda propia y no en un accesorio del catálogo: llevarla de ser un ítem que casi nadie compra a representar una porción relevante de tu margen mensual, vendiendo a audiencia templada y caliente.

**Objetivos secundarios**

| # | Objetivo | Cómo se verifica |
|---|---|---|
| 1 | Activar la escalada desde tu base existente | Compradoras previas de **Luna** o **Sol** que compran **Aurora** |
| 2 | Construir el activo de deseo | Retención de video y guardados en piezas de Aurora |
| 3 | Generar prueba social premium | Reseñas y UGC de Aurora, que hoy probablemente no tienes |
| 4 | Establecer la línea base de CAC de Aurora | Primer dato real de cuánto cuesta vender tu premium |

**Lo que este plan *no* busca:** volumen de pedidos ni clientas nuevas en frío. Aurora no se vende en frío, ya lo hablamos. Si al final del mes tienes pocas unidades pero con margen sano y una base de contenido y reseñas construida, la campaña fue exitosa.

---

## 2. Audiencia

Tres círculos, en orden de prioridad de presupuesto.

### 🔵 Círculo 1 — Tu base (60% del esfuerzo)

La audiencia más rentable de toda la campaña y la que ya es tuya.

- Compradoras previas de **Luna** con más de 30 días desde su compra
- Compradoras previas de **Sol**
- Suscriptoras de email y contactos de WhatsApp que nunca compraron Aurora
- Clientas que compraron 2+ veces (máxima prioridad: ya demostraron confianza)

Aquí no necesitas pauta casi: es email, WhatsApp y Stories.

### 🟣 Círculo 2 — Templada (30%)

- Visitantes de la página de **Aurora** en los últimos 90 días que no compraron
- Engagement de Instagram y TikTok de los últimos 60 días
- Carritos abandonados con Aurora
- Seguidoras que interactuaron con contenido de piel de altura

### ⚪ Círculo 3 — Frío selectivo (10%)

Solo para alimentar los círculos anteriores, **no para vender directo**:

- Lookalike 1% de tus mejores compradoras (mayor ticket histórico)
- Intereses de skincare premium + localidades de Bogotá con mayor poder adquisitivo: Usaquén, Chapinero, Suba (norte), Teusaquillo
- Mujeres 28–50 años

**Perfil de la compradora de Aurora:** no es la que busca el mejor precio. Es la que ya usa skincare, entiende la diferencia entre productos y está dispuesta a pagar por formulación y ritual. Probablemente ya te conoce por **Luna** o **Sol** — por eso el Círculo 1 pesa tanto.

---

## 3. Canales y rol de cada uno

| Canal | Rol en la campaña de Aurora | Peso |
|---|---|---|
| **Instagram orgánico** (Reels + Stories) | Construcción de deseo. El motor narrativo de las 4 semanas. | Alto |
| **Email** | Vehículo principal de escalada desde Luna y Sol. Aquí se explica el precio. | Alto |
| **WhatsApp** | Cierre y consulta personalizada. Aurora es compra consultada. | Alto |
| **Meta Ads (retargeting)** | Reimpactar Círculos 1 y 2. Poco presupuesto, muy dirigido. | Medio |
| **Micro-influencers selectas** | 3–4 perfiles bogotanos, no más. Calidad sobre alcance. | Medio |
| **Google Search (marca)** | Defensiva: capturar quien busca "Aurora" + tu marca tras ver contenido | Bajo |
| **TikTok** | Solo textura y ritual. Sin pauta. | Bajo |

**Fuera de la campaña:** TikTok Ads, marketplaces y prospección fría agresiva. No corresponden al perfil de Aurora en esta etapa.

---

## 4. Mensaje principal

### Concepto rector

> **"Aurora no es una crema más. Es el momento en que tu piel deja de sobrevivir a Bogotá."**

### Por qué este ángulo

Conecta las dos cosas que ya definimos como tu terreno propio: el **clima de altura de Bogotá** (2.600 m, aire seco, UV alta todo el año) y el **ritual premium** que justifica el precio de Aurora. Y te separa de **Botica Verde** y **Skin Lab** en el eje donde ellos difícilmente pueden responder rápido: no compites por ser más natural o más barata, compites por ser la que entiende esta piel, en esta ciudad.

### Mensajes de apoyo

1. **Formulación, no marketing.** Qué lleva Aurora, qué no lleva, y por qué.
2. **El precio explicado.** Transparencia radical: cuánto cuesta por uso, cuánto rinde, en qué se va el valor.
3. **Ritual, no rutina.** Aurora es el paso que se disfruta, no el que se cumple.
4. **Piel preparada.** Aurora hace que **Sol** se vea mejor. Venta cruzada natural dentro de tu escalera.

### Líneas de copy para usar

- *"Tu piel no está seca. Está a 2.600 metros."*
- *"Aurora cuesta lo que cuesta. Te explico exactamente por qué."*
- *"El set que hace que tu maquillaje se vea como debería."*
- *"No lo vas a comprar todos los meses. Esa es la idea."*

**Lo que nunca decimos sobre Aurora:** promesas de curar, eliminar manchas o tratar condiciones de la piel. Los cosméticos en Colombia están regulados por INVIMA y no admiten claims terapéuticos. Hablamos de hidratación, luminosidad, confort y textura.

---

## 5. Desarrollo semana a semana

### 🗓 Semana 1 — Deseo y educación
*"Por qué tu piel se comporta así en Bogotá"*

Ninguna venta directa esta semana. Se construye el problema.

| Canal | Acción |
|---|---|
| IG Reels | 2 piezas: "Lo que la altura le hace a tu barrera cutánea" + macro de textura de **Aurora** absorbiéndose |
| IG Stories | Serie de 4 días: encuesta "¿Sientes tirantez en las mejillas?" → resultados → explicación → teaser de Aurora |
| Email | Envío 1: educativo puro sobre piel de altura. Aurora se menciona al final, sin link de compra agresivo |
| TikTok | 3 videos: textura, ritual nocturno, "3 señales de deshidratación" |
| Meta Ads | Solo campaña de video views a Círculo 3 para construir audiencia de retargeting |
| Micro-influencers | Envío de Aurora a 3–4 perfiles bogotanos. Sin brief de venta: solo pedir uso real durante 3 semanas |

---

### 🗓 Semana 2 — Formulación y precio
*"Te muestro qué hay adentro y cuánto cuesta"*

Aquí se ataca de frente la objeción de precio, sin bajarlo.

| Canal | Acción |
|---|---|
| IG | Carrusel: cada ingrediente de **Aurora**, qué hace, por qué está. Reel: tú hablando del precio a cámara |
| Stories | Caja de preguntas: "¿Qué quieres saber de Aurora?" → responder una por una |
| Email | Envío 2: **desglose de precio**. Cuánto es formulación, empaque, envío. Costo por uso vs. frasco |
| WhatsApp | Estado con el desglose. Difusión única invitando a preguntar por Aurora por chat |
| Meta Ads | Arranca retargeting a Círculo 2 con el video de precio |
| Google | Activar campaña de marca + "Aurora" + nombres de **Botica Verde** y **Skin Lab** como keyword |

---

### 🗓 Semana 3 — Prueba social y escalada
*"Quién ya la está usando"*

La semana de mayor presión comercial hacia tu base.

| Canal | Acción |
|---|---|
| IG | UGC de las influencers (ya llevan 2 semanas de uso). Reposteo de clientas con nombre y localidad |
| Reels | "Piel preparada": **Aurora** + **Sol**, cómo cambia el acabado del maquillaje |
| Email | Envío 3, **segmentado**: a compradoras de Luna → "el siguiente paso de tu rutina". A compradoras de Sol → "por qué tu base se ve mejor con piel preparada" |
| WhatsApp | Mensajes 1 a 1 a clientas recurrentes. No masivo: personalizado, con tu nombre |
| Meta Ads | Retargeting con creativos de testimonio a Círculos 1 y 2 |
| Oferta | Lanzar el **Kit Ritual Completo**: Aurora + Sol + Luna. El ahorro viene del conjunto, no de rebajar Aurora |

---

### 🗓 Semana 4 — Cierre por valor agregado
*"Última semana del ritual"*

Cierre con urgencia legítima, sin descuento.

| Canal | Acción |
|---|---|
| Mecánica de cierre | Toda compra de **Aurora** incluye: **Luna** en tamaño viaje de regalo + empaque especial + consulta 1 a 1 de rutina contigo por WhatsApp. Disponible solo hasta el domingo |
| IG | Reel de unboxing de Aurora. Stories de countdown los últimos 3 días |
| Email | Envío 4 (martes) + recordatorio final (domingo, solo a quienes abrieron o hicieron clic) |
| WhatsApp | Estado diario + difusión el viernes. Cierre 1 a 1 con quienes preguntaron en semanas 2 y 3 |
| Meta Ads | Concentrar presupuesto en carritos abandonados y visitantes de la página de Aurora |
| Post-cierre | A quienes compraron: seguimiento a los 15 días pidiendo reseña |

---

## 6. Distribución sugerida de presupuesto

Sin conocer tu monto de pauta, te doy los porcentajes:

| Destino | % | Nota |
|---|---|---|
| Retargeting Meta (Círculos 1 y 2) | 45% | Concentrar en semanas 3 y 4 |
| Video views frío (Círculo 3) | 15% | Solo semanas 1 y 2, para construir audiencias |
| Google Search marca + competencia | 10% | Barato y de alta intención |
| Producto para influencers | 15% | 3–4 unidades de Aurora |
| Empaque especial + Luna de regalo | 10% | Costo variable, solo por venta cerrada |
| Reserva | 5% | Para doblar lo que funcione en semana 3 |

Nota de margen: el obsequio de **Luna** tamaño viaje y el empaque tienen costo, pero se cargan contra el margen de Aurora sin tocar su precio de lista. Verifica que el margen de contribución de Aurora siga sano después de descontarlos.

---

## 7. Métricas de éxito

### Las tres que definen si la campaña funcionó

| # | KPI | Por qué |
|---|---|---|
| 1 | **Margen de contribución generado por Aurora** en las 4 semanas | Vender Aurora sin margen no tiene sentido |
| 2 | **Tasa de escalada**: % de compradoras previas de Luna o Sol que compran Aurora | Valida tu escalera de precios completa |
| 3 | **CAC de Aurora**, separado por audiencia fría vs. templada | Tu primer dato real. Establece la línea base |

### Métricas de negocio

- Unidades de Aurora vendidas (total y por semana)
- **% de ingresos del mes que aporta Aurora** — el indicador de si tu premium dejó de ser decorativo
- Ticket promedio de los pedidos que incluyen Aurora
- Unidades del **Kit Ritual Completo** vendidas
- % de compras de Aurora que vienen de clientas nuevas vs. existentes

### Métricas de deseo (semanas 1–2)

Estas son las de alerta temprana. Si fallan, el problema aparecerá en ventas dos semanas después.

- Retención a 3 segundos en Reels de Aurora
- **Guardados y compartidos** de piezas de Aurora vs. tu promedio de cuenta
- Alcance en **no seguidores** del contenido de piel de altura
- Respuestas en la caja de preguntas de semana 2

### Métricas de canal

| Canal | Qué mirar |
|---|---|
| Email | Clics e **ingresos por email enviado** (no aperturas) |
| WhatsApp | Conversaciones iniciadas, conversación → venta, y **tasa de bloqueo** |
| Meta Ads | MER global de la campaña, más que el ROAS reportado |
| Google | Clics de marca y conversión asistida |
| Influencers | Ventas por código único + volumen de contenido generado |

### Métricas de activo construido

Estas no dan plata este mes pero sí los siguientes:

- Reseñas de Aurora obtenidas
- Piezas de UGC de Aurora disponibles para reutilizar
- Tamaño de la audiencia de retargeting construida en semanas 1–2
- Consultas por WhatsApp sobre Aurora que no cerraron (pipeline para el mes siguiente)

---

## 8. Reglas de decisión al cierre

- Si Aurora vendió pero **con CAC superior a su margen de primera compra** → el canal está mal, no el producto. Redirigir aún más hacia base propia y retargeting.
- Si la **tasa de escalada** fue casi nula → el problema es tu comunicación post-compra de Luna y Sol, no la campaña de Aurora.
- Si el contenido de Aurora tuvo **alta retención y guardados pero pocas ventas** → hay deseo pero fricción en el cierre. Revisar página de producto, garantía y percepción de riesgo.
- Si el contenido **no superó tu promedio de cuenta** → el problema es el territorio o el creativo. Antes de repetir, replantear el ángulo.
- **En ningún escenario la conclusión es bajar el precio de Aurora.** Un premium que se descuenta deja de ser premium y recuperar esa percepción cuesta muchísimo más que un mes flojo de ventas.

---

## 9. Riesgos del plan

| Riesgo | Mitigación |
|---|---|
| Tu base de clientas es aún pequeña y el Círculo 1 no da volumen | Extender a 6 semanas y dedicar las dos primeras a crecer base con Luna |
| **Botica Verde** o **Skin Lab** ya comunican el ángulo de clima bogotano | Pivotar el concepto hacia "sistema completo" y ritual, que son más difíciles de copiar |
| Las influencers no generan contenido de calidad | Elegir 3–4 y acordar entregables mínimos por escrito antes de enviar Aurora |
| Saturación de WhatsApp | Máximo 1 difusión semanal. Vigilar bloqueos cada semana |

---

**Lo que ajustaría si me das cuatro datos:** precio de lista de Aurora, margen bruto de Aurora, tamaño actual de tu base de clientas y contactos, y presupuesto mensual de pauta. Con eso convierto los porcentajes en pesos y las métricas en metas numéricas concretas en lugar de direcciones.


## Respuesta completa

## Campaña "Aurora" — Plan de 4 semanas

**Producto:** Aurora, tu set de cuidado facial premium (el de mayor precio de tu portafolio).
**Mercado:** Bogotá.
**Regla innegociable del plan:** Aurora **no entra en descuento directo** en ninguna semana. Todo el valor adicional se entrega vía experiencia, obsequio o formato de kit — nunca tocando el precio de lista.

---

## 1. Objetivo

**Objetivo principal**
Convertir a Aurora en un producto con demanda propia y no en un accesorio del catálogo: llevarla de ser un ítem que casi nadie compra a representar una porción relevante de tu margen mensual, vendiendo a audiencia templada y caliente.

**Objetivos secundarios**

| # | Objetivo | Cómo se verifica |
|---|---|---|
| 1 | Activar la escalada desde tu base existente | Compradoras previas de **Luna** o **Sol** que compran **Aurora** |
| 2 | Construir el activo de deseo | Retención de video y guardados en piezas de Aurora |
| 3 | Generar prueba social premium | Reseñas y UGC de Aurora, que hoy probablemente no tienes |
| 4 | Establecer la línea base de CAC de Aurora | Primer dato real de cuánto cuesta vender tu premium |

**Lo que este plan *no* busca:** volumen de pedidos ni clientas nuevas en frío. Aurora no se vende en frío, ya lo hablamos. Si al final del mes tienes pocas unidades pero con margen sano y una base de contenido y reseñas construida, la campaña fue exitosa.

---

## 2. Audiencia

Tres círculos, en orden de prioridad de presupuesto.

### 🔵 Círculo 1 — Tu base (60% del esfuerzo)

La audiencia más rentable de toda la campaña y la que ya es tuya.

- Compradoras previas de **Luna** con más de 30 días desde su compra
- Compradoras previas de **Sol**
- Suscriptoras de email y contactos de WhatsApp que nunca compraron Aurora
- Clientas que compraron 2+ veces (máxima prioridad: ya demostraron confianza)

Aquí no necesitas pauta casi: es email, WhatsApp y Stories.

### 🟣 Círculo 2 — Templada (30%)

- Visitantes de la página de **Aurora** en los últimos 90 días que no compraron
- Engagement de Instagram y TikTok de los últimos 60 días
- Carritos abandonados con Aurora
- Seguidoras que interactuaron con contenido de piel de altura

### ⚪ Círculo 3 — Frío selectivo (10%)

Solo para alimentar los círculos anteriores, **no para vender directo**:

- Lookalike 1% de tus mejores compradoras (mayor ticket histórico)
- Intereses de skincare premium + localidades de Bogotá con mayor poder adquisitivo: Usaquén, Chapinero, Suba (norte), Teusaquillo
- Mujeres 28–50 años

**Perfil de la compradora de Aurora:** no es la que busca el mejor precio. Es la que ya usa skincare, entiende la diferencia entre productos y está dispuesta a pagar por formulación y ritual. Probablemente ya te conoce por **Luna** o **Sol** — por eso el Círculo 1 pesa tanto.

---

## 3. Canales y rol de cada uno

| Canal | Rol en la campaña de Aurora | Peso |
|---|---|---|
| **Instagram orgánico** (Reels + Stories) | Construcción de deseo. El motor narrativo de las 4 semanas. | Alto |
| **Email** | Vehículo principal de escalada desde Luna y Sol. Aquí se explica el precio. | Alto |
| **WhatsApp** | Cierre y consulta personalizada. Aurora es compra consultada. | Alto |
| **Meta Ads (retargeting)** | Reimpactar Círculos 1 y 2. Poco presupuesto, muy dirigido. | Medio |
| **Micro-influencers selectas** | 3–4 perfiles bogotanos, no más. Calidad sobre alcance. | Medio |
| **Google Search (marca)** | Defensiva: capturar quien busca "Aurora" + tu marca tras ver contenido | Bajo |
| **TikTok** | Solo textura y ritual. Sin pauta. | Bajo |

**Fuera de la campaña:** TikTok Ads, marketplaces y prospección fría agresiva. No corresponden al perfil de Aurora en esta etapa.

---

## 4. Mensaje principal

### Concepto rector

> **"Aurora no es una crema más. Es el momento en que tu piel deja de sobrevivir a Bogotá."**

### Por qué este ángulo

Conecta las dos cosas que ya definimos como tu terreno propio: el **clima de altura de Bogotá** (2.600 m, aire seco, UV alta todo el año) y el **ritual premium** que justifica el precio de Aurora. Y te separa de **Botica Verde** y **Skin Lab** en el eje donde ellos difícilmente pueden responder rápido: no compites por ser más natural o más barata, compites por ser la que entiende esta piel, en esta ciudad.

### Mensajes de apoyo

1. **Formulación, no marketing.** Qué lleva Aurora, qué no lleva, y por qué.
2. **El precio explicado.** Transparencia radical: cuánto cuesta por uso, cuánto rinde, en qué se va el valor.
3. **Ritual, no rutina.** Aurora es el paso que se disfruta, no el que se cumple.
4. **Piel preparada.** Aurora hace que **Sol** se vea mejor. Venta cruzada natural dentro de tu escalera.

### Líneas de copy para usar

- *"Tu piel no está seca. Está a 2.600 metros."*
- *"Aurora cuesta lo que cuesta. Te explico exactamente por qué."*
- *"El set que hace que tu maquillaje se vea como debería."*
- *"No lo vas a comprar todos los meses. Esa es la idea."*

**Lo que nunca decimos sobre Aurora:** promesas de curar, eliminar manchas o tratar condiciones de la piel. Los cosméticos en Colombia están regulados por INVIMA y no admiten claims terapéuticos. Hablamos de hidratación, luminosidad, confort y textura.

---

## 5. Desarrollo semana a semana

### 🗓 Semana 1 — Deseo y educación
*"Por qué tu piel se comporta así en Bogotá"*

Ninguna venta directa esta semana. Se construye el problema.

| Canal | Acción |
|---|---|
| IG Reels | 2 piezas: "Lo que la altura le hace a tu barrera cutánea" + macro de textura de **Aurora** absorbiéndose |
| IG Stories | Serie de 4 días: encuesta "¿Sientes tirantez en las mejillas?" → resultados → explicación → teaser de Aurora |
| Email | Envío 1: educativo puro sobre piel de altura. Aurora se menciona al final, sin link de compra agresivo |
| TikTok | 3 videos: textura, ritual nocturno, "3 señales de deshidratación" |
| Meta Ads | Solo campaña de video views a Círculo 3 para construir audiencia de retargeting |
| Micro-influencers | Envío de Aurora a 3–4 perfiles bogotanos. Sin brief de venta: solo pedir uso real durante 3 semanas |

---

### 🗓 Semana 2 — Formulación y precio
*"Te muestro qué hay adentro y cuánto cuesta"*

Aquí se ataca de frente la objeción de precio, sin bajarlo.

| Canal | Acción |
|---|---|
| IG | Carrusel: cada ingrediente de **Aurora**, qué hace, por qué está. Reel: tú hablando del precio a cámara |
| Stories | Caja de preguntas: "¿Qué quieres saber de Aurora?" → responder una por una |
| Email | Envío 2: **desglose de precio**. Cuánto es formulación, empaque, envío. Costo por uso vs. frasco |
| WhatsApp | Estado con el desglose. Difusión única invitando a preguntar por Aurora por chat |
| Meta Ads | Arranca retargeting a Círculo 2 con el video de precio |
| Google | Activar campaña de marca + "Aurora" + nombres de **Botica Verde** y **Skin Lab** como keyword |

---

### 🗓 Semana 3 — Prueba social y escalada
*"Quién ya la está usando"*

La semana de mayor presión comercial hacia tu base.

| Canal | Acción |
|---|---|
| IG | UGC de las influencers (ya llevan 2 semanas de uso). Reposteo de clientas con nombre y localidad |
| Reels | "Piel preparada": **Aurora** + **Sol**, cómo cambia el acabado del maquillaje |
| Email | Envío 3, **segmentado**: a compradoras de Luna → "el siguiente paso de tu rutina". A compradoras de Sol → "por qué tu base se ve mejor con piel preparada" |
| WhatsApp | Mensajes 1 a 1 a clientas recurrentes. No masivo: personalizado, con tu nombre |
| Meta Ads | Retargeting con creativos de testimonio a Círculos 1 y 2 |
| Oferta | Lanzar el **Kit Ritual Completo**: Aurora + Sol + Luna. El ahorro viene del conjunto, no de rebajar Aurora |

---

### 🗓 Semana 4 — Cierre por valor agregado
*"Última semana del ritual"*

Cierre con urgencia legítima, sin descuento.

| Canal | Acción |
|---|---|
| Mecánica de cierre | Toda compra de **Aurora** incluye: **Luna** en tamaño viaje de regalo + empaque especial + consulta 1 a 1 de rutina contigo por WhatsApp. Disponible solo hasta el domingo |
| IG | Reel de unboxing de Aurora. Stories de countdown los últimos 3 días |
| Email | Envío 4 (martes) + recordatorio final (domingo, solo a quienes abrieron o hicieron clic) |
| WhatsApp | Estado diario + difusión el viernes. Cierre 1 a 1 con quienes preguntaron en semanas 2 y 3 |
| Meta Ads | Concentrar presupuesto en carritos abandonados y visitantes de la página de Aurora |
| Post-cierre | A quienes compraron: seguimiento a los 15 días pidiendo reseña |

---

## 6. Distribución sugerida de presupuesto

Sin conocer tu monto de pauta, te doy los porcentajes:

| Destino | % | Nota |
|---|---|---|
| Retargeting Meta (Círculos 1 y 2) | 45% | Concentrar en semanas 3 y 4 |
| Video views frío (Círculo 3) | 15% | Solo semanas 1 y 2, para construir audiencias |
| Google Search marca + competencia | 10% | Barato y de alta intención |
| Producto para influencers | 15% | 3–4 unidades de Aurora |
| Empaque especial + Luna de regalo | 10% | Costo variable, solo por venta cerrada |
| Reserva | 5% | Para doblar lo que funcione en semana 3 |

Nota de margen: el obsequio de **Luna** tamaño viaje y el empaque tienen costo, pero se cargan contra el margen de Aurora sin tocar su precio de lista. Verifica que el margen de contribución de Aurora siga sano después de descontarlos.

---

## 7. Métricas de éxito

### Las tres que definen si la campaña funcionó

| # | KPI | Por qué |
|---|---|---|
| 1 | **Margen de contribución generado por Aurora** en las 4 semanas | Vender Aurora sin margen no tiene sentido |
| 2 | **Tasa de escalada**: % de compradoras previas de Luna o Sol que compran Aurora | Valida tu escalera de precios completa |
| 3 | **CAC de Aurora**, separado por audiencia fría vs. templada | Tu primer dato real. Establece la línea base |

### Métricas de negocio

- Unidades de Aurora vendidas (total y por semana)
- **% de ingresos del mes que aporta Aurora** — el indicador de si tu premium dejó de ser decorativo
- Ticket promedio de los pedidos que incluyen Aurora
- Unidades del **Kit Ritual Completo** vendidas
- % de compras de Aurora que vienen de clientas nuevas vs. existentes

### Métricas de deseo (semanas 1–2)

Estas son las de alerta temprana. Si fallan, el problema aparecerá en ventas dos semanas después.

- Retención a 3 segundos en Reels de Aurora
- **Guardados y compartidos** de piezas de Aurora vs. tu promedio de cuenta
- Alcance en **no seguidores** del contenido de piel de altura
- Respuestas en la caja de preguntas de semana 2

### Métricas de canal

| Canal | Qué mirar |
|---|---|
| Email | Clics e **ingresos por email enviado** (no aperturas) |
| WhatsApp | Conversaciones iniciadas, conversación → venta, y **tasa de bloqueo** |
| Meta Ads | MER global de la campaña, más que el ROAS reportado |
| Google | Clics de marca y conversión asistida |
| Influencers | Ventas por código único + volumen de contenido generado |

### Métricas de activo construido

Estas no dan plata este mes pero sí los siguientes:

- Reseñas de Aurora obtenidas
- Piezas de UGC de Aurora disponibles para reutilizar
- Tamaño de la audiencia de retargeting construida en semanas 1–2
- Consultas por WhatsApp sobre Aurora que no cerraron (pipeline para el mes siguiente)

---

## 8. Reglas de decisión al cierre

- Si Aurora vendió pero **con CAC superior a su margen de primera compra** → el canal está mal, no el producto. Redirigir aún más hacia base propia y retargeting.
- Si la **tasa de escalada** fue casi nula → el problema es tu comunicación post-compra de Luna y Sol, no la campaña de Aurora.
- Si el contenido de Aurora tuvo **alta retención y guardados pero pocas ventas** → hay deseo pero fricción en el cierre. Revisar página de producto, garantía y percepción de riesgo.
- Si el contenido **no superó tu promedio de cuenta** → el problema es el territorio o el creativo. Antes de repetir, replantear el ángulo.
- **En ningún escenario la conclusión es bajar el precio de Aurora.** Un premium que se descuenta deja de ser premium y recuperar esa percepción cuesta muchísimo más que un mes flojo de ventas.

---

## 9. Riesgos del plan

| Riesgo | Mitigación |
|---|---|
| Tu base de clientas es aún pequeña y el Círculo 1 no da volumen | Extender a 6 semanas y dedicar las dos primeras a crecer base con Luna |
| **Botica Verde** o **Skin Lab** ya comunican el ángulo de clima bogotano | Pivotar el concepto hacia "sistema completo" y ritual, que son más difíciles de copiar |
| Las influencers no generan contenido de calidad | Elegir 3–4 y acordar entregables mínimos por escrito antes de enviar Aurora |
| Saturación de WhatsApp | Máximo 1 difusión semanal. Vigilar bloqueos cada semana |

---

**Lo que ajustaría si me das cuatro datos:** precio de lista de Aurora, margen bruto de Aurora, tamaño actual de tu base de clientas y contactos, y presupuesto mensual de pauta. Con eso convierto los porcentajes en pesos y las métricas en metas numéricas concretas en lugar de direcciones.