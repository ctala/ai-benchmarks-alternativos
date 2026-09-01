# GLM 5.3 Flash — startup_content/workshop_outline

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 241.914s | tokens_per_second: 34.4
- input_tokens: 202 | output_tokens: 8329
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada y materiales necesarios para el taller.

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
### Workshop Práctico · 3 horas · 20-30 emprendedores early-stage

**Promesa del día:** *"Hoy nadie sale de aquí sin un asistente de IA funcionando para SU negocio."*

---

## 1. AGENDA DETALLADA (180 minutos)

| Hora | Bloque | Duración | Formato |
|------|--------|----------|---------|
| 0:00 | Apertura: "Hoy te vas con tu asistente" | 10 min | Dinámica + energía |
| 0:10 | IA sin humo: qué sí y qué no | 20 min | Charla + demo en vivo |
| 0:30 | Bloque 1: Diagnóstico express | 25 min | Ejercicio individual + parejas |
| 0:55 | ☕ Pausa activa | 10 min | Networking informal |
| 1:05 | Bloque 2: 🔨 CONSTRUCCIÓN | 45 min | Ejercicio principal hands-on |
| 1:50 | Bloque 3: Test drive cruzado | 20 min | Ejercicio en parejas |
| 2:10 | Bloque 4: Nivel pro — automatización | 20 min | Demos + Q&A |
| 2:30 | Demo day relámpago | 15 min | Show & tell voluntario |
| 2:45 | Cierre: compromisos + kit | 15 min | Ritual de cierre |

---

## 2. MATERIALES Y PREPARACIÓN PREVIA

### 📧 Email pre-workshop (ENVIAR 3-5 DÍAS ANTES — crítico)
- **Tarea obligatoria (10 min):** crear cuenta gratuita en ChatGPT o Gemini ANTES de llegar, con verificación de teléfono hecha. *Crear cuentas en el momento es el ladrón de tiempo #1 de estos workshops.*
- Traer laptop **o** celular cargado + cargador
- Traer datos reales de su negocio: precios, preguntas frecuentes, texto de venta

### 🏢 Sala y logística
- Mesas en **islas de 4-6 personas** (no formato aula — la energía y el trabajo entre pares lo requieren)
- Proyector + adaptadores HDMI/USB-C
- WiFi para invitados + **hotspot de respaldo** del facilitador
- 2-3 regletas/tomas múltiples por isla
- Timer visible en pantalla o físico
- Playlist de música energética para entrada, pausa y ejercicios

### 🖨️ Impresos
- **Canvas del Asistente** (1 página por persona, ver sección 4)
- **Plantilla "Prompt Maestro"** (1 página por persona)
- Stickers o marcadores para votación final

### 👥 Equipo
- 1 facilitador principal + **1-2 asistentes de apoyo** (ratio mínimo 1 apoyo por cada 12 participantes)
- **Plan B:** videos de las demos grabados por si falla el internet

---

## 3. BLOQUES EN DETALLE

### 🔥 APERTURA: "Hoy te vas con tu asistente" — 10 min · 4 slides
- **Objetivo:** bajar la ansiedad tecnológica y anclar la promesa del día.
- **Dinámica:** Poll de manos a toda velocidad: *"¿Quién ya usó ChatGPT?" · "¿Quién siente que la IA no es para su negocio?" · "¿Quién quiere salir de aquí con la suya funcionando?"* + 3 reglas: laptops abiertas, preguntas bienvenidas, hecho es mejor que perfecto.
- **Key takeaway:** *"Hoy no vienes a escuchar sobre IA. Vienes a construirla."*

### 💡 IA SIN HUMO: qué sí y qué no — 20 min · 9 slides
- **Objetivo:** desmitificar la IA con un caso real, cero tecnicismos.
- **Dinámica:** Charla de 8 min con analogía central: *"Un asistente de IA es un empleado junior brillante: es rapidísimo, pero no sabe NADA de tu negocio hasta que le das el manual."* Luego **demo en vivo (7 min):** un asistente pre-construido para "Pastelería Doña Rosa" responde preguntas de clientes con precios, tono y hasta rechaza un intento de regateo. Cierre con discusión rápida (5 min): *"¿Qué tarea de SU negocio les vino a la mente?"*
- **Key takeaway:** *"La IA no reemplaza tu conocimiento — lo multiplica. Pero primero hay que dárselo."*

### 🎯 BLOQUE 1: Diagnóstico express — 25 min · 5 slides
- **Objetivo:** cada participante elige UN caso de uso concreto (no cinco).
- **Dinámica:** Ejercicio individual con el **Canvas del Asistente, casillas 1-4** (15 min). Luego en parejas se cuentan su caso en 60 segundos y el compañero pregunta: *"¿Eso te devuelve horas ESTA semana?"* (7 min). 3-4 shares al pleno (3 min).
- **Key takeaway:** *"El mejor asistente no es el más impresionante. Es el que te devuelve horas esta semana."*

### ☕ PAUSA — 10 min · 1 slide
- Música, café, y consigna: *"Comparte con alguien de otra mesa qué asistente vas a construir."*

### 🔨 BLOQUE 2: CONSTRUCCIÓN — 45 min · 8 slides ⭐ *el corazón del workshop*
- **Objetivo:** cada persona sale con su asistente respondiendo en pantalla.
- **Dinámica:** Instrucciones rápidas (5 min) → **construcción guiada** (25 min): completan casillas 5-6 del canvas, pasan todo a la **plantilla Prompt Maestro**, la pegan en ChatGPT/Gemini y hacen su primera prueba. Asistentes de apoyo circulando isla por isla. → **Iteración** (15 min): protocolo de 3 pruebas (ver sección 4).
- **Key takeaway:** *"Tu asistente es tan bueno como las instrucciones que le diste. Basura entra, basura sale."*

### 🧪 BLOQUE 3: Test drive cruzado — 20 min · 3 slides
- **Objetivo:** stress test con un "cliente" que no es tú.
- **Dinámica:** En parejas, intercambian asistentes: uno hace de **cliente difícil** (grosero, confundido, que regatea) y el otro observa dónde falla (12 min). Ajustes rápidos a las instrucciones en vivo (8 min).
- **Key takeaway:** *"Si tu asistente solo funciona cuando tú le preguntas, no sirve. Tiene que sobrevivir a clientes reales."*

### 📈 BLOQUE 4: Nivel pro — de asistente a automatización — 20 min · 7 slides
- **Objetivo:** mostrar el camino de crecimiento sin abrumar.
- **Dinámica:** Demo en vivo de las **3 rutas:** (1) *Hoy, gratis:* guardar tu asistente (Gem de Gemini o tu Prompt Maestro guardado en notas). (2) *Esta semana:* conectarlo a WhatsApp Business con herramientas no-code — demo de ManyChat o similar. (3) *Este mes:* automatizar el flujo completo con Make/Zapier — lead llega → IA responde → agenda → te avisa. Q&A abierto (10 min).
- **Key takeaway:** *"Hoy construiste el cerebro. Conectarlo a WhatsApp es solo plomería — y hay herramientas sin código para eso."*

### 🎤 DEMO DAY RELÁMPAGO — 15 min · 2 slides
- **Objetivo:** celebrar, mostrar variedad, inspirar a los que van más lento.
- **Dinámica:** 3-4 voluntarios, **3 minutos estrictos** cada uno: muestran su asistente respondiendo una pregunta real. Aplausos + voto con stickers para "el asistente más listo".
- **Key takeaway:** *"20 personas, 20 asistentes distintos. La IA es un multiplicador, no un producto uniforme."*

### 🏁 CIERRE: compromisos + kit — 15 min · 4 slides
- **Objetivo:** que esto no muera el lunes.
- **Dinámica:** Compromiso público: cada persona escribe en una tarjeta *"Esta semana mi asistente va a ___"* y lo dice en voz alta a su mesa. Entrega del Kit del Constructor (QR en pantalla). Foto grupal con asistentes en mano. Invitación al grupo de WhatsApp de la cohorte.
- **Key takeaway:** *"Tu asistente v1 ya existe. La v2 sale de usarlo con clientes reales esta semana."*

---

## 4. EJERCICIO PRINCIPAL: "El Canvas del Asistente + Prompt Maestro"

### Paso 1 — Canvas del Asistente (6 casillas, 1 página)

| Casilla | Qué llenan |
|---------|-----------|
| 1. Mi startup en una frase | Qué vendes, a quién |
| 2. Mi cliente típico | Cómo habla, qué le duele |
| 3. La tarea que más tiempo me roba | Elegir UNA: atención / ventas / contenido / operaciones |
| 4. Top 10 preguntas que recibo siempre | Las reales, de WhatsApp o DMs |
| 5. Mi tono | 3 adjetivos + 1 frase textual que diría yo |
| 6. Líneas rojas | Qué NO debe hacer mi asistente |

### Paso 2 — Plantilla "Prompt Maestro" (llenar espacios)

```
🎯 ASISTENTE: [nombre]

# QUIÉN ERES
Eres [nombre], el asistente de [startup].

# NUESTRO NEGOCIO
Vendemos [producto/servicio] a [cliente ideal].
Precios: [...]. Nos diferencia: [...].

# TU MISIÓN
[ej. responder dudas de clientes y agendar demos]

# CÓMO HABLAS
- Tono: [3 adjetivos] · Máximo 3-4 frases por respuesta
- [Tuteas / tratas de usted]

# REGLAS DE ORO
1. Solo respondes sobre [temas del negocio]
2. Si no sabes algo: "Buena pregunta, lo confirmo con el equipo
   y te escribo hoy." NUNCA inventes precios ni promesas.
3. Cada respuesta termina con una pregunta que acerque a [objetivo]

# EJEMPLOS (aprende de estos)
Cliente: [pregunta real] → Tú: [tu respuesta ideal]
```

### Paso 3 — Protocolo de las 3 pruebas
1. **Prueba fácil:** pregunta típica → ¿responde como tú responderías?
2. **Prueba trampa:** pregunta fuera de alcance → ¿admite que no sabe o inventa?
3. **Prueba de cliente difícil:** grosero o regateador → ¿mantiene el tono?

✅ **Criterio de éxito:** pasa las 3 pruebas = asistente v1 terminado.

---

## 5. KIT PARA LLEVAR A CASA (todo por QR/link)

1. 📊 Slides del workshop
2. 📝 Canvas del Asistente editable (Google Doc/Notion)
3. 🎯 Plantilla Prompt Maestro en digital
4. 🛠️ Guía rápida de herramientas: tabla comparativa (ChatGPT, Gemini, Claude gratis vs. pago + ManyChat, Wati, Make, Zapier)
5. ✅ **Checklist "Primeros 30 días":** Semana 1: úsalo a diario y anota errores · Semana 2: agrégale las preguntas reales que llegaron · Semana 3: 3 clientes reales lo prueban · Semana 4: decide si lo conectas a WhatsApp
6. 💬 Invitación al grupo de WhatsApp de la cohorte (seguimiento y comunidad)

---

## 6. SLIDES: RESUMEN

| Sección | Slides | Total parcial |
|---------|--------|---------------|
| Apertura | 4 | 4 |
| IA sin humo | 9 | 13 |
| Diagnóstico | 5 | 18 |
| Pausa | 1 | 19 |
| Construcción | 8 | 27 |
| Test drive | 3 | 30 |
| Nivel pro | 7 | 37 |
| Demo day | 2 | 39 |
| Cierre | 4 | **~43 slides** |

---

## 💡 Pro tips del facilitador

- **El enemigo #1 es la creación de cuentas.** El email pre-workshop no es opcional. Ten 2-3 cuentas de respaldo listas por si alguien llegó sin hacer la tarea.
- **Minuto 55-65 = valle de energía.** Ahí va la pausa. No la muevas.
- Si alguien trae un caso demasiado complejo, redirígelo: *"Hoy construimos la versión simple. La compleja es tu tarea de la semana."*
- Los asistentes de apoyo deben **no tocar los teclados de los participantes** — guiar con preguntas, no hacer el trabajo por ellos.

¿Quieres que desarrolle alguno de los materiales en detalle (el Canvas imprimible, el email pre-workshop, o el guion de la demo de Pastelería Doña Rosa)?