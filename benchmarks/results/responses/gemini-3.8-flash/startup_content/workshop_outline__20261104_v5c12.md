# Gemini 3.8 Flash — startup_content/workshop_outline

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.19 | quality: 9.72
- latency_total: 33.282s | tokens_per_second: 94.5
- input_tokens: 188 | output_tokens: 3145
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

¡A ensuciarse las manos! Aquí tienes el diseño curricular y operativo completo para un workshop dinámico, sin rodeos teóricos y 100% enfocado en ejecución.

---

# Workshop: "Construye tu Asistente de IA para tu Startup"
* **Duración:** 3 horas (180 minutos)
* **Audiencia:** 20-30 fundadores early-stage no técnicos.
* **Promesa del workshop:** *“Entras con una idea en servilleta y sales con un asistente funcional resolviendo un cuello de botella real de tu operación.”*

---

## 1. Materiales y Preparación Previa

### Para el Facilitador:
* Proyector/pantalla + clicker + adaptador HDMI/USB-C.
* Pizarra/Flipchart con marcadores gruesos.
* Cronómetro visible (Timer en pantalla para dinámicas).
* Playlist de Spotify de fondo para los momentos de trabajo (Lo-fi o Deep House suave).
* Hoja de trampas impresa o digital con la "Plantilla del Prompt Maestro".

### Requisitos enviados a los Founders (48h antes):
* **Laptop con cargador** (obligatorio; no tablet, no celular).
* **Cuenta activa** en OpenAI (ChatGPT Plus recomendado para Custom GPTs, o cuenta gratuita en Claude.ai con Projects / Coze / Poe). *El workshop se adapta para que funcione incluso con cuentas gratuitas usando System Prompts*.
* **Tener a mano 1 documento real de su startup:** Un FAQ, un PDF de ventas, su manual de onboarding, o notas desordenadas sobre su propuesta de valor.

---

## 2. Agenda Detallada con Tiempos y Bloques

| Tiempo | Minutos | Bloque | Dinámica |
| :--- | :--- | :--- | :--- |
| 00:00 - 00:20 | 20 min | **Bloque 1:** El "Empleado Cero": De Juguete a Palanca de Crecimiento | Charla interactiva + Icebreaker |
| 00:20 - 00:50 | 30 min | **Bloque 2:** La Anatomía de un Asistente que no Alucina | Micro-charla + Demo en vivo |
| 00:50 - 01:40 | 50 min | **Bloque 3:** Hands-On Lab I: El "Cerebro" de tu Asistente | Ejercicio individual guiado |
| 01:40 - 01:55 | 15 min | **Break:** Café con Misión (Networking de validación) | Pausa activa |
| 01:55 - 02:35 | 40 min | **Bloque 4:** Hands-On Lab II: Construcción, QA y Hackeo Cruzado | Construcción en plataforma + Peer Testing |
| 02:35 - 02:55 | 20 min | **Bloque 5:** Show & Tell: 3 Founders al Escenario | Pitches en vivo + Feedback táctico |
| 02:55 - 03:00 | 05 min | **Cierre:** Próximos pasos y Kit de Supervivencia | Cierre y CTA |

---

## 3. Desglose de Cada Bloque

### Bloque 1: El "Empleado Cero" (20 min)
* **Objetivo:** Destruir el síndrome de "la IA solo sirve para redactar emails" y alinear la mentalidad: la IA es tu pasante hiper-rápido al que debes darle instrucciones ejecutivas.
* **Dinámica:** Charla ágil (10 min) + Dinámica relámpago en parejas (10 min): *"¿En qué tarea operativa estás perdiendo 5 horas a la semana que te impiden vender?"*.
* **Key Takeaway:** No automatices procesos que no existen. El asistente resuelve un dolor concreto de hoy, no tu fantasía de escala de dentro de dos años.
* **Slides estimadas:** 5 slides.

### Bloque 2: La Anatomía de un Asistente que no Alucina (30 min)
* **Objetivo:** Entender la fórmula R-C-T-R-O (Rol, Contexto, Tareas, Restricciones y Output) y cómo alimentar conocimiento sin tocar una sola línea de código.
* **Dinámica:** Micro-charla con "Live Coding sin código" (Demo en vivo). El facilitador proyecta su pantalla y crea en 8 minutos un bot roto a propósito, muestra por qué falla y luego aplica la fórmula para arreglarlo frente a todos.
* **Key Takeaway:** Un asistente no falla porque la IA sea "tonta", falla porque tu contexto fue ambiguo.
* **Slides estimadas:** 8 slides (pantallazos claros, nada de diagramas técnicos complejos).

### Bloque 3: Hands-On Lab I: El "Cerebro" de tu Asistente (50 min)
* **Objetivo:** Redactar la arquitectura del asistente (System Prompt + Knowledge Base) antes de tocar software.
* **Dinámica:** Ejercicio práctico individual. Cada founder llena el *Canvas del Asistente*:
  1. Definir caso de uso (Ventas, Soporte, Onboarding o Calificación de Leads).
  2. Redactar el System Prompt Maestro usando la plantilla oficial.
  3. Curar el archivo de conocimiento base (FAQs, políticas de precio, objeciones típicas).
  *El facilitador y monitores caminan por la sala desbloqueando cuellos de botella.*
* **Key Takeaway:** La ventaja competitiva de tu asistente no es el modelo de lenguaje (es el mismo para todos); son tus datos y tus reglas de negocio.
* **Slides estimadas:** 4 slides (instrucciones fijas en pantalla + timer regresivo).

---

### [01:40 - 01:55] Break: Café con Misión (15 min)
* **Consigna antes de salir:** *"En la fila del café, explícale a la persona de al lado en 30 segundos qué hace tu bot y pídele que te diga cuál sería la primera pregunta tramposa que le haría a tu negocio"*.

---

### Bloque 4: Hands-On Lab II: Construcción, QA y Hackeo Cruzado (40 min)
* **Objetivo:** Montar el asistente en la plataforma elegida (Custom GPT / Claude Projects / Coze) y someterlo a pruebas de estrés.
* **Dinámica:**
  * **20 min:** Construcción e inyección del documento de contexto en la herramienta.
  * **20 min (Hackeo Cruzado):** Intercambio de laptops con el compañero de al lado. Cada founder intenta "romper" el asistente del otro: sacarlo de personaje, pedirle descuentos no autorizados, o hacerle preguntas capciosas. Ajuste de restricciones en tiempo real.
* **Key Takeaway:** Tu cliente siempre va a intentar romper tu bot. La sección de "Restricciones" es el 80% de la seguridad de tu marca.
* **Slides estimadas:** 3 slides (Pasos de despliegue + Reglas del juego de Hackeo Cruzado).

### Bloque 5: Show & Tell: 3 Founders al Escenario (20 min)
* **Objetivo:** Validar resultados reales, elevar la energía y dar feedback constructivo en vivo.
* **Dinámica:** 3 voluntarios suben al proyector. 2 minutos de demo en vivo + 3 minutos de feedback del facilitador: *"¿Añade valor?", "¿Suena robótico?", "¿Cómo conectarlo a WhatsApp/Web?"*.
* **Key Takeaway:** Ver cómo otro founder no técnico construyó algo en 2 horas elimina permanentemente la barrera mental del "yo no sé programar".
* **Slides estimadas:** 2 slides (Criterios de evaluación y aplausos).

### Bloque 6: Cierre y Escalabilidad (5 min)
* **Objetivo:** Dejar claro el siguiente paso lógico (integraciones vía no-code como Make/Zapier) sin abrumar.
* **Dinámica:** Cierre inspirador, entrega del QR con recursos y foto grupal.
* **Key Takeaway:** Hoy construyeron el MVP. Mañana empieza la iteración con clientes reales.
* **Slides estimadas:** 2 slides.

---

## 4. Ejercicio Principal del Workshop: "El Calificador y Vendedor 24/7"

Todos los participantes desarrollan el mismo arquetipo adaptado a su propio negocio: **Un Asistente Calificador de Leads y Manejador de Objeciones.**

### Entregable que cada founder se lleva funcionando en su laptop:
1. **Un System Prompt Maestro estructurado:**
   * **Identidad:** *"Eres Sofía, la estratega de admisiones de [Startup X]..."*
   * **Objetivo:** Descubrir presupuesto, timing y dolor principal del prospecto en menos de 4 intercambios.
   * **Base de conocimiento integrada:** Matriz de objeciones (Precio, "Tengo que consultarlo", Competidores) y tabla de precios/planes.
   * **Guardrails (Límites estrictos):** Jamás inventar descuentos, no hablar de competidores de forma despectiva y redirigir siempre a un enlace de Calendly si el lead califica.
2. **Validación completada:** Al menos 5 pruebas de estrés ejecutadas y corregidas durante el ejercicio en parejas.

---

## 5. Recursos para Llevar a Casa (Take-Home Toolkit)

Se entrega vía QR / Link al finalizar:

1. **Notion Template: "Prompt Maestro Library":**
   * 5 prompts de sistema listos para copiar y pegar (Customer Support, SDR de Ventas, Internal Knowledge Ops, Onboarding de Usuario, Preparador de Pitches).
2. **Cheat Sheet de Guardrails (PDF 1 pág.):**
   * Frases exactas de restricción para evitar alucinaciones, fugas de datos confidenciales y respuestas fuera de tono.
3. **Guía No-Code de Conexión (Video/Tutorial de 10 min):**
   * "Cómo conectar este asistente a WhatsApp usando Make + Typebot / ManyChat sin saber programar".
4. **Directorio de Herramientas Gratuitas:**
   * Comparativa de plataformas según presupuesto (OpenAI, Claude, Coze, Flowise).

---

## 6. Slide Count Estimado Total

* **Total de diapositivas:** **24 slides**
  * Bloque 1: 5
  * Bloque 2: 8
  * Bloque 3: 4
  * Bloque 4: 3
  * Bloque 5: 2
  * Cierre: 2
* *Filosofía visual:* Fondos oscuros, tipografía grande, capturas de pantalla reales, cero bloques de texto denso. La atención debe estar en la laptop del participante, no en la pantalla del facilitador.