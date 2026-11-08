# Gemma 4 26B MoE (3.8B activos) — startup_content/workshop_outline

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 8.87 | quality: 10.0
- latency_total: 34.067s | tokens_per_second: 45.4
- input_tokens: 207 | output_tokens: 1548
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

¡Hola, emprendedor/a! Qué gusto saludarte. Como facilitador, sé que con este perfil (early-stage, no-técnicos) el mayor error es caer en la teoría de "qué es un LLM". A ellos no les importa la arquitectura de la red neuronal; les importa **cómo la IA les ahorra 10 horas a la semana o les ayuda a cerrar una venta.**

Aquí tienes el diseño de un workshop de alto impacto, diseñado para que salgan con algo "vivo" y funcional.

---

# 🚀 Workshop: Construye tu Asistente de IA para tu Startup

**Concepto Central:** "No aprendas a programar, aprende a delegar a la IA".
**Tono:** Energético, *hands-on*, orientado a resultados y con lenguaje de negocios.

---

## 🛠 1. Materiales Necesarios (Pre-Workshop)

**Para la Organización:**
*   **Conectividad:** WiFi de alta velocidad (crítico para 30 personas usando LLMs simultáneamente).
*   **Mobiliario:** Mesas redondas o agrupadas (fomenta el networking y el trabajo colaborativo).
*   **Hardware:** Proyector, sonido para videos y un micrófono (si el espacio es grande).

**Para los Participantes (Checklist de envío previo):**
*   **Cuentas listas:** Deben traer cuenta activa en **ChatGPT (Plus recomendado)** o **Claude.ai**.
*   **Laptop:** Obligatorio (no se puede hacer en celular).
*   **El "Problema":** Pedirles que traigan anotada una tarea repetitiva de su startup que odien hacer (ej: redactar correos de ventas, resumir feedback de clientes, crear posts de LinkedIn).

---

## 📅 2. Agenda Detallada (3 Horas)

### Bloque 1: El Mindset del "AI-First Founder" (25 min)
*   **Objetivo:** Cambiar la mentalidad de "herramienta de chat" a "miembro del equipo".
*   **Dinámica:** Charla disruptiva + Demo rápida de "Lo que la IA puede y NO puede hacer".
*   **Key Takeaway:** La IA no es un buscador (Google), es un pasante brillante pero distraído.
*   **Slide Count:** 5-7 slides.

### Bloque 2: Ingeniería de Prompts para Negocios (45 min)
*   **Objetivo:** Dejar de dar órdenes mediocres y empezar a dar instrucciones de alto nivel.
*   **Dinámica:** Charla técnica (pero sin código) + Ejercicio de "Prompt de la mala vs. Prompt de la buena".
*   **Key Takeaway:** El framework **R-C-E (Rol, Contexto, Ejecución)**.
*   **Slide Count:** 8-10 slides.

### Bloque 3: BREAK / Networking Activo (15 min)
*   *Tip de facilitador:* Pon música up-beat y mantén la energía alta.

### Bloque 4: EL CORE - Construcción de tu Asistente Personalizado (75 min)
*   **Objetivo:** Crear un "GPT personalizado" o un "System Prompt" que resuelva su problema real.
*   **Dinámica:** Ejercicio principal (ver sección abajo) + Mentoring 1-a-1 mientras recorres las mesas.
*   **Key Takeaway:** Un asistente tiene memoria, personalidad y un objetivo claro.
*   **Slide Count:** 3-5 slides (instrucciones visuales).

### Bloque 5: Demo Day & Feedback (20 min)
*   **Objetivo:** Validar lo construido y compartir aprendizajes.
*   **Dinámica:** "Pitch de 30 segundos": 5 voluntarios muestran su asistente y qué problema resuelve.
*   **Key Takeaway:** La validación de pares es el mejor feedback.
*   **Slide Count:** 1 slide (instrucciones de pitch).

### Bloque 6: Cierre y Roadmap de Implementación (10 min)
*   **Objetivo:** Evitar que el entusiasmo muera al salir del salón.
*   **Dinámica:** Charla de cierre + Entrega de recursos.
*   **Key Takeaway:** La IA es un músculo; si no la usas mañana, se atrofia.
*   **Slide Count:** 2 slides.

---

## 🎯 3. El Ejercicio Principal: "Mi Primer Empleado Digital"

Este es el corazón del workshop. No vamos a jugar con la IA, vamos a construir una herramienta de trabajo.

**Instrucciones para el emprendedor:**
1.  **Identificar:** Elige la tarea que anotaste antes de venir.
2.  **Definir el Rol:** No es "un chat", es "Tu Director de Marketing Senior" o "Tu Especialista en Customer Success".
3.  **Cargar Contexto:** El participante debe copiar y pegar en la IA información real de su startup (su misión, su cliente ideal, su tono de voz).
4.  **Crear el Protocolo:** Diseñar una serie de instrucciones paso a paso (SOP - Standard Operating Procedure) dentro del prompt.
    *   *Ejemplo:* "Si te paso un feedback de un cliente, primero clasifícalo en: Positivo, Crítico o Bug. Luego, redacta una respuesta empática siguiendo este tono..."
5.  **Testeo de Estrés:** Intentar "romper" al asistente dándole una instrucción mal redactada para ver cómo reacciona.

**Resultado esperado:** Al terminar, el emprendedor debe tener un chat guardado (o un GPT personalizado) que, con solo un comando, ejecute una tarea compleja de su startup.

---

## 🎁 4. Recursos para llevar a casa (The "Startup AI Toolkit")

No los dejes con las manos vacías. Entrega un PDF o un Notion con:
1.  **Cheat Sheet de Prompts:** Una lista de "Power Prompts" para: Ventas, Copywriting, Análisis de Datos y Estrategia.
2.  **Framework R-C-E:** Una tarjeta visual para recordar cómo estructurar prompts.
3.  **Directorio de Herramientas:** No solo ChatGPT. Incluye menciones a *Perplexity* (investigación), *Claude* (escritura creativa) y *Gamma* (presentaciones).
4.  **Lista de "Próximos Pasos":** Cómo conectar la IA con herramientas como Zapier o Make para automatizar procesos reales.

---

### 💡 Pro-Tip de Facilitador para ti:
Como son emprendedores, muchos estarán pensando en "cómo monetizar esto". Durante el bloque 4, mientras caminas por las mesas, lanza preguntas como: *"¿Cómo este asistente te permite escalar sin contratar a una persona más este mes?"*. Eso les vuela la cabeza y los conecta con el valor real de la tecnología.

**¡Mucho éxito con el workshop! Vas a transformar la forma en que ven su negocio.**