# Gemini 3.8 Flash — startup_content/workshop_outline

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 33.439s | tokens_per_second: 113.5
- input_tokens: 188 | output_tokens: 3795
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada y práctica para el workshop.

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

¡De una! Aquí tienes el diseño instruccional completo para el workshop. Está pensado para que nadie se quede dormido, nadie se frustre con tecnicismos y todos salgan con una herramienta lista para usar en sus negocios al día siguiente.

---

# 🚀 Workshop: "Construye tu Asistente de IA para tu Startup"

* **Audiencia:** 20–30 fundadores y operadores early-stage (no técnicos).
* **Duración:** 3 horas (180 minutos).
* **Enfoque:** 70% práctico, 30% conceptual. Cero teoría innecesaria, 100% aplicabilidad al ecosistema startup en LatAm.

---

## 📋 1. Agenda General (Resumen de Tiempos)

| Bloque | Minutos | Tema |
| :--- | :--- | :--- |
| **01** | 00:00 - 00:25 (25 min) | Bienvenida, Icebreaker & Desmitificando la IA |
| **02** | 00:25 - 00:55 (30 min) | Anatomía de un Asistente de Negocio (El Framework R.O.L.E.) |
| **03** | 00:55 - 01:10 (15 min) | Live Demo: Creando un Bot de Ventas en Vivo |
| **☕** | **01:10 - 01:25 (15 min)**| **Pausa Activa + Café + Asistencia Técnica** |
| **04** | 01:25 - 02:25 (60 min) | **MANOS A LA OBRA: Construcción de tu Asistente** |
| **05** | 02:25 - 02:45 (20 min) | "Battle Testing": Testeo cruzado entre fundadores |
| **06** | 02:45 - 03:00 (15 min) | Escalado No-Code, Recursos y Cierre |

---

## 🛠️ 2. Materiales y Preparación Previa

### Check-in para Asistentes (Enviar 48h antes por email/WhatsApp):
* **Laptop con cargador** (obligatorio; no tablet, no celular).
* **Cuentas activadas:**
  * Opción A (recomendada): ChatGPT Plus (para crear Custom GPTs).
  * Opción B (gratuita): Claude (Anthropic), Poe.com o Google AI Studio (proporcionar enlace alternativo para quienes no paguen suscripción).
* **Un archivo real de su startup:** PDF o Doc con su FAQ, catálogo de servicios, deck de pitch o manual de ventas básico (máx. 3-5 páginas).

### Setup del Espacio y Facilitador:
* **Proyector / Pantalla HDMI** con buena resolución.
* **Internet de alta velocidad** (mínimo 100 Mbps dedicados; si 30 personas usan IA a la vez, el WiFi suele colapsar).
* **Post-its de colores y marcadores Sharpie** en las mesas.
* **Plantilla impresa / One-Pager:** *"Canvas de Diseño de Asistente de IA"* (1 hoja física por participante).
* **Música ambiental lista** (lo-fi / synthwave con energía para los momentos de trabajo individual).

---

## 🧩 3. Desarrollo de Bloques

---

### BLOQUE 1: Bienvenida, Icebreaker & Desmitificando la IA
* **Duración:** 25 min (00:00 - 00:25)
* **Objetivo:** Romper la barrera del "no soy técnico", alinear expectativas y elevar la energía de la sala.
* **Dinámica:** Charla interactiva + Icebreaker relámpago.
  * *Icebreaker (7 min):* "Gira con tu vecino: dile tu nombre, qué hace tu startup y cuál es la tarea repetitiva que más odias hacer a la semana". (Levantar 3 respuestas al azar al aire).
  * *Contenido (15 min):* La IA no viene a reemplazar tu equipo; viene a multiplicar tu tiempo. Explicar LLMs con la analogía del **"Pasante Genial con Amnesia"**: es ultra inteligente, pero si no le das contexto claro, inventa cosas.
* **Key Takeaway:** *"La IA no falla por falta de inteligencia; falla por falta de contexto e instrucciones claras."*
* **Slides estimadas:** 6 slides (Bienvenida, Reglas de juego, Icebreaker, Analogía del Pasante, Casos de uso LatAm, Objetivo del día).

---

### BLOQUE 2: Anatomía de un Asistente (El Framework R.O.L.E.)
* **Duración:** 30 min (00:25 - 00:55)
* **Objetivo:** Enseñar a estructurar el sistema de instrucciones (System Prompt) de un asistente profesional.
* **Dinámica:** Charla práctica con deconstrucción de casos reales.
  * Presentación del **Framework R.O.L.E.**:
    * **R - Rol e Identidad:** Quién es, qué tono usa (ej. "¿Hablas como banquero o como founder en Medellín/CDMX?").
    * **O - Objetivo:** Qué problema exacto resuelve y qué NO debe hacer.
    * **L - Límites & Reglas (Guardrails):** Manejo de precios, qué decir si no sabe algo, reglas de seguridad.
    * **E - Ejemplos (Few-Shot Prompting):** Casos de éxito y cómo debe contestar paso a paso.
  * Diferencia entre un simple "Chat" y un "Asistente con Memoria y Archivos" (Knowledge base).
* **Key Takeaway:** *"Un buen prompt de sistema no es una conversación; es el manual de operaciones de tu pasante digital."*
* **Slides estimadas:** 8 slides (Framework ROLE, Ejemplos Bueno vs. Malo, Manejo de límites, Subida de contexto/Knowledge).

---

### BLOQUE 3: Live Demo: Creando un Bot en Vivo
* **Duración:** 15 min (00:55 - 01:10)
* **Objetivo:** Modelar el proceso de punta a punta para eliminar la fricción técnica.
* **Dinámica:** Demo en vivo en pantalla completa (OpenAI Custom GPT / Poe).
  * El facilitador toma un caso real de la audiencia (ej. "Startup de delivery B2B").
  * Abre la plataforma en vivo y aplica el Canvas ROLE.
  * Sube un PDF de 2 páginas ficticio (lista de precios y zonas de cobertura).
  * Lo pone a prueba en tiempo real: le pide una cotización y simula una objeción de cliente ("Está muy caro").
* **Key Takeaway:** *"En 10 minutos pasamos de una idea a una herramienta funcional que responde como el mejor vendedor de tu equipo."*
* **Slides estimadas:** 2 slides (Checklist de la demo, Enlace al Canvas).

---

### ☕ PAUSA ACTIVA (15 min) | 01:10 - 01:25
* Café, snacks, estirar piernas.
* *Soporte técnico al vuelo:* El facilitador y staff ayudan a quienes tuvieron problemas de login o dudas con herramientas.

---

### BLOQUE 4: MANOS A LA OBRA (Ejercicio Principal)
* **Duración:** 60 min (01:25 - 02:25)
* **Objetivo:** Que cada participante construya, configure y pruebe su propio asistente funcional.
* **Dinámica:** Taller práctico individual / por startups, con música de fondo y facilitador circulando por las mesas.
  * *(Ver detalle completo en la Sección 4).*
* **Key Takeaway:** *"No necesitas levantar una ronda para tener un equipo de soporte o prospección 24/7."*
* **Slides estimadas:** 3 slides (Instrucciones con temporizador en pantalla, Matriz de dudas frecuentes, QR con prompts de base).

---

### BLOQUE 5: "Battle Testing" (Testeo Cruzado)
* **Duración:** 20 min (02:25 - 02:45)
* **Objetivo:** Encontrar alucinaciones, fallos y pulir la experiencia de usuario del asistente.
* **Dinámica:** Dinámica en parejas.
  * Cada fundador le comparte el link de su asistente al compañero de al lado.
  * **Misión:** "Rompe el bot del vecino". Tienen 7 minutos para hacer preguntas tramposas, pedir descuentos absurdos o preguntar cosas fuera del alcance.
  * Feedback relámpago (3 min): "¿Qué hizo bien y dónde empezó a inventar cosas?".
  * Ajuste rápido de instrucciones (5 min).
  * 2 personas voluntarias muestran en pantalla el bot del otro y qué tan bien resistió.
* **Key Takeaway:** *"Si tu bot no resiste a tu colega en esta sala, no resistirá a un cliente real en WhatsApp."*
* **Slides estimadas:** 3 slides (Reglas del Battle Testing, Preguntas tramposas para probar, Preguntas de feedback).

---

### BLOQUE 6: Escalado No-Code, Recursos y Cierre
* **Duración:** 15 min (02:45 - 03:00)
* **Objetivo:** Mostrar la ruta hacia adelante (integraciones) y cerrar con máxima energía.
* **Dinámica:** Charla inspiracional + Demo visual rápida.
  * ¿Cómo conectar esto al mundo real?: Breve mención de Make.com / Zapier + WhatsApp Business API.
  * Entrega del repositorio de recursos y prompts listos.
  * Foto grupal obligatoria con puño arriba.
* **Key Takeaway:** *"Hoy construiste el cerebro; mañana lo conectas a los músculos de tu negocio."*
* **Slides estimadas:** 4 slides (Arquitectura No-Code simple, Qué sigue mañana, QR de recursos, Foto y despedida).

---

## 🎯 4. Ejercicio Principal del Workshop (Paso a Paso)

**Título:** *"De Cero a Asistente Operativo en 4 Fases"*

### Paso 1: Llenado del Canvas en Papel (15 min)
Antes de tocar el teclado, escriben a mano en su plantilla física:
1. **Nombre del Asistente** (ej. *Santi - Calificador de Leads para SaaS*).
2. **Rol & Tono:** "Habla como un asesor senior, cercano pero profesional, usando modismos neutros de LatAm".
3. **Misión Principal:** "Hacer 3 preguntas para ver si el lead tiene más de 5 empleados y agendar con Calendly".
4. **Reglas de Oro:** "Nunca des precios cerrados, nunca hables de la competencia X".

### Paso 2: Creación del Contexto Base (10 min)
* Redactan o copian en un `.txt` o `.pdf` la información clave:
  * Propuesta de valor de su startup.
  * Preguntas Frecuentes (FAQs) con respuestas ideales.
  * Enlace al link de agendamiento (Calendly/HubSpot).

### Paso 3: Configuración en la Plataforma (25 min)
* Ingresan a la herramienta (ChatGPT Custom GPTs / Claude Project / Poe Bot).
* Pegan el prompt del framework R.O.L.E. en las instrucciones.
* Suben el archivo de conocimiento (*Knowledge*).
* Desactivan funciones innecesarias (ej. DALL-E si es un bot de soporte de texto).

### Paso 4: Calibración Inicial (10 min)
* El creador hace 3 pruebas básicas:
  1. Saludo inicial (¿responde en el tono correcto?).
  2. Pregunta técnica sobre el PDF subido (¿revisa el archivo o inventa?).
  3. Objeción de venta.

---

## 📦 5. Recursos para Llevar a Casa (Takeaways)

Todos los asistentes escanean un código QR al final que da acceso a una carpeta de Notion/Drive con:

1. **El Prompt Vault para Startups:** 10 System Prompts testeados listos para copiar y pegar:
   * *Bot de Calificación de Leads B2B.*
   * *Customer Support para E-commerce / D2C.*
   * *Entrenador de Pitch para Inversionistas (Simulador de VC de LatAm).*
   * *Copywriter de Redes Sociales con la voz de marca.*
2. **El Canvas de Asistentes en PDF (imprimible):** Para que puedan replicar el proceso con sus equipos.
3. **Guía de Conexión No-Code (PDF de 3 páginas):** Diagrama simple explicando cómo conectar su asistente a WhatsApp usando Make.com y OpenAI API.
4. **Cheat Sheet de Prompt Engineering:** Errores comunes que hacen que tu bot alucine y cómo corregirlos en 1 línea.

---

## 📊 6. Slide Count Estimado Total

| Sección | N° de Slides |
| :--- | :--- |
| 1. Bienvenida e Intro | 6 |
| 2. Anatomía del Asistente (ROLE) | 8 |
| 3. Live Demo | 2 |
| 4. Ejercicio Principal | 3 |
| 5. Battle Testing | 3 |
| 6. Siguientes Pasos y Cierre | 4 |
| **TOTAL ESTIMADO** | **26 slides** |

*(La presentación es minimalista: capturas grandes, poco texto y foco total en la pantalla del facilitador o en las laptops de los founders).*