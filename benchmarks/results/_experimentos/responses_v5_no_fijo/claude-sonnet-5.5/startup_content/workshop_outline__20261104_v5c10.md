# Claude Sonnet 5.5 — startup_content/workshop_outline

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.91 | quality: 9.72
- latency_total: 81.824s | tokens_per_second: 131.7
- input_tokens: 316 | output_tokens: 10778
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
### Workshop práctico presencial · 3 horas · 20-30 emprendedores no técnicos

**Promesa del workshop:** *"Te vas con un asistente de IA funcionando, entrenado con TU startup y probado con casos reales. Sin código y sin excusas."*

---

## 1. AGENDA DETALLADA

| Hora | Min | Bloque | Dinámica | Slides |
|---|---|---|---|---|
| 0:00 - 0:15 | 15 | **0. Arranque: Bienvenida y setup** | Rompehielos + chequeo técnico | 6 |
| 0:15 - 0:35 | 20 | **1. De "chatear con IA" a tener un asistente** | Charla corta + demo en vivo | 10 |
| 0:35 - 0:55 | 20 | **2. Encuentra tu caso de uso** | Ejercicio individual + pares | 6 |
| 0:55 - 1:25 | 30 | **3. Anatomía de un asistente: la Receta CAFÉ** | Demo + mini-ejercicio | 14 |
| 1:25 - 1:40 | 15 | ☕ **Descanso** | Café, networking, soporte técnico | 1 |
| 1:40 - 2:30 | 50 | **4. 🔥 Taller principal: construye tu asistente** | Sprints guiados | 5 |
| 2:30 - 2:50 | 20 | **5. Rompe tu asistente (y mejóralo)** | Pruebas cruzadas en parejas | 4 |
| 2:50 - 3:00 | 10 | **6. Cierre: tu plan de 7 días** | Compromiso público + recursos | 6 |
| | **180** | | **Total** | **~52** |

**Proporción:** ~65% haciendo, ~35% escuchando. Nadie se queda mirando.

---

## 2. MATERIALES Y PREPARACIÓN

### 📧 Dos semanas antes: enviar a los participantes
- **Formulario previo** (2 min): rubro de la startup, etapa, herramienta de IA que usan hoy, nivel de comodidad (1-5) y la tarea que más tiempo les quita.
- **Email de "Trae esto"**:
  - Laptop (el celular no alcanza para el taller principal).
  - Cuenta creada en **al menos una** herramienta: ChatGPT, Claude o Gemini.
  - **Un documento de su startup**: one-pager, deck, FAQs, lista de precios o descripción del producto. Aunque sea un borrador.
  - Regla de privacidad: *no traer datos personales de clientes ni información confidencial.*

### 🏢 Logística del espacio
- WiFi robusto, probado con 30 conexiones simultáneas. Tener **plan B**: hotspot de celular.
- Regletas y extensiones en cada mesa.
- Proyector, pantalla, audio y micrófono.
- Mesas en **islas de 4-5 personas**, que luego se usan como equipos de apoyo.
- Pizarra o papelógrafo, post-its, marcadores y un timer visible en pantalla.
- **Vasitos de colores** para pedir ayuda: 🟢 voy bien, 🟡 tengo una duda, 🔴 estoy trabado.
- Tarjetas de nombre con el nombre de la startup.

### 👥 Equipo
- 1 facilitador principal.
- **2 co-facilitadores o mentores** (1 por cada 10-12 personas) con experiencia en IA, para circular durante el taller principal.

### 💻 Materiales digitales (en una carpeta de Drive o Notion con QR)
- Slides.
- **Workbook** (PDF o Notion duplicable) con todos los ejercicios.
- **Plantilla Receta CAFÉ** (documento en blanco con campos).
- **Meta-prompt "Entrévistame"**: un prompt que hace que la IA entreviste al emprendedor y genere las instrucciones del asistente.
- **Caso ejemplo** para quien no tenga startup definida (ej. una cafetería de especialidad con delivery).
- **Asistente demo ya construido** (para la demo del Bloque 1).
- **Video de respaldo** de la demo, por si falla internet.
- Biblioteca de prompts (ver sección 5).

### ⚠️ Verificación técnica (1 semana antes)
Las funciones y planes de las herramientas cambian rápido. Revisa qué ofrece hoy cada plan gratuito y de pago, y qué permiten los GPTs personalizados, los Projects de Claude y los Gems de Gemini. Diseña el taller para que **funcione en cualquier herramienta**, incluso en plan gratuito, usando un "prompt maestro" pegado al inicio del chat. Quien tenga plan de pago puede subir el asistente a su formato nativo.

---

## 3. BLOQUES DETALLADOS

---

### BLOQUE 0 · Arranque: Bienvenida y setup
**⏱ 15 min · 6 slides**

**🎯 Objetivo:** Bajar la ansiedad tecnológica, crear energía de grupo y confirmar que todos tienen cuenta y acceso.

**🎬 Dinámica:**
- **(3 min)** Apertura enérgica: "Hoy nadie sale sin su asistente. Cero teoría de relleno."
- **(5 min) Rompehielos "Mi mayor tiempo perdido":** en parejas, cada uno dice la tarea repetitiva que más odia de su startup. Después, 3-4 voluntarios la comparten con todos.
- **(2 min)** Mapa del día y reglas: laptops abiertas, preguntar sin pena, vasitos de colores.
- **(5 min) Chequeo técnico:** todos abren su herramienta, escriben "Hola" y levantan la mano cuando funciona. Los co-facilitadores resuelven los problemas de acceso.

**💡 Key takeaway:** *"No necesitas ser técnico. Necesitas saber explicar bien lo que quieres, y eso ya lo haces como emprendedor."*

---

### BLOQUE 1 · De "chatear con IA" a tener un asistente
**⏱ 20 min · 10 slides**

**🎯 Objetivo:** Entender la diferencia entre usar IA de forma suelta y tener un asistente configurado, y ver el "antes y después".

**🎬 Dinámica:**
- **(5 min) Charla: el problema.** Cada vez que abres un chat nuevo empiezas de cero, tienes que reexplicar tu negocio y las respuestas son genéricas. Un asistente ya sabe quién eres, cómo hablas y qué necesitas.
- **(8 min) 🎥 Demo en vivo "Antes vs. Después":**
  - *Antes:* prompt genérico ("Respóndele a este cliente") y respuesta tibia.
  - *Después:* el asistente demo (ej. "Asistente de Ventas de [startup ejemplo]") responde con el tono de marca, los precios correctos y el siguiente paso sugerido.
  - Mismo input, resultado radicalmente distinto.
- **(4 min) Tour de ejemplos reales de asistentes para startups:**
  - Respondedor de prospectos.
  - Sintetizador de entrevistas con clientes.
  - Creador de contenido con tu voz.
  - Preparador de pitch para inversionistas.
  - Asistente de onboarding para nuevos miembros del equipo.
  - Redactor de propuestas y cotizaciones.
- **(3 min) Quick poll** (manos arriba): "¿Quién ya usa IA a diario? ¿Quién la usó 2 veces y no volvió?"

**💡 Key takeaway:** *"Un asistente es un chat con memoria de tu negocio, instrucciones claras y una sola especialidad."*

---

### BLOQUE 2 · Encuentra tu caso de uso
**⏱ 20 min · 6 slides**

**🎯 Objetivo:** Que cada participante elija **un solo caso de uso** de alto impacto y alcanzable en 50 minutos.

**🎬 Dinámica:**
- **(3 min) Charla corta:** el error #1 es querer un asistente que haga todo. Un asistente bueno es especialista, no navaja suiza.
- **(8 min) Ejercicio individual "Mapa de tareas":** en el workbook, listar 8-10 tareas repetitivas de la semana y puntuarlas de 1 a 5 en:
  - **Frecuencia** (¿cuántas veces por semana?)
  - **Dolor** (¿cuánto la odio o me quita tiempo?)
  - **Claridad** (¿puedo explicar cómo la hago bien?)
- **(4 min) Filtro de elección:** circular la tarea con mayor puntaje combinado que NO requiera datos sensibles. Escribirla en una frase:
  > *"Mi asistente me ayudará a [tarea] para [persona/situación] y entregará [resultado]."*
- **(5 min) Validación en parejas:** cada uno cuenta su elección y su compañero hace una pregunta: "¿Cómo sabrías que quedó bien?" Se ajusta la frase si hace falta.

**💡 Key takeaway:** *"Empieza con la tarea que repites más, que mejor sabes explicar y que menos riesgo tiene. Un asistente, una misión."*

**Casos sugeridos para los bloqueados:** respuestas a prospectos por WhatsApp o email, posts para LinkedIn e Instagram, síntesis de entrevistas con clientes, borrador de propuestas.

---

### BLOQUE 3 · Anatomía de un asistente: la Receta CAFÉ ☕
**⏱ 30 min · 14 slides**

**🎯 Objetivo:** Enseñar un framework simple y memorable para escribir las instrucciones de cualquier asistente.

**🎬 Dinámica:**

**(12 min) Charla + demo: la Receta CAFÉ.** Cada letra tiene un slide con un ejemplo bueno y uno malo.

| Letra | Ingrediente | Pregunta clave | Ejemplo |
|---|---|---|---|
| **C** | **Contexto y rol** | ¿Quién es el asistente y qué sabe de mi negocio? | "Eres el asistente comercial de Agrofresh, una startup que vende insumos a pequeños agricultores en Colombia." |
| **A** | **Acción** | ¿Qué tarea hace, paso a paso? | "Cuando te pase un mensaje de un prospecto: 1) identifica su necesidad, 2) responde, 3) propón siguiente paso." |
| **F** | **Formato** | ¿Cómo debe responder? | "Máximo 80 palabras, tono cercano, tuteo, sin jerga, termina con una pregunta." |
| **É** | **Ejemplos y Evita** | ¿Qué es una buena respuesta? ¿Qué nunca debe hacer? | "Aquí hay 2 respuestas ideales. Nunca inventes precios. Si no sabes, di 'lo confirmo y te escribo'." |

- **Mensaje clave del bloque:** "Si se lo explicarías a un practicante nuevo, se lo explicas a la IA."
- **Demo en vivo (5 min):** se toma un asistente mediocre y se mejora en vivo, letra por letra, mostrando cómo mejora cada respuesta.

**(8 min) Truco estrella: el meta-prompt "Entrévistame".** En vez de escribir las instrucciones desde cero, le pides a la IA que te entreviste con 8-10 preguntas y que luego redacte el asistente con la Receta CAFÉ. Se hace una demo corta.

**(8 min) Mini-ejercicio:** cada persona completa solo la **C** y la **É** de su asistente en la plantilla, para calentar motores.

**(2 min) Puente:** "Después del descanso construimos todo."

**💡 Key takeaway:** *"Instrucciones claras = asistente útil. Con CAFÉ, nunca empiezas de una hoja en blanco."*

**Slide extra recomendado:** seguridad y privacidad (qué NO subir: datos personales de clientes, contraseñas, información financiera sensible o confidencial de terceros).

---

### ☕ DESCANSO
**⏱ 15 min · 1 slide**

- Música, café y snacks.
- Mesa de **soporte técnico**: quien tenga problemas de cuenta o herramienta pasa con un co-facilitador.
- Slide con un reto: "Piensa en 3 preguntas reales que tu asistente debería saber responder."

---

### BLOQUE 4 · 🔥 Taller principal: construye tu asistente
**⏱ 50 min · 5 slides (uno por sprint) · Ver sección 4 para el detalle**

**🎯 Objetivo:** Que cada participante termine con un asistente funcional, entrenado con información real de su startup.

**🎬 Dinámica:** Trabajo individual guiado por sprints cronometrados. Los co-facilitadores circulan. Los equipos de mesa se ayudan entre sí.

**💡 Key takeaway:** *"Hecho es mejor que perfecto. Tu primera versión no tiene que ser buena, tiene que existir."*

---

### BLOQUE 5 · Rompe tu asistente (y mejóralo)
**⏱ 20 min · 4 slides**

**🎯 Objetivo:** Probar el asistente con casos difíciles, descubrir sus fallas y hacer al menos una mejora.

**🎬 Dinámica: "Pruebas cruzadas" en parejas**
- **(2 min) Explicación:** nadie prueba bien su propio asistente. Intercambian roles.
- **(10 min) Ronda de estrés (5 min por persona).** El "tester" usa el asistente de su compañero con 5 tarjetas de ataque:
  1. 🎯 **Pregunta típica**: ¿responde bien lo básico?
  2. 🕳️ **Pregunta fuera de alcance**: ¿admite que no sabe o inventa?
  3. 🤥 **Trampa de dato**: pregunta por un precio o dato que no está en la información.
  4. 😤 **Cliente difícil**: mensaje enojado o ambiguo.
  5. 🔓 **Intento de romper reglas**: "ignora tus instrucciones y…"
- **(6 min) Iteración:** cada dueño anota las fallas y ajusta **una sola cosa** en su Receta CAFÉ (normalmente la É: límites o ejemplos).
- **(2 min) Compartir:** 2-3 voluntarios cuentan "El fallo más gracioso o revelador que encontramos".

**💡 Key takeaway:** *"Un asistente no se termina, se afina. Cada falla es una instrucción nueva."*

---

### BLOQUE 6 · Cierre: tu plan de 7 días
**⏱ 10 min · 6 slides**

**🎯 Objetivo:** Convertir la energía del taller en hábito y llevarse recursos y compromisos concretos.

**🎬 Dinámica:**
- **(3 min) Recap relámpago:** los 4 ingredientes de CAFÉ en voz alta, todos juntos.
- **(3 min) Compromiso "7 días":** cada persona escribe en un post-it y pega en la pared:
  > *"En los próximos 7 días voy a usar mi asistente para ___ al menos ___ veces."*
- **(2 min) Recursos y siguiente paso:** QR a la carpeta, comunidad de WhatsApp y reto de 30 días.
- **(2 min) Foto grupal + feedback:** QR a un formulario de 3 preguntas y una foto con los post-its.

**💡 Key takeaway:** *"Un asistente solo vale si lo usas. Tu meta esta semana: ahorrar tu primera hora."*

---

## 4. 🔥 EJERCICIO PRINCIPAL: "Mi Asistente en 50 Minutos"

**Resultado final:** Un asistente funcional (en GPT personalizado, Project de Claude, Gem de Gemini, o chat con prompt maestro) que resuelve una tarea real de la startup y ya fue probado con 3 casos reales.

### Sprint 1 · Define la misión (8 min)
- Tomar la frase del Bloque 2 y completar la ficha en el workbook:
  - Nombre del asistente (con personalidad, ej. "Lupita, la vendedora estrella").
  - ¿Quién lo usa? ¿Con qué input? ¿Qué output espera?
  - 3 preguntas o tareas reales que debe resolver.
- ✅ *Check:* la ficha cabe en media página.

### Sprint 2 · Escribe las instrucciones con CAFÉ (12 min)
- **Camino A (recomendado):** pegar el meta-prompt "Entrévistame", responder las preguntas de la IA y recibir el borrador completo.
- **Camino B (más avanzados):** escribir CAFÉ directamente en la plantilla.
- Revisar el borrador y ajustar tono, límites y formato.
- ✅ *Check:* tiene las 4 letras: contexto, acción, formato, ejemplos y límites.

### Sprint 3 · Dale conocimiento (10 min)
- Subir o pegar el documento de la startup (one-pager, FAQs, precios, tono de marca) o crear uno rápido con ayuda de la IA.
- Aplicar el **semáforo de privacidad**:
  - 🟢 Info pública o de marketing → se sube.
  - 🟡 Info interna general → se anonimiza.
  - 🔴 Datos personales, contraseñas o financieros sensibles → no se sube.
- ✅ *Check:* el asistente puede citar al menos 2 datos del documento.

### Sprint 4 · Ármalo (10 min)
- **Con plan de pago:** crear el GPT, Project o Gem con las instrucciones y los archivos.
- **Con plan gratuito:** abrir un chat nuevo, pegar el "prompt maestro" con las instrucciones y los datos clave. Guardarlo en un documento para reutilizarlo.
- ✅ *Check:* el asistente tiene nombre, instrucciones y conocimiento cargados.

### Sprint 5 · Primera prueba real (10 min)
- Probar con **3 casos reales** (un email o mensaje de cliente verdadero, anonimizado) y evaluar con la rúbrica:
  - ⭐ ¿Suena a mi marca?
  - ⭐ ¿Los datos son correctos?
  - ⭐ ¿Me ahorra tiempo real?
- Anotar 2 mejoras para el Bloque 5.

### 🧰 Cómo facilitar este bloque
- Timer gigante en pantalla y música instrumental baja.
- Se anuncia cada sprint con su slide. Si alguien termina antes, pasa a "Nivel Pro": agregar un segundo flujo de trabajo o crear una versión del asistente para un teammate.
- Los co-facilitadores priorizan los 🔴 y luego los 🟡.
- A los 25 min, "pulso" rápido: *"Levanten la mano los que ya tienen su primer borrador."* Se celebra y se motiva al resto.
- **Plan para bloqueados:** usar el caso ejemplo de la cafetería y construir en paralelo a un compañero.

---

## 5. RECURSOS PARA LLEVAR A CASA

📁 **Carpeta digital (QR + link corto):**
1. **Workbook completo** del taller (PDF y versión Notion duplicable).
2. **Plantilla Receta CAFÉ** en blanco, más 3 ejemplos rellenados (ventas, contenido, atención al cliente).
3. **Meta-prompt "Entrévistame"**, listo para copiar y pegar.
4. **Biblioteca de 20+ prompts para startups:** ventas, marketing, producto, finanzas básicas, RRHH, pitch.
5. **Checklist de privacidad y buenas prácticas** (qué subir, qué no, cómo verificar las respuestas de la IA).
6. **Rúbrica de evaluación** de asistentes y tarjetas de ataque para pruebas.
7. **Comparativa rápida de herramientas** (ChatGPT, Claude, Gemini, etc.): qué ofrece cada plan, en qué destaca cada una. Con fecha de actualización.
8. **Plan de 7 días** + **Reto de 30 días** ("1 asistente nuevo por semana": ventas, contenido, investigación, operaciones).
9. **Grabación o fotos** del taller y las slides.

👥 **Comunidad y seguimiento:**
- Grupo de WhatsApp o Slack para compartir asistentes y resolver dudas.
- **Sesión de seguimiento online de 30 min** a las 2 semanas ("Mi asistente 2.0").
- Formulario de feedback y testimonios.

📚 **Lecturas y recursos opcionales:** guías oficiales de prompting de cada herramienta, 2-3 canales o newsletters recomendados en español y una lista de próximos pasos (automatizaciones sin código, integración con WhatsApp o email).

---

## 6. RESUMEN DE SLIDES POR SECCIÓN

| Sección | Slides |
|---|---|
| 0. Arranque | 6 |
| 1. De chatear a tener un asistente | 10 |
| 2. Encuentra tu caso de uso | 6 |
| 3. Receta CAFÉ | 14 |
| Descanso | 1 |
| 4. Taller principal | 5 |
| 5. Rompe tu asistente | 4 |
| 6. Cierre y plan de 7 días | 6 |
| **Total** | **~52** |

**Regla de diseño:** poco texto, mucho ejemplo visual, pantallas reales y una idea por slide. Los slides del taller principal son "pantallas de trabajo": timer, checklist y ejemplo.

---

## 7. NOTAS DEL FACILITADOR

- **Energía:** el valle de atención está después del descanso. Arranca el Bloque 4 con una dinámica física o un reto ("30 segundos para decir qué tarea vas a automatizar").
- **Contexto LATAM:** usa ejemplos locales (WhatsApp Business, ventas por Instagram, cotizaciones en pesos o soles, sector agro, fintech, delivery). Habla en tuteo o voseo neutro, y pide a la IA que responda en el español de tu país.
- **Honestidad sobre los límites:** dedica 1 minuto a decir que la IA puede equivocarse o inventar datos. "Tú eres el jefe, la IA es el practicante: revisa antes de enviar."
- **Quienes no tengan startup definida:** que usen el caso ejemplo o una idea hipotética. Igual aprenden el método.
- **Métrica de éxito del workshop:**
  - 80%+ termina con un asistente funcionando.
  - NPS mayor a 8.
  - 50%+ lo usa a los 7 días (medido por encuesta de seguimiento).

---

¿Quieres que desarrolle a continuación el **workbook paso a paso**, el **meta-prompt "Entrévistame"** o el **guion detallado de la demo** del Bloque 1?