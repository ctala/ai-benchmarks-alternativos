# Claude Sonnet 5 — startup_content/workshop_outline

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 7.9 | quality: 9.72
- latency_total: 55.98s | tokens_per_second: 93.2
- input_tokens: 314 | output_tokens: 5219
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

# 🚀 Construye tu Asistente de IA para tu Startup
### Workshop Práctico de 3 Horas | Para Fundadores No-Técnicos

---

## 🎯 Objetivo General del Workshop

Que cada participante salga con **un asistente de IA funcional** (no un prototipo teórico) que resuelva un problema real de su startup — atención a clientes, ventas, onboarding, o procesos internos — sin escribir una sola línea de código.

---

## 📋 AGENDA DETALLADA (3 horas = 180 min)

| Bloque | Tiempo | Duración |
|---|---|---|
| 1. Bienvenida + Rompehielo | 0:00 – 0:15 | 15 min |
| 2. ¿Qué es realmente un Asistente de IA? | 0:15 – 0:35 | 20 min |
| 3. Casos reales: Startups LATAM usando IA | 0:35 – 0:50 | 15 min |
| ☕ Break corto | 0:50 – 1:00 | 10 min |
| 4. Elige tu caso de uso (Ejercicio) | 1:00 – 1:20 | 20 min |
| 5. Demo en vivo: Construyendo el asistente | 1:20 – 1:45 | 25 min |
| 6. **EJERCICIO PRINCIPAL**: Construye el tuyo | 1:45 – 2:30 | 45 min |
| ☕ Break corto | 2:30 – 2:35 | 5 min |
| 7. Pruebas cruzadas + Feedback | 2:35 – 2:55 | 20 min |
| 8. Cierre: Siguientes pasos + Recursos | 2:55 – 3:10 | 15 min |

*(Nota: suma 190 min contando breaks — ajustable comprimiendo bloque 3 o 7 si el grupo es grande)*

---

## 🛠️ MATERIALES NECESARIOS (Preparar ANTES)

### Para el facilitador:
- [ ] Laptop + proyector + HDMI/adaptadores de respaldo
- [ ] Internet estable (¡backup con hotspot móvil!)
- [ ] Cuenta demo pre-configurada en la herramienta a usar (ChatGPT Teams, Voiceflow, Botpress, o similar — **elige UNA** herramienta no-code)
- [ ] Template de "Caso de Uso" impreso o en Google Form
- [ ] Lista de prompts de ejemplo por industria (e-commerce, servicios, SaaS, restaurantes)
- [ ] Encuesta de cierre (Google Form o Mentimeter)
- [ ] Música de fondo para los momentos de trabajo individual (energiza sin distraer)

### Para los participantes (enviar 48h antes):
- [ ] Crear cuenta gratuita en la plataforma elegida
- [ ] Traer laptop propia (obligatorio) y cargador
- [ ] Traer: 1 problema real de su startup que quieran resolver
- [ ] Pre-work de 10 min: llenar un mini-formulario con su "Perfil de Negocio" (industria, cliente ideal, canal principal)

### Infraestructura del venue:
- [ ] WiFi con capacidad para 30 dispositivos simultáneos
- [ ] Enchufes suficientes (o extensiones)
- [ ] Mesas en formato de islas (4-5 personas) para fomentar ayuda mutua

---

## 📦 DESARROLLO POR BLOQUES

---

### **BLOQUE 1: Bienvenida + Rompehielo**
**⏱ 15 min | 🎞 4 slides**

**Objetivo:** Romper el hielo, generar energía y bajar la ansiedad del "no soy técnico".

**Dinámica:**
- Apertura con una pregunta provocadora: *"¿Cuántos de ustedes ya perdieron una venta porque no respondieron un WhatsApp a tiempo?"* (levanten la mano)
- Ronda rápida: cada mesa se presenta en 60 segundos — nombre, startup, y "mi frustración #1 de este mes"
- El facilitador comparte una anécdota personal de cómo la IA le ahorró tiempo real

**Key Takeaway:**
> "No necesitas saber programar. Necesitas saber tu negocio — eso ya lo tienes."

---

### **BLOQUE 2: ¿Qué es realmente un Asistente de IA?**
**⏱ 20 min | 🎞 8 slides**

**Objetivo:** Desmitificar la IA. Que entiendan QUÉ pueden construir hoy, sin jerga técnica.

**Dinámica:** Charla con analogías simples
- Analogía central: *"Un asistente de IA es como contratar a un empleado nuevo: le das instrucciones claras (prompt), le das información de tu negocio (contexto/documentos), y lo pones a trabajar en un canal (WhatsApp, web, Instagram)"*
- Mostrar los 3 tipos de asistentes que pueden construir HOY:
  1. **Atención al cliente** (responde preguntas frecuentes 24/7)
  2. **Ventas/Calificación de leads** (filtra quién está listo para comprar)
  3. **Interno/Operativo** (ayuda a tu equipo con tareas repetitivas)
- Mini-quiz rápido con Mentimeter: "¿Cuál de estos usarías tú?"

**Key Takeaway:**
> "La IA no es magia, es un empleado que entrenas con instrucciones y datos de tu negocio."

---

### **BLOQUE 3: Casos reales — Startups LATAM usando IA**
**⏱ 15 min | 🎞 6 slides**

**Objetivo:** Generar aspiración mostrando ejemplos tangibles y cercanos (no Silicon Valley).

**Dinámica:** Mini-demos en video/screenshot de 3 casos reales
- Ejemplo 1: Un e-commerce que automatizó devoluciones por WhatsApp
- Ejemplo 2: Una startup de servicios que calificó leads mientras dormían
- Ejemplo 3: Un restaurante/delivery que redujo tiempo de respuesta de 2 horas a 30 segundos
- Pregunta de discusión rápida en mesas (3 min): *"¿Cuál de estos se parece más a tu negocio?"*

**Key Takeaway:**
> "Esto no es el futuro. Esto ya está pasando en negocios como el tuyo, hoy."

---

### ☕ **BREAK (10 min)**
*Aprovecha para que la gente instale/verifique su cuenta en la herramienta*

---

### **BLOQUE 4: Elige tu Caso de Uso (Ejercicio)**
**⏱ 20 min | 🎞 3 slides**

**Objetivo:** Que cada participante defina CON CLARIDAD qué va a construir en la siguiente hora.

**Dinámica:** Ejercicio individual con template guiado

📝 **Template "Mi Asistente en 4 Preguntas":**
1. ¿Qué pregunta repiten más tus clientes? (o qué tarea repetitiva odias)
2. ¿Dónde quieres que viva este asistente? (WhatsApp, web, Instagram)
3. ¿Qué información necesita saber? (precios, horarios, políticas, FAQs)
4. ¿Qué pasa si el asistente no sabe la respuesta? (escalar a humano, pedir datos)

- Trabajo individual (10 min) + compartir con su mesa (5 min) + 2 voluntarios comparten con todo el grupo (5 min)

**Key Takeaway:**
> "Un asistente mal definido es un asistente que nadie usa. La claridad es el 80% del trabajo."

---

### **BLOQUE 5: Demo en Vivo — Construyendo el Asistente**
**⏱ 25 min | 🎞 5 slides + demo en vivo**

**Objetivo:** Mostrar paso a paso, en tiempo real, cómo se construye un asistente desde cero.

**Dinámica:** Demo en vivo (facilitador construye frente a todos)
- Paso 1: Crear el asistente en la plataforma elegida
- Paso 2: Escribir el prompt/personalidad ("Eres el asistente de [Nombre], una startup que vende...")
- Paso 3: Cargar un documento de contexto (FAQ, catálogo, políticas)
- Paso 4: Probar con 2-3 preguntas reales en vivo
- Paso 5: Conectarlo a un canal (mostrar cómo se vería en WhatsApp/web)
- **Error intencional**: mostrar qué pasa cuando el prompt es vago, para que vean la diferencia

**Key Takeaway:**
> "Son 4 pasos, no 40. Lo que toma tiempo es pensar bien el contenido, no la tecnología."

---

### **BLOQUE 6: 🔥 EJERCICIO PRINCIPAL — Construye el Tuyo**
**⏱ 45 min | 🎞 2 slides (instrucciones) + trabajo en vivo**

**Objetivo:** Cada participante construye una versión funcional (mínima pero real) de su asistente.

**Dinámica:** Trabajo individual con apoyo itinerante
- Usan su template del Bloque 4 como guía
- Checklist en pantalla con los 4 pasos (igual que la demo)
- Facilitador + 1-2 asistentes/mentores circulan por las mesas resolviendo dudas
- A los 25 min: check-in grupal rápido — "¿Quién ya tiene su primera respuesta del asistente? ¡Levanten la mano!"
- Últimos 10 min: pulir y hacer 3 pruebas con preguntas reales de sus clientes

**Checklist que deben completar:**
- [ ] Asistente creado con nombre y personalidad
- [ ] Al menos 1 documento o bloque de info cargado
- [ ] 3 preguntas de prueba respondidas correctamente
- [ ] 1 plan de "qué hacer si no sabe la respuesta"

**Key Takeaway:**
> "Ya no es una idea. Es algo que existe y funciona — lo construiste tú, en 45 minutos."

---

### ☕ **BREAK (5 min)**

---

### **BLOQUE 7: Pruebas Cruzadas + Feedback**
**⏱ 20 min | 🎞 2 slides**

**Objetivo:** Validar el asistente con ojos externos y generar aprendizaje colectivo.

**Dinámica:** Speed-testing en parejas
- Se rotan por mesas: cada participante prueba el asistente de su compañero actuando como "cliente difícil"
- Feedback estructurado en 3 preguntas:
  1. ¿Qué te sorprendió (bien o mal)?
  2. ¿Qué le faltó?
  3. ¿Lo usarías si fueras cliente real?
- 2-3 participantes comparten su experiencia con todo el grupo

**Key Takeaway:**
> "Tu asistente no está listo cuando TÚ lo apruebas, está listo cuando un extraño lo entiende."

---

### **BLOQUE 8: Cierre — Siguientes Pasos + Recursos**
**⏱ 15 min | 🎞 6 slides**

**Objetivo:** Que se vayan con un plan de acción concreto, no solo inspiración.

**Dinámica:** Charla de cierre + compromiso público
- Plan de 7 días: qué hacer cada día para mejorar y lanzar el asistente
- Cada participante escribe en un post-it: *"Para el [fecha], mi asistente va a estar atendiendo clientes reales"*
- Fotos grupales, entrega de recursos, encuesta de satisfacción
- Invitación a comunidad/grupo de WhatsApp o Slack para seguimiento

**Key Takeaway:**
> "El workshop termina hoy. Tu asistente sigue trabajando mañana, y pasado, y el mes que viene."

---

## 💪 EJERCICIO PRINCIPAL — Resumen Ejecutivo

**"Construye tu Primer Asistente en 45 Minutos"**

| Paso | Qué hacen | Tiempo |
|---|---|---|
| 1 | Definen personalidad y rol del asistente | 5 min |
| 2 | Escriben el prompt base (instrucciones) | 10 min |
| 3 | Cargan información de contexto (FAQ/catálogo) | 15 min |
| 4 | Prueban con 5 preguntas reales de clientes | 10 min |
| 5 | Ajustan y pulen respuestas | 5 min |

✅ **Entregable al final:** Un asistente funcional, probado, con un plan claro de qué le falta para producción.

---

## 🎁 RECURSOS PARA LLEVAR A CASA

1. **📄 Template "Mi Asistente en 4 Preguntas"** (PDF editable)
2. **📚 Guía de Prompts por Industria** (e-commerce, servicios, SaaS, restaurantes, salud)
3. **✅ Checklist de Lanzamiento** (qué revisar antes de poner el asistente en producción con clientes reales)
4. **🎥 Grabación de la demo en vivo** (para repasar paso a paso)
5. **📊 Plan de 7 días** post-workshop
6. **💬 Acceso a comunidad** (WhatsApp/Slack) para dudas y casos de éxito
7. **🔗 Lista de herramientas no-code** comparadas (precio, facilidad, casos de uso ideales)
8. **📅 Invitación a sesión de seguimiento** (opcional, 2-3 semanas después, 1 hora de Q&A)

---

## 🎞 RESUMEN DE SLIDES ESTIMADOS

| Bloque | Slides estimados |
|---|---|
| 1. Bienvenida | 4 |
| 2. Qué es un Asistente de IA | 8 |
| 3. Casos reales LATAM | 6 |
| 4. Elige tu caso de uso | 3 |
| 5. Demo en vivo | 5 |
| 6. Ejercicio principal | 2 |
| 7. Pruebas cruzadas | 2 |
| 8. Cierre y recursos | 6 |
| **TOTAL** | **~36 slides** |

*(Ritmo ágil: ~5 min por slide en promedio, dejando espacio generoso para demos y ejercicios)*

---

## 🔑 Mantras del Facilitador Durante el Workshop

- "No existe la pregunta tonta, solo el prompt mal escrito."
- "Progreso, no perfección — tu asistente de hoy es v0.1, no la versión final."
- "Si te atoras, levanta la mano — para eso estamos aquí."