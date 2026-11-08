# Inkling Small — startup_content/workshop_outline

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 10.553s | tokens_per_second: 238.0
- input_tokens: 191 | output_tokens: 2512
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada, materiales necesarios y dinámicas de workshop bien estructuradas.

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

**TÍTULO:** Construye tu Asistente de IA para tu Startup — Workshop Práctico  
**FORMATO:** Presencial | **DURACIÓN:** 3 horas | **AUDIENCIA:** Emprendedores early-stage no-técnicos (20-30)  
**TONO:** Energético, sin miedo al código, 100% práctico. Nada de "teoría de la IA". Solo *hacer*.

---

### 1. AGENDA DETALLADA (3 HORAS)

| Bloque | Tiempo | Qué pasa |
|---|---|---|
| **Check-in + Energía** | 0:00 – 0:15 | Landing, café, pairing rápido |
| **Bloque 1: El Mito del Robot** | 0:15 – 0:45 | Charla + dinámica de "dolor" |
| **Bloque 2: Tu Asistente en 20 Min** | 0:45 – 1:35 | Demo en vivo + ejercicio principal |
| **PAUSA / NETWORKING** | 1:35 – 1:50 | Café, snacks, conexión |
| **Bloque 3: De la Idea al Prompt** | 1:50 – 2:35 | Discusión + construcción grupal |
| **Bloque 4: Roadmap de 48h** | 2:35 – 2:55 | Pitch rápido + cierre |
| **Wrap & Foto** | 2:55 – 3:00 | Recursos, foto grupal, energía |

---

### 2. MATERIALES NECESARIOS (PREPARAR ANTES)

**Para los participantes (en mesa, por persona):**
- Laptop propia (obligatorio) con navegador actualizado y cuenta de ChatGPT / Claude / Gemini activa (o crear una en los primeros 5 min).
- Notebook físico + 2 marcadores de colores (uno para "dolor", otro para "automático").
- 3 post-its (uno por cada "tarea que odia").
- Smoother: un "kit de café" o agua (opcional, pero el ambiente latino requiere café).

**Para el facilitador / sala:**
- Proyector + pantalla grande + sonido básico.
- 2 pantallas de respaldo (por si falla una laptop).
- Conexión WiFi de respaldo (hotspot 4G/5G).
- 30 hojas impresas: **"Tarjeta de Prompts"** (template de 5 líneas para copiar).
- 30 hojas: **"Roadmap de 48h"** (checklist de acciones).
- Post-its de colores y cinta adhesiva para el muro de "Dolores".
- 3 rotuladores grandes para el muro.
- Regalo físico pequeño: sticker o pin de "Asistente IA" (para foto final).

**Contenido digital pre-cargado:**
- Cuenta de demo en ChatGPT / Claude con un proyecto de ejemplo (ej: "Asistente de Ventas para Startup").
- 3 ejemplos reales de prompts ya probados (capturas de pantalla en el deck).
- Link de acceso a la carpeta de recursos (Google Drive / Notion) con el nombre del workshop.

---

### 3. BLOQUES DETALLADOS

#### BLOQUE 1: EL MITO DEL ROBOT
- **Duración:** 30 min (0:15 – 0:45)
- **Objetivo:** Romper la idea de que "IA = programador" y conectar con su dolor real de negocio.
- **Dinámica:** Charla corta (8 min) + **"Muro de Dolores"** (17 min) + **"Votación caliente"** (5 min).
  - *Charla:* "No necesitas ser dev. La IA es un asistente que nunca duerme, no un robot que te reemplaza."
  - *Ejercicio:* Cada uno escribe en 2 post-its: "¿Qué hago todos los días que me quita 2+ horas y odio?" (ej: responder emails, hacer propuestas, resumir reuniones). Pegan en muro. Todos votan con el marcador los 3 más repetidos.
- **Key Takeaway:** *"No construyas IA por moda. Construye un asistente porque te duele algo concreto."*

**Slides estimados:** 6

---

#### BLOQUE 2: TU ASISTENTE EN 20 MIN
- **Duración:** 50 min (0:45 – 1:35)
- **Objetivo:** Ver que se puede hacer *ahora*, sin código, con una sola herramienta.
- **Dinámica:** **Demo en vivo** (15 min) + **Ejercicio principal** (30 min) + **Share rápido** (5 min).
  - *Demo:* Facilitador abre ChatGPT/Claude, crea una "Instrucción" (system prompt) paso a paso para un caso real (ej: "Asistente de Ventas B2B para una startup de logística"). Muestra cómo darle contexto (nombre de la startup, tono, 3 tareas clave) y cómo pedirle que responda un email de ejemplo.
  - *Ejercicio principal (ver sección 4):* Cada uno construye su propio "Asistente" en su laptop siguiendo la plantilla.
- **Key Takeaway:** *"Un asistente de IA es solo un prompt muy bien escrito + contexto de tu negocio."*

**Slides estimados:** 10

---

#### BLOQUE 3: DE LA IDEA AL PROMPT
- **Duración:** 45 min (1:50 – 2:35)
- **Objetivo:** Aprender a pasar de "quiero algo" a "le pido exactamente eso".
- **Dinámica:** **Discusión de grupos** (10 min) + **"Prompt Battle"** (25 min) + **Retroalimentación** (10 min).
  - *Discusión:* ¿Qué pasó con tu asistente? ¿Qué falló? ¿Qué falta?
  - *Prompt Battle:* En grupos de 4, reciben 3 "escenarios de negocio" (ej: "Tienes 50 leads y no sabes cuál califica"). Tienen 10 min para escribir el mejor prompt posible. Ganador: el que genere la respuesta más útil en la pantalla.
- **Key Takeaway:** *"El secreto no es la herramienta, es la claridad del pedido. Escribe como si le hablaras a un socio nuevo."*

**Slides estimados:** 7

---

#### BLOQUE 4: ROADMAP DE 48H
- **Duración:** 20 min (2:35 – 2:55)
- **Objetivo:** Salir con una acción concreta para esta semana, no con "ya veremos".
- **Dinámica:** **Pitch rápido** (15 min) + **Cierre energético** (5 min).
  - Cada uno tiene 30 segundos para decir: "Mi asistente se llama ___, resuelve ___, y lo lanzo el ___".
  - Facilitador entrega la "Tarjeta de Prompts" física y anuncia el link de recursos.
- **Key Takeaway:** *"No necesitas 3 meses. Necesitas 48 horas y un prompt de 5 líneas."*

**Slides estimados:** 4

---

### 4. EJERCICIO PRINCIPAL DEL WORKSHOP (TODOS PUEDEN HACERLO)

**Nombre:** *"El Asistente de Tu Startup en 20 Minutos"*  
**Formato:** Individual, con laptop, guiado paso a paso por el facilitador.

**Pasos (el facilitador va dando instrucciones en pantalla y por voz):**

1. **Elige tu dolor:** De tu post-it del muro, elige una tarea que haces hoy y que te roba tiempo (ej: responder emails de clientes, hacer propuestas, resumir una reunión).
2. **Abre tu IA:** ChatGPT, Claude o Gemini. Usa la versión gratuita.
3. **Copia la plantilla (ya en pantalla):**
   > *"Actúa como [Nombre del Rol] para [Nombre de mi Startup]. Mi negocio es [1 línea]. Mi cliente ideal es [1 línea]. Tono: [profesional / cercano / direct]. Tareas que hago: [lista 3]. Responde como si fueras mi asistente de confianza. Aquí va mi solicitud: [pega tu tarea real]."*
4. **Completa con tu contexto:** Escribe 3 líneas de contexto real de tu startup (no genérico).
5. **Pide la primera tarea:** Escribe tu primer pedido real (ej: "Redacta un email de seguimiento a un cliente que pidió presupuesto hace 3 días").
6. **Itera 1 vez:** Si la respuesta no es perfecta, escribe: *"Mejoralo así: más corto, agrega una llamada a la acción, y usa lenguaje de [tu país/región]."*
7. **Guarda:** Copia la respuesta final, guarda tu prompt en la "Tarjeta de Prompts" y anota: *"Esto me ahorra ___ horas por semana."*

**Resultado esperado:** Cada persona sale con 1 asistente funcional, 1 prompt guardado y 1 idea de cómo usarlo mañana.

---

### 5. RECURSOS PARA LLEVAR A CASA

Todos reciben al final (físico + digital):

- **Tarjeta física "5 Prompts que Cambian Todo"** (impresa, tamaño tarjeta de crédito): prompts listos para copiar y pegar para ventas, atención al cliente, contenido y propuestas.
- **Link privado** al Drive/Notion con:
  - 10 ejemplos de prompts reales de startups latinoamericanas (ej: fintech, agtech, edtech).
  - Plantilla de "Asistente de Ventas" y "Asistente de Atención".
  - Video de 3 min: "Cómo mejorar cualquier respuesta de IA".
- **Checklist "48 Horas para tu Asistente"**: 3 pasos concretos (lunes: elegir dolor; martes: escribir prompt; miércoles: usarlo una vez real).
- **Grupo privado de WhatsApp / Telegram** (opcional) para que sigan compartiendo prompts entre ellos.

---

### 6. SLIDE COUNT ESTIMADO POR SECCIÓN

| Sección | Slides |
|---|---|
| Check-in / Intro (energía, reglas) | 3 |
| **Bloque 1:** El Mito del Robot | 6 |
| **Bloque 2:** Tu Asistente en 20 Min | 10 |
| **Bloque 3:** De la Idea al Prompt | 7 |
| **Bloque 4:** Roadmap de 48h | 4 |
| Cierre / Recursos / Foto | 2 |
| **TOTAL** | **~32 slides** |

---

### BONUS: CONSEJOS PARA EL FACILITADOR (LATINOAMÉRICA)

- **No digas "machine learning" ni "LLM".** Di: *"Esta es tu asistente, funciona como un socio que lee todo lo que le escribes."*
- **Usa ejemplos locales:** Menciona startups de México, Colombia, Chile, Argentina o Brasil. Que se sientan representados.
- **Si alguien no tiene laptop:** Que se una a un compañero (pairing obligatorio). No dejes a nadie fuera.
- **Mantén el ritmo:** Cada 15 min un cambio de dinámica (charla → hacer → hablar → hacer). En 3 horas, la energía baja en el minuto 90; por eso la pausa es clave.
- **Cierre con foto grupal y sticker:** El recuerdo físico aumenta la probabilidad de que usen lo aprendido.

**¿Listo para replicar?** Copia esta estructura, adapta los ejemplos a tu audiencia y recuerda: **no enseñas IA, enseñas a quitarse un dolor con una herramienta.** Eso vende. Eso se recuerda. Eso escala.