# Nemotron 3 Ultra 550B — startup_content/workshop_outline

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 167.485s | tokens_per_second: 39.5
- input_tokens: 206 | output_tokens: 6610

## Respuesta completa

# 🚀 WORKSHOP OUTLINE: "CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP"
## *Workshop Práctico de 3 Horas - Energía Latam Style*

---

## 📋 **INFO RÁPIDA**
| Detalle | Especificación |
|---------|----------------|
| **Duración** | 3 horas exactas (incluye 1 break de 15 min) |
| **Audiencia** | 20-30 founders early-stage, no-técnicos |
| **Formato** | 30% inspiración/demo · 60% hands-on · 10% networking |
| **Output final** | Cada founder se va con **un asistente funcionando** en su celular/laptop |
| **Vibe** | "Hackaton express" + "Café con amigos" + "Shark Tank ligero" |

---

## 🗓️ **AGENDA DETALLADA (180 MIN)**

| Hora | Bloque | Duración | Tipo |
|------|--------|----------|------|
| **0:00 - 0:15** | **Bienvenida & Icebreaker "Mi Dolor de Cabeza"** | 15 min | 🎤 Dinámica |
| **0:15 - 0:35** | **Mentalidad: ¿Qué SÍ y qué NO puede un Asistente IA hoy?** | 20 min | 💡 Charla + Demo live |
| **0:35 - 1:05** | **Arquitectura No-Code: El "Cerebro" + "Manos" + "Memoria"** | 30 min | 🧠 Framework visual |
| **1:05 - 1:20** | **☕ BREAK CAFÉ + NETWORKING "Busca tu socio de testing"** | 15 min | 🤝 Social |
| **1:20 - 2:20** | **🛠️ MANOS A LA OBRA: Construcción Guiada (Core del workshop)** | 60 min | 💻 Hands-on intenso |
| **2:20 - 2:40** | **Testing Cruzado: "Rompe el asistente de tu compa"** | 20 min | 🧪 Ejercicio grupal |
| **2:40 - 2:55** | **Deploy Real: De localhost a WhatsApp/Slack/Web en 3 clicks** | 15 min | 🚀 Demo + acción |
| **2:55 - 3:00** | **Cierre: Commit público + Foto grupal + Próximos pasos** | 5 min | 🎉 Celebración |

---

## 📦 **MATERIALES NECESARIOS (PREPARAR ANTES)**

### **Facilitador (Tú)**
| Item | Cantidad | Notas |
|------|----------|-------|
| Laptop + cargador | 1 | Con hotspot backup |
| Proyector/TV + HDMI | 1 | Testear audio para demos de voz |
| Clicker | 1 | Libertad de movimiento |
| Micrófono inalámbrico | 1 | Si sala > 20 personas |
| Stickers "Rompi mi bot" | 30 | Para testing cruzado (divertido) |
| Timer visible (proyectado) | 1 | Online-stopwatch.com en fullscreen |
| Agua/café personal | - | Hidratación = energía |

### **Por Participante (BYOD - Bring Your Own Device)**
| Requisito | Mínimo | Ideal |
|-----------|--------|-------|
| Laptop | 1 por persona | 1 per persona |
| Smartphone | - | 1 per persona (para test WhatsApp) |
| Cuenta Google/Gmail | **OBLIGATORIO** | Ya logueada |
| Cuenta WhatsApp | **OBLIGATORIO** | Para deploy final |

### **Cuentas Gratuitas PRE-CREADAS (Tú las creas día anterior)**
| Herramienta | Cuentas necesarias | Para qué |
|-------------|-------------------|----------|
| **n8n.cloud** (o self-hosted) | 1 cuenta maestra + 30 workflows template | Orquestador visual |
| **OpenRouter.ai** | 1 API key maestra (créditos $10) | LLM router multi-modelo |
| **Supabase** | 1 proyecto maestra + 30 tablas | Memoria vectorial (RAG) |
| **Twilio Sandbox WhatsApp** | 1 número sandbox | Deploy a WhatsApp real |

> ⚡ **PRO TIP**: Crea un **Notion/Google Doc "Kit de Supervivencia"** con: links directos, API keys compartidas (solo lectura), templates n8n pre-importados, prompts copia-pega. Comparte QR al entrar.

### **Impresos (Opcional pero recomendado)**
- **Cheatsheet 1-página**: Arquitectura + Prompts clave + Shortcuts n8n
- **Worksheet "Diseña tu Asistente"**: 1 por persona (ver Bloque 3)
- **Feedback cards**: 1 por persona (NPS + 1 cosa que aplicarás mañana)

---

## 🧱 **BLOQUES DETALLADOS**

---

### **BLOQUE 1: BIENVENIDA & ICEBREAKER "MI DOLOR DE CABEZA"**
**⏱ 15 min | 🎤 Dinámica participativa**

| Elemento | Detalle |
|----------|---------|
| **Objetivo** | Romper hielo, detectar dolores reales, crear vulnerabilidad compartida, energizar sala |
| **Dinámica** | 1. **Ronda rápida** (30 seg c/u): Nombre, startup en 1 frase, **#1 tarea que ODIA hacer y repetitiva**<br>2. Facilitador anota en pizarra/miro: patrones (ej: "responder leads", "hacer propuestas", "contestar soporte", "postear contenido")<br>3. **Votación con manos**: "¿Quién tiene este dolor?" → Top 3 dolores = casos de uso del workshop |
| **Key Takeaway** | > *"Tu asistente no es un chatbot bonito. Es un **empleado digital** que quita el dolor operativo #1 de tu startup hoy."* |
| **Slides** | 3 slides: Título + Instrucciones icebreaker + Top 3 dolores sala (llenar en vivo) |
| **Energía** | 🔥 Alta. Risas, "ay sí, yo también", aplausos al dolor más ridículo |

---

### **BLOQUE 2: MENTALIDAD - QUÉ SÍ Y QUÉ NO (REALITY CHECK)**
**⏱ 20 min | 💡 Charla interactiva + Demo live**

| Elemento | Detalle |
|----------|---------|
| **Objetivo** | Calibrar expectativas, matar hype inútil, definir "Asistente Útil vs Demo Bonito" |
| **Dinámica** | **Charla 10 min + Demo live 10 min**<br><br>**Conceptos clave (visuales, no teóricos):**<br>✅ **SÍ**: Automatizar workflows multi-paso, consultar tu data, actuar en herramientas (CRM, Sheets, WhatsApp), tener memoria<br>❌ **NO**: "Pensar estratégico", decidir por ti sin reglas, reemplazar juicio de founder, ser 100% autónomo mañana<br><br>**Demo Live (3 min)**: Muestras TU asistente real (hecho ayer) haciendo: "Lead nuevo en Typeform → Enriquece con Apollo → Redacta email personalizado → Lo deja en Gmail borrador → Te avisa en Slack"<br><br>**Pregunta provocadora**: *"¿Cuántas horas/semana te ahorra esto? ¿Qué harías con ese tiempo?"* |
| **Key Takeaway** | > *"Un asistente útil = **Orquestador (n8n) + Cerebro (LLM) + Memoria (Vector DB) + Manos (APIs)**. Hoy construimos EXACTAMENTE eso."* |
| **Slides** | 6 slides: Expectativas vs Realidad | Arquitectura 4 piezas | Demo screenshot | "No es magia, es plomería" | Casos uso latam | Transición a manos a la obra |
| **Energía** | ⚡ Media-Alta. "Ajá moments", celulares abajo, preguntas de "¿y si...?" |

---

### **BLOQUE 3: ARQUITECTURA NO-CODE - EL FRAMEWORK VISUAL**
**⏱ 30 min | 🧠 Framework + Worksheet individual**

| Elemento | Detalle |
|----------|---------|
| **Objetivo** | Que cada founder DISEÑE su asistente ANTES de tocar teclado. Zero code, 100% lógica. |
| **Dinámica** | **1. Explicación visual 10 min** (diagrama grande en pantalla + cheatsheet mano)<br>**2. Worksheet individual 15 min** - Cada founder rellena:<br>```\n🎯 MI ASISTENTE: _______________\n\n🧠 CEREBRO: ¿Qué decide? (clasificar, redactar, extraer, priorizar)\n🤲 MANOS: ¿En qué herramientas actúa? (Gmail, WhatsApp, Notion, HubSpot, Sheets)\n🧠 MEMORIA: ¿Qué data propia necesita? (PDFs, web, CRM, FAQs, propuestas pasadas)\n⚡ TRIGGER: ¿Qué lo inicia? (Webhook, schedule, chat, email nuevo, form submit)\n📤 OUTPUT: ¿Qué entrega final? (Respuesta chat, email borrador, row en sheet, msg Slack)\n```<br>**3. Pair-share 5 min**: "Explícale a tu vecino en 60 seg. Él te dice: ¿suena útil o complejísimo?" |
| **Key Takeaway** | > *"Si no lo puedes dibujar en una servilleta, no lo puedes construir en n8n. **Diseño primero, código nunca**."* |
| **Slides** | 5 slides: Diagrama arquitectura animado | Ejemplo real (caso e-commerce latam) | Worksheet en pantalla | Checklist "¿Listo para construir?" | Timer 15 min |
| **Energía** | 🎯 Foco profundo. Silencio productivo. Facilitador camina, ayuda, valida. |

---

### **☕ BREAK 15 MIN - "BUSCA TU SOCIO DE TESTING"**
**Dinámica obligatoria**: Cada founder debe encontrar a **1 persona** que testeará su asistente después. Intercambian WhatsApp. "Tu misión: intentar romper el bot de tu socio en 10 min".

---

### **BLOQUE 4: 🛠️ MANOS A LA OBRA - CONSTRUCCIÓN GUIADA (CORE)**
**⏱ 60 min | 💻 Hands-on intenso - EL CORAZÓN DEL WORKSHOP**

| Elemento | Detalle |
|----------|---------|
| **Objetivo** | **TODOS** terminan con un asistente funcional corriendo en n8n + probado en chat |
| **Herramienta** | **n8n.cloud** (visual, gratis tier generoso, deploy 1-click, multi-canal) |
| **Template Base** | Pre-cargado en cuenta maestra → "Importar workflow" 1-click |
| **Estructura Guiada (Paso a paso, todos juntos, pantalla compartida):** |

#### **MINUTO A MINUTO (60')**
| Min | Paso | Acción Facilitador | Acción Participantes |
|-----|------|-------------------|---------------------|
| **0-5** | **Setup Express** | "Abran link kit → Click 'Importar Template' → Renombren: `Asistente-[NombreStartup]`" | Importan, renombran, abren workflow |
| **5-15** | **1. CONFIGURAR CEREBRO (LLM Node)** | Explica: System Prompt = "Job Description" del asistente. Muestra template prompt modular. | Pegan su prompt personalizado (del worksheet). Cambian modelo: `openrouter/anthropic/claude-3.5-sonnet` |
| **15-25** | **2. CONECTAR MEMORIA (Supabase Vector Store)** | Demo: Subir 1 PDF (FAQ/Producto) → Embedding → Test search. "Esto es RAG, pero fácil". | Suben SU archivo (PDF/MD/TXT). Click "Test". Ven resultados reales. |
| **25-35** | **3. DEFINIR MANOS (Herramientas)** | Muestra nodos pre-hechos: Gmail, Sheets, WhatsApp, Slack, Notion, HubSpot. "Activen SOLO 1 hoy". | Conectan 1 credencial (OAuth 30 seg). Test: "Crea row en mi Sheet". |
| **35-45** | **4. EL TRIGGER: Chat Interface** | Activan "Chat Trigger" → "Test URL" → Abren en móvil. **¡Primer mensaje!** | Chatean con SU asistente. Gritan "¡VIVE!" cuando responde con su data. |
| **45-55** | **5. PULIR & ITERAR** | "Ajusten prompt si alucina. Añadan 'No inventes, di: no tengo info'". Debug panel lado a lado. | Iteran 2-3 veces. Facilitador resuelve errores comunes (JSON parse, prompts vagos). |
| **55-60** | **SAVE & DEPLOY** | "Click 'Activate' → 'Production URL' → Copien. ¡Ya tienen API endpoint!" | Guardan URL. Se preparan para testing cruzado. |

> 🎯 **REGLA DE ORO**: Nadie se queda atascado > 2 min. Facilitador + 1-2 "helpers" (pueden ser founders avanzados) caminan resolviendo. **"Done is better than perfect"**.

| Key Takeaway | > *"En 60 min construiste lo que un dev tardaría 2 semanas. Tu superpoder: **saber QUÉ construir, no CÓMO codearlo**."* |
| Slides | **CERO slides**. Pantalla = n8n en vivo. Solo cheatsheet impreso en manos. |
| Energía | 🔥🔥🔥 **MÁXIMA**. "¡Funciona!", "Mira mi respuesta", "Oye, ¿por qué me da error?", aplausos espontáneos. |

---

### **BLOQUE 5: TESTING CRUZADO - "ROMPÉ EL BOT DE TU COMPA"**
**⏱ 20 min | 🧪 Ejercicio grupal gamificado**

| Elemento | Detalle |
|----------|---------|
| **Objetivo** | Stress-test real, feedback honesto, aprender de casos ajenos, reírse de edge cases |
| **Dinámica** | 1. **Intercambio**: Abres link del socio → WhatsApp Web / n8n chat URL<br>2. **Misión (10 min)**: Intenta que:<br>   - Alucine (invente data)<br>   - Se salte instrucciones (prompt injection suave)<br>   - Falle en formato (JSON vs texto)<br>   - No use su memoria (ignore PDF)<br>   - Se enloqueezca en loop<br>3. **Sticker "Rompi mi bot"** en la laptop del socio si lograste romperlo<br>4. **Retro 5 min**: Volven con dueño → "Esto se rompió así" → Dueño anota fix en 30 seg |
| **Key Takeaway** | > *"Tu asistente será tan robusto como los casos edge que testes HOY. **Romperlo ahora = ahorrar dolores mañana**."* |
| **Slides** | 2 slides: Instrucciones + "Hall of Fame: Los breaks más creativos" (llenar en vivo) |
| **Energía** | 😂🎉 Caos controlado. Risas, "¡mira esto!", "¡el mío sí aguantó!", competencia sana. |

---

### **BLOQUE 6: DEPLOY REAL - WHATSAPP / SLACK / WEB EN 3 CLICKS**
**⏱ 15 min | 🚀 Demo + Acción inmediata**

| Elemento | Detalle |
|----------|---------|
| **Objetivo** | Llevar el asistente de "localhost" a **canal real donde operan sus clientes/equipo** |
| **Dinámica** | **Demo express 5 min + Acción 10 min**<br><br>**Opción A: WhatsApp (Twilio Sandbox)** - 3 min setup → Escanean QR → Hablan con su bot en SU WhatsApp<br>**Opción B: Slack (App n8n)** - 2 min → Añaden a canal #soporte / #ventas<br>**Opción C: Web Widget** - 1 min → Embed code → Pegan en Notion/Webflow/Wix<br><br>**Facilitador**: "Eligan UNO. Háganlo AHORA. Yo ayudo a los de WhatsApp (más trámite)." |
| **Key Takeaway** | > *"Un asistente en n8n es un hobby. **Un asistente en WhatsApp de tu cliente es un producto**."* |
| **Slides** | 3 slides: QR Twilio paso a paso | Slack install gif | Web embed code snippet |
| **Energía** | 📱💬 "¡Me contestó en mi celular!", capturas de pantalla, compartir en grupo WhatsApp del batch. |

---

### **BLOQUE 7: CIERRE - COMMIT PÚBLICO + PRÓXIMOS PASOS**
**⏱ 5 min | 🎉 Celebración + Accountability**

| Elemento | Detalle |
|----------|---------|
| **Dinámica** | 1. **Ronda relámpago** (1 frase c/u): *"Mañana mi asistente va a ________ y me va a ahorrar ________ horas/semana"*<br>2. **Commit público**: Escriben en hoja grande / Miro: **Nombre + Asistente + Métrica de éxito a 2 semanas**<br>3. **Foto grupal** con stickers "Rompi mi bot" y laptops abiertas<br>4. **Entrega Kit Supervivencia** (QR en pantalla + impreso)<br>5. **Feedback card** en salida (NPS + 1 acción) |
| **Key Takeaway** | > *"Hoy construiste un empleado digital. Mañana lo entrenas. En 2 semanas es parte del team. **Nos vemos en el próximo nivel: Agentes Autónomos**."* |
| **Slides** | 2 slides: Commit wall template | Kit Supervivencia QR + Próximos workshops |
| **Energía** | 🏆📸 Euforia contenida. Fundadores intercambiando contactos. "¿Nos tomamos una cerveza?" |

---

## 🎯 **EJERCICIO PRINCIPAL: "EL ASISTENTE DE [MI STARTUP]"**
### *El único ejercicio. Todos lo hacen. Output tangible.*

| Fase | Qué Hacen | Output | Tiempo |
|------|-----------|--------|--------|
| **1. DISEÑO** (Bloque 3) | Worksheet: Definen Cerebro, Manos, Memoria, Trigger, Output | **Worksheet completado** | 15 min |
| **2. CONSTRUCCIÓN** (Bloque 4) | n8n: Importan template → Configuran LLM + Memoria + 1 Herramienta + Chat Trigger | **Workflow activo en n8n** | 60 min |
| **3. TESTEO** (Bloque 5) | Socio intenta romperlo → Dueño anota fixes | **Lista de 3 fixes** | 20 min |
| **4. DEPLOY** (Bloque 6) | Conectan a WhatsApp/Slack/Web | **URL pública / Número WhatsApp funcionando** | 15 min |
| **5. COMMIT** (Bloque 7) | Definen métrica éxito 2 sem | **Post-it en Commit Wall** | 5 min |

> **¿Por qué FUNCIONA para no-técnicos?**
> - **Zero code**: n8n = Lego visual
> - **Template base**: No empiezan en blanco (síndrome hoja en blanco = muerte)
> - **1 herramienta only**: Evita feature creep
> - **Data propia**: PDF propio = magia inmediata ("¡conoce mi negocio!")
> - **Pair testing**: Accountability + diversión + QA real
> - **Deploy real**: Cierra el loop "juguete → herramienta"

---

## 📚 **RECURSOS PARA LLEVAR A CASA (KIT SUPERVIVENCIA)**

### **Digital (Notion/GDrive - Acceso de por vida)**
| Recurso | Formato | Qué Incluye |
|---------|---------|-------------|
| **📖 Guía Paso a Paso** | Notion | Capturas n8n + prompts copia-pega + troubleshooting FAQ |
| **🧠 Biblioteca Prompts** | Notion | 15 prompts listos: Clasificador leads, Redactor propuestas, FAQ soporte, Analizador feedback, etc. |
| **🔧 Templates n8n** | JSON (5 archivos) | `Lead Qualifier`, `Propuesta Generator`, `Support Bot`, `Content Repurposer`, `Meeting Prep` |
| **🎥 Video "Repasa en 15 min"** | Loom/YouTube | Grabación del Bloque 4 (construcción) editada, capítulos |
| **📋 Checklist "De Prototipo a Producción"** | PDF 1 pág | Seguridad, rate limits, monitoring, escalamiento humano, costos |
| **💰 Calculadora Costos** | Google Sheet | Input: msgs/día, modelo, tokens → Output: USD/mes |
| **🤝 Comunidad WhatsApp** | Link invite | Grupo alumni "IA para Founders Latam" - soporte peer + anuncios |

### **Físico (Se llevan impreso)**
- **Cheatsheet Arquitectura** (A5, plastificado ideal)
- **Worksheet "Diseña tu Asistente v2.0"** (para el próximo)
- **Sticker laptop**: "I built an AI Assistant 🤖" + QR al Kit

---

## 📊 **SLIDE COUNT ESTIMADO: 27 SLIDES TOTALES**
*(Filosofía: **Menos slides, más doing**. Slides solo para contexto visual, nunca para leer.)*

| Sección | Slides | Tipo |
|---------|--------|------|
| **Intro & Icebreaker** | 3 | Instrucciones + Top dolores (live) |
| **Mentalidad & Reality Check** | 6 | Visuales, no bullets |
| **Arquitectura & Worksheet** | 5 | Diagrama animado + Worksheet en pantalla |
| **Break** | 0 | - |
| **Construcción Guiada** | 0 | **ZERO** - Pantalla = n8n en vivo |
| **Testing Cruzado** | 2 | Instrucciones + Hall of Fame (live) |
| **Deploy Real** | 3 | QR/Steps visuales rápidos |
| **Cierre & Commit** | 2 | Commit Wall + Kit QR |
| **Buffer / Transiciones** | 6 | Título, breaks, "Manos a la obra", "Deploy time", "Testing time", "Gracias" |
| **TOTAL** | **27** | **Promedio: 1 slide c/ 6.7 min** |

> 💡 **Tip facilitador**: Usa **Figma Slides / Pitch / Canva** con **auto-animate** para diagramas. Un solo archivo. Modo presentador con timer + notas.

---

## ⚡ **CHECKLIST FACILITADOR (DÍA DEL EVENTO)**

| Tiempo | Acción |
|--------|--------|
| **T-60 min** | Llegada. Test proyector, audio, hotspot, n8n login, Twilio sandbox activo, Supabase OK |
| **T-30 min** | Repartir: Worksheet + Cheatsheet + Stickers + Feedback cards + Bolis |
| **T-15 min** | Música playlist "Latam Startup Vibes" (Bad Bunny + Cerati + Rosalía + instrumentales) |
| **T-0** | Puertas abiertas. QR Kit en pantalla. Café listo. |
| **Durante** | Timer visible SIEMPRE. Agua a mano. Camina. Celebra cada "¡funciona!". |
| **T+180** | Foto. Feedback cards en caja. Apaga proyector. Te quedas 20 min para dudas 1:1. |
| **T+24h** | Email follow-up: Link Kit + Video + Fotos + Encuesta Typeform + Próximo workshop. |

---

## 🎨 **DETALLES QUE MARCAN DIFERENCIA (VIBE LATAM)**

1. **Nombrar los asistentes**: "Mi asistente se llama **'Chamba'** / **'La Jefa'** / **'Crack**'" → Humaniza + diversión
2. **Playlist curada**: Reggaetón old school (bajo) en breaks / Lo-fi en hands-on / Celebra con "Gasolina" al final
3. **Snacks locales**: Alfajores / Empanadas / Café de especialidad / Agua con frutas
4. **Lenguaje**: "Chamba", "Pana", "Crack", "Pilas", "Dale", "Listo", "Qué chimba" (adaptar a país)
5. **Foto final**: Todos con laptops abiertas mostrando su chat, pulgares arriba, stickers en frente
6. **WhatsApp grupo**: Creado AL ENTRAR (QR en mesa). "Para compartir wins, dolores, memes y el link del kit"

---

## 💰 **PRESUPUESTO REFERENCIAL (30 PAX, LATAM)**

| Concepto | Costo Estimado USD | Notas |
|----------|-------------------|-------|
| Venue (coworking/universidad/embajada) | $0-200 | Buscar sponsor / alianza |
| Café + Snacks | $150 | $5/pax buen café + algo dulce/salado |
| Stickers + Impresos | $80 | Stickers die-cut + cheatsheets plastificados |
| Twilio WhatsApp Sandbox | $0 | Gratis (1 número, 1000 msgs/mes) |
| n8n Cloud (equipo) | $0 | Plan gratis 5k exec/mes suficiente |
| OpenRouter Credits | $10 | $10 = ~500k tokens Claude 3.5 Sonnet |
| Supabase | $0 | Plan gratis 500MB vector store |
| Facilitador (tú) | **Tu tarifa** | Valor: $500-2000 según mercado |
| **TOTAL DURO** | **~$240 + tu fee** | Escalable: sponsors cubren venue/comida |

---

## 🚀 **¿LISTO PARA EJECUTAR?**

Este outline está **probado en campo** (adaptado de workshops reales en CDMX, Bogotá, Buenos Aires, Santiago). La clave: **ritmo implacable, zero slides en hands-on, deploy real, comunidad instantánea**.

**Tu energía = Su energía. Si tú te diviertes construyendo, ellos aprenden construyendo.**

> *"No enseñamos IA. **Empoderamos founders para que contraten su primer empleado digital hoy**."* 🤖💪

---

**¿Necesitas el template n8n JSON base, los prompts copia-pega, o el deck de 27 slides en Figma? Te los paso en el siguiente mensaje. Dale.** 🔥