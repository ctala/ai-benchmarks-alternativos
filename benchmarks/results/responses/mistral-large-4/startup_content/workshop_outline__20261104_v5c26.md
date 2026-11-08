# Mistral Large 4.0 — startup_content/workshop_outline

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 8.19 | quality: 9.72
- latency_total: 108.575s | tokens_per_second: 53.1
- input_tokens: 190 | output_tokens: 5766
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

¡Listo! Aquí tienes el outline completo, diseñado para que salgan con un asistente funcional en sus manos (literalmente en sus celulares), no solo con notas.

---

# 🚀 WORKSHOP OUTLINE: "Construye tu Asistente de IA para tu Startup"
**Formato:** Presencial | **Duración:** 3 horas (180 min) | **Grupo:** 20-30 emprendedores early-stage no-técnicos
**Vibe:** Cero código, 100% acción. "Si puedes escribir un WhatsApp, puedes crear un asistente de IA."

---

## 1. AGENDA DETALLADA (180 min exactos)

| Horario | Bloque | Duración | Formato |
|---------|--------|----------|---------|
| **0:00 - 0:15** | 🔥 Apertura: El problema de las 2 horas diarias | 15 min | Rompehielos + Demo wow |
| **0:15 - 0:45** | 🧠 Bloque 1: El mapa del tesoro (qué es y para qué sirve) | 30 min | Charla interactiva + Mini-ejercicio |
| **0:45 - 1:45** | 🛠️ Bloque 2: MANOS A LA OBRA - Tu asistente en 60 min | 60 min | **Ejercicio principal guiado** |
| **1:45 - 2:00** | ☕ BREAK (café obligatorio) | 15 min | Networking |
| **2:00 - 2:30** | ⚡ Bloque 3: Potenciando tu asistente (integraciones & seguridad) | 30 min | Demo + Práctica rápida |
| **2:30 - 2:50** | 🎯 Bloque 4: De hoy a tu lanzamiento en 30 días | 20 min | Planificación + Discusión |
| **2:50 - 3:00** | 🎤 Cierre: Showcase de 3 minutos + Q&A | 10 min | Micro-presentaciones |

---

## 2. MATERIALES NECESARIOS (Checklist pre-evento)

### Tecnología & Espacio
- [ ] Proyector/pantalla grande + **backup**: video pre-grabado de la demo por si falla internet
- [ ] WiFi de alta capacidad (mínimo 50 Mbps dedicado) + **hotspot de respaldo** en tu celular
- [ ] 6-8 extensiones eléctricas (los emprendedores traen laptops y celulares)
- [ ] 2 micrófonos inalámbricos (uno para ti, otro para Q&A)
- [ ] Cargador universal / adaptadores (algunos vienen de otros países)

### Físicos (por participante)
- [ ] **Workbook impreso** (8 páginas A4 a color): incluye la plantilla del "System Prompt", checklist de seguridad y plan de 30 días
- [ ] 3 post-its de colores diferentes + plumón negro grueso
- [ ] Tarjeta "Mi Asistente" (para escribir el nombre de su bot y pegar en la laptop)
- [ ] Sticker de "Hecho con IA" para pegar en su laptop al final (moral boost)

### Digitales / Cuentas
- [ ] **Plan A:** Acceso a ChatGPT Plus (Custom GPTs) - prepara 5 cuentas de demo por si alguien no tiene tarjeta
- [ ] **Plan B (gratis):** Instrucciones para usar **Microsoft Copilot** (gratis con cuenta Microsoft) o **Claude** (gratis con límite) o **Poe.com**
- [ ] Carpeta compartida en Google Drive con:
  - 3 PDFs de ejemplo para subir (ej: "Propuesta de valor de una cafetería", "FAQ de una app de delivery", "Tonos de voz de marca")
  - La plantilla de prompts en Notion/Google Docs editable

### Logística LATAM
- [ ] Café/té/agua durante todo el evento (no solo en el break)
- [ ] Snacks salados (mantienen la energía alta)
- [ ] Ventiladores o aire acondicionado (el trabajo con laptops calienta la sala)

---

## 3. BLOQUES DETALLADOS

### 🔥 BLOQUE 0: APERTURA (15 min)
**Título:** "El asistente que te roba 10 horas a la semana (y cómo recuperarlo hoy)"
- **Objetivo:** Generar FOMO positivo y bajar la ansiedad tecnológica. Que entiendan que no necesitan saber programar.
- **Dinámica:**
  - Rompehielos (5 min): "Levanta la mano si hoy hiciste algo repetitivo que una máquina podría hacer por ti" (ej: responder el mismo email 20 veces, copiar datos a Excel, buscar info en Google)
  - Demo "wow" (10 min): Muestras en pantalla la diferencia entre preguntarle a ChatGPT normal "¿Cómo respondo a un cliente molesto?" vs preguntarle a un asistente personalizado que conoce TU producto, TU tono y TU política de devoluciones. La segunda respuesta usa el nombre del cliente, menciona el producto específico y propone un descuento del 10% según tus reglas.
- **Key Takeaway:** *"No necesitas una app nueva. Necesitas darle instrucciones claras a la IA que ya usas."*
- **Slides:** 5 (título, agenda visual, el problema, la demo antes/después, reglas del juego)

---

### 🧠 BLOQUE 1: EL MAPA DEL TESORO (30 min)
**Título:** "De asistente genérico a experto en TU negocio"
- **Objetivo:** Entender los 3 pilares de un buen asistente: **Rol + Conocimiento + Reglas**. Identificar 1 proceso repetitivo propio para automatizar.
- **Dinámica:**
  - Charla (15 min): Los 3 tipos de asistentes para startups early-stage:
    1. **El Vendedor 24/7** (responde DMs, cotiza)
    2. **El Creador de Contenido** (posts, emails, propuestas)
    3. **El Analista** (resume encuestas, encuentra patrones en datos de clientes)
  - Mini-ejercicio (15 min): En post-its, escriben 3 tareas que odian hacer y que toman >30 min. Los pegan en la pared. Votación con stickers: ¿Cuál les quita más tiempo?
- **Key Takeaway:** *"Tu asistente no es magia. Es un empleado nuevo al que le das un manual de bienvenida (tus documentos) y le dices exactamente cómo hablar."*
- **Slides:** 8 (los 3 arquetipos con ejemplos latinos: ej. "Bot de una tienda de ropa en Lima", "Asistente de un SaaS en CDMX", anatomía del prompt: Rol+Contexto+Tarea+Formato, ejercicio en pantalla)

---

### 🛠️ BLOQUE 2: MANOS A LA OBRA - EJERCICIO PRINCIPAL (60 min)
**Título:** "Construye tu Chief of Staff Digital en 60 minutos"
- **Objetivo:** Que cada participante salga con un asistente funcional, probado y personalizado para su startup.
- **Dinámica:** Trabajo individual guiado (tú y 1-2 co-facilitadores caminan entre las mesas). Ritmo tipo "cocina en vivo": todos haciendo lo mismo al mismo tiempo.
  - **Min 0-10:** Setup de cuentas (si no tienen, usan las de demo o alternativas gratis)
  - **Min 10-25:** Definición del rol y subida de conocimiento (ver sección 4 abajo)
  - **Min 25-45:** Prueba y refinamiento (cada uno hace 5 preguntas reales a su bot y ajusta)
  - **Min 45-60:** "Día de campo": prueban su bot con el celular de un compañero (validación externa)
- **Key Takeaway:** *"Un asistente sin tus documentos es como un becario sin acceso a la oficina. Sube tus PDFs y se vuelve experto en ti."*
- **Slides:** 12 (paso a paso visual: 1. Crear GPT, 2. Nombre y foto, 3. Instrucciones (system prompt), 4. Subir archivos, 5. Capacidades (activar/desactivar web search), 6. Prueba #1, 7. Errores comunes y fix, 8. Prueba con compañero, 9. Guardar/compartir, 10. Captura de pantalla para redes)

---

### ⚡ BLOQUE 3: POTENCIANDO TU ASISTENTE (30 min)
**Título:** "Conectándolo al mundo real (sin ser programador)"
- **Objetivo:** Mostrar cómo conectar el asistente con herramientas que ya usan (WhatsApp, email, calendario) usando automatizaciones no-code simples, y enseñar límites de seguridad.
- **Dinámica:**
  - Demo rápida (10 min): Cómo conectar su GPT a **Zapier** o **Make** (antes Integromat) para que responda automáticamente en WhatsApp Business o email. Mostrar un flujo simple: "Llega mensaje → GPT responde → Guarda en hoja de cálculo"
  - Charla seguridad (10 min): "La regla de oro: Nunca subas datos de tarjetas de crédito, identificaciones de clientes o contratos firmados sin revisar. La IA aprende de lo que subes."
  - Ejercicio rápido (10 min): Crean 3 "Prompts Maestros" (atajos guardados) para tareas frecuentes: ej. "/cotizar", "/post_linkedin", "/responder_reclamo"
- **Key Takeaway:** *"Empieza simple (solo en ChatGPT), pero piensa en grande: tu asistente puede vivir donde ya están tus clientes (WhatsApp, Instagram, tu web)."*
- **Slides:** 6 (arquitectura simple de integraciones, demo de Zapier paso a paso, checklist de seguridad en rojo, los 3 prompts maestros, alternativas low-cost, Q&A rápido)

---

### 🎯 BLOQUE 4: PLAN DE ACCIÓN (20 min)
**Título:** "Los próximos 30 días: de prototipo a herramienta de trabajo"
- **Objetivo:** Que se lleven un plan concreto para implementar en su startup esta semana, con métricas de éxito.
- **Dinámica:**
  - Planificación individual (10 min): Usan la última página del workbook: "Mi plan de 30 días" (Día 1-3: probar con equipo interno, Día 4-10: ajustar con feedback real, Día 11-20: lanzar a 10 clientes beta, Día 21-30: medir tiempo ahorrado)
  - Discusión grupal (10 min): "Share-out": 3 personas comparten en 1 minuto qué van a automatizar primero. Tú anotas en pizarra los patrones comunes.
- **Key Takeaway:** *"No esperes a que sea perfecto. Lánzalo con 5 usuarios reales esta semana y mejora con datos, no con suposiciones."*
- **Slides:** 4 (plantilla del plan 30 días en pantalla, métricas: horas ahorradas, tasa de respuesta, satisfacción del cliente, ejemplos de éxito de otros emprendedores latinos)

---

### 🎤 CIERRE (10 min)
**Título:** "Showcase: Tu asistente presentado en 60 segundos"
- **Objetivo:** Celebrar el logro, crear accountability grupal y cerrar con energía.
- **Dinámica:**
  - 3 voluntarios (pre-seleccionados durante el break) muestran en pantalla su asistente respondiendo una pregunta real de su negocio (60 seg cada uno)
  - Foto grupal con sus laptops mostrando el nombre de sus asistentes
  - Entrega de recursos digitales (QR en pantalla para escanear)
  - Q&A final (lo que quede)
- **Key Takeaway:** *"Ya no eres un emprendedor solo. Tienes un equipo de 1 (por ahora). Y puede crecer."*
- **Slides:** 3 (instrucciones del showcase, QR con recursos, contacto/redes/agrupación de WhatsApp del cohort)

---

## 4. EJERCICIO PRINCIPAL DETALLADO: "Tu Chief of Staff en 60 minutos"

**Nombre del ejercicio:** *"Elige tu rol y constrúyelo AHORA"*

Cada participante elige **UNO** de estos 4 arquetipos según su necesidad inmediata:

| Rol | Función | Ejemplo de prompt inicial |
|-----|---------|---------------------------|
| 🤝 **El Vendedor** | Responde dudas de clientes potenciales 24/7 | "Eres el asistente de ventas de [Mi Startup]. Conoces nuestro producto, precios y objeciones comunes..." |
| ✍️ **El Creador** | Genera contenido para redes/emails con el tono de la marca | "Eres el copywriter de [Marca]. Tu tono es [divertido/profesional/cercano]. Siempre incluyes un CTA..." |
| 📊 **El Analista** | Resume feedback de clientes o datos de ventas | "Analizas encuestas de clientes y encuentras patrones. Devuelves insights accionables en bullets..." |
| 🗓️ **El Ejecutivo** | Prepara briefings, agendas y resúmenes de reuniones | "Eres mi Chief of Staff. Preparas agendas con objetivos claros y resumes de decisiones pendientes..." |

### Pasos concretos (guía para el facilitador):

1. **Definir la personalidad (10 min):**
   - Escribir en el campo "Instructions" del GPT: Rol + Tono + 3 reglas de oro (ej: "Nunca inventes precios", "Siempre pregunta el nombre antes de cotizar", "Usa emojis moderadamente")

2. **Cargar el conocimiento (10 min):**
   - Subir 1-2 archivos: PDF de su propuesta de valor, lista de precios, FAQ, o transcripción de una venta exitosa
   - Tip: "Si no tienes PDF, pega texto directamente en las instrucciones (máx 8,000 caracteres)"

3. **Configurar capacidades (5 min):**
   - Activar: "Web Search" (si necesita info actualizada), "Code Interpreter" (si va a analizar datos)
   - Desactivar: "DALL-E" (a menos que sea creador de imágenes) para ahorrar tiempo

4. **Prueba de fuego (20 min):**
   - Cada uno hace 5 preguntas REALES de su negocio (no genéricas)
   - Si la respuesta es mala: iteran el prompt (ej: "Sé más específico", "Usa este ejemplo como referencia")
   - Mínimo 2 iteraciones

5. **Validación cruzada (10 min):**
   - Intercambian laptops con un compañero. El compañero hace 3 preguntas "de cliente molesto" o "curioso"
   - Anotan en post-it: ¿Qué le faltó? ¿Sonó robótico?

6. **Nombrar y guardar (5 min):**
   - Nombre creativo: "Sofia - Ventas Tienda X", "Carlos - Contenido Foodtruck Y"
   - Captura de pantalla para presumir en redes (hashtag #MiAsistenteIA)

**Criterio de éxito:** Al final de los 60 min, el asistente debe responder correctamente al menos 4 de 5 preguntas de prueba usando información específica de su negocio (no respuestas genéricas de internet).

---

## 5. RECURSOS PARA LLEVAR A CASA

### 📦 Físicos (en una carpeta o sobre)
- **Workbook impreso** con:
  - Plantilla "System Prompt Maestro" (estructura: Rol + Contexto + Tarea + Formato + Restricciones)
  - Checklist de seguridad de datos (qué NO subir)
  - Plan de implementación 30 días
  - Hoja de "Prompts listos para copiar y pegar" (10 prompts probados para emprendedores)
- **Sticker** "Mi startup corre con IA"
- Lista impresa de herramientas recomendadas con precios en USD (y alternativas gratis):
  - ChatGPT Plus ($20/mes) vs Copilot Pro vs Claude Pro
  - Make.com (automatizaciones) - plan gratis disponible
  - Botpress o Voiceflow (para bots en web/WhatsApp)

### 💻 Digitales (QR en pantalla al final + enviado por email)
- **Carpeta de Google Drive/Notion pública** con:
  - Los 3 PDFs de ejemplo usados en el workshop
  - Video tutorial de 10 min: "Cómo actualizar tu asistente cuando cambias de precio"
  - Plantilla de Notion para trackear interacciones con el bot
  - Comunidad: Link a grupo de WhatsApp/Discord "Emprendedores con IA - Cohort [Mes]" para follow-up mensual
- **Cupón de descuento:** Negociar 3 meses gratis o 20% off en alguna herramienta (ej: Notion AI, Zapier, o un curso complementario)
- **Encuesta de satisfacción** (Google Form) + certificado digital de participación (para LinkedIn)

---

## 6. SLIDE COUNT ESTIMADO POR SECCIÓN

| Sección | Slides | Notas |
|---------|--------|-------|
| Apertura | 5 | Minimalista, mucho video/demo en vivo |
| Bloque 1 - Fundamentos | 8 | Mucho ejemplo visual, poco texto |
| Bloque 2 - Construcción | 12 | Screenshots paso a paso (el participante sigue la pantalla) |
| Bloque 3 - Potenciación | 6 | Diagramas de flujo simples |
| Bloque 4 - Plan de acción | 4 | Plantillas visuales grandes |
| Cierre | 3 | QR grande, contactos, foto grupal |
| **TOTAL** | **~38 slides** | Para 3 horas es perfecto (≈1 slide por 5 min, deja tiempo para trabajar) |

---

## 💡 TIPS DE FACILITACIÓN PARA EL CONTEXTO LATINOAMERICANO

1. **Lenguaje:** Usa ejemplos locales: "Como cuando vendes tamales por WhatsApp", "Como tu tienda de ropa en Instagram", "Como el SaaS de facturación en Colombia". Evita referencias a Silicon Valley.
2. **Manejo del tiempo:** En LATAM a veces la gente llega tarde. Ten un "buffer" de 5 min en el Bloque 1 para recibir rezagados sin interrumpir.
3. **Tecnología:** Ten preparado un video de 3 min mostrando cómo crear el GPT por si el WiFi falla. Y di: "Si no tienes tarjeta para pagar ChatGPT Plus, usa Copilot que es gratis y hace lo mismo para empezar".
4. **Energía:** Cada 20 min, haz una pausa de 30 segundos: "¿Todos siguen vivos? Levanten la mano si ya crearon su bot". Celebra cada pequeño logro en voz alta.
5. **Seguridad:** Sé explícito: "No suban contratos con clientes, datos bancarios o información médica. La IA puede memorizar lo que suben."

**¡Éxito con el workshop!** 🚀 La clave es que salgan con algo funcional en el celular, no solo teoría.