# GLM 5.1 (NIM) — startup_content/workshop_outline

- model_id: `z-ai/glm-5.1`
- success: True  | final: 6.95 | quality: 9.44
- latency_total: 523.747s | tokens_per_second: 4.4
- input_tokens: 192 | output_tokens: 2282
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Hola, comunidad! Como facilitador que ha recorrido los ecosistemas de LatAm, sé que nuestros emprendedores tienen mucha garra pero poco tiempo (y menos paciencia para la teoría). Este workshop está diseñado para que se vayan en 3 horas con un asistente de IA **funcionando y ahorrándoles tiempo**, sin escribir una línea de código. 

Aquí tienes el outline completo:

---

# 🚀 Construye tu Asistente de IA para tu Startup - Workshop Práctico

**Público:** 20-30 emprendedores early-stage (no-tech)
**Duración:** 3 horas
**Filosofía:** Menos slides, más teclado. No venimos a hablar de IA, venimos a usarla.

---

## 2. Materiales Necesarios (Pre-workshop)
* **Para el facilitador:** Proyector, conexión a internet estable (vital), extensión de cables, marcadores y post-its.
* **Para los asistentes (MUST HAVE):** Laptop cargada (NO tablets), cuenta de Gmail creada, tarjeta de crédito/débito (para crear cuenta gratuita en OpenAI/ChatGPT Plus o Make.com trial - **aclarar en el registro que no se cobrará, es solo para validar**).
* **Setup del salón:** Islas de 4-5 personas (para apoyo mutuo, porque alguien siempre se olvida la contraseña).
* **Extras:** Café bien fuerte, agua, snacks con azúcar para la energía. Música indie/lo-fi para los ejercicios.

---

## 3. Agenda Detallada por Bloques

### Bloque 1: 🧠 Desmitificando la IA (De la teoría a la acción)
* **Duración:** 30 minutos
* **Objetivo:** Cambiar la mentalidad de "la IA es magia" a "la IA es un empleado becario muy rápido, pero que necesita instrucciones claras".
* **Dinámica:** Charla interactiva rápida + Demo de contraste. Mostrar un prompt vago ("hazme un plan de marketing") vs. un prompt estructurado con contexto de startup.
* **Key Takeaway:** La IA no te reemplaza, pero un emprendedor que usa IA sí reemplaza al que no. El secreto está en el **contexto**.
* **Slide count:** 8 slides (Corto y al grano).

### Bloque 2: 🏗️ Arquitectura de tu Asistente (El ADN)
* **Duración:** 45 minutos
* **Objetivo:** Definir qué hará exactamente el asistente y darle identidad antes de tocar la herramienta.
* **Dinámica:** Ejercicio de mapeo en papel + Discusión en parejas. No vamos a la computadora todavía. Usamos post-its para definir los 3 pilares del asistente.
* **Key Takeaway:** Un asistente que hace de todo, no hace nada bien. Empieza por **UN** problema doloroso de tu startup (ej. responder clientes, analizar competencia, onboarding).
* **Slide count:** 5 slides (Frameworks visuales).

### Bloque 3: ⚒️ Construcción en Vivo (Manos a la obra)
* **Duración:** 75 minutos (Incluye el Ejercicio Principal)
* **Objetivo:** Crear el Custom GPT (o Prompt Maestro) y conectarlo a una automatización básica.
* **Dinámica:** Demo paso a paso del facilitador + Ejercicio principal (los asistentes replican y personalizan). El facilitador camina por la sala ayudando a desbloquear.
* **Key Takeaway:** Tu asistente necesita "Instrucciones de Sistema" estrictas, tono de marca definido y base de conocimientos (PDFs) para no alucinar.
* **Slide count:** 4 slides (Solo pantallazos de guía visual de la herramienta).

### Bloque 4: 🧪 Prueba de Estrés y Refinamiento
* **Duración:** 45 minutos
* **Objetivo:** Encontrar los errores del asistente y corregirlos al vuelo.
* **Dinámica:** "Roulette de Startups" - Cada mesa intercambia su asistente con otra mesa y le hacen preguntas trampa para "romperlo". Luego, ajustan los prompts basados en los fallos.
* **Key Takeaway:** Tu primer prompt siempre va a fallar. La IA es iterativa: Prompt -> Resultado -> Ajuste -> Éxito.
* **Slide count:** 3 slides (Tips de debugging).

### Bloque 5: 🎯 Cierre y Próximos Pasos
* **Duración:** 15 minutos
* **Objetivo:** Mantener la motivación y dar recursos para que no se queden estancados al salir.
* **Dinámica:** Recap de 3 minutos, "Grito de guerra" (quién logró automatizar algo hoy) y entrega de recursos.
* **Key Takeaway:** La implementación empieza mañana. Usa tu asistente todos los días hasta que te aburra, luego evoluciónalo.
* **Slide count:** 2 slides (Contacto y QR de recursos).

---

## 4. Ejercicio Principal: "El Prompt Estructurado & Custom GPT"

**El Reto:** Cada emprendedor debe crear un "Asistente de Investigación de Mercado y Competencia" o un "Asistente de Respuestas a Clientes" (elegirán su dolor principal).

**Paso a Paso:**
1. **La Fórmula Mágica (15 min):** Usando la fórmula **R-T-C-V** (Rol - Tarea - Contexto - Voz), escriben en un documento el prompt base. 
   * *Ejemplo:* "Actúa como un Head de Customer Success de una fintech en LatAm (Rol). Tu tarea es responder consultas de clientes enojados por demoras en transferencias (Tarea). Nuestra app tuvo un downtime de 3 horas ayer (Contexto). Habla con empatía, profesional pero cercano, usa 'tú' y no ofrezcas soluciones técnicas, solo disculpas y tiempos estimados (Voz)."
2. **Subida a la Tool (20 min):** Entrar a ChatGPT Plus -> Explore -> Create. Pegar el prompt en las "Instructions".
3. **Alimentación de Conocimiento (20 min):** Subir 2 PDFs al Knowledge Base del GPT. (Previo al taller, les pediremos que traigan un PDF con su manual de marca y un PDF con su FAQ o un artículo de su industria).
4. **El Test de Fuego (20 min):** Hacerle 3 preguntas difíciles a su nuevo GPT y afinar las instrucciones si responde fuera de personaje.

---

## 5. Recursos para Llevar a Casa (Takeaway Kit)

Se entrega mediante un enlace (Notion o Google Drive) accesible con un QR en la última slide:

1. **El Playbook del Workshop:** PDF resumen de la fórmula R-T-C-V y los pasos para crear un Custom GPT.
2. **Biblioteca de Prompts para Startups LatAm:** 25 prompts listos para copiar y pegar (Pitch Deck analyzer, Email de ventas B2B, Generador de contenido para redes, Análisis de tendencia de mercado).
3. **Guía de Automatización No-Code (Make.com):** Tutorial en video de 10 minutos (grabado por el facilitador) sobre cómo conectar su nuevo GPT a Gmail o WhatsApp para que responda automáticamente.
4. **Comunidad (WhatsApp/Discord):** Acceso al grupo del taller para seguir haciendo preguntas los próximos 30 días.

---

## 6. Slide Count Estimado (Total: ~22 slides en 3 horas)

* **Bloque 1 (Desmitificando):** 8 slides
  * Slide 1: Título y reglas del juego (Laptops cerradas al inicio).
  * Slide 2: El mito de la IA vs. La realidad.
  * Slide 3: Demo: Prompt Vago vs. Prompt Pro.
  * Slide 4-8: Casos de uso reales en LatAm (Fintech, E-commerce, SaaS).
* **Bloque 2 (Arquitectura):** 5 slides
  * Slide 9: ¿Qué hace un asistente virtual? (Las 3 tareas).
  * Slide 10: Framework de identidad (Quién es, qué hace, qué NO hace).
  * Slide 11: Ejemplo visual en post-its.
  * Slide 12: Selección de la herramienta (Por qué Custom GPT hoy).
  * Slide 13: Instrucciones del ejercicio en papel.
* **Bloque 3 (Construcción):** 4 slides
  * Slide 14: Arquitectura de un Custom GPT (Instructions + Knowledge + Actions).
  * Slide 15: La Fórmula R-T-C-V desglosada.
  * Slide 16: Pantallazo de dónde subir los PDFs.
  * Slide 17: Pantallazo de dónde pegar el prompt.
* **Bloque 4 (Prueba de Estrés):** 3 slides
  * Slide 18: Reglas de la "Roulette de Startups" (Rompan al bot del compañero).
  * Slide 19: Tipos de errores comunes (Alucinaciones, tono incorrecto, fuga de datos).
  * Slide 20: Cómo arreglar el prompt basado en el error.
* **Bloque 5 (Cierre):** 2 slides
  * Slide 21: Resumen y el hábito del mañana.
  * Slide 22: QR de acceso a los Recursos para Llevar a Casa y contacto del facilitador.

---

**💡 Pro-Tip del Facilitador:** A la hora 1:45 (mitad del Bloque 3), la energía del salón va a bajar porque estarán leyendo y escribiendo en sus laptops. Ese es el momento de parar la clase 5 minutos, poner música a todo volumen (algo como Bad Bunny o Bizarrap para LatAm, ¡súper energético!), hacerles estirar las piernas y recargar café. ¡El ritmo lo es todo en un workshop práctico!