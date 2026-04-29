# GLM 5 (NIM) — startup_content/workshop_outline

- model_id: `z-ai/glm5`
- success: True  | final: 6.92 | quality: 9.2
- latency_total: 288.766s | tokens_per_second: 7.1
- input_tokens: 192 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Hola! Qué excelente iniciativa. Como facilitador en Latam, sé que el mayor pecado en estos workshops es ahogar a los emprendedores en teoría y jerga técnica. Nuestro objetivo aquí es que salgan con algo **funcional** que construyeron con sus propias manos y que les dé "superpoderes" desde el día 1. 

Aquí tienes el outline completo, diseñado con tono práctico, energético y enfocado 100% en acción.

---

# 🚀 CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP - WORKSHOP PRÁCTICO

**Duración:** 3 horas
**Audiencia:** 20-30 emprendedores early-stage (no-tecnicos)
**Regla de oro del facilitador:** Cero jerga, cero código, 100% acción.

---

## 1. AGENDA DETALLADA (3 Horas)

*   **00:00 - 00:20 | Bloque 1:** Encendiendo Motores: IA no es magia, es apalancamiento.
*   **00:20 - 00:40 | Bloque 2:** El Cerebro de tu Startup: Delegando tu "Pecho Frío".
*   **00:40 - 01:20 | Bloque 3:** Manos a la Obra: Creando tu Primer Asistente (Ejercicio Principal).
*   **01:20 - 01:35 | ☕ Break:** Cafe y networking (vital para procesar).
*   **01:35 - 02:00 | Bloque 4:** Demo Showcase: Viendo la Magia en Acción.
*   **02:00 - 02:40 | Bloque 5:** Nivelando Up: De Asistente a Proceso Automatizado.
*   **02:40 - 03:00 | Bloque 6:** Cierre y Kit de Vuelo.

---

## 2. MATERIALES NECESARIOS (Preparación previa)

*   **Para los asistentes (Traer):** Laptop cargada, cable de poder, y al menos **1 proceso/documento real** de su startup que les dé pereza hacer (ej. responder clientes, resumir reuniones, escribir posts).
*   **Tech del salón:** Proyector, pantalla grande, buena conexión Wi-Fi (¡crítico!), enchufes/regaderas suficientes.
*   **Facilitador:** Cuentas premium/plus activas de ChatGPT y/o Claude (para las demos), cuenta de Zapier o Make (plan gratis sirve para demo).
*   **Físico:** Post-its (2 colores), marcadores, hojas de papel (para el ejercicio de mapeo analógico previo a la pantalla).
*   **Digital:** Link a un Google Drive con los "Prompts Templates" y acceso al grupo de WhatsApp/Telegram del workshop.

---

## 3. DETALLE POR BLOQUE

### Bloque 1: Encendiendo Motores
*   **Duración:** 20 min
*   **Objetivo:** Cambiar el mindset de "la IA me va a reemplazar" a "la IA es mi primer empleado".
*   **Dinámica:** Charla interactiva rápida. Preguntar a la sala: *"¿Cuál es la tarea que más odian en su startup?"*. Mostrar casos reales (y latinos) de emprendedores 10x su productividad.
*   **Key Takeaway:** La IA no es un chat, es un empleado becado que no duerme y necesita instrucciones súper claras.

### Bloque 2: El Cerebro de tu Startup
*   **Duración:** 20 min
*   **Objetivo:** Identificar qué tareas son automatizables y cuáles no.
*   **Dinámica:** Ejercicio analógico en papel. Mapeo de "Pecho Frío". Cada emprendedor hace una lista de 3 tareas repetitivas y elige UNA para el ejercicio. Discusión rápida en parejas.
*   **Key Takeaway:** No intentes automatizar todo hoy. Empieza por la tarea que te quita más tiempo y menos pensamiento estratégico requiere.

### Bloque 3: Manos a la Obra (Ejercicio Principal)
*   **Duración:** 40 min
*   **Objetivo:** Construir el primer Custom GPT / Project en Claude funcional.
*   **Dinámica:** Ejercicio guiado paso a paso. El facilitador va lento en pantalla y los emprendedores replican en sus laptops. (Ver detalle en punto 4).
*   **Key Takeaway:** Un asistente sin contexto es tonto; un asistente con tu contexto y reglas es un experto.

### ☕ Break (15 min)

### Bloque 4: Demo Showcase
*   **Duración:** 25 min
*   **Objetivo:** Validar el trabajo hecho y generar inspiración cruzada.
*   **Dinámica:** 3-4 voluntarios pasan al frente, comparten pantalla y le hacen una pregunta en vivo a su recién creado Asistente de IA. El facilitador celebra y hace ajustes en vivo para mejorar la respuesta.
*   **Key Takeaway:** Tu asistente va a fallar al principio. Iterar el prompt es parte del proceso.

### Bloque 5: Nivelando Up
*   **Duración:** 40 min
*   **Objetivo:** Mostrar cómo conectar la IA a otras herramientas (sin código).
*   **Dinámica:** Demo impactante del facilitador. Mostrar cómo un correo en Gmail → dispara un Zapier/Make → alimenta a ChatGPT → devuelve un borrador de respuesta a un Google Doc. (No lo hacen ellos, solo ven el arte de lo posible). Luego, 15 min para que intenten hacer un Zap básico (ej. Gmail a ChatGPT).
*   **Key Takeaway:** La IA aislada en un chat es útil; la IA conectada a tus herramientas es una máquina de dinero.

### Bloque 6: Cierre y Kit de Vuelo
*   **Duración:** 20 min
*   **Objetivo:** Que se vayan con un plan de acción para los próximos 7 días.
*   **Dinámica:** Discusión final. Compromiso público: cada uno escribe en un post-it la 1 tarea que automatizarán esta semana y se lo llevan pegado al laptop.
*   **Key Takeaway:** Si no lo usas mañana, lo olvidas para siempre. La implementación es hoy.

---

## 4. EJERCICIO PRINCIPAL DEL WORKSHOP: "Tu Primer Empleado Virtual"

**Plataforma:** ChatGPT Plus (Custom GPTs) o Claude Pro (Projects). *Si alguien no tiene cuenta paid, se adapta usando "Custom Instructions" o System Prompts en la versión free.*

**Paso a Paso guiado por el facilitador:**

1.  **El Nombre y Rol (5 min):** Crear el GPT/Project. Ponerle un nombre (ej. "Sara la Copywriter" o "Carlos el Soporte"). Definir su rol principal en 1 frase.
2.  **El Contexto (10 min):** Subir el "Manual de la Startup". El facilitador pide que abran un documento de texto y escriban: *A quién le venden, cuál es su tono de voz (formal, chido, técnico), y cuáles son 3 cosas que NUNCA deben decir a un cliente*. Pegan esto en las instrucciones del Asistente.
3.  **La Base de Conocimiento (10 min):** Subir archivos reales. El facilitador pide que suban su pitch deck, un PDF de preguntas frecuentes, o 3 ejemplos de correos buenos que han enviado en el pasado. (¡Esto es la magia!).
4.  **Las Reglas de Juego (5 min):** Escribir 3 reglas estrictas. Ej: *"Regla 1: Nunca inventes precios. Regla 2: Si no sabes algo, di que lo vas a consultar con el equipo. Regla 3: Siempre termina con un llamado a la acción"*.
5.  **Prueba de Estrés (10 min):** Todos interactúan con su Asistente intentando "romperlo" o pidiéndole que haga la tarea difícil que eligieron en el Bloque 2.

---

## 5. RECURSOS PARA LLEVAR A CASA (El "Kit de Vuelo")

Se envía un link al terminar el workshop con:
1.  **El Prompt Bible:** 20 prompts listos para copiar-y-pegar organizados por área (Ventas, Marketing, Operaciones, Finanzas).
2.  **Template de "Job Description para IA":** Un Google Doc con la estructura exacta para crear instrucciones para nuevos Asistentes.
3.  **Grabación de la Demo de Automatización:** Un video corto (Loom) repitiendo la demo de Zapier/Make + ChatGPT para que la repitan en casa a su ritmo.
4.  **Comunidad:** Acceso al grupo de WhatsApp/Telegram del workshop para dudas de los próximos 30 días.

---

## 6. SL