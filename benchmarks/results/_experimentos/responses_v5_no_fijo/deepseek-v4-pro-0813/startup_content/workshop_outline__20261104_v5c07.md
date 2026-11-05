# DeepSeek V4 Pro (0813) — startup_content/workshop_outline

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 42.055s | tokens_per_second: 110.3
- input_tokens: 268 | output_tokens: 4639
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que se ajusta perfectamente a las necesidades de emprendedores no técnicos, proporcionando información práctica y útil.

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

# WORKSHOP: "Construye tu Asistente de IA para tu Startup"
## Workshop Práctico Presencial | 3 Horas | 20-30 Emprendedores No-Técnicos

---

## 1. AGENDA DETALLADA

| Hora | Bloque | Duración |
|------|--------|----------|
| 0:00 - 0:15 | Apertura + Icebreaker | 15 min |
| 0:15 - 0:35 | Bloque 1: IA para Startups (contexto) | 20 min |
| 0:35 - 1:05 | Bloque 2: Anatomía de un Asistente IA | 30 min |
| 1:05 - 1:20 | ☕ Break + Setup técnico | 15 min |
| 1:20 - 2:20 | Bloque 3: MANOS A LA OBRA (Ejercicio principal) | 60 min |
| 2:20 - 2:45 | Bloque 4: Showcase + Feedback | 25 min |
| 2:45 - 3:00 | Cierre + Recursos + Next Steps | 15 min |

---

## 2. MATERIALES NECESARIOS (Checklist Pre-Workshop)

### Infraestructura
- [ ] Sala con mesas en formato islas (4-5 personas por mesa)
- [ ] Proyector + pantalla grande
- [ ] WiFi estable (¡CRÍTICO! Mínimo 50 Mbps, probar antes)
- [ ] Extensiones eléctricas / regletas por mesa
- [ ] Micrófono inalámbrico para el facilitador
- [ ] Pizarra o papelógrafo + marcadores

### Digital (Preparar antes)
- [ ] Cuenta ChatGPT Plus o Claude Pro del facilitador (para demos en vivo)
- [ ] 5-6 cuentas de prueba gratuitas creadas (una por mesa) para evitar fricción
- [ ] Plantilla Google Docs "Canvas del Asistente IA" (link acortado + QR)
- [ ] Carpeta Drive con prompts de ejemplo
- [ ] Grupo WhatsApp/Discord temporal del workshop
- [ ] Presentación cargada en el proyector

### Físico
- [ ] Tarjetas de colores (rojo/amarillo/verde) para pedir ayuda
- [ ] Post-its + marcadores por mesa
- [ ] Plantilla impresa del Canvas (1 por persona)
- [ ] Stickers para el showcase

### Facilitación
- [ ] 2-3 "roamers" (facilitadores de apoyo) para ayudar en mesas
- [ ] Timer visible en pantalla
- [ ] Playlist energética para breaks

---

## 3. BLOQUES DETALLADOS

---

### 🎬 APERTURA + ICEBREAKER
**Duración:** 15 minutos

**Objetivo:**
Romper el hielo, establecer energía alta y entender qué espera cada persona del workshop.

**Dinámica:**
1. **Bienvenida relámpago (3 min):** El facilitador se presenta con su historia de 30 segundos: "Soy [nombre], he ayudado a [X] startups a [Y], y hoy vamos a construir algo real."
2. **Icebreaker "IA en tu vida" (7 min):** Cada persona comparte en su mesa (30 segundos cada uno):
   - "¿Cuál es la herramienta de IA que más usas hoy?"
   - "¿Qué tarea de tu startup te quita más tiempo que crees que un asistente podría hacer?"
3. **Share-out (5 min):** 3-4 personas comparten al grupo. El facilitador toma nota en pizarra de los "dolores" mencionados (esto se usa después).

**Key Takeaway:**
> "Todos aquí pierden horas en tareas repetitivas. Hoy vamos a construir un asistente que las haga por ti."

**Slides estimados:** 3-4
- Portada
- Agenda del día
- Reglas de juego (teléfonos, participación, pedir ayuda)

---

### 🧠 BLOQUE 1: IA PARA STARTUPS (CONTEXTO)
**Duración:** 20 minutos

**Objetivo:**
Nivelar el terreno: que todos entiendan qué es posible HOY con IA sin ser técnicos.

**Dinámica:**
1. **Charla relámpago (12 min):**
   - Qué es un LLM en 2 minutos (analogía: "un becario brillante que lee todo internet pero necesita instrucciones claras")
   - Los 5 usos más comunes en startups early-stage:
     - Atención al cliente
     - Generación de contenido
     - Investigación de mercado
     - Automatización de procesos internos
     - Análisis de datos
   - Ejemplos REALES de startups latinoamericanas usando IA (3 casos concretos)
   
2. **Demo en vivo (8 min):**
   - El facilitador muestra un asistente ya construido funcionando
   - Ejemplo: "Este es un asistente que responde preguntas de clientes para una tienda online. Veamos qué pasa cuando le pregunto sobre devoluciones..."
   - Momento "wow": mostrar cómo el asistente maneja una pregunta compleja

**Key Takeaway:**
> "No necesitas saber programar para crear un asistente de IA que trabaje para tu startup. Solo necesitas saber QUÉ quieres que haga y CÓMO decírselo."

**Slides estimados:** 8-10
- Qué es un LLM (1)
- Los 5 usos (5)
- Casos de éxito (2-3)
- Transición a demo (1)

---

### 🔧 BLOQUE 2: ANATOMÍA DE UN ASISTENTE IA
**Duración:** 30 minutos

**Objetivo:**
Entender los componentes básicos de un asistente IA y cómo "entrenarlo" con instrucciones (prompts).

**Dinámica:**
1. **Charla interactiva (15 min):**
   - Los 3 componentes de un asistente:
     - **Personalidad/Voz:** cómo se comunica
     - **Conocimiento:** qué información tiene (contexto, documentos, datos)
     - **Instrucciones:** qué debe hacer y qué NO debe hacer
   - El arte del prompt: fórmula práctica
     - "Eres [ROL] para [CONTEXTO]. Tu objetivo es [OBJETIVO]. Cuando [SITUACIÓN], haz [ACCIÓN]. Nunca [LÍMITE]."
   - Ejemplos buenos vs. malos (side by side)

2. **Ejercicio rápido en mesas (10 min):**
   - Cada mesa recibe un escenario: "Eres el asistente de una cafetería que vende online"
   - En 5 minutos, escriben un prompt inicial usando la fórmula
   - Comparten 1-2 ejemplos al grupo

3. **Demo guiada (5 min):**
   - El facilitador toma un prompt de una mesa y lo prueba EN VIVO
   - Muestra cómo iterar: "Veamos qué pasa si le agrego esto..."

**Key Takeaway:**
> "Un buen asistente no es magia: es una buena instrucción. Si puedes explicar una tarea a un pasante, puedes crear un asistente de IA."

**Slides estimados:** 10-12
- Los 3 componentes (3)
- Fórmula del prompt (2)
- Ejemplos buenos vs malos (3)
- Ejercicio instrucciones (1)
- Demo en vivo (1-2)

---

### ☕ BREAK + SETUP TÉCNICO
**Duración:** 15 minutos

**Qué pasa aquí:**
- Break real de 10 minutos (música, café, estirar piernas)
- Los roamers ayudan a cada mesa a:
  - Acceder a la herramienta (ChatGPT/Claude)
  - Abrir la plantilla del Canvas
  - Confirmar que todos tienen acceso

**Key Takeaway:**
> *No hay takeaway formal, pero el objetivo es que TODOS estén listos para construir sin fricción.*

---

### 🚀 BLOQUE 3: MANOS A LA OBRA (EJERCICIO PRINCIPAL)
**Duración:** 60 minutos

**Objetivo:**
Que cada persona construya su propio asistente de IA funcional para su startup y lo pruebe en tiempo real.

**Dinámica:**
1. **Instrucciones (5 min):**
   - Explicar el ejercicio completo
   - Mostrar el Canvas del Asistente IA (plantilla)
   - Tiempos por fase

2. **Fase 1 - Definir (10 min):**
   - Cada persona completa el Canvas:
     - ¿Qué tarea quieres automatizar?
     - ¿Quién es el usuario/audiencia?
     - ¿Qué tono debe tener?
     - ¿Qué información necesita saber?
     - ¿Qué NO debe hacer?

3. **Fase 2 - Construir (20 min):**
   - Escriben su prompt completo en la herramienta
   - Los roamers circulan ayudando
   - Sistema de tarjetas: 🟢 voy bien, 🟡 tengo duda, 🔴 necesito ayuda

4. **Fase 3 - Probar (15 min):**
   - Cada persona "entrevista" a su asistente con 3-5 preguntas reales
   - Iteran el prompt basado en respuestas
   - Documentan qué funcionó y qué no

5. **Fase 4 - Refinar (10 min):**
   - Comparten en su mesa: "¿Qué cambiaste y por qué?"
   - Eligen 1 asistente por mesa para el showcase

**Key Takeaway:**
> "Acabas de crear algo que hace 3 años requería un equipo de ingenieros. Esto es solo el inicio."

**Slides estimados:** 5-6
- Instrucciones del ejercicio (2)
- Canvas visual (1)
- Timer visible (1)
- Tips de troubleshooting (1-2)

---

### 🏆 BLOQUE 4: SHOWCASE + FEEDBACK
**Duración:** 25 minutos

**Objetivo:**
Mostrar lo construido, aprender de otros y recibir feedback accionable.

**Dinámica:**
1. **Showcase (15 min):**
   - 5-6 mesas presentan su asistente (2 min por mesa)
   - Formato: "Nuestro asistente ayuda a [STARTUP] a [TAREA]. Le preguntamos [PREGUNTA] y respondió [RESPUESTA]. Lo más difícil fue [DESAFÍO]."
   - El facilitador comenta 1 cosa positiva + 1 sugerencia por presentación

2. **Votación (3 min):**
   - Todos votan con stickers por:
     - 🏆 Más útil
     - 🎨 Más creativo
     - ⚡ Más ambicioso

3. **Reflexión grupal (7 min):**
   - Preguntas disparadoras:
     - "¿Qué fue más difícil de lo que esperaban?"
     - "¿Qué descubrieron que no sabían que su asistente podía hacer?"
     - "¿Cómo podrían usar esto en su startup esta misma semana?"

**Key Takeaway:**
> "Miren lo que construyeron en 1 hora. Imaginen lo que pueden hacer en 1 mes iterando."

**Slides estimados:** 3-4
- Instrucciones showcase (1)
- Slides de premios (1)
- Preguntas de reflexión (1-2)

---

### 🎁 CIERRE + RECURSOS + NEXT STEPS
**Duración:** 15 minutos

**Objetivo:**
Consolidar el aprendizaje, entregar recursos accionables y motivar a seguir construyendo.

**Dinámica:**
1. **Recapitulación energética (5 min):**
   - "Hoy aprendieron: qué es un asistente IA, cómo funciona, y construyeron uno real"
   - Recordar los "dolores" del inicio: "¿Cuántos de esos dolores podrían resolverse con lo que construyeron hoy?"

2. **Recursos para llevar (5 min):**
   - Entregar el kit de recursos (ver sección 5)
   - Mostrar comunidad/grupo para seguir en contacto

3. **Next Steps (3 min):**
   - Reto de 7 días: "Implementa tu asistente en una tarea real de tu startup. Comparte resultados en el grupo."
   - Invitación a workshop avanzado (si aplica)

4. **Cierre motivacional (2 min):**
   - "La IA no va a reemplazar a los emprendedores. Los emprendedores que USAN IA van a reemplazar a los que no la usan. Ustedes ya dieron el primer paso."

**Key Takeaway:**
> "Esto no termina aquí. Tu asistente es un proyecto vivo. Úsalo, itera, mejóralo. Y comparte lo que aprendas."

**Slides estimados:** 4-5
- Resumen visual (1)
- Recursos (1-2)
- Reto 7 días (1)
- Cierre + contacto (1)

---

## 4. EJERCICIO PRINCIPAL DETALLADO

# "Construye tu Primer Asistente de IA"

### Canvas del Asistente IA (Plantilla)

| Componente | Pregunta Guía | Tu Respuesta |
|------------|---------------|--------------|
| **Tarea** | ¿Qué tarea específica quieres automatizar? | |
| **Audiencia** | ¿Quién interactuará con tu asistente? | |
| **Personalidad** | ¿Cómo debe comunicarse? (formal, casual, técnico, amigable) | |
| **Conocimiento** | ¿Qué información necesita saber? (productos, precios, políticas, FAQ) | |
| **Límites** | ¿Qué NO debe hacer o decir? | |
| **Éxito** | ¿Cómo sabrás que funciona bien? | |

### Prompt Template (Fórmula)

```
Eres [ROL/NOMBRE], un asistente para [STARTUP/CONTEXTO]. 

Tu objetivo es [OBJETIVO PRINCIPAL].

INFORMACIÓN IMPORTANTE:
- [Dato clave 1]
- [Dato clave 2]
- [Dato clave 3]

CUANDO [SITUACIÓN], haz [ACCIÓN]:
- Si te preguntan por [TEMA], responde [CÓMO]
- Si no sabes algo, [ACCIÓN]

TONO: [PERSONALIDAD]

NUNCA:
- [Límite 1]
- [Límite 2]
```

### Ejemplo para la Demo

**Startup:** "Café Conecta" - cafetería online que vende café de especialidad

**Prompt de ejemplo:**
```
Eres "Cafecito", el asistente virtual de Café Conecta, una cafetería online 
que vende café de especialidad de Chiapas, México.

Tu objetivo es ayudar a clientes a elegir café y resolver dudas sobre pedidos.

INFORMACIÓN IMPORTANTE:
- Vendemos 3 tipos: Arábica ($250 MXN), Robusta ($180 MXN), y Mezcla Especial ($300 MXN)
- Envíos a todo México en 3-5 días hábiles
- Devoluciones aceptadas dentro de 7 días si el paquete no está abierto
- Horario de atención: L-V 9am-6pm

CUANDO:
- Si te preguntan por recomendaciones, pregunta primero si prefieren café suave o intenso
- Si preguntan por envíos, indica tiempos y costo según destino
- Si no sabes algo, di "Déjame consultar con el equipo y te respondo pronto"

TONO: Amigable y cálido, como un barista experto

NUNCA:
- Inventes precios o promociones
- Recomiendes café a embarazadas o niños sin sugerir consultar a su médico
- Compartas información personal de clientes
```

### Fases del Ejercicio

| Fase | Tiempo | Actividad | Entregable |
|------|--------|-----------|------------|
| 1. Definir | 10 min | Completar Canvas | Canvas lleno |
| 2. Construir | 20 min | Escribir prompt en herramienta | Prompt v1 |
| 3. Probar | 15 min | Entrevistar al asistente + iterar | Prompt v2 + notas |
| 4. Refinar | 10 min | Compartir en mesa + elegir showcase | Asistente final |

---

## 5. RECURSOS PARA LLEVAR A CASA

### 📦 Kit Digital (se entrega vía QR + link)

**Documentos:**
- [ ] Canvas del Asistente IA (Google Docs editable)
- [ ] 10 Prompts de ejemplo para diferentes industrias
- [ ] Guía "Cómo iterar tu asistente" (1 página)

**Herramientas recomendadas:**
- **Para empezar (gratis):**
  - ChatGPT (OpenAI)
  - Claude (Anthropic)
  - Gemini (Google)
  - Poe.com (multi-modelo)

- **Para avanzar (freemium):**
  - Custom GPTs (ChatGPT Plus)
  - Claude Projects
  - Zapier + IA (automatizaciones)
  - Make.com + IA

- **Para escalar (cuando tengan tracción):**
  - Voiceflow (asistentes conversacionales)
  - Botpress (chatbots avanzados)
  - LangChain (si contratan devs)

**Comunidad:**
- [ ] Link al grupo WhatsApp/Discord del workshop
- [ ] Newsletter "IA para Startups LATAM" (si el facilitador tiene)
- [ ] Calendario de próximos workshops

**Reto 7 días:**
- [ ] Día 1-2: Implementa tu asistente en una tarea real
- [ ] Día 3-4: Prueba con 3 usuarios/amigos
- [ ] Día 5-6: Itera basado en feedback
- [ ] Día 7: Comparte resultados en el grupo

---

## 6. SLIDE COUNT ESTIMADO

| Sección | Slides | Tipo de contenido |
|---------|--------|-------------------|
| Portada + Agenda | 3-4 | Título, agenda, reglas |
| Bloque 1: IA para Startups | 8-10 | Conceptos, usos, casos |
| Bloque 2: Anatomía | 10-12 | Componentes, fórmula, ejemplos |
| Bloque 3: Ejercicio | 5-6 | Instrucciones, canvas, timer |
| Bloque 4: Showcase | 3-4 | Instrucciones, premios, reflexión |
| Cierre | 4-5 | Resumen, recursos, reto, contacto |
| **TOTAL** | **33-41** | |

**Regla de oro:** Máximo 1 slide por minuto de charla. El workshop es 70% práctica, 30% presentación.

---

## 🎯 TIPS PARA EL FACILITADOR

1. **Energía alta desde el minuto 1:** Música al entrar, saluda a todos, muévete por la sala.

2. **Manejo del tiempo:** Usa timer visible. Sé estricto con los cortes. "¡Tiempo! Levanten las manos los que terminaron."

3. **Sistema de tarjetas:** 🟢 voy bien / 🟡 tengo duda / 🔴 necesito ayuda. Los roamers priorizan 🔴.

4. **Lenguaje no técnico:** Evita "prompt engineering", "fine-tuning", "tokens". Usa "instrucciones", "entrenar", "contexto".

5. **Fracaso es aprendizaje:** Si un asistente responde mal, celébralo: "¡Excelente! Encontraron un caso límite. ¿Cómo lo arreglarían?"

6. **Personaliza los ejemplos:** Usa startups locales, moneda local, contextos latinoamericanos.

7. **Cierra con acción:** Nadie sale sin saber exactamente qué hará mañana con su asistente.

---

¿Quieres que desarrolle alguna sección con más detalle, como los slides específicos, la guía del roamers, o el Canvas imprimible?