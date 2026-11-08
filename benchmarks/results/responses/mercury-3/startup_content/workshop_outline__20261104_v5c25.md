# Mercury 3 — startup_content/workshop_outline

- model_id: `inception/mercury-3`
- success: True  | final: 8.89 | quality: 9.72
- latency_total: 6.488s | tokens_per_second: 457.6
- input_tokens: 211 | output_tokens: 2969
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

# 🚀 Construye tu Asistente de IA para tu Startup — Workshop Práctico

**Duración total:** 3 horas | **Formato:** Presencial | **Audiencia:** 20–30 emprendedores early-stage no-técnicos

---

## 📋 Agenda General (3 horas)

| # | Bloque | Duración | Hora aprox. |
|---|--------|----------|-------------|
| 1 | Bienvenida + Icebreaker | 15 min | 0:00–0:15 |
| 2 | IA para no-técnicos: El ABC | 25 min | 0:15–0:40 |
| 3 | Demo en vivo: 3 asistentes reales | 20 min | 0:40–1:00 |
| 4 | **Pausa / Networking** | 10 min | 1:00–1:10 |
| 5 | Ejercicio principal: Construye tu asistente | 60 min | 1:10–2:10 |
| 6 | Presentaciones relámpago | 30 min | 2:10–2:40 |
| 7 | Cierre + Q&A + Recursos | 20 min | 2:40–3:00 |

---

## 🧰 Materiales Necesarios (Preparar Antes)

### Para el facilitador
- [ ] Laptop con proyector conectado y probado (con adaptador HDMI/USB-C)
- [ ] Slides listas en Google Slides o PowerPoint (ver conteo por sección)
- [ ] Cuenta de ChatGPT Plus, Claude Pro y Gemini Advanced abiertas en pestañas separadas
- [ ] Conexión a internet estable con backup (hotspot móvil)
- [ ] Micrófono de solapa o manos libres (si la sala es grande)
- [ ] Cronómetro visible para el ejercicio principal
- [ ] Playlist de música energética de fondo (volumen bajo)

### Para los participantes
- [ ] Laptop o tablet (mínimo 10 participantes con laptop para trabajo en grupos)
- [ ] Cuenta gratuita de ChatGPT o Claude creada previamente (enviar instrucciones por email 48h antes)
- [ ] Block de notas físico + lapiceros
- [ ] Post-its de colores (3 colores por persona)
- [ ] Stickers o premios pequeños (para ganadores de presentaciones)

### Para la sala
- [ ] Mesas para 5–6 grupos de 4–5 personas
- [ ] Pizarra blanca o flipchart con marcadores
- [ ] WiFi con acceso para invitados (probar velocidad antes)
- [ ] Agua y snacks ligeros

---

## 📝 Desglose de Bloques

### Bloque 1: Bienvenida + Icebreaker
**Duración:** 15 min | **Formato:** Charla + Dinámica

**Objetivo:** Romper el hielo, conectar a los participantes y crear energía positiva.

**Dinámica — "Mi Startup en 3 Emojis":**
- Cada persona se presenta en 20 segundos con su nombre, su startup, y 3 emojis que la representen.
- El facilitador anota en la pizarra los emojis más repetidos y los conecta con el tema del día.

**Key takeaway:** *Todos están en el mismo barco: aprendiendo y construyendo con lo que tienen.*

**Slide count:** 2 slides (título + instrucciones icebreaker)

---

### Bloque 2: IA para no-técnicos — El ABC
**Duración:** 25 min | **Formato:** Charla interactiva

**Objetivo:** Desmitificar la IA y dar un marco mental claro para que los emprendedores entiendan qué pueden construir sin saber programar.

**Contenido clave:**
- **El mito vs. la realidad:** No necesitas ser ingeniero para usar IA.
- **Los 3 tipos de IA que te importan:**
  - *Chatbots* (responden preguntas)
  - *Asistentes* (ejecutan tareas)
  - *Automatizaciones* (conectan herramientas)
- **El concepto de "Prompt Engineering" para no-técnicos:** hablar con la IA como hablarías con un asistente humano.
- **Lo que SÍ y NO puedes hacer sin código** (tabla visual clara).

**Dinámica — "¿Qué puedo automatizar?"**
- El facilitador pregunta: *"¿Qué tarea repetitiva odias hacer en tu startup?"*
- Los participantes gritan respuestas; el facilitador las escribe en la pizarra.
- Luego elige 3 y explica cómo un asistente de IA podría resolverlas.

**Key takeaway:** *La IA es una herramienta de productividad, no un reemplazo de tu equipo. Si puedes explicarlo, puedes construirlo.*

**Slide count:** 6 slides (mito vs realidad, 3 tipos de IA, prompt engineering, qué sí/no, ejemplos, transición)

---

### Bloque 3: Demo en Vivo — 3 Asistentes Reales
**Duración:** 20 min | **Formato:** Demo + Discusión

**Objetivo:** Mostrar ejemplos concretos de asistentes construidos con herramientas no-code para inspirar y demostrar posibilidades reales.

**Demostraciones (preparadas antes):**

1. **"Soporte al Cliente" — Chatbot con ChatGPT + Zapier**
   - Demo: Un cliente pregunta por el estado de su pedido.
   - El asistente responde automáticamente usando datos de una hoja de cálculo.
   
2. **"Asistente de Ventas" — Claude + Google Sheets**
   - Demo: El asistente califica leads según criterios y envía correos personalizados.
   
3. **"Asistente de Contenido" — Gemini + Notion**
   - Demo: Genera un calendario de contenido para Instagram basado en la marca.

**Discusión guiada:**
- ¿Qué vieron que les sorprendió?
- ¿Cuál de estos asistentes se parece más a lo que necesitan?

**Key takeaway:** *Estos asistentes los construyó una persona sin código en menos de 2 horas cada uno. Tú también puedes.*

**Slide count:** 3 slides (una por demo con capturas de pantalla)

---

### Bloque 4: Pausa / Networking
**Duración:** 10 min | **Formato:** Libre

**Objetivo:** Que los participantes se conozcan, compartan ideas y recarguen energía.

**Dinámica sugerida:** Poner música y pedir que cada persona hable con alguien que no conozca sobre "la tarea más aburrida de su startup".

**Key takeaway:** *El networking es parte del aprendizaje.*

**Slide count:** 1 slide (pantalla de "vuelve en 10 min" con música)

---

### Bloque 5: 🎯 Ejercicio Principal — Construye tu Asistente
**Duración:** 60 min | **Formato:** Taller práctico en grupos

**Objetivo:** Que cada participante diseñe y prototipe un asistente de IA para su startup usando herramientas no-code.

**Estructura del ejercicio:**

| Tiempo | Actividad |
|--------|-----------|
| 5 min | Instrucciones + ejemplo rápido del facilitador |
| 15 min | **Fase 1:** Definir el problema y el usuario (plantilla) |
| 20 min | **Fase 2:** Diseñar el prompt y el flujo del asistente |
| 15 min | **Fase 3:** Probar con ChatGPT/Claude y iterar |
| 5 min | Preparar presentación de 1 minuto |

**Plantilla entregada (impresa):**
```
📋 PLANTILLA: MI ASISTENTE DE IA

1. Nombre del asistente: _______
2. ¿Qué problema resuelve? _______
3. ¿Quién es el usuario? _______
4. ¿Qué puede hacer? (3 acciones máx.) _______
5. Prompt inicial (escribe el prompt que usarías): _______
6. ¿Qué herramientas usarías? (ChatGPT, Claude, Zapier, etc.): _______
7. ¿Cómo medirías su éxito? _______
```

**Dinámica de grupos:**
- Grupos de 4–5 personas (según mesas).
- Cada persona trabaja en su propio asistente, pero recibe feedback del grupo.
- El facilitador circula ayudando y sugiriendo mejoras de prompts.

**Key takeaway:** *En 60 minutos puedes pasar de "no tengo idea" a "tengo un prototipo funcional".*

**Slide count:** 4 slides (instrucciones, plantilla, ejemplo, tips de prompts)

---

### Bloque 6: Presentaciones Relámpago
**Duración:** 30 min | **Formato:** Presentaciones + Votación

**Objetivo:** Que los participantes compartan sus asistentes, reciban feedback y celebren logros.

**Dinámica:**
- 5–6 voluntarios presentan su asistente en 1 minuto cada uno.
- El público vota con stickers por el asistente más creativo, el más práctico y el más "quiero eso ya".
- Los 3 ganadores reciben premios pequeños (stickers, libros, etc.).

**Key takeaway:** *Lo que construiste hoy es real y tiene valor. Compártelo con el mundo.*

**Slide count:** 2 slides (instrucciones + sistema de votación)

---

### Bloque 7: Cierre + Q&A + Recursos
**Duración:** 20 min | **Formato:** Charla + Discusión abierta

**Objetivo:** Consolidar aprendizajes, resolver dudas finales y entregar recursos útiles.

**Contenido:**
- Resumen de los 3 aprendizajes clave del día.
- Q&A abierto (10 min).
- Entrega de recursos para llevar a casa.
- Invitación a la comunidad / próximo evento.

**Key takeaway:** *Hoy diste el primer paso. La IA es una habilidad que se aprende haciendo.*

**Slide count:** 3 slides (resumen, recursos, contacto/comunidad)

---

## 🏠 Recursos para Llevar a Casa

### Guía rápida de herramientas (entregar impreso o por email)

| Herramienta | Uso | Costo |
|-------------|-----|-------|
| **ChatGPT** | Chatbot + generación de texto | Gratis / $20 mes |
| **Claude** | Asistente más "conversacional" | Gratis / $20 mes |
| **Gemini** | Integración con Google Workspace | Gratis |
| **Zapier** | Conectar apps y automatizar | Gratis / desde $20 mes |
| **Make (Integromat)** | Alternativa a Zapier | Gratis / desde $9 mes |
| **Notion AI** | Base de conocimiento + IA | Desde $10 mes |
| **Voiceflow** | Crear chatbots visualmente | Gratis / desde $30 mes |

### Plantilla de Prompt (entregar impresa)

```
🎯 PLANTILLA DE PROMPT PARA TU ASISTENTE

"Eres [rol] que ayuda a [tipo de usuario] con [problema].
Tu tono es [amigable/profesional/divertido].
Cuando te pidan [acción], debes [comportamiento esperado].
Si no sabes algo, responde: [frase de fallback].
Empieza siempre con: [frase inicial]."
```

### Checklist de próximos pasos (30 días)
- [ ] Probar 3 herramientas diferentes esta semana
- [ ] Construir un segundo prototipo con feedback real de clientes
- [ ] Unirse a la comunidad del workshop (grupo de WhatsApp/Telegram)
- [ ] Agendar una sesión de mentoria de 30 min (link de reserva)

### Lecturas recomendadas
- *"The AI-Powered Business"* — guía corta para no-técnicos
- *"Prompt Engineering for Beginners"* — PDF gratuito
- Artículo: "10 asistentes de IA que puedes construir sin código" (link)

---

## 📊 Conteo Total de Slides

| Sección | Slides |
|---------|--------|
| Bienvenida + Icebreaker | 2 |
| IA para no-técnicos | 6 |
| Demo en vivo | 3 |
| Pausa | 1 |
| Ejercicio principal | 4 |
| Presentaciones relámpago | 2 |
| Cierre + Recursos | 3 |
| **Total** | **21 slides** |

---

## 💡 Tips para el Facilitador

1. **Energía:** Comienza con música y saluda personalmente a los primeros 5 participantes que lleguen.
2. **Flexibilidad:** Si el ejercicio principal toma más tiempo, recorta la demo a 15 min.
3. **Inclusividad:** Asegúrate de que nadie se quede atrás — circula y ayuda activamente.
4. **Conexión:** Usa ejemplos de startups latinoamericanas reales (Rappi, Kavak, Platzi, etc.).
5. **Cierre memorable:** Termina con una frase inspiradora y una foto grupal.

---

## 🎯 Resumen de Key Takeaways

> **"La IA no es magia. Es una herramienta que puedes aprender a usar hoy. Si puedes explicar el problema, puedes construir el asistente."**

---

*Workshop diseñado para ser práctico, energético y transformador. ¡A construir! 🚀*