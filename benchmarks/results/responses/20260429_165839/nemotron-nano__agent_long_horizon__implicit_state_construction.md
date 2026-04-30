# Nemotron 3 Nano 30B — agent_long_horizon/implicit_state_construction

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 6.45 | quality: 7.0
- latency_total: 239.929s | tokens_per_second: 88.2
- input_tokens: 38762 | output_tokens: 18409

## Respuesta completa

## **Campaña “Aurora ‑ Ritual de Lujo Andino”**  
**Producto:** *Set de cuidado facial “Aurora”* (precio premium)  
**Duración:** 4 semanas (28 días)  
**Objetivo principal:** Generar **ventas directas** del set Aurora y **capturar leads** de clientes potenciales de alto poder adquisitivo en Bogotá, sin depender de descuentos de precio.  

---  

### 1️⃣ OBJETIVO DE LA CAMPAÑA  
| KPI objetivo | Valor esperado en 4 semanas |
|--------------|-----------------------------|
| **Ventas atribuidas a la campaña** | **≥ 150 unidades** (≈ US$ 9 000 de ingreso) |
| **Costo por adquisición (CPA)** | ≤ US$ 15 (ROAS ≥ 3,0×) |
| **Leads (emails / números de teléfono)** | **≥ 1 200 contactos** (para nurturing) |
| **Tasa de conversión del embudo** (visitas → compra) | **≥ 3,0 %** |
| **NPS post‑compra (encuesta 7‑días después)** | **≥ 45** (satisfacción “luxury”) |

> **Nota:** El objetivo es vender *solo* el set Aurora. Los mensajes de los demás productos (Sol, Luna) se usarán solo como “cross‑sell” opcional al final de la compra, pero no serán el foco.

---  

### 2️⃣ AUDIENCIA PRIORITARIA  

| Segmento | Perfil demográfico | Psicográfico / comportamiento | Canal de mayor respuesta |
|----------|-------------------|--------------------------------|--------------------------|
| **A‑1: Mujer “Belleza Consciente Premium”** | 28‑45 a, ingreso mensual ≥ $4 500 USD (clase alta/middle‑high), vive en Chapinero, Usaquén, La Candelaria, Teusaquillo o Parque 93. | Busca productos con **ciencia + origen**, dispuesta a pagar por calidad y experiencia. Valora la *slow‑beauty*, la trazabilidad y el packaging elegante. | Instagram (Feed + Stories), TikTok (Reels), Google Search (keywords “set facial premium Bogotá”, “cuidado facial anti‑edad”). |
| **A‑2: Millennial “Influencer‑Aspirante”** | 22‑32 a, ingreso ≥ $2 800 USD, estudia o trabaja en sectores creativos (moda, diseño, comunicación). | Sigue tendencias de belleza, busca contenido visualmente impactante, comparte sus rutinas en redes. | Instagram Reels/TikTok, Influencer micro‑collabs. |
| **A‑3: Profesional “Mom‑Boss”** | 33‑45 a, ingreso ≥ $5 500 USD, mamá con carrera, busca autocuidado eficaz. | Prioriza resultados rápidos y rutinas simples; valora la rapidez de entrega en Bogotá. | Facebook Ads (retargeting), Instagram Ads (Carousel), Email (lista de clientes actuales). |

**Segmentación de audiencias en Meta Ads Manager:**  

- **Ubicación:** Bogotá (radio 15 km).  
- **Intereses:** “Cuidado de la piel”, “Belleza natural”, “Cosmética coreana”, “Luxury beauty”, “Guayaba”, “Péptidos”.  
- **Comportamiento:** “Compradores recientes de productos de belleza premium”, “Usuarios que interactuaron con contenido de dermatología”.  
- **Custom Audiences:** listas de clientes que ya compraron *Sol* o *Luna* (cross‑sell).  
- **Look‑alike:** 1 % a partir de los 2 500 clientes que compraron Aurora en los últimos 6 meses.

---  

### 3️⃣ CANALES Y TACTICAS (por semana)

| Semana | Acción | Canal | Detalle creativo | CTA / Enlace |
|--------|--------|-------|-------------------|--------------|
| **1** | **Teaser + “Behind‑the‑Science”** | Instagram Reels + TikTok (15‑30 s) | Video macro‑cámara del proceso de extracción de **guayaba & péptidos**, con subtítulos en español. Texto: “Descubre el secreto de la ciencia andina que transforma tu piel en 28 días”. | “Desliza ↑ para descubrir la revolución” → **Linktree** con botón **“Reserva tu Aurora”** (formulario de captura). |
| | **Landing Page “Aurora ‑ Ritual Andino”** | Web (Shopify) | Página exclusiva con: video 1 min del ritual, tabla de ingredientes con origen, testimonio de dermatólogo colombiano, botón **“Comprar ahora – Envío 24 h Bogotá”**. | Formulario de captura + botón de compra. |
| | **Email “Invita a tu piel a un ritual de lujo”** | Email (lista de clientes premium) | Asunto: “Solo 48 h: Aurora llega a tu puerta en Bogotá”. Texto breve + video embed. | “Reserva tu set Aurora”. |
| **2** | **Micro‑influencer “Rutina Aurora”** | Instagram Stories + Feed + TikTok (2 micro‑influencers, 15‑30 k seguidores en Bogotá) | Influencer muestra su *morning routine* con Aurora, incluye “Swipe‑up” a la landing, menciona “Solo para Bogotá”. | Enlace directo a landing con código de seguimiento UTM `utm_source=insta_influencer`. |
| | **Carousel Ads “3 Pasos + Resultados”** | Instagram Feed + Facebook Feed | 5‑slide carousel: 1‑Ingrediente estrella, 2‑Efecto visible, 3‑Testimonio antes‑después, 4‑Precio premium (Sin descuento), 5‑CTA “Compra ahora”. | “Compra Aurora”. |
| | **Retargeting (Pixel)** | Meta Ads (Dynamic Product Ads) | Anuncios dinámicos que muestran el set Aurora a quienes visitaron la landing pero no compraron (últimos 7 días). | “Regresa y completa tu ritual”. |
| **3** | **Live Q&A + Demo en tiempo real** | Instagram Live (45 min) + TikTok Live (re‑upload) | Camila responde preguntas, aplica Aurora en tiempo real, muestra textura y aroma. Cada asistente recibe **código exclusivo** para 10 % de descuento (no se reduce el precio final, solo un *voucher* de regalo para próxima compra). | “Regístrate en el link de la bio”. |
| | **Pinterest Pin “Aurora Routine”** | Pinterest | Infografía vertical con pasos de la rutina y botón “Compra en Bogotá”. | Pin → landing con UTM `pinterest`. |
| | **Google Search Ads (Keyword)** | Google Ads (Search) | Palabras clave: “set facial premium Bogotá”, “cuidado facial anti‑edad Bogotá”, “Aurora set”. Budget $300 USD para la semana. | Landing page con “Compra ahora”. |
| **4** | **UGC & Social Proof Push** | Instagram Feed + Stories + TikTok | Re‑post de fotos de clientas que recibieron Aurora (UGC). Texto: “Mi piel cambió en 28 días – #MiRitualAurora”. | “Compra el tuyo y únete al club”. |
| | **Oferta de “Pack Regalo” (sin descuento)** | Web + Email | Al comprar Aurora, el cliente recibe **una muestra de Sol** y **una muestra de Luna** en un estuche de lujo. | “Añade tu regalo”. |
| | **Retargeting final + Countdown** | Meta Ads (Stories) | Countdown “Últimas 48 h – Envío express Bogotá”. | “Última oportunidad – Compra Aurora”. |

---  

### 4️⃣ MENSAJE PRINCIPAL (copy central)

> **“Aurora – El ritual de lujo que combina la ciencia de los péptidos con el poder de la guayaba andina. 28 días para una piel más firme, luminosa y visiblemente rejuvenecida. Solo para Bogotá, entrega en 24 h y experiencia premium incluida.”**  

- **Tono:** Elegante, científico pero cercano; énfasis en *origen colombiano* y *experiencia sensorial*.  
- **Palabras clave a usar:** “luxury”, “ritual”, “ciencia andina”, “guayaba”, “péptidos”, “entrega 24 h Bogotá”, “exclusivo”, “premium”.  
- **Formato de copy:**  
  - **Headline (≤ 30 caracteres):** “Aurora – Tu piel, renovada”.  
  - **Body (≤ 125 caracteres):** “Descubre el set facial que combina guayaba natural y péptidos de última generación. Entrega express en Bogotá”.  
  - **CTA:** “Reserva tu set Aurora”.  

---  

### 5️⃣ MÉTRICAS DE ÉXITO (KPIs a monitorear)

| Métrica | Fuente | Umbral de éxito (4 semanas) |
|---------|--------|-----------------------------|
| **Impresiones totales (Meta + TikTok + Pinterest)** | Meta Insights, TikTok Analytics, Pinterest Analytics | ≥ 250 k |
| **Reach orgánico vs. paid** | Meta Insights | ≥ 55 % orgánico |
| **Vistas completadas de video (≥ 75 %)** | Reels/TikTok Analytics | ≥ 35 % de vistas completadas |
| **CTR a la landing (UTM)** | Google Analytics (UTM `utm_source=...`) | ≥ 2,5 % |
| **Leads captados (formulario)** | Formulario de captura (Google Forms / Shopify) | ≥ 1 200 |
| **Add‑to‑Cart (Aurora)** | GA4 Events → `add_to_cart` | ≥ 800 |
| **Conversiones (Compra Aurora)** | GA4 / Shopify → `purchase` | ≥ 150 unidades |
| **CPA (costo por adquisición)** | Meta Ads Manager | ≤ US$ 15 |
| **ROAS** | Ingresos atribuibles / gasto ads | ≥ 3,0× |
| **Tiempo medio de compra (desde click → checkout)** | GA4 → `ecommerce` | ≤ 3 min |
| **NPS post‑compra (encuesta 7 días)** | SurveyMonkey / Typeform (enviada vía email) | ≥ 45 |
| **Valor medio del pedido (incluye upsell Sol/Luna)** | Shopify | ≥ US$ 75 (incluye al menos 1 upsell) |
| **Retorno de inversión en influencers** | UTM `influencer` → conversiones | ≥ 2 ventas por influencer |

---  

### 6️⃣ CRONOGRAMA SEMANAL (Resumen visual)

| Semana | Tema central | Principal formato | CTA principal |
|--------|--------------|-------------------|---------------|
| **1** | *Descubrimiento* – “El origen del lujo” | Reel/TikTok teaser + email teaser | “Reserva tu Aurora”. |
| **2** | *Prueba social* – Influencers + Carousel | Carousel + Dynamic Retargeting | “Compra Aurora”. |
| **3** | *Experiencia en vivo* – Q&A + muestra gratuita | Instagram Live + TikTok Live | “Regístrate y recibe código”. |
| **4** | *Cierre urgente* – UGC + Regalo | UGC carousel + Countdown Stories | “Últimas 48 h – Compra Aurora”. |

---  

### 7️⃣ PRESUPUESTO RECOMENDADO (ejemplo)

| Rubro | % del presupuesto total (≈ US$ 2 000) |
|-------|--------------------------------------|
| Meta Ads (Feed + Stories + Dynamic) | 45 % (US$ 900) |
| TikTok Ads (In‑Feed) | 20 % (US$ 400) |
| Google Search (keywords) | 15 % (US$ 300) |
| Influencer micro‑collab (productos + Gift) | 10 % (US$ 200) |
| Producción de video (3‑4 reels + 1 live) | 5 % (US$ 100) |
| Herramientas/UTM y tracking | 5 % (US$ 100) |

> **Rationale:** La mayor parte del gasto se destina a **Meta** (el canal con mayor ROI para audiencias premium en Bogotá) y a **Google Search** para capturar intención de compra directa.

---  

### 8️⃣ FLUJO DE CONVERSIÓN RECOMENDADO

1. **Impresión / Visión del teaser** →  
2. **Click en “Reserva tu Aurora”** →  
3. **Landing page** – formulario de captura (email/teléfono) →  
4. **Email de bienvenida + código de regalo** →  
5. **Retargeting dinámico** (si no compra en 48 h) →  
6. **Live Q&A** (refuerzo de confianza) →  
7. **Checkout** – pago (Pagos Seguros) →  
8. **Email post‑compra (7 días)** – encuesta NPS + upsell Sol/Luna.  

---  

### 9️⃣ CHECK‑LIST DE LANZAMIENTO (para que nada se quede atrás)

| ✔️ | Acción |
|----|--------|
| 1 | Crear landing page exclusiva “Aurora ‑ Ritual Andino” con tracking UTM. |
| 2 | Configurar pixel de Meta y evento `purchase` en GA4. |
| 3 | Diseñar 3‑4 creativos de video (15‑30 s) y carousel. |
| 4 | Seleccionar 2 micro‑influencers (acuerdo de product + código). |
| 5 | Programar calendario de publicaciones (Meta, TikTok, Pinterest). |
| 6 | Programar email de teaser + reminder (día 3, día 7). |
| 7 | Preparar código de descuento “RITUAL10” (solo para próxima compra). |
| 8 | Configurar campaña de retargeting (audiencia “visita landing, no compra”). |
| 9 | Configurar Google Search campaña con keywords específicas. |
|10 | Crear encuesta NPS y automatizar envío 7 días después de la compra. |
|11 | Revisar y validar todos los enlaces (UTM correctos, checkout funcionando). |
|12 | Lanzar campaña (día 1) y monitorizar KPIs diariamente. |

---  

### 10️⃣ POST‑CAMPAÑA (Análisis y escalado)

1. **Reunión de revisión** (día 30) – comparar KPIs reales vs. metas.  
2. **Identificar creatividades top‑perform** → re‑usar en Q2 con mayor presupuesto.  
3. **Segmentar los 1 200 leads** en:  
   - 60 % → nurturing con contenido de *Sol* y *Luna* (cross‑sell).  
   - 40 % → re‑activación con oferta de “próxima colección”.  
4. **Exportar lista de compradores** → segmentar en CRM para futuros “early‑access” de nuevos lanzamientos.  
5. **Actualizar creatividades** con testimonios reales y resultados de ventas para la siguiente ronda de comunicación.  

---  

## Resumen rápido (para copy‑paste en tu plan)

- **Producto:** *Aurora – Set de cuidado facial premium*  
- **Objetivo:** ≥ 150 unidades vendidas, CPA ≤ US$ 15, ROAS ≥ 3×, 1 200 leads.  
- **Audiencia:** Mujeres 28‑45 a en Bogotá de alto poder adquisitivo + millennials creativos + mamás profesionales.  
- **Canales:** Instagram Reels/TikTok, Carousel Feed, Dynamic Retargeting, Instagram Live, Google Search, Pinterest, Email.  
- **Mensaje clave:** “Aurora – El ritual de lujo que combina la ciencia de los péptidos con la guayaba andina. Entrega express en Bogotá”.  
- **Métricas de éxito:** Alcance ≥ 250 k, CTR ≥ 2,5 %, CVR ≥ 3 %, CPA ≤ US$ 15, ROAS ≥ 3×, NPS ≥ 45.  

Con este plan tienes todo lo necesario para lanzar una campaña focalizada, medible y alineada con tu posicionamiento de **lujo accesible** en el mercado bogotano. ¡A lanzar “Aurora” y conquistar a esas pieles listas para un ritual andino!  

*¿Necesitas los assets visuales o el copy exacto para cada anuncio? Estoy listo para entregarte los textos y briefings de diseño.*