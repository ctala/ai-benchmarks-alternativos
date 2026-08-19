# Step 3.5 Flash — startup_content/workshop_outline

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 8.82 | quality: 9.8
- latency_total: 39.371s | tokens_per_second: 52.0
- input_tokens: 211 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una estructura detallada y práctica para el taller.

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

# **Workshop Presencial: "Construye tu Asistente de IA para tu Startup"**
**Audiencia:** Emprendedores early-stage, no técnicos (20-30 personas)  
**Duración total:** 3 horas  
**Tono:** Energético, práctico, sin tecnicismos. "Aprender haciendo" desde el minuto 1.

---

## **📋 AGENDA DETALLADA (3 HORAS)**

### **Bloque 0: Recepción y Energía Inicial (15 min)**
*   **Dinámica:** Registro rápido, café, música energética. Introducción oral del facilitador: "Hoy no vienen a ser programadores, vienen a ser *arquitectos* de soluciones. Su única herramienta será su laptop y su idea."
*   **Material preparado:** Lista de asistencia, stickers con nombres, conexión WiFi clara, café/agua.

---

### **Parte 1: ¿Por qué tu Startup YA necesita un Asistente de IA? (30 min)**
*   **Título:** Más allá del hype: Tu ventaja competitiva invisible.
*   **Objetivo:** Romper mitos ("es caro", "necesito un ingeniero") y conectar la IA con problemas reales de startups (captación, soporte, operación).
*   **Dinámica:** Charla interactiva con **ejemplos concretos y visuales** (capturas de pantalla de asistentes reales en startups latinas). Pregunta retórica: "¿Cuántas horas de tu semana gastas en tareas repetitivas que una IA podría hacer?"
*   **Key Takeaway:** "La IA no es el producto, es el *motor* que hace que tu producto o servicio sea 10x más eficiente y escalable."
*   **Slides:** 8-10 slides (imágenes de ejemplos, gráficos de ahorro de tiempo, quotes de founders).

---

### **Parte 2: El "Lego" de un Asistente de IA: Sin Miedo al Vocabulario (25 min)**
*   **Título:** Desarmando el robot: Prompt, Base de Conocimiento, Acciones.
*   **Objetivo:** Entender los 3 pilares de un asistente en lenguaje simple. Que puedan nombrar cada parte.
*   **Dinámica:** **Analogía del restaurante.** 
    *   *Prompt (Instrucciones)* = La receta y los estándares del chef.
    *   *Base de Conocimiento (Contexto)* = La bodega de ingredientes frescos (tu PDF, tu web, tu FAQ).
    *   *Acciones (Herramientas)* = Los electrodomésticos de la cocina (conectar con Calendly, enviar email, buscar en Google).
    *   Ejercicio rápido en parejas: "Identifiquen estos 3 elementos para el asistente de un gimnasio".
*   **Key Takeaway:** "No programas, *configuras*. Tú defines la receta, la IA cocina."
*   **Slides:** 6-7 slides (infografía clara de los 3 pilares, ejemplo del restaurante).

---

### **☕ COFFEE BREAK ESTRATÉGICO (15 min)**
*   **Consigna:** "Hablen con alguien que no conozcan y cuéntenle la idea de su asistente. Practiquen el 'pitch de 30 segundos'."

---

### **Parte 3: Manos a la Obra - Ejercicio Principal (60 min)**
*   **Título:** Taller de Prototipado Rápido: Tu Asistente en 45 Minutos.
*   **Objetivo:** Que cada asistente salga con un prototipo **funcional** de su asistente, aunque sea básico.
*   **Dinámica:** **Demo en vivo del facilitador** (15 min) usando una herramienta **no-code** (Ej: **Zapier Interfaces + OpenAI**, **Make.com + AI**, o **Bardeen**).
    1.  Crear una "interfaz" de chat simple.
    2.  Conectar una "Base de Conocimiento" (subir un PDF de su manual de usuario o un doc de FAQs).
    3.  Configurar una "Acción" (ej: que al pedir "agendar una reunión", abra un enlace a Calendly).
    4.  Probar en tiempo real.
*   **Ejercicio de los asistentes (30 min):** 
    *   **Paso 1 (5 min):** En sus laptops, definen en 1 párrafo: *"Mi asistente se llama [Nombre] y ayuda a [cliente] a resolver [problema] usando [info] y puede [acción]".*
    *   **Paso 2 (20 min):** Siguen la guía paso a paso (documentada en un Google Doc compartido) para crear su prototipo en la plataforma elegida. El facilitador y 2-3 "ayudantes" circulan resolviendo dudas específicas.
    *   **Paso 3 (5 min):** Prueban su asistente entre ellos. "Pídele a tu vecino que haga una pregunta a tu bot".
*   **Key Takeaway:** "Lo que acabas de crear es un MVP de IA. Es real, es tangible, y es el punto de partida. La perfección es enemiga del progreso."
*   **Slides:** 5 slides (solo capturas de pantalla de la herramienta, pasos numerados, enlace al doc de instrucciones).

---

### **Parte 4: ¿Y ahora qué? De Prototipo a Producción (25 min)**
*   **Título:** Del Papel al Producto: Cómo, Cuándo y con Qué.
*   **Objetivo:** Entender las opciones de escalamiento, costos aproximados y el camino a seguir.
*   **Dinámica:** Mesa redonda guiada.
    *   **Ruta 1 (DIY No-Code):** Herramientas como **Bubble, Softr, Voiceflow** para interfaces más complejas. Costos ~$50-$200/mes.
    *   **Ruta 2 (Híbrida):** Prototipo en no-code + contratar un desarrollador para la integración final.
    *   **Ruta 3 (Todo en Plataforma):** Usar soluciones todo-en-uno como **CustomGPT, SiteGPT** para chatbots de conocimiento.
    *   **Matriz de Decisión:** "¿Cuándo usar qué?" (Complejidad, presupuesto, urgencia).
*   **Key Takeaway:** "Empieza pequeño, valida con usuarios reales, y escala solo cuando sepas qué funciona. Tu primer asistente no será perfecto, pero será *tuyo* y te dará datos valiosos."
*   **Slides:** 8 slides (tabla comparativa simple, flujograma de decisión, ejemplos de costos).

---

### **