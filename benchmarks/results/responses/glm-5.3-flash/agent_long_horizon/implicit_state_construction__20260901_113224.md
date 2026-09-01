# GLM 5.3 Flash — agent_long_horizon/implicit_state_construction

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 7.4 | quality: 8.5
- latency_total: 352.712s | tokens_per_second: 38.3
- input_tokens: 14559 | output_tokens: 12521

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

¡Hola Camila! Sí, me queda perfectamente claro. Te confirmo lo que tengo registrado:

**Tu negocio**
- Tienda online en Colombia, con Bogotá como único mercado por ahora.

**Tu portafolio (3 productos)**
- **Aurora** – set de cuidado facial → precio premium
- **Sol** – kit de maquillaje natural → precio medio
- **Luna** – crema corporal → precio entrada

**Competidores principales**
- **Botica Verde** (Bogotá)
- **Skin Lab** (Bogotá)

Cuando hables de "el premium" o "el de entrada", por ejemplo, sabré que te refieres a Aurora y Luna respectivamente, y tus comparaciones competitivas las haré contra esas dos marcas.

¿Qué campaña quieres planificar primero?

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Claro, Camila. Aquí tienes tu propuesta de valor general en 2 oraciones:

> **"Somos la tienda online bogotana donde construyes tu ritual completo de belleza en un solo lugar: cuidado facial premium, maquillaje natural y cuidado corporal, con precios que se acomodan a cada etapa de tu vida. A diferencia de Botica Verde y Skin Lab, no te hacemos elegir entre calidad y presupuesto: nuestra línea en tres niveles te permite empezar por lo esencial y crecer con nosotros hacia lo premium."**

**Por qué funciona:**
- **Aprovecha tu portafolio escalonado** (Aurora → Sol → Luna) como diferenciador de precio y "camino de cliente": entras con Luna y subes hacia Aurora.
- **Usa "maquillaje natural"** (tu único atributo de producto explícito) como gancho de tendencia.
- **Localiza en Bogotá**, donde compites directamente contra tus dos rivales, para jugar la carta de cercanía.
- **Menciona a la competencia** solo si la usarás en canales comparativos; para web o redes, puedes omitir esa segunda parte y dejar: *"...no te hacemos elegir entre calidad y presupuesto."*

¿Quieres que la ajuste en tono (más emocional, más directa) o que la adapte para un canal específico?

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Buena pregunta. Antes de responder, un supuesto que uso (corrígeme si no aplica): por tu tipo de productos, asumo un público principal de **mujeres de ~20 a 45 años en Bogotá**, con distinto poder adquisitivo según el producto. Con eso, mi priorización sería:

## Prioridad 1 — Descubrimiento y prueba

**1. Instagram**
- El canal central del sector belleza: sirve para Aurora (contenido aspiracional, precio premium justificado con estética cuidada) y para Sol (Reels de aplicación, antes/después).
- Publicidad Meta Ads te permite segmentar por ubicación (Bogotá), edad e intereses de belleza.

**2. TikTok**
- "Maquillaje natural" es una categoría con altísimo volumen orgánico ahí. Ideal para dar a conocer **Sol** y usarlo como puerta de entrada a la marca.
- Alcance orgánico bajo costo: perfecto mientras validas mensajes.

## Prioridad 2 — Conversión y captura de demanda

**3. WhatsApp Business**
- En Colombia es donde se cierra la venta online. Catálogo, respuestas rápidas, seguimiento post-compra. Casi obligatorio para ecommerce local.

**4. Google (búsquedas + Shopping)**
- Aquí capturas demanda existente: "crema corporal Bogotá", "set cuidado facial Colombia". Es donde puedes monitorear y competir por términos contra **Botica Verde** y **Skin Lab**.

## Prioridad 3 — Retención y escalada de cliente

**5. Email marketing**
- Clave para tu estrategia de escalonado: quien compra **Luna** (entrada) recibe contenido que la lleva a **Sol** y luego a **Aurora**. Es el canal más barato para aumentar el valor de vida del cliente.

**Mi recomendación práctica:** arranca solo con **Instagram + WhatsApp + email**, añade TikTok desde el mes 2-3, y Google Ads cuando ya sepas qué mensajes convierten.

¿Quieres que definamos el objetivo y mensaje de la primera campaña para Instagram, o prefieres primero perfilar mejor al público por producto?

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Te doy frecuencias realistas, pensando en que seguramente estás haciendo esto tú misma o con equipo pequeño. La regla de oro: **mejor una cadencia que puedas sostener que una ambiciosa que abandones al mes**.

## Tabla resumen

| Canal | Mínimo sostenible | Ideal |
|---|---|---|
| Instagram (feed/Reels) | 3 posts/semana | 4-5/semana |
| Instagram (historias) | 4-5 por semana | A diario (3-5 historias) |
| TikTok | 3 videos/semana | 4-5/semana |
| WhatsApp (estados) | 2-3 por semana | A diario (1-2) |
| Email marketing | 2 al mes | 1 a la semana |
| Google (perfil/ficha) | 1 actualización/mes | 1-2 al mes |

## Detalle por canal

**Instagram** — Es tu canal central, aquí sí invierte tiempo. Mezcla: 1 Reel de producto (rotando Aurora/Sol/Luna), 1 contenido educativo o de rutina, 1 contenido de marca/bastidores. Las historias son tu herramienta de venta directa en Bogotá: encuestas, entregas del día, testimonios.

**TikTok** — El algoritmo premia constancia más que perfección. Truco: **graba los Reels de Instagram y súbelos también a TikTok sin edición extra**. Duplicas presencia sin duplicar trabajo.

**WhatsApp** — Los estados funcionan como historias: novedades, reposiciones, recordatorio de promociones. Ojo con los broadcasts masivos: máximo 2-3 al mes para no ganar la bloqueada.

**Email** — 2 al mes como mínimo (1 con contenido/valor + 1 promocional). Aquí vive tu estrategia de escalada Luna → Sol → Aurora: secuencias automatizadas post-compra cuentan como flujo aparte, no como frecuencia manual.

**Google** — No es canal de "publicación" propiamente, pero mantén actualizado tu feed de productos y, si tienes ficha de Google Business, 1 post al mes.

## Consejo operativo

Dedica **una sesión de batching semanal** (ej. lunes, 2-3 horas): grabas todo el video del mes, escribes los captions y programas. Publicar a diario desde cero es la receta del agotamiento.

¿Quieres que te arme un calendario semanal tipo con los tipos de contenido distribuidos por producto?

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

En skincare, el contenido que mejor funciona comparte un patrón: **resuelve dudas reales y muestra resultados creíbles**. Aquí los tipos ordenados por efectividad, conectados con tus productos:

## Los 6 tipos que mejor funcionan

**1. Educativo ("¿sabías que...?")**
El rey del sector. La gente no compra skincare que no entiende. Ejemplos para ti:
- "¿Por qué tu piel se reseca en Bogotá?" (el clima frío y seco de la ciudad a 2.600 m es un dolor real de tu público; úsalo a favor de **Aurora** y **Luna**).
- "Orden correcto de aplicación de tu rutina facial".
- "3 errores comunes al usar crema corporal".

**2. Demostración de textura y uso (ASMR / primer plano)**
Primerísimos planos de la textura del producto, aplicación en la piel, cómo se absorbe. Sin voz si quieres. Es el formato de skincare más consumido en Reels y TikTok, y no requiere talento frente a cámara.

**3. Antes / después y resultados progresivos**
Powerful para **Aurora** (premium exige prueba), pero con cuidado: documenta resultados reales y honestos ("día 1 vs. día 30"), nunca promesas milagrosas. La credibilidad vale más que el drama.

**4. Social proof (testimonios y UGC)**
Videos de clientas reales en Bogotá usando los productos, capturas de reseñas de WhatsApp, resposterías. Para un negocio local, "otra bogotana lo usó y le funcionó" convierte más que cualquier pauta.

**5. Rutinas completas ("GRWM" / Get Ready With Me)**
Aquí brilla tu escalonado: una rutina que integre **Luna** (cuerpo) + **Sol** (maquillaje natural) + **Aurora** (facial) vende el ritual completo, no productos sueltos. Es tu diferenciador de portafolio convertido en contenido.

**6. Bastidores y marca**
Cómo se empaca un pedido, tu historia como emprendedora, por qué elegiste cada ingrediente. Humaniza y funciona especialmente bien para justificar el precio premium de Aurora.

## Dos advertencias importantes

- **Cuidado con las afirmaciones**: en Colombia, INVIMA regula lo que puedes decir de cosméticos. Evita prometer tratar condiciones médicas ("cura", "trata acné") y quédate en términos cosméticos ("hidrata", "mejora la apariencia").
- **El maquillaje natural (Sol) es más visual y tendencial; el skincare (Aurora, Luna) es más educativo.** Alterna ambos:educación convierte para Aurora/Luna, tendencia y entretenimiento alcance para Sol.

## Regla práctica 40/30/30

Para arrancar: **40% educativo, 30% demostración/rutinas, 30% social proof y marca**. Con eso cubres descubrimiento, confianza y conversión sin saturar de venta directa.

¿Te preparo una lista de 10-15 ideas concretas de posts (título + formato + producto) para que tengas tu primer lote listo?

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Excelente pregunta, porque es la correcta: en una guerra de precios entre tres marcas locales, normalmente pierden las tres. La estrategia es **mover la competencia del terreno del precio al terreno del valor**. Aquí tienes las palancas concretas para tu caso:

## 1. Tu ventaja estructural: el portafolio escalonado

Ya lo tienes y tus competidores probablemente no: **Luna → Sol → Aurora** es un sistema, no un catálogo. Ellos venden productos; tú puedes vender un **camino**. Comunícalo explícitamente: "Empieza donde quieras, crece con nosotras". Quien entra con Luna no es un cliente de $X, es una clienta en construcción. Eso te permite mantener a Aurora en premium sin justificarlo contra precios ajenos.

## 2. Diferenciación local que ellos probablemente no explotan

Ambos compiten en Bogotá, pero apuesto a que ninguno tiene el **clima como eje de marca**: piel a 2.600 m de altura, sol fuerte por la altitud, frío y sequedad que deshidratan. "Skincare pensado para la piel en Bogotá" es un posicionamiento que:
- Justifica premium en **Aurora** sin compararte con nadie.
- Da a **Luna** una razón de ser (crema corporal para piel que sufre el clima).
- Te hace única en un radio de 40 km.

## 3. Encuentra tu diferenciador real espionando sus debilidades

Ejercicio práctico esta semana:
1. Lee las reseñas de **Botica Verde** y **Skin Lab** en Google Maps, Instagram y TikTok (las malas y las de 3 estrellas, que son oro).
2. Anota las quejas recurrentes: "tardó la entrega", "nadie me respondió", "no me asesoraron", "el empaque llegó dañado".
3. **Cada queja repetida es un diferenciador gratis**: conviértela en tu promesa operativa.

## 4. Palancas de valor que no tocan el precio

| Palanca | Cómo se ve en tu negocio |
|---|---|
| **Servicio cercano** | Asesoría real por WhatsApp: "cuéntame tu tipo de piel y te armo la rutina" — Skin Lab difícilmente puede hacer esto si es más grande |
| **Marca personal** | Tu historia como fundadora: la gente compra de personas, no de tiendas anónimas. Es gratuita y difícil de copiar |
| **Post-venta** | Seguimiento a los 15 días de compra, guía de uso, tips personalizados. Genera recompra sin descuento |
| **Experiencia de entrega** | Entrega rápida en Bogotá (mismo día o 24h) y unboxing cuidado: el empaque es parte de lo que se paga en **Aurora** |
| **Comunidad** | Clientas que se sienten parte ("Club Aurora" o similar) reciben acceso anticipado, no descuentos |

## 5. Disciplina de precios (la parte que se olvida)

- **Nunca descountes por presión competitiva.** Si ofreces promo, que siempre tenga razón externa: lanzamiento, temporada, aniversario. "Estamos de aniversario: -15%" comunica celebración; "-15%" comunica que tu precio estaba inflado.
- En lugar de bajar precio de Aurora, **sube valor**: incluye mini-guía de rutina, muestras de Luna en pedidos premium (que además alimenta tu escalada).
- Tu arma contra un competidor que baja precios es el contenido educativo: quien entiende *por qué* un producto vale lo que vale, no lo compara solo por precio.

**En una frase:** tu diferenciación no es un truco de marketing, es **operativa** — servicio, clima, sistema de productos y cercanía — y se construye con las quejas que tus competidores ignoran.

¿Quieres que te arme una plantilla de mini-análisis competitivo (qué mirar, dónde, y cómo volcarlo en decisiones) para que la llenes con lo que encuentres de Botica Verde y Skin Lab?

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Perfecto momento para preguntarlo, porque en el primer trimestre el error clásico es medir todo (y no actuar sobre nada). Mi enfoque: **pocos KPIs, cada uno atado a una decisión**. El trimestre 1 es de aprendizaje, no de optimización.

## Tus KPIs por etapa del embudo

| Etapa | KPI | Por qué importa | Referencia realista |
|---|---|---|---|
| **Alcance** | Alcance mensual en IG/TikTok (tendencia %) | ¿Te está descubriendo gente nueva? | Crecer mes a mes, aunque sea poco |
| **Engagement** | Tasa de engagement (interacciones ÷ alcance) | Calidad de la audiencia, no cantidad | 3-6% ya es bueno en cuenta pequeña |
| **Engagement** | Guardados + compartidos por post | Intención real: "esto me sirve" | Mejor predictor de venta que los likes |
| **Captura** | Conversaciones WhatsApp iniciadas/semana | Tu canal de cierre en Bogotá | Único KPI diario útil |
| **Captura** | Suscriptores de email nuevos/mes | Alimenta tu escalada Luna → Sol → Aurora | 50-150/mes sería un buen arranque |
| **Conversión** | **Pedidos por mes** | El KPI más honesto que existe | No hay excusa: se cuenta solo |
| **Conversión** | Tasa de conversión del sitio | ¿El tráfico sirve o es ruido? | 1-2% es razonable en ecommerce pequeño |
| **Conversión** | **Ticket promedio** | Si sube sin descuentos, tu propuesta de valor funciona | Comparar mes a mes, no contra otros |

## Los 3 KPIs estratégicos (solo tuyos)

Estos son los que validan *tu* estrategia, no benchmarks genéricos:

1. **Mix de entrada**: % de clientas nuevas que compran primero Luna vs. Sol vs. Aurora. Te dice cuál es tu verdadera puerta de entrada (puede que no sea la que asumes).
2. **Escalada**: % de compradoras de Luna que compran Sol o Aurora dentro del trimestre. Si es >10-15%, tu sistema de portafolio funciona.
3. **Recompra a 60-90 días**: las cremas se agotan; si no hay recompra, el problema es producto o post-venta, no marketing.

## Si solo pudieras medir 5 cosas

Pedidos por mes · conversaciones WhatsApp · ticket promedio · mix de entrada por producto · recompra a 90 días. Todo lo demás es secundario en el trimestre 1.

## Cadencia de revisión

- **Semanal (15 min):** pedidos, conversaciones WhatsApp, contenido publicado vs. planificado (¿cumpliste tu batching?).
- **Mensual (1 hora):** alcance, engagement, lista de email, ticket promedio, mix por producto.
- **Fin de trimestre:** la revisión grande — ¿qué producto trajo más clientas nuevas?, ¿qué tipo de contenido (educativo/demostración/social proof) generó más conversaciones?, y con eso decides qué se duplica en el trimestre 2.

## Dos advertencias

- **Vanity metrics fuera:** seguidores y likes no pagan facturas. Un Reel viral con cero conversaciones por WhatsApp es entretenimiento, no marketing.
- **CAC solo cuando enciendas pauta:** si el trimestre 1 es orgánico, no tienes costo de adquisición real que medir; ese KPI entra cuando actives Meta o Google Ads.

¿Quieres que te arme el scorecard como tabla lista para copiar a una hoja de cálculo (columnas, fórmulas y metas sugeridas por mes)?

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

Tu producto más caro es **Aurora**, así que esta campaña es 100% para él. Aquí el plan:

---

# Campaña: "Ritual Aurora" (4 semanas)

## Objetivo

Vender **Aurora** durante 4 semanas y posicionarlo como *el* set facial premium de Bogotá, sin tocar el precio. Meta sugerida: **duplica tus ventas mensuales actuales de Aurora** como piso (ej.: si vendes 4 al mes, apunta a 8-10 en la ventana de campaña) y genera **30+ conversaciones WhatsApp que mencionen Aurora**.

## Audiencia

Dos segmentos, un mismo producto:

| Segmento | Quiénes son | Por qué importan |
|---|---|---|
| **A. Clientas actuales** | Compradoras de Luna y Sol en tu base | Son las más baratas de convertir: ya confían en ti. Aurora es su siguiente paso natural |
| **B. Prospectas premium** | Mujeres 28-45 en Bogotá, interesadas en skincare, acostumbradas a invertir en su rutina facial | El volumen nuevo. Buscan calidad justificada, no ofertas |

## Canales

- **Instagram** (núcleo): todo el storytelling de la campaña vive aquí.
- **WhatsApp Business** (cierre): respuestas personalizadas + outreach 1:1 a clientas de Luna y Sol.
- **Email** (2 envíos): teaser semana 1, oferta semana 4.
- **TikTok** (apoyo): mismo video de Reels, sin edición extra.
- **Opcional — Meta Ads**: presupuesto pequeño solo para retargeting (visitas al sitio / interacciones) o interesadas en skincare en Bogotá. Si lo activas, mide CAC de Aurora desde el día 1.

## Mensaje principal

> **"Aurora: el ritual facial premium para la piel que vive a 2.600 metros."**

Mensajes de apoyo: lujo justificado (qué tiene dentro, por qué vale lo que vale), cercanía (asesoría 1:1 por WhatsApp, algo que Botica Verde y Skin Lab difícilmente igualan), y belleza local (tu piel no es la de un tutorial gringo). **Importante:** ajusta los atributos a lo que Aurora realmente contiene y quédate en términos INVIMA-safe: *hidrata, mejora la apariencia, aporta luminosidad*. Nunca "trata" ni "cura".

## Plan semanal

| Semana | Foco | Contenido clave | CTA |
|---|---|---|---|
| **1. Sembrar** | El problema que Aurora resuelve | Reel educativo: "¿por qué tu piel sufre el clima de Bogotá?"; carrusel "qué hace premium a un set facial"; encuesta en historias; email teaser a tu lista | Suave: "Guarda este post" / "Escribe AURORA por WhatsApp y recibe la guía de rutina" |
| **2. Revelar** | Mostrar Aurora sin venderlo aún | Video ASMR de texturas; unboxing detallado (qué incluye el set); bastidores de tu empaque; miniserie en historias "3 cosas de Aurora que no sabías" | "Pregúntame lo que quieras sobre Aurora" (caja de preguntas) |
| **3. Probar** | Prueba social | Testimonios reales de clientas de Aurora; "día 1 vs. día 30" honesto; respuestas en video a las preguntas de la semana 2; UGC si ya tienes | "Reserva tu Aurora esta semana" (sin presión de compra aún) |
| **4. Convertir** | Venta directa con razón externa | "Semana Aurora": las primeras 10 compradoras reciben una mini de cortesía + asesoría de rutina 1:1 por WhatsApp (regalo, no descuento); cuenta regresiva en historias; email de oferta a toda tu lista; mensaje 1:1 a compradoras de Luna y Sol | Duro: "Pide tu Aurora hoy" / link directo |

El regalo de la semana 4 cumple doble función: protege el precio premium de Aurora y siembra la escalada hacia Luna sin desviar el contenido de la campaña (que es 100% Aurora).

## Métricas de éxito

| Métrica | Meta orientativa |
|---|---|
| **Pedidos de Aurora** (north star) | 2x tu baseline mensual |
| Conversaciones WhatsApp mencionando Aurora | 30+ en las 4 semanas |
| Conversación → venta | ≥ 25-30% |
| Guardados + compartidos en posts de Aurora | Que al menos 3 posts superen tu promedio |
| Apertura email | ≥ 35% |
| Alcance de no-seguidoras en IG | En crecimiento semana a semana (descubrimiento) |
| Ticket promedio del mes | Debe subir (Aurora arrastra el promedio) |

**Cadencia de revisión:** 15 minutos cada viernes de campaña (pedidos, conversaciones, qué contenido funcionó) y una revisión completa al cierre: qué semana trajo más conversaciones y qué formato vendió más — eso define tu próxima campaña de Aurora.

¿Quieres que te escriba los textos concretos (captions, guion del Reel de la semana 1 y el email teaser) para arrancar sin bloqueo creativo?


## Respuesta completa

Tu producto más caro es **Aurora**, así que esta campaña es 100% para él. Aquí el plan:

---

# Campaña: "Ritual Aurora" (4 semanas)

## Objetivo

Vender **Aurora** durante 4 semanas y posicionarlo como *el* set facial premium de Bogotá, sin tocar el precio. Meta sugerida: **duplica tus ventas mensuales actuales de Aurora** como piso (ej.: si vendes 4 al mes, apunta a 8-10 en la ventana de campaña) y genera **30+ conversaciones WhatsApp que mencionen Aurora**.

## Audiencia

Dos segmentos, un mismo producto:

| Segmento | Quiénes son | Por qué importan |
|---|---|---|
| **A. Clientas actuales** | Compradoras de Luna y Sol en tu base | Son las más baratas de convertir: ya confían en ti. Aurora es su siguiente paso natural |
| **B. Prospectas premium** | Mujeres 28-45 en Bogotá, interesadas en skincare, acostumbradas a invertir en su rutina facial | El volumen nuevo. Buscan calidad justificada, no ofertas |

## Canales

- **Instagram** (núcleo): todo el storytelling de la campaña vive aquí.
- **WhatsApp Business** (cierre): respuestas personalizadas + outreach 1:1 a clientas de Luna y Sol.
- **Email** (2 envíos): teaser semana 1, oferta semana 4.
- **TikTok** (apoyo): mismo video de Reels, sin edición extra.
- **Opcional — Meta Ads**: presupuesto pequeño solo para retargeting (visitas al sitio / interacciones) o interesadas en skincare en Bogotá. Si lo activas, mide CAC de Aurora desde el día 1.

## Mensaje principal

> **"Aurora: el ritual facial premium para la piel que vive a 2.600 metros."**

Mensajes de apoyo: lujo justificado (qué tiene dentro, por qué vale lo que vale), cercanía (asesoría 1:1 por WhatsApp, algo que Botica Verde y Skin Lab difícilmente igualan), y belleza local (tu piel no es la de un tutorial gringo). **Importante:** ajusta los atributos a lo que Aurora realmente contiene y quédate en términos INVIMA-safe: *hidrata, mejora la apariencia, aporta luminosidad*. Nunca "trata" ni "cura".

## Plan semanal

| Semana | Foco | Contenido clave | CTA |
|---|---|---|---|
| **1. Sembrar** | El problema que Aurora resuelve | Reel educativo: "¿por qué tu piel sufre el clima de Bogotá?"; carrusel "qué hace premium a un set facial"; encuesta en historias; email teaser a tu lista | Suave: "Guarda este post" / "Escribe AURORA por WhatsApp y recibe la guía de rutina" |
| **2. Revelar** | Mostrar Aurora sin venderlo aún | Video ASMR de texturas; unboxing detallado (qué incluye el set); bastidores de tu empaque; miniserie en historias "3 cosas de Aurora que no sabías" | "Pregúntame lo que quieras sobre Aurora" (caja de preguntas) |
| **3. Probar** | Prueba social | Testimonios reales de clientas de Aurora; "día 1 vs. día 30" honesto; respuestas en video a las preguntas de la semana 2; UGC si ya tienes | "Reserva tu Aurora esta semana" (sin presión de compra aún) |
| **4. Convertir** | Venta directa con razón externa | "Semana Aurora": las primeras 10 compradoras reciben una mini de cortesía + asesoría de rutina 1:1 por WhatsApp (regalo, no descuento); cuenta regresiva en historias; email de oferta a toda tu lista; mensaje 1:1 a compradoras de Luna y Sol | Duro: "Pide tu Aurora hoy" / link directo |

El regalo de la semana 4 cumple doble función: protege el precio premium de Aurora y siembra la escalada hacia Luna sin desviar el contenido de la campaña (que es 100% Aurora).

## Métricas de éxito

| Métrica | Meta orientativa |
|---|---|
| **Pedidos de Aurora** (north star) | 2x tu baseline mensual |
| Conversaciones WhatsApp mencionando Aurora | 30+ en las 4 semanas |
| Conversación → venta | ≥ 25-30% |
| Guardados + compartidos en posts de Aurora | Que al menos 3 posts superen tu promedio |
| Apertura email | ≥ 35% |
| Alcance de no-seguidoras en IG | En crecimiento semana a semana (descubrimiento) |
| Ticket promedio del mes | Debe subir (Aurora arrastra el promedio) |

**Cadencia de revisión:** 15 minutos cada viernes de campaña (pedidos, conversaciones, qué contenido funcionó) y una revisión completa al cierre: qué semana trajo más conversaciones y qué formato vendió más — eso define tu próxima campaña de Aurora.

¿Quieres que te escriba los textos concretos (captions, guion del Reel de la semana 1 y el email teaser) para arrancar sin bloqueo creativo?