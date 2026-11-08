# GLM 5 — startup_content/workshop_outline

- model_id: `z-ai/glm-5`
- success: True  | final: 8.39 | quality: 9.72
- latency_total: 44.053s | tokens_per_second: 50.4
- input_tokens: 196 | output_tokens: 2221
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

¡Hola, emprendedor! Como facilitador que ha recorrido el ecosistema LatAm, te digo algo: los emprendedores early-stage no necesitan una clase magistral sobre redes neuronales; necesitan **ahorrar tiempo, validar más rápido y parecer equipos más grandes de lo que son**. 

Aquí tienes el outline diseñado para ser una experiencia de 3 horas, 100% práctica, donde nadie se queda dormido y todos se van con su primer "empleado de IA" funcionando.

---

# 🚀 Construye tu Asistente de IA para tu Startup - Workshop Práctico

**Duración:** 3 horas (180 min)
**Audiencia:** 20-30 emprendedores early-stage (no-tecnicos)
**Enfoque:** 20% Inspiración / 80% Ejecución

## 🎒 Materiales Necesarios (Preparación previa)
*   **Para el Facilitador:** Proyector, adaptadores de carga (crucial para un workshop de 3h), pizarra/rotafolio y marcadores.
*   **Para los Asistentes (Instrucción previa por email):** Traer laptop cargada, crear una cuenta gratuita en ChatGPT (o Claude) y traer 1 tarea específica que les quite mucho tiempo en su startup (ej: responder emails de clientes, redactar posts para LinkedIn, analizar competencia).
*   **Acomodación:** Mesas en formato "caballete" (grupos de 4-5 personas) para fomentar la colaboración y que se ayuden entre sí.

---

## 📋 Agenda Detallada y Bloques

### Bloque 1: El Nuevo Co-Founder de tu Startup
*   **Duración:** 30 minutos
*   **Objetivo:** Cambiar la mentalidad de "la IA es magia" a "la IA es un asistente que necesita instrucciones claras". Desmitificar la tecnología.
*   **Dinámica (Charla interactiva + Demo relámpago):** 
    *   *Charla (10 min):* ¿Por qué los solopreneurs y equipos early-stage quiebran? Por intentar hacer de todo. La IA es el primer "levantamiento de capital" que no te quita equity. 
    *   *Demo (20 min):* Muestra en pantalla cómo un prompt básico ("escribe un email") da un resultado mediocre, y cómo un prompt estructurado da un resultado de nivel senior.
*   **Key Takeaway:** La IA no lee mentes; lee contexto. Basura entra, basura sale.
*   **Slide count estimado:** 8 slides (Visuales grandes, poco texto).

### Bloque 2: La Fórmula del Prompt Perfecto (Sin ser ingeniero)
*   **Duración:** 45 minutos
*   **Objetivo:** Dotarlos de un framework replicable para comunicarse con cualquier modelo de IA.
*   **Dinámica (Charla corta + Ejercicio individual):**
    *   *Charla (15 min):* Enseñar la fórmula **CREA** (Contexto, Rol, Especificidad, Acción/Tono). Explicar qué es el "Few-Shot Prompting" (dar ejemplos) sin usar palabras técnicas.
    *   *Ejercicio (30 min):* Los asistentes tomarán la tarea que trajeron de casa y escribirán un prompt usando la fórmula CREA. El facilitador y los ayudantes (si los hay) caminan por las mesas ayudando a "destilar" las instrucciones. Cada uno prueba su prompt en ChatGPT/Claude.
*   **Key Takeaway:** Un buen prompt es como un TDR (Términos de Referencia) para un freelancer. Si no lo entiende un humano, no lo entenderá la IA.
*   **Slide count estimado:** 5 slides (Una con la fórmula, otra con un ejemplo mapeado, el resto de tiempo trabajando en sus laptops).

### ☕ Break de Networking y Café (15 min)
*   **Objetivo:** Oxigenar el cerebro, recargar baterías para la laptops y que hablen de sus startups. (Esencial en un workshop de 3 horas).

### Bloque 3: El Ejercicio Principal - Construye tu "Agente Especializado"
*   **Duración:** 45 minutos
*   **Objetivo:** Crear un sistema reutilizable (Custom GPT o Prompt Maestro) que actúe como un departamento específico de su startup.
*   **Dinámica (Ejercicio principal - Ver detalle abajo):** Trabajo individual con validación de pares.
*   **Key Takeaway:** No necesitas programar para automatizar; necesitas saber estructurar el conocimiento de tu negocio.
*   **Slide count estimado:** 3 slides (Instrucciones del ejercicio, reglas de validación, cronómetro en pantalla).

### Bloque 4: Integración y Próximos Pasos
*   **Duración:** 45 minutos
*   **Objetivo:** Entender cómo conectar esta IA con sus herramientas diarias y crear un plan de acción post-workshop.
*   **Dinámica (Demo + Discusión grupal):**
    *   *Demo (20 min):* Mostrar cómo llevar el asistente al mundo real. Ej: Conectar el prompt a Zapier para que responda correos automáticamente, o cómo guardarlo como "Custom GPT" para no tener que pegar el prompt cada vez.
    *   *Discusión (15 min):* Ronda de "Aha moments". 3 voluntarios comparten qué construyeron y cómo lo van a usar el lunes a las 8 AM.
    *   *Cierre (10 min):* Entrega de recursos y cierre energético.
*   **Key Takeaway:** La IA solo genera valor cuando se integra en tu flujo de trabajo diario, no cuando se queda en una pestaña abierta del navegador.
*   **Slide count estimado:** 6 slides (Demos visuales de integración, QR de recursos, slide final de cierre).

---

## 🛠️ Ejercicio Principal del Workshop: "Tu Primer Empleado Virtual"

**El Reto:** Cada emprendedor debe elegir un rol crítico que necesita en su startup hoy mismo (Ej: *Copywriter de Ventas, Analista de Competencia, Community Manager, Asistente Legal Básico*). Van a "entrenar" a la IA para que asuma ese rol.

**Paso a paso (45 min):**

1.  **Definir el Rol (5 min):** En un documento de texto, escriben: *"Necesito un [ROL] para mi startup que se dedica a [DESCRIPCIÓN DE LA STARTUP]"*.
2.  **Inyectar Conocimiento (10 min):** Escribir las instrucciones de la fórmula CREA. Aquí se les pide que suban a ChatGPT (si usan Plus) un PDF con su plan de negocios, tono de marca o ejemplos de contenido anterior. Si usan versión gratuita, pegan 2 o 3 ejemplos de texto directamente en el prompt.
3.  **Prueba de Fuego (15 min):** Le piden a su nuevo "empleado" que haga una tarea real. Ej: "Escribe el mensaje de bienvenida para mi nueva lista de correos" o "Analiza las 3 debilidades de mi competidor X".
4.  **Iteración de Pares / Peer Review (15 min):** Se ponen de pie, buscan a otra persona en la sala y se intercambian las laptops. El compañero debe interactuar con el Asistente de IA del otro y dar feedback: *"¿Sonó robótico? ¿Entendió bien el contexto de tu negocio?"*. Hacen ajustes finales.

*Resultado:* Se van con un asistente configurado, probado por un par y listo para usar.

---

## 🎒 Recursos para Llevar a Casa (Leave-behinds)

Al finalizar, se les envía por correo (o se proyecta un QR) un enlace a un Notion/Drive con:

1.  **El "Prompt Cheat Sheet" para Startups LatAm:** Un PDF de 1 página con la fórmula CREA y 5 plantillas de prompts listas para copiar/pegar (Validación de idea, Email de venta en frío, Post de LinkedIn, Análisis de competencia, Estructura de Pitch Deck).
2.  **Directorio de Herramientas No-Code:** Lista curada de herramientas de IA gratuitas o freemium para emprendedores (ChatGPT, Claude, Perplexity, Gamma para presentaciones, Gamma o Tome, y Zapier para automatizaciones).
3.  **Plantilla de "Custom GPT" en blanco:** Un documento estructurado con los campos vacíos (Contexto, Tono, Tareas, Limitaciones) para que puedan crear sus propios Custom GPTs en el futuro.
4.  **Comunidad:** Link a un grupo de WhatsApp exclusivo del workshop para compartir prompts y resolver dudas durante los siguientes 30 días.

---

### 💡 Tips del Facilitador para que sea un éxito:
*   **Manejo de la energía:** A las 2 horas, el público no-técnico sufre "fatiga de pantalla". Haz que el ejercicio de iteración (Paso 4) sea de pie. El movimiento físico cambia la energía de la sala.
*   **Expectativas de la IA:** Alguien se va a frustrar porque la IA "le inventó datos" (alucinación). Usa eso como aprendizaje en vivo: enséñales a agregar en su prompt la regla *"Si no sabes la respuesta o no tienes el dato en el contexto, di 'No tengo información', no inventes"*.
*   **Cero jerga:** Si te encuentras diciendo "LLM", "Parámetros" o "Temperatura", detente. Cámbialo por "Cerebro de la IA", "Nivel de creatividad" y "Reglas".