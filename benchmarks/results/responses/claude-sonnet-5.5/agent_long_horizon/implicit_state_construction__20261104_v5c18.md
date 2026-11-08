# Claude Sonnet 5.5 — agent_long_horizon/implicit_state_construction

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.05 | quality: 10.0
- latency_total: 86.604s | tokens_per_second: 133.4
- input_tokens: 21738 | output_tokens: 10525

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

¡Hola, Camila! Sí, me queda claro. Esto es lo que tengo:

**Tu negocio:** tienda online en Colombia, con un único mercado por ahora: **Bogotá**.

**Tus productos:**
- **Aurora**: set de cuidado facial, precio **premium**
- **Sol**: kit de maquillaje natural, precio **medio**
- **Luna**: crema corporal, precio **de entrada**

**Tus competidores principales (ambos en Bogotá):**
- **Botica Verde**
- **Skin Lab**

Con tres productos en tres niveles de precio, podemos pensar a Luna como puerta de entrada, a Sol como producto intermedio y a Aurora como producto de mayor valor. Eso da mucho juego para campañas.

¿Qué quieres planificar primero? Por ejemplo, un lanzamiento, una promoción para uno de los productos, una campaña para ganar clientes frente a Botica Verde o Skin Lab, o algo distinto. Cuéntame también si tienes un presupuesto o fechas en mente, y empezamos.

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Aquí va una propuesta basada en lo que me has contado:

**"Cuidado de la piel y maquillaje natural para cada etapa de tu rutina, desde el cuerpo hasta el rostro, con entrega en Bogotá. Con Luna, Sol y Aurora, empiezas con lo esencial y creces hacia un cuidado más completo a tu ritmo y a tu presupuesto."**

Me apoyé en tres cosas:
- **Tu escalera de precios** (Luna, Sol y Aurora), que permite entrar con poco y crecer hacia el producto premium.
- **El enfoque natural de Sol**, que di por hecho como eje de la marca. Si no aplica a Aurora y Luna, puedo ajustarlo.
- **Tu mercado único, Bogotá**, para reforzar cercanía y entrega local.

Para diferenciarte de Botica Verde y Skin Lab, la propuesta necesita un elemento que ellos no puedan decir. ¿Qué te hace distinta a ti? Por ejemplo, ingredientes, origen, atención personalizada o rapidez de entrega. Con eso la afino y la hago más específica.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Con lo que sé de tu negocio (online, solo Bogotá, tres productos en tres niveles de precio y dos competidores locales), este sería mi orden de prioridad:

**1. Instagram y TikTok (orgánico + Reels/videos cortos)**
- Es donde se decide la compra en belleza: tutoriales, antes y después, rutinas.
- **Luna** (precio de entrada) es ideal para contenido viral y atraer gente nueva.
- **Sol** funciona bien con tutoriales de maquillaje natural.

**2. Meta Ads (Instagram/Facebook) segmentados a Bogotá**
- Te permite limitar la inversión a tu único mercado y no desperdiciar presupuesto.
- Usa **Luna como producto gancho** para captar clientes y haz **retargeting** hacia Sol y Aurora.

**3. WhatsApp Business**
- En Colombia es clave para resolver dudas y cerrar ventas.
- Es especialmente útil para **Aurora**, porque un producto premium suele necesitar más confianza y asesoría antes de comprarse.

**4. Google (Búsqueda y Shopping)**
- Capta a quienes ya buscan lo que vendes. Considera también campañas de marca y comparación frente a **Botica Verde** y **Skin Lab**, sin atacarlos directamente.

**5. Email/WhatsApp para recompra**
- Cuando alguien compra Luna, es el canal para llevarlo a Sol y Aurora, que es lo que hace funcionar tu escalera de precios.

**6. Microinfluencers de Bogotá** (complemento)
- Mejor que figuras grandes si tu presupuesto es limitado. Úsalos sobre todo para **Aurora**, donde la recomendación de alguien confiable pesa más.

**Si tienes que empezar con poco:** Instagram/TikTok + Meta Ads con Luna + WhatsApp Business.

Para afinar esto necesito saber dos cosas que aún no me has dicho: el **rango de edad o perfil de tu clienta ideal** y tu **presupuesto mensual aproximado** para marketing. ¿Me los compartes?

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Estas son las frecuencias que recomiendo para los canales con contenido orgánico de los que hablamos. Es un punto de partida realista para un negocio pequeño:

| Canal | Frecuencia | Formato principal |
|---|---|---|
| **Instagram** | 3-4 Reels/semana + 1-2 carruseles o posts/semana + Stories casi a diario (3-5) | Reels de rutinas y tutoriales, Stories con dudas, reseñas y detrás de cámaras |
| **TikTok** | 3-5 videos/semana (mínimo 3) | Videos cortos, tendencias adaptadas, antes y después |
| **WhatsApp Business** | Estados 3-4 veces/semana + 1 mensaje/semana a tu lista de difusión (máximo 2) | Novedades, ofertas puntuales, pruebas sociales |
| **Email** | 1 correo cada 1-2 semanas + flujos automáticos (bienvenida, post-compra) | Rutinas, lanzamientos, recompra de Luna hacia Sol y Aurora |
| **Microinfluencers de Bogotá** | 2-4 colaboraciones/mes | Reseñas y rutinas, sobre todo con Aurora |

**Cómo repartir los temas entre tus productos:**
- **~50% Luna:** contenido de alcance y atracción de clientes nuevos.
- **~30% Sol:** tutoriales de maquillaje natural.
- **~20% Aurora:** educación sobre la rutina, resultados y testimonios, para generar confianza en el producto premium.

**Consejos para sostenerlo:**
- **Grábalo por lotes:** una sesión semanal puede darte el material para Instagram y TikTok, ya que el mismo video sirve en ambos.
- **Prefiere la constancia al volumen:** es mejor publicar 3 veces por semana durante meses que 7 durante dos semanas y abandonar.
- **Empieza con menos si estás sola:** Instagram 3 Reels/semana, TikTok reutilizando esos videos y WhatsApp con 2 estados/semana. Luego sube el ritmo.

Puedo armarte un calendario semanal con temas por producto y canal. Para ajustarlo me ayudaría saber cuánto tiempo o equipo tienes para crear contenido, y lo que sigue pendiente: el perfil de tu clienta ideal y tu presupuesto mensual de marketing.

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Para skincare, el contenido que mejor funciona es el que **demuestra resultados y educa**, más que el que solo muestra el producto. Lo aplico a tu caso:

**1. Rutinas paso a paso (Reels/TikTok)**
- "Mi rutina de 3 pasos en la mañana y en la noche".
- Es el formato ideal para **Aurora**, porque al ser un set muestra cómo se usa cada pieza y justifica el precio premium.

**2. Antes y después / progreso en el tiempo**
- Piel a la semana 1, 4 y 8, o textura y aplicación en primer plano.
- Sé honesta con los tiempos y evita prometer resultados médicos ("cura el acné", "elimina manchas"). Es mejor decir "mi experiencia" o "resultados de clientas".

**3. Educación breve**
- Qué hace cada paso, en qué orden aplicarlo y errores comunes.
- Si hablas de **Bogotá** (altura, radiación UV alta, clima seco o frío), conectas con tu público local y te diferencias de contenido genérico.

**4. Prueba social**
- Reseñas de clientas, mensajes de WhatsApp (con permiso), unboxings y contenido de microinfluencers bogotanas.
- Pesa mucho en **Aurora**, donde la confianza es clave para pagar más.

**5. Textura y aplicación (contenido sensorial)**
- Primeros planos de la crema, cómo se absorbe y cómo se siente.
- Funciona muy bien con **Luna**, que además es tu producto de entrada y de mayor alcance.

**6. Detrás de cámaras**
- Cómo eliges ingredientes, cómo empacas pedidos y quién está detrás de la marca. Esto te diferencia de **Botica Verde** y **Skin Lab**.

**7. Responder dudas (Stories, cajas de preguntas, WhatsApp)**
- "¿Piel sensible?", "¿cuál va primero?", "¿cuánto dura el set?". Esto genera conversación y ventas.

**Cómo priorizar según tu escalera de precios:**
- **Luna:** texturas, uso diario y contenido viral para atraer.
- **Aurora:** rutinas, resultados y testimonios para generar confianza.
- **Sol** no es skincare, pero puedes cruzarlo con Aurora en contenido de "piel preparada antes del maquillaje natural".

Si quieres, el siguiente paso es armarte un calendario de dos semanas con ideas de Reels por producto. Para ajustarlo, cuéntame el perfil de tu clienta ideal y cuánto tiempo tienes para crear contenido.

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

La clave es competir por **por qué te eligen**, no por cuánto cuestas. Así lo aplicaría a Botica Verde y Skin Lab en Bogotá:

**1. Elige un territorio que ellos no ocupen**
- Revisa qué comunican Botica Verde y Skin Lab (sus redes, su web, sus reseñas) y busca el hueco. Yo no conozco sus propuestas, así que conviene que lo verifiques tú.
- Ese hueco puede ser un ingrediente, un tipo de piel, una rutina simple o un tono de marca más cercano.

**2. Diferénciate con la escalera Luna → Sol → Aurora**
- Un competidor puede copiar un producto, pero es más difícil copiar una **ruta completa**: "empieza con Luna, suma Sol, crece a Aurora".
- Ofrece **sets o rutinas** (por ejemplo, Luna + Aurora) en lugar de descuentos sueltos. Subes el valor percibido sin bajar precios.

**3. Protege el posicionamiento de cada producto**
- **Aurora (premium):** nunca la descuentes de forma directa. Aporta valor con asesoría por WhatsApp, muestras, empaque cuidado y garantía de satisfacción.
- **Sol (medio):** compite con tutoriales y guía de tonos, que reducen la duda de compra.
- **Luna (entrada):** es el producto más expuesto a comparación de precios. Úsala como gancho de captación, pero apóyala con textura, resultados y reseñas, no con ofertas agresivas.

**4. Experiencia local en Bogotá**
- Entregas rápidas y confiables en la ciudad.
- Contenido adaptado a la altura, el clima y la radiación UV.
- Microinfluencers bogotanas y comunidad local.

**5. Servicio y cercanía**
- Atención personalizada por WhatsApp Business, con recomendaciones según el tipo de piel.
- Seguimiento posventa: "¿cómo te fue con Luna?, ¿quieres probar Sol?".

**6. Confianza como ventaja**
- Reseñas reales, resultados honestos y transparencia sobre ingredientes y origen. Si tus competidores no lo hacen bien, es un diferenciador fuerte.

**7. Programa de fidelización, en lugar de descuentos**
- Puntos, regalos por recompra o acceso anticipado a lanzamientos. Premias la lealtad sin enseñar que "solo se compra en oferta".

**Qué evitar**
- Descuentos generales y constantes.
- Mencionar o atacar a Botica Verde o Skin Lab por su nombre.
- Prometer resultados médicos.

**Sobre el diferenciador:** ya te he preguntado antes qué te hace distinta (ingredientes, origen, atención personalizada, rapidez de entrega) y aún no lo sé. Con eso puedo convertir estas ideas en un mensaje concreto. También me falta el perfil de tu clienta ideal y tu presupuesto mensual de marketing. ¿Me los compartes?

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Para tu primer trimestre te recomiendo pocos KPIs, organizados por etapa del embudo y conectados con tu escalera Luna → Sol → Aurora.

## 1. KPIs de negocio (los que importan)
| KPI | Por qué |
|---|---|
| **Ingresos y pedidos por producto** | Muestra cuál jala más: Luna, Sol o Aurora |
| **Ticket promedio (AOV)** | Si sube, tu escalera funciona |
| **CAC** (costo de adquirir una clienta) | Debe ser menor que el margen de tu primera compra, o que el valor de la clienta en el tiempo |
| **ROAS** de Meta Ads y Google | Su punto de equilibrio depende de tu margen por producto |
| **Tasa de recompra** | Clave para que Luna lleve a Sol y Aurora |

## 2. KPIs de tu escalera de producto
- **% de compradoras de Luna que compran Sol o Aurora** en 30, 60 y 90 días.
- **Tiempo promedio entre la primera y la segunda compra.**
- **Ventas de Aurora vía WhatsApp:** consultas recibidas → conversaciones → ventas.
- **Margen por producto,** para no celebrar ventas de Luna que apenas dejan ganancia.

## 3. KPIs por canal
- **Instagram/TikTok:** alcance, retención de video (¿ven más de 3 segundos?), guardados y compartidos, y visitas al perfil o al enlace. Pesan más que los "me gusta".
- **Meta Ads:** CTR, costo por clic, costo por compra y frecuencia (si pasa de 3-4, hay fatiga de anuncio).
- **Google:** búsquedas de tu marca y de tus productos. Si crecen, tu reconocimiento en Bogotá está subiendo.
- **WhatsApp:** tiempo de respuesta y % de conversaciones que cierran en venta.
- **Email:** tasa de apertura, clics y ventas por flujo (bienvenida, post-compra).
- **Microinfluencers:** ventas o visitas con código o enlace propio, y costo por venta.

## 4. KPIs de tu tienda online
- **Tasa de conversión** (como referencia, en e-commerce suele estar entre 1% y 3%, pero varía mucho).
- **Abandono de carrito** y **% de tráfico desde Bogotá.**

## 5. Cómo manejarlo en el trimestre
- **Mes 1:** configura el seguimiento (Meta Pixel, Google Analytics, códigos o enlaces por canal) y mide tu línea base. Todavía no hay que exigir resultados.
- **Mes 2:** optimiza. Apaga lo que no convierte y duplica lo que sí.
- **Mes 3:** mide recompra y venta cruzada, y decide dónde invertir más.
- **Revisión:** semanal para anuncios y contenido, mensual para negocio.

## 6. Cómo fijar las metas
No te doy cifras objetivo porque dependen de tu punto de partida y tu presupuesto. Puedes fijarlas así:
1. Mide tu línea base en las primeras 2-4 semanas.
2. Define metas realistas de mejora sobre ella.
3. Calcula tu **CAC máximo** a partir del margen de cada producto.

Si me das tu margen aproximado por producto y tu presupuesto mensual de marketing, te armo una tabla con metas para los tres meses. También me ayudaría saber cuál es tu clienta ideal y qué te distingue de Botica Verde y Skin Lab, para decidir qué KPIs de marca vale la pena seguir.

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

# Campaña de 4 semanas: Aurora, el set de cuidado facial premium

Como Aurora es tu producto más caro, la campaña se centra en **generar confianza**, no en bajar el precio. Todo gira en torno a Aurora, sin descuentos directos.

## Objetivo
**Generar las primeras ventas de Aurora (o aumentarlas) en Bogotá** y construir una base de clientas con reseñas y testimonios reales.

Objetivos secundarios:
- Conseguir conversaciones de WhatsApp con interesadas en Aurora.
- Reunir prueba social (reseñas, fotos, videos) para usarla después.

## Audiencia
No me has dado el perfil de tu clienta ideal, así que parto de supuestos que debes validar:
- **Mujeres en Bogotá** interesadas en skincare y con disposición a pagar por un set premium.
- **Tres grupos:**
  1. **Público frío:** intereses en skincare, rutinas faciales y belleza natural.
  2. **Público tibio:** quienes ya interactuaron con tu Instagram/TikTok, visitaron la página de Aurora o dejaron el carrito.
  3. **Clientas actuales:** quienes ya compraron en tu tienda y pueden querer subir a Aurora.

## Canales
| Canal | Rol en la campaña de Aurora |
|---|---|
| **Instagram + TikTok (orgánico)** | Rutinas, textura, educación y resultados de Aurora |
| **Meta Ads (Bogotá)** | Alcance en público frío y retargeting a quienes vieron Aurora |
| **WhatsApp Business** | Asesoría personalizada y cierre de venta de Aurora |
| **Microinfluencers bogotanas** | Reseñas y rutinas con Aurora |
| **Email/WhatsApp a clientas** | Aviso y oferta de valor de Aurora a tu base |

## Mensaje principal
**"Aurora: una rutina facial completa, pensada para tu piel en Bogotá."**

Ejes de apoyo:
- **Rutina simple:** cada pieza de Aurora tiene su paso y su razón.
- **Cuidado para el clima de Bogotá:** altura, sequedad, frío y radiación UV.
- **Confianza:** asesoría por WhatsApp y reseñas reales.

Evita promesas médicas ("elimina manchas", "cura el acné"). Usa "mi experiencia" o "resultados de clientas". Cuando tengas tu diferenciador real (ingredientes, origen, atención), reemplaza o refuerza estos ejes con él.

## Plan semana a semana

### Semana 1: Preparación y descubrimiento
- Configura el Meta Pixel, Google Analytics y enlaces o códigos por canal para medir Aurora.
- Crea una página de producto de Aurora clara, con fotos, modo de uso, ingredientes y preguntas frecuentes.
- Prepara el mensaje de bienvenida de WhatsApp para consultas sobre Aurora.
- Publica 3 Reels y 3 Stories: "Conoce Aurora", rutina paso a paso y por qué cada paso importa en Bogotá.
- Contacta y envía producto a 3-5 microinfluencers bogotanas.

### Semana 2: Educación y confianza
- Contenido: "Rutina de mañana y noche con Aurora", errores comunes y textura/aplicación en primer plano.
- Activa Meta Ads con el video que mejor funcione en público frío.
- Lanza una caja de preguntas en Stories: "¿Qué quieres saber de Aurora?".
- Empiezan a publicar las microinfluencers.

### Semana 3: Prueba social y retargeting
- Contenido: reseñas, testimonios y mensajes de WhatsApp de clientas (con permiso).
- Retargeting a quienes vieron el video, visitaron la página de Aurora o abandonaron el carrito.
- Escribe por WhatsApp o email a tus clientas actuales: "Conoce Aurora, nuestro set premium".
- Ofrece **asesoría personalizada gratis por WhatsApp** para elegir y usar Aurora.

### Semana 4: Cierre con valor, no con descuento
- Contenido: resultados y progreso de las clientas, y preguntas frecuentes de última hora.
- Ofrece un incentivo de valor: **muestra, regalo con la compra, empaque especial o garantía de satisfacción**, sin rebajar el precio de Aurora.
- Define una fecha límite clara para el incentivo.
- Haz el último empuje de retargeting y recopila reseñas de las nuevas compradoras.
- Revisa resultados y decide qué escalar.

## Métricas de éxito

| Etapa | Métrica |
|---|---|
| **Alcance** | Alcance y retención de video de los contenidos de Aurora |
| **Interés** | Guardados, compartidos, visitas a la página de Aurora, clics |
| **Conversación** | Consultas por WhatsApp sobre Aurora |
| **Venta** | Ventas de Aurora, tasa de conversión de la página y abandono de carrito |
| **Rentabilidad** | CAC de Aurora y ROAS de los anuncios |
| **Confianza** | Reseñas y testimonios nuevos de Aurora |

**Sobre las metas:** no te doy cifras porque dependen de tu punto de partida, tu presupuesto y el margen de Aurora. Mide la línea base en la semana 1, fija metas de mejora y calcula tu **CAC máximo** a partir del margen de Aurora. Si el costo por venta supera ese margen, pausa y ajusta el mensaje o la audiencia.

**Revisión:** semanal, y al final de la semana 4 compara resultados con la línea base.

## Lo que me falta para afinarla
1. **Tu presupuesto mensual de marketing**, para repartirlo entre anuncios, microinfluencers y muestras.
2. **El margen y precio de Aurora**, para calcular el CAC máximo.
3. **El perfil de tu clienta ideal.**
4. **Qué te distingue de Botica Verde y Skin Lab**, para dar al mensaje principal un diferenciador real.

Con eso puedo darte metas numéricas para las 4 semanas y un calendario día por día de publicaciones sobre Aurora.


## Respuesta completa

# Campaña de 4 semanas: Aurora, el set de cuidado facial premium

Como Aurora es tu producto más caro, la campaña se centra en **generar confianza**, no en bajar el precio. Todo gira en torno a Aurora, sin descuentos directos.

## Objetivo
**Generar las primeras ventas de Aurora (o aumentarlas) en Bogotá** y construir una base de clientas con reseñas y testimonios reales.

Objetivos secundarios:
- Conseguir conversaciones de WhatsApp con interesadas en Aurora.
- Reunir prueba social (reseñas, fotos, videos) para usarla después.

## Audiencia
No me has dado el perfil de tu clienta ideal, así que parto de supuestos que debes validar:
- **Mujeres en Bogotá** interesadas en skincare y con disposición a pagar por un set premium.
- **Tres grupos:**
  1. **Público frío:** intereses en skincare, rutinas faciales y belleza natural.
  2. **Público tibio:** quienes ya interactuaron con tu Instagram/TikTok, visitaron la página de Aurora o dejaron el carrito.
  3. **Clientas actuales:** quienes ya compraron en tu tienda y pueden querer subir a Aurora.

## Canales
| Canal | Rol en la campaña de Aurora |
|---|---|
| **Instagram + TikTok (orgánico)** | Rutinas, textura, educación y resultados de Aurora |
| **Meta Ads (Bogotá)** | Alcance en público frío y retargeting a quienes vieron Aurora |
| **WhatsApp Business** | Asesoría personalizada y cierre de venta de Aurora |
| **Microinfluencers bogotanas** | Reseñas y rutinas con Aurora |
| **Email/WhatsApp a clientas** | Aviso y oferta de valor de Aurora a tu base |

## Mensaje principal
**"Aurora: una rutina facial completa, pensada para tu piel en Bogotá."**

Ejes de apoyo:
- **Rutina simple:** cada pieza de Aurora tiene su paso y su razón.
- **Cuidado para el clima de Bogotá:** altura, sequedad, frío y radiación UV.
- **Confianza:** asesoría por WhatsApp y reseñas reales.

Evita promesas médicas ("elimina manchas", "cura el acné"). Usa "mi experiencia" o "resultados de clientas". Cuando tengas tu diferenciador real (ingredientes, origen, atención), reemplaza o refuerza estos ejes con él.

## Plan semana a semana

### Semana 1: Preparación y descubrimiento
- Configura el Meta Pixel, Google Analytics y enlaces o códigos por canal para medir Aurora.
- Crea una página de producto de Aurora clara, con fotos, modo de uso, ingredientes y preguntas frecuentes.
- Prepara el mensaje de bienvenida de WhatsApp para consultas sobre Aurora.
- Publica 3 Reels y 3 Stories: "Conoce Aurora", rutina paso a paso y por qué cada paso importa en Bogotá.
- Contacta y envía producto a 3-5 microinfluencers bogotanas.

### Semana 2: Educación y confianza
- Contenido: "Rutina de mañana y noche con Aurora", errores comunes y textura/aplicación en primer plano.
- Activa Meta Ads con el video que mejor funcione en público frío.
- Lanza una caja de preguntas en Stories: "¿Qué quieres saber de Aurora?".
- Empiezan a publicar las microinfluencers.

### Semana 3: Prueba social y retargeting
- Contenido: reseñas, testimonios y mensajes de WhatsApp de clientas (con permiso).
- Retargeting a quienes vieron el video, visitaron la página de Aurora o abandonaron el carrito.
- Escribe por WhatsApp o email a tus clientas actuales: "Conoce Aurora, nuestro set premium".
- Ofrece **asesoría personalizada gratis por WhatsApp** para elegir y usar Aurora.

### Semana 4: Cierre con valor, no con descuento
- Contenido: resultados y progreso de las clientas, y preguntas frecuentes de última hora.
- Ofrece un incentivo de valor: **muestra, regalo con la compra, empaque especial o garantía de satisfacción**, sin rebajar el precio de Aurora.
- Define una fecha límite clara para el incentivo.
- Haz el último empuje de retargeting y recopila reseñas de las nuevas compradoras.
- Revisa resultados y decide qué escalar.

## Métricas de éxito

| Etapa | Métrica |
|---|---|
| **Alcance** | Alcance y retención de video de los contenidos de Aurora |
| **Interés** | Guardados, compartidos, visitas a la página de Aurora, clics |
| **Conversación** | Consultas por WhatsApp sobre Aurora |
| **Venta** | Ventas de Aurora, tasa de conversión de la página y abandono de carrito |
| **Rentabilidad** | CAC de Aurora y ROAS de los anuncios |
| **Confianza** | Reseñas y testimonios nuevos de Aurora |

**Sobre las metas:** no te doy cifras porque dependen de tu punto de partida, tu presupuesto y el margen de Aurora. Mide la línea base en la semana 1, fija metas de mejora y calcula tu **CAC máximo** a partir del margen de Aurora. Si el costo por venta supera ese margen, pausa y ajusta el mensaje o la audiencia.

**Revisión:** semanal, y al final de la semana 4 compara resultados con la línea base.

## Lo que me falta para afinarla
1. **Tu presupuesto mensual de marketing**, para repartirlo entre anuncios, microinfluencers y muestras.
2. **El margen y precio de Aurora**, para calcular el CAC máximo.
3. **El perfil de tu clienta ideal.**
4. **Qué te distingue de Botica Verde y Skin Lab**, para dar al mensaje principal un diferenciador real.

Con eso puedo darte metas numéricas para las 4 semanas y un calendario día por día de publicaciones sobre Aurora.