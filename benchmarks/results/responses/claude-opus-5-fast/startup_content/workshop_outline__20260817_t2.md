# Claude Opus 5 Fast — startup_content/workshop_outline

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.85 | quality: 10.0
- latency_total: 40.44s | tokens_per_second: 202.6
- input_tokens: 314 | output_tokens: 8192
- judge_score: 5.0 | justificación: 

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

# 🚀 CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP
### Workshop Práctico · 3 horas · 20-30 emprendedores no-técnicos

**Promesa del workshop (dila en voz alta al inicio y al final):**
> "Nadie sale de esta sala sin un asistente de IA funcionando, con el contexto de SU negocio, haciendo UN trabajo real. No teoría. No 'les mando el material'. Funcionando."

---

## 📋 1. AGENDA MAESTRA (180 minutos)

| # | Hora | Min | Bloque | Formato |
|---|------|-----|--------|---------|
| 0 | 0:00–0:15 | 15 | **Aterrizaje + El Diagnóstico Brutal** | Energizer + votación en vivo |
| 1 | 0:15–0:35 | 20 | **Qué SÍ es y qué NO es un asistente de IA** | Charla + demo shock |
| 2 | 0:35–0:50 | 15 | **Elige tu Tornillo** (el trabajo a delegar) | Ejercicio individual + trío |
| 3 | 0:50–1:05 | 15 | **El Framework C.O.R.T.E.** | Charla + demo en vivo |
| — | 1:05–1:15 | 10 | ☕ **BREAK** (café, baño, cargar laptop) | — |
| 4 | 1:15–2:00 | 45 | **🔨 MANOS AL TECLADO — Sprint 1: El Cerebro** | Construcción guiada |
| 5 | 2:00–2:20 | 20 | **Sprint 2: Alimenta y Rompe tu Asistente** | Construcción + testeo cruzado |
| 6 | 2:20–2:35 | 15 | **Demo Roulette** | 5 demos de 90 segundos |
| 7 | 2:35–2:50 | 15 | **De juguete a sistema: costos, riesgos y el siguiente paso** | Charla + Q&A rápido |
| 8 | 2:50–3:00 | 10 | **Compromiso de 7 días + Kit para llevar** | Cierre + foto grupal |

**Total slides estimadas: 58** (desglose por bloque más abajo)

---

## 🎒 2. MATERIALES Y PREPARACIÓN

### A. Pre-workshop — 72 horas antes (email + WhatsApp)

Envía un correo con **UNA sola tarea** (si pides más, nadie la hace):

> **"Tarea de 10 minutos para el sábado. Sin esto, no vas a poder construir nada."**
> 1. Crea tu cuenta en **una** de estas tres (todas sirven, la 3 es gratis):
>    - ChatGPT (chat.openai.com) — Plus recomendado
>    - Claude (claude.ai) — Pro recomendado
>    - **Google Gemini (gemini.google.com) — GRATIS, y con esta construimos si no quieres pagar**
> 2. Trae tu **laptop cargada** (celular NO sirve para este workshop).
> 3. Trae **3 archivos de tu negocio** en tu compu o Drive: tu pitch deck, tu lista de precios/servicios, y 5-10 conversaciones reales con clientes (copiadas a un Word/Doc, sin datos personales).

### B. Recordatorio 24 horas antes (WhatsApp, con voz nota)
- Confirmación de asistencia (link)
- Recordar: laptop + cargador + los 3 archivos
- Link a la **carpeta de recursos** (ya abierta desde antes)

### C. Del facilitador — checklist física

| Categoría | Item | Cantidad |
|---|---|---|
| **Espacio** | Mesas en islas de 4-5 personas (NO auditorio) | 6 islas |
| | Regletas/extensiones eléctricas | 1 por mesa + 2 extra |
| | Proyector + cable HDMI + adaptador USB-C | 1 + backups |
| | Timer visible proyectado (timer.online) | 1 |
| **Conectividad** | WiFi dedicado, contraseña impresa en cada mesa | — |
| | **Hotspot 4G/5G de respaldo** (plan B real) | 2 |
| **Impresos** | **Canvas C.O.R.T.E.** tamaño A3 | 2 por persona |
| | Hoja "Mi Tornillo" (media carta) | 1 por persona |
| | Tarjeta de compromiso 7 días | 1 por persona |
| | Gafete: NOMBRE + STARTUP + "Mi tornillo: ______" | 1 por persona |
| **Papelería** | Post-its 3 colores | 3 blocks/mesa |
| | Plumones/marcadores | 2 por persona |
| | Cinta adhesiva + pared/rotafolio para "Muro de Tornillos" | — |
| **Humano** | **Mentores volantes (1 por cada 10 asistentes)** — resuelven bloqueos en el Bloque 4 | 2-3 |
| **Extras** | 2-3 laptops de respaldo prestadas | — |
| | Premio para el mejor demo (libro, mentoría 1:1, créditos) | 1-3 |
| | Música (playlist de trabajo para los sprints) + bocina | — |
| | Café, agua, snack para el break | — |

### D. Preparación digital del facilitador
- [ ] **Asistente demo YA construido** (el tuyo, o uno de una startup ficticia local: "Panadería Doña Rosa" / "Fulanito Fitness"). Es tu ancla del taller.
- [ ] **Asistente demo INTENCIONALMENTE malo** (para el contraste del Bloque 1).
- [ ] Carpeta pública (Notion o Drive) con TODO el kit, con QR grande impreso.
- [ ] Grupo de WhatsApp del workshop creado y QR de invitación en slide.
- [ ] Formulario de feedback (3 preguntas) con QR listo para el cierre.
- [ ] Slides descargadas offline (por si muere el internet).

---

## 🎤 3. BLOQUES EN DETALLE

---

### **BLOQUE 0 — Aterrizaje + El Diagnóstico Brutal**
**⏱ 15 min · 🎞 6 slides**

**Objetivo:** Romper el hielo, calibrar el nivel real de la sala y crear urgencia emocional en 15 minutos.

**Dinámica:**
1. **(3 min) Levántate si...** — Facilitador dispara: *"Levántate si nunca has usado ChatGPT. Si lo usas todos los días. Si has pagado por una herramienta de IA. Si alguien te ha vendido 'IA' y sentiste que te vieron la cara."* → Risas, energía, y tú ya sabes con quién estás hablando.
2. **(7 min) El Diagnóstico Brutal:** cada persona escribe en un post-it: *"La tarea que más horas me roba cada semana y que ODIO hacer."* Lo pega en el **Muro de Tornillos**. El facilitador lee 6-8 en voz alta rápido.
3. **(5 min) Reglas del juego + la promesa:**
   - Regla del **laptop cerrado**: cuando yo hablo, laptop a 45°. Cuando digo "manos al teclado", es de ustedes.
   - Regla del **vecino primero**: antes de levantar la mano, pregúntale a tu vecino. 60% de los problemas se resuelven ahí.
   - Regla de **"aquí no hay preguntas tontas, hay talleres mal explicados"**.

**Key takeaway:**
> "El asistente de IA no empieza con tecnología. Empieza con una tarea que odias."

---

### **BLOQUE 1 — Qué SÍ es y qué NO es un asistente de IA**
**⏱ 20 min · 🎞 12 slides**

**Objetivo:** Destruir 3 mitos, dar el modelo mental correcto y provocar un "ahhh" con una demo de contraste.

**Dinámica:** Charla rápida (8 min) + **Demo Shock** (8 min) + preguntas relámpago (4 min).

**Contenido:**

**Los 3 mitos que matamos hoy:**
| Mito | Realidad |
|---|---|
| ❌ "Necesito programar / contratar un dev" | ✅ Hoy lo haces con texto, en tu idioma, en 40 minutos |
| ❌ "Necesito 50 mil dólares y 6 meses" | ✅ Empiezas con $0-20 USD/mes |
| ❌ "Es un robot que reemplaza gente" | ✅ Es un **becario brillante con amnesia**: sabe muchísimo, pero no sabe NADA de tu negocio hasta que se lo dices |

**El modelo mental central — "El Becario Brillante":**
Un asistente de IA = **Modelo (el cerebro) + Instrucciones (su manual de puesto) + Contexto (los archivos de tu empresa) + Canal (dónde vive)**.
Tú no vas a construir el cerebro. Vas a **contratar y entrenar al becario**.

**🔥 DEMO SHOCK (lo más importante del bloque):**
1. Abro un ChatGPT vacío y le pido: *"Escribe la respuesta a un cliente que dice que estamos caros."* → Sale algo genérico, gringo, con viñetas, sin alma. La sala se ríe. **"Esto es lo que el 90% está haciendo."**
2. Abro mi **asistente entrenado** (Panadería Doña Rosa) y le pido exactamente lo mismo. → Responde con el tono de la marca, mencionando el producto real, el precio real, la política real de descuentos, en el español de la región.
3. **Muestro el "detrás de cámaras"**: abro las instrucciones y los 3 archivos que subí. *"Esta es toda la magia. 400 palabras y 3 documentos."*

**Key takeaway:**
> "La diferencia entre 'IA genérica' y 'TU asistente' no es el modelo. Es el CONTEXTO que le das. Y ese contexto ya lo tienes en tu cabeza y en tu Drive."

---

### **BLOQUE 2 — Elige tu Tornillo**
**⏱ 15 min · 🎞 7 slides**

**Objetivo:** Que cada persona salga con **UN solo trabajo específico y acotado** para su asistente. Este es el bloque que salva el workshop: sin foco, todos construyen un asistente inútil que "hace de todo".

**Dinámica:** Mini-charla (4 min) → Ejercicio individual (5 min) → Ronda en tríos (6 min).

**Contenido:**

**La regla del Tornillo:** No construyas una navaja suiza. Construye un desarmador que aprieta UN tornillo, perfecto.

**Matriz de selección (proyectada):** cada tarea de tu post-it se evalúa con 3 preguntas:
1. **¿Se repite?** (mínimo 3 veces por semana)
2. **¿Es puro texto o información?** (si requiere manos, piernas o firmas, no aplica hoy)
3. **¿Si sale un 80% bien, me sirve?** (si necesita 100% de precisión legal/médica/financiera, hoy no)

**3 de 3 = ese es tu tornillo.**

**Menú de tornillos típicos en startups early-stage LatAm** (para quien se atore):
- 🗣 Responder los 20 mensajes de WhatsApp que se repiten cada día
- 💰 Calificar leads del formulario y escribir el primer mensaje personalizado
- ✍️ Convertir 1 idea en 5 posts para LinkedIn/Instagram con mi tono
- 📄 Redactar propuestas comerciales con mi estructura y mis precios
- 🎧 Resumir llamadas con clientes y sacar los siguientes pasos
- 📊 Traducir una hoja de cálculo caótica en un reporte semanal legible
- 🧾 Redactar respuestas a inversionistas / actualizaciones mensuales de investors

**Ejercicio "Mi Tornillo" (hoja impresa):**
```
Mi asistente se va a llamar: ______________________
Su ÚNICO trabajo es: __________________________
Lo hace para (usuario): ⬜ Yo  ⬜ Mi equipo  ⬜ Mi cliente directo
Hoy esta tarea me toma _____ horas por semana.
Si funciona, en 30 días habré ahorrado _____ horas.
```

**Ronda en tríos (2 min c/u):** *"Mi asistente hace X para Y."* Los otros dos solo pueden decir: **"muy amplio"** o **"claro"**. Iterar hasta que sea "claro".

**Key takeaway:**
> "Un asistente que hace una cosa excelente vale más que diez que hacen todo más o menos. Elige el tornillo."

---

### **BLOQUE 3 — El Framework C.O.R.T.E.**
**⏱ 15 min · 🎞 9 slides**

**Objetivo:** Entregar la única herramienta conceptual del día: cómo escribir las instrucciones de un asistente sin ser técnico.

**Dinámica:** Charla (6 min) + **construcción en vivo del canvas frente a la sala** con una startup voluntaria de la audiencia (9 min).

**Contenido — El Canvas C.O.R.T.E.:**

| Letra | Qué es | Pregunta que responde | Ejemplo (Panadería Doña Rosa) |
|---|---|---|---|
| **C — Contexto** | Quién eres y a quién sirves | *"¿Qué debe saber de mi negocio para no decir tonterías?"* | "Panadería artesanal en Guadalajara, 3 sucursales, vendemos por WhatsApp, ticket promedio $250 MXN, clientas mujeres 30-55." |
| **O — Objetivo** | El único trabajo | *"¿Qué debe LOGRAR en cada interacción?"* | "Responder dudas de pedidos y cerrar la venta con un pedido confirmado (producto + fecha + sucursal)." |
| **R — Rol** | Quién es él/ella | *"¿A quién estoy contratando?"* | "Eres 'Rosita', asistente de ventas con 5 años de experiencia en atención por WhatsApp." |
| **T — Tono y formato** | Cómo suena y cómo entrega | *"¿Cómo hablamos aquí?"* | "Cálida, tuteas, máximo 4 líneas, usas 1 emoji máximo, español de México, nunca dices 'estimado cliente'." |
| **E — Ejemplos y límites** | Qué SÍ y qué NUNCA | *"¿Dónde está la línea?"* | "SÍ: ofrecer alternativas si algo se agotó. NUNCA: inventar precios, dar descuentos >10%, prometer entregas el mismo día. Si no sabes, di 'déjame confirmarlo con el equipo'." |

**La regla de oro de la E:** *Los límites son más importantes que las instrucciones.* Un asistente sin límites inventa. Un asistente con límites es confiable.

**Demo en vivo:** llamas a un voluntario, llenas su canvas en pantalla en 6 minutos con toda la sala aportando. Esto le da permiso al resto de escribir "feo y rápido".

**Key takeaway:**
> "Escribir las instrucciones de tu asistente es exactamente igual que entrenar a tu primer empleado. Si no se lo sabes explicar a un humano, la IA tampoco lo va a entender."

---

### ☕ **BREAK — 10 min**
*Proyecta: el timer en cuenta regresiva + el QR de la carpeta de recursos + "Conecta tu cargador AHORA".*
*Mentores volantes: circulen. Los que están atorados en su Tornillo, aprovechen aquí.*

---

### **BLOQUE 4 — 🔨 MANOS AL TECLADO: Sprint 1 — El Cerebro**
**⏱ 45 min · 🎞 8 slides (pantallas guía, se quedan proyectadas)**

**Objetivo:** Que cada persona tenga un asistente **creado y respondiendo** con las instrucciones C.O.R.T.E.

**Dinámica:** Construcción individual guiada, con música, mentores circulando y checkpoints colectivos.

**Estructura minuto a minuto:**

| Min | Qué pasa |
|---|---|
| 0-5 | **Elige tu camino** (slide proyectada permanentemente): <br>🟢 **Ruta Gratis:** Gemini → "Gems" → Nuevo Gem <br>🔵 **Ruta ChatGPT:** ChatGPT → Explorar GPTs → Crear <br>🟣 **Ruta Claude:** Claude → Proyectos → Nuevo proyecto → Instrucciones |
| 5-20 | **Escribe tu C.O.R.T.E. en el canvas de papel.** ✋ *Papel primero, teclado después.* Regla: **escribe feo y rápido**. Nadie va a leerlo. |
| 20-22 | 🛑 **Checkpoint 1:** "Levanten la mano quienes ya tienen las 5 letras llenas." Mentores van a las manos abajo. |
| 22-35 | **Transcribe tu canvas al campo de instrucciones** y crea el asistente. |
| 35-40 | **Primera prueba:** hazle las **3 preguntas más frecuentes** que te hacen