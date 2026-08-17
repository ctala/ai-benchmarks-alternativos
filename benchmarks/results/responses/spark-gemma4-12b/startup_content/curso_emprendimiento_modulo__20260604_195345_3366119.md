# Gemma 4 12B (Spark llama-server Q4_K_M) — startup_content/curso_emprendimiento_modulo

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 8.06 | quality: 9.44
- latency_total: 62.142s | tokens_per_second: 25.2
- input_tokens: 238 | output_tokens: 1564
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí tienes la estructura del Módulo 3 diseñada bajo un enfoque de **aprendizaje práctico (hands-on)**, pensado para que un emprendedor pueda implementar soluciones sin necesidad de saber programar.

---

# Módulo 3: Automatización con IA: De la idea al flujo de trabajo

## 1. Objetivo del Módulo
Al finalizar este módulo, el emprendedor será capaz de identificar procesos repetitivos en su negocio y diseñar flujos de trabajo automatizados utilizando herramientas de integración (como n8n o Zapier). El objetivo es que el alumno pase de "hacer tareas manuales" a "supervisar sistemas", permitiéndole escalar su operación sin aumentar proporcionalmente su carga de trabajo.

---

## 2. Contenido Teórico: El "Cerebro" de tu Operación

### ¿Qué es la Automatización con IA?
No es simplemente hacer que una máquina haga algo sola; es **integrar la capacidad de razonamiento de la IA en tus procesos operativos**. Mientras que la automatización tradicional sigue reglas rígidas (Si pasa A, haz B), la automatización con IA permite que el sistema tome decisiones basadas en contexto (Si pasa A, usa la IA para analizarlo y decide si debe hacer B, C o D).

### El concepto de "Flujo de Trabajo" (Workflow)
Un flujo de trabajo es la secuencia de pasos que sigue un proceso. Para un emprendedor, automatizar significa conectar aplicaciones que ya usas (WhatsApp, Gmail, Google Sheets, Instagram) para que "hablen" entre sí sin que tú tengas que copiar y pegar datos.

### Herramienta Clave: n8n (y el ecosistema No-Code)
Para este curso, nos enfocaremos en **n8n**. ¿Por qué?
*   **Es visual:** Construyes tu automatización uniendo "nodos" (cajitas que representan acciones).
*   **Es potente:** A diferencia de otras herramientas, n8n permite manejar flujos complejos y conectar con casi cualquier software.
*   **Escalable:** Es ideal para startups que quieren ahorrar costos a largo plazo pero necesitan una infraestructura robusta.

> **Concepto clave:** *Trigger* (Disparador) $\rightarrow$ *Action* (Acción) $\rightarrow$ *AI Processing* (Procesamiento de IA).

---

## 3. Ejemplos Prácticos para Startups

### A. Atención al Cliente Automatizada (WhatsApp/Telegram)
*   **El problema:** El equipo pierde horas respondiendo preguntas frecuentes (precios, horarios, ubicación).
*   **La solución:** Un flujo donde el mensaje del cliente entra a n8n $\rightarrow$ la IA analiza la intención $\rightarrow$ busca la respuesta en una base de datos de conocimientos $\rightarrow$ responde automáticamente. Si la duda es compleja, el sistema escala el caso a un humano.

### B. Generación de Contenido para Redes Sociales
*   **El problema:** El emprendedor no tiene tiempo para planificar y redactar contenido diario.
*   **La solución:** Un flujo donde tú ingresas un link de un artículo o una idea en una fila de Google Sheets $\rightarrow$ la IA genera 5 captions para Instagram, un guion para TikTok y un hilo para X $\rightarrow$ el sistema envía los borradores a un canal de Slack para tu aprobación.

### C. Calificación Automática de Leads (Lead Scoring)
*   **El problema:** Recibes muchos formularios de contacto, pero no sabes cuáles son los clientes "calientes" que están listos para comprar.
*   **La solución:** Cuando alguien llena un formulario $\rightarrow$ la IA analiza el presupuesto mencionado, el tamaño de la empresa y la urgencia $\rightarrow$ asigna una puntuación del 1 al 10 $\rightarrow$ si es mayor a 8, envía un correo de agendamiento automático; si es menor, lo añade a una secuencia de nutrición de emails.

---

## 4. Ejercicio Práctico: "Tu primer flujo de calificación de leads"

En este ejercicio, vas a construir un sistema que analice automáticamente los mensajes de interés de tus clientes potenciales.

**Escenario:** Un cliente potencial te escribe por un formulario web diciendo qué servicio necesita y cuál es su presupuesto.

**Pasos a seguir:**

1.  **Preparación (Inputs):** Crea un formulario simple (puedes usar Google Forms o Typeform) con dos preguntas: *"¿Qué servicio necesitas?"* y *"¿Cuál es tu presupuesto aproximado?"*.
2.  **Configuración del Trigger:** En n8n (o Zapier), crea un nuevo flujo y selecciona el nodo de "Google Forms" o "Webhook". Conéctalo para que cada vez que alguien responda, el flujo se active.
3.  **Procesamiento con IA:** Añade un nodo de "OpenAI" (o similar). Configura el *prompt* de la siguiente manera:
    > *"Actúa como un experto en ventas. Analiza la siguiente respuesta de un cliente: [Datos del formulario]. Determina si es un cliente de 'Alta Prioridad' (presupuesto > $1000 y necesidad clara) o 'Baja Prioridad'. Responde solo con la categoría y una breve razón de 10 palabras."*
4.  **Acción Final (Output):** Añade un nodo de "Gmail" o "Slack".
    *   *Condición:* Si la IA dice "Alta Prioridad", envía un mensaje a tu Slack diciendo: "¡Nuevo lead caliente! Contactar de inmediato".
    *   *Condición:* Si es "Baja Prioridad", añade al cliente a una hoja de cálculo de "Seguimiento Futuro".
5.  **Prueba:** Llena tu propio formulario con datos de un "cliente ideal" y verifica que el mensaje llegue a tu Slack/Email.

---

## 5. Recursos Adicionales

*   **Video Tutorial:** "Introducción a n8n para no-técnicos" (Enlace interno al curso).
*   **Plantilla de Prompts:** Documento PDF con 10 prompts de clasificación de clientes.
*   **Comunidad:** Acceso al canal de Discord "Automatización Startup" para compartir tus flujos de trabajo.
*   **Guía de Precios:** Comparativa de costos entre n8n (Self-hosted vs Cloud) y Zapier.

---

## 6. Preguntas de Autoevaluación

1.  **¿Cuál es la principal diferencia entre una automatización tradicional y una automatización con IA?**
    *(Respuesta esperada: La IA permite tomar decisiones basadas en contexto y lenguaje natural, no solo seguir reglas fijas de "si pasa A, haz B").*
2.  **En el flujo de "Calificación de Leads", ¿cuál es la función del nodo de IA?**
    *(Respuesta esperada: Analizar la información del cliente y decidir automáticamente si es una prioridad alta o baja basándose en criterios predefinidos).*
3.  **Si quieres ahorrar costos y tienes un proceso que requiere mucha lógica, ¿por qué elegirías n8n sobre herramientas más simples?**
    *(Respuesta esperada: Porque n8n permite flujos más complejos, mayor flexibilidad de nodos y es más económico a medida que el volumen de datos crece).*