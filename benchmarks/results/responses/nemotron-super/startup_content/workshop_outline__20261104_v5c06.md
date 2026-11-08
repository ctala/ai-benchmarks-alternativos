# Nemotron 3 Super — startup_content/workshop_outline

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.84 | quality: 9.72
- latency_total: 11.603s | tokens_per_second: 203.3
- input_tokens: 206 | output_tokens: 2359
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

¡Excelente! Como facilitador de workshops en Latinoamérica, sé que la clave con emprendedores no-técnicos es **quitarles el miedo a la tecnología** y hacer que se lleven algo funcionando en las manos antes de que termine la sesión.

Aquí tienes el outline completo, diseñado para ser dinámico, práctico y enfocado en resultados inmediatos.

---

# 🚀 Workshop: Construye tu Asistente de IA para tu Startup

**Duración:** 3 horas (180 minutos)
**Audiencia:** Emprendedores early-stage no-técnicos (20-30 personas)
**Formato:** Presencial, práctico, "learning by doing"

---

## 1. Agenda Detallada con Tiempos

| Hora | Bloque | Actividad | Duración |
| :--- | :--- | :--- | :--- |
| 00:00 - 00:20 | **Bienvenida y Contexto** | Icebreaker, expectativas y por qué IA para startups | 20 min |
| 00:20 - 00:50 | **Conceptos Clave (Sin Jerga)** | Qué es un asistente de IA, LLMs, Prompting básico | 30 min |
| 00:50 - 01:10 | **Demo en Vivo** | Construcción de un asistente en tiempo real | 20 min |
| 01:10 - 01:25 | **Break** | Networking y café | 15 min |
| 01:25 - 02:40 | **Laboratorio Práctico** | Los participantes construyen su propio asistente | 75 min |
| 02:40 - 02:55 | **Show & Tell** | Presentaciones rápidas de los asistentes creados | 15 min |
| 02:55 - 03:00 | **Cierre y Próximos Pasos** | Recursos, comunidad y despedida | 5 min |

---

## 2. Materiales Necesarios (Preparación previa)

### Para el Facilitador:
*   **Laptop** con buena conexión a internet.
*   **Proyector/Pantalla** y adaptadores (HDMI/USB-C).
*   **Cuenta de prueba** en la herramienta elegida (ej. Custom GPTs de OpenAI, Poe, o Botpress) con créditos activos.
*   **Presentación (Slides)** visuales y con pocos textos.
*   **Timer/Cronómetro** visible para los ejercicios.
*   **Hoja de trucos (Cheat Sheet)** impresa con ejemplos de prompts.

### Para los Participantes (Traer ellos):
*   **Laptop propio** (carga completa).
*   **Cuenta de email** activa (para crear cuentas en las herramientas de IA).
*   **Una idea clara** de un problema repetitivo en su startup (ej: responder DMs de Instagram, calificar leads, redactar facturas).

### Para el Espacio:
*   Mesas con enchufes eléctricos disponibles.
*   Wi-Fi de alta velocidad (contraseña visible en pizarra).
*   Marcadores y post-its para el icebreaker.

---

## 3. Bloques del Workshop (Detalle)

### Bloque 1: Bienvenida y Contexto
*   **Título:** "¿Por qué tu startup necesita un asistente de IA ayer?"
*   **Duración:** 20 minutos
*   **Objetivo:** Romper el hielo, alinear expectativas y motivar a los asistentes mostrando casos de éxito locales.
*   **Dinámica:** Charla breve + Icebreaker (cada uno dice su nombre, su startup y una tarea que odia hacer repetidamente).
*   **Key Takeaway:** La IA no reemplaza al emprendedor, pero le quita las tareas operativas para que se enfoque en crecer.
*   **Slide count estimado:** 5-6 slides.

### Bloque 2: Conceptos Clave (Sin Jerga)
*   **Título:** "IA para no-técnicos: Lo que necesitas saber"
*   **Duración:** 30 minutos
*   **Objetivo:** Desmitificar términos como LLM, Prompt, Token y Contexto sin entrar en código.
*   **Dinámica:** Charla interactiva + Ejemplo en pantalla (comparar un prompt malo vs uno bueno).
*   **Key Takeaway:** La calidad de tu asistente depende 100% de la calidad de tus instrucciones (prompting).
*   **Slide count estimado:** 8-10 slides.

### Bloque 3: Demo en Vivo
*   **Título:** "Construyendo un asistente en 15 minutos"
*   **Duración:** 20 minutos
*   **Objetivo:** Mostrar el proceso end-to-end: definir rol, subir conocimiento y probar.
*   **Dinámica:** Demo en vivo del facilitador compartiendo pantalla.
*   **Key Takeaway:** No necesitas programar; necesitas definir instrucciones claras y alimentar con datos de tu negocio.
*   **Slide count estimado:** 3 slides (principalmente pantalla compartida).

### Bloque 4: Laboratorio Práctico (El núcleo)
*   **Título:** "Manos a la obra: Construye tu asistente"
*   **Duración:** 75 minutos
*   **Objetivo:** Cada participante cree un asistente funcional para un caso de uso real de su startup.
*   **Dinámica:** Ejercicio individual con apoyo del facilitador y asistentes (circulan por la sala ayudando).
*   **Key Takeaway:** Salen del workshop con un prototipo funcional, no solo con teoría.
*   **Slide count estimado:** 2 slides (instrucciones del ejercicio y temporizador).

### Bloque 5: Show & Tell
*   **Título:** "Muestra lo que construiste"
*   **Duración:** 15 minutos
*   **Objetivo:** Validar aprendizajes, inspirar a otros y recibir retroalimentación inmediata.
*   **Dinámica:** 3-4 voluntarios comparten su pantalla (2 min cada uno) y explican para qué sirve su asistente.
*   **Key Takeaway:** Hay múltiples formas de usar la IA; aprender de los pares acelera el aprendizaje.
*   **Slide count estimado:** 1 slide.

### Bloque 6: Cierre y Próximos Pasos
*   **Título:** "De prototipo a producción"
*   **Duración:** 5 minutos
*   **Objetivo:** Dar ruta de continuación y cerrar con energía.
*   **Dinámica:** Charla de cierre + entrega de recursos digitales.
*   **Key Takeaway:** El asistente es un MVP; ahora lo prueban con clientes reales y lo iteran.
*   **Slide count estimado:** 3-4 slides.

---

## 4. Ejercicio Principal del Workshop

**Nombre:** "Tu Asistente de Operaciones en 60 minutos"

**Descripción:**
Cada emprendedor identificará **una tarea repetitiva** de su startup que consuma tiempo (ej: responder preguntas frecuentes de clientes, redactar publicaciones para redes sociales, calificar correos de prospectos, resumir notas de reuniones).

**Pasos del ejercicio:**
1.  **Definir el Rol:** "Actúas como un experto en atención al cliente para una startup de delivery de comida saludable..."
2.  **Alimentar el Contexto:** Subir un PDF, pegar texto de preguntas frecuentes o pegar ejemplos de respuestas ideales.
3.  **Configurar Instrucciones:** Definir tono de voz, limitaciones (qué no debe decir) y formato de salida.
4.  **Probar e Iterar:** Hacer 3-5 pruebas de conversación reales y ajustar el prompt según los resultados.

**Criterio de éxito:** El asistente responde correctamente al menos 3 preguntas simuladas de un cliente real.

---

## 5. Recursos para Llevar a Casa

Al finalizar el workshop, se envía por email un kit digital que incluye:

1.  **Guía de Prompting para Emprendedores:** Ejemplos de prompts para ventas, atención al cliente y operaciones.
2.  **Lista de Herramientas No-Code de IA:** Comparativa de plataformas (Custom GPTs, Poe, ManyChat, Voiceflow, etc.) con precios y pros/contras.
3.  **Plantilla de "Instrucciones del Asistente":** Un documento editable para que puedan seguir creando más asistentes.
4.  **Acceso a la Comunidad:** Link a un grupo de WhatsApp o Discord de ex-alumnos para seguir resolviendo dudas.
5.  **Grabación del Demo:** Video corto del facilitador construyendo el asistente de ejemplo (para repasar en casa).

---

## 6. Slide Count Estimado por Sección

| Sección | Slides Estimados | Enfoque Visual |
| :--- | :--- | :--- |
| Bienvenida | 5-6 | Fotos de startups latinoamericanas, frases motivadoras. |
| Conceptos | 8-10 | Diagramas simples, comparativos "Antes vs Después", íconos. |
| Demo en Vivo | 3 | Pantalla compartida (mínimo slides). |
| Laboratorio | 2 | Instrucciones paso a paso y temporizador. |
| Show & Tell | 1 | Slide de "¿Quién quiere compartir?". |
| Cierre | 3-4 | QR codes, links de recursos, datos de contacto. |
| **Total** | **22-26 slides** | |

---

### 💡 Tips del Facilitador (Experiencia en LatAm)

1.  **Conectividad:** En muchos países de la región el Wi-Fi falla. Ten un **hotspot personal** como respaldo y una versión offline de los recursos clave.
2.  **Nivel Técnico:** Evita palabras como "API", "Webhook" o "Fine-tuning". Usa "conectar", "enviar información" o "entrenar".
3.  **Energía:** Cada 45 minutos, haz una pausa activa de 2 minutos (estiramiento o pregunta rápida) para mantener la energía alta.
4.  **Idioma:** Usa ejemplos locales (ej: asistente para una tienda de ropa en Mercado Libre, o para una app de delivery local) en lugar de ejemplos de Silicon Valley.

¡Listo para facilitar! Si necesitas el guion detallado de algún bloque o la plantilla de prompts, avísame. 🚀