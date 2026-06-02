# DeepSeek V4 Flash (OpenRouter) — startup_content/workshop_outline

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.95 | quality: 9.44
- latency_total: 140.016s | tokens_per_second: 51.3
- input_tokens: 198 | output_tokens: 7176
- judge_score: 4.6 | justificación: 

## Respuesta completa

# Outline Completo: "Construye tu Asistente de IA para tu Startup - Workshop Práctico"

**Duración:** 3 horas (180 min)  
**Audiencia:** 20-30 emprendedores early-stage no técnicos  
**Formato:** Presencial, práctico, energético  
**Herramienta principal:** Poe.com (gratuita, sin código)

---

## 1. Agenda Detallada con Tiempos

| Hora | Bloque | Duración |
|------|--------|----------|
| 0:00 - 0:15 | Bienvenida y Setup | 15 min |
| 0:15 - 0:45 | Módulo 1: ¿Qué es un asistente de IA y por qué tu startup lo necesita? | 30 min |
| 0:45 - 1:30 | Módulo 2: Diseñando tu asistente | 45 min |
| 1:30 - 1:45 | Break | 15 min |
| 1:45 - 2:45 | Módulo 3: Construyendo tu asistente (Ejercicio Principal) | 60 min |
| 2:45 - 3:00 | Cierre, Demos y Recursos | 15 min |

---

## 2. Materiales Necesarios (Preparar Antes)

### Para el facilitador:
- [ ] Proyector y laptop con slides
- [ ] Conexión a internet estable (backup: hotspot móvil)
- [ ] Pizarrón o rotafolio + marcadores de colores
- [ ] Post-its (2 colores) y bolígrafos para participantes
- [ ] Parlante portátil (para música ambiental durante el break)
- [ ] Bot de ejemplo funcional en Poe (mostrar demo)

### Para los participantes (pedir con anticipación):
- [ ] Laptop o tablet con navegador actualizado
- [ ] Cuenta de correo para registrarse en Poe (recomendar crear cuenta antes)
- [ ] Opcional: un archivo PDF o texto con información de su startup (FAQ, descripción, etc.)

### Material impreso (copias para todos):
- [ ] **Hoja de trabajo "Diseña tu Asistente"** (ver sección 4)
- [ ] **Guía rápida de Poe** (1 página con pasos clave)
- [ ] **Tarjeta de recursos para llevar a casa** (QR con enlaces)

### Digital:
- [ ] Presentación de slides (27-34 slides, ver detalle abajo)
- [ ] Enlace a video tutorial de respaldo (por si internet falla)
- [ ] Plantilla de prompts de ejemplo en documento compartido (Google Docs)

---

## 3. Desarrollo Detallado por Bloque

### Bloque 1: Bienvenida y Setup (15 min)

**Título:** "De la idea al prototipo en 3 horas"

**Objetivo:** Romper el hielo, alinear expectativas y generar entusiasmo.

**Dinámica:**
- (3 min) Facilitador se presenta con energía: "Hoy no vas a escuchar teoría aburrida. Vas a construir algo que puedas usar mañana con tus clientes."
- (5 min) Ronda rápida: "Levanta la mano si…" (preguntas divertidas: ¿quién ha usado ChatGPT? ¿quién cree que la IA reemplazará su trabajo? ¿quién quiere un asistente que trabaje 24/7?)
- (5 min) Demo relámpago: Facilitador abre su bot de ejemplo (ej: "BotDelivery" para una startup de delivery) y hace 3 preguntas en vivo. Muestra cómo responde con personalidad y datos reales.
- (2 min) Explicar agenda y regla de oro: "No importa si nunca has programado. Hoy serás el arquitecto de tu propio asistente."

**Key takeaway:** No necesitas saber programar para crear un asistente de IA útil para tu startup. En 3 horas tendrás un prototipo funcional.

**Slides:** 4 (título, agenda, demo en vivo, "¿Qué lograrás hoy?")

---

### Bloque 2: Fundamentos de Asistentes de IA (30 min)

**Título:** "¿Qué es un asistente de IA y cómo puede ayudar a tu startup?"

**Objetivo:** Entender conceptos clave (LLM, prompt, personalidad, base de conocimiento) y casos de uso reales.

**Dinámica:**
- (10 min) **Charla rápida:** Explicar con analogía del "empleado digital":
  - **LLM = cerebro** (ChatGPT, Claude)
  - **Prompt = manual de instrucciones** (qué hace, cómo habla, qué no debe hacer)
  - **Base de conocimiento = manual de productos/FAQ**
  - Mostrar 3 casos de startups reales (con fotos o logos):
    1. Atención al cliente 24/7 (ej: ecommerce)
    2. Calificación de leads (ej: SaaS B2B)
    3. Onboarding de usuarios (ej: app mobile)
- (10 min) **Discusión interactiva:** "¿Qué problema de tu startup podrías resolver con un asistente?" – Cada persona escribe en un post-it y lo pega en la pizarra. Facilitador agrupa por tipo (ventas, soporte, marketing, etc.) y comenta.
- (10 min) **Mini-ejercicio en parejas:** "En 2 minutos, cuéntale a tu compañero una idea de asistente para tu startup. Luego él te da un feedback de 1 minuto." (usar cronómetro)

**Key takeaway:** Un asistente de IA es un "empleado digital" que puedes entrenar con instrucciones y datos. No es magia, es diseño de prompts.

**Slides:** 7 (definición, analogía, 3 casos de uso, cómo funciona, limitaciones comunes, ejercicio de post-its, transición al diseño)

---

### Bloque 3: Diseñando tu Asistente (45 min)

**Título:** "Define el rol, personalidad y conocimiento de tu asistente"

**Objetivo:** Que cada participante complete una hoja de diseño con propósito, tono, límites y ejemplos de preguntas.

**Dinámica:**
- (5 min) **Charla guía:** Facilitador muestra ejemplo completo en la pantalla:
  - **Nombre:** "BotDelivery"
  - **Rol:** Asistente de atención al cliente para startup de delivery de comida
  - **Personalidad:** Amigable, eficiente, usa emojis moderados, habla español neutro
  - **Límites:** Solo responde sobre pedidos activos, no da consejos de salud, no comparte datos personales
  - **Base de conocimiento:** Política de devoluciones, menú, horarios, zonas de entrega
- (15 min) **Ejercicio individual:** Cada participante completa su **Hoja de Diseño** (ver plantilla abajo). Facilitador circula resolviendo dudas.
- (10 min) **Compartir en tríos:** En grupos de 3, cada persona explica su diseño en 2 minutos. Los otros dan feedback: "¿El tono es coherente? ¿Los límites son claros?"
- (10 min) **Feedback general:** Facilitador recoge 3 ejemplos interesantes y los comenta en voz alta. Destaca errores comunes: ser demasiado genérico, no definir límites, olvidar el público objetivo.
- (5 min) **Transición:** "Ahora que tienes el diseño, vamos a convertirlo en un bot real. Prepárate para abrir Poe."

**Key takeaway:** Un buen asistente empieza con un diseño claro de personalidad y límites. Invertir tiempo aquí ahorra horas de ajustes después.

**Slides:** 6 (ejemplo completo, plantilla vacía, consejos para tono, cómo definir límites, errores comunes, instrucción para siguiente bloque)

---

### Break (15 min)

Música alegre, café/agua. Facilitador prepara enlace de Poe y verifica que todos tengan internet.

---

### Bloque 4: Construyendo tu Asistente (60 min) – Ejercicio Principal

**Título:** "Manos a la obra: crea tu primer asistente en Poe"

**Objetivo:** Cada participante crea un bot funcional en Poe con instrucciones personalizadas y base de conocimiento mínima.

**Dinámica (paso a paso, facilitador proyecta y todos siguen):**

| Tiempo | Paso | Detalle |
|--------|------|---------|
| 5 min | **1. Crear cuenta en Poe** | poe.com – Registro con correo o Google. Facilitador muestra en pantalla. Ayuda a quienes tengan problemas. |
| 3 min | **2. Crear nuevo bot** | Click en "Create bot". Elegir modelo base: **ChatGPT** (recomendado por versatilidad). |
| 15 min | **3. Configurar instrucciones del sistema** | Copiar y pegar desde su hoja de diseño: nombre, rol, personalidad, límites, ejemplos de respuestas. Facilitador muestra un prompt de ejemplo completo y da tips: "Sé específico, usa ejemplos, pon reglas claras." |
| 10 min | **4. Subir base de conocimiento** | Opción "Upload knowledge base". Subir archivo (PDF o texto). Si no tienen, usar **FAQ ficticio** que facilitador comparte (ej: preguntas frecuentes de una tienda online). |
| 10 min | **5. Probar el bot** | Escribir 3 preguntas en el chat del bot: una fácil, una compleja, una fuera de límites. Ver cómo responde. |
| 10 min | **6. Iterar** | Ajustar instrucciones según lo que falló. Facilitador da tips rápidos: "Si da respuestas largas, pídele que sea conciso. Si inventa, agrega 'Si no sabes, di que no tienes esa información'." |
| 7 min | **7. Compartir y probar en parejas** | Copiar enlace del bot y enviarlo al compañero. Cada uno hace 2 preguntas al bot del otro y da feedback verbal. |

**Rol del facilitador durante el bloque:**
- Circular constantemente, resolver dudas uno a uno.
- Tener un "bot de ayuda" (otro Poe) donde los participantes puedan preguntar dudas técnicas.
- Animar: "¡Ya tienes un asistente! Ahora pruébalo con preguntas difíciles."

**Para participantes sin contenido propio:** Facilitador comparte enlace a un **FAQ genérico** (ej: "Preguntas frecuentes de una startup de software") para que puedan subirlo.

**Key takeaway:** En menos de una hora puedes tener un prototipo funcional de asistente de IA para tu startup. Lo importante es iterar rápido.

**Slides:** 11 (pantallazos de cada paso en Poe, 3 ejemplos de prompts buenos/malos, tabla de errores comunes y soluciones, instrucciones para compartir)

---

### Bloque 5: Cierre y Próximos Pasos (15 min)

**Título:** "¿Y ahora qué? Lleva tu asistente al siguiente nivel"

**Objetivo:** Celebrar logros, compartir resultados, dar recursos para seguir.

**Dinámica:**
- (6 min) **Mini-demos:** 3 voluntarios (elegir con energía) muestran su bot en 1 minuto cada uno. Facilitador destaca algo positivo de cada uno y da un consejo rápido de mejora.
- (5 min) **Recursos y siguientes pasos:** Facilitador proyecta y comparte:
  - **Guía PDF** "Cómo crear tu asistente de IA en Poe" (paso a paso con capturas)
  - **Plantilla de hoja de diseño** editable (Google Docs)
  - **10 prompts efectivos** para asistentes de startups (ej: ventas, soporte, onboarding)
  - **Herramientas para integrar:** Zapier (conectar con WhatsApp/email), ManyChat (chatbots visuales), Voiceflow (asistentes de voz)
  - **Comunidad de seguimiento:** Enlace a grupo de WhatsApp o Slack para compartir avances
  - **Checklist de lanzamiento:** "10 preguntas para validar tu asistente antes de usarlo con clientes reales"
- (3 min) **Cierre emocional:** "Hoy demostraste que no necesitas ser técnico para innovar con IA. Tu startup tiene un nuevo empleado. Ahora ve y hazlo crecer." – Agradecimientos, fotos del grupo, QR para descargar materiales.
- (1 min) **Encuesta rápida:** Pedir feedback en un post-it (1 cosa que te llevas, 1 cosa que mejorarías).

**Key takeaway:** El prototipo es el punto de partida. Ahora pruébalo con usuarios reales, recoge feedback y mejora.

**Slides:** 4 (gracias, recursos con QR, próximos pasos, encuesta de satisfacción)

---

## 4. Ejercicio Principal del Workshop (Detallado)

**Nombre:** "Construye tu asistente en Poe en 60 minutos"

**Qué harán los participantes:**
1. Crear un bot en Poe con un nombre y descripción.
2. Escribir instrucciones del sistema (system prompt) basadas en su hoja de diseño.
3. Subir un archivo de conocimiento (FAQ, descripción de producto, políticas).
4. Probar el bot con preguntas reales.
5. Iterar el prompt según resultados.
6. Compartir el bot con un compañero para prueba cruzada.

**Resultado esperado:** Cada participante obtiene un enlace público a un asistente de IA funcional que responde preguntas sobre su startup con personalidad y datos coherentes.

**Material de apoyo para el ejercicio:**
- **Hoja de Diseño** (impresa, tamaño carta):
  ```
  Nombre del asistente: _______________
  Rol principal (ej: atención al cliente, lead qualification): _______________
  Personalidad (tono, estilo, palabras clave): _______________
  Público objetivo: _______________
  Límites (qué NO debe hacer): _______________
  Base de conocimiento (qué archivos subirás): _______________
  3 preguntas de ejemplo que debe responder bien:
  1. _______________________
  2. _______________________
  3. _______________________
  ```
- **FAQ ficticio de respaldo** (PDF) para quienes no tengan contenido propio. Incluye 10 preguntas comunes sobre un producto SaaS hipotético.
- **Plantilla de prompt inicial** (para copiar y pegar):
  ```
  Eres [nombre del asistente], el asistente de [nombre de startup]. Tu rol es [rol]. 
  Debes responder siempre en español [neutro/mexicano/argentino] con un tono [amigable/profesional/divertido].
  Reglas:
  - Solo respondes sobre [temas permitidos].
  - Si no sabes la respuesta, di: "No tengo esa información, ¿puedo ayudarte con otra cosa?"
  - No compartas información personal de los usuarios.
  - Mantén las respuestas concisas (máximo 3 oraciones).
  - Usa emojis solo cuando sea apropiado.
  Ejemplo de respuesta ideal:
  Usuario: "¿Cuánto cuesta el plan premium?"
  Asistente: "El plan premium cuesta $29/mes. Incluye acceso ilimitado a todas las funciones y soporte prioritario. ¿Te gustaría probarlo gratis por 7 días? 🚀"
  ```

---

## 5. Recursos para Llevar a Casa

**Formato:** Una hoja impresa (tamaño carta) con QR y enlaces, más una carpeta digital compartida.

### Contenido de la carpeta digital (Google Drive o similar):

1. **Guía PDF** "Cómo crear tu asistente de IA en Poe" (10 páginas, paso a paso con capturas de pantalla)
2. **Plantilla de Hoja de Diseño** editable (Google Docs)
3. **10 Prompts Efectivos para Startups** (ejemplos listos para copiar):
   - Atención al cliente
   - Calificación de leads
   - Onboarding de usuarios
   - FAQ dinámico
   - Generación de ideas de contenido
   - Resumen de feedback de clientes
   - Asistente de ventas
   - Soporte técnico básico
   - Encuestas de satisfacción
   - Asistente de recursos humanos
4. **Enlaces a herramientas complementarias:**
   - Poe.com
   - Zapier (automatizaciones)
   - ManyChat (chatbots visuales)
   - Voiceflow (asistentes de voz)
   - Botpress (open source, más avanzado)
5. **Checklist de Lanzamiento** (10 preguntas para validar antes de usar con clientes):
   - ¿El asistente responde correctamente las 5 preguntas más frecuentes?
   - ¿Maneja bien preguntas fuera de su alcance?
   - ¿El tono es coherente con tu marca?
   - ¿Has probado con al menos 3 personas ajenas al proyecto?
   - ¿Sabes cómo medir su efectividad? (NPS, tasa de resolución)
   - ¿Tienes un plan para actualizar su base de conocimiento?
   - ¿Has definido un límite de palabras por respuesta?
   - ¿El bot maneja correctamente la confidencialidad?
   - ¿Tienes un backup humano cuando el bot no puede responder?
   - ¿Has considerado integrarlo con tu canal de comunicación principal (web, WhatsApp, Messenger)?
6. **Enlace al grupo de comunidad** (WhatsApp o Slack) para seguimiento y resolución de dudas posteriores.

---

## 6. Slide Count Estimado por Sección

| Sección | Slides | Notas |
|---------|--------|-------|
| Bloque 1: Bienvenida | 4 | Título, agenda, demo en vivo, expectativas |
| Bloque 2: Fundamentos | 7 | Conceptos, casos, discusión, ejercicio parejas |
| Bloque 3: Diseño | 6 | Ejemplo, plantilla, consejos, errores, transición |
| Bloque 4: Construcción | 11 | 8 pasos con capturas + 3 de tips/errores |
| Bloque 5: Cierre | 4 | Demos, recursos, próximos pasos, encuesta |
| **Total** | **32** | Ritmo: ~1 slide cada 5-6 minutos |

**Nota:** Los slides deben ser visuales (pocas palabras, muchas imágenes/capturas). Incluir GIFs breves para mostrar pasos en Poe. Usar colores vibrantes y tipografía grande.

---

## Consejos para el Facilitador (Tono Energético y Práctico)

- **Lenguaje corporal:** Muévete por el espacio, no te quedes detrás del podio. Usa gestos amplios.
- **Frases clave:** "Esto no es teoría, es construcción." "Si puedes escribir un correo, puedes diseñar un asistente." "El error es tu mejor maestro hoy."
- **Manejo del tiempo:** Usa cronómetro visible. Si un bloque se alarga, acorta la discusión y ofrece seguimiento en el grupo.
- **Participación:** Cada 10-15 minutos haz una pregunta al aire ("¿Alguien ya tuvo una idea de cómo usar esto en su startup?"). Recompensa con stickers o aplausos.
- **Backup técnico:** Si Poe falla, tener un video pregrabado de la construcción paso a paso. Si internet es inestable, usar hotspot y pedir que algunos compartan datos.
- **Cierre con energía:** Termina con una frase motivacional y una foto grupal. Envía los recursos por correo esa misma noche.

---

**¡Listo! Con este outline tienes un workshop dinámico, práctico y memorable que dejará a los emprendedores con un asistente de IA funcional y ganas de seguir aprendiendo.**