# GPT-OSS 120B — startup_content/workshop_outline

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.61 | quality: 9.56
- latency_total: 43.773s | tokens_per_second: 46.8
- input_tokens: 247 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que proporciona una guía práctica para emprendedores no técnicos, aunque podría profundizar un poco más en algunos aspectos técnicos.

## Respuesta completa

## **Workshop Presencial (3 h) – “Construye tu Asistente de IA para tu Startup”**  
**Audiencia:** Fundadores y co‑fundadores early‑stage (no‑técnicos) – 20‑30 personas  
**Formato:** Híbrido “hands‑on” + charlas breves + tiempo para networking  
**Objetivo General:** Que cada participante salga con **un prototipo funcional (mínimo viable) de asistente IA** (chatbot / voz) listo para probar con sus propios clientes y con una hoja de ruta clara para escalarlo.

---

## 1️⃣ Agenda Detallada (180 min)

| Tiempo | Bloque | Tipo |
|--------|--------|------|
| **0:00 – 0:10** | **Bienvenida & Warm‑up** | Ice‑breaker rápido |
| **0:10 – 0:30** | **Bloque 1 – IA en acción: casos reales** | Charla + discusión |
| **0:30 – 0:55** | **Blo Bloque 2 – Arquitectura “no‑code” de un asistente** | Demo + Q&A |
| **0:55 – 1:05** | **Break “Café‑Tech”** | Networking |
| **1:05 – 1:45** | **Bloque 3 – Manos a la obra: crear tu asistente** | Taller guiado (ejercicio principal) |
| **1:45 – 2:00** | **Bloque 4 – Entrenamiento rápido: darle personalidad** | Mini‑lab + feedback |
| **2:00 – 2:15** | **Bloque 5 – Testeo con usuarios reales (role‑play)** | Simulación + retroalimentación |
| **2:15 – 2:30** | **Bloque 6 – Roadmap y métricas de éxito** | Charla + plantilla descargable |
| **2:30 – 2:45** | **Q&A abierto + “Pitch‑Flash” de ideas** | Dinámica de grupo |
| **2:45 – 3:00** | **Cierre, entrega de recursos y foto grupal** | Cierre energético |

> **Total:** 180 min (3 h)

---

## 2️⃣ Materiales Necesarios (pre‑work)

| Elemento | ¿Quién lo prepara? | Detalle |
|----------|-------------------|---------|
| **Sala** | Organizador | Sillas en “U” o mesas estilo coworking, proyector, pantalla, wifi estable, enchufes accesibles. |
| **Kits “IA‑Starter”** | Facilitador + asistente técnico | Cada participante recibe: <br>• Laptop (o se pide que traiga la suya) <br>• Acceso a cuentas gratuitas de **Zapier**, **Make (Integromat)**, **ChatGPT (OpenAI)**, **Google Sheets** <br>• QR o link a carpeta de Google Drive con slides, plantillas y cheatsheets. |
| **Plantilla “Prompt Canvas”** | Facilitador | PDF imprimible (A4) con secciones: objetivo, tono, ejemplos de preguntas, respuestas esperadas. |
| **Guía paso‑a‑paso (PDF)** | Facilitador | Instrucciones breves para conectar Zapier → OpenAI → Slack/WhatsApp/Web. |
| **Post‑its, marcadores, flip‑chart** | Facilitador | Para actividades de brainstorming y feedback. |
| **Feedback Form (Google Forms)** | Facilitador | Envío al final para medir satisfacción. |
| **Snacks + café** | Organizador | Para los 10 min de break. |

---

## 3️⃣ Detalle de Cada Bloque

### **Bloque 0 – Warm‑up (10 min)**
- **Objetivo:** Romper el hielo, crear energía grupal y alinear expectativas.  
- **Dinámica:** Cada participante dice su nombre, sector de su startup y **una frase “quiero que mi IA haga X”** (30 s).  
- **Key Takeaway:** Todos comparten una visión concreta de uso de IA; ya se generan ideas para el ejercicio final.  
- **Slides:** 2 (agenda, reglas de juego)

---

### **Bloque 1 – IA en acción: casos reales (20 min)**
- **Objetivo:** Mostrar, en 3‑4 minutos cada caso, cómo startups similares usan asistentes IA para ventas, soporte y operaciones.  
- **Dinámica:** Mini‑presentación con screenshots + 5 min de “speed‑round” donde el público vota su caso favorito (Mentimeter).  
- **Key Takeaway:** Ver que **no se necesita código** para entregar valor inmediato.  
- **Slides:** 6 (3 casos + beneficios + voting)

---

### **Bloque 2 – Arquitectura “no‑code” de un asistente (25 min)**
- **Objetivo:** Entender los bloques básicos: *Trigger → LLM (prompt) → Acción* (ej. crear lead en CRM).  
- **Dinámica:** Demo en vivo (Zapier + OpenAI) + esquema visual en la pantalla. Se muestra cómo conectar: **Google Form → Zapier → ChatGPT → Slack**.  
- **Key Takeaway:** Tener un “diagrama de flujo” listo para replicar con su propio caso.  
- **Slides:** 8 (arquitectura, componentes, demo paso‑a‑paso, checklist)

---

### **Break “Café‑Tech” (10 min)**
- Networking rápido, intercambio de tarjetas, preguntas informales.

---

### **Bloque 3 – Manos a la obra: crear tu asistente (40 min)**
- **Objetivo:** Cada participante construye su propio asistente mínimo viable (MVP) usando la plantilla “Prompt Canvas”.  
- **Dinámica:**  
  1. **5 min** – Repaso rápido de la plantilla.  
  2. **15 min** – Trabajo individual (llenar Canvas y crear Zap en Zapier).  
  3. **15 min** – “Buddy check”: parejas revisan el flujo del otro y dan 2 mejoras.  
  4. **5 min** – Compartir 2‑3 flujos destacados en pantalla.  
- **Key Takeaway:** Salir con **un Zap activo** que responde a un prompt y envía la respuesta a un canal (Slack/WhatsApp/web).  
- **Slides:** 5 (instrucciones paso‑a‑paso, ejemplos de Canvas)

---

### **Bloque 4 – Entrenamiento rápido: darle personalidad (15 min)**
- **Objetivo:** Afinar el tono y la precisión del asistente mediante *prompt engineering* básico.  
- **Dinámica:** Mini‑lab: en grupos de 4, prueban 3 variaciones de prompt (formal, friendly, técnico) y anotan la respuesta más útil. Luego cada grupo comparte su “prompt ganador”.  
- **Key Takeaway:** Un buen prompt = mejor experiencia de usuario; la plantilla de prompts será su “cheat‑sheet”.  
- **Slides:** 4 (principios de prompt, tabla de pruebas, cheat‑sheet)

---

### **Bloque 5 – Testeo con usuarios reales (role‑play) (15 min)**
- **Objetivo:** Validar el asistente con un “cliente ficticio” y detectar fallos de usabilidad.  
- **Dinámica:**  
  1. **5 min** – Escenario de role‑play (un cliente llama al asistente).  
  2. **5 min** – Cada equipo prueba el asistente de otro equipo (intercambio de laptops).  
  3. **5 min** – Feedback rápido (¿Entendió? ¿Fue útil?).  
- **Key Takeaway:** La iteración es clave; se identifican los 3 “puntos de dolor” a corregir antes del lanzamiento.  
- **Slides:** 3 (instrucciones del role‑play, checklist de test, ejemplos de feedback)

---

### **Blo Bloque 6 – Roadmap y métricas de éxito (15 min)**
- **Objetivo:** Definir los próximos pasos y cómo medir el impacto del asistente.  
- **Dinámica:** Presentación de una **plantilla de roadmap 30‑60‑90 días** + indicadores (NPS, tiempo de respuesta, leads generados). Los participantes rellenan su propia hoja (digital).  
- **Key Takeaway:** Tener un plan de acción concreto y métricas para presentar a inversionistas o al equipo.  
- **Slides:** 6 (roadmap, KPIs, ejemplos de OKR)

---

### **Bloque 7 – Q&A abierto + “Pitch‑Flash” (15 min)**
- **Objetivo:** Resolver dudas y practicar un pitch relámpago de 1 min sobre su asistente.  
- **Dinámica:** Preguntas rápidas (modo “fire‑ball”) y luego cada participante lanza su pitch; los demás votan con stickers de “👍”.  
- **Key Takeaway:** Claridad para comunicar valor de IA en menos de 60 s.  
- **Slides:** 2 (instrucciones de pitch, tabla de votos)

---

### **Cierre (15 min)**
- **Objetivo:** Consolidar aprendizajes, entregar recursos y crear comunidad.  
- **Dinámica:** Recapitulación rápida,