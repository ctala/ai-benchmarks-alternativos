# Kimi K2.5 — startup_content/workshop_outline

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 77.025s | tokens_per_second: 54.8
- input_tokens: 217 | output_tokens: 4222
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada y recursos prácticos.

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

**WORKSHOP: CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP**
*De la idea al agente funcional en 3 horas (sin escribir código)*

---

## 1. AGENDA DETALLADA (3 HORAS PUNTUALES)

| Tiempo | Bloque | Dinámica |
|--------|--------|----------|
| **0:00-0:15** | 🔥 **Kick-off: El MVP de tu IA** | Icebreaker + Setup |
| **0:15-0:45** | 🧠 **Arquitectura del Agente Perfecto** | Charla interactiva + Canvas |
| **0:45-1:15** | 🛠️ **Demo en Vivo: De 0 a Asistente** | Demo + Q&A rápido |
| **1:15-1:30** | ☕ **Break & Networking** | (¡Cargar laptops!) |
| **1:30-2:30** | ⚡ **Laboratorio: Manos al Código... ¡Sin Código!** | Work in pairs + Mentoring |
| **2:30-3:00** | 🚀 **Demo Day Express & Cierre** | Pitches 2-min + Recursos |

---

## 2. MATERIALES NECESARIOS (CHECKLIST PRE-EVENTO)

### Para el facilitador:
- **Proyector + adaptadores** (USB-C/HDMI) + **sonido** para demos
- **WiFi estable** (crítico: 30 conexiones simultáneas) + backup de hotspot
- **Extensiones/power strips** (mínimo 1 cada 3 personas)
- **Timer visible** (para respetar tiempos)
- **Stickers de "modo avión"** (para cuando demos)

### Para los participantes (comunicar antes):
- **Laptop obligatoria** (cargada al 100%, no tablets)
- **Cuenta de ChatGPT Plus** (trial de 1 día es suficiente) O cuenta gratuita de **Voiceflow**
- **Un documento/PDF** de su startup (pitch, FAQs, o descripción de producto) subido a la nube
- **Post-its y marcadores** (vos los proveés)

### Templates impresos (30 copias):
- **"Agent Design Canvas"** (1 página A3 o 2 A4)
- **Prompt Cheat Sheet** (guía rápida)

---

## 3. BLOQUES DETALLADOS

### BLOQUE 1: KICK-OFF (0:00-0:15)
**Título:** *"Tu primer empleado que no duerme ni cobra aguinaldo"*

**Objetivo:** Romper el miedo a la IA técnica y establecer expectativas realistas.

**Dinámica:**
- **Icebreaker (5 min):** "¿Qué tarea odias hacer cada semana en tu startup?" (cada uno dice una palabra). El facilitator clasifica en tiempo real: Atención, Ventas, Operaciones, Creatividad.
- **El Mito (5 min):** Charla rápida destruyendo "necesito un CTO para tener IA" vs realidad no-code 2024.
- **El Contrato (5 min):** Compromiso de salir con un agente funcional, no perfecto.

**Key Takeaway:** *"No necesitas programar, necesitas pensar como diseñador de procesos."*

**Slides:** 5 (Título, Who am I, Agenda, Expectativas, Reglas de juego)

---

### BLOQUE 2: ARQUITECTURA DEL AGENTE (0:15-0:45)
**Título:** *"Anatomía de un Asistente que Vende (y no solo charla)"*

**Objetivo:** Aprender el framework para diseñar agentes útiles, no chatbots tontos.

**Dinámica:**
- **Teoría 20 min:** Los 3 pilares del agente early-stage:
  1. **Personalidad** (tono, restricciones, qué NO debe decir)
  2. **Conocimiento** (base de datos única de tu negocio)
  3. **Acción** (qué hace: agenda citas, califica leads, responde FAQs)
- **Ejercicio en parejas (10 min):** Completan el *Agent Design Canvas* en papel para SU startup:
  - ¿Quién es tu cliente ideal?
  - ¿Qué pregunta hace 3 veces al día?
  - ¿Qué datos necesitas recolectar antes de hablar con él?

**Key Takeaway:** *"Un buen agente no responde todo, responde lo correcto y acciona."*

**Slides:** 10 (Casos reales: E-commerce vs SaaS vs Servicios, Ejemplos de prompts buenos vs malos, El Canvas visual)

---

### BLOQUE 3: DEMO EN VIVO (0:45-1:15)
**Título:** *"Construyendo en Tiempo Real: El Agente de María"*

**Objetivo:** Mostrar que en 20 min se puede tener algo funcional (sin trucos).

**Dinámica:**
- **Elección del caso (5 min):** Usar un ejemplo real de un participante (o genérico: "Yoga Studio Startup").
- **Demo técnica (20 min):** 
  - Opción A (Fácil): Crear un **GPT personalizado** en ChatGPT Plus (instrucciones + upload de PDF)
  - Opción B (Avanzado pero mejor): Crear flujo en **Voiceflow** (conexión con WhatsApp o Web)
- **Testing en vivo (10 min):** Los participantes le hacen preguntas difíciles al agente recién creado para "romperlo".

**Key Takeaway:** *"El 80% del trabajo es el 'prompt system' y la base de conocimiento, no la tecnología."*

**Slides:** 8 (Screenshots paso a paso, QR codes a las herramientas, Checklist de la demo)

---

### BLOQUE 4: LABORATORIO (1:30-2:30) - *EL CORAZÓN DEL WORKSHOP*
**Título:** *"Build Session: Tu Agente MVP"*

**Objetivo:** Cada equipo sale con un asistente funcional probado.

**Dinámica:**
- **Setup (10 min):** Formación de duplas (ideal: uno con conocimiento del producto, otro "cliente potencial" para testear). Distribución de la guía impresa paso a paso.
- **Build (40 min):** Música de fondo. Facilitador y ayudantes caminando resolviendo dudas técnicas.
- **Test & Iterate (10 min):** El "cliente" de la pareja intenta "romper" el agente del otro.

**Ejercicio Principal Detallado:**
> **"El Qualificador de Leads Automático"**
> 
> **Contexto:** Tu startup recibe 20 mensajes al día de prospectos confundidos. Necesitas filtrar quién está listo para comprar.
> 
> **Entregable:** Un agente (GPT o Voiceflow) que:
> 1. Salude con la personalidad de tu marca
> 2. Haga 3 preguntas específicas para calificar (presupuesto, urgencia, decisor)
> 3. Dé una respuesta diferente si es "lead calificado" vs "lead frío"
> 4. (Bonus) Intente agendar una llamada usando Calendly
> 
> **Input obligatorio:** Subir el PDF/URL de descripción de servicios al "knowledge base" del agente.

**Slides:** 3 (Pantalla de "Modo Laboratorio" con el brief, Timer grande en pantalla, QR a documentación de ayuda)

---

### BLOQUE 5: DEMO DAY EXPRESS & CIERRE (2:30-3:00)
**Título:** *"¿Quién tiene al mejor empleado virtual?"*

**Dinámica:**
- **Pitches (20 min):** 5 duplas voluntarias (2 min cada una). Muestran:
  - El peor mensaje que recibían antes vs cómo responde ahora su agente
  - Un "plot twist": pregunta difícil que resolvió
- **Premio simbólico:** Stickers de "IA Builder" o certificado digital.
- **Cierre energético (10 min):** 
  - Qué hacer la próxima semana (roadmap de mejora)
  - Comunidad de WhatsApp/Telegram para dudas post-taller

**Key Takeaway:** *"Hoy construiste el MVP. La versión 2.0 la haces con datos reales de uso."*

**Slides:** 5 (Formato del pitch, Criterios de evaluación, Roadmap 7-30-90 días, QR a recursos, Foto grupal)

---

## 4. RECURSOS PARA LLEVAR A CASA (DIGITAL + FÍSICO)

### Físico (entregar al salir):
- ** laminated "Prompt Cheat Sheet"**: 10 fórmulas mágicas (AIDA, Chain of Thought, Few-shot)
- **Sticker:** *"Mi startup tiene IA y no necesito un CTO (todavía)"*

### Digital (QR en pantalla final + email follow-up):
1. **El "Agent Design Canvas"** editable en Figma/Google Slides
2. **Template de Prompt System** (el "cerebro" escrito que pueden copiar y pegar)
3. **Comparativa de herramientas 2024:** 
   - Nivel 1: ChatGPT Custom GPTs (fácil, cerrado)
   - Nivel 2: Voiceflow/Botpress (chatbots con lógica)
   - Nivel 3: Make + OpenAI (automatizaciones)
4. **Base de datos de 50 prompts listos para copiar** para startups (email marketing, atención al cliente, research de competencia)
5. **Acceso a comunidad de Discord/WhatsApp:** "IA Builders LATAM" para troubleshooting post-evento

---

## 5. SLIDE COUNT ESTIMADO POR SECCIÓN

| Sección | Slides | Notas |
|---------|--------|-------|
| **Intro & Kick-off** | 5 | Bienvenida, Agenda, Ground rules |
| **Teoría & Canvas** | 10 | Incluye ejemplos visuales de "antes/después" de agentes |
| **Demo Técnica** | 8 | Screenshots numerados, no texto denso |
| **Laboratorio** | 3 | Minimalistas (instrucciones, timer, QR) |
| **Cierre & Recursos** | 5 | Roadmap, QR codes grandes, Call to action |
| **BUFFER** | 4 | Para preguntas imprevistas o demos que fallan |
| **TOTAL** | **~35 slides** | Diseño: 60% imágenes/diagramas, 40% texto máximo |

---

## 💡 TIPS DE FACILITACIÓN PARA ESTA AUDIENCIA

1. **Nunca digas "es fácil"** (es condescendiente para no-técnicos). Di: *"Es un proceso de 5 pasos, lo hacemos juntos"*.
2. **Ten un Plan B técnico:** Si el WiFi falla, tener un video pre-grabado de la demo en tu laptop.
3. **El "Genio de la Lámpara":** Cuando alguien haga un agente cool, detén todo 30 segundos para mostrarlo en proyector (motivación colectiva).
4. **Lenguaje:** Evita "embeddings", "fine-tuning", "API". Usa: "memoria", "entrenamiento básico", "conexión".
5. **Cierre con acción:** Que saquen el celular y le manden el link de su agente a un amigo/cliente real *antes de salir de la sala*.

**Resultado esperado:** 20-30 emprendedores con un asistente funcional en sus celulares/laptops, orgullosos de haber "programado sin programar" y con un roadmap claro para automatizar su primer proceso de negocio.