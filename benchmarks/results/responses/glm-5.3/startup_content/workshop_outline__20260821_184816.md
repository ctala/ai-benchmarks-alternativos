# GLM 5.3 — startup_content/workshop_outline

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.02 | quality: 9.72
- latency_total: 96.095s | tokens_per_second: 69.6
- input_tokens: 202 | output_tokens: 6685
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

# 🚀 Workshop: "Construye tu Asistente de IA para tu Startup"
### Outline completo — 3 horas | 20-30 emprendedores early-stage no-técnicos

**Filosofía del workshop:** 70% haciendo, 30% escuchando. Nadie sale con teoría — todos salen con un asistente de IA funcionando y un plan para los próximos 30 días.

---

## 1. AGENDA GENERAL (9:00 – 12:00)

| Hora | Bloque | Duración | Formato |
|------|--------|----------|---------|
| 9:00 | Bienvenida + Encendido | 10 min | Dinámica |
| 9:10 | La IA no es magia (contexto que importa) | 15 min | Charla corta |
| 9:25 | Anatomía de un asistente + Demo en vivo | 20 min | Demo |
| 9:45 | Diseña antes de construir: el Canvas | 25 min | Ejercicio individual |
| 10:10 | ☕ Break | 10 min | — |
| 10:20 | Manos a la obra: construye tu asistente | 50 min | Ejercicio guiado en 3 sprints |
| 11:10 | Stress test: "Rompe el asistente de tu compañero" | 20 min | Ejercicio en parejas |
| 11:30 | Show & Tell + aprendizajes | 15 min | Discusión |
| 11:45 | Tu plan de 30 días + cierre | 15 min | Charla + compromiso |
| 12:00 | Fin | | |

> ⏱️ **Tip de facilitador:** El bloque de construcción es sagrado. Si vas tarde, recorta la charla de contexto, nunca el tiempo de construir.

---

## 2. MATERIALES — CHECKLIST PRE-WORKSHOP

### Logística (1 semana antes)
- [ ] **WiFi probado con 30+ dispositivos conectados** (esto mata workshops de IA, en serio)
- [ ] 1 hotspot móvil de respaldo por cada 10 participantes
- [ ] Proyector + micrófono (si el salón es grande)
- [ ] Regletas/cables de poder suficientes
- [ ] Timer visible en pantalla + playlist energética
- [ ] **1 ayudante por cada 10 participantes** (estudiantes, mentores, equipo tuyo)

### Comunicación a participantes (3-5 días antes)
- [ ] Email/WhatsApp: "Trae laptop o celular cargado, crea tu cuenta gratis en [herramienta elegida], y trae info de tu startup: descripción, precios, 5 preguntas frecuentes de clientes, tono de tu marca"
- [ ] Encuesta rápida: ¿qué herramienta usan? ¿ChatGPT, Claude, Gemini, ninguna?

### Impresos y digitales
- [ ] **35 copias del Canvas del Asistente** (imprimir de más, siempre)
- [ ] Plumas y marcadores
- [ ] QR code → página de recursos (guía, prompts, grabación)
- [ ] Asistente de ejemplo YA construido (para el demo, nunca improvises en vivo sin red)
- [ ] Screenshots/video del demo grabado (plan B si se cae el internet)
- [ ] 2-3 cuentas demo de pago preparadas (para quien no logró crear cuenta)
- [ ] Grupo de WhatsApp creado y listo para compartir al cierre

---

## 3. DESGLOSE POR BLOQUE

---

### 🔥 BLOQUE 0: Bienvenida + Encendido (10 min)

**Objetivo:** Energía alta desde el minuto uno y romper el hielo tech ("no necesitas ser programador").

**Dinámica:**
- Bienvenida de 2 min: promesa del día — *"A las 12:00, todos ustedes van a tener un asistente de IA funcionando para su startup."*
- Dinámica rápida de 5 min: **"Levanta la mano si..."** — *...has usado ChatGPT alguna vez / ...te ha dado miedo que la IA te reemplace / ...tu startup tiene tareas repetitivas que odias.* (Genera risas, conecta al grupo, te da un pulso del nivel del salón.)
- Reglas del juego (3 min): no hay preguntas tontas, terminar > perfeccionar, ayúdense entre mesas.

**Key takeaway:** *"Hoy nadie se queda atrás. El que sabe más, ayuda al de al lado."*

**Slides: 3-4**

---

### 🧠 BLOQUE 1: La IA no es magia (15 min)

**Objetivo:** Contexto mínimo y relevante — qué puede y qué NO puede hacer un asistente de IA para una startup early-stage.

**Dinámica:** Charla corta y dinámica, con ejemplos de startups latam reales.
- Los 4 usos de oro para early-stage: **atención al cliente, contenido, calificación de leads, tareas operativas repetitivas**
- Qué es un "asistente" vs. usar ChatGPT suelto (la diferencia: contexto + instrucciones + conocimiento de TU negocio)
- El elefante en el salón: **alucinaciones** — la IA inventa con confianza. Regla de oro: *verifica antes de publicar.*
- Pregunta al aire: "¿Cuál es la tarea más repetitiva de su semana?" — 3 respuestas en voz alta

**Key takeaway:** *"Un asistente de IA no reemplaza tu criterio — multiplica tu tiempo. Tú eres el cerebro, la IA es el motor."*

**Slides: 10**

---

### 🎬 BLOQUE 2: Anatomía de un asistente + Demo en vivo (20 min)

**Objetivo:** Que vean, en vivo, que construir un asistente toma 15 minutos y no 15 meses.

**Dinámica:** Demo en vivo proyectada (5 min de teoría + 15 min de demo).
- Teoría exprés: **los 5 ingredientes de todo asistente:**
  1. **Identidad** (quién es y para qué existe)
  2. **Conocimiento** (info de tu negocio)
  3. **Tono** (cómo habla)
  4. **Límites** (qué NO debe hacer ni decir)
  5. **Formato de respuesta** (cómo estructura sus respuestas)
- **Demo en vivo:** construyes "Sofía", asistente de FAQ para un emprendimiento ficticio latam (ej. tienda de café de especialidad por suscripción). Construyes desde cero frente a ellos: escribes las instrucciones, pegas las FAQs, y pruebas con preguntas reales — incluida una pregunta trampa para mostrar cómo falla y cómo se corrige.
- **Momento clave del demo:** muestra el asistente fallando y arréglalo en vivo. Esto baja la ansiedad: fallar es parte del proceso.

**Key takeaway:** *"Un asistente = instrucciones claras + información de tu negocio. Eso es todo. No hay código."*

**Slides: 5** (la demo es en vivo, las slides solo tienen los 5 ingredientes)

---

### ✏️ BLOQUE 3: Diseña antes de construir — El Canvas del Asistente (25 min)

**Objetivo:** Cada participante define el blueprint de SU asistente en papel antes de tocar la tecnología.

**Dinámica:** Ejercicio individual con canvas impreso (15 min) + discusión en tríos (10 min).
- Facilitador proyecta el canvas y llena uno de ejemplo en 3 minutos
- Participantes llenan su canvas:
  1. **Nombre del asistente**
  2. **Usuario:** ¿quién lo va a usar? (clientes, tú, tu equipo)
  3. **Las 3 tareas** que resolverá (solo 3 — el error #1 es querer que haga todo)
  4. **Tono:** elige 3 adjetivos (ej. cercano, directo, con humor)
  5. **Conocimiento:** ¿qué info necesita? (precios, FAQs, proceso de entrega)
  6. **Límites:** qué NO debe hacer (inventar precios, dar promociones, hablar de temas X)
  7. **3 preguntas de prueba** que un usuario real le haría
- En tríos: se presentan sus canvases y se dan feedback mutuo — *"¿Es claro? ¿Le falta información?"*

**Key takeaway:** *"El 80% de la calidad de tu asistente se define ANTES de tocar la herramienta. Diseñar en papel es gratis; corregir en producción, caro."*

**Slides: 5**

---

### ☕ BREAK (10 min)

Música, café, y los ayudantes resuelven cuentas/tech issues pendientes. **Aprovecha para que nadie llegue al build sin cuenta funcional.**

---

### 🛠️ BLOQUE 4: Manos a la obra — Construye tu asistente (50 min)

**Objetivo:** TODO el mundo construye su asistente funcional, paso a paso, con soporte.

**Dinámica:** Ejercicio guiado en 3 sprints. Slides de referencia permanecen en pantalla durante todo el bloque. Tú y los ayudantes circulan sin parar.

**Niveles según herramienta (todos llegan a la meta):**
- **Nivel A:** ChatGPT Plus → Custom GPT
- **Nivel B:** Claude Pro → Project
- **Nivel C (gratis):** Gemini → Gem, o "mega-instrucción" guardada en notas para pegar en cualquier chat

**Sprint 1 — Crear (15 min):** Configuración básica + escribir las instrucciones usando su canvas (identidad, tareas, tono, límites). *Anuncian al terminar golpeando la mesa.* 🥁

**Sprint 2 — Alimentar (15 min):** Pegan el conocimiento de su negocio (FAQs, precios, descripción). Aquí es donde el asistente pasa de genérico a SUYO.

**Sprint 3 — Probar y refinar (20 min):** Le hacen las 3 preguntas de prueba de su canvas. Encuentran errores → ajustan instrucciones → vuelven a probar. Iteración mínima: 2 rondas.

> ⚠️ **Plan B si colapsa el WiFi:** parejas con hotspot, o trabajar en modo avión escribiendo instrucciones pulidas para pegar después. Nunca detengas el ejercicio.

**Key takeaway:** *"La primera versión va a ser regular — y está bien. Los asistentes se mejoran usándolos, no pensándolos."*

**Slides: 8** (guía paso a paso que se queda fija en pantalla)

---

### 💥 BLOQUE 5: Stress Test — "Rompe el asistente de tu compañero" (20 min)

**Objetivo:** Encontrar debilidades de forma divertida y aprender a iterar.

**Dinámica:** Ejercicio en parejas (10 min por ronda).
- Se intercambian laptops/celulares y el objetivo es **hacer que el asistente del otro falle o diga algo raro**: preguntas fuera de tema, pedirle descuentos, preguntarle cosas que no sabe, intentar que invente información
- Anotan los 2 fallos más graves encontrados
- Devuelven el equipo y cada quien tiene 5 min para corregir su mayor debilidad
- Cierre del bloque: 3 voluntarios comparten "el mejor fallo" del salón — siempre genera risas y aprendizajes de oro

**Key takeaway:** *"Tu asistente va a fallar. Lo importante no es que sea perfecto — es que sepas cómo arreglarlo en 2 minutos. Eso acabas de aprender."*

**Slides: 3**

---

### 🎤 BLOQUE 6: Show & Tell + Aprendizajes (15 min)

**Objetivo:** Celebrar logros, aprender de la diversidad de asistentes construidos y cerrar el tema técnico con energía.

**Dinámica:** Discusión grupal.
- 2-3 voluntarios proyectan su asistente y lo muestran en vivo (3 min c/u): qué hace, qué le costó, qué harían diferente
- Pregunta al salón: *"¿Qué fue lo más sorprendente que descubriste hoy?"* — 4-5 respuestas rápidas
- Tú cierras con el patrón que observaste en el salón (ej. "el 80% construyó asistentes de atención al cliente — hay una señal ahí sobre dónde está el dolor real de ustedes")

**Key takeaway:** *"Construyeron 25 asistentes distintos en 50 minutos. Imaginen lo que pueden construir en 30 días."*

**Slides: 2**

---

### 🎯 BLOQUE 7: Tu Plan de 30 Días + Cierre (15 min)

**Objetivo:** Que nadie salga sin saber qué hacer mañana por la mañana.

**Dinámica:** Charla final + compromiso individual.
- El plan de 30 días (proyectado y en el QR):
  - **Semana 1:** usa tu asistente a diario, corrige 1 cosa por día
  - **Semana 2:** muéstraselo a 3 usuarios reales, recolecta sus preguntas
  - **Semana 3:** integra las preguntas nuevas al conocimiento del asistente
  - **Semana 4:** decide — ¿lo implementas en tu operación? (web, WhatsApp, Instagram)
- **Compromiso en voz alta:** cada quien escribe en su canvas UNA acción para mañana y se la dice a su trio
- Compartir QR de recursos + grupo de WhatsApp de la comunidad
- Agradecimiento + foto grupal con sus canvases en alto 📸

**Key takeaway:** *"El workshop termina hoy. Tu ventaja competitiva empieza mañana a las 9 am."*

**Slides: 5**

---

## 4. EJERCICIO PRINCIPAL: "De Canvas a Asistente"

**El corazón del workshop** (Bloques 3 + 4 + 5, ~95 min en total):

Cada participante diseña, construye, prueba y estresa un asistente de IA para UNA tarea específica de SU propia startup — usando su información real (precios, FAQs, tono de marca). No hay ejercicio hipotético: trabajan sobre su negocio real.

**Por qué funciona:**
- ✅ No requiere código ni tarjeta de crédito (hay ruta 100% gratuita)
- ✅ Funciona en laptop o celular
- ✅ Cada persona sale con algo tangible y personalizado
- ✅ El stress test en parejas convierte el error en juego, no en frustración

---

## 5. RECURSOS PARA LLEVAR A CASA (vía QR)

1. 📄 **Canvas del Asistente** (PDF imprimible y editable)
2. 📖 **Guía paso a paso con screenshots** para Custom GPT, Claude Project y Gemini Gem
3. 💬 **Biblioteca de 50+ prompts para startups** organizados por área: ventas, marketing, operaciones, finanzas, pitch
4. 🛡️ **Checklist de uso responsable:** qué datos NO pegar en la IA, cómo verificar respuestas, errores comunes
5. 📅 **Plan de 30 días** en versión descargable con checklist semanal
6. 🎥 **Grabación del demo en vivo** por si quieren repetirlo con calma
7. 🧰 **Directorio de herramientas IA gratuitas/freemium** relevantes para startups latam
8. 👥 **Grupo de WhatsApp de la comunidad** — seguimiento, dudas, wins compartidos

---

## 6. RESUMEN DE SLIDES

| Sección | Slides |
|---------|--------|
| Bienvenida | 3-4 |
| Contexto IA | 10 |
| Demo + Anatomía | 5 |
| Canvas | 5 |
| Build (guía en pantalla) | 8 |
| Stress test | 3 |
| Show & Tell | 2 |
| Plan 30 días + Cierre | 5 |
| **TOTAL** | **~42 slides** |

> 💡 **Regla de oro:** slides mínimas, pantalla compartida máxima. Durante el build, la slide de pasos se queda quieta — la gente necesita referencia visual constante, no narración.

---

**¿Siguiente paso?** Si quieres, te preparo el Canvas del Asistente en detalle, el guion exacto del demo en vivo, o el email pre-workshop para los participantes. Solo dime cuál. 🚀