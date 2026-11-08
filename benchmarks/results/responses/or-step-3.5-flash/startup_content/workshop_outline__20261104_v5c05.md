# Step 3.5 Flash — startup_content/workshop_outline

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 8.65 | quality: 9.72
- latency_total: 45.38s | tokens_per_second: 81.6
- input_tokens: 211 | output_tokens: 3704
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

¡Excelente! Aquí tienes el outline completo, diseñado para ser **práctico, motivador y 100% accionable** para emprendedores sin perfil técnico.

---

### **Workshop: "Construye tu Asistente de IA para tu Startup - Workshop Práctico"**
**Público:** Emprendedores early-stage (no-técnicos)
**Duración:** 3 horas
**Filosofía:** "No necesitas ser programador para automatizar y escalar con IA. Necesitas una idea clara y las herramientas correctas."

---

### **1. Agenda Detallada con Tiempos (3 horas)**

*   **0-10 min:** **Bienvenida & Rompehielos Energético.**
*   **10-30 min:** **Bloque 1: El Poder del Asistente de IA (¿Por qué y para qué?).**
*   **30-55 min:** **Bloque 2: Diseñando el Cerebro de tu Asistente (Sin código).**
*   **55-70 min:** **Pausa Rápida & Networking (15 min).**
*   **70-130 min:** **Bloque 3: Manos a la Obra - Construyendo tu Primer Flujo.**
*   **130-150 min:** **Bloque 4: Probar, Fallar y Mejorar (El Ciclo de la IA Práctica).**
*   **150-175 min:** **Bloque 5: Tu Plan de Acción de 30 Días.**
*   **175-180 min:** **Cierre, Q&A y Próximos Pasos.**

---

### **2. Materiales Necesarios (Preparar Antes)**

*   **Para el Facilitador:**
    *   Presentación en Google Slides / Canva (muy visual, puro texto clave).
    *   Cuenta en **Voiceflow** (o **Botpress** / **Landbot**) con un proyecto de ejemplo ya creado.
    *   Acceso a internet estable y proyector.
    *   **Plantilla de "Matriz de Intenciones"** en Google Docs (compartida con todos).
    *   **Checklist "Mi Asistente en 30 Días"** en PDF (para handout).
    *   Pizarra blanca grande o rotafolio y marcadores.
*   **Para los Asistentes (Comunicar con anticipación):**
    *   **Laptop propia** (imprescindible).
    *   Conexión a internet.
    *   **Cuenta creada previamente en Voiceflow.com** (gratis, es drag-and-drop). *¡Clave para ahorrar tiempo!*
    *   Una idea clara de **UN** proceso de su startup que quieran automatizar (ej: "calificar leads", "responder preguntas frecuentes", "soporte post-venta básico").
    *   **Impresos:** 1 hoja con la **Matriz de Intenciones** y 1 hoja con el **Checklist de 30 días**.

---

### **3. Desarrollo por Bloques**

#### **Bloque 1: El Poder del Asistente de IA (¿Por qué y para qué?)**
*   **Duración:** 20 min.
*   **Objetivo:** **Motivar y cambiar el mindset.** Entender que un asistente es un "empleado digital" que no cobra, no se queja y trabaja 24/7, enfocado en tareas específicas, no en "ser una IA general".
*   **Dinámica:** Charla interactiva + Demo en vivo rápida.
    *   **Demo:** Muestro un asistente de Voiceflow que yo haya hecho (ej: un calificador de leads que hace 3 preguntas y entrega un lead score). ¡Lo muestro funcionando en mi celular!
    *   **Pregunta a la audiencia:** "¿Qué proceso repetitivo en su startup les roba 2 horas al día?" (Unos 5 comentarios en voz alta).
*   **Key Takeaway:** Un asistente exitoso **NO** intenta hacer todo. Hace **UNA COSA** muy bien, liberando tu tiempo para lo que solo tú puedes hacer: pensar, crear relaciones y cerrar ventas.

#### **Bloque 2: Diseñando el Cerebro de tu Asistente (Sin código)**
*   **Duración:** 25 min.
*   **Objetivo:** Aprender la **metáfora clave**: un asistente de conversación se construye con **"Intenciones"** (lo que el usuario quiere) y **"Entidades"** (los datos clave). No es magia, es lógica condicional.
*   **Dinámica:** Charla visual con slides de arquitectura simple.
    *   **Analogía:** "Es como un árbol de decisiones para tu recepcionista virtual".
    *   **Ejemplo en pizarra:** Usuario dice -> *"¿Cuánto cuesta?"* -> **Intención:** `cotizar_precio` -> **Entidad:** `producto` -> Respuesta: "El precio de [producto] es $X".
    *   **Ejercicio rápido en parejas (5 min):** En su hoja impresa de "Matriz de Intenciones", definen: 1) Su proceso, 2) 3 posibles "Intenciones" del usuario (ej: `consultar_horario`, `solicitar_cotizacion`, `hablar_con_humano`), 3) 1 "Entidad" clave por intención (ej: `servicio`, `fecha`).
*   **Key Takeaway:** Tu primera versión solo necesita **3-5 intenciones** bien definidas. El 80% del valor está en capturar correctamente la intención y los datos clave.

#### **Bloque 3: Manos a la Obra - Construyendo tu Primer Flujo**
*   **Duración:** 60 min. **(El corazón del workshop)**
*   **Objetivo:** **Que el 100% de la sala tenga un asistente funcional (aunque sea básico) al final del bloque.**
*   **Dinámica:** **Demo guiada paso a paso.**
    *   El facilitador comparte pantalla y, en **Voiceflow**, construye en vivo un flujo simple (ej: un asistente para una cafetería que toma un pedido).
    *   **Paso 1:** Crear un "Welcome Message".
    *   **Paso 2:** Añadir un "Capture Intent" (elegir de una lista predefinida, no crear las suyas aún).
    *   **Paso 3:** Conectar la intención a una respuesta.
    *   **Paso 4:** Añadir un "Capture Entity" (ej: "¿Para qué fecha?") y usar esa entidad en la respuesta.
    *   **Paso 5:** Probar el flujo en el *"Test Assistant"* de Voiceflow. ¡Que todos vean que funciona!
    *   **Tarea individual (30 min):** Cada persona abre su proyecto en Voiceflow y, usando su "Matriz de Intenciones" del bloque 2, construye **el flujo de UNA de sus intenciones**. El facilitador y asistentes avanzados circulan resolviendo dudas específicas.
*   **Key Takeaway:** La plataforma es un juego de conectar piezas. Si sabes lo que quieres que diga y pregunte, puedes construirlo arrastrando y soltando. **Perder el miedo a "romperlo"** (siempre se puede deshacer).

#### **Bloque 4: Probar, Fallar y Mejorar (El Ciclo de la IA Práctica)**
*   **Duración:** 20 min.
*   **Objetivo:** Entender que el primer flujo **no será perfecto** y que la clave es probar con usuarios reales (o colegas) y iterar.
*   **Dinámica:** Discusión guiada + Ejercicio de "Fallas Divertidas".
    *   Pregunta: "¿Qué pasa si el usuario escribe 'necesito una coti' en vez de 'solicitar_cotizacion'?" -> **Respuesta:** Entrenar con más ejemplos (sinónimos) en la intención.
    *   Pregunta: "¿Y si el usuario se desvía y pregunta '¿tienen wifi?'" -> **Respuesta:** Crear una intención de "fallback" (respuesta por defecto) que diga "No soy experto en eso, pero te conecto con un humano" y termine el flujo.
    *   **Ejercicio en parejas (10 min):** Intercambian sus asistentes. Uno es el "usuario confundido" y el otro es el "dueño". El usuario prueba escribiendo cosas raras. El dueño anota qué falló y cómo lo arreglaría (añadir más ejemplos, crear nueva intención).
*   **Key Takeaway:** Tu asistente mejora **con uso real**, no con más teoría. Lanza una versión "beta" a 5 amigos/clientes esta semana y pide feedback específico.

#### **Bloque 5: Tu Plan de Acción de 30 Días**
*   **Duración:** 25 min.
*   **Objetivo:** Comprometer a una **acción concreta y pequeña** post-workshop. Evitar la parálisis por análisis.
*   **Dinámica:** Trabajo individual silencioso + Compromiso en grupo.
    *   Cada persona completa su **Checklist "Mi Asistente en 30 Días"** (handout impreso):
        1.  **Semana 1:** Terminar el flujo de mi intención principal en Voiceflow.
        2.  **Semana 2:** Probar con 3 personas (amigos/familia) y anotar 3 fallos.
        3.  **Semana 3:** Corregir los 3 fallos y añadir 1 intención más.
        4.  **Semana 4:** Publicarlo en mi web/WhatsApp (usando el widget de Voiceflow) y medir 5 conversaciones.
    *   **Ronda de compromisos (5 min):** Cada quien dice en voz alta **UNA** cosa que hará el **lunes** (ej: "El lunes, terminaré de conectar mi flujo de cotizaciones").
*   **Key Takeaway:** El éxito no es tener un asistente "perfecto". El éxito es tener un asistente **en producción** que te dé datos reales para mejorarlo.

#### **Cierre (5 min)**
*   **Recursos para llevar a casa** (ver siguiente sección).
*   **Palabra final:** "Salgan y construyan la primera versión. No la segunda. La primera. El mundo no necesita tu asistente perfecto, necesita que empieces."
*   **Q&A rápido** (solo preguntas logísticas de la plataforma).

---

### **4. Ejercicio Principal del Workshop**
**Nombre:** "De la Idea al Flujo Funcional en 60 Minutos".
**Descripción:** Cada asistente, usando su laptop y su cuenta de Voiceflow, construirá el flujo de conversación para **la intención más importante** que definieron en la "Matriz de Intenciones".
**Pasos concretos que deben lograr:**
1.  Crear un mensaje de bienvenida personalizado.
2.  Configurar un nodo de "Capturar Intención" con **al menos 3 ejemplos de frases** de usuario para esa intención.
3.  Conectar esa intención a un nodo de respuesta que **incluya la entidad clave** que capturaron (ej: "Te enviaremos la cotización de [producto] a tu correo").
4.  Probar el flujo **en el simulador de Voiceflow** con una frase de ejemplo.
5.  (Opcional, si les da tiempo) Crear un nodo de "Respuesta por defecto" para cuando el asistente no entienda.
**Meta:** Que al final del bloque, todos puedan abrir su proyecto, hacer *click* en "Test" y ver su asistente responder correctamente a una frase de prueba.

---

### **5. Recursos para Llevar a Casa (Handout Digital + Físico)**
1.  **Presentación completa** (PDF).
2.  **Plantilla editable "Matriz de Intenciones"** (Google Sheets).
3.  **Checklist "Mi Asistente en 30 Días"** (PDF).
4.  **Lista Curada de Herramientas:**
    *   **Para construir:** Voiceflow (gratis), Botpress (open source), Landbot (no-code).
    *   **Para desplegar:** Widget de web, integración con WhatsApp (Twilio), Telegram, Instagram.
    *   **Para entrenar/mejorar:** Documentar ejemplos de usuario en un Google Doc simple.
5.  **Comunidad Privada:** Enlace a un grupo de WhatsApp/Telegram o foro simple para que los asistentes sigan compartiendo dudas y éxitos.
6.  **Grabación del workshop** (si se grabó) y **enlace a los proyectos de ejemplo** del facilitador en Voiceflow (para clonar).

---

### **6. Slide Count Estimado por Sección**
*   **Total:** ~35-45 slides (muy visuales, 1 idea por slide).
*   **Portada + Agenda:** 2 slides.
*   **Bloque 1:** 5 slides (motivación, ejemplos, demo).
*   **Bloque 2:** 8 slides (metáfora, arquitectura, ejemplo en pizarra, definición de intenciones/entidades).
*   **Bloque 3:** 10 slides (capturas de pantalla de Voiceflow, paso a paso visual, lo que deben ver en su pantalla).
*   **Bloque 4:** 5 slides (cómo probar, ejemplos de fallos comunes, ciclo iterativo).
*   **Bloque 5:** 4 slides (el checklist, ejemplos de compromisos).
*   **Recursos + Cierre:** 3 slides.
*   **Slides de "ejercicio en parejas" o "trabajo individual":** 2-3 slides con instrucciones claras.

---

**Nota final para el facilitador:** Tu rol no es ser un experto en Voiceflow, sino un **guía de proceso**. El valor está en ayudarles a **pensar** su asistente (intenciones/entidades), no en dominar la herramienta. Si alguien se atasca en la plataforma, dilo: "Eso es un problema técnico menor, yo te ayudo en 2 min. Lo importante es que tengas claro el flujo que quieres". ¡Mucho ánimo y a ensuciarse las manos! 🚀