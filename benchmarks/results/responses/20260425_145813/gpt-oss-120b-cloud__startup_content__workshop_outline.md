# GPT-OSS 120B (Ollama Cloud) — startup_content/workshop_outline

- model_id: `gpt-oss:120b-cloud`
- success: True  | final: 8.15 | quality: 9.72
- latency_total: 28.87s | tokens_per_second: 70.9
- input_tokens: 251 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa

## **Workshop Presencial – 3 horas**  
### “Construye tu Asistente de IA para tu Startup – Workshop Práctico”

> **Público:** Emprendedores early‑stage (no‑técnicos) – 20‑30 personas  
> **Formato:** 100 % presencial, con laptops o tablets (los participantes pueden traer su propio dispositivo).  
> **Objetivo General:** Que cada asistente salga con un prototipo “mínimo viable” (MVP) de un chatbot/assistant basado en IA que pueda integrarse rápidamente a su producto o proceso interno.

---

## 1️⃣ Agenda Detallada (3 h)

| Horario | Bloque | Duración |
|---------|--------|----------|
| **09:00 – 09:15** | **Bienvenida + Ice‑breaker** | 15 min |
| **09:15 – 09:45** | **Bloque 1 – ¿Qué es un Asistente de IA y por qué tu startup lo necesita?** | 30 min |
| **09:45 – 10:25** | **Bloque 2 – Diseño de la conversación (User Journey + Prompt Engineering)** | 40 min |
| **10:25 – 10:35** | **Coffee‑break / Networking** | 10 min |
| **10:35 – 11:35** | **Bloque 3 – Laboratorio práctico: Construye tu propio asistente (no‑code)** | 60 min |
| **11:35 – 11:55** | **Bloque 4 – Test rápido, feedback y próximos pasos** | 20 min |
| **11:55 – 12:00** | **Cierre relámpago & Encuesta** | 5 min |

> **Total:** 180 min (3 h)

---

## 2️⃣ Materiales Necesarios (pre‑work)

| Tipo | Detalle | Responsable |
|------|----------|--------------|
| **Sala** | Sillas en “U” o mesas grupales, proyector, pantalla, pizarra o muro de notas, conexión Wi‑Fi con buena velocidad. | Organizador |
| **Tech** | 1‑2 laptops con acceso a internet (para el facilitador). Cada participante debe traer su propio laptop/tablet (Android/iOS/Windows/macOS). | Participantes |
| **Cuentas** | Registro previo a **ChatGPT/OpenAI Playground**, **Google Cloud (Vertex AI)** o **Microsoft Azure AI** (plan free). Envío de invitación con tutorial de 5 min para crear la cuenta antes del día. | Facilitador |
| **Plantillas** | *Canvas de Prompt* (PDF imprimible), *Checklist de QA*, *Guía de integración* (One‑pager). | Facilitador |
| **Kits de papel** | Post‑its (amarillos y verdes), marcadores, tarjetas de “role‑play”. | Facilitador |
| **Hand‑outs** | Agenda impresa, hoja de “Mi Asistente” (espacio para anotar nombre, objetivo, métricas). | Facilitador |
| **Software no‑code** | Acceso a **Zapier**, **Make (Integromat)** o **Bubble** (plan free) – pre‑configurado con un “Webhook” de OpenAI. | Facilitador (pre‑setup) |
| **Audio** | Micrófono portátil (para preguntas al final). | Facilitador |

---

## 3️⃣ Bloques Detallados

### **Bloque 0 – Bienvenida + Ice‑breaker (15 min)**
| Elemento | Detalle |
|---------|----------|
| **Objetivo** | Romper la tensión, generar confianza y descubrir rápidamente los sectores de los asistentes. |
| **Dinámica** | Cada participante escribe en un post‑it: *“Mi startup, mi mayor dolor de comunicación”*. Se pegan en la pared y el facilitador lee 2‑3 en voz alta, creando una nube de palabras. |
| **Key Takeaway** | Todos comparten un problema real; el asistente de IA será la solución que vamos a prototipar. |
| **Slides** | 3 (Título, agenda, actividad ice‑breaker). |

---

### **Bloque 1 – ¿Qué es un Asistente de IA y por qué tu startup lo necesita? (30 min)**
| Elemento | Detalle |
|---------|----------|
| **Objetivo** | Entender, en lenguaje sencillo, los conceptos clave: IA generativa, chatbots, “prompt”, “API”, “no‑code”. |
| **Dinámica** | **Charla relámpago (12 min)** + **Demo flash (5 min)** (ejemplo en vivo de un asistente que responde a preguntas de soporte). <br>**Mini‑debate (8 min)**: “¿ChatGPT vs. Bot pre‑programado?” <br>**Poll interactivo (5 min)** usando Mentimeter para medir nivel de confianza antes/después. |
| **Key Takeaway** | La IA no es “magia negra”; con las herramientas correctas puedes lanzar un asistente funcional en < 1 h y sin código. |
| **Slides** | 8–10 (definiciones, casos de uso, arquitectura mínima, mito vs. realidad). |

---

### **Bloque 2 – Diseño de la conversación (User Journey + Prompt Engineering) (40 min)**
| Elemento | Detalle |
|---------|----------|
| **Objetivo** | Aprender a mapear la interacción cliente‑asistente y a redactar prompts claros que entreguen respuestas útiles. |
| **Dinámica** | **Ejercicio grupal (20 min)**: En equipos de 4‑5, usan el *Canvas de Prompt* (pregunta → contexto → formato de respuesta → restricción). Cada equipo elige un caso real de su startup (p.ej., “Agendar demo”, “Responder FAQ de precios”). <br>**Puesta en común (10 min)**: Cada equipo muestra su prompt y recibe retroalimentación rápida. <br>**Mini‑demo (5 min)**: El facilitador muestra cómo ese prompt se prueba en el Playground de OpenAI. <br>**Checklist rápido (5 min)**: “¿Mi prompt está listo?” |
| **Key Takeaway** | Un buen prompt = la mitad del trabajo. Con el canvas, cualquier emprendedor puede crear prompts de calidad en minutos. |
| **Slides** | 12–14 (ejemplos de prompts, canvas, errores comunes, checklist). |

---

### **Bloque 3 – Laboratorio práctico: Construye tu propio asistente (no‑code) (60 min)**
| Elementivo | Detalle |
|------------|----------|
| **Objetivo** | Llevar el prompt a una herramienta no‑code (Zapier/Make) y publicar un chatbot funcional (Web widget o Slack). |
| **Dinámica** | **Paso‑a‑paso guiado (30 min)**: <br>1. Conectar cuenta OpenAI (API key). <br>2. Crear “Zap” → Trigger: formulario Web (Google Form) o mensaje de Slack. <br>3. Acción: “Call OpenAI Completion” con nuestro prompt. <br>4. Acción: devolver respuesta al canal (Web widget, email o Slack). <br>**Hands‑on (25 min)**: Cada participante replica el flujo con su propio prompt y prueba en tiempo real. <br>**Check‑out (5 min)**: “¿Qué funciona? ¿Qué falla? ¿Qué cambiarías?”. |
| **Key Takeaway** | En menos de una hora tienes un asistente conectado a tu propio canal de comunicación. No se necesita programar, solo conectar bloques. |
| **Slides** | 10–12 (diagrama de flujo Zapier/Make, screenshots, tips de depuración). |

---

### **Bloque 4 – Test rápido, feedback y próximos pasos (20 min)**
| Elemento | Detalle |
|----------|----------|
| **Objetivo** | Validar rápidamente el MVP del asistente, recoger feedback y definir la hoja de ruta de mejora. |
| **Dinámica** | **Testing relámpago (8 min)**: Cada equipo hace 2‑3 preguntas al propio asistente (simulación de cliente). <br>**Retroalimentación estructurada (7 min)**: Uso de la plantilla *Checklist de QA* (precisión, tono, tiempo de respuesta). <br>**Roadmap express (5 min)**: Cada participante escribe 3 acciones concretas que hará en la siguiente semana (p.ej., “Añadir FAQ de precios”, “Integrar con Calendly”). |
| **Key Takeaway** | El MVP está listo para iterar. La siguiente fase es **medir** y **optimizar**, no lanzar perfecto. |
| **Slides** | 6 (test script, checklist, roadmap). |

---

## 4️⃣ **Ejercicio Principal – “Mi Asistente en 1 h”**

1. **Definir objetivo** (5 min) – Con el *Canvas de Prompt* el participante escribe: *“¿Qué problema quiero que mi