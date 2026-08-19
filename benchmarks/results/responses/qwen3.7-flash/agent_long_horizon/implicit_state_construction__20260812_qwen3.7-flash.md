# Qwen 3.7 Flash — agent_long_horizon/implicit_state_construction

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 7.78 | quality: 8.5
- latency_total: 161.344s | tokens_per_second: 107.0
- input_tokens: 16033 | output_tokens: 17323

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

Hola Camila, gracias por compartir esa información. Tengo completamente claro el contexto de tu negocio:

- **Ubicación y mercado:** Tienda online con enfoque exclusivo en **Bogotá**.
- **Portafolio de productos:** 
  - `Aurora`: Set de cuidado facial → **precio premium**
  - `Sol`: Kit de maquillaje natural → **precio medio**
  - `Luna`: Crema corporal → **precio entrada/accesible**
- **Competencia directa:** `Botica Verde` y `Skin Lab`, ambas operando en Bogotá.

Con estos datos ya tengo la base estructurada para ayudarte a diseñar campañas publicitarias, definir públicos objetivo, redactar mensajes diferenciados por producto, establecer presupuestos y comparar estrategias frente a tus dos competidores, sin necesidad de volver a consultar esta información.

¿Te gustaría comenzar analizando algún producto en concreto, definiendo un objetivo de campaña (ventas, reconocimiento, retención, etc.) o revisando cómo posicionarte frente a Botica Verde y Skin Lab?

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Para las bogotanas que buscan una rutina de belleza integral, ofrecemos una selección curada de productos que cubren desde el cuidado facial premium hasta el maquillaje natural y el corporal accesible, todo con entrega ágil y soporte personalizado en la ciudad. Nuestra propuesta combina calidad, ingredientes cuidadosamente seleccionados y precios escalonados por necesidad, garantizando una experiencia de belleza clara, confiable y adaptada a cada etapa de tu día a día.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Basado en tu modelo de negocio y tu enfoque exclusivo en Bogotá, te recomiendo priorizar estos cuatro canales digitales, ordenados por impacto inicial y alineados con tu mezcla de precios:

### 1. **Instagram + Meta Ads (Eje principal)**
- **Por qué priorizarlo:** Es la plataforma dominante en belleza en Colombia. Permite segmentación geográfica exacta (solo Bogotá + radios de entrega), formatos visuales que venden por sí solos y cierre directo desde el feed.
- **Aplicación por producto:**
  - `Aurora` (premium): Reels con explicación de activos/beneficios, carruseles “cómo usarlo en 3 pasos”, ads de conversión con copy enfocado en resultados y exclusividad.
  - `Sol` (medio): Stories con encuestas (“¿tono para hoy?”), catálogos shoppable, colaboraciones con microinfluencers bogotanas de nicho (estilo natural/minimalista).
  - `Luna` (entrada): Remarketing dinámico, anuncios de “combo económico”, UGC real de clientas locales.
- **Clave operativa:** Usa creatividades con contexto urbano bogotano (referencias sutiles a clima, transporte o estilo de vida local) para reforzar cercanía y confianza en la entrega.

### 2. **TikTok (Alcance + Virilidad orgánica)**
- **Por qué priorizarlo:** Bajo costo de adquisición y alto engagement en el segmento 18–35 años. Los tutoriales, rutinas y unboxings generan prueba social rápida.
- **Estrategia:** Contenido auténtico tipo “mi rutina completa en <5 min”, comparativas de textura/acabado sin nombrar competidores, challenges con hashtags locales (`#SkincareBOG`, `#MaquillajeNaturalColombia`). Impulsa con Spark Ads solo los videos que ya organicen >3% de tasa de finalización.

### 3. **Google Ads (Search + Shopping)**
- **Por qué priorizarlo:** Captura intención de compra activa. Muchas usuarias buscan términos como “kit maquillaje natural Bogotá”, “crema corporal económica” o “set facial premium entrega rápida”.
- **Estrategia:** Campañas de búsqueda con keywords geolocalizadas, Shopping Ads con fotos limpias y precios visibles, extensiones de promoción y horarios. Ideal para convertir tráfico frío en venta, especialmente en `Sol` y `Luna`.

### 4. **WhatsApp Business + Email (Retención y LTV)**
- **Por qué priorizarlo:** En Colombia el comercio conversacional tiene tasas de apertura >90%. Reduce dependencia de algoritmos y aumenta el valor de vida del cliente.
- **Uso táctico:** Catálogo integrado, respuestas rápidas con guía de selección según presupuesto, secuencia post-compra (instrucciones de uso + recomendación cruzada: ej. quien compra `Luna` recibe tips para `Sol`), recuperación de carritos abandonados en <2h.

---

**Recomendación de lanzamiento:**  
Comienza invirtiendo el **60% en Instagram/Meta**, **20% en TikTok (orgánico + Spark Ads)**, **15% en Google Shopping/Search** y **5% en herramientas de email/WhatsApp**. Esto te permite validar mensajes, escalar lo que funciona y proteger tu margen con retención automatizada.

¿Quieres que te arme un calendario de contenidos de 30 días para Instagram/TikTok, o prefieres que definamos los KPIs y estructura de campañas pagadas por producto?

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Para mantener visibilidad orgánica sin saturar tu equipo ni perder consistencia, te recomiendo esta cadencia realista y alineada al comportamiento algorítmico actual en Colombia:

### 📸 **Instagram**
- **Feed / Reels:** 3–4 publicaciones por semana  
- **Stories:** Diarias (5–10 fotogramas/día)  
- *Por qué:* Instagram premia la presencia constante. Las Stories mantienen tu cuenta “activa” ante el algoritmo entre publicaciones, mientras que Reels y carruseles son los motores de descubrimiento. En el nicho de belleza, la interacción diaria construye confianza y reduce la fricción para comprar `Sol` o `Luna`.

### 🎵 **TikTok**
- **Videos:** 3–5 publicaciones por semana  
- *Por qué:* TikTok prueba contenido en ventanas de 24–72 horas. Subir 3–5 videos/semana maximiza las oportunidades de viralidad orgánica sin exigir producción cinematográfica. El formato debe sentirse nativo: grabado con celular, ritmo ágil y enfoque en problema/solución.

### 🔁 **Estrategia operativa clave (para no quemarte)**
No creas contenido desde cero por canal. Aplica este flujo de repurposing:
1. Grabas **1 video vertical largo** (ej. “Mi rutina completa en 5 min”) → lo divides en:
   - 1 Reel/TikTok principal
   - 2–3 clips cortos para Stories/Reels secundarios
   - 3–4 imágenes estáticas para carrusel IG
2. Alineas los **pilares temáticos** con tu mezcla de precios:
   - `Aurora` (premium): beneficios clínicos, texturas, cuidado nocturno, “por qué vale la inversión”
   - `Sol` (medio): tutoriales rápidos, looks para oficina/fines de semana, comparativas de acabado
   - `Luna` (entrada): rutinas post-ducha, hidratación en clima frío de Bogotá, combos accesibles
3. Agendas todo en bloques: 1 sesión de grabación quincenal = 10–12 piezas listas para programar.

¿Quieres que te entregue un calendario semanal tipo plantilla (con horarios óptimos para Bogotá, distribución exacta de temas por producto y guiones base para Reels/TikTok)?

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

En skincare, el contenido que genera confianza y convierte son aquellos que combinan **educación práctica, prueba visual real y contexto local**. Aquí los formatos con mayor rendimiento, aplicados directamente a tu catálogo y mercado:

### 🔹 1. Rutinas paso a paso (Reels / TikTok)
- **Por qué funciona:** El 68% de las usuarias de belleza buscan instrucciones claras antes de añadir un producto a su carrito.
- **Aplicación por producto:**
  - `Aurora` (premium): “Rutina nocturna anti-luz azul en 3 pasos” → enfatiza concentración de activos, textura, absorción y por qué justifica el precio alto.
  - `Sol` (medio): “De oficina a plan en 2 minutos” → muestra versatilidad, acabado natural y cómo se integra con base/skincare.
  - `Luna` (entrada): “Hidratación post-ducha para clima frío de Bogotá” → enfoque práctico, resultados inmediatos y relación calidad-precio.

### 🔹 2. UGC auténtico + antes/después controlados
- **Por qué funciona:** En cuidado de piel, la duda central es “¿me funcionará a mí?”. Los videos grabados con celular por clientas reales superan al contenido pulido en tasa de guardados y conversiones.
- **Cómo escalarlo:** Activa un programa de microinfluencers bogotanas (5k–50k) a cambio de producto + código único. Pide siempre mostrar textura, aplicación en piel real y frase clave contextualizada (“Lo uso en inviernos sin resequedad”, “No deja residuos bajo maquillaje”).

### 🔹 3. Educación por problema/ingrediente (Carruseles IG)
- **Por qué funciona:** Posiciona tu marca como experta y justifica tu escala de precios sin parecer elitista.
- **Ejemplos alineados a tu portafolio:**
  - `Aurora`: “3 señales de que tu crema facial no está penetrando” → introduce el set como solución técnica, no cosmética.
  - `Sol`: “Ingredientes naturales que sí cumplen (y los que no)” → desmitifica tendencias, muestra origen/certificaciones, atrae a quienes buscan equilibrio entre eficacia y precio medio.
  - `Luna`: “Hidratantes económicos vs. premium: ¿cuándo vale la pena invertir?” → posiciona Luna como opción inteligente, no “barata”, y abre puerta a cross-selling hacia Sol/Aurora.

### 🔹 4. Contenido contextual-local (Stories + Reels efímeros)
- **Por qué funciona:** La cercanía geográfica reduce fricción logística y aumenta la percepción de marca cercana.
- **Ideas accionables:** “Tu piel en Bogotá: cómo ajustar tu rutina según la temporada”, “Entrega en <24h en comunas específicas”, o comparativas indirectas con competidores (“Si buscas X, aquí está Y con Z beneficio adicional”) sin nombrar a Botica Verde ni Skin Lab (evita exposición negativa y cumple normativa de publicidad comparativa en Colombia).

### ⚙️ Claves operativas
- Usa siempre **texto superpuesto** (muchas ven sin sonido), **audio trending moderado** y CTAs educativos (“Guárdalo para tu próxima rutina”, “Pregunta en DM para elegir tu capa”).
- Evita claims médicos o “cura/reemplaza tratamientos dermatológicos” (normativa INVIMA exige lenguaje cuidadoso en cosméticos).
- Métrica prioritaria: **retención al segundo 3, guardados y compartidos** (indicadores de valor real), no solo likes o vistas.

¿Quieres que te entregue 3 guiones listos para grabar (uno por producto) con hooks probados, tiempos exactos, sugerencias de audio y descripciones optimizadas para búsqueda en español?

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Para diferenciarte de **Botica Verde** y **Skin Lab** sin tocar precios, debes competir en **valor percibido, experiencia y relevancia contextual**. Aquí tienes un plan estructurado en 5 pilares aplicables directamente a tu portafolio y mercado bogotano:

### 🔑 1. Vende Rutinas Adaptadas, No Productos Aislados
- **Implementación:** Crea un quiz interactivo en tu web (`Tipo de piel + clima de Bogotá + estilo de vida → combinación Aurora/Sol/Luna`). Entrega un plan de 4 semanas con horarios, cantidades y advertencias específicas.
- **Diferenciación:** Tus competidores probablemente muestran catálogos estáticos. Tú posicionas tu tienda como **consejera de belleza local**, lo que justifica el precio premium de `Aurora`, facilita la adopción de `Sol` y naturaliza `Luna` como base de cuidado, no producto descartable.
- **KPI:** Tasa de conversión del quiz → carrito (%), ticket promedio por recomendación cruzada.

### 🌧️ 2. Identidad “Hecha Para El Clima y Ritmo de Bogotá”
- **Implementación:** Ajusta mensajes técnicos al contexto urbano: texturas que no oxiden bajo mascarilla, fórmulas que resistan la humedad relativa alta, empaques que aguanten transporte en moto-taxi, entregas programadas según zonas (Centro, Usaquén, Suba, etc.).
- **Diferenciación:** Botica Verde y Skin Lab operan con narrativa nacional/genérica. Tú lideras el **nicho geográfico emocional**: “Entendemos cómo afecta el frío, la altitud y la contaminación a tu piel y cuerpo”. Esto reduce fricción logística y aumenta percepción de cercanía.
- **KPI:** % de menciones orgánicas citando “clima/comuna de Bogotá”, tasa de recompra en <60 días.

### 📦 3. Unboxing Con Propósito + Postventa Sin Fricción
- **Implementación:** 
  - Empaque reutilizable (caja que se transforma en organizador de tocador o estuche de viaje).
  - Incluye una tarjeta física con código QR a un video tuyo explicando cómo usar cada pieza según su rutina.
  - Política clara: “Si al completar tu primera semana no ves el beneficio prometido, te cambiamos el producto o devolvemos el valor sin preguntas”.
- **Diferenciación:** En belleza online, la incertidumbre post-compra mata la recompra. Al eliminar riesgo percibido y convertir la entrega en momento de marca, elevas el valor percibido independientemente del precio.
- **KPI:** Tasa de devolución/reclamo (<2%), NPS post-entrega, % de clientes que comentan el unboxing en redes.

### 💬 4. Soporte Experto Accesible (WhatsApp + Micro-Consultas)
- **Implementación:** 
  - Triaje automatizado en WhatsApp Business que clasifique por necesidad (`Aurora` → anti-edad/sensibilidad, `Sol` → tono/acabado, `Luna` → hidratación/descamación).
  - Ofrece 2 sesiones mensuales de “consultas rápidas” (15 min por videollamada o audio) para clientas frecuentes. Graba las dudas más comunes y conviértelas en carruseles o Reels.
- **Diferenciación:** La mayoría de competidores responden con FAQs genéricas. Tú compites en **proximidad técnica**, lo que aumenta confianza en `Aurora`, reduce dudas de compra en `Sol` y fideliza compras recurrentes de `Luna`.
- **KPI:** Tiempo medio de respuesta (<2h en horario laboral), % de conversiones tras consulta, retención a 90 días.

### 📚 5. Contenido Como Autoridad, No Catálogo Digital
- **Implementación:** 
  - Serie fija semanal: *“Piel en Bogotá”* (ajustes por temporada, contaminación, estrés urbano).
  - Desmitifica tendencias sin nombrar competidores: “¿Por qué algunos kits naturales irritan en invierno?”, “La diferencia entre ‘hidratante’ y ‘oclusivo’ y cuándo usar cada uno”.
  - Invita a profesionales locales (dermatólogas, nutricionistas, terapeutas) a lives rotativos.
- **Diferenciación:** Competir en precio atrae compradores sensibles al costo. Competir en conocimiento atrae **compradores sensibles a resultados**, que son más leales y pagan mejor por claridad técnica.
- **KPI:** Guardados/compartidos, tasa de finalización en videos >30s, tráfico cualificado desde LinkedIn/IG a la web.

---

### 🛠️ Hoja de Ruta Rápida (Primeros 45 Días)
| Semana | Acción clave | Producto focal | Canal principal |
|--------|--------------|----------------|-----------------|
| 1–2    | Lanzar quiz + política postventa | Todos | Web + WhatsApp |
| 3      | Grabar 3 Reels/TikTok tipo “Piel en Bogotá” | Aurora + Luna | IG/TikTok |
| 4      | Implementar unboxing físico + tarjeta QR | Sol + Luna | Envíos reales |
| 5–6    | Activar micro-consultas + grabar Q&A | Aurora | Instagram Live + Stories |
| 7–8    | Analizar datos, escalar formato ganador | Según conversión | Meta Ads + Orgánico |

¿Quieres que te arme el guion del quiz interactivo, la estructura de la política postventa alineada a INVIMA, o un calendario de contenidos de 30 días enfocado en estos pilares?

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Para tu primer trimestre (fase de **validación y construcción de base**), te sugiero medir solo los KPIs que te permitan tomar decisiones operativas, validar tu propuesta frente a Botica Verde y Skin Lab, y establecer líneas base realistas. He organizado los indicadores por área, con su propósito, meta orientativa para Colombia/DTC belleza y cómo rastrearlos:

### 📊 KPIs Clave por Área (Trimestre 1)

| Área | KPI | Por qué importa en tu caso | Meta orientativa Q1 | Cómo medirlo |
|------|-----|----------------------------|---------------------|--------------|
| **Adquisición** | Costo por Adquisición (CPA) / Costo por Venta (CPV) | Define si tus anuncios en IG/TikTok/Google son rentables sin depender de descuentos | CPA ≤ 25–30% del ticket promedio por canal | Meta Ads Manager, TikTok Ads, Google Ads + CRM/e-commerce |
| **Conversión Web** | Tasa de conversión (Visita → Compra) | Mide la efectividad de tu tienda, pasarela y propuesta de valor en Bogotá | 2.0% – 3.5% | GA4 / panel nativo de tu plataforma |
| **Portafolio** | Distribución de ventas por producto (%) | Valida si la escala de precios (Aurora/Sol/Luna) está generando el mix esperado | Aurora 25–35% \| Sol 35–45% \| Luna 25–35% | E-commerce dashboard + reportes por SKU |
| **Retención** | Tasa de recompra/cross-sell a 60 días | La belleza online depende del ciclo de uso; mide si tu estrategia de WhatsApp/unboxing funciona | ≥ 20% de clientes recurrentes | Email/WhatsApp tags + segmentación por fecha de primera compra |
| **Experiencia** | Abandono de carrito & tiempo en checkout | Detecta fricciones logísticas, de pago o de confianza típicas en Bogotá | Abandono < 65% \| Checkout completo en < 3 min | GA4 Ecommerce Events / Hotjar (si aplicas) |
| **Contenido Orgánico** | Tasa de guardados + compartidos (vs. likes) | Indicador real de valor educativo y autoridad en skincare/maquillaje | ≥ 3.5% sobre alcance | Insights de IG/TikTok (exportar datos semanales) |
| **Operativo** | % de entregas en <48h en Bogotá | Tu ventaja logística frente a competidores nacionales debe ser medible | ≥ 93% cumplimiento | Sistema de envíos (Rappi, Intercourier, Servientrega, etc.) + bitácora |
| **Financiero** | Margen bruto ponderado | Garantiza que `Aurora` cubra costos de adquisición y `Luna` mantenga volumen saludable | ≥ 62–65% global | Facturación - Costo de mercadería vendida (CMV) mensual |

---

### 🔍 Cómo implementarlo sin saturarte
1. **Dashboard único semanal:** Usa una hoja de cálculo o Looker Studio conectado a GA4, Meta Ads y tu plataforma. Actualiza cada lunes con datos de la semana anterior.
2. **Regla del 80/20 en análisis:** Solo profundiza en canales/productos donde:
   - CPA supere la meta por 2 semanas consecutivas, O
   - Conversión caiga <1.5%, O
   - Un producto represente >50% de ventas (riesgo de dependencia).
3. **Segmenta siempre por origen de tráfico:** Orgánico vs. Pagado vs. WhatsApp directo. El comportamiento bogotano cambia drásticamente entre quienes llegan por búsqueda activa (`Sol`/`Luna`) y quienes descubren por Reels (`Aurora`).

---

### 📅 Cadencia de Revisión Recomendada
- **Semanal (15 min):** CPA, conversión, abandones de carrito, entregas <48h.
- **Quincenal (30 min):** Distribución por producto, guardados/compartidos, tasa de recompra temprana.
- **Mensual (1 hora):** Margen ponderado, NPS rápido (3 preguntas vía email/WhatsApp), ajuste de presupuesto por canal.

¿Quieres que te entregue una **plantilla lista para copiar en Google Sheets** con fórmulas automáticas para estos KPIs, o prefieres que definamos los umbrales exactos de alerta por producto (ej. “Si Aurora baja de 28% de margen, activar promo cruzada con Luna”)?

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

Aquí tienes el plan de campaña de 4 semanas enfocado exclusivamente en **`Aurora`**, diseñado para posicionarse como referencia premium en skincare facial sin depender de descuentos ni entrar en competencia directa con `Botica Verde` o `Skin Lab`.

---

### 🎯 OBJETIVO DE LA CAMPAÑA
Conseguir **150 ventas unitarias de `Aurora`** en 4 semanas, manteniendo un **CPA ≤ $45.000 COP**, un **ROAS ≥ 2.8x** y una **tasa de conversión web ≥ 3.2%**. Simultáneamente, validar que `Aurora` funciona como ancla de valor que justifica la escala de precios y abre rutas de cross-selling hacia `Sol` y `Luna`.

---

### 👥 AUDIENCIA (Segmentación precisa)
- **Geografía:** Bogotá, radio 15 km del centro. Priorizar comunas con alto poder adquisitivo y densidad digital: Chapinero, Usaquén, Suba alta, Teusaquillo, Los Mártires, La Candelaria, Puente Aranda, Engativá norte, Fontibón, Rafael Uribe Uribe, Antonio Nariño, Santa Fe, San Cristóbal, Kennedy centro, Barrios Unidos.
- **Demografía:** Mujeres 25–45 años, ingresos medios-altos, profesiones/actividades con exposición urbana (oficina, emprendimiento, maternidad activa, vida social).
- **Psicografía:** Valoran ingredientes activos, rutinas estructuradas y resultados medibles. Se sienten impactadas por contaminación, luz azul, cambios climáticos bruscos y estrés urbano. Dispuestas a invertir en productos que ahorren tiempo y reduzcan fricción en su cuidado diario.
- **Comportamiento digital:** Consumen Reels/TikTok de dermatología y rutinas reales, revisan carruseles educativos antes de comprar, responden a anuncios con prueba social contextualizada, usan WhatsApp para resolver dudas técnicas.
- **Exclusiones:** Público nacional fuera de Bogotá, usuarios que solo interactúan con contenido de maquillaje puro (sin intención de skincare), listas de clientes existentes de `Luna`/`Sol` (para evitar duplicidad de inversión en esta fase).

---

### 📡 CANALES & DISTRIBUCIÓN DE PRESUPUESTO
| Canal | Peso | Función en la campaña | Formato prioritario |
|-------|------|------------------------|---------------------|
| Instagram + Meta Ads | 60% | Descubrimiento, consideración y conversión directa | Reels educativos, Stories interactivas, Carrousel técnico, Catálogo shoppable, Conversión/Dynamic |
| TikTok | 20% | Virilidad orgánica + amplificación de UGC real | Videos nativos tipo “rutina en vivo”, Spark Ads sobre piezas orgánicas con >3% retención al segundo 3 |
| Google Search | 15% | Captura de intención alta y protección de marca | Keywords geolocalizadas (“set facial premium Bogotá”, “rutina skincare anti-contaminación”), Shopping Ads |
| WhatsApp + Email | 5% | Recuperación, postventa y cross-selling | Secuencia automatizada post-compra, catálogo conversacional, recordatorio de aplicación semanal de `Aurora` |

---

### 💬 MENSAJE PRINCIPAL & ÁNGULOS CREATIVOS
**Mensaje núcleo:**  
> “`Aurora` no es un set facial más: es tu escudo contra el ritmo y el clima de Bogotá. Concentración clínica, textura que respira bajo contaminación y resultados visibles desde la segunda semana. Diseñado para mujeres que exigen más de su piel.”

**Ángulos rotativos (para testing creativo):**
1. **Técnico/Justificación de precio:** “Por qué `Aurora` tiene 3 pasos y no 7” → explica sinergias de activos y evita saturación cutánea.
2. **Contexto local:** “Tu piel en Bogotá: cómo `Aurora` compensa humedad, altitud y luz azul” → conecta producto con realidad urbana.
3. **Prueba social controlada:** Testimonios reales de bogotanas mostrando textura, absorción y adaptación bajo mascarilla o oficina.
4. **Rutina optimizada:** “15 min nocturnos con `Aurora` = mañana lista para todo” → posiciona ahorro de tiempo + eficacia.

*Nota de cumplimiento:* Lenguaje alineado a normativa INVIMA (cuidado cosmético, no claims médicos). Se evitan términos como “cura”, “elimina arrugas” o “reemplaza tratamientos”.

---

### 📊 MÉTRICAS DE ÉXITO (KPIs de campaña)
| Indicador | Meta | Umbral de alerta | Herramienta |
|-----------|------|------------------|-------------|
| Ventas unitarias `Aurora` | 150 | < 90 en semana 4 | E-commerce dashboard |
| CPA / Costo por venta | ≤ $45.000 COP | > $60.000 x 2 semanas consecutivas | Meta Ads, TikTok Ads, Google Ads |
| ROAS ponderado | ≥ 2.8x | < 2.0x | Plataforma + CRM |
| Tasa de conversión web | ≥ 3.2% | < 2.0% | GA4 / Panel nativo |
| Guardados + compartidos (orgánico/paid) | ≥ 4% sobre alcance | < 2.5% | Insights IG/TikTok |
| Abandono de carrito | < 60% | > 70% | GA4 Events + Hotjar (si aplica) |
| Open rate secuencia post-compra `Aurora` | > 45% | < 35% | Email/WhatsApp CRM |
| Cross-sell `Aurora` → `Sol`/`Luna` (30 días) | ≥ 15% | < 8% | Segmentación CRM |

---

### 🗓️ PLAN SEMANA A SEMANA

#### **Semana 1: Lanzamiento + Educación Técnica**
- **Enfoque:** Validar ángulo premium y generar primera base de conversión.
- **Tácticas:**
  - Publicar 3 Reels/TikTok tipo “Desglose técnico de `Aurora`” (activos, sinergias, textura).
  - Activar campaña Meta de Conversión con audiencia fría segmentada por intereses (skincare activo, dermatología estética, bienestar urbano).
  - Lanzar carrousel IG: “Los 3 errores que hacen que tu crema facial no penetre en Bogotá”.
  - Configurar pixel/GA4 + evento `InitiateCheckout` y `Purchase` con parámetro `product_name: 'Aurora'`.
- **Mensaje clave:** “`Aurora` está formulado para trabajar en capas, no en exceso.”

#### **Semana 2: Prueba Social + Contexto Local**
- **Enfoque:** Reducir fricción de compra mediante validación real y relevancia geográfica.
- **Tácticas:**
  - Activar Spark Ads con 2 videos de microinfluencers/clientas reales aplicando `Aurora` en contexto bogotano (oficina, transporte, clima).
  - Stories interactivas: Encuesta “¿Qué parte de tu rutina facial te toma más tiempo?” → link directo a landing de `Aurora`.
  - Campaña Google Search con keywords de intención alta + extensiones de promoción silenciosa (valor agregado, no descuento).
  - Enviar email/WhatsApp a leads calificados: “Así se adapta `Aurora` a tu clima y estilo de vida”.
- **Mensaje clave:** “`Aurora` fue probado en pieles expuestas al ritmo de Bogotá.”

#### **Semana 3: Conversión + Escasez Perceptiva**
- **Enfoque:** Maximizar ventas sin tocar precio, usando disponibilidad y acompañamiento.
- **Tácticas:**
  - Remarketing dinámico de `Aurora` para visitantes web, viewers de Reels >50% y abandonadores de carrito.
  - Live IG/Q&A: “Resuelve tus dudas sobre `Aurora` en 15 min” → enlace directo en bio/stories.
  - Actualizar landing page con badge “Entrega en <48h en Bogotá” + política post-compra clara.
  - Activar secuencia WhatsApp automatizada: mensaje día 1 (confirmación), día 3 (tips de aplicación), día 7 (recordatorio de reabastecimiento).
- **Mensaje clave:** “`Aurora` se agota cuando las rutinas se consolidan.”

#### **Semana 4: Retención + Cross-Selling Controlado**
- **Enfoque:** Consolidar recompra y abrir ruta hacia `Sol` y `Luna` sin diluir el posicionamiento premium.
- **Tácticas:**
  - Campaña de remarketing a compradores de `Aurora` con oferta cruzada: “Completa tu escudo facial con `Sol` (maquillaje que respeta tu barra cutánea) o `Luna` (hidratación corporal que no compite con tu rutina).”
  - Publicar UGC recopilado: “Lo que dicen quienes ya usan `Aurora` en Bogotá”.
  - Analizar KPIs, pausar anuncios con CPA > meta, reinvertir en formatos con retención >35% y guardados >4%.
  - Enviar encuesta NPS breve (3 preguntas) a compradores de `Aurora` con código de agradecimiento no monetario (ej. acceso anticipado a nuevos lanzamientos).
- **Mensaje clave:** “`Aurora` es solo el inicio de tu rutina integral.”

---

### ⚙️ NOTAS OPERATIVAS CLAVE
1. **Creatividad:** Todas las piezas deben mostrar `Aurora` en uso real, con texto superpuesto claro y audio trending moderado. Evitar fondos genéricos; usar contextos urbanos bogotanos sutiles.
2. **Presupuesto mínimo recomendado:** $1.8–2.2 millones COP/semana distribuido según el peso de canales. Ajustar diariamente si CPA supera el umbral de alerta.
3. **Cumplimiento normativo:** Mantener lenguaje cosmético-validado. No comparar directamente con `Botica Verde` o `Skin Lab`. Incluir disclaimer opcional en landing: “Resultados pueden variar según tipo de piel y adherencia a la rutina”.
4. **Integración CRM:** Etiquetar todos los contactos de `Aurora` en WhatsApp/email para activar secuencias de cross-selling post-campaña.

¿Quieres que te entregue la estructura exacta de la landing page optimizada para `Aurora`, los guiones de los 3 Reels de lanzamiento, o la configuración paso a paso de los eventos de conversión en Meta Ads y GA4?


## Respuesta completa

Aquí tienes el plan de campaña de 4 semanas enfocado exclusivamente en **`Aurora`**, diseñado para posicionarse como referencia premium en skincare facial sin depender de descuentos ni entrar en competencia directa con `Botica Verde` o `Skin Lab`.

---

### 🎯 OBJETIVO DE LA CAMPAÑA
Conseguir **150 ventas unitarias de `Aurora`** en 4 semanas, manteniendo un **CPA ≤ $45.000 COP**, un **ROAS ≥ 2.8x** y una **tasa de conversión web ≥ 3.2%**. Simultáneamente, validar que `Aurora` funciona como ancla de valor que justifica la escala de precios y abre rutas de cross-selling hacia `Sol` y `Luna`.

---

### 👥 AUDIENCIA (Segmentación precisa)
- **Geografía:** Bogotá, radio 15 km del centro. Priorizar comunas con alto poder adquisitivo y densidad digital: Chapinero, Usaquén, Suba alta, Teusaquillo, Los Mártires, La Candelaria, Puente Aranda, Engativá norte, Fontibón, Rafael Uribe Uribe, Antonio Nariño, Santa Fe, San Cristóbal, Kennedy centro, Barrios Unidos.
- **Demografía:** Mujeres 25–45 años, ingresos medios-altos, profesiones/actividades con exposición urbana (oficina, emprendimiento, maternidad activa, vida social).
- **Psicografía:** Valoran ingredientes activos, rutinas estructuradas y resultados medibles. Se sienten impactadas por contaminación, luz azul, cambios climáticos bruscos y estrés urbano. Dispuestas a invertir en productos que ahorren tiempo y reduzcan fricción en su cuidado diario.
- **Comportamiento digital:** Consumen Reels/TikTok de dermatología y rutinas reales, revisan carruseles educativos antes de comprar, responden a anuncios con prueba social contextualizada, usan WhatsApp para resolver dudas técnicas.
- **Exclusiones:** Público nacional fuera de Bogotá, usuarios que solo interactúan con contenido de maquillaje puro (sin intención de skincare), listas de clientes existentes de `Luna`/`Sol` (para evitar duplicidad de inversión en esta fase).

---

### 📡 CANALES & DISTRIBUCIÓN DE PRESUPUESTO
| Canal | Peso | Función en la campaña | Formato prioritario |
|-------|------|------------------------|---------------------|
| Instagram + Meta Ads | 60% | Descubrimiento, consideración y conversión directa | Reels educativos, Stories interactivas, Carrousel técnico, Catálogo shoppable, Conversión/Dynamic |
| TikTok | 20% | Virilidad orgánica + amplificación de UGC real | Videos nativos tipo “rutina en vivo”, Spark Ads sobre piezas orgánicas con >3% retención al segundo 3 |
| Google Search | 15% | Captura de intención alta y protección de marca | Keywords geolocalizadas (“set facial premium Bogotá”, “rutina skincare anti-contaminación”), Shopping Ads |
| WhatsApp + Email | 5% | Recuperación, postventa y cross-selling | Secuencia automatizada post-compra, catálogo conversacional, recordatorio de aplicación semanal de `Aurora` |

---

### 💬 MENSAJE PRINCIPAL & ÁNGULOS CREATIVOS
**Mensaje núcleo:**  
> “`Aurora` no es un set facial más: es tu escudo contra el ritmo y el clima de Bogotá. Concentración clínica, textura que respira bajo contaminación y resultados visibles desde la segunda semana. Diseñado para mujeres que exigen más de su piel.”

**Ángulos rotativos (para testing creativo):**
1. **Técnico/Justificación de precio:** “Por qué `Aurora` tiene 3 pasos y no 7” → explica sinergias de activos y evita saturación cutánea.
2. **Contexto local:** “Tu piel en Bogotá: cómo `Aurora` compensa humedad, altitud y luz azul” → conecta producto con realidad urbana.
3. **Prueba social controlada:** Testimonios reales de bogotanas mostrando textura, absorción y adaptación bajo mascarilla o oficina.
4. **Rutina optimizada:** “15 min nocturnos con `Aurora` = mañana lista para todo” → posiciona ahorro de tiempo + eficacia.

*Nota de cumplimiento:* Lenguaje alineado a normativa INVIMA (cuidado cosmético, no claims médicos). Se evitan términos como “cura”, “elimina arrugas” o “reemplaza tratamientos”.

---

### 📊 MÉTRICAS DE ÉXITO (KPIs de campaña)
| Indicador | Meta | Umbral de alerta | Herramienta |
|-----------|------|------------------|-------------|
| Ventas unitarias `Aurora` | 150 | < 90 en semana 4 | E-commerce dashboard |
| CPA / Costo por venta | ≤ $45.000 COP | > $60.000 x 2 semanas consecutivas | Meta Ads, TikTok Ads, Google Ads |
| ROAS ponderado | ≥ 2.8x | < 2.0x | Plataforma + CRM |
| Tasa de conversión web | ≥ 3.2% | < 2.0% | GA4 / Panel nativo |
| Guardados + compartidos (orgánico/paid) | ≥ 4% sobre alcance | < 2.5% | Insights IG/TikTok |
| Abandono de carrito | < 60% | > 70% | GA4 Events + Hotjar (si aplica) |
| Open rate secuencia post-compra `Aurora` | > 45% | < 35% | Email/WhatsApp CRM |
| Cross-sell `Aurora` → `Sol`/`Luna` (30 días) | ≥ 15% | < 8% | Segmentación CRM |

---

### 🗓️ PLAN SEMANA A SEMANA

#### **Semana 1: Lanzamiento + Educación Técnica**
- **Enfoque:** Validar ángulo premium y generar primera base de conversión.
- **Tácticas:**
  - Publicar 3 Reels/TikTok tipo “Desglose técnico de `Aurora`” (activos, sinergias, textura).
  - Activar campaña Meta de Conversión con audiencia fría segmentada por intereses (skincare activo, dermatología estética, bienestar urbano).
  - Lanzar carrousel IG: “Los 3 errores que hacen que tu crema facial no penetre en Bogotá”.
  - Configurar pixel/GA4 + evento `InitiateCheckout` y `Purchase` con parámetro `product_name: 'Aurora'`.
- **Mensaje clave:** “`Aurora` está formulado para trabajar en capas, no en exceso.”

#### **Semana 2: Prueba Social + Contexto Local**
- **Enfoque:** Reducir fricción de compra mediante validación real y relevancia geográfica.
- **Tácticas:**
  - Activar Spark Ads con 2 videos de microinfluencers/clientas reales aplicando `Aurora` en contexto bogotano (oficina, transporte, clima).
  - Stories interactivas: Encuesta “¿Qué parte de tu rutina facial te toma más tiempo?” → link directo a landing de `Aurora`.
  - Campaña Google Search con keywords de intención alta + extensiones de promoción silenciosa (valor agregado, no descuento).
  - Enviar email/WhatsApp a leads calificados: “Así se adapta `Aurora` a tu clima y estilo de vida”.
- **Mensaje clave:** “`Aurora` fue probado en pieles expuestas al ritmo de Bogotá.”

#### **Semana 3: Conversión + Escasez Perceptiva**
- **Enfoque:** Maximizar ventas sin tocar precio, usando disponibilidad y acompañamiento.
- **Tácticas:**
  - Remarketing dinámico de `Aurora` para visitantes web, viewers de Reels >50% y abandonadores de carrito.
  - Live IG/Q&A: “Resuelve tus dudas sobre `Aurora` en 15 min” → enlace directo en bio/stories.
  - Actualizar landing page con badge “Entrega en <48h en Bogotá” + política post-compra clara.
  - Activar secuencia WhatsApp automatizada: mensaje día 1 (confirmación), día 3 (tips de aplicación), día 7 (recordatorio de reabastecimiento).
- **Mensaje clave:** “`Aurora` se agota cuando las rutinas se consolidan.”

#### **Semana 4: Retención + Cross-Selling Controlado**
- **Enfoque:** Consolidar recompra y abrir ruta hacia `Sol` y `Luna` sin diluir el posicionamiento premium.
- **Tácticas:**
  - Campaña de remarketing a compradores de `Aurora` con oferta cruzada: “Completa tu escudo facial con `Sol` (maquillaje que respeta tu barra cutánea) o `Luna` (hidratación corporal que no compite con tu rutina).”
  - Publicar UGC recopilado: “Lo que dicen quienes ya usan `Aurora` en Bogotá”.
  - Analizar KPIs, pausar anuncios con CPA > meta, reinvertir en formatos con retención >35% y guardados >4%.
  - Enviar encuesta NPS breve (3 preguntas) a compradores de `Aurora` con código de agradecimiento no monetario (ej. acceso anticipado a nuevos lanzamientos).
- **Mensaje clave:** “`Aurora` es solo el inicio de tu rutina integral.”

---

### ⚙️ NOTAS OPERATIVAS CLAVE
1. **Creatividad:** Todas las piezas deben mostrar `Aurora` en uso real, con texto superpuesto claro y audio trending moderado. Evitar fondos genéricos; usar contextos urbanos bogotanos sutiles.
2. **Presupuesto mínimo recomendado:** $1.8–2.2 millones COP/semana distribuido según el peso de canales. Ajustar diariamente si CPA supera el umbral de alerta.
3. **Cumplimiento normativo:** Mantener lenguaje cosmético-validado. No comparar directamente con `Botica Verde` o `Skin Lab`. Incluir disclaimer opcional en landing: “Resultados pueden variar según tipo de piel y adherencia a la rutina”.
4. **Integración CRM:** Etiquetar todos los contactos de `Aurora` en WhatsApp/email para activar secuencias de cross-selling post-campaña.

¿Quieres que te entregue la estructura exacta de la landing page optimizada para `Aurora`, los guiones de los 3 Reels de lanzamiento, o la configuración paso a paso de los eventos de conversión en Meta Ads y GA4?