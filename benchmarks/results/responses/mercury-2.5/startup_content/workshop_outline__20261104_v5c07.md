# Mercury 2.5 — startup_content/workshop_outline

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.14 | quality: 9.72
- latency_total: 5.37s | tokens_per_second: 370.2
- input_tokens: 207 | output_tokens: 1988
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

¡Excelente iniciativa! Como facilitador con experiencia en el ecosistema de emprendimiento en Latinoamérica, sé que los fundadores no técnicos necesitan ver resultados tangibles rápido, no teoría densa. Este workshop está diseñado para que salgan con un prototipo funcional y la confianza para implementarlo.

Aquí tienes el outline completo para **"Construye tu Asistente de IA para tu Startup - Workshop Práctico"**.

---

### **1. Agenda Detallada (3 Horas)**

| Tiempo | Bloque | Actividad Principal |
| :--- | :--- | :--- |
| **00:00 - 00:15** | **Bienvenida y Contexto** | Rompehielo + Demo en vivo |
| **00:15 - 00:45** | **Módulo 1: La Lógica del Asistente** | Conceptos clave + Ejercicio de Prompting |
| **00:45 - 01:15** | **Módulo 2: Construcción (Hands-on)** | Creación del Chatbot (Taller) |
| **01:15 - 01:30** | **Descanso y Networking** | Café + Charla libre |
| **01:30 - 02:15** | **Módulo 3: Casos de Uso Reales** | Integración + Optimización |
| **02:15 - 02:45** | **Módulo 4: Presentación y Feedback** | Demo en grupo + Discusión |
| **02:45 - 03:00** | **Cierre y Siguientes Pasos** | Recursos + Q&A |

---

### **2. Materiales Necesarios (Preparación Previa)**

*   **Para los Asistentes:**
    *   Laptop (obligatorio).
    *   Cuenta creada previamente en la herramienta de IA (recomendado: **Flowise**, **Dify**, o **Coze** para interfaz visual sin código). *Nota: El facilitador debe enviar un link de registro 48h antes.*
    *   Cuentas en sus plataformas de negocio (ej. Slack, Email, Notion, Trello) para pruebas.
*   **Para el Facilitador:**
    *   Proyector y pantalla grande.
    *   Plantilla de "Prompt Maestro" (documento compartido).
    *   Ejemplos pre-entrenados de asistentes para mostrar.
    *   Wi-Fi robusto (crítico para talleres en vivo).

---

### **3. Desglose por Bloque**

#### **Bloque 1: Bienvenida y Contexto (15 min)**
*   **Objetivo:** Romper el hielo y mostrar el "Wow factor" inmediato.
*   **Dinámica:** Charla interactiva + Demo en vivo.
*   **Ejecución:**
    *   Presentación rápida del facilitador y objetivos.
    *   **Demo:** Mostrar un asistente que responde preguntas sobre la propia audiencia o datos en tiempo real (ej. "¿Quién aquí está trabajando en Fintech y qué es su mayor dolor?").
    *   Explicación visual: ¿Cómo funciona "bajo el capó" sin tecnicismos (Modelo + Datos + Instrucciones).
*   **Key Takeaway:** La IA no reemplaza a tu equipo, es el nuevo empleador digital que puedes entrenar en minutos.

#### **Bloque 2: La Lógica del Asistente (30 min)**
*   **Objetivo:** Entender cómo hablarle a la IA para obtener resultados consistentes.
*   **Dinámica:** Minicharla + Ejercicio de "Prompt Engineering" guiado.
*   **Ejecución:**
    *   Explicar la estructura: **Rol + Tarea + Contexto + Formato de Salida**.
    *   **Ejercicio:** Los participantes toman una tarea aburrida de su startup (ej. "Clasificar correos de clientes") y escriben un prompt. Luego lo prueban en un sandbox compartido y ven cómo cambiar el "Contexto" mejora el resultado.
*   **Key Takeaway:** La calidad de la IA depende de la claridad de tus instrucciones, no de la tecnología en sí.

#### **Bloque 3: Construcción (Hands-on) (30 min)**
*   **Objetivo:** Crear un prototipo funcional de su asistente.
*   **Dinámica:** Taller práctico guiado paso a paso.
*   **Ejecución:**
    *   Los participantes entran a la herramienta visual (ej. Flowise/Dify).
    *   **Paso 1:** Conectar un "Prompt" base.
    *   **Paso 2:** Subir documentos propios (PDF de producto, FAQ, Notion) como base de conocimiento (RAG básico).
    *   **Paso 3:** Configurar la interfaz de chat.
*   **Key Takeaway:** Tienes un asistente experto en tu producto funcionando en menos de 30 minutos.

#### **Bloque 4: Casos de Uso Reales (45 min)**
*   **Objetivo:** Integrar el asistente en flujos reales de la startup.
*   **Dinámica:** Demo de integraciones + Discusión en grupos pequeños.
*   **Ejecución:**
    *   Mostrar cómo conectar el bot a herramientas simples (Slack, WhatsApp Web, o un formulario web).
    *   **Actividad:** En parejas, identificar 3 oportunidades donde su asistente podría ahorrar 5 horas semanales (Ventas, Soporte, RRHH).
*   **Key Takeaway:** El valor real está en la integración, no en el chat en sí.

#### **Bloque 5: Presentación y Feedback (30 min)**
*   **Objetivo:** Validar las ideas y aprender de los pares.
*   **Dinámica:** Demo en grupo + Feedback colaborativo.
*   **Ejecución:**
    *   Invitar a 3-4 voluntarios a compartir su pantalla y mostrar cómo funciona su bot.
    *   Feedback rápido del grupo: "¿Qué te gustaría preguntar a este bot?".
*   **Key Takeaway:** La iteración rápida es clave; empieza con algo imperfecto y mejóralo.

#### **Bloque 6: Cierre y Siguientes Pasos (15 min)**
*   **Objetivo:** Entregar herramientas para continuar el viaje.
*   **Dinámica:** Cierre inspirador + Q&A.
*   **Ejecución:**
    *   Resumen de los 3 pilares aprendidos.
    *   Entrega del paquete de recursos.
    *   Invitación a comunidad/WhatsApp para soporte post-workshop.
*   **Key Takeaway:** Ya tienes los fundamentos para escalar tus operaciones con IA.

---

### **4. Ejercicio Principal del Workshop: "El Onboarding Automático"**

**Objetivo:** Que todos construyan un asistente que pueda explicar su producto a un usuario nuevo usando solo los documentos que ellos tienen a mano.

**Pasos para los participantes:**
1.  **Recopilación:** Tomar un PDF de "Documentación del Producto", una nota de Notion con "FAQs", o una hoja de cálculo con "Precios".
2.  **Ingesta:** Subir ese archivo a la herramienta de IA (usando la función de "Knowledge Base" o "Upload Document").
3.  **Instrucción:** Configurar el sistema: *"Actúa como un asesor de ventas experto de [Nombre de la Startup]. Responde solo basándote en los documentos subidos. Si no sabes la respuesta, di que consultarás con un humano."*
4.  **Prueba:** Hacer 3 preguntas difíciles que suelen hacer los clientes reales.
5.  **Resultado:** Un chatbot funcional listo para ser pegado en su sitio web o compartido en WhatsApp.

---

### **5. Recursos para Llevar a Casa**

*   **Cheat Sheet de Prompting:** Una hoja PDF con plantillas de prompts para Ventas, Soporte y Marketing.
*   **Listado de Herramientas "No-Code":** Top 5 plataformas para construir asistentes sin programar (con precios y casos de uso).
*   **Plantilla de Prompt de Sistema:** El prompt exacto usado en el taller para ser copiado y pegado.
*   **Acceso a Comunidad:** Link a grupo de WhatsApp/Slack para continuar preguntando dudas técnicas.

---

### **6. Slide Count Estimado**

*   **Intro y Contexto:** 4 slides (Enfoque en imágenes y ejemplos de impacto).
*   **Módulo 1 (Lógica):** 6 slides (Diagramas simples de flujo, ejemplos de "Bien vs Mal" en prompts).
*   **Módulo 2 (Construcción):** 4 slides (Capturas de pantalla de la interfaz paso a paso).
*   **Módulo 3 (Casos de Uso):** 5 slides (Estudios de caso reales, diagramas de integración).
*   **Cierre y Recursos:** 3 slides (Resumen, lista de herramientas, contacto).
*   **Total:** ~22 slides (Diseño limpio, poco texto, máximo impacto visual).