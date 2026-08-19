# MiniMax M3 — startup_content/workshop_outline

- model_id: `minimax/minimax-m3`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 60.253s | tokens_per_second: 91.0
- input_tokens: 341 | output_tokens: 5482
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando una agenda detallada y materiales necesarios que son directamente aplicables para emprendedores no técnicos, con una estructura bien organizada y útil.

## Respuesta completa

# 🚀 WORKSHOP: "CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP"
## Outline Completo · 3 Horas · Presencial

---

## 📋 RESUMEN EJECUTIVO

| Elemento | Detalle |
|---|---|
| **Duración total** | 180 minutos (3 horas) |
| **Audiencia** | 20-30 emprendedores early-stage, no-técnicos |
| **Formato** | Híbrido: charla + demo + hands-on + discusión |
| **Resultado tangible** | Cada participante sale con un Asistente de IA funcional construido por ellos mismos |
| **Herramienta principal** | ChatGPT (Custom GPTs) + opciones no-code |
| **Tono** | Energético, directo, "manos a la obra", cero jerga académica |

---

## 🎒 MATERIALES NECESARIOS (PREPARACIÓN PREVIA)

### Logística del Espacio
- [ ] Sala con capacidad para 30 personas, tipo U o mesas grupales de 4-5
- [ ] Proyector + pantalla grande + cable HDMI/USB-C de repuesto
- [ ] Wi-Fi robusto (CRÍTICO: confirmar velocidad con 30 devices conectados)
- [ ] Wi-Fi de backup (hotspot móvil del facilitador como plan B)
- [ ] 1 toma de corriente por mesa
- [ ] Café, agua, snacks a media mañana ⏰

### Material del Participante (imprimir o digital)
- [ ] **Worksheet "Mapa de tu Asistente"** (1 hoja, ver ejercicio principal abajo)
- [ ] **Cheat sheet "Prompts Poderosos"** (1 página)
- [ ] **Tarjeta de acceso rápido** a los recursos post-workshop (QR code)
- [ ] Stickers de colores para votar / identificar niveles
- [ ] Post-its (3 colores: verde, amarillo, rosa)
- [ ] Sharpies + lapiceros

### Material del Facilitador
- [ ] Slides cargados (offline + online)
- [ ] 2-3 Custom GPTs de demo listos (uno fallando a propósito para mostrar errores)
- [ ] Cuenta de ChatGPT Plus de respaldo para conectar al proyector
- [ ] Playlist de fondo para transiciones ("lofi + latino beats")
- [ ] Cronómetro visible para todos
- [ ] Premios pequeños (stickers, libros, menciones) para gamificar

### Pre-work para Participantes (enviar 3 días antes)
> 📧 **Email pre-work:**
> - Crear cuenta gratuita de ChatGPT
> - Traer laptop cargada
> - Pensar en UN problema real de su startup que resuelven a diario
> - Traer 1-2 documentos típicos de su negocio (FAQs, propuesta de valor, etc.)

---

## 🗓️ AGENDA DETALLADA

```
00:00 - 00:10  →  BLOQUE 0:  Bienvenida + Icebreaker        (10 min)
00:10 - 00:30  →  BLOQUE 1:  ¿Por qué tu startup NECESITA IA? (20 min)
00:30 - 00:55  →  BLOQUE 2:  Los 4 superpoderes de un asistente (25 min)
00:55 - 01:05  →  ☕ BREAK + Networking                       (10 min)
01:05 - 02:15  →  BLOQUE 3:  HANDS-ON - Construye tu asistente (70 min)
02:15 - 02:40  →  BLOQUE 4:  Pruebas, iteración y errores      (25 min)
02:40 - 03:00  →  BLOQUE 5:  De prototipo a producción         (20 min)
03:00 - 03:00  →  CIERRE:    Q&A + foto grupal + despedida     (incluido en bloque 5)
```

**Total: 180 minutos exactos**

---

## 🎯 BLOQUE 0 — BIENVENIDA + ICEBREAKER (10 min)

| Campo | Detalle |
|---|---|
| **Objetivo** | Romper el hielo, generar energía, mapear expectativas |
| **Dinámica** | Sticky note + presentación relámpago |
| **Key takeaway** | "Todos estamos en el mismo barco y vamos a construir HOY" |

**Desarrollo:**

**0:00 - 0:03 · Arranque con energía** (3 min)
- Música de fondo mientras entran
- Facilitador recibe en la puerta, reparte stickers de 3 colores: 🟢 "ya uso IA", 🟡 "he jugado un poco", 🟣 "soy nuevo total"
- Foto grupal rápida en la entrada para Slack/WhatsApp grupal

**0:03 - 0:10 · Dinámica "30 segundos para brillar"** (7 min)
- Cada persona se para y dice en 30 segundos:
  - Nombre
  - Startup (1 frase)
  - Color de sticker (nivel con IA)
  - **EL PROBLEMA** que quiere resolver con IA hoy
- Facilitador va anotando en una pizarra los problemas recurrentes (esto nutre el Bloque 1)
- Reglas: nadie se presenta dos veces con el mismo problema → hacerlo memorable

**Slides: 2** (portada + reglas del juego)

---

## 🧠 BLOQUE 1 — ¿POR QUÉ TU STARTUP NECESITA UN ASISTENTE DE IA? (20 min)

| Campo | Detalle |
|---|---|
| **Objetivo** | Crear urgencia y mostrar el ROI de tener un asistente propio |
| **Dinámica** | Charla con datos + 1 demo en vivo + pregunta al público |
| **Key takeaway** | "No es lujo, es tu próximo empleado a costo cero" |

**Desarrollo:**

**0:10 - 0:18 · La verdad sin filtro** (8 min) — *Charla*
- 3 datos duros:
  - El 73% de las startups que escalan usan algún asistente de IA en menos de 6 meses (cita aproximada, fuente a confirmar)
  - "Tus clientes esperan respuesta en menos de 5 minutos"
  - "Tú estás haciendo 5 trabajos a la vez y tu startup lo sabe"
- Mostrar 2 ejemplos rápidos de asistentes YA funcionando en LATAM:
  - Asistente de menú para restaurant
  - Bot de calificación de leads para SaaS B2B
- **Analogía central:** "Un asistente de IA es como tener un pasante que nunca duerme, no cobra y siempre está de buen humor... PERO necesita que le expliques bien qué hacer"

**0:18 - 0:25 · Demo relámpago** (7 min) — *Demo en vivo*
- Mostrar un Custom GPT ya construido en 5 minutos
- Hacerle 3 preguntas en vivo y mostrar respuestas
- Mostrar también una respuesta MALA → introducir el concepto "garbage in, garbage out" sin tecnicismos

**0:25 - 0:30 · Discusión dirigida** (5 min)
- Pregunta al público: "De los problemas que anotamos en la pizarra, ¿cuáles se podrían resolver con un asistente así?"
- Votan con sticky notes
- **Transición al bloque 2:** "Para construir uno, primero necesitas entender qué puede y qué NO puede hacer"

**Slides: 6** (datos + analogía + ejemplos + demo + pregunta + transición)

---

## ⚡ BLOQUE 2 — LOS 4 SUPERPODERES DE UN ASISTENTE DE IA (25 min)

| Campo | Detalle |
|---|---|
| **Objetivo** | Entender capacidades reales vs. expectativas infladas |
| **Dinámica** | Charla visual + ejercicio rápido en parejas |
| **Key takeaway** | "La IA no piensa por ti, multiplica lo que tú ya sabes hacer" |

**Desarrollo:**

**0:30 - 0:40 · Los 4 superpoderes** (10 min) — *Charla + visuales*
- **Súper poder 1: RESPONDER** → FAQs, soporte 24/7, info de productos
- **Súper poder 2: GENERAR** → Copy, ideas, emails, propuestas
- **Súper poder 3: ANALIZAR** → Resumir reuniones, clasificar datos, encontrar patrones
- **Súper poder 4: PERSONALIZAR** → Onboarding de usuarios, recomendaciones, follow-ups
- Cada poder con 1 ejemplo concreto de startup real

**0:40 - 0:50 · Lo que la IA NO hace bien (todavía)** (10 min) — *Charla honesta*
- No reemplaza tu criterio
- No sabe cosas que no le das
- No decide por ti
- **Analogía:** "Es como un auto Fórmula 1: necesita un buen piloto (tú) y buena gasolina (tus datos)"
- Slide visual: "Lo que entra = lo que sale"

**0:50 - 0:55 · Ejercicio relámpago "Matchea el poder"** (5 min) — *Ejercicio en parejas*
- Repartir 8 tarjetas con problemas
- En 3 minutos, en parejas, emparejar cada problema con un superpoder
- 2-3 parejas comparten en voz alta
- **Premio:** sticker dorado para la dupla más rápida

**Slides: 10** (4 poderes + 1 NO hace + analogía + ejercicio + 2 transiciones)

---

## ☕ BREAK + NETWORKING (10 min)

| Campo | Detalle |
|---|---|
| **Objetivo** | Descanso,社交, validar problemas con pares |
| **Dinámica** | Café libre + 1 pregunta guiada |

- Música suena
- 1 pregunta en pantalla: "Cuéntale a tu vecino: ¿cómo resuelves hoy ese problema?"
- Facilitador circula, identifica a los que necesitan ayuda extra
- A los 8 minutos, todos de vuelta

---

## 🛠️ BLOQUE 3 — HANDS-ON: CONSTRUYE TU ASISTENTE (70 min)

> 🔥 **ESTE ES EL CORAZÓN DEL WORKSHOP. La sala se transforma en un maker space.**

| Campo | Detalle |
|---|---|
| **Objetivo** | Que cada participante salga con un asistente funcional |
| **Dinámica** | Demo paso a paso + construcción individual + soporte 1:1 |
| **Key takeaway** | "Si pudiste llenarlo en el worksheet, puedes construirlo" |

**Desarrollo:**

**01:05 - 01:15 · Demo guiada paso a paso** (10 min) — *Demo en vivo con proyector*
- Construir un Custom GPT desde cero EN VIVO
- Pasos que se muestran en pantalla:
  1. Crear GPT → nombre
  2. Escribir instrucciones (usar plantilla del worksheet)
  3. Subir 1 documento de ejemplo (FAQ de la startup)
  4. Probarlo con 2 preguntas reales
- Mientras se construye, **comentar CADA decisión en voz alta**

**01:15 - 01:35 · Fase 1: DISEÑO** (20 min) — *Trabajo individual con worksheet*
- Cada quien llena el **Worksheet "Mapa de tu Asistente"** (ver abajo)
- Facilitador y 2-3 co-facilitadores circulan mesa por mesa
- Música suave de fondo
- Meta: tener claro el **nombre, propósito y 3 preguntas clave** antes de tocar la laptop

**01:35 - 01:55 · Fase 2: CONSTRUCCIÓN** (20 min) — *Construcción individual en laptop*
- Todos abren ChatGPT → "Create a GPT"
- Siguen los pasos de la demo, pero con SU caso
- Regla: no avanzar al siguiente paso hasta que el anterior funcione
- Facilitadores circulan, resuelven bloqueos
- **Tip:** los más avanzados pueden empezar a subir 2-3 documentos

**01:55 - 02:10 · Fase 3: PRIMERA PRUEBA** (15 min) — *Testeo individual + pareja*
- Probar el asistente con 3 preguntas
- Anotar las respuestas que NO convencen en post-its amarillos
- Intercambiar con la persona de al lado y probarlo 5 minutos
- Feedback cruzado: "¿qué mejorarías?"
- **Micro-discusión:** ¿Qué patrones ven en lo que NO funciona?

**02:10 - 02:15 · Celebración rápida** (5 min)
- "Si tu asistente respondió algo útil aunque sea 1 vez: GANASTE"
- Aplausos
- Foto grupal con todos los asistentes construidos

**Slides: 4** (introducción al bloque + worksheet + 2 slides de tips durante construcción)

---

## 🔄 BLOQUE 4 — PRUEBAS, ITERACIÓN Y ERRORES (25 min)

| Campo | Detalle |
|---|---|
| **Objetivo** | Aprender a mejorar el asistente de forma continua |
| **Dinámica** | Discusión grupal + 1 caso de estudio en vivo |
| **Key takeaway** | "Tu primer asistente será un borrador. El verdadero empieza mañana" |

**Desarrollo:**

**02:15 - 02:25 · Caso de estudio: "El bot que casi la caga"** (10 min)
- Contar historia real (anonimizada) de un asistente que inventó precios
- Mostrar el prompt original y el prompt corregido
- Lección: "Si tu asistente no sabe, debe DECIR QUE NO SABE, no inventar"
- Slide con 5 reglas de oro para prompts

**02:25 - 02:35 · Demo "cirugía de prompts"** (10 min) — *Demo en vivo*
- Tomar UNO de los Custom GPTs construidos por la audiencia (pedir voluntario)
- Mostrar frente a todos cómo mejorarlo en 3 cambios simples
- Que el dueño del bot pruebe la versión mejorada
- **Esto demuestra que iterar es rápido**

**02:35 - 02:40 · Las 5 reglas de oro** (5 min)
1. Sé específico (no "responde bien", di "responde en máximo 3 líneas")
2. Dale personalidad (tono de tu marca)
3. Ponle límites (qué NO debe hacer)
4. Dale ejemplos (1 o 2 conversaciones modelo)
5. Pruebálo como si fueras tu peor cliente

**Slides: 6** (caso + demo + 5 reglas)

---

## 🚀 BLOQUE 5 — DE PROTOTIPO A PRODUCCIÓN (20 min)

| Campo | Detalle |
|---|---|
| **Objetivo** | Saber qué hacer mañana con lo construido hoy |
| **Dinámica** | Charla + roadmap + Q&A |
| **Key takeaway** | "Hoy es el día 1. Mañana tu asistente trabaja para ti" |

**Desarrollo:**

**02:40 - 02:50 · Tu roadmap de 30 días** (10 min) — *Charla*
- **Semana 1:** Probar con 5 usuarios reales, anotar TODAS las respuestas raras
- **Semana 2:** Iterar prompts + subir 5 documentos clave
- **Semana 3:** Integrar al canal real (WhatsApp, web, email)
- **Semana 4:** Medir: ¿cuántas horas te ahorraste?
- Mencionar herramientas de integración: WhatsApp Business API, Voiceflow, Make, Tidio
- **Honestidad:** "Esto no es magia, es iteración disciplinada"

**02:50 - 02:55 · Los siguientes pasos según tu nivel** (5 min) — *Charla segmentada*
- 🟢 Ya uso IA → "Crea tu segundo asistente, automatiza un flujo completo"
- 🟡 He jugado → "Llega al menos a 100 conversaciones reales este mes"
- 🟣 Nuevo → "Solo practica 15 min diarios con tu bot esta semana"

**02:55 - 03:00 · Cierre + Q&A + foto** (5 min)
- Recordar recursos (QR code)
- Foto grupal
- "Hoy se graduaron. Nos vemos en 30 días con resultados"

**Slides: 7** (roadmap + herramientas + niveles + cierre + 2 de Q&A)

---

## 📊 RESUMEN DE SLIDES POR SECCIÓN

| Sección | Slides | % del total |
|---|---|---|
| Bloque 0 — Bienvenida | 2 | 6% |
| Bloque 1 — Por qué IA | 6 | 17% |
| Bloque 2 — 4 superpoderes | 10 | 28% |
| Bloque 3 — Hands-on | 4 | 11% |
| Bloque 4 — Iteración | 6 | 17% |
| Bloque 5 — Producción + cierre | 7 | 20% |
| **TOTAL** | **~35 slides** | **100%** |

> 💡 **Nota:** El workshop es 60% práctica, 40% teoría. Los slides son apoyo, no protagonistas.

---

## 🏋️ EJERCICIO PRINCIPAL: WORKSHEET "MAPA DE TU ASISTENTE"

> **Objetivo:** Que cada participante diseñe en papel lo que luego construirá en ChatGPT.

### Plantilla del Worksheet (1 página, doble cara)

**FRENTE:**

```
┌─────────────────────────────────────────────────────┐
│  🗺️ MAPA DE TU ASISTENTE DE IA                     │
│  Workshop: Construye tu Asistente de IA             │
│  Nombre: ________________  Startup: _____________  │
└─────────────────────────────────────────────────────┘

1. ¿PARA QUIÉN es? (usuario/cliente/equipo)
   _____________________________________________

2. ¿QUÉ PROBLEMA concreto resuelve?
   _____________________________________________

3. ¿QUÉ TONO tiene? (formal, casual, técnico, etc.)
   _____________________________________________

4. Escribe 3 PREGUNTAS que le harían tus usuarios:
   a) __________________________________________
   b) __________________________________________
   c) __________________________________________

5. ¿Qué NO debe responder o hacer?
   _____________________________________________
```

**REVERSO:**

```
6. ¿Qué DOCUMENTOS debería "conocer"?
   (FAQs, manuales, info de productos, etc.)
   _____________________________________________

7. Nombre tentativo del asistente:
   _____________________________________________

8. Frase de inicio (cómo saluda):
   "_____________________________________________"

9. Personalidad en 3 adjetivos:
   _____________________________________________

10. ¿Cómo sabrás que está funcionando?
    (métrica simple: respuestas/día, ahorras X min, etc.)
    _____________________________________________
```

### Estructura de facilitación del ejercicio (70 min en Bloque 3):
- **5 min:** explicar el worksheet
- **20 min:** llenar individualmente
- **5 min:** validar con la persona de al lado (intercambio de feedback)
- **40 min:** construir el GPT en ChatGPT siguiendo el worksheet

---

## 📦 RECURSOS PARA LLEVAR A CASA

### 🎁 Paquete Digital (QR code + email post-workshop)

**1. Cheat sheet "20 Prompts Poderosos para Startups"**
- 20 prompts probados para: ventas, soporte, marketing, producto, ops

**2. Video tutorial "Cómo mejorar tu Custom GPT"**
- 15 minutos, screen-recording paso a paso

**3. Lista curada de herramientas**
- **Para construir:** ChatGPT, Claude, Gemini, Relevance AI
- **Para integrar:** Voiceflow, Make, Zapier, Tidio, n8n
- **Para datos:** Notion, Airtable, Google Sheets
- **Para WhatsApp:** Evolution API, WPPConnect, Wablas

**4. Comunidad post-workshop**
- Grupo de WhatsApp/Telegram privado para compartir avances
- 1 sesión de seguimiento en 30 días (60 min online)

**5. Plantillas listas para usar**
- Custom GPT de "Asistente de Soporte"
- Custom GPT de "Analizador de Competencia"
- Custom GPT de "Generador de Copy"
- Custom GPT de "Coach de Pitch"

**6. 3 lecturas recomendadas** (10 min cada una)
- "El estado del arte de los AI Agents en LATAM"
- "5 errores fatales al implementar IA en startups"
- "Cómo medir el ROI de tu asistente"

---

## 🎯 MÉTRICAS DE ÉXITO DEL WORKSHOP

Para que tú (facilitador) sepas si funcionó:

| Métrica | Meta |
|---|---|
| % que construyó un asistente funcional | >85% |
| % que respondió "lo usaría esta semana" | >90% |
| NPS del workshop | >8/10 |
| % que se une al grupo post-workshop | >70% |
| % que completa el ejercicio | >95% |

---

## 💡 TIPS FINALES PARA EL FACILITADOR

1. **Antes del workshop:** Envía el email pre-work 3 días antes Y un recordatorio 1 día antes. El 80% del éxito depende de que lleguen con cuenta creada.

2. **Durante:** Ten SIEMPRE 2-3 co-facilitadores si el grupo es de 20+. En el bloque hands-on vas a necesitarte multiplicar.

3. **Si alguien se atrasa:** Es normal. Empareja al más rápido con el más lento como "co-piloto".

4. **Si falla el Wi-Fi:** Ten screenshots de cada paso del Custom GPT para mostrar offline. La construcción se hace en laptops, pero la demo se hace con tu pantalla.

5. **La energía importa más que el contenido:** Si ves caras perdidas en el Bloque 1, acelera y salta directo al Bloque 3. Construir motiva más que escuchar.

6. **Repite el mantra:** "Hoy no estamos aprendiendo, estamos CONSTRUYENDO."

---

¿Quieres que profundice en alguna sección? Por ejemplo, puedo:
- 📝 Redactar el **guion completo palabra por palabra** de las demos en vivo
- 🎨 Diseñar el **worksheet en formato imprimible** con branding
- 📧 Redactar los **emails pre y post workshop**
- 🧪 Crear una **rúbrica de evaluación** para medir asistentes creados
- 🇨🇴 Adaptar los **ejemplos a un país específico** de LATAM

¡Tú dime hacia dónde seguimos! 🚀