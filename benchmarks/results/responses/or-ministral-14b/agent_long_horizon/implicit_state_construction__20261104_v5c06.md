# Ministral 14B — agent_long_horizon/implicit_state_construction

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 7.31 | quality: 8.5
- latency_total: 383.77s | tokens_per_second: 71.8
- input_tokens: 49419 | output_tokens: 21010

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

¡Hola Camila! Sí, me queda **muy claro** el contexto de tu negocio. Aquí está el resumen que guardaré para personalizar las recomendaciones sin repetir datos clave:

---
**Tu negocio:**
- **Nombre:** Tienda online (nombre no mencionado, pero lo anotaré si lo compartes).
- **Productos:**
  1. **Aurora**: Set de cuidado facial (*premium*).
  2. **Sol**: Kit de maquillaje natural (*precio medio*).
  3. **Luna**: Crema corporal (*precio entrada*).
- **Mercado:** **Exclusivo en Bogotá** (Colombia).
- **Competencia directa:**
  - *Botica Verde* (posicionamiento: natural/organic, probable enfoque en precios medios-altos).
  - *Skin Lab* (posicionamiento: *skincare* científico/clínico, posible enfoque en premium).

---
**Notas adicionales que mencionaste implícitamente:**
- **Estrategia de precios:** Segmentación clara por gama (entrada, medio, premium).
- **Enfoque:** Productos naturales (especialmente en *Sol* y *Luna*), pero con un toque *premium* en *Aurora*.

---
**¿Qué necesitas ayuda hoy?**
Por ejemplo, podríamos empezar con:
1. **Definir una campaña de lanzamiento** para *Aurora* (premium) en Bogotá, destacando su exclusividad frente a *Skin Lab*.
2. **Estrategias de precios o promociones** para *Luna* (entrada) que atraigan a un público nuevo sin canibalizar las ventas de *Sol*.
3. **Análisis de competencia**: ¿Quieres que profundice en cómo diferenciarte de *Botica Verde* en redes sociales o publicidad?
4. **Logística**: Optimizar envíos en Bogotá (¿tienes aliado de transporte?).

Dime por dónde prefieres empezar o si hay algo más específico que quieras ajustar en el contexto. ¡Estoy lista! 🌟

---
*PD: Si en algún momento quieres cambiar un detalle (ej: "Ah, *Aurora* también incluye un difusor de aceites esenciales"), avísame y lo actualizo.*

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Aquí tienes una propuesta de valor clara, alineada con lo que mencionaste (enfoque en **naturalidad + exclusividad por gama de precios**, diferenciación de competidores y mercado bogotano):

---
**"En [Nombre de tu tienda], combinamos ingredientes naturales de alta calidad con fórmulas innovadoras para que tu rutina de belleza sea **auténtica y efectiva**—desde el cuidado accesible de *Luna* hasta el lujo facial de *Aurora*, todo creado para que Bogotá respire belleza sin compromisos. A diferencia de *Botica Verde* (que prioriza lo orgánico masivo) o *Skin Lab* (enfoque clínico), nosotros **personalizamos tu experiencia**: con *Sol* llevas maquillaje natural a tu día a día, y con *Aurora* descubres rituales que cuidan tu piel como un secreto de spa en casa."**

---

### **¿Por qué funciona?**
1. **Diferenciación por producto**:
   - *Luna*: "accesible" (vs. competencia que puede ser más cara en entrada).
   - *Sol*: "maquillaje natural para el día a día" (vs. *Botica Verde*, que quizá sea más "herbolario").
   - *Aurora*: "lujo facial/secreto de spa" (vs. *Skin Lab*, que puede sonar más "laboratorio").

2. **Enfoque local**:
   - "Que Bogotá respire belleza" → Conexión emocional con el mercado objetivo.

3. **Ingredientes naturales + innovación**:
   - Evitas sonar genérico ("100% natural") y destacas que tus fórmulas son **pensadas** (ej: "rituales", "auténtica").

---
**Variante corta (si prefieres impacto en redes o packaging):**
*"Belleza natural que se adapta a tu bolsillo y a tu piel: desde cremas que cuidan sin gastar (*Luna*), hasta sets que transforman tu rutina en un momento premium (*Aurora*). En Bogotá, donde lo orgánico y lo sofisticado se encuentran."*

---
**¿Quieres ajustar algo?**
Por ejemplo:
- Si *Aurora* tiene un ingrediente estrella (ej: "con oro coloidal"), podríamos añadirlo.
- Si tu tienda tiene un nombre o eslogan, lo integro.
- Si prefieres un tono más **científico** (para competir con *Skin Lab*) o más **poético** (para conectar con emociones).

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Para tu tienda online en **Bogotá**, con productos de belleza natural segmentados por precios y competencia clara (*Botica Verde* y *Skin Lab*), te recomiendo priorizar estos **canales digitales**, ordenados por impacto potencial y alineados a tu propuesta de valor:

---

### **1. Instagram (Prioridad Máxima)**
**¿Por qué?**
- **Visual perfecto** para belleza (maquillaje, skincare, lifestyle).
- **Mercado bogotano**: Instagram es el rey en Colombia (80% de usuarios entre 18-34 años, tu público objetivo).
- **Herramientas clave**:
  - **Reels**: Tutoriales de uso de *Sol* (ej: *"Cómo aplicar el kit natural para un look office-friendly"*) o antes/después con *Aurora*.
  - **Stories**: Encuestas (*"¿Prefieres cremas con aceites o sin fragancia?"*), testimonios de clientes bogotanos, y *close-ups* de ingredientes (ej: "Este es el aloe vera de *Luna*, cultivado en...").
  - **Guías (IG Guides)**: "Rutina de skincare para cada tipo de piel bogotana" (incluyendo tus productos).
  - **Colaboraciones**: Microinfluencers bogotanos de belleza natural (ej: @bellanaturalco o @skincarecolombia, con 10K-50K seguidores). Ofrece productos gratis a cambio de contenido auténtico.

**Estrategia inicial**:
- **Contenido educativo**: Desmonta mitos (ej: *"¿El maquillaje natural realmente obstruye poros?"* con datos de *Sol*).
- **User-Generated Content (UGC)**: Pide a clientes que etiqueten tu marca con un hashtag único (#MiRutinaAurora) y repostea sus fotos.
- **Publicidad**: Anuncios en Reels dirigidos a bogotanos interesados en *"maquillaje natural"*, *"skincare premium"* o *"productos colombianos"*.

**Inversión**: $500-$1,000 COP/mes en ads (prueba segmentos como mujeres 25-40 años, C1-C3 en Bogotá).

---

### **2. TikTok (Prioridad Alta)**
**¿Por qué?**
- **Algoritmo favorable** para nuevos negocios (puedes viralizar con poco presupuesto).
- **Tendencias de belleza**: TikTok domina en Colombia con desafíos como *"GRWM"* (Get Ready With Me) o *"satisfying skincare routines"*.
- **Ejemplo de contenido**:
  - *"Un día usando solo productos de [Tu Tienda]"* (mostrando *Sol* + *Luna*).
  - *"¿Vale la pena el precio premium de Aurora?"* (comparando con *Skin Lab*).

**Diferencial**:
- Usa el **hashtag #BellezaBogota** para conectar con la identidad local.
- **Duetos**: Invita a una influencer a probar *Aurora* y reaccionar en vivo.

**Inversión**: $300-$800 COP/mes (prueba con videos orgánicos primero).

---

### **3. Facebook (Prioridad Media-Alta)**
**¿Por qué?**
- **Público más amplio**: Incluye mujeres 30-50 años (que pueden comprar *Aurora* como regalo).
- **Grupos locales**: Únete a comunidades como *"Belleza Natural Colombia"* o *"Skincare en Bogotá"* para participar (sin spam) y compartir tus productos cuando sean relevantes.
- **Marketplace**: Ideal para liquidar stock de *Luna* (precio entrada) con descuentos temporales.

**Estrategia**:
- **Videos cortos** en el feed (ej: *"Cómo usar el kit Sol en 60 segundos"*).
- **Eventos en vivo**: Charlas con dermatólogos bogotanos (ej: *"Mitologias del cuidado facial"*).

---

### **4. Google Ads (Prioridad Media)**
**¿Por qué?**
- **Búsqueda directa**: Cuando alguien en Bogotá busca *"kit maquillaje natural comprar"* o *"crema facial premium Bogotá"*, quieres aparecer.
- **Competencia**: *Botica Verde* y *Skin Lab* probablemente inviertan aquí; puedes destacar con palabras clave como:
  - *"maquillaje natural sin parabenos Bogotá"*
  - *"set skincare premium Colombia"*
  - *"crema corporal natural para piel seca"* (si *Luna* tiene ese enfoque).

**Estrategia**:
- **Campañas de Shopping**: Si usas Google Merchant Center, muestra tus productos con fotos y precios directamente en los resultados.
- **Extensiones de llamada**: Añade *"Envío gratis en Bogotá"* o *"Consulta por packs"* para aumentar clics.

**Inversión**: $1,000-$2,000 COP/mes (empieza con un presupuesto diario de $30 COP por campaña).

---

### **5. WhatsApp Business (Prioridad Alta para Ventas)**
**¿Por qué?**
- **Canales preferidos en Colombia**: El 90% de los bogotanos usan WhatsApp para comprar (especialmente para consultas rápidas).
- **Atención personalizada**: Puedes enviar catálogos interactivos (con emojis y enlaces a productos) o resolver dudas al instante.

**Cómo implementarlo**:
- **Automatiza respuestas**: Usa herramientas como *ManyChat* para saludar a nuevos contactos con un mensaje como:
  *"¡Hola! En [Tu Tienda] te ayudamos a elegir. ¿Buscas algo para hidratar (*Luna*), maquillarte naturalmente (*Sol*) o un ritual premium (*Aurora*)?"*.
- **Ofertas exclusivas**: Envía códigos de descuento a clientes recurrentes (ej: *"10% en tu próxima compra con el código BOGOTA10"*).

---

### **6. Email Marketing (Prioridad Media para Fidelización)**
**¿Por qué?**
- **Baja competencia**: Muchos negocios de belleza lo descuidan.
- **Ventas recurrentes**: Ideal para promocionar *Luna* (precio entrada) como "producto del mes".

**Estrategia**:
- **Secuencia de bienvenida**: Para nuevos suscriptores:
  1. *"Gracias por unirte a nuestra comunidad bogotana. Aquí tienes un 5% de descuento en *Sol*."*
  2. *"¿Sabías que *Aurora* incluye un difusor de aceites? Te contamos cómo usarlo..."* (con video).
- **Newsletter mensual**: *"Tendencias de belleza natural en Bogotá"* (incluye tus productos como solución).

**Herramienta**: Mailchimp (gratis hasta 500 contactos) o *Klick Tipp* (popular en Latinoamérica).

---

### **7. Pinterest (Prioridad Baja-Media)**
**¿Por qué?**
- **Tráfico orgánico**: Ideal para *Aurora* (inspiración de rutinas premium).
- **SEO visual**: Usa palabras clave como *"rutina nocturna skincare Colombia"* en las descripciones de tus pins.

**Contenido**:
- Tableros temáticos:
  - *"Maquillaje natural para oficina en Bogotá"*.
  - *"Ingredientes clave en belleza natural"* (con fotos de tus productos).

---

### **8. YouTube (Prioridad Baja, pero Potencial a Largo Plazo)**
**¿Por qué?**
- **Contenido evergreen**: Tutoriales como *"Cómo usar el kit Sol para un look de boda"* seguirán generando tráfico.
- **Monetización**: Si creces, puedes ganar con ads o afiliados.

**Ejemplo de video**:
*"Desempacando Aurora: ¿Vale el precio premium?"* (con review honesta).

---

### **Plan de Acción Recomendado (Primeros 3 Meses)**
| **Mes** | **Enfoque**                          | **Canales Prioritarios**               | **Meta**                          |
|---------|--------------------------------------|----------------------------------------|-----------------------------------|
| 1       | **Posicionamiento de marca**          | Instagram + TikTok (orgánico)          | 5K seguidores en IG, 1 video viral en TikTok. |
| 2       | **Ventas directas**                   | WhatsApp + Google Ads                  | 30 ventas/mes (objetivo: $X).     |
| 3       | **Fidelización**                      | Email + Facebook Groups                | 20% de clientes recurrentes.      |

---

### **¿Qué evitar?**
- **Redes genéricas**: LinkedIn o Twitter (a menos que hagas alianzas con dermatólogos).
- **Saturar con publicidad**: Empieza con contenido orgánico en Instagram/TikTok para generar confianza.
- **Ignorar el móvil**: El 70% de las compras en Colombia se hacen desde celular. Asegúrate de que tu tienda tenga diseño *responsive*.

---
**Pregunta clave para ti**:
- ¿Tienes un presupuesto definido para publicidad? Podría ajustar las recomendaciones (ej: si es bajo, enfocarnos en TikTok e Instagram orgánico).
- ¿Quieres que desarrolle una estrategia de *content calendar* para Instagram o TikTok con ejemplos de posts?

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Aquí tienes un **plan de frecuencia óptimo** para contenido orgánico en cada canal, diseñado para **maximizar alcance en Bogotá** sin saturar a tu audiencia. Las recomendaciones consideran:
1. **Algoritmos** (ej: Instagram premia la constancia en Reels).
2. **Comportamiento local** (bogotanos consumen más contenido en horarios específicos).
3. **Tu capacidad operativa** (como emprendedora, priorizo equilibrio entre calidad y consistencia).

---

### **1. Instagram (Prioridad Máxima)**
**Frecuencia ideal**:
- **Feed**: **3-4 publicaciones/semana** (calidad > cantidad).
  - *Ejemplo de distribución*:
    - **Lunes**: Producto destacado (*Aurora* o *Sol* con lifestyle).
    - **Miércoles**: Tutorial o "cómo usar" (ej: *"3 pasos para aplicar el kit Sol en 1 minuto"*).
    - **Viernes**: User-Generated Content (UGC) o testimonio de cliente bogotano.
    - **Domingo**: Contenido inspirational (ej: foto de ingredientes naturales con texto *"Belleza que respeta tu piel y el planeta"*).
- **Stories**: **Diario** (mínimo 1-2 por día).
  - *Ideas rápidas*:
    - Mañanas: Encuestas (*"¿Prefieres cremas con o sin aroma?"*).
    - Tardes: Behind-the-scenes (ej: *"Así empaquetamos *Luna* para ti"*).
    - Noche: Reels cortos o preguntas (*"¿Qué producto te gustaría ver en nuestra línea?"*).
- **Reels**: **3-4/semana** (prioriza los días con más engagement en tu audiencia: **martes y jueves**).
  - *Ejemplo de temas virales para Bogotá*:
    - *"POV: Usas maquillaje natural todo el día"* (muestra *Sol* en una rutina real).
    - *"Antes y después de usar *Aurora* 1 semana"* (con datos como *"-30% de poros visibles"*).
    - *"Desafío: 3 días con solo productos de [Tu Tienda]"* (colabora con microinfluencers).

**Horarios clave en Colombia**:
- **Mejores para publicaciones**: 7:00-9:00 AM o 6:00-8:00 PM (horario de transporte en Bogotá, ideal para contenido relajado o inspirador).
- **Stories**: 12:00-2:00 PM (hora de almuerzo) o 7:00-9:00 PM (navegación nocturna).

---

### **2. TikTok (Prioridad Alta)**
**Frecuencia ideal**:
- **3-5 videos/semana** (consistencia es clave para el algoritmo).
  - *Ejemplo de calendario*:
    - **Lunes**: Tutorial rápido (ej: *"Cómo ocultar ojeras con *Luna*"*).
    - **Miércoles**: Tendencia local (ej: *"GRWM para un día en Chapinero"* usando *Sol*).
    - **Viernes**: Contenido "satisfying" (ej: *"Proceso de creación de *Aurora*"*).
    - **Domingo**: Testimonios o desafíos (ej: *"Prueba *Luna* por 7 días y cuéntanos"*).
- **Live**: **1 vez cada 2 semanas** (ej: *"Q&A sobre skincare natural"* o demo de productos).

**Horarios clave**:
- **8:00-10:00 AM** (desayuno) o **7:00-9:00 PM** (navegación nocturna).

**Pro tip**:
- Usa **hashtags locales** como *#BellezaBogota* o *#SkincareColombia* para aparecer en búsquedas geográficas.
- Reutiliza contenido de Instagram en TikTok (ej: un Reel puede convertirse en un TikTok con un audio viral).

---

### **3. Facebook (Prioridad Media)**
**Frecuencia ideal**:
- **Feed**: **2-3 publicaciones/semana** (menos saturación = más engagement).
  - *Ejemplo*:
    - **Martes**: Video largo (ej: *"Guía completa para elegir tu crema facial"*).
    - **Jueves**: Promoción o descuento exclusivo para seguidores.
- **Stories**: **1-2/semana** (menos prioritario que en Instagram).
- **Grupos**: **Participación activa 2-3 veces/semana** (comenta, comparte contenido relevante *sin vender directo*).

**Horarios clave**:
- **1:00-3:00 PM** (hora de almuerzo) o **7:00-9:00 PM**.

---

### **4. Pinterest (Prioridad Baja-Media)**
**Frecuencia ideal**:
- **10-15 pins/semana** (pueden ser repost de tus productos con diferentes descripciones).
  - *Estrategia*:
    - Crea **tableros temáticos** (ej: *"Rutina nocturna para piel seca"*, *"Maquillaje natural para oficina"*).
    - Usa **palabras clave en descripciones** como *"kit maquillaje natural Bogotá"* o *"crema facial premium Colombia"*.
    - **Ideas de pins**:
      - Infografías (ej: *"Ingredientes que NO usar en tu skincare"*).
      - Fotos de productos con texto sobrecase (ej: *"Luna: tu aliada para piel hidratada todo el día"*).

**Horarios para subir**:
- **Cualquier hora** (Pinterest indexa contenido las 24 horas, pero evita fines de semana).

---

### **5. WhatsApp Business (Frecuencia Estratégica)**
- **Mensajes automáticos**:
  - **Bienvenida**: 1 mensaje al suscribirse (ej: *"¡Hola [Nombre]! Aquí tienes un 5% de descuento en tu primera compra con código BOGOTA5"*).
- **Contenido manual**:
  - **1-2 mensajes/semana** (ej: promociones exclusivas, recordatorios de carrito abandonado).
  - **Evita saturar**: Máximo 1 mensaje por semana sin respuesta previa.

---

### **6. Email Marketing (Frecuencia Moderada)**
- **Newsletter**: **1 vez cada 2 semanas** (ej: *"Tendencias de belleza natural en Bogotá"* con tips + productos tuyos).
- **Promociones**: **1 email/mes** (ej: *"Oferta especial para clientes recurrentes"*).
- **Automatizaciones**:
  - **Email de abandono de carrito**: Enviar 1 hora después de que el usuario lo deje.
  - **Secuencia de bienvenida**: 3 emails en 1 semana (ej: *"Conoce *Sol*", *"Descubre *Aurora*", *"Testimonio de [Cliente]"*).

---

### **7. YouTube (Prioridad Baja, pero Constante)**
**Frecuencia ideal**:
- **1 video/mes** (calidad sobre cantidad).
  - *Ejemplos*:
    - Tutoriales largos (ej: *"Mi rutina de skincare con productos colombianos"*).
    - Reviews comparativas (ej: *"Aurora vs. Skin Lab: ¿Cuál vale la pena?"*).
- **Shorts**: **1-2/semana** (para capitalizar tendencias).

**Horario de subida**:
- **Miércoles o viernes a las 3:00 PM** (momento con menos competencia en YouTube).

---

### **Resumen de Frecuencias por Canal**
| **Canal**       | **Publicaciones/Semana** | **Tipo de Contenido**                          | **Horarios Clave**          |
|------------------|--------------------------|------------------------------------------------|-----------------------------|
| **Instagram**    | Feed: 3-4                | Productos, tutorials, UGC.                     | 7-9 AM / 6-8 PM.            |
|                  | Stories: Diario          | Encuestas, BTS, preguntas.                    | 12-2 PM / 7-9 PM.           |
|                  | Reels: 3-4               | Tendencias, antes/después, desafíos.          | Martes/jueves 7-9 PM.       |
| **TikTok**       | 3-5 videos               | GRWM, satisfying, testimonios.                | 8-10 AM / 7-9 PM.           |
| **Facebook**     | Feed: 2-3                | Videos largos, promociones.                    | 1-3 PM / 7-9 PM.            |
| **Pinterest**    | 10-15 pins               | Infografías, productos con keywords.          | Cualquier hora.             |
| **WhatsApp**     | 1-2 mensajes manuales    | Promociones, recordatorios.                    | 9-11 AM / 5-7 PM.           |
| **Email**        | 1 newsletter cada 2 semanas | Tips + productos.                           | Martes/jueves 10 AM.        |
| **YouTube**      | 1 video/mes              | Tutoriales, comparativas.                    | Miércoles/viernes 3 PM.     |

---

### **Recomendaciones Adicionales**
1. **Batch Creation**:
   - Dedica **1 día/semana** (ej: domingos) a crear contenido para toda la semana. Usa herramientas como *Canva* o *CapCut* para editar rápido.
   - *Ejemplo*: Graba 3 Reels en una tarde y prográmalos para martes, jueves y sábado.

2. **Contenido Evergreen vs. Actual**:
   - **Evergreen** (siempre relevante): Tutoriales, guías de productos, "cómo usar".
   - **Actual** (tendencias): Desafíos virales, colaboraciones, noticias locales (ej: *"Nuevos ingredientes en *Luna* para el clima de Bogotá"*).

3. **Análisis y Ajustes**:
   - Revisa **Insights de Instagram/TikTok** cada semana para ver:
     - ¿Qué tipo de contenido tiene más guardados/compartidos? (Ej: si los Reels de *Aurora* funcionan mejor, haz más de ese producto).
     - ¿A qué hora tu audiencia está más activa? Ajusta horarios según datos reales (no solo los generales).

4. **Colaboraciones**:
   - Coordina con **1-2 microinfluencers bogotanos/mes** para que publiquen contenido orgánico. Ejemplo:
     - *"Prueba *Sol* por 15 días y cuéntanos tu experiencia"* (ellos ganan producto, tú ganas contenido auténtico).

---
**Pregunta para ti**:
- ¿Tienes un equipo o solo trabajas tú? Si es solo tú, podríamos optimizar aún más el plan para que sea **realizable en 5-10 horas/semana** (ej: enfocarnos en 2 canales principales + email).
- ¿Quieres que desarrolle un **calendario específico para las próximas 4 semanas** con ejemplos de posts?

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Para productos de **skincare** como los tuyos (*Aurora* premium, *Sol* maquillaje natural y *Luna* crema corporal), el contenido debe combinar **educación, emoción y prueba social** para generar confianza en un mercado saturado como el de Bogotá. Aquí tienes un desglose de los **tipos de contenido que mejor convierten**, con ejemplos específicos para cada uno de tus productos y cómo diferenciarte de *Botica Verde* (enfoque masivo/organic) y *Skin Lab* (enfoque clínico).

---

### **1. Contenido Educativo (El más efectivo para skincare)**
**Objetivo**: Posicionarte como experta y resolver dudas comunes.
**Formatos**:
- **Tutoriales/Guías**:
  - *"Cómo identificar tu tipo de piel en 3 pasos"* (con tips para elegir entre *Luna* o *Aurora*).
  - *"Mitologias del skincare: ¿El maquillaje natural realmente obstruye poros?"* (para desmontar mitos sobre *Sol*).
  - *"Rutina de skincare para el clima de Bogotá"* (incluyendo tus productos en cada paso).
- **Infografías/Reels explicativos**:
  - *"Ingredientes clave en *Aurora* y por qué funcionan"* (ej: ácido hialurónico, aceites esenciales).
  - *"Diferencia entre cremas hidratantes y reparadoras"* (destacando *Luna* como opción accesible).
- **FAQs en Stories/Reels**:
  - *"¿Puedo usar *Sol* si tengo piel grasa?"* (con respuesta + testimonio de cliente).
  - *"¿Cuánto tarda en hacer efecto *Aurora*?"* (ej: *"En 2 semanas, el 80% de nuestras usuarias notan piel más luminosa"*).

**Ejemplo para diferenciarte**:
- *Skin Lab* usa lenguaje técnico; tú podrías hacer lo mismo **pero con un toque cercano**:
  *"Explicado fácil: ¿Qué es el retinol y por qué *Aurora* lo incluye en su fórmula suave?"* (con animación sencilla).

---

### **2. Contenido de "Prueba Social" (Testimonios y UGC)**
**Objetivo**: Generar confianza con experiencias reales.
**Formatos**:
- **Antes/Después**:
  - Fotos o videos de clientes bogotanos usando *Aurora* o *Luna* (ej: *"Así lucía mi piel antes y después de 1 mes con *Luna*"*).
  - *Pro tip*: Usa un formato tipo *"POV"* (Point of View) en TikTok/Reels (ej: *"POV: Usas *Aurora* todos los días"*).
- **Testimonios en video**:
  - *"Por qué elegí *Sol* sobre otros maquillajes naturales"* (ideal para competir con *Botica Verde*).
  - *"Mi rutina nocturna con *Aurora*: resultados en 30 días"* (colabora con influencers).
- **User-Generated Content (UGC)**:
  - Crea un hashtag como **#MiRutina[TuMarca]** y repostea lo mejor.
  - *Ejemplo de llamado a acción*: *"Etiquétanos usando *Luna* y gana un kit *Aurora*!"*.

**Ejemplo para *Luna* (precio entrada)**:
- *"Así me siento usando *Luna* a diario: piel hidratada sin gastar mucho"* (ideal para atraer a clientes que dudan por el precio).

---

### **3. Contenido de "Cómo Usar" (Demostraciones Prácticas)**
**Objetivo**: Mostrar el producto en acción y destacar su facilidad de uso.
**Formatos**:
- **Tutoriales rápidos**:
  - *"Cómo aplicar el kit *Sol* en 60 segundos"* (ideal para bogotanas con poco tiempo).
  - *"Rutina de 5 minutos con *Aurora* para pieles cansadas"* (para competir con *Skin Lab*).
- **Demostraciones de ingredientes**:
  - *"Así se elabora *Luna*: del aceite de coco a tu crema"* (BTS que humaniza tu marca).
- **Comparativas**:
  - *"*Sol* vs. maquillaje convencional: ¿Cuál dura más?"* (con prueba en tiempo real).

**Ejemplo para *Aurora***:
- *"Cómo integrar *Aurora* en tu rutina de spa en casa"* (posiciona como un ritual premium).

---

### **4. Contenido Emocional (Storytelling)**
**Objetivo**: Conectar con valores (naturalidad, autenticidad, empoderamiento).
**Formatos**:
- **Historias detrás de los productos**:
  - *"El origen de *Luna*: por qué creamos una crema para pieles que merecen cuidado sin lujos"* (enfocado en accesibilidad).
  - *"Aurora nació para mujeres que buscan lujo sin químicos agresivos"* (para diferenciarte de *Skin Lab*).
- **Contenido inspirador**:
  - *"Belleza natural no es solo lo que pones en tu piel, sino cómo te sientes"* (con fotos de clientes usando *Sol*).
  - *"Por qué elegimos ingredientes 100% naturales para *Aurora*"* (con fotos de proveedores locales).
- **Desafíos o retos**:
  - *"Desafío 7 días sin maquillaje: usa solo *Sol* y cuéntanos"* (ideal para TikTok).

**Ejemplo para Bogotá**:
- *"Cómo adaptamos *Luna* para resistir el polvo y la humedad de Bogotá"* (enfoque local).

---

### **5. Contenido de Tendencias y Tendencias Locales**
**Objetivo**: Aprovechar el momento y posicionarte como relevante.
**Formatos**:
- **Tendencias de skincare**:
  - *"El 'skin cycling' y cómo hacerlo con *Aurora* y *Luna*"*.
  - *"Por qué el 'clean beauty' es más que una moda"* (con tus productos como ejemplo).
- **Tendencias bogotanas**:
  - *"Los productos de belleza que las bogotanas están probando en 2024"* (incluyendo tus productos).
  - *"Cómo llevar maquillaje natural al trabajo en Bogotá"* (con *Sol*).
- **Colaboraciones con tendencias**:
  - Participa en desafíos como *"Get Ready With Me para un día en el Parque 93"* usando *Sol*.

---

### **6. Contenido de "Behind the Scenes" (BTS)**
**Objetivo**: Humanizar la marca y mostrar transparencia.
**Formatos**:
- **Proceso de creación**:
  - *"Así se formula *Aurora*: de la idea al producto final"* (video en laboratorio).
  - *"Un día en la vida de [Tu Nombre]: cómo elegimos ingredientes para *Luna*"*.
- **Equipo o aliados**:
  - *"Conoce a los dermatólogos que revisan nuestras fórmulas"* (para competir con *Skin Lab*).
  - *"Nuestros proveedores de ingredientes naturales en Colombia"* (enfoque local).

---

### **7. Contenido Promocional (Pero con Valor)**
**Objetivo**: Impulsar ventas sin sonar spam.
**Formatos**:
- **Ofertas con historia**:
  - *"Por qué *Luna* está 20% de descuento esta semana"* (ej: *"Celebramos 100 clientes bogotanos"*).
- **Packaging creativo**:
  - *"Descubre el nuevo envase de *Aurora*: diseñado para durar"* (video mostrando detalles).
- **Limited editions**:
  - *"Edición especial de *Sol* para el Día de la Mujer"* (con diseño único).

---

### **8. Contenido Interactivo**
**Objetivo**: Aumentar engagement y datos de tu audiencia.
**Formatos**:
- **Encuestas en Stories**:
  - *"¿Prefieres cremas con o sin fragancia?"* (para segmentar a clientes).
  - *"¿Qué producto te gustaría que lanzáramos después?"* (*Luna* para hombres, *Aurora* en mini).
- **Preguntas y respuestas**:
  - *"Pregúntame sobre skincare y te respondo en Stories"* (ideal para posicionarte como experta).
- **Quizzes**:
  - *"¿Qué producto de [Tu Tienda] es perfecto para ti?"* (con resultados personalizados).

---

### **Ejemplos Específicos por Producto**
| **Producto** | **Tipo de Contenido que Funciona**                          | **Ejemplo de Post**                                                                 |
|--------------|----------------------------------------------------------------|------------------------------------------------------------------------------------|
| **Aurora**   | Contenido premium, rutinas de lujo, BTS de ingredientes.      | *"Rutina nocturna de 10 minutos con *Aurora* para pieles maduras"* (Reel).         |
|              | Comparativas con *Skin Lab*.                                  | *"Aurora vs. Skin Lab: ¿Cuál elige una dermatóloga bogotana?"* (video).              |
| **Sol**      | Tutoriales rápidos, maquillaje natural para oficina.          | *"Cómo aplicar *Sol* en 2 minutos para ir a trabajar"* (TikTok).                  |
|              | Testimonios de mujeres ocupadas.                             | *"Usé *Sol* por 1 mes: esto cambió"* (testimonio en Instagram).                   |
| **Luna**     | Contenido accesible, antes/después, tips de hidratación.      | *"Así lucía mi piel seca antes y después de *Luna*"* (Stories con fotos).          |
|              | Promociones para primerizos.                                 | *"Luna: la crema que todas en Bogotá merecen probar"* (email + Instagram).         |

---

### **¿Qué Evitar?**
1. **Contenido demasiado técnico** (a menos que sea para *Aurora*): Usa lenguaje sencillo para *Sol* y *Luna*.
2. **Sobreprometer resultados**: Enfócate en *"transparencia"* (ej: *"Puede tardar 4 semanas en ver cambios"*).
3. **Ignorar el humor**: En TikTok/Reels, usa memes o tonos ligeros para productos como *Sol* (ej: *"Cuando tu jefe te dice 'sin maquillaje' pero quieres lucir fresca"*).
4. **No adaptarte a tendencias locales**: Ejemplo: Si en Bogotá hay un *trending topic* como *"skincare para el sol fuerte"*, haz contenido al respecto.

---
### **Plan de Contenido Semanal Ejemplo**
| **Día**   | **Instagram**                          | **TikTok**                              | **Facebook**                          |
|-----------|----------------------------------------|----------------------------------------|---------------------------------------|
| **Lunes** | Reel: *"Cómo usar *Sol* para piel grasa"* | Video: *"POV: Usas *Aurora* en la mañana"* | Publicación: *"Ingredientes clave en *Luna*"* (infografía). |
| **Miércoles** | Story: Encuesta *"¿Qué producto probar primero?"* | Tutorial: *"Rutina de 5 min con *Aurora*"* | Video largo: *"Mitologias del skincare"*. |
| **Viernes** | Post: Testimonio de cliente con *Luna* | Desafío: *"7 días sin maquillaje con *Sol*"* | Promoción: *"Oferta del fin de semana"*. |
| **Domingo** | Carousel: *"Antes/después con *Aurora*"* | BTS: *"Así se empaqueta *Luna*"* | Story: *"Pregúntame sobre skincare"*. |

---
### **Herramientas Recomendadas para Crear Contenido**
1. **Edición**:
   - *CapCut* (gratis, ideal para Reels/TikTok).
   - *Canva* (plantillas para Stories y posts).
2. **Grabación**:
   - *InShot* (para videos rápidos con música).
   - *Ring Light* económico (ej: *Neewer 10"* para mejor calidad).
3. **Automatización**:
   - *Later* o *Planoly* (para programar posts en Instagram).
   - *ManyChat* (para responder mensajes en WhatsApp automáticamente).

---
**Pregunta para ti**:
- ¿Quieres que desarrolle **guiones específicos** para algunos de estos contenidos? Por ejemplo, el script exacto para un Reel de *"Cómo usar *Sol* en 2 minutos"* o un TikTok de *"Aurora vs. Skin Lab"*.
- ¿O prefieres priorizar **un tipo de contenido** (ej: solo testimonios o solo educación) para empezar?

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Para diferenciarte de **Botica Verde** (enfoque masivo/organic) y **Skin Lab** (enfoque clínico/premium) **sin bajar precios ni entrar en guerra comercial**, debes construir una **propuesta única** basada en **3 pilares**:
1. **Experiencia de marca** (cómo te perciben emocionalmente).
2. **Diferenciación por producto** (qué ofrece cada uno de tus productos que ellos no).
3. **Conexión local** (aprovechar el contexto bogotano para crear lealtad).

Aquí tienes una estrategia **detallada y accionable**, con ejemplos específicos para cada uno de tus productos (*Aurora*, *Sol*, *Luna*) y canales:

---

### **1. Experiencia de Marca: "Belleza Consciente con Alma Colombiana"**
**Objetivo**: Posicionarte como una marca que **cuidar la piel + el planeta + la comunidad**, sin caer en el genérico "100% natural".

#### **A. Storytelling Auténtico**
**¿Cómo?**
- **Enfoca tus historias en**:
  - **Origen de los ingredientes**: Ejemplo:
    *"El aceite de argán de *Aurora* viene de cooperativas en Boyacá, donde cada litro genera empleo para 5 familias"* (muestra fotos reales de los proveedores).
    *vs. Botica Verde*: Si ellos compran ingredientes al por mayor, tú destacas **relaciones directas**.
  - **Impacto local**: Ejemplo:
    *"Por cada *Luna* vendida, donamos una crema a una mujer en situación de vulnerabilidad en Bogotá"* (colabora con ONGs como *Fundación Saldarriaga Concha*).
    *vs. Skin Lab*: Ellos venden ciencia; tú vendes **ciencia + corazón**.

**Contenido para implementar**:
- **Instagram/TikTok**:
  - Video: *"Conoce a María, la productora de aceite de coco de *Luna*"* (entrevista corta en su finca).
  - Reel: *"Así apoyamos a los agricultores de ingredientes naturales"* (timelapse de envíos).
- **Packaging**:
  - Incluye un código QR en tus productos que lleve a una página con la historia de cada ingrediente (ej: *"Este aloe vera es cultivado por..."*).
  - *Diferencial*: *Botica Verde* puede tener ingredientes orgánicos, pero no necesariamente **historias humanas detrás**.

---

#### **B. Ritual, no solo Producto**
**¿Cómo?**
Transforma el uso de tus productos en una **experiencia sensorial y emocional**, especialmente para *Aurora* (premium) y *Sol* (maquillaje).

**Ejemplos**:
- **Aurora**:
  - *"Ritual de Luna Llena"*:
    - Guía en tu newsletter: *"Cómo usar *Aurora* en una noche de spa en casa"* (con música relajante, velas y pasos detallados).
    - *vs. Skin Lab*: Ellos venden resultados clínicos; tú vendes **un momento de autocuidado**.
  - Contenido:
    - TikTok: *"Mi rutina nocturna con *Aurora*: masaje, mascarilla y sueño profundo"* (con sonidos ASMR).
    - Instagram: Carousel con fotos de clientes usando el producto en su "ritual".
- **Sol**:
  - *"Maquillaje que respeta tu piel y tu tiempo"*:
    - Tutoriales rápidos: *"Cómo aplicar *Sol* en 90 segundos para ir a trabajar"* (ideal para bogotanas ocupadas).
    - *vs. Botica Verde*: Ellos pueden ser naturales, pero no necesariamente **prácticos para el día a día**.

**Lenguaje clave**:
- Usa palabras como *"ritual"*, *"momento"*, *"conexión"* en lugar de *"producto"* o *"fórmula"*.
- Ejemplo de caption: *"No es solo una crema, es tu momento de paz en medio del caos bogotano"* (para *Luna*).

---

### **2. Diferenciación por Producto**
**Estrategia**: Enfócate en **lo que cada producto ofrece que tus competidores no pueden (o no quieren) replicar fácilmente**.

| **Producto** | **Diferenciador Clave**                          | **Cómo Comunicarlo**                                                                 | **Ejemplo de Contenido**                                                                 |
|--------------|--------------------------------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Aurora**   | **Lujoso pero accesible en experiencia** (no en precio). | - Enfócate en la **experiencia sensorial** (texturas, aromas) y el **ritual**. <br> - Destaca ingredientes **premium pero naturales** (ej: oro coloidal, aceites raros). <br> - *vs. Skin Lab*: Ellos son clínicos; tú eres **"spa en casa"**. | - Reel: *"La textura de *Aurora* vs. otras cremas premium"* (con close-ups). <br> - Email: *"Los 3 ingredientes secretos de *Aurora* que no encontrarás en otras marcas"*. |
| **Sol**      | **Maquillaje natural para mujeres reales** (no solo "eco-friendly"). | - Enfócate en **prácticidad** (fácil de aplicar, dura todo el día, sin efecto "máscara"). <br> - *vs. Botica Verde*: Ellos son genéricos; tú eres **"maquillaje natural que funciona en Bogotá"**. <br> - Usa testimonios de mujeres con pieles sensibles o alergias. | - TikTok: *"Llevo 5 horas usando *Sol* y mi piel no está irritada"* (prueba en tiempo real). <br> - Instagram: *"Antes y después de usar *Sol* en piel grasa"*. |
| **Luna**     | **Hidratación profunda para pieles que merecen cuidado sin gastar mucho**. | - Enfócate en **resultados visibles** (piel suave, sin grietas) y **precio justo**. <br> - *vs. Competencia*: *Botica Verde* puede ser barata, pero no necesariamente **tan hidratante**; *Skin Lab* es cara. <br> - Usa el eslogan: *"El lujo de hidratarte bien, sin pagar de más"*. | - Story: *"Así se siente usar *Luna* vs. una crema económica"* (test de texturas). <br> - Post: *"Por qué *Luna* es la crema favorita de las bogotanas que trabajan 12 horas"*. |

---

### **3. Conexión Local: "Bogotá es Nuestra Inspiración"**
**Objetivo**: Crear un **vínculo emocional** con tu mercado objetivo usando elementos únicos de la ciudad.

#### **A. Contenido Hiperlocal**
**Ideas**:
- **"Belleza adaptada a Bogotá"**:
  - *"Cómo cuidar tu piel del polvo y la humedad de la ciudad"* (con tips usando *Luna* y *Aurora*).
  - *"Productos para sobrevivir al sol bogotano"* (destacando SPF en *Sol*).
- **Colaboraciones con lugares icónicos**:
  - *"Nuestra rutina de skincare en el Parque 93"* (fotos con el skyline de Bogotá).
  - *"Desayuno saludable + *Sol*: así lucen las influencers bogotanas"* (en un café como *Papaya Café*).
- **Eventos virtuales o presenciales**:
  - *"Taller gratuito: Skincare para pieles bogotanas"* (en vivo por Instagram o en un espacio como *La Tertulia*).
  - *"Sorteo de *Aurora*: Gana un kit si etiquetas a 3 amigas bogotanas"*.

**Ejemplo de post**:
*"En Bogotá, el sol, el polvo y el estrés se notan en la piel. Por eso *Luna* fue creada para hidratar **a fondo** y resistir tu día a día. ¿Ya la probaste?"* (con foto de una bogotana usando el producto en la calle).

---

#### **B. Lenguaje y Referencias Locales**
- **Usa modismos bogotanos** en captions o videos:
  - *"¡Pa’ que te vean, pero sin ahogar tu piel!"* (para *Sol*).
  - *"Esto sí es *chévere*: piel suave sin gastar fortuna"* (para *Luna*).
- **Referencias culturales**:
  - *"Tu piel merece un *cafecito* de hidratación"* (para *Aurora*).
  - *"Como el metro de Bogotá: *Luna* llega a donde otras cremas no llegan"* (para resaltar penetración).

---

#### **C. Packaging con Toque Local**
- **Detalles que hagan sentir a los bogotanos especiales**:
  - Incluye un **mapa ilustrado de Bogotá** en el empaque de *Luna* (ej: *"Hecho con amor para ti, bogotana"*).
  - Usa **colores inspirados en la ciudad**: verdes de Chapinero, morados de La Candelaria, o dorados para *Aurora*.
  - **Frase en criollo**: Ejemplo en la caja de *Sol*: *"Pa’ que luzcas natural, pero *pa’ dentro*"*.

---

### **4. Estrategias de Precio (Sin Guerra Comercial)**
**Objetivo**: Justificar tus precios sin competir directamente.

| **Producto** | **Estrategia**                                                                 | **Ejemplo de Mensaje**                                                                 |
|--------------|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| **Aurora**   | **Premium por experiencia, no solo ingredientes**.                           | *"No es lo más barato, pero es la inversión que tu piel merece. ¿Cuánto vale tu tiempo de autocuidado?"* <br> - Enfócate en **ritual**, **ingredientes raros** (ej: aceite de rosa de Damasco) y **resultados a largo plazo**. |
| **Sol**      | **Precio medio = valor por durabilidad y naturalidad**.                       | *"Pagas menos que un maquillaje convencional, pero ganas piel sana y sin químicos agresivos. ¿Vale la pena?"* <br> - Compara con marcas como *MAC* o *Maybelline* (ej: *"Un frasco de *Sol* dura 3 meses vs. 1 de maquillaje tradicional"*). |
| **Luna**     | **Precio entrada = mejor relación calidad-precio**.                          | *"Es la crema más hidratante que probaste, y cuesta menos que un café en Bogotá"* (ej: $25,000 vs. $5,000 de otras marcas económicas). <br> - Usa testimonios: *"Pagué $50,000 en cremas baratas y ninguna hidrataba como *Luna*"*. |

---

### **5. Canales para Implementar la Diferenciación**
| **Canal**       | **Tipo de Contenido**                          | **Ejemplo Específico**                                                                 |
|------------------|-----------------------------------------------|---------------------------------------------------------------------------------------|
| **Instagram**    | Carrousels, Reels, Stories interactivos.       | - *"Bogotá vs. Nueva York: ¿Cómo cuida tu piel el clima?"* (con tips para *Aurora*). <br> - *"El mito de que el maquillaje natural no dura"* (prueba con *Sol* en un día de trabajo). |
| **TikTok**       | Videos cortos, desafíos, BTS.                 | - *"POV: Usas *Luna* y tu piel ya no se ve seca en el metro"* (humor local). <br> - *"Así suena el packaging de *Aurora* al abrirlo"* (ASMR). |
| **Email**        | Guías descargables, historias de ingredientes. | - *"La historia del aceite de argán de *Aurora*: de Boyacá a tu piel"* (con fotos). <br> - *"Rutina de skincare para sobrevivir al tráfico bogotano"*. |
| **WhatsApp**     | Mensajes personalizados, promociones exclusivas. | - *"Hola [Nombre], como bogotana, sabemos que tu piel necesita extra hidratación. Aquí tienes 10% en *Luna* por ser de aquí"* (código BOGOTA10). |
| **Facebook**     | Videos largos, grupos locales.                | - *"Live: Cómo adaptar tu skincare al clima de Bogotá"* (con dermatóloga local). <br> - Publicación en grupos: *"¿Sabías que *Sol* es el maquillaje natural favorito de las mujeres en Chapinero?"* (con encuesta). |

---

### **6. Ejemplo de Campaña Integrada (1 Mes)**
**Tema**: *"Belleza que Respeta: Tu Piel y Bogotá"*
**Objetivo**: Posicionarte como la marca **natural, local y real** para bogotanas ocupadas.

| **Semana** | **Acciones**                                                                 | **Canales**                          | **KPI**                          |
|------------|-----------------------------------------------------------------------------|--------------------------------------|----------------------------------|
| **1**      | - Lanzar guía *"Skincare para el Clima de Bogotá"* (email + Instagram). <br> - Reel: *"Cómo usar *Sol* en un día de trabajo en Bogotá"*. <br> - Story: Encuesta *"¿Qué problema de piel te quita el sueño?"*. | Email, IG, TikTok.               | 500 descargas de la guía.        |
| **2**      | - TikTok: *"POV: Usas *Luna* y tu piel ya no se ve seca en el SITP"*. <br> - Colaboración con influencer bogotana para probar *Aurora*. <br> - Post: *"Los ingredientes de *Aurora* que no encontrarás en Skin Lab"*. | TikTok, IG, Instagram Stories.   | 3K visualizaciones en TikTok.     |
| **3**      | - Live en Facebook: *"Taller de Rituales de Belleza con *Aurora*"*. <br> - Story: *"Etiqueta a una amiga y gana *Luna*"*. <br> - Email: *"Testimonio de María, usuaria de *Sol* desde hace 3 meses"*. | FB Live, IG, Email.              | 200 participantes en el Live.    |
| **4**      | - Sorteo: *"Gana un kit *Aurora* si etiquetas a 3 amigas bogotanas"*. <br> - Reel: *"Antes/después de usar *Luna* 1 mes"*. <br> - Post: *"Por qué *Sol* es el maquillaje natural que todas en Bogotá merecen"*. | IG, TikTok, WhatsApp.            | 500 etiquetas en el sorteo.       |

---

### **7. ¿Qué NO Hacer?**
- **❌ Comparar precios directamente**: Ejemplo mal: *"Skin Lab cuesta $200,000 y *Aurora* solo $150,000"*.
  - **✅ Mejor**: *"Skin Lab es para laboratorios; *Aurora* es para tu ritual de spa en casa"*.
- **❌ Copiar el tono de tus competidores**:
  - *Botica Verde*: Genérico ("100% natural").
  - *Skin Lab*: Técnico ("con retinol").
  - **Tú**: **Emocional + local** ("para pieles bogotanas que merecen cuidarse sin complicaciones").
- **❌ Ignorar el servicio post-venta**:
  - Ofrece **respuestas rápidas en WhatsApp** (ej: *"Hola [Nombre], ¿cómo está tu piel con *Luna*? ¿Necesitas tips?"*).
  - Crea un **club de fidelidad** para clientes bogotanos (ej: *"Club Aurora": beneficios exclusivos en la ciudad*).

---

### **Resumen de Diferenciadores Clave**
| **Competidor** | **Su Enfoque**               | **Tu Diferenciador**                                                                 | **Cómo Comunicarlo**                                                                 |
|-----------------|------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **Botica Verde** | Natural masivo, genérico.   | **Belleza natural con alma colombiana y ritual**.                                    | Historias de ingredientes locales, packaging con toque bogotano, lenguaje criollo. |
| **Skin Lab**    | Clínico, premium.            | **Lujoso en experiencia, no en precio; enfocado en emociones**.                     | Rituales de spa en casa, testimonios de transformación, contenido sensorial.         |

---
**Pregunta para ti**:
- ¿Quieres que desarrolle **guiones específicos** para los primeros 3 posts de esta estrategia (ej: el Reel de *"Cómo usar Sol en un día de trabajo"* o el email de la guía para Bogotá)?
- ¿O prefieres enfocarnos en **algo más específico**, como cómo estructurar el "club de fidelidad" para clientes bogotanos?

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Para tu tienda online en Bogotá, con productos de skincare segmentados (*Aurora* premium, *Sol* medio, *Luna* entrada), los **KPIs del primer trimestre** deben enfocarse en:
1. **Validar tu propuesta de valor** (¿los bogotanos responden a tu diferenciación?).
2. **Optimizar conversiones** (desde tráfico hasta ventas).
3. **Medir engagement en canales clave** (Instagram, TikTok, WhatsApp).
4. **Entender el comportamiento de compra** (qué producto vende más, desde dónde, etc.).

Aquí tienes una **lista priorizada de KPIs**, cómo medirlos y qué acciones tomar basados en los resultados. Todo alineado a tu contexto (mercado local, competencia, productos).

---

### **1. KPIs de Tráfico y Alcance (Canales Digitales)**
**Objetivo**: Saber si estás llegando al público correcto en Bogotá.

| **KPI**                     | **Cómo Medirlo**                          | **Herramienta**               | **Meta Realista (Primer Trimestre)** | **Acción si No Cumples**                          |
|-----------------------------|-------------------------------------------|--------------------------------|--------------------------------------|----------------------------------------------------|
| **Visitas al sitio web**     | Total de visitas (orgánico + pago).      | Google Analytics              | 5,000 visitas/mes                   | Aumentar presupuesto en Google Ads o colaborar con influencers bogotanos. |
| **Tráfico por ciudad**      | % de visitas desde Bogotá.                | Google Analytics (Geolocalización) | 80% desde Bogotá.                  | Optimizar anuncios para geolocalización Bogotá o ajustar SEO local (ej: *"maquillaje natural Bogotá"*). |
| **Tráfico por dispositivo** | % de visitas desde móvil.                 | Google Analytics              | 90% desde móvil (Colombia es móvil-first). | Mejorar velocidad de carga en móvil o hacer pruebas A/B en el diseño responsive. |
| **Fuentes de tráfico**       | % de tráfico orgánico, social, pago.     | Google Analytics              | 40% orgánico, 30% social, 20% pago.  | Si social es bajo, aumentar frecuencia en Instagram/TikTok. Si pago es bajo, ajustar segmentación en ads. |
| **Seguidores en redes**      | Crecimiento en Instagram, TikTok, FB.     | Insights de cada plataforma.   | +2,000 seguidores en IG, +1,500 en TikTok. | Publicar contenido interactivo (encuestas, desafíos) o hacer colaboraciones con microinfluencers bogotanos. |

---

### **2. KPIs de Engagement (Redes Sociales)**
**Objetivo**: Medir si tu contenido conecta emocionalmente con el público bogotano.

| **KPI**                     | **Cómo Medirlo**                          | **Herramienta**               | **Meta Realista**                          | **Acción si No Cumples**                          |
|-----------------------------|-------------------------------------------|--------------------------------|--------------------------------------------|----------------------------------------------------|
| **Tasa de engagement**      | (Likes + Comentarios + Shares) / Seguidores. | Insights (IG, TikTok).       | 5-8% en IG, 7-10% en TikTok.              | Crear contenido más interactivo (preguntas, encuestas, desafíos). |
| **Guardados (Saves)**       | % de usuarios que guardan tus Reels/Stories. | Insights (IG, TikTok).       | 3-5% de alcance.                          | Enfocarte en contenido educativo (tutoriales, guías) que la gente quiera guardar. |
| **Comentarios significativos** | Comentarios que generen conversación (no solo "¡Qué bonito!"). | Insights.                    | 10-15 comentarios por post en IG.          | Hacer preguntas abiertas o usar Stories para fomentar diálogos. |
| **Tasa de compartidos**     | % de usuarios que comparten tu contenido. | Insights.                    | 2-4% en IG, 3-5% en TikTok.               | Crear contenido emocional o viral (ej: *"POV: Usas *Sol* en el metro"* con humor bogotano). |
| **Tasa de finalización de videos** | % de usuarios que ven tus Reels/TikToks completos. | Insights.                    | 60-70%.                                  | Empezar videos con ganchos fuertes (ej: *"Esto pasa si usas maquillaje convencional"* vs. *"Sol"*). |

---

### **3. KPIs de Conversión (Del Tráfico a Ventas)**
**Objetivo**: Optimizar el embudo de ventas (desde que llegan a tu sitio hasta que compran).

| **KPI**                     | **Cómo Medirlo**                          | **Herramienta**               | **Meta Realista**                          | **Acción si No Cumples**                          |
|-----------------------------|-------------------------------------------|--------------------------------|--------------------------------------------|----------------------------------------------------|
| **Tasa de conversión del sitio** | % de visitantes que compran.            | Google Analytics + Shopify.   | 2-3%.                                     | Optimizar landing pages (ej: añadir testimonios de bogotanos o videos de productos). |
| **Tasa de abandono de carrito** | % de usuarios que abandonan el carrito. | Google Analytics / Shopify.   | <70%.                                     | Enviar emails de recordatorio o ofrecer descuento en WhatsApp (ej: *"Olvidaste tu *Luna*? 10% de descuento con código BOGOTA10"*). |
| **Valor promedio del pedido (AOV)** | Ingresos totales / Número de pedidos.   | Shopify / Google Analytics.   | $80,000 - $100,000 COP.                   | Promover upselling (ej: *"Añade *Aurora* a tu *Luna* y obtén 15% de descuento"*). |
| **Productos más vendidos**   | Ventas por SKU.                           | Shopify Reports.              | *Luna* (entrada) > *Sol* (medio) > *Aurora* (premium). | Si *Aurora* vende poco, hacer packs (ej: *"Kit Bogotá": *Luna* + *Sol* + descuento*). |
| **Tráfico a producto específico** | Visitas a páginas de producto.       | Google Analytics.             | 30% del tráfico va a *Luna*, 25% a *Sol*, 15% a *Aurora*. | Si *Aurora* tiene poco tráfico, hacer contenido premium (ej: *"Por qué *Aurora* es la mejor inversión para tu piel"* en email). |

---

### **4. KPIs de Ventas y Rentabilidad**
**Objetivo**: Validar si tu modelo de precios y diferenciación funciona.

| **KPI**                     | **Cómo Medirlo**                          | **Herramienta**               | **Meta Realista**                          | **Acción si No Cumples**                          |
|-----------------------------|-------------------------------------------|--------------------------------|--------------------------------------------|----------------------------------------------------|
| **Ingresos por producto**   | Ventas totales por *Aurora*, *Sol*, *Luna*. | Shopify.                     | *Luna*: 40% de ingresos, *Sol*: 35%, *Aurora*: 25%. | Si *Aurora* vende poco, hacer promociones tipo *"Prueba *Aurora* por $X"* o bundles. |
| **Costo de adquisición por cliente (CAC)** | Gasto en ads / Nuevos clientes.      | Google Ads + Shopify.         | <$15,000 COP por cliente.                  | Optimizar segmentación en ads (ej: enfocarse en mujeres 25-40 años en Bogotá). |
| **Tasa de retención**       | % de clientes que compran nuevamente.    | Shopify (clientes recurrentes). | 20-25% de clientes compran 2 veces en 3 meses. | Implementar programa de fidelidad (ej: *"Club Aurora": puntos por compras*). |
| **Margen por producto**     | (Precio de venta - Costo) / Precio de venta. | Excel / Contabilidad.         | *Luna*: 60%, *Sol*: 50%, *Aurora*: 40%.   | Si un producto tiene bajo margen, evaluar si es por costos de producción o marketing. |
| **ROAS (Retorno de Inversión en Publicidad)** | Ingresos por ads / Gasto en ads. | Google Ads / Meta Ads.        | 3:1 (por cada $1 en ads, $3 en ventas).   | Si ROAS es bajo, probar nuevos creativos o audiencias (ej: *"Mujeres en Bogotá interesadas en skincare natural"*). |

---

### **5. KPIs de Experiencia del Cliente (Post-Venta)**
**Objetivo**: Medir satisfacción y lealtad en Bogotá.

| **KPI**                     | **Cómo Medirlo**                          | **Herramienta**               | **Meta Realista**                          | **Acción si No Cumples**                          |
|-----------------------------|-------------------------------------------|--------------------------------|--------------------------------------------|----------------------------------------------------|
| **Tasa de reseñas positivas** | % de reseñas 5 estrellas en Shopify/Google. | Shopify / Google My Business. | 80% de reseñas positivas.                 | Pedir reseñas automáticamente después de la compra (email o WhatsApp). |
| **Tiempo de respuesta en WhatsApp** | Tiempo promedio de respuesta a clientes. | WhatsApp Business.            | <2 horas en días hábiles.                 | Automatizar respuestas rápidas (ej: *"Hola [Nombre], gracias por contactarnos. Te respondemos en 1 hora"*). |
| **Tasa de devoluciones**    | % de productos devueltos.                | Shopify.                     | <5%.                                      | Mejorar descripciones de productos o añadir videos tutoriales de uso. |
| **NPS (Net Promoter Score)** | ¿Recomendarías [Tu Tienda] a un amigo? (Escala 0-10). | Encuesta en email/WhatsApp.   | NPS > 50 (promedio en e-commerce es 30).   | Enviar encuesta post-compra: *"¿Nos recomendarías en Bogotá? (0-10)"*. |

---

### **6. KPIs de Redes Sociales Específicos para Bogotá**
**Objetivo**: Validar si tu enfoque local está funcionando.

| **KPI**                     | **Cómo Medirlo**                          | **Herramienta**               | **Meta Realista**                          | **Acción si No Cumples**                          |
|-----------------------------|-------------------------------------------|--------------------------------|--------------------------------------------|----------------------------------------------------|
| **Hashtags locales**        | Uso de hashtags como #BellezaBogota o #SkincareColombia. | Insights (IG, TikTok).       | 50% de posts usan hashtags locales.         | Crear un hashtag propio (ej: #MiRutina[TuMarca]) y animar a clientes a usarlo. |
| **Mención de barrios bogotanos** | % de clientes que mencionan su barrio (ej: *"Vivo en Chapinero"*). | Comentarios en redes o emails. | 10-15% de clientes mencionan su barrio.     | Hacer contenido hiperlocal (ej: *"Rutina de skincare para mujeres de Usaquén"*). |
| **Colaboraciones con influencers bogotanos** | Número de colaboraciones con creadores locales. | Lista de colaboraciones.      | 3-5 colaboraciones en 3 meses.             | Contactar microinfluencers de barrios como La Candelaria o Chapinero. |

---

### **7. KPIs de Email Marketing**
**Objetivo**: Medir si tu estrategia de email está generando ventas recurrentes.

| **KPI**                     | **Cómo Medirlo**                          | **Herramienta**               | **Meta Realista**                          | **Acción si No Cumples**                          |
|-----------------------------|-------------------------------------------|--------------------------------|--------------------------------------------|----------------------------------------------------|
| **Tasa de apertura**        | % de emails abiertos.                     | Mailchimp / Klick Tipp.        | 25-30%.                                   | Mejorar asunto (ej: *"Camila, tu piel en Bogotá merece esto"* vs. *"Oferta exclusiva"*). |
| **Tasa de clics (CTR)**     | % de clics en enlaces del email.          | Mailchimp.                    | 3-5%.                                     | Incluir más imágenes y botones de llamada a la acción (CTA). |
| **Conversiones por email**  | Ventas generadas desde emails.            | Shopify + UTM en enlaces.     | 1-2% de aperturas generan ventas.          | Enviar emails con historias de clientes (ej: *"Así cambió la piel de Ana con *Luna*"*). |

---

### **8. KPIs de WhatsApp Business**
**Objetivo**: Medir si el canal de atención está generando ventas.

| **KPI**                     | **Cómo Medirlo**                          | **Herramienta**               | **Meta Realista**                          | **Acción si No Cumples**                          |
|-----------------------------|-------------------------------------------|--------------------------------|--------------------------------------------|----------------------------------------------------|
| **Mensajes recibidos**      | Total de mensajes en WhatsApp.            | WhatsApp Business.            | 50-100 mensajes/mes.                      | Promocionar WhatsApp como canal de atención (ej: *"Escríbenos por WhatsApp y te ayudamos a elegir"* en redes). |
| **Tasa de respuesta**       | % de mensajes respondidos en <24 horas.   | WhatsApp Business.            | 90%.                                      | Automatizar respuestas rápidas o contratar un asistente virtual. |
| **Ventas por WhatsApp**     | Ventas generadas desde conversaciones.    | Shopify (notas de pedido).    | 10-15% de ventas totales.                 | Enviar catálogos interactivos (ej: *"Haz clic en el producto que quieres"* con emojis). |

---

### **Dashboard de KPIs Recomendado (Primer Trimestre)**
| **Área**               | **KPI Clave**                          | **Meta**                     | **Herramienta**          |
|------------------------|----------------------------------------|------------------------------|--------------------------|
| **Tráfico**            | Visitas desde Bogotá.                  | 80% de tráfico.              | Google Analytics.        |
| **Engagement**         | Tasa de guardados en IG/TikTok.        | 3-5%.                       | Insights.                |
| **Conversión**         | Tasa de conversión del sitio.          | 2-3%.                       | Google Analytics.        |
| **Ventas**             | Ingresos por *Luna*, *Sol*, *Aurora*. | *Luna*: 40%, *Sol*: 35%.    | Shopify.                 |
| **Redes Sociales**     | Crecimiento de seguidores en IG.       | +2,000 seguidores.           | Insights.                |
| **Email Marketing**    | Tasa de apertura.                      | 25-30%.                      | Mailchimp.               |
| **WhatsApp**           | Mensajes respondidos en <24h.          | 90%.                        | WhatsApp Business.       |
| **Experiencia Cliente**| Reseñas positivas.                    | 80% 5 estrellas.             | Shopify.                 |

---

### **Acciones Basadas en Resultados (Ejemplos)**
1. **Si el tráfico desde Bogotá es <70%**:
   - Ajustar anuncios de Google/Facebook para geolocalización exclusiva en Bogotá.
   - Crear contenido con hashtags como *#BellezaBogota* o *#SkincareColombia*.

2. **Si la tasa de conversión es <2%**:
   - Añadir testimonios de bogotanas en la página de productos.
   - Ofrecer envío gratis en Bogotá (aunque sea simbólico, ej: *"Envío gratis en Bogotá para pedidos >$50,000"*).

3. **Si *Aurora* vende poco**:
   - Crear un pack *"Kit Bogotá"* (*Luna* + *Sol* + *Aurora* con descuento).
   - Hacer un video comparativo: *"Aurora vs. Skin Lab: ¿Cuál elige una dermatóloga bogotana?"*.

4. **Si el engagement en TikTok es bajo**:
   - Participar en desafíos virales locales (ej: *"GRWM para un día en el Parque 93"*).
   - Usar sonidos trending con tu producto (ej: *"Así se siente usar *Luna* después de un día de sol bogotano"*).

5. **Si el CAC es alto (>$20,000 COP)**:
   - Enfocarse en retargeting (anuncios a quienes visitaron tu sitio pero no compraron).
   - Ofrecer descuentos en WhatsApp para clientes potenciales (ej: *"Hola [Nombre], como visitante, aquí tienes 10% en *Luna*"*).

---

### **Herramientas Recomendadas para Medir KPIs**
1. **Google Analytics 4**: Tráfico, conversiones, comportamiento en el sitio.
2. **Shopify Reports**: Ventas, productos más vendidos, tasa de abandono de carrito.
3. **Meta Business Suite (Facebook/Instagram)**: Engagement, alcance, ROAS.
4. **TikTok Analytics**: Tasa de finalización de videos, guardados.
5. **Mailchimp/Klick Tipp**: Tasa de apertura, clics, conversiones por email.
6. **WhatsApp Business**: Mensajes recibidos/respondidos.
7. **Google My Business**: Reseñas y reputación local.

---
**Pregunta para ti**:
- ¿Quieres que prioricemos **3 KPIs críticos** para enfocarte en ellos los primeros 30 días? Por ejemplo:
  1. **Tasa de conversión del sitio** (para optimizar ventas).
  2. **Engagement en TikTok/Instagram** (para validar tu propuesta de valor).
  3. **Ingresos por producto** (para ajustar estrategias por SKU).
- O prefieres un **template de dashboard** en Google Sheets para llevar el seguimiento semanal.

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

### **Campaña de 4 Semanas para *Aurora*: "Ritual de Lujo para Pieles que Merecen lo Mejor"**
**Objetivo Principal**:
Posicionar *Aurora* como **el set de skincare premium para bogotanas que buscan un ritual de autocuidado exclusivo**, sin competir en precio con *Skin Lab*, sino en **experiencia sensorial y conexión emocional**. Validar si el público bogotano está dispuesto a invertir en un producto premium con enfoque en **naturalidad + ritual**, no solo resultados clínicos.

---

### **Audiencia Objetivo (Segmentación Detallada)**
**Perfil Demográfico**:
- **Edad**: 28-45 años.
- **Género**: Mujeres (y hombres que compran para sus parejas).
- **Ubicación**: Bogotá (enfocado en barrios como **Chapinero, Usaquén, La Candelaria, Suba**).
- **Nivel socioeconómico**: C2-C3 (clase media-alta bogotana).
- **Intereses**:
  - Belleza natural, skincare, wellness, yoga, spa en casa.
  - Moda sostenible, productos colombianos, autocuidado.

**Psychographics (Perfil Psicológico)**:
- Buscan **experiencias** (no solo productos).
- Valoran la **naturalidad** pero están dispuestas a pagar por calidad.
- Tienen **tiempo para rituales** (aunque sea en casa).
- Se identifican con marcas que **cuentan historias auténticas** y tienen un **toque local**.

**Competidores a Desplazar**:
- *Skin Lab*: Enfoque clínico/científico (frío).
- *Botica Verde*: Natural pero masivo (genérico).
- **Tú**: **Natural + lujo emocional + conexión bogotana**.

---

### **Mensaje Principal (Elevator Pitch)**
*"Aurora no es solo un set de skincare: es tu momento de spa en casa, con ingredientes naturales de Colombia y un ritual que transforma tu piel y tu día. Porque en Bogotá, mereces sentirte como en un resort... sin salir de tu casa."*

**Variantes por Canal**:
- **Instagram/TikTok**: *"¿Cansada de rutinas de skincare que no te hacen sentir especial? *Aurora* es tu ritual de lujo: ingredientes naturales, texturas que invitan a masajearte y resultados que se notan desde la primera semana."*
- **Email/WhatsApp**: *"Camila, tu piel es única. Por eso *Aurora* fue creado para ti: un set premium con ingredientes colombianos, diseñado para que cada noche sea un momento de autocuidado. Prueba 7 días y te devolveremos el dinero si no notas la diferencia."* (Oferta de garantía).

---

### **Estrategia de 4 Semanas**
#### **Semana 1: Lanzamiento del "Ritual Aurora" (Crear Deseo)**
**Objetivo**: Generar curiosidad y posicionar *Aurora* como un **experiencia premium**.

| **Día**  | **Acciones**                                                                 | **Canales**               | **Contenido Específico**                                                                 | **CTA (Llamado a la Acción)**                          |
|----------|-----------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------|
| **Lunes** | Publicar **Reel/TikTok**: *"¿Qué hay dentro de *Aurora*?"* (unboxing slow-motion con música relajante). | TikTok/Instagram Reels.   | Video mostrando cada producto del set (*Aurora*) con close-ups de texturas y aromas.       | *"¿Listas para tu ritual de lujo? Link en bio."*         |
| **Miércoles** | **Post en Instagram**: *"El origen de *Aurora*: ingredientes naturales de Colombia"*. | Instagram.               | Carousel con fotos de proveedores (ej: *"Este aceite de argán viene de Boyacá"*).      | *"Descubre la historia detrás de tu piel."*           |
| **Viernes** | **Live en Instagram/Facebook**: *"Q&A con la creadora de *Aurora*"*.           | Instagram Live/FB.        | Charla de 30 min sobre cómo se diseñó *Aurora* para pieles bogotanas.                   | *"Haz tu pregunta y gana un set *Aurora*."*            |
| **Domingo** | **Email**: *"Tu ritual de spa en casa empieza aquí"*.                        | Email.                    | Guía descargable: *"Cómo usar *Aurora* en 10 minutos"* + código de descuento 10%.      | *"Descarga tu guía y usa código RITUAL10."*            |

**Métricas de Éxito**:
- **Reel/TikTok**: 5,000 visualizaciones, 5% de guardados, 3% de compartidos.
- **Live**: 200 espectadores, 50 preguntas, 10 ventas durante el live.
- **Email**: Tasa de apertura >25%, CTR >3%.

---

#### **Semana 2: Prueba Social y Testimonios (Generar Confianza)**
**Objetivo**: Mostrar resultados reales y crear **prueba social** con testimonios de bogotanas.

| **Día**  | **Acciones**                                                                 | **Canales**               | **Contenido Específico**                                                                 | **CTA**                                      |
|----------|-----------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------|
| **Lunes** | **Reel/TikTok**: *"POV: Usas *Aurora* por primera vez"*.                     | TikTok/Instagram Reels.   | Video de una usuaria bogotana probando *Aurora* por primera vez (reacción de sorpresa).    | *"¿Quieres probar *Aurora*? Link en bio."*      |
| **Miércoles** | **Post en Instagram**: *"Antes y después con *Aurora* (1 semana)"*.          | Instagram.               | Fotos comparativas de piel (con permiso de la usuaria) + testimonio en texto.          | *"Etiquétanos usando *Aurora* y gana un pack."* |
| **Viernes** | **Story en Instagram**: *"Pregúntale a una usuaria de *Aurora*"*.              | Instagram Stories.        | Entrevista rápida a una cliente bogotana (ej: *"¿Qué cambiaste de tu rutina con *Aurora*?"*). | *"Escríbenos 'AURORA' y te contamos más."*      |
| **Domingo** | **Email**: *"Ellas ya lo probaron: sus historias con *Aurora*"*.               | Email.                    | Colección de testimonios con fotos (ej: *"Ana, 35 años: 'Mi piel nunca había lucido tan luminosa'"*). | *"Lee sus historias y prueba *Aurora* hoy."*  |

**Métricas de Éxito**:
- **Reel/TikTok**: 6,000 visualizaciones, 6% de guardados.
- **Post de testimonios**: 50 comentarios, 10 etiquetas (#MiRitualAurora).
- **Email**: Tasa de apertura >30%, 5 ventas directas.

---

#### **Semana 3: Escasez y Urgencia (Impulsar Ventas)**
**Objetivo**: Crear **urgencia** y limitar la disponibilidad para aumentar conversiones.

| **Día**  | **Acciones**                                                                 | **Canales**               | **Contenido Específico**                                                                 | **CTA**                                      |
|----------|-----------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------|
| **Lunes** | **Anuncio en Instagram/Facebook**: *"Solo 20 sets *Aurora* disponibles esta semana"*. | Instagram/FB Ads.        | Video corto: *"*Aurora* está volando de los estantes. ¿Te lo vas a perder?"*.          | *"Compra ahora y evita que se agote."*        |
| **Miércoles** | **Story en Instagram**: *"Countdown: Solo 48 horas para la oferta *Aurora*"*. | Instagram Stories.        | Story con reloj de cuenta regresiva + código de descuento exclusivo (ej: AURORA20).    | *"Usa AURORA20 antes de que se agote."*       |
| **Viernes** | **Live en Instagram**: *"Última oportunidad: Preguntas sobre *Aurora*"*.       | Instagram Live.           | Responder dudas en tiempo real + mostrar inventario en vivo.                           | *"Compra ahora y gana un difusor de aceites gratis."* |
| **Domingo** | **Email**: *"Oferta relámpago: *Aurora* con 20% de descuento (hasta agotar stock)"*. | Email.                    | Diseño de email con sensación de urgencia (ej: *"Solo 15 sets restantes"*).           | *"Haz clic ahora y usa código URGENCIA20."*   |

**Métricas de Éxito**:
- **Anuncios**: ROAS >3 (por cada $1 en ads, $3 en ventas).
- **Ventas**: 30% aumento en conversiones vs. semanas anteriores.
- **Stock**: Reducción del 50% en inventario de *Aurora*.

---

#### **Semana 4: Fidelización y Comunidad (Crear Lealtad)**
**Objetivo**: Convertir compradores en **embajadores** de la marca y crear una comunidad alrededor de *Aurora*.

| **Día**  | **Acciones**                                                                 | **Canales**               | **Contenido Específico**                                                                 | **CTA**                                      |
|----------|-----------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------|
| **Lunes** | **Reel/TikTok**: *"Cómo crear tu propio ritual con *Aurora*"*.               | TikTok/Instagram Reels.   | Tutorial de 60 segundos mostrando cómo combinar *Aurora* con otros productos (ej: *"Aurora + una taza de té de manzanilla = momento de paz"*). | *"Crea tu ritual y etiquétanos."*             |
| **Miércoles** | **Post en Instagram**: *"Club Aurora: Beneficios exclusivos para ti"*.       | Instagram.               | Publicación sobre el lanzamiento de un programa de fidelidad (ej: *"Compra *Aurora* y gana puntos para canjear por productos"*). | *"Únete al Club Aurora y obtén beneficios."*   |
| **Viernes** | **Live en Instagram**: *"Sesión de preguntas con una usuaria VIP de *Aurora*"*. | Instagram Live.           | Live con una cliente bogotana que use *Aurora* desde el lanzamiento (ej: *"Cómo ha cambiado mi rutina"*). | *"Hazte parte de la comunidad *Aurora*."*     |
| **Domingo** | **Email**: *"Gracias por ser parte del ritual *Aurora*: Aquí está tu regalo"*. | Email.                    | Email con código de descuento para próxima compra (ej: *"GRACIAS15")* + invitación a compartir su experiencia. | *"Usa GRACIAS15 en tu próxima compra."*        |

**Métricas de Éxito**:
- **Reel/TikTok**: 7,000 visualizaciones, 8% de guardados.
- **Club Aurora**: 100 suscriptores nuevos.
- **Ventas recurrentes**: 15% de clientes compran nuevamente en el mes.

---

### **Canales y Presupuesto Estimado**
| **Canal**               | **Estrategia**                                                                 | **Presupuesto (4 semanas)** | **KPI Principal**                          |
|-------------------------|-------------------------------------------------------------------------------|-----------------------------|---------------------------------------------|
| **Instagram**           | Reels, Stories, Posts + Anuncios.                                             | $1,500,000 COP              | Engagement (likes, compartidos, guardados). |
| **TikTok**              | Videos virales, colaboraciones con microinfluencers bogotanos.               | $1,000,000 COP              | Visualizaciones y guardados.               |
| **Facebook/Instagram Ads** | Anuncios de urgencia (Semana 3) y retargeting.                            | $2,000,000 COP              | ROAS >3.                                    |
| **Email Marketing**     | Secuencia de emails con testimonios y ofertas.                                | $500,000 COP (herramienta). | Tasa de apertura >30%, CTR >4%.              |
| **WhatsApp Business**   | Mensajes personalizados y atención al cliente.                                | $300,000 COP (tiempo).     | Respuestas en <24h, ventas por WhatsApp.    |
| **Colaboraciones**      | 2 microinfluencers bogotanos (10K-50K seguidores).                            | $1,500,000 COP (productos + comisión). | 500 nuevos seguidores y 10 ventas.          |

**Total Presupuesto**: **$6,800,000 COP** (aprox. $1,700 USD).

---

### **Mensajes Clave por Canal**
| **Canal**       | **Mensaje Principal**                                                                 | **Tono**                     |
|-----------------|---------------------------------------------------------------------------------------|------------------------------|
| **Instagram**   | *"*Aurora* es tu ritual de lujo: ingredientes naturales de Colombia para pieles que merecen lo mejor."* | Elegante, sensorial, emocional. |
| **TikTok**      | *"¿Cansada de skincare aburrido? *Aurora* es tu momento de spa en casa."*             | Divertido, cercano, con humor bogotano. |
| **Email**       | *"Camila, tu piel es única. *Aurora* fue creado para ti: un set premium con ingredientes colombianos y un ritual que transforma tu noche."* | Personalizado, exclusivo. |
| **WhatsApp**    | *"Hola [Nombre], como usuaria de *Aurora*, aquí tienes un 10% de descuento. ¿Necesitas ayuda para elegir?"* | Amigable, cercano. |
| **Anuncios**    | *"Solo 20 sets *Aurora* disponibles esta semana. ¿Te lo vas a perder?"*               | Urgente, escaso. |

---

### **Métricas de Éxito Globales (Campaña de 4 Semanas)**
| **Área**               | **KPI**                                  | **Meta**                          | **Cómo Medir**                          |
|------------------------|------------------------------------------|-----------------------------------|------------------------------------------|
| **Tráfico**            | Visitas al sitio desde Bogotá.           | 80% de tráfico.                   | Google Analytics.                       |
| **Engagement**         | Tasa de guardados en IG/TikTok.          | 5-8%.                             | Insights.                               |
| **Conversión**         | Tasa de conversión del sitio.           | 3-4%.                             | Google Analytics.                       |
| **Ventas**             | Ventas de *Aurora*.                     | 50-70 sets vendidos.              | Shopify.                                |
| **ROAS**               | Retorno de inversión en publicidad.     | >3.                               | Meta Ads / Google Ads.                   |
| **Redes Sociales**     | Crecimiento de seguidores en IG/TikTok.  | +1,500 seguidores en IG, +1,000 en TikTok. | Insights.                               |
| **Email**              | Tasa de apertura y CTR.                  | Apertura >30%, CTR >4%.           | Mailchimp.                              |
| **WhatsApp**           | Mensajes respondidos y ventas.          | 90% de respuestas en <24h, 5 ventas por WhatsApp. | WhatsApp Business.                      |
| **Prueba Social**      | Testimonios y etiquetas (#MiRitualAurora). | 20 testimonios + 50 etiquetas.    | Instagram/TikTok.                        |

---

### **Acciones si los KPIs No se Cumplen**
1. **Si el engagement es bajo (<5%)**:
   - Aumentar frecuencia de Stories interactivos (encuestas, preguntas).
   - Probar contenido más emocional (ej: *"Cómo *Aurora* cambió la rutina de Camila"*).

2. **Si las ventas son bajas (<50 sets)**:
   - Lanzar una oferta de *"Prueba 7 días, devuelve si no te convence"* (reduciendo riesgo percibido).
   - Hacer packs con *Luna* o *Sol* (ej: *"Kit Bogotá: *Luna* + *Aurora* con 15% de descuento"*).

3. **Si el ROAS es bajo (<3)**:
   - Reenfocar anuncios en audiencias que hayan interactuado con tu contenido (retargeting).
   - Probar nuevos creativos (ej: videos de testimonios en lugar de productos).

4. **Si el tráfico desde Bogotá es <70%**:
   - Ajustar geolocalización en anuncios a barrios específicos (Chapinero, Usaquén).
   - Crear contenido con hashtags locales (ej: *#BellezaChapinero*).

---

### **Ejemplo de Calendario Diario (Semana 1)**
| **Día**  | **Hora** | **Acción**                                                                 | **Canal**       | **Contenido**                                                                 |
|----------|----------|-----------------------------------------------------------------------------|-----------------|-------------------------------------------------------------------------------|
| **Lunes** | 8:00 AM  | Publicar Reel: *"¿Qué hay dentro de *Aurora*?"*.                            | TikTok/IG Reels. | Video slow-motion del unboxing con música relajante.                        |
| **Lunes** | 12:00 PM | Story: *"¿Listas para tu ritual de lujo?"* + enlace a sitio web.           | Instagram.      | Imagen del set *Aurora* con texto: *"Link en bio para tu momento de paz."*   |
| **Miércoles** | 7:00 PM | Publicar Post: *"El origen de *Aurora*: ingredientes naturales de Colombia"*. | Instagram.      | Carousel con fotos de proveedores y texto explicativo.                      |
| **Viernes** | 6:00 PM | Live: *"Q&A con la creadora de *Aurora*"*.                                  | Instagram Live. | Charla de 30 min respondiendo dudas sobre el producto.                       |
| **Domingo** | 9:00 AM | Enviar Email: *"Tu ritual de spa en casa empieza aquí"*.                   | Email.          | Guía descargable + código de descuento 10%.                                 |

---

### **Herramientas Recomendadas**
1. **Diseño**: Canva (para creativos de Instagram/Stories).
2. **Edición de Video**: CapCut (para Reels/TikTok) o InShot (para videos rápidos).
3. **Automatización**: ManyChat (para WhatsApp) o Mailchimp (para emails).
4. **Anuncios**: Meta Ads Manager (para Instagram/Facebook) y TikTok Ads.
5. **Analítica**: Google Analytics 4, Insights de Instagram/TikTok, Shopify Reports.

---
**Pregunta para ti**:
- ¿Quieres que desarrolle **guiones específicos** para los Reels/TikToks de esta campaña? Por ejemplo, el script exacto para el video de *"¿Qué hay dentro de *Aurora*?"* o el live de Q&A.
- ¿O prefieres ajustar algún elemento, como el **presupuesto** o el **enfoque de los mensajes** para alinearlos más con tu voz de marca?


## Respuesta completa

### **Campaña de 4 Semanas para *Aurora*: "Ritual de Lujo para Pieles que Merecen lo Mejor"**
**Objetivo Principal**:
Posicionar *Aurora* como **el set de skincare premium para bogotanas que buscan un ritual de autocuidado exclusivo**, sin competir en precio con *Skin Lab*, sino en **experiencia sensorial y conexión emocional**. Validar si el público bogotano está dispuesto a invertir en un producto premium con enfoque en **naturalidad + ritual**, no solo resultados clínicos.

---

### **Audiencia Objetivo (Segmentación Detallada)**
**Perfil Demográfico**:
- **Edad**: 28-45 años.
- **Género**: Mujeres (y hombres que compran para sus parejas).
- **Ubicación**: Bogotá (enfocado en barrios como **Chapinero, Usaquén, La Candelaria, Suba**).
- **Nivel socioeconómico**: C2-C3 (clase media-alta bogotana).
- **Intereses**:
  - Belleza natural, skincare, wellness, yoga, spa en casa.
  - Moda sostenible, productos colombianos, autocuidado.

**Psychographics (Perfil Psicológico)**:
- Buscan **experiencias** (no solo productos).
- Valoran la **naturalidad** pero están dispuestas a pagar por calidad.
- Tienen **tiempo para rituales** (aunque sea en casa).
- Se identifican con marcas que **cuentan historias auténticas** y tienen un **toque local**.

**Competidores a Desplazar**:
- *Skin Lab*: Enfoque clínico/científico (frío).
- *Botica Verde*: Natural pero masivo (genérico).
- **Tú**: **Natural + lujo emocional + conexión bogotana**.

---

### **Mensaje Principal (Elevator Pitch)**
*"Aurora no es solo un set de skincare: es tu momento de spa en casa, con ingredientes naturales de Colombia y un ritual que transforma tu piel y tu día. Porque en Bogotá, mereces sentirte como en un resort... sin salir de tu casa."*

**Variantes por Canal**:
- **Instagram/TikTok**: *"¿Cansada de rutinas de skincare que no te hacen sentir especial? *Aurora* es tu ritual de lujo: ingredientes naturales, texturas que invitan a masajearte y resultados que se notan desde la primera semana."*
- **Email/WhatsApp**: *"Camila, tu piel es única. Por eso *Aurora* fue creado para ti: un set premium con ingredientes colombianos, diseñado para que cada noche sea un momento de autocuidado. Prueba 7 días y te devolveremos el dinero si no notas la diferencia."* (Oferta de garantía).

---

### **Estrategia de 4 Semanas**
#### **Semana 1: Lanzamiento del "Ritual Aurora" (Crear Deseo)**
**Objetivo**: Generar curiosidad y posicionar *Aurora* como un **experiencia premium**.

| **Día**  | **Acciones**                                                                 | **Canales**               | **Contenido Específico**                                                                 | **CTA (Llamado a la Acción)**                          |
|----------|-----------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------|
| **Lunes** | Publicar **Reel/TikTok**: *"¿Qué hay dentro de *Aurora*?"* (unboxing slow-motion con música relajante). | TikTok/Instagram Reels.   | Video mostrando cada producto del set (*Aurora*) con close-ups de texturas y aromas.       | *"¿Listas para tu ritual de lujo? Link en bio."*         |
| **Miércoles** | **Post en Instagram**: *"El origen de *Aurora*: ingredientes naturales de Colombia"*. | Instagram.               | Carousel con fotos de proveedores (ej: *"Este aceite de argán viene de Boyacá"*).      | *"Descubre la historia detrás de tu piel."*           |
| **Viernes** | **Live en Instagram/Facebook**: *"Q&A con la creadora de *Aurora*"*.           | Instagram Live/FB.        | Charla de 30 min sobre cómo se diseñó *Aurora* para pieles bogotanas.                   | *"Haz tu pregunta y gana un set *Aurora*."*            |
| **Domingo** | **Email**: *"Tu ritual de spa en casa empieza aquí"*.                        | Email.                    | Guía descargable: *"Cómo usar *Aurora* en 10 minutos"* + código de descuento 10%.      | *"Descarga tu guía y usa código RITUAL10."*            |

**Métricas de Éxito**:
- **Reel/TikTok**: 5,000 visualizaciones, 5% de guardados, 3% de compartidos.
- **Live**: 200 espectadores, 50 preguntas, 10 ventas durante el live.
- **Email**: Tasa de apertura >25%, CTR >3%.

---

#### **Semana 2: Prueba Social y Testimonios (Generar Confianza)**
**Objetivo**: Mostrar resultados reales y crear **prueba social** con testimonios de bogotanas.

| **Día**  | **Acciones**                                                                 | **Canales**               | **Contenido Específico**                                                                 | **CTA**                                      |
|----------|-----------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------|
| **Lunes** | **Reel/TikTok**: *"POV: Usas *Aurora* por primera vez"*.                     | TikTok/Instagram Reels.   | Video de una usuaria bogotana probando *Aurora* por primera vez (reacción de sorpresa).    | *"¿Quieres probar *Aurora*? Link en bio."*      |
| **Miércoles** | **Post en Instagram**: *"Antes y después con *Aurora* (1 semana)"*.          | Instagram.               | Fotos comparativas de piel (con permiso de la usuaria) + testimonio en texto.          | *"Etiquétanos usando *Aurora* y gana un pack."* |
| **Viernes** | **Story en Instagram**: *"Pregúntale a una usuaria de *Aurora*"*.              | Instagram Stories.        | Entrevista rápida a una cliente bogotana (ej: *"¿Qué cambiaste de tu rutina con *Aurora*?"*). | *"Escríbenos 'AURORA' y te contamos más."*      |
| **Domingo** | **Email**: *"Ellas ya lo probaron: sus historias con *Aurora*"*.               | Email.                    | Colección de testimonios con fotos (ej: *"Ana, 35 años: 'Mi piel nunca había lucido tan luminosa'"*). | *"Lee sus historias y prueba *Aurora* hoy."*  |

**Métricas de Éxito**:
- **Reel/TikTok**: 6,000 visualizaciones, 6% de guardados.
- **Post de testimonios**: 50 comentarios, 10 etiquetas (#MiRitualAurora).
- **Email**: Tasa de apertura >30%, 5 ventas directas.

---

#### **Semana 3: Escasez y Urgencia (Impulsar Ventas)**
**Objetivo**: Crear **urgencia** y limitar la disponibilidad para aumentar conversiones.

| **Día**  | **Acciones**                                                                 | **Canales**               | **Contenido Específico**                                                                 | **CTA**                                      |
|----------|-----------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------|
| **Lunes** | **Anuncio en Instagram/Facebook**: *"Solo 20 sets *Aurora* disponibles esta semana"*. | Instagram/FB Ads.        | Video corto: *"*Aurora* está volando de los estantes. ¿Te lo vas a perder?"*.          | *"Compra ahora y evita que se agote."*        |
| **Miércoles** | **Story en Instagram**: *"Countdown: Solo 48 horas para la oferta *Aurora*"*. | Instagram Stories.        | Story con reloj de cuenta regresiva + código de descuento exclusivo (ej: AURORA20).    | *"Usa AURORA20 antes de que se agote."*       |
| **Viernes** | **Live en Instagram**: *"Última oportunidad: Preguntas sobre *Aurora*"*.       | Instagram Live.           | Responder dudas en tiempo real + mostrar inventario en vivo.                           | *"Compra ahora y gana un difusor de aceites gratis."* |
| **Domingo** | **Email**: *"Oferta relámpago: *Aurora* con 20% de descuento (hasta agotar stock)"*. | Email.                    | Diseño de email con sensación de urgencia (ej: *"Solo 15 sets restantes"*).           | *"Haz clic ahora y usa código URGENCIA20."*   |

**Métricas de Éxito**:
- **Anuncios**: ROAS >3 (por cada $1 en ads, $3 en ventas).
- **Ventas**: 30% aumento en conversiones vs. semanas anteriores.
- **Stock**: Reducción del 50% en inventario de *Aurora*.

---

#### **Semana 4: Fidelización y Comunidad (Crear Lealtad)**
**Objetivo**: Convertir compradores en **embajadores** de la marca y crear una comunidad alrededor de *Aurora*.

| **Día**  | **Acciones**                                                                 | **Canales**               | **Contenido Específico**                                                                 | **CTA**                                      |
|----------|-----------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------|
| **Lunes** | **Reel/TikTok**: *"Cómo crear tu propio ritual con *Aurora*"*.               | TikTok/Instagram Reels.   | Tutorial de 60 segundos mostrando cómo combinar *Aurora* con otros productos (ej: *"Aurora + una taza de té de manzanilla = momento de paz"*). | *"Crea tu ritual y etiquétanos."*             |
| **Miércoles** | **Post en Instagram**: *"Club Aurora: Beneficios exclusivos para ti"*.       | Instagram.               | Publicación sobre el lanzamiento de un programa de fidelidad (ej: *"Compra *Aurora* y gana puntos para canjear por productos"*). | *"Únete al Club Aurora y obtén beneficios."*   |
| **Viernes** | **Live en Instagram**: *"Sesión de preguntas con una usuaria VIP de *Aurora*"*. | Instagram Live.           | Live con una cliente bogotana que use *Aurora* desde el lanzamiento (ej: *"Cómo ha cambiado mi rutina"*). | *"Hazte parte de la comunidad *Aurora*."*     |
| **Domingo** | **Email**: *"Gracias por ser parte del ritual *Aurora*: Aquí está tu regalo"*. | Email.                    | Email con código de descuento para próxima compra (ej: *"GRACIAS15")* + invitación a compartir su experiencia. | *"Usa GRACIAS15 en tu próxima compra."*        |

**Métricas de Éxito**:
- **Reel/TikTok**: 7,000 visualizaciones, 8% de guardados.
- **Club Aurora**: 100 suscriptores nuevos.
- **Ventas recurrentes**: 15% de clientes compran nuevamente en el mes.

---

### **Canales y Presupuesto Estimado**
| **Canal**               | **Estrategia**                                                                 | **Presupuesto (4 semanas)** | **KPI Principal**                          |
|-------------------------|-------------------------------------------------------------------------------|-----------------------------|---------------------------------------------|
| **Instagram**           | Reels, Stories, Posts + Anuncios.                                             | $1,500,000 COP              | Engagement (likes, compartidos, guardados). |
| **TikTok**              | Videos virales, colaboraciones con microinfluencers bogotanos.               | $1,000,000 COP              | Visualizaciones y guardados.               |
| **Facebook/Instagram Ads** | Anuncios de urgencia (Semana 3) y retargeting.                            | $2,000,000 COP              | ROAS >3.                                    |
| **Email Marketing**     | Secuencia de emails con testimonios y ofertas.                                | $500,000 COP (herramienta). | Tasa de apertura >30%, CTR >4%.              |
| **WhatsApp Business**   | Mensajes personalizados y atención al cliente.                                | $300,000 COP (tiempo).     | Respuestas en <24h, ventas por WhatsApp.    |
| **Colaboraciones**      | 2 microinfluencers bogotanos (10K-50K seguidores).                            | $1,500,000 COP (productos + comisión). | 500 nuevos seguidores y 10 ventas.          |

**Total Presupuesto**: **$6,800,000 COP** (aprox. $1,700 USD).

---

### **Mensajes Clave por Canal**
| **Canal**       | **Mensaje Principal**                                                                 | **Tono**                     |
|-----------------|---------------------------------------------------------------------------------------|------------------------------|
| **Instagram**   | *"*Aurora* es tu ritual de lujo: ingredientes naturales de Colombia para pieles que merecen lo mejor."* | Elegante, sensorial, emocional. |
| **TikTok**      | *"¿Cansada de skincare aburrido? *Aurora* es tu momento de spa en casa."*             | Divertido, cercano, con humor bogotano. |
| **Email**       | *"Camila, tu piel es única. *Aurora* fue creado para ti: un set premium con ingredientes colombianos y un ritual que transforma tu noche."* | Personalizado, exclusivo. |
| **WhatsApp**    | *"Hola [Nombre], como usuaria de *Aurora*, aquí tienes un 10% de descuento. ¿Necesitas ayuda para elegir?"* | Amigable, cercano. |
| **Anuncios**    | *"Solo 20 sets *Aurora* disponibles esta semana. ¿Te lo vas a perder?"*               | Urgente, escaso. |

---

### **Métricas de Éxito Globales (Campaña de 4 Semanas)**
| **Área**               | **KPI**                                  | **Meta**                          | **Cómo Medir**                          |
|------------------------|------------------------------------------|-----------------------------------|------------------------------------------|
| **Tráfico**            | Visitas al sitio desde Bogotá.           | 80% de tráfico.                   | Google Analytics.                       |
| **Engagement**         | Tasa de guardados en IG/TikTok.          | 5-8%.                             | Insights.                               |
| **Conversión**         | Tasa de conversión del sitio.           | 3-4%.                             | Google Analytics.                       |
| **Ventas**             | Ventas de *Aurora*.                     | 50-70 sets vendidos.              | Shopify.                                |
| **ROAS**               | Retorno de inversión en publicidad.     | >3.                               | Meta Ads / Google Ads.                   |
| **Redes Sociales**     | Crecimiento de seguidores en IG/TikTok.  | +1,500 seguidores en IG, +1,000 en TikTok. | Insights.                               |
| **Email**              | Tasa de apertura y CTR.                  | Apertura >30%, CTR >4%.           | Mailchimp.                              |
| **WhatsApp**           | Mensajes respondidos y ventas.          | 90% de respuestas en <24h, 5 ventas por WhatsApp. | WhatsApp Business.                      |
| **Prueba Social**      | Testimonios y etiquetas (#MiRitualAurora). | 20 testimonios + 50 etiquetas.    | Instagram/TikTok.                        |

---

### **Acciones si los KPIs No se Cumplen**
1. **Si el engagement es bajo (<5%)**:
   - Aumentar frecuencia de Stories interactivos (encuestas, preguntas).
   - Probar contenido más emocional (ej: *"Cómo *Aurora* cambió la rutina de Camila"*).

2. **Si las ventas son bajas (<50 sets)**:
   - Lanzar una oferta de *"Prueba 7 días, devuelve si no te convence"* (reduciendo riesgo percibido).
   - Hacer packs con *Luna* o *Sol* (ej: *"Kit Bogotá: *Luna* + *Aurora* con 15% de descuento"*).

3. **Si el ROAS es bajo (<3)**:
   - Reenfocar anuncios en audiencias que hayan interactuado con tu contenido (retargeting).
   - Probar nuevos creativos (ej: videos de testimonios en lugar de productos).

4. **Si el tráfico desde Bogotá es <70%**:
   - Ajustar geolocalización en anuncios a barrios específicos (Chapinero, Usaquén).
   - Crear contenido con hashtags locales (ej: *#BellezaChapinero*).

---

### **Ejemplo de Calendario Diario (Semana 1)**
| **Día**  | **Hora** | **Acción**                                                                 | **Canal**       | **Contenido**                                                                 |
|----------|----------|-----------------------------------------------------------------------------|-----------------|-------------------------------------------------------------------------------|
| **Lunes** | 8:00 AM  | Publicar Reel: *"¿Qué hay dentro de *Aurora*?"*.                            | TikTok/IG Reels. | Video slow-motion del unboxing con música relajante.                        |
| **Lunes** | 12:00 PM | Story: *"¿Listas para tu ritual de lujo?"* + enlace a sitio web.           | Instagram.      | Imagen del set *Aurora* con texto: *"Link en bio para tu momento de paz."*   |
| **Miércoles** | 7:00 PM | Publicar Post: *"El origen de *Aurora*: ingredientes naturales de Colombia"*. | Instagram.      | Carousel con fotos de proveedores y texto explicativo.                      |
| **Viernes** | 6:00 PM | Live: *"Q&A con la creadora de *Aurora*"*.                                  | Instagram Live. | Charla de 30 min respondiendo dudas sobre el producto.                       |
| **Domingo** | 9:00 AM | Enviar Email: *"Tu ritual de spa en casa empieza aquí"*.                   | Email.          | Guía descargable + código de descuento 10%.                                 |

---

### **Herramientas Recomendadas**
1. **Diseño**: Canva (para creativos de Instagram/Stories).
2. **Edición de Video**: CapCut (para Reels/TikTok) o InShot (para videos rápidos).
3. **Automatización**: ManyChat (para WhatsApp) o Mailchimp (para emails).
4. **Anuncios**: Meta Ads Manager (para Instagram/Facebook) y TikTok Ads.
5. **Analítica**: Google Analytics 4, Insights de Instagram/TikTok, Shopify Reports.

---
**Pregunta para ti**:
- ¿Quieres que desarrolle **guiones específicos** para los Reels/TikToks de esta campaña? Por ejemplo, el script exacto para el video de *"¿Qué hay dentro de *Aurora*?"* o el live de Q&A.
- ¿O prefieres ajustar algún elemento, como el **presupuesto** o el **enfoque de los mensajes** para alinearlos más con tu voz de marca?