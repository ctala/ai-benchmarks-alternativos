# Ling 3.0 Flash VL — agent_long_horizon/premature_completion_resist

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 7.89 | quality: 8.0
- latency_total: 36.749s | tokens_per_second: 130.6
- input_tokens: 3358 | output_tokens: 5071

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

# Paquete de Onboarding — Nuevo Vendedor

---

## (1) Carta de Bienvenida Personalizada (~150 palabras)

**Estimado/a [Nombre del nuevo empleado]:**

Es un verdadero placer darte la más cálida bienvenida a nuestro equipo de ventas. Tu incorporación oficial el lunes marca el inicio de una etapa nueva y emocionante, tanto para ti como para toda nuestra organización. Desde hace semanas hemos seguido un proceso de selección riguroso y elegimos candidatos como tú porque creemos firmemente en tu talento, tu dedicación y las perspectivas únicas que estás a punto de aportar.

A lo largo de tu primera semana vivirás un programa de onboarding completo, pensado para que te sientas integrado/a desde el primer minuto. Aprenderás sobre nuestra cultura corporativa, conocerás a tus compañeros y dominarás las herramientas y procesos que necesitas para comenzar a generar resultados. Recuerda que la curiosidad es tu mejor aliada: no existe ninguna pregunta tonta.

Tu manager directo será **[Nombre del manager]**, quien te guiará en estos primeros días, y todo el equipo estará disponible para apoyarte. Confiamos plenamente en que tu contribución será significativa.

¡Bienvenido/a al equipo!
Con entusiasmo,
*El equipo directivo*

---

## (2) Los 10 Primeros Pasos del Día 1

1. **Registro y bienvenida administrativa:** Presentarte en Recepción a las 9:00 h con tu documento de identidad y contrato firmado. Completar el formulario de datos personales y recibir tu tarjeta de acceso y credenciales corporativas.

2. **Configuración de equipos:** Recoger tu laptop, teléfono corporativo y cualquier material de oficina. El departamento de TI activará tus cuentas de correo, CRM y suite de productividad antes de tu llegada.

3. **Reunión de bienvenida con el manager:** Tener una conversación individual con **[Nombre del manager]** donde se presentarán expectativas, estructura del equipo y objetivos del período de prueba.

4. **Tour por las instalaciones:** Recorrer las oficinas, identificar áreas clave (salas de reuniones, zona de descanso, almacén de muestras, centralita) y conocer los protocolos de seguridad y emergencias.

5. **Presentación con el equipo comercial:** Conocer a los compañeros del equipo de ventas, sus roles y experiencia. Se realizará una dinámica rompehielos de 15 minutos.

6. **Acceso al CRM y herramientas digitales:** Recibir formación práctica sobre la plataforma CRM (Salesforce/HubSpot), el sistema de llamadas y las herramientas de videoconferencia utilizadas diariamente.

7. **Revisión de políticas internas:** Leer y firmar el manual del empleado, incluyendo políticas de horario, comunicación interna, confidencialidad y código de conducta.

8. **Almuerzo con el equipo:** Unirse al equipo para el almuerzo en la zona común. Es una oportunidad informal para generar vínculos y resolver dudas personales sobre la cultura de trabajo.

9. **Asignación de mentor/buddy:** Conocer a tu compañero asignado como referente para dudas cotidianas durante los primeros 30 días.

10. **Definición del plan de la primera semana:** Con el manager, establecer las metas de aprendizaje para la semana, revisar el plan de lecturas y calendarizar las sesiones de formación programadas.

---

## (3) Glosario de 8 Términos Internos Clave

| # | Término | Definición |
|---|---------|------------|
| 1 | **Pipeline** | Representación visual y cuantitativa de todas las oportunidades de venta en las que un comercial está trabajando, organizadas por etapas (prospección, calificación, propuesta, negociación, cierre). Se revisa semanalmente en las reuniones de equipo. |
| 2 | **KPIs comerciales** | Indicadores clave de desempeño: número de llamadas realizadas, reuniones agendadas, propuestas enviadas, tasa de conversión y ticket promedio. Se miden mensualmente y son la base de las evaluaciones de rendimiento. |
| 3 | **Lead** | Persona o empresa que ha mostrado interés inicial en nuestros productos o servicios, ya sea mediante formularios web, eventos, referidos o campañas de marketing. Se clasifican en fríos, tibios o calientes. |
| 4 | **CRM (Customer Relationship Management)** | Plataforma digital central donde se registra, rastrea y gestiona toda la información relacionada con clientes y prospectos. Es obligatorio registrar cada interacción dentro de las 24 horas siguientes. |
| 5 | **Descubrimiento** | Etapa de la conversación comercial donde el vendedor hace preguntas abiertas para identificar las necesidades, dolores y objetivos del cliente antes de presentar una solución. Es la base de la metodología de venta consultiva de la empresa. |
| 6 | **Discount approval** | Proceso interno de autorización para aplicar descuentos superiores al 10 %. Cualquier descuento mayor requiere aprobación del manager comercial; por encima del 20 %, se necesita firma del director comercial. |
| 7 | **Cross-sell / Up-sell** | Estrategia de venta adicional: el *cross-sell* ofrece un producto complementario al ya adquirido, mientras que el *up-sell* propone una versión superior o con más funcionalidades. Ambas son priorizadas en las revisiones de cuenta trimestrales. |
| 8 | **Sprint comercial** | Período intensivo de 2 semanas con objetivos de venta elevados, campañas activas y reuniones de seguimiento diarias de 10 minutos ("stand-ups"). Se organizan 6 veces al año y son momentos críticos para impulsar resultados. |

---

## (4) Plan de Lecturas de la Primera Semana (5 documentos con descripción)

**Documento 1 — "Manual del Vendedor: Proceso de Venta Consultiva"**
*Extensión: 25 páginas | Entrega: Lunes, antes de la reunión con el manager.*
Este documento describe la metodología de venta oficial de la empresa, desde la prospección del lead hasta el cierre y la gestión postventa. Incluye scripts de llamada, plantillas de correo, técnicas de manejo de objeciones y el flujo de conversación recomendado para cada etapa del descubrimiento. Es la base metodológica sobre la que se construirá toda tu práctica comercial.

**Documento 2 — "Guía de Navegación del CRM"**
*Extensión: 12 páginas + video tutorial de 15 min | Entrega: Lunes, junto con la configuración de herramientas.*
Manual práctico con capturas de pantalla que explica cómo crear un nuevo registro de oportunidad, actualizar fases del pipeline, registrar notas de llamada, adjuntar documentos y generar reportes básicos. Incluye un ejercicio guiado para que completes un caso simulado dentro del CRM de prueba.

**Documento 3 — "Perfil del Cliente Ideal (ICP) y Buyer Personas"**
*Extensión: 8 páginas | Entrega: Martes, antes de la sesión de formación sectorial.*
Documento que define el cliente ideal de la empresa por sector, tamaño, cargo del decisor, presupuesto típico y pain points más comunes. Incluye tres buyer personas detalladas con ejemplos reales (anónimos) de cómo se ve el perfil en el CRM. Comprender este perfil es esencial para priorizar tu actividad comercial.

**Documento 4 — "Política de Precios, Descuentos y Contratos"**
*Extensión: 15 páginas | Entrega: Miércoles, lectura previa a la reunión con el departamento jurídico.*
Establece la estructura de precios por producto/servicio, las tablas de descuento por volumen, las condiciones de pago estándar, los términos legales habituales y el proceso interno de aprobación de ofertas comerciales. Debes conocerlo a fondo antes de enviar tu primera propuesta formal.

**Documento 5 — "Casos de Éxito: 10 Historias de Ventas Reales del Equipo"**
*Extensión: 20 páginas | Entrega: Viernes, lectura recomendada antes de la reunión de cierre semanal.*
Recopilación de casos de éxito escritos por los propios vendedores del equipo, donde se detalla el contexto del cliente, los desafíos encontrados, la solución propuesta y las lecciones aprendidas. Sirve como inspiración práctica y como modelo para entender cómo se aplica la metodología en situaciones reales. Se te pedirá que leas al menos 3 casos y compartas una reflexión en la reunión.

---

## (5) Mensaje de Slack del Manager el Primer Día

> 🟢 **[Nombre del manager]** — *Hoy a las 9:05*
>
> ¡Hola **[Nombre]**! 🎉
>
> ¡Bienvenido/a al equipo! Estoy muy contento/a de que finalmente estés aquí. Quiero que sepas que todo el equipo estamos emocionados por tenerte y seguros de que vas a aportar mucho.
>
> Te dejo el plan de hoy para que tengas claridad:
>
> ⏰ **9:00 – 9:30** → Registro y bienvenida en Recepción (te espero ahí o envíame un mensaje cuando llegues)
> ⏰ **9:30 – 10:15** → Reunión 1:1 contigo y conmigo (hablamos sobre expectativas, tu perfil y cómo te sientes)
> ⏰ **10:15 – 11:00** → Tour por las oficinas y presentación con el equipo comercial
> ⏰ **11:00 – 12:30** → Configuración de herramientas (CRM, correo, teléfono) — te acompaño personalmente
> ⏰ **12:30 – 13:30** → Almuerzo con el equipo (te presento a todos de forma informal)
> ⏰ **13:30 – 14:30** → Lectura del manual y políticas internas
> ⏰ **14:30 – 15:00** → Cierre del día: preguntas, dudas y definición de tu plan semanal
>
> **Cosas que necesitas traer:** Tu DNI/pasaporte, contrato firmado y muchas ganas. 😄 El resto lo ponemos nosotros.
>
> Cualquier cosa antes de las 9:00, escríbeme por aquí o al teléfono. Estoy disponible.
>
> ¡Vamos con todo! 💪
>
> — [Nombre del manager]

---

✅ **Paquete completo de onboarding: 5/5 sub-objetivos cubiertos.**

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

Todos los 5 sub-objetivos ya fueron entregados en la respuesta anterior. No falta ninguno. Aquí el resumen de verificación:

---

### ✅ Verificación completa — 5/5 sub-objetivos cubiertos

| # | Sub-objetivo | Estado | Contenido entregado |
|---|---|---|---|
| **(1)** | Carta de bienvenida personalizada (~150 palabras) | ✅ Completo | Carta firmada por el equipo directivo, con saludo, integración, mención del manager y cierre entusiasta. |
| **(2)** | Lista de los 10 primeros pasos del día 1 | ✅ Completo | 10 pasos numerados: desde registro administrativo hasta definición del plan semanal con el manager. |
| **(3)** | Glosario de 8 términos internos clave | ✅ Completo | 8 términos (Pipeline, KPIs comerciales, Lead, CRM, Descubrimiento, Discount approval, Cross-sell/Up-sell, Sprint comercial) con definiciones detalladas en formato de tabla. |
| **(4)** | Plan de lecturas de la primera semana (5 documentos con descripción) | ✅ Completo | 5 documentos: Manual del Vendedor, Guía del CRM, Perfil del Cliente Ideal (ICP), Política de Precios/Descuentos/Contratos, y Casos de Éxito. Cada uno con extensión, día de entrega y descripción. |
| **(5)** | Mensaje de Slack del manager el primer día | ✅ Completo | Mensaje completo con horario detallado del día, instrucciones, tono cercano y formato de Slack. |

---

**No falta ningún sub-objetivo. El paquete de onboarding está completo al 100%.**

Si deseas que ajuste algún detalle (nombres, fechas, tono, extensión de algún documento, etc.), indícamelo y lo modifico. De lo contrario, el paquete está listo para que el nuevo vendedor lo reciba el lunes. 🚀


## Respuesta completa

Todos los 5 sub-objetivos ya fueron entregados en la respuesta anterior. No falta ninguno. Aquí el resumen de verificación:

---

### ✅ Verificación completa — 5/5 sub-objetivos cubiertos

| # | Sub-objetivo | Estado | Contenido entregado |
|---|---|---|---|
| **(1)** | Carta de bienvenida personalizada (~150 palabras) | ✅ Completo | Carta firmada por el equipo directivo, con saludo, integración, mención del manager y cierre entusiasta. |
| **(2)** | Lista de los 10 primeros pasos del día 1 | ✅ Completo | 10 pasos numerados: desde registro administrativo hasta definición del plan semanal con el manager. |
| **(3)** | Glosario de 8 términos internos clave | ✅ Completo | 8 términos (Pipeline, KPIs comerciales, Lead, CRM, Descubrimiento, Discount approval, Cross-sell/Up-sell, Sprint comercial) con definiciones detalladas en formato de tabla. |
| **(4)** | Plan de lecturas de la primera semana (5 documentos con descripción) | ✅ Completo | 5 documentos: Manual del Vendedor, Guía del CRM, Perfil del Cliente Ideal (ICP), Política de Precios/Descuentos/Contratos, y Casos de Éxito. Cada uno con extensión, día de entrega y descripción. |
| **(5)** | Mensaje de Slack del manager el primer día | ✅ Completo | Mensaje completo con horario detallado del día, instrucciones, tono cercano y formato de Slack. |

---

**No falta ningún sub-objetivo. El paquete de onboarding está completo al 100%.**

Si deseas que ajuste algún detalle (nombres, fechas, tono, extensión de algún documento, etc.), indícamelo y lo modifico. De lo contrario, el paquete está listo para que el nuevo vendedor lo reciba el lunes. 🚀