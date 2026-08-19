# GPT-5.6 Luna Pro — startup_content/workshop_outline

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 67.357s | tokens_per_second: 311.3
- input_tokens: 22644 | output_tokens: 20967
- judge_score: 5 | justificación: La respuesta es precisa, relevante y profunda, proporcionando una agenda detallada y estructurada que se ajusta perfectamente al contexto del workshop. La claridad y la utilidad práctica son excepcionales, ofreciendo a los emprendedores no técnicos una guía clara y aplicable para desarrollar un asistente de IA.

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

# Workshop: **Construye tu Asistente de IA para tu Startup — Workshop Práctico**

**Duración:** 3 horas presenciales  
**Audiencia:** Emprendedores early-stage no técnicos  
**Tamaño ideal:** 20–30 personas  
**Formato:** 70% práctica, 20% demos, 10% conversación  
**Resultado esperado:** Cada participante termina con un prototipo funcional de un asistente de IA para una tarea concreta de su startup, acompañado de instrucciones, ejemplos y un plan de prueba.

---

# 1. Objetivo general del workshop

Que cada emprendedor pueda:

- Identificar una tarea repetitiva o crítica de su startup que pueda mejorar con IA.
- Diseñar el rol, contexto, tono y límites de un asistente.
- Crear un primer prototipo usando una herramienta de IA accesible y sin código.
- Probarlo con casos reales.
- Mejorar sus instrucciones a partir de los resultados.
- Definir el próximo paso para llevarlo a su operación diaria.

## Entregable final de cada participante

Al finalizar, cada persona tendrá:

1. Un caso de uso priorizado.
2. Un “canvas” de asistente.
3. Un prompt o conjunto de instrucciones base.
4. Entre 3 y 5 pruebas realizadas.
5. Una versión mejorada del asistente.
6. Un plan de implementación para los próximos 7 días.

---

# 2. Agenda detallada — 3 horas

| Tiempo | Bloque | Formato | Resultado |
|---|---|---|---|
| 00:00–00:10 | Bienvenida y activación | Dinámica + charla breve | Expectativas alineadas |
| 00:10–00:25 | ¿Qué puede hacer realmente un asistente de IA? | Charla + ejemplos | Mapa de oportunidades |
| 00:25–00:45 | Encuentra tu mejor caso de uso | Ejercicio individual + discusión | Problema priorizado |
| 00:45–01:05 | Demo: de una idea a un asistente funcional | Demo en vivo | Modelo mental claro |
| 01:05–01:40 | Sprint 1: Diseña y construye tu asistente | Ejercicio práctico | Primer prototipo |
| 01:40–01:50 | Break | Descanso | — |
| 01:50–02:15 | Sprint 2: Prueba, rompe y mejora | Ejercicio + trabajo en parejas | Asistente mejorado |
| 02:15–02:30 | IA responsable: datos, límites y revisión humana | Charla interactiva | Uso seguro y realista |
| 02:30–02:50 | Demo Day: muestra tu asistente | Presentaciones rápidas | Feedback y aprendizaje colectivo |
| 02:50–03:00 | Plan de acción y cierre | Reflexión + compromiso | Próximos pasos concretos |

**Total: 180 minutos**

---

# 3. Desarrollo de cada bloque

## Bloque 1 — Bienvenida y activación

**Duración:** 10 minutos  
**Horario:** 00:00–00:10  
**Formato:** Dinámica rápida + charla breve

### Objetivo

- Crear energía desde el comienzo.
- Conocer el nivel de experiencia de los participantes.
- Aclarar que el workshop no requiere saber programar.
- Establecer expectativas prácticas.

### Dinámica

#### 1. Encuesta de manos — 2 minutos

Preguntar:

- ¿Quién ya usa ChatGPT, Claude, Gemini u otra herramienta?
- ¿Quién la usa todas las semanas?
- ¿Quién ha intentado crear un asistente personalizado?
- ¿Quién todavía siente que “la IA responde bonito, pero no ayuda demasiado”?

#### 2. Presentación en parejas — 4 minutos

Cada participante comparte:

- Nombre y startup.
- Una tarea que le quita demasiado tiempo.
- Qué le gustaría que la IA hiciera por él o ella.

#### 3. Enmarcar el workshop — 4 minutos

Mensaje del facilitador:

> “Hoy no vamos a aprender teoría sobre IA. Vamos a salir con un pequeño miembro digital de su equipo: un asistente especializado en resolver una tarea concreta.”

### Key takeaway

**No vamos a construir una IA que haga todo. Vamos a construir un asistente que haga muy bien una tarea específica.**

### Slides estimados

**2 slides**

1. Título y promesa del workshop.
2. Objetivos, agenda y entregable final.

---

## Bloque 2 — ¿Qué puede hacer realmente un asistente de IA?

**Duración:** 15 minutos  
**Horario:** 00:10–00:25  
**Formato:** Charla breve + ejemplos + preguntas

### Objetivo

Mostrar aplicaciones concretas y realistas para startups early-stage.

### Contenido sugerido

Explicar la diferencia entre:

- **Chat genérico:** responde preguntas aisladas.
- **Asistente especializado:** tiene un rol, contexto, criterios y formato de respuesta.
- **Automatización completa:** ejecuta acciones conectada a otras herramientas.

Para este workshop se trabajará principalmente en el segundo nivel: **asistentes especializados**.

### Ejemplos de asistentes para startups

#### Ventas

- Asistente que analiza una llamada y propone próximos pasos.
- Generador de mensajes de seguimiento personalizados.
- Calificador inicial de leads.

#### Marketing

- Adaptador de una idea a LinkedIn, email, Instagram y landing page.
- Asistente de investigación de clientes.
- Generador de briefs de contenido.

#### Operaciones

- Convertidor de notas desordenadas en tareas.
- Preparador de reuniones.
- Generador de SOPs o procedimientos internos.

#### Producto

- Organizador de feedback de usuarios.
- Clasificador de tickets.
- Asistente para redactar historias de usuario.

#### Atención al cliente

- Borrador de respuestas según tono y políticas.
- Clasificador de solicitudes.
- Resumen de conversaciones complejas.

### Mini demostración conceptual

Mostrar el mismo pedido en dos versiones:

#### Prompt genérico

> “Escribe un email de ventas.”

#### Prompt especializado

> “Actúa como asistente de seguimiento comercial para una startup B2B. Escribe emails breves, claros y personalizados para leads que tuvieron una primera reunión. Nunca inventes información. Si falta un dato, indícalo como campo pendiente. Devuelve asunto, email y próximo paso sugerido.”

Preguntar al grupo:

- ¿Cuál produce un resultado más útil?
- ¿Qué información adicional se le dio al asistente?
- ¿Qué límites se incluyeron?

### Key takeaway

**La calidad de un asistente depende menos de una frase ingeniosa y más de darle contexto, criterios, ejemplos y límites.**

### Slides estimados

**4 slides**

1. Chat genérico vs. asistente especializado.
2. Mapa de casos de uso por área.
3. Comparación: prompt genérico vs. prompt especializado.
4. Fórmula base del asistente.

---

## Bloque 3 — Encuentra tu mejor caso de uso

**Duración:** 20 minutos  
**Horario:** 00:25–00:45  
**Formato:** Ejercicio individual + discusión en parejas

### Objetivo

Ayudar a cada participante a elegir un problema adecuado para construir durante el workshop.

### Criterios de un buen caso de uso

El problema ideal debe ser:

- Frecuente: ocurre varias veces por semana.
- Repetitivo: sigue un patrón.
- Importante: consume tiempo o afecta resultados.
- Textual o basado en información: emails, notas, documentos, feedback, mensajes.
- De bajo riesgo para prototipar.
- Fácil de revisar por una persona.

### Casos que conviene evitar en este workshop

- Decisiones médicas, legales o financieras críticas.
- Procesos donde un error pueda generar daños importantes.
- Automatizaciones que requieran integraciones complejas.
- Casos demasiado amplios, como “manejar todo mi negocio”.
- Uso de datos confidenciales sin autorización.

### Ejercicio: Matriz de oportunidades

Entregar una hoja con esta tabla:

| Tarea | ¿Con qué frecuencia ocurre? | ¿Cuánto tiempo consume? | ¿Qué tan repetitiva es? | ¿Qué pasa si se equivoca? | Puntaje |
|---|---:|---:|---:|---:|---:|

Cada participante lista entre 3 y 5 tareas.

Luego asigna de 1 a 5 puntos en:

- Frecuencia.
- Tiempo consumido.
- Repetitividad.
- Impacto positivo potencial.
- Facilidad para revisar el resultado.

Resta puntos si tiene alto riesgo.

### Fórmula sugerida

> **Prioridad = frecuencia + tiempo + repetitividad + impacto + facilidad de revisión – riesgo**

### Discusión en parejas

Cada persona completa:

> “Voy a construir un asistente que ayude a ________, para que pueda ________, sin tener que ________.”

Ejemplo:

> “Voy a construir un asistente que convierta notas de entrevistas con clientes en insights accionables, para detectar patrones más rápido, sin tener que revisar manualmente cada conversación.”

### Key takeaway

**El mejor primer asistente resuelve una tarea pequeña, frecuente y fácil de revisar.**

### Slides estimados

**3 slides**

1. Criterios de un buen caso de uso.
2. Ejemplos de casos recomendados y no recomendados.
3. Instrucciones de la matriz de oportunidades.

---

## Bloque 4 — Demo: de una idea a un asistente funcional

**Duración:** 20 minutos  
**Horario:** 00:45–01:05  
**Formato:** Demo en vivo, paso a paso

### Objetivo

Mostrar el proceso completo antes de que los participantes construyan su propio asistente.

### Herramienta sugerida

Utilizar una herramienta de IA conversacional con instrucciones persistentes o un chat nuevo:

- ChatGPT.
- Claude.
- Gemini.
- Otra herramienta disponible para el grupo.

La lógica debe ser independiente de la plataforma.

### Caso de demostración

Construir un asistente llamado:

> **Analista de Feedback de Clientes**

Su función será transformar notas desordenadas de entrevistas en:

- Problemas mencionados.
- Citas relevantes.
- Patrones repetidos.
- Nivel de urgencia.
- Ideas de próximos pasos.
- Preguntas pendientes.

### Estructura de instrucciones que se muestra

#### 1. Rol

> “Eres un analista de feedback para una startup early-stage.”

#### 2. Objetivo

> “Tu objetivo es ayudar al equipo fundador a identificar patrones y oportunidades a partir de entrevistas con clientes.”

#### 3. Contexto

> “La startup vende una herramienta de gestión de inventario para pequeños comercios.”

#### 4. Proceso

> “Cuando recibas notas, primero identifica problemas, luego agrúpalos por tema, estima frecuencia y propone preguntas de seguimiento.”

#### 5. Formato de salida

- Resumen ejecutivo.
- Problemas principales.
- Evidencia o citas.
- Frecuencia estimada.
- Oportunidades.
- Preguntas pendientes.

#### 6. Límites

> “No inventes citas ni datos. Si no existe suficiente evidencia, indícalo. Diferencia claramente entre hechos, inferencias e hipótesis.”

#### 7. Ejemplo de entrada

Mostrar unas notas breves de una entrevista.

#### 8. Prueba

Introducir información adicional y analizar el resultado frente al grupo.

### Interacción con el grupo

Preguntar:

- ¿Qué parte hizo que el resultado fuera más útil?
- ¿Dónde podría equivocarse?
- ¿Qué necesitaríamos revisar antes de usarlo con clientes?
- ¿Qué instrucciones agregarían?

### Key takeaway

**Un asistente se diseña como un mini miembro del equipo: rol, misión, proceso, formato de entrega y límites.**

### Slides estimados

**5 slides**

1. El caso de demo.
2. La anatomía de un asistente.
3. Las instrucciones base.
4. Ejemplo de entrada y salida.
5. Cómo evaluar rápidamente la respuesta.

---

## Bloque 5 — Sprint 1: Diseña y construye tu asistente

**Duración:** 35 minutos  
**Horario:** 01:05–01:40  
**Formato:** Ejercicio práctico individual, con apoyo del equipo facilitador

### Objetivo

Que cada participante construya la primera versión funcional de su asistente.

### Ejercicio principal del workshop

## “De tarea repetitiva a asistente funcional”

Cada participante utilizará un **Assistant Canvas** y luego convertirá ese diseño en instrucciones dentro de su herramienta de IA.

### Assistant Canvas

#### A. Nombre del asistente

¿Qué nombre tendría una persona de tu equipo?

Ejemplos:

- Copiloto de Seguimiento Comercial.
- Analista de Feedback.
- Editor de Contenido.
- Preparador de Reuniones.
- Asistente de Soporte.

#### B. Usuario principal

¿Quién lo va a utilizar?

- Fundador.
- Persona de ventas.
- Community manager.
- Equipo de soporte.
- Product manager.

#### C. Tarea específica

Completar:

> “Este asistente ayuda a ________ a convertir ________ en ________.”

Ejemplo:

> “Este asistente ayuda al fundador a convertir notas de reuniones comerciales en emails de seguimiento claros y personalizados.”

#### D. Inputs

¿Qué información recibirá?

- Notas.
- Transcripción.
- Descripción de cliente.
- Email recibido.
- Lista de funcionalidades.
- Feedback de usuarios.

#### E. Outputs

¿Qué debe entregar?

- Resumen.
- Lista priorizada.
- Email.
- Tabla.
- Ideas.
- Próximos pasos.
- Preguntas aclaratorias.

#### F. Criterios de calidad

¿Cómo se reconoce una buena respuesta?

- Es clara.
- Es breve.
- No inventa datos.
- Está adaptada al contexto.
- Incluye recomendaciones accionables.
- Distingue hechos de opiniones.

#### G. Tono y estilo

- Profesional.
- Cercano.
- Directo.
- Persuasivo.
- Simple.
- En español latinoamericano.

#### H. Límites

¿Qué no debe hacer?

- Inventar información.
- Tomar decisiones finales.
- Compartir datos confidenciales.
- Dar asesoría legal o financiera.
- Responder si faltan datos críticos.

### Plantilla de prompt base

Entregar esta estructura:

```text
# Rol
Eres [rol específico] para [tipo de startup o equipo].

# Objetivo
Tu objetivo es ayudar a [usuario] a [resultado concreto].

# Contexto
Ten en cuenta:
- [dato relevante sobre la startup]
- [tipo de cliente]
- [producto o servicio]
- [situación habitual]

# Proceso
Cada vez que recibas información:
1. [paso 1]
2. [paso 2]
3. [paso 3]
4. [paso 4]

# Formato de respuesta
Entrega siempre:
1. [sección 1]
2. [sección 2]
3. [sección 3]

Usa [tabla/lista/bullets/estructura].

# Tono
Utiliza un tono [descripción del tono].
Escribe en [idioma o variante].

# Reglas y límites
- No inventes información.
- Si falta un dato importante, haz una pregunta.
- Distingue entre hechos, inferencias e hipótesis.
- [regla específica del caso].

# Ejemplo
Entrada:
[ejemplo breve]

Salida esperada:
[ejemplo breve]
```

### Secuencia del sprint

| Minutos | Actividad |
|---:|---|
| 5 | Elegir y nombrar el asistente |
| 8 | Completar el Canvas |
| 10 | Escribir las instrucciones base |
| 7 | Probar con un caso real o simulado |
| 5 | Revisar y ajustar |

### Rol de los facilitadores

Con 20–30 personas, idealmente contar con 2 o 3 facilitadores.

Durante el sprint, circular y ayudar especialmente con:

- Casos de uso demasiado amplios.
- Prompts con objetivos ambiguos.
- Falta de formato de salida.
- Uso de datos sensibles.
- Expectativas irreales de automatización.

### Key takeaway

**La primera versión no tiene que ser perfecta: tiene que ser suficientemente útil para probarla.**

### Slides estimados

**4 slides**

1. Instrucciones del sprint.
2. Assistant Canvas.
3. Plantilla de prompt.
4. Checklist de primera versión.

---

## Bloque 6 — Break

**Duración:** 10 minutos  
**Horario:** 01:40–01:50

### Recomendaciones

Durante el descanso:

- Dejar proyectados ejemplos de asistentes.
- Mostrar un QR al template del workshop.
- Pedir a los participantes que no cierren su herramienta.
- Invitar a probar una entrada adicional si terminan antes.

### Slides estimados

**1 slide**

- “Break — vuelve con una prueba real de tu asistente”.

---

## Bloque 7 — Sprint 2: Prueba, rompe y mejora

**Duración:** 25 minutos  
**Horario:** 01:50–02:15  
**Formato:** Testing individual + revisión en parejas

### Objetivo

Pasar de un prompt “que suena bien” a un asistente que produce resultados consistentes.

### Introducción: no evaluar con un solo ejemplo

Explicar que un asistente debe probarse con diferentes tipos de input:

1. Caso normal.
2. Caso incompleto.
3. Caso ambiguo.
4. Caso difícil.
5. Caso con información que no debería inventar.

### Test Card

Cada participante debe ejecutar al menos tres pruebas:

| Prueba | Input utilizado | ¿Qué esperaba? | ¿Qué ocurrió? | Mejora necesaria |
|---|---|---|---|---|
| Normal |  |  |  |  |
| Incompleta |  |  |  |  |
| Difícil o ambigua |  |  |  |  |

### Preguntas para evaluar

- ¿Entendió correctamente la tarea?
- ¿Entregó el formato solicitado?
- ¿El tono fue adecuado?
- ¿Inventó información?
- ¿Hizo preguntas cuando faltaban datos?
- ¿La respuesta ahorra tiempo?
- ¿Qué parte aún requiere revisión humana?

### Revisión en parejas

Cada persona muestra:

- El caso de uso.
- Una entrada.
- La respuesta obtenida.
- El principal problema detectado.

La pareja debe responder:

1. ¿Qué está funcionando?
2. ¿Qué instrucción falta?
3. ¿Qué riesgo observamos?
4. ¿Qué cambiaríamos primero?

### Técnicas rápidas de mejora

#### Si responde demasiado genérico

Agregar contexto, audiencia y ejemplos.

#### Si entrega demasiado texto

Definir límite de extensión y formato.

#### Si inventa información

Agregar:

> “Si no tienes evidencia suficiente, responde ‘información insuficiente’ y explica qué dato falta.”

#### Si no sigue el formato

Mostrar un ejemplo exacto del formato esperado.

#### Si mezcla hechos y opiniones

Pedir secciones separadas:

- Hechos observados.
- Interpretaciones.
- Recomendaciones.

### Key takeaway

**La mejora ocurre al probar casos reales y convertir los errores en nuevas instrucciones.**

### Slides estimados

**3 slides**

1. Cómo probar un asistente.
2. Test Card.
3. Errores frecuentes y cómo corregirlos.

---

## Bloque 8 — IA responsable: datos, límites y revisión humana

**Duración:** 15 minutos  
**Horario:** 02:15–02:30  
**Formato:** Charla interactiva + mini casos

### Objetivo

Dar criterios prácticos para utilizar asistentes sin poner en riesgo información, clientes o decisiones importantes.

### Contenido

## Regla 1: No pegar información sensible sin autorización

Evitar introducir:

- Contraseñas.
- Datos bancarios.
- Información personal innecesaria.
- Información médica.
- Contratos confidenciales.
- Datos de clientes identificables.
- Información estratégica que no debería salir de la empresa.

Usar, cuando sea posible:

- Datos anonimizados.
- Nombres ficticios.
- Ejemplos sintéticos.
- Fragmentos mínimos necesarios.

## Regla 2: La IA puede ayudar, pero no siempre debe decidir

Especialmente en:

- Contrataciones.
- Despidos.
- Créditos.
- Asesoría legal.
- Diagnósticos médicos.
- Decisiones financieras.
- Evaluaciones de personas.

## Regla 3: Siempre definir un punto de revisión humana

Preguntar:

- ¿Qué revisará una persona?
- ¿Qué errores serían inaceptables?
- ¿Qué información debe escalarse?
- ¿Cuándo el asistente debe detenerse y pedir ayuda?

## Regla 4: No confundir fluidez con verdad

Una respuesta convincente puede ser incorrecta. Validar:

- Números.
- Fechas.
- Fuentes.
- Nombres.
- Compromisos con clientes.
- Recomendaciones críticas.

### Mini dinámica: “¿Lo automatizarías?”

Presentar tres casos y pedir que levanten una tarjeta:

- Verde: se puede automatizar con revisión mínima.
- Amarillo: IA ayuda, pero requiere revisión.
- Rojo: no delegar la decisión a la IA.

Ejemplos:

1. Convertir notas de una reunión en tareas.
2. Recomendar si aprobar o rechazar un crédito.
3. Redactar un primer borrador de email comercial.

### Key takeaway

**La IA puede preparar, resumir y sugerir; la responsabilidad final sigue siendo humana.**

### Slides estimados

**3 slides**

1. Datos que no se deben compartir.
2. Semáforo de automatización.
3. Checklist de revisión humana.

---

## Bloque 9 — Demo Day: muestra tu asistente

**Duración:** 20 minutos  
**Horario:** 02:30–02:50  
**Formato:** Presentaciones rápidas + feedback colectivo

### Objetivo

Celebrar avances, compartir aprendizajes y mostrar aplicaciones diversas.

### Dinámica

Seleccionar entre 6 y 8 participantes para presentaciones de aproximadamente 2 minutos.

Si hay 20–30 participantes, se puede hacer:

- 6 demos frente a todo el grupo.
- El resto comparte en grupos de 4 o 5 personas.

### Estructura de cada demo

Cada participante responde:

1. ¿Qué tarea resolvía?
2. ¿Para quién construyó el asistente?
3. ¿Qué input recibe?
4. ¿Qué output produce?
5. ¿Qué mejoró después de las pruebas?
6. ¿Qué parte todavía debe revisar una persona?

### Formato de feedback

El público responde usando:

- **Me gusta:** qué está funcionando.
- **Me pregunto:** qué falta aclarar.
- **Probaría:** qué caso adicional testearía.

### Criterios de evaluación amigables

No se busca premiar el prompt más sofisticado. Se evalúa:

- Claridad del problema.
- Utilidad práctica.
- Especificidad.
- Calidad del formato de salida.
- Manejo de límites.
- Potencial de uso semanal.

### Key takeaway

**Un buen asistente no es el que tiene más funciones, sino el que produce un resultado útil y repetible.**

### Slides estimados

**2 slides**

1. Instrucciones del Demo Day.
2. Formato de feedback: Me gusta / Me pregunto / Probaría.

---

## Bloque 10 — Plan de acción y cierre

**Duración:** 10 minutos  
**Horario:** 02:50–03:00  
**Formato:** Reflexión individual + compromiso

### Objetivo

Convertir el prototipo del workshop en una acción real dentro de la startup.

### Ejercicio: Plan de 7 días

Cada participante completa:

#### Mi asistente

> “Mi asistente ayuda a ________ con ________.”

#### Primera situación real de uso

> “Lo voy a utilizar por primera vez para ________.”

#### Métrica de éxito

Elegir una:

- Minutos ahorrados.
- Número de tareas procesadas.
- Reducción de retrabajo.
- Calidad percibida por el usuario.
- Tiempo de respuesta.
- Número de errores detectados.

#### Próximo paso en 48 horas

> “Antes de ________, voy a ________.”

#### Próximo paso en 7 días

> “En los próximos 7 días voy a probarlo con ________ casos reales.”

#### Riesgo a vigilar

> “Debo revisar especialmente ________.”

### Cierre del facilitador

Mensaje sugerido:

> “No se lleven la idea de que necesitan construir una gran plataforma de IA. Llévense la práctica de identificar una tarea, darle contexto a la IA, probarla con casos reales y mejorarla. Ese ciclo, repetido cada semana, es lo que construye una ventaja.”

### Key takeaway

**El verdadero resultado del workshop es instalar un hábito: detectar, prototipar, probar y mejorar.**

### Slides estimados

**2 slides**

1. Plan de acción de 7 días.
2. Cierre, recursos y llamada a la acción.

---

# 4. Ejercicio principal resumido

## Nombre

**De tarea repetitiva a asistente funcional**

## Duración total

- 20 minutos para elegir el caso de uso.
- 35 minutos para construir.
- 25 minutos para probar y mejorar.
- 20 minutos para compartir.

## Qué hace cada participante

1. Lista tareas repetitivas de su startup.
2. Prioriza una usando una matriz simple.
3. Define:
   - Rol.
   - Usuario.
   - Objetivo.
   - Input.
   - Output.
   - Tono.
   - Criterios de calidad.
   - Límites.
4. Escribe las instrucciones del asistente.
5. Prueba con tres tipos de casos.
6. Ajusta las instrucciones.
7. Define cómo lo probará durante los próximos 7 días.

## Ejemplos de asistentes que podrían construir

- Generador de follow-ups de ventas.
- Clasificador de feedback de clientes.
- Asistente para responder preguntas frecuentes.
- Creador de briefs de contenido.
- Preparador de reuniones.
- Generador de propuestas comerciales.
- Convertidor de notas en tareas.
- Asistente para entrevistas de usuarios.
- Organizador de solicitudes internas.
- Revisor de mensajes antes de enviarlos.

---

# 5. Materiales necesarios

## Para preparar antes del workshop

### Tecnología

- Computador del facilitador.
- Proyector o pantalla.
- Adaptador HDMI/USB-C.
- Buena conexión Wi-Fi.
- Extensiones y regletas.
- Temporizador visible.
- Micrófono si la sala es grande.
- Plan alternativo offline por si falla internet.

### Cuentas y herramientas

Definir una herramienta principal y una alternativa.

Por ejemplo:

- Herramienta principal: ChatGPT, Claude o Gemini.
- Herramienta alternativa: otra plataforma accesible desde navegador.

Antes del evento:

- Confirmar qué funcionalidades requieren plan pagado.
- Crear cuentas de prueba si es necesario.
- Preparar un asistente de demo.
- Probar la demo en la misma red o con hotspot.
- Tener capturas de pantalla de respaldo.
- Compartir con anticipación el enlace de acceso y requisitos.

### Material impreso

Imprimir:

1. Assistant Canvas.
2. Matriz de oportunidades.
3. Plantilla de prompt.
4. Test Cards.
5. Plan de acción de 7 días.
6. Hoja de feedback para el Demo Day.
7. Checklist de IA responsable.

Recomendación:

- 1 set por participante.
- 10% adicional para reemplazos.
- Hojas tamaño A4 o carta.
- Portapapeles si las mesas no son cómodas.

### Materiales de la sala

- Post-its.
- Marcadores gruesos.
- Bolígrafos.
- Stickers o tarjetas verdes, amarillas y rojas.
- Cinta adhesiva.
- Papelógrafos o pizarra.
- Tarjetas con ejemplos de casos de uso.

### Preparación del espacio

Idealmente:

- Mesas de 4–5 personas.
- Visibilidad clara de la pantalla.
- Espacio para circular.
- Una mesa o estación de soporte técnico.
- Pizarra visible para capturar aprendizajes.
- Enchufes accesibles.

## Preparación de los participantes

Enviar 24–72 horas antes:

- Objetivo del workshop.
- Duración y dirección.
- Recomendación de llevar computador.
- Enlace para crear una cuenta en la herramienta elegida.
- Pedido de pensar en 2 o 3 tareas repetitivas de su startup.
- Aviso de no traer datos confidenciales reales.
- Instrucción para llevar un ejemplo anonimizado.

---

# 6. Recursos para llevar a casa

## Pack digital del workshop

Crear una carpeta o página con:

### Templates

- Assistant Canvas.
- Matriz de priorización.
- Plantilla de prompt.
- Test Card.
- Checklist de calidad.
- Plan de implementación de 7 días.
- Plantilla de documentación del asistente.

### Guías rápidas

#### Guía 1: Anatomía de un buen asistente

- Rol.
- Objetivo.
- Contexto.
- Proceso.
- Formato.
- Tono.
- Ejemplos.
- Límites.

#### Guía 2: Cómo mejorar una respuesta

- Añadir contexto.
- Definir audiencia.
- Pedir estructura.
- Incluir ejemplos.
- Definir longitud.
- Separar hechos e hipótesis.
- Pedir preguntas aclaratorias.

#### Guía 3: Casos de uso para startups

Organizados por:

- Ventas.
- Marketing.
- Producto.
- Operaciones.
- Soporte.
- Finanzas administrativas.
- Recursos humanos.

### Biblioteca de prompts iniciales

Incluir prompts adaptables para:

1. Resumir una reunión.
2. Convertir notas en tareas.
3. Analizar feedback de usuarios.
4. Crear un email de seguimiento.
5. Redactar una propuesta comercial.
6. Generar un calendario de contenido.
7. Clasificar leads.
8. Preparar preguntas para entrevistas.
9. Crear un SOP.
10. Revisar un mensaje para clientes.

### Checklist para antes de usar un asistente

- ¿La tarea está claramente definida?
- ¿El asistente sabe quién es el usuario?
- ¿Tiene suficiente contexto?
- ¿El output está estructurado?
- ¿Incluye ejemplos?
- ¿Tiene límites?
- ¿Probé casos normales y difíciles?
- ¿Sé qué debe revisar una persona?
- ¿Estoy protegiendo datos sensibles?
- ¿Tengo una métrica de éxito?

### Recursos de aprendizaje

- Documentación oficial de la plataforma elegida.
- Cursos introductorios de prompting.
- Guías de privacidad y uso responsable de IA.
- Comunidades locales de founders y tecnología.
- Casos de uso de IA para pequeñas empresas.
- Plantilla para documentar aprendizajes de cada prueba.

---

# 7. Slide count estimado por sección

| Sección | Slides |
|---|---:|
| Bienvenida y objetivos | 2 |
| Qué puede hacer un asistente | 4 |
| Selección del caso de uso | 3 |
| Demo en vivo | 5 |
| Sprint 1: construcción | 4 |
| Break | 1 |
| Sprint 2: testing | 3 |
| IA responsable | 3 |
| Demo Day | 2 |
| Cierre y plan de acción | 2 |
| **Total estimado** | **29 slides** |

## Recomendación

Mantener el deck entre **28 y 32 slides**. Las instrucciones detalladas de los ejercicios deben estar también impresas o disponibles mediante QR para no llenar las diapositivas de texto.

---

# 8. Roles recomendados del equipo facilitador

Para 20–30 participantes:

## Facilitador principal

- Marca el ritmo.
- Conduce las explicaciones.
- Realiza la demo.
- Hace los cierres de cada bloque.

## Facilitador de apoyo 1

- Ayuda con problemas de acceso.
- Revisa casos de uso.
- Apoya a participantes que se queden bloqueados.

## Facilitador de apoyo 2

- Controla tiempos.
- Recoge preguntas.
- Coordina las presentaciones.
- Identifica buenos ejemplos para compartir.

---

# 9. Indicadores de éxito del workshop

Al terminar, idealmente:

- 90% de los participantes tiene un caso de uso definido.
- 80% tiene un prototipo funcional.
- Cada participante realizó al menos tres pruebas.
- Cada persona identificó un límite o riesgo.
- Cada participante tiene una acción concreta para los próximos 7 días.
- Se recopilaron ejemplos de asistentes de distintas áreas.

## Encuesta de cierre sugerida

Pedir una valoración de 1 a 5 sobre:

1. Claridad del workshop.
2. Utilidad práctica.
3. Facilidad para construir el asistente.
4. Confianza para seguir experimentando.
5. Probabilidad de usar el asistente en los próximos 7 días.

Pregunta abierta:

> “¿Qué tarea de tu startup vas a transformar con IA después de este workshop?”