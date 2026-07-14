# DeepSeek V4 Pro — startup_content/workshop_outline

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 95.053s | tokens_per_second: 71.6
- input_tokens: 198 | output_tokens: 6804
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, proporcionando un plan detallado y estructurado que se ajusta perfectamente a las necesidades de los emprendedores no técnicos.

## Respuesta completa

# ⚡️ Construye tu Asistente de IA para tu Startup – Workshop Práctico  
**Outline completo para un taller presencial de 3 horas**  
*Audiencia: 20-30 emprendedores early‑stage no‑técnicos*

---

## 1. Agenda detallada (3 horas, cronograma realista)

| Hora | Duración | Bloque |
|------|----------|--------|
| 0:00 – 0:10 | 10 min | **Bloque 1** – Bienvenida y rompehielos |
| 0:10 – 0:30 | 20 min | **Bloque 2** – El poder de los asistentes IA para startups |
| 0:30 – 1:00 | 30 min | **Bloque 3** – Diseña el cerebro de tu asistente (hands‑on) |
| 1:00 – 1:10 | 10 min | **Break** – Recarga energías |
| 1:10 – 2:10 | 60 min | **Bloque 4** – ¡Manos a la obra! Construye tu asistente en vivo |
| 2:10 – 2:40 | 30 min | **Bloque 5** – Prueba, mejora y presume tu creación |
| 2:40 – 3:00 | 20 min | **Bloque 6** – Recursos, próximos pasos y cierre |

---

## 2. Materiales que preparar ANTES del taller

### Para los participantes (se les avisa por email 1 semana antes)
- **Laptop** completamente cargada (fundamental).
- **Navegador web actualizado** (Chrome/Firefox).
- **Cuenta gratuita creada en [Poe.com](https://poe.com)** (verificar que puedan iniciar sesión). No requiere tarjeta de crédito.
- Un archivo digital (PDF, Word, .txt) que contenga información relevante de su startup: preguntas frecuentes, descripción de producto, biografía, etc. (opcional, pero muy útil).
- **Acceso a internet** (el venue debe tener Wi‑Fi de calidad).

### Materiales físicos / del facilitador
- **Proyector y pantalla** (conexión estable).
- **Slides** (Google Slides o PowerPoint) – se detalla cantidad de slides por sección más abajo.
- **Hoja de trabajo (worksheet) «Canvas de tu asistente IA»** – una copia por persona, impresa en papel carta. Incluye campos: Nombre del asistente, Propósito, Personalidad, Conocimiento, Ejemplos de preguntas, Límites, Archivo a subir.
- **Pósits y plumones** para la actividad de diseño y testing.
- **Premios simbólicos** (stickers, chocolates) para quienes se animen a mostrar su asistente.
- **Caja de herramientas del facilitador**: cable HDMI, adaptadores, extensión eléctrica, micrófono inalámbrico.
- **Documento de recursos post‑taller** (PDF listo para compartir al final).

### Equipo de apoyo
- Al menos **1 co‑facilitador** por cada 10 personas para ayudar durante la construcción.
- El facilitador principal maneja la pantalla; los co‑facilitadores caminan entre mesas.

---

## 3. Por bloque: título, objetivo, dinámica y key takeaway

### Bloque 1 – Bienvenida y rompehielos (10 min)
**Título:** *¡Bienvenidos a la era de la IA hecha por ti!*  
**Objetivo:** Romper el hielo, alinear expectativas y disparar la energía del grupo.  
**Dinámica:**  
- Charla ultra‑rápida del facilitador (3 min): por qué están aquí, lo que van a lograr.  
- Ejercicio en parejas (5 min): “Encuentra a alguien, preséntense en 30 segundos y cuéntenle el mayor dolor de su startup que una IA podría resolver”.  
- Ronda de cierre (2 min): 2‑3 voluntarios comparten su dolor en voz alta. El facilitador anota en un pizarrón o slide palabras clave (ventas, atención, contenido…).  
**Key takeaway:** *“Todos tenemos desafíos que un asistente inteligente puede atender HOY.”*  
**Slides estimados:** 3 (bienvenida, agenda, slide del rompehielos).

---

### Bloque 2 – El poder de los asistentes IA para startups (20 min)
**Título:** *De cero a productivo: cómo los asistentes IA están cambiando el juego*  
**Objetivo:** Inspirar con casos reales y mostrar que construir un asistente no es magia, es algo alcanzable ahora mismo.  
**Dinámica:**  
- **Charla con storytelling** (15 min): 3 casos de uso concretos, cada uno con un mini‑demo en vivo de un asistente real (hecho en Poe, por ejemplo).  
  - Caso 1: Asistente de atención al cliente que reduce tickets un 40%.  
  - Caso 2: Asistente para generar ideas de contenido en segundos.  
  - Caso 3: “Validador de ideas” que da feedback estructurado a emprendedores.  
- En cada caso se muestra la “receta” básica (prompt + archivo de conocimiento) en pantalla y el resultado funcionando.  
- **Gancho final** (5 min): El facilitador crea un bot mínimo en 2 minutos en vivo con ayuda de la audiencia (le preguntan qué problema quiere resolver).  
**Key takeaway:** *“Hoy construirás tu propio asistente, sin una línea de código, en menos de 1 hora.”*  
**Slides estimados:** 12 (portada de sección, 3 casos con screenshots + demos, slide «tú puedes», cierre transición al siguiente bloque).

---

### Bloque 3 – Diseña el cerebro de tu asistente (30 min)
**Título:** *Diseña el cerebro de tu asistente (worksheet + feedback)*  
**Objetivo:** Deﬁnir con claridad el propósito, la personalidad, el conocimiento y los límites del asistente antes de construirlo, ahorrando tiempo y evitando frustraciones.  
**Dinámica:**  
- **Explicación del canvas** (5 min): El facilitador muestra un ejemplo completo de «asistente de bienvenida para clientes de un SaaS» llenando el worksheet en un proyector.  
- **Trabajo individual** (15 min): Cada persona completa su propio «Canvas de tu asistente IA» (hoja impresa). Se pide que sean muy concretos. Los co‑facilitadores circulan para destrabar.  
- **Feedback rápido en parejas** (10 min): Intercambian su canvas con el vecino, le hacen una pregunta y comentan si la propuesta se entiende. Se puede añadir un pósit con una mejora.  
**Key takeaway:** *“Un asistente efectivo empieza con un diseño claro. Elige un solo trabajo y hazlo extraordinariamente bien.”*  
**Slides estimados:** 8 (plantilla ampliada, ejemplo lleno, instrucciones paso a paso, slide de transición al break).  
**Materiales necesarios:** Worksheet impreso, pósits, plumones.

---

### Bloque 4 – ¡Manos a la obra! Construye tu asistente en vivo (60 min)
**Título:** *Manos a la obra: construye tu asistente con Poe*  
**Objetivo:** Crear una versión funcional del asistente en una plataforma gratuita y sin código, siguiendo un paso a paso guiado.  
**Dinámica:**  
- **Demo paso a paso** en pantalla (el facilitador comparte su pantalla y la audiencia replica en su laptop, con pausas frecuentes).  
  1. **Abrir Poe.com**, verificar inicio de sesión.  
  2. **Crear bot nuevo** → elegir base (ChatGPT o Claude‑instant, recomendamos ChatGPT).  
  3. **Configurar nombre, avatar y descripción** – que coincidan con el canvas.  
  4. **Escribir el prompt (instrucción)** → transformar los campos del canvas en un prompt estructurado. Se entrega una plantilla:  
     *“Eres [Nombre], un asistente que [Propósito]. Tu personalidad es [Personalidad]. Debes responder basándote en [Conocimiento / archivo]. Puedes ayudar con [Ejemplos de preguntas]. NO debes [Límites].”*  
  5. **Subir archivo de conocimiento** (si aplica) – el PDF que prepararon o un ejemplo provisto por el facilitador.  
  6. **Agregar “preguntas sugeridas”** (Suggested Replies) para guiar al usuario.  
  7. **Probar** con al menos 3 preguntas propias, en vivo.  
- **Tiempo real de construcción** (la mayor parte de los 60 min): Cada persona avanza a su ritmo. Co‑facilitadores ayudan 1:1.  
- **Minuto extra** – “Hack del prompt”: El facilitador da un tip rápido para mejorar instrucciones (pedir al bot que haga preguntas de clarificación, o agregar un ejemplo de respuesta ideal).  
**Key takeaway:** *“En tus manos está la herramienta. Ya eres un creador de IA, no solo un usuario.”*  
**Slides estimados:** 18 (secuencia de screenshots con cada paso, plantilla de prompt en grande, recordatorios de revisión).  

**Nota sobre la herramienta:** Se eligió Poe porque permite crear bots personalizados de forma gratuita, no requiere conocimientos técnicos y el enlace se comparte fácilmente. Si algún participante quiere usar la versión de pago (OpenAI GPTs) se le da la opción, pero la guía principal es con Poe.

---

### Bloque 5 – Prueba, mejora y presume tu creación (30 min)
**Título:** *Prueba, mejora y presume tu creación*  
**Objetivo:** Validar el asistente con otro emprendedor, recibir feedback y hacer ajustes rápidos que aumenten su utilidad.  
**Dinámica:**  
- **Testing cruzado** (15 min): En parejas (rotar en cada ronda de 5 min), cada persona comparte el enlace de su bot con su compañero. El compañero hace 3 preguntas reales y anota en un pósit: 1 cosa que le gustó, 1 cosa que mejoraría. Luego intercambian roles.  
- **Momento showcase** (10 min): 3‑4 voluntarios salen al frente y proyectan su asistente. El facilitador hace de “cliente exigente” y el bot responde. La audiencia aplaude.  
- **Tips finales de iteración** (5 min): El facilitador comparte 3 tips rápidos:  
  1. Si se equivoca, agrega ejemplos concretos en el prompt.  
  2. Prueba con usuarios reales y anota las respuestas fallidas.  
  3. Vuelve a subir un archivo de conocimiento más limpio (sin texto basura).  
**Key takeaway:** *“La retroalimentación rápida es el acelerador del aprendizaje. El asistente que probaste hoy estará 10 veces mejor mañana.”*  
**Slides estimados:** 5 (instrucciones de testing, tips visuales, transición al cierre).  
**Materiales:** Pósits de colores, un premio simbólico para los que muestran.

---

### Bloque 6 – Recursos, próximos pasos y cierre (20 min)
**Título:** *De proyecto de taller a herramienta real en tu startup*  
**Objetivo:** Entregar un kit de recursos para seguir mejorando, conectar el asistente con procesos reales y cerrar con una inyección de acción.  
**Dinámica:**  
- **Presentación del “Kit post‑taller”** (5 min): Se comparte un PDF/Drive con:  
  - Plantilla de prompt avanzada.  
  - Guía de mejores prácticas para mantener tu asistente.  
  - Recetario de 10 ideas de asistentes IA para startups (onboarding, ventas, generación de leads, etc.).  
  - Tutorial de cómo integrar el bot en una web o WhatsApp usando herramientas no‑code (Zapier, Landbot).  
- **Plan de acción de 7 días** (5 min): El facilitador muestra un slide con mini‑compromisos:  
  - Día 1: Prueba el asistente con 5 personas de tu equipo.  
  - Día 3: Ajusta el prompt con base en el feedback.  
  - Día 5: Comparte el enlace con 3 clientes potenciales.  
  - Día 7: Decide si migrar a una versión de pago o conectar con tu CRM.  
- **Ronda final “una frase potente”** (8 min): Cada persona dice en voz alta lo que se lleva del taller (solo una frase). El facilitador aplaude cada contribución y refuerza la energía.  
- **Cierre** (2 min): Mensaje final motivador + foto grupal + invitación a la comunidad de WhatsApp/Telegram del evento.  
**Key takeaway:** *“No dejes que tu asistente se oxide en un cajón digital. Llévalo a tus clientes, a tu web, a tu whatsapp… ¡Empieza hoy!”*  
**Slides estimados:** 12 (kit visual, ejemplos de integración, plan de acción, slide de cierre con cita inspiradora, QR de la comunidad).

---

## 4. Ejercicio principal del workshop (que todos puedan hacer)

### “Construye tu propio Asistente de IA para tu Startup con Poe”
**Resumen del ejercicio (realizado en el Bloque 4 + Bloque 5)**
1. **Preparación previa** (Bloque 3): Llenas el Canvas de tu asistente (propósito, personalidad, conocimiento, límites).  
2. **Construcción guiada (60 min)**: Ingresas a Poe.com, creas un bot, copias la plantilla de prompt mejorada con tu diseño, subes un archivo de conocimiento real (FAQ, descripción de producto, etc.) y configuras preguntas sugeridas.  
3. **Validación inmediata (30 min)**: Compartes el enlace con un compañero, recibes feedback, realizas micro‑ajustes y, si te animas, proyectas tu asistente para todo el grupo.

**¿Qué se logra?** Cada participante sale del taller con un asistente funcional, alojado en la nube, que puede compartir mediante un simple enlace. Es un primer entregable que ya puede empezar a probar con su equipo o con clientes reales esa misma tarde.

---

## 5. Recursos para llevar a casa (entregables post‑taller)

Se enviará por email y/o se compartirá un link a una carpeta de Google Drive al finalizar el taller. Incluye:

- 📄 **PDF del Canvas de tu asistente IA** (versión digital editable).
- 📘 **“Guía del creador de asistentes IA para startups”** – 12 páginas con mejores prácticas de prompting, uso de archivos de conocimiento y casos de uso adicionales.
- 🔗 **Recetario de 10 bots que puedes construir hoy** (asistente de onboarding, robot de ventas por WhatsApp, generador de posts para redes, etc.) con los prompts listos para copiar y pegar.
- 🎬 **Video‑tutorial de 10 min** mostrando cómo integrar el bot creado en Poe con una landing page o con WhatsApp usando herramientas no‑code (Zapier y Landbot).
- 📋 **Lista de chequeo de 7 días** para no dejar morir el proyecto.
- 🧑‍🤝‍🧑 **Invitación a grupo de WhatsApp/Telegram** de la comunidad de emprendedores del taller, donde se resolverán dudas y se compartirán avances durante 2 semanas.

---

## 6. Slide count estimado por sección

| Sección | Cantidad de slides | Notas |
|---------|-------------------|-------|
| **Bloque 1** – Bienvenida y rompehielos | 3 | Dinámica, no sobrecargar |
| **Bloque 2** – El poder de los asistentes IA | 12 | Incluye demos visuales y casos |
| **Bloque 3** – Diseño del asistente | 8 | Muestra canvas, ejemplos, instrucciones |
| **Break** | 1 (opcional) | Slide de “volvemos en 10⏰” |
| **Bloque 4** – Construcción paso a paso | 18 | Screenshots, plantilla de prompt, tips |
| **Bloque 5** – Prueba y showcase | 5 | Instrucciones de testing cruzado, tips |
| **Bloque 6** – Recursos y cierre | 12 | Kit de recursos, plan de acción, foto grupal |
| **Total estimado** | **59 slides** | El número puede ajustarse; prima la claridad. |

---

**Energía y enfoque práctico garantizados:** Cada minuto del taller está pensado para que los emprendedores toquen resultado tangible con sus manos. Al final, nadie dirá “qué interesante”, sino “¡mira lo que ya tengo funcionando!”. 🚀

*¿Quieres que preparemos también el guion del facilitador o el diseño de las hojas de trabajo?*