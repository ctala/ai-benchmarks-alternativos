# Fugu Max — startup_content/workshop_outline

- model_id: `sakana/fugu-max`
- success: True  | final: 7.9 | quality: 9.72
- latency_total: 118.445s | tokens_per_second: 33.4
- input_tokens: 892 | output_tokens: 3960
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

# Workshop: Construye tu Asistente de IA para tu Startup
**Presencial · 3 horas · 20–30 emprendedores early-stage no-técnicos**

Promesa del día: *sales con un asistente diseñado, testeado y listo para usar mañana en tu startup. Cero código. Cero jerga innecesaria.*

---

## 1. Agenda detallada (180 min)

| Bloque | Tiempo | Minutos |
|---|---|---|
| 0. Apertura + energía | 0:00–0:12 | 12 |
| 1. El porqué (ahora, no “algún día”) | 0:12–0:28 | 16 |
| 2. Demo en vivo | 0:28–0:42 | 14 |
| 3. Anatomía de un asistente (sin ingeniería) | 0:42–0:58 | 16 |
| 4. Casos reales por tipo de startup | 0:58–1:10 | 12 |
| **BREAK** | **1:10–1:20** | **10** |
| 5. Ejercicio principal: construye el tuyo | 1:20–2:30 | 70 |
| 6. Del prototipo al hábito | 2:30–2:45 | 15 |
| 7. Recursos + cierre | 2:45–3:00 | 15 |

**Buffer realista:** 5 min de holgura absorbidos en transiciones. No recortes el ejercicio.

---

## 2. Materiales (preparar ANTES)

**Logística**
- Sala con mesas en clusters de 4–5 (no teatro). Wifi que aguante 30 dispositivos.
- Proyector + HDMI de respaldo. Parlantes. Micrófono de solapa si la sala es grande.
- Pizarrón o 2 flipcharts.
- Cargadores / alargadores (la gente llega con 12% de batería).

**Para cada participante**
- Canvas impreso A3: **“El Cerebro de tu Asistente”** (1 por persona + 10 extras).
- Marcadores, post-its de 3 colores, stickers.
- Credencial con nombre + startup (ayuda en el show & tell).
- QR en la mesa: carpeta de recursos + grupo de WhatsApp del workshop.

**Tú (facilitador)**
- Cuenta lista de ChatGPT / Gemini / Claude (la que uses en demo). Prompt del asistente demo YA pegado.
- 2 casos de demo: uno B2B (ventas/soporte) y uno B2C (contenido/atención).
- Timer visible (Time Timer o pantalla).
- Playlist de entrada (energía, no lounge).
- Lista de asistencia + foto de grupo al final (los emprendedores la usan en LinkedIn).

**Digital**
- Slides en modo presentador (notas cortas, no párrafos).
- Link único a un Notion/Drive con templates.
- Backup offline de slides (por si el wifi se cae en el minuto 40, que va a pasar).

**Regla de oro LATAM:** asume mix laptop + celular. El ejercicio principal funciona en papel primero; el test digital es opcional pero empujado.

---

## 3. Bloques (título, objetivo, dinámica, takeaway)

### BLOQUE 0 — Apertura + energía
**Duración:** 12 min · **Slides:** 4

**Objetivo:** Bajar la ansiedad de “yo no soy técnico” y crear permiso para experimentar.

**Dinámica:** Charla corta (3 min) + icebreaker de pie (7 min) + reglas del juego (2 min).
- Icebreaker: “En 20 segundos, dile a tu vecino: *qué tarea de tu startup odiarías seguir haciendo a mano en 6 meses*.”
- Reglas: celulares en modo avión excepto para el ejercicio · no hay preguntas tontas · si se traba, se comparte.

**Key takeaway:** No viniste a aprender IA. Viniste a quitarte trabajo de encima.

---

### BLOQUE 1 — El porqué (ahora, no “algún día”)
**Duración:** 16 min · **Slides:** 6

**Objetivo:** Conectar IA con caja, tiempo y ventaja competitiva de un early-stage, no con hype.

**Dinámica:** Charla con 3 historias cortas (startup LATAM que automatizó soporte / research / ventas) + 1 dato duro + pregunta al plenario.
- Dato: un founder early-stage hace 40–60% de trabajo repetible que un asistente ya puede cubrir.
- Pregunta: “Si mañana desaparece tu WhatsApp de clientes por 48 horas, ¿qué se rompe?”

**Key takeaway:** El asistente no reemplaza al founder. Reemplaza las 14 pestañas abiertas a las 11 pm.

---

### BLOQUE 2 — Demo en vivo
**Duración:** 14 min · **Slides:** 3 (el resto es pantalla compartida)

**Objetivo:** Que vean un asistente *de startup* funcionando, no un ChatGPT genérico respondiendo recetas.

**Dinámica:** Demo en vivo (no video grabado).
1. Muestras el “antes”: prompt flojo → respuesta genérica e inútil.
2. Muestras el asistente construido: rol + contexto de la empresa + documentos + límites.
3. Tres pruebas reales: (a) responde a un lead, (b) resume una reunión, (c) se niega a inventar un precio que no existe.
4. Error a propósito: le pides algo fuera de alcance para mostrar los *guardrails*.

**Key takeaway:** La magia no es el modelo. Es el brief. Un mal brief = un pasante perdido. Un buen brief = un socio junior que no duerme.

---

### BLOQUE 3 — Anatomía de un asistente (sin ingeniería)
**Duración:** 16 min · **Slides:** 8

**Objetivo:** Que memoricen las 6 piezas de cualquier asistente útil. Esto es el vocabulario del resto del día.

**Dinámica:** Charla visual (una pieza = una slide sucia, grande, memorable) + 1 ejemplo colectivo en pizarrón.

Las 6 piezas:
1. **Nombre + personalidad** (no “Bot 1”)
2. **Rol** (qué trabajo hace / qué trabajo NO hace)
3. **Contexto de la startup** (a quién sirve, oferta, tono de marca)
4. **Conocimiento** (qué sabe: precios, FAQs, ICP, no inventar)
5. **Tareas** (3–5 jobs-to-be-done, no 27)
6. **Límites** (privacidad, “si no sé, lo digo”, nunca promete descuentos)

Ejemplo colectivo: armamos en 4 minutos el asistente de una cafetería ficticia. Rápido, ruidoso, memorable.

**Key takeaway:** Si no puedes explicarlo en esas 6 cajas, no tienes un asistente. Tienes un ChatGPT con disfraz.

---

### BLOQUE 4 — Casos reales por tipo de startup
**Duración:** 12 min · **Slides:** 5

**Objetivo:** Que cada persona se reconozca y elija *un* caso de uso para el ejercicio (no tres).

**Dinámica:** Relámpago de 4 arquetipos (2 min c/u) + votación de pie (“párate si este es el tuyo”).

Arquetipos:
- **Ventas / fundraising:** califica leads, arma follow-ups, one-pagers.
- **Atención / ops:** responde FAQs, clasifica tickets, redacta políticas.
- **Contenido / marca:** ideas, copys, scripts, adaptación por canal.
- **Research / producto:** resume entrevistas, detecta patrones, arma PRDs feos pero útiles.

Cierre del bloque: “Hoy construyes UNO. El que te quite más horas esta semana. No el más sexy.”

**Key takeaway:** Un asistente que hace 1 trabajo excelente > un asistente que “hace de todo” y no sirve para nada.

---

### BREAK — 10 min
Agua, baño, recargar. Tú recorres mesas: “¿ya sabes qué tarea vas a atacar?”. Si alguien está perdido, le asignas una (soporte o contenido, las más universales).

---

### BLOQUE 5 — Ejercicio principal: construye el tuyo
**Duración:** 70 min · **Slides:** 6 (instrucciones) + canvas en papel

Ver sección 4 completa abajo.

**Key takeaway:** El primer asistente útil sale hoy. El segundo sale el martes porque ya tienes el molde.

---

### BLOQUE 6 — Del prototipo al hábito
**Duración:** 15 min · **Slides:** 7

**Objetivo:** Evitar el cementerio de GPTs abandonados. Pasar de “wow en el workshop” a “lo uso el lunes”.

**Dinámica:** Charla práctica + 3 errores mortales + mini-compromiso escrito.

Errores mortales:
1. Querer que sepa toda la empresa el día 1.
2. No pegarle documentos reales (el asistente alucina tu precio).
3. No usarlo 7 días seguidos en UNA tarea. Sin hábito, muere.

Herramientas en lenguaje humano (no feature dump):
- Gratis / casi: Gemini Gems, Claude Projects, ChatGPT (custom instructions).
- Siguiente nivel (cuando duela): Custom GPT, Make/Zapier, un bot de WhatsApp con un no-coder.
- Costo honesto: $0 para prototipar · $20/mes cuando ya te ahorra 5 horas.

Mini-compromiso (lo escriben en el canvas): *“Esta semana lo voy a usar para ______, ______ veces.”*

**Key takeaway:** Un asistente que no está en tu flujo diario es un PDF caro.

---

### BLOQUE 7 — Recursos + cierre
**Duración:** 15 min · **Slides:** 5

**Objetivo:** Dejar el kit, el grupo y la energía alta. Nadie se va “a pensarlo”.

**Dinámica:** Entrega de kit (QR) + 3 voluntarios de 45 segundos + foto + CTA.

CTA: “Mándale a tu asistente el primer brief real antes de que se acabe el café de mañana. Publica el resultado en el grupo.”

Cierre verbal (ensáyalo): *“No te convertiste en ingeniero. Te quitaste trabajo. Eso es un founder que escala.”*

**Key takeaway:** El workshop terminó. El asistente no.

---

## 4. Ejercicio principal (el que TODOS pueden hacer)

**Nombre:** *El Cerebro de tu Asistente — de papel a prueba en vivo*

**Duración total:** 70 min  
**Formato:** individual (o dupla si vinieron socios) · funciona con laptop O celular O solo papel.

### Parte A — Canvas (20 min)
Llenan el A3 con las 6 piezas. Tú das un ejemplo en voz alta los primeros 3 minutos y luego recorres mesas como un loco.

Prompt de arranque que lees en voz alta:

> “Elige UNA tarea que te robe mínimo 3 horas por semana. Si no puedes nombrarla en una frase, es demasiado amplia. Recórtala.”

Regla: máximo 5 tareas. Si escriben 12, les pides que maten 7.

### Parte B — Convierte el canvas en brief (10 min)
Les das la plantilla (también está en el QR). Copian/pegan y rellenan huecos. Cabe en una página. Esto ES el “código” de su asistente.

Estructura de la plantilla (se las dejas lista):

```
Eres [nombre], [rol] de [startup].
Ayudas a [quién] a [resultado].
Tono: [3 adjetivos]. Nunca: [3 prohibiciones].
Conoces esto: [bullet de oferta, ICP, precios, FAQs].
Tus 3 trabajos: 1) … 2) … 3) …
Si no tienes el dato, dices que no lo sabes y preguntas.
No inventas clientes, métricas ni compromisos comerciales.
Antes de responder algo largo, confirmas el objetivo en 1 línea.
```

### Parte C — Prueba en vivo (25 min)
Abren ChatGPT / Gemini / Claude (el que ya tengan; si no tienen, usan el del vecino o el tuyo en proyección para 2–3 personas).

Pegar el brief + 3 tests obligatorios:
1. **El caso feliz** (la tarea para la que nació).
2. **El caso sucio** (cliente enojado / brief incompleto / dato que no tiene).
3. **El caso trampa** (pídele que invente un descuento o un dato confidencial). Si lo hace, el brief está flojo → lo corrigen.

Tú gritas cada 8 minutos: “¿Ya corriste el caso trampa? Si tu asistente prometió un 40% off, reescríbelo YA.”

### Parte D — Show & tell relámpago (15 min)
4–5 voluntarios, 90 segundos c/u, de pie:
- Qué tarea ataca
- Una respuesta buena
- Una que falló y cómo la arreglaron

El resto aplaude el fallo tanto como el éxito. Eso baja el perfeccionismo.

**Por qué este ejercicio funciona con no-técnicos:** no instalan nada, no pagan nada obligatorio, el entregable es un texto que se llevan en el celular, y el criterio de éxito es “¿esto me ahorra una hora esta semana?”.

---

## 5. Recursos para llevar a casa

Kit digital (QR + WhatsApp del grupo, vive 30 días):

1. **Canvas en PDF + Notion** (El Cerebro de tu Asistente).
2. **Plantilla de brief** copiar/pegar (ES + variante corta para celular).
3. **Banco de 15 prompts** por arquetipo (ventas, soporte, contenido, research).
4. **Cheat sheet de herramientas** en una página: gratis vs $20 vs “cuando ya duele”, con para qué sirve cada una. Sin 40 logos.
5. **Checklist de 7 días:** día 1 pega el brief · día 2 súmale 1 documento real · día 3 caso trampa · … · día 7 decide si merece Custom GPT / Gem / Project.
6. **Guía de higiene:** qué NUNCA pegar (contraseñas, datos de clientes, estados financieros crudos). Versión simple de privacidad para founders.
7. **3 videos de 8 min** (los grabas tú después del piloto): cómo crear un Gem, un Project y un Custom GPT.
8. **Grupo WhatsApp** “Asistentes en la calle” — solo se publica: brief + resultado + 1 aprendizaje. Cero teoría.

Físico al salir: el canvas lleno (se lo llevan doblado) + sticker del workshop (van a ponerle foto).

---

## 6. Slide count estimado por sección

Mantén las slides sucias, grandes, 1 idea. Si una slide tiene un párrafo, mátala.

| Sección | Slides | Notas |
|---|---|---|
| 0. Apertura | 4 | Título, promesa, agenda visual, reglas |
| 1. El porqué | 6 | 3 historias + 1 dato + 1 pregunta |
| 2. Demo | 3 | “Antes / después / límites”. El resto es pantalla viva |
| 3. Anatomía | 8 | 6 piezas + ejemplo cafetería + recap |
| 4. Casos | 5 | 4 arquetipos + “elige UNO” |
| 5. Ejercicio | 6 | Instrucciones A-B-C-D + timer + plantilla en pantalla |
| 6. Del prototipo al hábito | 7 | 3 errores + herramientas humanas + compromiso |
| 7. Cierre | 5 | Kit, CTA, QR, foto, frase final |
| **Total** | **~44** | **Objetivo de corte: 32–36.** Mata 8 de relleno en el ensayo. |

**Regla de slides:** máximo 40 segundos por slide de contenido. Si hablas más, es demo o ejercicio, no slide.

---

## Notas de facilitación (para que no se caiga el cuarto)

- **Energía:** tú te mueves. Si te quedas atrás del podium 20 minutos, el workshop se vuelve clase. Recorre mesas en el ejercicio como si fueras mesero en hora pico.
- **El técnico de la sala:** siempre hay 2 que “ya saben de prompts”. Úsalos como ayudantes de mesa, no como copresentadores. Si empiezan a hablar de APIs, córtalos con cariño: “Eso es el módulo 2, hoy es el módulo que factura.”
- **Inclusión de dispositivos:** anuncia en el minuto 5: “Si solo trajiste el celular, estás perfecto. El canvas es el producto. La app es el horno.”
- **Idioma del asistente:** empújalos a escribir el brief en el idioma en el que atienden clientes, no en el idioma en el que les da vergüenza.
- **Cierre de ventas del siguiente paso (opcional):** si ofreces mentoría / cohort / implementación, el CTA es el checklist de 7 días, no un pitch de 8 minutos. El workshop ya vendió si el asistente les funcionó.

Frase para tener en el bolsillo cuando alguien diga “esto no sirve para mi industria”:

> “Tu industria no es especial. Tu brief está incompleto. Vamos a la mesa y lo llenamos en 6 minutos.”