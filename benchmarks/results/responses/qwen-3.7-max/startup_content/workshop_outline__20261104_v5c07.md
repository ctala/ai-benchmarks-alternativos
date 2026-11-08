# Qwen 3.7 Max — startup_content/workshop_outline

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 8.44 | quality: 10.0
- latency_total: 38.4s | tokens_per_second: 53.1
- input_tokens: 204 | output_tokens: 2038
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores no técnicos, proporcionando un plan detallado y práctico para el workshop.

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

¡Hola! Qué excelente iniciativa. Como facilitador que ha trabajado con emprendedores desde Ciudad de México hasta Buenos Aires, te digo algo clave: **a los founders no-tecnicos no les importa cómo funciona el transformer, les importa cómo la IA les ahorra 10 horas a la semana o les ayuda a cerrar su primera venta.**

Este outline está diseñado para ser **100% "Hands-on"**. Cero teoría aburrida. Si no están tecleando o configurando, estamos perdiendo el tiempo. El objetivo es que salgan con un prototipo funcional, no con apuntes.

Aquí tienes el plan de batalla para tu workshop:

---

### 1. Agenda Detallada (3 Horas)

| Tiempo | Bloque | Actividad Principal | Energía |
| :--- | :--- | :--- | :--- |
| 00:00 - 00:20 | **Rompehielos & Mindset** | "El dolor más caro": Identificar cuellos de botella | 🔥 Alta |
| 00:20 - 00:50 | **Bloque 1: Prompting Estratégico** | De "Chat genérico" a "Experto en mi Startup" | 🧠 Foco |
| 00:50 - 01:00 | *Break* | Networking rápido + Hidratación | ☕ Relax |
| 01:00 - 02:15 | **Bloque 2: Construcción (Core)** | Creando el Asistente con Conocimiento Propio | 🛠️ Acción |
| 02:15 - 02:45 | **Bloque 3: Integración & Validación** | Probando el asistente y conectándolo al mundo real | 🚀 Velocidad |
| 02:45 - 03:00 | **Cierre & Next Steps** | Demo relámpago y hoja de ruta | 🎉 Celebración |

---

### 2. Materiales Necesarios (Pre-Workshop)

**Logística:**
*   Proyector y pantalla grande (para demos en vivo).
*   WiFi robusto (CRÍTICO: ten un hotspot de respaldo, el WiFi de venues siempre falla).
*   Enchufes/regletas suficientes (todos traerán laptop).

**Digitales (Enviar 48h antes):**
*   **Cuenta creada:** Todos deben llegar con cuenta en la herramienta elegida (Recomiendo **Voiceflow**, **Botpress** o **CustomGPT** por ser No-Code/Low-Code y tener planes gratuitos generosos).
*   **"Kit de Datos Dummy":** Un PDF/Notion con información ficticia de una startup (precios, FAQs, tono de marca) para quienes no tengan datos propios listos. *Nadie se puede quedar parado por falta de info.*
*   Slide deck y plantilla de prompts.

**Físicos:**
*   Post-its y marcadores (para mapear flujos antes de tocar la computadora).
*   Stickers de "IA Builder" (gamificación simple).

---

### 3. Desglose por Bloques

#### Bloque 1: Prompting Estratégico para Funders
*   **Duración:** 30 min
*   **Objetivo:** Entender que la IA no es magia, es gestión de contexto. Aprender a estructurar instrucciones para obtener resultados de negocio, no respuestas de Wikipedia.
*   **Dinámica:** **"Prompt Dojo"**. Muestras un prompt malo ("Escribe un email de ventas"). La audiencia lo critica. Luego muestras la versión mejorada con framework (Rol + Contexto + Tarea + Formato + Restricciones). Ejercicio individual de 5 min refinando un prompt para SU problema real.
*   **Key Takeaway:** "La calidad de la respuesta depende de la calidad del contexto que tú le das. Tú eres el CEO, la IA es el becario superdotado pero sin contexto."
*   **Slides estimados:** 5-7

#### Bloque 2: Construcción del Asistente (El Core)
*   **Duración:** 1h 15min
*   **Objetivo:** Configurar un chatbot/asistente que responda basándose EXCLUSIVAMENTE en los documentos de la startup (RAG básico sin código).
*   **Dinámica:** **"Build-Along Sincronizado"**. Tú proyectas tu pantalla paso a paso. Ellos replican en tiempo real.
    1. Subir base de conocimiento (PDF/Web).
    2. Configurar System Prompt (Personalidad/Tono).
    3. Definir reglas de seguridad (qué NO debe responder).
    4. Testear en el sandbox.
    *Nota:* Camina por el salón constantemente. Los problemas técnicos son individuales.
*   **Key Takeaway:** "Tu asistente ya sabe de tu negocio en 20 minutos. Lo difícil no es la tecnología, es curar tu información."
*   **Slides estimados:** 3-5 (Solo capturas de pantalla de la interfaz, nada de texto).

#### Bloque 3: Integración & Validación
*   **Duración:** 30 min
*   **Objetivo:** Sacar al asistente del laboratorio y entender cómo medir si sirve.
*   **Dinámica:** **"Stress Test entre Pares"**. Se juntan en parejas. Uno usa el asistente del otro intentando "romperlo" o hacer preguntas trampa. Feedback honesto de 3 minutos. Breve demo de cómo embeberlo en Notion, WhatsApp Web o sitio web (solo mostrar, no hacer).
*   **Key Takeaway:** "Un asistente que alucina es peor que no tener asistente. La validación humana es obligatoria antes de lanzar."
*   **Slides estimados:** 4-6

---

### 4. Ejercicio Principal: "El Clon de Soporte/Ventas"

Todos construirán el mismo tipo de activo para evitar dispersión, pero personalizado: **Un Asistente de Atención al Cliente / SDR Junior.**

*   **Paso 1:** Suben su Pitch Deck, FAQ o Documento de Precios (o usan el Kit Dummy).
*   **Paso 2:** Definen la personalidad: "Eres Ana, SDR de [Startup]. Tono: Empático pero directo. Objetivo: Calificar leads. Si no sabes la respuesta, di 'Déjame verificar con el equipo humano'".
*   **Paso 3:** Prueban 3 escenarios obligatorios:
    1. Pregunta básica sobre precios.
    2. Objeción difícil ("Es muy caro").
    3. Pregunta fuera de tema ("¿Quién ganó el mundial?").
*   **Por qué este ejercicio:** Es tangible, resuelve un dolor inmediato (tiempo perdido en soporte/ventas) y demuestra el valor de la IA personalizada vs. ChatGPT genérico.

---

### 5. Recursos para Llevar a Casa (El "Survival Kit")

No les des un PDF de 50 páginas que nadie leerá. Entrega un **Notion Dashboard** con:

1.  **Biblioteca de System Prompts:** 5 plantillas copiar-pegar para diferentes roles (Soporte, Copywriter, Analista de Datos).
2.  **Checklist de Seguridad IA:** 10 puntos para revisar antes de publicar un bot.
3.  **Directorio LatAm Tech:** Herramientas recomendadas con descuentos para startups latinas.
4.  **Video Grabado:** La sesión grabada (editada solo en la parte práctica) para repasar.
5.  **Comunidad:** Link a grupo de WhatsApp/Slack exclusivo para resolver dudas post-workshop (el networking vale tanto como el contenido).

---

### 6. Consejos de Facilitador "Pro" para LatAm

1.  **Maneja la brecha técnica:** Tendrás desde ex-banqueros hasta diseñadores. Usa analogías locales. *"El RAG es como darle un manual de operaciones a tu empleado nuevo, en lugar de esperar que adivine"*.
2.  **El "Valley of Despair":** A la hora 1:30, alguien va a frustrarse porque su bot responde mal. Normalízalo públicamente: *"Si su bot está fallando, ¡excelente! Están aprendiendo dónde están los límites. Eso es más valioso que si funcionara perfecto a la primera"*.
3.  **Enfoque en Costos:** En LatAm somos sensibles al ROI. Menciona siempre: *"Esto reemplaza X horas de trabajo o Y dólares en contratación"*.
4.  **No hagas live-coding complejo:** Usa herramientas visuales. Si algo falla en vivo, ten un video pre-grabado de respaldo. La vergüenza técnica mata la energía.
5.  **Energía:** Música latina-lofi de fondo durante los ejercicios. Movimiento constante. Pregunta nombres. Haz que se sientan parte de una tribu, no alumnos en un aula.

¡Mucho éxito en el workshop! Recuerda: **Hecho es mejor que perfecto.** Que construyan algo feo pero funcional hoy, y lo pulirán mañana.