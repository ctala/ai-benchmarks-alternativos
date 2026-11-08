# Claude Sonnet 5.5 — agent_long_horizon/implicit_state_construction

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.02 | quality: 10.0
- latency_total: 97.88s | tokens_per_second: 132.3
- input_tokens: 22860 | output_tokens: 12155

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

¡Hola, Camila! Sí, me queda claro. Esto es lo que tengo:

**Tu negocio**
- Tienda online en Colombia
- Mercado actual: solo Bogotá

**Productos**
- **Aurora**: set de cuidado facial, precio **premium**
- **Sol**: kit de maquillaje natural, precio **medio**
- **Luna**: crema corporal, precio **de entrada**

**Competidores principales (ambos en Bogotá)**
- Botica Verde
- Skin Lab

Con esto puedo ayudarte a planificar campañas sin que me repitas estos datos. Por ejemplo, si me dices "la campaña del producto premium" o "el de entrada", sé que hablas de Aurora y Luna.

¿Qué quieres trabajar primero? Por ejemplo, el lanzamiento o promoción de un producto, una campaña para una fecha especial, la diferenciación frente a Botica Verde y Skin Lab, o cómo usar Luna para atraer clientes hacia Aurora y Sol.

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Aquí tienes una propuesta:

**"Te ofrecemos una rutina completa de belleza, con cuidado facial (Aurora), maquillaje natural (Sol) y cuidado corporal (Luna), en tres niveles de precio para que empieces por donde quieras y crezcas a tu ritmo. Somos una marca online pensada para Bogotá, con la comodidad de comprar desde casa y la cercanía de un negocio local."**

**Supuestos que hice:**
- Que la "cercanía local" es un valor real para ti frente a Botica Verde y Skin Lab. Si ellos también lo comunican, conviene buscar otro diferenciador.
- Que no todos tus productos son "naturales". Solo mencioné esa cualidad en Sol, porque es lo que me indicaste.

Para afinarla, me ayudaría saber qué te hace distinta de Botica Verde y Skin Lab (ingredientes, atención, envíos, precio, etc.). Con eso puedo reemplazar las partes más genéricas por algo que solo tú puedas decir.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Como tu único mercado es Bogotá y vendes en línea, te recomiendo este orden de prioridad:

**1. Instagram (Reels, Stories y pauta con Meta Ads)**
- Es el canal natural para belleza: demostraciones, antes/después, rutinas.
- Segmenta la pauta solo a Bogotá, para no gastar presupuesto fuera de tu zona de entrega.
- Usa **Luna** (precio de entrada) como producto de captación, y **Aurora** (premium) para contenido aspiracional y de confianza.

**2. TikTok**
- Buen alcance orgánico a bajo costo, ideal para **Sol** (maquillaje natural): tutoriales rápidos, "maquillaje en 5 minutos".
- Funciona bien con microinfluencers bogotanas, que además refuerzan tu cercanía local.

**3. WhatsApp Business**
- Muy usado en Colombia para resolver dudas y cerrar ventas.
- Sirve para recomendar la rutina completa (Aurora + Sol + Luna), enviar promociones a clientas recurrentes y dar seguimiento a carritos abandonados.

**4. Google (búsqueda y Shopping)**
- Captura a quienes ya buscan algo como "crema corporal Bogotá" o "maquillaje natural Bogotá".
- Aquí compites directamente con **Botica Verde** y **Skin Lab**, así que empieza con presupuesto bajo y términos específicos.

**Lo que dejaría para después:** email marketing (útil cuando ya tengas una base de clientas) y Facebook orgánico, salvo que tu público sea de mayor edad.

**Un paso sin costo:** revisa la Biblioteca de Anuncios de Meta para ver qué pauta están corriendo Botica Verde y Skin Lab. Te dirá en qué canales y con qué mensajes están invirtiendo.

**Supuesto:** aún no me has descrito a tu público (edad, estrato, intereses), así que asumí un perfil joven-adulto, activo en redes. Si es otro, el orden podría cambiar.

¿Quién es tu clienta ideal? Con eso puedo ajustar los canales y proponerte una distribución de presupuesto.

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Como no sé cuánto tiempo o equipo tienes, asumí que trabajas sola o con un equipo pequeño. Prefiero una frecuencia que puedas sostener antes que una ambiciosa que abandones en un mes.

| Canal | Frecuencia recomendada | Formato |
|---|---|---|
| **Instagram** | 3 publicaciones por semana (principalmente Reels) + Stories casi a diario (3-5) | Reels, carruseles, Stories con encuestas y preguntas |
| **TikTok** | 3 a 4 videos por semana | Tutoriales cortos, rutinas, tendencias adaptadas |
| **WhatsApp Business** | Estados 3 veces por semana + máximo 1 mensaje de difusión semanal | Novedades, promociones, testimonios |
| **Google** | Sin cadencia de publicación; revisa fichas de producto y palabras clave una vez al mes | Descripciones optimizadas, fotos, reseñas |

**Cómo repartir el contenido entre tus productos (semana tipo):**
- **1 pieza de Sol:** tutorial de maquillaje natural, ideal para TikTok y Reels.
- **1 pieza de Luna:** contenido de captación, como uso diario, resultados o una oferta de entrada.
- **1 pieza de Aurora:** contenido aspiracional o educativo, como rutina facial, ingredientes o testimonios.
- **Stories y estados:** detrás de cámaras, pedidos empacados, reseñas de clientas y preguntas.

**Para ahorrar tiempo:** graba una vez y publica en dos lugares. Un mismo video vertical sirve para Reels, TikTok y el estado de WhatsApp (idealmente sin marca de agua de otra app).

**Sobre Google:** no lo traté como canal de publicación porque tu tienda es online. Un perfil de negocio en Google normalmente exige una dirección física o un área de servicio, así que verifica si aplica en tu caso.

**Ajustes importantes:**
- Si tienes que elegir, prioriza **Instagram y TikTok** y deja WhatsApp para cuando ya tengas clientas a quienes escribirles.
- Mide durante 4 a 6 semanas qué formato y qué producto generan más interacción y ventas, y ajusta la frecuencia con esos datos.

¿Cuánto tiempo a la semana puedes dedicar a crear contenido, y lo harías tú sola? Con eso te armo un calendario de 4 semanas con ideas concretas para Aurora, Sol y Luna.

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Asumo que hablas sobre todo de **Aurora** (cuidado facial, premium) y, en menor medida, de **Luna** (crema corporal, entrada), porque Sol es maquillaje. Para skincare funcionan sobre todo los contenidos que generan **confianza y muestran el producto en uso**.

**Para Aurora (premium)**
Como el precio es alto, la clienta necesita más razones para confiar:
- **Rutina paso a paso:** "Mi rutina de noche en 4 pasos", mostrando el orden y el tiempo real.
- **Educativo:** qué hace cada producto del set, para qué tipo de piel es y cómo se aplica. Un carrusel o Reel de "3 errores al aplicar tu crema facial" posiciona como experta.
- **Textura y aplicación en primer plano:** videos cortos, bien iluminados y casi sin edición, que muestren cómo se siente el producto.
- **Testimonios reales de clientas bogotanas:** reseñas, videos o capturas de WhatsApp con permiso.
- **Constancia en el tiempo:** "Una clienta usó Aurora 4 semanas", siempre real y sin retoques.

**Para Luna (entrada)**
Aquí buscas captar clientas nuevas con poca fricción:
- **Contenido sensorial:** aplicación, textura y aroma, con un ritual corto como "después de la ducha".
- **Ofertas simples:** un precio de entrada o una muestra que lleve luego a Aurora.
- **Pregunta y respuesta:** piel seca, clima frío de Bogotá, altura, etc. El clima de Bogotá es un buen gancho local.

**Formatos según canal**
- **Instagram:** carruseles educativos, Reels de rutina y Stories con preguntas o encuestas ("¿piel seca o mixta?").
- **TikTok:** rutinas rápidas, "pregúntame lo que quieras sobre skincare" y respuestas a comentarios.
- **WhatsApp:** testimonios y asesoría personalizada ("cuéntame tu tipo de piel y te recomiendo").

**Qué cuidar**
- **No prometas resultados médicos** como "cura el acné" o "elimina manchas". Usa lenguaje cosmético ("hidrata", "suaviza", "deja la piel luminosa").
- **Verifica los requisitos del INVIMA** para tus productos y lo que puedes comunicar sobre ellos.
- Los antes/después deben ser honestos y sin filtros, o perderás credibilidad.

**Cómo diferenciarte de Botica Verde y Skin Lab**
Revisa qué tipo de contenido publican y en qué se parecen. Si ambos usan lenguaje muy técnico, puedes ganar con un tono cercano y cotidiano. Si ambos son muy estéticos, puedes ganar con contenido más real y educativo.

¿Qué ingredientes o beneficios principales tiene Aurora? Con eso te propongo ideas de contenido concretas para las primeras semanas.

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Como ya vendes tres productos en tres niveles de precio, tu margen para diferenciarte está en **cómo presentas y acompañas la compra**, no en bajar precios. No sé qué precios ni qué posicionamiento tienen Botica Verde y Skin Lab, así que parto de que no puedes ganarles por precio y que ambos venden productos parecidos a los tuyos.

**1. Diferénciate por la rutina completa, no por producto suelto**
- Tus tres productos cubren cara, maquillaje y cuerpo. Arma **sets o rutinas** (por ejemplo, Aurora + Luna) con un valor agregado en lugar de un descuento: una guía de uso, una muestra o un empaque especial.
- Así compites por una **solución**, no por el precio de una crema.

**2. Usa la escalera de precios a tu favor**
- **Luna** (entrada) trae clientas nuevas sin entrar en una guerra de precios, porque su función es captar, no ganar margen.
- **Aurora** (premium) debe sentirse premium: empaque, tono de marca, testimonios y claridad sobre por qué cuesta lo que cuesta.
- **Sol** (medio) puede ser el puente: "ya probaste Luna, ahora descubre tu maquillaje natural".

**3. Compite en experiencia, donde los grandes suelen ser más débiles**
- **Asesoría por WhatsApp:** "cuéntame tu tipo de piel y te recomiendo". Es muy difícil de copiar a escala.
- **Envíos en Bogotá:** entregas rápidas o con franjas horarias, y un empaque cuidado.
- **Seguimiento posventa:** un mensaje a las 2 semanas preguntando cómo le fue con el producto.
- **Garantía de satisfacción** clara, si tu margen lo permite.

**4. Construye una identidad que no dependa del precio**
- Elige **un territorio** y repítelo: por ejemplo, "skincare pensado para el clima y la altura de Bogotá" o "belleza natural sin complicaciones".
- Tono cercano y educativo, sobre todo si Botica Verde y Skin Lab se comunican de forma más técnica o más aspiracional.
- Muestra el rostro detrás de la marca: tú, tu historia, por qué creaste Aurora, Sol y Luna.

**5. Genera prueba social propia**
- Reseñas, testimonios y contenido de clientas bogotanas.
- Un programa sencillo de referidos: "trae a una amiga y ambas reciben una muestra".

**Lo que evitaría**
- Descuentos frecuentes en **Aurora**, porque entrenan a la clienta a esperar rebajas y debilitan la percepción premium.
- Copiar los mensajes de la competencia.
- Prometer más de lo que el producto puede cumplir.

**Siguiente paso sin costo:** haz una tabla con Botica Verde, Skin Lab y tu marca, y compara precio, tono de comunicación, tiempos de entrega, servicio al cliente y reseñas. Donde ambos coincidan, hay un espacio libre para ti.

Para concretar el diferenciador, cuéntame:
1. ¿Qué haces mejor que ellos hoy, aunque sea pequeño (ingredientes, atención, velocidad, origen)?
2. ¿Cómo se comparan los precios de Aurora, Sol y Luna con los de ellos?

Con eso te redacto un mensaje diferenciador y una idea de campaña para el primer mes.

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Parto de que vendes solo en Bogotá, tienes tres productos en tres niveles de precio y trabajas Instagram, TikTok, WhatsApp y Google. No sé tu punto de partida (ventas actuales, presupuesto de pauta, márgenes), así que **no te pongo metas numéricas fijas**. Usa el primer mes para medir tu línea base y fija metas con esos datos.

## 1. KPIs de negocio (los que deciden si la campaña funciona)
| KPI | Qué mide | Por qué importa |
|---|---|---|
| **Ventas e ingresos totales** | Pedidos y COP vendidos por mes | Es el resultado final |
| **Ticket promedio** | Ingreso ÷ pedidos | Muestra si logras vender más de un producto por compra |
| **Tasa de conversión de la tienda** | Compras ÷ visitas | Indica si el tráfico que traes sí compra |
| **CAC** | Gasto en marketing ÷ clientas nuevas | Te dice cuánto cuesta conseguir cada clienta |
| **ROAS** | Ingresos de pauta ÷ gasto en pauta | Mide la rentabilidad de Meta Ads y Google |
| **Margen después de marketing** | Ganancia tras costos de producto, envío y pauta | Un ROAS alto no sirve si el margen es bajo |

## 2. KPIs por producto (tu escalera de precios)
- **Luna (entrada):** unidades vendidas y **costo por clienta nueva**. Es tu producto de captación.
- **Luna → Aurora/Sol:** % de clientas de Luna que compran otro producto en 60 o 90 días. Es el KPI clave de tu estrategia.
- **Sol (medio):** conversión desde TikTok y Reels, y % de ventas que vienen de contenido de tutoriales.
- **Aurora (premium):** ventas, ticket y **% de ventas sin descuento**, para proteger la percepción premium.

## 3. KPIs por canal
- **Instagram y TikTok:** alcance, **guardados y compartidos** (pesan más que los "me gusta"), visitas al perfil, clics al enlace y ventas atribuidas.
- **Meta Ads:** CPM, CTR, costo por clic, costo por compra y ROAS, con segmentación solo en Bogotá.
- **Google:** impresiones, clics, CTR y conversiones en términos como "crema corporal Bogotá" o "maquillaje natural Bogotá".
- **WhatsApp Business:** conversaciones iniciadas, **% de conversaciones que terminan en compra** y tiempo de primera respuesta.

## 4. KPIs de retención y confianza
- **Tasa de recompra** a 60 o 90 días. Con un trimestre solo verás una señal temprana.
- **Reseñas y testimonios** conseguidos por mes.
- **Referidos** si lanzas el programa de "trae a una amiga".
- **Tiempo de entrega en Bogotá** y tasa de incidencias o devoluciones. Si compites por experiencia, esto también es un KPI de marketing.

## 5. Cómo repartir el foco en el trimestre
- **Mes 1: línea base.** Configura el seguimiento y mide sin sacar conclusiones apresuradas. Tu pregunta es qué producto, canal y formato responden mejor.
- **Mes 2: optimizar.** Pausa lo que no convierte y duplica lo que sí. Vigila CAC, conversión y ticket promedio.
- **Mes 3: retención y expansión.** Mide recompra, referidos, el paso de Luna a Aurora/Sol y el ROAS sostenido.

## 6. Qué configurar desde el día uno
- **Google Analytics 4** y **Píxel de Meta** en la tienda, con eventos de compra y carrito abandonado.
- **UTM** en cada enlace, para saber de qué canal viene cada venta.
- **Etiquetas en WhatsApp Business** (nueva, interesada, compró, recompra) y una pregunta de registro: "¿cómo nos conociste?".
- Una **hoja semanal** con 6 a 8 números, no 30.

## Lo que no priorizaría
- Seguidores y "me gusta" como métrica principal. Sirven de contexto, pero no pagan las cuentas.
- Comparar tus cifras con Botica Verde o Skin Lab sin datos reales de ellos. Solo puedes observar su pauta y su contenido, no sus ventas.

**Si solo puedes seguir 5 KPIs:** ventas, ticket promedio, CAC, conversión de la tienda y % de clientas de Luna que compran otro producto.

Para ponerle metas concretas, dime: ¿cuántos pedidos al mes tienes hoy y cuánto presupuesto de pauta mensual piensas destinar? Con eso te propongo una tabla de metas realistas para los tres meses.

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

# Campaña de 4 semanas: Aurora

Entiendo que tu producto más caro es **Aurora**, el set de cuidado facial premium. La campaña se enfoca solo en Aurora; Sol y Luna quedan fuera de esta pauta y del contenido.

## Objetivo
**Generar ventas de Aurora en Bogotá sin recurrir a descuentos, y construir la confianza que exige un producto premium.**

Objetivos específicos:
- Aumentar las ventas de Aurora frente a tu línea base actual.
- Conseguir testimonios y reseñas propias de Aurora.
- Mantener un alto % de ventas de Aurora sin descuento.

## Audiencia
No me has descrito a tu clienta, así que parto de este perfil. Ajústalo si no encaja:
- **Mujeres de 25 a 45 años en Bogotá**, con interés en skincare, rutinas de cuidado personal y belleza.
- **Capacidad y disposición de pagar un precio premium** por cuidado facial.
- **Dos subgrupos:**
  - **Exploradoras:** ya usan skincare, comparan opciones y quizá miran a Botica Verde o Skin Lab.
  - **Principiantes:** quieren empezar una rutina y buscan guía y confianza.

## Mensaje principal
**"Aurora: tu rutina facial completa, con el cuidado que tu piel merece."**

Pilares de apoyo:
1. **Rutina completa, no producto suelto:** Aurora es un set pensado para usarse en conjunto.
2. **Confianza antes que promesa:** muestras cómo se usa, cómo se siente y qué dicen clientas reales.
3. **Cercanía:** una marca bogotana que te acompaña y te asesora.

Si Aurora tiene un ingrediente, origen o beneficio distintivo, ese debe ser el eje del mensaje. Dime cuál es y reemplazo la frase genérica.

## Canales y rol de cada uno
| Canal | Rol en la campaña | Frecuencia |
|---|---|---|
| **Instagram** | Canal principal: educación, rutina y prueba social | 3 publicaciones/semana (Reels y carruseles) + Stories casi a diario |
| **TikTok** | Alcance y demostración: textura, aplicación, rutina | 3 videos/semana (reutiliza los Reels) |
| **Meta Ads** | Llevar tráfico segmentado a Bogotá hacia la página de Aurora | Desde la semana 2 |
| **WhatsApp Business** | Asesoría personalizada y cierre de venta | Atención continua + 1 difusión semanal |
| **Google** | Captar búsquedas con intención de compra (opcional, presupuesto bajo) | Revisión semanal |

## Plan semanal

### Semana 1: Presentación y confianza
**Meta:** que tu audiencia conozca Aurora y entienda qué es y para quién es.
- **Contenido:**
  - Reel de presentación: "Conoce Aurora" con unboxing y cada producto del set.
  - Carrusel educativo: "Cómo usar Aurora paso a paso".
  - Historia de marca: por qué creaste Aurora (tu rostro como fundadora).
  - Stories con encuestas: "¿Piel seca, mixta o grasa?"
- **Pauta:** sin inversión o mínima. Esta semana es para medir qué contenido resuena.
- **WhatsApp:** prepara respuestas rápidas y etiquetas (interesada, compró, recompra).
- **Configuración técnica:** Píxel de Meta, GA4 y UTM funcionando antes de gastar en pauta.

### Semana 2: Demostración y prueba
**Meta:** mostrar Aurora en uso y activar pauta con lo que mejor funcionó.
- **Contenido:**
  - Reel de rutina de mañana o noche con Aurora, en tiempo real.
  - Video de textura y aplicación en primer plano.
  - Respuestas a preguntas frecuentes ("¿cuánto dura el set?", "¿para qué piel es?").
  - Primeros testimonios, si ya tienes clientas de Aurora.
- **Pauta:** lanza Meta Ads con el Reel de mejor desempeño de la semana 1, segmentado a Bogotá, con dos audiencias (exploradoras y principiantes) para comparar.
- **WhatsApp:** difusión a contactos actuales con la rutina de Aurora y una oferta de asesoría.

### Semana 3: Conversión
**Meta:** convertir el interés en compras, sin bajar el precio.
- **Contenido:**
  - Testimonios y reseñas de clientas de Aurora.
  - Carrusel "Aurora vs. rutina improvisada": por qué un set funciona mejor que productos sueltos (sin atacar marcas).
  - Contenido de objeciones: "¿Vale la pena el precio?", mostrando valor, duración y resultados reales.
- **Oferta de valor agregado:** en lugar de descuento, usa **un bono por tiempo limitado**: muestra, guía de rutina en PDF, empaque de regalo o envío prioritario en Bogotá.
- **Pauta:** retargeting a quienes vieron Reels de Aurora, visitaron la página o abandonaron el carrito.
- **WhatsApp:** seguimiento a carritos abandonados y asesoría uno a uno.

### Semana 4: Cierre y retención
**Meta:** capturar las compras pendientes y empezar a construir recompra y referidos.
- **Contenido:**
  - Resumen de resultados y testimonios del mes.
  - Recordatorio del bono con fecha de cierre.
  - Contenido de "mi primer mes con Aurora".
- **Referidos:** "Trae a una amiga y ambas reciben una muestra".
- **Posventa:** mensaje por WhatsApp a las compradoras 2 semanas después, preguntando cómo les va con Aurora y pidiendo reseña.
- **Pauta:** mantén lo que mejor convirtió y pausa lo demás.

## Métricas de éxito
Como no conozco tu punto de partida, la semana 1 fija la línea base y las metas se definen al terminar. Estas son las métricas:

| Categoría | Métrica | Qué buscas |
|---|---|---|
| **Negocio** | Unidades e ingresos de Aurora | Crecimiento frente a la línea base |
| | **CAC de Aurora** | Menor que tu margen por unidad vendida |
| | **ROAS** de la pauta | Por encima de tu punto de equilibrio |
| | **% de ventas de Aurora sin descuento** | Lo más cercano a 100% |
| **Conversión** | Tasa de conversión de la página de Aurora | Mejora semana a semana |
| | % de conversaciones de WhatsApp que terminan en compra | Mide la calidad de tu asesoría |
| **Contenido** | Guardados, compartidos y clics al enlace | Señales de intención de compra |
| | Visitas a la página de Aurora desde redes | Tráfico cualificado |
| **Confianza** | Reseñas y testimonios nuevos de Aurora | Meta mínima: 3 a 5 en el mes |
| | Referidos | Señal de recomendación |

**Regla del CAC:** si cada clienta nueva de Aurora te cuesta más de lo que ganas por esa venta, la campaña pierde dinero aunque venda. Define tu margen por unidad antes de empezar.

## Qué evitar
- **Descuentos de Aurora:** debilitan la percepción premium. Usa bonos de valor en su lugar.
- **Promesas médicas** como "elimina manchas" o "trata el acné". Usa lenguaje cosmético y verifica los requisitos del INVIMA.
- **Mensajes que ataquen a Botica Verde o Skin Lab:** compite mostrando lo tuyo, no criticando lo suyo.

## Para afinar el plan
1. ¿Qué ingredientes o beneficios principales tiene Aurora?
2. ¿Cuánto cuesta y cuál es tu margen por set?
3. ¿Cuántas ventas de Aurora tienes hoy al mes y qué presupuesto de pauta puedes destinar?

Con eso te propongo metas numéricas por semana y un calendario con ideas de guion para cada pieza.


## Respuesta completa

# Campaña de 4 semanas: Aurora

Entiendo que tu producto más caro es **Aurora**, el set de cuidado facial premium. La campaña se enfoca solo en Aurora; Sol y Luna quedan fuera de esta pauta y del contenido.

## Objetivo
**Generar ventas de Aurora en Bogotá sin recurrir a descuentos, y construir la confianza que exige un producto premium.**

Objetivos específicos:
- Aumentar las ventas de Aurora frente a tu línea base actual.
- Conseguir testimonios y reseñas propias de Aurora.
- Mantener un alto % de ventas de Aurora sin descuento.

## Audiencia
No me has descrito a tu clienta, así que parto de este perfil. Ajústalo si no encaja:
- **Mujeres de 25 a 45 años en Bogotá**, con interés en skincare, rutinas de cuidado personal y belleza.
- **Capacidad y disposición de pagar un precio premium** por cuidado facial.
- **Dos subgrupos:**
  - **Exploradoras:** ya usan skincare, comparan opciones y quizá miran a Botica Verde o Skin Lab.
  - **Principiantes:** quieren empezar una rutina y buscan guía y confianza.

## Mensaje principal
**"Aurora: tu rutina facial completa, con el cuidado que tu piel merece."**

Pilares de apoyo:
1. **Rutina completa, no producto suelto:** Aurora es un set pensado para usarse en conjunto.
2. **Confianza antes que promesa:** muestras cómo se usa, cómo se siente y qué dicen clientas reales.
3. **Cercanía:** una marca bogotana que te acompaña y te asesora.

Si Aurora tiene un ingrediente, origen o beneficio distintivo, ese debe ser el eje del mensaje. Dime cuál es y reemplazo la frase genérica.

## Canales y rol de cada uno
| Canal | Rol en la campaña | Frecuencia |
|---|---|---|
| **Instagram** | Canal principal: educación, rutina y prueba social | 3 publicaciones/semana (Reels y carruseles) + Stories casi a diario |
| **TikTok** | Alcance y demostración: textura, aplicación, rutina | 3 videos/semana (reutiliza los Reels) |
| **Meta Ads** | Llevar tráfico segmentado a Bogotá hacia la página de Aurora | Desde la semana 2 |
| **WhatsApp Business** | Asesoría personalizada y cierre de venta | Atención continua + 1 difusión semanal |
| **Google** | Captar búsquedas con intención de compra (opcional, presupuesto bajo) | Revisión semanal |

## Plan semanal

### Semana 1: Presentación y confianza
**Meta:** que tu audiencia conozca Aurora y entienda qué es y para quién es.
- **Contenido:**
  - Reel de presentación: "Conoce Aurora" con unboxing y cada producto del set.
  - Carrusel educativo: "Cómo usar Aurora paso a paso".
  - Historia de marca: por qué creaste Aurora (tu rostro como fundadora).
  - Stories con encuestas: "¿Piel seca, mixta o grasa?"
- **Pauta:** sin inversión o mínima. Esta semana es para medir qué contenido resuena.
- **WhatsApp:** prepara respuestas rápidas y etiquetas (interesada, compró, recompra).
- **Configuración técnica:** Píxel de Meta, GA4 y UTM funcionando antes de gastar en pauta.

### Semana 2: Demostración y prueba
**Meta:** mostrar Aurora en uso y activar pauta con lo que mejor funcionó.
- **Contenido:**
  - Reel de rutina de mañana o noche con Aurora, en tiempo real.
  - Video de textura y aplicación en primer plano.
  - Respuestas a preguntas frecuentes ("¿cuánto dura el set?", "¿para qué piel es?").
  - Primeros testimonios, si ya tienes clientas de Aurora.
- **Pauta:** lanza Meta Ads con el Reel de mejor desempeño de la semana 1, segmentado a Bogotá, con dos audiencias (exploradoras y principiantes) para comparar.
- **WhatsApp:** difusión a contactos actuales con la rutina de Aurora y una oferta de asesoría.

### Semana 3: Conversión
**Meta:** convertir el interés en compras, sin bajar el precio.
- **Contenido:**
  - Testimonios y reseñas de clientas de Aurora.
  - Carrusel "Aurora vs. rutina improvisada": por qué un set funciona mejor que productos sueltos (sin atacar marcas).
  - Contenido de objeciones: "¿Vale la pena el precio?", mostrando valor, duración y resultados reales.
- **Oferta de valor agregado:** en lugar de descuento, usa **un bono por tiempo limitado**: muestra, guía de rutina en PDF, empaque de regalo o envío prioritario en Bogotá.
- **Pauta:** retargeting a quienes vieron Reels de Aurora, visitaron la página o abandonaron el carrito.
- **WhatsApp:** seguimiento a carritos abandonados y asesoría uno a uno.

### Semana 4: Cierre y retención
**Meta:** capturar las compras pendientes y empezar a construir recompra y referidos.
- **Contenido:**
  - Resumen de resultados y testimonios del mes.
  - Recordatorio del bono con fecha de cierre.
  - Contenido de "mi primer mes con Aurora".
- **Referidos:** "Trae a una amiga y ambas reciben una muestra".
- **Posventa:** mensaje por WhatsApp a las compradoras 2 semanas después, preguntando cómo les va con Aurora y pidiendo reseña.
- **Pauta:** mantén lo que mejor convirtió y pausa lo demás.

## Métricas de éxito
Como no conozco tu punto de partida, la semana 1 fija la línea base y las metas se definen al terminar. Estas son las métricas:

| Categoría | Métrica | Qué buscas |
|---|---|---|
| **Negocio** | Unidades e ingresos de Aurora | Crecimiento frente a la línea base |
| | **CAC de Aurora** | Menor que tu margen por unidad vendida |
| | **ROAS** de la pauta | Por encima de tu punto de equilibrio |
| | **% de ventas de Aurora sin descuento** | Lo más cercano a 100% |
| **Conversión** | Tasa de conversión de la página de Aurora | Mejora semana a semana |
| | % de conversaciones de WhatsApp que terminan en compra | Mide la calidad de tu asesoría |
| **Contenido** | Guardados, compartidos y clics al enlace | Señales de intención de compra |
| | Visitas a la página de Aurora desde redes | Tráfico cualificado |
| **Confianza** | Reseñas y testimonios nuevos de Aurora | Meta mínima: 3 a 5 en el mes |
| | Referidos | Señal de recomendación |

**Regla del CAC:** si cada clienta nueva de Aurora te cuesta más de lo que ganas por esa venta, la campaña pierde dinero aunque venda. Define tu margen por unidad antes de empezar.

## Qué evitar
- **Descuentos de Aurora:** debilitan la percepción premium. Usa bonos de valor en su lugar.
- **Promesas médicas** como "elimina manchas" o "trata el acné". Usa lenguaje cosmético y verifica los requisitos del INVIMA.
- **Mensajes que ataquen a Botica Verde o Skin Lab:** compite mostrando lo tuyo, no criticando lo suyo.

## Para afinar el plan
1. ¿Qué ingredientes o beneficios principales tiene Aurora?
2. ¿Cuánto cuesta y cuál es tu margen por set?
3. ¿Cuántas ventas de Aurora tienes hoy al mes y qué presupuesto de pauta puedes destinar?

Con eso te propongo metas numéricas por semana y un calendario con ideas de guion para cada pieza.