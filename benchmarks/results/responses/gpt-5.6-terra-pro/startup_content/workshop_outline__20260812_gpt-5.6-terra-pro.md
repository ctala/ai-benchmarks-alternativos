# GPT-5.6 Terra Pro — startup_content/workshop_outline

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 7.88 | quality: 9.72
- latency_total: 79.591s | tokens_per_second: 223.2
- input_tokens: 19155 | output_tokens: 17768
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

# Workshop presencial (3 horas)
# **“Construye tu Asistente de IA para tu Startup – Workshop Práctico”**

**Audiencia:** Emprendedores early-stage no técnicos  
**Tamaño ideal:** 20–30 personas  
**Formato:** Presencial, altamente práctico, trabajo individual + pares  
**Resultado prometido:** Cada participante sale con un primer asistente de IA funcional para una necesidad concreta de su startup, un prompt reutilizable, una base de conocimiento inicial y un plan de prueba de 7 días.

---

## 1. Objetivos del workshop

Al finalizar las 3 horas, cada participante podrá:

1. Identificar una tarea repetitiva y de alto valor que puede delegar parcialmente a IA.
2. Diseñar el rol, contexto, reglas y formato de respuesta de un asistente.
3. Construir un asistente funcional usando una herramienta no-code de IA generativa.
4. Probarlo con casos reales, detectar fallas y mejorarlo.
5. Llevarse un plan simple para implementarlo en su operación durante la siguiente semana.

> **Principio del workshop:** No vamos a “aprender IA”. Vamos a construir algo útil para que tu startup avance más rápido esta semana.

---

# 2. Agenda detallada — 180 minutos

| Hora / Minuto | Bloque | Duración | Formato |
|---|---:|---:|---|
| 00:00–00:10 | Bienvenida, contexto y reglas del juego | 10 min | Charla + activación |
| 00:10–00:25 | Qué es (y qué no es) un asistente de IA | 15 min | Charla + demo |
| 00:25–00:40 | Detecta la mejor oportunidad para automatizar | 15 min | Ejercicio individual |
| 00:40–00:55 | Anatomía de un buen asistente: el framework R.O.L.E. | 15 min | Charla + mini ejercicio |
| 00:55–01:15 | Demo en vivo: de cero a asistente funcional | 20 min | Demo guiada |
| 01:15–01:25 | Pausa / café / networking | 10 min | Break |
| 01:25–02:10 | Ejercicio principal: construye tu asistente | 45 min | Trabajo individual + facilitación |
| 02:10–02:35 | Prueba, rompe y mejora tu asistente | 25 min | Trabajo en parejas |
| 02:35–02:55 | Demo relay: comparte, recibe feedback y mejora | 20 min | Presentaciones rápidas |
| 02:55–03:00 | Cierre: plan de acción de 7 días | 5 min | Compromiso individual |

**Total: 180 minutos**

---

# 3. Materiales y preparación previa

## Para los participantes

Solicitar por correo o WhatsApp antes del evento:

- Laptop cargada y cargador.
- Acceso activo a una herramienta de IA generativa:
  - ChatGPT, Claude, Gemini, Copilot u otra alternativa disponible.
- Cuenta creada e inicio de sesión validado antes de llegar.
- Información básica de su startup:
  - Qué vende.
  - A quién le vende.
  - Problemas que resuelve.
  - Preguntas frecuentes de clientes.
  - Ejemplos de mensajes de ventas, soporte, propuestas o contenido.
- Idealmente: traer 3 a 5 documentos o textos reales que puedan usar como insumo:
  - Pitch deck.
  - Landing page.
  - FAQ.
  - Catálogo.
  - Mensajes de WhatsApp frecuentes.
  - Propuesta comercial.
  - Manual operativo.
  - Notas de entrevistas a clientes.

> **Regla importante:** No cargar información confidencial, datos personales de clientes, contraseñas, datos financieros sensibles ni información legal privada en herramientas públicas de IA.

---

## Para el facilitador

### Equipo y logística

- Proyector o pantalla grande.
- Audio y micrófono si la sala lo requiere.
- Wi-Fi robusto para 30 personas conectadas.
- Regleta eléctrica o estaciones de carga.
- Pizarra, rotafolios o Miro/FigJam proyectado.
- Post-its de 2 colores.
- Marcadores.
- Cronómetro visible.
- Mesas organizadas para trabajo en grupos de 3 a 5 personas.
- QR code visible con:
  - Plantilla de prompt.
  - Workbook del ejercicio.
  - Recursos post-workshop.
  - Encuesta de salida.

### Archivos que deben estar listos

1. **Plantilla “Diseña tu Asistente de IA”.**
2. **Banco de casos de uso para startups.**
3. **Prompt maestro editable.**
4. **Checklist de pruebas del asistente.**
5. **Guía de privacidad y uso responsable.**
6. **Plan de implementación de 7 días.**
7. Ejemplos preparados de asistentes para demo:
   - Asistente de ventas.
   - Asistente de soporte.
   - Asistente de contenido.
   - Asistente de research de clientes.
   - Asistente operativo.

### Preparación técnica recomendada

Antes del workshop, el facilitador debe:

- Probar el Wi-Fi con varias conexiones.
- Tener un hotspot móvil de respaldo.
- Preparar una demo funcional en al menos dos plataformas, por si una falla.
- Tener capturas de pantalla o video corto de respaldo de la demo.
- Abrir previamente todos los links y documentos.
- Preparar un ejemplo “malo” y uno “bueno” de prompt para comparar.

---

# 4. Outline detallado por bloque

---

## Bloque 1. Bienvenida, contexto y reglas del juego

**Duración:** 10 minutos  
**Dinámica:** Charla breve + activación de sala  
**Slide count estimado:** 3 slides

### Objetivo

Crear energía, alinear expectativas y dejar claro que el resultado será práctico: un asistente construido, no solo ideas sobre IA.

### Contenido

- Bienvenida y presentación breve del facilitador.
- Pregunta de activación:
  - “¿Qué tarea repites todas las semanas y te gustaría no hacer nunca más?”
- Levantamiento de manos:
  - Ventas.
  - Marketing.
  - Atención al cliente.
  - Operaciones.
  - Research.
  - Administración.
- Reglas del workshop:
  1. Construir antes que debatir.
  2. Trabajar con problemas reales.
  3. Compartir sin juzgar.
  4. La IA propone; tú decides.
  5. No ingresar información sensible.

### Key takeaway

> La mejor IA para una startup no es la más sofisticada: es la que elimina fricción en un proceso real de tu día a día.

---

## Bloque 2. Qué es (y qué no es) un asistente de IA

**Duración:** 15 minutos  
**Dinámica:** Charla + demo breve  
**Slide count estimado:** 5 slides

### Objetivo

Desmitificar la IA y mostrar que un asistente no requiere programación, APIs ni un equipo técnico para comenzar.

### Contenido

### Qué es un asistente de IA

Un asistente es una configuración clara que combina:

- Un **rol**: quién es.
- Un **objetivo**: qué resultado debe ayudar a producir.
- Un **contexto**: información sobre la startup, cliente y producto.
- Unas **reglas**: qué puede y qué no puede hacer.
- Un **formato de salida**: cómo debe responder.
- Una **base de conocimiento**: documentos, FAQs, ejemplos y materiales.
- Un proceso de **prueba y mejora**.

### Qué no es

- No es un reemplazo completo de un fundador.
- No es una respuesta mágica sin contexto.
- No siempre tiene razón.
- No debe tomar decisiones sensibles sin revisión humana.
- No necesita ser perfecto para generar valor desde el día uno.

### Casos de uso concretos para startups early-stage

- Convertir notas de llamadas en CRM y próximos pasos.
- Responder preguntas frecuentes de potenciales clientes.
- Preparar borradores de mensajes de ventas por WhatsApp o email.
- Crear contenido para LinkedIn, Instagram o newsletters.
- Transformar entrevistas de clientes en insights.
- Preparar propuestas comerciales.
- Estandarizar onboarding de clientes.
- Crear borradores de SOPs o procesos internos.
- Preparar briefs para freelancers o agencias.
- Analizar feedback de clientes y detectar patrones.

### Mini demo

Mostrar una tarea común:

**Input:** “Estas son mis notas de una llamada con un prospecto.”  
**Output:** Resumen, pains, objeciones, siguiente paso y mensaje de follow-up.

Mostrar la diferencia entre:

- Prompt vago: “Haz un email de seguimiento.”
- Prompt estructurado: “Actúa como asistente de ventas de [Startup]…”

### Key takeaway

> Un asistente de IA útil no depende de una herramienta “mágica”; depende de instrucciones claras y contexto real.

---

## Bloque 3. Detecta la mejor oportunidad para automatizar

**Duración:** 15 minutos  
**Dinámica:** Ejercicio individual + discusión breve en mesa  
**Slide count estimado:** 4 slides

### Objetivo

Ayudar a cada participante a elegir una tarea específica y alcanzable para su primer asistente.

### Instrucciones del ejercicio: “Mapa de fricción”

Cada participante lista entre 5 y 10 tareas repetitivas que realiza semanalmente.

Luego evalúa cada una con una matriz simple de 1 a 5:

| Criterio | Pregunta |
|---|---|
| Frecuencia | ¿Cuántas veces ocurre por semana? |
| Tiempo | ¿Cuánto tiempo me consume? |
| Repetición | ¿Sigue pasos similares cada vez? |
| Impacto | ¿Afecta ventas, clientes, velocidad o calidad? |
| Riesgo | ¿Puedo revisar la respuesta antes de usarla? |

### Fórmula de priorización

Seleccionar una tarea con:

- Alta frecuencia.
- Alta repetición.
- Impacto claro.
- Riesgo bajo o medio.
- Posibilidad de revisión humana.

### Ejemplos de buenas primeras tareas

- “Convertir notas de reuniones en un resumen comercial.”
- “Crear mensajes de seguimiento después de una demo.”
- “Responder FAQs de mi producto.”
- “Generar 10 variaciones de anuncios para una campaña.”
- “Transformar entrevistas de clientes en problemas y oportunidades.”
- “Preparar una propuesta comercial basada en un brief.”

### Ejemplos de malas primeras tareas

- “Construir mi estrategia completa de negocio.”
- “Manejar todo mi soporte sin revisión.”
- “Decidir a quién contratar.”
- “Dar asesoría legal, médica o financiera.”
- “Crear un producto completo sin validación.”

### Key takeaway

> Empieza por una tarea pequeña, frecuente y medible. Un asistente que ahorra 30 minutos diarios vale más que una idea gigante que nunca se implementa.

---

## Bloque 4. Anatomía de un buen asistente: Framework R.O.L.E.

**Duración:** 15 minutos  
**Dinámica:** Charla + mini ejercicio de redacción  
**Slide count estimado:** 6 slides

### Objetivo

Dar una estructura fácil de recordar para diseñar asistentes útiles sin requerir conocimientos técnicos.

## Framework R.O.L.E.

### R — Rol

¿Quién es el asistente?

Ejemplos:

- Asistente de ventas B2B.
- Asistente de soporte al cliente.
- Asistente de investigación de mercado.
- Asistente de contenido para founders.
- Asistente de operaciones.

### O — Objetivo

¿Qué resultado debe generar?

Ejemplos:

- Preparar un mensaje de seguimiento claro y personalizado.
- Resumir entrevistas e identificar patrones.
- Crear respuestas consistentes a preguntas de clientes.
- Convertir una idea en un brief de contenido.

### L — Límites

¿Qué debe evitar? ¿Cuándo debe pedir más información? ¿Cuándo debe escalar a una persona?

Ejemplos:

- No inventar precios, políticas o características del producto.
- Si no tiene información suficiente, hacer hasta 3 preguntas antes de responder.
- No usar promesas absolutas.
- No dar asesoría legal, médica o financiera.
- Responder en español latinoamericano claro y cercano.

### E — Entrega

¿Cómo debe devolver el resultado?

Ejemplos:

- Tabla con columnas específicas.
- Mensaje de WhatsApp de máximo 500 caracteres.
- Email con asunto, cuerpo y CTA.
- Resumen en bullets: dolor, objeción, siguiente paso.
- Tres opciones con distintos tonos.

### Mini ejercicio

Cada persona completa esta frase:

> “Estoy construyendo un asistente que actúa como ________, para ayudarme a ________, sin ________, y entregando el resultado en formato ________.”

### Key takeaway

> Si no puedes explicar claramente el rol, objetivo, límites y entrega de tu asistente, la IA tampoco podrá ejecutarlo bien.

---

## Bloque 5. Demo en vivo: de cero a asistente funcional

**Duración:** 20 minutos  
**Dinámica:** Demo guiada  
**Slide count estimado:** 4 slides + herramienta en vivo

### Objetivo

Mostrar el proceso completo antes de que los participantes lo hagan por su cuenta.

### Caso de demo sugerido

**Asistente de Follow-up Comercial para una startup B2B**

El facilitador construye en vivo un asistente que:

1. Recibe notas de una llamada comercial.
2. Identifica dolores, necesidades y objeciones.
3. Sugiere el siguiente paso.
4. Redacta un email de seguimiento.
5. Crea una versión corta para WhatsApp.
6. Señala información faltante o riesgos de seguimiento.

### Prompt de demo

```text
Actúa como un asistente de ventas B2B para [Nombre de Startup].

Tu objetivo es ayudarme a convertir notas de reuniones con prospectos en seguimientos claros, personalizados y orientados a avanzar la venta.

Contexto de la startup:
- Producto/servicio: [describir]
- Cliente ideal: [describir]
- Principal problema que resolvemos: [describir]
- Tono de comunicación: cercano, claro, profesional y sin lenguaje corporativo excesivo.

Cuando reciba notas de una reunión:

1. Resume en máximo 5 bullets:
   - Contexto del prospecto
   - Problemas o necesidades
   - Objeciones o dudas
   - Nivel de interés
   - Próximo paso recomendado

2. Identifica información faltante. Si es importante, haz hasta 3 preguntas antes de crear el mensaje.

3. Redacta:
   - Un email de seguimiento con asunto, cuerpo y CTA.
   - Una versión de WhatsApp de máximo 450 caracteres.

Reglas:
- No inventes precios, funcionalidades, casos de éxito ni compromisos.
- Si una afirmación no aparece en las notas, indícalo como “pendiente de validar”.
- Mantén un tono humano y directo.
- Evita frases genéricas como “espero que estés muy bien”.
```

### Mostrar el ciclo de mejora

1. Primer resultado.
2. Detectar una falla.
3. Añadir una regla o ejemplo.
4. Probar nuevamente.
5. Comparar versión 1 vs. versión 2.

### Key takeaway

> Tu primer prompt no tiene que ser perfecto. La ventaja viene de iterar: probar, observar, ajustar y volver a probar.

---

## Bloque 6. Pausa / café / networking

**Duración:** 10 minutos  
**Dinámica:** Break  
**Slide count estimado:** 1 slide

### Objetivo

Dar descanso y promover intercambio informal entre founders.

### Activación opcional en pantalla

> “Durante la pausa, pregúntale a alguien: ¿qué tarea repetitiva de tu startup te gustaría eliminar primero?”

### Key takeaway

> Los mejores casos de uso suelen aparecer al escuchar cómo otros founders están resolviendo problemas similares.

---

## Bloque 7. Ejercicio principal: Construye tu Asistente de IA

**Duración:** 45 minutos  
**Dinámica:** Trabajo individual + acompañamiento del facilitador y asistentes  
**Slide count estimado:** 5 slides

### Objetivo

Que todos los participantes construyan un asistente funcional para una tarea real de su startup.

---

# 5. Ejercicio principal del workshop

## Nombre del ejercicio

# **“Tu Primer Copiloto de Startup”**

Cada participante construirá un asistente para una tarea específica de ventas, marketing, soporte, investigación u operaciones.

## Resultado mínimo esperado

Al finalizar el ejercicio, cada persona debe tener:

- Un nombre para su asistente.
- Un problema concreto que resuelve.
- Un prompt estructurado con R.O.L.E.
- Al menos un documento, texto o ejemplo como contexto.
- Tres casos de prueba.
- Una versión mejorada del prompt.

---

## Paso a paso del ejercicio

### Paso 1. Elige una tarea (5 min)

Completar:

- La tarea que quiero acelerar es: __________
- Hoy esta tarea me toma: __________
- La hago aproximadamente: __________ veces por semana.
- El resultado ideal debería ser: __________

### Paso 2. Define a tu usuario y contexto (8 min)

Completar:

- Mi startup se llama: __________
- Vendemos: __________
- Nuestro cliente ideal es: __________
- El problema que resolvemos es: __________
- Nuestro tono de comunicación es: __________
- La información que el asistente necesita conocer es: __________

### Paso 3. Diseña con R.O.L.E. (10 min)

Completar la plantilla:

```text
ROL:
Actúa como [rol del asistente].

OBJETIVO:
Tu objetivo es ayudarme a [resultado específico].

CONTEXTO:
Mi startup es [nombre y descripción].
Nuestro cliente ideal es [descripción].
Nuestro producto/servicio ayuda a [resultado].
Nuestra propuesta de valor es [propuesta].
Nuestro tono es [tono].

LÍMITES:
- No inventes información.
- Si falta información importante, pregunta antes de responder.
- No realices [acciones prohibidas].
- Si detectas un tema sensible o de alto riesgo, indícalo claramente.
- Usa lenguaje [estilo de lenguaje].

ENTREGA:
Cuando reciba [tipo de input], responde con:
1. [Formato o sección 1]
2. [Formato o sección 2]
3. [Formato o sección 3]
```

### Paso 4. Agrega contexto real (7 min)

Cada participante incorpora uno o más de estos elementos:

- Texto de su landing page.
- Descripción del producto.
- FAQ.
- Propuesta comercial.
- Ejemplos de mensajes anteriores.
- Notas de llamadas con clientes.
- Testimonios.
- Políticas o condiciones relevantes.

> Recomendación: empezar con información breve y útil. Una página de contexto claro vale más que 50 documentos desordenados.

### Paso 5. Prueba con un caso real (8 min)

Ingresar un caso verdadero o simulado, por ejemplo:

- Un mensaje de cliente.
- Notas de una llamada.
- Un brief de contenido.
- Un problema operativo.
- Una pregunta frecuente.

Evaluar:

- ¿Entendió el contexto?
- ¿El resultado es útil?
- ¿Inventó algo?
- ¿El tono se parece a mi startup?
- ¿El formato me ahorra tiempo?

### Paso 6. Mejora una vez (7 min)

Aplicar al menos una mejora:

- Agregar una regla.
- Incluir un ejemplo de buena respuesta.
- Cambiar el formato de salida.
- Limitar longitud.
- Pedir preguntas de aclaración.
- Añadir una instrucción de tono.
- Explicitar qué no debe inventar.

---

## Rol del facilitador durante el ejercicio

El facilitador y asistentes deben circular por las mesas y hacer preguntas de desbloqueo:

- “¿Qué tarea haces más de dos veces por semana?”
- “¿Cómo sabrás que esta respuesta es buena?”
- “¿Qué información no puede inventar?”
- “¿Qué formato te permitiría usar esto inmediatamente?”
- “¿Qué haría una persona excelente de tu equipo en esta tarea?”
- “¿Qué ejemplo real puedes darle para que entienda mejor?”

### Key takeaway

> Un buen asistente no comienza con tecnología: comienza con una tarea bien definida y una instrucción que refleja cómo trabaja tu startup.

---

## Bloque 8. Prueba, rompe y mejora tu asistente

**Duración:** 25 minutos  
**Dinámica:** Trabajo en parejas + checklist de evaluación  
**Slide count estimado:** 4 slides

### Objetivo

Que los participantes detecten errores, riesgos y oportunidades de mejora antes de usar el asistente en su operación.

### Dinámica: “Red Team de Founders”

Formar parejas. Cada persona prueba el asistente de la otra durante 10 minutos.

La persona que prueba debe intentar “romperlo” usando casos como:

- Un input incompleto.
- Una pregunta ambigua.
- Una solicitud fuera de alcance.
- Un caso con información contradictoria.
- Una pregunta cuya respuesta no está en los documentos.
- Una solicitud con tono inadecuado.
- Un caso donde el asistente podría inventar información.

### Checklist de evaluación

Calificar del 1 al 5:

| Criterio | Pregunta |
|---|---|
| Claridad | ¿La respuesta se entiende rápido? |
| Utilidad | ¿La usaría en mi trabajo real? |
| Precisión | ¿Evita inventar información? |
| Tono | ¿Suena como la startup? |
| Formato | ¿Es fácil de copiar, enviar o ejecutar? |
| Seguridad | ¿Sabe cuándo pedir más contexto o escalar? |

### Mejora obligatoria

Cada participante realiza al menos una modificación a su prompt basándose en el feedback recibido.

### Key takeaway

> No confíes en tu asistente porque “suena inteligente”. Confía después de probarlo con casos reales, ambiguos y difíciles.

---

## Bloque 9. Demo relay: comparte, recibe feedback y mejora

**Duración:** 20 minutos  
**Dinámica:** Presentaciones rápidas + feedback colectivo  
**Slide count estimado:** 3 slides

### Objetivo

Celebrar avances, generar inspiración cruzada y convertir el aprendizaje en ideas aplicables para todos.

### Formato

Seleccionar entre 5 y 6 participantes voluntarios.

Cada participante tiene:

- **2 minutos** para mostrar:
  1. El problema que eligió.
  2. El asistente que construyó.
  3. Un ejemplo de input.
  4. El resultado generado.
  5. Una mejora que hizo después de probarlo.
- **1 minuto** de feedback rápido del grupo o facilitador.

### Framework de feedback

- “Me gustó…”
- “Sería aún más útil si…”
- “Una pregunta que el asistente debería hacer es…”
- “Un límite que podrías agregar es…”

### Categorías que el facilitador puede destacar

- Más útil para ventas.
- Más útil para ahorrar tiempo.
- Mejor uso de contexto.
- Mejor formato de salida.
- Mejor mejora después de feedback.

### Key takeaway

> La IA no elimina la creatividad del fundador: le devuelve tiempo y energía para enfocarse en clientes, producto y decisiones importantes.

---

## Bloque 10. Cierre: plan de acción de 7 días

**Duración:** 5 minutos  
**Dinámica:** Compromiso individual  
**Slide count estimado:** 3 slides

### Objetivo

Evitar que el asistente construido se quede como un experimento de workshop.

### Compromiso final

Cada participante completa:

- Mi asistente será usado para: __________
- Lo probaré con: __________ casos reales.
- La primera persona de mi equipo que lo probará será: __________
- La métrica que revisaré será: __________
- La fecha de revisión será: __________

### Métricas sugeridas

- Minutos ahorrados por tarea.
- Número de respuestas o piezas generadas.
- Tiempo de respuesta a clientes.
- Tasa de uso del equipo.
- Porcentaje de resultados que requieren edición.
- Calidad percibida por el usuario.
- Número de leads o seguimientos realizados.

### Cierre verbal sugerido

> “No necesitas automatizar toda tu empresa esta semana. Necesitas elegir una tarea, usar tu asistente en casos reales y mejorar una cosa a la vez.”

### Key takeaway

> El valor no está en crear el asistente hoy; está en usarlo y mejorarlo durante los próximos 7 días.

---

# 6. Plantilla de prompt para entregar a participantes

```text
NOMBRE DEL ASISTENTE:
[Ejemplo: Copiloto Comercial de Nativa]

ROL:
Actúa como un/a [rol específico] para [nombre de startup].

OBJETIVO:
Ayúdame a [tarea concreta] para lograr [resultado de negocio].

CONTEXTO DE MI STARTUP:
- Startup: [nombre]
- Qué hacemos: [descripción breve]
- Cliente ideal: [descripción]
- Problema que resolvemos: [descripción]
- Diferenciador: [descripción]
- Tono de comunicación: [tono]
- Mercado o país: [país/región si aplica]

INPUT QUE RECIBIRÁS:
Recibirás [notas de reuniones, preguntas de clientes, brief, mensajes, etc.].

INSTRUCCIONES:
1. Primero, identifica [elementos importantes].
2. Si falta información crítica, haz hasta [X] preguntas.
3. Luego, genera [resultado esperado].
4. Prioriza [criterios: claridad, conversión, precisión, velocidad, etc.].
5. Usa un tono [descripción].

LÍMITES:
- No inventes información, precios, políticas, datos o funcionalidades.
- Si no tienes suficiente contexto, indícalo claramente.
- No realices recomendaciones legales, médicas o financieras.
- No compartas ni solicites datos sensibles.
- Si una tarea requiere validación humana, indícalo.

FORMATO DE RESPUESTA:
Entrega la respuesta en este formato:
1. [Sección 1]
2. [Sección 2]
3. [Sección 3]
4. [Siguiente paso recomendado]

EJEMPLO DE BUENA RESPUESTA:
[Agregar un ejemplo real si está disponible]
```

---

# 7. Recursos para llevar a casa

Entregar vía QR, email o carpeta compartida.

## Recursos esenciales

### 1. Workbook del workshop

Incluye:

- Mapa de fricción.
- Matriz de priorización.
- Canvas R.O.L.E.
- Plantilla de prompt.
- Checklist de pruebas.
- Plan de implementación de 7 días.

### 2. Biblioteca de prompts para startups

Prompts listos para adaptar para:

- Seguimiento comercial.
- Mensajes de WhatsApp.
- Emails de prospección.
- Respuestas a FAQs.
- Preparación de propuestas.
- Síntesis de entrevistas con clientes.
- Creación de perfiles de cliente ideal.
- Generación de contenido.
- Briefs para diseño o agencias.
- Minutas y seguimiento de reuniones.
- Documentación de procesos.
- Análisis de feedback de clientes.

### 3. Checklist de calidad antes de usar IA con clientes

- ¿El asistente tiene contexto suficiente?
- ¿Puede estar inventando información?
- ¿Hay una persona revisando antes de enviar?
- ¿El tono representa a la marca?
- ¿Se están usando datos sensibles?
- ¿La respuesta tiene un siguiente paso claro?
- ¿Se está midiendo el tiempo o calidad ahorrada?

### 4. Guía “7 días para implementar tu asistente”

| Día | Acción |
|---|---|
| Día 1 | Elegir una tarea y usar el asistente con 3 casos reales. |
| Día 2 | Anotar errores, dudas y respuestas poco útiles. |
| Día 3 | Agregar reglas, ejemplos y contexto faltante. |
| Día 4 | Pedir a una persona del equipo que lo pruebe. |
| Día 5 | Comparar tiempo y calidad: antes vs. después. |
| Día 6 | Definir un proceso simple para usarlo semanalmente. |
| Día 7 | Decidir: mantener, ajustar, escalar o descartar. |

### 5. Lista de casos de uso por área

**Ventas**
- Follow-ups.
- Preparación de discovery calls.
- Manejo de objeciones.
- Propuestas comerciales.
- Actualización de CRM.

**Marketing**
- Calendario de contenidos.
- Repurpose de contenido.
- Copies para anuncios.
- Newsletter.
- Investigación de competidores.

**Soporte**
- FAQ.
- Clasificación de tickets.
- Respuestas iniciales.
- Resumen de problemas recurrentes.

**Operaciones**
- SOPs.
- Resumen de reuniones.
- Organización de tareas.
- Briefs internos.
- Onboarding.

**Producto y research**
- Síntesis de entrevistas.
- Identificación de pains.
- Priorización de feedback.
- User stories iniciales.
- Hipótesis de validación.

### 6. Guía de uso responsable para founders

- Nunca asumir que una respuesta de IA es correcta sin revisar.
- No cargar datos personales, contratos confidenciales o credenciales.
- Mantener supervisión humana en temas de alto impacto.
- Documentar qué usa el asistente y qué decisiones siguen siendo humanas.
- Comunicar transparencia cuando la IA interactúe directamente con clientes.
- Empezar con borradores y recomendaciones, no con decisiones irreversibles.

---

# 8. Slide count estimado por sección

| Sección | Slides estimados |
|---|---:|
| 1. Bienvenida y activación | 3 |
| 2. Qué es y qué no es un asistente de IA | 5 |
| 3. Detecta la oportunidad | 4 |
| 4. Framework R.O.L.E. | 6 |
| 5. Demo en vivo | 4 |
| 6. Pausa | 1 |
| 7. Ejercicio principal | 5 |
| 8. Prueba y mejora | 4 |
| 9. Demo relay | 3 |
| 10. Cierre y plan de 7 días | 3 |
| **Total estimado** | **38 slides** |

> Recomendación: Mantener las slides visuales y ligeras. El protagonismo debe estar en la herramienta, el workbook y el trabajo de los participantes, no en una presentación extensa.

---

# 9. Recomendaciones de facilitación para una audiencia latinoamericana early-stage

- Usar ejemplos cercanos: WhatsApp, ventas por Instagram, follow-ups, propuestas, cobros, soporte y operación con equipos pequeños.
- Evitar lenguaje excesivamente técnico como “RAG”, “agents”, “APIs” o “LLMs”, salvo que se explique en términos simples.
- Validar que no todos tendrán una suscripción paga: diseñar el ejercicio para funcionar con planes gratuitos.
- Tener participantes con distintos niveles de madurez: algunos tendrán landing page y clientes; otros estarán en etapa de idea. Preparar casos ficticios para quienes aún no tengan materiales.
- Repetir constantemente: “No busques perfección; busca una versión útil.”
- Celebrar los “errores” de la IA como oportunidades para mejorar las instrucciones.
- Usar un temporizador visible para mantener energía y ritmo.
- Contar con al menos 1 asistente de facilitación por cada 10–15 participantes si es posible.

---

# Resultado final esperado

Al terminar el workshop, cada founder se va con:

- Un problema concreto priorizado.
- Un asistente de IA configurado para ese problema.
- Un prompt reutilizable.
- Contexto inicial cargado o documentado.
- Al menos tres pruebas realizadas.
- Feedback de otro emprendedor.
- Una mejora aplicada.
- Un plan de implementación de 7 días.

> **Frase final para cerrar el workshop:**  
> “Tu startup no necesita más herramientas por tenerlas. Necesita sistemas simples que hagan que tú y tu equipo puedan avanzar más rápido.”