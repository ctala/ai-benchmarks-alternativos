# Mistral Large 4.0 — agent_long_horizon/implicit_state_construction

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 6.98 | quality: 8.5
- latency_total: 204.524s | tokens_per_second: 49.7
- input_tokens: 12080 | output_tokens: 12626

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

¡Hola Camila! Sí, me queda perfectamente claro. Tengo registrado:

- **Tu negocio**: Tienda online en Colombia, enfocada actualmente solo en **Bogotá**
- **Tu portafolio de 3 productos**:
  - **Aurora** (set facial) → precio **premium**
  - **Sol** (kit maquillaje natural) → precio **medio**
  - **Luna** (crema corporal) → precio **entrada**
- **Tus competidores directos en Bogotá**: **Botica Verde** y **Skin Lab**

Estoy lista para ayudarte a planificar tus campañas. ¿En qué estás pensando ahora? ¿Una campaña para lanzar algún producto específico, una promoción para competir con alguno de esos dos rivales, o algo para captar clientes nuevos en Bogotá?

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Ofrecemos cuidado personal para **todos los presupuestos en Bogotá**, con opciones que van desde nuestra crema **Luna** de precio entrada hasta el set facial **Aurora** premium, garantizando que puedas construir tu rutina ideal sin importar cuánto quieras invertir. Al ser una tienda **online 100% local**, te llevamos estos productos directamente a tu puerta en la capital con la rapidez y atención personalizada que solo un emprendimiento bogotano puede dar, diferenciándonos de grandes cadenas como Botica Verde o Skin Lab.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Para tu contexto en **Bogotá** y con productos de belleza visuales, te recomiendo este orden de prioridad:

**1. Instagram (Feed + Reels)**
Es tu vitrina principal. Usa Reels para mostrar texturas reales de **Aurora** (el premium), tutoriales rápidos de aplicación de **Sol** y comparativas de precio accesibles con **Luna**. Segmenta tus anuncios solo a Bogotá + intereses en skincare/maquillaje natural para competir directamente con Botica Verde y Skin Lab donde ya están sus clientes.

**2. TikTok**
El algoritmo favorece a cuentas nuevas sobre las grandes marcas establecidas, así que es tu oportunidad de diferenciarte de tus competidores. Crea contenido tipo "rutina de 3 pasos con mis productos" o "unboxing de Aurora", usando hashtags locales como #BogotáBeauty. Es ideal para mostrar el lado "emprendimiento local" que Botica Verde y Skin Lab no tienen.

**3. WhatsApp Business con Catálogo**
En Colombia este es tu canal de **cierre de ventas**. Configura respuestas automáticas con tiempos de entrega específicos por localidad de Bogotá (ej: "Entrega en Chapinero en 24h") para diferenciarte de la impersonalidad de tus competidores grandes. Usa el catálogo para enviar fotos de **Luna** (entrada) a quienes preguntan por precios bajos.

**4. Google Mi Negocio (gratuito)**
Esencial para captar búsquedas locales tipo "crema facial económica Bogotá" o "set cuidado premium Bogotá". Asegúrate de pedir reseñas a tus primeros clientes bogotanos para aparecer cuando compitas en búsquedas locales contra Skin Lab.

**Evita por ahora:** LinkedIn (no es tu canal B2C) y Twitter/X (poco engagement para belleza en Colombia comparado con IG/TikTok).

¿Tienes presupuesto para pauta pagada o prefieres empezar con estrategia 100% orgánica en estos canales?

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Para una emprendedora en Bogotá manejando sola la tienda, esta frecuencia es sostenible y efectiva (prioriza **consistencia sobre volumen**):

**Instagram**
- **Reels**: 4-5 por semana (tu motor de alcance orgánico; alterna entre Aurora mostrando lujo, Sol con tutoriales rápidos y Luna con "antes/después" de hidratación)
- **Feed (posts fijos)**: 3 veces por semana (fotos de alta calidad de productos en contexto bogotano: cafeterías de Chapinero, parques, etc.)
- **Stories**: Diario, mínimo 3-5 al día (encuestas, "desliza para ver precio de Luna", behind the scenes de empaques)

**TikTok**
- **1 video diario** (o mínimo 5 por semana). Como estás compitiendo con Botica Verde y Skin Lab que tienen más recursos, aquí ganas por autenticidad: muestra cómo empacas Aurora tú misma, o un "POV: usas Sol para ir a trabajar en Bogotá"

**WhatsApp Business**
- **Estados**: 2-3 al día (promoción del día: "Hoy envío gratis en Bogotá por Luna", foto de un pedido listo)
- **Mensajes masivos (broadcast)**: Máximo 1-2 veces por semana a tu lista de clientes bogotanos (para no saturar)

**Google Mi Negocio**
- **Posts**: 1-2 veces por semana (ofertas flash de 24h, nuevos ingresos de stock de Aurora, o fotos de clientes felices en Bogotá)

**Tip de eficiencia**: Graba un solo video mostrando **Aurora** y úsalo tanto en Reels como en TikTok (con textos diferentes). Así mantienes los 3 productos visibles sin triplicar tu trabajo. ¿Cuál de estos canales sientes que puedes empezar hoy mismo?

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Para skincare en Bogotá, donde la gente busca **confianza y resultados reales** (especialmente comprando online sin probar antes), estos formatos funcionan mejor, adaptados a tus tres líneas:

**1. Contenido educativo "micro-learning" (30-60 seg)**
- **"3 formas de usar Luna"** (tu producto entrada): muestra que sirve para manos, codos y como base hidratante antes de Sol. Así justificas que es entrada pero versátil.
- **"Qué contiene Aurora y por qué cuesta lo que cuesta"**: desglose de ingredientes premium vs. los genéricos de Botica Verde. Educa sobre el valor del premium.
- **Mitos del skincare bogotano**: "El clima de Bogotá reseca más de lo que crees" → conecta con Sol o Aurora según la necesidad.

**2. Social proof real (no stock photos)**
- **Antes/después honestos** (no perfectos) usando Aurora en pieles reales bogotanas, o resultados de hidratación con Luna en 7 días.
- **Testimonios en video de clientas en Bogotá**: que digan "me llegó en 2 días a Usaquén" o "lo pedí por WhatsApp y me respondieron rápido". Esto vence la desconfianza de comprar online vs. ir a la tienda física de Skin Lab.

**3. "Rutina completa" que integra tus 3 productos**
- Muestra cómo se usan juntos: Luna (base corporal), Sol (maquillaje del día), Aurora (tratamiento nocturno). Esto aumenta el ticket promedio y diferencia tu tienda de quienes venden productos sueltos como tus competidores.

**4. Behind the scenes del emprendimiento local**
- "Cómo empaco tu pedido de Aurora para que llegue perfecto a tu casa en Bogotá" o "Seleccionando los ingredientes de Sol esta semana". Esto humaniza tu marca frente a Botica Verde (corporativo) y genera lealtad.

**5. Comparativas de valor (educativas, no agresivas)**
- "Aurora vs. cremas de farmacia": explica por qué tu set premium dura X meses vs. comprar cremas sueltas.
- "Por qué Sol es mejor que el maquillaje convencional para pieles sensibles bogotanas".

**Tip específico para tu mix de precios**: Usa contenido de **Luna** para captar atención masiva (es accesible), contenido de **Sol** para mostrar resultados visibles (maquillaje natural que "se ve bien en cámara" para Reels), y contenido de **Aurora** para posicionarte como experta (tutoriales detallados que justifiquen el premium).

¿Cuál de estos formatos sientes que puedes grabar hoy con lo que tienes en casa?

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Para diferenciarte de **Botica Verde** (grande, genérico, nacional) y **Skin Lab** (técnico/clínico, distante) sin tocar los precios de **Aurora**, **Sol** o **Luna**, apuesta por la **hiper-personalización y la experiencia local bogotana**. Estas son tácticas concretas para tu contexto:

**1. La "Rutina Bogotá" personalizada por WhatsApp**
No vendas productos sueltos, vende *soluciones al clima y contaminación de Bogotá*. Ofrece asesoría gratuita por WhatsApp donde armas rutinas combinando tus 3 productos según la zona de la clienta (ej: "vives en Usaquén y trabajas en el centro, usa Luna en el cuerpo por la calefacción, Sol para el día y Aurora solo en la noche"). Botica Verde y Skin Lab no hacen esto uno a uno porque atienden a miles; tú puedes porque tu mercado es solo Bogotá.

**2. Entrega "mismo día" en zonas estratégicas**
Como eres online y local, ofrece envío express en moto propia (o aliada) en menos de 3 horas para pedidos de **Aurora** o **Sol** en localidades específicas de Bogotá (ej: Chapinero, Usaquén, La Candelaria). Esto vence a tus competidores que envían desde bodegas lejanas en 2-3 días. Cobra un valor fijo por este servicio premium, no lo des gratis (así no es guerra de precios, es servicio valorado).

**3. Garantía de riesgo cero solo para Aurora**
Como es tu producto premium y la gente duda en pagar alto precio online sin probar, ofrece: *"Si en 30 días no notas diferencia con Aurora, te devolvemos el 100% sin pedir el producto de vuelta"*. Esto justifica el precio premium (no lo bajas, eliminas el miedo) y Botica Verde difícilmente ofrece esto en su modelo masivo.

**4. Empaque que cuenta una historia local**
- **Aurora**: Caja rígida reutilizable (tipo joyería) con carta manuscrita tuya y una muestra gratis de **Luna** (cross-selling inteligente).
- **Sol**: Incluye una tarjeta impresa con "3 formas de aplicarlo para el smog de Bogotá" (referencia hiper-local que Skin Lab no usa).
- **Luna**: Sticker que diga "Hecho/seleccionado en Bogotá" + instrucciones para usarla después de caminar por la Séptima o el TransMilenio (contexto real del bogotano).

**5. Comunidad VIP cerrada para clientas de Bogotá**
Crea un grupo de WhatsApp exclusivo llamado *"Rutina Bogotá - Clientas VIP"* donde anuncies antes que en Instagram nuevos lotes de **Aurora**, o tips de belleza específicos para la altura de Bogotá. Da acceso anticipado a preventas. Esto genera lealtad que ni Botica Verde ni Skin Lab pueden replicar fácilmente.

**6. Transparencia de proceso (contenido "detrás de cámaras")**
Muestra en Reels/TikTok cómo seleccionas los productos de **Sol** o cómo empacas **Aurora** con cuidado extra. La gente paga más (precio premium) cuando ve que hay un humano detrás, no una bodega automática. Contrasta con la frialdad corporativa de tus competidores.

**¿Por dónde empezar?** Te sugiero implementar primero la **garantía de 30 días en Aurora** (reduce la objeción de compra del producto caro) y el **envío mismo día en 2-3 localidades de Bogotá** (justifica un costo de envío diferenciado). ¿Cuál de estas dos resuena más con tu operación actual?

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Para tu **primer trimestre** (Q1) en Bogotá, el objetivo no es maximizar ventas, sino **validar que tu modelo funciona**: que la gente confía en comprar online, que tus 3 rangos de precio coexisten bien y que tu diferenciación (rapidez + personalización) realmente pesa contra Botica Verde y Skin Lab.

Aquí tienes los KPIs organizados por prioridad, con la frecuencia con la que debes revisarlos:

---

### 1. KPIs de Validación (los más importantes en Q1)
Miden si tu propuesta resuena antes de gastar en escala.

- **Tasa de recompra a 30 días**: % de clientas que compran un segundo producto (cualquiera) dentro de 30 días de la primera compra.
  *Objetivo*: >20%. Si es bajo, tu producto no "engancha" o el servicio post-venta falla.
  *Por qué importa*: En skincare, si no vuelven, no hay negocio sostenible.

- **Mix de productos vendidos**: Distribución % de ventas entre **Luna** (entrada), **Sol** (medio) y **Aurora** (premium).
  *Objetivo*: Que Aurora represente al menos el 20-25% de los ingresos (no solo unidades), validando que el premium funciona en Bogotá online.
  *Alerta*: Si solo vendes Luna, estás en guerra de precios con supermercados; si solo Aurora, no estás captando volumen.

- **Tasa de "upsell" en WhatsApp**: % de pedidos donde la clienta termina comprando 2 productos (ej: Luna + Sol) en vez de 1, gracias a tu recomendación personalizada.
  *Objetivo*: >30%. Esto valida tu estrategia de "rutina personalizada" vs. venta de catálogo frío.

---

### 2. KPIs de Adquisición (Canales digitales)
- **CAC (Costo de Adquisición) por producto**: Cuánto te cuesta conseguir una clienta que compra **Aurora** vs. una que compra **Luna**.
  *Regla*: El CAC de Aurora puede ser 2-3x más alto que el de Luna, pero su margen debe cubrirlo. Si el CAC de Aurora supera el 30% de su precio de venta, pausa esa campaña.

- **Tasa de respuesta en WhatsApp**: Tiempo promedio de respuesta a mensajes nuevos (en minutos, durante horario laboral).
  *Objetivo*: <15 minutos. Esto es tu ventaja competitiva directa contra Botica Verde (que tarda horas) y Skin Lab.

- **Costo por lead calificado (CPL)**: Cuánto gastas (en ads o tiempo) para conseguir un contacto de WhatsApp que realmente pregunta por un producto específico (no solo "hola").

- **Tráfico orgánico vs. pagado en Instagram/TikTok**: % de visitas al perfil que vienen sin pagar.
  *Objetivo Q1*: Mínimo 60% orgánico. Si dependes 100% de ads, tu contenido no está resonando.

---

### 3. KPIs de Conversión (del clic a la venta)
- **Tasa de conversión por canal**: % de visitantes que compran en la web vs. % de quienes te escriben por WhatsApp y cierran.
  *Dato clave*: En Colombia, WhatsApp suele convertir 3-5x más alto que la web directa para productos de belleza. Si tu web convierte más que WhatsApp, algo falla en la experiencia de chat.

- **Tasa de abandono de carrito**: % de personas que añaden **Aurora** o **Sol** al carrito pero no compran.
  *Acción*: Si es >70%, el problema es desconfianza (soluciona con la garantía de 30 días destacada) o costo de envío sorpresa.

- **Ticket promedio (AOV)**: Valor promedio por pedido.
  *Objetivo*: Debe subir mes a mes en Q1 (ej: de $80.000 a $120.000 COP) porque estás vendiendo combos (Luna+Sol o Sol+Aurora), no productos sueltos.

---

### 4. KPIs Operativos (Logística Bogotá - tu diferenciador)
- **Tiempo promedio de entrega por localidad**: Horas desde el pago hasta la entrega en Chapinero, Usaquén, La Candelaria, etc.
  *Objetivo*: <4 horas en las zonas donde prometes "mismo día". Si sube a 24h, pierdes la ventaja sobre Skin Lab.

- **Tasa de entregas exitosas en primer intento**: % de pedidos entregados sin que la clienta no estuviera en casa.
  *Objetivo*: >90%. Si es bajo, ajusta los horarios de entrega o confirma por WhatsApp 1 hora antes.

- **Costo logístico como % del precio del producto**: Especialmente para **Luna** (precio entrada). Si el envío te cuesta el 30% del precio de Luna, estás perdiendo dinero en cada venta de entrada (a menos que sea para captar clienta y venderle Aurora después).

---

### 5. KPIs de Marca y Lealtad (validan tu diferenciación)
- **NPS (Net Promoter Score) post-compra**: Pregunta simple por WhatsApp 3 días después de recibir: *"Del 0 al 10, ¿qué tan probable es que recomiendes [tu marca] a una amiga en Bogotá?"*
  *Objetivo*: >50 (promotores). Si hay detractores (0-6), pregúntales por qué: suele ser "no llegó tan rápido como dijeron" o "el empaque se dañó".

- **Tasa de guardados (saves) en Instagram**: % de personas que guardan tus Reels de Aurora o tutoriales de Sol.
  *Por qué*: En skincare, guardar = intención de compra futura. Si tus saves son altos pero las ventas bajas, el problema es el precio o la confianza, no el contenido.

- **Tasa de crecimiento de tu lista de WhatsApp Business**: Nuevos contactos guardados por semana.
  *Objetivo*: Crecimiento constante (ej: +50 contactos/semana). Esta lista es tu activo más valioso; no depende del algoritmo de Meta.

- **Menciones cualitativas de diferenciación**: Cuenta cuántas reseñas o comentarios mencionan específicamente *"llegó rapidísimo"*, *"me atendieron personalmente"* o *"es bogotana como yo"*.
  *Meta*: Al menos 1 de cada 5 reseñas debe mencionar tu ventaja local/personal vs. los competidores.

---

### 📊 Tu "Dashboard Semanal" (revisa cada lunes 10 min)
Crea una hoja simple con estas 5 filas:

| KPI | Meta Q1 | Semana actual | Tendencia |
|-----|---------|---------------|-----------|
| Nuevas clientas (total) | 100/mes | | |
| % que compra 2do producto en 30 días | >20% | | |
| Ticket promedio | Subiendo | | |
| Tiempo respuesta WhatsApp | <15 min | | |
| Tiempo entrega promedio (Bogotá) | <4h zonas clave | | |

**Regla de oro para Q1**: Si un KPI de retención (recompra) está bajo pero el de adquisición (nuevas clientas) está alto, **no gastes más en ads**. Invierte ese dinero en mejorar el servicio post-venta o la garantía de Aurora hasta que la recompra suba.

¿Cuál de estos KPIs ya tienes forma de medir hoy (ej: ¿ya usas Google Analytics o solo ves los mensajes de WhatsApp)? Así te ayudo a automatizar el seguimiento.

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

Aquí tienes el **Plan de Campaña "Proyecto Aurora"** — 4 semanas dedicadas exclusivamente a vender tu set facial premium en Bogotá:

---

### 🎯 OBJETIVO SMART
Vender **40 unidades de Aurora** en Bogotá durante 4 semanas, con un **CAC (costo de adquisición) menor al 25% del precio de venta de Aurora**, y lograr que al menos el **30% de las compradoras de Aurora** agreguen también **Sol** o **Luna** al mismo pedido (validando que Aurora es puerta de entrada a tu portafolio).

---

### 👥 AUDIENCIA ESPECÍFICA
**Segmento principal:** Mujeres 28-42 años residentes en Bogotá (prioridad localidades: Chapinero, Usaquén, La Candelaria, Suba y Kennedy), con ingresos medios-altos, que ya han comprado productos de skincare >$150.000 COP en el último año.

**Intereses en Meta Ads:** Seguidoras de **Botica Verde** y **Skin Lab** (para robarles atención), seguidoras de influencers de belleza colombianas (ej: @camilamakeup, @skincarecolombia), interesadas en "rutina facial completa", "anti-edad", "piel luminosa", "cuidado facial premium Bogotá".

**Psicográfico clave:** Buscan **calidad sobre cantidad**, se frustran con la atención masiva de las grandes cadenas, y sienten que el clima de Bogotá (smog, altura, cambios bruscos de temperatura) les daña la piel y necesitan algo más potente que una crema básica.

---

### 📡 CANALES (Distribución del esfuerzo)
1. **Instagram (70%)**: Reels aspiracionales pero reales mostrando Aurora en contexto bogotano (ej: "Aurora antes de salir al tráfico de la Séptima"), Stories diarias con encuestas ("¿Ya usaste Aurora hoy?"), Feed con fotos de alta calidad del empaque de Aurora.
2. **WhatsApp Business (20%)**: Canal de cierre. Catálogo con fotos detalladas de Aurora, respuestas personalizadas enviando videos de cómo se usa Aurora paso a paso.
3. **TikTok (10%)**: Un video diario tipo "POV: usas Aurora en vez de solo una crema de Skin Lab" o "Unboxing Aurora: lo que incluye tu set premium".
4. **Google Mi Negocio**: Publicar 2 veces por semana sobre Aurora para captar búsquedas "set facial premium Bogotá" o "Aurora cuidado facial".

---

### 💬 MENSAJE PRINCIPAL (Único para toda la campaña)
> **"Aurora no es un gasto en tu piel, es la inversión que protege tu rostro del smog y el clima de Bogotá. Un set completo diseñado para darte resultados visibles en 30 días, con la garantía de que si no ves cambios, te devolvemos tu dinero."**

**Ángulos secundarios por semana:**
- Semana 1: *"Por qué Aurora cuesta lo que cuesta"* (educar sobre ingredientes premium vs. genéricos de Botica Verde)
- Semana 2: *"Aurora llegó a [Localidad] en 3 horas"* (prueba social + ventaja logística sobre Skin Lab)
- Semana 3: *"Solo quedan X unidades de Aurora"* (escasez real, no falsa)
- Semana 4: *"Así se ve tu piel después de 4 semanas con Aurora"* (resultados)

---

### 📅 PLAN SEMANA A SEMANA

**SEMANA 1: "Educación Premium" (Awareness)**
- **Contenido**: 5 Reels explicando cada paso del set Aurora (limpiador, sérum, crema) y por qué juntos cuestan menos que comprar 3 productos sueltos en Skin Lab. 1 post en Feed comparando Aurora vs. comprar productos separados en Botica Verde (tabla de costos y beneficios).
- **CTA**: "Comenta AURORA y te envío por DM la guía de uso exclusiva para pieles bogotanas".
- **Ads**: Campaña de tráfico (no venta) a tu perfil de Instagram, segmentada a seguidoras de Botica Verde/Skin Lab en Bogotá.
- **WhatsApp**: Activar respuesta automática para quienes escriban "AURORA": "Hola, gracias por tu interés en Aurora. ¿Vives en Bogotá? Te cuento los beneficios del envío express..."

**SEMANA 2: "Confianza y Prueba Social" (Consideration)**
- **Contenido**: 3 videos de clientas reales de Bogotá (si ya tienes, si no, graba 3 amigas tuyas) mostrando resultados de 15 días con Aurora. 1 Reel tuyo haciendo unboxing detallado de Aurora mostrando cada producto dentro. Stories con la **garantía de 30 días en Aurora** destacada.
- **Oferta**: "Esta semana: envío GRATIS mismo día en Bogotá si compras Aurora" (diferenciador clave vs. competidores que tardan 2-3 días).
- **Ads**: Campaña de mensajes (objetivo: conversaciones) a quienes vieron el 50% de los videos de Aurora en semana 1.
- **WhatsApp**: Enviar mensaje broadcast a tu lista existente: "Tengo 10 unidades de Aurora con envío gratis hoy en Bogotá. ¿Te interesa?"

**SEMANA 3: "Urgencia y Cierre" (Decision)**
- **Contenido**: Stories diarias con contador "Quedan X unidades de Aurora para envío gratis hoy". Reel mostrando pedidos de Aurora siendo empacados para salir en moto a Chapinero/Usaquén. Video "Aurora vs. tu rutina actual: 3 razones para cambiar".
- **Ads**: Retargeting a quienes agregaron Aurora al carrito pero no compraron, y a quienes visitaron tu perfil 3+ veces. Mensaje: "Aún tienes Aurora en tu carrito. Hoy envío gratis a [Localidad] si compras antes de las 6pm".
- **WhatsApp**: Mensajes 1 a 1 a leads de semanas 1-2 que no compraron: "Hola [Nombre], vi que te interesó Aurora. Tengo 2 unidades reservadas para ti hasta mañana con envío express en Bogotá. ¿Te las aparto?"

**SEMANA 4: "Última Llamada y Fidelización" (Cierre + Retención)**
- **Contenido**: Reel "Últimas 5 unidades de Aurora disponibles". Post con testimonios de quienes compraron Aurora en las semanas anteriores (fotos de ellas con Aurora). Contenido educativo para quienes YA compraron: "Cómo maximizar resultados con Aurora en tu rutina nocturna".
- **Ads**: Similar a semana 3 pero con urgencia máxima: "Último día para envío gratis de Aurora en Bogotá".
- **WhatsApp**: A quienes compraron Aurora: "¿Ya empezaste a usar Aurora? Cuéntame cómo te va y te regalo una muestra de Luna para tu próximo pedido". A quienes no compraron: "¿Aún quieres Aurora? Tengo 1 unidad disponible con descuento del 10% solo por hoy (no es guerra de precios, es última unidad)".

---

### 📊 MÉTRICAS DE ÉXITO ESPECÍFICAS PARA AURORA

| KPI | Meta en 4 semanas | Cómo medirlo |
|-----|-------------------|--------------|
| **Unidades de Aurora vendidas** | 40 unidades | Hoja de cálculo simple o Shopify/tienda online |
| **CAC de Aurora** | < 25% del precio de Aurora | (Gasto total en ads + tiempo valorado) / 40 ventas |
| **Tasa de conversión WhatsApp→Venta Aurora** | > 20% | De cada 10 personas que escriben "AURORA", 2 deben comprar en 48h |
| **Tasa de "bundle" (Aurora + otro producto)** | > 30% | % de pedidos que incluyen Aurora + Sol o Aurora + Luna |
| **Tasa de abandono de carrito Aurora** | < 60% | Si es mayor, revisar checkout o agregar más confianza (garantía visible) |
| **NPS específico de Aurora** | > 8/10 | Preguntar por WhatsApp 7 días después: "¿Del 0-10, recomendarías Aurora a una amiga en Bogotá?" |
| **Costo por lead calificado de Aurora** | < $15.000 COP | Cuánto gastas para conseguir un contacto que realmente pregunta por detalles de Aurora (no solo "hola") |
| **Guardados en contenido de Aurora** | > 5% de las vistas | En Instagram Insights, % de saves en Reels de Aurora (indica intención de compra futura) |

**Regla de decisión al final de la semana 2:** Si llevas menos de 10 ventas de Aurora pero tienes muchos leads en WhatsApp, **no gastes más en ads**, invierte ese dinero en mejorar la página de producto de Aurora (fotos, descripción de beneficios) o en ofrecer una llamada de 10 minutos por WhatsApp para cerrar la venta manualmente.

¿Tienes stock suficiente de Aurora para soportar 40 ventas en 4 semanas, o ajustamos la meta a lo que tengas disponible ahora?


## Respuesta completa

Aquí tienes el **Plan de Campaña "Proyecto Aurora"** — 4 semanas dedicadas exclusivamente a vender tu set facial premium en Bogotá:

---

### 🎯 OBJETIVO SMART
Vender **40 unidades de Aurora** en Bogotá durante 4 semanas, con un **CAC (costo de adquisición) menor al 25% del precio de venta de Aurora**, y lograr que al menos el **30% de las compradoras de Aurora** agreguen también **Sol** o **Luna** al mismo pedido (validando que Aurora es puerta de entrada a tu portafolio).

---

### 👥 AUDIENCIA ESPECÍFICA
**Segmento principal:** Mujeres 28-42 años residentes en Bogotá (prioridad localidades: Chapinero, Usaquén, La Candelaria, Suba y Kennedy), con ingresos medios-altos, que ya han comprado productos de skincare >$150.000 COP en el último año.

**Intereses en Meta Ads:** Seguidoras de **Botica Verde** y **Skin Lab** (para robarles atención), seguidoras de influencers de belleza colombianas (ej: @camilamakeup, @skincarecolombia), interesadas en "rutina facial completa", "anti-edad", "piel luminosa", "cuidado facial premium Bogotá".

**Psicográfico clave:** Buscan **calidad sobre cantidad**, se frustran con la atención masiva de las grandes cadenas, y sienten que el clima de Bogotá (smog, altura, cambios bruscos de temperatura) les daña la piel y necesitan algo más potente que una crema básica.

---

### 📡 CANALES (Distribución del esfuerzo)
1. **Instagram (70%)**: Reels aspiracionales pero reales mostrando Aurora en contexto bogotano (ej: "Aurora antes de salir al tráfico de la Séptima"), Stories diarias con encuestas ("¿Ya usaste Aurora hoy?"), Feed con fotos de alta calidad del empaque de Aurora.
2. **WhatsApp Business (20%)**: Canal de cierre. Catálogo con fotos detalladas de Aurora, respuestas personalizadas enviando videos de cómo se usa Aurora paso a paso.
3. **TikTok (10%)**: Un video diario tipo "POV: usas Aurora en vez de solo una crema de Skin Lab" o "Unboxing Aurora: lo que incluye tu set premium".
4. **Google Mi Negocio**: Publicar 2 veces por semana sobre Aurora para captar búsquedas "set facial premium Bogotá" o "Aurora cuidado facial".

---

### 💬 MENSAJE PRINCIPAL (Único para toda la campaña)
> **"Aurora no es un gasto en tu piel, es la inversión que protege tu rostro del smog y el clima de Bogotá. Un set completo diseñado para darte resultados visibles en 30 días, con la garantía de que si no ves cambios, te devolvemos tu dinero."**

**Ángulos secundarios por semana:**
- Semana 1: *"Por qué Aurora cuesta lo que cuesta"* (educar sobre ingredientes premium vs. genéricos de Botica Verde)
- Semana 2: *"Aurora llegó a [Localidad] en 3 horas"* (prueba social + ventaja logística sobre Skin Lab)
- Semana 3: *"Solo quedan X unidades de Aurora"* (escasez real, no falsa)
- Semana 4: *"Así se ve tu piel después de 4 semanas con Aurora"* (resultados)

---

### 📅 PLAN SEMANA A SEMANA

**SEMANA 1: "Educación Premium" (Awareness)**
- **Contenido**: 5 Reels explicando cada paso del set Aurora (limpiador, sérum, crema) y por qué juntos cuestan menos que comprar 3 productos sueltos en Skin Lab. 1 post en Feed comparando Aurora vs. comprar productos separados en Botica Verde (tabla de costos y beneficios).
- **CTA**: "Comenta AURORA y te envío por DM la guía de uso exclusiva para pieles bogotanas".
- **Ads**: Campaña de tráfico (no venta) a tu perfil de Instagram, segmentada a seguidoras de Botica Verde/Skin Lab en Bogotá.
- **WhatsApp**: Activar respuesta automática para quienes escriban "AURORA": "Hola, gracias por tu interés en Aurora. ¿Vives en Bogotá? Te cuento los beneficios del envío express..."

**SEMANA 2: "Confianza y Prueba Social" (Consideration)**
- **Contenido**: 3 videos de clientas reales de Bogotá (si ya tienes, si no, graba 3 amigas tuyas) mostrando resultados de 15 días con Aurora. 1 Reel tuyo haciendo unboxing detallado de Aurora mostrando cada producto dentro. Stories con la **garantía de 30 días en Aurora** destacada.
- **Oferta**: "Esta semana: envío GRATIS mismo día en Bogotá si compras Aurora" (diferenciador clave vs. competidores que tardan 2-3 días).
- **Ads**: Campaña de mensajes (objetivo: conversaciones) a quienes vieron el 50% de los videos de Aurora en semana 1.
- **WhatsApp**: Enviar mensaje broadcast a tu lista existente: "Tengo 10 unidades de Aurora con envío gratis hoy en Bogotá. ¿Te interesa?"

**SEMANA 3: "Urgencia y Cierre" (Decision)**
- **Contenido**: Stories diarias con contador "Quedan X unidades de Aurora para envío gratis hoy". Reel mostrando pedidos de Aurora siendo empacados para salir en moto a Chapinero/Usaquén. Video "Aurora vs. tu rutina actual: 3 razones para cambiar".
- **Ads**: Retargeting a quienes agregaron Aurora al carrito pero no compraron, y a quienes visitaron tu perfil 3+ veces. Mensaje: "Aún tienes Aurora en tu carrito. Hoy envío gratis a [Localidad] si compras antes de las 6pm".
- **WhatsApp**: Mensajes 1 a 1 a leads de semanas 1-2 que no compraron: "Hola [Nombre], vi que te interesó Aurora. Tengo 2 unidades reservadas para ti hasta mañana con envío express en Bogotá. ¿Te las aparto?"

**SEMANA 4: "Última Llamada y Fidelización" (Cierre + Retención)**
- **Contenido**: Reel "Últimas 5 unidades de Aurora disponibles". Post con testimonios de quienes compraron Aurora en las semanas anteriores (fotos de ellas con Aurora). Contenido educativo para quienes YA compraron: "Cómo maximizar resultados con Aurora en tu rutina nocturna".
- **Ads**: Similar a semana 3 pero con urgencia máxima: "Último día para envío gratis de Aurora en Bogotá".
- **WhatsApp**: A quienes compraron Aurora: "¿Ya empezaste a usar Aurora? Cuéntame cómo te va y te regalo una muestra de Luna para tu próximo pedido". A quienes no compraron: "¿Aún quieres Aurora? Tengo 1 unidad disponible con descuento del 10% solo por hoy (no es guerra de precios, es última unidad)".

---

### 📊 MÉTRICAS DE ÉXITO ESPECÍFICAS PARA AURORA

| KPI | Meta en 4 semanas | Cómo medirlo |
|-----|-------------------|--------------|
| **Unidades de Aurora vendidas** | 40 unidades | Hoja de cálculo simple o Shopify/tienda online |
| **CAC de Aurora** | < 25% del precio de Aurora | (Gasto total en ads + tiempo valorado) / 40 ventas |
| **Tasa de conversión WhatsApp→Venta Aurora** | > 20% | De cada 10 personas que escriben "AURORA", 2 deben comprar en 48h |
| **Tasa de "bundle" (Aurora + otro producto)** | > 30% | % de pedidos que incluyen Aurora + Sol o Aurora + Luna |
| **Tasa de abandono de carrito Aurora** | < 60% | Si es mayor, revisar checkout o agregar más confianza (garantía visible) |
| **NPS específico de Aurora** | > 8/10 | Preguntar por WhatsApp 7 días después: "¿Del 0-10, recomendarías Aurora a una amiga en Bogotá?" |
| **Costo por lead calificado de Aurora** | < $15.000 COP | Cuánto gastas para conseguir un contacto que realmente pregunta por detalles de Aurora (no solo "hola") |
| **Guardados en contenido de Aurora** | > 5% de las vistas | En Instagram Insights, % de saves en Reels de Aurora (indica intención de compra futura) |

**Regla de decisión al final de la semana 2:** Si llevas menos de 10 ventas de Aurora pero tienes muchos leads en WhatsApp, **no gastes más en ads**, invierte ese dinero en mejorar la página de producto de Aurora (fotos, descripción de beneficios) o en ofrecer una llamada de 10 minutos por WhatsApp para cerrar la venta manualmente.

¿Tienes stock suficiente de Aurora para soportar 40 ventas en 4 semanas, o ajustamos la meta a lo que tengas disponible ahora?