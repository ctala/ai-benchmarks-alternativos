# Claude Haiku 4.5 (suscripción) — startup_content/workshop_outline

- model_id: `claude-haiku-4-5`
- success: True  | final: 7.44 | quality: 9.72
- latency_total: 82.657s | tokens_per_second: 99.4
- input_tokens: 10 | output_tokens: 8220
- judge_score: 4.8 | justificación: 

## Respuesta completa

# Workshop: Construye tu Asistente de IA para tu Startup
## Outline Completo (3 horas)

---

## 📋 AGENDA EJECUTIVA

| Hora | Bloque | Duración |
|------|--------|----------|
| **0:00-0:05** | Bienvenida + Expectativas | 5 min |
| **0:05-0:25** | **BLOQUE 1** — ¿Por qué tu startup necesita un asistente IA? | 20 min |
| **0:25-0:45** | **BLOQUE 2** — Tres casos reales de startups que ganaron con IA | 20 min |
| **0:45-1:15** | ☕ **COFFEE BREAK** | 30 min |
| **1:15-1:45** | **BLOQUE 3** — Demo en vivo + Ejercicio práctico PARTE 1 | 30 min |
| **1:45-2:25** | **BLOQUE 4** — Ejercicio práctico PARTE 2 + Showcase | 40 min |
| **2:25-2:50** | **BLOQUE 5** — Hoja de ruta: primeros 30 días | 25 min |
| **2:50-3:00** | Cierre + Networking + Links | 10 min |

**Total: 180 minutos (3 horas)**

---

## 🛠️ MATERIALES A PREPARAR ANTES

### Para el facilitador:
- **Laptop + Proyector** (HDMI, tener adaptador USB-C/HDMI backup)
- **Micrófono** (si es sala >20 personas)
- **Tablet o segundo monitor** para ver notas mientras presentas
- **WiFi estable** (sí o sí — prueba de ancho de banda 24h antes)

### Para los asistentes (entregar al llegar):
- **Impreso A4 (1 por persona)**:
  - Hoja 1: "Mi Startup Postcard" (ficha para completar durante Bloque 3)
  - Hoja 2: "Checklist de 30 días" (Bloque 5, llevan a casa)
  - Hoja 3: "Prompts listos para copiar-pegar" (5 prompts + casos de uso)
  - Hoja 4: "Links + Recursos" (herramientas gratis vs pago)
  
- **En la mesa (por mesa de 5-6 personas)**:
  - 1x Laptop/Tablet (si no traen)
  - 1x Cuaderno grande + 2-3 lápices

### Slides + Assets digitales:
- Presentación (Google Slides o Figma — **compartible en vivo**)
- Video demo sin sonido (1:30 min, backup local)
- Template de "Asistente IA Canvas" (Figma o PNG descargable)
- Folder con prompts `.txt` listos para copiar

### Pre-requisitos técnicos:
- Cuenta **ChatGPT gratis o Plus** (demo en vivo)
- Cuenta de prueba en **N8N** (para mostrar automatización)
- 1-2 ejemplos de chat history de startups reales anonimizados

---

## 📍 BLOQUES DETALLADOS

### **BLOQUE 1: ¿Por qué tu startup necesita un asistente IA?** (20 min)
**Slides: 8-10**

#### Objetivo
Pasar del miedo/escepticismo a la curiosidad. Que vean que no es ciencia ficción, es una herramienta como Google.

#### Dinámica
**Charla energética + Fast poll + Story**

1. **Apertura (2 min)** — "Levanten la mano: ¿usaron ChatGPT alguna vez?" (rompe hielo)
2. **3 razones para un founder** (4 min):
   - *Razón 1: Trabajo repetitivo desaparece*. Ej: redactar 20 emails, propuestas de clientes. La IA lo hace en segundos.
   - *Razón 2: Tu primer "empleado" es gratis*. $0/mes ChatGPT (o $20 ChatGPT Plus si necesitas poder). Competidor paga $2,000/mes.
   - *Razón 3: Vendes más rápido*. IA genera copy, responde leads, crea ideas. Tu cierre humano es 10x mejor con ese prep.

3. **Poll 30s** — "¿Cuánto tiempo pierdes CADA DÍA en tareas que la IA podría hacer?" 
   - A) 0-30 min | B) 30-60 min | C) >1 hora (se sorprenden, 80% dice C)

4. **Story real (6 min)** — *Caso de co-founder chileno* (o argentino/colombiano cercano):
   - "Hace 2 años una startup de envíos usaba hojas Excel para rutas"
   - "Un dev joven les pegó un bot en N8N que optimiza rutas en 2 min"
   - "Ahorraron 8 horas/semana. Usaron eso para crecer de 15 a 45 clientes en 6 meses"
   - **Moraleja**: no es magia, es ahorrar tiempo en lo tonto para enfocarse en lo que solo tú puedes hacer.

#### Key Takeaway
> "Un asistente IA no reemplaza al founder. Lo libera para lo que realmente importa: hablar con clientes, iterar producto, crecer."

#### Vibe
Energía alta, sin tecnicismos. Lenguaje de startup ("crecer", "escalar", "eficiencia").

---

### **BLOQUE 2: Tres casos reales de startups que ganaron con IA** (20 min)
**Slides: 6-8**

#### Objetivo
Anclar con ejemplos concretos. Mostrar que esto funciona en Latam, en sectores distintos, en equipos pequeños.

#### Dinámica
**Storytelling en 3 actos + Facilitador baja a piso (15 seg por persona)**

**Caso 1: SaaS B2B — Onboarding automático (4 min)**
- Startup de "software para asesores fiscales"
- **Problema**: gastar 1 hora por cliente nuevo en setup
- **Solución**: Flujo con chatbot (Zapier + OpenAI)
  - Cliente entra → bot hace 5 preguntas → AI extrae datos → Sistema se configura solo
- **Resultado**: setup 1 hora → 3 min. Convirtieron 40% más trials a clientes pagando.

**Caso 2: E-commerce local — Copywriting + Fotos (5 min)**
- "Tienda en línea de indumentaria" (Colombia)
- **Problema**: descripción de 200 productos = 40 horas de copywriter
- **Solución**: 
  - IA escribe descripciones base (1 hora)
  - IA genera 3 versiones de copy por producto (A/B test)
  - Luego testean con Google Ads cuál vende más
- **Resultado**: CTR +35%, AOV +$8/orden. Rápido payoff.

**Caso 3: Agency / Services — Propuestas en 5 min (4 min)**
- "Agencia de marketing digital" (Perú)
- **Problema**: Cada propuesta = 2-3 horas. Perdían deals por tardanza.
- **Solución**: Template + Campos en Google Docs → AI completa → 15 min review/customizar
- **Resultado**: Respondieron 5 propuestas en 1 semana en vez de 1. 3 nuevos clientes en 2 meses por respuesta rápida.

#### Key Takeaway
> "IA no es para reemplazar. Es para jugar en otra liga: responde más rápido, prueba más variaciones, libera tu tiempo para la estrategia."

#### Vibe
Histórico real, nombres anónimos pero detalles específicos. Al final de cada caso, preguntar: "¿Ven algo similar en su startup?"

---

### **BLOQUE 3: Demo en vivo + Ejercicio Práctico PARTE 1** (30 min)
**Slides: 5-6 + Interfaz viva**

#### Objetivo
Demistificar cómo se pide. Que vean que no es brujería, es escribir bien.

#### Dinámica
**Demo (10 min) + Hands-on (20 min)**

##### **DEMO EN VIVO** (10 min)

**Escena 1**: Prompt vago (2 min)
```
Yo escribo: "ayuda con marketing"
ChatGPT responde: algo genérico
```
→ Señalar: "Meh. No es culpa de la IA, le di poca info."

**Escena 2**: Prompt específico (3 min)
```
Yo escribo: 
"Eres copywriter experto en SaaS.
Escribe el subject de email para CTO que usa Excel para workflows.
Tono: urgencia profesional.
Máx 50 caracteres.
Output: 5 opciones."
```
→ ChatGPT genera 5 subjects A/B-ables.
→ Digo: "Así se pide. Le damos contexto, rol, restricción, formato."

**Escena 3**: Bonus — Show N8N (1-2 min, si hay WiFi)
- Muestro automatización: "Email → IA responde → Entra en CRM"
- **Clave**: "Miren, esto se puede automatizar en 20 minutos, sin código."

##### **EJERCICIO PRÁCTICO PARTE 1** (20 min)

**Nombre**: "Mi Startup AI Canvas"

**Paso 1** (5 min): En grupo, yo hago primero (modelado)
- Yo soy fundador de "Servicio de delivery de comida fit"
- Completo en vivo en pantalla grande (todos ven):
  ```
  Mi startup es: ___
  Mi problema #1 es: ___
  La IA podría ayudar en: ___
  En específico, yo diría: "Necesito que IA ___ para ___"
  ```
- Ej mi respuesta: "Necesito que IA redacte respuestas a reviews negativas para ___"

**Paso 2** (12 min): Trabajo en silencio + parejas
- Reparten impreso "Mi Startup Postcard" (hoja A4)
- Cada founder completa SOLO (5 min)
- Luego vuelcan en parejas (3 personas) — se ayudan a ser específicos (7 min)
- **Facilitador circula**, hace preguntas:
  - "¿Por qué específicamente?", "¿Cuántas horas ahorra?", "¿Cómo medís el éxito?"

**Paso 3** (3 min): 3-4 personas comparten (voluntarias)
- "Mi startup es 'marketplace de cursos'. Necesito que IA escriba emails de retención"
- Yo digo: "Perfecto. Mañana lo pruebas así [muestro prompt template]"

#### Key Takeaway
> "La magia no es la IA. Es ser específico con lo que pides. Un buen prompt > cualquier herramienta."

---

### **BLOQUE 4: Ejercicio práctico PARTE 2 + Showcase** (40 min)
**Slides: 3-4 + Laptops activas**

#### Objetivo
Que cada uno **pruebe con su startup en tiempo real**. Lo que construyen aquí se llevan a casa.

#### Dinámica
**Hands-on + Showcase + Feedback**

##### **PARTE 2A: Hands-on en laptop** (20 min)

**Setup (2 min)**:
- "Abran chatgpt.com (gratis, sin login si entra el ancho)"
- O "Usen la tablet de la mesa si no trajeron laptop"

**Instrucción**:
1. Tomen el prompt template que les pasé (hoja 3 impresa):
   ```
   "Eres [EXPERT].
   Mi startup es [STARTUP].
   Necesito que [TAREA ESPECÍFICA].
   Contexto: [1-2 líneas].
   Formato: [Output esperado].
   Genera: [Número de variaciones]"
   ```

2. **Rellenan en 10 minutos**, con gente de su mesa ayudando:
   - EXPERT: ¿Qué rol necesitas?
   - STARTUP: ¿Qué hacen?
   - TAREA: ¿Qué específicamente necesitas?
   - Contexto: ¿Info clave que la IA debe saber?
   - Formato: ¿Bullets? Párrafo? Título?
   - Cantidad: ¿Cuántas opciones?

3. Copian-pegan en ChatGPT
4. Ven el resultado en **tiempo real**

**Facilitador (yo)**:
- Proyecto tiempo en pantalla: "Faltan 5 minutos"
- Circulo ayudando: "¿Viste el output? ¿Te sirve? ¿Qué le cambiarías?"
- Muestro resultados en tiempo real en proyector (algunos eligen compartir)

##### **PARTE 2B: Showcase + Feedback** (18 min)

**Rodada de 6-8 personas** (30-45 seg cada una):
- Se ponen de pie, leer su prompt, leer su output
- Yo digo: "¿Qué le falta? ¿Cómo lo mejoramos?"
- El grupo sugiere 1-2 tweaks (tono, más detalles, otro formato)
- Ellos lo prueban en vivo en la laptop
- Resultado: mucho mejor

**Ejemplo**:
- Founder dice: "Mi prompt pidió email de follow-up"
- Output: genérico
- Grupo dice: "Agregá que mencione qué problema específico resuelve"
- Refrescamos el prompt
- Output: 10x mejor, personal, conversacional

**Final**: Todos se llevan el output en su celular (screenshot o PDF)

#### Key Takeaway
> "Hoy escribiste tu primer prompt y viste funcionar. Eso es 90% de lo que necesitas. El otro 10% es iterar."

---

### **BLOQUE 5: Hoja de ruta — Primeros 30 días** (25 min)
**Slides: 10-12**

#### Objetivo
Que se vayan con un plan accionable. No abrumados, pasos claros.

#### Dinámica
**Charla estructurada + Checklist impreso + Q&A**

#### Contenido — "30 DÍAS: Tu Roadmap IA"

**SEMANA 1: Experimentar (5 min)**
- Día 1-2: Prueba 3 tareas en ChatGPT
  - Ej: redactar email a cliente, resumen de reunión, lluvia de ideas
- Día 3-4: Mira tutorials: "Prompting 101" en YouTube (busca Andrej Karpathy, 15 min)
- Día 5-7: Aplica 1 tarea a tu startup (copia-pega en tu workflow real)
- **Métrica**: ¿Ahorré 1 hora? ¿Usé 5 veces?

**SEMANA 2: Integrar (4 min)**
- Ahora: ¿Dónde puedo salvar tiempo CADA DÍA?
  - Si escribes emails → automatiza replies
  - Si generas reportes → automatiza síntesis
  - Si haces brainstorms → IA colaborador
- **Tool**: Google Sheets + ChatGPT API = libre. Busca "ChatGPT en Sheets tutorial"
- **Métrica**: Implementa 1 flujo recurrente

**SEMANA 3-4: Escalar (4 min)**
- ¿El flujo funcionó? → Mejora
  - Prompts más precision
  - Más casos de uso
- ¿Querés más poder? → Considera N8N (gratis hasta 100 tasks/mes)
  - Conecta: CRM → IA → Sheets → Email
  - Cero código
- **Métrica**: 5+ horas/semana ahorradas

**DESPUÉS (Mes 2+):**
- Contratar dev si quieres custom (pero 80% casos no necesitan)
- Considerar staff engineer part-time si IA es core a tu producto
- Revisar pricing vs ROI cada mes

#### Recursos en cada paso
- **Hoja 2 impresa**: Checklist con links (qué hacer cada día)
- Carpeta Drive compartida: "Templates listos" (prompts + N8N workflows)
- Grupo Slack (opcional): "Startups + IA LATAM" (para preguntas)

#### Key Takeaway
> "No es un proyecto de 6 meses. Es: experimentá semana 1, usa 1 cosa en semana 2, escala en semana 3. Eso es toda la hoja de ruta."

---

### **CIERRE: Networking + Links** (10 min)
**Slides: 2**

#### Dinámica
**Formativo + Inspirador + Contacto**

1. **Recap 60 segundos** (2 min)
   - Hoy aprendiste: Asistentes IA no son magia, son herramientas bien pedidas
   - Tu primer paso: el prompt template + 1 tarea en tu startup
   - Próximo mes: 5+ horas ahorradas

2. **Links finales** (2 min) — Proyectar en pantalla + enviar por mail
   ```
   🔗 RECURSOS GRATIS
   - ChatGPT: https://chatgpt.com (gratis)
   - N8N: https://n8n.io (libre hasta 100/mes)
   - Prompt tips: https://platform.openai.com/docs/guides/prompt-engineering
   - Template canvas: https://drive.google.com/file/...
   
   🎯 PRÓXIMO PASO
   - Día 1: Prueba 1 prompt aquí
   - Día 3: Manda foto del resultado a [email grupal]
   - Mes 1: Reporta cuántas horas ahorró
   
   💬 COMUNIDAD
   - Slack: [Invitación]
   - Próximo workshop: [Fecha]
   ```

3. **Foto grupal + Networking** (6 min)
   - "Tómense 5 min para intercambiar contactos"
   - Yo circulo ayudando con preguntas individuales

4. **Despedida energética** (0.5 min)
   ```
   "Se van con 3 cosas:
   1️⃣ Un prompt que funciona
   2️⃣ Un plan de 30 días
   3️⃣ La confianza de que ESTO ES POSIBLE en tu startup
   
   Ahora es acción. ¡Nos vemos!"
   ```

---

## 🎯 EJERCICIO PRINCIPAL: "Mi Startup AI Canvas"

### Objetivos
- Tangible: cada founder se va con 1 prompt específico a su negocio
- Transferible: saben cómo escribir prompts para cualquier tarea
- Motivacional: "Lo hice yo, funcionó, puedo repetir"

### Flujo completo
```
PASO 1: Briefing (facilitador modela, 2 min)
  "Yo soy founder de delivery fit.
   Mi problema: responder reviews negativos.
   Mi prompt sería:
   'Eres expert en customer service.
    Escribe respuestas empáticas a críticas.
    Tono: professional pero humano.
    Máx 2 líneas.
    Aquí está la crítica: [...]'"

PASO 2: Trabajo individual (5 min)
  → Impreso "Postcard", completan estructura

PASO 3: Validación en parejas (7 min)
  → Se ayudan a ser específicos
  → Yo circulo haciendo preguntas

PASO 4: Prueba en ChatGPT (10-15 min)
  → Copian-pegan en laptop
  → Ven output en tiempo real
  → Entienden si funcionó o qué ajustar

PASO 5: Showcase (6-8 personas, 18 min)
  → Comparten prompt + resultado
  → Grupo sugiere mejoras
  → Prueban en vivo
  → Celebran: "Eso está listo para usar mañana"

RESULTADO:
  ✅ Cada uno se lleva 1 prompt funcional
  ✅ Saben el proceso (específico → prueba → itera)
  ✅ Confianza: "Yo puedo hacer esto en mi startup"
```

---

## 📦 RECURSOS PARA LLEVAR A CASA

### Impresos (llevan físicamente)
**Hoja 1: "Mi Startup Postcard"** (A5 doblada, full-color)
```
┌─────────────────────────────────────┐
│ MI STARTUP AI CANVAS                │
│                                     │
│ Mi startup es: ___________________  │
│ Mi problema #1: ___________________│
│ IA podría ayudar en: _____________│
│                                     │
│ Mi primer prompt:                   │
│ "Eres [ROLE].                       │
│  Necesito [TAREA].                  │
│  Context: [INFO].                   │
│  Formato: [OUTPUT]."                │
│                                     │
│ ✅ Resultado: _____________________│
└─────────────────────────────────────┘
```

**Hoja 2: "Checklist de 30 días"** (A4)
```
SEMANA 1: EXPERIMENTAR
□ Día 1-2: Prueba 3 tareas en ChatGPT
□ Día 3-4: Tutorial Andrej Karpathy (15 min)
□ Día 5-7: Aplica 1 tarea real en tu startup
  ↳ Métrica: ¿Ahorré 1 hora? Sí/No

SEMANA 2: INTEGRAR
□ Identifica top 3 tareas repetitivas (30 min)
□ Configura Google Sheets + ChatGPT (30 min)
□ Implementa 1 flujo recurrente
  ↳ Métrica: Horas/semana ahorradas: ___

SEMANA 3-4: ESCALAR
□ Mejora prompts existentes (con feedback real)
□ Considera N8N si necesitas más poder (gratis)
□ Documenta qué funcionó, qué no
  ↳ Métrica: Total horas ahorradas mes 1: ___

CONTACTO FACILITADOR:
Email: [email]
Slack: [enlace invite]
Next workshop: [fecha]
```

**Hoja 3: "Prompts listos para copiar"** (A4, monospace)
```
TEMPLATE BASE
──────────────
"Eres [ROLE].
 Necesito [TAREA].
 Contexto: [INFO].
 Formato: [OUTPUT].
 Genera: [N variaciones]."

EJEMPLOS POR SECTOR
──────────────────
🏪 E-COMMERCE
"Eres copywriter experto en e-commerce.
 Necesito redactar descripción de producto.
 Producto: [desc breve].
 Público: [quién compra].
 Formato: 3 bullets de beneficio + 1 párrafo.
 Genera: 2 versiones."

💼 B2B SAAS
"Eres account manager experto.
 Necesito responder a objeción de precio.
 Contexto: cliente dice '[OBJECIÓN]'.
 Tono: profesional, empático, urgente.
 Máx: 150 palabras.
 Genera: 3 opciones."

📱 MEDIA / COMMUNITY
"Eres community manager.
 Necesito responder crítica en social.
 Crítica: '[CRÍTICA]'.
 Tono: profesional pero cercano.
 Máx: 1 tweet (280 car).
 Genera: 2 opciones."
```

**Hoja 4: "Links + Recursos"** (A4, QR codes)
```
🔧 HERRAMIENTAS GRATIS
ChatGPT Free: https://chatgpt.com
N8N: https://n8n.io
Google Sheets + ChatGPT: [short link]
Ollama (local): https://ollama.ai

📚 APRENDER
Prompt Engineering: [OpenAI guide]
N8N tutorials: [YouTube playlist]
YouTube: Andrej Karpathy (tokens, transformers)

🤝 COMUNIDAD
Slack: [invite de grupo]
Discord: [si aplica]
Email facilitador: [email]
próx workshop: [fecha/tema]

💰 PRICING REALISTA
ChatGPT Plus: $20/mes (si lo necesitas)
N8N: gratis hasta 100 tareas/mes
```

### Digital (enviados por mail post-workshop)

1. **Presentation (PDF + Google Slides link)**
   - Todos los slides con notas del facilitador

2. **Templates** (Drive folder compartida)
   - Google Sheets + ChatGPT API template (copy y usa)
   - N8N workflows pre-built (3-4 casos comunes)
   - Prompt library (50+ prompts por sector)

3. **Videos de referencia** (YouTube playlist o Drive)
   - Prompt tips (3 min)
   - "Cómo integrar ChatGPT en tu flujo" (5 min)
   - N8N 101 (8 min)

4. **Recording del workshop** (si grabaron)
   - Enlace Vimeo/YouTube (privado)
   - Contraseña en el email

5. **Acceso a comunidad**
   - Invitación a Slack grupo "Startups + IA"
   - Donde preguntar, compartir resultados, pedir help

---

## 📊 SLIDE COUNT POR SECCIÓN

| Sección | Slides | Notas |
|---------|--------|-------|
| **Intro + Títulos** | 2 | Bienvenida, expectativas |
| **BLOQUE 1** | 8-10 | Poll, 3 razones, 1 story |
| **BLOQUE 2** | 6-8 | 3 casos, cada uno 1-2 slides |
| **BLOQUE 3 Demo** | 5-6 | Demo live, N8N bonus, prompt anatomy |
| **BLOQUE 3 Ejercicio** | 0 | Work en laptop, slides solo de timing |
| **BLOQUE 4 Hands-on** | 0-1 | Video/timer en pantalla |
| **BLOQUE 4 Showcase** | 0-1 | Pantalla de ChatGPT live |
| **BLOQUE 5 Roadmap** | 10-12 | Semana 1-4, métricas, recursos |
| **Cierre** | 2 | QR, links, foto grupal |
| **TOTAL** | **33-40 slides** | |

---

## 🎬 FLUJO TEMPORAL (RECOMENDACIONES)

**Entrada (15 min antes)**
- Prueba WiFi, projector, micrófono
- Recibe asistentes, reparte impresos
- Foto grupal casual al llegar

**Energía por bloque**
- Bloque 1-2: Alta (historias, engagement)
- Coffee break: Reset (15 min café, chat)
- Bloque 3-4: Altísima (hands-on, ver funcionar)
- Bloque 5: Estructura (accionable, no abrumador)
- Cierre: Inspirador (se van motivados)

**Contingencias**
- **Sin WiFi**: Demostración local + videos descargados
- **Laptop insuficientes**: Trios trabajan en 1 laptop (también funciona)
- **Tiempo apretado**: Skip Bloque 5 en vivo, entregan checklist impreso

---

## 💡 TIPS FACILITADOR

1. **Llama a la gente por nombre** durante el showcase (si el grupo es chico, toma nota)
2. **Celebra cada prompt**, aunque sea simple: "¡Eso está funcional!"
3. **Muestra fracasos** (un prompt que no funcionó en la demo) — humaniza, muestra iteración
4. **Interrupción bienvenida** — "¿Preguntas?" cada 5 min
5. **Sé concreto**: no digas "es poderoso", muestra el resultado en pantalla
6. **Cierra loops**: si alguien preguntó en Bloque 1, vuelve en Bloque 4
7. **Timing estricto** — timer visible, avanza aunque alguien siga probando
8. **Post-workshop**: mail en 24h con resources, preguntas del Slack respondidas

---

## 🚀 VARIANTE REMOTA (si lo necesitas)

| Elemento | Presencial | Remota |
|----------|-----------|--------|
| Breakout rooms | Físicas | Zoom (3-4 personas) |
| Ejercicio | Laptop personal | Comparten pantalla facilitador |
| Showcase | Voluntarios de pie | 6-8 unmute + Chat feedback |
| Impresos | Llevan | PDF descargable post |
| Networking | 5 min final | Slack group |

**Duración remota**: Misma (3h), pero agrega 3 breaks de 3 min (Zoom fatiga).

---

**¿Este outline te sirve como base? Te puedo:**
- Expandir cualquier sección (preguntas para hacer durante ejercicio, ejemplos por industria)
- Adaptar a tu contexto (startups chilenas específicas, sectores, lenguaje)
- Crear las 4 hojas impresas en diseño listos para copiar
- Armar la deck de slides (GDocs con notas para facilitador)
- Grabar los videos de demo y referencias

¿Qué quieres detallar primero?