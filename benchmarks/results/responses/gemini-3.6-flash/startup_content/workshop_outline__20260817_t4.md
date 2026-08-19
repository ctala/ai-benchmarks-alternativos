# Gemini 3.6 Flash — startup_content/workshop_outline

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 28.431s | tokens_per_second: 155.8
- input_tokens: 190 | output_tokens: 4430
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada y práctica para el workshop.

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

¡Hola! Qué excelente iniciativa. Para emprendedores *no-técnicos*, la clave de este workshop es **democratizar la tecnología**: que pierdan el miedo, vean resultados inmediatos y salgan del evento con una herramienta real que les ahorre horas de trabajo esa misma semana.

Aquí tienes la propuesta completa para el workshop, diseñada con un enfoque 80% práctico, dinámico y con la jerga justa del ecosistema startup latinoamericano.

---

# OUTLINE DEL WORKSHOP
## "Construye tu Asistente de IA para tu Startup"
**Duración:** 3 Horas | **Formato:** Presencial | **Audiencia:** 20-30 Founders No-Técnicos

---

### 1. MATERIALES Y PREPARACIÓN PREVIA

#### Para el Facilitador / Organización:
*   Proyector/Pantalla grande con conexión HDMI/Type-C y sonido.
*   Internet Wi-Fi de ALTA VELOCIDAD (crucial: 20-30 personas haciendo llamadas a APIs/modelos simultáneamente).
*   Extensiones eléctricas / multicontactos (las laptops se agotarán).
*   Post-its de colores (3 colores por persona) y plumones negros.
*   Pizarra blanca o Flipchart.
*   1 asistente/co-facilitador en sala (para destrabar problemas técnicos individuales).

#### Para los Asistentes (Requisitos Previos enviados por email):
*   Laptop con cargador (obligatorio, no celular ni tablet).
*   Cuenta activa en **ChatGPT (Plus o versión Gratuita)** o **Claude.ai**.
*   *Pre-work (5 minutos):* Traer identificado un "cuello de botella" de su startup (ej: responder las mismas 10 preguntas de clientes, redactar correos de ventas, analizar feedback, crear contenido).

---

### 2. AGENDA DETALLADA Y BLOQUES

#### VISIÓN GENERAL DE TIEMPOS
*   **00:00 - 00:30** | Bloque 1: Bienvenida, Mindset y el "Súper Poder" de la IA
*   **00:30 - 01:10** | Bloque 2: La Fórmula del Prompting para Founders
*   **01:10 - 01:25** | *BREAK / NETWORKING (15 min)*
*   **01:25 - 02:25** | Bloque 3: **MANOS A LA OBRA (Ejercicio Principal)**
*   **02:25 - 02:45** | Bloque 4: Show & Tell + Testing Cruzado
*   **02:45 - 03:00** | Bloque 5: Escalando tu Asistente y Cierre

---

### 3. DESGLOSE BLOQUE POR BLOQUE

---

#### BLOQUE 1: Bienvenida, Mindset y el "Súper Poder" de la IA
*   **Duración:** 30 minutos (0:00 - 0:30)
*   **Objetivo:** Romper el hielo, eliminar el mito de que la IA es "solo para programadores" y alinear las expectativas del workshop.
*   **Dinámica:**
    1.  *Icebreaker (10 min):* "El Muro del Dolor". Cada founder escribe en un Post-it rojo la tarea más aburrida/repetitiva de su semana y la pega en la pared.
    2.  *Charla / Demo en vivo (20 min):* Presentación del facilitador. Mostrar en 3 minutos cómo un asistente mal configurado da respuestas genéricas y cómo uno bien configurado actúa como un empleado estrella Senior.
*   **Key Takeaway:** *"La IA no va a reemplazar a tu startup, pero un founder usando IA va a reemplazar al founder que no la usa. La IA es tu primer empleado contratado por $0."*
*   **Slide Count Estimado:** 5 slides.

---

#### BLOQUE 2: La Fórmula del Prompting para Founders
*   **Duración:** 40 minutos (0:30 - 1:10)
*   **Objetivo:** Enseñar la estructura lógica (Framework C.R.O.P.S.) para darle instrucciones precisas a un modelo de IA.
*   **Dinámica:**
    1.  *Charla interactiva (20 min):* Explicación de la anatomía de un System Prompt:
        *   **C**ontexto (Quién eres y qué hace tu startup).
        *   **R**ol (Qué persona/puesto asume la IA).
        *   **O**bjetivo (Qué debe lograr la interacción).
        *   **P**arametros/Límites (Qué NO debe hacer, tono de voz).
        *   **S**alida (Formato exacto de respuesta: tabla, email, JSON, bullets).
    2.  *Ejercicio rápido en parejas (20 min):* Analizar un "Prompt Basura" en pantalla y reescribirlo usando la fórmula C.R.O.P.S. Compartir 2 ejemplos con la sala.
*   **Key Takeaway:** *"Basura entra, basura sale. El secreto de un asistente inteligente no es la tecnología, es la claridad de tus instrucciones."*
*   **Slide Count Estimado:** 7 slides.

---

☕ **BREAK / NETWORKING (15 minutos / 1:10 - 1:25)**
*Música en vivo, café, agua. Consigna: Hablar con la persona de al lado sobre el post-it del Muro del Dolor.*

---

#### BLOQUE 3: MANOS A LA OBRA - Construye tu Asistente
*(Ver sección 4 para el detalle completo del ejercicio)*
*   **Duración:** 60 minutos (1:25 - 2:25)
*   **Objetivo:** Que el 100% de los asistentes configure y cree la primera versión (MVP) de su propio asistente en vivo (usando Custom GPTs de OpenAI o Projects en Claude / Poe).
*   **Dinámica:** Ejercicio práctico individual guiado paso a paso. El facilitador muestra el paso en la pantalla principal y luego los asistentes lo replican. El co-facilitador circula resolviendo dudas.
*   **Key Takeaway:** *"Construir software antes tomaba meses y miles de dólares. Hoy toma 30 minutos de lógica e instrucciones claras."*
*   **Slide Count Estimado:** 4 slides (Checklist de pasos visible todo el tiempo).

---

#### BLOQUE 4: Show & Tell + Testing Cruzado
*   **Duración:** 20 minutos (2:25 - 2:45)
*   **Objetivo:** Validar los asistentes en un entorno real, hacer prueba de estrés y recibir feedback inmediato.
*   **Dinámica:**
    1.  *Parejas de Testing (10 min):* Los founders se juntan de a dos. Founder A prueba el asistente de Founder B como si fuera un cliente/usuario difícil ("Intentar romper el bot").
    2.  *Demo Day Exprés (10 min):* 3 founders voluntarios suben al escenario, proyectan su pantalla y muestran su asistente en acción durante 2 minutos cada uno.
*   **Key Takeaway:** *"Tu asistente necesita iteración. Pruébalo con usuarios reales para descubrir sus puntos ciegos."*
*   **Slide Count Estimado:** 2 slides (Reglas del juego y temporizador en pantalla).

---

#### BLOQUE 5: Escalando tu Asistente y Cierre
*   **Duración:** 15 minutos (2:45 - 3:00)
*   **Objetivo:** Mostrar la hoja de ruta futura (cómo conectar este asistente a WhatsApp, CRM o Email sin código) y cerrar con alta energía.
*   **Dinámica:**
    1.  *Demo relámpago (7 min):* Mostrar cómo conectar el asistente creado a Zapier/Make o Botpress/ManyChat para responder automáticamente en canales reales (sin profundizar en código).
    2.  *Q&A y Cierre (8 min):* Espacio de preguntas rápidas, foto grupal y llamado a la acción.
*   **Key Takeaway:** *"Hoy construiste el cerebro. El siguiente paso es conectarle los brazos (automatizaciones) a tu negocio."*
*   **Slide Count Estimado:** 4 slides.

---

### 4. DETALLE DEL EJERCICIO PRINCIPAL (Bloque 3)

**Nombre del Ejercicio:** "Mi Asistente MVP en 45 Minutos"

**Descripción:**
Cada emprendedor elegirá **UNA** de las siguientes 3 plantillas de asistente para construir (según su necesidad actual):

1.  **Opción A: SDR de Ventas (Sales Assistant):** Entrenado con el pitch y FAQs de la startup para redactar correos de prospección hiper-personalizados y calificar leads.
2.  **Opción B: Customer Success & Soporte:** Creado subiendo la documentación/PDFs de la startup para responder dudas complejas de clientes con el tono de la marca.
3.  **Opción C: Growth & Content Copilot:** Un estratega de contenido entrenado con la propuesta de valor para generar ideas, guiones de video y posts adaptados a la audiencia objetivo.

**Paso a Paso del Ejercicio (Guiado en pantalla):**

*   **Paso 1 (10 min) - Configuración del Perfil:** Crear el GPT/Proyecto, asignarle un nombre, foto (usando DALL-E) y definir el *Role* y *Context*.
*   **Paso 2 (15 min) - Inyección de Conocimiento (Knowledge Base):** Subir al asistente al menos 1 archivo relevante (PDF de la empresa, landing page guardada como texto, catálogo de precios o transcripts de llamadas con clientes).
*   **Paso 3 (15 min) - Definición de Reglas y Guardrails (Instrucciones):** Escribir la lógica C.R.O.P.S., definir qué responder cuando no sepa la información ("Si no sabes la respuesta, di: *Dejame consultarlo con el equipo humano y te contacto*").
*   **Paso 4 (10 min) - Calibración Inicial:** Hacer 3 preguntas de prueba en la ventana de chat y ajustar las instrucciones según los fallos observados.

---

### 5. RECURSOS PARA LLEVAR A CASA (Take-Home Kit)

Al finalizar, se enviará un correo o código QR con un repositorio en Notion/PDF que incluye:

1.  **Plantilla "System Prompt Matrix" (Cheat-sheet):** Un documento editable con la estructura exacta C.R.O.P.S. para copiar y pegar en futuros proyectos.
2.  **Librería de 10 Prompts para Founders:**
    *   Prompt para validar ideas de producto.
    *   Prompt para hacer análisis de competencia.
    *   Prompt para preparar reuniones con inversionistas (Simulador de VC).
    *   Prompts para copywriting y marketing.
3.  **El "No-Code AI Tech Stack" Recomendado:** Lista curada de herramientas sin código para el siguiente nivel (Zapier, Make, Softr, Botpress, Voiceflow, Claude, ChatGPT).
4.  **Acceso a la Comunidad:** Enlace al grupo de WhatsApp/Slack de egresados del workshop para seguir compartiendo prompts y dudas.

---

### 6. RESUMEN DE SLIDES ESTIMADO

| Sección | No. de Slides | Contenido Clave |
| :--- | :--- | :--- |
| **Intro & Mindset** | 5 | Bienvenida, La regla del 10x, Demo impactante |
| **Framework Prompting** | 7 | C.R.O.P.S., Ejemplos Antes/Después, Guardrails |
| **Ejercicio Guiado** | 4 | Pantalla fija con la guía de pasos 1-4 |
| **Testing & Demos** | 2 | Reglas de prueba de estrés + Timer de pitches |
| **Siguientes Pasos** | 4 | No-code integrations, Stack técnico, QR de recursos |
| **TOTAL** | **~22 Slides** | *Diseño minimalista, poco texto, visualmente moderno.* |

---

### 🔥 CONSEJO DE FACILITACIÓN LATAM:
Mantén la música alta durante los ejercicios prácticos (Lofi Beats o Pop en español suave), usa un lenguaje muy aterrizado ("vamos a desglosar esto", "cero rollo", "manos a la masa") y **felicita públicamente los errores** durante las demos: un asistente que "alucina" en vivo es la mejor oportunidad de enseñanza para toda la sala. ¡Mucho éxito con el taller!