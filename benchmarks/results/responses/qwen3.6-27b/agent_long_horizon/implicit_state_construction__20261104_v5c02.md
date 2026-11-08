# Qwen 3.6 27B base (OpenRouter FP8) — agent_long_horizon/implicit_state_construction

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 7.08 | quality: 8.5
- latency_total: 359.963s | tokens_per_second: 60.3
- input_tokens: 18291 | output_tokens: 20216

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

¡Hola, Camila! Sí, me queda perfectamente claro. Tengo guardado el contexto de tu negocio:

📍 **Ubicación y mercado:** Tienda online enfocada exclusivamente en Bogotá por ahora.  
🛍️ **Productos y posicionamiento:**
- `Aurora`: set de cuidado facial → precio premium
- `Sol`: kit de maquillaje natural → precio medio
- `Luna`: crema corporal → precio de entrada
🏁 **Competencia directa en Bogotá:** `Botica Verde` y `Skin Lab`

Estoy listo para ayudarte a diseñar campañas que se alineen con tu estructura de precios, destaquen frente a esos competidores y maximicen tu alcance en Bogotá. ¿Por dónde te gustaría empezar? Podemos definir objetivos de campaña, segmentar tu público, elegir canales, o trabajar directamente en una estrategia para uno de los tres productos. Tú diriges. 💡

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Aquí tienes tu propuesta de valor general, redactada en exactamente dos oraciones y alineada con tu estructura de precios, mercado y competencia:

Ofrecemos una experiencia de belleza natural y consciente en Bogotá, con productos diseñados para adaptarse a cada presupuesto y etapa de tu rutina, desde la crema de entrada Luna, pasando por el kit Sol, hasta el set premium Aurora. Nos diferenciamos al combinar transparencia en ingredientes, compra 100% digital y una propuesta curada específicamente para el estilo de vida y las necesidades reales de las mujeres de la capital.

💡 *Cómo se usa tu contexto:* La primera oración integra tu escalera de precios y los tres productos sin sonar como un catálogo. La segunda posiciona frente a Botica Verde y Skin Lab destacando lo que ellos no enfatizan tanto: la escalabilidad de precios, el canal 100% online y el enfoque hiperlocal en Bogotá.

¿Quieres que la adaptemos a un tono más cercano, más científico o más minimalista antes de pasar a definir los objetivos y KPIs de tu primera campaña?

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Para tu modelo 100% online y enfoque hiperlocal en Bogotá, te recomiendo priorizar estos canales en este orden estratégico:

**1. Instagram + TikTok (Conciencia y Deseo)**
- *Por qué:* La belleza en Colombia se descubre y valida por contenido visual y rutinas reales. Instagram te da Reels, Stories con enlaces directos, etiquetado de productos y una comunidad activa en Bogotá. TikTok amplifica el alcance orgánico con tutoriales, texturas, antes/después y trends de skincare/maquillaje.
- *Cómo diferenciarte:* Mientras Botica Verde y Skin Lab suelen invertir en contenido institucional o promociones genéricas, tú puedes apostar por UGC (micro-creadoras bogotanas), rutinas adaptadas al clima y la rutina urbana de la capital, y demostraciones sensoriales que muestren la diferencia entre Luna, Sol y Aurora sin sonar como catálogo.

**2. WhatsApp Business (Conversión y Aceleración)**
- *Por qué:* En Colombia, la mayoría de las dudas de compra y los cierres se resuelven por WhatsApp. Es tu canal de menor fricción para recuperar carritos, ofrecer asesoría personalizada (“¿Luna para hidratación diaria o Sol para acabado natural?”) y lanzar cupones exclusivos por mensaje.
- *Cómo activarlo:* Configura respuestas rápidas por intención, usa el catálogo integrado, crea listas de difusión segmentadas por producto de interés y automatiza seguimientos post-compra para solicitar reseñas o recomendar el siguiente nivel de tu escalera de precios.

**3. Google Ads (Search & Shopping) (Intención de Compra)**
- *Por qué:* Captura a quien ya busca activamente “crema corporal hidratante Bogotá”, “kit maquillaje natural” o “set cuidado facial premium”. Es el canal más predecible para conversión inmediata y ROI medible.
- *Cómo estructurarlo:* Campañas Shopping para Luna (volumen alto, precio entrada) y Sol (precio medio, búsqueda por “kit natural”). Campañas de Búsqueda con keywords transaccionales y de alta consideración para Aurora (precio premium, menor volumen pero mayor margen). Geolocaliza todo a Bogotá y excluye zonas con baja densidad de tu público objetivo.

**4. Email Marketing (Retención y Escalera de Productos)**
- *Por qué:* Te permite guiar al cliente por tu ecosistema sin depender de algoritmos. Ideal para cruzar ventas: quien compra Luna recibe contenido y un incentivo para probar Sol; quien usa Sol, recibe rutinas avanzadas y acceso anticipado a Aurora.
- *Cómo activarlo:* Captura emails con un lead magnet local (“Guía de rutina facial según el clima y la contaminación de Bogotá”), automatiza flujos de bienvenida, post-compra y win-back, y segmenta por historial de compra y frecuencia.

**Canal secundario:** Facebook Ads. Útil para retargeting y audiencias 30+ en Bogotá, pero con menor eficiencia orgánica que IG/TikTok en el nicho de belleza. Úsalo principalmente para remarketing y ampliación de audiencias similares.

¿Quieres que mapeemos el *customer journey* completo asignando un canal específico a cada fase (conciencia → consideración → compra → retención) y a cada producto (Luna, Sol, Aurora)? Con eso tendremos la arquitectura lista para diseñar tu primera campaña con KPIs, presupuesto y calendario de contenidos.

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Para tu modelo 100% digital, enfoque en Bogotá y estructura de tres niveles de precio, esta es la frecuencia orgánica que maximiza alcance sin saturarte ni diluir la calidad:

📱 **Instagram**
- **Feed:** 3 publicaciones/semana (mezcla de: rutina según clima bogotano, textura/aplicación de Luna/Sol/Aurora, testimonios reales, educación de ingredientes)
- **Reels:** 3-4/semana (el algoritmo premia la constancia; enfócate en demostraciones rápidas, “antes/después”, hacks de aplicación y comparativas suaves vs. tendencias del mercado)
- **Stories:** Diarias (5-10/día). Úsalas para encuestas, preguntas de skincare, countdowns de envíos Bogotá, y CTA directo a WhatsApp. Aquí es donde puedes destacar frente a Botica Verde y Skin Lab mostrando transparencia, proceso de armado y atención personalizada.

🎵 **TikTok**
- **Publicaciones:** 4-5/semana. La belleza en TikTok escala con consistencia y formato nativo. Prioriza: texturas de Luna (viral por naturaleza), looks naturales con Sol adaptados a la humedad/lluvia de Bogotá, y rutinas premium de Aurora con enfoque en ingredientes activos y resultados a mediano plazo.
- *Tip:* Repurpura los Reels aquí con subtítulos nativos y hooks en los primeros 2 segundos. No copies 1:1; adapta el ritmo y la música a la plataforma.

💬 **WhatsApp Business**
- **Difusiones:** 2/semana (nunca más; el canal se valora por exclusividad y utilidad). Segmenta por interés: quienes compraron Luna reciben tips de hidratación + incentivo para probar Sol; quienes usan Sol, rutinas de mantenimiento + preview de Aurora.
- **Estado:** 3-4/semana (visual, ligero, enfocado en confianza: unboxing, reseñas, tips rápidos, recordatorio de envío gratis Bogotá).

📧 **Email Marketing**
- **Campañas:** 1-2/semana. Mantén un ritmo predecible: educación de ingredientes, guías de rutina según estación/clima capitalino, lanzamientos, y flujos automatizados (bienvenida, post-compra, win-back). La frecuencia es sostenible porque el canal es opt-in y medible.

📘 **Facebook (Secundario)**
- **Publicaciones:** 2-3/semana. Repurpura el contenido de mayor engagement de IG/TikTok, enfocado en audiencias 30+ en Bogotá y en comunidad (grupos de belleza natural, cuidado de la piel, emprendimiento local). Úsalo principalmente para retención y remarketing orgánico.

🔑 **Claves para sostenerlo sin quemarte:**
- **Batching:** Graba y edita 8-10 piezas de video en 2 días al mes. Usa plantillas de Canva para carruseles y stories.
- **Regla 70/20/10:** 70% valor/educación (clima Bogotá, ingredientes, rutinas), 20% social proof/UGC, 10% promoción directa.
- **Mide, no adivines:** Revisa cada 15 días: tasa de guardados/compartidos (IG/TikTok), clics a WhatsApp, tasa de apertura/clics (email). Ajusta frecuencia según engagement, no por obligación.

¿Quieres que te arme un **calendario de contenidos de 4 semanas** con temas listos, asignados por canal y alineados a tu escalera de precios (Luna → Sol → Aurora), incluyendo hooks y CTAs específicos para Bogotá?

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

En skincare, el contenido que convierte combina **educación clara, prueba social auténtica y experiencia sensorial**. Para tu línea (Aurora, Sol, Luna) y tu mercado en Bogotá, estos son los formatos con mayor impacto orgánico y conversión, ya alineados a tu escalera de precios y diferenciación frente a Botica Verde y Skin Lab:

### 🔹 1. Rutinas paso a paso (“Layering” inteligente)
- **Ideal para:** Aurora (premium)
- **Por qué funciona:** El set facial vende por sistematización. Mostrar el orden, tiempos de absorción y por qué cada producto no es intercambiable genera percepción de valor y justifica el precio premium.
- **Hook ejemplo:** “¿Tu sérum se absorbe o se queda en la superficie? Así se aplica Aurora en 3 pasos.”
- **Formato:** Reels/TikTok 30-45s + carrusel con checklist descargable.

### 🔹 2. Textura y prueba sensorial
- **Ideal para:** Luna (entrada) y Sol (medio)
- **Por qué funciona:** La crema corporal y el maquillaje natural se compran por tacto y acabado. El contenido que muestra consistencia, velocidad de absorción y acabado en piel real reduce la fricción de compra online.
- **Hook ejemplo:** “Hidratación que no deja pegajosidad, ni con el frío de Bogotá.”
- **Formato:** Close-ups, aplicación en brazo/espalda, transición con/sin producto, sonidos ASMR suaves.

### 🔹 3. Resultados reales con tracking (14/30 días)
- **Ideal para:** Los tres productos (especialmente Aurora)
- **Por qué funciona:** Skincare exige credibilidad. Evita promesas mágicas; usa diarios con misma luz, ángulo y condiciones. Muestra lo que sí cambia (hidratación, textura, brillo) y lo que no (manchas profundas, líneas estáticas).
- **Hook ejemplo:** “Día 1 vs Día 21 con Aurora: lo que sí cambió (y lo que no).”
- **Formato:** TikTok/Reels + Stories con encuestas de progreso y CTA a WhatsApp para rutina personalizada.

### 🔹 4. Educación de ingredientes + desmitificación
- **Ideal para:** Diferenciación vs Botica Verde y Skin Lab
- **Por qué funciona:** Explicar activos clave sin jerga médica construye autoridad. Aclarar mitos (“¿La niacinamida seca? No, si se usa así…”) posiciona tu marca como transparente y cercana.
- **Hook ejemplo:** “3 ingredientes de Aurora que sí funcionan en clima seco y altitud.”
- **Formato:** Carruseles educativos, videos hablados con gráficos simples, glosario visual.

### 🔹 5. Adaptación al clima y estilo de vida bogotano
- **Ideal para:** Contenido local de alta retención
- **Por qué funciona:** Bogotá tiene humedad variable, frío, contaminación y agua dura. El contenido que resuelve eso genera confianza inmediata y te separa de competidores con mensajes genéricos.
- **Hook ejemplo:** “¿Tu rutina se rompe con las lluvias de Bogotá? Ajusta esto.”
- **Formato:** Guías estacionales, comparativas “verano vs invierno capitalino”, tips de aplicación para commute y oficina.

### 🔹 6. UGC y prueba social auténtica
- **Ideal para:** Escalar confianza sin presupuesto de influencers
- **Por qué funciona:** Clientas reales > testimonios producidos. Micro-creadoras bogotanas, reseñas con foto/video, unboxing sincero y respuestas a dudas frecuentes reducen la tasa de abandono del carrito.
- **Hook ejemplo:** “Lo que dice una clienta que lleva 3 meses con Luna.”
- **Formato:** Reposts con crédito, collages de reseñas, videos de 15s con subtítulos y CTA directo a WhatsApp.

---

📊 **Métricas que te dirán qué está funcionando:**
- `Guardados y compartidos` → educación/rutinas (Aurora)
- `Retención >30s` → interés real en textura/resultados (Luna/Sol)
- `Clics a WhatsApp + tasa de respuesta` → conversión efectiva
- `Menciones de “Bogotá/clima/altitud” en comentarios` → relevancia local y diferenciación

⚠️ **Nota de compliance:** Evita afirmaciones médicas (“cura”, “elimina”). Usa “puede ayudar”, “resultado visible en X días con uso constante”, y siempre menciona que los resultados varían según piel y rutina.

¿Quieres que te entregue **5 guiones listos para grabar** (uno por producto + uno de rutina climática) con estructura de 3 actos, hooks validados y CTAs optimizados para tu tienda online? Con eso podrías grabar tu primer batch de contenido esta semana y medir qué formato resuena más con tu público bogotano.

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Para diferenciarte de **Botica Verde** y **Skin Lab** sin entrar en guerra de precios, tu ventaja está en la **experiencia, la personalización y la relevancia local**. En belleza online, el precio es solo el 30% de la decisión; el resto lo define confianza, percepción de valor y facilidad para obtener resultados. Aquí tienes 5 ejes estratégicos, ya adaptados a tu escalera de precios y a tu enfoque en Bogotá:

### 🔹 1. Diagnóstico y rutina personalizada (gratis)
- **Cómo funciona:** Al comprar cualquier producto, la clienta completa un micro-quiz (tipo de piel, clima, objetivo) y recibe por WhatsApp una rutina de 3 pasos con el orden exacto, frecuencia y ajustes según estación.
- **Aplicación por producto:** 
  - `Aurora`: diagnóstico facial + guía de layering premium
  - `Sol`: recomendación de acabado según humedad/lluvia de Bogotá
  - `Luna`: frecuencia de aplicación y zonas clave (rodillas, codos, espalda)
- **Por qué te separa:** Tus competidores suelen vender el producto; tú vendes el sistema. El valor percibido sube sin tocar el precio.

### 🔹 2. Transparencia radical + educación accesible
- **Cómo funciona:** Publica fichas de ingredientes en lenguaje claro: “Qué hace, por qué está en tu piel, qué evita”. Evita jerga clínica o marketing vacío.
- **Serie de contenido:** “Desmitificamos Bogotá”: cómo la altitud, el agua dura, la contaminación y los cambios bruscos de temperatura afectan la piel, y cómo cada producto responde.
- **Por qué te separa:** Botica Verde y Skin Lab compiten en posicionamiento genérico o científico. Tú compites en claridad y utilidad inmediata.

### 🔹 3. Unboxing y packaging con propósito local
- **Cómo funciona:** Diseña una experiencia de apertura que refleje la rutina capitalina: materiales reciclables locales, mensajes en el empaque que reconozcan el día a día (“Para esos días grises de Chapinero”, “Hidratación que sobrevive al commute”).
- **Valor agregado:** Incluye una mini guía estacional descargable o un estuche reutilizable para `Sol`. El costo es marginal, pero la percepción de cuidado y exclusividad se dispara.
- **Por qué te separa:** El packaging deja de ser un contenedor y se convierte en tu primer canal de marketing post-compra.

### 🔹 4. Prueba social estructurada (UGC real, no producido)
- **Cómo funciona:** Programa “Mujeres que prueban”: clientas bogotanas documentan 14/30 días a cambio de un crédito para subir de nivel (Luna → Sol → Aurora). Publicas sus resultados con contexto real (edad, tipo de piel, barrio, clima).
- **Formato:** Videos cortos con subtítulos, carruseles de “antes/durante/ahora”, y respuestas a dudas frecuentes en Stories.
- **Por qué te separa:** La prueba social auténtica supera a cualquier descuento agresivo y genera confianza orgánica que los competidores no pueden replicar rápidamente.

### 🔹 5. Garantía de experiencia, no solo de producto
- **Cómo funciona:** “30 días para encontrar tu rutina”. Si no le funciona, ajustas la recomendación, cambias el producto o devuelves el valor como crédito. Acompaña con seguimiento activo por WhatsApp (día 3, 7, 14).
- **Por qué te separa:** Reduce el riesgo percibido de comprar skincare online. Tus competidores garantizan el empaque; tú garantizas el resultado y el acompañamiento.

---

📊 **Cómo medir que la diferenciación está funcionando:**
- `% de clientes que compran 2+ productos` (cross-sell por escalera de precios)
- `Tasa de conversión de tráfico orgánico` vs. campañas de descuento
- `NPS / reseñas con mención a “rutina personalizada”, “atención”, “resultado real”`
- `Retención a 60/90 días` (LTV)

🚫 **Lo que NO debes hacer:**
- Competir en “2x1” o “envío gratis ilimitado” como estándar
- Copiar el tono clínico o minimalista de tus competidores
- Prometer resultados médicos (“elimina manchas”, “cura acné”)

---

¿Quieres que diseñemos la **primera campaña de diferenciación** enfocada en `Aurora` (tu producto premium) con: mensaje central, activos de contenido listos para grabar, flujo de WhatsApp de acompañamiento, y KPIs medibles? Así validamos el enfoque antes de escalar a `Sol` y `Luna`, sin tocar precios ni entrar en descuento.

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Para tu primer trimestre, el objetivo no es escalar a toda costa, sino **validar qué funciona, ajustar la experiencia y construir los cimientos de retención**. Aquí tienes los KPIs esenciales, agrupados por pilar, con metas realistas para un e-commerce de belleza en Bogotá y la lógica de por qué importan para tu modelo:

---

### 📊 1. Adquisición y Eficiencia
| KPI | Por qué importa para ti | Meta Q1 |
|-----|------------------------|---------|
| **CAC por canal** (IG, TikTok, Google, WA) | Te dice dónde inviertes mejor sin entrar en descuento. Si un canal tiene CAC > ticket promedio, lo reestructuras o lo pausas. | ≤ $15.000–$20.000 COP |
| **% tráfico geolocalizado a Bogotá** | Valida que no pierdas presupuesto o esfuerzo orgánico fuera de tu mercado único. | >85% del tráfico total |
| **ROAS inicial** (solo si haces ads) | En Q1 el algoritmo aprende. Un ROAS de 1.5x–2.0x es saludable si el CAC y la retención temprana son positivos. | 1.5x – 2.0x |

---

### 🛒 2. Conversión y Mix de Productos
| KPI | Por qué importa para ti | Meta Q1 |
|-----|------------------------|---------|
| **Tasa de conversión general** | Refleja la claridad de tu propuesta, la fricción del checkout y la confianza generada. | 1.5% – 2.5% |
| **Conversión por producto** | `Luna` (volumen/entrada) > `Sol` (consideración media) > `Aurora` (premium/alta consideración). Si Aurora convierte muy bajo, revisa educación y prueba social. | Luna: >2.5% \| Sol: ~1.8% \| Aurora: ~1.0% |
| **AOV (Valor promedio del carrito)** | Mide si tu escalera de precios y los upsells funcionen. Si está bajo, faltan bundles o recomendaciones en checkout. | $80.000 – $120.000 COP |
| **Tasa de abandono de carrito** | En belleza online es alta. Tu diferenciación (WhatsApp, guía personalizada) debe recuperarla. | <70% |

---

### 🤝 3. Experiencia y Fidelización Temprana
| KPI | Por qué importa para ti | Meta Q1 |
|-----|------------------------|---------|
| **CSAT / NPS post-compra** | Valida que la experiencia (envío Bogotá, empaque, rutina personalizada) supere a Botica Verde y Skin Lab sin tocar precios. | CSAT ≥ 4.5/5 \| NPS ≥ 30 |
| **Tasa de recompra o upgrade** (Luna→Sol, Sol→Aurora) | Señal temprana de que tu ecosistema y acompañamiento funcionan. | 8% – 12% |
| **Tiempo de respuesta WA & resolución en 1er contacto** | Tu canal de conversión y diferenciación clave. La velocidad y calidad definen la confianza. | <2h (horario comercial) \| >90% resolución |
| **Tasa de devolución/reclamo** | Si sube, revisa expectativas, instrucciones de uso o compatibilidad de ingredientes. | <3% |

---

### 📱 4. Contenido y Engagement (Validación de Mensaje)
| KPI | Por qué importa para ti | Meta Q1 |
|-----|------------------------|---------|
| **Guardados y compartidos** (% del alcance) | Indicador de intención real y utilidad. Supera a los “likes” para skincare. | >5% |
| **CTR a WhatsApp / tienda** | Mide si tus hooks y CTAs están generando acción, no solo consumo pasivo. | Orgánico: >3% \| Ads: >1.5% |
| **Volumen de UGC espontáneo** | Prueba social orgánica que te separa de competidores. Incluye reseñas con foto/video, menciones, diarios de uso. | 15–20 piezas validadas |

---

### 🛠️ Cómo operativizarlo sin complicarte
- **Herramientas mínimas:** GA4 (tráfico/conversión), Meta/TikTok Ads Manager (CAC/ROAS), WhatsApp Business (respuestas/difusiones), tu plataforma de e-commerce (AOV, abandono, mix), Google Forms/Typeform (CSAT/NPS).
- **Ritmo de revisión:** 
  - *Semanal:* Operativo (WA, abandono, CTR, UGC)
  - *Quincenal:* Ajuste de contenido/canales (engagement, CAC, conversión por producto)
  - *Mensual:* Estratégico (AOV, upgrade rate, NPS, mix de precios)
- **Regla de oro Q1:** Si un KPI se desvía >15% de la meta, **cambia el mensaje, el flujo o el canal, no el precio**. Tu diferenciación es experiencia y relevancia local, no descuento.

---

¿Quieres que te genere un **dashboard mínimo viable en Google Sheets** con las fórmulas listas, umbrales de alerta (🟢🟡🔴) y una plantilla de reporte semanal de 1 página para que lo revises en 10 minutos? Con eso tendrás el sistema de medición listo para tu primera campaña.

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

Aquí tienes el plan de campaña de 4 semanas diseñado exclusivamente para **`Aurora`**, alineado con tu posicionamiento premium, tu mercado único en Bogotá y tu estrategia de diferenciación sin descuentos.

---
### 🎯 Objetivo de la Campaña
Posicionar `Aurora` como el set de cuidado facial premium esencial para mujeres bogotanas, generando conciencia, validación social y conversión inicial basada en experiencia y resultados comprobables.  
**Meta concreta:** 80–100 ventas de `Aurora` en 4 semanas, con ≥10% de intención de recompra o upgrade desde `Luna`/`Sol`, y un NPS ≥35.

---
### 👥 Audiencia Objetivo (Bogotá)
- **Demografía:** Mujeres 25–45 años, estratos 4–6, residentes en Bogotá.
- **Psicografía:** Buscan eficacia y sostenibilidad, valoran transparencia en ingredientes, tienen una rutina base pero la optimizan, son sensibles al clima capitalino (frío, humedad variable, contaminación, altitud).
- **Comportamiento digital:** Activas en IG/TikTok, consumen contenido educativo de skincare, responden a asesoría 1:1 por WhatsApp, compran online cuando hay prueba social real y garantía de experiencia.
- **Segmentación en ads:** Intereses en skincare premium/coreano, rutina facial, dermatología estética, bienestar; ubicación: Bogotá (excluir zonas con baja densidad de compra).

---
### 💡 Mensaje Principal
> “`Aurora` no es un set más: es tu rutina facial optimizada para el clima, la altitud y el estilo de vida de Bogotá. Resultados visibles en 21 días, con ingredientes que sí trabajan en tu piel.”

**Pilares de comunicación:**
1. Adaptación climática bogotana
2. Eficacia comprobable (tracking 14/21 días)
3. Experiencia premium sin fricción (diagnóstico + acompañamiento WA)
4. Transparencia radical en ingredientes

---
### 📅 Plan Semanal (4 Semanas)

#### 🟦 Semana 1: Conciencia y Educación (“Por qué `Aurora`”)
- **IG/TikTok (3 piezas):**
  1. “3 errores que arruinan tu rutina facial en Bogotá (y cómo `Aurora` los soluciona)”
  2. Textura y layering de `Aurora` (close-up, ASMR suave, orden exacto de aplicación)
  3. “¿Premium o sobreprecio? Te muestro lo que hay dentro de `Aurora`” (ficha de ingredientes en lenguaje claro)
- **Stories:** Encuestas (“¿Tu piel se reseca con el frío bogotano?”), CTA a micro-quiz de diagnóstico facial
- **WhatsApp Business:** Difusión a base existente: “Accede gratis a tu rutina personalizada con `Aurora` + guía de adaptación climática”
- **Email:** Lead magnet “Guía: Rutina facial según el clima de Bogotá” → introducción a `Aurora` + CTA a tienda

#### 🟨 Semana 2: Prueba Social y Validación (“Quién usa `Aurora`”)
- **IG/TikTok (3 piezas):**
  1. UGC: “Día 1 vs Día 14 con `Aurora`” (clienta real, misma luz/ángulo, subtítulos, sin promesas médicas)
  2. “Lo que dicen 3 bogotanas sobre `Aurora`” (collage de reseñas + audio real de aplicación)
  3. “`Aurora` vs rutina básica: qué cambia en hidratación y textura” (comparativa educativa, no despectiva)
- **Stories:** Countdown a “Acompañamiento post-compra de `Aurora`”, caja de preguntas frecuentes sobre `Aurora`
- **WhatsApp:** Secuencia automatizada post-quiz: rutina personalizada + video de 30s aplicando `Aurora` correctamente
- **Email:** Caso de estudio breve + CTA a compra con “Garantía de experiencia `Aurora` 30 días”

#### 🟧 Semana 3: Conversión y Acompañamiento (“Cómo comprar y usar `Aurora`”)
- **IG/TikTok (3 piezas):**
  1. “Cómo aplicar `Aurora` en 3 pasos (sin desperdiciar ni una gota)”
  2. “¿`Aurora` vale la pena para piel mixta/grasa en Bogotá?” (educación + demo en piel real)
  3. Unboxing `Aurora` + mini guía estacional incluida + CTA directo a tienda
- **Stories:** Link directo a producto `Aurora`, Q&A en vivo sobre `Aurora`, recordatorio de envío Bogotá 24–48h
- **WhatsApp:** Seguimiento día 3 y 7 post-compra: “¿Cómo se siente tu piel con `Aurora`?” + tips de integración con tu rutina actual
- **Email:** Recuperación de carrito abandonado (si aplica) + incentivo de valor: “Acceso a masterclass gratuita de layering facial con `Aurora`”

#### 🟩 Semana 4: Retención y Escalabilidad (“Qué sigue después de `Aurora`”)
- **IG/TikTok (3 piezas):**
  1. “Día 21 con `Aurora`: lo que sí cambió (y lo que requiere paciencia)”
  2. “Cómo mantener los resultados de `Aurora` en la siguiente temporada bogotana”
  3. UGC recopilado: “Mujeres que eligieron `Aurora` y no volvieron atrás”
- **Stories:** Encuesta de satisfacción, CTA a reseña con foto/video, preview de rutina avanzada post-`Aurora`
- **WhatsApp:** Difusión exclusiva: “¿Listo para optimizar tu rutina? Agenda tu revisión gratuita con `Aurora`”
- **Email:** Encuesta NPS + guía “Cómo potenciar `Aurora` con hábitos bogotanos” + invitación a programa de lealtad

---
### 📊 Métricas de Éxito (KPIs Específicos para `Aurora`)
| Pilar | KPI | Meta Q1 (4 semanas) |
|-------|-----|---------------------|
| **Adquisición** | CAC por canal (IG/TikTok/Google) | ≤ $18.000 COP |
| | % tráfico geolocalizado a Bogotá | >85% |
| | ROAS (si se usa paid) | ≥ 1.8x |
| **Conversión** | Tasa de conversión de `Aurora` | ≥ 1.2% |
| | Abandono de carrito (tráfico a `Aurora`) | <65% |
| | AOV impulsado por `Aurora` | ≥ $110.000 COP |
| **Engagement/Validación** | Guardados/compartidos vs alcance | >6% |
| | CTR a tienda/WA desde contenido de `Aurora` | ≥ 3.5% |
| | UGC validados mencionando `Aurora` | 15–20 piezas |
| **Experiencia/Retención** | CSAT post-compra de `Aurora` | ≥ 4.6/5 |
| | NPS de clientes de `Aurora` | ≥ 35 |
| | Tasa de recompra/upgrade (Luna/Sol → `Aurora`) | ≥ 10% |
| | Tiempo de respuesta WA (consultas sobre `Aurora`) | <1.5h (horario comercial) |
| **Meta de ventas** | Unidades de `Aurora` vendidas | 80–100 |

---
### 🔑 Notas Críticas de Ejecución
- **Cero descuentos:** El incentivo es valor agregado (diagnóstico, guía climática, acompañamiento WA, garantía de experiencia). Mantén el precio premium intacto.
- **Mención explícita:** Todo hook, subtítulo, CTA y activo debe nombrar `Aurora` para reforzar recall y evitar dilución con `Sol`/`Luna`.
- **Geolocalización:** Ads y contenido orgánico apuntan solo a Bogotá. Usa hashtags locales (#SkincareBogotá #RutinaFacialBogotá #BellezaCapitalina) y menciona barrios/clima en copy.
- **Revisión semanal:** Si conversión de `Aurora` <1% o CAC >$20k, ajusta hooks, segmentación o flujo de WA. No toques precio.
- **Cumplimiento:** Evita “cura”, “elimina”, “dermatológicamente probado”. Usa “puede ayudar”, “resultado visible en 21 días con uso constante”, “los resultados varían según tu piel”.

---
¿Quieres que te entregue los **3 guiones completos para la Semana 1** (hook, estructura de 3 actos, subtítulos sugeridos, CTA y assets visuales) listos para grabar esta semana? Así lanzas `Aurora` con material profesional, alineado al plan y medible desde el día 1.


## Respuesta completa

Aquí tienes el plan de campaña de 4 semanas diseñado exclusivamente para **`Aurora`**, alineado con tu posicionamiento premium, tu mercado único en Bogotá y tu estrategia de diferenciación sin descuentos.

---
### 🎯 Objetivo de la Campaña
Posicionar `Aurora` como el set de cuidado facial premium esencial para mujeres bogotanas, generando conciencia, validación social y conversión inicial basada en experiencia y resultados comprobables.  
**Meta concreta:** 80–100 ventas de `Aurora` en 4 semanas, con ≥10% de intención de recompra o upgrade desde `Luna`/`Sol`, y un NPS ≥35.

---
### 👥 Audiencia Objetivo (Bogotá)
- **Demografía:** Mujeres 25–45 años, estratos 4–6, residentes en Bogotá.
- **Psicografía:** Buscan eficacia y sostenibilidad, valoran transparencia en ingredientes, tienen una rutina base pero la optimizan, son sensibles al clima capitalino (frío, humedad variable, contaminación, altitud).
- **Comportamiento digital:** Activas en IG/TikTok, consumen contenido educativo de skincare, responden a asesoría 1:1 por WhatsApp, compran online cuando hay prueba social real y garantía de experiencia.
- **Segmentación en ads:** Intereses en skincare premium/coreano, rutina facial, dermatología estética, bienestar; ubicación: Bogotá (excluir zonas con baja densidad de compra).

---
### 💡 Mensaje Principal
> “`Aurora` no es un set más: es tu rutina facial optimizada para el clima, la altitud y el estilo de vida de Bogotá. Resultados visibles en 21 días, con ingredientes que sí trabajan en tu piel.”

**Pilares de comunicación:**
1. Adaptación climática bogotana
2. Eficacia comprobable (tracking 14/21 días)
3. Experiencia premium sin fricción (diagnóstico + acompañamiento WA)
4. Transparencia radical en ingredientes

---
### 📅 Plan Semanal (4 Semanas)

#### 🟦 Semana 1: Conciencia y Educación (“Por qué `Aurora`”)
- **IG/TikTok (3 piezas):**
  1. “3 errores que arruinan tu rutina facial en Bogotá (y cómo `Aurora` los soluciona)”
  2. Textura y layering de `Aurora` (close-up, ASMR suave, orden exacto de aplicación)
  3. “¿Premium o sobreprecio? Te muestro lo que hay dentro de `Aurora`” (ficha de ingredientes en lenguaje claro)
- **Stories:** Encuestas (“¿Tu piel se reseca con el frío bogotano?”), CTA a micro-quiz de diagnóstico facial
- **WhatsApp Business:** Difusión a base existente: “Accede gratis a tu rutina personalizada con `Aurora` + guía de adaptación climática”
- **Email:** Lead magnet “Guía: Rutina facial según el clima de Bogotá” → introducción a `Aurora` + CTA a tienda

#### 🟨 Semana 2: Prueba Social y Validación (“Quién usa `Aurora`”)
- **IG/TikTok (3 piezas):**
  1. UGC: “Día 1 vs Día 14 con `Aurora`” (clienta real, misma luz/ángulo, subtítulos, sin promesas médicas)
  2. “Lo que dicen 3 bogotanas sobre `Aurora`” (collage de reseñas + audio real de aplicación)
  3. “`Aurora` vs rutina básica: qué cambia en hidratación y textura” (comparativa educativa, no despectiva)
- **Stories:** Countdown a “Acompañamiento post-compra de `Aurora`”, caja de preguntas frecuentes sobre `Aurora`
- **WhatsApp:** Secuencia automatizada post-quiz: rutina personalizada + video de 30s aplicando `Aurora` correctamente
- **Email:** Caso de estudio breve + CTA a compra con “Garantía de experiencia `Aurora` 30 días”

#### 🟧 Semana 3: Conversión y Acompañamiento (“Cómo comprar y usar `Aurora`”)
- **IG/TikTok (3 piezas):**
  1. “Cómo aplicar `Aurora` en 3 pasos (sin desperdiciar ni una gota)”
  2. “¿`Aurora` vale la pena para piel mixta/grasa en Bogotá?” (educación + demo en piel real)
  3. Unboxing `Aurora` + mini guía estacional incluida + CTA directo a tienda
- **Stories:** Link directo a producto `Aurora`, Q&A en vivo sobre `Aurora`, recordatorio de envío Bogotá 24–48h
- **WhatsApp:** Seguimiento día 3 y 7 post-compra: “¿Cómo se siente tu piel con `Aurora`?” + tips de integración con tu rutina actual
- **Email:** Recuperación de carrito abandonado (si aplica) + incentivo de valor: “Acceso a masterclass gratuita de layering facial con `Aurora`”

#### 🟩 Semana 4: Retención y Escalabilidad (“Qué sigue después de `Aurora`”)
- **IG/TikTok (3 piezas):**
  1. “Día 21 con `Aurora`: lo que sí cambió (y lo que requiere paciencia)”
  2. “Cómo mantener los resultados de `Aurora` en la siguiente temporada bogotana”
  3. UGC recopilado: “Mujeres que eligieron `Aurora` y no volvieron atrás”
- **Stories:** Encuesta de satisfacción, CTA a reseña con foto/video, preview de rutina avanzada post-`Aurora`
- **WhatsApp:** Difusión exclusiva: “¿Listo para optimizar tu rutina? Agenda tu revisión gratuita con `Aurora`”
- **Email:** Encuesta NPS + guía “Cómo potenciar `Aurora` con hábitos bogotanos” + invitación a programa de lealtad

---
### 📊 Métricas de Éxito (KPIs Específicos para `Aurora`)
| Pilar | KPI | Meta Q1 (4 semanas) |
|-------|-----|---------------------|
| **Adquisición** | CAC por canal (IG/TikTok/Google) | ≤ $18.000 COP |
| | % tráfico geolocalizado a Bogotá | >85% |
| | ROAS (si se usa paid) | ≥ 1.8x |
| **Conversión** | Tasa de conversión de `Aurora` | ≥ 1.2% |
| | Abandono de carrito (tráfico a `Aurora`) | <65% |
| | AOV impulsado por `Aurora` | ≥ $110.000 COP |
| **Engagement/Validación** | Guardados/compartidos vs alcance | >6% |
| | CTR a tienda/WA desde contenido de `Aurora` | ≥ 3.5% |
| | UGC validados mencionando `Aurora` | 15–20 piezas |
| **Experiencia/Retención** | CSAT post-compra de `Aurora` | ≥ 4.6/5 |
| | NPS de clientes de `Aurora` | ≥ 35 |
| | Tasa de recompra/upgrade (Luna/Sol → `Aurora`) | ≥ 10% |
| | Tiempo de respuesta WA (consultas sobre `Aurora`) | <1.5h (horario comercial) |
| **Meta de ventas** | Unidades de `Aurora` vendidas | 80–100 |

---
### 🔑 Notas Críticas de Ejecución
- **Cero descuentos:** El incentivo es valor agregado (diagnóstico, guía climática, acompañamiento WA, garantía de experiencia). Mantén el precio premium intacto.
- **Mención explícita:** Todo hook, subtítulo, CTA y activo debe nombrar `Aurora` para reforzar recall y evitar dilución con `Sol`/`Luna`.
- **Geolocalización:** Ads y contenido orgánico apuntan solo a Bogotá. Usa hashtags locales (#SkincareBogotá #RutinaFacialBogotá #BellezaCapitalina) y menciona barrios/clima en copy.
- **Revisión semanal:** Si conversión de `Aurora` <1% o CAC >$20k, ajusta hooks, segmentación o flujo de WA. No toques precio.
- **Cumplimiento:** Evita “cura”, “elimina”, “dermatológicamente probado”. Usa “puede ayudar”, “resultado visible en 21 días con uso constante”, “los resultados varían según tu piel”.

---
¿Quieres que te entregue los **3 guiones completos para la Semana 1** (hook, estructura de 3 actos, subtítulos sugeridos, CTA y assets visuales) listos para grabar esta semana? Así lanzas `Aurora` con material profesional, alineado al plan y medible desde el día 1.