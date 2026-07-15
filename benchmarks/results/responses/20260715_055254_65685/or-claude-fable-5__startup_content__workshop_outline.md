# Claude Fable 5 — startup_content/workshop_outline

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.77 | quality: 10.0
- latency_total: 74.975s | tokens_per_second: 73.8
- input_tokens: 314 | output_tokens: 5536
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada, materiales necesarios y un desglose de bloques que facilitan la creación de un asistente de IA.

## Respuesta completa

# 🚀 Construye tu Asistente de IA para tu Startup
## Workshop Práctico – 3 horas | 20-30 emprendedores early-stage no-técnicos

---

## 🎯 Objetivo General del Workshop

Que cada participante salga con **un asistente de IA funcionando** (creado por ellos mismos), configurado para una tarea real de su startup, y con la confianza de seguir iterándolo solos.

**Promesa del workshop:** "Llegas con un problema, te vas con un asistente que trabaja para ti."

---

## 📋 1. AGENDA DETALLADA (180 minutos)

| Hora | Bloque | Duración |
|------|--------|----------|
| 0:00 – 0:15 | Bienvenida + Rompehielos "Tu tarea más odiada" | 15 min |
| 0:15 – 0:35 | Bloque 1: IA sin humo – Qué es y qué NO es | 20 min |
| 0:35 – 1:00 | Bloque 2: Anatomía de un buen prompt (Demo en vivo) | 25 min |
| 1:00 – 1:15 | Bloque 3: Define la misión de tu asistente | 15 min |
| 1:15 – 1:25 | ☕ BREAK + Networking dirigido | 10 min |
| 1:25 – 2:25 | Bloque 4: EJERCICIO PRINCIPAL – Construye tu asistente | 60 min |
| 2:25 – 2:45 | Bloque 5: Demo Day Express – Muestra tu asistente | 20 min |
| 2:45 – 3:00 | Cierre: Próximos pasos + Recursos + Foto grupal | 15 min |

---

## 🛠️ 2. MATERIALES NECESARIOS (Preparar ANTES)

### Logística / Espacio
- [ ] Salón con mesas para trabajo en grupos de 4-5 (no auditorio)
- [ ] WiFi robusto (probar con 30 dispositivos simultáneos — crítico)
- [ ] Proyector + pantalla + adaptadores HDMI/USB-C
- [ ] Micrófono si el espacio es grande
- [ ] Multicontactos/extensiones en cada mesa (los laptops se descargan)
- [ ] Café, agua y snacks para el break

### Digital (preparar 1 semana antes)
- [ ] Instructivo pre-workshop enviado por email: "Trae laptop + crea tu cuenta gratuita en [Claude / ChatGPT / Gemini]"
- [ ] Cuentas de respaldo por si alguien no la creó (siempre pasa, prepara 5-6)
- [ ] Plantilla del ejercicio en Google Docs (link corto + QR)
- [ ] Presentación de slides
- [ ] Grupo de WhatsApp del workshop creado (QR para unirse)
- [ ] 3 asistentes de IA de ejemplo ya construidos para la demo

### Impresos
- [ ] Hoja de trabajo "Canvas de mi Asistente" (1 por persona) — el corazón del ejercicio
- [ ] Cheat sheet de prompting (1 por persona, para llevar)
- [ ] Carteles con QR del grupo de WhatsApp y recursos

### Equipo humano
- [ ] Idealmente 1-2 co-facilitadores o voluntarios que circulen ayudando durante el ejercicio (ratio ideal: 1 ayudante por cada 10 personas)

---

## 📚 3. DESGLOSE POR BLOQUES

---

### ⚡ APERTURA: Bienvenida + "Tu Tarea Más Odiada" (15 min)

**Objetivo:** Romper el hielo, generar energía y conectar la IA con un dolor real de cada participante desde el minuto uno.

**Dinámica:** Ejercicio rápido
- 2 min: Bienvenida energética + regla del workshop: "Aquí no hay preguntas tontas, hay preguntas que 15 personas más tienen"
- 5 min: Cada persona escribe en un post-it la tarea repetitiva que más odia de su startup (responder correos, hacer posts, cotizaciones, etc.)
- 5 min: 4-5 voluntarios comparten en voz alta
- 3 min: Facilitador conecta: "Hoy vamos a construir un asistente que ataque exactamente eso"

**Key takeaway:** *La IA no es para "algún día", es para el dolor que escribiste en ese post-it.*

**Slides:** 4 (portada, agenda, reglas, instrucción del post-it)

---

### 🧠 BLOQUE 1: IA sin Humo – Qué es y qué NO es (20 min)

**Objetivo:** Desmitificar la IA generativa y calibrar expectativas realistas sin tecnicismos.

**Dinámica:** Charla interactiva con votación a mano alzada
- Analogía central: "Un LLM es como un empleado brillante recién llegado: sabe muchísimo del mundo, pero NADA de tu startup. Tu trabajo es darle contexto."
- Mini-quiz de mitos (mano alzada): "¿La IA sabe si lo que dice es verdad?" "¿Se puede equivocar con total confianza?"
- 3 casos reales de startups latinoamericanas usando asistentes de IA (atención a clientes, contenido, análisis de feedback)
- Los 3 riesgos que sí importan: alucinaciones, datos sensibles, dependencia ciega

**Key takeaway:** *La IA es un becario genio con amnesia: el valor está en cómo TÚ le das contexto e instrucciones.*

**Slides:** 8

---

### 🔧 BLOQUE 2: Anatomía de un Buen Prompt (Demo en Vivo) (25 min)

**Objetivo:** Que entiendan la diferencia dramática entre un prompt flojo y uno bien estructurado, viéndolo en pantalla en tiempo real.

**Dinámica:** Demo en vivo + framework
- 5 min: Presentar el framework **R.C.T.F.** (fácil de recordar):
  - **R**ol → "Eres un experto en..."
  - **C**ontexto → "Mi startup hace... mi cliente es..."
  - **T**area → "Necesito que..."
  - **F**ormato → "Entrégalo como... con este tono..."
- 12 min: **Demo en vivo** con caso real: "Escribe un post de Instagram para mi startup" (prompt flojo) vs. el mismo pedido con R.C.T.F. → el contraste vende solo
- 5 min: Segunda demo: cómo iterar ("hazlo más corto", "usa un tono más cercano", "dame 3 versiones")
- 3 min: Preguntas rápidas

**Key takeaway:** *No necesitas saber programar. Necesitas saber pedir. R.C.T.F. es tu fórmula.*

**Slides:** 6 (el resto es pantalla en vivo)

---

### 🎯 BLOQUE 3: Define la Misión de tu Asistente (15 min)

**Objetivo:** Que cada participante aterrice QUÉ va a construir antes de tocar el teclado (evita la parálisis de la hoja en blanco).

**Dinámica:** Ejercicio individual con hoja impresa ("Canvas de mi Asistente")
- Cada quien llena en papel:
  1. ¿Qué tarea odiosa va a resolver mi asistente? (recuperar el post-it)
  2. ¿Quién es mi cliente / mi startup en una frase?
  3. ¿Qué tono debe tener? (formal, cercano, vendedor...)
  4. ¿Cómo se ve un resultado exitoso? (un ejemplo concreto)
- 3 min: Compartir con la persona de al lado (peer feedback express)

**Key takeaway:** *Un asistente sin misión clara es un chatbot genérico. Primero papel, luego teclado.*

**Slides:** 3

---

### ☕ BREAK + Networking Dirigido (10 min)

Consigna: "Toma tu café con alguien que NO conoces y cuéntale qué asistente vas a construir." (El networking también se diseña.)

**Slides:** 1 (con timer y consigna en pantalla)

---

### 🏗️ BLOQUE 4: EJERCICIO PRINCIPAL – Construye tu Asistente (60 min)

**Objetivo:** Que cada participante construya, pruebe e itere un asistente de IA funcional para su startup. **Este es el corazón del workshop** (ver detalle completo en sección 4).

**Dinámica:** Ejercicio guiado individual, con facilitadores circulando
- Fase 1 (15 min): Redactar el "system prompt" / instrucciones maestras usando la plantilla
- Fase 2 (15 min): Primera prueba con casos reales de su startup
- Fase 3 (20 min): Iterar — corregir tono, agregar contexto, afinar formato
- Fase 4 (10 min): Prueba cruzada — tu compañero de mesa usa tu asistente como si fuera tu cliente

**Key takeaway:** *La primera versión nunca es la buena. Construir un asistente es iterar, no acertar.*

**Slides:** 5 (instrucciones de cada fase, con timer visible)

---

### 🎤 BLOQUE 5: Demo Day Express (20 min)

**Objetivo:** Celebrar los logros, mostrar la variedad de casos de uso e inspirar con lo que crearon sus pares.

**Dinámica:** Presentaciones relámpago
- 5-6 voluntarios pasan al frente (2-3 min cada uno): muestran su asistente en pantalla, cuentan qué resuelve y qué fue lo más difícil
- Aplausos obligatorios 👏 (la energía importa)
- Facilitador destaca 1 aprendizaje de cada demo

**Key takeaway:** *Si ellos pudieron en 60 minutos, imagina lo que puedes hacer con esto en tu semana.*

**Slides:** 2

---

### 🏁 CIERRE: Próximos Pasos + Recursos (15 min)

**Objetivo:** Convertir el impulso del workshop en acción sostenida los próximos 7 días.

**Dinámica:** Charla de cierre + compromiso público
- El "Reto de los 7 días": usar tu asistente todos los días esta semana con tareas reales
- Recorrido rápido por los recursos para llevar a casa (QR en pantalla)
- Cada persona escribe en el grupo de WhatsApp: "Mi asistente se llama ___ y esta semana lo usaré para ___"
- Foto grupal + agradecimientos

**Key takeaway:** *El workshop termina hoy; tu asistente empieza a trabajar mañana.*

**Slides:** 5

---

## 🏋️ 4. EJERCICIO PRINCIPAL (Detalle Completo)

### "Mi Primer Asistente de IA" — 60 minutos

**Herramienta:** Claude (Projects), ChatGPT (GPTs/instrucciones personalizadas) o Gemini (Gems) — cuenta gratuita suficiente. Elegir UNA plataforma principal para el workshop y dominar esa demo.

**Plantilla que llenan (la base del system prompt):**

```
Eres [ROL: asistente de atención al cliente / redactor / analista...]
de [NOMBRE DE MI STARTUP], que se dedica a [QUÉ HACE en 1-2 frases].

Nuestros clientes son [DESCRIPCIÓN DEL CLIENTE].
Nuestro tono es [3 adjetivos: ej. cercano, profesional, directo].

Tu trabajo es [TAREA PRINCIPAL].

Reglas:
- Siempre [regla 1: ej. responde en español neutro]
- Nunca [regla 2: ej. prometas descuentos]
- El formato de tus respuestas debe ser [FORMATO]

Ejemplo de una buena respuesta:
[PEGAR UN EJEMPLO REAL]
```

**Casos de uso sugeridos** (para quien se traba):
1. 📧 Asistente que responde correos/mensajes de clientes
2. 📱 Generador de contenido para redes sociales
3. 💰 Redactor de cotizaciones y propuestas
4. 🔍 Analista de feedback de clientes
5. 📝 Asistente de pitch: mejora tu descripción para inversionistas

**Criterio de éxito:** Al final de los 60 minutos, el asistente debe pasar la "prueba del compañero": otra persona lo usa con un caso real y obtiene un resultado útil sin que el creador intervenga.

**Rol de los facilitadores:** circular constantemente, desbloquear a quienes se traban, y detectar 2-3 casos brillantes para el Demo Day.

---

## 🎁 5. RECURSOS PARA LLEVAR A CASA

Entregar vía QR + grupo de WhatsApp (y el cheat sheet impreso):

1. **Cheat Sheet de Prompting R.C.T.F.** (PDF 1 página, también impreso)
2. **Plantilla "Canvas de mi Asistente"** editable en Google Docs
3. **Banco de 20 prompts probados** para startups (ventas, marketing, operaciones, pitch)
4. **Guía paso a paso con capturas:** cómo crear tu asistente en Claude/ChatGPT/Gemini (para replicar en casa)
5. **Checklist de seguridad:** qué datos NUNCA subir a una IA
6. **El Reto de los 7 días:** mini-calendario con una tarea diaria para consolidar el hábito
7. **Grupo de WhatsApp de la comunidad** para dudas y compartir avances
8. **Grabación de las slides / material** enviado por email en 48 horas

---

## 📊 6. SLIDE COUNT ESTIMADO

| Sección | Slides |
|---------|--------|
| Apertura + rompehielos | 4 |
| Bloque 1: IA sin humo | 8 |
| Bloque 2: Anatomía del prompt | 6 |
| Bloque 3: Misión del asistente | 3 |
| Break | 1 |
| Bloque 4: Ejercicio principal | 5 |
| Bloque 5: Demo Day | 2 |
| Cierre + recursos | 5 |
| **TOTAL** | **~34 slides** |

> 💡 Regla de oro: en un workshop práctico, las slides son señalización, no contenido. Máximo 20 palabras por slide. La acción está en las pantallas de los participantes, no en la tuya.

---

## ⚠️ Tips del Facilitador (bonus)

- **Plan B sin WiFi:** ten capturas de pantalla de todas las demos por si internet falla
- **Timers visibles** en pantalla durante cada fase del ejercicio — mantienen la energía
- **No rescates demasiado rápido:** deja que iteren y se equivoquen 5 minutos antes de intervenir; ahí está el aprendizaje
- **Los no-técnicos se intimidan al inicio:** los primeros 10 minutos del ejercicio son críticos, circula intensamente ahí
- Encuesta de salida de 3 preguntas (QR en la última slide) para mejorar la próxima edición

¿Quieres que desarrolle alguno de los materiales en detalle (el cheat sheet, la guía paso a paso, o el guion palabra por palabra de la demo en vivo)?