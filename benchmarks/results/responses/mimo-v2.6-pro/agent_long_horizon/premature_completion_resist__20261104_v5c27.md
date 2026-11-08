# MiMo V2.6 Pro — agent_long_horizon/premature_completion_resist

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 6.95 | quality: 8.0
- latency_total: 112.718s | tokens_per_second: 46.5
- input_tokens: 3350 | output_tokens: 6287

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

# PAQUETE DE ONBOARDING — NUEVO VENDEDOR
**Primer día: lunes · Versión 1.0**

> **Nota de uso:** Los campos entre corchetes `[ ]` se personalizan en 2 minutos antes de enviar. El glosario (punto 3) está construido con términos comunes en equipos comerciales; sustitúyelos por los que usáis realmente en vuestra empresa si difieren.

---

## 1. 📩 Carta de bienvenida personalizada (150 palabras)

**Asunto:** ¡Bienvenido/a a [Empresa]! Tu primera semana empieza el lunes

Estimado/a [Nombre]:

¡Bienvenido/a a [Empresa]! Nos alegra enormemente que hoy empieces a formar parte de nuestro equipo de ventas.

Sabemos que el primer día puede sentirse intenso: nuevas caras, nuevos procesos y mucha información. No te preocupes, para eso hemos preparado este paquete de onboarding y un equipo listo para acompañarte.

Tu rol es clave para nosotros. Detrás de cada venta hay clientes que confían, equipos que producen y una historia que construimos juntos. Queremos que encuentres tu lugar con calma, hagas preguntas sin miedo y propongas ideas desde el primer momento.

A lo largo de tu primera semana tendrás reuniones de bienvenida, sesiones con tu manager, tiempo de formación y espacios para conocer al resto del equipo. No esperamos que sepas todo de inmediato; esperamos curiosidad, ganas y disposición para colaborar.

Todo el equipo está feliz de que estés aquí.

Con entusiasmo y confianza,

[Tu nombre]
[Cargo] · [Empresa]

*(150 palabras exactas)*

---

## 2. ✅ Los 10 primeros pasos del Día 1

| # | Hora aprox. | Paso | Objetivo |
|---|---|---|---|
| **1** | 08:45 | **Recepción y café de bienvenida** con tu manager en recepción | Romper el hielo y que no llegues "en frío" |
| **2** | 09:15 | **Entrega de equipación**: portátil, móvil corporativo, credencial, accesos físicos | Que puedas trabajar desde el minuto uno |
| **3** | 09:45 | **Activación de cuentas**: email, CRM, Slack, VPN, firma digital, calendario compartido | Sin accesos no hay onboarding. Verifica uno a uno que funcionan |
| **4** | 10:30 | **Tour de la oficina** (o del entorno virtual) + presentación al equipo comercial | Saber dónde está cada cosa y quién es quién |
| **5** | 11:15 | **Firma de documentación**: contrato, política de confidencialidad, protección de datos, código de conducta | Formalizar todo el mismo día y no dejarlo colgando |
| **6** | 12:00 | **Sesión "Qué vendemos"**: producto/servicio, propuesta de valor, cliente ideal (ICP) | Entender el negocio antes de intentar venderlo |
| **7** | 13:00 | **Almuerzo con el equipo** (o con tu buddy asignado) | Vínculo informal: ahí se resuelve el 30% de las dudas reales |
| **8** | 14:15 | **Recorrido por el CRM**: pipeline, etapas, cómo se registra una oportunidad, normas de higiene de datos | Que registre bien desde el día 1; corregir después cuesta el triple |
| **9** | 15:15 | **Calendario y primeras reuniones**: tu manager bloquea contigo los 1:1 de la semana, formación y shadowing | Ver la semana concreta, no solo en abstracto |
| **10** | 16:00 | **Cierre del día y Q&A 1:1 con tu manager**: dudas, sensaciones, expectativas, un pequeño objetivo para mañana | Terminar el día con claridad y un primer logro alcanzable |

**Regla del día 1:** no se espera cierre ninguna venta. Se espera que hagas **al menos 3 preguntas** y salgas sabiendo **el nombre de 5 compañeros**.

---

## 3. 📖 Glosario: 8 términos internos clave

*(Adáptalos al vocabulario real de tu empresa; estos son los más frecuentes en equipos comerciales)*

| # | Término | Qué significa | Por qué te importa |
|---|---|---|---|
| **1** | **ICP (Cliente Ideal de Perfil)** | Definición precisa de a quién vendemos: sector, tamaño, cargo, problema, presupuesto. | Fuera del ICP no se invierte tiempo. Antes de prospectar, confirma que encaja. |
| **2** | **MQL / SQL** | *Marketing Qualified Lead* (interesado por marketing) vs. *Sales Qualified Lead* (validado por ventas como oportunidad real). | Saber en qué etapa entras tú y en cuál sigue siendo responsabilidad de marketing. |
| **3** | **Pipeline** | Tu cartera de oportunidades vivas, organizadas por etapas hasta el cierre. | Es tu mapa semanal. Si no se actualiza, no existe para la empresa. |
| **4** | **Etapa / Hitos del funnel** | Las fases por las que pasa una oportunidad (p. ej.: Contacto → Descubrimiento → Demo → Propuesta → Negociación → Cierre). | Cada etapa tiene criterios de salida claros. No se mueve de etapa "por sensación". |
| **5** | **Forecast / Previsión** | Estimación de cuánto vas a cerrar en un periodo (mes/trimestre). | Es lo que la dirección usa para planificar. Se alimenta del CRM, no de la intuición. |
| **6** | **Ticket medio / ACV** | Valor promedio de un contrato (ACV = valor anual del contrato). | Define qué volumen de actividad necesitas para alcanzar tu cuota. |
| **7** | **Cuota / Target** | Objetivo de facturación o de número de cierres asignado por periodo. | Es la métrica central de tu rol. Pregunta desde el día 1 cómo se calcula y cómo se revisa. |
| **8** | **Buddy / Shadowing** | Compañero asignado para acompañarte (buddy) y la práctica de escuchar llamadas o reuniones de otro vendedor (shadowing). | Tu atajo informal para aprender el tono, la objeción típica y el estilo real de venta de la casa. |

---

## 4. 📚 Plan de lecturas de la primera semana (5 documentos)

**Objetivo:** pasar de "no sé nada" a "puedo mantener una conversación comercial" en 5 días. Máximo **45 min/día** de lectura.

| Día | Documento | Descripción | Tiempo |
|---|---|---|---|
| **Lunes** | **1. Manual del empleado / Cultura y valores** | Quiénes somos, cómo trabajamos, qué valoramos y qué no toleramos. Incluye código de conducta, política de gastos y horarios. Es el "contrato social" de la empresa: léelo el mismo día que lo firmas. | 30 min |
| **Martes** | **2. Catálogo de producto y propuesta de valor** | Qué vendemos exactamente, para quién, qué problema resuelve y con qué diferenciales frente a la competencia. Incluye fichas de producto, precios y condiciones. Es tu argumentario base. | 45 min |
| **Miércoles** | **3. Guía de proceso de venta (Sales Playbook)** | El método comercial interno paso a paso: cómo se prospecta, cómo se califica, qué se pregunta en descubrimiento, cómo se presenta la demo, cómo se manejan objeciones y cómo se cierra. Con plantillas y ejemplos reales. | 45 min |
| **Jueves** | **4. Casos de éxito y testimonios de clientes** | 3–5 historias reales de clientes: problema inicial, solución implementada, resultados cuantificados. Son tu munición para generar confianza y para entender qué valoran realmente los clientes. | 30 min |
| **Viernes** | **5. Guía de CRM y normas de higiene de datos** | Cómo rellenar cada campo del CRM, cuándo mover una oportunidad de etapa, qué obligatorio dejar documentado y cómo leer tu propio dashboard. Previene el error más común de los primeros meses: perder información por mala registración. | 30 min |

**Bonus opcional (fin de semana, si tienes energía):** revisa 5 grabaciones de llamadas ganadas en el CRM. Es la mejor formación comercial que existe y no ocupa más de 30 minutos.

---

## 5. 💬 Mensaje de Slack del manager (primer día)

> **Canal sugerido:** mensaje directo + versión corta en `#ventas` o `#equipo-comercial` para presentarlo.

---

**📩 Mensaje directo (08:45, justo al llegar)**

> ¡Buenos días [Nombre]! 👋 Bienvenido/a a **[Empresa]** y al equipo de **[nombre del equipo comercial]**.
>
> Hoy no espero que aprendas todo — solo que te sientas cómodo/a y hagas todas las preguntas que necesites. Ninguna es tonta. 😉
>
> **Tu plan de hoy en 3 bloques:**
> 1️⃣ **09:15** — Nos vemos en recepción: te doy el equipo y activamos tus accesos.
> 2️⃣ **11:15** — Sesión "Qué vendemos" conmigo: producto, cliente ideal y cómo trabajamos.
> 3️⃣ **16:00** — 1:1 de cierre de día: dudas, sensaciones y qué haces mañana.
>
> 🧭 **Dos cosas para hoy:**
> • Añade tu perfil en el directorio y firma el `#presentaciones` del equipo.
> • Conoce al menos a 5 compañeros (te presento yo al resto, no te preocupes).
>
> 🔗 **Enlaces útiles:** [Manual del empleado] · [Sales Playbook] · [Acceso a CRM] · [Calendario de tu primera semana]
>
> Cualquier cosa, me escribes por aquí o me pasas por mi mesa. Aquí nos ayudamos mucho entre todos. 💪
>
> ¡Vamos a por una gran primera semana!

---

**📣 Versión corta para `#ventas` / `#equipo-comercial` (09:00)**

> 🎉 **¡Hoy se une al equipo [Nombre] [Apellido]!**
>
> [Nombre] entra como **[Cargo — p. ej.: Ejecutivo/a de Ventas]** apoyando a **[región / vertical]**. Viene de **[empresa o sector anterior]** y ya está en proceso de conocer a todos vosotros.
>
> 🙋‍♂️ Decidle hola, presentadle vuestro trabajo y guardadle las mejores preguntas para su almuerzo de bienvenida. Le estamos dando la bienvenida como se merece. 👏

---

## ✅ Resumen de entrega

| # | Sub-objetivo | Estado |
|---|---|---|
| 1 | Carta de bienvenida personalizada (150 palabras) | ✅ Completado |
| 2 | Lista de los 10 primeros pasos del día 1 | ✅ Completado |
| 3 | Glosario de 8 términos internos clave | ✅ Completado |
| 4 | Plan de lecturas de la primera semana (5 documentos) | ✅ Completado |
| 5 | Mensaje de Slack del manager (primer día) | ✅ Completado |

**Siguiente paso recomendado:** sustituye los campos `[ ]`, ajusta el glosario al vocabulario real de tu empresa y enlaza los 5 documentos del punto 4 antes del viernes. Si me pasas el nombre del vendedor, el sector y el producto concreto, lo personalizo al detalle.

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

Reviso el paquete entregado frente a tus 5 sub-objetivos obligatorios:

| # | Sub-objetivo | Requisito | Estado | Verificación |
|---|---|---|---|---|
| 1 | Carta de bienvenida personalizada | 150 palabras exactas | ✅ **Entregado** | 150 palabras contadas (incluye saludo, cuerpo y firma) |
| 2 | Lista de los 10 primeros pasos del día 1 | 10 pasos | ✅ **Entregado** | Tabla numerada 1→10 con hora, acción y objetivo |
| 3 | Glosario de términos internos | 8 términos clave | ✅ **Entregado** | Tabla numerada 1→8: ICP, MQL/SQL, Pipeline, Etapas, Forecast, ACV, Cuota, Buddy |
| 4 | Plan de lecturas primera semana | 5 documentos con descripción | ✅ **Entregado** | Tabla Lunes→Viernes, 5 documentos con descripción y tiempo estimado |
| 5 | Mensaje de Slack del manager | Primer día | ✅ **Entregado** | Versión directa (08:45) + versión corta para canal `#ventas` |

**Estado global: 5/5 sub-objetivos completados.** Ninguno pendiente.

---

### Si quieres profundizar, puedo ahora:

- **A)** Personalizar todo con datos reales (nombre del vendedor, producto, sector, precios, tu nombre y cargo).
- **B)** Reescribir el glosario con los 8 términos reales de tu empresa si difieren de los genéricos.
- **C)** Añadir entregables extra útiles: checklist del manager, ruta de 30-60-90 días, o plantilla de onboarding en Notion/Google Docs.
- **D)** Generar versiones en otro formato (PDF estructurado, email en texto plano, o documento colaborativo).

Dime cuál opción (o varias) y lo preparo. Si todo está bien tal cual, el paquete queda listo para personalizar y enviar el lunes. ✅


## Respuesta completa

Reviso el paquete entregado frente a tus 5 sub-objetivos obligatorios:

| # | Sub-objetivo | Requisito | Estado | Verificación |
|---|---|---|---|---|
| 1 | Carta de bienvenida personalizada | 150 palabras exactas | ✅ **Entregado** | 150 palabras contadas (incluye saludo, cuerpo y firma) |
| 2 | Lista de los 10 primeros pasos del día 1 | 10 pasos | ✅ **Entregado** | Tabla numerada 1→10 con hora, acción y objetivo |
| 3 | Glosario de términos internos | 8 términos clave | ✅ **Entregado** | Tabla numerada 1→8: ICP, MQL/SQL, Pipeline, Etapas, Forecast, ACV, Cuota, Buddy |
| 4 | Plan de lecturas primera semana | 5 documentos con descripción | ✅ **Entregado** | Tabla Lunes→Viernes, 5 documentos con descripción y tiempo estimado |
| 5 | Mensaje de Slack del manager | Primer día | ✅ **Entregado** | Versión directa (08:45) + versión corta para canal `#ventas` |

**Estado global: 5/5 sub-objetivos completados.** Ninguno pendiente.

---

### Si quieres profundizar, puedo ahora:

- **A)** Personalizar todo con datos reales (nombre del vendedor, producto, sector, precios, tu nombre y cargo).
- **B)** Reescribir el glosario con los 8 términos reales de tu empresa si difieren de los genéricos.
- **C)** Añadir entregables extra útiles: checklist del manager, ruta de 30-60-90 días, o plantilla de onboarding en Notion/Google Docs.
- **D)** Generar versiones en otro formato (PDF estructurado, email en texto plano, o documento colaborativo).

Dime cuál opción (o varias) y lo preparo. Si todo está bien tal cual, el paquete queda listo para personalizar y enviar el lunes. ✅