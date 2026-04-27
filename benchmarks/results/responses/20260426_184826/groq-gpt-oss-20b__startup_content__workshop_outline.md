# GPT-OSS 20B (Groq) — startup_content/workshop_outline

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.15 | quality: 9.44
- latency_total: 2.424s | tokens_per_second: 844.9
- input_tokens: 250 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

## 🎯 **Workshop: “Construye tu Asistente de IA para tu Startup – Workshop Práctico”**  
**Duración total:** 3 h (180 min)  
**Participantes:** 20‑30 emprendedores early‑stage (no técnicos)  
**Formato:** Presencial, energía + hands‑on

---

### 📋 1. Agenda Detallada con Tiempos

| Hora | Bloque | Tiempo | Actividad |
|------|--------|--------|-----------|
| 0:00 – 0:10 | **Welcome & Energizer** | 10 min | Charla breve + dinámica de “2‑min‑talk” para romper el hielo |
| 0:10 – 0:30 | **Visión del Asistente de IA** | 20 min | Charla + demo de casos reales |
| 0:30 – 0:50 | **Ideación de tu Asistente** | 20 min | Brainstorming + matriz de “Problema‑Solución‑Valor” |
| 0:50 – 1:10 | **Selección de Herramientas** | 20 min | Demo de plataformas low‑code + comparativa |
| 1:10 – 1:20 | **Break rápido / Energizer** | 10 min | Snack, estiramientos, música |
| 1:20 – 2:10 | **Construye tu Prototipo** | 50 min | Ejercicio práctico: crear un chatbot en 5 min con Zapier/ChatGPT |
| 2:10 – 2:30 | **Test & Iterate** | 20 min | Test en parejas + feedback rápido |
| 2:30 – 2:50 | **Road‑map & Próximos Pasos** | 20 min | Charla + plantilla de plan de acción |
| 2:50 – 3:00 | **Cierre & Networking** | 10 min | Preguntas, agradecimientos, intercambio de contactos |

---

### 📦 2. Materiales Necesarios (Pre‑Workshop)

| Recurso | Qué preparar / traer |
|---------|----------------------|
| **Laptop con conexión a internet** | ✔️ |
| **Cuenta de OpenAI (o equivalente)** | Regístrate en <https://platform.openai.com/signup> y copia tu API Key |
| **Acceso a Zapier/Make.com** | Crea una cuenta gratuita |
| **Editor de texto (VS Code / Sublime)** | Opcional, para el código mínimo |
| **Google Drive / Dropbox** | Para guardar el “whiteboard” colaborativo |
| **Post‑it, marcadores, rota‑folios** | Para la sesión de ideación |
| **Proyector + pantalla** | Para la presentación |
| **Café, snacks** | Energía extra |

> **Nota:** Si el lugar no dispone de Wi‑Fi fiable, pide a los participantes que descarguen la app de ChatGPT y la app de Zapier para usar offline (solo se necesita conexión al iniciar).

---

### 📑 3. Bloques Detallados

| Bloque | Duración | Objetivo | Dinámica | Key Takeaway | Slides Estimados |
|--------|----------|----------|----------|--------------|------------------|
| **Welcome & Energizer** | 10 min | Romper el hielo y crear energía | “2‑min‑talk”: cada participante se presenta y comparte una palabra que asocie con IA | *La IA no es un misterio; es una herramienta que todos podemos usar* | 3 |
| **Visión del Asistente de IA** | 20 min | Entender el valor y casos de uso | Charla + demo rápido (ChatGPT + Zapier) | *Un asistente de IA puede escalar tu startup sin contratar más gente* | 5 |
| **Ideación de tu Asistente** | 20 min | Definir el problema y la propuesta de valor | Brainstorming en grupos + matriz “Problema‑Solución‑Valor” | *El asistente debe resolver un dolor real de tu cliente* | 5 |
| **Selección de Herramientas** | 20 min | Elegir la stack más accesible | Demo de Zapier, Make.com y “ChatGPT API + LangChain” (si hay tiempo) | *Puedes crear un asistente sin escribir 100 líneas de código* | 5 |
| **Construye tu Prototipo** | 50 min | Crear un MVP funcional | Ejercicio práctico en parejas: 5 min de configuración + 35 min de “drag‑and‑drop” + 10 min de test | *El prototipo es la base para iterar y validar* | 8 |
| **Test & Iterate** | 20 min | Validar y recopilar feedback | Pruebas en parejas + “speed‑feedback” de 1 min cada una | *El feedback rápido acelera la mejora* | 4 |
| **Road‑map & Próximos Pasos** | 20 min | Planificar la siguiente fase | Charla + plantilla de hoja de ruta (Kick‑off, MVP, beta, escala) | *Tienes un plan claro para llevarlo a producción* | 4 |
| **Cierre & Networking** | 10 min | Consolidar aprendizajes y conectar | Preguntas abiertas + intercambio de contactos | *Conectarte con otros emprendedores acelera el crecimiento* | 0 |

> **Tip de presentación:** Mantén cada slide con *máx. 3 líneas de texto*, 1 imagen o icono, y 1 “punto clave” que resuma el mensaje.

---

### 🛠️ 4. Ejercicio Principal del Workshop

**“Construye tu Asistente de IA en 5 min”**

1. **Define la tarea** (ej.: responder preguntas frecuentes sobre tu producto).  
2. **Crea un flujo** en Zapier:  
   - Trigger: “Webhooks by Zapier – Catch Hook” (para recibir mensajes).  
   - Action: “ChatGPT – Send Prompt” (usa tu API Key).  
   - Action: “Webhooks – POST” (para enviar la respuesta al canal de tu elección: Slack, WhatsApp, email).  
3. **Prueba** enviando un mensaje a tu Webhook y observa la respuesta.  
4. **Itera**: ajusta la prompt, añade condiciones (if‑then), y prueba de nuevo.  

> **Resultado esperado:** Cada pareja tendrá un asistente funcional que responde a una pregunta sencilla. Se guarda el Zap y el script para usarlo después.

---

### 📚 5. Recursos para Llevar a Casa

| Tipo | Enlace / Descripción |
|------|----------------------|
| **Plantilla de Canvas** | PDF descargable: “Asistente de IA Canvas” |
| **Cheat Sheet** | “Prompt Engineering 101” (PDF) |
| **Tutoriales en vídeo** | Canal de YouTube: “AI for Startups” (playlist de 5‑min demos) |
| **Repositorios de código** | GitHub: `starter-ai-assistant` (ejemplo con LangChain + FastAPI) |
| **Comunidades** | Slack: #ai-entrepreneurs, Discord: AI Startups |
| **API Docs** | OpenAI: <https://platform.openai.com/docs> |
| **Herramientas gratuitas** | Zapier, Make.com, Google Apps Script |

> **Tip:** Anima a los asistentes a crear un “repo” de GitHub con su prototipo y compartirlo en la comunidad.

---

### 📊 6. Slide Count Estimado por Sección

| Sección | Slides |
|---------|--------|
| Welcome | 3