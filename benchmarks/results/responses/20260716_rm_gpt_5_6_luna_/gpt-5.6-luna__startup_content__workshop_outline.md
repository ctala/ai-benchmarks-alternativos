# GPT-5.6 Luna — startup_content/workshop_outline

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 46.048s | tokens_per_second: 150.0
- input_tokens: 186 | output_tokens: 6908
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que proporciona un plan detallado y práctico para un workshop de emprendimiento, ofreciendo insights útiles para emprendedores no técnicos.

## Respuesta completa

# Workshop presencial de 3 horas  
## **Construye tu Asistente de IA para tu Startup — Workshop Práctico**

**Audiencia:** Emprendedores early-stage no técnicos  
**Tamaño ideal:** 20–30 personas  
**Duración:** 3 horas / 180 minutos  
**Formato:** 30% conceptos, 70% práctica  
**Resultado esperado:** Cada participante termina con un prototipo funcional de un asistente de IA, una ficha de diseño y un plan para probarlo en su startup.

---

# 1. Objetivos del workshop

Al finalizar, los participantes podrán:

1. Identificar una tarea repetitiva de su startup que pueda ser asistida por IA.
2. Diseñar el rol, alcance y personalidad de un asistente.
3. Escribir instrucciones claras para un asistente sin necesidad de programar.
4. Crear un prototipo utilizando una herramienta de IA generativa.
5. Probarlo con casos reales y mejorar sus respuestas.
6. Reconocer límites, riesgos y datos que no deben compartirse.
7. Definir el siguiente experimento para llevarlo a su negocio.

---

# 2. Agenda general — 180 minutos

| Tiempo | Bloque | Formato | Resultado |
|---|---|---|---|
| 00:00–00:10 | Bienvenida y activación | Dinámica | Expectativas y problema elegido |
| 00:10–00:25 | IA aplicada a startups | Charla interactiva | Entender qué puede y no puede hacer un asistente |
| 00:25–00:45 | Encuentra el caso de uso correcto | Ejercicio | Seleccionar una tarea concreta |
| 00:45–01:05 | Diseña tu asistente | Ejercicio guiado | Ficha de diseño completada |
| 01:05–01:20 | Cómo escribir instrucciones efectivas | Demo + práctica | Primer prompt estructurado |
| 01:20–01:30 | Pausa | Networking | — |
| 01:30–02:00 | Construcción paso a paso | Demo + construcción | Primer prototipo funcional |
| 02:00–02:25 | Prueba con casos reales | Ejercicio | Feedback y detección de errores |
| 02:25–02:40 | Mejora: contexto, tono y límites | Iteración práctica | Versión mejorada |
| 02:40–02:55 | Demo relámpago y aprendizajes | Presentaciones | Compartir resultados |
| 02:55–03:00 | Cierre y próximos pasos | Reflexión | Plan de acción de 7 días |

---

# 3. Detalle de cada bloque

## Bloque 1 — Bienvenida y activación  
### 00:00–00:10 | 10 minutos

**Objetivo**  
Romper el hielo, alinear expectativas y conectar el workshop con problemas reales de los participantes.

**Dinámica**

1. Bienvenida del facilitador.
2. Presentación rápida del resultado esperado:
   - “En tres horas vas a salir con un asistente que puedes probar en tu startup”.
3. Encuesta rápida a mano alzada:
   - ¿Quién ya utiliza ChatGPT, Gemini, Claude u otra herramienta?
   - ¿Quién siente que pierde tiempo en tareas repetitivas?
   - ¿Quién ya intentó crear un asistente?
4. Dinámica “Mi tarea más repetitiva”:
   - Cada participante escribe en una tarjeta una tarea que repite semanalmente.
   - Ejemplos:
     - Responder preguntas frecuentes.
     - Crear propuestas comerciales.
     - Resumir entrevistas.
     - Preparar contenido.
     - Analizar feedback de clientes.

**Key takeaway**  
> La IA no empieza con la herramienta. Empieza con una tarea concreta y repetitiva que vale la pena mejorar.

**Slide count estimado:** 2 slides

---

## Bloque 2 — IA aplicada a startups: de chatbot a asistente  
### 00:10–00:25 | 15 minutos

**Objetivo**  
Dar un marco simple para entender qué es un asistente de IA y cuándo tiene sentido utilizarlo.

**Dinámica**  
Charla interactiva con ejemplos y preguntas al grupo.

### Contenidos sugeridos

#### ¿Qué es un asistente de IA?

Un asistente es una combinación de:

1. **Rol:** quién es y qué función cumple.
2. **Objetivo:** qué resultado debe ayudar a conseguir.
3. **Contexto:** qué necesita saber sobre el negocio.
4. **Proceso:** cómo debe realizar la tarea.
5. **Formato:** cómo debe entregar la respuesta.
6. **Límites:** qué no debe hacer.
7. **Criterios de calidad:** cómo saber si la respuesta es buena.

#### Ejemplos para una startup

- Asistente de ventas:
  - Califica leads y propone próximos pasos.
- Asistente de customer success:
  - Sugiere respuestas para clientes.
- Asistente de contenido:
  - Convierte ideas en publicaciones.
- Asistente de investigación:
  - Resume entrevistas y detecta patrones.
- Asistente operativo:
  - Convierte notas desordenadas en tareas.
- Asistente financiero inicial:
  - Ayuda a categorizar gastos, sin reemplazar asesoría contable.

#### Qué puede hacer bien

- Clasificar información.
- Resumir.
- Generar primeras versiones.
- Comparar alternativas.
- Adaptar tono y formato.
- Detectar patrones en información proporcionada.

#### Qué no debemos asumir

- Que siempre tiene razón.
- Que conoce el contexto de la empresa automáticamente.
- Que puede tomar decisiones sensibles sin supervisión.
- Que los datos confidenciales están protegidos por defecto.
- Que una respuesta convincente es necesariamente correcta.

**Mini demostración**

Mostrar el mismo pedido de dos formas:

> “Escribe un email de ventas.”

 versus:

> “Actúa como ejecutivo de ventas B2B para una startup de software de gestión de inventario. Escribe un email breve para un gerente de operaciones que descargó nuestra guía sobre reducción de quiebres de stock. Usa un tono consultivo, no agresivo. Incluye un asunto y un llamado a una conversación de 20 minutos.”

Comparar el resultado.

**Key takeaway**  
> Un buen asistente no es el que “responde bonito”; es el que ayuda consistentemente a lograr un resultado específico.

**Slide count estimado:** 3 slides

---

## Bloque 3 — Encuentra el caso de uso correcto  
### 00:25–00:45 | 20 minutos

**Objetivo**  
Evitar casos demasiado amplios y elegir una tarea realista para construir durante el workshop.

**Dinámica**  
Ejercicio individual + discusión en parejas.

### Ejercicio: Matriz de selección de oportunidades

Cada participante lista 3 tareas de su startup y las evalúa de 1 a 5 en cuatro criterios:

| Criterio | Pregunta |
|---|---|
| Frecuencia | ¿La hacemos seguido? |
| Dolor | ¿Consume tiempo o genera frustración? |
| Repetibilidad | ¿Tiene pasos relativamente similares? |
| Impacto | ¿Mejorarla tendría valor para el negocio? |

**Fórmula sencilla:**

> Oportunidad = Frecuencia + Dolor + Repetibilidad + Impacto

Luego seleccionan una tarea con estas características:

- Tiene un usuario claro.
- Tiene una entrada concreta.
- Tiene una salida esperada.
- Puede ser revisada por una persona.
- No requiere acceso a sistemas complejos para el primer prototipo.

### Ejemplos recomendados

**Buen caso de uso para el workshop:**

> “Convertir notas de una entrevista con clientes en insights, citas y próximos experimentos.”

**Demasiado amplio:**

> “Crear un asistente que maneje todo mi negocio.”

**Buen caso de uso:**

> “Generar una primera respuesta para consultas frecuentes de potenciales clientes.”

**Demasiado riesgoso para empezar:**

> “Responder automáticamente reclamos legales o recomendaciones médicas.”

### Discusión en parejas

Cada persona explica:

1. Qué tarea eligió.
2. Quién la realiza hoy.
3. Cuánto tiempo consume.
4. Qué resultado espera obtener.

La pareja debe hacer una pregunta:

> “¿Cómo sabrías que la respuesta del asistente fue útil?”

**Key takeaway**  
> El primer asistente debe resolver una tarea pequeña, frecuente y medible. No hay que automatizar toda la startup el primer día.

**Slide count estimado:** 4 slides

---

## Bloque 4 — Diseña tu asistente antes de construirlo  
### 00:45–01:05 | 20 minutos

**Objetivo**  
Transformar una idea general en una especificación sencilla y accionable.

**Dinámica**  
Ejercicio guiado utilizando una ficha de diseño.

## Ficha de diseño del asistente

Cada participante completa:

### 1. Nombre del asistente

Ejemplos:

- ValidaPro
- Copiloto de Ventas
- Entrevista Insight
- Content Booster
- Soporte Inicial

### 2. Usuario principal

¿Quién lo utilizará?

- Fundador.
- Ejecutivo comercial.
- Equipo de soporte.
- Community manager.
- Analista de operaciones.

### 3. Tarea principal

Completar:

> “Este asistente ayuda a ________ a ________.”

Ejemplo:

> “Este asistente ayuda a fundadores a convertir entrevistas con clientes en aprendizajes accionables.”

### 4. Entrada

¿Qué debe recibir?

- Texto de una entrevista.
- Mensaje de un cliente.
- Descripción de un lead.
- Idea de contenido.
- Lista de gastos.
- Notas de una reunión.

### 5. Salida

¿Qué debe entregar?

- Resumen.
- Tabla.
- Email.
- Recomendaciones.
- Lista priorizada.
- Próximos pasos.
- Preguntas de seguimiento.

### 6. Tono

- Directo.
- Cercano.
- Profesional.
- Desafiante.
- Simple.
- Ejecutivo.

### 7. Qué debe evitar

- Inventar información.
- Dar respuestas definitivas sin evidencia.
- Usar lenguaje demasiado técnico.
- Ser agresivo en ventas.
- Compartir información confidencial.
- Tomar decisiones sin aprobación humana.

### 8. Criterios de calidad

Una buena respuesta debe ser:

- Clara.
- Específica.
- Accionable.
- Basada en la información entregada.
- Fácil de revisar.
- Consistente con el tono de la marca.

**Key takeaway**  
> Antes de construir el asistente, define claramente quién lo usa, para qué, con qué información y cómo debe responder.

**Slide count estimado:** 4 slides

---

## Bloque 5 — Cómo escribir instrucciones efectivas  
### 01:05–01:20 | 15 minutos

**Objetivo**  
Enseñar una estructura de instrucciones que cualquier persona pueda reutilizar.

**Dinámica**  
Demo en vivo + práctica rápida de reescritura.

## Framework de instrucciones: ROL + OBJETIVO + CONTEXTO + PROCESO + FORMATO + LÍMITES

### Plantilla

```text
ROL
Actúa como [rol específico] para [tipo de negocio o usuario].

OBJETIVO
Tu objetivo es ayudar a [usuario] a [resultado concreto].

CONTEXTO
Nuestra startup ofrece [descripción breve].
Nuestro cliente principal es [tipo de cliente].
El tono de comunicación es [tono].

PROCESO
Cuando recibas información:
1. [Paso 1]
2. [Paso 2]
3. [Paso 3]
4. Si falta información, haz hasta [número] preguntas antes de responder.

FORMATO DE RESPUESTA
Entrega la respuesta en este formato:
- Resumen:
- Hallazgos:
- Recomendación:
- Próximos pasos:

LÍMITES
- No inventes datos.
- Distingue hechos de opiniones.
- Indica qué información falta.
- No tomes decisiones finales sin aprobación humana.
```

### Mini ejercicio

Entregar un prompt débil:

> “Ayúdame con mis entrevistas de clientes.”

Pedir que lo conviertan en una instrucción más específica usando la plantilla.

### Demo de mejora

Mostrar cómo cambia la respuesta al agregar:

- Rol.
- Contexto.
- Formato.
- Límites.
- Ejemplo de respuesta ideal.

**Key takeaway**  
> La calidad de la respuesta depende mucho de la calidad de las instrucciones y del contexto entregado.

**Slide count estimado:** 3 slides

---

## Bloque 6 — Pausa  
### 01:20–01:30 | 10 minutos

**Objetivo**  
Dar descanso y permitir que los participantes creen o revisen sus cuentas.

**Dinámica**

- Pausa libre.
- Networking rápido.
- El equipo facilitador ayuda con:
  - Acceso a la herramienta.
  - Recuperación de contraseñas.
  - Elección del caso de uso.
  - Problemas de conexión.

**Key takeaway**  
> La pausa también es parte del prototipo: conversar con otros ayuda a descubrir mejores casos de uso.

**Slide count estimado:** 1 slide

---

## Bloque 7 — Construcción paso a paso  
### 01:30–02:00 | 30 minutos

**Objetivo**  
Construir el primer prototipo funcional del asistente.

**Dinámica**  
Demo del facilitador seguida de construcción individual o en parejas.

## Herramienta sugerida

Utilizar una herramienta de IA generativa con instrucciones personalizadas, por ejemplo:

- ChatGPT con GPT personalizado, proyecto o conversación estructurada.
- Claude con proyecto o instrucciones persistentes.
- Gemini con Gem.
- Otra plataforma no-code disponible para los participantes.

**Importante:** El workshop debe tener una ruta alternativa basada únicamente en copiar y pegar el prompt en un chat, para quienes no tengan acceso a funciones premium.

### Paso 1: Crear la conversación o asistente

Explicar:

- Dónde colocar las instrucciones.
- Dónde agregar información de contexto.
- Cómo nombrar el asistente.
- Cómo iniciar una conversación de prueba.

### Paso 2: Copiar la instrucción base

Cada participante utiliza la ficha completada en el bloque anterior.

### Paso 3: Agregar contexto mínimo

Ejemplos:

- Descripción de la startup.
- Cliente objetivo.
- Producto o servicio.
- Tono de marca.
- Ejemplo de una buena respuesta.
- Glosario de términos importantes.

### Paso 4: Probar con una entrada real

Cada participante utiliza información no sensible de su negocio.

Ejemplos:

- Una entrevista ficticia o anonimizada.
- Un mensaje de cliente sin datos personales.
- Una descripción genérica de un lead.
- Una idea de contenido.
- Notas de una reunión.

### Paso 5: Revisar la salida

Preguntas de revisión:

- ¿Respondió a la tarea?
- ¿Usó el tono correcto?
- ¿Entregó el formato solicitado?
- ¿Inventó algo?
- ¿Faltó información?
- ¿Qué cambiarías en sus instrucciones?

**Key takeaway**  
> El primer prototipo no tiene que ser perfecto. Tiene que ser suficientemente funcional para probarlo con un caso real.

**Slide count estimado:** 5 slides

---

# 4. Ejercicio principal del workshop

## “Construye, prueba y mejora tu asistente en 60 minutos”

El ejercicio principal ocurre entre los bloques 4 y 9 y tiene tres entregables:

### Entregable 1: Ficha de diseño

Cada participante define:

- Nombre.
- Usuario.
- Problema.
- Entrada.
- Salida.
- Tono.
- Límites.
- Criterios de calidad.

### Entregable 2: Instrucciones del asistente

Cada participante convierte la ficha en instrucciones utilizando:

> Rol + Objetivo + Contexto + Proceso + Formato + Límites

### Entregable 3: Prototipo probado

Cada participante debe tener:

- Un asistente configurado o una conversación con instrucciones persistentes.
- Al menos tres pruebas realizadas.
- Una mejora aplicada después de revisar los resultados.
- Un caso de uso concreto para probar durante la siguiente semana.

## Casos de uso sugeridos para quienes no sepan qué construir

### Opción A: Asistente de entrevistas

Transforma notas de entrevistas en:

- Problemas detectados.
- Evidencia textual.
- Necesidades recurrentes.
- Hipótesis.
- Preguntas de seguimiento.
- Próximos experimentos.

### Opción B: Asistente de ventas

Recibe información de un potencial cliente y entrega:

- Nivel de interés.
- Necesidad principal.
- Preguntas pendientes.
- Próximo paso sugerido.
- Borrador de seguimiento.

### Opción C: Asistente de contenido

Recibe una idea y entrega:

- Tres ángulos de contenido.
- Un post para LinkedIn.
- Un guion corto para video.
- Un llamado a la acción.
- Preguntas que podrían generar conversación.

### Opción D: Asistente de soporte

Recibe una pregunta frecuente y entrega:

- Respuesta sugerida.
- Nivel de confianza.
- Información faltante.
- Cuándo escalar a una persona.

---

## Bloque 8 — Prueba con casos reales  
### 02:00–02:25 | 25 minutos

**Objetivo**  
Validar si el asistente funciona fuera del ejemplo ideal.

**Dinámica**  
Testing individual y revisión cruzada en parejas.

## Protocolo de prueba: “3 casos, 3 preguntas”

Cada participante prueba su asistente con tres inputs:

1. **Caso normal:** información completa y clara.
2. **Caso incompleto:** faltan datos importantes.
3. **Caso difícil:** información ambigua, contradictoria o fuera de alcance.

### Checklist de evaluación

Calificar cada respuesta de 1 a 5:

| Criterio | Pregunta |
|---|---|
| Relevancia | ¿Respondió a la tarea correcta? |
| Claridad | ¿Es fácil de entender? |
| Utilidad | ¿Puedo actuar a partir de la respuesta? |
| Consistencia | ¿Mantiene el formato y tono? |
| Confiabilidad | ¿Evita inventar información? |

### Revisión en parejas

Cada persona le muestra su asistente a otra y responde:

- ¿Qué parte fue más útil?
- ¿Qué parte fue confusa?
- ¿Qué pregunta debería hacer el asistente antes de responder?
- ¿Qué información adicional necesitaría?
- ¿En qué situación no confiarías en este asistente?

**Key takeaway**  
> Un asistente se valida con casos imperfectos, no solamente con el ejemplo que usamos para construirlo.

**Slide count estimado:** 3 slides

---

## Bloque 9 — Mejora: contexto, tono y límites  
### 02:25–02:40 | 15 minutos

**Objetivo**  
Mejorar la calidad del prototipo con iteraciones simples.

**Dinámica**  
Ejercicio de iteración rápida.

Cada participante elige al menos dos mejoras de esta lista:

### Mejora 1: Agregar preguntas de clarificación

> “Si faltan datos críticos, no respondas inmediatamente. Haz primero hasta tres preguntas concretas.”

### Mejora 2: Reducir respuestas inventadas

> “Utiliza únicamente la información entregada. Si haces una inferencia, indícalo explícitamente. Si no tienes suficiente información, di ‘No hay suficiente información’.”

### Mejora 3: Mejorar el formato

> “Entrega primero un resumen ejecutivo de máximo tres líneas y luego una tabla con hallazgos y próximos pasos.”

### Mejora 4: Agregar ejemplos

Incluir un ejemplo de:

- Entrada.
- Respuesta esperada.
- Respuesta no deseada.

### Mejora 5: Definir cuándo escalar a una persona

> “Si el caso involucra una queja grave, riesgo legal, datos financieros o una decisión irreversible, recomienda revisión humana.”

### Mejora 6: Ajustar el tono

> “Escribe en español latinoamericano, con un tono claro, cercano y directo. Evita exageraciones, jerga técnica y frases genéricas.”

**Key takeaway**  
> La mejora del asistente es un ciclo: probar, observar, ajustar instrucciones y volver a probar.

**Slide count estimado:** 2 slides

---

## Bloque 10 — Demo relámpago y aprendizajes  
### 02:40–02:55 | 15 minutos

**Objetivo**  
Celebrar avances, compartir aprendizajes y demostrar variedad de aplicaciones.

**Dinámica**

Seleccionar 5–6 participantes para demos de máximo 90 segundos cada uno.

Cada presentación debe responder:

1. ¿Qué tarea resuelve tu asistente?
2. ¿Quién lo utilizaría?
3. ¿Qué entrada recibe?
4. ¿Qué salida entrega?
5. ¿Qué aprendiste al probarlo?

### Alternativa para grupos grandes

En lugar de presentaciones frente a todos:

- Cada mesa elige un asistente.
- Las mesas comparten su mejor aprendizaje.
- El facilitador recoge los patrones en una pizarra.

### Criterio de selección de demos

Priorizar variedad:

- Ventas.
- Marketing.
- Operaciones.
- Investigación.
- Soporte.
- Gestión personal del fundador.

**Key takeaway**  
> El valor no está solamente en crear un asistente, sino en integrarlo en un flujo de trabajo real.

**Slide count estimado:** 2 slides

---

## Bloque 11 — Cierre y próximos pasos  
### 02:55–03:00 | 5 minutos

**Objetivo**  
Convertir el prototipo en una acción concreta después del workshop.

**Dinámica**

Cada participante completa esta frase:

> “Durante los próximos 7 días voy a probar mi asistente con ________, mediré ________ y decidiré ________.”

### Plan de acción recomendado

Durante la siguiente semana:

1. Elegir una tarea real.
2. Usar el asistente al menos cinco veces.
3. Guardar ejemplos buenos y malos.
4. Pedir feedback a una persona del equipo.
5. Mejorar una parte de las instrucciones.
6. Decidir si:
   - Se mantiene como herramienta personal.
   - Se comparte con el equipo.
   - Se conecta a otro flujo.
   - Se descarta porque no generó suficiente valor.

**Key takeaway**  
> El workshop termina hoy, pero el aprendizaje real comienza cuando el asistente se prueba en el trabajo cotidiano.

**Slide count estimado:** 1 slide

---

# 5. Materiales necesarios

## Para preparar antes del workshop

### Herramientas

- Plataforma de presentación.
- Herramienta de IA generativa principal.
- Herramienta alternativa o ruta manual por chat.
- Temporizador visible.
- Código QR con enlaces:
  - Herramienta de IA.
  - Plantilla de diseño.
  - Plantilla de prompt.
  - Formulario de feedback.
  - Recursos para llevar a casa.

### Material impreso

Preparar una carpeta por participante con:

1. Agenda del workshop.
2. Matriz de selección de casos de uso.
3. Ficha de diseño del asistente.
4. Plantilla de instrucciones.
5. Checklist de pruebas.
6. Plan de acción de 7 días.
7. Hoja de notas.
8. Stickers o tarjetas para dinámicas.

### Casos y demos

Preparar con anticipación:

- Un asistente de ejemplo completamente funcional.
- Un caso de uso de ventas.
- Un caso de uso de investigación de clientes.
- Un caso de uso de contenido.
- Tres ejemplos de inputs:
  - Bueno.
  - Incompleto.
  - Confuso.
- Un ejemplo de respuesta problemática para explicar límites.

### Conectividad y equipos

- Wi-Fi estable.
- Contraseña disponible en tarjetas o diapositiva.
- Proyector o pantalla.
- Adaptadores necesarios.
- Tomas eléctricas o extensiones.
- Idealmente, una laptop por persona o por pareja.
- Cargadores y adaptadores extra.

### Equipo humano recomendado

Para 20–30 participantes:

- 1 facilitador principal.
- 1 o 2 asistentes de sala.
- 1 persona responsable de tecnología, si es posible.

## Preparación de los participantes

Enviar 2–3 días antes:

- Recomendación de crear una cuenta en la herramienta seleccionada.
- Instrucción de llevar laptop.
- Recordatorio de cargar la batería.
- Pedido de pensar en tres tareas repetitivas de su startup.
- Advertencia de no llevar datos sensibles de clientes.
- Link a un video opcional de introducción de 5 minutos.

---

# 6. Recomendaciones de facilitación

## Enfoque del facilitador

Mantener el ritmo con la regla:

> “Menos explicación, más construcción.”

Después de cada concepto, hacer que los participantes lo apliquen inmediatamente.

## Frases útiles

- “No buscamos la solución perfecta; buscamos una primera versión útil.”
- “Si tu caso de uso requiere diez integraciones, simplifícalo para el workshop.”
- “La IA es un copiloto, no un piloto automático.”
- “Si el resultado no es bueno, primero revisemos las instrucciones y el contexto.”
- “No compartas información que no entregarías a una persona externa.”
- “Una respuesta segura incluye reconocer lo que no sabe.”

## Qué hacer si alguien no tiene una cuenta o la herramienta falla

Tener una ruta alternativa:

1. Usar un documento compartido con la plantilla de instrucciones.
2. Copiar y pegar el prompt en cualquier chat de IA disponible.
3. Trabajar en parejas.
4. Usar el caso de ejemplo del facilitador.
5. Simular la entrada y salida manualmente para validar el diseño.

---

# 7. Slide deck estimado

| Sección | Slides |
|---|---:|
| Bienvenida y activación | 2 |
| IA aplicada a startups | 3 |
| Selección del caso de uso | 4 |
| Diseño del asistente | 4 |
| Instrucciones efectivas | 3 |
| Pausa | 1 |
| Construcción paso a paso | 5 |
| Pruebas | 3 |
| Mejora e iteración | 2 |
| Demos y aprendizajes | 2 |
| Cierre | 1 |
| **Total estimado** | **30 slides** |

## Principio para las slides

Las diapositivas deben ser visuales y simples:

- Una idea principal por slide.
- Pocos textos largos.
- Capturas de pantalla de la herramienta.
- Ejemplos “antes y después”.
- Timers visibles para los ejercicios.
- Instrucciones paso a paso.

---

# 8. Recursos para llevar a casa

## 1. Plantilla de diseño de asistentes

```text
Nombre del asistente:

Usuario principal:

Problema que resuelve:

Tarea específica:

Entrada que recibe:

Salida que entrega:

Tono:

Información de contexto:

Qué debe hacer:

Qué debe evitar:

Cuándo debe pedir más información:

Cuándo debe escalar a una persona:

¿Cómo mediremos si es útil?
```

## 2. Plantilla de instrucciones

```text
Actúa como [rol] para [tipo de startup o usuario].

Tu objetivo es ayudar a [usuario] a [resultado concreto].

Contexto:
- Nuestra empresa:
- Nuestro cliente:
- Nuestro producto:
- Tono de comunicación:
- Información relevante:

Cuando recibas una solicitud:
1. Analiza la información entregada.
2. Identifica los datos relevantes.
3. Señala cualquier información faltante.
4. Sigue este proceso: [pasos].
5. Entrega el resultado en este formato: [formato].

Reglas:
- No inventes datos.
- Distingue hechos de inferencias.
- Haz preguntas si falta información crítica.
- Mantén un tono [tono].
- Escala a una persona cuando [condiciones].
```

## 3. Checklist de calidad

Antes de usar el asistente, comprobar:

- [ ] Tiene una tarea específica.
- [ ] Tiene un usuario definido.
- [ ] Sabe qué información recibe.
- [ ] Sabe qué formato debe entregar.
- [ ] Tiene ejemplos de respuestas deseadas.
- [ ] Reconoce cuándo no tiene suficiente información.
- [ ] No utiliza datos sensibles innecesarios.
- [ ] Tiene un punto claro de revisión humana.
- [ ] Fue probado con casos normales e imperfectos.
- [ ] Tiene un criterio de éxito medible.

## 4. Framework de pruebas

Probar siempre:

1. Caso normal.
2. Caso incompleto.
3. Caso ambiguo.
4. Caso fuera de alcance.
5. Caso con información contradictoria.

## 5. Plan de experimentación de 7 días

```text
Asistente:

Tarea que voy a probar:

Número de usos durante la semana:

Métrica principal:

Ejemplo de respuesta útil:

Ejemplo de respuesta deficiente:

Feedback de usuarios:

Cambio que implementaré:

Decisión al final de la semana:
[ ] Mantener
[ ] Mejorar
[ ] Compartir con el equipo
[ ] Integrar a otro flujo
[ ] Descartar
```

## 6. Reglas básicas de seguridad

Compartir con los participantes:

- No copiar contraseñas, claves API o credenciales.
- No incluir datos personales de clientes si no es necesario.
- Anonimizar nombres, teléfonos, emails y documentos.
- No subir información legal, financiera o estratégica sensible sin autorización.
- Revisar manualmente las respuestas antes de enviarlas a clientes.
- No utilizar el asistente como sustituto de asesoría legal, médica, financiera o contable.
- Aclarar a los usuarios cuándo están interactuando con IA, si corresponde.

---

# Resultado final esperado

Al terminar las tres horas, cada participante debería contar con:

1. Un problema concreto seleccionado.
2. Una ficha clara de diseño.
3. Un prompt o conjunto de instrucciones reutilizable.
4. Un asistente prototipo funcionando.
5. Tres pruebas realizadas.
6. Al menos una mejora aplicada.
7. Un plan de validación de 7 días.

La promesa del workshop puede resumirse así:

> **No vas a salir sabiendo “todo sobre IA”. Vas a salir con un asistente que ya puedes poner a trabajar en una tarea concreta de tu startup.**