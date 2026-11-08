# Kimi K2.5 — startup_content/workshop_outline

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 7.87 | quality: 9.72
- latency_total: 245.593s | tokens_per_second: 24.5
- input_tokens: 219 | output_tokens: 6026
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

# 🤖 CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP
## Workshop Práctico | Outline Completo

---

## 1. AGENDA DETALLADA (3 HORAS)

| Tiempo | Bloque | Duración |
|--------|--------|----------|
| 0:00 - 0:20 | 🔥 Apertura: El emprendedor que no codea ya no existe | 20 min |
| 0:20 - 0:50 | 💡 Bloque 1: Mapea tu dolor, no elijas la herramienta primero | 30 min |
| 0:50 - 1:20 | ⚡ BREAK + Networking rápido | 30 min |
| 1:20 - 2:00 | 🛠️ Bloque 2: Construye tu primer asistente (manos en la masa) | 40 min |
| 2:00 - 2:30 | 🧪 Bloque 3: Itera con prompts y conecta con tu operación real | 30 min |
| 2:30 - 2:50 | 🚀 Bloque 4: Tu roadmap de IA para los próximos 30 días | 20 min |
| 2:50 - 3:00 | 🎯 Cierre + Compromisos públicos | 10 min |

---

## 2. MATERIALES NECESARIOS (PRE-WORKSHOP)

### Para el facilitador:
| Ítem | Especificaciones |
|------|----------------|
| Proyector + pantalla grande | Mínimo 1080p, visible desde atrás |
| Micrófono inalámbrico (si sala >15 personas) | Para moverse entre mesas |
| 2-3 extensiones + zapatillas eléctricas | Cargadores de laptops |
| Flipchart o pizarra + marcadores | Para capturar preguntas en vivo |
| Timer visible para todos | Proyectado o físico grande |
| Spotify lista "focus beats" | Para momento de trabajo individual |
| Stickers de colores (3 colores) | Para votación rápida |

### Para cada participante (preparar antes):
| Ítem | Cantidad | Notas |
|------|----------|-------|
| Laptop con WiFi estable | 1 por persona | **OBLIGATORIO** - avisar 3 días antes |
| Cuenta de OpenAI/ChatGPT (gratis) | 1 | Crear antes del workshop |
| Cuenta de Make.com (gratis) | 1 | Crear antes del workshop |
| Cuenta de Google (Gmail) | 1 | Para Sheets/Forms si no la tienen |
| Plantilla "Mi Asistente IA" (Notion/Google Docs) | 1 link | Enviar 24h antes |
| Hoja de trabajo impresa | 2 por persona | Backup si falla internet |

### Para la sala:
- Mesas de 4-5 personas máximo (no auditorio)
- Conexión WiFi que aguante 30 personas simultáneas
- Café + agua + algo dulce (no almuerzo pesado, es 3 horas)

---

## 3. BLOQUES DETALLADOS

---

### 🔥 APERTURA: El emprendedor que no codea ya no existe
**Duración:** 20 min | **Slides:** 8 | **Dinámica:** Charla energética + interacción inicial

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Romper el miedo técnico, establecer que "no-code + IA" = superpoder para emprendedores, crear energía de sala |
| **Dinámica** | Charla rápida (10 min) + "Levanta la mano si..." (3 preguntas) + Compromiso de la sala (2 min) + Presentación de ejemplos reales de founders latinos (5 min) |
| **Actividad clave** | *"Levanta la mano si..."* — ¿Te despiertas respondiendo WhatsApp? ¿Tienes un proceso que explicas 10 veces al día? ¿Pagaste +$500 por algo que ahora dices 'lo pudo haber hecho una IA'? |
| **Key Takeaway** | *"No viniste a aprender IA. Viniste a resolver un cuello de botella que te está costando dinero o sueño. La IA es el cómo, no el qué."* |

**Slides (8):**
1. Título impacto + foto de founder latino con su asistente IA
2. "Hace 2 años necesitabas un dev. Hoy necesitas 40 minutos y claridad"
3. 3 ejemplos antes/después (con logos reales): fintech mexicana, e-commerce colombiano, servicio profesional argentino
4. El mito del "emprendedor técnico" vs. la realidad del "emprendedor que orquesta"
5. Lo que NO vamos a hacer (no codeamos, no vemos teoría de ML, no hablamos de API)
6. Lo que SÍ vamos a hacer (todos se van con un asistente funcionando)
7. Reglas de la sala: pregunta en cualquier momento, "no entiendo" es la frase más valiosa, ayuda al de al lado
8. Agenda visual con emoji por bloque

---

### 💡 BLOQUE 1: Mapea tu dolor, no elijas la herramienta primero
**Duración:** 30 min | **Slides:** 6 | **Dinámica:** Ejercicio individual + compartir en parejas + votación grupal

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Cada participante identifica EL proceso específico que su asistente automatizará (no aprender "IA en general") |
| **Dinámica** | Mini-charla (8 min) → Ejercicio individual con hoja de trabajo (10 min) → Parejas: pitch de 1 minuto cada uno (8 min) → 3-4 personas comparten con sala + feedback rápido (4 min) |
| **Key Takeaway** | *"El 80% de los asistentes de IA fallan porque intentan hacer todo. El tuyo va a hacer UNA cosa muy bien definida."* |

**Ejercicio: "El Triángulo del Dolor"** (hoja de trabajo)

```
PASO 1: Lista 3 tareas que haces más de 5 veces por semana
        1. _________________________
        2. _________________________  
        3. _________________________

PASO 2: Para cada una, puntúa (1-5):
        - ¿Me quita energía? (1 = me divierte, 5 = me drena)
        - ¿La hago cuando debería estar en otra cosa? (estrategia, ventas, familia)
        - ¿Es predecible? (sigo pasos similares siempre)

PASO 3: Elige LA ÚNICA que tenga mayor puntaje. Escribe:
        "Mi asistente va a: _________________________"
        "Para: _________________________" (¿quién se beneficia? cliente, equipo, yo)
        "Cuando: _________________________" (¿qué lo activa?)

PASO 4: El "antes y después" de tu viernes:
        ANTES: Yo hago ______ → ______ → ______ (30 min)
        DESPUÉS: La IA hace ______ → Yo solo reviso ______ (5 min)
```

**Slides (6):**
1. "La trampa: empezar por la herramienta" (imagen de alguien perdido en 50 logos de IA)
2. Framework: "Dolor frecuente + predecible + te quita de lo importante = candidato perfecto"
3. Ejemplo paso a paso: founder de delivery que eligió "responder dudas de repartidores nuevos" (no "automatizar todo")
4. Instrucciones del ejercicio con timer visible
5. Criterios de "buena elección" vs. "mala elección" (checklist visual)
6. "Tu asistente tiene nombre: '[Tarea] + para + [quién]'" — ejemplos de la sala en tiempo real si es posible

---

### ⚡ BREAK + NETWORKING RÁPIDO
**Duración:** 30 min | **Slides:** 1 (timer) | **Dinámica:** Networking estructurado + café

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Descanso real + que conozcan a alguien que resuelva un dolor similar + resolver problemas técnicos de login |
| **Dinámica** | "Speed dating de dolores": 3 rondas de 3 minutos. En cada ronda, comparten su "Mi asistente va a..." y dan un tip o reciben uno. Facilitador circula resolviendo problemas de cuentas. |
| **Key Takeaway** | *"Tu 'competidor' de la mesa de al lado puede ser tu beta tester de prompts."* |

**Instrucciones proyectadas:**
```
RONDA 1 (3 min): Comparte tu elección. ¿Coinciden en el tipo de tarea?
RONDA 2 (3 min): ¿Qué información necesita tu asistente? ¿Dónde está ahora?
RONDA 3 (3 min): Intercambia contactos si quieren testear los asistentes del otro.
```

Facilitador y 1 ayudante técnico resuelven: cuentas de OpenAI, Make.com, problemas de WiFi.

---

### 🛠️ BLOQUE 2: Construye tu primer asistente (manos en la masa)
**Duración:** 40 min | **Slides:** 10 | **Dinámica:** Demo en vivo + trabajo guiado + asistencia de mesa

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Cada participante tiene funcionando un asistente básico que responda algo útil para su caso específico |
| **Dinámica** | Demo del facilitador (10 min, proyectado paso a paso) → Trabajo guiado con checklist en pantalla (25 min) → 3-5 personas comparten su asistente funcionando (5 min) |
| **Key Takeaway** | *"Tu primer asistente no es perfecto. Es real. Y ya te ahorró más tiempo que leer 10 artículos sobre IA."* |

**Demo en vivo: El "Asistente de Onboarding de Cliente" (ejemplo genérico adaptable)**

Plataforma: **ChatGPT (GPTs)** o **Make.com + OpenAI** según complejidad del grupo

**Opción A (más simple): Crear un GPT personalizado**
1. Ir a chat.openai.com → "Explore GPTs" → "Create"
2. Nombre: "Onboarding [NombreStartup]"
3. Instrucciones: "Eres el especialista de onboarding. Tu trabajo es..." (plantilla dada)
4. Subir documento: FAQ, proceso, tono de voz (PDF)
5. Probar con pregunta real
6. Guardar + copiar link para compartir

**Opción B (más poderoso): Make.com + OpenAI + Google Sheets**
1. Google Sheet con: Pregunta frecuente | Respuesta ideal | Categoría
2. Make.com: Trigger (nuevo row o webhook) → OpenAI module → respuesta generada → enviar a (email/Slack/Guardar en sheet)
3. Test con datos reales del participante

**Checklist proyectada durante trabajo:**
```
□ Tengo abierta mi cuenta de OpenAI/Make
□ Elegí mi opción A o B (pregunta al facilitador si dudas)
□ Mi asistente tiene nombre relacionado a MI tarea, no genérico
□ Escribí las instrucciones base (mínimo 3 líneas de contexto)
□ Agregué al menos 1 ejemplo real de mi operación
□ LO PROBÉ con una pregunta/situación real de esta semana
□ Funcionó o sé QUÉ ajustar (no me rindo si la primera no sale)
```

**Slides (10):**
1. "Manos en la masa - silencio de focus en 3, 2, 1" (timer grande)
2. Opción A vs. Opción B: ¿Cuál te va mejor? (árbol de decisión simple)
3. Demo paso 1: Crear/entrar (screenshot real, no genérico)
4. Demo paso 2: Las instrucciones = el 80% del éxito (antes/después de mal vs. buen prompt)
5. Demo paso 3: Darle contexto específico (subir doc vs. pegar texto)
6. Demo paso 4: Prueba y el arte de "esto no salió, ajusto"
7. Plantilla de instrucciones (screenshot grande, legible)
8. Timer de trabajo: 25 minutos (con música de fondo)
9. "¿Atascado?" 3 problemas comunes y solución rápida
10. "Showtime": ¿Quién quiere mostrar su asistente? (premio: sticker o mención honorífica)

---

### 🧪 BLOQUE 3: Itera con prompts y conecta con tu operación real
**Duración:** 30 min | **Slides:** 7 | **Dinámica:** Ejercicio de mejora + demo avanzada + plan de conexión

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Pasar de "funciona" a "funciona COMO YO quiero" + entender cómo conectarlo al flujo real de trabajo |
| **Dinámica** | Mini-charla sobre iteración de prompts (5 min) → Ejercicio: "Mejora tu prompt en 3 rounds" (15 min) → Demo: Cómo conectarlo a WhatsApp/email/Slack sin código (7 min) → Compromiso de conexión (3 min) |
| **Key Takeaway** | *"Un asistente bueno es 10% tecnología, 90% saber qué le pedís y cómo le corregís."* |

**Ejercicio: "El Challenge de los 3 Prompts"**

```
ROUND 1 (5 min): Probá tu asistente con la pregunta MÁS DIFÍCIL que te hicieron este mes.
¿Qué falló? Escribí: "Quiero que en vez de _____, haga _____"

ROUND 2 (5 min): Ajustá las instrucciones. Probá de nuevo.
¿Mejoró en lo que querías? ¿Empeoró en algo que antes funcionaba?
Escribí: "Mantener _____, cambiar _____"

ROUND 3 (5 min): Agregá una restricción específica de tu negocio.
Ejemplo: "Nunca ofrezcas descuento sin que me consultes" / 
"Si no sabés, decí 'voy a confirmar con [Nombre]' en vez de inventar"
```

**Demo avanzada (para quienes quieran más):**
- Make.com → WhatsApp Business API (via Twilio o Wati)
- Make.com → enviar email con respuesta generada
- ChatGPT → compartir link del GPT con equipo/cliente

**Slides (7):**
1. "Tu asistente ahora funciona. El 90% restante es iteración."
2. Los 3 errores de prompt: vago (hazme un resumen), asume contexto (como siempre), no define tono (formal/casual)
3. Fórmula del buen prompt: Rol + Contexto + Tarea + Formato + Restricción (ejemplo antes/después)
4. Instrucciones del challenge de 3 rounds con timer
5. "Conectar = donde la magia multiplica" (diagrama: IA aislada vs. IA en tu flujo)
6. Opciones de conexión sin código (logos: WhatsApp, Email, Slack, Notion, Sheets)
7. "Tu compromiso de esta semana": escribir en post-it y pegar en laptop

---

### 🚀 BLOQUE 4: Tu roadmap de IA para los próximos 30 días
**Duración:** 20 min | **Slides:** 5 | **Dinámica:** Charla + ejercicio de planificación + compromisos públicos

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Evitar que el asistente quede abandonado; crear plan realista de expansión; establecer comunidad de seguimiento |
| **Dinámica** | Charla de expansiones posibles (7 min) → Ejercicio: "Semana 1, 2, 3, 4" en hoja (8 min) → Compromisos públicos en voz alta (5 min) |
| **Key Takeaway** | *"El que construye 1 asistente perfecto le gana al que planea 10. Pero el que tiene plan de los próximos 3 le gana al que se queda con 1."* |

**Ejercicio: "Mi Mes IA"**

```
SEMANA 1: Pulir
□ Mi asistente responde correctamente 8/10 veces en pruebas
□ Alguien más (socio, cliente, empleado) lo probó y dio feedback
□ Ajusté el tono para que suene como mi marca

SEMANA 2: Conectar
□ Mi asistente está donde necesito usarlo (WhatsApp, email, etc.)
□ Ya no entro a ChatGPT/Make para usarlo; llega a mí
□ Medí: ¿cuánto tiempo me ahorró esta semana? (aprox)

SEMANA 3: Delegar
□ Alguien más de mi equipo usa el asistente sin preguntarme
□ Documenté cómo usarlo en 1 página
□ Identifiqué el SIGUIENTE proceso para automatizar

SEMANA 4: Escalar
□ Tengo 2 asistentes o 1 más complejo
□ Compartí mi experiencia con 1 emprendedor (networking da asimetrías)
□ Decidí: ¿contrato alguien para esto o sigo solo con no-code?
```

**Slides (5):**
1. "Hoy construiste el primer piso. El edificio se construye en 30 días."
2. Las 3 expansiones: más preciso → más conectado → más procesos (diagrama)
3. Plantilla "Mi Mes IA" (screenshot legible)
4. "El error que mata asistentes: perfeccionismo eterno sin conectar"
5. Comunidad y recursos: dónde seguir, quién preguntar, próximo workshop

---

### 🎯 CIERRE: Compromisos públicos
**Duración:** 10 min | **Slides:** 2 | **Dinámica:** Ritual de cierre + foto grupal + encuesta rápida

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Energía de cierre alto; capturar aprendizajes; iniciar relación post-workshop |
| **Dinámica** | 3-5 voluntarios: "Mi asistente se llama ___, hace ___, y esta semana voy a ___" (5 min) → Foto grupal con laptops mostrando asistentes (2 min) → Encuesta 1 minuto (QR en pantalla) (3 min) |
| **Key Takeaway** | *"El workshop termina hoy. Tu asistente empieza mañana. El grupo sigue."* |

**Slides (2):**
1. "El momento de la verdad: ¿quién se anima?" (fondo con aplausos)
2. QR a encuesta + link a recursos + foto grupal

---

## 4. EJERCICIO PRINCIPAL DEL WORKSHOP

### 🏆 "MI PRIMER ASISTENTE EN 25 MINUTOS"

**Descripción:** Cada participante construye un asistente funcional usando ChatGPT (GPT personalizado) o Make.com + OpenAI, según su caso específico elegido en el Bloque 1.

**Por qué funciona para no-técnicos:**
- No se escribe código
- La interfaz es conversacional (como WhatsApp)
- El "error" es visible inmediatamente y corregible
- El resultado es tangible (un link, una respuesta real)

**Flujo del ejercicio:**

| Fase | Qué hace el participante | Qué hace el facilitador |
|------|--------------------------|------------------------|
| Preparación (5 min) | Abre cuentas, revisa su hoja "Triángulo del Dolor" | Circula, resuelve problemas de login, da ánimos |
| Construcción (15 min) | Sigue checklist paso a paso, prueba, ajusta | Circula mesa por mesa, no espera que levanten la mano, identifica quién puede ser "ayudante de mesa" |
| Validación (5 min) | Prueba con caso real de su semana | Pide 3 voluntarios para mostrar en pantalla grande |

**Criterio de éxito mínimo:** El asistente responde coherente y útil a UNA pregunta real del negocio del participante.

**Criterio de éxito stretch:** El asistente tiene nombre propio, tono definido, y el participante sabe cómo mejorarlo esta semana.

---

## 5. RECURSOS PARA LLEVAR A CASA

### 📦 Kit digital (enviar por email 2 horas después del workshop)

| Recurso | Formato | Descripción |
|---------|---------|-------------|
| **Guía "Mi Asistente IA: de 0 a funcional"** | PDF (15 páginas, diseñado) | Repaso de todo el workshop con screenshots paso a paso |
| **Plantilla de instrucciones para GPTs** | Google Doc editable | 5 plantillas según tipo de asistente: atención al cliente, contenido, análisis de datos, coaching interno, creatividad |
| **Biblioteca de 20 prompts probados para founders** | Notion/Google Sheets | Categorizados por: ventas, operaciones, marketing, finanzas, equipo |
| **Video de la demo en vivo** | Loom/YouTube privado | Grabación de 10 min del facilitador haciendo el paso a paso |
| **Checklist "Mi Mes IA"** | PDF + versión Notion | Para seguimiento semana a semana |
| **Directorio de herramientas no-code** | Google Sheet | Comparativa: qué hace, cuánto cuesta, cuándo usarla, alternativa gratis |
| **Acceso a comunidad/grupo** | WhatsApp/Discord/Slack | Con reglas: solo preguntas específicas, no teoría; "mostrá tu asistente" los viernes |

### 🎁 Bonus para los que completan la encuesta:
- **Prompt de "Revisión de pitch"**: copiar tu pitch, la IA te da 5 mejoras específicas
- **Plantilla de "Análisis de competidor con IA"**: estructura para que la IA analice landing pages de competidores

---

## 6. SLIDE COUNT ESTIMADO

| Sección | Slides | Notas de diseño |
|---------|--------|-----------------|
| Apertura | 8 | Alta energía visual, mucho blanco, poco texto, fotos reales |
| Bloque 1: Mapea tu dolor | 6 | Diagramas simples, hoja de trabajo en pantalla al final |
| Break | 1 | Solo timer grande, sin distracción |
| Bloque 2: Construcción | 10 | Screenshots reales, no genéricos; checklist visible durante trabajo |
| Bloque 3: Iteración | 7 | Fórmulas visuales, ejemplos de prompts antes/después |
| Bloque 4: Roadmap | 5 | Plantilla semanal, inspiración no abrumo |
| Cierre | 2 | QR grande, foto grupal |
| **TOTAL** | **39 slides** | ~20% con animación simple, optimizado para proyección no para leer offline |

---

## 💡 NOTAS DEL FACILITADOR (EXTRA)

### Para manejar el "no soy técnico":
- Nunca digas "es fácil". Dí "es posible, y te muestro cómo".
- Cuando alguien dice "no me sale", responde "¿en qué paso estás? Veamos juntos" (no "intenta de nuevo").
- Celebra públicamente los "casi funciona" igual que los "funciona perfecto".

### Para la energía de 3 horas:
- Minuto 60-70: bajón natural. El break debe ser REAL, no "5 minutos para ir al baño".
- Minuto 100: si la mitad tiene asistente funcionando, la energía se contagia. Si no, parar y resolver en grupo.

### Para Latinoamérica específico:
- Mencionar casos de México, Colombia, Argentina, Chile (no solo Silicon Valley).
- Asumir que algunos no tienen tarjeta de crédito para pagar herramientas: siempre dar alternativa gratis.
- El WhatsApp es el canal central de la región: enfatizar conexión a WhatsApp Business como "premio" del roadmap.

---

¿Querés que desarrolle alguna sección con más profundidad? Por ejemplo: la guía paso a paso de la demo en vivo, las plantillas de prompts específicas por industria, o el diseño de la encuesta post-workshop.