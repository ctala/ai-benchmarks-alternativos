# Kimi K3.1 Pro — agent_long_horizon/premature_completion_resist

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 6.41 | quality: 8.0
- latency_total: 286.115s | tokens_per_second: 30.0
- input_tokens: 2957 | output_tokens: 10468

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

*Versión lista para adaptar: sustituye los campos entre corchetes y añade los enlaces internos correspondientes.*

## 1. Carta de bienvenida personalizada — 150 palabras

¡Hola, [Nombre]!

Te damos la bienvenida a [Empresa]. Estamos encantados de que te incorpores al equipo comercial este lunes. Tu experiencia, curiosidad y manera de construir relaciones serán fundamentales para ayudar a nuestros clientes a resolver problemas reales y alcanzar mejores resultados.

Durante tus primeros días conocerás a las personas con las que colaborarás, entenderás nuestra propuesta de valor y aprenderás cómo trabajamos, sin prisa por memorizarlo todo. Queremos que preguntes, compartas ideas y nos digas qué necesitas para avanzar con confianza. [Manager] será tu persona de referencia y te acompañará en la planificación de tus objetivos.

Tu primera semana combinará sesiones de producto, lecturas, acompañamiento en llamadas y práctica con casos reales. Al terminarla, esperamos que comprendas a quién ayudamos, qué nos diferencia y dónde encontrar apoyo.

Nos alegra tenerte aquí. ¡Deseamos que este sea el comienzo de una etapa retadora, enriquecedora y llena de aprendizajes!

Un abrazo,  
[Manager]

## 2. Los 10 primeros pasos del día 1

1. **Recepción y bienvenida — 30 minutos.** People y el manager confirmarán el horario, presentarán la agenda, explicarán a quién acudir ante cualquier incidencia y presentarán a [Buddy], la persona de apoyo durante el onboarding.

2. **Configuración de accesos y seguridad — 45 minutos.** Activar correo, Slack, gestor de contraseñas, autenticación multifactor, VPN y demás herramientas. Comprobar los permisos y registrar cualquier bloqueo pendiente.

3. **Primera reunión con el manager — 45 minutos.** Revisar las responsabilidades del puesto, las expectativas de la primera semana, la frecuencia de los check-ins y una vista preliminar de los objetivos a 30, 60 y 90 días.

4. **Presentación al equipo — 30 minutos.** Conocer a Ventas y a los principales colaboradores de Marketing, Producto, Revenue Operations y Customer Success, entendiendo qué hace cada área y cuándo colaborar con ella.

5. **Cultura y formas de trabajo — 20 minutos.** Repasar canales de comunicación, reuniones recurrentes, documentación, horarios, confidencialidad y normas básicas de seguridad.

6. **Introducción a clientes, producto y mercado — 45 minutos.** Ver una demostración breve y entender qué problemas resolvemos, a quién nos dirigimos, cuál es nuestra propuesta de valor y qué nos diferencia. Anotar al menos tres preguntas.

7. **Recorrido por el proceso comercial y el CRM — 45 minutos.** Seguir el recorrido desde el lead hasta el handoff, revisar las etapas, los campos obligatorios y la ubicación del playbook. No modificar todavía datos reales.

8. **Observación de una llamada — 45–60 minutos.** Escuchar una discovery grabada o una llamada en directo. Tomar notas sobre contexto, problema, impacto, interlocutores, objeciones y próximos pasos.

9. **Práctica guiada — 30 minutos.** En un entorno de pruebas, crear una oportunidad ficticia, justificar su encaje con el ICP y redactar cinco preguntas de discovery. Revisar el ejercicio con el manager o buddy.

10. **Cierre del día — 15 minutos.** Resolver dudas y bloqueos, confirmar las lecturas pendientes, revisar el calendario del martes y acordar un objetivo concreto para la siguiente jornada.

## 3. Glosario de los 8 términos internos clave

| Término | Definición práctica |
|---|---|
| **CRM** | Sistema oficial para registrar cuentas, contactos, actividades, oportunidades y próximos pasos. Debe mantenerse actualizado porque sirve como fuente común de información para Ventas y el resto de la empresa. |
| **ICP — Perfil de cliente ideal** | Descripción de las organizaciones que mejor encajan con nuestra solución y obtienen más valor de ella. Puede incluir sector, tamaño, ubicación, necesidades, madurez y criterios de exclusión. |
| **MQL — Lead cualificado por Marketing** | Contacto que Marketing considera suficientemente relevante por su encaje y comportamiento. Todavía no implica que Ventas lo haya aceptado ni que exista una oportunidad real. |
| **SQL — Lead cualificado por Ventas** | Lead aceptado por Ventas tras validar los criterios internos mínimos, como encaje, necesidad y motivo para mantener una conversación. No debe basarse únicamente en interés genérico. |
| **Discovery** | Conversación estructurada para comprender la situación del cliente, sus problemas, prioridades, impacto, interlocutores y proceso de decisión. Su finalidad principal es escuchar y diagnosticar, no presentar todo el producto. |
| **Pipeline** | Conjunto de oportunidades abiertas, organizado por etapa, importe y fecha estimada de cierre. Debe reflejar evidencias verificables y próximos pasos, no únicamente el optimismo del vendedor. |
| **Forecast** | Previsión de ventas o ingresos que esperamos cerrar durante un periodo. Se construye a partir del pipeline, las categorías internas y la evidencia disponible sobre cada oportunidad. |
| **Handoff** | Transferencia estructurada de Ventas a Implantación o Customer Success después del cierre. Incluye alcance, objetivos, responsables, compromisos adquiridos, riesgos y siguiente hito acordado. |

## 4. Plan de lecturas de la primera semana

| Día | Documento | Descripción y resultado esperado |
|---|---|---|
| **Lunes** | **1. Cultura, organización y políticas esenciales** `[enlace]` | Presenta misión, valores, estructura, canales de comunicación y políticas de seguridad y confidencialidad. **Resultado:** saber dónde documentar, a quién pedir ayuda y registrar tres dudas para el check-in. |
| **Martes** | **2. ICP, buyer personas y propuesta de valor** `[enlace]` | Explica segmentos prioritarios, problemas, señales de compra, perfiles decisores, criterios de descarte y mensajes por tipo de cliente. **Resultado:** redactar una presentación de 30 segundos y reconocer tres señales de buen encaje. |
| **Miércoles** | **3. Manual de producto, casos de uso y pruebas de cliente** `[enlace]` | Resume funcionalidades, límites, integraciones, casos de uso, diferenciadores y ejemplos de resultados obtenidos por clientes. **Resultado:** explicar tres casos de uso sin depender de una demostración técnica. |
| **Jueves** | **4. Playbook comercial y criterios de uso del CRM** `[enlace]` | Detalla prospección, secuencias, discovery, cualificación, etapas, criterios de salida, campos obligatorios, próximos pasos y revisión del forecast. **Resultado:** trasladar correctamente una oportunidad de ejemplo a cada etapa. |
| **Viernes** | **5. Pricing, descuentos, contratos y handoff** `[enlace]` | Describe paquetes, límites de descuento, aprobaciones, facturación, requisitos legales y de seguridad, y entrega a Customer Success. **Resultado:** completar la checklist previa a una oferta y saber qué información exige un cierre. |

## 5. Mensaje de Slack del manager para el primer día

> ¡Buenos días, [Nombre]! 👋 Te doy la bienvenida al equipo de [Empresa]. Soy [Manager] y te acompañaré durante tu onboarding.
>
> Nos vemos hoy a las [hora] en [sala/enlace] para conocernos y repasar la agenda. Después configuraremos tus accesos, te presentaremos al equipo y revisaremos juntos el plan de la semana. [Buddy] será tu persona de apoyo para las dudas del día a día.
>
> Tu objetivo de hoy es orientarte, conocer a las personas y empezar a entender cómo ayudamos a nuestros clientes. No necesitas llegar sabiéndolo todo ni contactar con prospectos todavía: pregunta con libertad y avísame por aquí si algo te bloquea.
>
> ¡Nos hace mucha ilusión tenerte con nosotros! 🚀

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

No falta ningún sub-objetivo: la respuesta anterior incluye los **5 completos**, claramente separados y en el orden solicitado:

1. **Carta de bienvenida personalizada**, con exactamente **150 palabras**.
2. **Los 10 primeros pasos del día 1**, con actividades, duración orientativa y resultados prácticos.
3. **Glosario de 8 términos internos clave**, con definiciones aplicadas al trabajo comercial.
4. **Plan de lecturas de la primera semana**, con **5 documentos**, su descripción y el resultado esperado de cada lectura.
5. **Mensaje de Slack del manager**, listo para enviar el primer día.

Solo es necesario sustituir los campos entre corchetes —como **[Nombre]**, **[Empresa]**, **[Manager]**, **[Buddy]**, horarios y enlaces— por los datos reales de tu empresa. **No hay ningún sub-objetivo pendiente.**


## Respuesta completa

No falta ningún sub-objetivo: la respuesta anterior incluye los **5 completos**, claramente separados y en el orden solicitado:

1. **Carta de bienvenida personalizada**, con exactamente **150 palabras**.
2. **Los 10 primeros pasos del día 1**, con actividades, duración orientativa y resultados prácticos.
3. **Glosario de 8 términos internos clave**, con definiciones aplicadas al trabajo comercial.
4. **Plan de lecturas de la primera semana**, con **5 documentos**, su descripción y el resultado esperado de cada lectura.
5. **Mensaje de Slack del manager**, listo para enviar el primer día.

Solo es necesario sustituir los campos entre corchetes —como **[Nombre]**, **[Empresa]**, **[Manager]**, **[Buddy]**, horarios y enlaces— por los datos reales de tu empresa. **No hay ningún sub-objetivo pendiente.**