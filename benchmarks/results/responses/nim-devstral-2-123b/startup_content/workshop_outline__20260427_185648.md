# Devstral 2 123B (NIM) — startup_content/workshop_outline

- model_id: `mistralai/devstral-2-123b-instruct-2512`
- success: True  | final: 7.2 | quality: 9.44
- latency_total: 65.546s | tokens_per_second: 31.2
- input_tokens: 195 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

**🚀 Workshop: "Construye tu Asistente de IA para tu Startup - Taller Práctico"**
*(Para emprendedores early-stage NO técnicos | 3 horas | 20-30 personas)*

---

### **📌 Agenda Detallada**
**Duración total:** 3 horas (con 1 break de 10 min).

| **Bloque**               | **Duración** | **Dinámica**          |
|--------------------------|-------------|-----------------------|
| **1. Bienvenida & Calentamiento** | 15 min      | Charla + Icebreaker   |
| **2. ¿Por qué tu startup necesita IA?** | 20 min      | Charla + Ejemplo real |
| **3. Demo en Vivo: Asistente de IA en acción** | 20 min      | Demo interactiva      |
| **4. Ejercicio Práctico: "Crea tu primer asistente"** | 60 min      | Hands-on (grupos)     |
| **5. Break + Networking** | 10 min      | Café y conexión       |
| **6. Escala tu asistente: Tips para no-morir en el intento** | 25 min      | Charla + Q&A          |
| **7. Cierre: Recursos y próximos pasos** | 10 min      | Discusión + Feedback  |

---

### **🎒 Materiales Necesarios (Preparar antes)**
**Para el facilitador:**
- Laptop + proyector (con acceso a internet estable).
- Cuenta en herramientas NO-CODE de IA (ej: [Voiceflow](https://www.voiceflow.com/), [Landbot](https://landbot.io/), o [ManyChat](https://manychat.com/) con integración de IA).
- Slides (ver sección de *Slide count*).
- Ejemplo pre-construido de un asistente de IA (ej: chatbot para reservas, soporte al cliente, o lead qualification).
- Lista de *prompts* útiles para startups (ej: "Genera 3 respuestas para un cliente enojado").
- Premium accounts para herramientas (si hay demo con límites).

**Para los participantes:**
- Laptop o tablet (obligatorio).
- Cuenta creada en la herramienta NO-CODE seleccionada (enviar instrucciones antes).
- Hoja de trabajo impresa/digital con:
  - Plantilla de "Personas de tu cliente" (para definir el tono del asistente).
  - Checklist de pasos para construir el asistente.
- Stickers o tarjetas para dinámicas de votación (opcional).

---

### **🔍 Detalle por Bloque**

#### **1. Bienvenida & Calentamiento** *(15 min)*
- **Objetivo:** Romper el hielo, alinear expectativas y energizar al grupo.
- **Dinámica:**
  - *Icebreaker:* "En 1 palabra, ¿qué problema de tu startup te quita el sueño?" (todos gritan su respuesta).
  - Charla relámpago: "IA no es magia, es tu nuevo employee #1".
  - Slide: "3 mitos de la IA para startups" (ej: "Necesitas ser técnico", "Es muy caro").
- **Key takeaway:** "Hoy vas a salir con un asistente de IA funcional, aunque no sepas código".
- **Slides:** 3-5.

---

#### **2. ¿Por qué tu startup necesita IA?** *(20 min)*
- **Objetivo:** Mostrar casos reales donde la IA resuelve problemas de startups early-stage.
- **Dinámica:**
  - Charla con ejemplos locales (Latam):
    - *Ejemplo 1:* Chatbot de WhatsApp para agendar citas (salón de belleza en México).
    - *Ejemplo 2:* Asistente para filtrar leads en un marketplace (Colombia).
    - *Ejemplo 3:* Generador de contenido para redes sociales (Argentina).
  - Mini-ejercicio: "Identifica 1 tarea repetitiva en tu startup que podrías automatizar".
- **Key takeaway:** "La IA no reemplaza tu trabajo, te ayuda a escalar lo que ya haces".
- **Slides:** 8-10.

---

#### **3. Demo en Vivo: Asistente de IA en acción** *(20 min)*
- **Objetivo:** Mostrar que construir un asistente es más fácil de lo que parece.
- **Dinámica:**
  - Demo en tiempo real usando una herramienta NO-CODE (ej: Voiceflow):
    1. Crear un flujo básico: "Bienvenida + pregunta frecuente + derivación a humano".
    2. Integrar IA (ej: usar la API de OpenAI para generar respuestas dinámicas).
    3. Probar el asistente en el celular de un voluntario (¡siempre sale algo gracioso!).
  - Pregunta al público: "¿Qué le faltaría a este asistente para ser útil en tu negocio?".
- **Key takeaway:** "Con herramientas visuales, cualquier persona puede prototipar un asistente en 1 hora".
- **Slides:** 5 (solo para apoyar la demo).

---

#### **4. Ejercicio Práctico: "Crea tu primer asistente"** *(60 min)*
**🎯 Ejercicio principal del workshop:**
*"Diseña un asistente de IA que resuelva 1 problema específico de tu startup en 1 hora"*.

**Pasos:**
1. **Define el problema** (10 min):
   - En grupos de 2-3, escriban en un post-it: "Mi asistente va a resolver [problema] para [cliente]".
   - Ejemplos: "Responder dudas de precios en mi e-commerce", "Agendar citas para mi consultorio".

2. **Diseña el flujo** (20 min):
   - Usando la herramienta NO-CODE, creen un flujo de 3-5 pasos:
     - Bienvenida (ej: "Hola, soy [Nombre], ¿en qué te ayudo?").
     - 1-2 preguntas/respuestas clave (ej: "¿Qué producto te interesa?").
     - Cierre (ej: "Te paso con un humano" o "¡Listo, tu cita está agendada").

3. **Integra IA** (15 min):
   - Usar un *prompt* predefinido para generar respuestas automáticas (ej: en Voiceflow + OpenAI).
   - *Tip:* "Si no sabes qué escribir, copia y pega este prompt: *‘Actúa como un asistente amable de [tu industria]. Responde en menos de 2 líneas: [pregunta del cliente]’*".

4. **Prueba y feedback** (15 min):
   - Cada grupo prueba su asistente con otro equipo.
   - Votan: "¿Qué asistente resolvería un problema real HOY?".

**Key takeaway:** "No necesitas perfección, necesitas un MVP que funcione y aprenda de tus clientes".
**Slides:** 0 (solo guía impresa/digital).

---

#### **5. Break + Networking** *(10 min)*
- **Objetivo:** Oxigenar y conectar a los participantes.
- **Dinámica:**
  - Café + música.
  - Tarjetas con preguntas para romper el hielo: "¿Qué asistente te sorprendió más?".

---

#### **6. Escala tu asistente: Tips para no-morir en el intento** *(25 min)*
- **Objetivo:** Dar consejos prácticos para evitar frustraciones comunes.
- **Dinámica:**
  - Charla con *do’s and don’ts*:
    - **DO:** Empieza con 1 solo canal (ej: WhatsApp o web).
    - **DON’T:** Intentes automatizar el 100% (siempre deja una salida a humano).
  - Demo rápida de cómo medir métricas simples (ej: % de preguntas resueltas sin humano).
  - Q&A: "Pregúntame lo que Google no te supo responder".
- **Key takeaway:** "Escala cuando tu asistente ya resuelva el 80% de las consultas básicas".
- **Slides:** 5-7.

---

#### **7. Cierre: Recursos y próximos pasos** *(10 min)*
- **Objetivo:** Dejar a los participantes con herramientas accionables.
- **Dinámica:**
  - **Recursos para llevar a casa:**
    - Lista de herramientas NO-CODE (gratis y de pago).
    - Plantilla de *prompts* para startups (ej: atención al cliente, ventas, soporte técnico).
    - Comunidad de Slack/Telegram para seguir aprendiendo (creada por el facilitador).
  - *Compromiso público:* "¿Quién se compromete a lanzar su asistente en 1 semana?" (levantar la mano).
  - Feedback rápido: "1 cosa que te llevas + 1 cosa que mejoraría del taller".
- **Slides:** 3.

---

### **📦 Recursos para Llevar a Casa**
1. **Guía PDF:** "Pasos para lanzar tu asistente de IA en 7 días".
2. **Plantillas