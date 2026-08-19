# KAT Coder Air v2.5 — startup_content/workshop_outline

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 8.78 | quality: 9.72
- latency_total: 10.501s | tokens_per_second: 195.0
- input_tokens: 202 | output_tokens: 2048
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



# 🚀 Workshop: Construye tu Asistente de IA para tu Startup
## Outline Completo — 3 Horas Presencial

---

## 1. AGENDA DETALLADA

| Hora | Bloque | Actividad |
|------|--------|-----------|
| 0:00 – 0:15 | Bienvenida + Rompehielo | Dinámica interactiva |
| 0:15 – 0:45 | Bloque 1 | ¿Qué puede hacer un Asistente de IA por tu negocio? |
| 0:45 – 1:00 | Bloque 2 | Demo en vivo — De cero a funcionando en 15 min |
| 1:00 – 1:10 | ☕ Break | |
| 1:10 – 2:00 | Bloque 3 | **Ejercicio principal** — Construye tu asistente |
| 2:00 – 2:25 | Bloque 4 | Conecta tu asistente a tu negocio real |
| 2:25 – 2:50 | Bloque 5 | Sharing + Q&A |
| 2:50 – 3:00 | Cierre | Recursos + Next Steps |

---

## 2. MATERIALES PREPARAR ANTES

### 📋 Logística del evento
- [ ] Proyector + pantalla
- [ ] WiFi dedicado para el workshop (mínimo 50 Mbps)
- [ ] Micrófono para el facilitador
- [ ] Pizarra o flipchart
- [ ] Stickers / post-its / marcadores
- [ ] Nombres (nombres propios en los asientos)

### 💻 Para cada participante
- [ ] Laptop con acceso a internet
- [ ] Cuenta de **Voiceflow** (crear con anticipación — ver guía pre-workshop)
- [ ] Cuenta de **Make.com** (versión gratuita)
- [ ] Cuenta de **Google** (para Sheets)
- [ ] Cuenta de **OpenAI** (API key — o usar la demo integrada de Voiceflow)

### 📦 Material del facilitador
- [ ] Cuenta de Voiceflow de demo (proyecto listo para clonar)
- [ ] Cuenta de Make de demo (escenarios ya armados)
- [ ] Base de datos de ejemplo en Google Sheets (50+ filas de datos ficticios)
- [ ] Guía rápida impresa o PDF para cada participante
- [ ] Plantilla de "Mi Asistente de IA" (canvas de 1 página)
- [ ] Lista de check-in de problemas comunes (troubleshooting)

### 🎯 Pre-workshop (enviar 3 días antes)
- [ ] Email con: link de registro, requisitos técnicos, y guía de "Crea tu cuenta en Voiceflow"
- [ ] Encuesta corta: "¿Qué problema quieres resolver con IA?" (para personalizar ejemplos)

---

## 3. BLOQUES DETALLADOS

---

### BLOQUE 0 — Bienvenida + Rompehielo
**Duración:** 15 min

**Objetivo:** Crear energía, conectar al grupo, y generar expectativa.

**Dinámica:**
1. **Bienvenida del facilitador** (3 min) — Quién eres, por qué estás aquí, qué van a lograr hoy.
2. **Rompehielo "Mi dolor con IA"** (10 min):
   - Cada persona escribe en un post-it: *"Mi mayor dolor hoy que la IA podría resolver"*
   - Los pega en la pared y el facilitador agrupa en 3-4 categorías
   - 2-3 voluntarios comparten
3. **Presentación del roadmap del día** (2 min)

**Key Takeaway:** *"Hoy salimos con un asistente de IA funcionando para nuestro negocio."*

**Slide count:** 3 slides

---

### BLOQUE 1 — ¿Qué puede hacer un Asistente de IA por tu negocio?
**Duración:** 30 min

**Objetivo:** Que cada emprendedor identifique SU caso de uso ideal y entienda qué es posible hoy.

**Dinámica:**
1. **Mini-charla interactiva** (12 min):
   - Qué es un asistente de IA (sin tecnicismos): "Es como un empleado que nunca duerme, responde en segundos, y cuesta centavos por conversación"
   - 4 tipos de asistentes que existen hoy:
     - 💬 **Chatbot de atención al cliente** — FAQ, soporte, agendamiento
     - 📞 **Asistente de ventas** — Qualificación de leads, seguimiento
     - 📊 **Asistente de operaciones** — Búsqueda de datos, reportes
     - ✍️ **Asistente de contenido** — Generación de copy, respuestas personalizadas
   - Casos reales LATAM: ejemplo de una startup de delivery, una clínica, una tienda de e-commerce

2. **Ejercicio rápido individual** (10 min):
   - Canvas de 1 página: *"¿Qué tarea de tu negocio haces manualmente y te quita más de 5 horas por semana?"*
   - Cada uno identifica 1-2 tareas candidatas

3. **Discusión grupal** (8 min):
   - En parejas: comparten su tarea candidata
   - 2-3 personas comparten con el grupo

**Key Takeaway:** *"Ya tengo identificada la tarea que mi asistente de IA va a resolver."*

**Slide count:** 8 slides

---

### BLOQUE 2 — Demo en vivo: De cero a funcionando en 15 min
**Duración:** 15 min

**Objetivo:** Demostrar que NO se necesita saber programar. Generar "wow factor".

**Dinámica:**
1. **Setup previo** (5 min antes del workshop):
   - El facilitador tiene abierto Voiceflow con un proyecto vacío
   - Proyector compartido en vivo

2. **Demo paso a paso** (10 min):
   - Crear un nuevo proyecto → nombre del asistente
   - Agregar un "Intent" (ej: "¿Cuáles son tus horarios?")
   - Agregar respuestas (múltiples formas de preguntar)
   - Agregar un "Block" de conocimiento (conectar a un PDF o URL)
   - Publicar y probar en el chat en vivo
   - Mostrar el resultado: el bot responde correctamente

3. **Q&A rápido** (5 min):
   - "¿Qué tan difícil fue eso?"
   - "¿Alguien tiene dudas?"

**Key Takeaway:** *"Esto es más fácil de lo que pensaba. Yo también puedo hacerlo."*

**Slide count:** 4 slides (con screenshots del proceso)