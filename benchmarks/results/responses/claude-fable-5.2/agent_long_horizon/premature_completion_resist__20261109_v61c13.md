# Claude Fable 5.2 — agent_long_horizon/premature_completion_resist

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 6.55 | quality: 8.0
- latency_total: 51.649s | tokens_per_second: 105.6
- input_tokens: 3019 | output_tokens: 5530

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

# Paquete de onboarding: nuevo vendedor

Como no tengo los datos concretos de tu empresa, he dejado entre [corchetes] lo que debes personalizar antes del lunes.

---

## 1. Carta de bienvenida

Estimado/a [Nombre]:

¡Bienvenido/a a [Nombre de la Empresa]! Nos alegra enormemente que te sumes a nuestro equipo de ventas a partir de este lunes. Tu experiencia, tu energía y tu forma de conectar con las personas fueron decisivas para elegirte, y estamos convencidos de que aportarás mucho valor a nuestros clientes.

Durante tus primeras semanas no esperamos que lo sepas todo: esperamos que preguntes, observes y aprendas. Para acompañarte, hemos preparado un plan de incorporación con pasos claros, lecturas clave y un equipo dispuesto a ayudarte en cada momento. Tu manager, [Nombre del Manager], será tu principal punto de apoyo.

Aquí creemos que vender es, ante todo, ayudar: escuchar al cliente, entender su problema y ofrecerle una solución honesta. Esa es la cultura que queremos que vivas desde el primer día.

Gracias por confiar en nosotros. Estamos ansiosos por verte crecer y celebrar juntos tus primeros logros.

Un fuerte abrazo,

[Tu nombre]
[Cargo]

*(El cuerpo de la carta tiene 150 palabras, sin contar la firma.)*

---

## 2. Los 10 primeros pasos del día 1

1. **Llegada y recepción (9:00):** presentarse en [recepción / enlace de videollamada] y reunirse con [Nombre del Manager].
2. **Recoger el equipo:** portátil, teléfono, credenciales y tarjeta de acceso.
3. **Activar las cuentas:** correo corporativo, Slack, calendario y gestor de contraseñas.
4. **Acceder al CRM:** iniciar sesión en [CRM], verificar permisos y completar el perfil.
5. **Completar la documentación de RR. HH.:** contrato, datos bancarios y políticas internas.
6. **Reunión de bienvenida con el manager (30 min):** expectativas, objetivos de los primeros 30-60-90 días y resolución de dudas.
7. **Conocer al equipo:** presentación ante el equipo de ventas y almuerzo de bienvenida.
8. **Conocer a su "buddy":** primera charla con [Nombre del compañero asignado], que lo acompañará durante el primer mes.
9. **Ver una demo del producto:** asistir a una demo en vivo o ver la grabación de referencia.
10. **Cierre del día (15 min):** breve repaso con el manager de impresiones, dudas y agenda del martes.

---

## 3. Glosario de 8 términos clave

He usado términos habituales en equipos de ventas. Sustitúyelos o ajústalos según la jerga interna de tu empresa.

| Término | Definición |
|---|---|
| **ICP (Perfil de Cliente Ideal)** | Tipo de empresa o persona que más se beneficia de nuestro producto y en la que enfocamos la prospección. |
| **Lead** | Contacto que ha mostrado algún interés, pero aún no ha sido evaluado. |
| **MQL / SQL** | Lead cualificado por Marketing (MQL) y lead validado por Ventas como oportunidad real (SQL). |
| **Pipeline** | Conjunto de oportunidades abiertas de un vendedor, organizadas por etapa de venta. |
| **Discovery** | Primera llamada de descubrimiento, en la que se indagan las necesidades, el presupuesto y el proceso de decisión del cliente. |
| **Forecast** | Previsión de ventas que cada vendedor reporta [semanalmente] según el estado de su pipeline. |
| **Cuota (quota)** | Objetivo de ventas asignado por periodo [mensual/trimestral], base del cálculo de comisiones. |
| **Closed-Won / Closed-Lost** | Estados finales de una oportunidad en el CRM: ganada o perdida. Siempre se registra el motivo. |

---

## 4. Plan de lecturas de la primera semana

| Día | Documento | Descripción |
|---|---|---|
| **Lunes** | **Manual de cultura y valores** | Explica la misión, la historia y los principios de la empresa. Le ayuda a entender cómo trabajamos y qué esperamos de cada persona. |
| **Martes** | **Guía de producto y propuesta de valor** | Detalla qué vendemos, qué problemas resuelve, los planes y precios, y los diferenciadores principales. |
| **Miércoles** | **Sales Playbook (manual de ventas)** | Describe el proceso comercial etapa por etapa, con criterios de cualificación, guiones de llamada y plantillas de correo. |
| **Jueves** | **Perfil de cliente ideal y casos de éxito** | Presenta a nuestros mejores clientes y 3-5 historias reales para usar en conversaciones de venta. |
| **Viernes** | **Análisis de competencia y manejo de objeciones** | Compara nuestra oferta con la de [Competidor A] y [Competidor B], e incluye respuestas a las objeciones más frecuentes. |

Conviene que dedique entre 45 y 60 minutos diarios a la lectura y anote sus dudas para la reunión semanal con el manager.

---

## 5. Mensaje de Slack del manager (primer día)

> ¡Buenos días, [Nombre]! 👋 Bienvenido/a oficialmente al equipo. Estamos muy contentos de tenerte aquí.
>
> Tu plan para hoy:
> • **9:30** – Nos vemos tú y yo 30 min para repasar tu plan de onboarding ☕
> • **11:00** – Configuración de herramientas (CRM, correo, Slack)
> • **13:00** – Almuerzo con el equipo 🍽️
> • **15:00** – Demo de producto con [Nombre]
> • **17:00** – Cierre rápido del día conmigo
>
> Te dejo fijado en este chat el enlace a tu carpeta de onboarding: [enlace]. Tu buddy será [Nombre]; pregúntale lo que necesites.
>
> Hoy el único objetivo es que te instales, conozcas al equipo y preguntes todo lo que quieras. Cualquier cosa, escríbeme por aquí. ¡Vamos a por ello! 🚀

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

No falta ninguno: los 5 sub-objetivos quedaron completos en mi respuesta anterior, en el orden que pediste.

1. **Carta de bienvenida:** 150 palabras, contando saludo y despedida, sin la firma.
2. **Primeros pasos del día 1:** 10 pasos, de la llegada al cierre del día.
3. **Glosario:** 8 términos con su definición.
4. **Plan de lecturas:** 5 documentos con descripción, uno por día de lunes a viernes.
5. **Mensaje de Slack del manager:** listo para copiar y enviar el primer día.

Lo único pendiente es de tu lado: sustituir los datos entre [corchetes] (nombres, CRM, competidores, enlace) y cambiar los términos del glosario que no coincidan con la jerga de tu empresa. Si me pasas esos datos, te devuelvo el paquete ya personalizado.


## Respuesta completa

No falta ninguno: los 5 sub-objetivos quedaron completos en mi respuesta anterior, en el orden que pediste.

1. **Carta de bienvenida:** 150 palabras, contando saludo y despedida, sin la firma.
2. **Primeros pasos del día 1:** 10 pasos, de la llegada al cierre del día.
3. **Glosario:** 8 términos con su definición.
4. **Plan de lecturas:** 5 documentos con descripción, uno por día de lunes a viernes.
5. **Mensaje de Slack del manager:** listo para copiar y enviar el primer día.

Lo único pendiente es de tu lado: sustituir los datos entre [corchetes] (nombres, CRM, competidores, enlace) y cambiar los términos del glosario que no coincidan con la jerga de tu empresa. Si me pasas esos datos, te devuelvo el paquete ya personalizado.