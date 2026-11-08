# MiMo V2.6 Pro — startup_content/workshop_outline

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 8.22 | quality: 9.72
- latency_total: 148.302s | tokens_per_second: 37.4
- input_tokens: 211 | output_tokens: 5544
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
## Workshop Presencial — 3 Horas | 20-30 emprendedores early-stage

---

## 📋 AGENDA DETALLADA (3 HORAS)

| # | Bloque | Duración | Min Acum. |
|---|--------|----------|-----------|
| 1 | 🔥 Bienvenida + Energía | 15 min | 0:15 |
| 2 | 🧠 "IA en 10 min: lo que necesitas saber" | 20 min | 0:35 |
| 3 | 🎯 "Tu Asistente IA en Acción: Demo en Vivo" | 20 min | 0:55 |
| 4 | ☕ Break + Networking | 10 min | 1:05 |
| 5 | 🛠️ **EJERCICIO PRINCIPAL: Construye tu Asistente** | 60 min | 2:05 |
| 6 | 🚀 "Del Asistente al Negocio: Escala y ROI" | 25 min | 2:30 |
| 7 | 🎤 Pitches Relámpago + Cierre | 25 min | 2:55 |
| 8 | 📸 Networking + Entrega de Recursos | 5 min | 3:00 |

---

## 📦 MATERIALES NECESARIOS (Preparar ANTES)

### Para el facilitador:
- [ ] Laptop con proyección + adaptador HDMI/USB-C
- [ ] Conexión a internet estable (pedir WiFi dedicado al venue)
- [ ] **Hotspot de respaldo** (teléfono o MiFi) — CRÍTICO
- [ ] Cuenta de ChatGPT Plus (o Claude) abierta y logueada
- [ ] Cuenta de **Make.com** (o Zapier) abierta
- [ ] Cuenta de **Notion AI** o Google Sheets preparada
- [ ] Slides listas (ver conteo abajo) + backup en USB
- [ ] Cronómetro visible (teléfono proyectado o timer en slides)
- [ ] Micrófono inalámbrico (si >20 personas)
- [ ] Marcadores + 2 pizarras blancas (o pizarra virtual tipo Miro)

### Para cada participante:
- [ ] **Laptop cargada** (requisito obligatorio en la invitación)
- [ ] Cuenta gratuita de ChatGPT creada ANTES del workshop (instrucciones en email previo)
- [ ] Cuenta gratuita de Make.com (instrucciones en email previo)
- [ ] Cuaderno + bolígrafo
- [ ] **Ficha de trabajo impresa** (1 por persona — ver template abajo)
- [ ] **Tarjeta de prompts** laminada (handout físico)

### Para el venue:
- [ ] Mesas de trabajo en clusters de 4-5 personas
- [ ] Tomas de corriente accesibles (extensión multi-toma por mesa)
- [ ] Pizarra o superficie para pegar post-its
- [ ] Break: agua, café, snack ligero

---

## 🗂️ BLOQUES DETALLADOS

---

### BLOQUE 1: 🔥 Bienvenida + Energía
**⏱ Duración:** 15 min | **Slides:** 5

**Objetivo:** Romper el hielo, generar expectativa, conectar con la audiencia.

**Dinámica:** Interactiva — Icebreaker + Poll en vivo

**Contenido:**
1. (2 min) Bienvenida, reglas del workshop: *"Hoy no hay teoría muerta. Todo lo que haces lo usas mañana."*
2. (5 min) **Icebreaker "Tu Mayor Miedo con IA":** Cada persona escribe en un post-it su mayor miedo/duda sobre IA y lo pega en la pizarra. El facilitador agrupa en 3-4 categorías visibles.
3. (5 min) **Poll rápido** (Mentimeter o levantando mano):
   - "¿Ya usan IA en su negocio?" (Sí/No)
   - "¿Qué les frena?" (No sé usarla / No sé para qué / Me da miedo / Es caro)
   - Resultados visibles en pantalla → *"Hoy vamos a romper TODO esto."*
4. (3 min) Presentación del facilitador (30 segundos, no más) + Agenda visual + *"La promesa: al final de las 3 horas, van a tener un asistente de IA funcionando para SU startup."*

**Key Takeaway:**
> *"No necesitas ser técnico. Necesitas ser claro en lo que tu negocio necesita. La IA es el nuevo Excel: si no lo usas, estás perdiendo tiempo."*

---

### BLOQUE 2: 🧠 "IA en 10 Min: Lo Que Realmente Necesitas Saber"
**⏱ Duración:** 20 min | **Slides:** 12

**Objetivo:** Desmitificar la IA, dar vocabulario mínimo viable, y encuadrar la mentalidad correcta (IA como copiloto, no como magia).

**Dinámica:** Charla interactiva + Micro-ejercicio (2 min)

**Contenido:**
1. (3 min) **"¿Qué es IA generativa en 1 frase?"** — No es magia. Es un modelo de lenguaje que predice texto. *"Es como un interno súper rápido que leyó todo internet, pero que necesita que le des instrucciones claras."*
2. (4 min) **Los 3 conceptos que importan:**
   - **Prompt** = Instrucción. La calidad de la IA = la calidad de tu prompt.
   - **Contexto** = Información que le das (sobre tu negocio, tu cliente, tu tono).
   - **Output** = Lo que te devuelve. Tú decides si sirve o no.
3. (5 min) **"Lo que la IA SÍ puede hacer por tu startup"** (casos reales LatAm):
   - Responder clientes (WhatsApp/email)
   - Crear contenido (posts, emails, pitches)
   - Analizar datos (ventas, feedback)
   - Generar propuestas y cotizaciones
   - Automatizar tareas repetitivas
4. (3 min) **"Lo que NO puede"** — No reemplaza tu criterio. No conoce tu negocio a menos que se lo expliques. No decide por ti. *"Es tu copiloto, no tu CEO."*
5. (3 min) **Micro-ejercicio:** En la ficha de trabajo, escribir en 1 línea: **"En mi startup, la IA me ayudaría a ahorrar tiempo en ___"** (30 segundos para escribir + compartir en parejas por 1 min).
6. (2 min) Transición: *"Ya saben lo básico. Ahora van a VERLO funcionar."*

**Key Takeaway:**
> *"La IA no es complicada. Es un interno súper rápido que necesita instrucciones claras (prompts) y contexto de tu negocio. La clave no es la tecnología: es saber qué pedirle."*

---

### BLOQUE 3: 🎯 "Tu Asistente IA en Acción: Demo en Vivo"
**⏱ Duración:** 20 min | **Slides:** 8

**Objetivo:** Generar el "wow moment" — ver un asistente de IA real resolviendo problemas de una startup real.

**Dinámica:** Demo en vivo + Discusión rápida

**Contenido:**
1. (2 min) Setup: *"Van a ver un asistente construido para una startup real de LatAm."*
2. (12 min) **Demo en vivo** — Caso: **"Café Andina"** (startup ficticia pero realista de venta de café online en Colombia):
   - Escenario 1: Cliente pregunta por WhatsApp → El asistente responde con info de productos, precios, y tiempos de envío.
   - Escenario 2: Se le pide al asistente generar un email de seguimiento post-venta.
   - Escenario 3: Se le pide analizar un CSV de ventas del mes y dar 3 insights accionables.
   - Escenario 4: Se le pide crear un post de Instagram para el lanzamiento de un nuevo producto.
   - *(En cada escenario, mostrar el prompt que se usa y por qué funciona)*
3. (4 min) **Discusión guiada:**
   - *"¿Qué vieron que les sirve para SU negocio?"*
   - *"¿Qué les pareció imposible que hiciera y lo hizo?"*
   - 3-4 respuestas rápidas de la audiencia.
4. (2 min) **"El secreto no es la herramienta. Es el PROMPT."** — Mostrar la estructura del prompt que hizo posible la demo (rol + contexto + tarea + formato).
5. (2 min) Transición: *"Ahora les toca a ustedes. Vamos a construir SU asistente."*

**Key Takeaway:**
> *"Un buen asistente de IA no se trata de tecnología sofisticada. Se trata de darle contexto claro de tu negocio y pedirle tareas específicas. Lo que acaban de ver, ustedes pueden hacerlo HOY."*

---

### BLOQUE 4: ☕ Break + Networking
**⏱ Duración:** 10 min | **Slides:** 1 (slide de break con música)

**Objetivo:** Descomprimir, recargar energía, networking informal.

**Dinámica:** Libre — *"Durante el break, busquen a alguien de un rubro diferente al suyo y pregunten: '¿Cómo usarías IA en tu negocio?'"*

**Key Takeaway:**
> *(N/A — pero el facilitador aprovecha para revisar post-its y ajustar el contenido restante si es necesario)*

---

### BLOQUE 5: 🛠️ EJERCICIO PRINCIPAL — "Construye tu Asistente IA"
**⏱ Duración:** 60 min | **Slides:** 6 (instrucciones visuales)

**Objetivo:** Que cada participante construya un asistente de IA funcional para su startup, usando una plantilla guiada.

**Dinámica:** Taller práctico guiado (hands-on) + soporte 1-a-1

---

#### 📌 ESTRUCTURA DEL EJERCICIO (paso a paso)

**Fase 1: Define el problema (10 min)**
> 📝 En la **Ficha de Trabajo** (impresa), completar:
> - **Nombre de mi startup:** ___
> - **¿Qué problema resuelve mi asistente?** (elegir 1 de 3 opciones):
>   - A) Atender clientes / responder preguntas
>   - B) Crear contenido / comunicaciones
>   - C) Analizar datos / generar reportes
> - **¿Quién lo usará?** (yo, mi equipo, mis clientes)
> - **¿Qué tiempo me ahorra?** (estimar en horas/semana)

**Fase 2: Escribe el Prompt Maestro (20 min)**
> 📝 Guiados por el facilitador, completar la plantilla de prompt:
>
> ```
> ERES UN ASISTENTE EXPERTO EN [tu industria].
>
> CONTEXTO:
> - Mi startup se llama [nombre] y se dedica a [qué hace].
> - Nuestros clientes son [tipo de cliente].
> - Nuestro tono de comunicación es [formal/casual/profesional].
> - Nuestros productos/servicios principales son: [lista].
>
> TU TAREA:
> - Ayúdame a [tarea principal: responder clientes / crear contenido / analizar datos].
>
> REGLAS:
> - Responde siempre en [idioma].
> - Si no tienes información, di "No tengo esa información, pero puedo ayudarte con..."
> - Sé [conciso/detallado].
> ```
>
> **Durante esta fase, el facilitador:**
> - Proyecta la plantilla
> - Hace 1 ejemplo en vivo (para la startup ficticia)
> - Recorre las mesas ayudando a 1-a-1
> - Tiempo visible en pantalla

**Fase 3: Prueba y Refina (20 min)**
> 📝 Cada participante:
> 1. Copia su prompt en ChatGPT (o Claude)
> 2. Le hace 3 preguntas de prueba (el facilitador da ejemplos de preguntas)
> 3. Evalúa la respuesta: ¿Es útil? ¿Es precisa? ¿Suena como mi marca?
> 4. Refina el prompt (agrega/quita contexto, ajusta reglas)
> 5. **Criterio de éxito:** La respuesta de la IA suena como si fuera de tu startup.
>
> **Durante esta fase, el facilitador:**
> - Recorre las mesas
> - Ayuda a los que están atascados
> - Pide a 2-3 personas que compartan su pantalla y muestren resultados (5 min de "show & tell" rápido)

**Fase 4: Documenta y Planifica (10 min)**
> 📝 Completar en la ficha:
> - **Mi prompt final** (copiarlo completo)
> - **¿Dónde lo voy a usar?** (ChatGPT, WhatsApp, email, Notion, etc.)
> - **¿Qué voy a automatizar primero?** (1 tarea concreta para esta semana)
> - **Mi meta:** "Voy a ahorrar ___ horas/semana usando este asistente."

**Key Takeaway:**
> *"Un asistente de IA útil = contexto claro de tu negocio + una tarea específica + reglas de comportamiento. Ya tienen su primer asistente funcionando. Ahora lo que falta es USARLO todos los días."*

---

### BLOQUE 6: 🚀 "Del Asistente al Negocio: Escala y ROI"
**⏱ Duración:** 25 min | **Slides:** 10

**Objetivo:** Mostrar el camino desde un prompt hasta un sistema de IA que escala, con foco en ROI y casos reales.

**Dinámica:** Charla + mini-casos + discusión

**Contenido:**
1. (5 min) **"Del prompt al sistema"** — Evolución:
   - Nivel 1: Un prompt manual (lo que hicieron hoy)
   - Nivel 2: Prompt + automatización (Make/Zapier + WhatsApp/email)
   - Nivel 3: Asistente integrado (API + CRM + herramientas)
   - *"Hoy están en Nivel 1. El 80% del valor está aquí. No subestimen esto."*
2. (7 min) **3 mini-casos reales de LatAm:**
   - 🇨🇴 Startup de e-commerce: redujo tiempo de respuesta al cliente de 4h a 5 min con IA
   - 🇲🇽 Agencia de marketing: generaba 30 posts/semana con 1 persona + IA (antes 3 personas)
   - 🇦🇷 SaaS B2B: automatizó propuestas comerciales, cerró 40% más rápido
   - *(En cada caso: problema → solución IA → resultado medible)*
3. (5 min) **"Calcula tu ROI en 2 minutos"** — Ejercicio rápido en la ficha:
   - Horas que pierdo por semana en tareas que IA puede hacer: ___
   - Mi costo-hora (o el de mi equipo): ___
   - Ahorro mensual estimado: ___
   - *"Si ahorran 5 horas/semana y su tiempo vale $20/hora, son $400/mes. La IA es gratis o cuesta $20/mes. El ROI es absurdo."*
4. (5 min) **Discusión abierta:**
   - *"¿Cuál es el mayor obstáculo para implementar IA en su startup?"*
   - *"¿Qué necesitan para dar el próximo paso?"*
   - 4-5 respuestas rápidas
5. (3 min) **"Los 3 errores que matan tu asistente IA":**
   - ❌ Prompt vago (sin contexto)
   - ❌ No iterar (aceptar la primera respuesta)
   - ❌ No medir (no saber si te ahorra tiempo)

**Key Takeaway:**
> *"La IA no es un gasto: es el empleado más barato que vas a contratar. El ROI está en las horas que te libera. Empieza simple, mide resultados, y escala."*

---

### BLOQUE 7: 🎤 Pitches Relámpago + Cierre
**⏱ Duración:** 25 min | **Slides:** 4

**Objetivo:** Celebrar los resultados, generar momentum, y cerrar con energía.

**Dinámica:** Pitches rápidos + Cierre inspirador

**Contenido:**
1. (15 min) **"60-Second Pitches"** — 5-6 voluntarios presentan:
   - *"Mi asistente se llama ___ y ayuda a ___ para ___"*
   - Muestran su prompt en pantalla (proyector compartido)
   - 1 minuto cada uno + 30 seg de aplausos/preguntas
   - *(El facilitador elige una mezcla: 1 que salió perfecto, 1 que está en progreso, 1 que tuvo problemas — para normalizar todos los caminos)*
2. (5 min) **Cierre energético:**
   - Recap visual: *"Hoy construiste un asistente de IA. No es perfecto. Pero FUNCIONA."*
   - Los 3 pasos para mañana: (1) Usa tu prompt hoy mismo, (2) Pide feedback a 1 cliente, (3) Refina 1 vez por semana
   - Frase de cierre: *"La IA no va a reemplazar a los emprendedores. Pero los emprendedores que usan IA SÍ van a reemplazar a los que no."*
3. (5 min) **Entrega de recursos** (ver abajo) + **CTA:**
   - QR code a carpeta de Google Drive con todos los recursos
   - QR code al grupo de WhatsApp/Telegram de alumni
   - Encuesta de satisfacción (Google Form, 2 min)

**Key Takeaway:**
> *"No necesitas ser técnico para usar IA. Necesitas ser claro en lo que tu negocio necesita. Ya tienen la herramienta. Ahora es cuestión de usarla."*

---

### BLOQUE 8: 📸 Networking + Entrega de Recursos
**⏱ Duración:** 5 min | **Slides:** 1 (slide final con QR codes)

**Objetivo:** Cierre informal, fotos, intercambio de contactos.

**Dinámica:** Libre

---

## 🛠️ EJERCICIO PRINCIPAL — Resumen Visual

```
┌─────────────────────────────────────────────────────┐
│           EJERCICIO: "CONSTRUYE TU ASISTENTE"        │
│                    (60 minutos)                       │
├─────────────────────────────────────────────────────┤
│                                                      │
│  FASE 1 (10 min)  →  DEFINE el problema              │
│  FASE 2 (20 min)  →  ESCRIBE el Prompt Maestro       │
│  FASE 3 (20 min)  →  PRUEBA y REFINA                 │
│  FASE 4 (10 min)  →  DOCUMENTA y PLANIFICA           │
│                                                      │
│  RESULTADO: Un asistente IA funcional para tu        │
│  startup, con prompt listo para usar HOY.            │
│                                                      │
│  CRITERIO DE ÉXITO: La respuesta de la IA suena      │
│  como si fuera de tu startup.                        │
│                                                      │
└─────────────────────────────────────────────────────┘
```

---

## 📚 RECURSOS PARA LLEVAR A CASA

### 📁 Google Drive / Notion (acceso vía QR)

| Recurso | Descripción |
|---------|-------------|
| **Prompt Library** | 25 prompts listos para startups (ventas, marketing, soporte, finanzas, legal) |
| **Plantilla de Asistente IA** | Template editable (Google Doc) con la estructura del prompt maestro |
| **Checklist: Primeros 7 días con IA** | Guía paso a paso para implementar lo aprendido |
| **Calculadora de ROI** | Google Sheet para estimar ahorro de tiempo/dinero |
| **Video: "5 Prompts que Cambian tu Negocio"** | Grabación de 15 min (bonus) |
| **Glosario de IA para no-técnicos** | PDF de 2 páginas |
| **Carpeta de herramientas recomendadas** | Lista con links: ChatGPT, Claude, Make, Notion AI, Perplexity |
| **Grupo WhatsApp/Telegram** | Comunidad de alumni para preguntas y soporte |

### 📄 Handouts físicos (imprimir)
- **Ficha de Trabajo** (2 páginas, doble cara)
- **Tarjeta de Prompts** (tamaño tarjeta de crédito, laminada) — con los 5 prompts más útiles
- **Agenda del workshop** (1 hoja)

---

## 📊 SLIDE COUNT ESTIMADO

| Bloque | Slides | Notas |
|--------|--------|-------|
| 1. Bienvenida + Energía | 5 | Incluye slide de poll |
| 2. IA en 10 Min | 12 | Conceptos visuales, no texto |
| 3. Demo en Vivo | 8 | Screenshots + live demo |
| 4. Break | 1 | Timer + música |
| 5. Ejercicio Principal | 6 | Instrucciones + plantilla |
| 6. Escala y ROI | 10 | Casos + calculadora |
| 7. Pitches + Cierre | 4 | Recap + QR codes |
| 8. Networking | 1 | Slide final |
| **TOTAL** | **~47 slides** | **Máximo 50** |

---

## ⚡ CHECKLIST DE PREPARACIÓN (7 días antes)

```
D-7:  Confirmar venue, WiFi, y logística
D-5:  Enviar email a participantes con:
      - Requisito: laptop + cuentas creadas
      - Pre-work: "Piensa en 1 tarea que te roba tiempo"
D-3:  Preparar slides (47 slides max)
D-2:  Imprimir fichas de trabajo + tarjetas de prompts
D-2:  Preparar demo (probar TODO en vivo, 2 veces)
D-1:  Backup: USB con slides + hotspot listo
D-1:  Preparar carpeta de recursos + QR codes
D-day: Llegar 60 min antes. Probar WiFi, proyector, audio.
       Tener plan B si internet falla (screenshots de demo).
```

---

## 🎯 MÉTRICAS DE ÉXITO DEL WORKSHOP

| Métrica | Target |
|---------|--------|
| Participantes que terminan con prompt funcional | 90%+ |
| Satisfacción (encuesta post-evento) | 4.5+/5 |
| Participantes que usan IA en los primeros 7 días | 60%+ |
| Pitches presentados (voluntarios) | 5-6 |
| Post-its en la pizarra (engagement) | 100% de participantes |

---

> **💡 Nota para el facilitador:** El tono es ENERGÉTICO y PRÁCTICO. Cada 10 minutos hay que cambiar de dinámica (charla → demo → ejercicio → discusión). Si alguien pregunta algo muy técnico, responder: *"Buena pregunta, la guardamos para el final o te la respondo al break. Hoy el foco es que SALGAN con algo funcionando."*

> **🚨 Plan B:** Si internet falla → usar screenshots de la demo + enfatizar el ejercicio de escritura de prompts (no requiere conexión). La Fase 1 y 2 del ejercicio son offline-friendly.