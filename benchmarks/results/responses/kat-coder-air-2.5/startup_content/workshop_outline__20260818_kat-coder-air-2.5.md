# KAT Coder Air v2.5 — startup_content/workshop_outline

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 8.39 | quality: 9.16
- latency_total: 10.452s | tokens_per_second: 195.9
- input_tokens: 202 | output_tokens: 2048
- judge_score: 4.4 | justificación: 

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



# 🚀 CONSTRUCTE TU ASISTENTE DE IA PARA TU STARTUP
## Workshop Práctico — 3 Horas

---

## 1. AGENDA DETALLADA

| Hora | Bloque |
|------|--------|
| 0:00 - 0:20 | Bienvenida + Contexto + Icebreaker |
| 0:20 - 0:50 | Bloque 1: El Problema Real + Demo en Vivo |
| 0:50 - 1:20 | Bloque 2: Fundamentos sin Código |
| 1:20 - 1:30 | ☕ Break |
| 1:30 - 2:20 | Bloque 3: Manos a la Obra — Ejercicio Principal |
| 2:20 - 2:45 | Bloque 4: Presentaciones + Feedback |
| 2:45 - 3:00 | Bloque 5: Cierre + Recursos |

---

## 2. MATERIALES NECESARIOS (PREPARAR CON ANTELACIÓN)

### Logística del espacio
- [ ] Proyector + pantalla
- [ ] WiFi estable (mínimo 50 Mbps) con contraseña visible
- [ ] Pizarra o pizarras blancas (2-3) con marcadores de colores
- [ ] Post-its (3 colores) + marcadores gruesos
- [ ] 1 powerpoint/extensiones (mínimo 1 por cada 2 personas)
- [ ] Altavoz o sistema de audio para demos

### Materiales para participantes
- [ ] Laptop con acceso a internet (confirmar en RSVP)
- [ ] Cuentas creadas de antemano en:
  - [ ] **Make (ex-Integromat)** — cuenta gratuita
  - [ ] **n8n.cloud** — cuenta gratuita (opcional, como alternativa)
  - [ ] **Google Sheets** — ya la tienen
  - [ ] **WhatsApp Business API** (demo) o **Telegram Bot**
  - [ ] **ElevenLabs** (cuenta gratuita para TTS)
- [ ] Formulario de inscripción con: nombre, startup, sector, problema que quieren resolver, experiencia con IA

### Materiales impresos / digitales
- [ ] Checklist "Tu Asistente en 1 Hora" (1 por persona)
- [ ] Cheat sheet de prompts efectivos
- [ ] QR codes con links a todas las herramientas
- [ ] Plantilla de "Prompt Builder" (hoja de trabajo)
- [ ] Certificado de participación (digital)

### Para el facilitador
- [ ] Demo preparada con 2-3 escenarios listos (no depender de internet en vivo sin backup)
- [ ] Screenshots de cada paso por si falla la demo en vivo
- [ ] Video grabado de la demo como plan B
- [ ] Ejercicios con datos de ejemplo (no pedir que usen datos reales de su startup en el primer intento)

---

## 3. BLOQUES DETALLADOS

---

### 🟢 BLOQUE 0: Bienvenida + Contexto + Icebreaker
**Duración:** 20 min

**Objetivo:** Romper el hielo, generar expectativa y conectar el tema con la realidad de cada emprendedor.

**Dinámica:**
1. **(5 min) Introducción del facilitador** — quién eres, por qué te importa esto, tu historia con IA en startups
2. **(5 min) "¿Quién es tu cliente y cuánto tiempo pierde en tareas repetitivas?"** — ejercicio rápido en parejas: cada uno explica en 2 min su startup y la tarea que más tiempo le quita
3. **(5 min) Lluvia de ideas en vivo** — "¿Qué crees que es un asistente de IA?" — post-its al muro, se agrupan ideas
4. **(5 min) El gancho** — mostrar UN ejemplo real impactante: "Este emprendedor de [sector] ahorró 15 horas/semana con esto que vamos a construir hoy"

**Key Takeaway:** *"Un asistente de IA no es magia, es automatización inteligente. Y cualquiera puede construir uno."*

**Slide count estimado:** 5-7 slides

---

### 🟡 BLOQUE 1: El Problema Real + Demo en Vivo
**Duración:** 30 min

**Objetivo:** Mostrar el poder real de un asistente de IA con un ejemplo concreto que la audiencia pueda replicar.

**Dinámica:**
1. **(5 min) El problema que todos conocen** — charla breve sobre las 3 tareas que matan a todo emprendedor: responder mensajes, organizar información, generar contenido
2. **(15 min) DEMO EN VIVO** — construir un asistente paso a paso:
   - Escenario: Un emprendedor de e-commerce que recibe 50 mensajes diarios preguntando "¿tienen envío gratis?"
   - El asistente: Lee el mensaje → entiende la intención → responde automáticamente → si no sabe, pasa a humano
   - Herramientas usadas en la demo: Make + Google Sheets + WhatsApp/Telegram + GPT-4o
   - Mostrar el flujo completo: desde que llega el mensaje hasta que se responde
3. **(5 min) Desmenuzando la demo** — "¿Qué acabamos de ver?" — identificar los 3 componentes: INPUT → PROCESAMIENTO → OUTPUT
4. **(5 min) Preguntas rápidas** — "¿Qué les sorprendió? ¿Qué les asustó?"

**Key Takeaway:** *"Todo asistente de IA tiene 3 partes: lo que recibe, lo que piensa, y lo que responde. Eso es todo."*

**Slide count estimado:** 8-10 slides

---

### 🟠 BLOQUE 2: Fundamentos sin Código
**Duración:** 30 min

**Objetivo:** Entender los conceptos clave sin tecnicismos para que puedan diseñar su propio asistente.

**Dinámica:**
1. **(10 min) Los 3 pilares de todo asistente** — charla visual:
   - **INPUT:** ¿De dónde viene la información? (WhatsApp, email, formulario, web)
   - **CEREBRO:** ¿Quién decide qué hacer? (GPT, Claude, modelos locales)
   - **OUTPUT:** ¿Qué acción se ejecuta? (Responder, crear un archivo, enviar un email, actualizar un sheet)
2. **(10 min) Cómo piensa la IA** — explicación simple de prompts, context window, y por qué importar cómo le hablas:
   - Demo rápida: mismo prompt con 2 estructuras diferentes → resultados muy distintos
   - Framework: **R.C.O.** (Rol + Contexto + Output esperado)
3. **(10 min) Arquitectura de un flujo** — mostrar 3 niveles de complejidad con ejemplos reales:
   - **Nivel 1:** Un chatbot que responde FAQs (solo INPUT + CEREBRO + OUTPUT simple)
   - **Nivel 2:** Un asistente que recibe un email, lo lee, y crea una tarea en tu CRM (INPUT + CEREBRO + OUTPUT con acción)
   - **Nivel 3:** Un asistente que escucha llamadas, resume la conversación, y actualiza tu pipeline (INPUT complejo + CEREBRO avanzado + múltiples OUTPUTs)

**Key Takeaway:** *"No necesitas saber programar. Necesitas saber QUÉ quieres automatizar y cómo estructurarlo."*

**Slide count estimado:** 10-12 slides

---

### ☕ BREAK (10 min)

---

### 🔴 BLOQUE 3: Manos a la Obra — Ejercicio Principal
**Duración:** 50 min

**Objetivo:** Que cada participante construya su primer asistente de IA funcional para su startup.

**Dinámica:** **EJERCICIO PRINCIPAL — "Tu Asistente en 50 Minutos"**

**Fase 1: Diseño (10 min)**
- Cada participante completa la plantilla "Prompt Builder":
  - ¿Qué tarea quiero automatizar? (especificar)
  - ¿Quién es el usuario? (cliente, yo, equipo)
  - ¿Por dónde entra la información? (canal)
  - ¿Qué debe hacer el asistente? (acción)
  - ¿Qué pasa si no sabe la respuesta? (fallback)
- El facilitador circula y ayuda a afinar el diseño

**Fase 2: Construcción (30 min)**
- Todos construyen el mismo asistente base: **Un asistente de WhatsApp/Telegram para responder preguntas frecuentes de su startup**
- Paso a paso guiado:
  1. Crear un bot de Telegram (5 min) — @BotFather, obtener token
  2. Crear un scenario en Make.com (10 min) — trigger de Telegram → GPT-4o → respuesta
  3. Configurar el prompt con su información real (10 min)
  4. Probar