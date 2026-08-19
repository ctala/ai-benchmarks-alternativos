# DeepSeek V4 Pro (0813) — startup_content/workshop_outline

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.34 | quality: 10.0
- latency_total: 147.254s | tokens_per_second: 53.7
- input_tokens: 277 | output_tokens: 7902
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando un plan detallado y práctico para el taller.

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

# Outline Workshop Presencial  
## “Construye tu Asistente de IA para tu Startup – Workshop Práctico”

**Promesa del workshop:**  
En 3 horas sales con un asistente de IA versión 1 funcionando para un proceso real de tu startup. Cero código, cero humo, 100% práctico.

**Herramienta base:**  
ChatGPT (gratis o Plus) + una plantilla de prompt maestro. Si alguien usa Claude, también funciona.

---

## 1. Agenda detallada con tiempos (3 horas)

| Hora | Bloque | Formato | Slides |
|---|---|---|---|
| 0:00 – 0:15 | Bienvenida y encuadre | Charla + rompehielo | 5 |
| 0:15 – 0:30 | La oportunidad IA para startups no-técnicas | Charla energética | 6 |
| 0:30 – 0:50 | Anatomía de un asistente de IA | Charla + demo en vivo | 8 |
| 0:50 – 1:10 | Casos reales y anti-errores | Demo + discusión | 7 |
| 1:10 – 1:20 | Break | Pausa | 0 |
| 1:20 – 2:30 | Manos a la obra: construye tu asistente | Ejercicio principal guiado | 10 |
| 2:30 – 2:45 | Testeo en parejas y feedback | Ejercicio + discusión | 2 |
| 2:45 – 3:00 | Cierre, recursos y próximos pasos | Charla + Q&A | 5 |

**Total slides estimado:** 43 + 5 slides de backup con ejemplos extra.

---

## 2. Materiales necesarios (qué preparar antes)

### Espacio y tecnología
- Sala con mesas en islas de 4–5 personas, no estilo teatro.
- Proyector o TV grande.
- WiFi estable para 30 personas conectadas al mismo tiempo.
- Extensiones eléctricas y regletas en cada mesa.
- Pizarra o papelógrafo con marcadores.
- Plan B offline: plantillas descargadas en PDF por si falla internet.

### Materiales físicos
- Post-its de colores.
- Marcadores gruesos.
- Name tags.
- Hojas impresas: **“Canvas del Asistente”** (1 por persona).
- Tarjetas con casos de uso recortables.

### Materiales digitales (facilitador)
- Slide deck con los 43 slides.
- Plantilla de **Prompt Maestro** en Google Docs o Notion.
- Carpeta compartida con ejemplos de asistentes ya armados.
- 3–5 asistentes de demo listos para mostrar en vivo.
- Acceso a ChatGPT o Claude para demo.
- Formulario de feedback post-workshop.

### Preparación para participantes (enviar 48h antes)
- Crear cuenta gratuita en ChatGPT o Claude.
- Traer laptop con cargador. Nada de tablet o celular como herramienta principal.
- Pensar en **1 proceso repetitivo** de su startup que quieran automatizar. Ej: responder preguntas frecuentes, generar cotizaciones, publicar en redes, calificar leads.
- Opcional: traer 5–10 preguntas reales de clientes.

---

## 3. Detalle por bloque

### Bloque 1: Bienvenida y encuadre  
**Duración:** 15 min  
**Objetivo:** Romper el hielo, alinear expectativas y explicar las reglas del juego.  
**Dinámica:** Charla breve + rompehielo con post-its. Pregunta detonadora: *“¿Qué tarea te quita más tiempo cada semana?”*. Se pegan en la pared y el facilitador agrupa por patrones.  
**Key takeaway:** Hoy no venimos a aprender teoría. Venimos a construir algo que puedas usar mañana.  
**Slides:** 5

---

### Bloque 2: La oportunidad IA para startups no-técnicas  
**Duración:** 15 min  
**Objetivo:** Bajar la barrera mental y mostrar que la IA es una ventaja competitiva accesible, incluso sin saber programar.  
**Dinámica:** Charla energética con 3 mini-casos latinoamericanos reales o inspirados. Ej: ecommerce que automatiza soporte, consultora que genera propuestas, foodtech que califica leads.  
**Key takeaway:** No necesitas ser ingeniero. Necesitas conocer tu negocio y saber preguntar.  
**Slides:** 6

---

### Bloque 3: Anatomía de un asistente de IA  
**Duración:** 20 min  
**Objetivo:** Entender los 5 componentes de un asistente: **rol, conocimiento, tono, tareas y límites**.  
**Dinámica:** Charla + demo en vivo. El facilitador desarma un asistente de soporte en pantalla y muestra cómo cada componente cambia la respuesta.  
**Key takeaway:** Un asistente no es magia. Es un prompt bien estructurado + ejemplos + reglas claras.  
**Slides:** 8

---

### Bloque 4: Casos reales y anti-errores  
**Duración:** 20 min  
**Objetivo:** Aprender de asistentes malos y buenos para evitar frustraciones típicas.  
**Dinámica:** Demo comparativa: asistente genérico vs asistente bien diseñado. Luego discusión en parejas: *“¿Qué error viste y cómo lo evitarías?”*  
**Key takeaway:** Si tu asistente no tiene contexto ni límites, va a inventar. El diseño es tu responsabilidad.  
**Slides:** 7

---

### Bloque 5: Break  
**Duración:** 10 min  
**Objetivo:** Recargar energía antes del ejercicio principal.  
**Dinámica:** Pausa libre. Se recomienda estirarse, hidratarse y revisar que todos tengan acceso a ChatGPT.  
**Key takeaway:** Vuelve con la laptop abierta y tu caso de uso elegido.  
**Slides:** 0

---

### Bloque 6: Manos a la obra: construye tu asistente  
**Duración:** 70 min  
**Objetivo:** Construir un asistente funcional para un proceso real de su startup.  
**Dinámica:** Ejercicio guiado paso a paso. El facilitador muestra cada paso en pantalla, da tiempo para ejecutar y circula por las mesas resolviendo dudas.  
**Key takeaway:** Un asistente versión 1 se construye en menos de una hora si tienes claro el proceso.  
**Slides:** 10

---

### Bloque 7: Testeo en parejas y feedback  
**Duración:** 15 min  
**Objetivo:** Probar el asistente con un compañero y detectar mejoras rápidas.  
**Dinámica:** En parejas, cada uno hace 3 preguntas reales al asistente del otro. Luego comparten un hallazgo: *“lo que más me sorprendió”* o *“lo que rompería”*.  
**Key takeaway:** Testear con usuarios reales separa un demo bonito de una herramienta útil.  
**Slides:** 2

---

### Bloque 8: Cierre, recursos y próximos pasos  
**Duración:** 15 min  
**Objetivo:** Consolidar aprendizajes y dar una ruta clara para seguir iterando en casa.  
**Dinámica:** Charla breve + Q&A + entrega de recursos digitales. Se invita a compartir en voz alta un compromiso de 7 días.  
**Key takeaway:** Tu asistente no está terminado. Está empezando. Itera cada semana.  
**Slides:** 5

---

## 4. Ejercicio principal del workshop  
### “Construye tu Asistente de IA en 5 pasos”  
**Duración total:** 70 min  
**Materiales:** Laptop, plantilla de Prompt Maestro, acceso a ChatGPT o Claude.

### Paso 0 — Elige tu proceso (5 min)
Elige **un solo** proceso de tu startup. Opciones:
- Responder preguntas frecuentes de clientes.
- Generar respuestas para comentarios en redes.
- Crear borradores de correos de ventas.
- Resumir reuniones o notas.
- Generar ideas de contenido para redes.

Regla: si no lo puedes explicar en 2 frases, todavía no es tu proceso.

### Paso 1 — Define rol y objetivo (10 min)
Completa esta frase:
> “Eres un asistente para [nombre de tu startup]. Tu objetivo es ayudar a [audiencia] a [resultado].”

Ejemplo:  
*“Eres Sofía, asistente de una tienda online de café. Tu objetivo es ayudar a clientes nuevos a elegir su primer café y resolver dudas de envío.”*

### Paso 2 — Carga conocimiento (15 min)
Pega dentro del prompt:
- 5–10 preguntas frecuentes reales con respuestas breves.
- Texto de tu web o catálogo.
- Políticas de envío, precios, horarios.
- Lo que NO debe responder.

Si usas ChatGPT Plus, puedes crear un GPT y subir un archivo. Si usas versión gratuita, pega el conocimiento directamente en el prompt.

### Paso 3 — Define tono y límites (15 min)
Escribe reglas claras:
- Tono: cercano, profesional, divertido, directo.
- Extensión: máximo 80 palabras.
- Qué hacer si no sabe la respuesta.
- Cuándo escalar a un humano.
- Qué datos no compartir.

Ejemplo:  
*“No inventes precios ni fechas. Si no tienes la información, responde: ‘Déjame confirmarlo con el equipo y te escribo hoy mismo’.”*

### Paso 4 — Prueba y ajusta (15 min)
Haz 5 preguntas reales a tu asistente. Evalúa:
- ¿Respondió lo que preguntaste?
- ¿Inventó algo?
- ¿El tono es correcto?
- ¿Fue útil o solo decorativo?

Ajusta el prompt después de cada prueba. No busques perfección, busca funcionalidad.

### Paso 5 — Guarda y comparte (10 min)
- Copia tu prompt maestro en un Google Doc o Notion.
- Ponle nombre a tu asistente.
- Compártelo con un compañero para recibir feedback rápido.
- Si usas ChatGPT Plus, guárdalo como GPT personalizado.

### Plantilla de Prompt Maestro

```text
# Rol
Eres [nombre del asistente], asistente de [startup] para [tarea].

# Objetivo
Ayudar a [audiencia] a [resultado] de forma [tono].

# Conocimiento
Aquí está la información de la empresa:
[pegar FAQ, productos, precios, políticas]

# Tono y estilo
- Cercano, sin tecnicismos.
- Respuestas en menos de 80 palabras.
- Usa emojis solo si la marca lo permite.
- Siempre cierra con una pregunta o siguiente paso.

# Tareas
- Responder preguntas sobre [tema].
- Ayudar a [acción].
- Redactar [tipo de contenido].

# Límites
- No inventar precios, fechas ni datos.
- Si no sabes, di: "No tengo esa información, te conecto con [persona]".
- No compartir datos personales.
- Si el usuario pide algo fuera de tu alcance, deriva a un humano.

# Formato de respuesta
1. Saludo breve.
2. Respuesta directa.
3. Pregunta de cierre o siguiente paso.
```

---

## 5. Recursos para llevar a casa

- **Plantilla de Prompt Maestro** en Google Docs/Notion.
- **Checklist de 10 puntos** para mejorar tu asistente esta semana.
- **Guía rápida:** cómo convertir tu prompt en un GPT personalizado con ChatGPT Plus.
- **Lista de herramientas gratuitas:** ChatGPT, Claude, Google AI Studio, Poe, Make, Zapier, Botpress, Voiceflow.
- **Mini-playbook de casos de uso** por área: ventas, soporte, marketing, operaciones.
- **Plantilla de Canvas del Asistente** en PDF.
- **5 prompts de prueba** para evaluar cualquier asistente.
- **Video tutorial de 10 minutos** para iterar en casa.
- **Acceso a comunidad o grupo de WhatsApp** del workshop para seguimiento.
- **Plan de 7 días:**
  - Día 1–2: prueba con 10 preguntas reales.
  - Día 3–4: comparte tu asistente con 2 clientes o amigos.
  - Día 5–7: conecta tu asistente a tu web o WhatsApp con herramientas no-code.

---

## 6. Slide count estimado por sección

| Sección | Slides |
|---|---|
| Bienvenida y encuadre | 5 |
| Oportunidad IA para startups no-técnicas | 6 |
| Anatomía de un asistente de IA | 8 |
| Casos reales y anti-errores | 7 |
| Break | 0 |
| Manos a la obra: construye tu asistente | 10 |
| Testeo en parejas y feedback | 2 |
| Cierre, recursos y próximos pasos | 5 |
| **Total** | **43** |

**Backup recomendado:** 5 slides extra con ejemplos de asistentes por industria.