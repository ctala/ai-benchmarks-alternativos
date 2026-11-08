# Fugu Max — startup_content/workshop_outline

- model_id: `sakana/fugu-max`
- success: True  | final: 8.23 | quality: 10.0
- latency_total: 45.484s | tokens_per_second: 216.9
- input_tokens: 316 | output_tokens: 9867
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un plan detallado y práctico que los emprendedores no técnicos pueden seguir directamente.

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
### Outline completo de facilitación · 3 horas · Presencial · 20–30 emprendedores early-stage no técnicos

---

## 🎯 Promesa del workshop (el "por qué estás aquí")

> **Sales con un asistente de IA funcionando, probado y con un plan de 7 días para ponerlo frente a clientes reales. No sales con apuntes. Sales con un producto.**

**Regla de oro de la facilitación:** máximo 25% del tiempo hablando el facilitador. El resto: manos en el teclado, parejas, demos y decisiones.

---

## 1. AGENDA DETALLADA (180 min)

| Hora | Min | Bloque | Formato |
|---|---|---|---|
| 0:00–0:10 | 10 | **Apertura: "Ya usas IA y no te has dado cuenta"** | Charla + encendido |
| 0:10–0:35 | 25 | **Bloque 1: La anatomía de un asistente que SÍ sirve** | Charla + demo + micro-ejercicio |
| 0:35–0:50 | 15 | **Bloque 2: Elige el caso de uso que paga la renta** | Ejercicio en parejas |
| 0:50–1:00 | 10 | **Bloque 3: Demo en vivo — de cero a asistente en 10 min** | Demo construida en público |
| 1:00–1:10 | 10 | **☕ BREAK + Mesa de Rescate** (cuentas, wifi, laptops) | Pausa activa |
| 1:10–2:00 | 50 | **Bloque 4: ¡A CONSTRUIR! — Ejercicio principal** | Build individual/grupal |
| 2:00–2:15 | 15 | **Bloque 5: La Hora de la Verdad — testing cruzado** | Speed-testing en tríos |
| 2:15–2:35 | 20 | **Bloque 6: De prototipo a producto (sin romper nada)** | Charla + demo de despliegue |
| 2:35–2:50 | 15 | **Bloque 7: Tu plan de 7 días + compromiso público** | Ejercicio + pacto |
| 2:50–3:00 | 10 | **Cierre: Recursos, foto y grupo** | Cierre energético |

> **Nota de ritmo:** entre bloques, 60 segundos de música + "párate y dile a alguien qué caso de uso elegiste". La energía del salón se cae a los 75 min si no la mueves tú.

---

## 2. MATERIALES A PREPARAR ANTES

### 2.1 Pre-work obligatorio (email 72h y 24h antes)

**Asunto: "Trae tu laptop y 3 documentos — o te toca hacerlo con los míos"**

- ✅ Laptop cargada + cargador (el celular NO sirve para construir, sí para probar)
- ✅ Cuenta creada y **logueada** en una de estas: Gemini (gratis), ChatGPT (gratis o Plus), Copilot, Claude
- ✅ **3 documentos de tu negocio** en un solo folder: (1) FAQ de clientes, (2) precios/productos, (3) tono de marca o "cómo hablamos"
- ✅ Si no tienes documentos: te damos el **Paquete Express** en el salón (no hay excusa)
- ✅ 1 caso de uso en mente: "¿qué pregunta me hacen 20 veces por semana?"

### 2.2 Material impreso (por persona)

| Material | Cant. | Formato |
|---|---|---|
| Workbook del participante | 30 (+5 repuesto) | A4, 8 páginas, grapado |
| Tarjeta laminada **"La Receta del Asistente"** | 32 | Credencial, entra en la billetera |
| Matriz de 12 casos de uso (1 hoja) | 30 | Media carta |
| Rúbrica de testing (10 preguntas trampa) | 30 | Media carta |
| Plantilla Plan de 7 días | 30 | Hoja suelta |
| Post-its (2 colores) + marcador grueso | 30 sets | En una bolsa por mesa |

### 2.3 Kit técnico del salón

- 📶 **Wifi con contraseña impresa en grande en 3 paredes** (el 40% de los problemas técnicos son esto)
- 🔌 Regletas en cada mesa (4–5 personas/mesa, formato cabaret, NO auditorio)
- 🖥️ Proyector + **cable HDMI de respaldo** + adaptador USB-C
- 📱 **3 tablets de la "Mesa de Rescate"** con cuentas demo ya logueadas (para quien no trajo laptop o se le cayó el wifi)
- 🎵 Parlante + playlist (entradas, breaks, transiciones)
- ⏱️ **Timer gigante visible** (proyector o tablet) — en este workshop el reloj ES un facilitador
- 📲 QR code gigante → carpeta compartida con todo el material
- 💾 **Kit offline:** USB con la demo grabada en video + los PDFs. Si se cae el internet, el workshop NO se cae.

### 2.4 Equipo humano (ratio 1:10)

| Rol | Quién | Hace qué |
|---|---|---|
| **Facilitador/a** | 1 | Lleva el ritmo, habla, hace la demo |
| **Co-facilitador técnico** | 1 | Resuelve cuentas/logins, "swat team" |
| **Roamers** | 2 | Circulan por mesas durante el build, desatascan prompts |

### 2.5 Contenido listo en la carpeta compartida

- **Paquete Express de Conocimiento**: 3 documentos ficticios de una startup ejemplo ("Café Andino", suscripción de café) — FAQ, precios, tono de marca. Imprimibles y digitales.
- **20 casos de uso de IA para startups LatAm** (1 PDF)
- **Comparativa de herramientas** con precios reales en USD
- **Grabación de la demo** (link, se manda al cierre)
- **Checklist de gobernanza**: qué datos NO meter nunca en un asistente

---

## 3. BLOQUES EN DETALLE

---

### 🚀 BLOQUE 0 — Apertura: "Ya usas IA y no te has dado cuenta"
**⏱ 10 min · Slides: 4**

- **Objetivo:** Bajar la ansiedad técnica, subir la energía y encuadrar la promesa del día.
- **Dinámica:**
  - (2 min) Facilitador abre con un dato brutal y local: *"El 80% de ustedes ya contestó a un cliente hoy con ChatGPT y no lo llamó 'IA'. Hoy lo vamos a volver un empleado."*
  - (4 min) **Encendido de mano alzada:** "¿Quién usa ChatGPT?" → "¿Quién le paga a alguien por responder WhatsApps?" → "¿Quién tiene un proceso que odia hacer?" (con cada mano, el facilitador hace un chiste del dolor).
  - (4 min) Encuadre: la promesa, la agenda en 3 palabras (**Elegir → Construir → Poner a prueba**) y las 3 reglas de la casa: *"se pregunta todo", "se vale copiar", "nadie se va sin su asistente funcionando"*.
- **Key takeaway:** *"La IA no te va a reemplazar. Te va a reemplazar alguien que sí la usa — y hoy ese alguien eres tú."*

---

### 🧠 BLOQUE 1 — La anatomía de un asistente que SÍ sirve
**⏱ 25 min · Slides: 10**

- **Objetivo:** Que entiendan que un asistente NO es "un ChatGPT mejor" — es **rol + contexto + reglas + conocimiento + formato**. Y que el prompt ES el producto.
- **Dinámica (charla + demo + micro-ejercicio):**
  - (8 min) **Charla con demo comparativa en vivo, en pantalla dividida:**
    - Prompt malo: *"Ayúdame a responder clientes"* → respuesta genérica, inútil.
    - Prompt bueno: rol + contexto + reglas + formato → respuesta que parece escrita por alguien del equipo.
    - El facilitador **lee ambas respuestas en voz alta** con drama. El salón ríe. Ahí se aprende.
  - (6 min) **Los 5 ingredientes** (la Receta) con un ejemplo de startup real de la región. Se proyecta la tarjeta laminada y todos la tienen en la mano.
  - (8 min) **Micro-ejercicio "La cirugía del prompt"** (en parejas, 4 min de trabajo + 4 de discusión): se les da un prompt malo impreso y lo reescriben con los 5 ingredientes. 2 parejas leen el suyo. El facilitador mejora uno en vivo, en pantalla.
  - (3 min) **Los 3 errores que matan asistentes:** (1) meterle la empresa entera, (2) no decirle qué NO hacer, (3) nunca probarlo con preguntas difíciles.
- **Key takeaway:** *"Un asistente bueno no es el que sabe más. Es el que sabe qué hacer con lo que sabe."*

---

### 🎯 BLOQUE 2 — Elige el caso de uso que paga la renta
**⏱ 15 min · Slides: 5**

- **Objetivo:** Que cada persona salga con UN caso de uso concreto, acotado a 60 minutos de construcción — no "quiero una IA para todo".
- **Dinámica (ejercicio en parejas):**
  - (2 min) Se presenta la **Matriz de 12 casos de uso** para startups early-stage, agrupados: *Atención al cliente · Ventas · Contenido · Operaciones · Onboarding · Research competitivo*.
  - (6 min) Cada persona marca **3 casillas** en su hoja y se queda con **1**, filtrando con 4 preguntas:
    1. ¿Pasa **muchas veces** por semana?
    2. ¿Es **repetitivo** y con reglas claras?
    3. ¿Tengo **documentos** para alimentarlo?
    4. ¿Si sale mal, **me cuesta caro**? (si sí → es el caso correcto para practicar HOY)
  - (5 min) **"Pitch de 20 segundos"** en parejas: *"Mi asistente va a hacer ___ para ___ y hoy lo hago ___ veces por semana."* El facilitador escucha 2–3 en el micrófono.
  - (2 min) **Filtro anti-trampa:** el facilitador descarta en voz alta los casos que no se pueden construir en 50 min (agentes que hacen compras, asistentes de voz, "que revise mi correo solo").
- **Key takeaway:** *"Si no puedes describir tu caso de uso en una frase, no es un caso de uso, es una fantasía."*

---

### 🎬 BLOQUE 3 — Demo en vivo: de cero a asistente en 10 minutos
**⏱ 10 min · Slides: 3 (la demo ES el contenido)**

- **Objetivo:** Desmitificar. Que vean **con sus ojos** que el ejercicio principal es alcanzable, y que memoricen el clic-a-clic.
- **Dinámica (demo construida en público, sin red de seguridad):**
  - El facilitador construye un asistente **real de una startup real** de la sala (ideal: alguien del público ofreció su caso en el Bloque 2). Pantalla grande, todo visible.
  - Cronómetro en pantalla. 6 pasos narrados: crear → pegar rol → pegar reglas → subir 2 documentos → probar 1 pregunta → ajustar 1 regla.
  - **Momento clave preparado:** el asistente **falla a propósito** (contesta algo fuera de alcance) y el facilitador lo corrige en vivo en 30 segundos. *"Ven cómo se arregla. Eso es todo lo que van a hacer ustedes."*
- **Key takeaway:** *"No hay magia. Hay seis pasos. Los acaban de ver."*

---

### ☕ BREAK + MESA DE RESCATE
**⏱ 10 min · Slides: 2 (timer + QR)**

- **Objetivo:** Que nadie llegue al Bloque 4 con un problema técnico.
- **Dinámica:** Música alta. Los 2 roamers + co-facilitador van mesa por mesa verificando: **¿laptop prendida? ¿sesión iniciada? ¿documentos en el escritorio?** Semáforo en la puerta: verde = listo, amarillo = ayúdenme, rojo = necesito tablet. Los rojos pasan a la Mesa de Rescate.
- **Key takeaway:** *"Aquí nadie construye solo."*

---

### 🛠️ BLOQUE 4 — ¡A CONSTRUIR! (Ejercicio principal)
**⏱ 50 min · Slides: 6 (instrucciones + timers por etapa)**

- **Objetivo:** Cada participante sale con **un asistente v1 funcionando**, con conocimiento propio cargado y probado con 5 preguntas.
- **Dinámica:** Ver **sección 4** (Ejercicio principal, detallado abajo).
- **Key takeaway:** *"Lo que acabas de construir vale más que el 90% de los cursos de IA que existen."*

---

### 🔍 BLOQUE 5 — La Hora de la Verdad: testing cruzado
**⏱ 15 min · Slides: 4**

- **Objetivo:** Que el asistente sea **puesto a prueba por alguien que no sabe nada del negocio**. El creador es el peor tester de su propio asistente.
- **Dinámica (speed-testing en tríos, sin piedad):**
  - (2 min) Se explican las reglas: tríos rotativos, **cada quien testea el asistente del de al lado** con la **rúbrica de 10 preguntas**: 3 fáciles, 3 de negocio, 2 difíciles, 1 trampa ("¿me haces un descuento del 50%?"), 1 fuera de alcance.
  - (9 min) Rotación: **3 min por asistente**, con timer visible. Se anota ✅/❌ en la rúbrica, no se explica ni se defiende.
  - (4 min) **Debrief relámpago:** el facilitador pregunta "¿quién rompió el asistente del vecino?" y normaliza: *"Rompimos a propósito. Eso es QA, no fracaso."* Se anotan las 3 fallas más comunes en una pizarra para todo el salón.
- **Key takeaway:** *"Tu asistente no es bueno cuando a ti te convence. Es bueno cuando convence a un desconocido."*

---

### 🚢 BLOQUE 6 — De prototipo a producto (sin romper nada)
**⏱ 20 min · Slides: 8**

- **Objetivo:** Que sepan dónde vive el asistente, cuánto cuesta, qué NO hacer y cómo medir si sirve.
- **Dinámica (charla rápida + demo + decisión):**
  - (6 min) **Charla "Los 3 lugares donde vive un asistente"** con demo en vivo de cada uno: (1) chat interno para el equipo, (2) widget en la web, (3) WhatsApp / bot de atención. Mostrar un widget real instalado en una landing.
  - (5 min) **Plata: costos reales y gobernanza.** Tabla de precios en USD + los 3 datos que **jamás** se suben a un asistente (datos de tarjetas, datos de salud, datos personales de clientes sin consentimiento). Regla simple: *"si no lo pondrías en un correo externo, no lo pongas en el asistente."*
  - (6 min) **Las 3 métricas que importan** (y una hoja de cálculo simple): (1) % de preguntas resueltas sin humano, (2) tiempo ahorrado por semana, (3) satisfacción del cliente. Se proyecta la calculadora de ROI: *"si ahorras 5 h/semana a $8/h, son $160/mes. Eso es lo que tienes que superar en costo."*
  - (3 min) **El "no" más importante:** no lo pongas frente a un cliente real sin 20 pruebas y un humano de respaldo. Un bot que falla quema más confianza que un WhatsApp sin responder.
- **Key takeaway:** *"Un asistente es un producto, no un experimento. Se mide, se cuida y se apaga si no funciona."*

---

### 🗓️ BLOQUE 7 — Tu plan de 7 días + compromiso público
**⏱ 15 min · Slides: 4**

- **Objetivo:** Convertir el entusiasmo en calendario. Sin esto, el 90% no lo toca nunca más.
- **Dinámica (ejercicio individual + pacto):**
  - (2 min) Se presenta la **Plantilla de 7 días**: Día 1 cargar 5 documentos nuevos · Día 2 mejorar reglas con 10 preguntas reales · Día 3 mostrárselo a 1 compañero de equipo · Día 4–5 pruebas con 5 clientes reales · Día 6 definir métrica · Día 7 decidir: escalar, ajustar o archivar.
  - (6 min) Cada quien lo llena en papel y **escribe UN obstáculo** y **UN nombre** (su compañero de accountability).
  - (5 min) **Pacto público:** de a dos, se dicen en voz alta *"En 7 días te muestro mi asistente con ___".* Se intercambian contacto. Opcional: post-it en la pared de los compromisos + foto grupal de la pared.
  - (2 min) **Anti-sabotaje:** el facilitador nombra los 3 asesinos del plan ("se me acaba el trial", "mi equipo no me da los documentos", "espero a tenerlo perfecto") y una respuesta de 10 segundos para cada uno.
- **Key takeaway:** *"Un asistente sin fecha es un pasatiempo. Con fecha, es un producto."*

---

### 🎉 CIERRE
**⏱ 10 min · Slides: 4**

- **Objetivo:** Cerrar con recursos, comunidad y una foto que se comparta.
- **Dinámica:** (3 min) recorrido por los recursos de la carpeta y QR. (3 min) **"Una frase, una silla":** 3 personas al azar dicen su asistente en 1 frase. (2 min) Grupo de WhatsApp/Telegram + fecha de check-in a 7 días. (2 min) Foto grupal con los asistentes abiertos en pantalla.
- **Key takeaway:** *"Ya no eres alguien que 'escuchó sobre IA'. Eres alguien que construyó una."*

---

## 4. 🏗️ EJERCICIO PRINCIPAL DEL WORKSHOP

# "Un asistente, 50 minutos, cero código"

> **Todos pueden hacerlo porque no hay una sola línea de código, y hay 3 niveles de entrada.** El que no trajo nada usa el Paquete Express. El que no tiene laptop usa una tablet de la Mesa de Rescate. El que ya sabe, escala a Nivel 2.

### 4.1 La Receta del Asistente (los 5 ingredientes)

| # | Ingrediente | Qué escribir | Ejemplo (startup de café por suscripción) |
|---|---|---|---|
| 1 | **ROL** | Quién es y para quién | "Eres el asistente de atención de Café Andino, una suscripción de café de especialidad en Bogotá. Hablas con clientes de 25–45 años." |
| 2 | **CONTEXTO** | 3 datos del negocio que cambian la respuesta | "Enviamos el día 5 de cada mes. Tenemos 3 planes. Zona de entrega: Bogotá y Medellín." |
| 3 | **REGLAS** | Qué sí, qué NO, tono y límites | "Tono cercano, tuteo, máximo 4 líneas. Nunca prometas descuentos. Si no sabes algo, di: 'te conecto con una persona del equipo'." |
| 4 | **CONOCIMIENTO** | Los documentos que subes | FAQ de clientes · lista de precios · política de envíos |
| 5 | **FORMATO** | Cómo responde | "Responde siempre en 2 partes: respuesta directa + siguiente paso concreto." |

**Regla de facilitación:** el ingrediente 3 (REGLAS) es el que más se salta y el que más importa. Repetirlo hasta el cansancio.

### 4.2 Estructura de los 50 minutos (cronometrada en pantalla)

| Min | Etapa | Qué pasa | Rol del facilitador |
|---|---|---|---|
| 0–5 | **Setup** | Abren la herramienta, eligen su caso de uso del Bloque 2, sacan la tarjeta de la Receta | Verifica que todos tengan sesión iniciada |
| 5–15 | **Rol + Reglas** | Escriben ingredientes 1, 2 y 3. Sin tocar documentos todavía. | Roamers circulan: "¿qué le dijiste que NO haga?" |
| 15–30 | **Conocimiento** | Suben 2–3 documentos (o llenan el Paquete Express). Ajustan el formato. | Ayudan a exportar/limpiar documentos |
| 30–42 | **Prueba 5 preguntas** | 3 fáciles, 1 difícil, 1 trampa. Anotan qué falló. | "No arregles el prompt todavía. Primero rompe." |
| 42–50 | **Pulir + pitch de 60 seg** | Ajustan 1–2 reglas y preparan su demo de 60 segundos para el Bloque 5 | Anuncia el pitch: "en 60 seg: qué hace, para quién, qué falló" |

### 4.3 Tres niveles de entrada (para que nadie se quede atrás)

| Nivel | Quién | Herramienta | Qué logra |
|---|---|---|---|
| **Nivel 0** | Sin cuenta paga, sin ganas de registrarse | Instrucciones personalizadas / "Gem" / "Project" en ChatGPT, Gemini o Claude gratis | Asistente con rol + reglas + conocimiento, en su cuenta de siempre |
| **Nivel 1** ⭐ | La mayoría | **Gem de Gemini (gratis)** o **Custom GPT (ChatGPT Plus)** | Asistente guardado, reusable, con archivos cargados |
| **Nivel 2** | Quien ya lo hizo o va rápido | Chatbase / Voiceflow / Dante (trial gratis) | Widget embebible en su web, con link público para compartir |

**Recomendación operativa:** arrancar TODOS en Nivel 0/1 (5 min de setup garantizado). El Nivel 2 se muestra en el Bloque 6 como demo, y quien quiera escalar lo hace ahí con apoyo.

### 4.4 Kit anti-fracaso (lo que salva el workshop)

- 📁 **Paquete Express**: 3 documentos ya listos de una startup ficticia para quien no trajo nada. Imposible excusarse.
- 🖨️ **Tarjeta laminada de la Receta**: todos la tienen en la mano. Nadie tiene que recordar nada de la pantalla.
- 👥 **Regla del trío**: nadie construye solo. Si alguien se traba 3 minutos, el vecino entra.
- 📶 **Plan sin internet**: si se cae el wifi, se pasa a "construye tu prompt a mano en el workbook" y el testing se hace leyendo en voz alta. El aprendizaje sobrevive.
- 🎯 **Caso de uso "enlatado"**: para quien se paraliza eligiendo, hay 3 casos pre-aprobados en el workbook ("responde FAQs de precios", "califica leads", "responde objeciones de venta").

---

## 5. RECURSOS PARA LLEVAR A CASA

Entregados por QR **y** en físico (los dos, siempre):

1. **La Receta del Asistente** — plantilla editable de 5 campos + 3 ejemplos completos reales.
2. **Workbook impreso** (8 pág.) — todo lo del día, con espacio para escribir, no solo leer.
3. **Biblioteca de 20 prompts para startups LatAm** — atención, ventas, contenido, research, onboarding.
4. **Rúbrica de testing de 10 preguntas** — para reusar con cada versión nueva.
5. **Paquete Express de Conocimiento** — los 3 documentos plantilla para llenar.
6. **Comparativa de herramientas con precios reales** — qué es gratis, qué cuesta y cuándo vale la pena pagar.
7. **Checklist de gobernanza de IA** — qué datos nunca meter, qué decirle a tu equipo, qué poner en tu política de privacidad.
8. **Calculadora de ROI** (hoja de cálculo simple) — horas ahorradas × costo/hora vs. costo de la herramienta.
9. **Plan de 7 días** — impreso y llenado a mano por cada participante.
10. **Grabación de la demo en vivo** + link al grupo de la comunidad y fecha del check-in a 7 días.

---

## 6. CONTEO DE SLIDES ESTIMADO

| Sección | Slides | Tipo |
|---|---|---|
| Apertura | 4 | Título, promesa, agenda, reglas de la casa |
| Bloque 1 — Anatomía | 10 | Comparativa prompt malo/bueno, 5 ingredientes, 3 errores |
| Bloque 2 — Caso de uso | 5 | Matriz de 12 casos, 4 filtros, ejemplos |
| Bloque 3 — Demo en vivo | 3 | Solo el checklist de 6 pasos (la demo es en vivo) |
| Break | 2 | Timer + QR de la carpeta |
| Bloque 4 — Build | 6 | Instrucciones, timer por etapa, Receta grande en pantalla |
| Bloque 5 — Testing | 4 | Reglas del speed-testing, rúbrica, pizarra de fallas |
| Bloque 6 — Prototipo a producto | 8 | 3 lugares, costos, gobernanza, 3 métricas, ROI |
| Bloque 7 — Plan 7 días | 4 | Plantilla, anti-sabotaje, pacto |
| Cierre | 4 | Recursos, QR, check-in, foto |
| **TOTAL NÚCLEO** | **~50** | |
| Anexo / respaldo | 10 | Glosario, herramientas por caso de uso, contactos, plan B si falla el wifi |
| **TOTAL** | **~60** | |

> **Nota de diseño de slides:** máximo 15 palabras por slide, una idea por slide, cero capturas de pantalla ilegibles. Todo lo denso va en el **workbook impreso**, no en la pantalla.

---

## 7. RUN-OF-SHOW DEL EQUIPO (imprescindible)

| Momento | Facilitador | Co-facilitador técnico | Roamers |
|---|---|---|---|
| −60 min | Prueba proyector, timer, música | Verifica tablets y cuentas demo | Arma mesas, regletas, materiales |
| 0:00–0:50 | Lleva la charla y la demo | Monitorea logins entre bastidores | Ayudan en el micro-ejercicio |
| Break | Anima la pausa | **Mesa de Rescate** (semáforo) | Chequeo mesa por mesa |
| 1:10–2:00 | Da tiempos y circula | Resuelve cuentas rotas | **Desatascan prompts** (1:3 personas) |
| 2:00–2:35 | Lleva el testing y la charla | Cronometra rotaciones | Recolectan rúbricas, arman la pizarra de fallas |
| 2:35–3:00 | Cierre y pacto | Toma fotos, manda el link | Reparten recursos, recogen post-its |

---

## 8. PLAN B / CONTINGENCIAS

| Si pasa esto | Hacemos esto |
|---|---|
| Se cae el internet | Modo "prompt en papel": escriben la Receta a mano en el workbook, testing leyendo en voz alta. Se manda la demo grabada. **El workshop no se detiene.** |
| Una herramienta está bloqueada o caída | Cambio inmediato al Nivel 0 (ChatGPT/Gemini/Copilot). Siempre hay un plan B de herramienta por cada nivel. |
| 40% no hizo el pre-work | Se activa el Paquete Express en el minuto 0 del Bloque 4. Nadie pide permiso, se reparte. |
| El grupo es muy callado | Los roamers siembran la participación: "pregúntale a esta persona su caso de uso" y luego el facilitador la nombra. |
| El grupo es muy avanzado | Se salta el Nivel 1 y van directo a Nivel 2 (widget embebible). Se les pide que ayuden a los demás: rol de "co-facilitador honorario". |
| Alguien monopoliza | "Regla de los 30 segundos" + pase al trío. El facilitador retoma con "gracias, eso lo retomamos en el break". |

---

## 9. LO QUE HACE QUE ESTE WORKSHOP SE RECUERDE

- ✅ **Se construye antes del minuto 60.** Nada de 90 minutos de teoría.
- ✅ **La demo falla a propósito.** Se desmonta la idea de que la IA "sale perfecta".
- ✅ **El testing es de un desconocido, no del creador.** Es la parte que la gente comenta al salir.
- ✅ **Todos se van con un plan con fecha y un compañero que les va a preguntar.**
- ✅ **La energía se gestiona con música, timers gigantes y movimiento cada 25 minutos.**

> **Frase de cierre del facilitador (memorizar):** *"No se vayan a casa a 'pensarlo'. Váyanse a casa a probarlo. La IA no premia a los que entienden mejor, premia a los que iteran más rápido."*