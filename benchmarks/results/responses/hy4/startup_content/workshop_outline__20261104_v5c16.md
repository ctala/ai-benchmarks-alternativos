# Tencent Hy4 — startup_content/workshop_outline

- model_id: `tencent/hy4`
- success: True  | final: 8.57 | quality: 10.0
- latency_total: 47.021s | tokens_per_second: 81.2
- input_tokens: 223 | output_tokens: 3818
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y práctica, proporcionando un plan detallado y estructurado que se ajusta perfectamente a las necesidades de emprendedores no técnicos, con insights útiles y una dinámica bien pensada.

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

¡Listo, equipo! 🔥 Acá va el outline armado con la vibra de un taller real en LatAm: menos teoría, más "lo probamos ya", cafeína, post-its y laptops abiertas. Pensado para 25 emprendedores que no saben código pero sí saben qué problema quieren resolver.

---

# 🚀 Workshop: **Construye tu Asistente de IA para tu Startup**
**Formato:** Presencial · 3 horas · 20–30 personas · No-técnicos · Español LATAM  
**Promesa de salida:** *Te vas con un asistente funcionando (sí, funcionando) para una tarea real de tu startup + un prompt listo para seguir iterando.*

---

## 1️⃣ Agenda Detallada (180 min)

| Hora | Bloque | Duración |
|------|--------|----------|
| 00:00 – 00:15 | **Bienvenida & Rompehielo: "Tu dolor favorito"** | 15 min |
| 00:15 – 00:35 | **Bloque 1: IA sin humo (lo que sí te sirve hoy)** | 20 min |
| 00:35 – 01:00 | **Bloque 2: Demo en vivo – De idea a asistente en 7 min** | 25 min |
| 01:00 – 01:15 | ☕ **Pausa activa + Networking relámpago** | 15 min |
| 01:15 – 02:00 | **Bloque 3: EJERCICIO PRINCIPAL – Construye el tuyo** | 45 min |
| 02:00 – 02:25 | **Bloque 4: Show & Tell (3 startups, 3 minutos c/u)** | 25 min |
| 02:25 – 02:45 | **Bloque 5: Cuidado con el "casi funciona" (límites, datos y ética light)** | 20 min |
| 02:45 – 03:00 | **Cierre: Tu roadmap de 7 días + Foto + Compromiso** | 15 min |

---

## 2️⃣ Materiales (preparar ANTES 🧰)

**Para el facilitador**
- Proyector + HDMI + adaptador (siempre, siempre lleva el adaptador 😅)
- Laptop con: ChatGPT / Claude / Gemini **ya logueados**, + una cuenta de **Make / n8n / Zapier** (demo)
- Slides (ver conteo abajo) + cronómetro visible (usa `time.timer` en pantalla)
- Plantilla impresa **"Canvas del Asistente"** (A3, 1 por persona) 👇 ver recurso
- Post-its de 3 colores + marcadores gruesos (por mesa de 5)
- Sticker que diga: *“Ya lo probé ✅”* (premio psicológico, funciona demasiado)
- Playlist lo-fi / cumbia suave de fondo 🎶

**Para los participantes (pedir en el mail de confirmación)**
- Laptop o tablet (📌 **no solo celular**, mejor si es laptop)
- Cuenta gratuita creada en ChatGPT o Claude (mandar link 48h antes)
- 1 problema real de su startup anotado (ej: “respondo 20 veces lo mismo por WhatsApp”)

**Extra que salva el taller**
- 2–3 “copilotos” (gente del equipo o voluntarios) circulando por mesas 🧑‍💻
- WiFi de respaldo (hotspot del celular del facilitador, sí, pasa)
- Extensión / multiprise (en LATAM nunca sobra 🔌)

---

## 3️⃣ Bloques (Objetivo · Dinámica · Key Takeaway)

### 🟢 Bloque 0 · Bienvenida & Rompehielo: *"Tu dolor favorito"* · 15 min
- **Objetivo:** Bajar la ansiedad técnica y sacar a flote tareas repetitivas reales.
- **Dinámica:** Cada persona escribe en un post-it **la tarea que más odia repetir**, lo pega en la pared y dice su nombre + startup en 1 frase. El facilitador agrupa en vivo: *“Ventas / Soporte / Contenido / Ops”*.
- **Key takeaway:** *No viniste a aprender IA. Viniste a quitarte un dolor de encima.*

📊 **Slides: 3** (Portada · Promesa del día · “Reglas del juego: probar > entender”)

---

### 🟡 Bloque 1 · IA sin humo · 20 min
- **Objetivo:** Dar el mínimo marco mental para no perderse (sin hablar de transformers 🙅).
- **Dinámica:** Charla corta + 2 preguntas al aire. Metáfora LATAM:  
  > *“La IA es como un practicante muy rápido, muy obediente… pero que no conoce tu negocio si no le das el contexto.”*
  - Mini-modelo en pizarra: **Rol + Contexto + Tarea + Formato + Límite** (la semilla del prompt).
- **Key takeaway:** *La magia no está en el modelo, está en cómo le explicas tu chamba.*

📊 **Slides: 5** (Mit vs Real · El practicante · Los 5 ingredientes · Ejemplo malo vs bueno · “No necesitas API aún”)

---

### 🔵 Bloque 2 · Demo en vivo: *De idea a asistente en 7 min* · 25 min
- **Objetivo:** Ver que SÍ se puede, en tiempo real, sin código.
- **Dinámica:** **Demo en vivo (sin slides)**. El facilitador toma un dolor del rompehielo (ej: *“responder preguntas de precios por IG”*) y construye:
  1. Prompt con los 5 ingredientes
  2. Un **GPT personalizado** (o Claude Project / Gem) con 3 FAQs pegadas
  3. Lo prueba con un mensaje real inventado por alguien del público 🎤
  4. Bonus relámpago: conecta ese asistente a un Google Sheet con Make (solo visual, 2 min)
- **Key takeaway:** *Si lo hice en 7 minutos con un post-it, tú lo haces en 45.*

📊 **Slides: 2** (Solo “Modo demo 🛠️” + QR al template)

---

### ☕ Pausa activa · 15 min
- Café, agua, moverse.  
- **Dinámica relámpago:** *“Gira y dile a alguien: ‘mi asistente va a hacer ___’”* (30 seg c/u).  
- El facilitador reparte los stickers ✅ y acomoda mesas de 5.

---

### 🟣 Bloque 3 · EJERCICIO PRINCIPAL · 45 min ⭐
- **Objetivo:** Que **cada persona salga con un asistente funcionando**.
- **Dinámica:** Trabajo individual + acompañamiento de copilotos. Ver detalle abajo 👇.
- **Key takeaway:** *Ya no estás “aprendiendo IA”. Ya tienes un empleado digital probado.*

📊 **Slides: 4** (Timer gigante · Canvas en pantalla · “Si te trabas, levanta la mano” · Checklist de entrega)

---

### 🟠 Bloque 4 · Show & Tell · 25 min
- **Objetivo:** Socializar, inspirar y destilar aprendizajes del grupo.
- **Dinámica:** 3 voluntarios (elegidos por “el más raro / el más útil / el que falló bonito”) muestran:
  - El prompt (30 seg)
  - Un input real → output real (1 min)
  - *“Lo que me sorprendió”* (30 seg)
  - Ronda de 1 aplauso + 1 pregunta del público por caso.
- **Key takeaway:** *Los mejores asistentes no son los más complejos, son los que resuelven lo de siempre.*

📊 **Slides: 2** (Plantilla de feedback: 👏 / 🤔 / 🔁 + “Los 3 patrones que vimos”)

---

### 🔴 Bloque 5 · *“Cuidado con el casi funciona”* · 20 min
- **Objetivo:** Evitar el clásico error LATAM: confiarle datos de clientes al chat sin filtro.
- **Dinámica:** Discusión rápida con 3 “tarjetas de riesgo” que se leen en voz alta:
  1. 🧾 **Datos reales** → “Nunca pegues RUT / DNI / tarjetas / contratos completos”
  2. 🎭 **Alucinación** → “Si inventa un precio, tú lo revisas. Siempre.”
  3. 🧍 **Tono** → “¿Suena a tu marca o a un call center de 2005?”
  - Mini-fix en vivo: agregar al prompt → *“Si no sabes, responde: ‘Te lo confirmo con el equipo en 2 min’ ”*
- **Key takeaway:** *Un asistente confiable no es el que más sabe, es el que sabe cuándo callarse.*

📊 **Slides: 4** (3 tarjetas · La frase salvadora · Checklist “Antes de mandarlo a un cliente” · QR a la guía)

---

### 🏁 Bloque 6 · Cierre: Roadmap 7 días + Compromiso · 15 min
- **Objetivo:** Que no muera en el slide final.
- **Dinámica:** Cada persona escribe en el dorso del Canvas:  
  > *“El lunes a las 9am le paso ___ a mi asistente”*  
  Se pega en la pared de salida 📌 → foto grupal → se lee el compromiso de 2 personas en voz alta.
- **Key takeaway:** *No te vas con un certificado. Te vas con una tarea menos para mañana.*

📊 **Slides: 3** (Roadmap 7 días · QR de recursos · “Gracias, nos vemos en el grupo 📲”)

---

## 4️⃣ ⭐ Ejercicio Principal (todos lo terminan, sin código)

**Nombre:** *“Mi primer empleado digital (en 45 min)”*

**Herramienta:** ChatGPT (Custom GPT / Proyecto) · Claude (Project) · Gemini (Gem) → **elige uno, no importa cuál**.  
**Zero integraciones obligatorias** (Make/Zapier es opcional para los que vuelan).

### Canvas del Asistente (A3 impreso, 5 casillas)

| Casilla | Pregunta guía | Ejemplo real |
|---|---|---|
| 1️⃣ **Nombre** | ¿Cómo se llama? | *Rosi, la de precios* |
| 2️⃣ **Rol** | ¿Quién es? | *Encargada de responder dudas de planes de CaféFit* |
| 3️⃣ **Contexto** | Pega 3–5 frases reales (FAQs, tono, precios) | *“Somos una suscripción de café en Medellín. Plan Básico $29k… Hablamos de vos, sin emoji excesivo.”* |
| 4️⃣ **Tarea + Formato** | ¿Qué hace y cómo entrega? | *Responde en máx. 3 líneas, siempre cierra con ‘¿Te lo aparto? ☕’* |
| 5️⃣ **Límite** | ¿Qué NO debe hacer? | *Si no sabe el precio → ‘Te lo confirmo con el equipo en 2 min’. Nunca inventes descuentos.* |

### Secuencia guiada (el facilitador marca tiempos en voz alta)

| Min | Acción |
|---|---|
| 0–5 | Elegir **1 solo dolor** del post-it inicial (no el negocio entero 🙏) |
| 5–15 | Llenar el Canvas a mano (lápiz, sí, a mano → baja la fricción) |
| 15–25 | Pasar el Canvas a la herramienta → crear el asistente / proyecto |
| 25–35 | **Probar con 3 mensajes reales**: 1 fácil, 1 raro, 1 “tramposo” |
| 35–42 | Ajustar **una sola cosa** del prompt (la que falló) y volver a probar |
| 42–45 | Pegar sticker ✅ + escribir el compromiso del lunes al dorso |

> 🧑‍💻 **Regla de oro del facilitador:** *Si alguien se traba más de 90 seg, el copiloto no le explica… le escribe la primera línea del prompt con él. Se aprende haciendo.*

**Entregable tangible:** Asistente publicado (link privado) + Canvas firmado + 1 screenshot del output bueno 📸.

---

## 5️⃣ Recursos para llevar a casa 🎒

Todo en **1 solo QR** (usa un Linktree / Notion público / PDF en Drive):

1. 📄 **Canvas del Asistente** (PDF A3 + versión editable en Canva / Notion)
2. 🧩 **Plantilla de prompt** (los 5 ingredientes, copiar-pegar, con ejemplo LATAM)
3. 🛠️ **Cheatsheet: “ChatGPT vs Claude vs Gemini para no-técnicos”** (1 página, cuándo usar cada uno)
4. ⚠️ **Checklist pre-cliente** (7 ítems: datos, tono, alucinación, fallback, firma…)
5. 🗓️ **Roadmap 7 días**  
   - D1: úsalo tú · D2: pásale 5 casos reales · D3: ajusta el límite · D4: muéstralo a tu cofounder · D5: conecta un Sheet (opcional) · D6: mide cuántos minutos ahorraste · D7: cuéntalo en el grupo 📲
6. 💬 **Grupo de WhatsApp / Slack del workshop** (se abre ahí mismo, se comparte el QR en la última slide)
7. 🎥 **Grabación de la demo (2 min, celular, sin editar)** → subida al drive esa misma noche

> Bonus criollo: una **“Playlist del Taller”** de Spotify para que la vuelvan a poner el lunes mientras laburan 🎧

---

## 6️⃣ Slide Count Estimado

| Sección | Slides |
|---|---|
| Bienvenida & Rompehielo | 3 |
| Bloque 1 · IA sin humo | 5 |
| Bloque 2 · Demo (casi sin slides) | 2 |
| Pausa (pantalla timer) | 1 |
| Bloque 3 · Ejercicio | 4 |
| Bloque 4 · Show & Tell | 2 |
| Bloque 5 · Límites | 4 |
| Cierre & Recursos | 3 |
| **TOTAL** | **~24 slides** |

> 💡 Regla de facilitador: **máximo 24, mínimo 18**. Si pasas de 25 en un taller práctico, la gente deja de mirar la pantalla y empieza a mirar el reloj ⏰.

---

## 🧠 Notas finales para vos (facilitador LATAM)

- **No corrijas el español técnico.** Si dicen “le puse un prompt medio así nomás”, está perfecto.
- **Celebrá el error en voz alta:** *“¡Miren, acá inventó un descuento! Eso es oro, ya sabemos qué poner en el límite.”*
- **Nunca digas “API” antes del minuto 150.** Si alguien la menciona, sonreí: *“Eso es para el sábado, hoy primero que funcione.”*
- **Cerrá con energía, no con resumen.** Que el último ruido del salón sea un sticker pegándose en la pared, no un “¿alguna pregunta?”.

¿Querés que te arme también el **guion literal del facilitador** (frases exactas para la demo y el rompehielo) o el **PDF del Canvas listo para imprimir**? Lo saco en un toque ☕🚀