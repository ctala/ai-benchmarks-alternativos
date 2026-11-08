# Gemma 4 31B — agent_long_horizon/implicit_state_construction

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 8.64 | quality: 10.0
- latency_total: 62.36s | tokens_per_second: 88.1
- input_tokens: 14968 | output_tokens: 5327

## Conversación completa (8 turnos)

### Turno 1 — usuario

Hola. Soy Camila, tengo una tienda online en Colombia que vende tres productos: un set de cuidado facial llamado 'Aurora' a precio premium, un kit de maquillaje natural llamado 'Sol' a precio medio, y una crema corporal llamada 'Luna' a precio entrada. Mi único mercado por ahora es Bogotá. Mis dos competidores principales son 'Botica Verde' y 'Skin Lab', ambos también en Bogotá. ¿Te queda claro el contexto?

### Turno 1 — modelo

Hola, Camila. Sí, el contexto me queda totalmente claro.

Tengo registrados los siguientes detalles de tu negocio:

*   **Ubicación y Mercado:** Tienda online operando exclusivamente en Bogotá, Colombia.
*   **Portafolio de Productos:**
    1.  **Aurora:** Set de cuidado facial (Posicionamiento Premium).
    2.  **Sol:** Kit de maquillaje natural (Posicionamiento Precio Medio).
    3.  **Luna:** Crema corporal (Posicionamiento Precio de Entrada).
*   **Competencia Directa:** Botica Verde y Skin Lab.

Estoy listo para ayudarte a planificar tus campañas. ¿En qué te gustaría enfocarte primero? (Por ejemplo: lanzar una promoción para alguno de los productos, una estrategia para ganar terreno frente a tus competidores o atraer nuevos clientes en Bogotá).

### Turno 2 — usuario

Bien. Ayúdame a definir mi propuesta de valor general en 2 oraciones.

### Turno 2 — modelo

Para definir tu propuesta de valor, debemos resaltar que ofreces una solución completa de belleza (desde el cuidado básico hasta el premium) adaptada a diferentes presupuestos, con la ventaja de la cercanía y agilidad de estar en Bogotá.

Aquí tienes dos opciones dependiendo del enfoque que quieras darle:

**Opción 1: Enfoque en Accesibilidad y Variedad (Más comercial)**
"Ofrecemos una experiencia integral de belleza y cuidado personal en Bogotá, con opciones que van desde el cuidado esencial hasta el tratamiento premium. Brindamos productos de alta calidad diseñados para adaptarse a cada presupuesto y necesidad de la piel, sin complicaciones."

**Opción 2: Enfoque en Bienestar y Segmentación (Más aspiracional)**
"Acompañamos la rutina de belleza de la mujer bogotana a través de tres niveles de cuidado: desde la hidratación diaria hasta el maquillaje natural y el cuidado facial avanzado. Unimos calidad y versatilidad para que el bienestar sea accesible para todas, sin importar su presupuesto."

**¿Cuál de las dos resuena más con la personalidad de tu marca?** Si prefieres algo más disruptivo para diferenciarte de Botica Verde y Skin Lab, dímelo y lo ajustamos.

### Turno 3 — usuario

¿Qué canales digitales recomendarías priorizar para llegar a mi público?

### Turno 3 — modelo

Dado que tu mercado es exclusivamente **Bogotá** y tienes una escalera de precios muy clara (entrada, medio y premium), necesitas canales que permitan segmentar muy bien el presupuesto y que sean visualmente atractivos.

Para diferenciarte de Botica Verde y Skin Lab, te recomiendo priorizar estos tres canales:

### 1. Instagram y TikTok (El motor visual)
Son fundamentales porque vendes belleza y cuidado personal, donde el "antes y después" y la textura del producto son clave.
*   **Para 'Luna' (Precio entrada):** Crea contenido rápido, dinámico y viral en TikTok. Enfócate en el uso diario y la accesibilidad.
*   **Para 'Sol' (Precio medio):** Tutoriales de maquillaje natural ("get ready with me") en Reels, resaltando la naturalidad.
*   **Para 'Aurora' (Premium):** Contenido más estético, sofisticado y educativo en Instagram, enfocándote en los beneficios a largo plazo y la exclusividad.

### 2. Meta Ads (Segmentación hiper-local)
Al estar solo en Bogotá, no puedes desperdiciar presupuesto. La publicidad pagada en Facebook e Instagram te permitirá:
*   **Geocercas:** Dirigir los anuncios específicamente a barrios o zonas de Bogotá donde se encuentre tu cliente ideal.
*   **Segmentación por interés:** Diferenciar los anuncios. Por ejemplo, mostrar **Aurora** a personas interesadas en "lujo" o "skincare avanzado", y **Luna** a quienes buscan "hidratación" o "belleza económica".

### 3. WhatsApp Business (Cierre de ventas y fidelización)
En el mercado colombiano, y especialmente en Bogotá, el cierre de ventas por WhatsApp es altísimo.
*   **Asesoría personalizada:** Al tener productos de diferentes precios, puedes guiar a la cliente. Si alguien pregunta por **Luna**, puedes hacer un *upselling* sugiriendo el kit **Sol**.
*   **Logística:** Al ser una tienda online local, usar WhatsApp para coordinar los envíos rápidos en la ciudad genera mucha confianza frente a competidores más grandes y fríos.

**Mi recomendación de prioridad:**
Si tienes recursos limitados, empieza con **Instagram $\rightarrow$ Meta Ads (Bogotá) $\rightarrow$ WhatsApp**. 

¿Te gustaría que diseñemos una estrategia de contenidos específica para alguno de tus tres productos?

### Turno 4 — usuario

¿Con qué frecuencia debería publicar contenido orgánico en cada canal?

### Turno 4 — modelo

Para definir la frecuencia, debemos equilibrar la visibilidad sin saturar a tu audiencia, considerando que manejas tres niveles de productos (**Luna, Sol y Aurora**). No necesitas publicar lo mismo en todo, sino distribuir el peso según el objetivo de cada canal.

Aquí tienes una propuesta de calendario orgánico:

### 1. Instagram (Tu vitrina y catálogo)
Es donde el cliente valida que tu marca es real y profesional.
*   **Historias (Daily):** 3 a 5 veces al día. Es el canal más importante para generar confianza. 
    *   *Contenido:* Encuestas, testimonios de clientes en Bogotá, el "detrás de escena" de los envíos y recordatorios rápidos de los beneficios de **Aurora, Sol y Luna**.
*   **Reels (3 a 4 veces por semana):** Es lo que te traerá gente nueva. 
    *   *Contenido:* Tutoriales cortos de maquillaje con **Sol**, texturas de la crema **Luna** o la experiencia de lujo de **Aurora**.
*   **Posts/Carruseles (2 veces por semana):** Contenido educativo y estético.
    *   *Contenido:* Guías de pasos para el cuidado facial o comparativas de beneficios.

### 2. TikTok (Tu motor de descubrimiento)
Aquí el algoritmo premia la cantidad y la autenticidad sobre la perfección.
*   **Frecuencia:** 1 video diario (o mínimo 4 a 5 por semana).
*   **Estrategia:** No busques la estética perfecta de Instagram. Haz videos más "crudos": "3 razones por las que necesitas la crema **Luna**", "Cómo lograr un look natural con **Sol**" o "Mi rutina nocturna premium con **Aurora**".

### 3. WhatsApp Business (Tu canal de cierre y retención)
Aquí no publicas para atraer, sino para convertir a quienes ya te conocen.
*   **Estados de WhatsApp (2 a 3 veces por semana):** 
    *   *Contenido:* "Últimas unidades de **Sol** disponibles para entrega hoy en Bogotá", o un testimonio real de una cliente satisfecha. Evita publicar diario para no cansar al cliente y que te silencien.

---

### Resumen de frecuencia semanal:

| Canal | Historias/Estados | Posts/Reels/Videos | Objetivo Principal |
| :--- | :--- | :--- | :--- |
| **Instagram** | Diariamente (3-5) | 5 - 6 piezas totales | Aspiración y Confianza |
| **TikTok** | N/A | 5 - 7 videos | Alcance y Viralidad |
| **WhatsApp** | 2 - 3 veces/sem | N/A | Venta Directa y Fidelidad |

**Un consejo estratégico:** 
Para no agotarte creando contenido diferente, usa el **"Reciclaje de Contenido"**: Graba un video largo para TikTok $\rightarrow$ súbelo como Reel en Instagram $\rightarrow$ toma una captura de pantalla del mejor comentario de ese video y súbelo a tus Historias y Estados de WhatsApp.

¿Quieres que te ayude a armar una parrilla de contenidos para la primera semana, distribuyendo los tres productos?

### Turno 5 — usuario

¿Qué tipo de contenido funciona mejor para productos de skincare?

### Turno 5 — modelo

Para el skincare, el contenido que mejor funciona es aquel que **elimina la duda y genera confianza**, ya que el cliente siente que está poniendo algo sobre su piel y teme una reacción negativa o que el producto no funcione.

Dado que tienes tres niveles de precios, el contenido debe variar según el producto. Aquí tienes los formatos ganadores divididos por el objetivo:

### 1. Contenido de "Prueba Social" (El más efectivo)
Nadie quiere ser el primero en probar. La gente compra resultados, no ingredientes.
*   **Antes y Después:** Fotos reales (sin filtros) de los efectos de **Aurora** en la piel.
*   **Testimonios en video:** Una cliente de Bogotá contando cómo siente su piel después de usar la crema **Luna**.
*   **UGC (User Generated Content):** Repostear cuando una clienta etiqueta tu marca en sus historias. Esto es oro puro para competir con Botica Verde y Skin Lab.

### 2. Contenido Educativo (Genera autoridad)
Si enseñas a la persona a cuidar su piel, confiará en que tu producto es la solución.
*   **El "Cómo usar":** Un paso a paso claro. Ejemplo: "El orden correcto: primero el set **Aurora**, luego el maquillaje **Sol**".
*   **Mitos vs. Realidades:** "Mito: Las cremas económicas no hidratan. Realidad: Te mostramos cómo **Luna** mantiene la hidratación todo el día".
*   **Ingredientes clave:** Explicar de forma sencilla qué hace el ingrediente estrella de cada producto (sin usar lenguaje médico aburrido).

### 3. Contenido Sensorial y Estético (Genera deseo)
El skincare es una experiencia de autocuidado ("self-care").
*   **ASMR de texturas:** Videos cortos con sonido real abriendo el envase, aplicando la crema **Luna** en la piel o mostrando la pigmentación de **Sol**.
*   **Rutinas "Aesthethic":** Videos relajantes de una rutina de noche usando el set **Aurora**, con música tranquila y luz tenue. Esto justifica el precio premium.

### 4. Contenido de Comparación y Guía (Facilita la compra)
Ayuda al cliente a elegir cuál de tus tres productos es para él.
*   **"¿Cuál elegir según tu presupuesto?":** Un cuadro comparativo donde muestres que **Luna** es para hidratación básica, **Sol** para un look natural y **Aurora** para una transformación profunda.
*   **"Solución a un problema":** "Si tienes la piel seca por el clima de Bogotá $\rightarrow$ Usa **Luna**".

---

### Estrategia aplicada a tu portafolio:

| Producto | Enfoque de Contenido | Formato Ideal |
| :--- | :--- | :--- |
| **Luna (Entrada)** | Utilidad, precio, uso diario. | TikToks rápidos, "Life hacks". |
| **Sol (Medio)** | Naturalidad, versatilidad, look final. | Reels de "Get Ready With Me" (GRWM). |
| **Aurora (Premium)** | Exclusividad, ciencia, resultados profundos. | Carruseles educativos, videos cinemáticos. |

**Tip extra:** Como estás en Bogotá, aprovecha el factor climático. Crea contenido sobre **"Cómo proteger tu piel del frío y la contaminación de Bogotá"** usando tus productos. Esto te hará sentir mucho más cercana que una marca genérica.

¿Te gustaría que redactara los guiones para 3 videos cortos (uno para cada producto) siguiendo estas pautas?

### Turno 6 — usuario

¿Cómo diferenciarme de mis competidores sin entrar en guerra de precios?

### Turno 6 — modelo

Entrar en una guerra de precios es peligroso, especialmente cuando tienes un producto premium como **Aurora**, ya que bajar los precios puede destruir la percepción de calidad y lujo.

Para diferenciarte de **Botica Verde** y **Skin Lab** sin tocar el precio, debes mover la conversación del "cuánto cuesta" al "qué valor me aporta". Aquí tienes cuatro estrategias concretas:

### 1. Especialización en el "Contexto Bogotá" (Hiper-localización)
Tus competidores probablemente usan marketing general. Tú puedes ganar siendo la experta en la piel de la mujer bogotana.
*   **El ángulo:** Crea contenido y soluciones basadas en el clima y entorno de la ciudad.
*   **Ejemplo:** "La rutina para combatir la sequedad del frío de Bogotá" (usando **Luna**) o "Cómo proteger tu piel de la contaminación del tráfico de la ciudad" (usando **Aurora**).
*   **El valor:** No vendes una crema, vendes una solución específica para el entorno donde vive tu cliente.

### 2. Experiencia de Cliente "Boutique" vs. "Corporativa"
Botica Verde y Skin Lab suelen ser marcas más masivas y frías. Tú puedes ganar en la **humanización**.
*   **Asesoría Personalizada:** En lugar de solo vender, ofrece un "Diagnóstico de rutina rápido" vía WhatsApp. Ayuda a la cliente a decidir si necesita la simplicidad de **Luna** o la potencia de **Aurora**.
*   **Packaging con Alma:** Incluye una nota escrita a mano en cada envío en Bogotá o una muestra pequeña de **Sol** cuando alguien compre **Luna**. Ese detalle hace que el precio pase a segundo plano porque la experiencia es superior.

### 3. Venta por "Escalera de Valor" (Estrategia de Portafolio)
Usa tus tres productos no como opciones aisladas, sino como un camino de crecimiento para la cliente.
*   **El concepto:** No compitas con el precio de entrada de los demás; crea un ecosistema. 
*   **La narrativa:** "Empieza tu camino al cuidado con **Luna**, eleva tu look con **Sol** y alcanza tu máxima versión con **Aurora**". 
*   **El valor:** Le das a la cliente una razón para quedarse contigo a medida que su presupuesto o sus necesidades de piel evolucionen, en lugar de que se vaya a la competencia.

### 4. Enfoque en "Resultados Reales" sobre "Promesas de Marca"
Las marcas grandes suelen usar modelos y fotos de estudio. Tú puedes diferenciarte con la **transparencia**.
*   **Contenido Real:** Muestra pieles reales de mujeres en Bogotá, con poros, texturas y resultados honestos.
*   **Educación Profunda:** Mientras la competencia dice "hidrata la piel", tú explica *por qué* el ingrediente de **Aurora** funciona mejor para alguien que vive en la altura de Bogotá.
*   **El valor:** La autoridad y la honestidad generan una lealtad que el precio bajo no puede comprar.

**Resumen para tu comunicación:**
*   **Botica Verde/Skin Lab:** Venden productos de belleza.
*   **Tú (Camila):** Vendes una rutina de cuidado diseñada específicamente para la mujer que vive y enfrenta el día a día en Bogotá.

**¿Cuál de estos enfoques sientes que va más con tu personalidad como emprendedora?** Si eliges uno, podemos crear una acción concreta para implementarlo esta misma semana.

### Turno 7 — usuario

¿Qué KPIs debería medir el primer trimestre?

### Turno 7 — modelo

Para el primer trimestre, el error más común es obsesionarse solo con las ventas totales. Como estás construyendo marca y tienes una estructura de precios escalonada (**Luna, Sol y Aurora**), necesitas medir no solo *cuánto* vendes, sino *cómo* se están comportando tus clientes y tus canales.

Aquí tienes los KPIs divididos por objetivos estratégicos:

### 1. KPIs de Ventas y Portafolio (Salud del Negocio)
Estos te dirán si tu estrategia de precios está funcionando y cuál es tu producto "gancho".
*   **Ventas por Producto:** ¿Cuál se vende más? (Si **Luna** es el más vendido, es tu puerta de entrada; si es **Aurora**, tienes un mercado premium fuerte).
*   **Ticket Promedio de Venta:** (Ventas totales / Número de pedidos). Esto te dirá si las clientas compran un solo producto o si estás logrando que lleven, por ejemplo, **Luna + Sol**.
*   **Tasa de Conversión de WhatsApp:** (Número de ventas cerradas / Número de personas que escribieron). Este es vital porque es tu canal de cierre en Bogotá.

### 2. KPIs de Adquisición y Visibilidad (Crecimiento)
Para saber si tus esfuerzos en TikTok e Instagram están trayendo gente nueva de Bogotá.
*   **Crecimiento de Comunidad Local:** No midas solo seguidores, mide el crecimiento de personas que interactúan y que están en Bogotá.
*   **Costo de Adquisición de Cliente (CAC):** Si haces Meta Ads, divide lo invertido entre el número de clientes nuevos. Esto te dirá si captar un cliente de **Luna** es rentable o si necesitas enfocarte más en vender **Aurora**.
*   **Alcance (Reach) de Reels/TikToks:** Cuántas personas nuevas vieron tu contenido. Esto mide la efectividad de tu estrategia de "descubrimiento".

### 3. KPIs de Fidelización y Calidad (Diferenciación)
Para medir si realmente te estás diferenciando de Botica Verde y Skin Lab.
*   **Tasa de Recompra:** ¿Cuántas clientes que compraron **Luna** regresaron al mes siguiente por **Sol** o **Aurora**? (Este es el KPI más importante para medir tu "Escalera de Valor").
*   **Número de Testimonios/UGC Recibidos:** Cuántas clientas te enviaron una foto o video de sus resultados. Esto mide la confianza y la lealtad.
*   **Tasa de Recomendación:** Pregunta en WhatsApp: *"¿Cómo te enteraste de nosotros?"*. Si el porcentaje de "recomendación de una amiga" sube, tu diferenciación está funcionando.

---

### Tabla de seguimiento sugerida (Dashboard Trimestral)

Si quieres llevar un control sencillo en un Excel, usa estas columnas:

| KPI | Meta Mes 1 | Meta Mes 2 | Meta Mes 3 | ¿Por qué medirlo? |
| :--- | :--- | :--- | :--- | :--- |
| **Ventas Luna / Sol / Aurora** | $\text{X units}$ | $\text{X units}$ | $\text{X units}$ | Ver qué producto impulsa el flujo. |
| **Ticket Promedio** | $\text{\$ Valor}$ | $\text{\$ Valor}$ | $\text{\$ Valor}$ | Medir el éxito del *upselling*. |
| **Conversión WhatsApp** | $\text{X\%}$ | $\text{X\%}$ | $\text{X\%}$ | Optimizar el cierre de ventas. |
| **Tasa de Recompra** | $\text{X\%}$ | $\text{X\%}$ | $\text{X\%}$ | Validar la lealtad vs competencia. |
| **CAC (Meta Ads)** | $\text{\$ Valor}$ | $\text{\$ Valor}$ | $\text{\$ Valor}$ | Controlar el gasto en publicidad. |

**Mi consejo final:** 
En el **Mes 1**, enfócate en el **Alcance y Conversión de WhatsApp** (atraer y cerrar). 
En el **Mes 2**, enfócate en el **Ticket Promedio** (vender más a los mismos). 
En el **Mes 3**, enfócate en la **Tasa de Recompra** (fidelizar para no depender siempre de anuncios).

¿Te gustaría que te ayude a definir metas numéricas realistas para alguno de estos KPIs basándonos en tu capacidad actual de operación?

### Turno 8 — usuario

Perfecto. Ahora hagamos una campaña enfocada exclusivamente en mi producto más caro. Quiero un plan de 4 semanas con objetivo, audiencia, canales, mensaje principal y métricas de éxito. Sé específica con el nombre del producto en todo el plan.

### Turno 8 — modelo

Esta es la planificación estratégica para el lanzamiento o impulso de tu producto premium. Al ser el de mayor precio, no venderemos "una crema", sino un **resultado transformador y una experiencia de lujo**.

### Campaña: "El Despertar de tu Piel con Aurora"

**1. Objetivo General:**
Posicionar el set de cuidado facial **Aurora** como la inversión definitiva en salud cutánea para la mujer bogotana, logrando [X] ventas en 4 semanas y elevando la percepción de valor de la marca.

**2. Audiencia Objetivo (Buyer Persona):**
*   **Ubicación:** Bogotá (Zonas con mayor poder adquisitivo o mujeres profesionales que trabajan en centros empresariales).
*   **Perfil:** Mujeres de 25 a 45 años que ya tienen una rutina básica, pero sienten que su piel no mejora o que el clima de la ciudad la apaga.
*   **Psicografía:** Valoran el tiempo, buscan calidad sobre cantidad, están dispuestas a pagar más por resultados comprobados y ven el skincare como un ritual de bienestar, no solo como higiene.

**3. Canales Prioritarios:**
*   **Instagram:** (Feed y Stories) para la parte aspiracional y educativa.
*   **Meta Ads:** Segmentación cerrada en Bogotá por intereses en "Lujo", "Cuidado de la piel avanzado" y "Cosmecéuticos".
*   **WhatsApp Business:** Para asesorías personalizadas de cierre (estilo Concierge).

**4. Mensaje Principal (Concepto Creativo):**
*"Tu piel merece un nuevo amanecer. **Aurora** no es solo un set de cuidado facial; es la ciencia y el lujo diseñados para devolverle la luminosidad a tu rostro, protegiéndolo del ritmo y el clima de Bogotá."*

---

### 5. Plan de Ejecución Semanal

#### Semana 1: Educación y Deseo (La Fase de Concientización)
*   **Objetivo:** Que la audiencia entienda por qué **Aurora** es premium y qué problema resuelve que los otros no.
*   **Contenido:**
    *   **Reel:** "La diferencia entre hidratar y regenerar". Explicación de los activos de **Aurora**.
    *   **Carrusel:** "3 señales de que tu piel necesita el set **Aurora**" (opacidad, líneas de expresión, daño ambiental).
    *   **Stories:** Encuestas sobre problemas de la piel en Bogotá.
*   **Ads:** Video corto resaltando la textura y el empaque de **Aurora**.

#### Semana 2: Autoridad y Prueba Social (La Fase de Confianza)
*   **Objetivo:** Eliminar el miedo al precio mediante la demostración de resultados.
*   **Contenido:**
    *   **Video:** Testimonio real de una cliente bogotana usando **Aurora** (Antes y Después).
    *   **Post:** "La ciencia detrás de **Aurora**": Desglose de ingredientes clave y sus beneficios.
    *   **Stories:** Q&A (Preguntas y respuestas) sobre el uso correcto del set.
*   **Ads:** Testimonios en formato Story dirigidos a quienes vieron los anuncios de la semana 1.

#### Semana 3: Experiencia y Exclusividad (La Fase de Conversión)
*   **Objetivo:** Empujar la venta resaltando la experiencia de lujo.
*   **Contenido:**
    *   **Reel ASMR:** El ritual nocturno con **Aurora** (sonidos del empaque, aplicación lenta, música relajante).
    *   **Post:** "Invierte en ti: Por qué **Aurora** es la mejor decisión para tu piel este año".
    *   **Stories:** "Solo [X] sets de **Aurora** disponibles para envío inmediato en Bogotá esta semana". (Uso de escasez).
*   **Ads:** Llamado a la acción directo: "Agenda tu asesoría personalizada para **Aurora** vía WhatsApp".

#### Semana 4: Cierre y Fidelización (La Fase de Recolección)
*   **Objetivo:** Cerrar ventas rezagadas y recolectar feedback.
*   **Contenido:**
    *   **Post:** "Lo que dicen las primeras mujeres que transformaron su piel con **Aurora**".
    *   **Stories:** Cuenta regresiva para finalizar la promoción de lanzamiento o el stock disponible.
    *   **WhatsApp:** Seguimiento directo a quienes preguntaron en las semanas 1 y 2 pero no compraron.
*   **Ads:** Retargeting agresivo: "Última oportunidad de obtener tu set **Aurora**".

---

### 6. Métricas de Éxito (KPIs de la Campaña)

1.  **Ventas Totales de Aurora:** Número de sets vendidos durante el mes.
2.  **Tasa de Conversión de WhatsApp:** % de personas que preguntaron por **Aurora** y efectivamente compraron.
3.  **Costo de Adquisición (CAC) de Aurora:** Cuánto invertiste en Meta Ads dividido entre los clientes nuevos de este producto.
4.  **Calidad de Leads:** Cantidad de solicitudes de "asesoría personalizada" (esto indica que el cliente valora el producto y no solo el precio).

**¿Te gustaría que redactara los copies (textos) para los anuncios de Meta Ads de la Semana 1?**


## Respuesta completa

Esta es la planificación estratégica para el lanzamiento o impulso de tu producto premium. Al ser el de mayor precio, no venderemos "una crema", sino un **resultado transformador y una experiencia de lujo**.

### Campaña: "El Despertar de tu Piel con Aurora"

**1. Objetivo General:**
Posicionar el set de cuidado facial **Aurora** como la inversión definitiva en salud cutánea para la mujer bogotana, logrando [X] ventas en 4 semanas y elevando la percepción de valor de la marca.

**2. Audiencia Objetivo (Buyer Persona):**
*   **Ubicación:** Bogotá (Zonas con mayor poder adquisitivo o mujeres profesionales que trabajan en centros empresariales).
*   **Perfil:** Mujeres de 25 a 45 años que ya tienen una rutina básica, pero sienten que su piel no mejora o que el clima de la ciudad la apaga.
*   **Psicografía:** Valoran el tiempo, buscan calidad sobre cantidad, están dispuestas a pagar más por resultados comprobados y ven el skincare como un ritual de bienestar, no solo como higiene.

**3. Canales Prioritarios:**
*   **Instagram:** (Feed y Stories) para la parte aspiracional y educativa.
*   **Meta Ads:** Segmentación cerrada en Bogotá por intereses en "Lujo", "Cuidado de la piel avanzado" y "Cosmecéuticos".
*   **WhatsApp Business:** Para asesorías personalizadas de cierre (estilo Concierge).

**4. Mensaje Principal (Concepto Creativo):**
*"Tu piel merece un nuevo amanecer. **Aurora** no es solo un set de cuidado facial; es la ciencia y el lujo diseñados para devolverle la luminosidad a tu rostro, protegiéndolo del ritmo y el clima de Bogotá."*

---

### 5. Plan de Ejecución Semanal

#### Semana 1: Educación y Deseo (La Fase de Concientización)
*   **Objetivo:** Que la audiencia entienda por qué **Aurora** es premium y qué problema resuelve que los otros no.
*   **Contenido:**
    *   **Reel:** "La diferencia entre hidratar y regenerar". Explicación de los activos de **Aurora**.
    *   **Carrusel:** "3 señales de que tu piel necesita el set **Aurora**" (opacidad, líneas de expresión, daño ambiental).
    *   **Stories:** Encuestas sobre problemas de la piel en Bogotá.
*   **Ads:** Video corto resaltando la textura y el empaque de **Aurora**.

#### Semana 2: Autoridad y Prueba Social (La Fase de Confianza)
*   **Objetivo:** Eliminar el miedo al precio mediante la demostración de resultados.
*   **Contenido:**
    *   **Video:** Testimonio real de una cliente bogotana usando **Aurora** (Antes y Después).
    *   **Post:** "La ciencia detrás de **Aurora**": Desglose de ingredientes clave y sus beneficios.
    *   **Stories:** Q&A (Preguntas y respuestas) sobre el uso correcto del set.
*   **Ads:** Testimonios en formato Story dirigidos a quienes vieron los anuncios de la semana 1.

#### Semana 3: Experiencia y Exclusividad (La Fase de Conversión)
*   **Objetivo:** Empujar la venta resaltando la experiencia de lujo.
*   **Contenido:**
    *   **Reel ASMR:** El ritual nocturno con **Aurora** (sonidos del empaque, aplicación lenta, música relajante).
    *   **Post:** "Invierte en ti: Por qué **Aurora** es la mejor decisión para tu piel este año".
    *   **Stories:** "Solo [X] sets de **Aurora** disponibles para envío inmediato en Bogotá esta semana". (Uso de escasez).
*   **Ads:** Llamado a la acción directo: "Agenda tu asesoría personalizada para **Aurora** vía WhatsApp".

#### Semana 4: Cierre y Fidelización (La Fase de Recolección)
*   **Objetivo:** Cerrar ventas rezagadas y recolectar feedback.
*   **Contenido:**
    *   **Post:** "Lo que dicen las primeras mujeres que transformaron su piel con **Aurora**".
    *   **Stories:** Cuenta regresiva para finalizar la promoción de lanzamiento o el stock disponible.
    *   **WhatsApp:** Seguimiento directo a quienes preguntaron en las semanas 1 y 2 pero no compraron.
*   **Ads:** Retargeting agresivo: "Última oportunidad de obtener tu set **Aurora**".

---

### 6. Métricas de Éxito (KPIs de la Campaña)

1.  **Ventas Totales de Aurora:** Número de sets vendidos durante el mes.
2.  **Tasa de Conversión de WhatsApp:** % de personas que preguntaron por **Aurora** y efectivamente compraron.
3.  **Costo de Adquisición (CAC) de Aurora:** Cuánto invertiste en Meta Ads dividido entre los clientes nuevos de este producto.
4.  **Calidad de Leads:** Cantidad de solicitudes de "asesoría personalizada" (esto indica que el cliente valora el producto y no solo el precio).

**¿Te gustaría que redactara los copies (textos) para los anuncios de Meta Ads de la Semana 1?**