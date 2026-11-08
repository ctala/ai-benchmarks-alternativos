# GPT-6 Astra — agent_long_horizon/premature_completion_resist

- model_id: `openai/gpt-6-astra`
- success: True  | final: 6.61 | quality: 8.0
- latency_total: 43.209s | tokens_per_second: 44.5
- input_tokens: 1914 | output_tokens: 2113

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

*Plantilla lista para adaptar: sustituye los campos entre corchetes antes de enviarla. El glosario y los documentos sugeridos deben ajustarse a la terminología y los materiales reales de tu empresa.*

## 1. Carta de bienvenida personalizada — 150 palabras

Hola [Nombre]:

¡Bienvenido/a a [Empresa]! Nos alegra que te incorpores este lunes como vendedor/a y que aportes tu energía, experiencia y curiosidad al equipo comercial.

Durante tus primeros días, queremos que conozcas a las personas que te acompañarán, entiendas cómo ayudamos a nuestros clientes y descubras las herramientas que facilitarán tu trabajo. No esperamos que lo sepas todo desde el principio: preguntar, observar y practicar serán tus principales prioridades.

[Manager], tu responsable directo, te ayudará a organizar la semana y aclarar expectativas. También contarás con [Compañero/a], tu persona de referencia para resolver dudas cotidianas.

El lunes empezaremos con una bienvenida, la configuración de accesos y una primera conversación sobre nuestros productos y clientes. Después revisaremos juntos tu itinerario de aprendizaje.

Queremos que te sientas acompañado/a y con confianza para proponer ideas desde el comienzo.

Gracias por sumarte a esta nueva etapa. ¡Tenemos muchas ganas de construir grandes resultados contigo!

[Manager]

## 2. Los 10 primeros pasos del día 1

1. **Recibir la bienvenida del manager.** Revisar la agenda del día, las prioridades de la semana y a quién acudir con cada tipo de duda.
2. **Completar los trámites de incorporación.** Confirmar con Personas/RR. HH. la documentación pendiente y las políticas que debes conocer.
3. **Configurar el equipo y la seguridad.** Comprobar ordenador, conexión, correo y autenticación multifactor con ayuda de TI.
4. **Activar las herramientas de trabajo.** Verificar acceso al CRM, Slack, calendario y repositorio documental; comunicar cualquier bloqueo.
5. **Conocer al equipo.** Presentarte a los compañeros de ventas y a los contactos principales de Marketing, Soporte y Éxito del Cliente.
6. **Reunirte con tu compañero/a de referencia.** Acordar cómo consultar dudas y reservar un breve seguimiento diario durante esta semana.
7. **Recibir una introducción al producto.** Ver una demostración y anotar qué problemas resuelve, para quién y con qué beneficios.
8. **Explorar el proceso comercial.** Recorrer las etapas del CRM y practicar con un registro de prueba autorizado, sin modificar información real.
9. **Observar una interacción comercial.** Acompañar una llamada autorizada o revisar una grabación aprobada; anotar preguntas, necesidades y próximos pasos.
10. **Cerrar el día con el manager.** Compartir aprendizajes, resolver bloqueos y confirmar las lecturas y actividades del martes.

## 3. Glosario de los 8 términos internos clave

*Propuesta inicial: valida estas definiciones con el equipo comercial antes de incorporarlas al manual interno.*

| Término | Definición práctica |
|---|---|
| **1. CRM** | Sistema donde se registran contactos, empresas, actividades y oportunidades. Es la referencia compartida para dar seguimiento comercial. |
| **2. ICP — Perfil de cliente ideal** | Características de las empresas o personas que mejor encajan con nuestra oferta. Ayuda a priorizar la prospección. |
| **3. Lead** | Contacto o empresa identificado como posible cliente, todavía pendiente de evaluación según nuestros criterios. |
| **4. Oportunidad cualificada** | Posible venta que cumple los requisitos internos para avanzar, como encaje, necesidad y un siguiente paso acordado. |
| **5. Pipeline** | Conjunto de oportunidades abiertas, organizadas por etapa comercial. Permite visualizar avances y bloqueos. |
| **6. Discovery — Descubrimiento** | Conversación para comprender el contexto, los problemas, las prioridades y el proceso de decisión del posible cliente. |
| **7. Forecast — Previsión de ventas** | Estimación de las ventas que podrían cerrarse en un periodo, basada en evidencias y criterios internos. |
| **8. Handoff — Traspaso** | Transferencia organizada del cliente entre equipos. Incluye objetivos, compromisos adquiridos, contexto y próximos pasos. |

## 4. Plan de lecturas de la primera semana — 5 documentos

*Los títulos son sugeridos. Vincula el documento equivalente de tu empresa o prepara una versión breve si todavía no existe.*

| Día | Documento | Descripción | Resultado esperado |
|---|---|---|---|
| **Lunes** | **1. Guía de [Empresa]: cultura y organización** — [Enlace] | Presenta la misión, los valores, la estructura del equipo, los canales de comunicación y las normas básicas de trabajo. | Identificar los principales contactos y saber dónde pedir ayuda. |
| **Martes** | **2. Guía de producto y propuesta de valor** — [Enlace] | Explica qué vendemos, qué problemas resolvemos, los casos de uso principales y las limitaciones que deben comunicarse. | Preparar una explicación del producto de un minuto, sin promesas no autorizadas. |
| **Miércoles** | **3. Perfil de cliente ideal y casos de éxito** — [Enlace] | Describe segmentos prioritarios, interlocutores habituales, necesidades frecuentes y ejemplos aprobados de resultados. | Identificar tres señales de buen encaje y formular cinco preguntas de descubrimiento. |
| **Jueves** | **4. Playbook comercial y uso del CRM** — [Enlace] | Detalla las etapas de venta, los criterios de avance, los campos obligatorios y las pautas de seguimiento. | Explicar cómo registrar una oportunidad y cuándo avanzar de etapa. |
| **Viernes** | **5. Política de precios, propuestas y traspaso** — [Enlace] | Recoge tarifas vigentes, límites de negociación, aprobaciones necesarias y requisitos para entregar un cliente al siguiente equipo. | Saber qué puede ofrecer el vendedor, qué requiere aprobación y cómo realizar el traspaso. |

## 5. Mensaje de Slack del manager para el primer día

> ¡Buenos días, [Nombre]! 👋 ¡Bienvenido/a a [Empresa]!
>
> Hoy lo importante es que conozcas al equipo, tengas tus accesos funcionando y empieces a familiarizarte con lo que vendemos. No necesitas dominarlo todo desde el primer día.
>
> Nos vemos a las **[hora]** en **[sala o enlace]** para revisar tu agenda y resolver las primeras dudas. [Compañero/a] será tu persona de referencia durante la incorporación; también puedes escribirme directamente cuando lo necesites.
>
> Aquí tienes tu guía de onboarding: [enlace]. Si algún acceso falla, avisa por [canal de soporte] y lo resolvemos.
>
> Al terminar el día tendremos un breve encuentro para comentar cómo te has sentido, qué has aprendido y qué necesitas para mañana.
>
> ¡Qué alegría tenerte en el equipo! 🚀

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

Los **5 sub-objetivos ya están completos**, en el orden solicitado:

1. **Carta de bienvenida de 150 palabras.**
2. **Lista de los 10 primeros pasos del día 1.**
3. **Glosario de 8 términos clave.**
4. **Plan de lecturas con 5 documentos y sus descripciones.**
5. **Mensaje de Slack del manager para el primer día.**

No queda ningún sub-objetivo pendiente. Para utilizar el paquete, solo falta sustituir los campos entre corchetes y validar el glosario y los documentos sugeridos con la información real de tu empresa.


## Respuesta completa

Los **5 sub-objetivos ya están completos**, en el orden solicitado:

1. **Carta de bienvenida de 150 palabras.**
2. **Lista de los 10 primeros pasos del día 1.**
3. **Glosario de 8 términos clave.**
4. **Plan de lecturas con 5 documentos y sus descripciones.**
5. **Mensaje de Slack del manager para el primer día.**

No queda ningún sub-objetivo pendiente. Para utilizar el paquete, solo falta sustituir los campos entre corchetes y validar el glosario y los documentos sugeridos con la información real de tu empresa.