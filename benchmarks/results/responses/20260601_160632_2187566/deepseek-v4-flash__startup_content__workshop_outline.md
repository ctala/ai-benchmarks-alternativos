# DeepSeek V4 Flash (OpenRouter) — startup_content/workshop_outline

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 8.36 | quality: 9.72
- latency_total: 37.229s | tokens_per_second: 68.0
- input_tokens: 198 | output_tokens: 2533
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes el outline completo para el workshop **"Construye tu Asistente de IA para tu Startup - Workshop Práctico"**, diseñado para emprendedores no técnicos en etapa temprana.

---

## 📋 **Resumen General**
- **Duración:** 3 horas (180 minutos)  
- **Formato:** Presencial, 20-30 personas  
- **Nivel:** Principiante, sin código  
- **Enfoque:** 70% práctica / 30% teoría  
- **Herramienta principal:** **ChatGPT + Zapier + Make (Integromat)** o **Voiceflow** (según presupuesto y acceso)

---

## 🧰 **Materiales Necesarios (Preparar antes)**

### Para el facilitador:
- Computadora con proyector y sonido
- Cuenta gratuita de **ChatGPT** (OpenAI) o **Claude** (Anthropic) – demo en vivo
- Cuenta gratuita de **Zapier** o **Make** (para automatización)
- Acceso a **Google Colab** (opcional, para mostrar código simple)
- **Plantilla de prompt** impresa o en PDF (1 por persona)
- Post-its, marcadores, pizarra blanca
- **Documento compartido** (Google Docs) con enlaces y recursos

### Para los asistentes:
- Laptop o tablet con internet
- Cuenta de **ChatGPT** (gratuita) creada antes del taller
- Cuenta de **Zapier** o **Make** (gratuita) – recomendar crear 1 día antes
- **Teléfono** para pruebas de voz (si se incluye asistente de voz)

### Setup del salón:
- Mesas en islas (4-5 personas por grupo)
- WiFi estable con ancho de banda suficiente
- Extensiones eléctricas para laptops
- Snacks y café para mantener energía

---

## 🗓️ **Agenda Detallada (3 horas)**

### **Bloque 1: ¿Por qué tu startup necesita un asistente de IA? (20 min)**
- **Título:** "De la idea al asistente: el superpoder que no sabías que tenías"
- **Objetivo:** Entender el valor de un asistente de IA para startups sin equipo técnico.
- **Dinámica:** Charla + Demo rápida
  - Cuenta la historia de una startup latina que redujo tiempo de atención al cliente en 70% con un chatbot simple.
  - Muestra en vivo: "Mira, este asistente responde preguntas de mi pitch deck en 2 segundos".
- **Key takeaway:** Un asistente de IA no es magia, es una herramienta que puedes construir hoy sin saber programar.

### **Bloque 2: Anatomía de un asistente de IA (25 min)**
- **Título:** "El cerebro, la memoria y la voz de tu asistente"
- **Objetivo:** Desglosar las partes clave: prompt, base de conocimiento, canales (chat, voz, web).
- **Dinámica:** Charla interactiva + Pizarra
  - Dibuja en vivo un diagrama simple: **Input → Prompt → Base de conocimiento → Output → Canal**
  - Pide ejemplos del público: "¿Qué tareas tediosas haces cada día?"
- **Key takeaway:** Tu asistente es tan bueno como la claridad de tu prompt y la calidad de tu base de conocimiento.

### **Bloque 3: Ejercicio principal – Construye tu primer asistente (60 min)**
- **Título:** "Manos a la obra: tu asistente en 45 minutos"
- **Objetivo:** Cada participante crea un asistente funcional que responda preguntas sobre su startup.
- **Dinámica:** **Ejercicio práctico guiado paso a paso** (ver sección detallada abajo)
  - El facilitador proyecta cada paso y los asistentes lo replican.
  - Los ayudantes (si hay) circulan resolviendo dudas.
- **Key takeaway:** En menos de 1 hora puedes tener un prototipo funcional.

### **Bloque 4: Automatización – Haz que tu asistente trabaje solo (25 min)**
- **Título:** "El asistente que nunca duerme: conecta con tu negocio"
- **Objetivo:** Conectar el asistente con herramientas como correo, CRM o calendario.
- **Dinámica:** Demo + Mini-ejercicio
  - Muestra cómo conectar el asistente a un formulario de Google Sheets o Slack.
  - Los asistentes crean una automatización simple (ej: "Cuando alguien pregunte por precio, enviar un email automático").
- **Key takeaway:** La automatización convierte un asistente pasivo en un miembro activo de tu equipo.

### **Bloque 5: Presentación y feedback (20 min)**
- **Título:** "Demo Day de asistentes: muestra lo que creaste"
- **Objetivo:** Compartir aprendizajes y recibir feedback del grupo.
- **Dinámica:** **Pitch relámpago**
  - 3 voluntarios (o grupos) muestran su asistente en 2 minutos cada uno.
  - El facilitador da feedback rápido y constructivo.
  - El grupo aplaude y comenta ideas.
- **Key takeaway:** El mejor aprendizaje viene de ver lo que otros construyeron.

### **Bloque 6: Cierre y recursos (10 min)**
- **Título:** "Ahora te toca a ti: próximos pasos"
- **Objetivo:** Dar herramientas para seguir avanzando.
- **Dinámica:** Charla + Entrega de recursos
  - Repaso rápido de los 3 pasos post-workshop: 1) Mejorar prompt, 2) Agregar más datos, 3) Probar con usuarios reales.
  - Comparte el documento con enlaces (ver sección Recursos).
- **Key takeaway:** El workshop es el inicio, no el final. Tu asistente mejorará con cada interacción.

---

## 🛠️ **Ejercicio Principal del Workshop (60 min)**

**Objetivo:** Cada participante construye un asistente de IA funcional que responda preguntas sobre su startup.

### **Paso 1: Prepara tu base de conocimiento (10 min)**
- Los asistentes escriben en un documento de Google Docs (o Notion) las 10 preguntas más frecuentes de sus clientes.
- Agregan respuestas claras y enlaces a su web/producto.

### **Paso 2: Crea el prompt del asistente (10 min)**
- Usan la **plantilla de prompt** (ver Recursos) para definir:
  - Rol del asistente (ej: "Eres un experto en ventas para mi startup")
  - Contexto de la startup (en 1 párrafo)
  - Reglas de comportamiento (ej: "Siempre pregunta el email antes de dar un precio")
  - Ejemplos de preguntas y respuestas ideales

### **Paso 3: Configura el asistente en ChatGPT (15 min)**
- En ChatGPT, crean un **GPT personalizado** (si tienen ChatGPT Plus) o usan **Claude** con el prompt copiado.
- Suben el documento de preguntas frecuentes como archivo de conocimiento.
- Prueban: hacen 3 preguntas y ajustan el prompt si es necesario.

### **Paso 4: Conecta a un canal (15 min)**
- Opción A (fácil): **Comparten el enlace del GPT** para que otros lo prueben.
- Opción B (intermedio): **Usan Zapier** para conectar el asistente a un formulario web (Typeform o Google Forms) que envíe respuestas por email.
- Opción C (avanzado): **Usan Voiceflow** para crear un chatbot embedible en su web (si hay tiempo).

### **Paso 5: Prueba en vivo (10 min)**
- Los asistentes intercambian enlaces con su compañero de mesa y prueban el asistente del otro.
- Dan feedback: ¿Respondió bien? ¿Fue amigable? ¿Qué falta?

---

## 📦 **Recursos para Llevar a Casa**

### **Documento compartido (Google Docs) con:**
1. **Plantilla de prompt** (descargable en .docx)
2. **Guía paso a paso** con capturas de pantalla (PDF)
3. **Enlaces útiles:**
   - ChatGPT: [chat.openai.com](https://chat.openai.com)
   - Claude: [claude.ai](https://claude.ai)
   - Zapier: [zapier.com](https://zapier.com)
   - Make: [make.com](https://make.com)
   - Voiceflow: [voiceflow.com](https://voiceflow.com) (para chatbots visuales)
   - Google Colab: [colab.research.google.com](https://colab.research.google.com) (para código simple)
4. **Lista de 10 prompts avanzados** para mejorar el asistente (ej: "Haz que recuerde conversaciones anteriores", "Responde en tono divertido")
5. **Checklist de lanzamiento:** Pasos para poner el asistente en producción (dominio propio, integración con WhatsApp, análisis de conversaciones)

### **Bonus:**
- **Video de 5 minutos** (grabado antes) con tips para escalar el asistente
- **Grupo de WhatsApp** para dudas post-workshop (opcional)

---

## 📊 **Slide Count Estimado por Sección**

| Bloque | Tema | Slides |
|--------|------|--------|
| 1 | ¿Por qué tu startup necesita un asistente? | 5 slides (historia, demo, estadísticas) |
| 2 | Anatomía de un asistente | 4 slides (diagrama, ejemplos, preguntas) |
| 3 | Ejercicio principal | 8 slides (pasos con capturas) |
| 4 | Automatización | 4 slides (demo, mini-ejercicio) |
| 5 | Presentación y feedback | 2 slides (instrucciones, cronómetro) |
| 6 | Cierre | 3 slides (próximos pasos, recursos, contacto) |
| **Total** | | **26 slides** |

---

## 🔥 **Tips para el Facilitador (Para que el workshop sea inolvidable)**

- **Empieza con una historia personal:** "Yo también pensaba que la IA era solo para ingenieros, hasta que..."
- **Usa el reloj en grande:** Cada bloque tiene tiempo límite. Pon un cronómetro visible.
- **Prepárate para fallos técnicos:** Ten un plan B (ej: si ChatGPT falla, usa Claude o una demo grabada).
- **Fomenta el ruido:** El taller debe sonar a tecleo y risas, no a silencio.
- **Cierra con energía:** "¡Hoy construiste algo que el 90% de los emprendedores no tiene! Ahora ve y hazlo crecer."

---

**¡Listo!** Este outline te dará un workshop dinámico, práctico y memorable. Si necesitas ajustar algún bloque o agregar más detalles, dime.