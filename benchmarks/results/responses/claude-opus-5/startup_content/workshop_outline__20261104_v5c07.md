# Claude Opus 5 — startup_content/workshop_outline

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.49 | quality: 9.72
- latency_total: 253.701s | tokens_per_second: 70.6
- input_tokens: 314 | output_tokens: 17906
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

# WORKSHOP: "Construye tu Asistente de IA para tu Startup"
## Guía completa de facilitación — 3 horas presenciales

---

## CONTEXTO Y PROMESA DEL WORKSHOP

**Promesa al participante:**
> "Entras sin saber nada de IA. Sales con un asistente funcionando que responde preguntas de tus clientes con TU información, TU tono y TU conocimiento del negocio."

**Lo que NO es este workshop:**
- No es una charla sobre "el futuro de la IA"
- No es un curso de programación
- No es una demo donde solo mira el facilitador

**Lo que SÍ es:**
- Taller con laptop abierta desde el minuto 25
- Cada persona se va con un link funcionando que puede compartir
- Enfoque en 1 caso de uso real de SU negocio

**Nivel técnico requerido:** Saber usar Google Docs. Eso es todo.

---

# 1. AGENDA DETALLADA (180 minutos)

| # | Bloque | Duración | Reloj | Tipo |
|---|--------|----------|-------|------|
| 0 | Pre-workshop / Check-in técnico | 15 min | -15 a 0 | Logística |
| 1 | Apertura: "El empleado que nunca duerme" | 15 min | 0:00–0:15 | Charla + encuesta viva |
| 2 | Demo demoledora: 3 asistentes en vivo | 15 min | 0:15–0:30 | Demo |
| 3 | Ejercicio 1: Encuentra tu tarea sangrante | 20 min | 0:30–0:50 | Ejercicio individual + parejas |
| 4 | Mini-clase: Cómo piensa un asistente de IA | 20 min | 0:50–1:10 | Charla con analogías |
| 5 | **BUILD SPRINT 1** — Tu asistente nace | 30 min | 1:10–1:40 | Hands-on guiado |
| — | ☕ BREAK + Galería de asistentes | 15 min | 1:40–1:55 | Networking activo |
| 6 | Mini-clase: Prompt de sistema y personalidad | 15 min | 1:55–2:10 | Charla + ejemplos |
| 7 | **BUILD SPRINT 2** — Dale cerebro y carácter | 25 min | 2:10–2:35 | Hands-on + QA cruzado |
| 8 | Demo Day Express: 6 asistentes al frente | 15 min | 2:35–2:50 | Pitches de 90 seg |
| 9 | Qué sigue: escalar, integrar, cuidarte | 10 min | 2:50–3:00 | Charla + cierre |

**Total: 180 minutos** (con 5 min de colchón distribuido)

---

# 2. MATERIALES Y PREPARACIÓN

## 2.1 Preparación del facilitador (1 semana antes)

**Comunicación previa a participantes (email -7 días):**
- Traer laptop cargada + cargador (NO tablet, NO celular como único dispositivo)
- Crear cuenta gratuita en la plataforma elegida ANTES de llegar
- **Tarea previa obligatoria:** traer en un Google Doc o PDF:
  - Lista de 10–20 preguntas frecuentes de sus clientes
  - Descripción de su producto/servicio (1 página)
  - Precios o rangos de precios (si aplica)
- Email -1 día: recordatorio + link al checklist

**Decisión de plataforma — elige UNA como "oficial":**

| Opción | Pro | Contra | Recomendación |
|--------|-----|--------|---------------|
| **Custom GPT (ChatGPT)** | Súper simple, UI en español, carga archivos fácil | Requiere Plus ($20) | ⭐ Primera opción si el grupo puede pagar |
| **Google Gemini Gems** | Gratis, cuenta Google ya existe | Menos opciones de publicación | ⭐ Primera opción si presupuesto = 0 |
| **Claude Projects** | Excelente con documentos largos | Requiere plan pago para compartir | Plan B |
| **Chatbase / Botpress** | Se embebe en web real, widget | Más pasos, curva mayor | Para el "qué sigue" |

> **Recomendación de facilitación:** Oficializa **Gemini Gems** (gratis, cero friction) y menciona Custom GPT como "versión premium". Así nadie se queda fuera por dinero. Tener ambos tutoriales listos.

## 2.2 Materiales físicos

| Material | Cantidad | Uso |
|----------|----------|-----|
| Plantilla impresa "Canvas del Asistente" | 1 por persona + 10 extra | Ejercicio principal |
| Post-its 3 colores (amarillo/rosa/verde) | 1 block por mesa | Ejercicio 1 |
| Marcadores gruesos | 2 por mesa | Canvas |
| Papelógrafo "Muro de Tareas Sangrantes" | 2 pliegos | Ejercicio 1 colectivo |
| Tarjetas de mesa numeradas | 5–6 mesas | Logística |
| Stickers rojo/verde | 2 por persona | Sistema de ayuda |
| Tarjeta impresa "Recursos para llevar" + QR | 1 por persona | Cierre |

**Sistema de stickers (crítico en workshops hands-on):**
Cada persona pega en su laptop un sticker verde ("voy bien") y uno rojo ("estoy atascado"). Durante los sprints, levantan el rojo en la pantalla cerrada o lo pegan visible. El facilitador y asistentes escanean la sala visualmente. Elimina el "no quiero levantar la mano".

## 2.3 Logística de sala

- **Formato:** mesas redondas o islas de 5 personas (NO filas de auditorio)
- **Energía eléctrica:** 1 regleta por mesa — confirmar con el venue
- **WiFi:** probar velocidad con 25 dispositivos simultáneos. Tener hotspot 4G de respaldo.
- **Proyector:** probar que se lea el texto desde la última fila (tamaño mínimo 24pt en demos)
- **Agua y café disponible todo el tiempo**, no solo en el break

## 2.4 Equipo humano

- **1 facilitador principal**
- **2 asistentes técnicos** (ratio 1:10) — su único trabajo es resolver atascos durante sprints
- Brief a asistentes: "No resuelvan por ellos. Pregunten '¿qué intentaste?' y guíen. Máximo 3 min por persona."

## 2.5 Plan B técnico (tenlo listo, lo vas a necesitar)

- Si cae el WiFi: tener 5 asistentes pre-construidos de distintos rubros para que trabajen sobre ellos en modo "edición conceptual" en el Canvas de papel
- Si alguien no trae laptop: parejas obligadas (uno maneja, uno dicta) — funciona bien
- Si alguien no trae su documento de FAQs: tener un paquete genérico por rubro (restaurante, consultoría, ecommerce, servicios) en una carpeta Drive

---

# 3. DESARROLLO BLOQUE POR BLOQUE

---

## BLOQUE 0 — Pre-workshop: Check-in técnico
**Duración:** 15 min (antes de la hora de inicio)
**Slides: 1** (slide de bienvenida con checklist proyectado)

**Objetivo:** Que a la hora cero, el 100% esté logueado y nadie pierda los primeros 30 min peleando con contraseñas.

**Dinámica:**
Mientras llega la gente, hay un slide proyectado:

> **ANTES DE SENTARTE:**
> 1. Conéctate al WiFi: `[red] / [clave]`
> 2. Abre `gemini.google.com` y loguéate
> 3. Abre tu documento de FAQs
> 4. Pega tu sticker VERDE en la laptop
> 5. Si algo falla → levanta la mano, alguien va

Los asistentes técnicos circulan resolviendo. Café disponible.

**Key takeaway:** "Aquí se trabaja, no se escucha."

---

## BLOQUE 1 — Apertura: "El empleado que nunca duerme"
**Duración:** 15 min
**Slides: 8**

**Objetivo:** Conectar emocionalmente con el dolor real (estoy haciendo todo yo), bajar el miedo técnico y establecer el contrato del workshop.

**Dinámica:** Charla energética + encuesta viva de pie.

### Guion sugerido

**(2 min) Encuesta viva — todos de pie:**
> "Siéntate solo si NO te aplica. Permanece de pie si sí:
> — ¿Respondes mensajes de clientes después de las 9pm?
> — ¿Has contestado la misma pregunta más de 20 veces este mes?
> — ¿Has perdido un cliente porque tardaste en responder?
> — ¿Haces cotizaciones/propuestas desde cero cada vez?"

Mira la sala. Casi todos de pie. **"Esto es por lo que estamos aquí."**

**(5 min) El reframe central:**

El mensaje clave NO es "la IA es el futuro". Es:

> "Tú no necesitas aprender IA. Necesitas dejar de ser el cuello de botella de tu propia empresa.
>
> Hoy no vas a aprender inteligencia artificial. Vas a **contratar a tu primer empleado digital**. Y lo vas a entrenar en los próximos 90 minutos."

**(3 min) Qué sí y qué no:**

| Un asistente de IA SÍ puede | NO puede (todavía) |
|---|---|
| Responder las 50 preguntas repetidas de tus clientes | Cerrar la venta y cobrar |
| Redactar tu propuesta en tu tono, en 2 min | Entender el contexto político de tu cliente |
| Explicar tus precios y políticas sin errores | Reemplazar tu criterio en decisiones difíciles |
| Darte un primer borrador de cualquier cosa | Hacerse responsable de un error |

> "Regla de oro: la IA hace el primer 80%. Tú haces el 20% que te hace valioso."

**(3 min) Expectativas y el contrato:**
> "Al final de estas 3 horas vas a tener un link funcionando. No un PDF de apuntes. Un link. Que puedes mandar a tu socio hoy mismo.
>
> Mi contrato contigo: cero teoría innecesaria.
> Tu contrato conmigo: laptop abierta, celular abajo, y si te atascas, lo dices."

**(2 min) Presentación express por mesa:**
Cada persona dice en 20 segundos: nombre, qué vende, y "la tarea que más odio de mi semana".

**Key takeaway:**
> "No voy a aprender IA. Voy a contratar y entrenar a mi primer empleado digital. Hoy."

---

## BLOQUE 2 — Demo demoledora: 3 asistentes en vivo
**Duración:** 15 min
**Slides: 3** (puro screen share, slides mínimas)

**Objetivo:** Crear el momento "ah, ESO quiero" y mostrar que el resultado es alcanzable, no mágico.

**Dinámica:** Demo en vivo. Facilitador en pantalla grande. Participantes solo mirando (laptops cerradas o a medio cerrar — importante, que miren).

### Las 3 demos (5 min cada una)

**Demo 1 — "La Recepcionista": Asistente de FAQs de clientes**
Un asistente pre-construido de una marca ficticia pero realista: *"Panadería Artesanal La Masa"*.
- Preguntar: "¿hacen tortas para 50 personas?" → responde con precios reales del documento
- Preguntar: "¿tienen opciones sin gluten?" → responde con política real
- **Momento clave:** preguntar algo que NO está en los documentos → el asistente dice "no tengo esa información, te conecto con el equipo"
  > "¿Vieron eso? Esto es lo más importante de todo el día. Un buen asistente sabe cuándo callarse. Vamos a configurar eso juntos."

**Demo 2 — "El Vendedor": Generador de propuestas**
Asistente de una consultora ficticia.
- Pegar 4 líneas de notas crudas de una reunión
- En 30 segundos sale una propuesta estructurada con el tono de la marca
> "Esto es lo que antes te tomaba 2 horas un domingo."

**Demo 3 — "El Analista": Procesador de información**
- Pegar 15 reseñas de clientes desordenadas
- Pedir: "agrúpame los 3 problemas más repetidos y dame una acción para cada uno"
> "Esta es la que menos esperaban y la que más plata les va a hacer ganar."

**(cierre, 1 min) El spoiler honesto:**
> "Les voy a decir el secreto: estos tres asistentes no se construyeron con código. Se construyeron con **documentos y buenas instrucciones**. Eso es todo. Y eso lo saben hacer ustedes."

**Key takeaway:**
> "Un asistente útil = mis documentos + instrucciones claras. Cero código."

---

## BLOQUE 3 — EJERCICIO 1: Encuentra tu tarea sangrante
**Duración:** 20 min
**Slides: 4**

**Objetivo:** Que cada participante elija UN caso de uso específico y acotado. Este es el bloque que determina si el workshop funciona o no — el 90% de los fracasos vienen de elegir un caso de uso demasiado ambicioso.

**Dinámica:** Individual (5 min) → Parejas (8 min) → Muro colectivo (7 min)

### Paso 1 — Individual: El Brain Dump (5 min)
Post-its amarillos. Una tarea por post-it.
> "Escribe TODAS las tareas repetitivas de tu semana que te roban tiempo y no requieren tu genialidad. Mínimo 6 post-its. No pienses, escribe."

### Paso 2 — El Filtro 3F (3 min)
Proyectar el filtro y que cada uno puntúe sus post-its:

> **¿Es candidata para IA? Pregúntale 3 cosas:**
>
> **F1 — FRECUENTE:** ¿Pasa al menos 3 veces por semana?
> **F2 — FASTIDIOSA:** ¿La harías con los ojos cerrados y te da pereza?
> **F3 — FUNDAMENTADA:** ¿La respuesta correcta está escrita en algún lugar, o la tengo en la cabeza y la puedo escribir?
>
> **3 de 3 = empieza por ahí hoy.**
> **2 de 3 = sirve, con trabajo.**
> **1 de 3 = no es para hoy.**

> ⚠️ **Advertencia del facilitador:** "Si tu tarea requiere que la IA adivine algo que solo está en tu cabeza y nunca lo has escrito — ese es el trabajo real. Escribirlo. La IA no lee mentes, lee documentos."

### Paso 3 — Parejas: Afilar el caso (8 min)
Rotar al vecino. 4 min cada uno. El que escucha tiene UNA sola misión: **hacer el caso más pequeño.**

Preguntas obligatorias del escucha (proyectadas):
1. "¿Quién exactamente le va a hablar al asistente? ¿Tu cliente o tú?"
2. "¿Me puedes decir 3 preguntas EXACTAS que le harán?"
3. "¿Dónde está escrita la respuesta hoy? ¿Existe ese documento?"
4. "¿Cómo sabrás si funcionó? Dame un número."

### Paso 4 — Muro de Tareas Sangrantes (4 min)
Todos pegan su post-it ganador en el papelógrafo, agrupados por categoría (el facilitador va clusterizando en voz alta: "atención a clientes... generación de contenido... procesos internos...").

El facilitador lee 5–6 en voz alta y hace micro-coaching público de 30 segundos:
> "'Asistente que maneje toda mi empresa' — demasiado grande. Hoy haz: 'asistente que responda las 15 preguntas de WhatsApp'. Eso sí lo terminas hoy."

**Key takeaway:**
> "El error #1 es querer un asistente que haga todo. El ganador es el que resuelve UNA tarea específica, frecuente y documentada. Empieza chiquito y gana rápido."

---

## BLOQUE 4 — Mini-clase: Cómo piensa un asistente de IA
**Duración:** 20 min
**Slides: 12**

**Objetivo:** Dar el modelo mental mínimo indispensable para que el build sprint tenga sentido y no sea copiar-pegar a ciegas.

**Dinámica:** Charla con analogías + 2 micro-demos de 90 segundos.

### Contenido

**(4 min) La analogía madre: El Pasante Brillante con Amnesia**

> "Imagina que contratas a un pasante que:
> - Leyó medio internet, es increíblemente rápido y escribe mejor que tú
> - **Pero cada mañana llega sin recordar nada de tu empresa**
> - Y si no sabe algo, antes de decir 'no sé', **se inventa algo que suena creíble** para no quedar mal
>
> Todo lo que vamos a hacer hoy es resolver esas dos últimas cosas."

Esto permite introducir los 3 conceptos de forma natural:

| Concepto técnico | Cómo lo explicamos hoy |
|---|---|
| Prompt de sistema | **El manual de inducción** del pasante: quién eres, cómo hablas, qué NO haces |
| Base de conocimiento (RAG) | **La carpeta** que le dejas en el escritorio para que consulte |
| Alucinación | Cuando el pasante **inventa para no quedar mal** |

**(5 min) Los 4 ingredientes de todo asistente**
Slide con diagrama simple:

```
┌────────────────────────────────────────────┐
│  1. ROL      → Quién es y para quién       │
│  2. CONOCIMIENTO → Qué documentos consulta │
│  3. REGLAS   → Qué hace y qué NUNCA hace   │
│  4. FORMATO  → Cómo responde (tono, largo) │
└────────────────────────────────────────────┘
```
> "Estos 4 son el 90% del resultado. Lo demás es afinar."

**(4 min) Micro-demo del contraste**
En vivo, mismo pedido, dos asistentes:
- Asistente A (sin instrucciones): respuesta genérica, larga, en tono corporativo gringo
- Asistente B (con los 4 ingredientes): respuesta corta, en el tono de la marca, con precios reales y cerrando con una pregunta de venta

> "La diferencia no es la IA. Es la instrucción. Y eso lo controlas tú."

**(4 min) Alucinaciones: el riesgo real para tu negocio**
> "Si tu asistente inventa un precio que no existe, el problema no es técnico. Es legal y reputacional."

**Las 3 defensas (y las vamos a implementar hoy):**
1. **Darle fuentes** → sube tus documentos reales
2. **Darle permiso de no saber** → "si no está en tus documentos, di que no lo sabes y deriva a WhatsApp +52..."
3. **Humano en el loop** → nunca dejes que confirme compras, descuentos o fechas sin validación

**(3 min) Privacidad y datos: lo que debes saber hoy**
Reglas prácticas, sin discurso legal:
- ❌ NO subas datos personales de clientes (cédulas, direcciones, historial médico, tarjetas)
- ❌ NO subas contratos confidenciales ni información de nómina
- ✅ SÍ sube catálogos, FAQs, precios públicos, políticas, tu tono de marca
- ✅ Revisa la configuración de "usar mis datos para entrenamiento" y apágala si existe
> "Regla simple: si no lo pondrías en tu página web o no se lo mandarías a un proveedor nuevo, no lo subas hoy."

**Key takeaway:**
> "Un asistente es un pasante brillante con amnesia. Mi trabajo es darle (1) un rol claro, (2) documentos reales, (3) permiso para decir 'no sé'. Eso es todo el truco."

---

## BLOQUE 5 — BUILD SPRINT 1: Tu asistente nace
**Duración:** 30 min
**Slides: 6** (pasos numerados, grandes, visibles desde el fondo)

**Objetivo:** Que el 100% de la sala tenga un asistente creado, con conocimiento cargado y respondiendo su primera pregunta. **Es el bloque crítico del workshop.**

**Dinámica:** Hands-on guiado, ritmo de "yo hago → tú haces". Música de fondo baja. Asistentes técnicos circulando.

### Estructura del sprint

**(3 min) El Canvas primero, la pantalla después**
> "Antes de tocar la computadora: llena las 4 primeras cajas de tu Canvas. Cinco minutos de papel te ahorran veinte de pantalla."

**(5 min) Paso 1: Crear el asistente y ponerle rol**
Facilitador demuestra en pantalla, paso a paso, con pausas:
1. Crear nuevo Gem / Custom GPT
2. Nombre del asistente (que suene a empleado: "Sofía de Atención", no "Bot v1")
3. Pegar el **prompt de sistema versión 1** desde la plantilla (ver sección 4)

> "Levanten la mano quien ya tiene su asistente creado con nombre." → esperar al 80% antes de avanzar.

**(10 min) Paso 2: Cargar el conocimiento**
1. Subir el documento de FAQs / catálogo / precios
2. Si no tienen documento listo: 10 minutos para escribir las 10 preguntas y sus respuestas en un Doc y subirlo
3. Guardar

> ⚠️ Punto de atasco frecuente: formatos. Tener listo el tip: "Si falla el PDF, cópialo a un Google Doc y súbelo así. O pega el texto directamente en las instrucciones."

**(8 min) Paso 3: Primer contacto — la Prueba del Cliente Real**
> "Ahora háblale como te hablaría tu cliente más impaciente. No como le hablarías a un robot."

Las 3 preguntas obligatorias de prueba:
1. Una pregunta que **SÍ** está en sus documentos
2. Una pregunta que **NO** está (ver si inventa)
3. Una pregunta **mal escrita, con faltas de ortografía y jerga local** ("ola cuanto sale lo mas varato q tengan")

Anotar en el Canvas: ¿qué respondió mal? ¿qué inventó? ¿qué tono se sintió falso?

**(4 min) Check de sala y rescate**
Facilitador pide levantar sticker rojo. Asistentes atienden. Facilitador resuelve en voz alta los 2 atascos más comunes de la sala.

**Key takeaway:**
> "Ya tengo un asistente vivo. Es mediocre, y eso es exactamente lo normal en la versión 1. Ahora empieza el trabajo real: entrenarlo."

---

## ☕ BREAK + GALERÍA DE ASISTENTES
**Duración:** 15 min

**No es un break pasivo.** Instrucción:
> "Dejen su laptop abierta con el asistente en pantalla. Levántense, sírvanse café y vayan a probar el asistente de 3 personas de OTRAS mesas. Déjenle un post-it rosa con una pregunta que no supo responder bien."

Esto genera:
- Testing cruzado gratis y real (nadie prueba su propio producto bien)
- Networking con un pretexto concreto, no forzado
- Insumos accionables para el Sprint 2
- La energía no cae, que es el riesgo típico del break en la hora 1:40

---

## BLOQUE 6 — Mini-clase: Prompt de sistema y personalidad
**Duración:** 15 min
**Slides: 10**

**Objetivo:** Dar las herramientas para pasar de "funciona" a "funciona bien y suena a mi marca". Aquí es donde el asistente se vuelve defendible como activo del negocio.

**Dinámica:** Charla + corrección en vivo de un prompt malo (con voluntario de la sala).

### Contenido

**(5 min) La anatomía de un buen prompt de sistema**
Mostrar el antes/después:

❌ **Prompt débil:**
> "Eres un asistente útil que responde preguntas sobre mi negocio de forma amable."

✅ **Prompt fuerte (estructura de 6 bloques):**

```
1. ROL:        Eres [nombre], asistente de [empresa], que vende
               [producto] a [cliente].

2. OBJETIVO:   Tu meta es resolver dudas rápido y lograr que la
               persona [acción deseada: agende / cotice / compre].

3. TONO:       Habla en [español de México / rioplatense / neutro],
               tuteando. Máximo 4 líneas por respuesta. Cálido pero
               directo. Nada de "estimado usuario".

4. CONOCIMIENTO: Responde ÚNICAMENTE con base en los documentos
               adjuntos.

5. REGLAS DURAS:
   - Si la información NO está en los documentos, di exactamente:
     "No tengo ese dato, te paso con el equipo: [WhatsApp]".
   - NUNCA inventes precios, plazos, descuentos ni disponibilidad.
   - NUNCA ofrezcas descuentos ni confirmes fechas de entrega.
   - Si la persona está molesta o pide hablar con un humano,
     derívala de inmediato sin insistir.

6. CIERRE:     Termina cada respuesta con UNA pregunta que ayude a
               avanzar (ej: "¿Te comparto los horarios disponibles?")
```

**(4 min) Los 4 errores que vemos siempre**
1. **Prompt genérico** → "asistente amable" no significa nada. Sé específico o no digas nada.
2. **Sin reglas de "no sé"** → es la causa #1 de problemas reales con clientes
3. **Sin límite de longitud** → nadie lee 3 párrafos en WhatsApp
4. **Tono copiado de gringo traducido** → "Estimado usuario, ¡gracias por su consulta!" nadie habla así

**(6 min) Corrección en vivo — voluntario de la sala**
Pedir un voluntario que proyecte su prompt. El facilitador lo mejora en vivo con la sala aportando. Esto vale más que 10 slides, porque todos ven el "cómo se piensa".

> Facilitador modela el proceso en voz alta: "Aquí dice 'amable'. ¿Amable cómo? ¿Como un banco o como tu vecina? Ah, como tu vecina. Entonces escribimos: 'cercano, tuteando, puedes usar máximo un emoji'."

**Key takeaway:**
> "El tono y las reglas de qué NO hacer son lo que separa un bot genérico de un asistente que representa dignamente a mi marca."

---

## BLOQUE 7 — BUILD SPRINT 2: Dale cerebro y carácter
**Duración:** 25 min
**Slides: 4**

**Objetivo:** Iterar con base en evidencia (los post-its rosas del break) y dejar el asistente en estado "usable mañana".

**Dinámica:** Hands-on + QA cruzado estructurado en parejas.

**(12 min) Iteración individual — las 4 mejoras obligatorias**
Checklist proyectado, que todos ejecuten:

> ☐ **1.** Reescribe tu prompt con la estructura de 6 bloques
> ☐ **2.** Agrega tu **regla de "no sé"** con tu contacto real de derivación
> ☐ **3.** Define el **límite de longitud** y el idioma/tono local
> ☐ **4.** Resuelve los fallos de los post-its rosas (agregando info al documento o regla al prompt)

**(10 min) QA cruzado en parejas — "Rompe mi asistente"**
Intercambian laptops. 5 min cada uno. El tester tiene una misión adversarial:

> **Protocolo "Rompe mi asistente" — intenta las 5:**
> 1. Pregúntale algo que NO esté en sus documentos → ¿se inventó algo?
> 2. Pídele un descuento del 50% → ¿lo ofreció?
> 3. Escríbele con faltas de ortografía y jerga local → ¿entendió?
> 4. Enójate y exige hablar con un humano → ¿te derivó bien?
> 5. Pregúntale algo totalmente fuera de tema (fútbol, política) → ¿se mantuvo en su rol?

El tester anota resultados en el Canvas del dueño, sección "Bitácora de fallos".

**(3 min) Fix final express**
Cada uno aplica el arreglo más importante que encontró su pareja.

**Key takeaway:**
> "No se mejora un asistente adivinando. Se mejora probándolo con adversarios y arreglando lo que falló. Esto nunca termina: es el ciclo probar → arreglar → probar."

---

## BLOQUE 8 — DEMO DAY EXPRESS
**Duración:** 15 min
**Slides: 2**

**Objetivo:** Cerrar con sensación de logro colectivo, cross-polinizar ideas y generar compromiso público.

**Dinámica:** 6 voluntarios (uno por mesa), 90 segundos cada uno, laptop conectada al proyector o pantalla compartida.

**Formato estricto del pitch (proyectado con cronómetro visible):**
> 1. "Mi negocio es ___ y la tarea que odiaba era ___" (20 seg)
> 2. **Demo en vivo:** una pregunta, una respuesta (40 seg)
> 3. "Lo que más me sorprendió fue ___" (15 seg)
> 4. "El lunes lo voy a usar para ___" (15 seg)

El facilitador selecciona voluntarios durante el Sprint 2 para asegurar diversidad de rubros (no 6 consultores). Aplausos obligatorios. Si hay presupuesto: premio simbólico al mejor tono de marca y al "mejor rompiendo asistentes" (reconocer al mejor tester).

**Key takeaway:**
> "Entré sin saber nada y en 3 horas tengo algo funcionando. Y los 25 casos de uso de la sala son 25 ideas que puedo robar."

---

## BLOQUE 9 — Qué sigue: escalar, integrar, cuidarte
**Duración:** 10 min
**Slides: 8**

**Objetivo:** Dar el mapa de los siguientes 30 días para que el asistente no muera el martes, y advertir honestamente sobre los riesgos.

**Dinámica:** Charla rápida + compromiso escrito.

**(4 min) La escalera de madurez — dónde estás y qué sigue**

| Nivel | Qué es | Esfuerzo | Tú estás aquí |
|---|---|---|---|
| **1. Asistente interno** | Lo usas tú y tu equipo | ✅ Hecho hoy | ⬅️ |
| **2. Asistente compartido** | Link a clientes beta y socios | 1 semana | Próximo paso |
| **3. Widget en tu web** | Chat embebido (Chatbase, Botpress) | 2–4 semanas | |
| **4. Conectado a WhatsApp** | Donde realmente están tus clientes en LATAM | 1–2 meses, requiere ayuda o proveedor | |
| **5. Integrado a tus sistemas** | Lee tu CRM, agenda, inventario en vivo | Requiere desarrollador | |

> "No salten al nivel 4. El 90% del valor está en el 1 y 2, y es lo único que pueden sostener solos."

**(3 min) Las 3 advertencias honestas**
1. **Esto no se mantiene solo.** Agenda 30 min cada viernes: revisa las conversaciones, agrega lo que no supo responder. Sin esto, tu asistente se vuelve obsoleto en un mes.
2. **Nunca dejes que la IA sea la última palabra en dinero, plazos legales o datos sensibles.** Siempre humano en el loop.
3. **Cuidado con el "síndrome del juguete nuevo".** Si tu asistente no te ahorra tiempo medible o no te gana un cliente, apágalo. No es un trofeo, es una herramienta.

**(3 min) Compromiso y cierre**
Última página del Canvas, llenar y fotografiar:

> **MI COMPROMISO DE 7 DÍAS**
> En los próximos 7 días voy a:
> ☐ Compartir el link de mi asistente con ____ personas
> ☐ Agregar ____ a su base de conocimiento
> ☐ Medir si me ahorró ____ horas / ganó ____ consultas
>
> Mi accountability partner de este workshop: ______________
> (nombre + WhatsApp de alguien de la sala)

**Cierre del facilitador:**
> "Hoy no aprendieron inteligencia artificial. Contrataron a su primer empleado digital y lo entrenaron en 3 horas. La diferencia entre los que van a usar esto y los que no, no es técnica. Es que el lunes a las 9am, unos van a abrir el link y otros no. Nos vemos en el grupo de WhatsApp."

**Key takeaway:**
> "Mi asistente es un activo vivo, no un proyecto terminado. 30 minutos cada viernes y mi compromiso de 7 días es la diferencia entre una herramienta y un recuerdo de workshop."

---

# 4. EJERCICIO PRINCIPAL: "CANVAS DEL ASISTENTE"

Es el hilo conductor de todo el workshop. Documento impreso de 2 caras que se llena progresivamente y que el participante se lleva como plano de trabajo.

## CARA A — Diseño del asistente

```
╔═══════════════════════════════════════════════════════════════╗
║           CANVAS DEL ASISTENTE DE IA                          ║
║   Nombre: ____________    Negocio: ____________               ║
╚═══════════════════════════════════════════════════════════════╝

┌─── 1. LA TAREA SANGRANTE ──────────────── (Bloque 3) ────────┐
│                                                               │
│ Tarea que resuelve: _______________________________________   │
│                                                               │
│ Pasa ___ veces por semana · Me toma ___ min cada vez          │
│                                                               │
│ Filtro 3F:  Frecuente ☐   Fastidiosa ☐   Fundamentada ☐      │
│ (necesitas 3 de 3 para empezar por aquí hoy)                  │
└───────────────────────────────────────────────────────────────┘

┌─── 2. ¿QUIÉN LE HABLA? ────────────────── (Bloque 3) ────────┐
│                                                               │
│ Usuario:  ☐ Mi cliente   ☐ Mi equipo   ☐ Yo                   │
│                                                               │
│ Las 3 preguntas EXACTAS que le va a hacer:                    │
│ 1. ____________________________________________________       │
│ 2. ____________________________________________________       │
│ 3. ____________________________________________________       │
└───────────────────────────────────────────────────────────────┘

┌─── 3. SU CONOCIMIENTO ─────────────────── (Bloque 5) ────────┐
│                                                               │
│ Documentos que le voy a dar:          ¿Ya existe?             │
│ ☐ _________________________________    Sí ☐  Lo creo hoy ☐    │
│ ☐ _________________________________    Sí ☐  Lo creo hoy ☐    │
│ ☐ _________________________________    Sí ☐  Lo creo hoy ☐    │
│                                                               │
│ ⚠️ Lo que NUNCA voy a subir (datos sensibles):                │
│ ______________________________________________________        │
└───────────────────────────────────────────────────────────────┘

┌─── 4. SU PERSONALIDAD ─────────────────── (Bloque 6) ────────┐
│                                                               │
│ Se llama: _________________                                   │
│                                                               │
│ Habla como... (marca 2):                                      │
│ ☐ Vecina de confianza  ☐ Experto serio  ☐ Amigo jovial        │
│ ☐ Asesor premium       ☐ Directo al punto                     │
│                                                               │
│ Tutea ☐  /  Usted ☐        Máximo ___ líneas por respuesta    │
│ Emojis: Sí ☐ No ☐          Modismos locales: ____________     │
│                                                               │
│ Frases que NUNCA diría: _______________________________       │
└───────────────────────────────────────────────────────────────┘

┌─── 5. SUS LÍMITES (lo más importante) ─── (Bloque 7) ────────┐
│                                                               │
│ Cuando NO sepa algo, dirá exactamente:                        │
│ "_____________________________________________________"       │
│                                                               │
│ Y derivará a: _______________________ (WhatsApp/email real)   │
│                                                               │
│ NUNCA debe:                                                   │
│ ☐ Inventar precios   ☐ Ofrecer descuentos                     │
│ ☐ Confirmar fechas   ☐ Dar consejo legal/médico/financiero    │
│ ☐ Otro: ______________________________________________        │
└───────────────────────────────────────────────────────────────┘

┌─── 6. MI PROMPT DE SISTEMA ────────────── (Bloque 6) ────────┐
│ (Escribe aquí tu versión final en los 6 bloques)              │
│                                                               │
│ ROL: ________________________________________________         │
│ OBJETIVO: ___________________________________________         │
│ TONO: _______________________________________________         │
│ CONOCIMIENTO: _______________________________________         │
│ REGLAS DURAS: _______________________________________         │
│ CIERRE: _____________________________________________         │
└───────────────────────────────────────────────────────────────┘
```

## CARA B — Testing y compromiso

```
┌─── 7. BITÁCORA DE FALLOS ──────────────── (Sprint 1 y 2) ────┐
│                                                               │
│ Qué le pregunté │ Qué respondió mal │ Cómo lo arreglé         │
│─────────────────┼───────────────────┼──────────────────────   │
│                 │                   │                         │
│                 │                   │                         │
│                 │                   │                         │
│                 │                   │                         │
└───────────────────────────────────────────────────────────────┘

┌─── 8. "ROMPE MI ASISTENTE" ────────────── (Sprint 2) ────────┐
│ Lo llenó mi pareja: ____________________                      │
│                                                               │
│ 1. Pregunta sin respuesta  → ¿Inventó?        Sí ☐ No ☐       │
│ 2. Pidió descuento 50%     → ¿Lo dio?         Sí ☐ No ☐       │
│ 3. Faltas de ortografía    → ¿Entendió?       Sí ☐ No ☐       │
│ 4. Cliente enojado         → ¿Derivó bien?    Sí ☐ No ☐       │
│ 5. Tema fuera de contexto  → ¿Se mantuvo?     Sí ☐ No ☐       │
│                                                               │
│ El arreglo más urgente: ______________________________        │
└───────────────────────────────────────────────────────────────┘

┌─── 9. MI MÉTRICA DE ÉXITO ──────────────── (Bloque 9) ───────┐
│                                                               │
│ Sabré que funcionó si en 30 días:                             │
│ ☐ Me ahorró ____ horas por semana                             │
│ ☐ Respondió ____ consultas sin mí                             │
│ ☐ Me generó ____ cotizaciones/leads                           │
└───────────────────────────────────────────────────────────────┘

┌─── 10. COMPROMISO DE 7 DÍAS ────────────── (Bloque 9) ───────┐
│                                                               │
│ ☐ Comparto el link con ____ personas                          │
│ ☐ Agrego ____________ a su conocimiento                       │
│ ☐ Agendo 30 min el viernes para revisarlo                     │
│                                                               │
│ Mi accountability partner: _________ WhatsApp: _________      │
│                                                               │
│ 📸 Tómale foto a esta hoja antes de irte                      │
└───────────────────────────────────────────────────────────────┘
```

## Plantilla de prompt entregable (hoja aparte, para copiar y pegar)

```
Eres [NOMBRE], asistente de [EMPRESA]. [EMPRESA] vende [PRODUCTO]
a [TIPO DE CLIENTE].

TU OBJETIVO: resolver dudas de forma rápida y clara, y llevar a la
persona a [AGENDAR / COTIZAR / COMPRAR].

TONO: Habla en español de [PAÍS], [tuteando/de usted]. Cálido y
directo. Máximo [4] líneas por respuesta. Nunca uses lenguaje
corporativo rígido ni digas "estimado usuario".

CONOCIMIENTO: Responde ÚNICAMENTE con base en los documentos
adjuntos. No uses conocimiento general sobre el rubro.

REGLAS DURAS:
- Si la información NO está en los documentos, responde exactamente:
  "No tengo ese dato a mano, pero te conecto con el equipo:
  [CONTACTO REAL]".
- NUNCA inventes precios, plazos, disponibilidad ni políticas.
- NUNCA ofrezcas descuentos ni promociones no documentadas.
- Si la persona está molesta o pide un humano, derívala de inmediato
  sin insistir ni intentar resolver.
- Si pregunta algo fuera de [TEMA], redirige amablemente a tu función.

CIERRE: Termina cada respuesta con UNA pregunta que ayude a avanzar.
```

---

# 5. RECURSOS PARA LLEVAR A CASA

Entregados vía **QR impreso en tarjeta + email de seguimiento el mismo día**. Todo en una carpeta de Drive pública.

## Kit del participante

**📁 1. Plantillas listas para usar**
- Canvas del Asistente (PDF imprimible + versión editable en Google Docs)
- Plantilla de prompt de sistema (los 6 bloques, para copiar/pegar)
- **5 prompts pre-armados por rubro:** servicios profesionales, retail/ecommerce, restaurante, educación, inmobiliaria
- Plantilla de "Documento de Conocimiento" (estructura para escribir sus FAQs bien)

**📁 2. Guías paso a paso (con screenshots, en español)**
- Cómo crear un Gem en Gemini (gratis)
- Cómo crear un Custom GPT (plan pago)
- Cómo publicar y compartir tu asistente por link
- Cómo poner tu asistente en tu web con Chatbase (nivel 3 de la escalera)

**📁 3. Checklists operativos**
- ✅ Checklist "¿Mi asistente está listo para clientes?" (12 puntos pre-lanzamiento)
- ✅ Protocolo "Rompe mi asistente" (los 5 tests, para repetir cada mes)
- ✅ Rutina de mantenimiento de 30 minutos (qué revisar cada viernes)
- ✅ Checklist de privacidad: qué subir y qué nunca subir

**📁 4. Referencia rápida**
- Los 4 ingredientes de un asistente (1 página, para pegar en la pared)
- Filtro 3F para evaluar nuevos casos de uso
- Glosario de 10 términos sin tecnicismos (prompt, alucinación, token, RAG, API, agente...)
- "Los 7 errores más comunes y cómo evitarlos"

**📁 5. Comparativa de herramientas (actualizada)**
Tabla con precios en USD, nivel de dificultad, si tiene interfaz en español y para qué sirve cada una. Incluye opciones gratuitas y las que funcionan con WhatsApp en LATAM.

## Seguimiento post-workshop

| Cuándo | Qué |
|---|---|
| **Mismo día** | Email con carpeta de recursos + fotos del Muro de Tareas Sangrantes + grupo de WhatsApp |
| **Día 2** | Grupo de WhatsApp activo: cada quien comparte el link de su asistente para testing cruzado |
| **Día 7** | Mensaje del facilitador: "¿cumpliste tu compromiso de 7 días?" + 3 casos destacados de la sala |
| **Día 30** | Sesión opcional de 60 min online: "Mi asistente en producción — qué funcionó, qué rompí" |
| **Permanente** | Directorio de los asistentes de la cohorte (quién construyó qué, para inspirar y conectar) |

---

# 6. SLIDE COUNT ESTIMADO

| Bloque | Slides | Densidad |
|---|---|---|
| 0. Check-in técnico | 1 | Instrucciones grandes, proyectadas fijas |
| 1. Apertura | 8 | Alto impacto, poca letra |
| 2. Demo en vivo | 3 | Solo títulos — el protagonista es la pantalla |
| 3. Ejercicio 1 | 4 | Instrucciones + filtro 3F |
| 4. Mini-clase: cómo piensa | 12 | La sección más "conceptual" |
| 5. Build Sprint 1 | 6 | Pasos numerados, legibles desde el fondo |
| Break | 1 | Instrucción de la galería |
| 6. Mini-clase: prompts | 10 | Ejemplos antes/después |
| 7. Build Sprint 2 | 4 | Checklists + protocolo de testing |
| 8. Demo Day | 2 | Formato de pitch + cronómetro |
| 9. Qué sigue + cierre | 8 | Escalera, advertencias, compromiso |
| Buffer / backup | 6 | Troubleshooting, plan B, slides de rescate |
| **TOTAL** | **~65 slides** | |

**Reglas de diseño del deck:**
- Máximo 15 palabras por slide (excepto las plantillas de prompt)
- Tipografía mínima 28pt para texto, 40pt para títulos
- Los slides de instrucciones de ejercicio quedan **proyectados fijos** todo el ejercicio — nunca avanzar mientras trabajan
- Numerar los pasos de los sprints de forma gigante ("PASO 2 de 3") para que los rezagados se ubiquen sin preguntar
- Un slide-reloj visible durante sprints con el tiempo restante

---

# 7. NOTAS CRÍTICAS DE FACILITACIÓN

## Las 5 reglas de oro de este workshop

1. **El reloj manda sobre la perfección.** Si vas tarde, recorta el Bloque 4 (teoría) o el Bloque 8 (demo day a 4 personas). **Nunca recortes los Build Sprints.** Un participante sin asistente funcionando = workshop fallido para esa persona.

2. **No avances hasta el 80%.** En cada paso del sprint, pide confirmación visible (manos arriba, stickers). El ritmo lo marca el percentil 20, no el más rápido.

3. **Los que terminan rápido se vuelven ayudantes.** Dales el rol: "ya terminaste, ve a ayudar a tu mesa". Convierte un problema de ritmo en capacidad adicional de soporte.

4. **Celebra en voz alta y específico.** "¡Miren el tono que logró María, suena exactamente a su marca!" La energía del hands-on se sostiene con reconocimiento público frecuente.

5. **Si alguien no logra terminar, no lo dejes ir con las manos vacías.** Que se vaya al menos con el Canvas completo en papel. Eso ya es un plan ejecutable el lunes.

## Riesgos y mitigaciones

| Riesgo | Probabilidad | Mitigación |
|---|---|---|
| WiFi insuficiente para 25 dispositivos | **Alta** | Hotspot 4G de respaldo + probar la semana previa + plan B en papel |
| Participantes sin documento de FAQs | **Alta** | 10 min de escritura dentro del Sprint 1 + paquetes genéricos por rubro en Drive |
| Alguien quiere un asistente demasiado complejo | **Alta** | Es la razón de existir del Bloque 3. Micro-coaching público: "eso es el nivel 5, hoy hacemos el nivel 1" |
| Dispersión de ritmos (unos vuelan, otros se atascan) | **Alta** | Ratio 1:10 de soporte + rápidos como ayudantes + stickers rojo/verde |
| Escéptico que monopoliza con "la IA se equivoca" | Media | Validar y reencauzar: "tienes toda la razón, por eso el Bloque 7 es completo sobre límites y derivación a humano" |
| Caída del servicio de IA | Baja | Tener 2 plataformas como opción + screenshots del flujo completo para trabajar en papel |

## Cómo sabes que el workshop funcionó

| Métrica | Meta |
|---|---|
| Participantes con asistente funcionando al cerrar | **≥ 90%** |
| Participantes con Canvas completo | **100%** |
| Casos de uso específicos y acotados (no "que haga todo") | ≥ 80% |
| Que comparten su link en el grupo en 7 días | ≥ 50% |
| Que siguen usándolo a los 30 días | ≥ 30% |
| NPS del workshop | ≥ 60 |

> La métrica que realmente importa no es la satisfacción del día. Es cuántos abren su asistente el lunes a las 9am. Diseña todo el cierre pensando en eso.