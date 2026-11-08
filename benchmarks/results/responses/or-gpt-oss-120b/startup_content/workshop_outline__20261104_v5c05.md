# GPT-OSS 120B — startup_content/workshop_outline

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.35 | quality: 9.56
- latency_total: 135.049s | tokens_per_second: 26.4
- input_tokens: 237 | output_tokens: 3567
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada, materiales necesarios y un ejercicio práctico.

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

## Workshop presencial (3 h)  
**Título:** **“Construye tu Asistente de IA para tu Startup – Workshop Práctico”**  
**Audiencia:** Emprendedores early‑stage sin experiencia técnica (20‑30 personas)  
**Formato:** Energético, “hands‑on”, con mucha interacción y resultados visibles al final.

---

## 1️⃣ Agenda detallada (180 min)

| Tiempo | Bloque | Tipo |
|--------|--------|------|
| **0‑15 min** | Bienvenida + Contexto | Charla + dinámica ice‑breaker |
| **15‑40 min** | 1️⃣ ¿Qué es un asistente de IA y por qué tu startup lo necesita? | Charla + mini‑debate |
| **40‑60 min** | 2️⃣ Define el caso de uso de tu asistente | Ejercicio grupal (canvas) |
| **60‑90 min** | 3️⃣ Herramientas “no‑code” para crear asistentes (Landbot, ChatGPT + Zapier, Voiceflow…) | Demo + preguntas |
| **90‑95 min** | **Break 5 min** – café, networking | – |
| **95‑155 min** | 4️⃣ **Ejercicio principal:** Construye tu propio asistente (paso a paso) | Hands‑on guiado + trabajo en parejas |
| **155‑165 min** | 5️⃣ Testea, recibe feedback y planifica los próximos pasos | Prueba rápida + discusión |
| **165‑180 min** | Cierre, recursos para llevar a casa & Q&A | Charla final + entrega de material |

---

## 2️⃣ Materiales necesarios (preparar con antelación)

| Qué | Para quién | Cómo prepararlo |
|-----|-----------|-----------------|
| **Sala** | Todos | Sillas en “U” o mesas grupales, proyector, pantalla, pizarra + marcadores, sonido. |
| **Conexión Wi‑Fi** | Todos | SSID visible, contraseña en la mesa de registro. |
| **Laptop o tablet** | Cada participante | Pedir que traigan su propio equipo; verificar que tengan navegador actualizado. |
| **Cuentas pre‑creadas (gratuitas)** | Cada participante | - **Landbot** (plan free) <br> - **Zapier** (plan free) <br> - **OpenAI** (API‑key de prueba) <br> Enviar los accesos 24 h antes. |
| **Plantilla “Canvas de Asistente”** | Todos | PDF de una hoja A4 con secciones: objetivo, usuario, flujo principal, tono, métricas. |
| **Guía de prompts** | Todos | PDF con ejemplos de prompts para ChatGPT (saludo, FAQ, captura datos). |
| **Kit de stickers & post‑its** | Grupos | Para brainstorming y votaciones. |
| **Handout “Roadmap post‑workshop”** | Todos | Checklist de 7 pasos para lanzar el asistente. |
| **Cables y adaptadores** | Todos | Verificar que haya suficientes enchufes y cables de carga. |

---

## 3️⃣ Bloques de contenido (detallados)

### **Bloque 0 – 0‑15 min**  
**Título:** *Arranque energético*  
**Objetivo:** Romper el hielo, crear comunidad y alinear expectativas.  
**Dinámica:**  
- 2 min: Bienvenida relámpago (presentación del facilitador).  
- 5 min: Ice‑breaker “Pitch de 30 s”: cada participante menciona su startup y un reto de atención al cliente.  
- 8 min: Mini‑charla “¿Por qué los asistentes de IA son el nuevo super‑poder de una startup?” (slides 1‑5).  
**Key Takeaway:** *Un asistente bien diseñado puede ahorrar hasta 30 % del tiempo de atención al cliente y abrir nuevos canales de venta.*  

---

### **Bloque 1 – 15‑40 min**  
**Título:** *IA en 5 minutos: conceptos sin tecnicismos*  
**Objetivo:** Que todos comprendan, en lenguaje cotidiano, qué es un modelo de lenguaje y cómo “habla” con los usuarios.  
**Dinámica:**  
- 10 min: Charla visual (slides 6‑14) con analogías (ej. “ChatGPT = un chef que sigue recetas de prompts”).  
- 5 min: Preguntas rápidas vía Mentimeter (¿Qué te asusta de la IA? ¿Qué te emociona?).  
- 5 min: Mini‑debate en parejas: “¿En qué parte de mi negocio podría usar un asistente?” (post‑it en la pizarra).  
**Key Takeaway:** *La IA no es magia; es una herramienta que responde a instrucciones claras (prompts) y puede integrarse a cualquier flujo.*  

---

### **Bloque 2 – 40‑60 min**  
**Título:** *Diseña tu caso de uso*  
**Objetivo:** Transformar la idea vaga de “quiero un chatbot” en un caso de uso concreto y medible.  
**Dinámica:**  
- 2 min: Explicación del “Canvas de Asistente” (slide 15).  
- 13 min: Trabajo en grupos de 4‑5 personas (canvas en PDF). Cada grupo define:  
  1. Usuario objetivo.  
  2. Problema que soluciona.  
  3. Flujo principal (3‑4 pasos).  
  4. Métrica de éxito (ej. “% de leads calificados”).  
- 5 min: Cada grupo comparte su canvas (post‑it en la pared).  
**Key Takeaway:** *Un caso de uso bien definido es la brújula que guiará la construcción del asistente.*  

---

### **Bloque 3 – 60‑90 min**  
**Título:** *Toolbox no‑code: elige tu motor*  
**Objetivo:** Presentar 2‑3 plataformas sin código que permiten crear asistentes sin escribir una sola línea de código.  
**Dinámica:**  
- 20 min: Demo “Landbot + OpenAI” (slides 16‑23) – creación de un bloque de “FAQ”.  
- 10 min: Demo “Zapier + ChatGPT” (slides 24‑30) – conectar formulario de captura a respuesta automática.  
- 5 min: Comparativa rápida (tabla de precios, limitaciones, tiempo de puesta en marcha).  
- 0 min: Preguntas‑respuesta en tiempo real (chat de la sala).  
**Key Takeaway:** *Con una cuenta gratuita puedes lanzar un prototipo funcional en menos de 30 min.*  

---

### **Break – 90‑95 min**  
Café, networking y recarga de energía.  

---

### **Bloque 4 – 95‑155 min**  
**Título:** *Manos a la obra: construye tu propio asistente*  
**Objetivo:** Que cada participante tenga **un prototipo funcional** al final del workshop.  
**Dinámica paso‑a‑paso (30 min de guía + 25 min de construcción + 5 min de puesta en marcha):**  

| Paso | Acción | Herramienta | Tiempo |
|------|--------|------------|--------|
| 1️⃣ | Crear bot en **Landbot** → “Nuevo proyecto” | Landbot | 5 min |
| 2️⃣ | Definir saludo y tono usando la **Guía de prompts** | Prompt editor | 5 min |
| 3️⃣ | Añadir bloque de **FAQ** (copiar tabla de preguntas frecuentes de su startup) | Landbot UI | 5 min |
| 4️⃣ | Conectar **Zapier**: cuando el usuario escribe “quiero demo”, Zapier llama a la **API de OpenAI** y devuelve un mensaje personalizado. | Zapier + OpenAI API | 10 min |
| 5️⃣ | Probar flujo: enviar mensaje de prueba desde el preview y ajustar respuestas. | Preview | 5 min |
| 6️⃣ **(Opcional)** | Añadir **captura de lead** (campo email) y envío a Google Sheet. | Zapier | 5 min |
| 7️⃣ **(Opcional)** | Publicar el bot en una página de prueba (embed) o en WhatsApp (via Twilio). | Landbot embed | 5 min |

**Formato:** Los participantes trabajan **en parejas** (una con más conocimientos de IA, otra con visión de negocio) y el facilitador circula, resolviendo dudas y dando tips en tiempo real.  

**Key Takeaway:** *En 30 min puedes pasar de “idea” a “bot en vivo” listo para validar con usuarios reales.*  

---

### **Bloque 5 – 155‑165 min**  
**Título:** *Test, feedback y plan de acción*  
**Objetivo:** Enseñar a validar rápidamente el asistente y definir los siguientes pasos.  
**Dinámica:**  
- 5 min: Cada pareja prueba su bot con otro grupo (intercambio de enlaces).  
- 5 min: Rápida encuesta de 3 preguntas (¿Entendió?, ¿Fue útil?, ¿Qué falta?) usando Google Forms.  
- 2 min: Recapitulación de métricas a seguir (tasa de respuesta, tiempo de conversación, leads generados).  
**Key Takeaway:** *Validar antes de escalar ahorra tiempo y dinero; la métrica clave es el % de usuarios que completan el objetivo del bot.*  

---

### **Cierre – 165‑180 min**  
**Título:** *Entrega de recursos y Q&A*  
**Objetivo:** Dejar a los asistentes con material práctico y motivación para seguir construyendo.  
**Dinámica:**  
- 5 min: Repaso rápido de los **7 pasos del roadmap** (slide final).  
- 5 min: Entrega física/digital del **Handout “Roadmap post‑workshop”**, **cheat‑sheet de prompts**, y **lista de herramientas**.  
- 5 min: Preguntas abiertas y anuncio de comunidad Slack/WhatsApp para soporte continuo.  
**Key Takeaway:** *No te quedes con la teoría: el próximo paso es lanzar tu bot a 5 clientes y medir.*  

---

## 4️⃣ Ejercicio principal (todos pueden hacerlo)

**Construye tu propio asistente de IA en 30 min**  
- **Resultado tangible:** Un bot activo (URL) que responde a al menos 3 preguntas de tu caso de uso y captura un lead.  
- **Metodología:**  
  1. **Plantilla** de flujo (3‑4 bloques) + **prompt** de saludo.  
  2. **Zapier** → **OpenAI** (API call) para generar respuestas dinámicas.  
  3. **Publicación** en Landbot (embed o link).  
- **Criterios de éxito:** Bot responde sin errores, guarda datos en Google Sheet y se puede compartir.  

---

## 5️⃣ Recursos para llevar a casa

| Tipo | Contenido | Formato |
|------|-----------|---------|
| **Cheat‑sheet de prompts** | 20 prompts listos para FAQ, captura de datos, agendamiento, upsell. | PDF (1 pág.) |
| **Lista de herramientas no‑code** | Landbot, ChatGPT API (free tier), Zapier, Make, Voiceflow, Botpress Cloud. | Tabla comparativa (PDF) |
| **Roadmap 7 pasos** | Desde prototipo → test → iteración → lanzamiento beta. | PDF + Checklist imprimible |
| **Tutoriales en video** | “Crear un bot en Landbot + OpenAI” (10 min) y “Conectar Zapier a OpenAI” (8 min). | Enlace a carpeta Google Drive |
| **Plantilla Canvas** | Canvas de caso de uso + hoja de métricas. | PDF editable |
| **Acceso a comunidad** | Slack/WhatsApp exclusivo del workshop para preguntas post‑evento. | Enlace invitación |
| **Oferta de mentoría** | 30 min de consultoría gratuita (para los 10 primeros que soliciten). | Código de descuento |

---

## 6️⃣ Slide count estimado por sección

| Sección | Slides estimados |
|---------|-----------------|
| Bienvenida & Ice‑breaker | 5 |
| IA en 5 min (conceptos) | 9 |
| Canvas de caso de uso | 4 |
| Toolbox no‑code (demo) | 12 |
| Guía paso a paso del ejercicio principal | 15 |
| Test & métricas | 4 |
| Roadmap & cierre | 5 |
| **Total** | **≈ 54 slides** (≈ 1‑2 min por slide, con espacio para interacción) |

---

## 🎉 Resumen rápido para ti, facilitador

| Momento | Acción clave |
|---------|--------------|
| **0‑15 min** | Energiza, conecta a los emprendedores y plantea el “porqué”. |
| **15‑40 min** | Desmitifica IA con ejemplos cotidianos. |
| **40‑60 min** | Convierte la idea en caso de uso concreto (canvas). |
| **60‑90 min** | Muestra 2‑3 herramientas no‑code; elige la que mejor se ajuste. |
| **95‑155 min** | **Hands‑on:** cada dupla lanza su bot funcional. |
| **155‑165 min** | Test rápido, feedback y métricas de validación. |
| **165‑180 min** | Entrega de recursos, Q&A, invita a comunidad post‑evento. |

Con este outline tendrás una jornada dinámica, práctica y con resultados visibles que dejarán a los emprendedores listos para **pilotar su primer asistente de IA** en la semana siguiente. ¡Éxitos y que la energía del workshop sea contagiosa! 🚀