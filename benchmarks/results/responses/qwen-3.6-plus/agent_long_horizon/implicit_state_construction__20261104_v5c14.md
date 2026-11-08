# Qwen 3.6 Plus — agent_long_horizon/implicit_state_construction

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.17 | quality: 10.0
- latency_total: 296.804s | tokens_per_second: 57.7
- input_tokens: 14673 | output_tokens: 16650

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

Sí, Camila, me queda perfectamente claro. He registrado los siguientes datos para usarlos en todo lo que trabajemos sin tener que volver a preguntártelos:

- **Negocio:** Tienda online en Colombia, con cobertura exclusiva en **Bogotá** por ahora.
- **Portafolio:** 
  - `Aurora`: set de cuidado facial (precio premium)
  - `Sol`: kit de maquillaje natural (precio medio)
  - `Luna`: crema corporal (precio de entrada)
- **Competencia directa en Bogotá:** `Botica Verde` y `Skin Lab`

Estoy listo para ayudarte a estructurar campañas de marketing, definir públicos, elegir canales, armar calendarios o analizar estrategias frente a tu competencia. ¿Por qué producto o objetivo te gustaría empezar?

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Ofrecemos una experiencia de belleza integral para Bogotá que combina el cuidado facial premium de *Aurora*, el maquillaje natural de *Sol* y la hidratación accesible de *Luna*, adaptando calidad y resultados a cada presupuesto. Frente a las opciones locales, te garantizamos una compra online ágil, asesoría personalizada y fórmulas limpias que cuidan tu piel sin complicaciones ni sobreprecios.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Para tu tienda en Bogotá y tu mix de tres productos con distintos rangos de precio, te recomiendo priorizar estos 4 canales digitales, ordenados por impacto y viabilidad operativa:

1. **Instagram + Meta Ads (Facebook/Instagram)**  
   *Por qué:* Es el canal visual por excelencia para belleza y skincare en Colombia. Permite segmentar exclusivamente por Bogotá, crear públicos similares y usar el catálogo de productos para vender directo.  
   *Cómo usarlo:* Reels y carruseles mostrando rutinas con *Aurora* (premium), swatches y looks naturales con *Sol* (medio), y testimonios rápidos de hidratación con *Luna* (entrada). Usa campañas de conversión con píxel activo y retargeting por producto visto o carrito abandonado.

2. **TikTok**  
   *Por qué:* Alto alcance orgánico y bajo costo por visualización en Colombia. Ideal para generar confianza mediante contenido auténtico y UGC, diferenciándote del tono más corporativo de *Botica Verde* y *Skin Lab*.  
   *Cómo usarlo:* Tutoriales de 15-30 seg, "antes/después" con *Luna*, duetos con microinfluencers bogotanas, y tendencias de skincare limpio. Usa TikTok Ads con objetivo de tráfico o conversión, segmentando por intereses de belleza y ubicación Bogotá.

3. **WhatsApp Business**  
   *Por qué:* En Colombia es el canal de cierre y fidelización con mayor tasa de conversión. Te permite ofrecer asesoría personalizada (clave para justificar el premium de *Aurora*) y recuperar ventas perdidas sin fricción.  
   *Cómo usarlo:* Enlace directo en anuncios y web, mensajes automatizados de bienvenida, seguimiento post-compra, y campañas de remarketing manual o con herramientas como ManyChat para ofrecer combos (ej. *Luna* + *Sol*) o descuentos por primera compra.

4. **Google Ads (Búsqueda + Shopping)**  
   *Por qué:* Captura intención de compra activa. Quien busca "set facial premium Bogotá" o "maquillaje natural tienda online" ya está listo para convertir.  
   *Cómo usarlo:* Campañas de búsqueda con palabras clave geo-localizadas y Shopping con feed de tu catálogo. Prioriza *Aurora* en búsquedas de alto valor y usa extensiones de ubicación/llamada para reforzar confianza local.

**Recomendación de enfoque inicial:**  
Arranca con **Instagram + Meta Ads** como motor principal (tráfico + conversión), apóyate en **TikTok** para alcance y prueba social, y cierra con **WhatsApp** para asesoría y recuperación de carritos. Cuando tengas tracción y margen claro, activa **Google Ads** para capturar demanda existente.

¿Quieres que te arme un plan de contenido de 2 semanas alineado a estos canales, o prefieres definir primero el presupuesto y los KPIs por producto?

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Para mantener el algoritmo a tu favor sin saturarte, te recomiendo esta frecuencia orgánica por canal, ajustada al sector belleza y a la realidad operativa de una tienda en Bogotá:

- **Instagram**  
  • *Feed/Reels:* **3 a 4 veces por semana**. Alterna entre educación (rutinas con *Aurora*), demostración (looks naturales con *Sol*) y resultados/UGC (hidratación con *Luna*).  
  • *Historias:* **Diarias (5-10 al día)**. No saturan el feed y son clave para engagement: encuestas, preguntas, detrás de cámaras, recordatorios de envío en Bogotá y respuestas a consultas.

- **TikTok**  
  • **3 a 5 veces por semana**. El algoritmo premia la constancia más que la producción pulida. Puedes reutilizar tus Reels de Instagram (exporta sin marca de agua) y añadir subtítulos nativos. Prioriza formatos de 15-30 seg: tips rápidos, “mitos vs realidad”, unboxings y micro-testimonios.

- **WhatsApp Business**  
  • No es un canal de publicación tradicional, pero sí de *Estados*: **2 a 3 veces por semana**. Comparte lanzamientos, cupos limitados para Bogotá, tips de cuidado o recordatorios de stock.  
  • Para mensajes directos, **no publiques manualmente**; activa flujos automáticos (bienvenida, post-compra, recuperación de carrito, seguimiento de uso de *Aurora*) para mantener la conversación sin depender de tu tiempo diario.

**Claves para sostenerlo sin burnout:**  
1. **Graba en bloques:** 1 sesión semanal (2-3 horas) te da 8-10 piezas editables.  
2. **Repurpose inteligente:** 1 Reel → 1 TikTok + 3 Historias + 1 Estado de WhatsApp.  
3. **Distribución por producto:** 70% valor/educación (justifica el premium de *Aurora*), 20% demostración/entretenimiento (*Sol*), 10% venta directa o UGC (*Luna* para bajar barrera de entrada).

¿Quieres que te arme una plantilla de calendario semanal con ejemplos concretos de guiones, formatos y horarios de publicación optimizados para Bogotá?

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Para productos de skincare, especialmente con un ítem premium como *Aurora*, el contenido que mejor convierte y retiene es el que combina **educación aplicada, evidencia visible y experiencia sensorial**. Estos son los 5 formatos con mayor rendimiento en Colombia y cómo adaptarlos a tu portafolio:

1. **Rutinas paso a paso (Educación aplicada)**  
   - *Por qué funciona:* El skincare exige constancia; mostrar cómo integrar *Aurora* en la rutina AM/PM reduce la fricción de compra y justifica el precio premium.  
   - *Formato:* Reels/TikToks de 30-45 seg con voz en off, pasos numerados y adaptación por tipo de piel.  
   - *Tu ventaja:* Contextualiza para Bogotá (altitud, clima seco, contaminación urbana). *Botica Verde* y *Skin Lab* suelen usar pasos genéricos; tú puedes mostrar cómo tu set se ajusta a la realidad local.

2. **Resultados reales / Antes y después (Prueba social)**  
   - *Por qué funciona:* La piel es visual; los cambios medibles (hidratación, luminosidad, textura) generan credibilidad inmediata.  
   - *Formato:* Carruseles o videos con mismo ángulo, luz natural y lapsos de 2-4 semanas. Incluye testimonios breves en texto o audio.  
   - *Tu ventaja:* Usa *Luna* para mostrar resultados rápidos (7-10 días) como prueba de entrada, y *Aurora* para evolución a mediano plazo (barrera cutánea, uniformidad).

3. **Desglose de ingredientes y ciencia (Transparencia premium)**  
   - *Por qué funciona:* El público de skincare premium investiga; explicar el “por qué” detrás de cada activo valida el ticket alto.  
   - *Formato:* Gráficos simples, comparativas visuales o videos tipo “qué hay dentro de Aurora”.  
   - *Tu ventaja:* Si tus fórmulas son clean, dermatológicamente probadas o libres de irritantes comunes, resáltalo. Diferénciate del tono clínico de *Skin Lab* equilibrando ciencia + cercanía emocional.

4. **Texturas, ASMR y experiencia sensorial (Engagement puro)**  
   - *Por qué funciona:* El skincare se “siente” antes de comprarlo. Los videos de aplicación, absorción y packaging retienen +60% más en TikTok/Reels.  
   - *Formato:* 15-20 seg, primeros planos, sonido ambiente, sin voz, solo subtítulos.  
   - *Tu ventaja:* Úsalo como gancho para luego redirigir a una rutina o testimonio. Ideal para *Aurora* (serum/crema) y *Luna* (textura corporal).

5. **Mitos vs. Realidad + Preguntas frecuentes (Autoridad y cierre)**  
   - *Por qué funciona:* Resuelve objeciones de compra (“¿el serum engrasa?”, “¿sirve para piel sensible con maquillaje?”) y posiciona tu marca como experta.  
   - *Formato:* Stories interactivas convertidas en Reels/TikToks de respuesta.  
   - *Tu ventaja:* Vincula las dudas con la sinergia *Aurora* + *Sol* (preparación de piel base que no obstruye poros) y usa *Luna* para derribar mitos sobre cremas corporales “pesadas”.

**Regla práctica para tu operación:**  
Mantén la proporción **70% valor/educación + 20% evidencia/UGC + 10% venta directa**. Para *Aurora* prioriza ciencia y rutinas; para *Luna*, texturas y testimonios rápidos; para *Sol*, enfócate en la compatibilidad skincare-maquillaje natural.

¿Quieres que te entregue 3 guiones listos para grabar esta semana (uno por producto), con estructura probada, ganchos de los primeros 3 segundos y llamado a la acción alineado a Bogotá?

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Para diferenciarte de `Botica Verde` y `Skin Lab` sin competir por precio, debes elevar el **valor percibido** y convertir tu marca en una experiencia que ellos no replican fácilmente. Aquí tienes 5 ejes concretos, diseñados para tu portafolio y tu mercado en Bogotá:

### 1. Hiperlocalización inteligente
- **Qué hacer:** Posiciona tu línea como la primera formulada/optimizada para la realidad cutánea bogotana (altitud ~2.600 m, baja humedad, contaminación urbana, agua con minerales).
- **Cómo se ve en práctica:** 
  - Contenido: *"Por qué tu serum no absorbe igual en Chapinero que en Miami"*, *"Rutina anti-polución para el tráfico de la 7ma"*.
  - Empaque/Comunicación: Incluye una mini-guía digital *"Cuidado facial para el clima de Bogotá"* con cada pedido de `Aurora`.
- **Diferencia vs competencia:** Ellos suelen usar mensajes globales o genéricos; tú hablas el lenguaje de la piel local.

### 2. Ecosistema de cuidado (no productos aislados)
- **Qué hacer:** Vende la sinergia entre tus 3 líneas como un ciclo completo: `Aurora` prepara y repara, `Sol` potencia sin obstruir, `Luna` cierra y mantiene la barrera corporal.
- **Cómo se ve en práctica:** 
  - Combos temáticos: *"Prep & Glow"* (`Aurora` + `Sol`), *"Weekend Reset"* (`Luna` + guía de exfoliación suave).
  - En redes: Muestra cómo `Sol` se aplica sobre piel ya tratada con `Aurora` para evitar oxidación o clogging.
- **Diferencia vs competencia:** Ellos venden SKUs; tú vendes un sistema con lógica clara, lo que justifica el premium y aumenta el ticket promedio sin descuentos.

### 3. Experiencia de compra y postventa tipo "asesora personal"
- **Qué hacer:** Usa WhatsApp Business como canal de acompañamiento, no solo de cierre.
- **Cómo se ve en práctica:** 
  - Flujo automático: Día 1 (guía de uso), Día 7 (check-in + ajuste de rutina), Día 21 (foto de evolución + recomendación de `Sol` o `Luna` según necesidad).
  - Garantía de adaptación: Si en 14 días la piel no responde, ofreces cambio de producto o sesión 1:1 con una especialista aliada.
- **Diferencia vs competencia:** `Skin Lab` suele ser frío/clínico; `Botica Verde`, transaccional. Tú ofreces cercanía experta que retiene y genera referidos.

### 4. Transparencia radical y educación accesible
- **Qué hacer:** Explica el "por qué" detrás de cada precio, ingrediente y fórmula sin tecnicismos vacíos.
- **Cómo se ve en práctica:** 
  - Reels tipo *"Lo que pagas en Aurora (y lo que no)"*: desglose de activos, pruebas de estabilidad, origen de insumos.
  - Comparativas honestas: *"¿Cuándo sí conviene una crema de entrada? Cuándo invertir en un set premium"*.
- **Diferencia vs competencia:** El público premium investiga; si tú educas con honestidad, el precio deja de ser objeción y se vuelve señal de calidad.

### 5. Voz de marca y comunidad local
- **Qué hacer:** Construye un tono cálido, experto y bogotano. Nada de "piel perfecta", sino "piel que respira en tu ritmo".
- **Cómo se ve en práctica:** 
  - UGC real de clientas de localidades específicas (Usaquén, Kennedy, Suba, etc.).
  - Alianzas con esteticistas, dermatólogos o coaches de bienestar locales para lives o talleres virtuales gratuitos.
  - Nombre para tu comunidad: *"Círculo Bogotá Glow"* o similar, con acceso a contenido exclusivo y preventas.
- **Diferencia vs competencia:** Humanizas la marca. Ellos compiten por alcance; tú compites por pertenencia.

### 🔑 Cómo implementarlo sin saturarte:
1. Elige **1 eje para lanzar este mes** (recomiendo hiperlocalización + ecosistema).
2. Convierte cada eje en **3 piezas de contenido reutilizables** (1 Reel, 1 carrusel, 1 flujo de WhatsApp).
3. Mide no solo ventas, sino **tasa de retención a 30 días** y **preguntas resueltas por WhatsApp** (indicadores reales de diferenciación).

¿Quieres que te arme el guion de lanzamiento para el primer eje (con copy, estructura de video y flujo de WhatsApp listo para copiar y pegar), o prefieres definir primero cómo medir el impacto de esta estrategia en tus KPIs?

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Para el primer trimestre, tu foco debe ser **validar, establecer líneas base y optimizar** antes de escalar. Te recomiendo medir estos KPIs agrupados por función, todos alineados a tu portafolio, canales y estrategia de diferenciación:

### 🔍 1. Adquisición & Tráfico
- **CPA (Costo por Adquisición) por canal**: Meta, TikTok, Google Ads y orgánico+WhatsApp. *Meta Q1*: validar qué canal trae compradores reales, no solo curiosos.
- **% de tráfico geolocalizado (Bogotá)**: Asegura que el 85-90% de tus visitas vengan de tu mercado objetivo.
- **CTR de anuncios y contenido**: Indicador de resonancia del mensaje (hiperlocal, sinergia de productos, transparencia).

### 🛒 2. Conversión & Ventas
- **Tasa de conversión del sitio**: % de visitantes que compran. *Benchmark CO belleza*: 1.5-3%. Si está <1.5%, revisa fricción en checkout o falta de prueba social.
- **AOV (Valor Promedio del Pedido)**: Clave para rentabilizar el tráfico. Monitorea si los combos `Aurora+Sol` o `Luna+Sol` lo elevan vs. compras unitarias.
- **Tasa de abandono de carrito**: Objetivo <70%. Activa recuperación por WhatsApp con asesoría o guía de uso, no solo descuento.

### 💰 3. Rentabilidad & Eficiencia
- **ROAS por producto/campaña**: Mínimo 3x en Q1 para validar viabilidad. Separa por `Aurora` (premium), `Sol` (medio) y `Luna` (entrada).
- **Margen bruto por pedido**: Después de costo de producto, envío en Bogotá, comisión de pasarela y packaging. Te dirá si tu pricing y mix son sostenibles.
- **CAC vs. Tasa de recompra temprana (30-60 días)**: En Q1 aún no tienes LTV real, pero sí puedes medir cuántos compran una segunda vez. Si >15%, tu ecosistema y asesoría están funcionando.

### 📦 4. Desempeño por Producto (Mix & Sinergia)
- **% de ventas por SKU**: `Aurora` / `Sol` / `Luna`. Te muestra si el mercado responde al premium o si `Luna` está actuando como puerta de entrada.
- **Tasa de cross-sell**: % de compradores de `Luna` que añaden `Sol` o `Aurora` en la misma compra o en los siguientes 30 días.
- **Devoluciones/consultas por producto**: Indicador temprano de expectativas vs. realidad (clave para mantener transparencia y evitar guerra de precios).

### 💬 5. Experiencia & Retención (Tu diferenciador)
- **% de consultas cerradas por WhatsApp**: Mensajes que terminan en compra o asesoría programada. Meta Q1: >40%.
- **Tasa de engagement de valor (IG/TikTok)**: `(Guardados + Compartidos) / Alcance`. Los likes son vanity; los guardados/compartidos indican que tu contenido educativo o hiperlocal está generando intención.
- **NPS o satisfacción post-compra**: Encuesta de 1 pregunta a los 7 días. Te da feedback rápido para ajustar guías, empaque o flujos.

### 🛠️ Cómo medirlo sin complicarte
- **Meta Pixel + GA4**: Conversión, tráfico, ROAS, AOV, abandono.
- **Shopify/WooCommerce + Spreadsheet**: Mix de ventas, margen, recompra temprana.
- **WhatsApp Business + ManyChat/Tool similar**: Tasa de cierre, tiempo de respuesta, recuperación de carrito.
- **Revisión semanal**: 30 min para ajustar presupuestos, creatividades y flujos. **Revisión mensual**: decidir escalar, pausar o pivotar.

### 🚫 Qué NO priorizar en Q1
- Seguidores, impresiones o likes sin conversión.
- LTV completo (requiere +6 meses de datos).
- Compararte directamente con el volumen de `Botica Verde` o `Skin Lab`; en Q1 tu métrica real es **eficiencia y validación de propuesta**.

¿Quieres que te arme una plantilla de dashboard en Google Sheets con estas métricas, fórmulas automáticas y un checklist semanal de revisión, o prefieres definir primero los umbrales de alerta (cuándo pausar una campaña o cambiar un flujo de WhatsApp)?

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

Aquí tienes el plan de campaña de 4 semanas, diseñado exclusivamente para **`Aurora`** y alineado a tu contexto de Bogotá, posicionamiento premium y canales priorizados:

### 🎯 Objetivo
Generar **150-200 ventas directas de `Aurora` en Bogotá** en 4 semanas, validando la disposición a pagar precio premium mediante educación hiperlocal, prueba social real y cierre asesorado por WhatsApp. Meta de eficiencia: **ROAS ≥ 3.5x** y **tasa de conversión de la landing de `Aurora` ≥ 2.5%**.

### 👥 Audiencia
- **Demografía:** Mujeres 25-45 años, residentes en Bogotá (estratos 4-6), con poder adquisitivo medio-alto a alto.
- **Psicografía/Intereses:** Skincare premium, belleza limpia, dermatología, bienestar, sostenibilidad, rutinas de autocuidado, seguidoras de dermatólogos/esteticistas locales.
- **Comportamiento:** Compradoras online frecuentes, usuarias de pasarelas con tarjeta/cuotas, interactúan con contenido educativo (guardan/comparten), excluye intereses de "ofertas", "maquillaje económico" o "dupes".
- **Segmentación técnica:** Públicos de intención (búsquedas de `Aurora`/competencia premium), Lookalike 1-3% de compradores previos (si existen), y retargeting por interacción con contenido de `Aurora`.

### 📡 Canales
1. **Meta Ads (Instagram + Facebook):** Reels, carruseles y Stories para storytelling visual y conversión directa.
2. **TikTok Ads:** In-Feed + Spark Ads para alcance orgánico amplificado con tono auténtico y UGC.
3. **WhatsApp Business:** Flujo de asesoría 1:1, quiz de tipo de piel, recuperación de carrito y cierre personalizado para `Aurora`.
4. **Google Ads (Búsqueda):** Captura de intención alta con keywords geo-localizadas y de alto valor comercial.
5. **Orgánico (IG + TikTok):** 3 piezas semanales + Historias diarias para sostener el algoritmo y nutrir el embudo.

### 💬 Mensaje Principal
*"Tu piel en Bogotá enfrenta altitud, clima seco y polución. `Aurora` no es solo un set facial: es un ritual premium formulado para restaurar tu barrera cutánea, con activos visibles y asesoría personalizada incluida. Invierte en resultados reales, no en promesas."*

---

### 📅 Plan Semanal (4 semanas)

**Semana 1: Conciencia + Educación (Validación de propuesta `Aurora`)**
- **Acción:** Lanzar 2 Reels/TikToks educativos: "¿Por qué tu rutina falla en Bogotá?" + desglose de 1 activo clave de `Aurora`. Activar campaña de tráfico/conversión en Meta y TikTok.
- **WhatsApp:** Flujo automático con quiz de tipo de piel + entrega de mini-guía "Cuidado facial para la altitud de Bogotá".
- **Métrica de validación:** CTR > 1.5%, tasa de inicio de quiz > 20%, costo por lead < 15% del precio de `Aurora`.

**Semana 2: Prueba Social + Rutina (Confianza en `Aurora`)**
- **Acción:** Carruseles y Spark Ads con "Antes/Después 14 días usando `Aurora`", UGC de clientas bogotanas y video de rutina AM/PM paso a paso.
- **WhatsApp:** Seguimiento día 3 a quienes hicieron el quiz: mensaje de voz/texto con recomendación personalizada de `Aurora` + enlace directo a checkout.
- **Métrica de validación:** Tasa de conversión landing `Aurora` ≥ 2%, guardados/compartidos ≥ 5% del alcance, consultas WhatsApp activas ≥ 30/día.

**Semana 3: Cierre + Asesoría (Conversión de `Aurora`)**
- **Acción:** Retargeting agresivo (carrito abandonado, video visto >50%, visitantes landing `Aurora`). Activar Google Ads con keywords: "set facial premium Bogotá", "cuidado facial altitud Bogotá".
- **WhatsApp:** Mensaje de cierre con valor añadido: "Agenda tu sesión 1:1 gratuita para ajustar tu rutina con `Aurora`" + recordatorio de stock limitado para envíos en Bogotá.
- **Métrica de validación:** ROAS ≥ 3x, CAC ≤ 30% del precio de `Aurora`, tasa de cierre por WhatsApp ≥ 35%.

**Semana 4: Optimización + Escalado Controlado (`Aurora`)**
- **Acción:** Pausar creatividades con ROAS < 2.5x. Escalar presupuesto en las 2 mejores piezas. Crear Lookalike 1% de compradores de `Aurora`. Lanzar campaña de valor (Value Optimization) en Meta.
- **WhatsApp:** Post-compra día 7: check-in de uso de `Aurora`, solicitud de reseña/foto y activación de programa "Círculo Bogotá Glow" para retención.
- **Métrica de validación:** ROAS ≥ 3.5x, tasa de conversión ≥ 2.5%, NPS post-compra ≥ 8/10, % de compradores `Aurora` que inician segunda interacción ≥ 15%.

---

### 📊 Métricas de Éxito (Campaña `Aurora`)
| Indicador | Meta Q1 | Herramienta de medición |
|-----------|---------|------------------------|
| Ventas directas de `Aurora` | 150-200 | Shopify/WooCommerce + GA4 |
| ROAS campaña `Aurora` | ≥ 3.5x | Meta Ads Manager / TikTok Ads / Google Ads |
| Tasa de conversión (landing `Aurora`) | ≥ 2.5% | GA4 + Hotjar (si aplica) |
| CAC `Aurora` | ≤ 30% del precio | Spreadsheet de costos de campaña |
| Tasa de cierre por WhatsApp | ≥ 35% | WhatsApp Business + ManyChat |
| Engagement de valor (`Aurora`) | Guardados/Compartidos ≥ 8% alcance | Insights nativos IG/TikTok |
| NPS post-compra `Aurora` | ≥ 8/10 | Encuesta automática día 7 |

¿Quieres que te entregue el **guion exacto de los 3 anuncios de la Semana 1** (gancho, cuerpo, CTA) + el **flujo de WhatsApp preconfigurado** para que solo copies, pegues y lances `Aurora` esta semana?


## Respuesta completa

Aquí tienes el plan de campaña de 4 semanas, diseñado exclusivamente para **`Aurora`** y alineado a tu contexto de Bogotá, posicionamiento premium y canales priorizados:

### 🎯 Objetivo
Generar **150-200 ventas directas de `Aurora` en Bogotá** en 4 semanas, validando la disposición a pagar precio premium mediante educación hiperlocal, prueba social real y cierre asesorado por WhatsApp. Meta de eficiencia: **ROAS ≥ 3.5x** y **tasa de conversión de la landing de `Aurora` ≥ 2.5%**.

### 👥 Audiencia
- **Demografía:** Mujeres 25-45 años, residentes en Bogotá (estratos 4-6), con poder adquisitivo medio-alto a alto.
- **Psicografía/Intereses:** Skincare premium, belleza limpia, dermatología, bienestar, sostenibilidad, rutinas de autocuidado, seguidoras de dermatólogos/esteticistas locales.
- **Comportamiento:** Compradoras online frecuentes, usuarias de pasarelas con tarjeta/cuotas, interactúan con contenido educativo (guardan/comparten), excluye intereses de "ofertas", "maquillaje económico" o "dupes".
- **Segmentación técnica:** Públicos de intención (búsquedas de `Aurora`/competencia premium), Lookalike 1-3% de compradores previos (si existen), y retargeting por interacción con contenido de `Aurora`.

### 📡 Canales
1. **Meta Ads (Instagram + Facebook):** Reels, carruseles y Stories para storytelling visual y conversión directa.
2. **TikTok Ads:** In-Feed + Spark Ads para alcance orgánico amplificado con tono auténtico y UGC.
3. **WhatsApp Business:** Flujo de asesoría 1:1, quiz de tipo de piel, recuperación de carrito y cierre personalizado para `Aurora`.
4. **Google Ads (Búsqueda):** Captura de intención alta con keywords geo-localizadas y de alto valor comercial.
5. **Orgánico (IG + TikTok):** 3 piezas semanales + Historias diarias para sostener el algoritmo y nutrir el embudo.

### 💬 Mensaje Principal
*"Tu piel en Bogotá enfrenta altitud, clima seco y polución. `Aurora` no es solo un set facial: es un ritual premium formulado para restaurar tu barrera cutánea, con activos visibles y asesoría personalizada incluida. Invierte en resultados reales, no en promesas."*

---

### 📅 Plan Semanal (4 semanas)

**Semana 1: Conciencia + Educación (Validación de propuesta `Aurora`)**
- **Acción:** Lanzar 2 Reels/TikToks educativos: "¿Por qué tu rutina falla en Bogotá?" + desglose de 1 activo clave de `Aurora`. Activar campaña de tráfico/conversión en Meta y TikTok.
- **WhatsApp:** Flujo automático con quiz de tipo de piel + entrega de mini-guía "Cuidado facial para la altitud de Bogotá".
- **Métrica de validación:** CTR > 1.5%, tasa de inicio de quiz > 20%, costo por lead < 15% del precio de `Aurora`.

**Semana 2: Prueba Social + Rutina (Confianza en `Aurora`)**
- **Acción:** Carruseles y Spark Ads con "Antes/Después 14 días usando `Aurora`", UGC de clientas bogotanas y video de rutina AM/PM paso a paso.
- **WhatsApp:** Seguimiento día 3 a quienes hicieron el quiz: mensaje de voz/texto con recomendación personalizada de `Aurora` + enlace directo a checkout.
- **Métrica de validación:** Tasa de conversión landing `Aurora` ≥ 2%, guardados/compartidos ≥ 5% del alcance, consultas WhatsApp activas ≥ 30/día.

**Semana 3: Cierre + Asesoría (Conversión de `Aurora`)**
- **Acción:** Retargeting agresivo (carrito abandonado, video visto >50%, visitantes landing `Aurora`). Activar Google Ads con keywords: "set facial premium Bogotá", "cuidado facial altitud Bogotá".
- **WhatsApp:** Mensaje de cierre con valor añadido: "Agenda tu sesión 1:1 gratuita para ajustar tu rutina con `Aurora`" + recordatorio de stock limitado para envíos en Bogotá.
- **Métrica de validación:** ROAS ≥ 3x, CAC ≤ 30% del precio de `Aurora`, tasa de cierre por WhatsApp ≥ 35%.

**Semana 4: Optimización + Escalado Controlado (`Aurora`)**
- **Acción:** Pausar creatividades con ROAS < 2.5x. Escalar presupuesto en las 2 mejores piezas. Crear Lookalike 1% de compradores de `Aurora`. Lanzar campaña de valor (Value Optimization) en Meta.
- **WhatsApp:** Post-compra día 7: check-in de uso de `Aurora`, solicitud de reseña/foto y activación de programa "Círculo Bogotá Glow" para retención.
- **Métrica de validación:** ROAS ≥ 3.5x, tasa de conversión ≥ 2.5%, NPS post-compra ≥ 8/10, % de compradores `Aurora` que inician segunda interacción ≥ 15%.

---

### 📊 Métricas de Éxito (Campaña `Aurora`)
| Indicador | Meta Q1 | Herramienta de medición |
|-----------|---------|------------------------|
| Ventas directas de `Aurora` | 150-200 | Shopify/WooCommerce + GA4 |
| ROAS campaña `Aurora` | ≥ 3.5x | Meta Ads Manager / TikTok Ads / Google Ads |
| Tasa de conversión (landing `Aurora`) | ≥ 2.5% | GA4 + Hotjar (si aplica) |
| CAC `Aurora` | ≤ 30% del precio | Spreadsheet de costos de campaña |
| Tasa de cierre por WhatsApp | ≥ 35% | WhatsApp Business + ManyChat |
| Engagement de valor (`Aurora`) | Guardados/Compartidos ≥ 8% alcance | Insights nativos IG/TikTok |
| NPS post-compra `Aurora` | ≥ 8/10 | Encuesta automática día 7 |

¿Quieres que te entregue el **guion exacto de los 3 anuncios de la Semana 1** (gancho, cuerpo, CTA) + el **flujo de WhatsApp preconfigurado** para que solo copies, pegues y lances `Aurora` esta semana?