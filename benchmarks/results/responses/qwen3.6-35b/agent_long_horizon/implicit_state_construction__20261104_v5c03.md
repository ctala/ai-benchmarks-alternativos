# Qwen 3.6 35B base (OpenRouter FP8) — agent_long_horizon/implicit_state_construction

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 87.999s | tokens_per_second: 121.0
- input_tokens: 15764 | output_tokens: 10447

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo



Hola, Camila. Sí, me queda completamente claro. He registrado la siguiente información de tu negocio para usarla como base en todo el proceso de planificación:

- **Ubicación y alcance:** Tienda online con foco exclusivo en Bogotá.
- **Portafolio y posicionamiento por precio:**
  - `Aurora`: set de cuidado facial → precio premium
  - `Sol`: kit de maquillaje natural → precio medio
  - `Luna`: crema corporal → precio entrada
- **Competencia directa:** `Botica Verde` y `Skin Lab` (ambos operando en Bogotá).

Tendré estos datos activos en cada turno para segmentar públicos, comparar ventajas competitivas, ajustar mensajes y medir resultados sin necesidad de que me los repitas. 

¿Te gustaría empezar planificando la campaña para uno de los tres productos, o prefieres que primero definamos la estrategia general de lanzamiento/posicionamiento para Bogotá?

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo



Aquí tienes una propuesta de valor general, redactada en exactamente dos oraciones y alineada con tu contexto:

En Bogotá, ofrecemos una línea completa de belleza que integra un set de cuidado facial premium, un kit de maquillaje natural y una crema corporal accesible, permitiendo que cada cliente encuentre la solución ideal según su presupuesto y rutina. A diferencia de las marcas clínicas o dermatológicas de la ciudad, nuestra propuesta se diferencia por ofrecer una experiencia cercana, transparente y con productos que equilibran calidad, naturalidad y resultados visibles desde el primer uso.

¿Te gustaría que ahora desglosemos cómo adaptar esta propuesta general a mensajes específicos para cada producto (`Aurora`, `Sol` y `Luna`) o que definamos primero los públicos objetivo en Bogotá?

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo



Te recomiendo priorizar estos canales digitales, ordenados por impacto inmediato y ajuste específico a tu operación en Bogotá:

1. **Instagram + Meta Ads (Facebook/Instagram)**: Canal central para belleza en Colombia. Permite segmentación geográfica exacta (solo Bogotá), formatos visuales de alto rendimiento (Reels, carruseles, Stories) y campañas de conversión directas. Se adapta naturalmente a tus tres precios: `Aurora` con contenido educativo/premium y testimonios de alto valor; `Sol` con tutoriales y demos de maquillaje; `Luna` con prueba social, reseñas y ofertas de entrada. Además, te permite monitorear en tiempo real las estrategias de `Botica Verde` y `Skin Lab` y ajustar tu diferenciación.

2. **TikTok**: Priorízalo para alcance orgánico y contenido auténtico. Funciona excepcionalmente bien para `Sol` y `Luna` mediante rutinas rápidas, “día a día con mi rutina”, desmitificación de ingredientes naturales y comparativas honestas. En Bogotá tiene una penetración altísima en el segmento 18-35 años, y el costo de publicidad sigue siendo más accesible que en Instagram para pruebas iniciales.

3. **WhatsApp Business**: En Colombia no es solo un canal de soporte, es un canal de cierre y fidelización. Úsalo con catálogo integrado para `Sol` y `Luna`, y con asesoría personalizada (quizás con dermatóloga o maquilladora asociada) para `Aurora`. Permite recuperar carritos abandonados, programar recordatorios de reposición y construir una lista de clientes propia sin depender de algoritmos.

4. **Email marketing + Landing pages optimizadas**: No como canal de adquisición principal, sino como ecosistema de conversión y retención. Ideal para `Aurora` (newsletters con ciencia detrás de la fórmula, beneficios a largo plazo y contenido exclusivo) y para nutrir a los compradores de `Sol` y `Luna` hacia el upsell al set premium.

**Recomendación de ejecución inicial**: Enfoca el 70% de tu esfuerzo y presupuesto en Instagram + Meta Ads, usa TikTok como motor de contenido orgánico y retargeting de bajo costo, y cierra/fidelize por WhatsApp. Así cubres descubrimiento, consideración y conversión con un solo flujo.

¿Quieres que te arme un calendario de contenidos y estructura de campañas para los primeros 30 días en Instagram y TikTok, con ejemplos de copy y creatividades adaptados a `Aurora`, `Sol` y `Luna`?

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo



Para maximizar el alcance y la conversión en tu mercado de Bogotá, te recomiendo esta frecuencia de publicación orgánica, priorizando la **consistencia** sobre la cantidad:

### 1. Instagram (Tu canal principal)
*   **Feed (Posts/Carruseles):** 3 veces por semana (ej: Lunes, Miércoles, Viernes).
    *   *Lunes:* Educativo/Valor (ej: "Por qué `Aurora` es diferente a las cremas de `Skin Lab`").
    *   *Miércoles:* Producto/Demo (ej: Tutorial de `Sol` para un look de oficina en Bogotá).
    *   *Viernes:* Lifestyle/Prueba Social (ej: Reseña de `Luna` o un "antes y después").
*   **Stories:** Diarias (5-7 al día).
    *   Muestra el "detrás de cámaras", encuestas, Q&A, y repostea a clientes bogotanos. Esto mantiene la marca "viva" en la parte superior de la pantalla.
*   **Reels:** 2-3 veces por semana.
    *   Formato clave para alcance orgánico. Usa audios en tendencia con contenido rápido y visualmente atractivo.

### 2. TikTok (Tu canal de alcance masivo)
*   **Publicaciones:** 1 vez al día (o al menos 5 veces por semana).
    *   TikTok premia la frecuencia. Si no puedes publicar diario, alterna entre contenido de `Sol` (tutoriales rápidos), `Luna` (ASMR/texturas) y `Aurora` (testimonios de resultados).
    *   *Nota:* El contenido puede ser más "crudo" y auténtico aquí que en Instagram.

### 3. WhatsApp Business (No es "publicación", es "interacción")
*   **Estados:** 3-5 veces por semana.
    *   Similar a Instagram Stories, pero para tu lista de contactos y clientes. Úsalo para ofertas relámpago de `Luna`, recordatorios de reposición o nuevos lanzamientos de `Aurora`.
*   **Mensajes directos:** Proactivos pero no intrusivos.
    *   Responde en menos de 1 hora. Si un cliente consulta por `Sol`, envíale un video corto mostrando la textura.

### 4. Email Marketing (Retención)
*   **Frecuencia:** 1 vez por semana (ej: Viernes de mañana).
    *   No satures. Envía valor: tips de cuidado, novedades, o una oferta exclusiva para suscriptores de Bogotá.

### Resumen Visual de tu Semana Orgánica:
| Día | Instagram (Feed/Stories) | TikTok | WhatsApp (Estados) |
| :--- | :--- | :--- | :--- |
| **Lunes** | Post Educativo + Stories | Video Rápido (Sol) | Encuesta/Q&A |
| **Martes** | Stories (Detrás de cámaras) | Video Tutorial (Luna) | Testimonio Cliente |
| **Miércoles** | Post Demo (Aurora) + Stories | Video "Día a Día" | Oferta Relámpago (Luna) |
| **Jueves** | Stories (Interacción) | Video Educativo (Aurora) | Recordatorio Reposición |
| **Viernes** | Post Lifestyle/Prueba Social + Stories | Video Trending (Sol) | Newsletter Link |
| **Sábado** | Stories (Lifestyle) | (Opcional: Repost de UGC) | (Descanso o casual) |
| **Domingo** | Stories (Preparación Semana) | (Descanso o Repost) | (Descanso) |

**Consejo clave:** Usa **Contenido UGC (User-Generated Content)**. Anima a tus primeras clientas en Bogotá a enviar videos usando `Sol` o `Luna`. Repostea ese contenido. Es más auténtico y genera más confianza que tu marca sola.

¿Quieres que te dé 3 ideas concretas de guiones para tus primeros 3 Reels de TikTok, enfocados en cada producto?

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo



Para productos de skincare como tu set 'Aurora' y tu crema 'Luna', el contenido que mejor funciona es aquel que demuestra **resultados tangibles** y **educación**. Aquí están los formatos más efectivos:

1. **Pruebas de Textura y Aplicación (ASMR Visual):**
   *   **Por qué funciona:** El skincare es táctil. Los videos en primer plano (macro) mostrando la textura de la crema 'Luna' o la consistencia de los sérums de 'Aurora' generan satisfacción visual y ayudan al cliente a imaginar cómo se sentirá en su piel.
   *   **Formato:** Reels o TikToks de 15-30 segundos sin música fuerte, solo sonidos de la aplicación y voz en off suave explicando la absorción.

2. **Antes y Después (Prueba Social Real):**
   *   **Por qué funciona:** Es el argumento de venta más poderoso. Muestra la evolución de la piel en 7, 14 o 30 días.
   *   **Formato:** Carruseles en Instagram o videos de transición en TikTok. Asegúrate de que las fotos tengan la misma iluminación para que sean creíbles. Usa testimonios reales de clientas de Bogotá para generar confianza local.

3. **Contenido Educativo ("¿Por qué funciona?"):**
   *   **Por qué funciona:** Diferencia tu marca de competidores genéricos. Explica los ingredientes clave de 'Aurora' (ej: ¿por qué es premium? ¿qué activos tiene?) y cómo combaten problemas comunes en la piel bogotana (contaminación, altitud).
   *   **Formato:** Videos cortos de "Profe Camila" (o tu marca personal) explicando un mito vs. realidad, o un carrusel con infografías simples.

4. **Rutinas Paso a Paso (Cómo usarlo):**
   *   **Por qué funciona:** Reduce la fricción de compra. Muchos clientes no saben cómo combinar productos.
   *   **Formato:** Video mostrando la secuencia exacta: Limpieza -> 'Aurora' -> Hidratación con 'Luna'. Incluye tips para el día vs. la noche.

5. **Detrás de Cámaras y Humanización:**
   *   **Por qué funciona:** Conecta emocionalmente. Muestra el empaque, el proceso de envío en Bogotá, o por qué elegiste esos ingredientes naturales.
   *   **Formato:** Stories y Reels casuales. Muestra la cara detrás de la marca.

**Clave para tu mercado:** Enfócate en **problemas específicos de la piel en Bogotá** (contaminación, clima frío/húmedo) y cómo tus productos los resuelven. Esto hace que el contenido sea hiperrelevante para tu audiencia local.

¿Te gustaría que desarrolle un guion detallado para un video de "Antes y Después" enfocado en el set 'Aurora'?

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo



Para diferenciarte de `Botica Verde` y `Skin Lab` sin bajar precios, debes atacar sus puntos débiles típicos: la frialdad clínica o la masificación. Tu ventaja es la **personalización, la experiencia y la conexión local**.

Aquí tienes 4 pilares estratégicos para tu diferenciación:

### 1. Diferenciación por "Experiencia de Unboxing" (El factor sorpresa)
*   **Competencia:** `Botica Verde` y `Skin Lab` suelen enviar en cajas de cartón genéricas o bolsas de polietileno.
*   **Tu Estrategia:** Convierte el envío en un evento.
    *   Usa papel de seda con tu logo.
    *   Incluye una tarjeta manuscrita (o que parezcalo) de agradecimiento específica para Bogotá.
    *   **El detalle clave:** Para el set premium `Aurora`, incluye una muestra gratis de `Luna` o `Sol` (mini tamaño). Esto incentiva la prueba de tus otros productos sin costo adicional de producción alto.
    *   **Mensaje:** "Tu rutina de belleza merece un inicio bonito".

### 2. Diferenciación por Asesoría Hiper-Personalizada (El factor humano)
*   **Competencia:** Son grandes tiendas; la atención es masiva, a menudo robótica o automatizada.
*   **Tu Estrategia:** Posiciónate como "Tu experta de belleza en Bogotá".
    *   **Para `Aurora` (Premium):** Ofrece una consulta gratuita de 10 minutos por WhatsApp antes de la compra. Analiza el tipo de piel de la clienta y recoméndale cómo usar el set. Esto justifica el precio premium porque vendes *solución*, no solo producto.
    *   **Para `Sol` y `Luna`:** Crea "Rutinas Bogotá". Ej: "Rutina Anti-contaminación para el tráfico de la 26" o "Rutina Anti-humedad para Chapinero". Adapta el lenguaje a su vida real.

### 3. Diferenciación por Agilidad y Conexión Local (El factor velocidad/confianza)
*   **Competencia:** Envíos nacionales que pueden tardar días o llegar a puntos de recogida lejanos.
*   **Tu Estrategia:**
    *   **Envío Express en Bogotá:** "Recíbelo mañana en Bogotá". Si puedes ofrecer recolección en puntos estratégicos (ej: zonas como Usaquén, El Retiro, Zona T) sin costo extra para compras sobre cierto monto, gana mucha lealtad.
    *   **Comunidad Local:** Haz sorteos exclusivos para Bogotá o colaboraciones con influencers micro-locales (de barrios específicos) en lugar de influencers nacionales genéricos.

### 4. Diferenciación por Transparencia y Educación (El factor confianza)
*   **Competencia:** Suelen enfocarse en la promesa del producto ("piel perfecta").
*   **Tu Estrategia:** Enfócate en el *proceso* y la *naturalidad*.
    *   Crea contenido que explique *por qué* usas ingredientes naturales (para `Sol`) o por qué tu fórmula `Aurora` es más efectiva que las químicas agresivas.
    *   Sé transparente sobre los tiempos de entrega y el origen de los insumos. La honestidad genera confianza en un mercado saturado de promesas vacías.

**Resumen de tu Propuesta de Valor vs. Competencia:**

| Característica | Botica Verde / Skin Lab | Tu Marca (Camila) |
| :--- | :--- | :--- |
| **Enfoque** | Clínico / Genérico | Personalizado / Local |
| **Atención** | Masiva / Automatizada | Humana / Asesora |
| **Experiencia** | Funcional (Recibir un producto) | Emocional (Unboxing + Asesoría) |
| **Velocidad** | Estándar Nacional | Express Local (Bogotá) |

**Acción Inmediata:**
¿Te gustaría que diseñemos el guion para un mensaje de WhatsApp tipo "Asesoría Express" que puedas enviar a las personas que consulten por `Aurora`? Así puedes empezar a implementar la diferenciación humana hoy mismo.

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo



Para el primer trimestre, enfócate en KPIs que validen tu modelo, optimicen tu inversión y midan la salud real de cada producto. Aquí los esenciales, agrupados por área, con metas realistas para tu etapa y tu mercado en Bogotá:

### 📈 Adquisición & Efectividad Publicitaria
| KPI | Qué mide | Meta Q1 | Por qué importa para ti |
|-----|----------|---------|------------------------|
| **CAC** (Costo por Adquisición) | Gasto marketing / Nuevos clientes | `< $15.000 COP` | Valida si tus campañas en Bogotá son rentables antes de escalar. |
| **ROAS** | Ingresos generados / Gasto publicitario | `> 3.0x` | Te dice si puedes reinvertir sin quemar capital. Crucial para `Sol` y `Luna`. |
| **Distribución Geográfica** | % de tráfico/ventas desde Bogotá | `> 85%` | Evita desperdiciar presupuesto fuera de tu mercado único. |

### 🛒 Conversión & Comportamiento de Compra
| KPI | Qué mide | Meta Q1 | Por qué importa para ti |
|-----|----------|---------|------------------------|
| **Tasa de Conversión** | Compras / Sesiones totales | `2.0% - 2.5%` | Benchmark real para belleza online en Colombia. Si está bajo, el problema suele ser landing, precio o confianza. |
| **Ticket Promedio (AOV) por Producto** | Venta promedio agrupada por producto | `Aurora > $120k | Sol ~$65k | Luna ~$35k` | Detecta si el upsell/cross-sell funciona y si tu posicionamiento por precio se mantiene. |
| **Tasa de Abandono de Carrito** | Carritos abandonados / Carritos creados | `< 65%` | En belleza supera el 70% si no hay recuperación ágil. Activa WhatsApp/email si pasa de 65%. |

### 🔄 Retención & Salud Operativa
| KPI | Qué mide | Meta Q1 | Por qué importa para ti |
|-----|----------|---------|------------------------|
| **Tasa de Recompra** | Clientes que compran 2da vez en 30-90 días | `15% - 20%` | Validación real de producto. Si `Luna` no recompra, no habrá escalado a `Sol`/`Aurora`. |
| **Sell-Through Rate** | Unidades vendidas / Unidades recibidas | `> 60% en 60 días` | Controla inventario. Evita quiebres de `Aurora` (premium) o sobrestock de `Luna`. |
| **Tasa de Devoluciones/Quejas** | Pedidos con reclamo o devolución | `< 3%` | En skincare, >5% suele indicar descripción engañosa, fórmula no adaptada o logística deficiente. |

### 💬 Canal & Experiencia (Diferenciador vs. Competencia)
| KPI | Qué mide | Meta Q1 | Por qué importa para ti |
|-----|----------|---------|------------------------|
| **Conversión desde WhatsApp** | Compras generadas / Mensajes atendidos | `> 25% de tus ventas totales` | En Colombia, WhatsApp cierra ventas de belleza. Mide si tu asesoría manual funciona. |
| **Tiempo de Respuesta + NPS Simple** | < 15 min en horario laboral / Encuesta post-compra | `NPS > 40` | Tu ventaja sobre `Botica Verde` y `Skin Lab` es la atención humana y cercana. |

### 📊 Cómo implementarlo en tu primer trimestre
1. **Segmenta por producto** en tu plataforma (Shopify/WooCommerce/MercadoLibre) para ver AOV, sell-through y recompra por `Aurora`, `Sol` y `Luna` por separado.
2. **Revisión semanal de 15 min:** Cada lunes toma 9 datos, identifica el que está fuera de meta y ajusta 1 acción (ej: si CAC sube, cambia creatividades o audiencia; si abandono >65%, activa mensaje de WhatsApp automático).
3. **Herramientas ligeras:** Meta Ads Manager, TikTok Analytics, GA4, WhatsApp Business (con etiquetas y respuestas rápidas), y una hoja de cálculo con fórmulas automáticas.

¿Quieres que te arme una **plantilla de seguimiento semanal (Google Sheets)** con fórmulas listas para calcular estos KPIs, alertas visuales si sales de meta, y un cronograma de revisión de 12 semanas para tu Q1? Puedo dártela estructurada y lista para copiar.

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo



Aquí tienes el plan de campaña de 4 semanas para **Aurora**, tu set de cuidado facial premium, diseñado para posicionarlo como la opción superior en Bogotá:

### 🎯 **Objetivo de la Campaña**
*   **Primario:** Posicionar **Aurora** como el estándar de lujo y eficacia en el cuidado facial bogotano.
*   **Secundario:** Generar una lista de clientes "Premium" (que comprarán **Aurora** en el futuro) y validar el mensaje de "experiencia y asesoría personalizada".

---

### 👥 **Audiencia Objetivo (Bogotá)**
*   **Segmento Principal:** Mujeres de 25 a 45 años en Bogotá (específicamente en zonas de alto poder adquisitivo: Usaquén, Chicó, Rosales, La Candelaria y Chapinero Alto).
*   **Intereses:** Skincare de lujo, ingredientes naturales, bienestar holístico, marcas premium de belleza (ej: La Mer, Sunday Riley, Kiehl's).
*   **Comportamiento:** Compradoras online frecuentes, interesadas en "experiencias de compra" y "asesoría personalizada".

---

### 📢 **Mensaje Principal (Propuesta de Valor de Aurora)**
> **"Aurora: Tu ritual de belleza premium en Bogotá. No es solo un set, es una experiencia de cuidado facial personalizado, con ingredientes de alta eficacia y la asesoría experta que solo tú mereces."**

---

### 📅 **Plan de Acción por Semanas**

| Semana | Enfoque | Canales | Acciones Clave |
| :--- | :--- | :--- | :--- |
| **Semana 1** | **Lanzamiento & Expectativa** | Instagram (Stories/Reels) + TikTok | **Contenido:** "Detrás de Aurora" (ingredientes, proceso de elaboración, el "por qué" es premium). <br>**CTA:** "Reserva tu asesoría gratuita de 10 min para saber si Aurora es para ti". |
| **Semana 2** | **Prueba Social & Diferenciación** | Instagram (Feed/Ads) + WhatsApp | **Contenido:** Testimonios reales de primeras clientas en Bogotá. Comparativa sutil: "Aurora vs. Rutina Genérica". <br>**CTA:** "Últimas unidades de Aurora con envío express en Bogotá". |
| **Semana 3** | **Educación & Valor** | Instagram (Carruseles) + Email | **Contenido:** "Los 3 errores comunes en tu rutina facial y cómo Aurora los corrige". <br>**CTA:** "Agenda tu sesión de diagnóstico de piel con Camila". |
| **Semana 4** | **Cierre & Escasez** | Instagram Stories + WhatsApp | **Contenido:** "El ritual Aurora completo: ¿Por qué funciona?" (Video de 60s). <br>**CTA:** "Oferta de lanzamiento: Muestra gratis de Luna con tu compra de Aurora" (Solo para los últimos 5 días). |

---

### 📊 **Métricas de Éxito (KPIs para Aurora)**
1.  **CAC (Costo por Adquisición) de Aurora:** Meta `< $25.000 COP` (más alto que los otros productos, justificado por el precio premium).
2.  **Tasa de Conversión de Landing Page de Aurora:** Meta `> 3.0%` (Debe ser más alta que el promedio general debido a la calidad del tráfico y la oferta).
3.  **Tasa de Agendamiento de Asesoría:** Meta `> 15%` de los que visitan la página de Aurora. (Valida el interés real y la propuesta de valor).
4.  **Ticket Promedio (AOV) de Aurora:** Meta `> $120.000 COP` (Asegura que el posicionamiento premium se mantiene).
5.  **NPS (Satisfacción) Post-Compra:** Meta `> 50` (Para validar la experiencia "premium" y la asesoría).

¿Quieres que desarrolle el **guion detallado para el Reel de la Semana 1** ("Detrás de Aurora") y el **texto para el mensaje de WhatsApp de la asesoría gratuita**?


## Respuesta completa



Aquí tienes el plan de campaña de 4 semanas para **Aurora**, tu set de cuidado facial premium, diseñado para posicionarlo como la opción superior en Bogotá:

### 🎯 **Objetivo de la Campaña**
*   **Primario:** Posicionar **Aurora** como el estándar de lujo y eficacia en el cuidado facial bogotano.
*   **Secundario:** Generar una lista de clientes "Premium" (que comprarán **Aurora** en el futuro) y validar el mensaje de "experiencia y asesoría personalizada".

---

### 👥 **Audiencia Objetivo (Bogotá)**
*   **Segmento Principal:** Mujeres de 25 a 45 años en Bogotá (específicamente en zonas de alto poder adquisitivo: Usaquén, Chicó, Rosales, La Candelaria y Chapinero Alto).
*   **Intereses:** Skincare de lujo, ingredientes naturales, bienestar holístico, marcas premium de belleza (ej: La Mer, Sunday Riley, Kiehl's).
*   **Comportamiento:** Compradoras online frecuentes, interesadas en "experiencias de compra" y "asesoría personalizada".

---

### 📢 **Mensaje Principal (Propuesta de Valor de Aurora)**
> **"Aurora: Tu ritual de belleza premium en Bogotá. No es solo un set, es una experiencia de cuidado facial personalizado, con ingredientes de alta eficacia y la asesoría experta que solo tú mereces."**

---

### 📅 **Plan de Acción por Semanas**

| Semana | Enfoque | Canales | Acciones Clave |
| :--- | :--- | :--- | :--- |
| **Semana 1** | **Lanzamiento & Expectativa** | Instagram (Stories/Reels) + TikTok | **Contenido:** "Detrás de Aurora" (ingredientes, proceso de elaboración, el "por qué" es premium). <br>**CTA:** "Reserva tu asesoría gratuita de 10 min para saber si Aurora es para ti". |
| **Semana 2** | **Prueba Social & Diferenciación** | Instagram (Feed/Ads) + WhatsApp | **Contenido:** Testimonios reales de primeras clientas en Bogotá. Comparativa sutil: "Aurora vs. Rutina Genérica". <br>**CTA:** "Últimas unidades de Aurora con envío express en Bogotá". |
| **Semana 3** | **Educación & Valor** | Instagram (Carruseles) + Email | **Contenido:** "Los 3 errores comunes en tu rutina facial y cómo Aurora los corrige". <br>**CTA:** "Agenda tu sesión de diagnóstico de piel con Camila". |
| **Semana 4** | **Cierre & Escasez** | Instagram Stories + WhatsApp | **Contenido:** "El ritual Aurora completo: ¿Por qué funciona?" (Video de 60s). <br>**CTA:** "Oferta de lanzamiento: Muestra gratis de Luna con tu compra de Aurora" (Solo para los últimos 5 días). |

---

### 📊 **Métricas de Éxito (KPIs para Aurora)**
1.  **CAC (Costo por Adquisición) de Aurora:** Meta `< $25.000 COP` (más alto que los otros productos, justificado por el precio premium).
2.  **Tasa de Conversión de Landing Page de Aurora:** Meta `> 3.0%` (Debe ser más alta que el promedio general debido a la calidad del tráfico y la oferta).
3.  **Tasa de Agendamiento de Asesoría:** Meta `> 15%` de los que visitan la página de Aurora. (Valida el interés real y la propuesta de valor).
4.  **Ticket Promedio (AOV) de Aurora:** Meta `> $120.000 COP` (Asegura que el posicionamiento premium se mantiene).
5.  **NPS (Satisfacción) Post-Compra:** Meta `> 50` (Para validar la experiencia "premium" y la asesoría).

¿Quieres que desarrolle el **guion detallado para el Reel de la Semana 1** ("Detrás de Aurora") y el **texto para el mensaje de WhatsApp de la asesoría gratuita**?