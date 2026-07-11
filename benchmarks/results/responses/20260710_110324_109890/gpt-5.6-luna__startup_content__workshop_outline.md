# GPT-5.6 Luna — startup_content/workshop_outline

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 34.926s | tokens_per_second: 190.7
- input_tokens: 186 | output_tokens: 6661
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que proporciona información práctica y útil para emprendedores no técnicos, aunque podría profundizar un poco más en algunos aspectos.

## Respuesta completa

# Workshop: **Construye tu Asistente de IA para tu Startup – Workshop Práctico**

**Duración:** 3 horas presenciales  
**Audiencia:** Emprendedores early-stage no técnicos  
**Tamaño ideal:** 20–30 personas  
**Formato:** 30% conceptos y demos, 70% práctica  
**Resultado esperado:** Cada participante termina con un prototipo funcional de un asistente de IA, un prompt maestro, una mini base de conocimiento y un plan de aplicación para los próximos 7 días.

---

# 1. Objetivos del workshop

Al finalizar, los participantes podrán:

1. Identificar una tarea repetitiva o crítica de su startup que pueda ser asistida por IA.
2. Diseñar el rol, alcance y personalidad de un asistente.
3. Crear instrucciones efectivas sin necesidad de programar.
4. Alimentar el asistente con información relevante de su negocio.
5. Probarlo con casos reales y mejorar sus respuestas.
6. Definir límites, riesgos y reglas de uso responsable.
7. Salir con un prototipo que puedan seguir usando al día siguiente.

---

# 2. Agenda general — 3 horas

| Tiempo | Bloque | Formato | Resultado |
|---|---|---|---|
| 00:00–00:10 | Bienvenida y activación | Dinámica | Expectativas y reto del día |
| 00:10–00:25 | ¿Qué puede hacer un asistente de IA por tu startup? | Charla + ejemplos | Entender oportunidades concretas |
| 00:25–00:45 | De problema a caso de uso | Ejercicio | Elegir qué asistente construir |
| 00:45–01:00 | Anatomía de un buen asistente | Demo + explicación | Conocer el “blueprint” |
| 01:00–01:10 | Break | — | Pausa |
| 01:10–01:35 | Construye la versión 1 | Ejercicio guiado | Crear instrucciones iniciales |
| 01:35–01:55 | Dale contexto: conocimiento y ejemplos | Demo + práctica | Incorporar información del negocio |
| 01:55–02:15 | Testea, rompe y mejora | Ejercicio | Detectar fallas y corregirlas |
| 02:15–02:35 | Demo en parejas y feedback | Peer review | Mejorar el asistente con feedback |
| 02:35–02:50 | Del prototipo a la operación | Discusión + plan | Definir próximo uso real |
| 02:50–03:00 | Cierre y compromisos | Plenaria | Acción concreta en 7 días |

**Duración total: 180 minutos**

---

# 3. Preparación previa

## Para los participantes

Enviar entre 3 y 5 días antes:

- Traer laptop, idealmente no solo celular.
- Tener acceso a internet.
- Crear una cuenta en al menos una herramienta de IA:
  - ChatGPT
  - Claude
  - Gemini
  - Otra plataforma disponible para asistentes personalizados
- Llegar con un proceso de su startup que:
  - Se repite frecuentemente.
  - Consume tiempo.
  - Requiere responder, analizar, redactar o clasificar información.
- Traer ejemplos no confidenciales de:
  - Preguntas frecuentes de clientes.
  - Mensajes de venta.
  - Descripciones de productos.
  - Documentos internos públicos o ficticios.
  - Políticas o procesos.
- No traer información sensible:
  - Datos personales de clientes.
  - Contraseñas.
  - Información financiera confidencial.
  - Contratos no autorizados.
  - Información médica o legal privada.

## Para el facilitador

Preparar:

### Tecnología

- Proyector o pantalla grande.
- Internet estable.
- Adaptador HDMI/USB-C.
- Extensiones eléctricas y regletas.
- Cronómetro visible.
- Plan B offline en PDF o capturas de pantalla.
- Una cuenta de IA lista para la demo.
- Un asistente previamente configurado como respaldo.

### Material impreso

- Canvas de diseño del asistente.
- Hoja de selección de caso de uso.
- Plantilla de prompt maestro.
- Checklist de testing.
- Hoja de plan de acción de 7 días.
- Stickers o post-its.
- Marcadores.
- Tarjetas con casos de uso sugeridos.

### Preparar antes de la sesión

Crear una demo con un asistente sencillo, por ejemplo:

> **Asistente:** “Nora, asistente de atención al cliente para una startup de delivery saludable.”

Debe poder:

- Responder preguntas frecuentes.
- Usar un tono definido.
- Pedir información faltante.
- Decir “no lo sé” cuando no tenga datos.
- Escalar casos complejos a una persona.
- Crear respuestas listas para enviar.

También preparar tres versiones del mismo caso:

1. Prompt débil.
2. Prompt mejorado.
3. Prompt robusto con contexto, formato y límites.

---

# 4. Ejercicio principal del workshop

## “Construye y prueba tu asistente en 90 minutos”

Cada participante construirá un asistente para una tarea concreta de su startup.

### Casos de uso sugeridos

Para reducir la fricción, ofrecer estas opciones:

- Asistente de respuestas para clientes.
- Asistente de generación de propuestas comerciales.
- Asistente de análisis de feedback.
- Asistente de onboarding de nuevos colaboradores.
- Asistente de creación de contenido.
- Asistente de preparación de reuniones.
- Asistente para priorizar leads.
- Asistente de documentación de procesos.
- Asistente de investigación de mercado.
- Asistente de soporte interno para el equipo.

### Entregables del ejercicio

Cada participante debe terminar con:

1. Nombre del asistente.
2. Problema que resuelve.
3. Usuario principal.
4. Instrucciones del asistente.
5. Contexto o base de conocimiento inicial.
6. Tres ejemplos de conversación.
7. Cinco pruebas realizadas.
8. Dos mejoras aplicadas.
9. Regla de seguridad o escalamiento.
10. Próximo paso de implementación.

---

# 5. Desarrollo detallado por bloques

---

## Bloque 1 — Bienvenida y activación

**Duración:** 10 minutos  
**Horario:** 00:00–00:10  
**Dinámica:** Actividad rápida + encuadre

### Objetivo

Romper el hielo, alinear expectativas y poner a todos en modo práctico desde el primer minuto.

### Dinámica

1. El facilitador presenta el objetivo:
   > “En tres horas no vamos a hablar solamente de IA. Vamos a salir con algo construido y probado.”

2. Pregunta rápida al grupo:
   - ¿Quién ya usa IA semanalmente?
   - ¿Quién la usa solo para escribir textos?
   - ¿Quién siente que pierde tiempo en tareas repetitivas?
   - ¿Quién ya intentó crear un asistente?

3. Actividad de 60 segundos:
   Cada persona completa:
   > “Si tuviera un asistente que me ayudara con una sola cosa esta semana, sería con…”

4. Se comparten 3 o 4 respuestas.

### Key takeaway

> La oportunidad no está en “usar IA porque está de moda”, sino en eliminar fricción de una tarea concreta del negocio.

### Slides estimados

**2 slides**

1. Título y promesa del workshop.
2. Resultado final esperado.

---

## Bloque 2 — ¿Qué puede hacer un asistente de IA por tu startup?

**Duración:** 15 minutos  
**Horario:** 00:10–00:25  
**Dinámica:** Charla breve + ejemplos

### Objetivo

Mostrar posibilidades concretas y aterrizadas para startups early-stage.

### Contenido

Explicar la diferencia entre:

- Usar IA como chat ocasional.
- Usar un prompt repetido.
- Tener un asistente con rol, instrucciones, contexto y criterios definidos.

### Modelo simple

Un asistente útil tiene cinco componentes:

1. **Rol:** ¿Quién es?
2. **Objetivo:** ¿Qué resultado debe producir?
3. **Contexto:** ¿Qué necesita saber?
4. **Proceso:** ¿Cómo debe trabajar?
5. **Límites:** ¿Qué no debe hacer?

### Ejemplos por área

#### Ventas

- Calificar leads.
- Preparar respuestas personalizadas.
- Crear propuestas.
- Preparar reuniones comerciales.

#### Marketing

- Convertir ideas en contenido.
- Adaptar mensajes por segmento.
- Analizar comentarios de clientes.
- Generar variaciones de campañas.

#### Operaciones

- Documentar procesos.
- Crear checklists.
- Resumir reuniones.
- Preparar reportes semanales.

#### Customer success

- Responder preguntas frecuentes.
- Clasificar solicitudes.
- Detectar clientes en riesgo.
- Crear respuestas empáticas.

#### Fundadores

- Preparar decisiones.
- Comparar alternativas.
- Analizar feedback.
- Convertir notas desordenadas en planes de acción.

### Mini demo

Mostrar el mismo pedido a un chat genérico y a un asistente configurado.

**Pedido:**

> “Respóndele a este cliente.”

Luego demostrar que el asistente configurado:

- Pregunta el contexto faltante.
- Usa el tono de la empresa.
- Propone una respuesta.
- Indica cuándo debe escalar a una persona.

### Key takeaway

> Un asistente no es magia. Es un proceso de negocio bien definido, convertido en instrucciones reutilizables.

### Slides estimados

**6 slides**

1. IA como herramienta vs. IA como asistente.
2. Ejemplos de asistentes por área.
3. El modelo de cinco componentes.
4. Antes: chat genérico.
5. Después: asistente contextualizado.
6. Regla de oro: empezar con una tarea específica.

---

## Bloque 3 — De problema a caso de uso

**Duración:** 20 minutos  
**Horario:** 00:25–00:45  
**Dinámica:** Ejercicio individual + discusión en parejas

### Objetivo

Elegir un caso de uso concreto, valioso y suficientemente pequeño para construir durante el workshop.

### Introducción del facilitador

Presentar la fórmula:

> **Tarea repetitiva + información disponible + resultado claro = buen caso de uso para un asistente**

### Hoja de selección de caso de uso

Cada participante responde:

1. ¿Qué tarea repetitiva me quita tiempo?
2. ¿Quién realiza hoy esa tarea?
3. ¿Cuántas veces ocurre por semana?
4. ¿Qué información necesita la persona?
5. ¿Qué resultado debería entregar?
6. ¿Qué pasa si el resultado no es perfecto?
7. ¿Qué tan fácil es revisar el trabajo de la IA?
8. ¿Qué riesgo tendría automatizarlo?

### Criterios de selección

Puntuar del 1 al 5:

- Frecuencia.
- Impacto en el negocio.
- Facilidad de probar.
- Disponibilidad de información.
- Bajo riesgo inicial.

Elegir el caso con mayor puntuación.

### Dinámica en parejas

Cada persona explica su caso en 60 segundos usando:

> “Quiero construir un asistente que ayude a [usuario] a [tarea], usando [información], para producir [resultado].”

La pareja debe hacer una sola pregunta:

> “¿Cómo sabrás que la respuesta del asistente es buena?”

### Key takeaway

> El mejor primer asistente no intenta manejar todo el negocio. Resuelve muy bien una tarea específica y frecuente.

### Slides estimados

**4 slides**

1. Fórmula para encontrar un caso de uso.
2. Ejemplos buenos y malos.
3. Criterios de priorización.
4. Instrucción para el ejercicio.

---

## Bloque 4 — Anatomía de un buen asistente

**Duración:** 15 minutos  
**Horario:** 00:45–01:00  
**Dinámica:** Demo + explicación guiada

### Objetivo

Entregar una estructura simple para que los participantes puedan crear su asistente sin conocimientos técnicos.

### Plantilla “R-O-C-P-L”

Presentar este framework:

### R — Rol

¿Quién es el asistente?

> “Eres un asistente de ventas B2B para una startup de software…”

### O — Objetivo

¿Qué resultado debe producir?

> “Tu objetivo es ayudar a preparar respuestas comerciales claras y personalizadas…”

### C — Contexto

¿Qué necesita saber sobre el negocio?

> “La empresa vende una plataforma de gestión de inventario para comercios medianos…”

### P — Proceso

¿Qué pasos debe seguir?

1. Identificar el tipo de cliente.
2. Detectar la necesidad principal.
3. Hacer preguntas si falta información.
4. Proponer una respuesta.
5. Incluir siguiente paso recomendado.

### L — Límites

¿Qué no debe hacer?

- No inventar precios.
- No prometer funcionalidades.
- No entregar información confidencial.
- Escalar reclamos legales o financieros.
- Decir explícitamente cuando no tiene suficiente información.

### Formato de salida

También mostrar cómo pedir una estructura:

> “Entrega tu respuesta con este formato:  
> 1. Diagnóstico  
> 2. Respuesta sugerida  
> 3. Pregunta pendiente  
> 4. Próximo paso”

### Key takeaway

> Los prompts efectivos no son frases mágicas: son instrucciones claras, contexto relevante, pasos de trabajo y criterios de calidad.

### Slides estimados

**6 slides**

1. La anatomía del asistente.
2. Rol.
3. Objetivo y contexto.
4. Proceso paso a paso.
5. Límites y seguridad.
6. Formato de salida.

---

## Break

**Duración:** 10 minutos  
**Horario:** 01:00–01:10

Durante la pausa, proyectar una slide con la instrucción:

> “Vuelve con la tarea que elegiste y al menos tres ejemplos reales o ficticios de entradas que el asistente debería poder manejar.”

---

## Bloque 5 — Construye la versión 1

**Duración:** 25 minutos  
**Horario:** 01:10–01:35  
**Dinámica:** Ejercicio guiado paso a paso

### Objetivo

Crear la primera versión del asistente utilizando la plantilla R-O-C-P-L.

### Instrucción

Los participantes pueden trabajar en:

- Un asistente personalizado dentro de su herramienta de IA.
- Un proyecto o espacio de trabajo.
- Un chat nuevo utilizando el prompt maestro.

El facilitador debe aclarar:

> “No queremos una versión perfecta. Queremos una versión suficientemente buena para probarla.”

### Plantilla de construcción

Copiar y completar:

```text
NOMBRE DEL ASISTENTE:
[Nombre claro y memorable]

ROL:
Eres [tipo de especialista] para [tipo de startup o negocio].

OBJETIVO:
Tu objetivo principal es ayudar a [usuario] a [tarea o resultado].

CONTEXTO DEL NEGOCIO:
- Qué vendemos:
- A quién:
- Problema que resolvemos:
- Diferenciadores:
- Información importante:

PROCESO DE TRABAJO:
Cada vez que recibas una solicitud:
1. ...
2. ...
3. ...
4. ...

FORMATO DE RESPUESTA:
Entrega tus respuestas usando esta estructura:
- ...
- ...
- ...

TONO:
Sé [claro, directo, cálido, profesional, persuasivo, etc.].
Evita [jerga, exageraciones, respuestas demasiado largas, etc.].

LÍMITES:
- No inventes información.
- Si falta información, pregunta antes de responder.
- No prometas lo que no esté confirmado.
- Escala a una persona cuando [condición].

CRITERIO DE CALIDAD:
Una buena respuesta debe ser:
- ...
- ...
- ...
```

### Rol del facilitador

Circular por la sala y revisar especialmente:

- Que el objetivo sea específico.
- Que el proceso tenga pasos observables.
- Que los límites sean realistas.
- Que no intenten resolver cinco problemas a la vez.

### Key takeaway

> La primera versión debe ser simple, editable y testeable. La mejora viene después de observar cómo responde.

### Slides estimados

**3 slides**

1. Instrucción del ejercicio.
2. Plantilla R-O-C-P-L.
3. Checklist de versión 1.

---

## Bloque 6 — Dale contexto: conocimiento y ejemplos

**Duración:** 20 minutos  
**Horario:** 01:35–01:55  
**Dinámica:** Demo + práctica individual

### Objetivo

Aprender a darle al asistente información útil sin sobrecargarlo ni incluir datos sensibles.

### Contenido

Explicar tres formas de aportar contexto:

#### 1. Información fija

- Descripción del negocio.
- Productos y servicios.
- Público objetivo.
- Tono de comunicación.
- Políticas.
- Preguntas frecuentes.

#### 2. Información variable

- Mensaje actual del cliente.
- Detalles de una oportunidad.
- Notas de una reunión.
- Datos de una campaña.
- Comentarios recientes.

#### 3. Ejemplos

Mostrar al asistente ejemplos de:

- Entrada.
- Razonamiento esperado, sin pedir cadenas internas de pensamiento.
- Formato de respuesta.
- Respuesta correcta.
- Respuesta que debe evitar.

### Ejercicio

Cada participante incorpora:

- 5 datos relevantes de su negocio.
- 3 preguntas frecuentes.
- 2 ejemplos de buena respuesta.
- 1 ejemplo de respuesta incorrecta o peligrosa.

### Recomendación de estructura

Separar la información así:

```text
INFORMACIÓN DEL NEGOCIO
...

PREGUNTAS FRECUENTES
Pregunta:
Respuesta:

EJEMPLOS DE RESPUESTAS
Caso:
Respuesta ideal:

RESPUESTAS A EVITAR
...
```

### Advertencia práctica

No cargar documentos “por si acaso”. El contexto debe ser:

- Relevante.
- Actualizado.
- Fácil de revisar.
- Autorizado para compartir.
- Entendible para el asistente.

### Key takeaway

> Un asistente mejora más con contexto relevante y buenos ejemplos que con instrucciones interminables.

### Slides estimados

**5 slides**

1. La importancia del contexto.
2. Información fija vs. variable.
3. Ejemplos de entrada y salida.
4. Qué información no cargar.
5. Actividad de enriquecimiento.

---

## Bloque 7 — Testea, rompe y mejora

**Duración:** 20 minutos  
**Horario:** 01:55–02:15  
**Dinámica:** Ejercicio individual guiado

### Objetivo

Probar el asistente con situaciones reales y detectar dónde falla.

### Método de testing: “5 pruebas”

Cada participante debe probar:

#### Prueba 1: Caso normal

Una solicitud frecuente y sencilla.

#### Prueba 2: Caso incompleto

La solicitud no tiene todos los datos necesarios.

#### Prueba 3: Caso ambiguo

El mensaje puede interpretarse de distintas maneras.

#### Prueba 4: Caso fuera de alcance

El usuario pide algo que el asistente no debería hacer.

#### Prueba 5: Caso difícil

Un cliente molesto, un pedido urgente o una situación con tensión.

### Tabla de evaluación

| Prueba | ¿Respondió correctamente? | ¿Qué faltó? | ¿Qué instrucción cambiaré? |
|---|---|---|---|
| Caso normal | Sí / No |  |  |
| Caso incompleto | Sí / No |  |  |
| Caso ambiguo | Sí / No |  |  |
| Fuera de alcance | Sí / No |  |  |
| Caso difícil | Sí / No |  |  |

### Preguntas para mejorar

- ¿Inventó información?
- ¿Fue demasiado largo?
- ¿No hizo preguntas cuando debía?
- ¿Usó un tono incorrecto?
- ¿Entregó la respuesta en el formato solicitado?
- ¿Supo decir “no lo sé”?
- ¿Escaló correctamente un caso sensible?

### Key takeaway

> Testear no es buscar que la IA diga “algo bonito”; es verificar si produce un resultado confiable para el negocio.

### Slides estimados

**4 slides**

1. Por qué hay que testear.
2. Las cinco pruebas.
3. Tabla de evaluación.
4. Ejemplos de errores frecuentes.

---

## Bloque 8 — Demo en parejas y feedback

**Duración:** 20 minutos  
**Horario:** 02:15–02:35  
**Dinámica:** Peer review + demostración rápida

### Objetivo

Obtener feedback externo y comprobar si el asistente es entendible para alguien que no lo diseñó.

### Dinámica

Formar parejas. Cada participante tiene:

- 4 minutos para mostrar su asistente.
- 3 minutos para que la pareja lo pruebe.
- 3 minutos para entregar feedback.

Luego cambian roles.

### La pareja debe probar tres cosas

1. Hacer una solicitud normal.
2. Hacer una solicitud incompleta.
3. Hacer una solicitud que esté fuera del alcance.

### Feedback con formato “Más / Menos / Próximo”

- **Más:** ¿Qué debería hacer más?
- **Menos:** ¿Qué debería evitar?
- **Próximo:** ¿Cuál sería la mejora más importante?

### Criterios de feedback

La pareja evalúa del 1 al 5:

- Claridad del objetivo.
- Utilidad de la respuesta.
- Consistencia del tono.
- Calidad de las preguntas.
- Manejo de límites.
- Facilidad de uso.

### Mini demos voluntarias

Invitar a 2 o 3 personas a mostrar:

- El problema elegido.
- Una respuesta del asistente.
- Una mejora aplicada.

### Key takeaway

> Si otra persona puede usar tu asistente sin que tengas que explicarlo durante 10 minutos, vas por buen camino.

### Slides estimados

**3 slides**

1. Instrucciones de la dinámica.
2. Guía de pruebas.
3. Formato de feedback.

---

## Bloque 9 — Del prototipo a la operación

**Duración:** 15 minutos  
**Horario:** 02:35–02:50  
**Dinámica:** Reflexión + plan individual

### Objetivo

Convertir el prototipo en una herramienta que pueda usarse realmente en la startup.

### Ejercicio: Plan de acción de 7 días

Cada participante completa:

### Día 1

¿Con quién probaré el asistente?

### Día 2

¿Qué tres casos reales usaré?

### Día 3

¿Qué respuestas revisaré con una persona del equipo?

### Día 4

¿Qué error o patrón quiero corregir?

### Día 5

¿Qué documento o información autorizada agregaré?

### Día 6

¿Cómo mediré si ayuda?

### Día 7

¿Decidiré mantenerlo, modificarlo o descartarlo?

### Métricas simples

No hace falta comenzar con métricas sofisticadas. Pueden medir:

- Tiempo ahorrado.
- Número de tareas asistidas.
- Porcentaje de respuestas reutilizables.
- Errores detectados.
- Nivel de satisfacción del equipo.
- Tiempo desde solicitud hasta respuesta.
- Número de escalaciones correctas.

### Discusión plenaria

Preguntar:

- ¿Qué tarea probarán primero?
- ¿Qué riesgo deben controlar?
- ¿Quién será responsable de mantener actualizado el asistente?

### Key takeaway

> Un asistente se vuelve valioso cuando entra en un flujo de trabajo real, tiene un dueño y se mejora con uso.

### Slides estimados

**4 slides**

1. Del prototipo al proceso.
2. Plan de acción de 7 días.
3. Métricas simples.
4. La importancia de tener un responsable.

---

## Bloque 10 — Cierre y compromisos

**Duración:** 10 minutos  
**Horario:** 02:50–03:00  
**Dinámica:** Plenaria + compromiso final

### Objetivo

Consolidar aprendizajes y cerrar con una acción concreta.

### Dinámica

Cada participante completa en una tarjeta:

> “Durante los próximos 7 días voy a usar mi asistente para ______ y mediré ______.”

Se pueden recoger las tarjetas o pedir que las fotografíen.

### Recapitulación

Recordar los cinco principios:

1. Empieza por una tarea concreta.
2. Define claramente el resultado esperado.
3. Agrega contexto relevante.
4. Prueba con casos normales y difíciles.
5. Mantén supervisión humana en decisiones importantes.

### Cierre del facilitador

> “No se trata de reemplazar al equipo. Se trata de quitar trabajo repetitivo para que el equipo pueda enfocarse en pensar, vender, crear y atender mejor.”

### Key takeaway

> El primer asistente no tiene que ser perfecto. Tiene que ser útil, seguro y usado.

### Slides estimados

**3 slides**

1. Cinco aprendizajes principales.
2. Compromiso de 7 días.
3. Recursos y próximos pasos.

---

# 6. Slide count estimado total

| Sección | Slides |
|---|---:|
| Bienvenida | 2 |
| Oportunidades de IA | 6 |
| Selección de caso de uso | 4 |
| Anatomía del asistente | 6 |
| Construcción versión 1 | 3 |
| Contexto y ejemplos | 5 |
| Testing | 4 |
| Peer review | 3 |
| Implementación | 4 |
| Cierre | 3 |
| **Total estimado** | **40 slides** |

## Recomendación

Mantener las slides visuales y usar las plantillas impresas para el trabajo detallado. Evitar slides con párrafos largos. La presentación debe marcar el ritmo, no convertirse en el workshop.

---

# 7. Recursos para llevar a casa

## A. Plantilla de prompt maestro

```text
Eres [ROL] para [TIPO DE NEGOCIO].

Tu objetivo es [RESULTADO PRINCIPAL].

Debes ayudar a [USUARIO] a [TAREA].

Contexto del negocio:
- [Dato 1]
- [Dato 2]
- [Dato 3]

Cuando recibas una solicitud:
1. [Paso 1]
2. [Paso 2]
3. [Paso 3]
4. [Paso 4]

Antes de responder:
- Verifica si tienes suficiente información.
- Si falta información importante, haz una pregunta.
- No inventes datos.
- Indica los supuestos que estés haciendo.

Responde con este formato:
1. [Sección 1]
2. [Sección 2]
3. [Sección 3]

Usa un tono [TONO].
Evita [COMPORTAMIENTOS A EVITAR].

No debes:
- [Límite 1]
- [Límite 2]
- [Límite 3]

Escala a una persona cuando:
- [Condición 1]
- [Condición 2]

Una respuesta de calidad debe ser:
- [Criterio 1]
- [Criterio 2]
- [Criterio 3]
```

## B. Checklist de calidad

Antes de usar el asistente en producción, verificar:

- ¿Tiene un objetivo específico?
- ¿Está claro quién lo usará?
- ¿Conoce suficientemente el negocio?
- ¿Tiene instrucciones paso a paso?
- ¿Hace preguntas cuando falta información?
- ¿Evita inventar datos?
- ¿Tiene límites definidos?
- ¿Sabe cuándo escalar?
- ¿Entrega respuestas en un formato útil?
- ¿Fue probado con casos reales?
- ¿Hay una persona responsable de actualizarlo?

## C. Biblioteca inicial de prompts

### Para mejorar una respuesta

> “Revisa tu respuesta usando estos criterios: claridad, precisión, tono y utilidad. Indica qué cambiarías y entrega una nueva versión.”

### Para hacer preguntas primero

> “Antes de responder, identifica hasta tres datos que necesitas conocer. Si no son indispensables, continúa usando supuestos explícitos.”

### Para resumir

> “Resume la siguiente información en cinco bullets. Separa hechos, decisiones, pendientes y riesgos.”

### Para convertir información en acción

> “Convierte estas notas en un plan de acción con responsables, fechas, dependencias y próximos pasos.”

### Para desafiar una idea

> “Analiza esta idea como un asesor crítico. Identifica supuestos, riesgos, señales de validación y el experimento más barato para probarla.”

### Para adaptar tono

> “Reescribe este mensaje en un tono claro, humano y profesional. Mantén la intención original, elimina jerga y usa frases cortas.”

## D. Guía de seguridad y uso responsable

Compartir como regla práctica:

- No ingresar información sensible sin autorización.
- Revisar todas las respuestas antes de enviarlas a clientes.
- No utilizar IA como única fuente para decisiones legales, médicas o financieras.
- Mantener actualizada la información del asistente.
- Informar al equipo cuándo y cómo debe usarse.
- Definir qué decisiones siempre requieren revisión humana.
- Guardar ejemplos de errores para mejorar las instrucciones.

---

# 8. Recomendaciones de facilitación

## Para mantener la energía

- Evitar exposiciones de más de 10 minutos seguidos.
- Hacer que todos escriban o prueben algo en cada bloque.
- Circular constantemente por la sala.
- Celebrar prototipos imperfectos.
- Usar ejemplos latinoamericanos y lenguaje de negocio cotidiano.
- Repetir: “No busques perfección; busca una primera versión útil”.
- Hacer visibles los tiempos con un cronómetro.

## Para manejar diferentes niveles de experiencia

### Participantes principiantes

Entregar casos de uso predefinidos y usar la plantilla paso a paso.

### Participantes más avanzados

Invitarlos a trabajar en:

- Múltiples tipos de usuarios.
- Flujos con clasificación.
- Diferentes formatos de salida.
- Métricas de calidad.
- Integración futura con herramientas de trabajo.

## Para evitar bloqueos técnicos

Tener siempre tres caminos:

1. Asistente personalizado en una plataforma de IA.
2. Chat nuevo con el prompt maestro.
3. Simulación manual con la plantilla impresa.

El objetivo del workshop es aprender a diseñar y probar un asistente, no perder tiempo resolviendo configuraciones técnicas específicas.