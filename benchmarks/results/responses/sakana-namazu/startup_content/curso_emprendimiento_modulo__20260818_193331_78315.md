# Sakana Namazu — startup_content/curso_emprendimiento_modulo

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 32.816s | tokens_per_second: 198.7
- input_tokens: 279 | output_tokens: 6521
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores, cubriendo todos los aspectos solicitados con ejemplos prácticos e instrucciones detalladas.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un disenador instruccional especializado en emprendimiento y tecnologia.
Creas contenido educativo practico para emprendedores latinoamericanos.
Tu enfoque es hands-on, con ejercicios aplicables y ejemplos reales.

**user:**

Disena el Modulo 3 de un curso llamado "IA Practica para Emprendedores".

El modulo se titula: "Automatizacion con IA: De la idea al flujo de trabajo"

Incluye:
1. Objetivo del modulo (1 parrafo)
2. Contenido teorico (explicacion de automatizacion con IA, herramientas como N8N)
3. 3 ejemplos practicos de automatizacion para startups:
   - Atencion al cliente automatizada
   - Generacion de contenido para redes sociales
   - Calificacion automatica de leads
4. Ejercicio practico paso a paso (que el alumno pueda seguir)
5. Recursos adicionales
6. Preguntas de autoevaluacion (3 preguntas)

Formato: Markdown con buena estructura. Nivel: Emprendedor no-tecnico.


## Respuesta completa

# Módulo 3: Automatización con IA — De la idea al flujo de trabajo

---

## 1. Objetivo del módulo

Al completar este módulo, serás capaz de identificar procesos repetitivos en tu startup que consuman horas de tu semana y que puedan ser ejecutados por una máquina, diseñar flujos de trabajo automatizados usando herramientas **no-code/low-code** como N8N (sin necesidad de saber programar), e integrar modelos de inteligencia artificial para que tomen decisiones simples —como clasificar clientes o redactar respuestas—, liberando tu tiempo para enfocarte en estrategia, ventas y crecimiento, mientras reducis costos operativos desde el primer día.

---

## 2. Contenido teórico

### ¿Qué es la automatización con IA?
Imaginá que en tu empresa cada tarea es un empleado nuevo. Uno recibe un mensaje de WhatsApp, otro copia ese dato a una hoja de cálculos, otro decide si el cliente es prioritario y otro le escribe un email. La automatización es, simplemente, **conectar esos “empleados” (tus aplicaciones) para que trabajen solos las 24 horas**. 

La IA actúa como el “capatare inteligente” dentro de ese equipo: lee textos, clasifica intenciones, resume conversaciones o redacta borradores, permitiendo que el flujo no solo mueva datos, sino que **tome decisiones** sin intervención humana.

### ¿Por qué automatizar si sos emprendedor?
- **Tiempo:** En América Latina, el 40 % del tiempo de un founder se va en tareas operativas. Automatizar es recuperar esas horas.
- **Escalabilidad:** No necesitás contratar a alguien para responder lo mismo 50 veces al día.
- **Velocidad:** Un lead contactado en los primeros 5 minutos tiene hasta 9 veces más chances de convertir.

### Herramientas clave: N8N y el ecosistema no-code

**N8N** (se pronuncie “n-eight-n”, como “workflow”) es una plataforma de automatización tipo Lego: unís bloques (llamados *nodos*) para crear flujos. Es muy popular entre emprendedores porque tiene una **versión gratuita** que podés instalar en tu servidor o usar en la nube con créditos iniciales.

Otras herramientas del ecosistema:
- **Make** (ex-Integromat): Muy visual, ideal para conectar APIs.
- **Zapier:** Fácil, pero más caro para volúmenes altos. 
- **WhatsApp Business API, Google Sheets, Notion, Gmail:** Las aplicaciones que N8N conecta.

> **Anatomía de un flujo simple**
> 1. **Trigger (el detonante):** “Cuando pasa X…” (ej: llega un email, alguien completa un formulario).
> 2. **Acción de IA (el cerebro):** “La IA lee y decide…” (ej: clasifica el mensaje, resume, responde).
> 3. **Action (la acción final):** “Hacé Y…” (ej: enviar WhatsApp, guardar en hoja, notificar al equipo).

---

## 3. Tres ejemplos prácticos de automatización para startups

### Ejemplo A: Atención al cliente automatizada (WhatsApp/Instagram)
**Contexto:** Tu tienda de ropa recibe 80 mensajes diarios en Instagram preguntando “¿Tienen stock?”, “¿Hacen envíos a provincia?” y “¿Cuál es el precio?”.

**Flujo de trabajo:**
1. **Trigger:** Llega un mensaje directo de Instagram o WhatsApp Business.
2. **Nodo de IA (OpenAI/N8N):** La IA analiza el texto del cliente con un prompt preconfigurado: *“Sos el vendedor de esta tienda. Respondé la consulta en 2 líneas usando este catálogo de precios…”*.
3. **Decisión automática:** 
   - Si la IA detecta una pregunta frecuente (stock/envío), **responde sola al instante**.
   - Si detecta una queja compleja (*“mi pedido llegó roto”*) o una intención de compra mayorista, **enciende una alerta** y deriva a un humano por Telegram/WhatsApp del vendedor.
4. **Action:** Envía la respuesta al cliente y, en paralelo, guarda la conversación en una Google Sheet para estadísticas.

**Resultado:** Atención 24/7, cero leads perdidos por la madrugada y tu equipo solo interviene en lo importante.

---

### Ejemplo B: Generación de contenido para redes sociales
**Contexto:** Tu consultora de finanzas personales necesita estar presente en LinkedIn y TikTok, pero no tenés tiempo de escribir todos los días.

**Flujo de trabajo:**
1. **Trigger:** Todos los lunes a las 9:00 a.m., N8N se activa automáticamente.
2. **Action inicial:** Lee una fila de una Google Sheet donde vos previamente cargaste 5 “temas” de la semana (ej: “cómo ahorrar en inflación”, “errores comunes en impuestos”).
3. **Nodo de IA:** Envía el tema a un modelo de lenguaje con el prompt: *“Generá 3 opciones de post para LinkedIn y 1 guión de 30 segundos para TikTok para el tema X, con tono profesional pero cercano para Latinoamérica”*.
4. **Action final:** La IA guarda los textos generados en un documento de Notion o Google Docs, y te envía un resumen por email. Vos solo revisás, ajustás y programás en Buffer o Meta Business Suite.

**Resultado:** Pasás de 3 horas a 20 minutos semanales en contenido, manteniendo constancia sin creatividad forzada.

---

### Ejemplo C: Calificación automática de leads
**Contexto:** Tu agencia de marketing digital recibe solicitudes de presupuesto por una landing page. No todos tienen el presupuesto mínimo ni la urgencia.

**Flujo de trabajo:**
1. **Trigger:** Alguien completa tu formulario de Typeform/Jotform.
2. **Nodo de IA:** Envía las respuestas (presupuesto, tamaño de empresa, urgencia) con este tipo de instrucción: *“Clasificá este lead como ‘Caliente’, ‘Tibio’ o ‘Frío’. ‘Caliente’ si el presupuesto es mayor a $500 y quiere empezar este mes”*.
3. **Decisiones automáticas (Switch/IF):**
   - **Caliente:** N8N envía un mensaje de WhatsApp al vendedor diciendo *“🔥 Lead caliente: María de ABC S.A. Contactala ya”*. Además, crea una tarjeta automática en Trello/HubSpot.
   - **Tibio:** El lead recibe un email automático con una case study y queda en una lista de Mailchimp para *nurturing*.
   - **Frío:** Se guarda solo en una Google Sheet para una campaña futura.
4. **Action:** Resumen diario enviado al equipo con cuántos leads entraron y cómo se clasificaron.

**Resultado:** El equipo de ventas solo llama a los que realmente importan. Cero tiempo perdido en leads que no están listos.

---

## 4. Ejercicio práctico paso a paso
### 🛠️ “Tu primer robot de ventas”: Clasificá leads y respondelos automáticamente con N8N + OpenAI

**Herramientas necesarias:** Cuenta gratuita de N8N Cloud, una cuenta de Google (Sheets/Gmail) y una API Key de OpenAI (podés usar los créditos gratuitos iniciales).

---

**Paso 1: Creá tu “tablero de control” en Google Sheets**
- Creá una hoja llamada `Leads Curso IA`.
- Columnas: `Nombre`, `Email`, `Presupuesto`, `Necesidad`, `Clasificación IA`, `¿Notificado?`.
- Completá 2 o 3 filas de ejemplo con datos falsos de potenciales clientes.

**Paso 2: Entrá a N8N Cloud y creá un “Workflow” nuevo**
- Dale clic a **“Add Workflow”** y nombralo: `Robot de Ventas v1`.

**Paso 3: Configurá el disparador (Trigger)**
- Buscá el nodo **“Google Sheets”** y arrastralo al canvas (tablero).
- Elegí la acción **“Read Rows”** (leer filas).
- Conectá tu cuenta de Google y seleccioná la hoja y pestaña que creaste.
- Esto le dice a N8N: *“Revisá la hoja periódicamente”*.

**Paso 4: Agregá el “cerebro” de IA (OpenAI)**
- Buscá el nodo **“OpenAI”** y conectalo al nodo de Google Sheets.
- Dentro de la configuración de OpenAI, seleccioná **“Create Chat Completion”**.
- En el campo de **System Prompt** escribí:  
  *“Sos un vendedor experto para mi startup. Clasificá al lead como ‘CALIENTE’ si su presupuesto es mayor a 500 USD y su necesidad es urgente. Si no, clasificá como ‘FRIO’. Solo respondé una palabra: CALIENTE o FRIO.”*
- En **User Prompt**, arrastrá los datos de la hoja: *“El lead se llama X, tiene un presupuesto de Y y necesita Z”*.

**Paso 5: Creá la regla de decisión (el “Si A, entonces B”)**
- Agregá un nodo **“IF”** (también llamado *Conditional*).
- Configuralo para que, si el texto que devuelve OpenAI **contiene “CALIENTE”**, vaya por la rama **“true”**; si no, por la **“false”**.

**Paso 6: Configurá las acciones finales**
- En la rama **“true” (CALIENTE):**
  - Agregá un nodo **“Gmail”** (o Email) para enviarte un correo a vos o a tu vendedor con el asunto: `🔥 Lead Caliente: [Nombre]`.
  - Agregá otro nodo **“Google Sheets”** en modo **“Update Row”** para escribir “CALIENTE” en la columna `Clasificación IA` y “SI” en `¿Notificado?`.
- En la rama **“false” (FRIO):**
  - Agregá solo un nodo **“Google Sheets”** para actualizar la fila con “FRIO”.

**Paso 7: Probar y activar**
- Hacé clic en **“Test Workflow”**. Observá cómo N8N lee la hoja, consulta a la IA, toma una decisión y actualiza/alerta según corresponda.
- Si funciona, activá el “toggle” de **“Active”** para que se ejecute solo (por ejemplo, cada hora o cada vez que detecte una nueva fila, según tu configuración).

> 💡 **Tip para no caer en la trampa técnica:** Si te sentís perdido en la conexión de Google o OpenAI, usá las guías visuales de N8N. No necesitás saber de código; solo copiar y pegar claves de seguridad (API Keys) como si fuera una contraseña de banca online.

---

## 5. Recursos adicionales

| Recurso | Descripción | Enlace/Indicación |
|---------|-------------|-------------------|
| **Plantilla del flujo del ejercicio** | JSON listo para importar en tu N8N y no empezar de cero. | Buscá en el material complementario del curso: `plantilla_robot_ventas_n8n.json`. |
| **Video tutorial complementario** | *“De cero a tu primera automatización en 20 minutos”*, grabado especialmente para emprendedores no técnicos. | Disponible en la plataforma del curso, sección Videos. |
| **Prompts para clasificación de leads** | Biblioteca de 5 prompts probados para ventas, soporte y contenido. | PDF descargable en el módulo. |
| **Comparativa rápida: N8N vs Make vs Zapier** | Tabla para decidir qué herramienta usar según tu presupuesto y complejidad. | Incluido en las diapositivas del módulo. |
| **Comunidad de N8N en español** | Grupo de Telegram donde emprendedores latinoamericanos comparten flujos y resuelven dudas. | Buscá en Telegram: *“N8N en Español — Automatizadores LATAM”*. |

---

## 6. Preguntas de autoevaluación

### Pregunta 1 (Comprensión conceptual)
En un flujo de automatización, ¿cuál es la diferencia principal entre un **Trigger** y una **Action**?
- A) No hay diferencia; son sinónimos.
- B) El Trigger es el evento que inicia el flujo (*“cuando pasa algo”*); la Action es la tarea que ejecuta el flujo (*“hace algo”*).
- C) El Trigger solo sirve para enviar emails; la Action es solo para recibir datos.

<details>
<summary>Ver respuesta correcta</summary>

**B)** — El Trigger es el detonante (ej: nueva fila, nuevo mensaje); la Action es la ejecución (ej: enviar email, clasificar con IA).
</details>

---

### Pregunta 2 (Aplicación al negocio)
Tu startup de cursos online recibe un pago a las 2 a.m. El alumno necesita recibir **inmediatamente** su usuario y contraseña de acceso al campus, y vos querés ser notificado por la mañana **solo si** el monto es mayor a $200 (para ofrecerle un upgrade a asesoría). ¿Qué combinación de nodos necesitás mínimamente en tu flujo?

- A) Gmail (solo para enviar el mail al alumno).
- B) Trigger de pago (ej. Stripe/PayPal) → Nodo de IA o IF (para verificar si el monto > $200) → Gmail (enviar acceso al alumno) + WhatsApp/Email (alerta condicional a vos).
- C) Un solo nodo de Google Sheets que escriba “pagó”.

<details>
<summary>Ver respuesta correcta</summary>

**B)** — Necesitás un disparador de pago, una condición para filtrar por monto y dos acciones diferentes: una para el alumno (siempre) y otra para tu equipo (condicional).
</details>

---

### Pregunta 3 (Reflexión y acción)
Mirá honestamente tu operación actual. Escribí **una tarea concreta** que:
1. Te consuma más de 3 horas semanales.
2. Sea altamente repetitiva.
3. Involucre leer, escribir o clasificar texto (ideal para IA).

Describí en 4 líneas máximo: **¿cuál sería el Trigger y cuál la Action principal** para automatizarla sin tocar una línea de código?

> *(Esta pregunta no tiene respuesta fija; usala para compartir tu caso en el foro del curso y recibir feedback del instructor sobre si conviene automatizarlo con N8N u otra herramienta).*