# Qwen3-Coder-Next (OpenRouter FP8) — startup_content/workshop_outline

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.63 | quality: 9.28
- latency_total: 13.877s | tokens_per_second: 147.6
- input_tokens: 211 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa

¡Claro! Aquí tienes un **outline completo y listo para ejecutar** para un workshop presencial de **3 horas**, diseñado específicamente para **emprendedores *early-stage* no técnicos** en Latinoamérica — con enfoque práctico, cercano, energético y 100% orientado a la acción.

---

## 🚀 **Workshop: "Construye tu Asistente de IA para tu Startup"**  
**Duración:** 3 horas  
**Audiencia:** 20–30 emprendedores no técnicos (foco en MVP, validación, crecimiento temprano)  
**Tono:** Práctico, divertido, sin jerga técnica innecesaria — como un *cofounder* tech que te ayuda a hacerlo real.

---

## 📋 **1. Agenda Detallada (3 horas)**

| Hora | Bloque | Duración | Modalidad |
|------|--------|----------|-----------|
| 09:00–09:15 | **Arrancamos con fuego: ¿Por qué tu startup *ya* necesita un asistente de IA?** | 15 min | Charla + Encuesta rápida |
| 09:15–09:40 | **El asistente de IA no es magia (es producto)** | 25 min | Charla + Demo interactiva |
| 09:40–10:20 | **Diseña tu asistente en 10 minutos (sin código)** | 40 min | Ejercicio guiado + Herramienta en vivo |
| 10:20–10:35 | *☕️ BREAK* | 15 min | — |
| 10:35–11:15 | **Conecta tu asistente con lo que ya usas (WhatsApp, Notion, Calendly)** | 40 min | Demo + Ejercicio práctico |
| 11:15–11:50 | **Valida, mejora y lanza tu MVP de asistente** | 35 min | Dinámica en parejas + Feedback rápido |
| 11:50–12:00 | **Cierre: Tu primer paso *mañana* (y recursos)** | 10 min | Charla + Entrega de recursos |

---

## 🧰 **2. Materiales necesarios (preparar antes)**

✅ **Para el facilitador:**
- Laptop con conexión a internet estable  
- Proyector + pantalla  
- Cuenta de **Zapier** (o similar) para demo de integración  
- Cuenta en **CrewAI** o **LangChain Studio** (opcional, para demo avanzada)  
- Cuenta en **Botpress Cloud** (gratuita) o **Rasa X** (demo simplificada)  
- **Plantilla Canva** con guía paso a paso para crear el asistente  
- **Google Form** para recoger resultados del ejercicio (opcional, para seguimiento post-workshop)  

✅ **Para los participantes (imprimir o compartir en Google Drive):**
- 1 hoja de **"El Asistente de IA de Tu Startup"** (plantilla visual: *¿Qué hace? ¿Quién lo usa? ¿Dónde vive? ¿Qué aprende?*)  
- Lista de **herramientas sin código recomendadas** (Botpress, Voiceflow, FlowXO, Make, Zapier)  
- Guía rápida: **“3 preguntas para validar tu asistente en 10 minutos”**  
- Enlaces directos a demos funcionales (ej: [demo Botpress en vivo](https://www.botpress.com/demo))  

✅ **Ambientación:**
- Mesas redondas o en islas (para trabajar en equipos de 2–3 personas)  
- Papelógrafo o pizarra blanca digital (Miro/Mural)  
- Marcadores, post-its, stickers 😄  

---

## 🧩 **3. Bloques por bloque: Objetivo, Dinámica y Key Takeaway**

---

### **Bloque 1: Arrancamos con fuego** *(15 min)*  
- **Objetivo:** Romper el miedo a la IA, conectar con su realidad y mostrar valor inmediato.  
- **Dinámica:**  
  - Charla corta (10 min) con historias reales:  
    - *“¿Te pasa que respondes 10 veces lo mismo en DMs? ¿O pierdes horas en onboarding de clientes?”*  
    - Casos reales:  
      - **Fintech colombiana** que redujo un 40% sus respuestas repetidas con un asistente en WhatsApp  
      - **EdTech mexicana** que automatizó el 1er contacto con prospectos usando un asistente en Instagram  
  - Encuesta rápida en vivo (via Mentimeter o emoji reaction): *¿Qué tarea repetitiva te gustaría automatizar primero?*  
- **Key takeaway:**  
  > **“Tu asistente de IA no es un chatbot de ‘Hola, ¿en qué le puedo ayudar?’. Es tu *cofunder virtual* para escalar sin crecer tu carga mental.”**

---

### **Bloque 2: El asistente de IA no es magia (es producto)** *(25 min)*  
- **Objetivo:** Desmitificar la IA, enfocarse en *producto*, no en tecnología.  
- **Dinámica:**  
  - Demo **interactiva** (15 min):  
    - Mostrar un asistente funcional (ej: Botpress en modo *demo*) que ya está entrenado con un flujo real:  
      > *“Quiero saber si soy elegible para el programa de aceleración”* → El asistente responde con reglas claras, pregunta si quiere agendar, y envía datos a Notion.  
  - Análisis visual del “mapa del asistente” (10 min):  
    - Diagrama sencillo en pizarra:  
      `Entrada → Intención → Acción → Salida`  
      (sin mencionar NLU, LLM, etc.)  
- **Key takeaway:**  
  > **“No necesitas entender cómo funciona la IA. Solo necesitas definir: 1) qué pregunta recibes, 2) qué respuesta debes dar, 3) qué acción disparar. Eso es tu MVP de asistente.”**

---

### **Bloque 3: Diseña tu asistente en 10 minutos (sin código)** *(40 min)*  
- **Objetivo:** Que *todos* salgan con un prototipo funcional de su asistente.  
- **Dinámica:**  
  - **Ejercicio guiado en parejas o individuales** (35 min):  
    - Usando **Botpress Cloud (versión gratuita)** o **Voiceflow (modo ‘quick build’)**:  
      1. Crear cuenta en <2 min  
      2. Elegir canal (WhatsApp, Web, Telegram)  
      3. Definir 3 frases clave (ej: “Quiero saber precios”, “Quiero agendar”, “¿Tienen descuentos?”)  
      4. Mapear respuestas y acciones (ej: responder con link de Calendly)  
    - El facilitador circula ayudando con “shortcuts”:  
      > *“No necesitas 20 respuestas. Empieza con 3. Si no funciona, cambias 1 frase y listo.”*  
  - Demo de “cómo probarlo” (5 min):  
    - Enviar mensaje desde WhatsApp real al número de prueba del asistente.  
- **Key takeaway:**  
  > **“Hoy salís con un MVP funcional. No con un MVP perfecto. Con uno que *ya resuelve un problema que tienes hoy*.”**

---

### **☕️ BREAK (15 min)**  
- Snacks locales + música relajada  
- Pizarra con pregunta: *“¿Qué fue lo más útil hasta ahora?”* (para retroalimentación rápida)  

---

### **Bloque 4: Conecta tu asistente con lo que ya usas** *(40 min)*  
- **Objetivo:** Mostrar cómo el asistente se vuelve *operativo* al conectarse con su stack actual.  
- **Dinámica:**  
  - Demo en vivo (15 min):  
    - Asistente recibe mensaje → Dispara Zapier → Crea contacto en CRM (ej: HubSpot) + Envía email de bienvenida + Agrega a lista de WhatsApp.  
    - Usar **Make (Integromat)** o **Zapier** con plantillas precreadas (para facilitar).  
  - Ejercicio práctico (25 min):  
    - Cada equipo elige **una herramienta que ya usa** (Google Sheets, Calendly, Notion, Trello, Airtable) y conecta su asistente a ella.  
    - Plantilla visual:  
      > *“Mi asistente