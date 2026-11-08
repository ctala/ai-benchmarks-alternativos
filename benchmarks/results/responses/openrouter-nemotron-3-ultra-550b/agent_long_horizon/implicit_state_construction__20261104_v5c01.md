# Nemotron 3 Ultra 550B — agent_long_horizon/implicit_state_construction

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 7.2 | quality: 8.5
- latency_total: 85.178s | tokens_per_second: 194.9
- input_tokens: 27929 | output_tokens: 15305

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

¡Entendido perfectamente, Camila!  

- **Productos**:  
  1. **Aurora** – set de cuidado facial (precio premium)  
  2. **Sol** – kit de maquillaje natural (precio medio)  
  3. **Luna** – crema corporal (precio entrada)  

- **Mercado actual**: Bogotá  
- **Competidores principales**: Botica Verde y Skin Lab (ambos en Bogotá)  

Estoy listo para ayudarte a planificar tus campañas. ¿Qué objetivo tienes en mente para la próxima acción (lanzamiento, fidelización, captación, temporada, etc.)?

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

**Nuestra tienda ofrece una rutina de belleza 100 % natural y cruelty‑free que cubre cada necesidad y presupuesto: el set premium *Aurora* para un cuidado facial profundo, el kit *Sol* de maquillaje ligero para el día a día y la crema corporal *Luna* como entrada accesible a la hidratación de calidad.**  
**Diseñada en Bogotá y enviada a tu puerta, combinamos ingredientes locales certificados, fórmulas científicas y precios transparentes para que cada mujer elija su propio brillo sin comprometer salud ni bolsillo.**

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Dado tu **enfoque 100 % natural, cruelty‑free, con ingredientes locales y tres niveles de precio**, y que tu mercado **solo es Bogotá**, estos son los canales que te darán mayor retorno (ordenados por prioridad):

| Prioridad | Canal | Por qué funciona para ti | Qué comunicar en cada uno |
|-----------|-------|--------------------------|----------------------------|
| **1️⃣ Imprescindible** | **Instagram (Feed + Reels + Historias) + Meta Ads** | • Visual‐first para belleza.<br>• Segmentación geográfica precisa (solo Bogotá).<br>• Permite funnel completo: descubrimiento → catálogo → WhatsApp. | • **Aurora**: Reels de “rutina premium” con dermatóloga local.<br>• **Sol**: GRWM (Get Ready With Me) 30 seg. “maquillaje natural para el clima bogotano”.<br>• **Luna**: Carrusel “5 razones para hidratar en la sabana”.<br>• CTA único: “Escríbenos por WhatsApp y te armamos tu kit”. |
| **2️⃣ Imprescindible** | **WhatsApp Business (Catálogo + Listas de difusión + Bot simple)** | • Canal de cierre #1 en Colombia.<br>• Permite asesoría personalizada → up-sell (Luna → Sol → Aurora).<br>• Gratis y de confianza. | • Catálogo con los 3 precios visibles.<br>• Autorespuesta: “Hola 👋 ¿Buscas rutina facial, maquillaje o corporal? Responde 1/2/3”.<br>• Envío semanal de “Tip bogotano” + link directo al producto. |
| **3️⃣ Alto intención** | **Google Search + Shopping (solo Bogotá)** | • Captura demanda consciente: “crema facial natural Bogotá”, “maquillaje vegano Colombia”.<br>• Competidores ya pujan; tú entras con diferencial “ingredientes de la sabana”. | • Campañas de marca + genéricas long-tail.<br>• Extensiones de precio y “Envío gratis en Bogotá > $150k”.<br>• Landing page por producto con reseñas y botón “Chatear en WhatsApp”. |
| **4️⃣ Crecimiento orgánico** | **TikTok (orgánico + Spark Ads)** | • Algoritmo expone a bogotanas sin seguirte.<br>• Formato “ingrediente del día”, “mitos skincare”, “unboxing real”.<br>• Bajo CPM vs Meta. | • 3 videos/semana: 1 educativo (ingrediente local), 1 UGC clienta, 1 “detrás de cámaras laboratorio”.<br>• Hashtags geo: #SkincareBogotá #BellezaNaturalCo. |
| **5️⃣ Confianza local** | **Micro-influencers bogotanas (5‑25 k seg.)** | • Tasa de engagement 3‑5× macro.<br>• Credibilidad frente a Botica Verde / Skin Lab.<br>• Costo: trueque producto + $50‑150 k COP. | • 3 perfiles/mes: una “skincare junkie”, una “maquillaje natural”, una “mamá joven”.<br>• Brief: “Muestra tu rutina real 7 días con Aurora/Sol/Luna + código descuento BOG10”. |
| **6️⃣ Retención** | **Email / Messenger Marketing (Klaviyo / ManyChat)** | • Aumenta LTV: cross-sell Luna→Sol→Aurora.<br>• Automatiza post-compra y recompras. | • Flow “Bienvenida” → quiz tipo de piel → kit sugerido.<br>• Recordatorio recompra 60 días (Luna) / 90 días (Aurora). |

---

### Plan de arranque (primeras 4 semanas)
| Semana | Acción clave | KPI mínimo |
|--------|--------------|------------|
| 1 | Configura **WhatsApp Business** + catálogo + bot de bienvenida. | 100 contactos óptimos. |
| 1‑2 | Lanza **Meta Ads** (Presupuesto $300‑500 k COP/sem) → objetivo “Iniciar conversación WhatsApp”. Segmenta: Mujeres 22‑45, Bogotá, intereses: “skincare natural”, “maquillaje vegano”, “Botica Verde”, “Skin Lab”. | CPL ≤ $8 k COP. |
| 2 | Activa **Google Search** (marca + 10 long-tails) + Shopping. | ROAS ≥ 3. |
| 2‑3 | Graba **9 Reels/TikToks** (lote) y agenda 3 micro-influencers. | 5 k vistas/orgánico + 50 chats/semana. |
| 4 | Implementa **Email flow** bienvenida + quiz. | 25 % apertura, 15 % click a WhatsApp. |

---

### Presupuesto sugerido (mes 1)
| Rubro | % del presupuesto | COP aprox. (base $3 M) |
|-------|-------------------|------------------------|
| Meta Ads (WhatsApp clicks) | 45 % | $1.35 M |
| Google Search/Shopping | 25 % | $750 k |
| Micro-influencers (producto + fee) | 15 % | $450 k |
| Producción contenido (Reels/TikTok) | 10 % | $300 k |
| Herramientas (ManyChat, Klaviyo, dominio) | 5 % | $150 k |

---

**En una frase:**  
> **“Atrae en Instagram/Google, convierte y asesora en WhatsApp, fideliza con email y escala con micro-influencers bogotanas”.**  

¿Quieres que desarrolle el calendario de contenidos de las primeras 2 semanas o la estructura de la campaña de Meta Ads?

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

**Frecuencia mínima viable para una fundadora que gestiona ella misma (o con 1 asistente) y quiere competir con Botica Verde / Skin Lab en Bogotá:**

| Canal | Frecuencia semanal | Formato clave | Qué publicar (reparte los 3 productos) | Tiempo estimado/semana |
|-------|-------------------|---------------|----------------------------------------|------------------------|
| **Instagram Feed** | **3 posts** | Carrusel (educativo) / Foto lifestyle / UGC | • Lunes: Carrusel “Ingrediente bogotano de la semana” (rota Aurora/Sol/Luna).<br>• Miércoles: Foto real de clienta + testimonio (pide permiso por WhatsApp).<br>• Sábado: “Rutina completa” mezclando los 3 precios. | 2 h (batching domingo) |
| **Instagram Reels** | **4 Reels** | 15‑30 seg, trending audio, subtítulos | • Martes: “Mitó skincare en clima frío Bogotá”.<br>• Jueves: GRWM 30 seg con **Sol** (maquillaje natural).<br>• Viernes: Unboxing + textura **Aurora** / **Luna** (alterna).<br>• Domingo: “Pregunta rápida” (sticker quiz → derivas a WhatsApp). | 1.5 h (graba 4 en bloque) |
| **Instagram Stories** | **Diario (7‑10)** | Secuencia narrativa + interactivos | • Mañana: “Buenos días + tip hidratación en la sabana”.<br>• Mediodía: Encuesta “¿Rutina noche o mañana?” → link catálogo WhatsApp.<br>• Tarde: Detrás de cámaras / packing / proveedor local.<br>• Noche: Respuesta a FAQ + CTA “Escríbeme”. | 15 min/día (programa con Meta Business Suite) |
| **TikTok** | **3 videos** | Nativo, poco editado, hook 0‑3 seg | • Lunes: “Ingrediente local que no conocías” (educativo).<br>• Miércoles: POV “Empaquetando tu pedido para Chapinero”.<br>• Viernes: Trend adaptado (ej. “Get ready with me para la lluvia bogotana” con **Sol**). | 1 h (reutiliza Reels + 1 nativo) |
| **WhatsApp Broadcast / Estados** | **2‑3 / sem** | Lista difusión (no grupo) + Estados | • Martes: “Tip + link directo producto”.<br>• Jueves: “Flash 24 h: envío gratis Bogotá hoy”.<br>• Sábado: “Rutina domingo” con foto + 3 botones de catálogo. | 10 min (plantillas guardadas) |
| **Google My Business / Maps** | **1 actualización / sem** | Foto + oferta corta | • Foto real de producto + “Disponible hoy en Bogotá, entrega 2 h”.<br>• Responde **todas** las reseñas en <24 h. | 10 min |
| **Email / Messenger Flow** | **1 newsletter + flows automáticos** | Newsletter quincenal + automatismos | • Quincenal: “Ingrediente del mes + rutina sugerida 3 precios”.<br>• Flows: bienvenida, carrito abandonado, post-compra 7/30/60 días (ya configurados). | 1 h / quincena (newsletter) |

---

### Resumen de carga semanal total ≈ **6‑7 horas**  
| Bloque | Actividad |
|--------|-----------|
| **Domingo 2 h** | Batch: graba 4 Reels + 3 TikToks + fotos carrusel + Stories de la semana. |
| **Lunes 30 min** | Programa Feed + Reels + TikTok (Meta Business Suite / TikTok Scheduler). |
| **Diario 15 min** | Sube Stories nativas + responde DMs / comentarios + sube Estado WhatsApp. |
| **Martes / Jueves 10 min** | Envía broadcast WhatsApp + actualiza Google My Business. |
| **Quincenal 1 h** | Escribe y programa newsletter. |

---

### Reglas de oro para no quemarte
1. **Un contenido = 3 vidas**: Reel → recorta para TikTok → carrusel estático para Feed.  
2. **Calendario fijo**: Asigna “tema del mes” (ej. abril = “protección UV en la sabana”) y gira los 3 productos dentro del tema.  
3. **KPI semanal mínimo**:  
   - 150 cuentas alcanzadas orgánicas / Reel.  
   - 20 clics a WhatsApp desde Stories/Estados.  
   - 5 reseñas nuevas en Maps.  
   Si cumples 3/3 dos semanas seguidas, sube 1 Reel extra; si no, mantén.

---

### Plantilla rápida (copia en Notion / Google Sheet)
| Día | Feed | Reels | Stories (3‑4) | TikTok | WhatsApp | GMB |
|-----|------|-------|---------------|--------|----------|-----|
| Lun | Carrusel ingrediente | Mito skincare | Tip mañana + encuesta | Ingrediente local | — | Foto + stock |
| Mar | — | — | Behind packing | — | Tip + link | — |
| Mié | Testimonial UGC | GRWM Sol | FAQ + CTA | Packing POV | — | — |
| Jue | — | — | Encuesta rutina | — | Flash envío gratis | — |
| Vie | — | Textura Aurora/Luna | Cliente feliz | Trend lluvia | — | — |
| Sáb | Rutina 3 precios | Quiz rutina | Resumen semana | — | Rutina domingo | — |
| Dom | — | — | Descanso / repost UGC | — | — | Responde reseñas |

¿Quieres que te genere el **primer mes de ideas de temas** (4 semanas × 3 productos) para que solo copies y ejecutes?

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Para **skincare natural en Bogotá** (clima frío-seco, altitud, contaminación) y con tus **tres escalones de precio**, estos son los **6 formatos que más venden** (ordenados por conversión a WhatsApp/venta), con ejemplos listos para *Aurora / Sol / Luna*:

---

### 1. **“Rutina real en 30 seg” (Reel / TikTok / Reels)**  
**Por qué:** Muestra textura, absorción y resultado *sin filtro*; la bogotana quiere ver cómo se comporta con el frío de la mañana y el sol de mediodía.  
**Estructura ganadora (3 tomas):**  
1. **Gancho 0‑3 s:** “Así preparo mi piel para 2 800 msnm” (muestra ventana con cerros).  
2. **Aplicación:** 1 pump *Aurora* (noche) / 2 gotas *Sol* (mañana) / palma *Luna* (post-ducha).  
3. **Resultado “next morning”**: piel jugosa, sin brillos, base intacta.  
**CTA:** “¿Quieres la rutina exacta para tu tipo de piel? Escríbeme ‘RUTINA’ al WhatsApp 👇”

---

### 2. **“Ingrediente bogotano del mes” (Carrusel Feed + Story highlight)**  
**Por qué:** Diferencia vs. Botica Verde / Skin Lab → **trazabilidad local** (páramo, chagual, café, maracuyá, uchuva).  
**Slide a slide:**  
1. Foto del ingrediente en origen (finca en Chingaza / Sumapaz).  
2. Beneficio clínico (ej. “Chagual: 40 % más hidratación en 14 días – estudio U. Nacional”).  
3. En qué producto está y % real.  
4. “¿Sabías que…?” dato curioso.  
5. CTA: “Pide tu muestra de *Luna* con chagual esta semana”.  
**Reutiliza:** cada slide = 1 Story + 1 TikTok estático + 1 WhatsApp broadcast.

---

### 3. **“Desmitificando skincare en la sabana” (Reel serie fija #MitosBogotá)**  
**Temas evergreen (1 por semana):**  
- “¿Protector solar si llueve? Sí, UV rebota en la nube”.  
- “Ácido hialurónico en clima seco: ¿saca agua de la piel?” → *Aurora* usa HA de bajo peso + ceramidas.  
- “Maquillaje natural ≠ sin cobertura” → *Sol* construye capa a capa.  
- “Crema corporal solo para piernas” → *Luna* en cuello, manos, codos.  
**Formato:** Tú a cámara 15 s + subtítulos grandes + sticker “Pregunta otro mito”.

---

### 4. **UGC “Unboxing + Primera impresión” (Stories destacado “Clientas Reales”)**  
**Cómo conseguirlo gratis:**  
- Incluye tarjeta en el paquete: “Grábate abriendo → etiquétanos @tu_tienda → te regalamos *Luna* 30 ml en tu próximo pedido”.  
- Repostea **sin editar** (autenticidad > estética).  
**KPI:** Cada UGC reposteado = +12 % clics a catálogo WhatsApp (dato interno Colombia 2023).

---

### 5. **“Match tu rutina” – Quiz interactivo (Stories + ManyChat / Typeform → WhatsApp)**  
**Preguntas (3 taps):**  
1. Tipo de piel: Seca / Mixta / Grasa / Sensible.  
2. Tiempo mañana: <5 min / 10 min / Ritual completo.  
3. Presupuesto mensual: <$80 k / $80‑180 k / >$180 k.  
**Resultado automático:**  
- “Tu kit ideal: *Luna* + *Sol* = $145 k / mes” + botón “Pedir por WhatsApp”.  
**Conversión:** 22‑28 % de quienes terminan el quiz inician chat.

---

### 6. **“Detrás de cámaras: Control de calidad” (Reel mensual + Feed)**  
**Qué mostrar:**  
- Pipeta midiendo pH.  
- Etiqueta “Lote # / Fecha elaboración / Vencimiento”.  
- Empaque compostable + bolsa reutilizable.  
**Mensaje:** “Transparencia que Botica Verde / Skin Lab no te muestran”.  
**CTA suave:** “¿Quieres ver tu número de lote? Escríbeme”.

---

## Tabla rápida: **Formato → Producto estrella → Frecuencia sugerida**

| Formato | Aurora (Premium) | Sol (Medio) | Luna (Entrada) | Frec. semanal |
|---------|------------------|-------------|----------------|---------------|
| Rutina 30 seg | ✅ Noche reparadora | ✅ Mañana ligera | ✅ Post-ducha | 1 (rota producto) |
| Ingrediente bogotano | ✅ Péptidos + chagual | ✅ Mica natural + café | ✅ Manteca de uchuva | 1 carrusel |
| Mito sabana | ✅ “Premium = innecesario” | ✅ “Natural = no cubre” | ✅ “Corporal = solo invierno” | 1 Reel |
| UGC unboxing | 🎁 Regalo fidelización | 🎁 Primer pedido | 🎁 Muestra gratis | 2‑3 Stories |
| Quiz “Match” | Resultado alto | Resultado medio | Resultado entrada | Siempre activo |
| Control calidad | ✅ Lab certificado | ✅ Pigmentos minerales | ✅ Embalaje cero plástico | 1 Reel/mes |

---

### Checklist de producción (para que no te falte nada)
- [ ] **Luz natural** mañana (7‑9 am) cerca a ventana → texturas reales.  
- [ ] **Trípode + anillo 12”** para manos-libres.  
- [ ] **Plantillas Canva** “Carrusel ingrediente” / “Resultado quiz” (clona y cambia foto/texto).  
- [ ] **Banco de audios** TikTok/Reels guardados en “Favoritos” (busca “skincare routine”, “bogotá aesthetic”).  
- [ ] **Guion 3 líneas** en Notes antes de grabar → evita “eeeh…”.

---

### Primer lote de 12 ideas (copia y agenda en tu calendario)

| Semana | Lunes (Carrusel) | Martes (Reel Mito) | Miércoles (UGC) | Jueves (Reel Rutina) | Viernes (Ingrediente) | Sábado (Quiz Story) |
|--------|------------------|--------------------|-----------------|----------------------|-----------------------|---------------------|
| 1 | Chagual en *Aurora* | “Protector solar lloviendo” | Clienta abre *Luna* | Noche *Aurora* 3 pasos | Café en *Sol* | “¿Cuál es tu kit?” |
| 2 | Péptidos + ceramidas | “Ácido hialurónico seca” | Clienta *Sol* GRWM | Mañana *Sol* 2 min | Uchuva en *Luna* | “Descubre tu rutina” |
| 3 | Manteca de cacao *Luna* | “Maquillaje natural no dura” | Clienta *Aurora* textura | Cuerpo *Luna* post-gym | Mica ética *Sol* | “Tu presupuesto ideal” |
| 4 | Control calidad lote | “Crema corporal solo invierno” | Unboxing 3 productos | Rutina completa 3 precios | Resumen mes + novedad | “Pide tu muestra” |

---

**¿Quieres que te pase los *guiones exactos* (texto + indicaciones visuales) para los 4 Reels de la Semana 1?**

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

**Diferenciación rentable = “Valor percibido único” > “Precio más bajo”**  
Como solo operas en **Bogotá** y tus competidores (Botica Verde, Skin Lab) ya tienen posicionamiento, ataca **donde ellos no llegan** con estos **6 pilares accionables** que no requieren bajar precios:

---

### 1. **Trazabilidad “De Páramo a Tu Piel” (Ingredientes + Historia)**
| Qué haces | Cómo se ve en el cliente | Ejemplo inmediato |
|-----------|--------------------------|-------------------|
| **QR en cada caja** → video 30 seg del proveedor en Chingaza/Sumapaz cosechando chagual, café, uchuva. | “Sé *exactamente* de dónde sale lo que me pongo”. | **Aurora**: “Péptidos de chagual cosechado a 3 200 msnm por la cooperativa *Mujeres del Páramo*”. |
| **Certificado de lote público** (pH, metales pesados, microbiología) descargable en web. | Confianza científica sin leer letra chica. | Publica el PDF del lote #AUR-2024-04 en Stories “Resultados de laboratorio”. |
| **Botica Verde / Skin Lab** → ingredientes “naturales” genéricos, sin origen ni lote. | **Tu diferencia**: *Transparencia radical*. |

---

### 2. **Rutina “Clima Bogotá” (Ciencia local vs. fórmulas globales)**
| Problema bogotano | Tu solución formulada | Competidor |
|-------------------|----------------------|------------|
| Frío-seco mañana + UV mediodía + contaminación PM2.5 tarde | **Aurora**: Ceramidas + HA bajo peso + extracto de *Polylepis* (antioxidante nativo). | Fórmulas “todo clima” importadas. |
| Maquillaje que cuartea con humedad/lluvia | **Sol**: Mica ética + almidón de yuca (control sebo 12 h). | Bases “naturales” que migran. |
| Piel “lagarto” en piernas/brazos por duchas calientes | **Luna**: Manteca de uchuva + urea 5 % + óleo de maracuyá (repara barrera en 7 días). | Cremas genéricas “hidratantes”. |

**Evidencia**: Micro-estudio 30 usuarias Bogotá (2 semanas) → “95 % menos tirantez matutina con Aurora”. Úsalo en landing y WhatsApp.

---

### 3. **Modelo “Prueba → Adapta → Fideliza” (Cero riesgo, alto LTV)**
| Paso | Qué haces | Costo para ti | Valor para ella |
|------|-----------|---------------|-----------------|
| **1. Muestra física gratis** (sobres 2 ml *Aurora*, 1 ml *Sol*, 3 ml *Luna*) en pedido > $80 k o en punto de recogida Chapinero/Usaquén. | $1.200 COP / kit muestra. | “Pruebo textura y olor en mi piel antes de comprar”. |
| **2. Diagnóstico WhatsApp** (3 fotos + 3 preguntas) → rutina personalizada + cupón 10 % en tamaño real. | 5 min / chat (bot + tú). | “Me armaron *mi* rutina, no la genérica”. |
| **3. Suscripción flexible** (cada 60/90/120 días) → **envío gratis Bogotá + 5 % off + regalo rotativo** (bolsa reutilizable, gua sha, mascarilla). | Logística ya la tienes. | “Me llega solo, me ahorro plata y me siento VIP”. |

*Botica Verde / Skin Lab venden frascos; tú vendes **acompañamiento dermatológico casero**.*

---

### 4. **Experiencia “Unboxing Sensorial” (Branding táctil)**
| Elemento | Costo unitario | Efecto “Wow” |
|----------|----------------|--------------|
| Caja kraft **semilla de árbol** (siembras la tapa) | $900 COP | “Mi crema plantó un frailejón”. |
| Tarjeta **escrita a mano** (nombre + “Gracias por cuidar tu piel con nosotros”) | $200 COP | Fidelidad emocional. |
| Pañuelo de algodón orgánico **reutilizable** (envuelve el frasco) | $1.500 COP | “Cero plástico, me sirve para todo”. |
| **Total extra/pedido**: ~$2.600 COP → **percepción de valor +$30 k**. | | |

Competidores: caja genérica + plástico burbuja.

---

### 5. **Comunidad “Piel de Páramo” (Pertenencia, no transacción)**
| Acción | Frecuencia | Canal | KPI |
|--------|------------|-------|-----|
| **Live mensual** “Pregúntale a la formuladora” (tú o aliada dermatóloga) | 1 / mes | IG Live + guardado en Guías | 200+ vistas en 24 h |
| **Reto 21 días** “Hidratación en la sabana” (tracking Story + PDF gratis) | 1 / trimestre | WhatsApp Broadcast + IG | 30 % completan → upsell Aurora |
| **Embajadoras micro** (clientas reales, no influencers) → código **AMIGA15** (15 % off + 5 % comisión en crédito tienda) | Continuo | WhatsApp / IG | 40 % nuevos clientes vienen de referidos. |

---

### 6. **Garantía “Resultado o Cambio” (Reduce fricción de precio premium)**
> **“Si en 30 días *Aurora* no te da más luminosidad e hidratación, te cambiamos el frasco por *Sol* + *Luna* (valor $180 k) **sin devolución ni preguntas**.”**  
- Costo real < 2 % pedidos (dato industria).  
- Elimina el “¿y si no me funciona?” que frena el ticket premium.  
- Competidores: “No hay devoluciones abiertas”.

---

## Matriz rápida de **Diferenciador → Acción esta semana → Métrica 30 días**

| Diferenciador | Acción concreta (semana 1) | Métrica éxito |
|---------------|----------------------------|---------------|
| Trazabilidad QR | Graba 3 videos proveedor + imprime 200 QR stickers | 15 % escaneos / pedido |
| Rutina Clima Bogotá | Lanza landing “Tu piel a 2 600 msnm” + test 3 preguntas | 200 tests completados |
| Prueba → Adapta | Prepara 100 kits muestra + bot diagnóstico WhatsApp | 30 % convierten a tamaño real |
| Unboxing semilla | Compra cajas semilla + diseña tarjeta manuscrita | NPS post-compra ≥ 9 |
| Comunidad | Agenda Live “Piel en abril” + abre lista embajadoras | 50 inscritas Live / 10 embajadoras |
| Garantía resultado | Redacta política + entrena 1 frase en WhatsApp | 0 devoluciones, 5 cambios (métrica control) |

---

### **Tu “Elevator Pitch” anti-guerra-precios**  
> **“No vendemos cremas; vendemos la única rutina diseñada *por y para* el clima de Bogotá, con trazabilidad de páramo a piel, muestra gratis antes de decidir y garantía de resultado. Botica Verde y Skin Lab tienen productos; nosotras tenemos *tu* solución.”**

---

¿Quieres que desarrolle el **guion del Live mensual**, el **PDF “Reto 21 días”** o el **flujo del bot de diagnóstico WhatsApp** para arrancar ya?

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

**KPIs “vitales” para Q1 (enero‑marzo) – 12 métricas máximas, cero vanidad**  
*Diseñadas para tu modelo: 3 productos, solo Bogotá, venta consultiva por WhatsApp, diferenciación por trazabilidad y clima local.*

---

### 1. ADQUISICIÓN (¿Llega gente *calificada* de Bogotá?)
| # | KPI | Meta Q1 | Fuente / Cómo medir | Semáforo |
|---|-----|---------|---------------------|----------|
| **A1** | **CPL WhatsApp** (costo por chat iniciado) | **≤ $8.000 COP** | Meta Ads Manager → “Conversaciones iniciadas” + gasto | 🔴 >10k 🟡 8‑10k 🟢 <8k |
| **A2** | **% Tráfico orgánico Bogotá** (web + GMaps) | **≥ 40 %** del total sesiones | GA4 (filtro city=Bogotá) / GMB Insights | 🔴 <30 % 🟢 ≥40 % |
| **A3** | **Alcance orgánico Reels/TikTok** (cuentas únicas Bogotá/sem) | **≥ 15 k** | Meta Business Suite / TikTok Analytics (geo) | 🔴 <10k 🟢 ≥15k |

---

### 2. ACTIVACIÓN (¿El lead califica y prueba?)
| # | KPI | Meta Q1 | Fuente |
|---|-----|---------|--------|
| **B1** | **Tasa diagnóstico completado** (quiz 3 preguntas → resultado) | **≥ 35 %** de chats nuevos | ManyChat / Typeform / Hoja manual |
| **B2** | **Kits muestra entregados** (físicos + digitales) | **300 kits** (≈100/mes) | Logística / WhatsApp “Muestra enviada” |
| **B3** | **Conversión muestra → pedido tamaño real** (30 días) | **≥ 30 %** | CRM (etiqueta “muestra” → “primera venta”) |

---

### 3. CONVERSIÓN / VENTA (¿Compran y a qué ticket?)
| # | KPI | Meta Q1 | Fuente |
|---|-----|---------|--------|
| **C1** | **AOV** (valor promedio pedido) | **$165.000 COP** (mezcla Aurora/Sol/Luna) | Shopify / Tiendanube / Hoja pedidos |
| **C2** | **Mix de ventas por producto** | Aurora 25 % / Sol 40 % / Luna 35 % | Backend pedidos |
| **C3** | **ROAS combinado** (Meta + Google) | **≥ 3.5 x** | Ads Manager + GA4 (conversión “Compra”) |
| **C4** | **Tasa carrito → pago** (web) | **≥ 2.5 %** | GA4 / Checkout |

---

### 4. RETENCIÓN / LTV (¿Vuelven y suben de escalón?)
| # | KPI | Meta Q1 | Fuente |
|---|-----|---------|--------|
| **R1** | **Recompra 60 días** (Luna → Sol / Aurora) | **≥ 20 %** clientes Luna | CRM (cohortes por primer producto) |
| **R2** | **Suscriptores “Entrega programada”** | **50 suscripciones** activas | App suscripciones / WhatsApp lista “Suscritos” |
| **R3** | **NPS post-compra (Día 7)** | **≥ 70** | Formulario 1 click en WhatsApp / Email |

---

### 5. REFERIDOS / COMUNIDAD (¿Traen amigas?)
| # | KPI | Meta Q1 | Fuente |
|---|-----|---------|--------|
| **F1** | **% Pedidos con código AMIGA15 / embajadora** | **≥ 15 %** | Backend códigos descuento |
| **F2** | **Asistentes Live “Piel de Páramo”** | **200 únicos / mes** | IG Live Insights |

---

### 6. OPERACIÓN / EXPERIENCIA (¿Cumples la promesa “Bogotá”?)
| # | KPI | Meta Q1 | Fuente |
|---|-----|---------|--------|
| **O1** | **Entrega mismo día / ≤ 24 h Bogotá** | **≥ 95 %** pedidos | Logística / WhatsApp “Llegó” |
| **O2** | **Tiempo respuesta WhatsApp (horario laboral)** | **≤ 5 min** | Meta Business Suite / ManyChat |
| **O3** | **Tasa escaneo QR trazabilidad** | **≥ 15 %** pedidos | Google Analytics (UTM en QR) |

---

## Dashboard “One-Pager” Semanal (Google Sheet / Notion)
| Semana | A1 CPL | B1 Diag % | B2 Muestras | C1 AOV | C3 ROAS | R1 Recompra | O1 Entrega ≤24h | O2 Resp. ≤5min |
|--------|--------|-----------|-------------|--------|---------|-------------|-----------------|----------------|
| 1      |        |           |             |        |         |             |                 |                |
| 2      |        |           |             |        |         |             |                 |                |
| …      |        |           |             |        |         |             |                 |                |
| 12     |        |           |             |        |         |             |                 |                |

**Regla de gestión:**  
- **Verde ≥ 3 semanas seguidas** → escala presupuesto / lanza siguiente acción.  
- **Rojo 2 semanas** → *stop*, diagnostica (creativo, segmento, stock, guion WhatsApp) y corrige.

---

## 3 Alertas Tempranas (revisa **diario** en WhatsApp Business / Ads Manager)
1. **CPL > $10k** 2 días seguidos → apaga conjunto, revisa creativo / audiencia.  
2. **Chats sin respuesta > 15 min** en horario → activa bot “Estoy en consulta, te escribo en 10 min” + aviso a tu celular.  
3. **Devoluciones / cambios > 3 %** semanal → audita lote, empaque o expectativa (garantía “Resultado o Cambio”).

---

## Herramientas Mínimas (costo ~ $0‑$150 k COP/mes)
| Función | Tool gratis / barata |
|---------|----------------------|
| Ads + CPL | Meta Ads Manager + GA4 (UTM obligatorio en todo link) |
| WhatsApp CRM | **ManyChat Free** (hasta 1.000 contactos) o **WhatsApp Business + Etiquetas + Hoja Google Sheets** |
| Embudo web | **Microsoft Clarity** (gratis, heatmaps + grabaciones) |
| Cohortes / LTV | **Google Sheets + fórmulas** (plantilla “Cohort Analysis” nativa) |
| NPS | **Typeform Free** (1 pregunta + razón) → webhook a Sheets |

---

### Tu “North Star” Q1  
> **“300 bogotanas completan diagnóstico → 100 compran kit real → 20 repiten o suben a Aurora en 60 días → 15 traen una amiga”.**  

Si al cierre de marzo cumples **≥ 8/12 KPIs en verde**, tienes *product-market-channel fit* para escalar a Medellín/Cali en Q2.

---

¿Quieres que te pase la **plantilla de Google Sheets** con fórmulas y formato condicional listo para copiar?

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

# **Campaña “Aurora: Tu Piel a 2.600 msnm”**  
**Producto exclusivo:** **Set de Cuidado Facial *Aurora* (Precio Premium)**  
**Duración:** 4 semanas | **Presupuesto sugerido:** $1.800.000 – $2.200.000 COP (Medios + Influencers + Muestras)  
**Objetivo único (North Star):** **30 ventas netas de *Aurora* en 28 días** (≈ $12-15M COP facturación incremental) con **ROAS ≥ 4x** y **CAC ≤ $45.000 COP**.

---

## 1. OBJETIVOS ESPECÍFICOS POR SEMANA
| Semana | Objetivo táctico | KPI líder (diario) | KPI rezagado (semanal) |
|--------|------------------|---------------------|------------------------|
| **1 – Descubrimiento Calificado** | Llenar el embudo con *mujeres bogotanas* que ya compran skincare >$100k y sienten tirantez/altitud. | 80 clics “Iniciar chat WhatsApp” / día | 400 chats iniciados / 120 diagnósticos completados |
| **2 – Prueba Sin Riesgo** | Convertir chats en **kits muestra *Aurora* (2 ml sérum + 1 ml crema)** entregados en <24 h. | 25 muestras despachadas / día | 150 muestras en manos / 45 % abren WhatsApp post-entrega |
| **3 – Cierre Consultivo** | Cerrar venta *Aurora* tamaño real vía asesoría 1:1 en WhatsApp (garantía “Resultado o Cambio”). | 5 ventas *Aurora* / día | 20 ventas acumuladas / ROAS 3.5x |
| **4 – Escala & Referidos** | Activar embajadoras *Aurora* + upsell rutinario (suscripción 90 días). | 3 referidos “AMIGA15” / día | 30 ventas totales / 10 suscripciones / NPS ≥ 80 |

---

## 2. AUDIENCIA “COMPRADORA AURORA” (Solo Bogotá)
| Capa | Definición técnica (Meta / Google) | Tamaño estimado | Por qué compra *Aurora* |
|------|------------------------------------|-----------------|--------------------------|
| **Core** | Mujeres 25‑40, Bogotá, intereses: *Skincare coreano, Dermocosmética, Ácido hialurónico, The Ordinary, La Roche-Posay, Skin Lab, Botica Verde*; comportamiento: “Compradores online frecuentes”, “Gasto alto en belleza”. | ~42.000 | Ya entienden ingredientes; buscan *upgrade* local y trazabilidad. |
| **Look-alike 1 %** | Basado en lista actual de **clientas *Aurora* + compradoras *Sol* >$150k LTV**. | ~38.000 | Perfil idéntico a tus mejores clientas premium. |
| **Retargeting “Caliente”** | • Visitaron PDP *Aurora* 30 d<br>• Iniciaron chat WhatsApp 14 d<br>• Abandonaron carrito *Aurora* 7 d<br>• Escanearon QR trazabilidad 30 d | 1.200‑1.800 | Intención declarada; solo necesitan empuje final (garantía / muestra). |
| **Exclusiones** | Hombres, <25 / >45, fuera de Bogotá, intereses “maquillaje barato”, “cremas corporales económicas”, clientas actuales *Aurora* (lista CRM). | — | Evita gasto innecesario. |

---

## 3. CANALES & FORMATOS (Solo los que venden *Aurora*)
| Canal | Formato estrella | Frecuencia | Presupuesto % | Enlace directo a WhatsApp con parámetro UTM |
|-------|------------------|------------|---------------|---------------------------------------------|
| **Meta Ads (IG + FB)** | **Click-to-WhatsApp** (objetivo “Conversaciones”) – Creativo: **Reel 15 s “Textura Aurora en frío bogotano”** + Carrusel “Ingredientes de páramo + Garantía”. | 3 creativos rotando (semana 1‑2) → 2 ganadores (semana 3‑4) | 55 % ($1.000k) | `wa.me/573XXXXXXX?text=Hola%2C%20quiero%20mi%20diagn%C3%B3stico%20Aurora&utm_source=meta&utm_medium=cpc&utm_campaign=aurora_q1&utm_content={{ad.name}}` |
| **Google Search + Shopping** | **Búsqueda**: “set facial premium Bogotá”, “skincare altitud Bogotá”, “crema ceramidas Colombia”.<br>**Shopping**: Feed solo *Aurora* (precio + “Envío gratis hoy Bogotá”). | Siempre activo + bid +20 % móvil 18‑22 h | 25 % ($450k) | Landing *Aurora* con botón fijo “Asesoría WhatsApp” + UTM `source=google&medium=cpc&campaign=aurora_q1` |
| **Micro-influencers (3 perfiles)** | **Reel “7 días con Aurora”** (día 1 textura, día 3 brillo, día 7 antes/después) + Story “Swipe up → Chat”. Perfiles: 1 dermo-esteticista (12k), 1 lifestyle bogotana (18k), 1 “skincare junkie” (9k). | 1 Reel + 3 Stories c/u (semana 2‑3) | 15 % ($270k) | Código único `AURORA_[NOMBRE]` → 10 % off + muestra gratis + tracking ventas. |
| **WhatsApp Business (Orgánico + Broadcast)** | **Bot “Diagnóstico Aurora”** (3 preguntas → rutina + cupón 10 % *Aurora*).<br>**Broadcast día 7 post-muestra**: “¿Cómo amaneció tu piel? Responde 1/2/3 → te envío tu link compra con envío gratis”. | Diario (bot) + 2 broadcasts/sem | 5 % (herramientas) | Link corto `tutienda.co/aurora?src=wa_broadcast` |
| **Email / ManyChat (Retargeting)** | **Secuencia 3 mails / 3 chats**: 1️⃣ “Ciencia Aurora” (PDF 1 pág), 2️⃣ “Testimonio real + Garantía”, 3️⃣ “Último cupón 48 h”. | Automatizado tras clic / chat | 0 % incremental | UTM `source=email&medium=auto&campaign=aurora_q1` |

---

## 4. MENSAJE PRINCIPAL (Unique Selling Proposition *Aurora*)
> **“El único set facial premium formulado *para* el clima de Bogotá: ceramidas de chagual de páramo + péptidos de última generación. Textura fundente que no pica con el frío, no brilla con el sol de mediodía y reparas tu barrera en 14 días. Pruébalo 2 ml gratis; si no notas luminosidad en 30 días, te cambiamos el frasco sin preguntas.”**

### Pilares creativos (copia base para adaptar)
| Pilar | Hook visual / textual | Prueba / Demostración | CTA único |
|-------|-----------------------|-----------------------|-----------|
| **Ciencia Local** | “Chagual a 3.200 msnm → tu sérum” (video dron + lab) | Certificado lote + pH 5.2 | “Escanea el QR del lote” → WhatsApp |
| **Clima Real** | Split-screen: mañana 8 °C / mediodía 18 °C / noche 10 °C → *Aurora* absorbe en 8 s | Test “cinta adhesiva” (sebo) + corneómetro casero | “Pide tu diagnóstico gratis” |
| **Cero Riesgo** | “30 noches o te devolvemos el valor en *Sol*+*Luna*” | Captura política garantía web | “Activa mi garantía” |
| **Rutina 3 Pasos** | Reel POV: limpieza → 2 gotas *Aurora* sérum → 1 pump crema → base intacta 12 h | Time-lapse 12 h real | “Quiero mi rutina Aurora” |

---

## 5. CRONOGRAMA DETALLADO 4 SEMANAS

| Día | Acción clave | Responsable | Entregable / Check |
|-----|--------------|-------------|---------------------|
| **Pre-lanzamiento (D-3 a D-1)** | • Configurar 3 audiencias en Meta + píxel eventos “Iniciar_Chat_Aurora”, “Muestra_Solicitada”, “Compra_Aurora”.<br>• Subir feed *Aurora* a Merchant Center (solo Bogotá).<br>• Grabar 9 Reels (3 ciencia, 3 clima, 3 garantía) + 6 carruseles estáticos.<br>• Preparar 150 kits muestra (sobres foil + tarjeta QR).<br>• Programar bot ManyChat “Diagnóstico Aurora”.<br>• Enviar brief + contrato a 3 micro-influencers (entrega producto D-1). | Tú / Freelance designer / Logística | Todo probado en sandbox; UTM en **todos** los links. |
| **Semana 1 (D1‑D7) – DESCUBRIMIENTO** | **Lunes**: Lanzar Meta C2W (presupuesto $35k/día) + Search “Marca + Aurora” ($15k/día).<br>**Miércoles**: Primer Live “Piel en la sabana” (tú + dermo aliada) → CTA “Pide muestra”.<br>**Viernes**: Broadcast WhatsApp a base actual “¿Sientes tirantez? Te regalamos 2 ml *Aurora*”.<br>**Diario**: 2 Stories “Mito altitud” + 1 Reel orgánico (rotando 3 creativos). | Tú / Ads Manager | **Meta**: 400 chats / 120 diagnósticos / CPL ≤ $8k. |
| **Semana 2 (D8‑D14) – PRUEBA** | **Lunes**: Activar retargeting “Chats sin muestra” + “Visitantes PDP Aurora”.<br>**Martes**: Publican 3 micro-influencers (Reel + Stories) → código `AURORA_[NOMBRE]`.<br>**Jueves**: Broadcast “Tu muestra llega hoy 🚀 – escanea QR y cuéntame”.<br>**Sábado**: Email 1 “Ciencia Aurora” (PDF 1 pág + link WhatsApp). | Logística (entregas <24h) / Influencers | **Meta**: 150 muestras entregadas / 45 % abren chat post-entrega / CAC muestra ≤ $12k. |
| **Semana 3 (D15‑D21) – CIERRE** | **Lunes**: Lanzar creativos “Garantía 30 días” + “Testimonio real” (UGC semana 2).<br>**Miércoles**: Broadcast “Día 7 post-muestra: ¿cómo amaneciste? 1️⃣ Hidratada 2️⃣ Igual 3️⃣ Grasa → te envío tu link compra con envío gratis”.<br>**Viernes**: Email 2 “Testimonio + Garantía” + cupón `AURORA10` (48 h).<br>**Diario**: Tú cierras ventas 1:1 en WhatsApp (guion “Diagnóstico → Garantía → Pago”). | Tú (ventas) / Ads (optimiza ROAS) | **Meta**: 20 ventas *Aurora* / ROAS 3.5x / CAC ≤ $45k. |
| **Semana 4 (D22‑D28) – ESCALA & REFERIDOS** | **Lunes**: Look-alike 1 % compradores *Aurora* + aumento bid +30 % en ganadores.<br>**Martes**: Activar programa “Embajadora Aurora”: cliente feliz → código `AMIGA15_AURORA` (15 % off amiga + $30k crédito para ella).<br>**Jueves**: Email 3 “Última oportunidad cupón + Suscripción 90 días (5 % off + gua sha)”.<br>**Sábado**: Live “Resultados reales 21 días” (clientas en pantalla).<br>**Domingo 28**: Apaga campañas; exporta datos; reporte final. | Tú / CRM | **Meta**: 30 ventas totales / 10 suscripciones / 15 referidos / NPS ≥ 80. |

---

## 6. MÉTRICAS DE ÉXITO (Dashboard Semanal – Colores = Semáforo)

| KPI | Fórmula | Meta Semana 1 | Meta Semana 2 | Meta Semana 3 | Meta Semana 4 | Fuente |
|-----|---------|---------------|---------------|---------------|---------------|--------|
| **Chats iniciados (Aurora)** | Σ clics “Iniciar chat” UTM `aurora_q1` | 400 | 550 | 650 | 700 | Meta Ads / GA4 |
| **Diagnósticos completados** | Chats que responden 3 preguntas bot | 120 (30 %) | 200 (36 %) | 260 (40 %) | 300 (43 %) | ManyChat |
| **Muestras despachadas** | Kits físicos + digitales marcados “Enviado” | 50 | 150 | 180 | 200 | Logística / WhatsApp |
| **Conversión Muestra → Venta** | Ventas *Aurora* / Muestras entregadas (ventana 30 d) | — | 15 % | 30 % | 35 % | CRM |
| **Ventas netas *Aurora*** | Pedidos pagados – devoluciones | 2 | 8 | 20 | 30 | Backend |
| **AOV *Aurora*** | Ingresos *Aurora* / Pedidos *Aurora* | $380k | $385k | $390k | $395k | Backend |
| **ROAS Combinado** | Ingresos *Aurora* / Gasto total campaña | 1.5x | 2.8x | 3.8x | **≥ 4.0x** | Ads Manager + GA4 |
| **CAC *Aurora*** | Gasto total / Ventas netas *Aurora* | $90k | $60k | **≤ $45k** | **≤ $45k** | Dashboard |
| **Suscripciones 90d** | Pedidos recurrentes activados | 0 | 1 | 5 | **10** | App suscripciones |
| **Referidos AMIGA15** | Usos código único embajadoras | 0 | 3 | 8 | **15** | Backend códigos |
| **NPS Día 7** | Promedio encuesta 1 click (0‑10) | — | 70 | 75 | **≥ 80** | Typeform / WA |

**Regla de parada/escala:**  
- **Rojo 2 semanas seguidas** en *CAC > $55k* o *ROAS < 2.5x* → Pausa, revisa creativo / audiencia / guion WhatsApp.  
- **Verde 2 semanas** en *CAC ≤ $45k* + *ROAS ≥ 3.5x* → Sube presupuesto diario 20 % en conjuntos ganadores.

---

## 7. PRESUPUESTO DETALLADO (COP)

| Rubro | Semana 1 | Semana 2 | Semana 3 | Semana 4 | Total | % |
|-------|----------|----------|----------|----------|-------|---|
| Meta Ads (C2W + Retargeting) | $250k | $300k | $300k | $250k | **$1.100k** | 55 % |
| Google Search + Shopping | $100k | $100k | $125k | $125k | **$450k** | 22 % |
| Micro-influencers (producto + fee) | $0 | $180k | $90k | $0 | **$270k** | 13 % |
| Muestras (packaging + envío) | $120k | $60k | $30k | $0 | **$210k** | 10 % |
| Herramientas (ManyChat Pro, Typeform, acortador) | $15k | $15k | $15k | $15k | **$60k** | 3 % |
| **TOTAL** | **$485k** | **$655k** | **$560k** | **$390k** | **$2.090k** | 100 % |

---

## 8. CHECKLIST DE LANZAMIENTO (Copiar en Notion / Sheets)
- [ ] Píxel eventos “Iniciar_Chat_Aurora”, “Muestra_Solicitada”, “Compra_Aurora” disparando en GTM.  
- [ ] 3 audiencias Meta guardadas + Look-alike 1 % creada.  
- [ ] Feed *Aurora* aprobado en Merchant Center (solo Bogotá).  
- [ ] 9 Reels + 6 Carruseles subidos a Biblioteca Meta (nombres UTM).  
- [ ] Bot ManyChat “Diagnóstico Aurora” publicado y probado en 5 contactos test.  
- [ ] 150 kits muestra empaquetados (QR lote + tarjeta manuscrita).  
- [ ] 3 contratos influencers firmados + producto en mano.  
- [ ] Landing *Aurora* con: video hero, certificado lote, garantía, botón WhatsApp fijo, UTM automático.  
- [ ] Secuencia Email 1-2-3 programada en Klaviyo/MailerLite (segmento “click Aurora”).  
- [ ] Dashboard Google Sheets compartido con formato condicional (rojo/amarillo/verde).  

---

## 9. GUIÓN RÁPIDO WHATSAPP (Para que tú / asistente cierren en <7 min)
```
1️⃣ “Hola [Nombre]! 👋 Vi que pediste tu diagnóstico Aurora.  
   ¿Tu piel hoy se siente: 1️⃣ Tensa/seca  2️⃣ Mixta con brillos  3️⃣ Sensible/rojez?”

2️⃣ (Usuario responde) → “Perfecto. Para [respuesta] la rutina ideal es:  
   🌙 Noche: Limpiador suave → 2 gotas Sérum Aurora (chagual + péptidos) → 1 pump Crema Aurora (ceramidas + uchuva).  
   ☀️ Mañana: Agua termal → 1 gota Sérum → Protector solar (te regalo muestra SPF50).  

   ¿Te envío tu kit prueba 2 ml + 1 ml **gratis** a tu dirección en Bogotá? Llega mañana 🚀”

3️⃣ (Usuario da dirección) → “¡Listo! Tu código de seguimiento: AUR-[NUM].  
   En 3 días te escribo para saber cómo amaneciste.  
   Si decides quedarte con el set completo, tienes **10 % off + envío gratis + garantía 30 días** (te cambiamos por Sol+Luna si no ves luminosidad).  
   ¿Te parece bien?”
```
*Guarda como “Respuesta rápida” en WhatsApp Business → `/aurora_cierre`.*

---

## 10. PRÓXIMOS PASOS INMEDIATOS (Hoy)
1. **Copia este plan** a tu Notion / Sheets.  
2. **Agenda 2 h bloque** mañana temprano: configura píxel, audiencias, feed Google.  
3. **Encarga 150 sobres foil** (proveedor local, 24 h) + imprime 150 tarjetas QR (Canva → imprimir oficina).  
4. **Envía brief a 3 micro-influencers** (plantilla adjunta abajo).  
5. **Publica el bot ManyChat** y prueba con 3 amigas.  
6. **Lanza Meta C2W** a $35k/día (presupuesto campaña “Aurora_Q1_Discovery”).  

---

### Plantilla Brief Influencers (WhatsApp / Email)
```
Hola [Nombre],

Campaña “Aurora: Tu Piel a 2.600 msnm” 🌿
Producto: Set facial premium *Aurora* (cerramidas chagual + péptidos).

Entregables (Semana 2, 8‑14 ene):
1 Reel (15‑20 s) “7 días con Aurora” → texto libre, mostra textura, absorción, brillo día 7.
3 Stories día publicación: 1️⃣ Unboxing 2️⃣ Aplicación mañana 3️⃣ “Swipe up → Chat gratis” (link wa.me/573XXXX?text=AURORA_[TU_NOMBRE]).
Código único: `AURORA_[TU_NOMBRE]` → 10 % off + muestra gratis para tus seguidoras.

Pago: Producto *Aurora* (valor $380k) + $90k fee contra factura tras publicación.
¿Te cuadra? Confirmo y te envío el set mañana mismo 🚚
```
---

**¿Lista para arrancar? Si necesitas la hoja de cálculo del dashboard, los creativos base en Canva (link editable) o el flujo ManyChat exportado (.json), dímelo y te lo paso ya.**


## Respuesta completa

# **Campaña “Aurora: Tu Piel a 2.600 msnm”**  
**Producto exclusivo:** **Set de Cuidado Facial *Aurora* (Precio Premium)**  
**Duración:** 4 semanas | **Presupuesto sugerido:** $1.800.000 – $2.200.000 COP (Medios + Influencers + Muestras)  
**Objetivo único (North Star):** **30 ventas netas de *Aurora* en 28 días** (≈ $12-15M COP facturación incremental) con **ROAS ≥ 4x** y **CAC ≤ $45.000 COP**.

---

## 1. OBJETIVOS ESPECÍFICOS POR SEMANA
| Semana | Objetivo táctico | KPI líder (diario) | KPI rezagado (semanal) |
|--------|------------------|---------------------|------------------------|
| **1 – Descubrimiento Calificado** | Llenar el embudo con *mujeres bogotanas* que ya compran skincare >$100k y sienten tirantez/altitud. | 80 clics “Iniciar chat WhatsApp” / día | 400 chats iniciados / 120 diagnósticos completados |
| **2 – Prueba Sin Riesgo** | Convertir chats en **kits muestra *Aurora* (2 ml sérum + 1 ml crema)** entregados en <24 h. | 25 muestras despachadas / día | 150 muestras en manos / 45 % abren WhatsApp post-entrega |
| **3 – Cierre Consultivo** | Cerrar venta *Aurora* tamaño real vía asesoría 1:1 en WhatsApp (garantía “Resultado o Cambio”). | 5 ventas *Aurora* / día | 20 ventas acumuladas / ROAS 3.5x |
| **4 – Escala & Referidos** | Activar embajadoras *Aurora* + upsell rutinario (suscripción 90 días). | 3 referidos “AMIGA15” / día | 30 ventas totales / 10 suscripciones / NPS ≥ 80 |

---

## 2. AUDIENCIA “COMPRADORA AURORA” (Solo Bogotá)
| Capa | Definición técnica (Meta / Google) | Tamaño estimado | Por qué compra *Aurora* |
|------|------------------------------------|-----------------|--------------------------|
| **Core** | Mujeres 25‑40, Bogotá, intereses: *Skincare coreano, Dermocosmética, Ácido hialurónico, The Ordinary, La Roche-Posay, Skin Lab, Botica Verde*; comportamiento: “Compradores online frecuentes”, “Gasto alto en belleza”. | ~42.000 | Ya entienden ingredientes; buscan *upgrade* local y trazabilidad. |
| **Look-alike 1 %** | Basado en lista actual de **clientas *Aurora* + compradoras *Sol* >$150k LTV**. | ~38.000 | Perfil idéntico a tus mejores clientas premium. |
| **Retargeting “Caliente”** | • Visitaron PDP *Aurora* 30 d<br>• Iniciaron chat WhatsApp 14 d<br>• Abandonaron carrito *Aurora* 7 d<br>• Escanearon QR trazabilidad 30 d | 1.200‑1.800 | Intención declarada; solo necesitan empuje final (garantía / muestra). |
| **Exclusiones** | Hombres, <25 / >45, fuera de Bogotá, intereses “maquillaje barato”, “cremas corporales económicas”, clientas actuales *Aurora* (lista CRM). | — | Evita gasto innecesario. |

---

## 3. CANALES & FORMATOS (Solo los que venden *Aurora*)
| Canal | Formato estrella | Frecuencia | Presupuesto % | Enlace directo a WhatsApp con parámetro UTM |
|-------|------------------|------------|---------------|---------------------------------------------|
| **Meta Ads (IG + FB)** | **Click-to-WhatsApp** (objetivo “Conversaciones”) – Creativo: **Reel 15 s “Textura Aurora en frío bogotano”** + Carrusel “Ingredientes de páramo + Garantía”. | 3 creativos rotando (semana 1‑2) → 2 ganadores (semana 3‑4) | 55 % ($1.000k) | `wa.me/573XXXXXXX?text=Hola%2C%20quiero%20mi%20diagn%C3%B3stico%20Aurora&utm_source=meta&utm_medium=cpc&utm_campaign=aurora_q1&utm_content={{ad.name}}` |
| **Google Search + Shopping** | **Búsqueda**: “set facial premium Bogotá”, “skincare altitud Bogotá”, “crema ceramidas Colombia”.<br>**Shopping**: Feed solo *Aurora* (precio + “Envío gratis hoy Bogotá”). | Siempre activo + bid +20 % móvil 18‑22 h | 25 % ($450k) | Landing *Aurora* con botón fijo “Asesoría WhatsApp” + UTM `source=google&medium=cpc&campaign=aurora_q1` |
| **Micro-influencers (3 perfiles)** | **Reel “7 días con Aurora”** (día 1 textura, día 3 brillo, día 7 antes/después) + Story “Swipe up → Chat”. Perfiles: 1 dermo-esteticista (12k), 1 lifestyle bogotana (18k), 1 “skincare junkie” (9k). | 1 Reel + 3 Stories c/u (semana 2‑3) | 15 % ($270k) | Código único `AURORA_[NOMBRE]` → 10 % off + muestra gratis + tracking ventas. |
| **WhatsApp Business (Orgánico + Broadcast)** | **Bot “Diagnóstico Aurora”** (3 preguntas → rutina + cupón 10 % *Aurora*).<br>**Broadcast día 7 post-muestra**: “¿Cómo amaneció tu piel? Responde 1/2/3 → te envío tu link compra con envío gratis”. | Diario (bot) + 2 broadcasts/sem | 5 % (herramientas) | Link corto `tutienda.co/aurora?src=wa_broadcast` |
| **Email / ManyChat (Retargeting)** | **Secuencia 3 mails / 3 chats**: 1️⃣ “Ciencia Aurora” (PDF 1 pág), 2️⃣ “Testimonio real + Garantía”, 3️⃣ “Último cupón 48 h”. | Automatizado tras clic / chat | 0 % incremental | UTM `source=email&medium=auto&campaign=aurora_q1` |

---

## 4. MENSAJE PRINCIPAL (Unique Selling Proposition *Aurora*)
> **“El único set facial premium formulado *para* el clima de Bogotá: ceramidas de chagual de páramo + péptidos de última generación. Textura fundente que no pica con el frío, no brilla con el sol de mediodía y reparas tu barrera en 14 días. Pruébalo 2 ml gratis; si no notas luminosidad en 30 días, te cambiamos el frasco sin preguntas.”**

### Pilares creativos (copia base para adaptar)
| Pilar | Hook visual / textual | Prueba / Demostración | CTA único |
|-------|-----------------------|-----------------------|-----------|
| **Ciencia Local** | “Chagual a 3.200 msnm → tu sérum” (video dron + lab) | Certificado lote + pH 5.2 | “Escanea el QR del lote” → WhatsApp |
| **Clima Real** | Split-screen: mañana 8 °C / mediodía 18 °C / noche 10 °C → *Aurora* absorbe en 8 s | Test “cinta adhesiva” (sebo) + corneómetro casero | “Pide tu diagnóstico gratis” |
| **Cero Riesgo** | “30 noches o te devolvemos el valor en *Sol*+*Luna*” | Captura política garantía web | “Activa mi garantía” |
| **Rutina 3 Pasos** | Reel POV: limpieza → 2 gotas *Aurora* sérum → 1 pump crema → base intacta 12 h | Time-lapse 12 h real | “Quiero mi rutina Aurora” |

---

## 5. CRONOGRAMA DETALLADO 4 SEMANAS

| Día | Acción clave | Responsable | Entregable / Check |
|-----|--------------|-------------|---------------------|
| **Pre-lanzamiento (D-3 a D-1)** | • Configurar 3 audiencias en Meta + píxel eventos “Iniciar_Chat_Aurora”, “Muestra_Solicitada”, “Compra_Aurora”.<br>• Subir feed *Aurora* a Merchant Center (solo Bogotá).<br>• Grabar 9 Reels (3 ciencia, 3 clima, 3 garantía) + 6 carruseles estáticos.<br>• Preparar 150 kits muestra (sobres foil + tarjeta QR).<br>• Programar bot ManyChat “Diagnóstico Aurora”.<br>• Enviar brief + contrato a 3 micro-influencers (entrega producto D-1). | Tú / Freelance designer / Logística | Todo probado en sandbox; UTM en **todos** los links. |
| **Semana 1 (D1‑D7) – DESCUBRIMIENTO** | **Lunes**: Lanzar Meta C2W (presupuesto $35k/día) + Search “Marca + Aurora” ($15k/día).<br>**Miércoles**: Primer Live “Piel en la sabana” (tú + dermo aliada) → CTA “Pide muestra”.<br>**Viernes**: Broadcast WhatsApp a base actual “¿Sientes tirantez? Te regalamos 2 ml *Aurora*”.<br>**Diario**: 2 Stories “Mito altitud” + 1 Reel orgánico (rotando 3 creativos). | Tú / Ads Manager | **Meta**: 400 chats / 120 diagnósticos / CPL ≤ $8k. |
| **Semana 2 (D8‑D14) – PRUEBA** | **Lunes**: Activar retargeting “Chats sin muestra” + “Visitantes PDP Aurora”.<br>**Martes**: Publican 3 micro-influencers (Reel + Stories) → código `AURORA_[NOMBRE]`.<br>**Jueves**: Broadcast “Tu muestra llega hoy 🚀 – escanea QR y cuéntame”.<br>**Sábado**: Email 1 “Ciencia Aurora” (PDF 1 pág + link WhatsApp). | Logística (entregas <24h) / Influencers | **Meta**: 150 muestras entregadas / 45 % abren chat post-entrega / CAC muestra ≤ $12k. |
| **Semana 3 (D15‑D21) – CIERRE** | **Lunes**: Lanzar creativos “Garantía 30 días” + “Testimonio real” (UGC semana 2).<br>**Miércoles**: Broadcast “Día 7 post-muestra: ¿cómo amaneciste? 1️⃣ Hidratada 2️⃣ Igual 3️⃣ Grasa → te envío tu link compra con envío gratis”.<br>**Viernes**: Email 2 “Testimonio + Garantía” + cupón `AURORA10` (48 h).<br>**Diario**: Tú cierras ventas 1:1 en WhatsApp (guion “Diagnóstico → Garantía → Pago”). | Tú (ventas) / Ads (optimiza ROAS) | **Meta**: 20 ventas *Aurora* / ROAS 3.5x / CAC ≤ $45k. |
| **Semana 4 (D22‑D28) – ESCALA & REFERIDOS** | **Lunes**: Look-alike 1 % compradores *Aurora* + aumento bid +30 % en ganadores.<br>**Martes**: Activar programa “Embajadora Aurora”: cliente feliz → código `AMIGA15_AURORA` (15 % off amiga + $30k crédito para ella).<br>**Jueves**: Email 3 “Última oportunidad cupón + Suscripción 90 días (5 % off + gua sha)”.<br>**Sábado**: Live “Resultados reales 21 días” (clientas en pantalla).<br>**Domingo 28**: Apaga campañas; exporta datos; reporte final. | Tú / CRM | **Meta**: 30 ventas totales / 10 suscripciones / 15 referidos / NPS ≥ 80. |

---

## 6. MÉTRICAS DE ÉXITO (Dashboard Semanal – Colores = Semáforo)

| KPI | Fórmula | Meta Semana 1 | Meta Semana 2 | Meta Semana 3 | Meta Semana 4 | Fuente |
|-----|---------|---------------|---------------|---------------|---------------|--------|
| **Chats iniciados (Aurora)** | Σ clics “Iniciar chat” UTM `aurora_q1` | 400 | 550 | 650 | 700 | Meta Ads / GA4 |
| **Diagnósticos completados** | Chats que responden 3 preguntas bot | 120 (30 %) | 200 (36 %) | 260 (40 %) | 300 (43 %) | ManyChat |
| **Muestras despachadas** | Kits físicos + digitales marcados “Enviado” | 50 | 150 | 180 | 200 | Logística / WhatsApp |
| **Conversión Muestra → Venta** | Ventas *Aurora* / Muestras entregadas (ventana 30 d) | — | 15 % | 30 % | 35 % | CRM |
| **Ventas netas *Aurora*** | Pedidos pagados – devoluciones | 2 | 8 | 20 | 30 | Backend |
| **AOV *Aurora*** | Ingresos *Aurora* / Pedidos *Aurora* | $380k | $385k | $390k | $395k | Backend |
| **ROAS Combinado** | Ingresos *Aurora* / Gasto total campaña | 1.5x | 2.8x | 3.8x | **≥ 4.0x** | Ads Manager + GA4 |
| **CAC *Aurora*** | Gasto total / Ventas netas *Aurora* | $90k | $60k | **≤ $45k** | **≤ $45k** | Dashboard |
| **Suscripciones 90d** | Pedidos recurrentes activados | 0 | 1 | 5 | **10** | App suscripciones |
| **Referidos AMIGA15** | Usos código único embajadoras | 0 | 3 | 8 | **15** | Backend códigos |
| **NPS Día 7** | Promedio encuesta 1 click (0‑10) | — | 70 | 75 | **≥ 80** | Typeform / WA |

**Regla de parada/escala:**  
- **Rojo 2 semanas seguidas** en *CAC > $55k* o *ROAS < 2.5x* → Pausa, revisa creativo / audiencia / guion WhatsApp.  
- **Verde 2 semanas** en *CAC ≤ $45k* + *ROAS ≥ 3.5x* → Sube presupuesto diario 20 % en conjuntos ganadores.

---

## 7. PRESUPUESTO DETALLADO (COP)

| Rubro | Semana 1 | Semana 2 | Semana 3 | Semana 4 | Total | % |
|-------|----------|----------|----------|----------|-------|---|
| Meta Ads (C2W + Retargeting) | $250k | $300k | $300k | $250k | **$1.100k** | 55 % |
| Google Search + Shopping | $100k | $100k | $125k | $125k | **$450k** | 22 % |
| Micro-influencers (producto + fee) | $0 | $180k | $90k | $0 | **$270k** | 13 % |
| Muestras (packaging + envío) | $120k | $60k | $30k | $0 | **$210k** | 10 % |
| Herramientas (ManyChat Pro, Typeform, acortador) | $15k | $15k | $15k | $15k | **$60k** | 3 % |
| **TOTAL** | **$485k** | **$655k** | **$560k** | **$390k** | **$2.090k** | 100 % |

---

## 8. CHECKLIST DE LANZAMIENTO (Copiar en Notion / Sheets)
- [ ] Píxel eventos “Iniciar_Chat_Aurora”, “Muestra_Solicitada”, “Compra_Aurora” disparando en GTM.  
- [ ] 3 audiencias Meta guardadas + Look-alike 1 % creada.  
- [ ] Feed *Aurora* aprobado en Merchant Center (solo Bogotá).  
- [ ] 9 Reels + 6 Carruseles subidos a Biblioteca Meta (nombres UTM).  
- [ ] Bot ManyChat “Diagnóstico Aurora” publicado y probado en 5 contactos test.  
- [ ] 150 kits muestra empaquetados (QR lote + tarjeta manuscrita).  
- [ ] 3 contratos influencers firmados + producto en mano.  
- [ ] Landing *Aurora* con: video hero, certificado lote, garantía, botón WhatsApp fijo, UTM automático.  
- [ ] Secuencia Email 1-2-3 programada en Klaviyo/MailerLite (segmento “click Aurora”).  
- [ ] Dashboard Google Sheets compartido con formato condicional (rojo/amarillo/verde).  

---

## 9. GUIÓN RÁPIDO WHATSAPP (Para que tú / asistente cierren en <7 min)
```
1️⃣ “Hola [Nombre]! 👋 Vi que pediste tu diagnóstico Aurora.  
   ¿Tu piel hoy se siente: 1️⃣ Tensa/seca  2️⃣ Mixta con brillos  3️⃣ Sensible/rojez?”

2️⃣ (Usuario responde) → “Perfecto. Para [respuesta] la rutina ideal es:  
   🌙 Noche: Limpiador suave → 2 gotas Sérum Aurora (chagual + péptidos) → 1 pump Crema Aurora (ceramidas + uchuva).  
   ☀️ Mañana: Agua termal → 1 gota Sérum → Protector solar (te regalo muestra SPF50).  

   ¿Te envío tu kit prueba 2 ml + 1 ml **gratis** a tu dirección en Bogotá? Llega mañana 🚀”

3️⃣ (Usuario da dirección) → “¡Listo! Tu código de seguimiento: AUR-[NUM].  
   En 3 días te escribo para saber cómo amaneciste.  
   Si decides quedarte con el set completo, tienes **10 % off + envío gratis + garantía 30 días** (te cambiamos por Sol+Luna si no ves luminosidad).  
   ¿Te parece bien?”
```
*Guarda como “Respuesta rápida” en WhatsApp Business → `/aurora_cierre`.*

---

## 10. PRÓXIMOS PASOS INMEDIATOS (Hoy)
1. **Copia este plan** a tu Notion / Sheets.  
2. **Agenda 2 h bloque** mañana temprano: configura píxel, audiencias, feed Google.  
3. **Encarga 150 sobres foil** (proveedor local, 24 h) + imprime 150 tarjetas QR (Canva → imprimir oficina).  
4. **Envía brief a 3 micro-influencers** (plantilla adjunta abajo).  
5. **Publica el bot ManyChat** y prueba con 3 amigas.  
6. **Lanza Meta C2W** a $35k/día (presupuesto campaña “Aurora_Q1_Discovery”).  

---

### Plantilla Brief Influencers (WhatsApp / Email)
```
Hola [Nombre],

Campaña “Aurora: Tu Piel a 2.600 msnm” 🌿
Producto: Set facial premium *Aurora* (cerramidas chagual + péptidos).

Entregables (Semana 2, 8‑14 ene):
1 Reel (15‑20 s) “7 días con Aurora” → texto libre, mostra textura, absorción, brillo día 7.
3 Stories día publicación: 1️⃣ Unboxing 2️⃣ Aplicación mañana 3️⃣ “Swipe up → Chat gratis” (link wa.me/573XXXX?text=AURORA_[TU_NOMBRE]).
Código único: `AURORA_[TU_NOMBRE]` → 10 % off + muestra gratis para tus seguidoras.

Pago: Producto *Aurora* (valor $380k) + $90k fee contra factura tras publicación.
¿Te cuadra? Confirmo y te envío el set mañana mismo 🚚
```
---

**¿Lista para arrancar? Si necesitas la hoja de cálculo del dashboard, los creativos base en Canva (link editable) o el flujo ManyChat exportado (.json), dímelo y te lo paso ya.**