# GPT-5.6 Terra — startup_content/workshop_outline

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 52.002s | tokens_per_second: 105.2
- input_tokens: 186 | output_tokens: 5469
- judge_score: 5.0 | justificación: 

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

# Workshop Presencial: “Construye tu Asistente de IA para tu Startup - Workshop Práctico”

**Duración total:** 3 horas  
**Formato:** Presencial, altamente práctico  
**Audiencia:** 20–30 emprendedores early-stage no técnicos  
**Objetivo general:** Que cada participante salga con un primer asistente de IA funcional —o al menos un prototipo claramente definido y listo para construir— que resuelva una tarea real de su startup.

---

## Resultado esperado al finalizar

Cada participante tendrá:

- Un caso de uso concreto y priorizado para IA en su startup.
- Un “brief” claro de su asistente: rol, usuario, tarea, inputs, outputs y límites.
- Un prompt base reutilizable.
- Un asistente configurado en una herramienta no-code, por ejemplo:
  - ChatGPT (GPT personalizado / instrucciones)
  - Claude Project
  - Gemini Gem
  - Alternativa simple: un chat con prompt maestro guardado
- Una prueba real con ejemplos de su negocio.
- Un plan de iteración de 7 días.

---

# 1. Agenda detallada con tiempos

| Hora | Bloque | Duración |
|---|---:|---:|
| 0:00 – 0:10 | Bienvenida, contexto y reglas del juego | 10 min |
| 0:10 – 0:30 | IA útil para startups: dónde genera valor de verdad | 20 min |
| 0:30 – 0:45 | Elegir el problema correcto para tu asistente | 15 min |
| 0:45 – 1:05 | Anatomía de un buen asistente de IA | 20 min |
| 1:05 – 1:15 | Demo en vivo: de idea a asistente funcional | 10 min |
| 1:15 – 1:25 | Pausa / café / soporte de setup | 10 min |
| 1:25 – 2:15 | Ejercicio principal: construye tu asistente | 50 min |
| 2:15 – 2:40 | Pruebas, mejora de prompts y feedback entre pares | 25 min |
| 2:40 – 2:55 | Show & tell: demos rápidas de participantes | 15 min |
| 2:55 – 3:00 | Cierre, plan de 7 días y próximos pasos | 5 min |

---

# 2. Materiales necesarios y preparación previa

## Para preparar antes del workshop

### Herramientas digitales

Pedir a los participantes que lleguen con:

- Laptop cargada.
- Acceso a una cuenta de al menos una plataforma de IA:
  - ChatGPT
  - Claude
  - Gemini
- Acceso a internet.
- Idealmente, una suscripción de pago si la tienen, pero el workshop debe poder realizarse con versiones gratuitas.
- Una carpeta con materiales básicos de su startup, si los tienen:
  - Presentación o pitch deck
  - Descripción del producto
  - Landing page
  - Mensajes de ventas
  - FAQ
  - Perfil de cliente ideal
  - Entrevistas con clientes
  - Ejemplos de contenido o emails
  - Manuales, SOPs o documentos internos

> Recomendación: enviar un correo 3–5 días antes con una checklist y una mini guía para crear cuenta en la herramienta recomendada.

---

## Materiales físicos

- Proyector y pantalla.
- Micrófono, si la sala lo requiere.
- Wi-Fi estable para 30 personas.
- Regletas/extensiones eléctricas.
- Post-its de al menos dos colores.
- Marcadores gruesos.
- Hojas impresas del “Canvas de Asistente de IA”.
- Hojas impresas del “Prompt Builder”.
- Tarjetas o stickers para votación.
- Reloj visible o temporizador proyectado.
- Pizarrón, rotafolio o pared para post-its.
- Cinta adhesiva.

---

## Materiales para el facilitador

- Presentación preparada.
- Ejemplo de startup ficticia para demos, por ejemplo:
  - SaaS de gestión para restaurantes
  - Marketplace de servicios para pymes
  - Fintech de educación financiera
- 2–3 asistentes preparados previamente para mostrar:
  1. Asistente de research de clientes.
  2. Asistente de ventas y follow-up.
  3. Asistente de creación de contenido.
- QR con recursos, plantillas y enlaces.
- Plan B offline: screenshots del proceso y prompts impresos, por si falla el internet.

---

# 3. Bloques del workshop

---

## Bloque 1. Bienvenida, contexto y reglas del juego

**Duración:** 10 minutos  
**Formato:** Charla breve + interacción rápida  
**Slides estimados:** 3–4

### Objetivo

Romper el hielo, alinear expectativas y dejar claro que este no es un workshop de “teoría de IA”, sino de construcción práctica.

### Dinámica

1. Bienvenida energética.
2. Pregunta al público:
   - “¿Quién ya usa IA al menos una vez por semana?”
   - “¿Quién siente que la usa, pero todavía no logra resultados consistentes?”
3. Explicar el objetivo de salida:
   - “Hoy no vienen a aprender todos los conceptos de IA. Vienen a salir con un asistente para una tarea concreta.”
4. Definir reglas:
   - Construir antes de perfeccionar.
   - Elegir un problema pequeño y repetible.
   - Probar con datos reales.
   - No compartir información sensible de clientes, finanzas o empleados en herramientas públicas.

### Key takeaway

**La IA genera valor cuando se convierte en un flujo de trabajo repetible, no cuando solo se usa para hacer preguntas sueltas.**

---

## Bloque 2. IA útil para startups: dónde genera valor de verdad

**Duración:** 20 minutos  
**Formato:** Charla interactiva + ejemplos  
**Slides estimados:** 7–9

### Objetivo

Ayudar a los participantes a identificar usos concretos y realistas de IA en una startup early-stage.

### Dinámica

Presentar la idea central:

> Un asistente de IA no reemplaza a tu startup ni a tu equipo. Te ayuda a ejecutar más rápido una tarea específica, repetitiva y basada en información.

Mostrar oportunidades en cinco áreas:

1. **Clientes y research**
   - Resumir entrevistas.
   - Detectar patrones de dolor.
   - Crear perfiles de cliente ideal.
   - Analizar reviews y feedback.

2. **Ventas**
   - Preparar mensajes de outreach.
   - Personalizar follow-ups.
   - Calificar leads.
   - Preparar guiones de discovery calls.

3. **Marketing y contenido**
   - Crear ideas de contenido.
   - Adaptar mensajes a canales.
   - Redactar newsletters.
   - Crear primeros borradores de casos de éxito.

4. **Operaciones**
   - Convertir procesos en checklists.
   - Documentar SOPs.
   - Resumir reuniones.
   - Generar borradores de propuestas.

5. **Producto**
   - Organizar feedback.
   - Crear user stories.
   - Convertir dolores de clientes en hipótesis.
   - Generar FAQs y documentación inicial.

### Actividad rápida: “¿Qué tarea te roba tiempo?”

Pedir que cada persona escriba en un post-it:

- Una tarea que hace frecuentemente.
- Que le toma al menos 30 minutos por semana.
- Que sigue una lógica relativamente repetible.
- Que le gustaría delegar parcialmente.

Pegar los post-its en una pared dividida por categorías: Ventas, Marketing, Operaciones, Producto, Clientes.

### Key takeaway

**No empieces construyendo “un chatbot para todo”. Empieza por una tarea específica que consume tiempo y tiene un resultado claro.**

---

## Bloque 3. Elegir el problema correcto para tu asistente

**Duración:** 15 minutos  
**Formato:** Ejercicio individual + discusión en parejas  
**Slides estimados:** 4–5

### Objetivo

Que cada participante seleccione un único caso de uso viable para construir durante el workshop.

### Dinámica

Entregar o proyectar la matriz de priorización:

| Criterio | Pregunta |
|---|---|
| Frecuencia | ¿Esta tarea sucede semanalmente? |
| Dolor | ¿Me quita tiempo, energía o foco? |
| Claridad | ¿Sé cómo luce un buen resultado? |
| Repetibilidad | ¿La tarea sigue pasos similares? |
| Riesgo | ¿Puedo probarla sin tomar decisiones críticas automáticamente? |
| Datos | ¿Tengo ejemplos, contexto o documentos para alimentarla? |

Pedir que cada participante liste tres posibles asistentes y los evalúe rápidamente de 1 a 5.

Luego elegir uno.

### Ejemplos de asistentes aptos para construir

- “Asistente de follow-up para leads de mi startup.”
- “Asistente que convierte entrevistas de clientes en insights.”
- “Asistente para crear posts de LinkedIn para mi ICP.”
- “Asistente para responder preguntas frecuentes de usuarios.”
- “Asistente para preparar propuestas comerciales.”
- “Asistente para convertir reuniones en tareas y próximos pasos.”
- “Asistente para analizar feedback de clientes y detectar prioridades.”

### Ejemplos que se deben evitar en esta sesión

- “Quiero crear un copiloto que maneje toda mi empresa.”
- “Quiero automatizar por completo mis ventas.”
- “Quiero que tome decisiones financieras.”
- “Quiero construir un agente conectado a todos mis sistemas.”
- “Quiero un chatbot complejo para mi producto sin tener contenido ni FAQs.”

### Key takeaway

**Un buen primer asistente resuelve un problema pequeño, frecuente, medible y de bajo riesgo.**

---

## Bloque 4. Anatomía de un buen asistente de IA

**Duración:** 20 minutos  
**Formato:** Charla + construcción guiada  
**Slides estimados:** 7–8

### Objetivo

Enseñar una estructura sencilla para diseñar asistentes que entreguen respuestas útiles y consistentes.

### Dinámica

Presentar el framework: **ROL + OBJETIVO + CONTEXTO + PROCESO + FORMATO + LÍMITES + EJEMPLOS**

### 1. Rol

¿Quién es el asistente?

Ejemplo:

> “Eres un asistente de ventas B2B para una startup SaaS que ayuda a restaurantes a gestionar inventario.”

### 2. Objetivo

¿Qué debe lograr?

> “Tu objetivo es crear mensajes de seguimiento personalizados para leads que asistieron a una demo.”

### 3. Contexto

¿Qué necesita saber de la startup?

- Producto.
- Público objetivo.
- Propuesta de valor.
- Tono de comunicación.
- Objeciones frecuentes.
- Etapa del cliente.

### 4. Proceso

¿Qué pasos debe seguir antes de responder?

> “Primero identifica el tipo de lead. Luego selecciona el beneficio más relevante. Después redacta un mensaje de máximo 100 palabras. Finalmente, sugiere un CTA.”

### 5. Formato de salida

¿Cómo debe entregar la respuesta?

- Tabla.
- Email.
- Lista de acciones.
- Resumen ejecutivo.
- Guion de llamada.
- Post para LinkedIn.
- Checklist.

### 6. Límites y guardrails

¿Qué no debe hacer?

- No inventar datos.
- No prometer resultados.
- No usar tono agresivo.
- No dar asesoría legal o financiera definitiva.
- Pedir aclaraciones cuando falte contexto.

### 7. Ejemplos

Mostrar que dar uno o dos ejemplos de “buen output” mejora mucho la calidad.

### Prompt base ejemplo

```text
Eres un asistente de ventas para [NOMBRE DE STARTUP].

Tu objetivo es ayudarme a redactar mensajes de follow-up para leads B2B.

Contexto de la empresa:
- Producto: [DESCRIBE TU PRODUCTO]
- Cliente ideal: [ICP]
- Problema que resolvemos: [DOLOR]
- Propuesta de valor: [VALOR]
- Tono: cercano, claro, profesional y sin exageraciones.

Cuando recibas información de un lead:
1. Identifica su principal dolor o posible necesidad.
2. Redacta un mensaje de seguimiento de máximo 120 palabras.
3. Personaliza el mensaje usando solo la información entregada.
4. Incluye un CTA simple para agendar una conversación o responder una pregunta.
5. No inventes datos, casos de éxito ni resultados.

Entrega:
- Asunto del email
- Mensaje
- CTA
- Una versión corta para WhatsApp o LinkedIn
```

### Key takeaway

**La calidad del asistente depende menos de “usar la mejor herramienta” y más de darle instrucciones claras, contexto real y un formato específico de salida.**

---

## Bloque 5. Demo en vivo: de idea a asistente funcional

**Duración:** 10 minutos  
**Formato:** Demo en vivo  
**Slides estimados:** 2–3

### Objetivo

Reducir la ansiedad técnica demostrando que un primer asistente se puede construir rápidamente con una herramienta accesible.

### Dinámica

Construir en vivo un asistente sencillo, por ejemplo:

**“Asistente de entrevistas de clientes”**

Input:
- Transcripción o notas de una entrevista.

Output:
- Dolor principal.
- Jobs to be done.
- Frases textuales destacadas.
- Objeciones.
- Oportunidades de producto.
- Preguntas para la próxima entrevista.

Mostrar el flujo:

1. Abrir ChatGPT, Claude o Gemini.
2. Pegar el prompt maestro.
3. Agregar contexto de la startup.
4. Incluir una entrevista real o ficticia.
5. Revisar output.
6. Mejorar una instrucción en vivo.
7. Volver a probar.

### Key takeaway

**No necesitas programar para empezar: puedes construir una primera versión útil con un buen prompt, contexto y pruebas reales.**

---

## Bloque 6. Pausa / café / soporte de setup

**Duración:** 10 minutos  
**Formato:** Pausa activa + soporte técnico  
**Slides estimados:** 1

### Objetivo

Dar energía al grupo y asegurar que todos tengan acceso a una herramienta antes del ejercicio principal.

### Dinámica

Mientras las personas toman café, el facilitador y asistentes ayudan a quienes tengan problemas de acceso, cuentas o conexión.

### Key takeaway

**El objetivo es que nadie se quede fuera por una barrera técnica.**

---

## Bloque 7. Ejercicio principal: construye tu asistente de IA

**Duración:** 50 minutos  
**Formato:** Trabajo individual + acompañamiento del facilitador + apoyo entre pares  
**Slides estimados:** 6–8

### Objetivo

Que cada participante construya y pruebe la primera versión de un asistente para una tarea real de su startup.

### Dinámica

Ver ejercicio principal detallado más abajo.

### Key takeaway

**Un asistente no se “termina” en una sesión: se construye, prueba, ajusta y mejora con uso real.**

---

## Bloque 8. Pruebas, mejora de prompts y feedback entre pares

**Duración:** 25 minutos  
**Formato:** Prueba práctica + parejas + iteración  
**Slides estimados:** 4–5

### Objetivo

Que los participantes detecten fallas, ajusten sus instrucciones y mejoren la utilidad de su asistente.

### Dinámica

Formar parejas. Cada participante muestra:

1. El problema que su asistente resuelve.
2. El prompt o instrucciones principales.
3. Un input real.
4. El output generado.

La pareja usa una checklist de feedback:

- ¿Está claro qué hace el asistente?
- ¿El output sirve para una acción concreta?
- ¿Qué información falta?
- ¿Qué parte de la respuesta sobra?
- ¿El formato es fácil de usar?
- ¿Está inventando información?
- ¿Qué instrucción se podría agregar para mejorar el resultado?

Luego, cada persona realiza una mejora y corre una nueva prueba.

### Prompt de mejora sugerido

```text
Evalúa la respuesta anterior usando estos criterios:
- Claridad
- Precisión
- Utilidad práctica
- Personalización al contexto
- Formato

Indica qué se puede mejorar y luego entrega una nueva versión mejorada.
No inventes información que no esté en el contexto.
```

### Key takeaway

**La primera respuesta de IA es un borrador. El valor aparece cuando aprendes a revisar, corregir y estandarizar el resultado.**

---

## Bloque 9. Show & tell: demos rápidas de participantes

**Duración:** 15 minutos  
**Formato:** Presentaciones rápidas + celebración  
**Slides estimados:** 1–2

### Objetivo

Generar aprendizaje colectivo, inspiración y sensación de avance tangible.

### Dinámica

Invitar a 4–5 voluntarios a presentar en máximo 2 minutos:

1. Nombre de su startup.
2. Tarea que eligieron.
3. Nombre de su asistente.
4. Ejemplo de output.
5. Qué mejoró respecto a hacerlo manualmente.

Formato sugerido:

> “Antes me tomaba ___ minutos hacer ___. Mi asistente me ayuda a ___. Todavía debo revisar ___, pero ahora puedo avanzar más rápido.”

Reconocer tanto los asistentes más sofisticados como los más simples pero útiles.

### Key takeaway

**El mejor asistente no es el más complejo: es el que realmente se incorpora al trabajo semanal.**

---

## Bloque 10. Cierre, plan de 7 días y próximos pasos

**Duración:** 5 minutos  
**Formato:** Cierre inspirador + compromiso individual  
**Slides estimados:** 2–3

### Objetivo

Evitar que el asistente quede abandonado después del workshop y convertir el aprendizaje en hábito.

### Dinámica

Pedir que cada participante complete:

> “Durante los próximos 7 días, usaré mi asistente para ______ al menos ______ veces.”

Plan de 7 días:

- **Día 1:** usarlo en una tarea real.
- **Día 2:** guardar los mejores outputs.
- **Día 3:** detectar dónde falla.
- **Día 4:** mejorar el prompt.
- **Día 5:** probar con otro caso real.
- **Día 6:** crear una plantilla o proceso.
- **Día 7:** decidir si se mantiene, ajusta o descarta.

### Key takeaway

**Tu asistente empieza a tener valor cuando lo integras a una rutina real de trabajo.**

---

# 4. Ejercicio principal del workshop

## Nombre del ejercicio

# “Tu primer asistente útil en 50 minutos”

## Objetivo

Construir un asistente de IA que ayude con una tarea concreta, repetitiva y relevante para la startup de cada participante.

---

## Paso 1. Define la tarea específica — 5 minutos

Completar:

- La tarea que quiero mejorar es: __________
- Hoy la hago: diaria / semanal / mensual.
- Me toma aproximadamente: __________
- El resultado que quiero obtener es: __________
- Mi usuario final es: yo / mi equipo / clientes / leads.

Ejemplo:

> “Quiero convertir notas de llamadas con prospectos en emails de follow-up personalizados.”

---

## Paso 2. Completa el Canvas de Asistente de IA — 10 minutos

### Canvas

| Elemento | Pregunta |
|---|---|
| Nombre del asistente | ¿Cómo lo llamarás? |
| Rol | ¿Qué tipo de asistente es? |
| Usuario | ¿Quién lo usará? |
| Problema | ¿Qué tarea resuelve? |
| Resultado esperado | ¿Qué debe entregar? |
| Contexto de negocio | ¿Qué debe saber sobre tu startup? |
| Inputs | ¿Qué información recibirá? |
| Output | ¿En qué formato debe responder? |
| Tono | ¿Cómo debe comunicarse? |
| Límites | ¿Qué no debe hacer? |
| Criterio de éxito | ¿Cómo sabrás si funciona? |

---

## Paso 3. Crea tu prompt maestro — 10 minutos

Usar esta estructura:

```text
Eres [ROL DEL ASISTENTE] para [NOMBRE DE LA STARTUP].

Tu objetivo es [RESULTADO CONCRETO].

Contexto de la startup:
- Producto o servicio: [DESCRIPCIÓN]
- Cliente ideal: [ICP]
- Problema que resolvemos: [DOLOR]
- Propuesta de valor: [VALOR DIFERENCIAL]
- Tono de comunicación: [TONO]

Cuando recibas [TIPO DE INPUT], debes:
1. [PASO 1]
2. [PASO 2]
3. [PASO 3]
4. [PASO 4]

Entrega la respuesta en este formato:
[FORMATO DE OUTPUT]

Reglas:
- No inventes datos.
- Si falta información importante, haz máximo [X] preguntas antes de responder.
- Mantén un tono [TONO].
- Evita [COSAS A EVITAR].
```

---

## Paso 4. Agrega contexto real — 10 minutos

Pedir que cada persona agregue al menos uno de estos elementos:

- Una descripción de producto.
- Su landing page.
- Una propuesta comercial.
- Una transcripción de cliente.
- Un email anterior.
- Una lista de FAQs.
- Ejemplos de tono de marca.
- Una tabla de leads.
- Feedback de usuarios.

> Regla práctica: mientras más claro y relevante sea el contexto, mejores serán las respuestas.

---

## Paso 5. Prueba con tres casos reales — 10 minutos

Cada participante debe probar tres inputs distintos:

1. Caso fácil.
2. Caso típico.
3. Caso difícil o incompleto.

Ejemplo para un asistente de ventas:

- Lead muy interesado.
- Lead que dejó de responder.
- Lead con una objeción de precio.

---

## Paso 6. Itera una vez — 5 minutos

Después de observar los resultados, responder:

- ¿Qué funcionó?
- ¿Qué faltó?
- ¿Qué fue demasiado largo o genérico?
- ¿Qué instrucción debo agregar?
- ¿Qué dato necesito entregar mejor?

Ajustar el prompt y volver a probar.

---

# 5. Recursos para llevar a casa

Entregar mediante QR, email o carpeta compartida.

## Plantillas

1. **Canvas de Asistente de IA**
   - Rol.
   - Problema.
   - Usuario.
   - Inputs.
   - Outputs.
   - Límites.
   - Métricas.

2. **Prompt Builder**
   - Plantilla editable para distintos casos de uso.

3. **Biblioteca de prompts para startups**
   - Ventas.
   - Research.
   - Marketing.
   - Atención al cliente.
   - Operaciones.
   - Producto.
   - Fundraising.

4. **Checklist de evaluación de outputs**
   - ¿Es preciso?
   - ¿Es útil?
   - ¿Es accionable?
   - ¿Mantiene el tono?
   - ¿Está basado en el contexto?
   - ¿Necesita revisión humana?

5. **Guía “Cómo mejorar un prompt en 10 minutos”**
   - Añadir contexto.
   - Especificar formato.
   - Agregar ejemplos.
   - Definir límites.
   - Pedir preguntas de aclaración.
   - Probar con casos variados.

---

## Ejemplos de asistentes listos para adaptar

- Asistente para resumir entrevistas de clientes.
- Asistente para crear mensajes de outbound.
- Asistente para follow-ups de ventas.
- Asistente para convertir reuniones en tareas.
- Asistente para generar contenido de LinkedIn.
- Asistente para responder FAQs.
- Asistente para preparar propuestas comerciales.
- Asistente para analizar feedback de producto.
- Asistente para escribir descripciones de producto.
- Asistente para preparar reuniones con inversores.

---

## Recursos recomendados

- Guía de buenas prácticas para uso responsable de IA.
- Recomendaciones de privacidad:
  - No subir datos sensibles sin autorización.
  - Anonimizar información de clientes.
  - No compartir contraseñas, datos bancarios o información legal confidencial.
  - Revisar siempre outputs antes de enviarlos a clientes o usarlos en decisiones importantes.
- Lista de herramientas no-code para la siguiente etapa:
  - Zapier
  - Make
  - Notion AI
  - Airtable
  - Tally
  - Typeform
  - HubSpot
  - Google Sheets + IA
  - n8n, para quienes quieran explorar automatización más adelante

---

# 6. Slide count estimado por sección

| Sección | Slides estimados |
|---|---:|
| Bienvenida y objetivos | 3–4 |
| IA útil para startups | 7–9 |
| Elegir el problema correcto | 4–5 |
| Anatomía de un buen asistente | 7–8 |
| Demo en vivo | 2–3 |
| Pausa / instrucciones de setup | 1 |
| Ejercicio principal | 6–8 |
| Pruebas y feedback | 4–5 |
| Show & tell | 1–2 |
| Cierre y plan de 7 días | 2–3 |
| **Total estimado** | **37–48 slides** |

---

# Sugerencia de mensaje de apertura

> “No necesitas saber programar para empezar a usar IA en tu startup. Pero sí necesitas claridad: qué problema estás resolviendo, qué información tienes y cómo se ve un buen resultado. Hoy vamos a construir algo pequeño, útil y real. Si al final del workshop tu asistente te ahorra aunque sea 30 minutos por semana, ya estamos ganando.”

---

# Sugerencia de mensaje de cierre

> “La IA no premia a quien prueba más herramientas. Premia a quien convierte una tarea repetitiva en un sistema mejor. Tu misión esta semana no es construir diez asistentes: es usar uno, mejorarlo y convertirlo en parte de cómo trabaja tu startup.”