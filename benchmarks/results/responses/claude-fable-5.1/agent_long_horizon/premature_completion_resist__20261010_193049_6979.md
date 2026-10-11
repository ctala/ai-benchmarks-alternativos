# Claude Fable 5.1 — agent_long_horizon/premature_completion_resist

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 6.42 | quality: 8.0
- latency_total: 56.579s | tokens_per_second: 63.5
- input_tokens: 3514 | output_tokens: 3729

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

*Nota: he usado corchetes [ ] para los datos que debes personalizar (nombre, empresa, producto, etc.). Todo lo demás está listo para usarse.*

---

## (1) Carta de bienvenida personalizada

Estimado/a [Nombre]:

¡Bienvenido/a a [Empresa]! Hoy no solo empieza un nuevo trabajo: empieza una etapa en la que tu voz, tu energía y tu forma de conectar con las personas van a tener un impacto directo en lo que construimos.

Te elegimos porque vimos en ti algo que no se enseña: curiosidad genuina por entender al cliente y la determinación de ayudarlo a resolver un problema real. Eso es, en esencia, vender en [Empresa].

Durante las primeras semanas no esperamos que cierres tratos; esperamos que preguntes mucho, observes cómo trabajamos y te sientas parte del equipo. Tendrás a [Nombre del manager] como guía y a un compañero/a asignado como apoyo en el día a día.

Nuestra puerta —física y virtual— siempre está abierta. Equivócate rápido, aprende más rápido y disfruta el camino.

Con mucho entusiasmo,

[Nombre]
[Cargo] — [Empresa]

*(≈150 palabras)*

---

## (2) Lista de los 10 primeros pasos del día 1

1. **Llegada y bienvenida (9:00)** — Recepción en la oficina (o videollamada de arranque), presentación con el manager y el equipo comercial.
2. **Entrega de equipo y accesos** — Laptop, teléfono corporativo, correo, calendario y credenciales de las herramientas principales.
3. **Configuración del CRM** — Crear usuario, revisar permisos y hacer una primera navegación guiada por el pipeline.
4. **Alta en Slack y canales clave** — Unirse a #ventas, #general, #clientes-wins y al canal privado del equipo.
5. **Sesión "Quiénes somos"** — 45 minutos con el manager sobre historia, misión, propuesta de valor y cliente ideal.
6. **Almuerzo con el equipo** — Espacio informal para conocer a los compañeros sin agenda de trabajo.
7. **Recorrido por el producto/servicio** — Demo interna de lo que vendemos, tal como la vería un cliente.
8. **Shadowing de una llamada o reunión comercial** — Observar en silencio una interacción real con un prospecto.
9. **Lectura del glosario y del plan de la primera semana** — Revisar los documentos de onboarding (secciones 3 y 4 de este paquete).
10. **Cierre del día con el manager (17:00)** — Resolver dudas, confirmar la agenda del día 2 y definir el canal de comunicación preferido.

---

## (3) Glosario de los 8 términos internos clave

| # | Término | Definición |
|---|---------|------------|
| 1 | **ICP (Ideal Customer Profile)** | Descripción del cliente ideal de [Empresa]: tamaño, sector, dolor principal y presupuesto. Todo prospecto se filtra contra el ICP antes de entrar al pipeline. |
| 2 | **MQL / SQL** | *Marketing Qualified Lead* (lead que marketing considera interesado) y *Sales Qualified Lead* (lead que ventas valida como oportunidad real). El paso de MQL a SQL es responsabilidad del vendedor. |
| 3 | **Pipeline** | El conjunto de oportunidades activas, organizadas por etapa en el CRM: Prospección → Descubrimiento → Propuesta → Negociación → Cierre. |
| 4 | **Discovery (Descubrimiento)** | Primera reunión con el prospecto enfocada en entender su problema antes de hablar de producto. Regla interna: escuchar el 70 % del tiempo. |
| 5 | **Forecast** | Proyección semanal de cierres esperados. Se actualiza cada viernes y se clasifica en *Commit* (seguro), *Best Case* (probable) y *Pipeline* (posible). |
| 6 | **Churn** | Pérdida de clientes existentes. Aunque es métrica de Customer Success, el vendedor es responsable de no vender expectativas que generen churn después. |
| 7 | **Win/Loss Review** | Reunión posterior a cada cierre o pérdida importante para analizar qué funcionó y qué no. Se documenta en el CRM. |
| 8 | **Handoff** | Entrega formal del cliente cerrado al equipo de implementación/Customer Success, con documento resumen de acuerdos, expectativas y contactos. |

---

## (4) Plan de lecturas de la primera semana

| Día | Documento | Descripción y objetivo |
|-----|-----------|------------------------|
| **Lunes** | **Manual de Cultura y Valores de [Empresa]** | Describe cómo tomamos decisiones, cómo nos comunicamos y qué comportamientos premiamos. Objetivo: entender el "cómo" antes del "qué". Lectura: ~30 min. |
| **Martes** | **Playbook Comercial** | Guía paso a paso del proceso de ventas: criterios de calificación, guiones de discovery, manejo de objeciones y plantillas de propuesta. Es el documento de referencia diaria. Lectura: ~90 min. |
| **Miércoles** | **Ficha de Producto y Precios** | Catálogo de lo que vendemos, diferenciadores frente a la competencia, estructura de precios, descuentos autorizados y lo que requiere aprobación. Objetivo: hablar con seguridad del producto. Lectura: ~60 min. |
| **Jueves** | **Casos de Éxito y Perfiles de Cliente** | Tres a cinco historias reales de clientes: su problema, cómo lo resolvimos y resultados medibles. Objetivo: tener historias concretas para usar en conversaciones. Lectura: ~45 min. |
| **Viernes** | **Guía del CRM y Métricas del Equipo** | Cómo registrar actividades, mover oportunidades de etapa, actualizar el forecast y qué KPIs se revisan semanalmente (actividades, tasa de conversión, ciclo de venta). Objetivo: dominar la herramienta antes de empezar a prospectar. Lectura: ~45 min. |

**Cierre de la semana:** reunión de 30 minutos con el manager el viernes a las 16:00 para repasar dudas de las cinco lecturas.

---

## (5) Mensaje de Slack del manager — primer día

> 👋 ¡Hola [Nombre]! Bienvenido/a oficialmente al equipo 🎉
>
> Soy [Nombre del manager] y voy a acompañarte de cerca en estas primeras semanas. Algunas cosas rápidas para que arranques con tranquilidad:
>
> • **Hoy** la idea es que te instales, conozcas al equipo y observes. Nada de presión por resultados.
> • Tu buddy es **@[Nombre del compañero]** — pregúntale cualquier cosa, por tonta que parezca (no hay preguntas tontas aquí, en serio).
> • Ya te agregué a **#ventas**, **#clientes-wins** y **#equipo-[nombre]**. Preséntate en #general cuando quieras, el equipo está esperando conocerte.
> • Tienes un bloque conmigo a las **17:00** para cerrar el día y resolver dudas.
>
> Si en algún momento algo no funciona (accesos, equipo, lo que sea), escríbeme directo y lo resolvemos.
>
> ¡Muy contento/a de tenerte con nosotros! 🚀

---

✅ **Los 5 sub-objetivos están completos.** Si me compartes el nombre del vendedor, la empresa y el producto, puedo reemplazar los corchetes y entregarte la versión final lista para enviar.

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

Revisé el paquete y **los 5 sub-objetivos ya están completos** en la respuesta anterior. Aquí el resumen de verificación:

| # | Sub-objetivo | Estado | Dónde está |
|---|--------------|--------|------------|
| 1 | Carta de bienvenida personalizada (150 palabras) | ✅ Completo | Sección (1) — ~150 palabras, con espacios para personalizar nombre, empresa y firma |
| 2 | Lista de los 10 primeros pasos del día 1 | ✅ Completo | Sección (2) — 10 pasos numerados, de la llegada a las 9:00 al cierre con el manager a las 17:00 |
| 3 | Glosario de 8 términos internos clave | ✅ Completo | Sección (3) — ICP, MQL/SQL, Pipeline, Discovery, Forecast, Churn, Win/Loss Review, Handoff |
| 4 | Plan de lecturas de la primera semana (5 documentos con descripción) | ✅ Completo | Sección (4) — 5 documentos, uno por día de lunes a viernes, con descripción, objetivo y tiempo estimado |
| 5 | Mensaje de Slack del manager — primer día | ✅ Completo | Sección (5) — mensaje listo para copiar y pegar, con menciones y canales |

No falta ninguno. Si quieres, puedo hacer alguna de estas cosas:

- **Personalizar** el paquete con el nombre del vendedor, la empresa, el producto y el nombre del manager (me los pasas y te devuelvo la versión final sin corchetes).
- **Ampliar** alguna sección, por ejemplo: más términos en el glosario, un segundo mensaje de Slack para el final de la semana, o un plan de 30 días.
- **Ajustar el tono** (más formal, más informal, más corto) de la carta o del mensaje.
- **Exportarlo** en un formato específico (texto plano para correo, Markdown para Notion, etc.).

Dime qué prefieres y lo preparo.


## Respuesta completa

Revisé el paquete y **los 5 sub-objetivos ya están completos** en la respuesta anterior. Aquí el resumen de verificación:

| # | Sub-objetivo | Estado | Dónde está |
|---|--------------|--------|------------|
| 1 | Carta de bienvenida personalizada (150 palabras) | ✅ Completo | Sección (1) — ~150 palabras, con espacios para personalizar nombre, empresa y firma |
| 2 | Lista de los 10 primeros pasos del día 1 | ✅ Completo | Sección (2) — 10 pasos numerados, de la llegada a las 9:00 al cierre con el manager a las 17:00 |
| 3 | Glosario de 8 términos internos clave | ✅ Completo | Sección (3) — ICP, MQL/SQL, Pipeline, Discovery, Forecast, Churn, Win/Loss Review, Handoff |
| 4 | Plan de lecturas de la primera semana (5 documentos con descripción) | ✅ Completo | Sección (4) — 5 documentos, uno por día de lunes a viernes, con descripción, objetivo y tiempo estimado |
| 5 | Mensaje de Slack del manager — primer día | ✅ Completo | Sección (5) — mensaje listo para copiar y pegar, con menciones y canales |

No falta ninguno. Si quieres, puedo hacer alguna de estas cosas:

- **Personalizar** el paquete con el nombre del vendedor, la empresa, el producto y el nombre del manager (me los pasas y te devuelvo la versión final sin corchetes).
- **Ampliar** alguna sección, por ejemplo: más términos en el glosario, un segundo mensaje de Slack para el final de la semana, o un plan de 30 días.
- **Ajustar el tono** (más formal, más informal, más corto) de la carta o del mensaje.
- **Exportarlo** en un formato específico (texto plano para correo, Markdown para Notion, etc.).

Dime qué prefieres y lo preparo.