# DeepSeek V4 Pro — startup_content/workshop_outline

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.22 | quality: 9.8
- latency_total: 51.474s | tokens_per_second: 81.4
- input_tokens: 198 | output_tokens: 4192
- judge_score: 5.0 | justificación: 

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

¡Excelente iniciativa! Aquí tienes el outline completo para un workshop que no solo informará, sino que transformará a esos emprendedores en creadores de su propia tecnología. Está diseñado al estilo "aprender haciendo", con la energía de una startup en sus inicios.

---

### Título del Workshop:
**"Construye tu Asistente de IA para tu Startup - Workshop Práctico"**

**Concepto Central:** En 3 horas, cada emprendedor pasará de "no sé nada de código" a tener un prototipo funcional de un asistente de IA que resuelve un problema real de su startup (ej: onboarding de clientes, FAQ inteligente, generador de ideas de contenido).

---

### 1. Agenda Detallada (3 Horas)

| Hora | Duración | Bloque |
| :--- | :--- | :--- |
| 09:00 - 09:30 | 30 min | **Bloque 0: Bienvenida & Setup Relámpago** |
| 09:30 - 10:00 | 30 min | **Bloque 1: El "Por Qué" y el "Qué" de tu Asistente IA** |
| 10:00 - 10:30 | 30 min | **Bloque 2: Manos al Teclado - Tu Primer "Hola Mundo" Inteligente** |
| 10:30 - 11:15 | 45 min | **Bloque 3: El Corazón del Workshop - Construye el Prototipo** |
| 11:15 - 11:45 | 30 min | **Bloque 4: De Prototipo a Producto - Testeo y Empaquetado** |
| 11:45 - 12:00 | 15 min | **Bloque 5: Showtime, Recursos y Próximos Pasos** |

---

### 2. Materiales Necesarios (Preparar Antes)

**Para el Facilitador:**
- **Kit de Slides:** (Google Slides/PowerPoint) con el outline abajo.
- **Guía de la Plataforma:** Elegir UNA plataforma no-code. Recomendación TOP para este workshop: **Botpress** (la versión cloud gratuita es muy visual y potente) o **Voiceflow**. Tener una cuenta de prueba creada para mostrar.
- **Plantilla Base:** Un "bot esqueleto" pre-configurado en la plataforma elegida, con la integración a la API de OpenAI ya hecha. Esto es CRÍTICO para no perder tiempo en setup. El workshop es de construcción, no de configuración de APIs.
- **PDF de Recursos:** Un documento descargable con links, guías y la plantilla (detallado en el punto 5).
- **3-4 Casos de Éxito Relámpago:** Ejemplos de startups que usan asistentes de IA para cosas concretas (no grandes corporaciones).

**Para los Participantes (Enviar 3 días antes):**
- **Laptop con batería:** Indispensable. "Sin laptop, no hay workshop".
- **Navegador Chrome/Firefox actualizado.**
- **Cuenta Creada:** Pedirles crear una cuenta gratuita en la plataforma elegida (ej: app.botpress.cloud) ANTES de llegar. Enviar un video tutorial de 2 minutos.
- **Un Problema en Mente:** Pedirles que traigan un caso de uso simple: "¿Cuál es la pregunta más repetitiva que te hacen tus clientes?" o "¿Qué tarea manual de tu startup te quita 1 hora al día?".

**En la Sala (Logística):**
- **Post-its y Sharpies.**
- **Conexión Wi-Fi de alta velocidad (¡probada!).**
- **Pantalla grande y buen sonido.**
- **Música energética de fondo para la bienvenida.**
- **Premio simbólico:** Un libro de IA/startups o 3 meses gratis de la herramienta para el mejor prototipo.

---

### 3. Desarrollo de Cada Bloque

#### Bloque 0: Bienvenida & Setup Relámpago (30 min)

- **Título:** Arranque de Motor: Preparados para Construir.
- **Objetivo:** Energizar a la audiencia, romper el hielo y asegurar que el 100% de las máquinas estén listas para construir.
- **Dinámica:**
    1.  **Charla (5 min):** Bienvenida explosiva. "Hoy no vienen a aprender teoría. Saldrán de aquí con un asistente de IA funcionando. ¿Listos para hackear su startup?".
    2.  **Ejercicio Rompehielos (15 min):** "El Problema de tu Vecino". En parejas, cada uno comparte en 1 minuto el problema repetitivo que quiere resolver con IA. Luego, presentan el problema de su compañero en 30 segundos. Esto activa la mentalidad de "diseño para el usuario".
    3.  **Verificación de Setup (10 min):** "Momento de la verdad". Manos arriba. Facilitador y co-facilitadores caminan para verificar que todos tengan la cuenta abierta en la plataforma. Quienes no, se les ayuda en el momento.
- **Key Takeaway:** "La tecnología es lo de menos; el problema a resolver lo es todo. Y tú ya tienes uno identificado."

---

#### Bloque 1: El "Por Qué" y el "Qué" de tu Asistente IA (30 min)

- **Título:** De la Idea al Plano: Diseñando un Asistente que Sirva.
- **Objetivo:** Entender los conceptos clave de un asistente de IA (no-code) y diseñar la "personalidad" y el flujo de su propio bot en papel.
- **Dinámica:**
    1.  **Charla-Demo (10 min):** Explicar los 3 componentes de un asistente moderno de forma simple:
        - **La Personalidad (System Prompt):** "¿Cómo le dices a la IA que actúe? Es el ADN de tu startup".
        - **El Conocimiento (Knowledge Base):** "¿De dónde saca la info? Tu web, un PDF, un FAQ."
        - **La Conversación (User Prompt):** Lo que el usuario pregunta.
        *Demo en vivo:* Mostrar un bot genérico vs uno con personalidad de startup (ej: "Responde como un barista experto y sarcástico").
    2.  **Ejercicio (15 min):** "El Plano de tu Bot". Cada emprendedor usa un Post-it para escribir:
        - **Post-it 1 (Personalidad):** 3 adjetivos que definan el tono de su asistente (ej: "Empático, Conciso, Proactivo").
        - **Post-it 2 (Conocimiento):** 1 fuente de info (ej: "El archivo de preguntas frecuentes que tengo en mi escritorio").
        - **Post-it 3 (Objetivo):** La frase que quieren que su asistente NUNCA diga y la que SIEMPRE debe decir.
    3.  **Discusión (5 min):** 2-3 voluntarios comparten su plano en 1 minuto. El facilitador da feedback rápido y energético.
- **Key Takeaway:** "Un gran asistente de IA no se programa, se diseña. Tu plano de 3 Post-its es el 50% del trabajo."

---

#### Bloque 2: Manos al Teclado - Tu Primer "Hola Mundo" Inteligente (30 min)

- **Título:** Clics, no Código: Domando la Plataforma.
- **Objetivo:** Familiarizarse con la interfaz de la herramienta no-code y crear un primer flujo conversacional simple.
- **Dinámica:**
    1.  **Demo Guiada Paso a Paso (20 min):** "Síganme". El facilitador proyecta su pantalla y todos hacen lo mismo en su computadora.
        - Paso 1: Crear un nuevo bot desde la plantilla base.
        - Paso 2: Encontrar el nodo "Personalidad" y pegar los adjetivos de su Post-it. *¡Primer momento mágico!*
        - Paso 3: Encontrar el nodo "Conocimiento" y subir un archivo simple (ej: un .txt con 5 preguntas frecuentes genéricas que el facilitador provee).
        - Paso 4: Probar el bot en el emulador integrado. Hacerle una pregunta del FAQ. *¡Segundo momento mágico! Funciona.*
    2.  **Resolución de Micro-Problemas (10 min):** "¿Quién tiene un error? Manos arriba." El facilitador y asistentes resuelven problemas comunes en tiempo real. Esto genera comunidad y confianza.
- **Key Takeaway:** "Acaban de darle vida a una IA. No escribieron una sola línea de código, pero ya tiene su conocimiento y personalidad."

---

#### Bloque 3: El Corazón del Workshop - Construye el Prototipo (45 min)

- **Título:** Hora de Hackear: Construyendo Tu Caso de Uso Real.
- **Objetivo:** Este es el ejercicio principal. Cada emprendedor transforma su bot genérico en un prototipo que resuelve su problema de startup.
- **Dinámica:**
    1.  **Charla de Enfoque (5 min):** "Olviden el bot genérico. Ahora vamos a darle un propósito. Su misión en estos 45 minutos es que su asistente pueda manejar el problema que identificaron al inicio."
    2.  **Ejercicio Principal "Construcción Libre Guiada" (40 min):**
        - **Min 0-10:** Refinan la personalidad y suben su propio documento de conocimiento (o crean uno en el momento).
        - **Min 10-25:** Añaden un flujo simple. Ej: "Si el usuario saluda, el bot se presenta y ofrece 3 opciones de ayuda basadas en el conocimiento cargado".
        - **Min 25-40:** Prueban y depuran. Se piden que se hagan preguntas difíciles a su propio bot.
        - **Rol del Facilitador:** Música de concentración de fondo. Facilitador y asistentes caminan, destraban dudas 1-a-1, y motivan. "¡Ese error es genial, significa que estás empujando los límites!"
- **Key Takeaway:** "No están soñando con un asistente de IA. Lo están usando. Y lo construiste tú."

---

#### Bloque 4: De Prototipo a Producto - Testeo y Empaquetado (30 min)

- **Título:** El Pase Final: Prueba, Pule y Publica.
- **Objetivo:** Aprender a probar el asistente con otra persona, iterar basado en feedback, y entender cómo publicarlo en un canal real.
- **Dinámica:**
    1.  **Ejercicio de Testeo en Parejas (15 min):** "Intercambien el link de prueba de su bot con el vecino". Cada uno prueba el asistente del otro e intenta "romperlo" o encontrar puntos ciegos. Se da feedback usando la técnica "Me gustó... / Me gustaría que...".
    2.  **Demo de Publicación (10 min):** El facilitador muestra en 2 minutos cómo se publica el bot en un canal de prueba (ej: un demo de WhatsApp o un link web simple). Explica los conceptos de "staging" vs "producción" de forma simple. El resto del tiempo es para que ellos lo publiquen.
    3.  **Discusión (5 min):** "¿Quién logró publicar su bot? ¿Quién recibió un feedback que le abrió los ojos?".
- **Key Takeaway:** "Un prototipo que solo tú ves es un hobby. Un asistente que otros prueban es un producto. Hoy cruzaste esa línea."

---

#### Bloque 5: Showtime, Recursos y Próximos Pasos (15 min)

- **Título:** De Vuelta al Mundo Real: Tu Kit de Vuelo IA.
- **Objetivo:** Celebrar los logros, entregar recursos para seguir aprendiendo y dar un cierre inspirador.
- **Dinámica:**
    1.  **Showtime (5 min):** ¡El premio! Un voluntario (o el que el facilitador vio que hizo algo increíble) proyecta su asistente y lo muestra en 2 minutos. Aplausos y entrega del premio simbólico.
    2.  **Entrega de Recursos (5 min):** "Llévense esto a casa". Se presenta el PDF descargable (detallado abajo) y se explica brevemente.
    3.  **Cierre Inspirador (5 min):** "Hoy construyeron un asistente. Pero lo más importante es que perdieron el miedo a la IA. Su startup ya no es pre-IA. La ventaja competitiva no es la herramienta, es el emprendedor que sabe qué problema resolver con ella. Ustedes ahora son ese emprendedor. ¡A construir!"
- **Key Takeaway:** "Este workshop no es el final, es el inicio de su mentalidad 'builder' con IA. El 80% del éxito es atreverse a empezar, y ustedes ya lo hicieron."

---

### 4. Ejercicio Principal del Workshop (Detalle del Bloque 3)

- **Nombre:** "De la Pregunta Frecuente al Asistente Inteligente"
- **Objetivo:** Que cada emprendedor cree un asistente capaz de responder al menos 5 preguntas frecuentes complejas sobre su startup, con un tono de marca definido, y que pueda derivar a un humano si no sabe la respuesta.
- **Instrucciones para el Participante:**
    1.  **Define el "ADN" (5 min):** En la sección de personalidad de tu bot, escribe: "Eres [Nombre del Asistente], el asistente virtual de [Nombre de Startup]. Tu misión es ayudar a clientes potenciales a entender [Propuesta de Valor en 1 frase]. Responde con un tono [Adjetivo 1], [Adjetivo 2] y [Adjetivo 3]. Si te preguntan algo que no está en tu base de conocimiento, di: '¡Excelente pregunta! Permíteme conectar a un co-founder para que te responda personalmente'."
    2.  **Alimenta el Cerebro (10 min):** Crea un archivo de texto simple (.txt) en tu computadora. Escribe las 5 preguntas más frecuentes que recibes de clientes, y para cada una, escribe la respuesta perfecta, como si la estuvieras dando tú. Sube este archivo a la sección de "Conocimiento" de tu bot.
    3.  **Prueba y Desafía (15 min):** En el emulador, hazle las 5 preguntas. Luego, hazle preguntas difíciles: "¿Eres mejor que la competencia?", "Dame un descuento del 90%", "¿Quién fundó la empresa?". Ajusta la personalidad o el conocimiento hasta que las respuestas te enorgullezcan.
    4.  **El Toque Humano (10 min):** Asegúrate de que, ante una pregunta que no puede responder, active el "plan B" de derivar a un humano que escribiste en el paso 1. ¡Pruébalo!

---

### 5. Recursos para Llevar a Casa (PDF Descargable)

- **Título del PDF:** "Kit de Supervivencia IA para tu Startup: Del Workshop al Mundo Real"
- **Contenido:**
    1.  **Link a la Plantilla Base:** El archivo del bot usado en el workshop para que puedan duplicarlo.
    2.  **Video-Tutoriales Express (2-3 min cada uno):**
        - Cómo conectar el bot a WhatsApp Business.
        - Cómo añadir una base de conocimiento desde una URL.
        - Cómo analizar las conversaciones de tu bot.
    3.  **Guía de "System Prompts Mágicos":** 5 plantillas de personalidad para distintos tipos de startups (Fintech, E-commerce, SaaS, Salud, Educación).
    4.  **Checklist de Lanzamiento:** 5 cosas que verificar antes de hacer público tu asistente.
    5.  **Comunidad:** Link a un grupo de WhatsApp/Discord exclusivo para ex-alumnos del workshop donde compartir dudas y logros.
    6.  **Bonificación:** 3 casos de estudio de startups que empezaron con un bot así y lo escalaron.

---

### 6. Slide Count Estimado por Sección

- **Portada y Agenda (2 slides):** Título impactante y lo que van a construir.
- **Bloque 0 (3 slides):** Setup, reglas del juego, rompehielos.
- **Bloque 1 (8 slides):**
    - 2 slides: Conceptos clave (Personalidad, Conocimiento).
    - 2 slides: Casos de éxito relámpago.
    - 1 slide: Instrucciones del ejercicio de los Post-its.
    - 3 slides: De apoyo visual con ejemplos de "personalidad".
- **Bloque 2 (5 slides):**
    - 5 slides con capturas de pantalla gigantes de la plataforma, una por cada paso de la demo guiada.
- **Bloque 3 (2 slides):** Una con las instrucciones del ejercicio principal y otra con un "temporizador" de 45 minutos.
- **Bloque 4 (4 slides):**
    - 1 slide: Instrucciones de testeo en parejas.
    - 1 slide: Técnica de feedback "Me gustó / Me gustaría".
    - 2 slides: Demo de publicación (capturas de pantalla).
- **Bloque 5 (4 slides):**
    - 1 slide: Contenido del PDF descargable.
    - 1 slide: Frase de cierre inspirador.
    - 1 slide: Llamado a la acción (unirse a la comunidad).
    - 1 slide: Agradecimientos y QR al PDF.
- **Total: 28 slides.** (Perfecto para 3 horas, priorizando la práctica sobre las diapositivas).