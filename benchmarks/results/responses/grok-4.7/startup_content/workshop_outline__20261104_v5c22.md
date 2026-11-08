# Grok 4.7 — startup_content/workshop_outline

- model_id: `x-ai/grok-4.7`
- success: True  | final: 8.07 | quality: 10.0
- latency_total: 96.646s | tokens_per_second: 45.5
- input_tokens: 1423 | output_tokens: 4399
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando una agenda detallada, materiales necesarios y una estructura de bloques bien pensada, lo que la hace altamente útil para emprendedores no técnicos.

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

**Workshop presencial · 3 horas**  
**“Construye tu Asistente de IA para tu Startup”**  
Audiencia: 20–30 emprendedores early-stage, no técnicos · LatAm  
Tono: manos a la obra. Salen con un asistente usable, no con teoría.

---

## 1. Agenda (180 min)

| Hora | Bloque | Min |
|---|---|---|
| 0:00 | Apertura y contrato del día | 15 |
| 0:15 | Por qué un asistente y no “usar ChatGPT a lo loco” | 20 |
| 0:35 | Demo en vivo: el mismo pedido, mal vs. bien | 15 |
| 0:50 | El lienzo del asistente (4 piezas) | 25 |
| 1:15 | **Pausa** | 10 |
| 1:25 | Ejercicio principal: construye y prueba el tuyo | 70 |
| 2:35 | Showcase rápido + ajustes en caliente | 20 |
| 2:55 | Plan de 7 días y cierre | 15 |

Buffer real: los 70 min del ejercicio absorben retrasos. Si el grupo llega tarde, recorta apertura a 10 y showcase a 15. No recortes la prueba del asistente.

---

## 2. Materiales (preparar antes)

**Sala**
- Proyector + HDMI/USB-C de respaldo + clicker
- WiFi estable; hotspot de respaldo (cuenta con 30 personas en la misma red)
- Mesas en islas de 4–5, no teatro
- Pizarra o flipchart + marcadores
- Timer visible (proyección o celular en grande)

**Para cada persona (impreso, 1 hoja doble cara)**
- Lienzo del asistente (rol, contexto, tareas, límites)
- Checklist de prueba (3 escenarios)
- Plan de 7 días (media hoja)

**Digital**
- Cuenta del facilitador en ChatGPT y/o Claude (la que uses en la demo), ya logueada
- Plantilla de prompt en un doc compartido (link corto / QR). Versión “copiar y pegar”, no PDF
- 1 ejemplo completo de una startup ficticia latam (ej. marca de snacks saludables que vende por WhatsApp e Instagram) para quien llegue sin idea clara de su negocio
- Lista de herramientas gratuitas que funcionan desde el celular: ChatGPT, Claude, Gemini. Aclara qué se puede hacer sin plan de pago

**Facilitador**
- Laptop cargada + cargador
- Asistente demo ya armado (y una versión “mala” para contrastar)
- 6 tarjetas de roles de mesa: tiempo, calidad, “¿y si no tiene laptop?”, energía
- Hojas extra y 2–3 laptops/tablets de préstamo si puedes
- Lista de asistencia con correo o WhatsApp para mandar recursos el mismo día

**Antes del día**
- Mail/WhatsApp 48 h antes: “trae 1 dolor repetitivo de tu startup (ventas, soporte, contenido, operaciones) y el celular con una cuenta de IA ya creada”. Link de registro a ChatGPT o Claude.
- Chequear que el ejemplo ficticio no use datos reales de clientes.

---

## 3. Bloques

### Bloque 1 — Apertura y contrato del día
**15 min · Dinámica: charla corta + ronda de pie**

**Objetivo:** que sepan que hoy no van a “aprender IA”, van a salir con un asistente que hace un trabajo concreto de su startup.

**Cómo corre**
- 3 min: quién eres, promesa del día en una frase: *“En 3 horas tu asistente contesta como tu negocio, no como un chatbot genérico.”*
- 5 min: de pie, en parejas de 60 segundos: “¿Qué tarea repites cada semana y odias?” Una palabra en la pizarra (ventas, soporte, contenido, propuestas, research).
- 5 min: reglas: celulares sí (son la herramienta), una sola tarea por persona, no perfección, pregunta en voz alta si te atoras. Aviso de privacidad: no peguen datos reales de clientes, contraseñas ni números de tarjetas.

**Key takeaway:** un buen asistente resuelve *una* tarea repetible, no “todo el negocio”.

**Slides:** 4

---

### Bloque 2 — Por qué un asistente y no “usar ChatGPT a lo loco”
**20 min · Dinámica: charla + 2 ejemplos de la sala**

**Objetivo:** separar chat suelto de asistente con memoria de contexto, tono y límites.

**Cómo corre**
- Chat suelto = empleado nuevo cada mañana, sin briefing.
- Asistente = briefing fijo: quién es, qué sabe de tu startup, qué hace, qué no hace.
- 3 usos que sí valen en early-stage (con ejemplo latam de 20 segundos cada uno):
  1. Responder DMs / WhatsApp de ventas con el tono de la marca
  2. Convertir una idea suelta en post, mail o propuesta
  3. Ordenar notas de una llamada en próximos pasos
- 3 usos que no: decidir precio solo, inventar datos de mercado, reemplazar hablar con el cliente.
- Pide 2 dolores de la pizarra y di en voz alta si encajan o no. Corta la discusión si se va a “¿la IA va a quitarme el trabajo?”. Una frase y sigues: *“Hoy armamos una herramienta, no un manifiesto.”*

**Key takeaway:** el valor no está en el modelo, está en el briefing que tú escribes.

**Slides:** 6

---

### Bloque 3 — Demo en vivo: el mismo pedido, mal vs. bien
**15 min · Dinámica: demo**

**Objetivo:** que vean la diferencia en pantalla antes de escribir nada.

**Cómo corre**
- Caso fijo (el de snacks por WhatsApp, o uno tuyo de la región): *“Un cliente pregunta si hacen envíos a Medellín y si hay descuento por docena.”*
- Prompt malo: “contesta este mensaje”. Lees la respuesta genérica en voz alta. 30 segundos de risa está bien.
- Prompt bueno: pegas el briefing (marca, ciudades, precios, tono, qué nunca prometer). Misma pregunta. Señalas 3 diferencias: tono, dato concreto, límite (“no inventa descuento”).
- Cierras con la anatomía en 4 cajas, sin teoría de prompts.

**Key takeaway:** mismo modelo, otro briefing, otro negocio.

**Slides:** 5 (la demo es la pantalla, no el slide)

---

### Bloque 4 — El lienzo del asistente
**25 min · Dinámica: charla guiada + llenado individual de 8 min**

**Objetivo:** que cada quien deje escrito, en papel, las 4 piezas antes de abrir la herramienta.

**Las 4 piezas (dilo así, no con jerga)**
1. **Rol:** “Eres el asistente de ventas de [marca]. Hablas como…”
2. **Contexto:** qué vendes, a quién, precio aproximado, canal (IG, WhatsApp, web), ciudad/país, lo que nunca ofreces.
3. **Tareas:** máximo 3. Verbo + resultado. Ej. “Redacta la respuesta al DM y sugiere el siguiente paso.”
4. **Límites:** no inventes precios, no prometas fechas, no des consejos legales/médicos, pregunta si falta un dato, responde en español neutro o en el acento de la marca.

**Cómo corre**
- 10 min explicando con el ejemplo ficticio ya lleno (proyectado).
- 8 min en silencio: cada quien llena su hoja. Tú caminas. Quien esté en blanco usa la plantilla de la startup ficticia y la adapta a su rubro en 2 líneas.
- 5 min: voluntario lee solo el rol + 1 límite. Tú corriges en público un límite flojo (“sé amable” no es límite; “no ofrezcas más del 10% sin preguntarme” sí).

**Key takeaway:** si no cabe en una hoja, el asistente está demasiado ambiguo para servir.

**Slides:** 7

---

### Pausa — 10 min
Agua, baño, y que abran la cuenta de IA *ahora*, no cuando empiece el ejercicio. Tú ayudas a los 3–4 que no lograron entrar.

---

### Bloque 5 — Ejercicio principal
**70 min · Dinámica: ejercicio individual con apoyo de mesa**  
Detalle completo en la sección 4.

**Objetivo:** tener un asistente pegado en la herramienta, probado con 3 casos reales de su startup, y corregido al menos una vez.

**Key takeaway:** el asistente mejora cuando lo enfrentas a un mensaje real, no cuando le agregas más instrucciones “por si acaso”.

**Slides:** 4 (instrucciones + timer + ejemplo de prueba)

---

### Bloque 6 — Showcase y ajustes en caliente
**20 min · Dinámica: discusión corta, no presentaciones**

**Objetivo:** que el grupo vea 4 patrones que funcionan y 2 errores comunes, y corrija el suyo en 5 minutos.

**Cómo corre**
- 4 voluntarios, 90 segundos cada uno: leen el rol y *una* respuesta que les gustó. Tú proyectas solo si quieren. No dejes que cuenten la historia de la startup.
- Tú nombras el patrón: “este límite salvó la respuesta”, “aquí el contexto de precio evitó que inventara”.
- Error típico que vas a ver: asistente que habla como consultor gringo, o que promete envío. Corrección en voz alta, ellos la pegan.
- 5 min finales: cada quien ajusta *una* línea de su briefing.

**Key takeaway:** un límite bien escrito vale más que diez adjetivos de personalidad.

**Slides:** 3

---

### Bloque 7 — Plan de 7 días y cierre
**15 min · Dinámica: charla + compromiso escrito**

**Objetivo:** que el asistente no se muera en el cuaderno.

**Plan (lo dicen en voz alta mientras lo escriben)**
- Día 1: úsalo en 5 mensajes reales (pueden ser borradores, no hace falta enviarlos).
- Día 3: agrega 1 ejemplo de “respuesta buena” que tú hayas escrito.
- Día 7: borra la instrucción que no sirvió. Quédate con una tarea, no con cinco.

Cierre en 60 segundos por mesa: “mañana lo uso para ___”. Foto grupal opcional. QR de recursos. Aviso: esto no sustituye criterio de precios, legal ni atención a clientes enojados; tú sigues firmando.

**Key takeaway:** 5 usos reales esta semana > un prompt “perfecto” que nunca abres.

**Slides:** 4

**Total slides estimado: 33.** Meta: menos de 40. Si pasas de ahí, estás dando clase, no workshop.

---

## 4. Ejercicio principal (lo hacen todos)

**Nombre:** “Tu primer empleado de IA, en una hoja.”  
**Duración:** 70 min · **Individual**, con mesa como soporte. No es trabajo en equipo: cada startup es distinta. La mesa solo desatora.

**Herramienta:** la que ya tengan abierta (ChatGPT, Claude o Gemini). No hace falta plan de pago. Si alguien no tiene laptop, celular + el doc compartido alcanza. Quien no tenga cuenta usa el ejemplo ficticio en una laptop de préstamo, al lado de alguien, y se lleva el texto igual.

### Minuto a minuto

| Min | Qué hacen |
|---|---|
| 0–5 | Pegan en el chat el esqueleto del doc compartido y reemplazan los corchetes con su hoja. No empiezan a “conversar”. |
| 5–15 | Primera versión del briefing. Máximo una pantalla. Tú circulas y tachas adjetivos vacíos (“innovador”, “apasionado”). |
| 15–25 | **Prueba 1 — mensaje fácil.** Un cliente pregunta precio y cómo comprar. ¿Responde con su tono y su dato, o inventa? |
| 25–40 | **Prueba 2 — mensaje incómodo.** Queja, pedido de descuento grande, o “¿me das asesoría gratis?”. Deben ver si respeta el límite. Si no, reescriben *una* línea del límite y vuelven a probar. No reescriben todo. |
| 40–55 | **Prueba 3 — mensaje incompleto.** “¿Tienen de ese?” sin decir cuál. El asistente debe preguntar, no adivinar. |
| 55–65 | Guardan el briefing donde lo van a reencontrar: chat fijado, nota del celular, o doc propio. Copian 1 respuesta buena como ejemplo dentro del briefing (“cuando pregunten envío, responde así”). |
| 65–70 | En la hoja, una frase: “Mañana lo uso para [tarea].” Eso es el entregable. No hay presentación obligatoria. |

### Esqueleto que pegan (está en el doc compartido)

```
Eres el asistente de [rol] de [nombre de la startup].
Hablamos a [cliente ideal] por [canal].
Vendemos [qué], en [ciudad/país]. Precio de referencia: [rango o “preguntar antes de dar cifra”].
Tono: [2 rasgos concretos, ej. cercano, corto, sin tecnicismos].

Tus tareas, solo estas:
1. [verbo + resultado]
2. [verbo + resultado]
3. [opcional]

Reglas:
- Si falta un dato, pregunta. No inventes precios, plazos ni stock.
- Nunca prometas [X].
- Si la pregunta es legal, médica o de un reclamo grave, di que lo pasa a la persona del equipo.
- Responde en [idioma], en menos de [N] líneas, salvo que pidan más.
- Cierra con un siguiente paso claro.

Ejemplo de buena respuesta:
Cliente: “[mensaje]”
Tú: “[respuesta modelo]”
```

**Criterio de “listo” (dilo en voz alta a los 55 min):**  
Si un socio leyera solo ese texto y pudiera contestar un DM parecido al tuyo, está listo. Si todavía dice “ayuda con lo que sea”, no.

**Rol del facilitador durante los 70 min**
- Min 10, 30 y 50: anuncias en qué prueba van. La gente se pierde en pulir el tono.
- Intervención típica: “borra la mitad”. Early-stage no técnicos escriben de más.
- No depures prompts ajenos en público más de 40 segundos. Anota el patrón para el showcase.

---

## 5. Recursos para llevar a casa

Mándalo por WhatsApp/correo **el mismo día**, no “la próxima semana”.

1. **PDF de 2 páginas:** lienzo + esqueleto de prompt + checklist de las 3 pruebas.
2. **Doc vivo** (Google Doc o Notion): el esqueleto editable y el ejemplo completo de la startup ficticia.
3. **Guía de 1 página “dónde vive tu asistente”:**
   - ChatGPT: instrucciones personalizadas o un GPT, si tienen Plus; si no, chat fijado con el briefing al inicio.
   - Claude: Project con el briefing en las instrucciones.
   - Gemini: Gem, si está disponible en su cuenta; si no, el mismo pegado al inicio del chat.
   - Atajo realista en LatAm: nota fijada + pegar el briefing cuando atienden WhatsApp. No les vendas una integración que no van a mantener.
4. **Plan de 7 días** (la media hoja, también en digital).
5. **Lista de lo que no automatizar todavía:** precios finales, reclamos fuertes, promesas de entrega, cualquier dato de un cliente real dentro del prompt.
6. **3 prompts de mantenimiento**, no de “hacks”:
   - “Reescribe mi briefing para que quepa en 150 palabras, sin perder límites.”
   - “Estas 5 respuestas salieron mal. Dime qué línea del briefing falta.”
   - “Convierte esta respuesta mía (la que sí envié) en un ejemplo para el briefing.”

No incluyas un dump de 40 herramientas. Una herramienta bien usada gana.

---

## 6. Slide count por sección

| Sección | Slides | Qué va (no más) |
|---|---|---|
| Apertura | 4 | Título, promesa, agenda en 5 líneas, reglas + privacidad |
| Por qué un asistente | 6 | Chat vs. asistente, 3 usos sí, 3 usos no |
| Demo | 5 | Caso, prompt malo, prompt bueno, 3 diferencias, puente al lienzo |
| Lienzo | 7 | 1 slide por pieza + ejemplo lleno + “esto no es un límite” |
| Ejercicio | 4 | Pasos, esqueleto, timer de pruebas, criterio de listo |
| Showcase | 3 | Cómo se presenta (90 s), patrones, error típico |
| Cierre | 4 | Plan 7 días, QR, qué no automatizar, gracias |
| **Total** | **33** | |

Slides de respaldo (no se proyectan salvo pregunta): diferencias mínimas entre ChatGPT / Claude / Gemini, y “qué hago si la herramienta se cae” (siguen en papel y pegan después). No las cuentes en las 33.

---

**Promesa que puedes decir al abrir y repetir al cerrar:**  
No se van con un curso de IA. Se van con un briefing de una página, probado con tres mensajes de su propio negocio, y una fecha: mañana.