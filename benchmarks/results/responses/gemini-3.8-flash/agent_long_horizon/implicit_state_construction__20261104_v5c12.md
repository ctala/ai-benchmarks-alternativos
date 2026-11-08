# Gemini 3.8 Flash — agent_long_horizon/implicit_state_construction

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 97.625s | tokens_per_second: 111.9
- input_tokens: 13351 | output_tokens: 9635

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

¡Hola, Camila! Sí, me queda completamente claro. 

Tengo registrados todos los detalles:
* **Mercado actual:** Exclusivamente Bogotá.
* **Catálogo:**
  * **Luna:** Crema corporal (precio de entrada).
  * **Sol:** Kit de maquillaje natural (precio medio).
  * **Aurora:** Set de cuidado facial (precio premium).
* **Competencia directa en Bogotá:** *Botica Verde* y *Skin Lab*.

Estoy listo para ayudarte a planificar tus campañas. ¿En qué objetivo o producto te gustaría que nos enfoquemos primero?

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Ofrecemos a Bogotá una rutina integral de belleza consciente y natural que cuida de ti de pies a cabeza, con alternativas versátiles que van desde el cuidado corporal diario y accesible hasta tratamientos faciales de alta gama. Frente a la oferta local tradicional, combinamos fórmulas limpias, maquillaje sutil y cuidado de la piel premium para resaltar tu luminosidad auténtica con la cercanía y rapidez que solo una marca de tu ciudad te puede dar.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Para tu tienda en Bogotá y el tipo de catálogo que manejas (desde el cuidado accesible hasta el premium), te recomiendo priorizar estos canales, ordenados por impacto:

### 1. Instagram y TikTok (Atracción y Construcción de Marca)
* **Por qué:** La belleza y el cuidado personal son categorías 100% visuales y de demostración. 
* **Estrategia:** 
  * Usa **TikTok y Reels** para mostrar la textura y absorción de *Luna*, tutoriales de "look no-makeup" con *Sol*, y rutinas completas de skincare que justifiquen el valor de *Aurora*.
  * Colabora con microcreadoras de contenido locales en Bogotá para generar confianza y cercanía.

### 2. Meta Ads (Facebook e Instagram Ads - Tráfico y Conversión)
* **Por qué:** Permite una segmentación geográfica hiperlocal exclusiva para Bogotá (e incluso por localidades con mayor poder adquisitivo para empujar *Aurora*).
* **Estrategia:**
  * Campañas de conversión directo al sitio web.
  * Anuncios segmentados por intereses en cosmética limpia, bienestar y seguidores de marcas afines (públicos similares a los de *Botica Verde* y *Skin Lab*).
  * Retargeting: Si alguien ve *Luna* o *Sol*, muéstrales cómo complementarlo con *Aurora*.

### 3. WhatsApp Business (Cierre de Ventas y Fidelización)
* **Por qué:** En el e-commerce colombiano, WhatsApp es el canal definitivo para generar confianza, resolver dudas sobre tipos de piel y cerrar ventas asistidas.
* **Estrategia:**
  * Fundamental para brindar asesoría personalizada a quienes dudan en comprar el set premium (*Aurora*).
  * Automatiza respuestas para temas de envíos locales en Bogotá y métodos de pago populares (Nequi, Daviplata, contra entrega).

### 4. Google Search Ads (Captura de Intención Alta - Secundario)
* **Por qué:** Para capturar a personas en Bogotá que ya están buscando activamente soluciones específicas.
* **Estrategia:** Palabras clave de intención de compra como *"rutina facial natural Bogotá"*, *"maquillaje natural Colombia"* o términos de búsqueda relacionados con la oferta de tu competencia.

**Recomendación de arranque:** Concentra el 80% de tus esfuerzos iniciales en el ecosistema **Instagram + Meta Ads + WhatsApp Business** para generar un ciclo rápido de descubrimiento, prueba y recompra dentro de la ciudad.

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Para un e-commerce que está consolidándose en Bogotá, la clave no es saturar, sino mantener una **consistencia realista** que puedas sostener sin descuidar la operación ni los despachos. 

Aquí tienes un calendario semanal recomendado para tus canales orgánicos principales:

---

### 1. Instagram
Es tu vitrina principal y donde se construye la comunidad.

* **Reels (3 a 4 veces por semana):**
  * Es el formato con mayor alcance para atraer gente nueva en Bogotá.
  * *Ideas:* Textura e hidratación de *Luna* contra el frío/viento bogotano, tutoriales de maquillaje rápido con *Sol*, o explicación de ingredientes y rutina paso a paso de *Aurora*.
* **Carruseles / Posts estáticos (1 a 2 veces por semana):**
  * Ideales para educar, compartir testimonios, guías de uso o comparativas sutiles de beneficios frente a formulaciones convencionales.
* **Stories (Diario / 5 a 6 días a la semana, 3–5 historias al día):**
  * Para venta directa y cercanía humana.
  * Muestra el detrás de cámaras (empacando pedidos hacia Chapinero, Usaquén, etc.), encuestas sobre tipo de piel, recordatorios de stock y enlaces directos a WhatsApp o la web.

---

### 2. TikTok
Tu canal de descubrimiento y viralidad.

* **Videos cortos (3 a 4 veces por semana):**
  * Puedes reciclar los mejores Reels aquí o viceversa.
  * Prioriza contenido espontáneo y en tendencia: "get ready with me" (GRWM) usando el kit *Sol*, rutinas nocturnas con el set *Aurora*, o resolviendo mitos del cuidado corporal con *Luna*.

---

### 3. WhatsApp Business (Estados y Listas de Difusión)
Tu canal de fidelización y venta directa.

* **Estados de WhatsApp (2 a 3 veces por semana):**
  * Comparte fotos de clientes reales recibiendo sus pedidos en Bogotá, tips rápidos o alertas de envíos el mismo día.
* **Mensajes / Listas de difusión (Máximo 2 veces al mes):**
  * Úsalo con moderación para no saturar. Reserva este espacio para ofertas exclusivas, preventas, o recordatorios de reposición (por ejemplo, cuando calcules que se les está terminando su crema *Luna*).

---

### Resumen de rutina semanal recomendada:
* **Lunes, Miércoles, Viernes:** Publicar Reel/TikTok + Stories.
* **Martes, Jueves:** Carrusel educativo en Instagram + Stories.
* **Sábado o Domingo:** Stories de estilo de vida / descanso + Estado de WhatsApp.

**Tip local:** Aprovecha situaciones propias de Bogotá en tus contenidos (el clima frío que reseca la piel, la polución de la ciudad o la necesidad de una rutina express para no perder tiempo en el tráfico) para conectar de inmediato con la realidad de tu audiencia.

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Para el cuidado de la piel (skincare), el contenido más efectivo es aquel que **genera confianza técnica**, **demuestra la experiencia sensorial** y **muestra resultados reales sin filtros**. En este nicho, la audiencia es analítica y busca justificar su inversión (especialmente cuando evalúa productos de gama alta como tu set *Aurora*).

Aquí están los 5 tipos de contenido que mejor convierten:

---

### 1. Macro-tomas y contenido sensorial (ASMR de texturas)
El skincare entra por los ojos y por la sensación de alivio.
* **Qué mostrar:** Primeros planos detallados de la textura (cómo se funde la crema, cómo cae la gota del serum con el gotero, la espuma del limpiador).
* **Por qué funciona:** Muestra la calidad de la formulación y la rápida absorción, algo clave para convencer al cliente de que no dejará sensación pesada o grasosa.

### 2. Rutinas paso a paso y orden de aplicación
El consumidor suele tener dudas sobre cómo combinar productos y qué va primero.
* **Qué mostrar:** 
  * Rutina AM (protección y luminosidad) vs. Rutina PM (reparación y nutrición profunda) usando el paso a paso de *Aurora*.
  * La cantidad exacta de producto a usar (ejemplo: "dos gotas son suficientes", "el tamaño de una arveja").
* **Por qué funciona:** Reduce la fricción de "no sé cómo usarlo" y demuestra cómo un set completo resuelve el cuidado diario en pocos minutos.

### 3. Educación sobre ingredientes y función de la barrera cutánea
Hoy las compradoras leen etiquetas y quieren saber qué se están aplicando.
* **Qué mostrar:** 
  * "Por qué tu piel se deshidrata en Bogotá" (el frío, el viento de la tarde y la altitud afectan la barrera de la piel).
  * Explicar el activo estrella de la fórmula: para qué sirve, por qué es natural y cómo actúa frente a la polución de la ciudad.
* **Por qué funciona:** Posiciona tu marca como una autoridad ética frente a competidores locales (*Botica Verde* o *Skin Lab*), justificando con argumentos el precio premium.

### 4. Prueba social y piel real ("Skin Realness")
El exceso de filtros en redes ha hecho que la gente desconfíe de pieles de porcelana falsas.
* **Qué mostrar:**
  * Piel con poros reales, textura natural y luminosidad saludable.
  * Fotos de evolución de clientas (día 1 vs. día 21 de uso continuo).
  * Capturas de pantalla de mensajes espontáneos de WhatsApp o reseñas en la tienda web ("Llevo 2 semanas y siento la piel súper suave").
* **Por qué funciona:** Disminuye el riesgo percibido antes de pagar.

### 5. Resolución de problemas cotidianos (Storytelling situacional)
Conectar el producto con momentos específicos de la vida diaria bogotana.
* **Qué mostrar:**
  * "Rutina de 3 minutos para no llegar tarde por el trancón".
  * "Cómo recuperar la piel opaca después de un día entero expuesta a la contaminación de la Séptima".
  * Cómo preparar la piel con tu rutina facial antes de aplicar un maquillaje ligero como *Sol*.
* **Por qué funciona:** Hace que el producto se sienta una solución práctica y no un lujo prescindible.

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Para diferenciarte de **Botica Verde** y **Skin Lab** en Bogotá sin sacrificar tus márgenes ni desgastarte en promociones, debes competir en **posicionamiento, experiencia y conveniencia**, no en precio. 

Por sus nombres, tus competidores proyectan dos extremos comunes: *Botica Verde* sugiere un enfoque artesanal/herbal tradicional, mientras que *Skin Lab* apunta a lo clínico/dermatológico frío. 

Tu oportunidad está en adueñarte del **punto de equilibrio perfecto: cosmética consciente, moderna y práctica para la rutina urbana**. Aquí tienes cuatro formas concretas de lograrlo:

---

### 1. El concepto "Skincare híbrido + Maquillaje natural" (La sinergia de tu catálogo)
La mayoría de las marcas de nicho solo hacen cuidado facial o solo maquillaje. Tu gran ventaja es que puedes ofrecer la rutina completa:
* **El mensaje:** *“Tu piel cuidada es tu mejor base”*. Muestra cómo preparar la piel con la rutina de alta gama de **Aurora** para que el kit **Sol** quede con un acabado impecable y luminoso en minutos.
* Ni la rigidez clínica de *Skin Lab* ni el enfoque de farmacia botánica de *Botica Verde* suelen ofrecer esta transición fluida y estética hacia el color y el día a día.

---

### 2. Formulación y comunicación adaptada al clima de Bogotá
En lugar de hablar de beneficios genéricos ("piel hidratada"), habla de los problemas específicos de vivir en la capital:
* **El ángulo:** El frío sabanero, el viento seco de la tarde, la altitud (2.600 m) y la polución del tráfico resecan la barrera cutánea.
* Posiciona tus productos como la **"barrera protectora urbana"**: cómo **Luna** combate la resequedad en brazos y piernas provocada por las duchas calientes y el frío bogotano, o cómo los antioxidantes de **Aurora** defienden el rostro del smog de la ciudad.

---

### 3. Experiencia de compra y conveniencia hiperlocal
El cliente bogotano valora enormemente la rapidez y la certidumbre en las entregas:
* **Velocidad de entrega:** Ofrece envíos express (el mismo día o máximo 24 horas para Bogotá). Mientras competidores nacionales o marcas más grandes tardan 2 a 4 días hábiles, tu cercanía física te permite ganar por inmediatez.
* **Unboxing sensorial y cuidado:** Un empaque impecable con un aroma distintivo de la marca, notas personalizadas a mano y una guía impresa paso a paso. Quien compra un set premium como *Aurora* espera sentirse en un spa al abrir la caja.
* **Asesoría personalizada por WhatsApp:** Un diagnóstico rápido y cercano de la piel antes de comprar genera una confianza que ninguna farmacia o laboratorio clínico automatizado puede igualar.

---

### 4. "Value Stacking" (Añadir valor percibido en vez de restar precio)
Si compites por precio con productos como *Aurora*, dañas su percepción premium. En su lugar, agrega valor que no te cueste mucho:
* **Muestras cruzadas:** Con cada compra del set *Aurora*, incluye una muestra de viaje de la crema *Luna* o una muestra de tono de *Sol*. Esto premia al cliente y fomenta la recompra en otra categoría.
* **Garantía o soporte:** "Te acompañamos las primeras 3 semanas por WhatsApp para enseñarte a sacarle el máximo provecho a tu kit".

---

**En resumen:**  
Deja que *Botica Verde* pelee por lo netamente artesanal y *Skin Lab* por lo farmacéutico. Tu marca puede ser la **marca de estilo de vida bogotana, moderna, cercana y elegante**, que resuelve en tres pasos simples (cuerpo con *Luna*, rostro con *Aurora* y look diario con *Sol*) la vida de una mujer activa en la ciudad.

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Para el primer trimestre, el objetivo principal no es solo ver cuánto dinero entra, sino **validar la tracción de tus productos en Bogotá, la rentabilidad de tus anuncios y la eficiencia de tu embudo**. 

Con un catálogo escalonado (*Luna* como entrada, *Sol* en la mitad y *Aurora* como premium), estos son los **6 KPIs esenciales** que debes monitorear semana a semana:

---

### 1. Costo de Adquisición de Clientes (CAC)
* **Qué mide:** Cuánto te cuesta en publicidad conseguir una compradora nueva en Bogotá.
  $$\text{CAC} = \frac{\text{Gasto total en pauta (Meta Ads)}}{\text{Número de clientes nuevos adquiridos}}$$
* **Por qué importa en tu caso:** Tu crema de entrada (*Luna*) debe tener un CAC muy bajo. Si alguien entra comprando *Luna*, el CAC debe dejar margen de ganancia o permitirte recuperar la inversión rápido cuando decida probar *Sol* o *Aurora*.

### 2. Ticket Promedio o Valor Medio del Pedido (AOV - Average Order Value)
* **Qué mide:** Cuánto gasta, en promedio, cada persona por pedido.
  $$\text{Ticket Promedio} = \frac{\text{Ventas totales en pesos}}{\text{Número total de pedidos}}$$
* **Por qué importa:** Te indica si tu público solo está comprando el producto barato (*Luna*) o si están llevando combos (ejemplo: *Luna* + *Sol*) o animándose con el set premium (*Aurora*). Tu meta en Q1 es incentivar bundles para elevar este número.

### 3. Tasa de Conversión Web (Conversion Rate)
* **Qué mide:** El porcentaje de visitantes de tu tienda online que efectivamente terminan la compra.
  $$\text{Tasa de Conversión} = \left(\frac{\text{Pedidos completados}}{\text{Visitas a la tienda}}\right) \times 100$$
* **Benchmark:** En e-commerce de belleza en Colombia, una buena tasa oscila entre el **1.2% y el 2.5%**. Si está por debajo del 1%, revisa costos de envío en Bogotá, fricción en la pasarela de pago o falta de claridad en las fotos/descripciones.

### 4. Tasa de Cierre en WhatsApp
* **Qué mide:** De las conversaciones que inician interesadas en un producto o pidiendo asesoría, cuántas se convierten en una venta real.
* **Por qué importa:** En Colombia, los productos de mayor valor como tu set *Aurora* casi siempre pasan por una duda previa ("¿sirve para piel grasa?", "¿qué incluye el set?"). Medir esto te dice si tu asesoría personalizada está cerrando las ventas de ticket alto.

### 5. ROAS (Retorno del Gasto Publicitario en Meta Ads)
* **Qué mide:** Cuántos pesos recibes en ventas por cada peso invertido en anuncios.
  $$\text{ROAS} = \frac{\text{Ingresos generados por anuncios}}{\text{Gasto en anuncios}}$$
* **Meta para Q1:** Apunta a un ROAS mínimo de **3x a 4x** en campañas de conversión directa, asegurando que cubra el costo de los productos y la logística de entrega local.

### 6. Mix de Ventas por Producto (% sobre el total facturado)
* **Qué mide:** La proporción de ingresos que aporta cada uno de tus 3 productos (*Luna*, *Sol* y *Aurora*).
* **Por qué importa:** Te permite responder preguntas estratégicas al final del trimestre:
  * ¿*Luna* está sirviendo de gancho efectivo para atraer clientes nuevos?
  * ¿*Aurora* está teniendo suficiente tracción para justificar su posicionamiento premium frente a *Skin Lab*?
  * ¿*Sol* funciona bien como venta cruzada (upsell)?

---

### Resumen para tu tablero de control en Q1:
| KPI | Frecuencia de revisión | ¿Qué te avisa? |
| :--- | :--- | :--- |
| **CAC** | Semanal | Si tus anuncios en Bogotá están siendo rentables. |
| **Ticket Promedio** | Quincenal | Si estás logrando vender *Aurora* o combos. |
| **Conversión Web** | Semanal | Si tu tienda online es clara y genera confianza. |
| **Cierre en WhatsApp** | Semanal | Tu efectividad resolviendo dudas para productos premium. |
| **ROAS** | Semanal | La eficiencia directa de tu presupuesto publicitario. |
| **Mix de Ventas** | Mensual | Qué producto lidera el volumen vs. cuál lidera la ganancia. |

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

Aquí tienes el plan de campaña de 4 semanas enfocado exclusivamente en **Aurora**, tu set de cuidado facial premium.

---

# Campaña: "El Ritual Aurora: Tu piel protegida en Bogotá"

### 1. Objetivo de la campaña
* **Objetivo comercial:** Lograr un objetivo de ventas directas del set **Aurora** (por ejemplo, meta inicial de 30 a 50 unidades en el mes), elevando el ticket promedio de la tienda.
* **Objetivo de marca:** Posicionar el set **Aurora** como la alternativa local de alta gama más completa y sensorial frente a las opciones clínicas impersonales como *Skin Lab*.

---

### 2. Audiencia objetivo (Bogotá)
* **Perfil:** Mujeres de 25 a 45 años residentes en Bogotá (con enfoque geográfico en zonas como Usaquén, Chapinero, Chicó, Rosales, Santa Ana, Salitre).
* **Intereses:** Cuidado facial avanzado, ingredientes limpios, cosmética botánica, bienestar y estilo de vida consciente.
* **Dolor principal:** Piel deshidratada, apagada o reactiva por el frío capitalino, el viento y la polución, sumado a la falta de tiempo para armar una rutina compleja de 10 pasos.

---

### 3. Canales priorizados
1. **Meta Ads (Instagram / Facebook):** Segmentación exclusiva en Bogotá enfocada en conversión directa a la página de **Aurora**.
2. **Instagram Orgánico:** Vitrina visual y educativa para justificar el valor premium y los resultados de **Aurora**.
3. **WhatsApp Business:** Canal de cierre VIP (asesoría facial personalizada para resolver dudas antes de comprar un producto de alto valor).

---

### 4. Mensaje principal
> *"El clima y el ritmo de Bogotá no tienen por qué apagar tu piel. El set **Aurora** es tu ritual facial integral: alta nutrición botánica que restaura la luminosidad de tu rostro sin rutinas complicadas."*

---

### 5. Plan de acción por semanas

#### **Semana 1: Conciencia y el Problema Urbano**
* **Enfoque:** Educar sobre por qué la piel en Bogotá sufre de resequedad y daño prematuro, presentando el set **Aurora** como la solución integral.
* **Acciones en contenido orgánico:**
  * Reel: *"¿Sientes la piel tirante al final del día en Bogotá? Te explicamos qué le pasa a tu barrera cutánea y por qué creamos el set Aurora"*.
  * Carrusel: Desglose de los productos que componen el set **Aurora** y qué problema específico resuelve cada uno.
* **Meta Ads:** Lanzamiento de anuncios en video corto enfocados en el problema (piel opaca/seca por el clima frío) y la revelación del set **Aurora**.

#### **Semana 2: Experiencia Sensorial y Desglose de Valor**
* **Enfoque:** Justificar el precio premium del set **Aurora** mostrando su calidad, texturas y practicidad.
* **Acciones en contenido orgánico:**
  * Video ASMR de texturas: Aplicación paso a paso del set **Aurora** en piel real (mostrando absorción inmediata, sin sensación grasa).
  * Stories interactivas: *"¿Cuánto te tardas en tu rutina actual?"* Demostración de cómo el set **Aurora** simplifica el cuidado facial en solo 3 pasos clave.
  * Detrás de cámaras: El empaque y la experiencia de unboxing del set **Aurora** (detalles cuidados, presentación de lujo lista para regalo o autocuidado).
* **Meta Ads:** Anuncios de tráfico y conversión mostrando la rutina completa con **Aurora** y destacando ingredientes activos naturales.

#### **Semana 3: Prueba Social y Derribo de Objeciones**
* **Enfoque:** Generar confianza y resolver dudas técnicas que frenan la compra de un producto de alta gama como **Aurora**.
* **Acciones en contenido orgánico:**
  * Reseñas y testimonios en video/captura de clientas que ya usan el set **Aurora** en Bogotá.
  * Comparativa sutil: Explicar por qué elegir la cosmética activa y gentil de **Aurora** frente a tratamientos agresivos o químicos tradicionales.
  * En vivo o Q&A en Stories: *"Resolvemos tus dudas sobre el set Aurora en directo"*.
* **WhatsApp Business:** Activación de un botón directo: *"¿Dudas sobre si el set Aurora es para tu tipo de piel? Habla con una asesora por WhatsApp"*.

#### **Semana 4: Conversión y Cierre con Beneficio Exclusivo**
* **Enfoque:** Crear urgencia e incentivar la compra final del set **Aurora** sin recurrir a descuentos de precio.
* **Estrategia de cierre (Incentivo de alto valor):** Durante esta última semana, por la compra del set **Aurora**, el cliente recibe **envío express gratis en Bogotá** + una minitalla de cortesía de tu crema corporal *Luna*.
* **Acciones en contenido orgánico:**
  * Recordatorios en Stories: *"Últimos días para recibir tu set Aurora con envío prioritario y regalo especial"*.
  * Prueba social reforzada: Fotos de pedidos de **Aurora** saliendo a reparto por las distintas localidades de Bogotá.
* **Meta Ads:** Campaña agresiva de retargeting dirigida a todas las personas que visitaron la página del set **Aurora** o interactuaron con el perfil en las últimas 3 semanas.

---

### 6. Métricas de éxito (KPIs de campaña para Aurora)
1. **Unidades vendidas del set Aurora:** El indicador principal de volumen en el mes.
2. **ROAS específico de la campaña de Aurora:** Meta mínima de **3.5x** en la pauta de Meta Ads.
3. **Tasa de conversión en la página de Aurora:** Meta entre **1.5% y 2.5%** sobre el tráfico bogotano calificado.
4. **Tasa de cierre en WhatsApp para consultas de Aurora:** Meta de al menos el **30%** de compras sobre las personas que pregunten por el set.
5. **Costo por Adquisición (CAC) de Aurora:** Monitorear que el costo de pauta por cada set vendido mantenga un margen neto saludable sobre su precio premium.


## Respuesta completa

Aquí tienes el plan de campaña de 4 semanas enfocado exclusivamente en **Aurora**, tu set de cuidado facial premium.

---

# Campaña: "El Ritual Aurora: Tu piel protegida en Bogotá"

### 1. Objetivo de la campaña
* **Objetivo comercial:** Lograr un objetivo de ventas directas del set **Aurora** (por ejemplo, meta inicial de 30 a 50 unidades en el mes), elevando el ticket promedio de la tienda.
* **Objetivo de marca:** Posicionar el set **Aurora** como la alternativa local de alta gama más completa y sensorial frente a las opciones clínicas impersonales como *Skin Lab*.

---

### 2. Audiencia objetivo (Bogotá)
* **Perfil:** Mujeres de 25 a 45 años residentes en Bogotá (con enfoque geográfico en zonas como Usaquén, Chapinero, Chicó, Rosales, Santa Ana, Salitre).
* **Intereses:** Cuidado facial avanzado, ingredientes limpios, cosmética botánica, bienestar y estilo de vida consciente.
* **Dolor principal:** Piel deshidratada, apagada o reactiva por el frío capitalino, el viento y la polución, sumado a la falta de tiempo para armar una rutina compleja de 10 pasos.

---

### 3. Canales priorizados
1. **Meta Ads (Instagram / Facebook):** Segmentación exclusiva en Bogotá enfocada en conversión directa a la página de **Aurora**.
2. **Instagram Orgánico:** Vitrina visual y educativa para justificar el valor premium y los resultados de **Aurora**.
3. **WhatsApp Business:** Canal de cierre VIP (asesoría facial personalizada para resolver dudas antes de comprar un producto de alto valor).

---

### 4. Mensaje principal
> *"El clima y el ritmo de Bogotá no tienen por qué apagar tu piel. El set **Aurora** es tu ritual facial integral: alta nutrición botánica que restaura la luminosidad de tu rostro sin rutinas complicadas."*

---

### 5. Plan de acción por semanas

#### **Semana 1: Conciencia y el Problema Urbano**
* **Enfoque:** Educar sobre por qué la piel en Bogotá sufre de resequedad y daño prematuro, presentando el set **Aurora** como la solución integral.
* **Acciones en contenido orgánico:**
  * Reel: *"¿Sientes la piel tirante al final del día en Bogotá? Te explicamos qué le pasa a tu barrera cutánea y por qué creamos el set Aurora"*.
  * Carrusel: Desglose de los productos que componen el set **Aurora** y qué problema específico resuelve cada uno.
* **Meta Ads:** Lanzamiento de anuncios en video corto enfocados en el problema (piel opaca/seca por el clima frío) y la revelación del set **Aurora**.

#### **Semana 2: Experiencia Sensorial y Desglose de Valor**
* **Enfoque:** Justificar el precio premium del set **Aurora** mostrando su calidad, texturas y practicidad.
* **Acciones en contenido orgánico:**
  * Video ASMR de texturas: Aplicación paso a paso del set **Aurora** en piel real (mostrando absorción inmediata, sin sensación grasa).
  * Stories interactivas: *"¿Cuánto te tardas en tu rutina actual?"* Demostración de cómo el set **Aurora** simplifica el cuidado facial en solo 3 pasos clave.
  * Detrás de cámaras: El empaque y la experiencia de unboxing del set **Aurora** (detalles cuidados, presentación de lujo lista para regalo o autocuidado).
* **Meta Ads:** Anuncios de tráfico y conversión mostrando la rutina completa con **Aurora** y destacando ingredientes activos naturales.

#### **Semana 3: Prueba Social y Derribo de Objeciones**
* **Enfoque:** Generar confianza y resolver dudas técnicas que frenan la compra de un producto de alta gama como **Aurora**.
* **Acciones en contenido orgánico:**
  * Reseñas y testimonios en video/captura de clientas que ya usan el set **Aurora** en Bogotá.
  * Comparativa sutil: Explicar por qué elegir la cosmética activa y gentil de **Aurora** frente a tratamientos agresivos o químicos tradicionales.
  * En vivo o Q&A en Stories: *"Resolvemos tus dudas sobre el set Aurora en directo"*.
* **WhatsApp Business:** Activación de un botón directo: *"¿Dudas sobre si el set Aurora es para tu tipo de piel? Habla con una asesora por WhatsApp"*.

#### **Semana 4: Conversión y Cierre con Beneficio Exclusivo**
* **Enfoque:** Crear urgencia e incentivar la compra final del set **Aurora** sin recurrir a descuentos de precio.
* **Estrategia de cierre (Incentivo de alto valor):** Durante esta última semana, por la compra del set **Aurora**, el cliente recibe **envío express gratis en Bogotá** + una minitalla de cortesía de tu crema corporal *Luna*.
* **Acciones en contenido orgánico:**
  * Recordatorios en Stories: *"Últimos días para recibir tu set Aurora con envío prioritario y regalo especial"*.
  * Prueba social reforzada: Fotos de pedidos de **Aurora** saliendo a reparto por las distintas localidades de Bogotá.
* **Meta Ads:** Campaña agresiva de retargeting dirigida a todas las personas que visitaron la página del set **Aurora** o interactuaron con el perfil en las últimas 3 semanas.

---

### 6. Métricas de éxito (KPIs de campaña para Aurora)
1. **Unidades vendidas del set Aurora:** El indicador principal de volumen en el mes.
2. **ROAS específico de la campaña de Aurora:** Meta mínima de **3.5x** en la pauta de Meta Ads.
3. **Tasa de conversión en la página de Aurora:** Meta entre **1.5% y 2.5%** sobre el tráfico bogotano calificado.
4. **Tasa de cierre en WhatsApp para consultas de Aurora:** Meta de al menos el **30%** de compras sobre las personas que pregunten por el set.
5. **Costo por Adquisición (CAC) de Aurora:** Monitorear que el costo de pauta por cada set vendido mantenga un margen neto saludable sobre su precio premium.