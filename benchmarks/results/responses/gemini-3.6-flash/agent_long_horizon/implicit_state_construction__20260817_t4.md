# Gemini 3.6 Flash — agent_long_horizon/implicit_state_construction

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 66.206s | tokens_per_second: 164.8
- input_tokens: 12118 | output_tokens: 9922

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

¡Hola, Camila! Sí, me queda perfectamente claro todo el contexto de tu negocio. 

Tengo registrados todos los datos claves:
* **Ubicación y mercado:** Bogotá, Colombia (tienda online).
* **Catálogo de productos:**
  1. **Aurora:** Set de cuidado facial (Gama alta / Precio premium).
  2. **Sol:** Kit de maquillaje natural (Gama media / Precio medio).
  3. **Luna:** Crema corporal (Gama inicial / Precio de entrada).
* **Competencia directa local:** *Botica Verde* y *Skin Lab*.

Estoy listo para ayudarte a estructurar tus campañas. ¿En qué producto o estrategia te gustaría que nos enfoquemos primero?

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Ofrecemos a Bogotá una experiencia integral de belleza natural y cuidado consciente, diseñada para adaptarse a los diferentes presupuestos y etapas de la rutina de nuestras clientas. Desde opciones accesibles para el cuidado diario hasta tratamientos faciales premium, transformamos el bienestar personal con productos de alta calidad entregados directamente en tu hogar.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Para tu tienda en Bogotá y la naturaleza visual de tus productos de belleza, te recomiendo priorizar una estrategia enfocada en tres canales principales:

1. **Instagram y TikTok (Meta Ads + Contenido Orgánico):**
   * **Por qué:** Son los canales reyes para el sector belleza y maquillaje. Te permitirán mostrar el "antes y después", rutinas de cuidado con *Aurora* y tutoriales de maquillaje natural con *Sol*. 
   * **Estrategia:** Usa la segmentación geográfica exclusiva para Bogotá y crea anuncios dirigidos según el poder adquisitivo (ej. anuncios de *Luna* a audiencias más amplias y *Aurora* a audiencias con intereses de alta gama).

2. **WhatsApp Business:**
   * **Por qué:** En el e-commerce en Colombia, el contacto directo genera muchísima confianza y acelera la decisión de compra, especialmente para vender el set premium *Aurora*, donde las clientas suelen hacer preguntas sobre su tipo de piel antes de invertir.
   * **Estrategia:** Enlaza tus anuncios de Instagram directo a WhatsApp para ofrecer asesoría personalizada.

3. **Google Ads (Búsqueda y Shopping):**
   * **Por qué:** Te permite captar a clientas en Bogotá que ya tienen la intención de compra activa (buscando términos como "crema corporal Bogotá", "maquillaje natural Colombia" o "set cuidado facial").
   * **Estrategia:** Posicionarte frente a las búsquedas que también atraen a *Botica Verde* y *Skin Lab*.

**Canal secundario para fidelizar:** 
* **Email Marketing:** Ideal para hacer *cross-selling* (venta cruzada). A quien te compró la crema *Luna* (precio entrada), le envías una secuencia educativa para que semanas después pruebe *Sol* o *Aurora*.

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Para una emprendedora, es clave mantener una frecuencia constante pero **sostenible** en el tiempo para no saturarse. Considerando el clima frío de Bogotá (que influye mucho en el cuidado de la piel) y tus tres productos (*Luna*, *Sol* y *Aurora*), esta es la frecuencia recomendada por canal:

### 1. Instagram y TikTok (Nivel de prioridad: Alto)
Son canales de descubrimiento visual. Aquí debes repartir el contenido por formatos:

*   **Instagram Stories (Todos los días, 3 a 5 historias):** 
    *   *Uso:* Mostrar el "detrás de cámaras", testimonios de clientas en Bogotá, encuestas y tips rápidos (ej. *"¿Cómo cuidar tu piel con el frío de Bogotá hoy?"*).
*   **Reels / TikToks (3 a 5 veces por semana):**
    *   *Uso:* Es tu motor de alcance. Haz tutoriales de maquillaje "no-makeup" con *Sol*, rutinas paso a paso de noche con *Aurora*, o el efecto hidratante de *Luna*.
*   **Publicaciones en el Grid / Carrouseles (2 a 3 veces por semana):**
    *   *Uso:* Contenido educativo (ej. *"Diferencias entre hidratar y nutrir la piel"*), fotos estéticas de los empaques o comparativas de ingredientes.

---

### 2. WhatsApp Business (Nivel de prioridad: Medio-Directo)
Es un canal de conversión y cercanía, no debes saturar a tus contactos.

*   **Estados de WhatsApp (3 a 4 veces por semana):**
    *   *Uso:* Fotos reales de envíos saliendo en Bogotá, testimonios de clientas felices o promociones relámpago. Es muy efectivo y no es invasivo.
*   **Mensajes masivos / Listas de difusión (Máximo 1 o 2 veces al mes):**
    *   *Uso:* Exclusivamente para lanzamientos, re-stock o promociones especiales para clientas VIP. Si escribes más seguido, te bloquearán.

---

### 3. Email Marketing (Nivel de prioridad: Fidelización)
*   **1 correo cada 10 o 15 días:**
    *   *Uso:* Enviar contenido de valor sobre cuidado de la piel, guías de uso de tus productos y ofertas exclusivas de venta cruzada (por ejemplo: enviar a quienes compraron *Luna* una guía de cómo complementar su rutina con el set *Aurora*).

---

**💡 Consejo pro para organizar tu tiempo:** 
Dedica un solo día a la semana (ej. los lunes) a grabar y programar todos los Reels y publicaciones. Así solo tendrás que preocuparte en el día a día por responder mensajes en Bogotá y subir las historias.

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Para el sector de *skincare*, el contenido que mejor funciona es aquel que **educa, muestra texturas reales y genera confianza**, ya que la gente está aplicando estos productos directamente sobre su piel.

Aquí tienes los 5 tipos de contenido con mayor tasa de conversión para skincare, aplicados a tu catálogo y al público de Bogotá:

---

### 1. Demostración de Texturas y ASMR (Primeros planos)
A las consumidoras de skincare les encanta ver cómo se siente el producto antes de comprarlo.
*   **Cómo aplicarlo:** Graba videos en muy alta resolución (con luz natural) mostrando la densidad de la crema corporal *Luna*, la absorción de los sueros del set *Aurora*, o el acabado del kit *Sol*. 
*   **Por qué funciona:** Transmite calidad visual. Mostrar una textura rica y cremosa para *Luna* conecta directo con el clima frío de Bogotá, donde la piel suele resecarse más.

### 2. Rutinas Paso a Paso ("Get Ready With Me" / GRWM)
El skincare no se vende como un producto aislado, sino como un **hábito o ritual**.
*   **Cómo aplicarlo:** Haz videos de "Rutina de noche para recuperar la piel tras el frío de Bogotá" usando el set *Aurora*, o un "Maquillaje en 5 minutos para ir a trabajar" usando el kit *Sol*.
*   **Por qué funciona:** Muestra el producto en uso real y ayuda a la clienta a visualizarse usándolo en su día a día.

### 3. Educativo: Problema vs. Solución
El público de skincare ama aprender sobre los ingredientes y los beneficios reales.
*   **Cómo aplicarlo:** Carrouseles o Reels tipo: *"3 errores que resecan tu piel en clima frío (y cómo evitarlos)"* o *"¿En qué orden aplicar tus productos faciales?"* (aquí aprovechas para posicionar las bondades de *Aurora*).
*   **Por qué funciona:** Te posiciona como una experta en cuidado de la piel en Bogotá, diferenciándote de opciones más genéricas como *Skin Lab* o *Botica Verde*.

### 4. Resultados Reales y Prueba Social (Sin Filtros)
En belleza, la transparencia vende más que la perfección publicitaria.
*   **Cómo aplicarlo:** Muestra fotos o videos de "Antes y Después" de clientas reales (con su autorización) utilizando *Aurora* durante 3 semanas, o testimonios en video mostrando el empaque al recibirlo en su casa en Bogotá.
*   **Por qué funciona:** Elimina el miedo a comprar marcas independientes en internet y valida que el producto de verdad funciona.

### 5. Contenido "Mitos vs. Realidades" e Ingredientes
*   **Cómo aplicarlo:** Desmitifica ingredientes populares. Por ejemplo: *"¿Por qué tu crema corporal no te está hidratando lo suficiente?"* para introducir el poder de *Luna*.
*   **Por qué funciona:** Rompe objeciones de venta antes de que la clienta las plantee.

---

**💡 Regla de oro para tu marca:** 
En skincare, **nunca uses filtros de belleza** al grabar los resultados o las rutinas. Muestra la piel real, con sus poros y textura natural. La honestidad visual es lo que hará que las bogotanas elijan tu tienda sobre la competencia.

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Para no competir por precio con **Botica Verde** y **Skin Lab**, debes competir por **valor percibido, experiencia y especialización**. Cuando el valor es claro, el precio pasa a segundo plano.

Aquí tienes 5 estrategias concretas para diferenciar tu marca en Bogotá sin bajar un solo peso a tus productos (*Luna*, *Sol* y *Aurora*):

---

### 1. Hiperlocalización: "Skincare diseñado para el clima de Bogotá"
Ni *Botica Verde* ni *Skin Lab* se están posicionando como especialistas exclusivos del clima bogotano. Adueñate de ese nicho.
*   **Cómo aplicarlo:** Crea tu narrativa alrededor de los factores ambientales de la ciudad: la altitud, la radiación UV en la montaña, el frío matutino y la contaminación. 
*   **Mensaje clave:** *"No es solo cuidado facial; es la fórmula que tu piel necesita para resistir el clima de Bogotá."* Posiciona a *Luna* como el escudo contra la resequedad por el frío y a *Aurora* como el rescate intensivo.

### 2. Pasa de "vender productos" a ofrecer "Asesoría Personalizada"
La mayor desventaja de la competencia suele ser la atención fría y automatizada. Tú puedes ofrecer un toque humano que genera alta fidelización.
*   **Cómo aplicarlo:** Ofrece un "Diagnóstico de Piel Gratuito por WhatsApp". Antes de vender el set premium *Aurora*, invita a las clientas a responder 3 preguntas sobre su piel. 
*   **Por qué funciona:** La clienta no siente que le estás vendiendo un producto costoso, sino que está recibiendo una consulta guiada para invertir bien su dinero.

### 3. La experiencia de "Unboxing" y los detalles memorables
En el comercio electrónico, el empaque es tu tienda física. Si *Botica Verde* entrega en una caja genérica, tú debes entregar una experiencia.
*   **Cómo aplicarlo:** 
    *   Empaque impecable y aromático.
    *   Una tarjeta escrita a mano que diga: *"Camila preparó este pedido especialmente para ti en Bogotá"*.
    *   **Muestras estratégicas:** Si te compran el kit de maquillaje *Sol*, incluyes una muestra de la crema *Luna*. Esto no descuenta precio, pero aumenta el valor percibido y genera ventas cruzadas automáticas.

### 4. Transparencia y "Piel Real" (Diferenciación de marca)
Muchas marcas de la competencia usan modelos de banco de imágenes o filtros perfectos. 
*   **Cómo aplicarlo:** Muestra pieles reales de mujeres en Bogotá, con pecas, textura o rojeces por el frío. Muestra cómo *Sol* realza la belleza natural sin ocultarla y cómo *Aurora* mejora la salud de la piel gradualmente.
*   **Por qué funciona:** Genera una conexión empática y profunda. Las consumidoras actuales valoran más la honestidad que la perfección inalcanzable.

### 5. Entregas ultrarrápidas y locales ("Efecto Bogotá")
Aprovecha que tu único mercado actual es Bogotá para ofrecer una logística superior a la de competidores que quizás envían desde otras ciudades o tardan días.
*   **Cómo aplicarlo:** Ofrece opciones como *"Recíbelo hoy mismo en Bogotá si pides antes del mediodía"* o tarifas de envío fijas/gratuitas a partir de cierto monto (por ejemplo, en la compra del set *Aurora*).
*   **Por qué funciona:** La inmediatez destruye la duda de compra.

---

**En resumen:** Deja que *Botica Verde* y *Skin Lab* peleen por descuentos. Tú posiciona tu marca como la opción experta, cercana, personalizada y perfectamente adaptada a la mujer de Bogotá.

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Para el primer trimestre de tu marca en Bogotá, el objetivo principal es **validar tu embudo de ventas, entender qué producto atrae a más clientas y asegurar la rentabilidad inicial**. No necesitas abrumarte con docenas de métricas; enfócate en estos 6 KPIs clave divididos en 3 áreas:

---

### 1. Ventas y Rentabilidad (Lo vital)

*   **1. Ticket Promedio (AOV - Average Order Value):**
    *   *Qué mide:* El valor promedio que gasta una clienta en cada compra.
    *   *Por qué en tu caso:* Tienes tres niveles de precio (*Luna* entrada, *Sol* medio, *Aurora* premium). Este KPI te dirá si la gente solo está comprando el producto barato (*Luna*) o si tus estrategias de venta cruzada están logrando que combinen productos o adquieran el set *Aurora*.
*   **2. Costo de Adquisición de Cliente (CAC):**
    *   *Qué mide:* Cuánto dinero inviertes en publicidad en Bogotá para conseguir **una** nueva clienta.
    *   *Por qué importa:* Si vender una crema *Luna* te cuesta en publicidad más de lo que ganas por ella, sabrás que debes ajustar los anuncios o enfocar la pauta publicitaria en los productos de mayor margen (*Sol* o *Aurora*).

---

### 2. Rendimiento del Catálogo (Tus productos)

*   **3. Mix de Ventas por Producto (% sobre el total):**
    *   *Qué mide:* Qué porcentaje de las ventas totales representa cada uno de tus tres productos (*Luna*, *Sol* y *Aurora*).
    *   *Por qué importa:* Te confirmará cuál es tu verdadero "producto gancho" en Bogotá. Lo ideal en el primer trimestre es que *Luna* atraiga volumen de clientas nuevas y *Aurora* genere el mayor margen de ganancia.
*   **4. Tasa de Recompra o Venta Cruzada (Cross-selling):**
    *   *Qué mide:* Porcentaje de clientas que entraron comprando un producto (ej. la crema *Luna*) y regresan a comprar otro (ej. el kit *Sol* o el set *Aurora*) durante los primeros 90 días.

---

### 3. Eficiencia de Canales Digitales

*   **5. ROAS (Retorno de la Inversión Publicitaria):**
    *   *Qué mide:* Cuántos pesos colombianos generas por cada peso invertido en anuncios (Meta Ads / Google Ads).
    *   *Meta Q1:* Para e-commerce de belleza, busca un ROAS inicial de al menos **3x** (es decir, recuperar $3 por cada $1 invertido en pauta).
*   **6. Tasa de Conversión en WhatsApp:**
    *   *Qué mide:* De todas las personas de Bogotá que te escriben a WhatsApp desde las redes sociales, ¿cuántas terminan comprando?
    *   *Por qué importa:* Dado que WhatsApp será tu canal clave para vender el set premium *Aurora*, medir esto te dirá si tu atención y asesoría al cliente están cerrando ventas de forma efectiva.

---

**💡 Consejo para tu primer mes:**
No te preocupes si el CAC es un poco alto durante las primeras semanas; las plataformas publicitarias estarán aprendiendo a identificar a tu público ideal en Bogotá. La clave del primer trimestre es lograr que la experiencia de compra sea tan buena que el voz a voz empiece a crecer.

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

¡Excelente decisión! Enfocarnos en tu producto de mayor valor es la mejor estrategia para maximizar el retorno de inversión y posicionar tu marca en el segmento de alta gama en Bogotá.

Aquí tienes el plan de campaña de 4 semanas diseñado exclusivamente para el **set de cuidado facial premium 'Aurora'**.

---

# 🌟 Plan de Campaña: "Ritual Aurora: Transformación Facial Intensiva"

### 1. Objetivo General
Generar un volumen significativo de ventas del set **'Aurora'** en Bogotá durante 30 días, posicionándolo como el tratamiento facial indispensable para combatir los efectos del clima frío y la contaminación en la piel, logrando un **ROAS superior a 3.5x**.

### 2. Audiencia Objetivo
*   **Ubicación:** Bogotá (enfoque en zonas de poder adquisitivo medio-alto y alto / Estratos 4, 5 y 6).
*   **Perfil:** Mujeres de 28 a 52 años interesadas en cuidado facial, cosmética limpia, antienvejecimiento, dermatología y marcas de belleza premium.
*   **Compradora ideal de 'Aurora':** Mujeres que buscan resultados visibles, dispuestas a invertir en una rutina completa y que valoran la atención personalizada antes de comprar.

### 3. Canales Principales
*   **Meta Ads (Instagram / Facebook):** Anuncios segmentados por ubicación en Bogotá e intereses de alta gama.
*   **WhatsApp Business:** Canal central de conversión ("Diagnóstico Facial Aurora").
*   **Email Marketing:** Secuencia de educación y venta directa a tu base de datos existente.

### 4. Mensaje Principal (Core Message)
> *"Tu piel no necesita más productos, necesita el ritual correcto. Descubre el set facial 'Aurora': la dosis de nutrición e hidratación profunda que rescata tu rostro del frío de Bogotá."*

---

## 🗓️ Cronograma Semanal (Estrategia de 4 Semanas)

### **Semana 1: Educación y Revelación del Deseo**
*   **Objetivo:** Generar curiosidad, posicionar la calidad premium de **'Aurora'** y exponer los problemas de la piel en Bogotá (deshidratación, opacidad por el frío).
*   **Contenido / Acciones:**
    *   **Anuncios (Meta Ads):** Video de alta calidad mostrando la textura de cada producto dentro del set **'Aurora'** con el gancho: *"¿Tu piel se siente seca u opaca por las mañanas en Bogotá?"*.
    *   **Reels / TikTok:** "Desempacando el set **'Aurora'**: ¿Qué contiene y por qué vale cada peso?".
    *   **Historias:** Explicación ingrediente por ingrediente de la fórmula de **'Aurora'**.
    *   **Email:** "El secreto para mantener una piel radiante en el clima de Bogotá: Presentando el set **'Aurora'**".

### **Semana 2: Prueba Social y Asesoría Directa**
*   **Objetivo:** Romper objeciones de precio demostrando resultados reales y llevando tráfico a WhatsApp.
*   **Contenido / Acciones:**
    *   **Anuncios (Meta Ads):** Formato carrusel con testimonios reales y fotos (sin filtros) del "Antes y Después" tras usar el set **'Aurora'** durante 21 días.
    *   **Estrategia WhatsApp:** Lanzamiento del *"Diagnóstico de Piel Gratuito 'Aurora'"*. Los anuncios invitan a escribir a WhatsApp para saber si el set **'Aurora'** es ideal para su tipo de piel.
    *   **Reels:** "Cómo aplicar el set **'Aurora'** paso a paso en tu rutina de noche".
    *   **Diferenciación:** Resaltar por qué el set **'Aurora'** supera a alternativas de la competencia en Bogotá (como *Skin Lab* o *Botica Verde*).

### **Semana 3: Experiencia de Lujo e Incentivo VIP**
*   **Objetivo:** Elevar el valor percibido del set **'Aurora'** y acelerar la decisión de compra de las usuarias indecisas.
*   **Contenido / Acciones:**
    *   **Incentivo Exclusivo:** Por la compra del set **'Aurora'**, regalar una minitalla de la crema corporal *Luna* + Envío exprés gratis en Bogotá.
    *   **Reels:** Mostrar la experiencia de empaque de un pedido del set **'Aurora'** (la nota personalizada, el aroma al abrir la caja, la elegancia del empaque).
    *   **Historias:** Respuestas a preguntas frecuentes sobre **'Aurora'** (ej. *"¿Sirve para piel mixta?", "¿Cuánto dura el set completo?"*).

### **Semana 4: Urgencia y Cierre de Ventas**
*   **Objetivo:** Convertir al público que interactuó con los anuncios de **'Aurora'** en semanas anteriores pero no compró (Retargeting).
*   **Contenido / Acciones:**
    *   **Anuncios de Retargeting (Meta Ads):** Mensaje enfocado en urgencia: *"Últimos sets **'Aurora'** con regalo VIP y envío gratis en Bogotá"*.
    *   **WhatsApp / Difusión:** Seguimiento personalizado a las clientas que pidieron información de **'Aurora'** en la semana 2 y no cerraron la compra.
    *   **Email:** "Últimas 48 horas: Asegura tu set **'Aurora'** con beneficio exclusivo".

---

## 📊 Métricas de Éxito de la Campaña (KPIs)

Al finalizar las 4 semanas, evaluaremos el éxito del set **'Aurora'** con los siguientes números:

1.  **Unidades vendidas del set 'Aurora':** Definir la meta de unidades según tu stock actual (ej. 30 a 50 sets).
2.  **ROAS específico para 'Aurora':** Mínimo **3.5x** en las campañas pagadas.
3.  **Tasa de conversión en WhatsApp:** Lograr que al menos el **20%** de las personas que pregunten por el set **'Aurora'** por WhatsApp completen la compra.
4.  **Costo por Adquisición (CAC) de 'Aurora':** Debe mantenerse por debajo del 30% del precio de venta total del set para garantizar un alto margen de ganancia.


## Respuesta completa

¡Excelente decisión! Enfocarnos en tu producto de mayor valor es la mejor estrategia para maximizar el retorno de inversión y posicionar tu marca en el segmento de alta gama en Bogotá.

Aquí tienes el plan de campaña de 4 semanas diseñado exclusivamente para el **set de cuidado facial premium 'Aurora'**.

---

# 🌟 Plan de Campaña: "Ritual Aurora: Transformación Facial Intensiva"

### 1. Objetivo General
Generar un volumen significativo de ventas del set **'Aurora'** en Bogotá durante 30 días, posicionándolo como el tratamiento facial indispensable para combatir los efectos del clima frío y la contaminación en la piel, logrando un **ROAS superior a 3.5x**.

### 2. Audiencia Objetivo
*   **Ubicación:** Bogotá (enfoque en zonas de poder adquisitivo medio-alto y alto / Estratos 4, 5 y 6).
*   **Perfil:** Mujeres de 28 a 52 años interesadas en cuidado facial, cosmética limpia, antienvejecimiento, dermatología y marcas de belleza premium.
*   **Compradora ideal de 'Aurora':** Mujeres que buscan resultados visibles, dispuestas a invertir en una rutina completa y que valoran la atención personalizada antes de comprar.

### 3. Canales Principales
*   **Meta Ads (Instagram / Facebook):** Anuncios segmentados por ubicación en Bogotá e intereses de alta gama.
*   **WhatsApp Business:** Canal central de conversión ("Diagnóstico Facial Aurora").
*   **Email Marketing:** Secuencia de educación y venta directa a tu base de datos existente.

### 4. Mensaje Principal (Core Message)
> *"Tu piel no necesita más productos, necesita el ritual correcto. Descubre el set facial 'Aurora': la dosis de nutrición e hidratación profunda que rescata tu rostro del frío de Bogotá."*

---

## 🗓️ Cronograma Semanal (Estrategia de 4 Semanas)

### **Semana 1: Educación y Revelación del Deseo**
*   **Objetivo:** Generar curiosidad, posicionar la calidad premium de **'Aurora'** y exponer los problemas de la piel en Bogotá (deshidratación, opacidad por el frío).
*   **Contenido / Acciones:**
    *   **Anuncios (Meta Ads):** Video de alta calidad mostrando la textura de cada producto dentro del set **'Aurora'** con el gancho: *"¿Tu piel se siente seca u opaca por las mañanas en Bogotá?"*.
    *   **Reels / TikTok:** "Desempacando el set **'Aurora'**: ¿Qué contiene y por qué vale cada peso?".
    *   **Historias:** Explicación ingrediente por ingrediente de la fórmula de **'Aurora'**.
    *   **Email:** "El secreto para mantener una piel radiante en el clima de Bogotá: Presentando el set **'Aurora'**".

### **Semana 2: Prueba Social y Asesoría Directa**
*   **Objetivo:** Romper objeciones de precio demostrando resultados reales y llevando tráfico a WhatsApp.
*   **Contenido / Acciones:**
    *   **Anuncios (Meta Ads):** Formato carrusel con testimonios reales y fotos (sin filtros) del "Antes y Después" tras usar el set **'Aurora'** durante 21 días.
    *   **Estrategia WhatsApp:** Lanzamiento del *"Diagnóstico de Piel Gratuito 'Aurora'"*. Los anuncios invitan a escribir a WhatsApp para saber si el set **'Aurora'** es ideal para su tipo de piel.
    *   **Reels:** "Cómo aplicar el set **'Aurora'** paso a paso en tu rutina de noche".
    *   **Diferenciación:** Resaltar por qué el set **'Aurora'** supera a alternativas de la competencia en Bogotá (como *Skin Lab* o *Botica Verde*).

### **Semana 3: Experiencia de Lujo e Incentivo VIP**
*   **Objetivo:** Elevar el valor percibido del set **'Aurora'** y acelerar la decisión de compra de las usuarias indecisas.
*   **Contenido / Acciones:**
    *   **Incentivo Exclusivo:** Por la compra del set **'Aurora'**, regalar una minitalla de la crema corporal *Luna* + Envío exprés gratis en Bogotá.
    *   **Reels:** Mostrar la experiencia de empaque de un pedido del set **'Aurora'** (la nota personalizada, el aroma al abrir la caja, la elegancia del empaque).
    *   **Historias:** Respuestas a preguntas frecuentes sobre **'Aurora'** (ej. *"¿Sirve para piel mixta?", "¿Cuánto dura el set completo?"*).

### **Semana 4: Urgencia y Cierre de Ventas**
*   **Objetivo:** Convertir al público que interactuó con los anuncios de **'Aurora'** en semanas anteriores pero no compró (Retargeting).
*   **Contenido / Acciones:**
    *   **Anuncios de Retargeting (Meta Ads):** Mensaje enfocado en urgencia: *"Últimos sets **'Aurora'** con regalo VIP y envío gratis en Bogotá"*.
    *   **WhatsApp / Difusión:** Seguimiento personalizado a las clientas que pidieron información de **'Aurora'** en la semana 2 y no cerraron la compra.
    *   **Email:** "Últimas 48 horas: Asegura tu set **'Aurora'** con beneficio exclusivo".

---

## 📊 Métricas de Éxito de la Campaña (KPIs)

Al finalizar las 4 semanas, evaluaremos el éxito del set **'Aurora'** con los siguientes números:

1.  **Unidades vendidas del set 'Aurora':** Definir la meta de unidades según tu stock actual (ej. 30 a 50 sets).
2.  **ROAS específico para 'Aurora':** Mínimo **3.5x** en las campañas pagadas.
3.  **Tasa de conversión en WhatsApp:** Lograr que al menos el **20%** de las personas que pregunten por el set **'Aurora'** por WhatsApp completen la compra.
4.  **Costo por Adquisición (CAC) de 'Aurora':** Debe mantenerse por debajo del 30% del precio de venta total del set para garantizar un alto margen de ganancia.