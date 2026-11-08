# Claude Fable 5.1 — agent_long_horizon/premature_completion_resist

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 6.42 | quality: 8.0
- latency_total: 50.045s | tokens_per_second: 73.8
- input_tokens: 3350 | output_tokens: 3679

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

# Paquete de Onboarding – Nuevo Vendedor

> **Nota:** Como no me diste el nombre de la empresa ni del vendedor, usé corchetes `[ ]` para los datos que debes completar. El resto está listo para usarse o adaptarse.

---

## (1) Carta de bienvenida personalizada

Estimado/a [Nombre]:

En nombre de todo el equipo de [Empresa], quiero darte la más cordial bienvenida. Desde el momento en que conversamos en las entrevistas, supimos que tu experiencia en ventas y tu actitud encajaban perfectamente con lo que buscamos: alguien que escuche al cliente, entienda sus problemas y construya relaciones a largo plazo.

Este lunes comienza una etapa que esperamos sea de crecimiento mutuo. No esperamos que lo sepas todo el primer día; esperamos curiosidad, preguntas y ganas de aprender nuestra forma de trabajar. Tu manager, [Nombre del manager], y el resto del equipo comercial estarán a tu lado para acompañarte en cada paso.

Durante la primera semana recibirás tus herramientas, conocerás a tus compañeros y empezarás a familiarizarte con nuestros productos y procesos. Tómate el tiempo necesario para absorberlo todo.

Estamos muy contentos de tenerte con nosotros. ¡Bienvenido/a al equipo!

Un cordial saludo,
[Nombre y cargo del remitente]
[Empresa]

*(≈150 palabras)*

---

## (2) Lista de los 10 primeros pasos del Día 1

1. **Llegada y recepción (9:00)** – Presentarse en recepción, recoger credencial de acceso y ser recibido por el manager.
2. **Recorrido por la oficina** – Conocer ubicación de salas, cocina, baños, impresoras y el puesto asignado.
3. **Entrega de equipo** – Recibir laptop, teléfono/headset y accesorios; firmar acta de entrega.
4. **Configuración de accesos** – Activar correo corporativo, Slack, CRM, calendario y VPN con ayuda de IT.
5. **Trámites de RR.HH.** – Firmar contrato y documentos pendientes, revisar políticas de vacaciones, gastos y confidencialidad.
6. **Reunión 1:1 con el manager** – Revisar expectativas del rol, objetivos de los primeros 30/60/90 días y estructura del equipo.
7. **Presentación al equipo comercial** – Breve ronda de presentaciones (en persona o por videollamada) con colegas de ventas, marketing y soporte.
8. **Sesión introductoria de producto** – Demo de 45–60 minutos del producto/servicio principal a cargo de un vendedor senior.
9. **Almuerzo con el equipo** – Espacio informal para conocer a los compañeros y resolver dudas sin presión.
10. **Cierre del día y plan de la semana** – Revisar con el manager lo visto, entregar el plan de lecturas y agendar las sesiones de la semana.

---

## (3) Glosario de 8 términos internos clave

| Término | Definición |
|---|---|
| **ICP (Ideal Customer Profile)** | Perfil del cliente ideal: tamaño, sector, presupuesto y necesidades que mejor encajan con nuestra oferta. Toda prospección debe partir de aquí. |
| **Pipeline** | Conjunto de oportunidades abiertas en el CRM, organizadas por etapa. Se revisa cada semana en el *pipeline review*. |
| **MQL / SQL** | *Marketing Qualified Lead* (lead calificado por marketing) y *Sales Qualified Lead* (lead validado por ventas tras un primer contacto). Solo los SQL cuentan en el pipeline. |
| **Discovery call** | Primera llamada con un prospecto para entender su situación, problema y presupuesto antes de hacer una demo. |
| **Forecast** | Proyección de ventas del mes/trimestre basada en el pipeline. Se actualiza los viernes y debe ser realista, no optimista. |
| **Deal desk** | Equipo interno que aprueba descuentos, condiciones especiales y contratos no estándar. Nada fuera de la lista de precios se envía sin pasar por aquí. |
| **Handoff** | Traspaso formal de un cliente cerrado al equipo de Customer Success, con documentación de lo prometido durante la venta. |
| **Quota** | Objetivo de ventas asignado por período (mensual/trimestral). Base para el cálculo de comisiones. |

*(Ajusta las definiciones si tu empresa usa estos términos de forma distinta o añade los propios.)*

---

## (4) Plan de lecturas de la primera semana

| Día | Documento | Descripción |
|---|---|---|
| **Lunes** | **Manual del empleado y cultura de [Empresa]** | Misión, valores, políticas internas (horarios, gastos, vacaciones, código de conducta). Base para entender cómo funcionamos. |
| **Martes** | **Guía de producto y propuesta de valor** | Descripción de cada producto/servicio, beneficios clave, diferenciadores frente a la competencia y preguntas frecuentes de clientes. |
| **Miércoles** | **Playbook de ventas** | Nuestro proceso comercial paso a paso: prospección, discovery, demo, propuesta, negociación y cierre. Incluye guiones y plantillas de correo. |
| **Jueves** | **Manual del CRM y reglas de registro** | Cómo crear oportunidades, actualizar etapas, registrar actividades y mantener el pipeline limpio. Qué campos son obligatorios y por qué. |
| **Viernes** | **Casos de éxito y perfiles de cliente** | 3–5 historias de clientes reales con el problema, la solución y los resultados. Útil para construir argumentos y referencias en las primeras llamadas. |

**Sugerencia:** al terminar cada lectura, anotar 3 preguntas para tratar en el 1:1 del viernes.

---

## (5) Mensaje de Slack del manager (primer día)

> 👋 ¡Hola, [Nombre]! Bienvenido/a oficialmente al equipo de ventas de [Empresa]. 🎉
>
> Estoy muy contento/a de tenerte con nosotros. Hoy el objetivo es simple: que tengas todo configurado, conozcas a la gente y te vayas a casa con una idea clara de cómo trabajamos. Nada de presión por resultados esta semana.
>
> Un par de cosas prácticas:
> • A las 10:00 tenemos nuestro primer 1:1 (te envié la invitación al calendario).
> • Si tienes problemas con accesos o equipo, escribe en #it-soporte y te ayudan rápido.
> • Únete a #ventas, #ventas-wins y #random para ir conociendo el ambiente.
> • A las 13:00 comemos juntos con el equipo, tú invitado/a 🍽️
>
> Cualquier duda, por pequeña que sea, escríbeme por aquí. Prefiero mil preguntas a una suposición equivocada.
>
> ¡Vamos con todo! 💪
> [Nombre del manager]

---

✅ **Los 5 sub-objetivos están completos.** Si me compartes el nombre de la empresa, del vendedor y del manager, puedo personalizar todos los textos y ajustar el glosario a tu vocabulario interno real.

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

Revisé el paquete y **los 5 sub-objetivos ya están completos** en mi respuesta anterior. Te confirmo el estado de cada uno:

| # | Sub-objetivo | Estado | Dónde está |
|---|---|---|---|
| 1 | Carta de bienvenida personalizada (150 palabras) | ✅ Completo | Sección (1) – ~150 palabras, con campos `[ ]` para nombre y empresa |
| 2 | Lista de los 10 primeros pasos del Día 1 | ✅ Completo | Sección (2) – 10 pasos numerados, de llegada a cierre del día |
| 3 | Glosario de 8 términos internos clave | ✅ Completo | Sección (3) – ICP, Pipeline, MQL/SQL, Discovery call, Forecast, Deal desk, Handoff, Quota |
| 4 | Plan de lecturas de la primera semana (5 documentos) | ✅ Completo | Sección (4) – 5 documentos, uno por día, cada uno con descripción |
| 5 | Mensaje de Slack del manager para el primer día | ✅ Completo | Sección (5) – mensaje listo para copiar y pegar |

No falta ninguno, así que no hay nada que "continuar".

Si lo que necesitas es alguno de estos ajustes, dímelo y lo hago de inmediato:

- **Personalizar** con el nombre de la empresa, del vendedor y del manager (así desaparecen los corchetes).
- **Adaptar el glosario** a los términos reales que usa tu empresa (si me pasas tu vocabulario interno).
- **Cambiar el tono** de la carta o del Slack (más formal, más informal, más breve).
- **Ampliar** algún punto (por ejemplo, convertir el plan de lecturas en un calendario con horarios, o añadir un plan 30/60/90 días).
- **Entregar todo en un solo documento** sin tablas, listo para pegar en Word o Google Docs.

¿Quieres que proceda con alguno de estos?


## Respuesta completa

Revisé el paquete y **los 5 sub-objetivos ya están completos** en mi respuesta anterior. Te confirmo el estado de cada uno:

| # | Sub-objetivo | Estado | Dónde está |
|---|---|---|---|
| 1 | Carta de bienvenida personalizada (150 palabras) | ✅ Completo | Sección (1) – ~150 palabras, con campos `[ ]` para nombre y empresa |
| 2 | Lista de los 10 primeros pasos del Día 1 | ✅ Completo | Sección (2) – 10 pasos numerados, de llegada a cierre del día |
| 3 | Glosario de 8 términos internos clave | ✅ Completo | Sección (3) – ICP, Pipeline, MQL/SQL, Discovery call, Forecast, Deal desk, Handoff, Quota |
| 4 | Plan de lecturas de la primera semana (5 documentos) | ✅ Completo | Sección (4) – 5 documentos, uno por día, cada uno con descripción |
| 5 | Mensaje de Slack del manager para el primer día | ✅ Completo | Sección (5) – mensaje listo para copiar y pegar |

No falta ninguno, así que no hay nada que "continuar".

Si lo que necesitas es alguno de estos ajustes, dímelo y lo hago de inmediato:

- **Personalizar** con el nombre de la empresa, del vendedor y del manager (así desaparecen los corchetes).
- **Adaptar el glosario** a los términos reales que usa tu empresa (si me pasas tu vocabulario interno).
- **Cambiar el tono** de la carta o del Slack (más formal, más informal, más breve).
- **Ampliar** algún punto (por ejemplo, convertir el plan de lecturas en un calendario con horarios, o añadir un plan 30/60/90 días).
- **Entregar todo en un solo documento** sin tablas, listo para pegar en Word o Google Docs.

¿Quieres que proceda con alguno de estos?