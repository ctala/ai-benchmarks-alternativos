# MiniMax M3 — startup_content/workshop_outline

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.98 | quality: 9.12
- latency_total: 69.11s | tokens_per_second: 106.9
- input_tokens: 341 | output_tokens: 7387
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

# Outline completo del workshop

## **Construye tu Asistente de IA para tu Startup**
### Workshop práctico presencial | 3 horas | 20–30 emprendedores early-stage no técnicos

**Enfoque:** pensar rápido, construir simple, probar con casos reales y salir con un asistente funcional.  
**Estilo:** energético, participativo, con demostraciones, ejercicios cortos y feedback entre pares.

---

# 1. Agenda detallada con tiempos

| Hora | Bloque | Duración | Formato |
|---|---|---:|---|
| 00:00–00:15 | Bienvenida y encuadre del reto | 15 min | Charla + dinámica |
| 00:15–00:40 | IA aplicada a startups: qué sí funciona | 25 min | Charla + ejemplos |
| 00:40–01:00 | Demo: del problema al asistente | 20 min | Demo en vivo |
| 01:00–01:10 | Descanso activo y reset | 10 min | Dinámica |
| 01:10–01:30 | Diseño del caso de uso | 20 min | Ejercicio guiado |
| 01:30–02:00 | Construcción del MVP sin código | 30 min | Ejercicio práctico |
| 02:00–02:10 | Pausa | 10 min | Descanso |
| 02:10–02:35 | Prueba, feedback y mejora | 25 min | Prueba + discusión |
| 02:35–02:50 | Qué hacer después en tu startup | 15 min | Charla + plan |
| 02:50–03:00 | Cierre, snapshots y próximos pasos | 10 min | Cierre + networking |

**Total: 180 minutos**

---

# 2. Materiales necesarios para preparar antes

## A. Materiales físicos

Para 20–30 participantes:

- Hojas grandes de papel adhesivo o cartulina por equipo.
- Marcadores de colores, mínimo 2 por participante.
- Post-its de tres colores:
  - Verde: ideas y respuestas.
  - Amarillo: riesgos o dudas.
  - Rosa: decisiones o improvements.
- Tarjetas o sobres de “caso de usuario”.
- Cronómetro visible con proyector.
- Hojas de trabajo impresas o compartidas digitalmente.
- Etiquetas adhesivas con nombres de los equipos.
- Pizarrón o panel visual con tres zonas:
  - “Lo que sí es un buen asistente”
  - “Lo que no hace”
  - “Lo que probaremos hoy”.
- Bloc de notas y lápiz para cada participante.
- Botella de agua, si el espacio no ofrece servicio.
- Snacks simples, si el horario lo permite.

## B. Materiales digitales

- Presentación principal en formato `.pptx` o `.pdf`.
- Formulario de registro:
  - Nombre.
  - Startup.
  - Etapa.
  - Desafío principal.
  - Nivel técnico.
- Formulario de feedback final.
- Plantilla de definición del caso de uso.
- Plantilla de instrucciones del asistente.
- Plantilla de prompts y pruebas.
- Carpeta compartida con:
  - Links de herramientas.
  - Guías rápidas.
  - Templates.
  - Grabación o material de apoyo.
- Un documento de “reglas para construir el asistente”.
- Un tablero compartido o lienzo en una herramienta colaborativa, si los participantes tienen dispositivos.

## C. Herramientas para el taller

La lista exacta debe confirmarse antes del evento, pero conviene preparar una o más de estas opciones:

- **Para crear el asistente:**
  - ChatGPT con GPT Builder o equivalente.
  - Google Gemini, Microsoft Copilot u otra herramienta accesible desde la cuenta de los participantes.
  - Zapier, Make o n8n para automatizaciones simples, si se desea mostrar un flujo.
- **Para documentar y organizar:**
  - Google Docs, Sheets o Miro.
  - Una plantilla imprimida como alternativa.
- **Para presentar:**
  - Proyector, pantalla, adaptador HDMI/USB-C, clicker y sonido.
- **Para gestionar turnos:**
  - Formulario con submissions o una app de preguntas como Mentimeter, Slido o equivalente.
- **Para cerrar:**
  - Formulario de salida con link投影ado y QR visible.

## D. Preparación logística

- Reservar 20–30 seatscomfortables.
- Preparar 6 a 8 mesas o grupos de 3–5 personas.
- Verificar que la herramienta de IA esté disponible antes del evento y que los participantes puedan crear cuentas.
- Preparar una cuenta demo con:
  - Un asistente funcionando.
  - Un caso de negocio completo.
  - Un ejemplo de respuesta incorrecta.
  - Un ejemplo de respuesta con buena guía de uso.
- Enviar un email 24–48 horas antes con:
  - Confirmación de asistencia.
  - Link para crear cuenta.
  - Instrucciones para instalar la herramienta.
  - Una breve encuesta de necesidades.
  - Pedido de llevar un problema real de su startup.

---

# 3. Desarrollo por bloque

## Bloque 1. Bienvenida y encuadre del reto

**Duración:** 15 minutos  
**Tiempo total acumulado:** 00:00–00:15

### Objetivo

- Crear energía y expectativa.
- Aterrizar la promesa: no se trata de aprender teoría, sino de construir un asistente útil para una startup.
- Identificar el nivel y las necesidades de la audiencia.
- Formar equipos equilibrados.

### Dinámica

#### 1. Apertura y promesa — 4 min

- Saludo breve del facilitador.
- Presentación del objetivo del workshop.
- Mostrar el resultado final esperado: un asistente de IA con propósito, instrucciones, respuestas y límites claros.
- Mensaje central:

> “Hoy no vamos a hablar de inteligencia artificial como tecnología. Vamos a usarla como teammate para resolver problemas concretos de negocio.”

#### 2. Quick poll: ¿qué te gustaría delegar a un asistente? — 4 min

Los participantes escriben una respuesta breve:

- “¿Qué tarea te gustaría que un asistente realizara por ti?”
- “¿Qué proceso de tu startup podría estandarizarse?”
- “¿Qué pregunta se repite demasiado en tu equipo?”

Puede hacerse en dos opciones:

- Post-it individual.
- Formulario digital con respuestas anónimas.

El facilitador agrupa 4–5 respuestas en el pizarrón, sin discutirlas a fondo.

#### 3. Formar equipos — 4 min

- Agrupar participantes en equipos de 3–5 personas.
- Cada equipo debe tener al menos un caso de negocio real.
- Asignar roles:
  - **Responsable del negocio:** define el problema.
  - **Investigador:** revisa herramientas y ejemplos.
  - **Constructor:** leading de prompts e instrucciones.
  - **Crítico:** prueba riesgos y respuestas.
  - Si el equipo tiene menos personas, se combinan roles.

#### 4. Compromiso del grupo — 3 min

Cada equipo completa una frase:

> “Durante las próximas 3 horas construiremos un asistente que nos ayudará con ______.”

### Key takeaway

> Un buen asistente de IA comienza con un problema específico, no con una tecnología.

---

## Bloque 2. IA aplicada a startups: qué sí funciona

**Duración:** 25 minutos  
**Tiempo total acumulado:** 00:15–00:40

### Objetivo

- Explicar, en lenguaje simple, cómo puede usarse la IA en una startup.
- Diferenciar un asistente de un chatbot genérico.
- Enseñar a identificar tareas que son buenas candidatas a automatización.
- Mostrar límites, riesgos y criterios básicos de calidad.

### Dinámica

#### 1. Concepto central — 5 min

Explicar la diferencia entre:

- **Chatbot genérico:** responde preguntas generales.
- **Asistente especializado:** conoce el contexto, las reglas, el tono y el objetivo de tu startup.
- **Automatización:** ejecuta una tarea o conecta herramientas.
- **Agente:** planifica y realiza acciones con permisos.

Enfoque práctico:

> “Un asistente útil tiene contexto. Sin contexto, es solo una respuesta bonita.”

#### 2. Mapa de casos de uso — 7 min

Presentar áreas frecuentes:

- **Atención al cliente:** responder preguntas frecuentes con tono de marca.
- **Ventas:** calificar prospectos, preparar discovery, redactar seguimientos.
- **Marketing:** convertir ideas en posts, campañas, emails y contenido.
- **Operaciones:** resumir pedidos, clasificar solicitudes, crear checklists.
- **Producto y feedback:** sintetizar entrevistas, agrupar observaciones, priorizarINSIGHTS.
- **Administración:** redactar proposals, minutas, contratos iniciales o reportes.
- **Conocimiento interno:** responder preguntas sobre procesos, onboarding y políticas.

No presentar esto como una lista para hacer todo. La pregunta guía es:

> “¿Qué tarea repetitiva, costosa o propensa a errores quieres resolver primero?”

#### 3. Actividad: “elige tu caso” — 8 min

Cada participante revisa una matriz de 6 criterios, puntuando de 1 a 5:

1. Frecuencia.
2. Tiempo que consume.
3. Claridad del resultado esperado.
4. Disponibilidad de información o datos.
5. Riesgo relativamente bajo.
6. Impacto en el negocio.

Se recomienda elegir un caso que cumpla:

- Ocurra al menos una vez por semana.
- Tome más de 15–20 minutos.
- Tenga reglas relativamente claras.
- No requiera, por ahora, decisiones legales, médicas o financieras sensibles.

#### 4. Límites y riesgos — 5 min

Explicar brevemente:

- La IA puede inventar información.
- Puede perder el contexto.
- Puede sonar genérica.
- Puede sesgar respuestas.
- Puede exponer datos sensibles.
- No sustituye la validación con clientes ni la revisión humana.

Regla de oro:

> “La IA puede acelerar el trabajo, pero no debe inventar la verdad de tu negocio.”

### Key takeaway

> Empieza por una tarea frecuente, medible y de bajo riesgo; define primero qué significa una buena respuesta.

---

## Bloque 3. Demo: del problema al asistente

**Duración:** 20 minutos  
**Tiempo total acumulado:** 00:40–01:00

### Objetivo

- Mostrar el proceso completo de construcción de un asistente.
- Hacer visible cada decisión: problema, contexto, instrucciones, herramientas, pruebas y límites.
- Mostrar tanto un resultado exitoso como un error y cómo se corrige.

### Dinámica

#### 1. Demo en vivo: caso de negocio — 14 min

Ejemplo recomendado:

**Asistente de pre-venta para una startup B2B de software.**

Proceso:

1. **Definir el objetivo**
   - “Calificar leads entrantes y preparar una respuesta personalizada.”

2. **Dar contexto**
   - Startup, producto, cliente ideal, objeciones frecuentes y proceso comercial.

3. **Establecer instrucciones**
   - Rol.
   - Tareas permitidas.
   - Tono.
   - Preguntas que debe hacer.
   - Reglas de escalamiento.
   - Límites.

4. **Agregar herramientas o fuentes, si aplica**
   - FAQ.
   - Información de producto.
   - Calendario.
   - CRM.
   - Formulario de lead.

5. **Probar en vivo**
   - Pregunta típica.
   - Pregunta ambigua.
   - Pregunta fuera de alcance.
   - Lead que amerita escalamiento.

6. **Corregir**
   - Reescribir instrucciones.
   - Agregar reglas.
   - Ajustar tono.
   - Redactar mejor el prompt.

#### 2. Mini-test: “¿esto es un buen asistente?” — 4 min

Mostrar una respuesta generada con Contexto insuficiente y preguntar:

- “¿Sabría un cliente qué hacer con esta respuesta?”
- “¿Suena como nuestra startup?”
- “¿Dice claramente qué hacer si no sabe?”
- “¿Podría causar un error comercial?”
- “¿La persona sabe cuándo tomar el control?”

#### 3. Recap de la demo — 2 min

Mostrar el esquema:

> **Problema → Contexto → Instrucciones → Herramientas → Pruebas → Mejora**

### Key takeaway

> La calidad de un asistente depende menos de “magic prompts” y más de la claridad del contexto, las instrucciones y los casos de prueba.

---

## Bloque 4. Descanso activo y reset

**Duración:** 10 minutos  
**Tiempo total acumulado:** 01:00–01:10

### Objetivo

- Recuperar atención.
- Permitir que los participantes discutan casos de uso sin entrar en construcción.
- Generar nuevas ideas antes del ejercicio principal.

### Dinámica

- Música o audio guiado durante la pausa.
- En una tarjeta opcional: “El problema que más me gustaría resolver con IA”.
- Si hay tiempo, dos participantes comparten su caso en 30 segundos.
- El facilitador anota 3 casosoul湧 como candidatos para la demo final.

### Key takeaway

> La mejor idea de asistente suele surgir de una frustration concreta y repetida del negocio.

---

## Bloque 5. Diseño del caso de uso

**Duración:** 20 minutos  
**Tiempo total acumulado:** 01:10–01:30

### Objetivo

- Convertir una idea amplia en un caso de uso específico y construible.
- Definir qué puede hacer el asistente y qué no.
- Preparar la base para construir el MVP.

### Dinámica

#### 1. Lección relámpago: “Anatomía de un buen caso” — 4 min

Presentar cinco preguntas:

1. **¿A quién ayuda?**
2. **¿En qué momento o canal?**
3. **¿Qué tarea concreta realiza?**
4. **¿Qué entradas recibe?**
5. **¿Qué salida útil produce?**

Ejemplo:

- “Ayuda a un vendedor que recibe un lead desde Instagram, durante la fase de discovery, para calificar necesidad, presupuesto y timeframe, y devolver una conversación breve con próximos pasos.”

#### 2. Ejercicio en equipo:填写 Canvas del caso — 12 min

Cada equipo completa un lienzo con las siguientes secciones:

**A. Situación actual**

- ¿Quién realiza la tarea hoy?
- ¿Con qué frecuencia?
- ¿Cuánto tiempo toma?
- ¿Dónde se produce el error?

**B. Resultado esperado**

- ¿Qué debería hacer el asistente?
- ¿Qué artefacto produce?
- ¿Cómo sabremos que funciona?

**C. Contexto necesario**

- Información del producto.
- Datos del cliente.
- Tone of voice.
- FAQs.
- Proceso interno.
- Excepciones.

**D. Límites**

- Lo que no debe hacer.
- Información que no debe inventar.
- Casos que debe escalar.
- Acciones que requieren aprobación humana.

**E. Primera versión**

- Una sola función principal.
- Un solo canal.
- Un solo tipo de usuario.
- Una sola integración, si es indispensable.

#### 3. Peer check en 2 minutos — 4 min

Los equipos intercambian su canvas con otro equipo. El equipo revisor comprueba:

- ¿El caso es específico?
- ¿Se entiende quién lo usará?
- ¿La salida está clara?
- ¿Los límites son realistas?
- ¿Es posible construirlo en 30 minutos?

### Key takeaway

> Un MVP de asistente no es una versión pequeña de un producto completo: es una promesa pequeña, clara y verificable.

---

## Bloque 6. Construcción del MVP sin código

**Duración:** 30 minutos  
**Tiempo total acumulado:** 01:30–02:00

### Objetivo

- Construir un asistente funcional o, como mínimo, un prototipo sólido y listo para probar.
- Practicar la definición de instrucciones, contexto, tono y límites.
- Experimentar directamente con la herramienta sin depender de habilidades técnicas.

### Dinámica

#### 1. Setup técnico — 3 min

El facilitador muestra:

- Cómo acceder a la herramienta.
- Cómo crear un asistente.
- Dónde pegar instrucciones.
- Dónde agregar contexto o archivos.
- Cómo probarlo.
- Cómo compartirlo con el equipo.

Incluir un plan B:

- Si la herramienta no funciona para alguien, el equipo usa una plantilla de prompt y simula el flujo en un documento compartido.
- Al final, todos deben tener al menos un prototipo funcional o una instrucción lista para implementar.

#### 2. Construcción individual del prompt maestro — 8 min

Cada participante redacta su prompt siguiendo esta estructura:

```text
ROL
Eres el asistente de [startup] para [usuario].

OBJETIVO
Tu trabajo principal es [tarea específica].

CONTEXTO
- Negocio:
- Producto:
- Usuario:
- Momento del proceso:
- Información disponible:

TAREAS
1.
2.
3.

TONO
- 
- 
- 

REGLAS
- Si no sabes algo, pregunta o indica que no tienes esa información.
- No prometas [límite].
- No inventes datos.
- Si el caso supera estas instrucciones, deriva a [persona/proceso].

FORMATO DE SALIDA
- ...
- ...

CASOS LÍMITE
- ...
- ...
```

#### 3. Agregar contexto — 6 min

Cada equipo pega o adjunta:

- Descripción de la startup.
- FAQ.
- Tone of voice.
- Ejemplo de una buena respuesta.
- Ejemplo de una mala respuesta.
- Procedimiento o checklist.

#### 4. Configurar herramientas o canal — 5 min

Opciones:

- Publicar una página de chat.
- Conectar una base de conocimiento.
- Agregar un formulario.
- Conectar un calendario.
- Exportar instrucciones a una herramienta low-code.

Debe遴arse a una sola función adicional para no convertir el ejercicio en una implementación compleja.

#### 5. Primera prueba rápida — 4 min

Cada equipo hace tres pruebas:

1. Una pregunta normal.
2. Una pregunta ambigua.
3. Una pregunta fuera de alcance.

#### 6. Micro-feedback entre pares — 4 min

Otro equipo responde:

- “¿La respuesta te sirve?”
- “¿Suena como la startup?”
- “¿Entendiste qué hacer?”
- “¿Qué mejorarías primero?”

### Key takeaway

> No necesitas saber programar; necesitas saber definir el trabajo, darle contexto y establecer límites claros.

---

## Bloque 7. Pausa

**Duración:** 10 minutos  
**Tiempo total acumulado:** 02:00–02:10

### Objetivo

- Dar descanso antes de la ronda final de pruebas.
- Permitir que los equipos revisen y ajusten su prototipo.
- Compartir preguntas técnicas breves.

### Dinámica

- Descanso.
- Se permite seguir trabajando en el prototipo.
- El facilitador circula por las mesas paraResolver bloqueos.
- Se pueden llevar preguntas al pizarrón, pero no dar una charla técnica extensa.

### Key takeaway

> Antes de compartir, conviene preguntar: “¿Qué haría que esto funcione mejor en mi operación real?”

---

## Bloque 8. Prueba, feedback y mejora

**Duración:** 25 minutos  
**Tiempo total acumulado:** 02:10–02:35

### Objetivo

- Evaluar el prototipo con criterios claros.
- Identificar mejoras de alto impacto.
- Practicar feedback短时间内 y constructivo.
- Dejar cada asistente listo para un siguiente paso real.

### Dinámica

#### 1. Presentaciones relámpago — 12 min

- 2 minutos por equipo como máximo.
- Formato:
  1. Nombre del asistente.
  2. Problema que resuelve.
  3. Demostración en vivo de una interacción.
  4. Una aprendizaje o limitation.
- Si hay más equipos, dividir en dos grupos:
  - 4 minutos por grupo.
  - Otros equipos observan ySsending feedback en notas.

#### 2. Rúbrica de evaluación — 8 min

Cada equipo evalúa al equipo expositor de 1 a 5 en cuatro categorías:

| Criterio | Pregunta |
|---|---|
| Utilidad | ¿Resuelve un problema real? |
| Claridad | ¿Se entiende la tarea y la salida? |
| Calidad | ¿Las respuestas son útiles y consistentes? |
| Control | ¿Tiene límites y sabe cuándo escalar? |

Pregunta final:

> “Si este asistente llegara mañana a nuestro equipo, ¿lo usaríamos o no? ¿Por qué?”

#### 3. Iteración final — 5 min

Cada equipo aplica al menos un cambio:

- Agregar una FAQ.
- Aclarar el formato de salida.
- Definir una regla.
- Cambiar el tono.
- Quitar una tarea.
- Agregar un caso límite.
- Mejorar la respuesta de escalamiento.

### Key takeaway

> Un prototipo no necesita ser perfecto; necesita resolver algo real y demostrar con claridad su valor y sus límites.

---

## Bloque 9. Qué hacer después en tu startup

**Duración:** 15 minutos  
**Tiempo total acumulado:** 02:35–02:50

### Objetivo

- Mostrar cómo convertir el prototipo en una herramienta adoptable.
- Definir un plan de validación y despliegue de bajo riesgo.
- Introducir métricas, gobernanza y mejora continua.

### Dinámica

#### 1. Del prototipo al sistema útil — 5 min

Explicar el camino:

1. Validar con casos reales.
2. Recopilar feedback.
3. Integrar una herramienta o fuente.
4. Definir responsable humano.
5. Medir resultados.
6. Iterar semanal o quincenalmente.

#### 2. Matriz de priorización — 4 min

Mostrar cuatro fases:

- **Asistente:** una tarea, un canal, un usuario.
- **Copiloto:** aparece dentro de una herramienta existente.
- **Automatización:** conecta sistemas y ejecuta procesos.
- **Agente:** planifica acciones, con permisos y supervisión.

Recomendación para una startup early-stage:

> “No salten al agente. PrimeroRegression bien un asistente simple y medible.”

#### 3. Mini-plan de 7 días — 4 min

Cada participante completa:

- **Día 1:** definir el caso y sus límites.
- **Día 2:** preparar contexto y FAQ.
- **Día 3:** construir la primera versión.
- **Día 4:** probarla con 5 casos reales.
- **Día 5:** pedir feedback a 2–3 personas.
- **Día 6:** corregir los tres problemas principales.
- **Día 7:** publicarla en un canal limitado y definir una métrica.

#### 4. Métricas mínimas — 2 min

Elegir una o dos:

- Tiempo promedio por tarea.
- % de respuestas aprobadas sin edición.
- Tiempo de respuesta.
- Tasa de finalización.
- Satisfacción del usuario.
- Número de escalamientos.
- Errores críticos detectados.

### Key takeaway

> El éxito no es “tener IA”, sino reducir tiempo,提升 calidad o mejorar una experiencia de forma medible.

---

## Bloque 10. Cierre, snapshots y próximos pasos

**Duración:** 10 minutos  
**Tiempo total acumulado:** 02:50–03:00

### Objetivo

- Cerrar con energía y claridad.
- Consolidar los aprendizajes.
- Crear compromiso de acción.
- Abrir espacio para networking y preguntas finales.

### Dinámica

#### 1. Round-up: tres aprendizajes — 3 min

Cada participante escribe:

1. Una cosa que va a implementar.
2. Un riesgo que va a cuidar.
3. Una persona o herramienta con la que quiere seguir.

#### 2. Snapshot final — 2 min

El facilitador pide a cada equipo una frase:

> “Nuestro asistente se llama ___ y，帮助á a ___ a ___.”

Opcionalmente se toma una foto grupal con la pantalla donde se ven los asistentes.

#### 3. Compromiso de 7 días — 2 min

Los participantes calendarizan una tarea concreta:

- “Voy a probarlo con cinco casos antes del [fecha].”
- “Voy a pedir feedback a un teammate.”
- “Voy a definir quién será responsable de revisarlo.”

#### 4. Feedback final — 2 min

Formulario con 4–6 preguntas:

- ¿Qué fue más útil?
- ¿Qué也应该 cambiar?
- ¿Qué aprendiste?
- ¿Qué te falta para usarlo mañana?
- Calificación de 1 a 5.
- ¿Recomendarías este workshop?

#### 5. Cierre — 1 min

Mensaje final:

> “No están solo usando IA. Están diseñando cómo su startup puede trabajar mejor.”

### Key takeaway

> Un workshop termina cuando el asistente deja de ser un ejercicio y empieza a convertirse en un hábito de trabajo.

---

# 4. Ejercicio principal del workshop

## **“Construye tu copiloto de startup en 30 minutos”**

### Propósito

Que cada equipo construya un asistente de IA funcional para resolver una tarea concreta de una startup early-stage. No se busca crear un sistema complejo; se busca producir algo que pueda probarse con usuarios reales.

### Duración total

**50–55 minutos**, contando:

- 20 minutos de diseño.
- 30 minutos de construcción.
- 5–10 minutos de prueba y feedback durante el bloque final.

### Formato

Equipos de 3–5 personas. Cada equipo elige un caso entre:

1. **Asistente de pre-venta**
   - Califica prospectos.
   - Detecta objeciones.
   - Propone próximos pasos.

2. **Asistente de onboarding de clientes**
   - Explica el producto.
   - Responde preguntas frecuentes.
   - Entrega un checklist inicial.

3. **Asistente de feedback de usuarios**
   - Resume entrevistas.
   - Clasifica temas.
   - Detecta patrones y oportunidades.

4. **Asistente de contenido de marketing**
   - Convierte una idea en múltiples formatos.
   - Adapta el mensaje por segmento.
   - Mantiene la voz de la marca.

5. **Asistente de soporte de primer nivel**
   - Responde FAQs.
   - Clasifica solicitudes.
   - Escala casos complejos.

6. **Asistente de operaciones internas**
   - Convierte pedidos o solicitudes en tareas.
   - Revisa checklists.
   - Detecta información faltante.

7. **Asistente de preparation de reuniones**
   - Prepara agendas.
   - Resume contexto.
   - Genera preguntas de discovery.

8. **Asistente de proposals y cotizaciones**
   - Transforma información en un primer borrador.
   - Hace preguntas de control.
   - Señala campos que requieren aprobación.

### Entregables obligatorios

Cada equipo debe dejar:

1. **Nombre del asistente.**
2. **Usuario principal.**
3. **Una tarea principal.**
4. **Prompt o instrucciones completas.**
5. **Contexto mínimo:**
   - Descripción de la startup.
   - FAQ o datos de producto.
   - Tono de voz.
6. **Tres límites o reglas de seguridad.**
7. **Tres casos de prueba:**
   - Normal.
   - Ambiguo.
   - Fuera de alcance.
8. **Una demo de una interacción.**
9. **Un plan de prueba para los siguientes 7 días.**

### Reglas para mantener el alcance

- Un solo objetivo principal.
- Un solo tipo de usuario.
- Un solo canal.
- Máximo una integración.
- Si una feature no es esencial, se anota como “fase 2”.
- No pasar más de 10 minutos configurando una automatización.

### Criterios de éxito

El ejercicio se considera exitoso si:

- El asistente tiene una tarea clara.
- Un usuario sabe exactamente cuándo usarlo.
- La salida es accionable.
- El asistente reconoce sus límites.
- El equipo puede probarlo con un caso real.
- Al menos un cambio de mejora surge del feedback.

---

# 5. Recursos para llevar a casa

## A. Kit de implementación

### 1. Template: Canvas del asistente

Incluir las secciones:

- Problema.
- Usuario.
- Momento del proceso.
- Tarea.
- Entradas.
- Salida esperada.
- Contexto.
- Tone of voice.
- Reglas.
- Límites.
- Casos de prueba.
- Métrica de éxito.

### 2. Template: Prompt maestro

```text
ROL
Eres [nombre] y ayudas a [usuario] en [startup].

OBJETIVO
[Resultado específico que debe lograr].

CONTEXTO
[Información relevante del negocio, producto y proceso].

TAREAS
- [Tarea 1]
- [Tarea 2]
- [Tarea 3]

TONO
[Estilo, vocabulario y nivel de formalidad].

FORMATO DE SALIDA
[Estructura, longitud y elementos requeridos].

REGLAS
- No inventes datos.
- Si falta información, haz una pregunta.
- Si la solicitud está fuera de alcance, explica por qué y deriva.
- [Reglas específicas del negocio].

CASOS LÍMITE
- [Situación y respuesta esperada].
```

### 3. Checklist de contexto

- Descripción de la startup en 100 palabras.
- Lista de clientes objetivo.
- FAQ de 10 preguntas.
- Tono de voz con 5 atributos.
- 3 ejemplos de respuestas buenas.
- 3 ejemplos de respuestas malas.
- Procedimiento actual paso a paso.
- Excepciones conocidas.
- Datos que nunca deben compartirse con la IA.

### 4. Banco de 30 casos de prueba

Casos sugeridos:

- Pregunta directa.
- Pregunta ambigua.
- Solicitud fuera de alcance.
- Información faltante.
- Cliente enojado.
- Cliente confundido.
- Lead no qualificado.
- Lead listo para comprar.
- Feedback positivo.
- Feedback negativo.
- Feedback contradictorio.
- Petición de una automatización no permitida.
- Petición de una garantía inexistente.
- Petición de diagnóstico financiero o legal.

Cada caso debe evaluarse con:

- Utilidad.
- Exactitud.
- Tono.
- Claridad.
- Escalamiento correcto.

### 5. Plan de 30 días

**Semana 1: MVP**

- Definir caso.
- Preparar contexto.
- Construir y probar manualmente.

**Semana 2: Validación**

- Probar con 5–10 casos reales.
- Medir tiempo y calidad.
- Recoger feedback.

**Semana 3: Iteración**

- Corregir errores frecuentes.
- Agregar Integración sencilla.
- Definir un responsable humano.

**Semana 4: Uso limitado**

- Liberar a un grupo pequeño.
- Establecer métricas.
- Revisar qué tareas no debe hacer.

### 6. Kit de seguridad y gobernanza

Checklist mínimo:

- Revisar datos antes de pegarlos en la IA.
- Evitar información sensible, personal o confidencial.
- No usar respuestas de la IA como aprobación final.
- Definir quién monitorea el asistente.
- Registrar problemas y correcciones.
- Revisar Instructions periódicamente.
- Mantener un canal de escalamiento humano.
- Revisar afirmaciones comerciales, legales y de precio.

### 7. Biblioteca de lecturas y herramientas

Seleccionar pocos recursos, relevantes y维持 actualizados:

- Documentación oficial de ChatGPT.
- Documentación oficial de Gemini.
- Documentación oficial de Copilot.
- Zapier, Make o n8n para automatizaciones.
- Miro o Google Docs como espacio de diseño.
- CRM usado por la startup para conectar la herramienta.
- Una guía de prompts para negocio.
- Una plantilla de evaluación de respuestas.
- Una lista de verificaciones de privacidad.

### 8. Videos de seguimiento sugeridos

- Cómo construir una base de conocimiento.
- Cómo diseñar instrucciones paso a paso.
- Cómo conectar un formulario.
- Cómo conectar un CRM.
- Cómo evaluar un asistente de IA.
- Cómo diseñar un proceso con revisión humana.

---

# 6. Slide count estimado por sección

| Sección | Slides estimados | Contenido visual sugerido |
|---|---:|---|
| Portada y objetivos | 2–3 | Título, promesa, resultado final |
| Bienvenida y dinámica | 2 | Agenda, pregunta inicial, instrucción de equipos |
| IA aplicada a startups | 5–6 | Casos de uso, matriz de priorización, riesgos |
| Demo en vivo | 3–4 | Antes/después, prompt, proceso, ejemplo de error |
| Descanso | 1 | Mensaje breve y temporizador |
| Diseño del caso de uso | 3–4 | Canvas, preguntas clave, ejemplo |
| Construcción del MVP | 4–5 | Prompt maestro, contexto, herramientas, checklist |
| Pausa | 1 | Temporizador |
| Pruebas y feedback | 3 | Rúbrica, formato de presentación, preguntas |
| Qué hacer después | 3–4 | Roadmap, plan de 7 días, métricas |
| Cierre | 2–3 | Compromiso, feedback, cierre |
| **Total estimado** | **27–34 slides** | **Promedio: 30–32 slides** |

## Recomendación de diseño de presentación

- 1 idea principal por slide.
- Poco texto y frases breves.
- Capturas reales de la herramienta.
- Diagramas simples: “problema → asistente → resultado”.
- La demo debe estar preparada con ventanas, cuentas y archivos abiertos.
- Los templates y herramientas deben estar disponibles como recursos descargables, no solo explicados oralmente.

---

# 7. Checklist final del facilitador

## Antes del evento

- [ ] Confirmar lista y registrar la asistencia.
- [ ] Enviar instrucciones y link de acceso 24–48 horas antes.
- [ ] Verificar cuentas, tool licenses y Espacio de trabajo.
- [ ] Preparar el caso demo funcional.
- [ ] Probar projector, sonido, timer, Wi-Fi y adaptador.
- [ ] Imprimir templates y tarjetas de trabajo.
- [ ] Preparar un plan B si falla la herramienta.
- [ ] Definir los horarios de pausa y cierre.
- [ ] Preparar formulario de feedback y carpeta de recursos.

## Durante el evento

- [ ] Mantener cada explicación técnica por debajo de 10 minutos.
- [ ] Circular entre mesas y detectar bloqueos.
- [ ] Tomar notas de buenos casos para compartir.
- [ ] Mostrar el tiempo restante al menos en bloques de 30 y 10 minutos.
- [ ] Guardar los mejores prompts y ejemplos para el cierre.
- [ ] Corregir cualquier producto层面的 promise unrealistic.
- [ ] Ensure de que cada equipo tenga un entregable.

## Después del evento

- [ ] Enviar recursos y templates en menos de 24 horas.
- [ ] Compartir acceso a las demos o prototipos.
- [ ] Enviar formulario de seguimiento.
- [ ] Recopilar respuestas sobre el plan de 7 días.
- [ ] Realizar una revisión de aprendizaje en 2–3 semanas.
- [ ] Crear un espacio opcional para compartir iteraciones y resultados.