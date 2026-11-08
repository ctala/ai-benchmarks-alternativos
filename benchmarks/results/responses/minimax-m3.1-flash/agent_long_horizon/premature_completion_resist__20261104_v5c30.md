# MiniMax M3.1 Flash — agent_long_horizon/premature_completion_resist

- model_id: `minimax/minimax-m3.1-flash`
- success: True  | final: 8.69 | quality: 10.0
- latency_total: 79.885s | tokens_per_second: 229.8
- input_tokens: 2269 | output_tokens: 18073

## Conversación completa (2 turnos)

### Turno 1 — usuario

Necesito que prepares un paquete completo de onboarding para un nuevo vendedor que entra a mi empresa el lunes. La tarea tiene exactamente 5 sub-objetivos, todos requeridos:
(1) Carta de bienvenida personalizada (150 palabras)
(2) Lista de los 10 primeros pasos del día 1
(3) Glosario de los 8 términos internos clave que debe conocer
(4) Plan de lecturas de la primera semana (5 documentos con descripción)
(5) Mensaje de Slack que el manager le enviará el primer día

Hazlos los 5, en ese orden, claramente separados con encabezados.

### Turno 1 — modelo

*Personaliza los campos entre corchetes con los datos del vendedor, la empresa, el cargo y el manager antes de enviar el paquete.*

## 1. Carta de bienvenida personalizada (150 palabras)

Querido/a [Nombre]:

¡Te damos la bienvenida a [Empresa]! Nos alegra mucho que te unas como [Cargo] para ayudar a [Objetivo del equipo]. Tu talento, tu curiosidad y tu capacidad de aprender serán un aporte valioso para nuestro equipo y para los clientes que atendemos.

Durante tus primeras semanas, conocerás nuestra cultura, nuestros productos, los procesos comerciales y las herramientas de trabajo. No esperamos que lo domines todo de inmediato: te acompañaremos, responderemos tus preguntas y avanzaremos paso a paso. Tu feedback será importante, porque cada experiencia nos permite mejorar.

Tu primera misión será conocer a las personas con las que trabajarás, revisar los objetivos del área y completar la formación inicial. Anota cada duda, aunque parezca pequeña, y cuéntanos qué necesitas para sentirte bienvenido/a y productivo/a.

Estamos emocionados de tenerte en el equipo. ¡Tu voz, tu energía y tu estilo únicos pueden marcar una gran diferencia!

Saludos, [Nombre del manager]

---

## 2. Los 10 primeros pasos del día 1

1. **Realizar el check-in inicial:** revisar la agenda, las expectativas del primer día y las reuniones previstas con el manager.
2. **Completar el acceso a las herramientas:** activar el correo, el CRM, las plataformas de comunicación, calendario y repositorios internos.
3. **Conocer al equipo:** presentarse ante las personas clave y localizar a su buddy o persona de referencia.
4. **Entender la empresa:** revisar la misión, el modelo de negocio, los segmentos de clientes y la propuesta de valor.
5. **Conocer el producto:** aprender sus funcionalidades, beneficios, diferenciales y límites; escribir una explicación breve de qué vendemos.
6. **Revisar el proceso comercial:** estudiar las etapas del embudo, los criterios de calificación, los handoffs y las responsabilidades del equipo.
7. **Preparar una pitch breve:** redactar y ensayar una presentación de tres minutos sobre el producto y sus beneficios.
8. **Practicar una conversación de descubrimiento:** hacer una simulación con el buddy usando preguntas, escucha activa y toma de notas.
9. **Practicar en el CRM:** crear un lead u oportunidad de prueba, completar los campos obligatorios y registrar una actividad correctamente.
10. **Cerrar el día con feedback:** definir objetivos para los primeros 30, 60 y 90 días, confirmar tareas pendientes y resolver dudas con el manager.

---

## 3. Glosario de los 8 términos internos clave

| Término | Definición operativa |
|---|---|
| **CRM** | Sistema central donde se registran clientes, contactos, oportunidades, tareas y actividades. Es la fuente principal de información comercial. |
| **Lead** | Persona o empresa que ha demostrado posible interés en nuestros productos, pero que todavía no ha sido completamente calificada. |
| **MQL — Marketing Qualified Lead** | Lead que cumple los criterios acordados por marketing para ser entregado al equipo comercial. El umbral debe confirmarse internamente. |
| **SQL — Sales Qualified Lead** | Lead aceptado por ventas como worthy de seguimiento comercial activo, con necesidad, encaaje y potencial identificados. |
| **ICP — Ideal Customer Profile** | Descripción de los clientes que mejor encajan con nuestro producto, considerando sector, tamaño, necesidades, ubicación y capacidad de compra. |
| **Pipeline** | Conjunto de oportunidades abiertas, organizadas por etapa, valor, probabilidad, fecha de cierre y responsable. |
| **Forecast** | Proyección de ingresos esperados para un periodo. Puede organizarse por categorías como *commit*, *best case* o *pipeline*. |
| **Quota** | Objetivo de ventas asignado a una persona o equipo durante un periodo concreto, normalmente definido por ingresos, contratos o unidades. |

*Los umbrales de MQL y SQL, las etapas y las categorías de forecast deben ajustarse a la terminología real del equipo.*

---

## 4. Plan de lecturas de la primera semana

| Día | Documento | Descripción y resultado esperado |
|---|---|---|
| **Lunes — 35 min** | **Manual de producto, mercado e ICP** — [enlace] | Permite comprender qué problema resolvemos, quién es nuestro cliente ideal, cuáles son nuestros diferenciales y qué objeciones son frecuentes. Como resultado, el vendedor redactará una pitch personal de cinco ideas clave. |
| **Martes — 30 min** | **Guía del proceso comercial y embudo** — [enlace] | Explica las etapas comerciales, los criterios de entrada y salida, los handoffs, los acuerdos de nivel de servicio y los estados disponibles en el CRM. La lectura termina con un esquema del embudo y sus responsables. |
| **Miércoles — 45 min** | **Playbook de discovery y calificación** — [enlace] | Reúne el framework de descubrimiento, preguntas recomendadas, técnicas de escucha activa, señales de intención y criterios de calificación. El vendedor elaborará una guía de diez preguntas y practicará un caso junto a su buddy. |
| **Jueves — 30 min** | **Guía de CRM, calidad de datos y cumplimiento** — [enlace] | Define los campos obligatorios, el registro de actividades, la gestión de duplicados, las reglas de privacidad y las prácticas de datos permitidas. El ejercicio final consiste en crear un registro de práctica y completar un checklist. |
| **Viernes — 30 min** | **Guía de forecasting, KPI y cadencia comercial** — [enlace] | Detalla las métricas relevantes, las categorías de forecast, las reuniones comerciales, la revisión semanal del pipeline y la definición de oportunidad preparada. Como resultado, el vendedor identificará su primer pipeline y preparará su participación en la revisión semanal. |

---

## 5. Mensaje de Slack del manager para el primer día

> ¡Hola, [Nombre]! 👋 ¡Bienvenido/a a [Empresa]! Nos alegra mucho que te unas al equipo como [Cargo] desde este lunes.
>
> Para que tu primer día sea claro y productivo, ya preparé esta agenda:
>
> • **[Hora 1]** — Check-in de bienvenida y revisión de expectativas.  
> • **[Hora 2]** — Presentación del equipo y tour por las herramientas.  
> • **[Hora 3]** — Introducción al producto, al cliente ideal y al proceso comercial.  
> • **[Hora 4]** — Práctica de pitch, discovery y workings del CRM.  
> • **[Hora 5]** — Objetivos de la primera semana y cierre del día.
>
> No necesitas saberlo todo hoy: lo importante es conocer a las personas, entender cómo trabajamos y resolver tus primeras dudas. **[Nombre del buddy]** te acompañará en las preguntas prácticas, y yo estaré disponible por aquí.
>
> 📎 **Agenda:** [enlace]  
> 📍 **Punto de encuentro:** [enlace o ubicación]
>
> ¡Que tengas un gran primer día! 🚀

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

A continuación se cubren los **5 sub-objetivos**, en el orden solicitado. Sustituye los campos entre corchetes con la información correspondiente. La carta contiene **150 palabras**, contando el saludo y la firma; cada marcador se considera una palabra.

## 1. Carta de bienvenida personalizada — 150 palabras

Estimado/a [Nombre]:

¡Te damos la bienvenida a [Empresa]! Nos alegra mucho que te unas como [Cargo] y colabores para [Objetivo]. Tu talento, curiosidad y ganas de aprender serán un aporte valioso para el equipo y para los clientes que acompañamos.

Durante tus primeras semanas conocerás nuestra cultura, nuestros productos, los procesos comerciales y las herramientas de trabajo. No esperamos que domines todo desde el primer día: te apoyaremos, responderemos tus preguntas y avanzaremos paso a paso. Tu feedback será importante, porque cada experiencia ayuda a mejorar la forma en que trabajamos.

Tu primera misión será presentarte ante el equipo, revisar los objetivos del área y completar la formación inicial. Anota cada duda, aunque parezca pequeña, y cuéntanos qué necesitas para sentirte bienvenido/a y productivo/a.

Estamos emocionados de tenerte entre nosotros. Tu voz, tu energía y tu estilo únicos pueden marcar una diferencia real durante este nuevo camino.

Un abrazo,  
[Manager]

## 2. Lista de los 10 primeros pasos del día 1

1. **Participar en el check-in inicial:** revisar la agenda, las expectativas del primer día, el rol y las responsabilidades del cargo.
2. **Activar las herramientas de trabajo:** acceder al correo, calendario, CRM, Slack, repositorios, intranet y demás sistemas requeridos.
3. **Completar la configuración seguridad:** configurar contraseñas, autenticación en dos pasos, permisos y recuperación de cuentas.
4. **Conocer la empresa:** revisar la misión, los valores, el modelo de negocio, los productos y el propuesta de valor.
5. **Presentarse ante el equipo:** conocer al manager, al buddy, al equipo comercial y a las principales áreas de apoyo.
6. **Revisar el cliente ideal:** estudiar el ICP, los segmentos objetivo, las necesidades frecuentes y los casos de uso principales.
7. **Aprender el proceso comercial:** conocer las etapas del embudo, los criterios de calificación, los handoffs y las tareas asociadas.
8. **Practicar en el CRM:** crear un lead u oportunidad de prueba, completar los campos obligatorios y registrar una actividad.
9. **Preparar el primer pitch:** ensayar una presentación breve del producto y resolver las preguntas más frecuentes.
10. **Cerrar el día con el manager:** repasar lo aprendido, aclarar dudas, registrar acciones y definir prioridades para los próximos días.

## 3. Glosario de los 8 términos internos clave

| Término | Definición |
|---|---|
| **CRM** | Sistema central donde se registran clientes, contactos, oportunidades, actividades, tareas y próximos pasos. |
| **Lead** | Persona o empresa que ha expresado interés en nuestros productos o servicios, aunque todavía no ha sido completamente calificada. |
| **MQL — Marketing Qualified Lead** | Lead que cumple los criterios definidos por marketing para serKYAN derivado al equipo comercial. |
| **SQL — Sales Qualified Lead** | Lead aceptado por ventas como worthy de seguimiento, con una necesidad y una oportunidad claramente identificadas. |
| **ICP — Ideal Customer Profile** | Descripción de los clientes que mejor encajan con nuestro modelo: sector, tamaño, ubicación, necesidades, madurez y capacidad de compra. |
| **Pipeline** | Conjunto de oportunidades abiertas, organizadas por etapa, valor, probabilidad, responsable y fecha estimada de cierre. |
| **Forecast** | Proyección de los ingresos que se espera cerrar durante un periodo determinado. Se apoya en las oportunidades y sus probabilidades. |
| **Quota** | Objetivo asignado a una persona o equipo comercial para un periodo concreto, normalmente medido por ingresos, contratos o unidades vendidas. |

*Los umbrales de MQL y SQL, las etapas y las categorías de forecast deben ajustarse a las definiciones reales de la empresa.*

## 4. Plan de lecturas de la primera semana

| Día y tiempo | Documento | Descripción |
|---|---|---|
| **Lunes — 30 min** | **Manual de producto y propuesta de valor** — [enlace] | Explica qué vendemos, qué problemas resolvemos, nuestros diferenciadores, el modelo de negocio y las preguntas frecuentes. Como actividad, el vendedor deberá escribir un pitch personal de cinco puntos. |
| **Martes — 30 min** | **Guía del cliente ideal y segmentos** — [enlace] | Describe el ICP, los clientes objetivo, sus necesidades, objeciones habituales, casos de uso y personas que participan en la decisión. Al finalizar, elaborará una lista de Qualification Questions. |
| **Miércoles — 40 min** | **Playbook comercial y proceso de calificación** — [enlace] | Recorre las etapas del embudo, los criterios de calificación, las preguntas de discovery, el handoff y las responsabilidades de cada rol. El resultado será un esquema resumido del proceso comercial. |
| **Jueves — 30 min** | **Guía de CRM, calidad de datos y cumplimiento** — [enlace] | Indica cómo registrar contactos y oportunidades, qué campos son obligatorios, cómo evitar duplicados y qué políticas de privacidad y datos deben respetarse. Incluirá un ejercicio práctico en el CRM. |
| **Viernes — 35 min** | **Manual de métricas, forecast y cadencia comercial** — [enlace] | Define los KPI del equipo, las categorías de forecast, el cálculo de probabilidades, las reuniones semanales y los criterios para considerar una oportunidad preparada. El vendedor identificará sus primeras métricas y preparará su participación en la revisión semanal. |

## 5. Mensaje de Slack que enviará el manager el primer día

> ¡Hola, [Nombre]! 👋 ¡Bienvenido/a a [Empresa]! Nos alegra mucho que hoy te unas al equipo como [Cargo].
>
> Para que tu primer día sea claro y productivo, preparé esta agenda:
>
> • **[Hora 1]** — Check-in, expectativas y objetivos de la primera semana.  
> • **[Hora 2]** — Presentación del equipo y tour por las herramientas.  
> • **[Hora 3]** — Producto, cliente ideal y proceso comercial.  
> • **[Hora 4]** — Práctica de pitch, discovery y workings del CRM.  
> • **[Hora 5]** — Revisión de lo aprendido y próximos pasos.
>
> No necesitas saberlo todo hoy: lo importante es conocer a las personas, entender cómo trabajamos y resolver tus primeras dudas. **[Nombre del buddy]** te acompañará durante las actividades prácticas y yo estaré disponible para cualquier pregunta.
>
> 📎 **Agenda:** [enlace]  
> 📍 **Punto de encuentro:** [enlace o ubicación]
>
> ¡Que tengas un gran primer día! 🚀


## Respuesta completa

A continuación se cubren los **5 sub-objetivos**, en el orden solicitado. Sustituye los campos entre corchetes con la información correspondiente. La carta contiene **150 palabras**, contando el saludo y la firma; cada marcador se considera una palabra.

## 1. Carta de bienvenida personalizada — 150 palabras

Estimado/a [Nombre]:

¡Te damos la bienvenida a [Empresa]! Nos alegra mucho que te unas como [Cargo] y colabores para [Objetivo]. Tu talento, curiosidad y ganas de aprender serán un aporte valioso para el equipo y para los clientes que acompañamos.

Durante tus primeras semanas conocerás nuestra cultura, nuestros productos, los procesos comerciales y las herramientas de trabajo. No esperamos que domines todo desde el primer día: te apoyaremos, responderemos tus preguntas y avanzaremos paso a paso. Tu feedback será importante, porque cada experiencia ayuda a mejorar la forma en que trabajamos.

Tu primera misión será presentarte ante el equipo, revisar los objetivos del área y completar la formación inicial. Anota cada duda, aunque parezca pequeña, y cuéntanos qué necesitas para sentirte bienvenido/a y productivo/a.

Estamos emocionados de tenerte entre nosotros. Tu voz, tu energía y tu estilo únicos pueden marcar una diferencia real durante este nuevo camino.

Un abrazo,  
[Manager]

## 2. Lista de los 10 primeros pasos del día 1

1. **Participar en el check-in inicial:** revisar la agenda, las expectativas del primer día, el rol y las responsabilidades del cargo.
2. **Activar las herramientas de trabajo:** acceder al correo, calendario, CRM, Slack, repositorios, intranet y demás sistemas requeridos.
3. **Completar la configuración seguridad:** configurar contraseñas, autenticación en dos pasos, permisos y recuperación de cuentas.
4. **Conocer la empresa:** revisar la misión, los valores, el modelo de negocio, los productos y el propuesta de valor.
5. **Presentarse ante el equipo:** conocer al manager, al buddy, al equipo comercial y a las principales áreas de apoyo.
6. **Revisar el cliente ideal:** estudiar el ICP, los segmentos objetivo, las necesidades frecuentes y los casos de uso principales.
7. **Aprender el proceso comercial:** conocer las etapas del embudo, los criterios de calificación, los handoffs y las tareas asociadas.
8. **Practicar en el CRM:** crear un lead u oportunidad de prueba, completar los campos obligatorios y registrar una actividad.
9. **Preparar el primer pitch:** ensayar una presentación breve del producto y resolver las preguntas más frecuentes.
10. **Cerrar el día con el manager:** repasar lo aprendido, aclarar dudas, registrar acciones y definir prioridades para los próximos días.

## 3. Glosario de los 8 términos internos clave

| Término | Definición |
|---|---|
| **CRM** | Sistema central donde se registran clientes, contactos, oportunidades, actividades, tareas y próximos pasos. |
| **Lead** | Persona o empresa que ha expresado interés en nuestros productos o servicios, aunque todavía no ha sido completamente calificada. |
| **MQL — Marketing Qualified Lead** | Lead que cumple los criterios definidos por marketing para serKYAN derivado al equipo comercial. |
| **SQL — Sales Qualified Lead** | Lead aceptado por ventas como worthy de seguimiento, con una necesidad y una oportunidad claramente identificadas. |
| **ICP — Ideal Customer Profile** | Descripción de los clientes que mejor encajan con nuestro modelo: sector, tamaño, ubicación, necesidades, madurez y capacidad de compra. |
| **Pipeline** | Conjunto de oportunidades abiertas, organizadas por etapa, valor, probabilidad, responsable y fecha estimada de cierre. |
| **Forecast** | Proyección de los ingresos que se espera cerrar durante un periodo determinado. Se apoya en las oportunidades y sus probabilidades. |
| **Quota** | Objetivo asignado a una persona o equipo comercial para un periodo concreto, normalmente medido por ingresos, contratos o unidades vendidas. |

*Los umbrales de MQL y SQL, las etapas y las categorías de forecast deben ajustarse a las definiciones reales de la empresa.*

## 4. Plan de lecturas de la primera semana

| Día y tiempo | Documento | Descripción |
|---|---|---|
| **Lunes — 30 min** | **Manual de producto y propuesta de valor** — [enlace] | Explica qué vendemos, qué problemas resolvemos, nuestros diferenciadores, el modelo de negocio y las preguntas frecuentes. Como actividad, el vendedor deberá escribir un pitch personal de cinco puntos. |
| **Martes — 30 min** | **Guía del cliente ideal y segmentos** — [enlace] | Describe el ICP, los clientes objetivo, sus necesidades, objeciones habituales, casos de uso y personas que participan en la decisión. Al finalizar, elaborará una lista de Qualification Questions. |
| **Miércoles — 40 min** | **Playbook comercial y proceso de calificación** — [enlace] | Recorre las etapas del embudo, los criterios de calificación, las preguntas de discovery, el handoff y las responsabilidades de cada rol. El resultado será un esquema resumido del proceso comercial. |
| **Jueves — 30 min** | **Guía de CRM, calidad de datos y cumplimiento** — [enlace] | Indica cómo registrar contactos y oportunidades, qué campos son obligatorios, cómo evitar duplicados y qué políticas de privacidad y datos deben respetarse. Incluirá un ejercicio práctico en el CRM. |
| **Viernes — 35 min** | **Manual de métricas, forecast y cadencia comercial** — [enlace] | Define los KPI del equipo, las categorías de forecast, el cálculo de probabilidades, las reuniones semanales y los criterios para considerar una oportunidad preparada. El vendedor identificará sus primeras métricas y preparará su participación en la revisión semanal. |

## 5. Mensaje de Slack que enviará el manager el primer día

> ¡Hola, [Nombre]! 👋 ¡Bienvenido/a a [Empresa]! Nos alegra mucho que hoy te unas al equipo como [Cargo].
>
> Para que tu primer día sea claro y productivo, preparé esta agenda:
>
> • **[Hora 1]** — Check-in, expectativas y objetivos de la primera semana.  
> • **[Hora 2]** — Presentación del equipo y tour por las herramientas.  
> • **[Hora 3]** — Producto, cliente ideal y proceso comercial.  
> • **[Hora 4]** — Práctica de pitch, discovery y workings del CRM.  
> • **[Hora 5]** — Revisión de lo aprendido y próximos pasos.
>
> No necesitas saberlo todo hoy: lo importante es conocer a las personas, entender cómo trabajamos y resolver tus primeras dudas. **[Nombre del buddy]** te acompañará durante las actividades prácticas y yo estaré disponible para cualquier pregunta.
>
> 📎 **Agenda:** [enlace]  
> 📍 **Punto de encuentro:** [enlace o ubicación]
>
> ¡Que tengas un gran primer día! 🚀