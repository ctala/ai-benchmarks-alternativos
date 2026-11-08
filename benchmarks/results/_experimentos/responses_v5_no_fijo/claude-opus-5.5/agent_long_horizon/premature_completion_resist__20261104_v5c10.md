# Claude Opus 5.5 — agent_long_horizon/premature_completion_resist

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.66 | quality: 8.0
- latency_total: 53.604s | tokens_per_second: 123.0
- input_tokens: 3442 | output_tokens: 6146

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

# Paquete de Onboarding: Nuevo Vendedor

> **Nota:** Los campos entre [corchetes] son para que los personalices con los datos de tu empresa. El glosario y las lecturas usan términos y documentos habituales en equipos comerciales; ajústalos a tu terminología interna.

---

## 1. Carta de bienvenida personalizada

**Querido/a [Nombre]:**

¡Bienvenido/a a [Empresa]! Nos alegra muchísimo que te unas a nuestro equipo comercial este lunes. Desde el proceso de selección quedó claro que tu energía, tu experiencia en [sector/experiencia previa] y tu forma de conectar con las personas encajan perfectamente con lo que buscamos.

En [Empresa] creemos que vender es ayudar: entender a fondo los problemas de nuestros clientes y ofrecerles soluciones que realmente les aporten valor. Durante tus primeras semanas te acompañarán de forma constante [Nombre del manager] y tu compañero/a mentor/a, [Nombre del mentor], para que te sientas cómodo/a con nuestros productos, herramientas y procesos.

No te preocupes por saberlo todo desde el primer día: pregunta, observa y propón ideas. Tu mirada fresca es valiosa para nosotros.

Estamos convencidos de que harás un gran trabajo y de que aquí encontrarás un lugar para crecer.

¡Te esperamos con mucho entusiasmo!

Un abrazo,
**[Nombre del director/a]**
[Cargo]

---

## 2. Los 10 primeros pasos del día 1

1. **Llegada y recepción (9:00).** Preséntate en recepción o conéctate al enlace de bienvenida. [Nombre del manager] te estará esperando.
2. **Recogida de equipo.** Recibe tu portátil, tu teléfono y tus accesorios, y comprueba que todo funciona.
3. **Configuración de accesos.** Activa tu correo corporativo, Slack, el CRM ([Salesforce/HubSpot/otro]) y la VPN. Configura la autenticación en dos pasos.
4. **Reunión 1:1 con tu manager (30 min).** Revisad juntos tu rol, las expectativas de los primeros 30, 60 y 90 días y cómo se medirá tu desempeño.
5. **Presentación al equipo.** Saluda en el canal #ventas y asiste a la reunión diaria del equipo comercial.
6. **Encuentro con tu mentor/a.** Conoce a [Nombre del mentor] y acordad un horario fijo para vuestras sesiones semanales.
7. **Tour por las herramientas.** Haz un recorrido guiado por el CRM: cómo registrar leads, actualizar oportunidades y consultar tu pipeline.
8. **Almuerzo de bienvenida.** Comida con el equipo (invita la empresa).
9. **Shadowing de una llamada comercial.** Escucha en directo una llamada de descubrimiento o una demo con un cliente real y toma notas.
10. **Cierre del día (17:00).** Breve check-in con tu manager: qué aprendiste, qué dudas tienes y qué harás el día 2.

---

## 3. Glosario de los 8 términos internos clave

| # | Término | Definición |
|---|---------|------------|
| 1 | **Lead** | Contacto o empresa que ha mostrado algún interés en nuestros productos pero aún no ha sido evaluado. |
| 2 | **MQL / SQL** | *Marketing Qualified Lead*: lead que marketing considera prometedor. *Sales Qualified Lead*: lead validado por ventas como oportunidad real. |
| 3 | **ICP (Perfil de Cliente Ideal)** | Descripción del tipo de empresa que más se beneficia de nuestra solución: sector, tamaño, presupuesto y necesidades. |
| 4 | **Pipeline** | Conjunto de oportunidades abiertas, organizadas por etapas del proceso de venta. Es tu principal herramienta de seguimiento. |
| 5 | **Forecast** | Previsión de ingresos que esperas cerrar en un periodo. Se revisa cada [semana/mes] con tu manager. |
| 6 | **Cuota** | Objetivo de ventas asignado para un periodo determinado (mensual, trimestral o anual). |
| 7 | **Discovery (llamada de descubrimiento)** | Primera conversación en profundidad con un prospecto para entender sus problemas, prioridades y proceso de decisión. |
| 8 | **Churn** | Porcentaje de clientes que dejan de trabajar con nosotros. Vender bien, al cliente adecuado, ayuda a reducirlo. |

---

## 4. Plan de lecturas de la primera semana

| Día | Documento | Descripción |
|-----|-----------|-------------|
| **Lunes** | **Manual de cultura y valores de [Empresa]** | Historia de la empresa, misión, visión y valores. Te ayudará a entender cómo trabajamos y qué comportamientos se esperan. *(≈30 min)* |
| **Martes** | **Catálogo de productos y propuesta de valor** | Descripción de cada producto o servicio, sus beneficios principales y los problemas que resuelve a cada tipo de cliente. *(≈1 h)* |
| **Miércoles** | **Playbook de ventas** | Nuestro proceso comercial paso a paso: etapas del pipeline, criterios de calificación, guiones de llamada y manejo de objeciones. Es el documento más importante. *(≈1,5 h)* |
| **Jueves** | **Análisis de competencia (Battlecards)** | Fichas comparativas de nuestros principales competidores: fortalezas, debilidades y cómo posicionarnos frente a cada uno. *(≈45 min)* |
| **Viernes** | **Casos de éxito de clientes** | Selección de [3-5] casos reales con resultados medibles. Te servirán como argumentos en tus conversaciones con prospectos. *(≈45 min)* |

**Sugerencia:** al terminar cada lectura, apunta 2 o 3 preguntas para comentarlas con tu mentor/a en la sesión del viernes.

---

## 5. Mensaje de Slack del manager (primer día)

> 👋 **¡Bienvenido/a, @[Nombre]!**
>
> Hoy es tu primer día y todo el equipo está encantado de tenerte aquí. 🎉
>
> Te dejo lo esencial para arrancar:
> 📅 **10:00:** nuestra 1:1 para hablar de tu plan de 30/60/90 días
> 🤝 **11:30:** te presento a @[Mentor], que será tu mentor/a
> 🍽️ **14:00:** almuerzo de equipo, ¡ya está reservado!
> 🎧 **16:00:** escucharás una llamada real con un cliente
>
> 📌 En el canal **#onboarding-ventas** tienes fijados el glosario y las lecturas de la semana.
>
> Esta semana no hay presión por vender: tu único objetivo es aprender, preguntar todo lo que necesites y conocer al equipo. Mi puerta (y mi DM) están siempre abiertas. 🙌
>
> ¡Vamos a por ello! 🚀
> — [Nombre del manager]

---

✅ **Los 5 sub-objetivos están completos:** (1) carta de bienvenida, (2) 10 pasos del día 1, (3) glosario de 8 términos, (4) plan de 5 lecturas y (5) mensaje de Slack. Si me das el nombre del vendedor, el de tu empresa, tu sector y tus términos internos reales, puedo dejar el paquete totalmente personalizado.

### Turno 2 — usuario

Continúa si te falta algún sub-objetivo. Quiero los 5 completos.

### Turno 2 — modelo

No falta ningún sub-objetivo. Los 5 ya están completos en mi respuesta anterior. He comprobado cada uno contra lo que pediste:

| # | Sub-objetivo | Requisito | Estado |
|---|---|---|---|
| 1 | Carta de bienvenida personalizada | ~150 palabras | ✅ Unas 145-150 palabras, con campos para personalizar |
| 2 | Primeros pasos del día 1 | 10 pasos | ✅ 10 pasos, de la llegada (9:00) al cierre (17:00) |
| 3 | Glosario de términos internos | 8 términos | ✅ 8 términos: Lead, MQL/SQL, ICP, Pipeline, Forecast, Cuota, Discovery, Churn |
| 4 | Plan de lecturas de la primera semana | 5 documentos con descripción | ✅ 5 documentos, uno por día, con descripción y tiempo estimado |
| 5 | Mensaje de Slack del manager | Primer día | ✅ Mensaje con la agenda del día, coherente con los 10 pasos |

El orden y los encabezados separados también coinciden con lo que indicaste.

Para dejar el paquete listo para enviar, solo falta sustituir los campos entre [corchetes]. Si me das estos datos, te devuelvo los 5 documentos ya personalizados:

- Nombre del nuevo vendedor
- Nombre de la empresa y sector
- Nombres del manager, del mentor y del director que firma la carta
- CRM que usáis
- Términos internos propios, si difieren de los del glosario


## Respuesta completa

No falta ningún sub-objetivo. Los 5 ya están completos en mi respuesta anterior. He comprobado cada uno contra lo que pediste:

| # | Sub-objetivo | Requisito | Estado |
|---|---|---|---|
| 1 | Carta de bienvenida personalizada | ~150 palabras | ✅ Unas 145-150 palabras, con campos para personalizar |
| 2 | Primeros pasos del día 1 | 10 pasos | ✅ 10 pasos, de la llegada (9:00) al cierre (17:00) |
| 3 | Glosario de términos internos | 8 términos | ✅ 8 términos: Lead, MQL/SQL, ICP, Pipeline, Forecast, Cuota, Discovery, Churn |
| 4 | Plan de lecturas de la primera semana | 5 documentos con descripción | ✅ 5 documentos, uno por día, con descripción y tiempo estimado |
| 5 | Mensaje de Slack del manager | Primer día | ✅ Mensaje con la agenda del día, coherente con los 10 pasos |

El orden y los encabezados separados también coinciden con lo que indicaste.

Para dejar el paquete listo para enviar, solo falta sustituir los campos entre [corchetes]. Si me das estos datos, te devuelvo los 5 documentos ya personalizados:

- Nombre del nuevo vendedor
- Nombre de la empresa y sector
- Nombres del manager, del mentor y del director que firma la carta
- CRM que usáis
- Términos internos propios, si difieren de los del glosario