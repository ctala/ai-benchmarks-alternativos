# Qwen 3.5 397B — startup_content/workshop_outline

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 8.26 | quality: 9.72
- latency_total: 39.895s | tokens_per_second: 59.1
- input_tokens: 204 | output_tokens: 2359
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

¡Hola, futuros unicornios de Latinoamérica! 🚀🦄

Como facilitador que ha visto nacer cientos de ideas desde Ciudad de México hasta Buenos Aires, sé que el mayor miedo del emprendedor no técnico es quedarse atrás con la Inteligencia Artificial. Pero les tengo una noticia: **no necesitan saber programar para tener un superpoder hoy mismo.**

Este workshop está diseñado para ser **100% "manos a la obra"**. Nada de teoría aburrida; vamos a salir de aquí con una herramienta real funcionando para su startup.

Aquí tienen el plan de batalla para **"Construye tu Asistente de IA para tu Startup"**.

---

### 🛠️ 2. Materiales Necesarios (Pre-Workshop Checklist)

Para que esto fluya sin fricciones técnicas (el enemigo #1 en LatAm), preparemos todo antes:

*   **Para los Participantes:**
    *   Laptop cargada (aviso previo: traer cargador).
    *   Cuentas creadas y activas en:
        *   [ChatGPT](https://chat.openai.com) o [Claude.ai](https://claude.ai) (Nivel gratuito sirve, pero recomendar Premium si pueden).
        *   [Zapier](https://zapier.com) o [Make.com](Make es más visual y barato, ideal para startups).
        *   Google Sheets / Notion (donde guardan sus datos).
    *   Conexión a Wi-Fi robusta (tener un hotspot de respaldo por si falla la red del venue).
*   **Para el Facilitador:**
    *   Proyector y pantalla grande.
    *   Pizarra blanca + marcadores de colores (para mapear flujos).
    *   **Cheat Sheet Impreso:** Una hoja con los "Prompts Maestros" y pasos clave (nadie quiere escribir URLs largas).
    *   Cuenta demo pre-configurada con un caso de éxito listo para mostrar.
    *   Música energética para los momentos de trabajo individual (playlist "Deep Focus" o "Latino Tech Vibes").

---

### ⏱️ 3. Agenda Detallada (3 Horas)

| Tiempo | Bloque | Actividad Principal |
| :--- | :--- | :--- |
| **00:00 - 00:20** | **1. El Despegue: IA sin Código** | Charla inspiradora + Demo de impacto |
| **00:20 - 00:50** | **2. Diseñando el Cerebro de tu Asistente** | Dinámica de definición de rol y prompt engineering |
| **00:50 - 01:50** | **3. Manos a la Obra: Construcción Live** | **Ejercicio Principal** (Paso a paso guiado) |
| **01:50 - 02:00** | *Break Energético (Café/Mate)* | Networking rápido |
| **02:00 - 02:40** | **4. Prueba de Fuego y Iteración** | Testing en parejas y ajuste fino |
| **02:40 - 03:00** | **5. Pitch de Resultados y Cierre** | Demo flash + Recursos finales |

---

### 📝 4. Detalle de Cada Bloque

#### **Bloque 1: El Despegue: IA sin Código**
*   **Duración:** 20 min
*   **Objetivo:** Romper el mito de que "IA = Programación compleja" y mostrar el potencial inmediato.
*   **Dinámica:**
    *   *Charla Relámpago (5 min):* Casos reales de startups latinas usando IA simple para ahorrar 20 horas/semana.
    *   *Demo Impactante (10 min):* Mostrar un asistente respondiendo preguntas de clientes y agendando citas automáticamente en tiempo real.
    *   *Q&A Rápido (5 min).*
*   **Key Takeaway:** "La IA no reemplaza al fundador, pero el fundador que usa IA reemplaza al que no lo hace."
*   **Slides Estimados:** 5-7 slides (Visuales, poco texto, muchos GIFs/Demos).

#### **Bloque 2: Diseñando el Cerebro de tu Asistente**
*   **Duración:** 30 min
*   **Objetivo:** Definir claramente QUÉ hará el asistente y CÓMO debe comportarse (Contexto).
*   **Dinámica:**
    *   *Ejercicio Individual (15 min):* Llenar el "Canvas del Asistente" (Rol, Tarea, Tono, Restricciones).
    *   *Discusión en Parejas (10 min):* Validar si la tarea es clara o demasiado ambiciosa para 3 horas.
    *   *Feedback Flash (5 min):* El facilitador corrige 2-3 ejemplos en la pizarra.
*   **Key Takeaway:** Un mal prompt da resultados genéricos; un buen contexto da un empleado digital experto.
*   **Slides Estimados:** 4 slides (Plantilla del Canvas y ejemplos de buenos/malos prompts).

#### **Bloque 3: Manos a la Obra - Construcción Live (El Núcleo)**
*   **Duración:** 60 min
*   **Objetivo:** Tener un prototipo funcional conectado a una herramienta básica.
*   **Dinámica:**
    *   *Tutorial Guiado (Paso a paso):* El facilitador hace un paso, todos replican.
    *   *Enfoque:* Usaremos **ChatGPT Custom Instructions** (o un GPT personalizado) + **Zapier/Make** simple para conectar con Gmail o Sheets.
    *   *Soporte:* El facilitador y 1-2 ayudantes circulan resolviendo dudas técnicas ("¡No me logueo!", "¿Dónde está el botón?").
*   **Key Takeaway:** La barrera de entrada es baja; la magia está en la conexión de herramientas simples.
*   **Slides Estimados:** 10-12 slides (Capturas de pantalla grandes, flechas rojas indicando dónde hacer clic).

#### **Bloque 4: Prueba de Fuego y Iteración**
*   **Duración:** 40 min
*   **Objetivo:** Validar que el asistente funciona en escenarios reales y mejorarlo.
*   **Dinámica:**
    *   *Roleplay Cruzado (20 min):* El participante A actúa como "Cliente difícil" y prueba el asistente del participante B. Luego intercambian roles.
    *   *Iteración (15 min):* Ajustar el prompt basado en los fallos detectados ("Me contestó muy robot", "No entendió mi pregunta sobre precios").
    *   *Mini-Discusión (5 min):* ¿Qué fue lo más difícil de ajustar?
*   **Key Takeaway:** La IA necesita entrenamiento continuo; la primera versión nunca es la perfecta, pero sí la más rápida.
*   **Slides Estimados:** 3 slides (Checklist de pruebas: Claridad, Precisión, Tono).

#### **Bloque 5: Pitch de Resultados y Cierre**
*   **Duración:** 20 min
*   **Objetivo:** Celebrar logros y dar ruta de seguimiento.
*   **Dinámica:**
    *   *Demo Flash (10 min):* 3 voluntarios muestran su asistente en 60 segundos cada uno. ¡Aplausos asegurados!
    *   *Cierre Motivacional (5 min):* Cómo escalar esto mañana mismo.
    *   *Entrega de Recursos (5 min).*
*   **Key Takeaway:** Ya tienes la herramienta. Ahora, ¡a vender y ejecutar!
*   **Slides Estimados:** 4 slides (Resumen, QR de recursos, Foto grupal).

---

### 🧪 5. Ejercicio Principal del Workshop: "El Recepcionista Infinito"

**Descripción:**
Todos construirán un asistente capaz de recibir una consulta de cliente (simulada por email o formulario), analizar la intención, responder con el tono de la marca y registrar los datos en un Google Sheet automáticamente.

**Flujo que construirán (No-Code):**
1.  **Entrada:** Un correo electrónico llega a una dirección específica (o un webhook de prueba).
2.  **Procesamiento (IA):** Zapier/Make envía el texto a ChatGPT/Claude con un *System Prompt* definido en el Bloque 2 (ej: "Eres el experto en ventas de [Startup X], responde amablemente y extrae nombre y teléfono").
3.  **Acción 1:** La IA devuelve la respuesta y los datos estructurados.
4.  **Acción 2:** Zapier/Make envía la respuesta al cliente (borrador o automático) y guarda los datos en Google Sheets.

**Por qué este ejercicio:**
*   Es universal (todas las startups necesitan atender clientes).
*   Combina generación de texto (LLM) con automatización (Workflow).
*   Da un resultado tangible inmediato (ves el dato en tu Excel).

---

### 🎒 6. Recursos para llevar a casa (Digital Pack)

Al finalizar, los participantes escanearán un QR para descargar:

1.  **La Biblioteca de Prompts:** 10 plantillas de prompts probadas para Ventas, Soporte, RRHH y Marketing.
2.  **Video-Tutorial Grabado:** Una grabación de 15 mins repitiendo la construcción del ejercicio principal (por si se trabaron en algo).
3.  **Lista de Herramientas "Freemium":** Top 15 herramientas de IA gratuitas o baratas recomendadas para LatAm (evitando las que requieren tarjeta de crédito de EE.UU.).
4.  **Plantilla del "Canvas del Asistente":** En PDF editable.
5.  **Comunidad Slack/WhatsApp:** Invitación a un grupo exclusivo de "Fundadores No-Técnicos con IA" para seguir compartiendo trucos.

---

### 💡 Nota Final para el Facilitador (Tú)

Mantén la energía alta. Si alguien se traba con la tecnología (pasará), acércate rápido, sonríe y diles: *"Esto es normal, la tecnología a veces tiene celos, pero lo vamos a domar juntos"*. En Latinoamérica valoramos mucho la calidez humana; úsala para que pierdan el miedo a la máquina.

¡A construir el futuro! 🚀