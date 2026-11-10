# GPT-OSS 120B — startup_content/workshop_outline

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.81 | quality: 9.72
- latency_total: 41.188s | tokens_per_second: 68.2
- input_tokens: 250 | output_tokens: 2811
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un facilitador de workshops de emprendimiento y tecnologia con experiencia en Latinoamerica.

**user:**

Crea el outline completo para un workshop presencial de 3 horas titulado:
"Construye tu Asistente de IA para tu Startup - Workshop Practico"

La audiencia son emprendedores early-stage no-tecnicos (20-30 personas).

Incluye:
1. Agenda detallada con tiempos (3 horas)
2. Materiales necesarios (que preparar antes)
3. Para cada bloque:
   - Titulo y duracion
   - Objetivo
   - Dinamica (charla, ejercicio, demo, discusion)
   - Key takeaway
4. Ejercicio principal del workshop (que todos puedan hacer)
5. Recursos para llevar a casa
6. Slide count estimado por seccion

El tono debe ser energico y practico, no academico.


## Respuesta completa

## **Workshop Presencial – 3 horas**  
**Título:** **“Construye tu Asistente de IA para tu Startup – Workshop Práctico”**  
**Audiencia:** Emprendedores early‑stage (no‑técnicos) – 20‑30 personas  
**Objetivo General:** Que cada participante salga con un prototipo “mínimo viable” (MVP) de un asistente de IA (chatbot, generador de texto o analizador de datos) que pueda integrarse rápidamente a su negocio y con una hoja de ruta clara para escalarlo.

---

## 1️⃣ Agenda Detallada (180 min)

| Tiempo | Bloque | Tipo |
|--------|--------|------|
| **0:00 – 0:10** | **Bienvenida & Warm‑up** | Dinámica rápida + presentación |
| **0:10 – 0:30** | **Bloque 1 – IA en los negocios** | Charla + ejemplos |
| **0:30 – 0:55** | **Bloque 2 – Arquitectura “Low‑Code” de un asistente** | Demo + discusión |
| **0:55 – 1:25** | **Bloque 3 – Manos‑a‑la‑obra: Construye tu primer flujo** | Ejercicio guiado (todos) |
| **1:25 – 1:35** | **Break “Coffee & Networking”** | Café + intercambio de ideas |
| **1:35 – 2:05** | **Bloque 4 – Personaliza y entrena tu IA** | Taller práctico + Q&A |
| **2:05 – 2:30** | **Bloque 5 – Testea, lanza y mide** | Simulación de pruebas + métricas |
| **2:30 – 2:50** | **Bloque 6 – Roadmap y próximos pasos** | Discusión grupal + plan de acción |
| **2:50 – 3:00** | **Cierre & Feedback** | Encuesta relámpago + entrega de recursos |

---

## 2️⃣ Materiales Necesarios (pre‑work)

| Tipo | Qué preparar | Responsable |
|------|--------------|--------------|
| **Sala** | Sillas en “U” o mesas grupales, proyector, pantalla, pizarra/flipchart, conexión Wi‑Fi (SSID y contraseña visibles) | Organizador |
| **Tecnología** | 1‑2 laptops con acceso a internet por facilitador, **cuentas demo** en: <br>• **ChatGPT (OpenAI)** o **Claude (Anthropic)** <br>• **Zapier / Make (Integromat)** <br>• **Google Sheets** <br>• **Notion/ Coda** (para bases de conocimiento) <br>• **Voiceflow** (si se quiere voz) | Facilitador + IT |
| **Plantillas** | - Guía paso‑a‑paso (PDF) <br>- Canvas “IA‑Assistant Business Model” <br>- Checklist de pruebas <br>- Lista de prompts de referencia | Facilitador |
| **Material impreso** | Post‑its, marcadores, lápices, hojas de papel kraft (para brainstorming) | Equipo de logística |
| **Software de votación** | Mentimeter / Slido (para encuestas rápidas) | Facilitador |
| **Café & Snacks** | Agua, café, té, galletas, fruta | Organización del evento |
| **Acceso a APIs** | Clave API de OpenAI (plan gratuito) y de Zapier (plan trial) – crear cuentas antes del día y compartir credenciales de demo | Facilitador |

---

## 3️⃣ Detalle de Cada Bloque

### **Bloque 0 – Bienvenida & Warm‑up (10 min)**
- **Objetivo:** Romper el hielo, generar energía y alinear expectativas.  
- **Dinámica:** “Elevator Pitch 30” – Cada asistente tiene 30 segundos para contar qué hace su startup y qué problema le gustaría que el asistente resolviera.  
- **Key Takeaway:** “Todos aquí tienen una necesidad concreta que IA puede atacar”.  

---

### **Bloque 1 – IA en los Negocios (20 min)**
- **Objetivo:** Mostrar, en lenguaje simple, cómo la IA está transformando startups (ventas, soporte, contenido, análisis).  
- **Dinámica:** Charla rápida (10 min) + 3 casos de estudio locales (5 min) + mini‑encuesta en Mentimeter (5 min).  
- **Key Takeaway:** “La IA no es solo para gigantes; hay “quick‑wins” que cualquier startup puede implementar hoy”.  
- **Slides estimadas:** 8–10  

---

### **Bloque 2 – Arquitectura Low‑Code de un Asistente (25 min)**
- **Objetivo:** Que los participantes entiendan la estructura básica: **Input → Prompt → Modelo → Output → Acción** y cómo conectarla sin escribir código.  
- **Dinámica:** Demo en vivo (15 min) usando **ChatGPT + Zapier** para crear un “Asistente de FAQ” que responde a preguntas de clientes y envía la respuesta a Slack. Luego, 10 min de Q&A.  
- **Key Takeaway:** “Con 3 bloques (Prompt, Modelo, Acción) puedes crear un asistente funcional”.  
- **Slides estimadas:** 6–8  

---

### **Bloque 3 – Manos‑a‑la‑obra: Construye tu primer flujo (30 min)**
- **Objetivo:** Que cada participante diseñe y pruebe un flujo sencillo de IA que resuelva su caso de uso.  
- **Dinámica:** **Ejercicio guiado** paso a paso (ver detalle en sección 4). Cada 5 min se avanza a la siguiente fase, con facilitadores circulando para ayudar.  
- **Key Takeaway:** “Tienes un prototipo que responde a tu prompt y ejecuta una acción (p.ej., enviar email, generar texto, actualizar hoja)”.  
- **Slides estimadas:** 4–5 (instrucciones visuales)  

---

### **Break – Coffee & Networking (10 min)**
- Espacio para que los emprendedores compartan ideas y hagan preguntas informales.  

---

### **Bloque 4 – Personaliza y entrena tu IA (30 min)**
- **Objetivo:** Enseñar a refinar prompts, añadir contexto y crear “memoria” usando bases de datos simples (Google Sheets).  
- **Dinámica:** Taller práctico: cada equipo agrega 5 “FAQ” propias a una hoja, conecta la hoja a ChatGPT via Zapier y prueba respuestas más precisas.  
- **Key Takeaway:** “Los prompts bien estructurados + datos propios = respuestas a medida”.  
- **Slides estimadas:** 5–6  

---

### **Bloque 5 – Testea, lanza y mide (25 min)**
- **Objetivo:** Introducir pruebas rápidas (A/B de prompts) y métricas básicas (tasa de respuesta correcta, tiempo de respuesta, satisfacción).  
- **Dinámica:** Simulación: los participantes usan un “scorecard” impreso para calificar 3 interacciones del asistente. Luego, discusión de resultados y ajustes.  
- **Key Takeaway:** “Iterar es tan fácil como cambiar un prompt y volver a medir”.  
- **Slides estimadas:** 4–5  

---

### **Bloque 6 – Roadmap y próximos pasos (20 min)**
- **Objetivo:** Que cada asistente salga con un plan de 30‑60‑90 días para escalar su asistente.  
- **Dinámica:** Llenado del **Canvas “IA‑Assistant Roadmap”** (3 columnas: “Primer MVP”, “Iteración 2‑3”, “Escalado”). Trabajo individual + puesta en común rápida (5 min).  
- **Key Takeaway:** “Tienes una hoja de ruta concreta y los recursos para seguir avanzando”.  
- **Slides estimadas:** 6–7  

---

### **Cierre & Feedback (10 min)**
- **Objetivo:** Consolidar aprendizajes y recoger retroalimentación.  
- **Dinámica:** Encuesta en Mentimeter (3 preguntas) + entrega de “Kit de Recursos” (digital).  
- **Key Takeaway:** “No se queda en la teoría; ya tienes herramientas y comunidad”.  
- **Slides estimadas:** 2–3  

---

## 4️⃣ **Ejercicio Principal – “Crea tu Asistente de FAQ en 20 min”**

1. **Formar equipos de 2‑3 personas** (para que haya colaboración y apoyo mutuo).  
2. **Seleccionar un caso de uso** (p.ej., “Responder preguntas de precios”, “Ayudar a agendar citas”, “Generar ideas de contenido”).  
3. **Crear una hoja de Google “FAQ”** con 5‑7 preguntas y respuestas típicas de su negocio.  
4. **Abrir Zapier (o Make)** y crear un Zap:
   - **Trigger:** “New row in Google Sheets”.  
   - **Action 1:** “Send prompt to ChatGPT” (prompt = “Usa la información de la fila para contestar la pregunta del cliente”).  
   - **Action 2:** “Send email / Slack message” con la respuesta generada.  
5. **Probar el flujo** ingresando una nueva pregunta en la hoja; observar la respuesta automática.  
6. **Iterar:** Ajustar el prompt (añadir “si la respuesta no está clara, responde con “Lo siento, no tengo esa información””).  
7. **Documentar** en una hoja de notas: Prompt usado, resultados, mejoras a probar.  

> **Resultado esperado:** Cada equipo tiene un asistente funcional que responde a preguntas de su dominio y entrega la respuesta por el canal que elijan (email, Slack, WhatsApp vía Twilio, etc.).

---

## 5️⃣ **Recursos para Llevar a Casa**

| Tipo | Contenido | Formato |
|------|-----------|---------|
| **Guía paso‑a‑paso** | “Construye tu asistente de FAQ con ChatGPT + Zapier” | PDF (2 pág.) |
| **Plantilla de Prompt** | 10 prompts pre‑diseñados para ventas, soporte, contenido | Google Doc |
| **Canvas “IA‑Assistant Roadmap”** | Hoja de trabajo para plan 30‑60‑90 días | PDF imprimible |
| **Lista de APIs gratuitas** | OpenAI (GPT‑3.5), Cohere, HuggingFace Inference, Zapier free tier | Enlace web |
| **Comunidad** | Invitación a Slack privado “IA‑Startups LATAM” | Enlace de invitación |
| **Vídeo recap** | Grabación de 15 min con los highlights y pasos clave | Link a Google Drive |
| **Checklist de pruebas** | 5 ítems para validar antes de lanzar (prompt, datos, latencia, privacidad) | PDF |

---

## 6️⃣ **Estimado de Slides por Sección**

| Sección | Slides |
|---------|--------|
| Bienvenida & Warm‑up | 2 |
| IA en los negocios | 8‑10 |
| Arquitectura Low‑Code | 6‑8 |
| Manos‑a‑la‑obra (instrucciones) | 4‑5 |
| Personaliza y entrena | 5‑6 |
| Testea, lanza y mide | 4‑5 |
| Roadmap & próximos pasos | 6‑7 |
| Cierre & Feedback | 2‑3 |
| **Total** | **≈ 37‑46 slides** (dependiendo del nivel de detalle visual) |

---

## 🎉 **Tips para Mantener la Energía Alta**

1. **Start with a “rock‑star” demo** – muestra un asistente que responda en tiempo real a una pregunta divertida (p.ej., “¿Cuál es la mejor pizza en la ciudad?”).  
2. **Gamify** – cada equipo gana “puntos IA” por: completar el flujo, mejorar un prompt, presentar su caso de uso. Pequeño premio al final (libro de IA, suscripción trial).  
3. **Micro‑breaks** – cada 25 min invita a estirarse o lanzar una pregunta rápida en Mentimeter para mantener la atención.  
4. **Visual aids** – usa diagramas de flujo simples (caja‑flecha) y colores corporativos de la startup para que el contenido sea memorable.  

---

### ¡Listo!  
Con este outline tendrás todo lo necesario para ejecutar un workshop dinámico, práctico y memorable, que deje a los emprendedores con un prototipo real y una hoja de ruta clara para integrar IA en sus startups. 🚀