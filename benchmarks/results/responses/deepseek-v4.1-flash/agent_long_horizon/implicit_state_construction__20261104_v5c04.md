# DeepSeek V4.1 Flash — agent_long_horizon/implicit_state_construction

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 7.54 | quality: 8.5
- latency_total: 117.612s | tokens_per_second: 117.5
- input_tokens: 15752 | output_tokens: 11205

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

Sí, Camila, me queda claro:

- **Tienda online en Colombia**
- **Productos:**
  - **Aurora**: set de cuidado facial, precio **premium**
  - **Sol**: kit de maquillaje natural, precio **medio**
  - **Luna**: crema corporal, precio **entrada**
- **Mercado único actual:** **Bogotá**
- **Competidores principales:** **Botica Verde** y **Skin Lab**, ambos en Bogotá

Lo tendré presente para las siguientes recomendaciones y para resolver referencias implícitas sin volver a preguntarte estos datos.

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Ofrezco una selección curada de cuidado facial, maquillaje natural y bienestar corporal para personas en Bogotá, con productos en tres niveles de precio —entrada, medio y premium— para que cada clienta encuentre la opción ideal según su necesidad y presupuesto. A diferencia de Botica Verde y Skin Lab, mi propuesta combina la comodidad de comprar online con una oferta clara y accesible que cubre desde el autocuidado diario hasta experiencias premium.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Camila, para tu caso —tienda online, solo Bogotá, belleza/cuidado personal y tres niveles de precio— priorizaría así:

### 1. Instagram + WhatsApp Business (núcleo)
- **Instagram** es el canal principal para descubrir y desear tus productos: Reels con rutinas, antes/después, texturas, testimonios y contenido educativo que te diferencie de **Botica Verde** y **Skin Lab**.
- **WhatsApp Business** es clave en Colombia para convertir: catálogo, respuestas rápidas, asesoría de rutina, cierre de pedidos, recuperación de carritos y postventa. Úsalo como puente entre el contenido y la compra.

### 2. Meta Ads geolocalizado en Bogotá
- Anuncios en **Instagram y Facebook** con segmentación exclusiva en **Bogotá**.
- Empieza con **retargeting** a quienes visitaron la tienda o interactuaron, y luego amplía a públicos similares.
- Separa mensajes: **Aurora** (premium, beneficio/experiencia), **Sol** (maquillaje natural, practicidad) y **Luna** (entrada, prueba/impulso).

### 3. TikTok orgánico + microinfluencers locales
- Úsalo para **descubrimiento**, sobre todo para **Sol** y **Luna**.
- Microinfluencers de belleza en Bogotá pueden dar credibilidad local sin el costo de grandes creadores.
- No necesitas publicar a diario: prioriza videos con textura, rutina, “lo que uso”, empaque y compra online.

### 4. Google Search + Shopping (cuando tengas catálogo y feed listos)
- Captura intención alta: búsquedas como “crema corporal Bogotá”, “maquillaje natural Colombia”, “set facial premium”.
- Es más efectivo cuando ya tienes fotos, descripciones y precios bien estructurados. Puede ser tu siguiente inversión después de Meta.

### 5. Email/CRM para retención
- No es el primer canal de adquisición, pero sí el más rentable a mediano plazo.
- Úsalo para recompra de **Luna**, educación sobre **Aurora** y cross-sell de **Sol**.

**Si tuvieras que empezar con solo tres:** Instagram orgánico + WhatsApp Business + Meta Ads geolocalizado en Bogotá. Luego sumaría TikTok orgánico y, por último, Google Shopping/Search. Evitaría por ahora canales como LinkedIn o X, que no encajan con tu categoría ni con tu mercado inicial.

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Camila, te propongo una frecuencia **realista y sostenible** para una emprendedora que también atiende pedidos y WhatsApp. La clave es la constancia, no la cantidad.

| Canal | Frecuencia recomendada | Qué publicar |
|---|---|---|
| **Instagram (orgánico)** | **3–4 publicaciones/Reels por semana** + **historias 3–5 días/semana** | Reels de rutina, texturas, testimonios, educación y detrás de cámaras. Alterna **Luna** (frecuente), **Sol** (demos/practicidad) y **Aurora** (menos frecuente, más cuidada). |
| **TikTok** | **3–5 videos por semana** | Contenido de descubrimiento: texturas, “cómo lo uso”, empaque, compra online, microinfluencers locales. Prioriza **Sol** y **Luna**. |
| **WhatsApp Business** | **Estados 3–5 veces/semana** + **mensajes/broadcast 2–4 veces al mes** | Estados con novedades, tips, testimonios y recordatorios suaves. Broadcast solo con valor: lanzamientos, reposiciones, promos segmentadas. |
| **Email/CRM** | **2–4 envíos al mes** | Educación de **Aurora**, recompra de **Luna**, cross-sell de **Sol** y contenido de rutina. |
| **Facebook orgánico** | **Baja prioridad**: 1–2 publicaciones/semana o solo replicar Instagram | Úsalo principalmente como apoyo a Meta Ads, no como canal principal. |
| **Google** | **No aplica contenido orgánico frecuente** | Optimiza fichas de producto, descripciones y reseñas; eso es SEO, no calendario editorial. |

### Cómo lo haría en la práctica
- **Semana tipo mínima:** 3 Reels de Instagram, 3 TikToks, historias 4 días y 1 estado de WhatsApp casi diario.
- **Reutiliza:** un mismo video puede servir para Reels y TikTok; una historia puede alimentar un broadcast o un email.
- **No satures:** si una semana no llegas a todo, prioriza **Instagram + WhatsApp**, que son tu núcleo de conversión.
- **Prueba 4 semanas** con esta cadencia y ajusta según guardados, respuestas, clics a la tienda y pedidos por WhatsApp.

**Regla simple:** publica menos pero con intención. Es mejor **3 contenidos buenos por semana** que 7 genéricos.

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Camila, para **skincare** funciona especialmente el contenido que **enseña, muestra y genera confianza**. La venta directa sirve, pero si es solo “compra ya” cansa. Te ordeno los tipos que mejor rinden, aplicados a tu caso:

### 1. Textura y experiencia sensorial
- Videos cortos mostrando la textura del producto: cómo se extiende, cómo se absorbe, brillo, empaque, gotero, crema.
- Funciona muy bien para **Luna** (crema corporal) y para mostrar la experiencia premium de **Aurora**.
- Formato: Reel/TikTok de 7–15 segundos, primer plano, luz natural, sonido suave o ASMR.

### 2. Rutina paso a paso
- “Mi rutina de noche con Aurora”, “rutina express de 3 pasos”, “cómo combino Sol y Aurora”.
- Ayuda a que la clienta entienda **cómo usar** el producto y por qué vale el precio.
- Ideal para **Aurora**, que al ser premium necesita más educación y contexto.

### 3. Educación y resolución de dudas
- “Cómo elegir un set facial según tu tipo de piel”, “qué diferencia hay entre precio entrada, medio y premium”, “mitos sobre skincare”.
- Posiciona tu marca frente a **Botica Verde** y **Skin Lab** sin atacar directamente.
- Formato: carrusel en Instagram, Reel hablado o video de TikTok con texto en pantalla.

### 4. Antes y después realistas
- Muy potente, pero con cuidado: muestra **cambios de apariencia** (hidratación, luminosidad, suavidad), no prometas curas.
- Usa tiempos realistas: “después de 2 semanas de uso constante”.
- Mejor si son testimonios reales de clientas en Bogotá.

### 5. Testimonios y UGC
- Reseñas en video, capturas de WhatsApp, clientas mostrando el producto.
- Para skincare, la prueba social pesa mucho: “lo probé y esto sentí”.
- Puedes pedir a compradoras de **Luna** que graben una historia corta; es más fácil que con **Aurora**.

### 6. Ingredientes y “por qué lo formulamos así”
- Explica ingredientes clave en lenguaje simple, sin tecnicismos excesivos.
- Para **Aurora** funciona muy bien: justifica el precio premium con formulación, textura, empaque y experiencia.
- Evita promesas médicas o exageradas; habla de hidratación, suavidad, sensación y apariencia.

### 7. Detrás de cámaras y founder content
- Tú mostrando cómo empacas, eligiendo productos, respondiendo dudas, contando por qué creaste la tienda.
- En marcas pequeñas, la fundadora genera confianza local. En Bogotá, además, refuerza la cercanía y la entrega.

### 8. Contenido de compra y logística
- “Cómo comprar online”, “qué pasa después de tu pedido”, “envíos en Bogotá”, “cómo elegir tu regalo”.
- No es el más glamuroso, pero **reduce fricción** y responde objeciones típicas.

### 9. Comparativas útiles, no agresivas
- “Luna vs. Aurora: cuál elegir según lo que buscas”, “Sol para el día, Aurora para la noche”.
- Ayuda a vender los tres niveles de precio sin canibalizarlos.

### 10. Contenido de temporada/local
- Clima de Bogotá, rutina para días fríos, regalos, fechas especiales.
- Te da cercanía y diferenciación local frente a marcas genéricas.

### Prioridad práctica para tu calendario
Si tuvieras que elegir **5 formatos base**:
1. **Textura/ASMR** (Luna y Aurora)
2. **Rutina paso a paso** (Aurora)
3. **Educación/mitos** (marca)
4. **Testimonios reales** (los tres productos)
5. **Detrás de cámaras/fundadora** (confianza)

**Regla clave:** en skincare gana el contenido que **muestra el producto en uso + explica + da prueba social**. Combina los tres y evita publicar solo fotos de producto bonitas sin contexto.

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Camila, la forma de diferenciarte sin guerra de precios es **competir en claridad, experiencia y confianza**, no en descuentos. Tus competidores están en Bogotá y venden belleza, así que tu ventaja no debería ser “somos más baratas”, sino **“somos más fáciles de elegir y de comprar”**.

### 1. Posiciónate como “curaduría por niveles”, no como catálogo
Tienes algo que puedes explotar muy bien: **tres niveles de precio con propósito claro**.

- **Luna** = entrada / autocuidado diario / primera compra.
- **Sol** = maquillaje natural / practicidad / rutina rápida.
- **Aurora** = premium / experiencia / ritual completo.

Comunica: *“No vendemos productos sueltos: te ayudamos a elegir según tu momento, tu rutina y tu presupuesto”*. Eso te diferencia de competidores que quizá compiten producto por producto.

### 2. Vende asesoría, no solo producto
En belleza, la duda frena la compra. Usa **WhatsApp Business** para ofrecer una **asesoría breve de rutina**:

- “Cuéntame tu tipo de piel y qué buscas”.
- Recomienda **Luna** si es primera compra o autocuidado.
- Recomienda **Sol** si busca practicidad.
- Recomienda **Aurora** si busca experiencia premium.

Esa atención personalizada es difícil de igualar y justifica pagar tu precio sin descuentos.

### 3. Protege el premium con experiencia, no con rebajas
**Aurora** no debería entrar en promociones frecuentes. Su diferencial debe ser:

- Empaque cuidado.
- Contenido educativo sobre cómo usarlo.
- Ritual de uso.
- Atención postcompra.
- Posibilidad de regalo o experiencia especial.

Si bajas el precio de Aurora constantemente, le enseñas a tu clienta que espere descuento y pierdes el posicionamiento premium.

### 4. Usa bundles y valor agregado en lugar de descuentos
En vez de “20% off”, ofrece:

- **Kit Luna + Sol** para rutina diaria.
- **Rutina Aurora completa** con guía de uso.
- **Muestra o detalle** en la primera compra.
- **Envío local ágil en Bogotá** o entrega coordinada.
- **Empaque para regalo** en fechas especiales.

Así compites en **valor percibido**, no en precio.

### 5. Sé muy local y muy humana
Tus competidores también están en Bogotá, pero tú puedes ganar en cercanía:

- Contenido con referencias locales: clima, rutina para Bogotá, entregas en la ciudad.
- Mostrar a la fundadora: tú empacando, respondiendo dudas, eligiendo productos.
- Testimonios de clientas bogotanas.
- Lenguaje cercano y servicio rápido por WhatsApp.

Una marca pequeña puede ser **más humana y más ágil** que una competidora más grande.

### 6. Educación como marca: “te enseñamos a elegir”
Publica contenido que resuelva decisiones:

- “¿Luna o Aurora? Depende de esto”.
- “Cómo armar una rutina con tres pasos”.
- “Qué esperar de un set facial premium”.
- “Maquillaje natural para todos los días”.

Si te conviertes en la marca que **explica bien**, la clienta te compra a ti aunque Botica Verde o Skin Lab tengan algo parecido.

### 7. Fideliza en lugar de perseguir precios
Como tienes un producto de entrada, usa **Luna** para captar y luego llevar a **Sol** o **Aurora**:

- Seguimiento postcompra por WhatsApp.
- Recomendación de recompra.
- Beneficio por compra recurrente.
- Contenido exclusivo para clientas.

Es más rentable retener que igualar promociones.

### 8. Ten una promesa diferencial clara
Puede ser algo como:

> “En [tu marca] te ayudamos a elegir tu rutina de belleza según tu necesidad y presupuesto, con atención personalizada y entrega en Bogotá.”

O:

> “Tres niveles, una misma promesa: productos seleccionados, asesoría cercana y compra online fácil en Bogotá.”

### Lo que evitaría
- Igualar cada descuento de Botica Verde o Skin Lab.
- Poner Aurora en promoción permanente.
- Competir diciendo “somos más baratas”.
- Copiar su contenido sin adaptarlo a tu voz.
- Vender los tres productos con el mismo mensaje.

**En una frase:** diferénciate siendo **la marca que ayuda a elegir y acompaña la compra**, con una arquitectura clara de entrada, medio y premium, atención cercana por WhatsApp y una experiencia premium que no se negocia por precio.

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Camila, en tu **primer trimestre** el objetivo no es solo vender: es **aprender qué canal, mensaje y producto funcionan** con tu público de Bogotá. Mediría pocos KPIs, bien definidos y segmentados. Te propongo este marco:

## 1. KPI norte
**Ventas netas por trimestre** y **número de pedidos**, separando **Bogotá** y por producto:
- **Luna** (entrada): captación y primera compra.
- **Sol** (medio): ticket y cross-sell.
- **Aurora** (premium): margen y valor por pedido.

No usaría seguidores como KPI principal.

## 2. KPIs comerciales base
| KPI | Fórmula / cómo medirlo | Para qué |
|---|---|---|
| **Pedidos** | N.º de órdenes pagadas | Volumen real |
| **Ticket promedio / AOV** | Ventas netas ÷ pedidos | Ver si bundles y Sol/Aurora suben el ticket |
| **Tasa de conversión web** | Pedidos ÷ sesiones | Eficacia de la tienda |
| **Tasa de conversión por WhatsApp** | Pedidos cerrados ÷ conversaciones iniciadas | Tu canal clave de cierre |
| **Margen bruto por producto** | (Precio − costo variable) ÷ precio | Evitar crecer sin rentabilidad |
| **Ventas por producto y mix** | % de ventas de Luna, Sol y Aurora | Saber qué producto jala y cuál no |

**Meta práctica:** en el mes 1 establece línea base; en meses 2 y 3 busca mejorar conversión y AOV, no solo tráfico.

## 3. Adquisición y canales
| KPI | Qué revisar |
|---|---|
| **CAC** | Costo de adquisición por pedido, idealmente **por producto** |
| **ROAS** | Retorno de Meta Ads, separado por campaña y producto |
| **CTR y CPC** | Qué creatividades atraen clics de calidad en Bogotá |
| **Alcance y frecuencia** | Evitar saturar; frecuencia alta sin conversión = alerta |
| **Clics a la tienda desde Instagram/TikTok** | No solo likes: intención real |
| **Conversiones asistidas por WhatsApp** | Pedidos donde WhatsApp intervino |

**Regla:** compara **CAC contra margen bruto**. Si el CAC se come el margen de Luna, ese producto necesita recompra o cross-sell para ser rentable.

## 4. Producto y pricing
- **Unidades vendidas por producto**: Luna, Sol, Aurora.
- **% de pedidos con más de un producto** (cross-sell).
- **AOV de pedidos con Aurora** vs. sin Aurora.
- **Descuento promedio aplicado**: si sube mucho, estás entrando en guerra de precios.
- **Tasa de devoluciones o cancelaciones**.
- **Participación de bundles** si lanzas combos.

## 5. Retención y recompra
En el primer trimestre ya puedes medir señales tempranas:
- **Tasa de recompra a 30/60/90 días**, sobre todo de **Luna**.
- **Tiempo hasta la segunda compra**.
- **Migración Luna → Sol/Aurora**.
- **Clientas recurrentes vs. nuevas**.
- **Base de email/WhatsApp**: contactos captados y crecimiento mensual.

No necesitas LTV perfecto todavía; sí saber si **Luna está generando recompra o solo pedidos aislados**.

## 6. Contenido orgánico
Mediría calidad, no vanidad:
- **Guardados y compartidos** por publicación.
- **Retención de video** (primeros 3 segundos y duración vista).
- **Respuestas y mensajes directos** generados.
- **Clics al enlace de la tienda**.
- **Contenidos que más conversaciones por WhatsApp generan**.

El KPI útil es: **¿qué contenido genera conversaciones y clics?**, no solo alcance.

## 7. Operación y experiencia
- **Tiempo de primera respuesta en WhatsApp**.
- **Tasa de carritos abandonados** y recuperación.
- **Entregas a tiempo en Bogotá**.
- **Quejas o reclamos por pedido**.
- **Reseñas/testimonios recolectados**.

## 8. Cadencia de revisión
- **Semanal:** pedidos, conversión web, conversión WhatsApp, CTR/ROAS, carritos abandonados.
- **Mensual:** CAC, margen por producto, mix de ventas, recompra, contenido top.
- **Al cierre del trimestre:** decides si escalas Meta Ads, si TikTok merece más inversión y si Aurora necesita más educación o menos promoción.

## Si solo pudieras medir 8 KPIs, serían:
1. **Ventas netas y pedidos**.
2. **Ticket promedio (AOV)**.
3. **Tasa de conversión web**.
4. **Tasa de conversión por WhatsApp**.
5. **CAC y ROAS por campaña**.
6. **Margen bruto por producto**.
7. **Mix de ventas Luna/Sol/Aurora y cross-sell**.
8. **Recompra temprana de Luna**.

**Consejo:** no pongas metas agresivas de ROAS desde la semana 1. Usa el primer mes para **establecer línea base**, el segundo para **optimizar creatividades y WhatsApp**, y el tercero para **escalar solo lo que ya demuestra conversión y margen**.

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

# Campaña 4 semanas — **Aurora** (set de cuidado facial premium)

**Mercado:** Bogotá · **Canal de venta:** tienda online + WhatsApp Business · **Competidores de referencia:** Botica Verde y Skin Lab

> **Regla de oro de esta campaña:** **Aurora** no se promociona con descuento. Se vende con **educación, experiencia y asesoría**. El precio premium se justifica, no se rebaja.

---

## 1. Objetivo

**Objetivo principal:** generar **las primeras ventas sostenidas de Aurora** en Bogotá y construir la base de datos de compradoras e interesadas en el producto, midiendo CAC y margen real.

**Objetivos secundarios:**
- Posicionar **Aurora** como el set facial premium de referencia frente a Botica Verde y Skin Lab.
- Captar **conversaciones calificadas por WhatsApp** sobre Aurora (asesoría de rutina).
- Elevar el **ticket promedio** de la tienda mediante un producto de mayor valor.
- Recoger **testimonios y UGC de Aurora** para el trimestre siguiente.

**Lo que esta campaña NO busca:** volumen masivo, ventas por impulso ni competir por precio.

---

## 2. Audiencia

Trabajaría **4 segmentos**, en este orden de prioridad:

| # | Segmento | Quién es | Mensaje que le habla |
|---|---|---|---|
| **1** | **Base propia (Luna y Sol)** | Clientas que ya te compraron y confían en tu tienda | “El siguiente paso de tu rutina es **Aurora**” |
| **2** | **Retargeting** | Quienes visitaron la página de Aurora, guardaron contenido o escribieron por WhatsApp y no compraron | “Resuelve tus dudas sobre **Aurora** antes de decidir” |
| **3** | **Público frío en Bogotá** | Mujeres 25–45, Bogotá, interés en skincare, cuidado facial, rutinas, marcas premium y belleza natural | “**Aurora**: un ritual facial completo, con asesoría real” |
| **4** | **Microinfluencers locales** | Creadoras de belleza/skincare en Bogotá, 5k–30k seguidores | “Probad **Aurora** y contad la experiencia” |

**Segmentación clave:** solo **Bogotá**. No abras a otras ciudades en esta campaña; el foco local es parte de tu diferencial.

**Público lookalike:** actívalo en la semana 3, usando como semilla a las compradoras de **Aurora** (o, si aún son pocas, a las compradoras de **Sol** y **Luna**).

---

## 3. Canales y rol de cada uno

| Canal | Rol en la campaña de **Aurora** |
|---|---|
| **Instagram (Reels + carruseles + historias)** | Canal principal de **deseo y educación**. Aquí se explica qué es Aurora, cómo se usa y por qué vale lo que vale. |
| **WhatsApp Business** | Canal principal de **conversión**. Asesoría 1:1, envío de la guía de uso, resolución de objeciones y cierre. |
| **Meta Ads (Instagram + Facebook)** | **Amplificar** el contenido de Aurora a Bogotá y hacer **retargeting** a quien ya mostró interés. |
| **TikTok orgánico** | Descubrimiento secundario. Texturas, ritual de uso, “cómo se ve Aurora”. |
| **Email** | Educación profunda sobre **Aurora** y activación de la base propia. |
| **Google Shopping/Search** | Opcional en la semana 4, solo si el catálogo de Aurora ya está bien descrito. |

**Prioridad absoluta:** Instagram + WhatsApp + Meta Ads. Si el tiempo aprieta, sostén esos tres y sacrifica el resto.

---

## 4. Mensaje principal

> ### **“Aurora: tu ritual facial completo, con la asesoría que necesitas para usarlo bien.”**

**Promesa de campaña:** *Aurora no es un producto más en el catálogo: es el set facial premium de tu rutina, acompañado de asesoría personalizada y entrega en Bogotá.*

### Variantes por ángulo (no todas a la vez)
- **Ángulo educación:** “Cómo armar tu ritual facial completo con **Aurora**, paso a paso.”
- **Ángulo experiencia:** “La textura, el empaque y el ritual de **Aurora**.”
- **Ángulo asesoría:** “Te ayudamos a saber si **Aurora** es para tu piel.”
- **Ángulo upgrade:** “Si ya usas Luna, el siguiente paso es **Aurora**.”
- **Ángulo diferenciación:** “Sin promesas exageradas: **Aurora**, explicado bien.”

### Lo que nunca diría de Aurora
- “El más barato”, “últimas unidades con descuento”, “50% off”.
- Promesas médicas o de resultados garantizados.
- Comparaciones directas y agresivas con Botica Verde o Skin Lab.

---

## 5. Plan semana a semana

### **Semana 1 — Fundamentos y lanzamiento**
**Objetivo:** instalar a **Aurora** en el imaginario de tu audiencia y establecer la línea base.

- **Instagram:** 3 Reels + 1 carrusel educativo + historias 5 días.
  - Reel 1: textura y empaque de **Aurora**.
  - Reel 2: “Qué es **Aurora** y para quién es”.
  - Carrusel: “Cómo usar **Aurora** en 3 pasos”.
- **WhatsApp:** estado diario presentando **Aurora**; mensaje broadcast a la base de Luna y Sol: *“Llegó Aurora, el siguiente paso de tu rutina”*.
- **Meta Ads:** activar **retargeting** y un conjunto frío en Bogotá con el Reel de textura y el carrusel educativo.
- **Email:** 1 envío a la base presentando **Aurora** y su ritual de uso.
- **TikTok:** 3 videos de textura y ritual con **Aurora**.
- **Operación:** preparar la **guía de uso de Aurora** en PDF y la respuesta estándar de WhatsApp para objeciones de precio.

**Entregable de la semana:** línea base documentada (CTR, CPC, conversaciones, visitas a la página de Aurora).

---

### **Semana 2 — Prueba social y consideración**
**Objetivo:** reducir la objeción de precio con **evidencia y experiencia**, no con rebajas.

- **Instagram:** 3 Reels + historias diarias.
  - Reel: testimonio real de alguien que ya usa **Aurora** (aunque sea una sola persona).
  - Reel: “Antes de comprar **Aurora**, esto deberías saber”.
  - Carrusel: “Por qué **Aurora** es premium” (formulación, textura, empaque, ritual).
- **Microinfluencers de Bogotá:** enviar **Aurora** a 2–3 creadoras y pedir contenido honesto, no guionizado.
- **WhatsApp:** activar **asesoría 1:1 de Aurora**: “Cuéntame tu tipo de piel y te digo si Aurora encaja”. Enviar la guía de uso a quien la pida.
- **Meta Ads:** sumar creatividades de testimonio y de “por qué es premium”. Mantener retargeting.
- **Email:** envío educativo profundo sobre el ritual de **Aurora**.

**Entregable de la semana:** primeras 10–15 conversaciones calificadas de Aurora por WhatsApp y al menos 1 contenido UGC.

---

### **Semana 3 — Conversión y valor agregado**
**Objetivo:** cerrar ventas de **Aurora** agregando valor, nunca bajando el precio.

- **Instagram:** 3 Reels + historias con cuenta regresiva a un **beneficio de valor**:
  - **Empaque de regalo** sin costo en compras de **Aurora** esta semana.
  - **Asesoría de rutina 1:1 ampliada** para compradoras de **Aurora**.
  - **Detalle de bienvenida** en la primera compra de Aurora.
- **WhatsApp:** recuperación activa de quienes preguntaron por **Aurora** y no compraron. Mensaje de seguimiento personalizado.
- **Meta Ads:** activar el **lookalike** de compradoras y subir presupuesto solo en el conjunto que esté convirtiendo.
- **TikTok:** video de “cómo se ve Aurora en la rutina real”.
- **Email:** recordatorio del beneficio de valor en **Aurora**, con la guía de uso como gancho.

**Entregable de la semana:** pico de ventas de **Aurora** y validación del beneficio de valor que mejor funciona.

---

### **Semana 4 — Cierre, recompra y aprendizaje**
**Objetivo:** cerrar el ciclo, convertir interesadas rezagadas y definir qué escalar.

- **Instagram:** Reel de cierre con testimonios de **Aurora** y un “todo lo que aprendimos de Aurora este mes”.
- **WhatsApp:** último seguimiento a conversaciones abiertas de **Aurora**; encuesta breve a compradoras: *“¿Cómo te fue con Aurora?”* → base para testimonios.
- **Meta Ads:** mantener solo las campañas con CAC dentro de margen; pausar el resto.
- **Email:** cierre de campaña de **Aurora** + invitación a dejar reseña.
- **Google:** si está listo, activar Shopping solo para **Aurora** y evaluar.
- **Análisis:** comparar las 4 semanas y decidir si **Aurora** necesita más educación, más prueba social o mejor precio percibido (nunca descuento).

**Entregable de la semana:** informe de campaña con CAC, ROAS, margen y aprendizajes sobre **Aurora**.

---

## 6. Métricas de éxito

### Métricas del norte
| Métrica | Meta para las 4 semanas |
|---|---|
| **Unidades vendidas de Aurora** | Definir meta realista con tu línea base; apuntar a crecimiento semanal sostenido |
| **% de pedidos totales que incluyen Aurora** | 15–25% del total |
| **Margen bruto de Aurora** | Mantenerlo sin erosión por descuentos |
| **CAC de Aurora vs. margen bruto** | CAC **por debajo** del margen bruto de Aurora |

### Métricas de adquisición
| Métrica | Meta orientativa |
|---|---|
| **CTR en Meta Ads (Aurora)** | ≥ 1,5% en frío; ≥ 2,5% en retargeting |
| **ROAS de retargeting** | ≥ 3x |
| **ROAS de frío** | ≥ 1,5x (escalable si supera esto) |
| **Visitas a la página de Aurora** | Crecimiento semanal constante |

### Métricas de WhatsApp (tu canal de cierre)
| Métrica | Meta orientativa |
|---|---|
| **Conversaciones iniciadas sobre Aurora** | 30–50 en el mes |
| **Tasa de cierre de conversaciones de Aurora** | ≥ 15% |
| **Tiempo de primera respuesta** | < 15 minutos en horario comercial |

### Métricas de contenido
- **Guardados y compartidos** en publicaciones de **Aurora** (indicador de intención premium).
- **Retención de video** en Reels de Aurora (primeros 3 segundos).
- **Respuestas en historias** mencionando Aurora.

### Métricas de retención y base
- **Compradoras nuevas de Aurora** captadas.
- **Testimonios de Aurora** recolectados (meta: 5).
- **Migración Luna/Sol → Aurora** (cuántas clientas previas subieron de nivel).
- **Crecimiento de la base de WhatsApp y email** segmentada por interés en Aurora.

### Criterios de decisión al cierre
- **Escalar Aurora** si el CAC está por debajo del margen y el ROAS de retargeting ≥ 3x.
- **Reformular el mensaje de Aurora** si hay mucho clic pero poca conversación.
- **Reformular la asesoría** si hay conversaciones pero no cierre.
- **No tocar el precio de Aurora** en ningún escenario de esta campaña.

---

## 7. Riesgos y cómo los manejo

| Riesgo | Acción preventiva |
|---|---|
| **Aurora se percibe cara sin contexto** | Contenido educativo y asesoría 1:1 desde la semana 1 |
| **Tentación de descontar Aurora** | Sustituir cualquier descuento por **valor agregado** (empaque, guía, asesoría) |
| **Pocos testimonios al inicio** | Usar microinfluencers y primeras compradoras; pedir reseña desde la semana 1 |
| **Dispersión de canales** | Si falta tiempo, recortar TikTok y Google; sostener Instagram + WhatsApp + Meta Ads |
| **Público frío demasiado amplio** | Mantener segmentación estricta en Bogotá y creatividades específicas de Aurora |

---

**En una frase:** durante 4 semanas, **Aurora** se vende explicando, acompañando y demostrando experiencia —con Instagram y WhatsApp como núcleo, Meta Ads como amplificador y **cero descuentos sobre Aurora**.


## Respuesta completa

# Campaña 4 semanas — **Aurora** (set de cuidado facial premium)

**Mercado:** Bogotá · **Canal de venta:** tienda online + WhatsApp Business · **Competidores de referencia:** Botica Verde y Skin Lab

> **Regla de oro de esta campaña:** **Aurora** no se promociona con descuento. Se vende con **educación, experiencia y asesoría**. El precio premium se justifica, no se rebaja.

---

## 1. Objetivo

**Objetivo principal:** generar **las primeras ventas sostenidas de Aurora** en Bogotá y construir la base de datos de compradoras e interesadas en el producto, midiendo CAC y margen real.

**Objetivos secundarios:**
- Posicionar **Aurora** como el set facial premium de referencia frente a Botica Verde y Skin Lab.
- Captar **conversaciones calificadas por WhatsApp** sobre Aurora (asesoría de rutina).
- Elevar el **ticket promedio** de la tienda mediante un producto de mayor valor.
- Recoger **testimonios y UGC de Aurora** para el trimestre siguiente.

**Lo que esta campaña NO busca:** volumen masivo, ventas por impulso ni competir por precio.

---

## 2. Audiencia

Trabajaría **4 segmentos**, en este orden de prioridad:

| # | Segmento | Quién es | Mensaje que le habla |
|---|---|---|---|
| **1** | **Base propia (Luna y Sol)** | Clientas que ya te compraron y confían en tu tienda | “El siguiente paso de tu rutina es **Aurora**” |
| **2** | **Retargeting** | Quienes visitaron la página de Aurora, guardaron contenido o escribieron por WhatsApp y no compraron | “Resuelve tus dudas sobre **Aurora** antes de decidir” |
| **3** | **Público frío en Bogotá** | Mujeres 25–45, Bogotá, interés en skincare, cuidado facial, rutinas, marcas premium y belleza natural | “**Aurora**: un ritual facial completo, con asesoría real” |
| **4** | **Microinfluencers locales** | Creadoras de belleza/skincare en Bogotá, 5k–30k seguidores | “Probad **Aurora** y contad la experiencia” |

**Segmentación clave:** solo **Bogotá**. No abras a otras ciudades en esta campaña; el foco local es parte de tu diferencial.

**Público lookalike:** actívalo en la semana 3, usando como semilla a las compradoras de **Aurora** (o, si aún son pocas, a las compradoras de **Sol** y **Luna**).

---

## 3. Canales y rol de cada uno

| Canal | Rol en la campaña de **Aurora** |
|---|---|
| **Instagram (Reels + carruseles + historias)** | Canal principal de **deseo y educación**. Aquí se explica qué es Aurora, cómo se usa y por qué vale lo que vale. |
| **WhatsApp Business** | Canal principal de **conversión**. Asesoría 1:1, envío de la guía de uso, resolución de objeciones y cierre. |
| **Meta Ads (Instagram + Facebook)** | **Amplificar** el contenido de Aurora a Bogotá y hacer **retargeting** a quien ya mostró interés. |
| **TikTok orgánico** | Descubrimiento secundario. Texturas, ritual de uso, “cómo se ve Aurora”. |
| **Email** | Educación profunda sobre **Aurora** y activación de la base propia. |
| **Google Shopping/Search** | Opcional en la semana 4, solo si el catálogo de Aurora ya está bien descrito. |

**Prioridad absoluta:** Instagram + WhatsApp + Meta Ads. Si el tiempo aprieta, sostén esos tres y sacrifica el resto.

---

## 4. Mensaje principal

> ### **“Aurora: tu ritual facial completo, con la asesoría que necesitas para usarlo bien.”**

**Promesa de campaña:** *Aurora no es un producto más en el catálogo: es el set facial premium de tu rutina, acompañado de asesoría personalizada y entrega en Bogotá.*

### Variantes por ángulo (no todas a la vez)
- **Ángulo educación:** “Cómo armar tu ritual facial completo con **Aurora**, paso a paso.”
- **Ángulo experiencia:** “La textura, el empaque y el ritual de **Aurora**.”
- **Ángulo asesoría:** “Te ayudamos a saber si **Aurora** es para tu piel.”
- **Ángulo upgrade:** “Si ya usas Luna, el siguiente paso es **Aurora**.”
- **Ángulo diferenciación:** “Sin promesas exageradas: **Aurora**, explicado bien.”

### Lo que nunca diría de Aurora
- “El más barato”, “últimas unidades con descuento”, “50% off”.
- Promesas médicas o de resultados garantizados.
- Comparaciones directas y agresivas con Botica Verde o Skin Lab.

---

## 5. Plan semana a semana

### **Semana 1 — Fundamentos y lanzamiento**
**Objetivo:** instalar a **Aurora** en el imaginario de tu audiencia y establecer la línea base.

- **Instagram:** 3 Reels + 1 carrusel educativo + historias 5 días.
  - Reel 1: textura y empaque de **Aurora**.
  - Reel 2: “Qué es **Aurora** y para quién es”.
  - Carrusel: “Cómo usar **Aurora** en 3 pasos”.
- **WhatsApp:** estado diario presentando **Aurora**; mensaje broadcast a la base de Luna y Sol: *“Llegó Aurora, el siguiente paso de tu rutina”*.
- **Meta Ads:** activar **retargeting** y un conjunto frío en Bogotá con el Reel de textura y el carrusel educativo.
- **Email:** 1 envío a la base presentando **Aurora** y su ritual de uso.
- **TikTok:** 3 videos de textura y ritual con **Aurora**.
- **Operación:** preparar la **guía de uso de Aurora** en PDF y la respuesta estándar de WhatsApp para objeciones de precio.

**Entregable de la semana:** línea base documentada (CTR, CPC, conversaciones, visitas a la página de Aurora).

---

### **Semana 2 — Prueba social y consideración**
**Objetivo:** reducir la objeción de precio con **evidencia y experiencia**, no con rebajas.

- **Instagram:** 3 Reels + historias diarias.
  - Reel: testimonio real de alguien que ya usa **Aurora** (aunque sea una sola persona).
  - Reel: “Antes de comprar **Aurora**, esto deberías saber”.
  - Carrusel: “Por qué **Aurora** es premium” (formulación, textura, empaque, ritual).
- **Microinfluencers de Bogotá:** enviar **Aurora** a 2–3 creadoras y pedir contenido honesto, no guionizado.
- **WhatsApp:** activar **asesoría 1:1 de Aurora**: “Cuéntame tu tipo de piel y te digo si Aurora encaja”. Enviar la guía de uso a quien la pida.
- **Meta Ads:** sumar creatividades de testimonio y de “por qué es premium”. Mantener retargeting.
- **Email:** envío educativo profundo sobre el ritual de **Aurora**.

**Entregable de la semana:** primeras 10–15 conversaciones calificadas de Aurora por WhatsApp y al menos 1 contenido UGC.

---

### **Semana 3 — Conversión y valor agregado**
**Objetivo:** cerrar ventas de **Aurora** agregando valor, nunca bajando el precio.

- **Instagram:** 3 Reels + historias con cuenta regresiva a un **beneficio de valor**:
  - **Empaque de regalo** sin costo en compras de **Aurora** esta semana.
  - **Asesoría de rutina 1:1 ampliada** para compradoras de **Aurora**.
  - **Detalle de bienvenida** en la primera compra de Aurora.
- **WhatsApp:** recuperación activa de quienes preguntaron por **Aurora** y no compraron. Mensaje de seguimiento personalizado.
- **Meta Ads:** activar el **lookalike** de compradoras y subir presupuesto solo en el conjunto que esté convirtiendo.
- **TikTok:** video de “cómo se ve Aurora en la rutina real”.
- **Email:** recordatorio del beneficio de valor en **Aurora**, con la guía de uso como gancho.

**Entregable de la semana:** pico de ventas de **Aurora** y validación del beneficio de valor que mejor funciona.

---

### **Semana 4 — Cierre, recompra y aprendizaje**
**Objetivo:** cerrar el ciclo, convertir interesadas rezagadas y definir qué escalar.

- **Instagram:** Reel de cierre con testimonios de **Aurora** y un “todo lo que aprendimos de Aurora este mes”.
- **WhatsApp:** último seguimiento a conversaciones abiertas de **Aurora**; encuesta breve a compradoras: *“¿Cómo te fue con Aurora?”* → base para testimonios.
- **Meta Ads:** mantener solo las campañas con CAC dentro de margen; pausar el resto.
- **Email:** cierre de campaña de **Aurora** + invitación a dejar reseña.
- **Google:** si está listo, activar Shopping solo para **Aurora** y evaluar.
- **Análisis:** comparar las 4 semanas y decidir si **Aurora** necesita más educación, más prueba social o mejor precio percibido (nunca descuento).

**Entregable de la semana:** informe de campaña con CAC, ROAS, margen y aprendizajes sobre **Aurora**.

---

## 6. Métricas de éxito

### Métricas del norte
| Métrica | Meta para las 4 semanas |
|---|---|
| **Unidades vendidas de Aurora** | Definir meta realista con tu línea base; apuntar a crecimiento semanal sostenido |
| **% de pedidos totales que incluyen Aurora** | 15–25% del total |
| **Margen bruto de Aurora** | Mantenerlo sin erosión por descuentos |
| **CAC de Aurora vs. margen bruto** | CAC **por debajo** del margen bruto de Aurora |

### Métricas de adquisición
| Métrica | Meta orientativa |
|---|---|
| **CTR en Meta Ads (Aurora)** | ≥ 1,5% en frío; ≥ 2,5% en retargeting |
| **ROAS de retargeting** | ≥ 3x |
| **ROAS de frío** | ≥ 1,5x (escalable si supera esto) |
| **Visitas a la página de Aurora** | Crecimiento semanal constante |

### Métricas de WhatsApp (tu canal de cierre)
| Métrica | Meta orientativa |
|---|---|
| **Conversaciones iniciadas sobre Aurora** | 30–50 en el mes |
| **Tasa de cierre de conversaciones de Aurora** | ≥ 15% |
| **Tiempo de primera respuesta** | < 15 minutos en horario comercial |

### Métricas de contenido
- **Guardados y compartidos** en publicaciones de **Aurora** (indicador de intención premium).
- **Retención de video** en Reels de Aurora (primeros 3 segundos).
- **Respuestas en historias** mencionando Aurora.

### Métricas de retención y base
- **Compradoras nuevas de Aurora** captadas.
- **Testimonios de Aurora** recolectados (meta: 5).
- **Migración Luna/Sol → Aurora** (cuántas clientas previas subieron de nivel).
- **Crecimiento de la base de WhatsApp y email** segmentada por interés en Aurora.

### Criterios de decisión al cierre
- **Escalar Aurora** si el CAC está por debajo del margen y el ROAS de retargeting ≥ 3x.
- **Reformular el mensaje de Aurora** si hay mucho clic pero poca conversación.
- **Reformular la asesoría** si hay conversaciones pero no cierre.
- **No tocar el precio de Aurora** en ningún escenario de esta campaña.

---

## 7. Riesgos y cómo los manejo

| Riesgo | Acción preventiva |
|---|---|
| **Aurora se percibe cara sin contexto** | Contenido educativo y asesoría 1:1 desde la semana 1 |
| **Tentación de descontar Aurora** | Sustituir cualquier descuento por **valor agregado** (empaque, guía, asesoría) |
| **Pocos testimonios al inicio** | Usar microinfluencers y primeras compradoras; pedir reseña desde la semana 1 |
| **Dispersión de canales** | Si falta tiempo, recortar TikTok y Google; sostener Instagram + WhatsApp + Meta Ads |
| **Público frío demasiado amplio** | Mantener segmentación estricta en Bogotá y creatividades específicas de Aurora |

---

**En una frase:** durante 4 semanas, **Aurora** se vende explicando, acompañando y demostrando experiencia —con Instagram y WhatsApp como núcleo, Meta Ads como amplificador y **cero descuentos sobre Aurora**.