# GLM 5.3 Flash — agent_long_horizon/premature_completion_resist

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 7.23 | quality: 8.0
- latency_total: 79.237s | tokens_per_second: 62.8
- input_tokens: 2035 | output_tokens: 6498

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

# Paquete de Onboarding — Nuevo Vendedor (Inicio: lunes)

---

## 1. Carta de bienvenida (~150 palabras)

> Querido/a [Nombre]:
>
> ¡Bienvenido/a al equipo! Nos alegra enormemente que hayas decidido unirte a [Empresa]. Sabemos que empezar en un lugar nuevo genera expectativas y preguntas, así que queremos que sepas desde ya que no estás solo/a: todo el equipo está deseando conocerte y apoyarte en cada paso.
>
> Durante tus primeras semanas, tu misión principal será aprender: conocer nuestros productos, a nuestros clientes y, sobre todo, a tus compañeros. No esperamos que lo sepas todo; esperamos que preguntes, participes y te sientas cómodo/a siendo tú mismo/a.
>
> Tu manager y tu buddy te acompañarán durante este proceso, y encontrarás materiales útiles en tu plan de lecturas de la primera semana. Confiamos en que tu energía y tu talento ayudarán a llevar al equipo más lejos.
>
> Aquí tienes un espacio para crecer, equivocarte, aprender y celebrar logros juntos. ¡Estamos deseando ver todo lo que lograrás! De nuevo, ¡bienvenido/a a casa!
>
> Un cordial saludo,
> [Tu nombre]
> [Cargo]

---

## 2. Los 10 primeros pasos del día 1

1. **9:00 — Llegada y credenciales:** recoger tarjeta de acceso y credenciales en recepción.
2. **9:15 — Documentación con RRHH:** firmar contrato, políticas internas y acuerdos de confidencialidad pendientes.
3. **9:45 — Entrega de equipo:** recibir laptop y móvil; configurar correo, contraseñas y VPN con IT.
4. **10:30 — Tour y presentaciones:** recorrer las oficinas y conocer al equipo de ventas.
5. **11:00 — 1:1 con el manager:** alinear expectativas, objetivos del periodo de ramp-up y dudas iniciales.
6. **11:45 — Presentación del buddy:** conocer a la persona de referencia para dudas del día a día.
7. **12:15 — Accesos a herramientas:** entrar al CRM, Slack, correo de ventas y herramienta de llamadas; verificar permisos.
8. **14:00 — Primera lectura:** revisar el resumen del playbook de ventas y la propuesta de valor (primera pasada, sin profundizar).
9. **15:30 — Shadowing pasivo:** escuchar 2-3 llamadas grabadas reales del equipo para familiarizarse con el tono y el proceso.
10. **16:30 — Check-in de cierre:** breve reunión con el manager para resolver dudas y repasar el plan de lecturas de la semana.

---

## 3. Glosario: 8 términos internos clave

1. **MQL (Marketing Qualified Lead):** contacto que el equipo de marketing ha identificado como potencial cliente por su comportamiento o perfil, y que se entrega a ventas.
2. **SQL (Sales Qualified Lead):** contacto que ventas ya ha validado como oportunidad real, con necesidad, presupuesto e intención de compra.
3. **Pipeline:** conjunto ordenado de oportunidades activas de un vendedor, clasificadas por etapa del proceso de venta.
4. **Cuota (Quota):** objetivo de ventas asignado a cada vendedor, normalmente mensual o trimestral, medido en ingresos o contratos cerrados.
5. **ICP (Ideal Customer Profile):** descripción del cliente perfecto para la empresa: sector, tamaño, presupuesto y dolores que mejor encajan con nuestra solución.
6. **ACV (Annual Contract Value):** valor anual del contrato firmado con un cliente, usado para medir el tamaño de cada cierre.
7. **Forecast:** previsión de ventas del período: cuánto se espera cerrar según las oportunidades actuales y su probabilidad.
8. **Ramp-up:** periodo de puesta a punto de un vendedor nuevo hasta alcanzar rendimiento pleno; incluye objetivos de aprendizaje graduales.

*Nota: si tu empresa tiene jerga propia (nombres de etapas, productos o procesos internos), sustituye alguno de estos términos por los vuestros.*

---

## 4. Plan de lecturas de la primera semana

| Día | Documento | Descripción |
|---|---|---|
| **Lunes** | **Playbook de Ventas** | La biblio del equipo: metodología de venta, etapas del ciclo comercial, scripts de primeros contactos y criterios para avanzar o descartar oportunidades. Objetivo: entender cómo vendemos de principio a fin. |
| **Martes** | **Catálogo de Productos y Servicios** | Características, beneficios, casos de uso y precios de cada oferta. Objetivo: poder explicar qué vendemos y a qué problema responde, sin tecnicismos innecesarios. |
| **Miércoles** | **Guía rápida del CRM** | Cómo registrar actividades, mover oportunidades de etapa, campos obligatorios y buenas prácticas de registro. Objetivo: operar el CRM de forma autónoma antes del jueves. |
| **Jueves** | **Perfil de Cliente Ideal y Buyer Personas** | A quién vendemos, cuáles son sus dolores principales, quién decide la compra y las objeciones más habituales. Objetivo: identificar rápidamente si un lead encaja con nosotros. |
| **Viernes** | **Casos de Éxito y Objeciones Frecuentes** | Recopilación de cierres reales, cómo se resolvieron las objeciones típicas y qué argumentos funcionan mejor por segmento. Objetivo: llegar a la semana 2 con material conversacional concreto. |

*Recomendación: lectura de 60-90 min por mañana, con tiempo después para preguntas con el buddy.*

---

## 5. Mensaje de Slack del manager (día 1)

> Hola [Nombre] 👋 ¡Bienvenido/a oficialmente al equipo! Enhorabuena por tu primer día 🎉
>
> Algunas cosas para hoy:
>
> • Tu buddy será **@[Nombre del buddy]**: cualquier duda técnica o logística, es tu persona de referencia.
> • A las **[hora]** tenemos nuestro 1:1 de bienvenida (sala [X] / [link de videollamada]).
> • Te he compartido el plan de lecturas de la semana: ve a tu ritmo, sin prisa.
> • Canales recomendados: **#equipo-ventas**, **#general**, **#logros**.
>
> No esperes tenerlo todo claro el primer día: aquí todos hemos sido "el nuevo/a" alguna vez, así que pregunta todo lo que necesites. Mi bandeja de entrada (y mi puerta) están siempre abiertas.
>
> ¡Vamos a por ello! 💪
>
> — [Nombre del manager]

---

**Antes de enviar el paquete**, sustituye los marcadores: [Nombre], [Empresa], [Nombre del buddy], [hora], [X], [Nombre del manager] y ajusta los términos del glosario a la jerga real de tu equipo. Los 5 sub-objetivos están completos y en el orden solicitado. ✅

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

Todos los sub-objetivos están completos en mi respuesta anterior. Aquí tienes la verificación uno a uno:

| # | Sub-objetivo | Estado | Verificación |
|---|---|---|---|
| 1 | Carta de bienvenida personalizada | ✅ Completo | ~150 palabras, tono cálido, con espacios para personalizar ([Nombre], [Empresa]) |
| 2 | 10 primeros pasos del día 1 | ✅ Completo | 10 pasos numerados, con horarios estimados de 9:00 a 16:30 |
| 3 | Glosario de 8 términos internos | ✅ Completo | Exactamente 8 términos definidos (MQL, SQL, Pipeline, Cuota, ICP, ACV, Forecast, Ramp-up) |
| 4 | Plan de lecturas de la primera semana | ✅ Completo | 5 documentos (Lunes a Viernes), cada uno con descripción y objetivo de aprendizaje |
| 5 | Mensaje de Slack del manager | ✅ Completo | Listo para copiar/pegar, con buddy, 1:1, canales y tono cercano |

**Nada falta.** Los 5 sub-objetivos están desarrollados en el orden solicitado (1 → 5), separados con encabezados, y el paquete termina con la nota de marcadores a sustituir antes de enviarlo.

Si al revisarlo sientes que alguno se quedó corto o quieres ajustarlo (por ejemplo: más formal la carta, pasos sin horarios, glosario con jerga específica de tu empresa, o el mensaje de Slack en otro tono), dime cuál y lo reescribo. Si no, el paquete está listo para usarse tal cual, solo rellenando los [corchetes].


## Respuesta completa

Todos los sub-objetivos están completos en mi respuesta anterior. Aquí tienes la verificación uno a uno:

| # | Sub-objetivo | Estado | Verificación |
|---|---|---|---|
| 1 | Carta de bienvenida personalizada | ✅ Completo | ~150 palabras, tono cálido, con espacios para personalizar ([Nombre], [Empresa]) |
| 2 | 10 primeros pasos del día 1 | ✅ Completo | 10 pasos numerados, con horarios estimados de 9:00 a 16:30 |
| 3 | Glosario de 8 términos internos | ✅ Completo | Exactamente 8 términos definidos (MQL, SQL, Pipeline, Cuota, ICP, ACV, Forecast, Ramp-up) |
| 4 | Plan de lecturas de la primera semana | ✅ Completo | 5 documentos (Lunes a Viernes), cada uno con descripción y objetivo de aprendizaje |
| 5 | Mensaje de Slack del manager | ✅ Completo | Listo para copiar/pegar, con buddy, 1:1, canales y tono cercano |

**Nada falta.** Los 5 sub-objetivos están desarrollados en el orden solicitado (1 → 5), separados con encabezados, y el paquete termina con la nota de marcadores a sustituir antes de enviarlo.

Si al revisarlo sientes que alguno se quedó corto o quieres ajustarlo (por ejemplo: más formal la carta, pasos sin horarios, glosario con jerga específica de tu empresa, o el mensaje de Slack en otro tono), dime cuál y lo reescribo. Si no, el paquete está listo para usarse tal cual, solo rellenando los [corchetes].