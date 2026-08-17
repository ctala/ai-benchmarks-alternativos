# Kimi K2.7 Code — startup_content/workshop_outline

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 7.54 | quality: 9.72
- latency_total: 111.091s | tokens_per_second: 54.0
- input_tokens: 217 | output_tokens: 6002
- judge_score: 4.8 | justificación: 

## Respuesta completa

¡Listo! Aquí tienes el outline completo para un workshop **presencial, práctico y sin código**, diseñado para que emprendedores *early-stage* y no técnicos salgan con un asistente de IA funcional para su startup.

---

# 🤖 Construye tu Asistente de IA para tu Startup — Workshop Práctico

**Duración:** 3 horas  
**Audiencia:** Emprendedores early-stage, no técnicos (20-30 personas)  
**Metodología:** 70% práctica / 30% concepto  
**Promesa del workshop:** *“Vas a diseñar, entrenar y probar tu primer asistente de IA para tu startup, usando herramientas gratuitas y sin escribir una línea de código.”*

---

## 1. 📋 Agenda Detallada con Tiempos

| Horario | Duración | Actividad |
|---|---|---|
| 0:00 - 0:10 | 10 min | Bienvenida, energizante y expectativas |
| 0:10 - 0:40 | 30 min | **Bloque 1:** ¿Qué puede hacer un asistente de IA en tu startup? |
| 0:40 - 1:15 | 35 min | **Bloque 2:** Diseña la personalidad y el “cerebro” de tu asistente |
| 1:15 - 1:30 | 15 min | *Coffee break + networking* |
| 1:30 - 2:15 | 45 min | **Bloque 3:** Construye tu prototipo en vivo (sin código) |
| 2:15 - 2:45 | 30 min | **Bloque 4:** Prueba, itera y recibe feedback real |
| 2:45 - 3:00 | 15 min | Cierre, plan de los próximos 7 días y recursos |

---

## 2. 🛠 Materiales Necesarios

### Antes del evento
- **Inscripción con pre-tarea:** pedir a cada asistente que traiga:
  - Laptop cargada (celular como plan B).
  - Cuenta gratuita de ChatGPT creada.
  - Una idea clara de su startup, cliente ideal y al menos 3 preguntas frecuentes que le hacen sus clientes.
- **Crear una plantilla compartida:** Google Docs o Notion con el “Prompt Template” y el “Canvas de Persona del Asistente”.
- **Preparar cuentas demo:** tener una cuenta de ChatGPT Plus lista para mostrar la creación de un GPT (si aplica). También tener abierta una cuenta de **Poe.com** (gratuita, crea bots con prompt) como alternativa para quienes no tengan Plus.
- **Materiales impresos:** 30 hojas de trabajo con el ejercicio principal, post-its, marcadores.
- **Música de fondo** para las dinámicas y breaks.

### Día del evento
- Proyector o pantalla grande.
- Micrófono inalámbrico (si el salón es grande).
- WiFi estable + contraseña visible.
- Extensiones y regletas eléctricas.
- Stickers de nombres con espacio para “Mi startup ayuda a ___ a ___”.
- Cronómetro visible o timer en pantalla.
- 1 o 2 ayudantes / mentores de piso para resolver dudas técnicas rápidas.

---

## 3. 🧩 Detalle de Cada Bloque

---

### 🚀 Bloque 0: Bienvenida y calentamiento
**Duración:** 10 min  
**Dinámica:** Charla rápida + interacción  
**Objetivo:** Generar energía, alinear expectativas y romper el hielo.  

**Actividad:**
- Pregunta de entrada: *“¿Cuántas horas a la semana pierdes respondiendo preguntas repetitivas o calificando leads?”* Levanten la mano.
- Cada uno escribe en su sticker: *“Mi asistente ideal se llamaría ___ y me ayudaría a ___.”*

**Key takeaway:**  
> *“Un asistente de IA no reemplaza tu humanidad: te libera para que te enfoques en crecer.”*

**Slides estimados:** 4

---

### 🧠 Bloque 1: ¿Qué puede hacer un asistente de IA en tu startup?
**Duración:** 30 min  
**Dinámica:** Mini charla + ejercicio grupal  
**Objetivo:** Identificar los 2-3 casos de uso de mayor impacto para cada startup.  

**Actividad:**
1. Muestra 3 ejemplos rápidos de asistentes reales:
   - Asistente de WhatsApp para e-commerce que responde preguntas de envío.
   - Bot calificador de leads en la web de una agencia de servicios.
   - Asistente de onboarding para una app SaaS.
2. Ejercicio: cada asistente llena una matriz en post-it:
   - ¿Qué pregunta me hacen 10 veces por semana?
   - ¿Dónde se “pierde” el cliente antes de comprar?
   - ¿Qué tarea repetitiva me quita tiempo creativo?
3. Comparten con el vecino y eligen **1 caso de uso prioritario**.

**Key takeaway:**  
> *“No automatices todo. Automatiza la pregunta #1 que te roba tiempo y la respuesta #1 que acelera la venta.”*

**Slides estimados:** 8

---

### 🎨 Bloque 2: Diseña la personalidad y el cerebro de tu asistente
**Duración:** 35 min  
**Dinámica:** Charla corta + ejercicio individual con plantilla  
**Objetivo:** Crear el “system prompt” y la base de conocimiento inicial del asistente.  

**Actividad:**
1. Explica con analogía: *“El prompt es el manual de empleo de tu asistente. La base de conocimiento es su libreta de respuestas.”*
2. Cada uno completa el **Canvas del Asistente**:
   - Nombre del asistente
   - Rol (¿qué hace?)
   - Audiencia (¿a quién atiende?)
   - Tono y personalidad (5 adjetivos)
   - Límites (qué NO debe decir ni hacer)
   - Formato de respuesta (largo, emojis, bullets)
3. Introduce el **Prompt Template** y cada uno lo adapta a su startup.
4. Muestra cómo crear una “mini base de conocimiento” con 5-10 FAQs.

**Key takeaway:**  
> *“Un asistente útil no es el que más sabe, es el que sabe qué responder, cómo responder y cuándo decir ‘te conecto con un humano’.”*

**Slides estimados:** 10

---

### ☕ Break + Networking
**Duración:** 15 min  
**Dinámica:** Networking informal  
**Objetivo:** Descansar, conectar y que los asistentes compartan avances.  

**Actividad opcional:** Mientras toman café, invítalos a pegar sus post-its en un “Muro de Asistentes”.

---

### 🛠 Bloque 3: Construye tu prototipo en vivo
**Duración:** 45 min  
**Dinámica:** Demo + ejercicio práctico guiado  
**Objetivo:** Cada asistente construye y prueba una primera versión funcional.  

**Actividad — El ejercicio principal:**
1. El facilitador hace una demo en pantalla de 10 min:
   - Cómo crear un bot en **Poe.com** (gratis, sin código) usando el prompt.
   - Alternativa: cómo usar el prompt en **ChatGPT** con “Instrucciones personalizadas” o como GPT (si tienen Plus).
2. Los asistentes trabajan individualmente o en parejas:
   - Copian el Prompt Template.
   - Lo completan con su startup.
   - Agregan sus 5-10 FAQs como contexto.
   - Lo pegan en ChatGPT / Poe y prueban 3 preguntas de clientes reales.
3. Mentores de piso ayudan a quienes se atoren.

**Key takeaway:**  
> *“En 15 minutos puedes tener un asistente que responda mejor que tú a las 5 preguntas más frecuentes de tu negocio.”*

**Slides estimados:** 12 (la mitad son pantallazos/demo)

---

### 🧪 Bloque 4: Prueba, itera y recibe feedback real
**Duración:** 30 min  
**Dinámica:** Role-play en parejas + ajustes rápidos  
**Objetivo:** Detectar errores, mejorar el prompt y validar utilidad.  

**Actividad:**
1. **Role-play “Cliente vs. Asistente”**:
   - Una persona hace de cliente difícil.
   - La otra copia y pega las preguntas en su asistente.
   - Evalúan: ¿La respuesta fue clara? ¿Sonó a humano? ¿Faltó información? ¿Se inventó algo?
2. Ajustan el prompt en vivo:
   - Agregan una regla.
   - Corrigen el tono.
   - Añaden una pregunta de clarificación.
3. Comparten 1 aprendizaje con la sala.

**Key takeaway:**  
> *“Un asistente de IA se mejora con conversaciones reales, no con teoría. Cada pregunta difícil es una actualización para tu base de conocimiento.”*

**Slides estimados:** 6

---

### 🎯 Cierre y plan de los próximos 7 días
**Duración:** 15 min  
**Dinámica:** Charla + entrega de recursos + foto grupal  
**Objetivo:** Cerrar con un plan concreto de implementación.  

**Actividad:**
1. Comparte el checklist “Tu asistente en 7 días”.
2. Pregunta de cierre: *“¿Cuál es la primera pregunta que vas a delegar a tu asistente mañana?”*
3. Foto grupal con el Muro de Asistentes.

**Key takeaway:**  
> *“Hoy no saliste con un producto terminado: saliste con un sistema para seguir mejorándolo sin depender de un desarrollador.”*

**Slides estimados:** 5

---

## 4. ⭐ Ejercicio Principal del Workshop

### “Construye tu Asistente en 15 minutos”

**Entregable:** Cada asistente tendrá un prompt funcional + una mini base de conocimiento probada.

### Paso a paso:

**Paso 1 — Elige el caso de uso (3 min)**
> Ejemplo: *“Calificar leads que llegan por la web de mi agencia de marketing.”*

**Paso 2 — Completa el Canvas del Asistente (5 min)**
| Campo | Tu respuesta |
|---|---|
| Nombre del asistente | |
| Rol principal | |
| Cliente al que atiende | |
| Tono de voz | |
| 3 cosas que SÍ puede hacer | |
| 3 cosas que NO puede hacer | |
| Formato de respuesta ideal | |

**Paso 3 — Llena el Prompt Template (5 min)**

```markdown
Rol: Eres [NOMBRE], el asistente virtual de [STARTUP]. 
Tu trabajo es [CASO DE USO: responder FAQs, calificar leads, agendar citas, etc.].

Audiencia: Atiendes a [CLIENTE IDEAL]. 
Tono: [3-5 adjetivos, ej. amigable, directo, profesional, cálido].

Reglas:
1. Responde solo con base en la información que te daremos abajo.
2. Si no sabes la respuesta o el usuario pide algo fuera de tu alcance, di: 
   “No estoy seguro, te conecto con alguien del equipo.”
3. Haz máximo 1 o 2 preguntas de clarificación antes de recomendar.
4. No inventes precios, fechas, funciones ni promesas que no estén en la información.
5. Mantén tus respuestas cortas: máximo 3 líneas o un bullet list.

Contexto de la startup:
[Descripción de qué haces, problema que resuelves, propuesta de valor.]

Preguntas frecuentes:
1. P: ¿Cuánto cuesta? R: [respuesta]
2. P: ¿Cómo funciona? R: [respuesta]
3. P: ¿Tienen garantía? R: [respuesta]
4. P: ¿En qué horarios atienden? R: [respuesta]
5. P: ¿Cómo empiezo? R: [respuesta]
```

**Paso 4 — Pruébalo (5 min)**
Pega el prompt en ChatGPT, Poe.com o en tu no-code tool. Hazle estas 3 preguntas:
1. Una pregunta frecuente fácil.
2. Una pregunta difícil que no esté en tu FAQ.
3. Una pregunta “tramposa” para ver si se inventa algo.

**Paso 5 — Ajusta (2 min)**
Corrige el prompt según lo que falló.

---

## 5. 📦 Recursos para Llevar a Casa

Entrega un paquete digital (QR o email) con:

1. **Prompt Template editable** (Google Docs / Notion).
2. **Canvas del Asistente** en PDF imprimible.
3. **Base de conocimiento template** (Google Sheets).
4. **Checklist “Mi asistente de IA en 7 días”**:
   - Día 1: Definir caso de uso.
   - Día 2: Escribir prompt y FAQs.
   - Día 3: Probar con 10 preguntas reales.
   - Día 4: Conectar a WhatsApp / web (usando Voiceflow, Chatbase, Botpress o Landbot).
   - Día 5: Entrenar a tu equipo.
   - Día 6: Publicar en tu sitio o canal.
   - Día 7: Medir y ajustar.
5. **Comparativo de herramientas no-code**:
   - **Poe.com** — crear bots gratis con prompt.
   - **Chatbase.co** — chatbot para web con tu contenido.
   - **Voiceflow** — flujos conversacionales avanzados.
   - **Landbot / Typebot** — chatbots visuales para web y WhatsApp.
   - **Botpress** — más potente, ideal para WhatsApp.
   - **Zapier + OpenAI** — automatizar respuestas por email/CRM.
6. **Video o Loom de la demo** del facilitador.
7. **Plantilla de métricas**: cuántas conversaciones, cuántos leads calificados, cuántas escalaciones a humano.
8. **Comunidad de apoyo**: enlace a Slack / WhatsApp / Discord del grupo.

---

## 6. 🎞 Slide Count Estimado por Sección

| Sección | Slides estimados |
|---|---|
| Bienvenida y calentamiento | 4 |
| Bloque 1: Casos de uso | 8 |
| Bloque 2: Persona y prompt | 10 |
| Bloque 3: Construcción en vivo | 12 |
| Bloque 4: Pruebas e iteración | 6 |
| Cierre y recursos | 5 |
| **Total** | **~45 slides** |

> 💡 **Nota del facilitador:** Muchos de los slides del Bloque 3 son pantallazos de herramientas y pasos visuales. No leas los slides: usalos como apoyo visual mientras los asistentes hacen.

---

## 🎤 Tips de Facilitación para que Funcione

- **Nunca digas “ahora programamos”**. Diles: *“ahora le das las instrucciones a tu asistente”*.
- Camina por el salón. Con 20-30 personas, necesitas al menos 1 ayudante técnico.
- Ten un **plan B listo**: si el WiFi falla, usa el ejercicio en papel y la demo desde tu celular con datos.
- Celebra los “errores” del asistente: *“¡Miren! Se inventó un precio. Eso significa que tenemos que mejorar el prompt. Esto es machine learning en la vida real.”*
- Cierra con una **acción inmediata**: que cada uno se comprometa con una tarea para mañana.

---

¿Quieres que te prepare también el **pitch de venta del workshop**, el **email de pre-tarea para los inscritos**, o una **versión abreviada de 90 minutos**? 🚀