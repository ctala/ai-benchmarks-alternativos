# Claude Sonnet 4.6 (suscripción) — startup_content/workshop_outline

- model_id: `claude-sonnet-4-6`
- success: True  | final: 6.93 | quality: 9.72
- latency_total: 158.634s | tokens_per_second: 52.5
- input_tokens: 3 | output_tokens: 8330
- judge_score: 4.8 | justificación: 

## Respuesta completa

# 🚀 WORKSHOP: "Construye tu Asistente de IA para tu Startup"
## Outline Completo — Workshop Presencial 3 Horas

---

## 📋 RESUMEN EJECUTIVO

| Elemento | Detalle |
|---|---|
| **Duración total** | 3 horas (180 min) |
| **Audiencia** | 20–30 emprendedores early-stage, no técnicos |
| **Formato** | Presencial + Ejercicio hands-on |
| **Herramienta principal** | Claude.ai Projects o ChatGPT Custom GPTs (sin código) |
| **Resultado concreto** | Cada participante sale con un asistente IA funcionando para su startup |
| **Slides totales estimados** | 45–52 slides |

---

## 🛠️ MATERIALES — PREPARAR ANTES DEL WORKSHOP

### Para el facilitador
- [ ] Proyector + pantalla (o TV grande)
- [ ] Adaptadores HDMI/USB-C (siempre hay uno que falta)
- [ ] Micrófono si hay >20 personas
- [ ] Whiteboard o papelógrafo + plumones de colores
- [ ] Timer visible (app en pantalla secundaria o timer físico)
- [ ] Tu propio asistente de IA ya construido y testeado como demo en vivo
- [ ] 3 demos de asistentes distintos preparados (startup de contenido, e-commerce, servicios B2B)

### Para los participantes
- [ ] **Ficha de trabajo impresa** (1 por persona) — ver Sección 5
- [ ] Post-its amarillos y azules (1 block por mesa)
- [ ] Marcadores (1 por persona)
- [ ] WiFi funcional con contraseña en la pizarra desde antes
- [ ] QR code impreso en cada mesa → lleva a doc compartido con recursos
- [ ] Cuenta en Claude.ai o ChatGPT ya creada (enviar recordatorio 24h antes por email)
- [ ] Agua y snacks visibles (energía física = energía mental)

### Comunicación previa (enviar 48h antes)
```
Asunto: Prepárate para el workshop — 2 pasos rápidos

1. Crea cuenta gratis en claude.ai (o chatgpt.com si ya tienes)
2. Trae en mente: ¿cuál es la tarea repetitiva que más tiempo te roba cada semana?

Nos vemos el [fecha]. Trae laptop o tablet cargada.
```

---

## ⏱️ AGENDA DETALLADA

```
00:00 ─── Apertura y Energía                    10 min
00:10 ─── Bloque 1: El Problema Real            20 min
00:30 ─── Bloque 2: Qué Puede Hacer la IA       25 min
00:55 ─── Bloque 3: Diseña tu Asistente         25 min
01:20 ─── ☕ BREAK                              10 min
01:30 ─── Bloque 4: CONSTRUCCIÓN (core)         50 min
02:20 ─── Bloque 5: Test + Iteración            20 min
02:40 ─── Bloque 6: Próximos Pasos              15 min
02:55 ─── Bloque 7: Showcase + Cierre            5 min
03:00 ─── FIN
```

---

## 🎯 BLOQUES DETALLADOS

---

### 🟡 APERTURA — "El ambiente que define todo"
**⏱ Duración:** 10 minutos
**📍 Slides:** 3

**Objetivo:**
Romper el hielo, establecer tono energético y no académico, y calibrar el nivel del grupo.

**Dinámica:**
> Mientras la gente entra, suena música (playlist energética, nada de música de meditación). En el proyector: una sola pregunta gigante:
> **"¿Cuántas horas a la semana pierdes en tareas que odias hacer?"**

Cuando hay quorum (~80%), paras la música y preguntas en voz alta. Pedís que levanten la mano:
- "¿Más de 5 horas?" → contás en voz alta
- "¿Más de 10 horas?" → reacción dramática
- "¿Más de 20 horas? Hermano, necesitás esto más que nadie acá."

Luego la regla del workshop en 10 segundos:
> *"Hoy no hay teoría. Cada bloque termina con algo que se hace, no algo que se aprende. Si en algún momento no entendés algo, levantá la mano — no hay preguntas tontas, hay preguntas que otros 15 no tuvieron los cojones de hacer."*

**Key takeaway:** El workshop es diferente. No es clase. Hay permiso para equivocarse.

---

### 🔴 BLOQUE 1 — "Tu startup tiene un problema que no sabe que tiene"
**⏱ Duración:** 20 minutos
**📍 Slides:** 6–8

**Objetivo:**
Hacer que cada participante identifique su mayor problema operacional antes de ver soluciones. El diagnóstico primero.

**Dinámica: El Mapa de Dolor (10 min ejercicio individual)**

Entregas la **Ficha de Trabajo** y decís:
> *"Tenés 3 minutos. Anotá las 5 tareas que más tiempo te roban cada semana. No filtres. No pienses si son importantes. Solo anotá."*

Timer visible en pantalla. Silencio absoluto.

Luego: rotación en parejas (2 min) — cada uno le cuenta al de al lado su lista.

Facilitador recorre el salón, escucha, anota en el whiteboard las categorías que aparecen (suelen ser siempre: emails, contenido, research, atención a clientes, reportes, propuestas). Esas categorías en el pizarrón van a ser el hilo conductor del resto del workshop.

**Charla corta (10 min):** Mostrar el dato real:
- Emprendedor promedio early-stage: 60% del tiempo en tareas de ejecución repetitiva
- Solo 40% en estrategia y producto
- Slide de impacto: *"Un asistente bien configurado no te reemplaza. Te clona en las partes aburridas."*

Mostrar brevemente (sin entrar en detalle) 3 casos reales latinoamericanos:
1. E-commerce chileno que automatizó respuesta a consultas (de 4h/día → 20 min de revisión)
2. Consultora colombiana que genera propuestas en 15 min (antes: 3 horas)
3. Newsletter en México con 3.000 suscriptores, 1 persona, sin agencia

**Key takeaway:** El problema no es la IA. El problema es que todavía no sabés exactamente qué pedirle.

---

### 🟠 BLOQUE 2 — "Qué puede hacer la IA por tu startup (sin mentirte)"
**⏱ Duración:** 25 minutos
**📍 Slides:** 10–12

**Objetivo:**
Calibrar expectativas reales. Ni "la IA lo hace todo" ni "es puro hype". Mostrar el rango real de usos para early-stage.

**Dinámica: Demo en vivo (15 min)**

Tres demos cortos y concretos. Sin preparación aparente (aunque están preparados):

**Demo 1 — Contenido (5 min)**
> *"Tomemos el negocio de alguien acá."*
Pedís voluntario. Preguntás: ¿Qué vendés? Escribís en tiempo real un prompt y mostrás cómo el asistente genera un post de LinkedIn, email de prospección y FAQ del producto. En vivo.

**Demo 2 — Atención al cliente (5 min)**
> *"¿Cuántos de ustedes responden las mismas 10 preguntas por WhatsApp todos los días?"*
Mostrás cómo un asistente entrenado con la info del producto responde preguntas de clientes con contexto real.

**Demo 3 — Research y análisis (5 min)**
Pegás un artículo o documento. El asistente lo resume, extrae insights y genera preguntas estratégicas. "Eso habría tardado 45 minutos."

**Charla corta (10 min): El semáforo de la IA**
Usás un slide con semáforo:

| 🟢 VERDE — La IA clava | 🟡 AMARILLO — Revisión humana | 🔴 ROJO — Humano siempre |
|---|---|---|
| Redactar, resumir, estructurar | Análisis financiero crítico | Decisiones estratégicas |
| Responder preguntas frecuentes | Contenido con datos propios | Relaciones con clientes VIP |
| Generar opciones y borradores | Research con fuentes nuevas | Negociaciones importantes |
| Traducir y adaptar tono | Código para producción | Ética y valores de marca |

*"El error del 90% de los emprendedores es pedirle lo rojo y no darle lo verde."*

**Key takeaway:** La IA no piensa por vos. Ejecuta bien lo que vos diseñás bien.

---

### 🔵 BLOQUE 3 — "Diseña tu Asistente: El Sistema de 4 Ingredientes"
**⏱ Duración:** 25 minutos
**📍 Slides:** 8–10

**Objetivo:**
Dar el framework simple que van a usar en el bloque de construcción. No más de 4 conceptos.

**Dinámica: Charla + ejercicio previo a construcción (15 min charla + 10 min ejercicio)**

**El Framework de los 4 Ingredientes** (slide central del workshop):

```
┌─────────────────────────────────────────────────┐
│           TU ASISTENTE PERFECTO                 │
├──────────────┬──────────────────────────────────┤
│  1. ROL      │  ¿Quién es? ¿Qué cargo tendría   │
│              │  en tu empresa?                  │
├──────────────┼──────────────────────────────────┤
│  2. CONTEXTO │  ¿Qué sabe de tu negocio,        │
│              │  producto y cliente ideal?        │
├──────────────┼──────────────────────────────────┤
│  3. TONO     │  ¿Cómo habla? ¿Formal, cercano,  │
│              │  técnico, simple?                 │
├──────────────┼──────────────────────────────────┤
│  4. LÍMITES  │  ¿Qué NO debe hacer ni decir?    │
└──────────────┴──────────────────────────────────┘
```

Pasás por los 4 con ejemplos reales y anti-ejemplos.

**Anti-ejemplo favorito:**
> *"La mayoría escribe: 'Ayudame con mi negocio.' Y la IA responde como si fuera Google. El problema no es la IA. Es que le diste basura y te devolvió basura con mejor gramática."*

**Ejercicio pre-construcción (10 min):**
En la Ficha de Trabajo, cada uno llena los 4 ingredientes para su asistente antes de tocarlo. Papel primero, pantalla después.

Facilitador circula, ayuda a clarificar, especialmente en "ROL" (muchos ponen "asistente general" — los empujás a ser específicos: "Especialista en ventas de software B2B para Pymes").

**Key takeaway:** Un asistente mal diseñado en papel va a ser un asistente mal diseñado en la pantalla. Pensar antes de construir.

---

### ☕ BREAK — 10 minutos

> Anunciás: *"Tienen 10 minutos. Carguen el computador. Abran Claude.ai o ChatGPT. Miren lo que escribieron en la ficha. Volvemos y construimos."*

Suena música. El ambiente es de anticipación, no de descanso.

---

### 🟢 BLOQUE 4 — "MANOS A LA OBRA: Construye tu Asistente" *(Ejercicio Principal)*
**⏱ Duración:** 50 minutos
**📍 Slides:** 5 (solo instrucciones paso a paso en pantalla)

**Objetivo:**
Cada participante construye y prueba un asistente de IA funcionando para su caso de uso real. Este es el corazón del workshop.

---

#### 📌 EJERCICIO PRINCIPAL DETALLADO

**Nombre:** *"El Asistente del Millón"*

**Herramienta:** Claude.ai (Projects) — plan gratuito alcanza. Alternativa: ChatGPT (Custom GPT en plan Plus) o instrucciones personalizadas en plan Free.

**Duración total:** 50 minutos

---

##### PASO 1 — Crear el Proyecto (10 min)
*(Facilitador hace esto en vivo mientras explica, pantalla proyectada)*

```
En Claude.ai:
1. Click en "Projects" → "New Project"
2. Nombre: "[Tu startup] - Asistente [Rol elegido]"
3. Ir a "Project Instructions"
```

En pantalla aparece el **Template de Instrucciones** que todos copian y adaptan:

```
TEMPLATE BASE — COPIAR Y PERSONALIZAR:

Eres [ROL ESPECÍFICO] de [NOMBRE STARTUP].

SOBRE NUESTRA EMPRESA:
- Qué hacemos: [descripción en 2 líneas]
- A quién le vendemos: [perfil del cliente ideal]
- Problema que resolvemos: [dolor concreto]
- Diferenciador clave: [por qué nos eligen]

CÓMO DEBES HABLAR:
- Tono: [formal/cercano/técnico/simple]
- Idioma: español [de qué país si aplica]
- Extensión respuestas: [corta/detallada/según soliciten]

TUS TAREAS PRINCIPALES:
1. [Tarea 1 — ej: redactar emails de prospección]
2. [Tarea 2 — ej: responder preguntas frecuentes]
3. [Tarea 3 — ej: generar contenido para redes]

NUNCA DEBES:
- Inventar precios o datos que no te haya dado
- Hablar mal de competidores
- [Límite específico de tu industria]
```

Todos copian el template en su pantalla y lo personalizan con su info.

---

##### PASO 2 — Cargar Contexto (10 min)

> *"Ahora le damos memoria. Un asistente sin contexto es como contratar a alguien y no mostrarle la empresa."*

Cada uno sube o pega en el proyecto:
- Descripción de su producto/servicio (pueden copiar de su web o LinkedIn)
- 3–5 preguntas frecuentes que reciben (las tenían en la Ficha de Trabajo)
- Tono de voz: les pedís que copien un post o email que ya escribieron y les gustó

*(Para quien no tiene nada escrito: el facilitador tiene un template de 10 preguntas que pueden responder en 5 minutos en papel y dictar)*

---

##### PASO 3 — Primera Prueba (15 min)

> *"Hora de la verdad. Lánzale la tarea real."*

Cada uno escribe su **primer prompt real** — el que resolvería el problema que anotaron en el Bloque 1.

**Facilitador en voz alta guía:**
1. Escribe el prompt (2 min)
2. Lee la respuesta (1 min)
3. Evalúa con 3 preguntas:
   - ¿Entendió tu negocio?
   - ¿El tono es el correcto?
   - ¿Lo usarías tal cual o necesita ajuste?

**Iteración guiada:**
> *"Si la respuesta es buena pero el tono está mal, no borrés todo. Decile: 'Bien, pero más [cercano/formal/directo]'. La IA tiene memoria dentro de la conversación."*

Facilitador circula activamente. Ayuda a quien está bloqueado. Los más avanzados empiezan a probar casos más complejos.

---

##### PASO 4 — Segundo caso de uso (15 min)

> *"Ya tienen un asistente funcionando. Ahora denle una segunda tarea — la segunda de su lista."*

Libertad total. El facilitador deja que cada uno explore. Interviene solo cuando alguien está frustrado.

**Truco para personas bloqueadas:**
> *"Si no sabés qué probar, usá esta fórmula:
> 'Actúa como [tu rol] y ayúdame a [tarea] para [contexto específico]. El resultado debe tener [formato/extensión].' "*

---

**Key takeaway del Bloque 4:** Construir un asistente no requiere código. Requiere saber qué querés y explicarlo bien.

---

### 🟣 BLOQUE 5 — "Test en vivo: Rompamos los asistentes"
**⏱ Duración:** 20 minutos
**📍 Slides:** 4

**Objetivo:**
Aprender a evaluar y mejorar un asistente mediante pruebas reales y feedback entre pares.

**Dinámica: Intercambio de asistentes (10 min)**

> *"Intercambien la computadora con la persona de al lado. Prueben el asistente del otro con preguntas que el dueño no esperaba."*

Objetivo: encontrar los bordes donde el asistente falla. Esto es lo más divertido del workshop. Siempre hay risas y descubrimientos.

Preguntas guía para quien prueba el asistente ajeno:
- "¿Qué pasa si le pregunto algo que no está en su contexto?"
- "¿Mantiene el tono si le escribo en mayúsculas y enojado?"
- "¿Responde coherente si le hago dos preguntas en una?"

**Debrief (10 min):**
El facilitador pregunta en voz alta: *"¿Quién encontró algo raro en el asistente del otro?"*

Mínimo 4–5 historias graciosas o reveladoras. Se van al whiteboard los patrones comunes de fallo:
- Inventó datos (→ solución: decirle explícitamente que no invente)
- Fue demasiado formal/informal (→ solución: dar ejemplo de tono en instrucciones)
- No entendió el producto (→ solución: agregar más contexto específico)
- Fue demasiado largo (→ solución: límite de extensión en instrucciones)

**Key takeaway:** El primer asistente nunca es el mejor. Las instrucciones se refinan con uso real.

---

### ⚪ BLOQUE 6 — "Cómo no abandonarlo en 48 horas"
**⏱ Duración:** 15 minutos
**📍 Slides:** 6

**Objetivo:**
Darles un sistema concreto de adopción para que el asistente entre en su rutina y no quede abandonado.

**Dinámica: Charla + compromiso escrito**

**El error más común post-workshop:**
> *"Salen de acá emocionados, lo usan 2 días, se olvidan, y en 3 semanas dicen 'probé la IA y no funcionó'. No falló la IA. Faltó el hábito."*

**Sistema de adopción en 3 pasos:**

```
SEMANA 1: El Disparador
→ Elige UNA tarea de tu lista del Bloque 1
→ Configura un recordatorio diario en tu calendario
→ Úsalo para ESA tarea todos los días, 7 días seguidos
→ Meta: que se vuelva automático, no reflexivo

SEMANA 2–3: La Expansión
→ Agrega una segunda tarea al asistente
→ Documenta lo que mejoraste en las instrucciones
→ Comparte 1 output bueno con tu equipo o redes

MES 2 EN ADELANTE: El Stack
→ Conéctalo a herramientas que ya usás (Make, Zapier, WhatsApp)
→ Enseñale a alguien de tu equipo
→ Iterá instrucciones cada 2 semanas
```

**El dato motivador:**
> *"Los emprendedores que usan IA consistentemente por 30 días recuperan en promedio 8 horas semanales. Eso es 1 día laboral que se gana. Cada semana."*

**Ejercicio de cierre del bloque (3 min):**
En la Ficha de Trabajo: escribir el **compromiso de la semana**.
> "Esta semana voy a usar mi asistente para [tarea específica] los días [días] a las [hora]."

Firma. Guarda la ficha.

**Key takeaway:** El ROI de la IA es proporcional a la consistencia del uso, no a lo sofisticado del asistente.

---

### 🏆 BLOQUE 7 — "Showcase + Próximos pasos"
**⏱ Duración:** 5 minutos
**📍 Slides:** 3**

**Objetivo:**
Cerrar con energía alta, celebrar lo que construyeron y dejar claros los próximos pasos.

**Dinámica: Showcase relámpago**

> *"Necesito 3 voluntarios. Tienen 30 segundos cada uno para mostrar su asistente y decir para qué lo van a usar esta semana."*

Aplauso genuino después de cada uno. Nada de crítica.

**Cierre del facilitador (2 min):**
> *"Entraron hace 3 horas sin un asistente. Salen con uno funcionando. Eso es real. Ahora el trabajo es simple: usarlo.*
>
> *La diferencia entre emprendedores que escalan y los que se quedan atascados no es que unos sean más inteligentes. Es que unos delegaron lo repetitivo y otros no."*

Recordatorio del QR con recursos. Invitación a comunidad (si aplica).

---

## 📄 FICHA DE TRABAJO — Para imprimir (1 por persona)

```
┌─────────────────────────────────────────────────────────┐
│     WORKSHOP: Construye tu Asistente de IA              │
│                                                         │
│  Nombre: ________________  Startup: ________________    │
│                                                         │
│  BLOQUE 1 — Mis 5 tareas que más tiempo me roban:       │
│  1. _________________________________________________    │
│  2. _________________________________________________    │
│  3. _________________________________________________    │
│  4. _________________________________________________    │
│  5. _________________________________________________    │
│                                                         │
│  BLOQUE 3 — Los 4 Ingredientes de mi Asistente:         │
│                                                         │
│  ROL: _______________________________________________    │
│  (Ej: "Especialista en ventas de SaaS para Pymes")      │
│                                                         │
│  CONTEXTO (qué sabe de mi startup):                     │
│  _________________________________________________      │
│  _________________________________________________      │
│                                                         │
│  TONO: _____________________________________________     │
│  (Ej: cercano, técnico, inspirador, directo)            │
│                                                         │
│  LÍMITES (qué NO debe hacer):                           │
│  _________________________________________________      │
│                                                         │
│  BLOQUE 4 — Tarea real para probar hoy:                 │
│  _________________________________________________      │
│                                                         │
│  Mi primer prompt:                                      │
│  _________________________________________________      │
│  _________________________________________________      │
│                                                         │
│  BLOQUE 6 — Mi compromiso de la semana:                 │
│  "Voy a usar mi asistente para ________________         │
│   los días __________ a las ________"                   │
│                                                         │
│  Firma: ___________________                             │
└─────────────────────────────────────────────────────────┘
```

---

## 📦 RECURSOS PARA LLEVAR A CASA

*(Entregar via QR code en mesa — link a Notion, Google Doc o similar)*

### Herramientas (todas con plan gratuito disponible)
| Herramienta | Para qué usarla | Link |
|---|---|---|
| **Claude.ai** | Asistente con Projects y memoria | claude.ai |
| **ChatGPT** | Custom GPTs si ya tenés cuenta | chatgpt.com |
| **Make.com** | Automatizar sin código (Zapier pero mejor) | make.com |
| **Notion AI** | Base de conocimiento + IA integrada | notion.so |
| **Perplexity** | Research con fuentes verificadas | perplexity.ai |

### Templates listos para usar
- [ ] Template de instrucciones para asistente de ventas
- [ ] Template de instrucciones para asistente de contenido
- [ ] Template de instrucciones para asistente de atención al cliente
- [ ] Template de instrucciones para asistente de research competitivo
- [ ] 50 prompts para emprendedores (organizados por área)

### Lecturas de 10 minutos (no libros, no cursos)
- "El prompt perfecto en 4 preguntas" — artículo
- "Cómo entrenar tu asistente con la voz de tu marca" — artículo
- "Los 3 errores que arruinan un asistente de IA" — artículo

### Comunidad
- Grupo de WhatsApp/Slack post-workshop (comparten prompts que funcionan)
- Office hours 2 semanas después: *"¿Cómo les fue con su asistente?"* (30 min, online)

---

## 🎯 RESUMEN DE SLIDES POR BLOQUE

| Bloque | Slides | Tipo dominante |
|---|---|---|
| Apertura | 3 | Impacto visual, pregunta gigante |
| Bloque 1 — El Problema | 6–8 | Datos + casos reales |
| Bloque 2 — Qué puede hacer la IA | 10–12 | Demo en vivo + semáforo |
| Bloque 3 — Diseño del Asistente | 8–10 | Framework visual + ejercicio |
| Break | 1 | Instrucciones de break |
| Bloque 4 — Construcción | 5 | Solo instrucciones paso a paso |
| Bloque 5 — Test e iteración | 4 | Dinámico, poco slide |
| Bloque 6 — Adopción | 6 | Sistema visual + compromiso |
| Bloque 7 — Cierre | 3 | Energía alta, simple |
| **TOTAL** | **46–52** | |

---

## 💡 TIPS DE FACILITACIÓN

**Las 3 situaciones que van a pasar (y cómo manejarlas):**

1. **"Yo no tengo WiFi / mi cuenta no funciona"**
   → Siempre tené 1 asistente pre-construido en tu pantalla. Esa persona lo ve en tu pantalla y customiza en papel. Mejor que quedarse afuera.

2. **"La IA me dio una respuesta horrible"**
   → Celebrarlo. *"Perfecto. Eso es exactamente lo que pasa cuando las instrucciones son vagas. Vamos a arreglarlo ahora."*

3. **"¿Pero esto no nos va a quitar el trabajo?"**
   → *"Los emprendedores en esta sala contratan personas. La IA no es un empleado que reemplaza, es una herramienta que multiplica lo que hacés vos. El que usa IA va a contratar más gente, no menos, porque va a crecer más rápido."*

---

> **Nota final del facilitador:** El momento más poderoso del workshop no es cuando la IA responde bien. Es cuando el emprendedor dice *"esperen, si esto me funciona para ventas, lo puedo usar también para..."* — ese momento de transferencia es tuyo para cultivar. Deja que ocurra.