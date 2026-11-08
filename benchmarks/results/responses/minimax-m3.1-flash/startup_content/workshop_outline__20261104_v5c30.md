# MiniMax M3.1 Flash — startup_content/workshop_outline

- model_id: `minimax/minimax-m3.1-flash`
- success: True  | final: 7.91 | quality: 8.84
- latency_total: 84.924s | tokens_per_second: 187.6
- input_tokens: 367 | output_tokens: 15929
- judge_score: 4.6 | justificación: 

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

# Outline completo: **“Construye tu Asistente de IA para tu Startup — Workshop Práctico”**

## 1. Enfoque general del workshop

**Formato:** sprint práctico de construcción, no una clase teórica.  
**Duración:** 3 horas, incluida una pausa de 10 minutos.  
**Modalidad:** presencial, en mesas de 4–6 personas.  
**Nivel:**，多次實驗，結論如下。

Cada participante construirá un **asistente de IA funcional para un caso real o simulado de su startup**, sin programación.

### Resultado tangible

Al finalizar, cada participante tendrá:

1. **Un caso de uso priorizado** para su startup.
2. **Un prompt maestro o asistente publicable**, con rol, contexto, tono, reglas y formato de respuesta.
3. **Una base de conocimiento inicial** con preguntas frecuentes e información de la empresa.
4. **Al menos cinco casos de prueba**, resultados y correcciones.
5. **Un flujo simple de implementación**: dónde entra la consulta, qué hace el asistente y cuándo interviene una persona.
6. **Un plan de acción de siete días** para probarlo con usuarios reales.

### Regla de accesibilidad

- No se requiere saber programar.
- No se requiere usar APIs.
- No es obligatorio contratar planes premium.
- El entregable mínimo es un **prompt maestro guardado y reutilizable**.
- Si la plataforma disponible permite publicar el asistente o conectarlo a otra herramienta, esa integración se realiza como opción avanzada.

---

# 2. Agenda detallada

| Horario | Duración | Bloque | Modalidad principal | Entregable |
|---|---:|---|---|---|
| 00:00–00:10 | 10 min | **Arranque: ¿qué vas a construir hoy?** | Bienvenida, dinámica, poll | Expectativas y objetivos claros |
| 00:10–00:25 | 15 min | **Dónde la IA puede ahorrarte tiempo** | Charla corta, ejemplos, discusión | Lista de casos de uso potenciales |
| 00:25–00:45 | 20 min | **Demo en vivo: de una tarea repetitiva a un asistente** | Demo en vivo | Modelo mental del proceso |
| 00:45–01:05 | 20 min | **Ejercicio 1: define tu caso de uso** | Ejercicio individual y en parejas | Lienzo de caso de uso |
| 01:05–01:15 | 10 min | **Pausa y conexión** | Descanso, networking opcional | Una idea aplicada a otro negocio |
| 01:15–01:30 | 15 min | **Demo: contexto, límites y pruebas** | Demo y comparación | Criterios para un asistente confiable |
| 01:30–02:10 | 40 min | **Ejercicio 2: construye y prueba tu asistente** | Construcción, testing en parejas | Asistente MVP y registro de pruebas |
| 02:10–02:25 | 15 min | **Demo: convierte el asistente en un sistema** | Demo de flujo no-code | Mapa de implementación |
| 02:25–02:45 | 20 min | **Ejercicio 3: diseña tu primer despliegue** | Ejercicio individual y en mesa | Flujo, escalamiento y plan piloto |
| 02:45–03:00 | 15 min | **Compromiso, showcase y cierre** | Showcase, plan, feedback | Compromiso de siete días |
| **Total** | **180 min** |  |  |  |

---

# 3. Diseño detallado por bloque

## Bloque 1. Arranque: ¿qué vas a construir hoy?

**Duración:** 10 minutos

### Objetivo

- Generar energía y expectativa.
- Explicar claramente que la sesión termina con un prototipo funcional.
- Identificar las necesidades de la audiencia mediante un poll rápido.

### Dinámica

- **2 min:** bienvenida y promesa del workshop.
- **3 min:** poll en Mentimeter, Google Forms o/show of hands:
  - “¿Qué tarea repetitiva te consume más tiempo?”
  - “¿Qué te gustaría que un asistente resolviera?”
- **3 min:** presentación de los seis entregables finales.
- **2 min:** reglas de trabajo:
  - Una persona trabaja; las parejas retroalimentan.
  - No se suben datos reales ni sensibles.
  - Se prioriza working prototype sobre perfección.
  - Todo se documenta con ejemplos sencillos.

### Key takeaway

> **Hoy no vas a aprender teoría: vas a construir, probar y salir con una primera versión que puedas usar.**

---

## Bloque 2. Dónde la IA puede ahorrarte tiempo

**Duración:** 15 minutos

### Objetivo

Ayudar a los participantes a distinguir una buena oportunidad de automatización de una tarea que todavía no vale la pena automatizar.

### Dinámica

- **5 min:** explicación simple:
  - Un asistente combina **rol + información + instrucciones + límites + capacidad de escalar**.
  - No es “un empleado digital que decide todo”.
- **6 min:** ejemplosHat öğretmen:
  - Ventas: primera respuesta y precalificación de prospectos.
  - Soporte: respuesta a preguntas frecuentes.
  - Operaciones: resumen de reuniones y siguiente acción.
  - Marketing: adaptación de mensajes por segmento.
- **4 min:** discusión en mesa:
  - ¿Qué tareas se repiten?
  - ¿Cuáles tienen respuestas claras?
  - ¿Cuáles dependen demasiado del criterio humano?

### Filtros para un buen primer caso

1. Se repite frecuentemente.
2. Consume tiempo o respuestas之间的 cost.
3. Tiene entradas y salidas claras.
4. Puede apoyarse en información de la empresa.
5. Permite revisión humana antes de generar un impacto importante.

### Key takeaway

> **Empieza por una tarea repetitiva y bien definida, no por “usar IA para todo”.**

---

## Bloque 3. Demo en vivo: de una tarea repetitiva a un asistente

**Duración:** 20 minutos

### Objetivo

Mostrar el proceso completo de construcción y que los participantes entiendan que un asistente se diseña y mejora, no se “invoca y queda listo”.

### Dinámica

La demo utilize un caso ficticio: **TurnoFácil**, una app de reservas para pequeños negocios de servicios.

**Flujo de la demo:**

1. **2 min:** contexto del negocio y problema a resolver.
2. **3 min:** definition del asistente:
   - Recibe una consulta de un prospecto.
   - Explica el servicio.
   - Hace hasta tres preguntas.
   - Recopila los datos necessários.
   - Entrega un resumen y escala al equipo.
3. **5 min:** construcción de las instrucciones maestros:
   - Identidad.
   - Objetivo.
   - Contexto.
   - Proceso.
   - Tono.
   - Reglas.
   - Formato de salida.
4. **5 min:** prueba con una consulta real simulada.
5. **3 min:** muestran una respuesta mejorada después de agregar reglas y preguntas frecuentes.
6. **2 min:** explanation del valor y del criteria de éxito.

El facilitador debe mostrar también **un error deliberado**: una respuesta demasiado genérica, demasiado larga o que promete algo que no está en la base de conocimiento.

### Key takeaway

> **Un buen asistente no depende solo del modelo: depende de buenas instrucciones, contexto y límites.**

---

## Bloque 4. Ejercicio 1: define tu caso de uso

**Duración:** 20 minutos

### Objetivo

Que cada participante elija un caso concreto, defina su resultado esperado y establezca una métrica de éxito.

### Dinámica

- **12 min individual:** completar el **Lienzo de Caso de Uso**.
- **5 min en parejas:** cada persona presenta su caso y recibe feedback.
- **3 min de cierre:** dos o tres ejemplos comentados desde el 组.

### Lienzo de Caso de Uso

1. **Tarea que quiero resolver**
2. **Quién la utiliza**
3. **Cómo llega la solicitud**
4. **Información disponible**
5. **Respuesta o resultado esperado**
6. **Qué decisiones no puede tomar el asistente**
7. **Cuándo debe intervenir una persona**
8. **Cómo sabré que funciona**

### Criterio de selección

Cada persona califica sus ideas de 1 a 5 en:

- Impacto.
- Frecuencia.
- Facilidad.
- Riesgo.

Se recomienda elegir el caso con **alto impacto, alta frecuencia y bajo riesgo de implementación**.

### Key takeaway

> **Si no puedes describir la entrada, la salida y el escalamiento humano, todavía no tienes un caso de uso suficientemente claro.**

---

## Bloque 5. Pausa y conexión

**Duración:** 10 minutos

### Objetivo

- Permitir descanso yreset.
- Generar una conversación de trabajo.

### Dinámica

- Música o sonido ambiental.
- Opcionalmente, una pregunta para compartir:
  - “¿Qué tarea repetitiva tiene el negocio de la persona a tu lado?”
- El facilitador toma una foto de las ideas visibles, sin datos personales.

### Key takeaway

> **Una buena conversación de peers puede desbloque ideas que ningún tutorial resuelve.**

---

## Bloque 6. Demo: contexto, límites y pruebas

**Duración:** 15 minutos

### Objetivo

Mostrar cómo convertir un prototipo “interesante” en un asistente más confiable y preparado para interacted con clientes.

### Dinámica

- **3 min:** agregar contexto y base de conocimiento.
- **3 min:** definir límites:
  - No inventar precios.
  - No prometer fechas.
  - No solicitar información sensible.
  - No tomar decisiones comerciales sin aprobación.
- **3 min:** designing de la escalamiento humano.
- **4 min:** demonstration de cinco escenarios de prueba.
- **2 min:** comparación entre respuesta inicial y respuesta corregida.

### Cinco pruebas esenciales

1. Consulta completa y典型.
2. Consulta con información incompleta.
3. Pregunta fuera del alcance del asistente.
4. Solicitud que contradice las políticas de la empresa.
5. Consulta que debe ser escalada a una persona.

### Key takeaway

> **La calidad no se demuestra con una respuesta bonita, sino con cómo se comporta cuando la información falta o la pregunta se sale del剧本.**

---

## Bloque 7. Ejercicio 2: construye y prueba tu asistente

**Duración:** 40 minutos

### Objetivo

Construir, probar y mejorar una primera versión funcional del asistente.

### Dinámica

- **3 min:** explicación del reto y distribución de la guía.
- **7 min:** escribir identidad, objetivo, contexto, tono y formato.
- **8 min:** redactar el proceso y las reglas.
- **5 min:** agregar tres a cinco preguntas frecuentes o fuentes de verdad.
- **10 min:** realizar al menos cinco pruebas.
- **5 min:** corregir el prompt y repetir las pruebas fallidas.
- **2 min:** guardar el prompt o publicar el asistente si la plataforma lo permite.

En este bloque, el facilitador circula mesa por mesa con una lista de control:

- ¿El asistente sabe quién es?
- ¿Sabe para quién trabaja?
- ¿Tiene un objetivo claro?
- ¿Pide solo la información necesaria?
- ¿Evita inventar información?
- ¿Tiene reglas de escalamiento?
- ¿Entrega la respuesta en el formato esperado?

### Key takeaway

> **Iterar con casos concretos es más rápido y más efectivo que escribir un prompt perfecto a la primera.**

---

## Bloque 8. Demo: convierte el asistente en un sistema

**Duración:** 15 minutos

### Objetivo

Mostrar dónde vive el asistente dentro de las operaciones reales de la startup y por qué siempre debe existir un punto de control humano.

### Dinámica

La demo presenta el flujo:

**Canal de entrada → Asistente → Resultado → Revisión humana → Registro → Mejora**

### Ejemplos

- Formulario web → asistente → respuesta + fila en CRM.
- Correo o WhatsApp → asistente → respuesta FAQ + escalamiento.
- Documento → asistente → resumen y tareas pendientes.
- Formulario → hoja de cálculo → asistente → tabla de seguimiento.

La demo core se realiza primero sobre papel o una herramienta visual. Después se muestra, si es posible, una integración real con una plataforma no-code.

### Niveles de despliegue

1. **Manual:** copiar y pegar respuestas; ideal para validar.
2. **Semi-automático:** formulario + automatización + hoja de cálculo.
3. **Publicado:** asistente disponible en un enlace o canal.
4. **Avanzado:** conectado con CRM, mensajería o sistema interno.

### Key takeaway

> **El asistente debe vivir dentro de un flujo de trabajo y dejar trazabilidad; no basta con que “responda bien” en un chat.**

---

## Bloque 9. Ejercicio 3: diseña tu primer despliegue

**Duración:** 20 minutos

### Objetivo

Diseñar un despliegue seguro, pequeño y medible para los próximos siete días.

### Dinámica

- **4 min:** elegir canal y flujo.
- **6 min:** completar el **Lienzo de Flujo**.
- **5 min:** configurar una simulación del flujo y registrar una interacción.
- **3 min:** definir qué se medirá.
- **2 min:** escribir el primer paso y las condiciones de escalamiento.

### Lienzo de Flujo

1. **Evento que inicia el flujo**
2. **Canal de entrada**
3. **Información enviada al asistente**
4. **Resultado generado**
5. **Revisión humana**
6. **Acción siguiente**
7. **Dónde se registra**
8. **Cuándo escalar**
9. **Métrica de éxito**
10. **Riesgo principal**

### Opciones de despliegue

- **Opción A — Piloto manual:** el fundador usa el asistente para responder cinco consultas simuladas o reales controladas.
- **Opción B — Semi-automatización:** formulario + asistente + hoja de seguimiento.
- **Opción C — Publicación:** asistente accesible para clientes o equipo.
- **Opción D — Integración:** conexión con CRM, WhatsApp Business, correo u otra herramienta.

Todos los participantes completan, como mínimo, la opción A.

### Key takeaway

> **El primer despliegue debe ser pequeño, observable y reversible; validar antes de automatizar por completo.**

---

## Bloque 10. Compromiso, showcase y cierre

**Duración:** 15 minutos

### Objetivo

Cerrar con una decisión concreta,peer feedback y recursos para continuar.

### Dinámica

- **5 min:** showcase relámpago:
  - Dos o tres participantes muestran su asistente.
  - El resto puede compartir capturas mediante una pizarra o enlace.
- **5 min:** cada participante completa su **Plan de 7 días**.
- **3 min:** entrega de recursos y acceso al buzón/community.
- **2 min:** encuesta de satisfacción y feedback.

### Plan de siete días

- **Día 1:** escribir y guardar el prompt final.
- **Día 2:** agregar cinco casos más de prueba.
- **Día 3:** definir el canal de entrada.
- **Día 4:** preparar la escalamiento humano.
- **Día 5:** realizar cinco simulaciones.
- **Día 6:** revisar resultados y corregir.
- **Día 7:** poner en marcha el piloto y medir.

### Key takeaway

> **El workshop termina cuando el asistente sale de la mesa y entra en una prueba real.**

---

# 4. Ejercicio principal del workshop

## Reto central: **“Construye tu Asistente MVP de Respuesta y Escalamiento”**

### ¿Qué construyen?

Cada participante construye un asistente para uno de estos casos:

### Track A — Ventas y prospectos — recomendado

El asistente:

- Responde una primera consulta.
- Explica la propuesta de valor.
- Hace hasta tres preguntas.
- Califica al prospecto.
- Entrega un resumen para el equipo.

### Track B — Soporte al cliente

El asistente:

- Responde preguntas frecuentes.
- Solicita los datos necesarios.
- Detecta cuándo el caso requiere una persona.
- Entrega un resumen del ticket.

### Track C — Operaciones internas

El asistente:

- Convierte notas o mensajes en tareas.
- Clasifica el tipo de solicitud.
- Identifica responsables y fechas sugeridas.
- Escala casos ambiguos.

Si el participante no tiene un caso definido, puede usar el caso ficticio **TurnoFácil**.

---

## Reglas del ejercicio

- Cada persona construye su propio asistente.
- Las parejas solo retroalimentan; no se trabaja “en lugar de” otro.
- Se utilizan datos ficticios o anonimizados.
- No es necesario publicar el asistente.
- No se busca una respuesta perfecta: se busca una versión que pueda probarse.

---

## Plantilla de prompt maestro

Los participantes pueden copiar y completar esta estructura:

```text
IDENTIDAD
Eres [nombre del asistente], el asistente de [empresa].

OBJETIVO
Tu función principal es [resolver esta tarea].
Tu prioridad es [objetivo comercial o operativo].

CONTEXTO
Nuestra empresa ofrece [producto/servicio].
Nuestro cliente ideal es [cliente].
La consulta suele llegar por [canal].
El proceso comercial o operativo es [descripción breve].

BASE DE CONOCIMIENTO
- [pregunta frecuente + respuesta]
- [pregunta frecuente + respuesta]
- [pregunta frecuente + respuesta]
- [condición comercial o regla importante]

PROCESO
1. Saluda de forma breve.
2. Identifica la intención principal.
3. Haz como máximo tres preguntas, una a una, solo si son necesarias.
4. Entrega la respuesta disponible según la base de conocimiento.
5. Resume la necesidad y los datos collected.
6. Indica el siguiente paso.

TONO
Habla en español claro, cercano y profesional.
Usa frases breves. Evita tecnicismos.

REGLAS
- Usa únicamente la información proporcionada.
- No inventes precios, fechas, políticas o garantías.
- Si no sabes algo, dilo y ofrece escalar a una persona.
- No prometas resultados que no estén respaldados.
- No solicites datos sensibles que no sean necesarios.
- Si el cliente solicita una decisión comercial, déjala pendiente de aprobación humana.

ESCALAMIENTO
Escala a [persona/equipo] cuando:
- [condición 1]
- [condición 2]
- [condición 3]

FORMATO DE SALIDA
Cuando el caso requiera escalamiento, entrega:
- Resumen:
- Necesidad:
- Datos faltantes:
- Clasificación:
- Siguiente paso:
```

---

## Casos de prueba

Cada participante prueba, como mínimo:

1. **Caso típico:** información completa.
2. **Caso con vacío:** falta un dato importante.
3. **Caso fuera de alcance:** la pregunta no corresponde al servicio.
4. **Caso de límite:** el cliente pide una garantía o precio no documentado.
5. **Caso ambiguo:** existen varias interpretaciones.

### Evaluación rápida

Cada respuesta recibe 0 o 1 punto en cada criterio:

- Sigue el rol del asistente.
- Hace preguntas relevantes.
- No inventa información.
- Usa la base de conocimiento.
- Escala cuando corresponde.
- Respeta el formato solicitado.

**Criterio de aprobación:** al menos 4 de 6 puntos en cada prueba.

### Entregables del ejercicio

- Lienzo de caso de uso.
- Prompt maestro completo.
- Tres a cinco entradas de base de conocimiento.
- Registro de cinco pruebas.
- Versión corregida del prompt.
- Opcionalmente, enlace al asistente publicado.

---

# 5. Materiales necesarios y preparación

## 5.1 Materiales para los participantes

### Equipos

- Laptop o tablet por participante; el teléfono es plan de respaldo.
- Cargador y cable de carga.
- Cuenta en una herramienta conversacional de IA:
  - ChatGPT.
  - Gemini.
  - Claude.
  - Otra alternativa disponible en el país.
- Navegador actualizado.
- Documento con información básica del startup:
  - Nombre.
  - Problema que resuelve.
  - Cliente ideal.
  - Propuesta de valor.
  - Precios o planes, si pueden compartirse.
  - Tres preguntas frecuentes.
  - Tres reglas comerciales.

### Kit digital

- Guía imprimible o digital del workshop.
- Lienzo de caso de uso.
- Plantilla de prompt maestro.
- Plantilla de base de conocimiento.
- Hoja de pruebas.
- Checklist de guardarraíles.
- Lienzo de flujo.
- Plan de siete días.
- Carpeta con demos y enlaces a herramientas.

## 5.2 Materiales del facilitador

- Presentación de aproximadamente 34 slides.
- Cuenta de demostración previamente configurada.
- Asistente de ejemplo listo para abrir.
- Carpeta con el material ficticio de TurnoFácil.
- Video o capturas de pantalla como respaldo por falla de internet.
- 25–30 copias impresas del ejercicio principal.
- Tarjetas de mesa o roles.
- Marcadores, sticky notes y“白?".
- Timer visible para cada bloque.
- Formulario de registro, survey y feedback.
- QR de acceso al buzón de recursos.
- Lista de asistencia y contactos para seguimiento.

## 5.3 Preparación del espacio

- Proyector, pantalla grande o TV y control remoto.
- Audio si se utiliza música o micrófono.
- Wi-Fi estable y credenciales visibles.
- Enchufes y regletas de extensión.
- Organización de 5–6 mesas de 4–6 personas.
- Pizarra o pared para政策和 notas.
- Espacio para circular y asistir a participantes.
- Dispositivos de respaldo para demostrar ante fallas.

### Organización recomendada de mesas

- **Mesa 1:** Ventas.
- **Mesa 2:** Soporte.
- **Mesa 3:** Operaciones.
- **Mesas 4–6:** Cualquier track.

Esto ayuda a que las conversaciones entre pares sean。十。因此。

---

## 5.4 Equipo de facilitación

Para una audiencia de 20–30 personas:

- **1 facilitador principal:** contenido, demos y ritmo.
- **2 helpers recommended:** soporte técnico, dudas individuales y revisión de ejercicios.
- Una persona de soporte durante los primeros 15 minutos para resolver bloqueos de acceso.

### Roles dentro de cada mesa

- **Constructor:** mantiene el prompt en el chat.
- **Tester:** prueba casos y busca respuestas incorrectas.
- **Cliente:** representa al usuario final.
- **Observador:** revisa claridad, riesgos y escalamiento.

Los roles rotan para que no quede nadie como espectador pasivo.

---

## 5.5 Cronograma de preparación

### Siete días antes

- Enviar inscripción y encuesta de necesidades.
- Confirmar cantidad de laptops y herramientas disponibles.
- Enviar instrucciones de acceso y lista de herramientas.

### Tres días antes

- Enviar el material de prelectura.
- Pedir una descripción breve del startup y sus tareas repetitivas.
- Preparar el caso ficticio para participantes sin contexto.

### Un día antes

- Probar la demo completa en la misma red que se usar en el taller.
- Verificar que las cuentas, links y QR funcionen.
- Preparar capturas y video de respaldo.
- Imprimir los materiales.

### Día del workshop

- Probar sonido, Wi-Fi, proyectores y corriente.
- Abrir la demo y el buzón de recursos.
- Colocar temporizadores y materiales en cada mesa.
- Tener preparados los tres tracks de ejercicio.

---

# 6. Recursos para llevar a casa

## 6.1 Carpeta de templates y herramientas

| Recurso | Para qué sirve |
|---|---|
| **Lienzo de caso de uso** | Elegir y priorizar qué tarea automatizar |
| **Prompt Builder** | Construir instrucciones maestros paso a paso |
| **Plantilla de base de conocimiento** | Organizar FAQs, políticas y respuestas |
| **Suite de pruebas** | Validar respuestas normales y casos límite |
| **Checklist de guardarraíles** | Reducir invenciones, riesgos y respuestas inapropiadas |
| **Lienzo de flujo** | Definir entrada, asistente, revisión, escalamiento y registro |
| **Calculadora de impacto** | Estimar tiempo recuperado y valor del piloto |
| **Plan de siete días** | Llevar el asistente a una prueba real |
| **Directorio de herramientas** | Elegir herramienta según necesidad y presupuesto |

## 6.2 Biblioteca de herramientas por función

La plataforma principal debe ser aquella que la mayoría ya utiliza o que pueda试用 sin costo. El directorio puede incluir:

### Construcción del asistente

- ChatGPT.
- Gemini.
- Claude.
- Herramientas de creación de asistentes o “bots”.

### Conocimiento y documentación

- Google Docs o Drive.
- Notion.
- Google Sheets.

### Formularios y operación

- Google Forms.
- Trello.
- HubSpot.
-其他 CRM de uso sencillo.

### Automatización sin código

- Zapier.
- Make.
- Integraciones nativas de las propias herramientas.

### Mensajería y atención

- WhatsApp Business.
- ManyChat.
- Herramientas de helpdesk.

> Las funciones, precios y disponibilidad pueden variar según el país. El facilitador debe verificar las condiciones vigentes antes del taller.

## 6.3 Recursos de seguridad y responsabilidad

Incluir un checklist breve con:

- No subir datos personales, financieros, médicos o confidenciales.
- Usar datos ficticios durante la construcción.
- Revisar las políticas de privacidad y uso de datos del proveedor.
- Identificar claramente cuándo una respuesta fue generada por IA.
- Mantener aprobación humana para decisiones comerciales, legales, financieras o de alto impacto.
- Registrar conversaciones y correcciones para mejorar el asistente.
- Proporcionar una opción de contacto humano.

## 6.4 Seguimiento posterior

- Carpeta de recursos accesible mediante QR y enlace corto.
- Recording del demo y de la sesión, solo con consentimiento.
- Video de 5–10 minutos explicando cómo actualizar el prompt.
- Office hour opcional una semana después.
- Canal de comunidad para compartir casos y resultados.
- Mensaje automático siete días después:

> “¿Activaste tu asistente? ¿Cuántas conversaciones procesaste? ¿Qué respuesta fue incorrecta? ¿Qué ajustarías durante la próxima semana?”

---

# 7. Slide count estimado por sección

**Total recomendado: 34 slides.**  
Las slides de ejercicio permanecen en pantalla durante el trabajo; las explicativas deben ser visuales y breves.

| Sección | Slides estimadas | Contenido sugerido |
|---|---:|---|
| Apertura y objetivos | **4** | Título, entregables, agenda, poll y reglas |
| Identificación de casos de uso | **4** | Qué es un asistente, fórmula, ejemplos, filtros de riesgo |
| Demo de construcción | **5** | Contexto, prompt inicial, contexto, reglas, prueba |
| Ejercicio 1 | **2** | Lienzo de caso de uso y criterios de selección |
| Pausa | **1** | Slide de descanso con pregunta de networking |
| Demo de calidad | **5** | Base de conocimiento, límites, escalamiento, pruebas, antes/después |
| Ejercicio 2 | **3** | Instrucciones, lienzo de prompt y checklist de pares |
| Demo de workflow | **4** | Diagrama del flujo, opciones no-code, human-in-the-loop, despliegue |
| Ejercicio 3 | **2** | Lienzo de flujo y checklist de despliegue seguro |
| Cierre | **4** | Showcase, plan de siete días, QR de recursos y encuesta |
| **Total** | **34** |  |

### Recomendaciones de diseño

- Máximo 6–8 líneas por slide.
- Una idea principal por slide.
- Menos de 10 palabras en títulos.
- Antes/después, diagramas y capturas reales.
- Los templates deben estar siempre disponibles.
- Las instrucciones de ejercicio permanecen visibles hasta que todos terminen.

---

# 8. Indicadores de éxito del workshop

### Durante el taller

- **90% o más** termina con un prompt maestro completo.
- **80% o más** completa al menos cinco pruebas.
- **80% o más** define un canal de despliegue y una regla de escalamiento.
- Cada participante escribe una acción concreta para los próximos siete días.

### Después de una semana

- Porcentaje de asistentes que activa el piloto.
- Número de conversaciones procesadas.
- Tiempo promedio de respuesta.
- Porcentaje de casos resueltos o calificados.
- Errores más frecuentes.
- Escalamientos a personas.
- Satisfacción de usuarios internos o externos.

---

## Frase de cierre recomendada

> **“No necesitas terminar con una IA perfecta. Necesitas salir con un asistente que resuelve una tarea real, que sabes testar, que puedes controlar y que ya tiene un plan para funcionar mañana.”**