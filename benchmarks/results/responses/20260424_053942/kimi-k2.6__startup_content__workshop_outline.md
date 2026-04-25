# Kimi K2.6 — startup_content/workshop_outline

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 6.9 | quality: 9.44
- latency_total: 190.03s | tokens_per_second: 43.1
- input_tokens: 217 | output_tokens: 8192
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí tienes el outline completo, diseñado para que salgan con un asistente funcionando y cero excusas para no usarlo esta misma semana.

---

# 🤖 CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP
## Workshop Práctico | 3 Horas | Emprendedores No-Técnicos

---

## 1. AGENDA DETALLADA (3 Horas exactas)

| Hora | Bloque | Duración |
|------|--------|----------|
| 0:00 - 0:10 | 🔥 Bienvenida: El Cofounder que no Pide Vacaciones | 10 min |
| 0:10 - 0:40 | 🧠 IA sin Código: El Manual del "Jefe de un Pasante Digital" | 30 min |
| 0:40 - 1:15 | 📝 Diseña antes de Construir: El Blueprint de tu Agente | 35 min |
| 1:15 - 1:30 | ☕ Break | 15 min |
| 1:30 - 2:10 | 🛠️ Laboratorio: Manos al Código Cero | 40 min |
| 2:10 - 2:40 | ⚔️ Guerra de Bots: Testeo Cruzado | 30 min |
| 2:40 - 3:00 | 🚀 Cierre, Recursos y Plan de Ataque | 20 min |

---

## 2. MATERIALES NECESARIOS (Checklist Pre-Workshop)

### Para ti (Facilitador)
- Proyector + HDMI/USB-C de respaldo + **micrófono** (esencial para 20-30 personas).
- Hotspot de internet (el WiFi del lugar siempre falla cuando más lo necesitas).
- Cuenta de ChatGPT Plus de "demostración" (por si alguien no tiene Plus y quiere probar la creación de GPTs).
- 2 rotafolios o pizarra grande + marcadores.
- Timer visible en pantalla para las dinámicas.
- Playlist de fondo (bajito) para los momentos de trabajo individual.

### Para los participantes (enviar por mail 3 días antes)
- **Laptop obligatoria** (no se puede construir desde el celular en 40 min).
- **Celular** para la dinámica de pruebas.
- Cuenta activa de **ChatGPT** (gratuita sirve) o **Claude.ai**.
- Traer **1 archivo** (PDF, Word o Excel) con información de su startup: descripción del producto, precios, FAQs o una hoja de cálculo con datos reales. Esto será el "cerebro" que le alimentarán a su asistente.

### Impresiones en sala (30 copias mínimo)
- **Canvas del Agente** (hoja A4 a color, fill-in-the-blanks).
- **Plantilla "Prompt Maestro"** (fórmula RIPA lista para completar).
- Post-its verdes (funcionó) y rojos (se confundió).

---

## 3. BLOQUES DETALLADOS

### 🔥 BLOQUE 1: El Cofounder que no Pide Vacaciones
**Duración:** 10 min  
**Dinámica:** Energizante rápida + Seteo de expectativas.  
**Slides:** 3

- **0:00 - 0:05 | El Pitch del Bot:** Cada uno se presenta en 15 segundos respondiendo: *"Mi startup es..., y la tarea que más odio hacer semanalmente es..."*. Tú anotas 3-4 en la pizarra.
- **0:05 - 0:10 | Reglas del juego:** Hoy no hay examen. Si sales sin tocar tu laptop, perdiste el tiempo. El objetivo es salir con un asistente que atienda clientes, cree contenido o analice datos **antes de dormir hoy**.
- **Objetivo:** Romper el hielo y que se sientan dueños del proceso (no víctimas de la tecnología).
- **Key Takeaway:** *La IA no te va a quitar el trabajo, pero un emprendedor que use IA le va a quitar el mercado a uno que no.*

---

### 🧠 BLOQUE 2: IA sin Código — El Manual del "Jefe de un Pasante Digital"
**Duración:** 30 min  
**Dinámica:** Charla rápida + Demo en vivo.  
**Slides:** 10

- **0:10 - 0:20 | El Estagiario Infinito:** Analogía central. Un asistente de IA es como un pasante: lee rápido, no duerme, pero si le das instrucciones vagas, te manda fruta. Explicar los 3 perfiles que toda startup early-stage necesita probar:
  1. **El que vende:** Responde dudas, califica leads, sigue cotizaciones.
  2. **El que crea:** Escribe emails, posts, descripciones de producto.
  3. **El que analiza:** Resume reuniones, saca insights de encuestas, ordena excels caóticos.
- **0:20 - 0:35 | Demo en vivo:** Construyes frente a ellos, en máximo 5 minutos, un mini-asistente de ventas para una startup inventada (o usa una de la sala). Usa ChatGPT Plus para que vean la velocidad. Luego le preguntas como si fueras un cliente difícil. *Efecto "¡No jodas, eso fue rápido!" buscado.*
- **0:35 - 0:40 | Mito vs. Realidad:** No necesitas ser programador. Necesitas ser **específico**. Mostrar ejemplos de prompts malos ("responde como experto") vs. prompts que funcionan ("actúas como vendedor senior de una SaaS B2B en LATAM; nunca prometas descuentos; si no sabes la respuesta, pide el email y di que te contactarán").
- **Objetivo:** Quitarles el miedo y mostrarles el techo real de lo que pueden hacer hoy mismo.
- **Key Takeaway:** *No es un problema de tecnología, es un problema de instrucciones claras. Tú eres el jefe; la IA es el empleado.*

---

### 📝 BLOQUE 3: Diseña antes de Construir — El Blueprint de tu Agente
**Duración:** 35 min  
**Dinámica:** Ejercicio individual con hoja impresa (Canvas del Agente).  
**Slides:** 5 (instrucciones + ejemplos visuales)

- **0:40 - 0:50 | Instrucción:** Entregas el **Canvas del Agente**. Explicas que construir sin diseñar es como contratar a alguien sin saber qué va a hacer. Cada uno elige **UNA** tarea real de su negocio (la que nombraron al inicio).
- **0:50 - 1:10 | Relleno del Canvas:** Trabajan en silencio completando 6 bloques:
  1. **Nombre del Agente** (darle identidad ayuda a la claridad).
  2. **Rol exacto** (ej: "No eres un chatbot, eres el community manager").
  3. **3 tareas concretas esta semana** (ej: "Responder DM de Instagram sobre precios").
  4. **Voz y personalidad** (ej: "Cercano pero no confianzudo, usa 'tú', nunca emojis").
  5. **Guardrails / Lo que NUNCA debe hacer** (ej: "Nunca inventar precios", "Nunca agendar sin confirmar disponibilidad").
  6. **Conocimiento base** (ej: "PDF de precios", "transcripción de 5 llamadas con clientes").
- **1:10 - 1:15 | Socialización rápida:** 2-3 voluntarios leen su Canvas. El grupo da 1 mejora en 30 segundos.
- **Objetivo:** Traducir el dolor del negocio a una arquitectura de instrucciones.
- **Key Takeaway:** *Un mal prompt es un mal jefe. Si no sabes qué quieres, la IA tampoco lo sabrá.*

---

### ☕ BREAK (15 min)
**Mandatorio.** La gente necesita café, baño y revisar el celular. Tú aprovechas para solucionar problemas de login con quienes llegaron sin cuenta.

---

### 🛠️ BLOQUE 4: Laboratorio — Manos al Código Cero
**Duración:** 40 min  
**Dinámica:** Construcción individual en laptop con apoyo de facilitador caminando.  
**Slides:** 8 (paso a paso visual, screenshots grandes, mínimo texto)

- **1:30 - 1:40 | Setup y Tracks:** Divides la sala en dos tracks según sus cuentas. **No hay vergüenza en ninguno.**
  - **Track A (ChatGPT Plus):** Crearán un GPT personalizado usando el botón "Explore GPTs > Create".
  - **Track B (Gratis u otras IAs):** Crearán un **Prompt de Sistema Maestro** y lo usarán con Custom Instructions o al inicio de un nuevo chat (funciona en ChatGPT gratuito, Claude, Gemini, etc.).
- **1:40 - 2:05 | Ejercicio Principal: "Tu Agente en 20 Minutos"**
  1. **Traduce:** Pasan su Canvas a la **Plantilla RIPA** (Rol, Instrucciones, Pasos, Antifrases) que les diste impresa.
  2. **Alimenta:** Suben su archivo de conocimiento (PDF de precios, etc.) si están en Track A. Si están en Track B, pegan 3 párrafos clave al inicio del prompt.
  3. **Construye:** Configuran el asistente.
  4. **Prueba:** Le escriben 3 mensajes de prueba:
     - Un cliente fácil.
     - Un cliente difícil.
     - Una pregunta fuera de lugar (para testear guardrails).
- **2:05 - 2:10 | Salvataje rápido:** Quien ya lo tenga, ayuda a quien esté atorado (1 min de "ayuda vecinal"). Tú resuelves los 3 problemas más comunes en voz alta.
- **Objetivo:** Cada uno debe tener **una interacción exitosa** con su propio asistente antes de que suene el timer.
- **Key Takeaway:** *Tu asistente no necesita ser perfecto; necesita ser útil para una tarea real de hoy.*

---

### ⚔️ BLOQUE 5: Guerra de Bots — Testeo Cruzado
**Duración:** 30 min  
**Dinámica:** Dinámica grupal "Speed Dating de IA".  
**Slides:** 2 (instrucciones + timer en pantalla)

- **2:10 - 2:15 | Instrucciones:** En mesas de 4-5 personas, cada uno presta su laptop. Los otros 3 interactúan con su bot durante 3 minutos como si fueran clientes reales. Usan post-its:
  - 🟢 Verde: "Esto funcionó de puta madre" (perdona la expresión, pero así se siente).
  - 🔴 Rojo: "Aquí se confundió / inventó / falló".
- **2:15 - 2:35 | Rondas:** 3 rondas de 5-6 minutos. Ruido de sala, caos controlado. Tú caminas escuchando las "mentiras" que inventan los bots para corregirlas después.
- **2:35 - 2:40 | Hallazgos:** Pides 3 ejemplos de verdes y 3 de rojos. Muestras en el proyector cómo se corrige un rojo en 10 segundos (ajustando el prompt).
- **Objetivo:** Aprender a iterar rápido y descubrir fallas con datos reales.
- **Key Takeaway:** *Tu bot va a alucinar (mentir) al principio. El arte no es evitarlo, es detectarlo y ponerle rejas rápido.*

---

### 🚀 BLOQUE 6: Cierre, Recursos y Plan de Ataque
**Duración:** 20 min  
**Dinámica:** Charla de cierre + Compromiso público.  
**Slides:** 5

- **2:40 - 2:50 | La realidad de escalar:**
  - Costos: De gratis a $20/mes puede ser el salario de tu primer empleado digital.
  - Privacidad: No subas datos de clientes reales a herramientas gratuitas sin revisar términos.
  - Mantenimiento: Revisa tu bot cada vez que cambien precios o políticas.
- **2:50 - 2:57 | Compromiso 48h:** Cada uno escribe en el chat de la sala (o en un post-it que recoges) la **primera tarea real** que le delegará a su asistente antes del viernes.
- **2:57 - 3:00 | Foto grupal** y entrega de recursos.
- **Objetivo:** Pasar de la emoción del taller a la acción inmediata.
- **Key Takeaway:** *Un asistente que no usas esta semana es un pasante que renunció antes de empezar.*

---

## 4. EJERCICIO PRINCIPAL DEL WORKSHOP
### 🏗️ "Tu Agente en 20 Minutos" (Ejercicio Unificado)

**Para qué sirve:** Que cada participante salga con un asistente funcional, aunque nunca haya escrito una línea de código.

**La fórmula RIPA (La usan todos):**

| Letra | Significado | Ejemplo |
|-------|-------------|---------|
| **R** | **Rol** | "Eres el vendedor digital de una fintech mexicana..." |
| **I** | **Instrucciones** | "Tu trabajo es calificar leads por WhatsApp y enviar la cotización base." |
| **P** | **Pasos** | "1. Saluda. 2. Pregunta presupuesto. 3. Si es >$10k, pide email. Si es <$10k, envía link." |
| **A** | **Antifrases / Guardrails** | "NUNCA inventas tasas de interés. Si no sabes, dices 'déjame confirmar'." |

**Pasos del ejercicio:**

1. **DEFINE (Papel):** Con el Canvas del Agente, elige 1 tarea que te robe +3 horas semanales.
2. **TRADUCE (Papel + Digital):** Escribe tu Prompt Maestro usando RIPA. Mínimo 10 líneas. Máximo 1 página.
3. **CONSTRUYE (Laptop):**
   - *Con Plus:* Ve a ChatGPT > Explore GPTs > Create. Pega tu prompt. Sube tu archivo PDF/Excel en "Knowledge". Guarda.
   - *Sin Plus:* Ve a Settings > Custom Instructions. Pega la parte de Rol e Instrucciones. O inicia un chat nuevo pegando todo el prompt como primer mensaje.
4. **PRUEBA (Laptop + Celular):** Escríbele como si fueras tu peor cliente. ¿Inventó algo? ¿Se salió del guion? Anota.
5. **AJUSTA (2 min):** Corrige UNA frase de tu prompt para cerrar esa grieta. Vuelve a probar.

**Criterio de éxito:** El asistente responde correctamente al menos 2 de 3 escenarios sin inventar datos peligrosos.

---

## 5. RECURSOS PARA LLEVAR A CASA
(Pack digital que envías por mail al finalizar o en QR al salir)

1. **📄 Canvas del Agente (PDF editable)** — Para que diseñen el siguiente.
2. **📝 Plantilla RIPA (Google Docs / Notion)** — Copia y pega para futuros bots.
3. **⚡ Cheatsheet: "50 Tareas para Delegar a tu IA esta Semana"** — Organizado por área: Ventas, Marketing, Ops, Legal básico.
4. **🛠️ Toolkit No-Code/Low-Cost LATAM** — Lista curada de herramientas con planes gratuitos reales (Make, Zapier, Relevance AI, Stack AI) y cómo saber cuándo saltar de ChatGPT a una de estas.
5. **🎥 Video del Demo en vivo** — Grabado por ti durante el taller (o uno que prepares antes) para quienes quieran replicar los pasos con calma.
6. **💬 Acceso al Grupo de WhatsApp/Telegram "Bots & Café"** — Comunidad de 30 días para preguntas rápidas. (Esto aumenta la retención y el valor percibido).

---

## 6. SLIDE COUNT ESTIMADO

| Sección | Slides | Estilo |
|---------|--------|--------|
| Bienvenida + Reglas | 3 | Grandes, poco texto, fotos de pasantes vs. robots |
| Fundamentos + Demo | 10 | 60% visuales (memes, screenshots), 40% texto |
| Blueprint (Canvas) | 5 | 1 slide instrucción + 4 ejemplos de canvas llenos |
| Laboratorio de Construcción | 8 | Screenshots paso a paso, flechas rojas, timers |
| Guerra de Bots | 2 | 1 instrucción + 1 slide de "reglas del juego" |
| Cierre + Recursos | 5 | Datos duros de costos, screenshot del grupo QR, foto de des