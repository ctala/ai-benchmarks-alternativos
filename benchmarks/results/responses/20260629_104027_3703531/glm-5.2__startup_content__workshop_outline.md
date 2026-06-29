# GLM 5.2 — startup_content/workshop_outline

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.04 | quality: 9.44
- latency_total: 51.281s | tokens_per_second: 61.2
- input_tokens: 202 | output_tokens: 3136
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Hola! Qué buena iniciativa. Como facilitador que ha recorrido el ecosistema LatAm, sé que los emprendedores early-stage no necesitan teoría sobre redes neuronales; necesitan **ahorrar tiempo y validar más rápido**. 

Aquí tienes el outline completo, diseñado para ser dinámico, ruidoso (en el buen sentido) y 100% accionable.

---

# 🚀 Workshop: "Construye tu Asistente de IA para tu Startup - Workshop Práctico"
**Duración:** 3 horas (180 min) | **Audiencia:** 20-30 emprendedores early-stage no-técnicos

## 🎒 Materiales Necesarios (Preparación previa)
**Para el facilitador:**
- Proyector y audio bueno (para demos).
- Conexión a internet de respaldo (Hotspot), por si el venue falla.
- Un Custom GPT (o Claude Project) ya creado y funcional para hacer la demo en vivo.
- Slides preparadas (Google Slides / Canva).

**Para los asistentes (se les debe avisar 1 semana antes):**
- Laptop obligatoria (no tablets).
- Cuenta activa en ChatGPT (idealmente Plus, pero tener lista una alternativa gratuita como Poe.com para quienes no tengan Plus).
- 1 documento PDF de su startup (Pitch deck, Business Model Canvas, o un FAQ de su producto).

**Físicos:**
- Post-its (2 colores diferentes) y bolígrafos.
- Pizarra o papelógrafo.

---

## ⏱️ Agenda Detallada (180 min)

### 1. Bienvenida y Mentalidad IA (15 min)
* **Objetivo:** Romper el hielo, calibrar expectativas y cambiar el chip de "la IA me va a quitar el trabajo" a "la IA es mi becario incansable".
* **Dinámica (Interacción):** Encuesta rápida a mano alzada ("¿Quién ha usado ChatGPT hoy?", "¿Quién se frustra cuando la IA alucina?"). Charla corta de 5 min sobre por qué los founders pierden tiempo en tareas de bajo valor.
* **Key Takeaway:** La IA no es magia, es delegación. Tu trabajo no es hacer la tarea, es ser el "Gerente" del Asistente de IA.
* **Slides estimadas:** 5 slides.

### 2. Bloque 1: Anatomía de un Buen Prompt (30 min)
* **Objetivo:** Entender la estructura de una instrucción efectiva para dejar de chatear y empezar a programar con palabras.
* **Dinámica (Charla + Ejercicio rápido):** 
  - Charla de 10 min: El framework CICA (Contexto, Instrucción, Características/Tono, Acción/Formato).
  - Ejercicio de 10 min: El facilitador pone un prompt malo ("Escribe un post para mi startup"). Los asistentes lo reescriben usando CICA en sus laptops y lo prueban en vivo.
* **Key Takeaway:** Un prompt sin contexto es como contratar a un empleado sin darle un manual de funciones. 
* **Slides estimadas:** 8 slides.

### 3. Bloque 2: Manos a la obra - Construyendo tu Asistente (75 min)
*(Este es el corazón del workshop)*
* **Objetivo:** Que cada emprendedor salga del salón con un Asistente de IA personalizado y funcional para su startup.
* **Dinámica (Demo guiada + Ejercicio principal):**
  - **Demo (15 min):** El facilitador muestra cómo crear un "Custom GPT" (o un Project en Claude/Poe) en 3 minutos. Le sube un PDF, le da instrucciones de rol y le hace preguntas.
  - **Ejercicio Principal (60 min):** *Ver detalle abajo.*
* **Key Takeaway:** La IA se vuelve 10x más útil cuando ya tiene el contexto de tu negocio precargado. Ya no tienes que explicarle quién eres cada vez.
* **Slides estimadas:** 6 slides (visuales de pasos, el resto es acción en pantalla).

### 4. ☕ Break (15 min)
* Pausa técnica. El facilitador camina por la sala resolviendo dudas puntuales de los que se atascaron.

### 5. Bloque 3: Integración y Siguiente Nivel (30 min)
* **Objetivo:** Mostrar cómo conectar este asistente con sus flujos de trabajo diarios sin escribir código.
* **Dinámica (Demo + Discusión):**
  - Demo rápida de 10 min usando Zapier o Make.com (ej: "Cuando llegue un correo de un cliente potencial, mándalo a mi Asistente de IA para que redacte la respuesta y me la envíe por Slack/WhatsApp").
  - Discusión de 10 min: ¿Dónde más puedo aplicar esto? (Atención al cliente, generación de contenido, análisis de competencia).
* **Key Takeaway:** Tu asistente de IA no vive aislado; puede conectarse a tus herramientas diarias para automatizar lo aburrido.
* **Slides estimadas:** 5 slides.

### 6. Bloque 4: Cierre y Compromiso (15 min)
* **Objetivo:** Aterrizar el aprendizaje y generar un compromiso de acción inmediata.
* **Dinámica (Share-out):** 3 personas voluntarias comparten en 30 segundos qué asistente crearon y para qué lo van a usar mañana. El facilitador cierra con un mensaje motivador.
* **Key Takeaway:** La tecnología no genera ventaja competitiva hasta que se convierte en hábito.
* **Slides estimadas:** 3 slides.

---

## 🛠️ Ejercicio Principal del Workshop (Bloque 2 - 60 min)

**Nombre:** "Tu Primer Empleado Virtual"
**Plataforma:** ChatGPT Plus (Custom GPTs) o Poe.com (para usuarios free).

**Paso 1: Definir el dolor (10 min - Offline)**
Cada emprendedor toma un post-it y escribe la tarea que MÁS ODIA hacer o que más tiempo le roba en su startup (ej: responder dudas de clientes, redactar posts para LinkedIn, resumir correos de proveedores).

**Paso 2: Darle Rol e Instrucciones (15 min)**
En la plataforma elegida, inician la creación del Asistente. Deben definir:
- **Nombre:** (Ej: "GrowthBot", "SoporteNinja")
- **Rol:** "Eres un [rol] experto en [industria]..."
- **Instrucciones base:** Usando el framework CICA visto en el Bloque 1. (Ej: "Tu objetivo es redactar 3 posts semanales para LinkedIn basados en el tono de nuestro CEO...").

**Paso 3: Alimentar el Contexto (15 min)**
Suben el PDF que trajeron (Pitch deck o FAQ). Le piden al asistente que lea el documento y resuma en 3 puntos qué hace la startup. *Si lo hace bien, el contexto está cargado.*

**Paso 4: Prueba de Estrés (10 min)**
Los asistentes le piden a su nuevo asistente que haga la tarea del Paso 1. 
- *Iteración:* Si la respuesta es genérica, deben ajustar las instrucciones para ser más específicos. (Ej: "No uses emojis", "Habla en segunda persona del plural", "Máximo 100 palabras").

**Paso 5: Intercambio (10 min)**
Se levantan y en parejas, se muestran mutuamente sus asistentes y les hacen una pregunta a la IA del otro. (Genera mucho ruido y networking).

---

## 🎁 Recursos para llevar a casa (Entregables)

Al finalizar, se les envía un enlace (Notion o Google Drive) con:
1. **El Deck del Workshop:** Con los frameworks explicados.
2. **Biblioteca de Prompts para Startups:** 20 prompts listos para copiar y pegar (Validación de idea, análisis de competencia, redacción de cold emails, estructuración de pitch).
3. **Guía "Paso a Paso No-Code":** Un PDF de 2 páginas con capturas de pantalla de cómo crear un Custom GPT y cómo crear una automatización básica en Zapier.
4. **Lista de Herramientas IA recomendadas para LatAm:** (Ej: ChatGPT, Claude, Perplexity, Gamma para slides, Tome, Notion AI).
5. **Acceso a la comunidad:** (Si tienes un grupo de WhatsApp o Slack para la cohorte) para seguir compartiendo prompts y casos de uso.

---

*Nota para el facilitador:* Mantén la energía alta. Usa música de fondo suave durante los ejercicios prácticos para que el silencio no se sienta pesado. ¡Mucho éxito en el escenario!